#!/usr/bin/env python3
"""Mine Claude Code session transcripts into a compact, evidence-bearing digest.

Reads ~/.claude/projects/*/<session>.jsonl (plus subagent transcripts) and writes a JSON
digest with per-session friction signals and per-skill aggregates. Stdlib only.

Usage:
  mine_sessions.py [--days 14] [--project SUBSTR] [--skill NAME] [--exclude-skill self-improve]
                   [--out digest.json] [--root ~/.claude/projects]
"""
import argparse, collections, glob, json, os, re, sys
from datetime import datetime, timedelta, timezone

CORRECTION = re.compile(
    r"^\s*(no\b|nope|don'?t|do not|stop|wrong|that'?s not|not what|actually|instead|"
    r"why did you|you (didn'?t|forgot|missed|ignored)|still\b|again\b|revert|undo|"
    r"i said|i asked|i (did not|didn'?t) like)", re.I)
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
PASTED = re.compile(r"<pasted_content[^>]*>.*?</pasted_content[^>]*>", re.S)
CMD = re.compile(r"<command-name>/?([^<]+)</command-name>")


def ts(s):
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def text_of(content):
    if isinstance(content, str):
        return content
    out = []
    for b in content or []:
        if isinstance(b, dict) and b.get("type") == "text":
            out.append(b.get("text", ""))
    return "\n".join(out)


def clean(s, n=400):
    s = PASTED.sub("[pasted]", REMINDER.sub("", s)).strip()
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[:n] + "…"


def result_text(b):
    c = b.get("content")
    if isinstance(c, list):
        c = " ".join(x.get("text", "") for x in c if isinstance(x, dict))
    return clean(str(c or ""), 240)


def parse(path, since, is_sub=False):
    s = dict(file=path, title=None, cwd=None, start=None, end=None, cost=None, models={},
             prompts=[], skills=[], tools=collections.Counter(), errors=[], interrupts=0,
             rejects=[], api_errors=0, compactions=0, edits=collections.Counter(),
             bash_fail=collections.Counter(), subagents=0, corrections=[])
    pending = {}  # tool_use_id -> (name, short input)
    active_skill = None
    for line in open(path, errors="replace"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        t = d.get("type")
        when = ts(d.get("timestamp", "")) if d.get("timestamp") else None
        if when:
            s["start"] = s["start"] or when
            s["end"] = when
        s["cwd"] = s["cwd"] or d.get("cwd")
        if t == "custom-title":
            s["title"] = d.get("customTitle")
        elif t == "cost-state":
            s["cost"] = d.get("totalCostUSD")
            s["models"] = {k: round(v.get("costUSD", 0), 2) for k, v in (d.get("modelUsage") or {}).items()}
        elif t == "system":
            st = d.get("subtype")
            s["api_errors"] += st == "api_error"
            s["compactions"] += st == "compact_boundary"
        pd = d.get("permissionDecision")
        if isinstance(pd, dict) and pd.get("decision") == "reject":
            s["rejects"].append(pd.get("reasonType") or pd.get("source"))
        m = d.get("message")
        if not isinstance(m, dict):
            continue
        content = m.get("content")
        if t == "user" and (d.get("origin") or {}).get("kind") == "human" and not d.get("isMeta"):
            raw = text_of(content)
            cmd = CMD.search(raw)
            if cmd:
                active_skill = cmd.group(1).strip()
                s["skills"].append(dict(skill=active_skill, via="slash", at=len(s["prompts"])))
            p = clean(raw)
            if p:
                s["prompts"].append(dict(i=len(s["prompts"]), skill=active_skill, text=p))
                if CORRECTION.search(p) and len(s["prompts"]) > 1:
                    s["corrections"].append(dict(i=len(s["prompts"]) - 1, skill=active_skill, text=p))
        if not isinstance(content, list):
            continue
        for b in content:
            if not isinstance(b, dict):
                continue
            bt = b.get("type")
            if bt == "tool_use":
                name, inp = b.get("name", "?"), b.get("input") or {}
                s["tools"][name] += 1
                if name == "Skill":
                    active_skill = inp.get("skill")
                    s["skills"].append(dict(skill=active_skill, via="tool", at=len(s["prompts"])))
                elif name in ("Agent", "Task"):
                    s["subagents"] += 1
                elif name in ("Edit", "Write", "MultiEdit"):
                    s["edits"][inp.get("file_path", "?")] += 1
                short = inp.get("command") or inp.get("file_path") or inp.get("skill") or inp.get("url") or ""
                pending[b.get("id")] = (name, clean(str(short), 160))
            elif bt == "tool_result":
                name, short = pending.get(b.get("tool_use_id"), ("?", ""))
                if b.get("is_error"):
                    s["errors"].append(dict(tool=name, input=short, skill=active_skill, msg=result_text(b)))
                    if name == "Bash":
                        s["bash_fail"][short] += 1
            elif bt == "text" and "interrupted by user" in b.get("text", ""):
                s["interrupts"] += 1
    if not s["end"] or s["end"] < since:
        return None
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--project")
    ap.add_argument("--skill")
    ap.add_argument("--exclude-skill", action="append", default=["self-improve"])
    ap.add_argument("--root", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--out", default="-")
    a = ap.parse_args()
    since = datetime.now(timezone.utc) - timedelta(days=a.days)

    sessions = []
    for path in glob.glob(os.path.join(a.root, "*", "*.jsonl")):
        if os.path.getmtime(path) < since.timestamp():
            continue
        s = parse(path, since)
        if not s:
            continue
        if a.project and a.project.lower() not in (s["cwd"] or path).lower():
            continue
        skills = {x["skill"] for x in s["skills"]}
        if skills & set(a.exclude_skill) and len(skills) == 1:
            continue  # this skill's own runs aren't evidence about anything
        if a.skill and a.skill not in skills:
            continue
        subdir = path[:-6] + "/subagents"
        subs = glob.glob(os.path.join(subdir, "*.jsonl"))
        sub_err = 0
        for sp in subs:
            ss = parse(sp, datetime.min.replace(tzinfo=timezone.utc), True)
            if ss:
                sub_err += len(ss["errors"])
        s["subagent_transcripts"], s["subagent_tool_errors"] = len(subs), sub_err
        sessions.append(s)

    per_skill = collections.defaultdict(lambda: dict(sessions=0, cost=0.0, errors=0, corrections=0,
                                                     interrupts_in_session=0, prompts_while_active=0))
    for s in sessions:
        for sk in {x["skill"] for x in s["skills"]}:
            ag = per_skill[sk]
            ag["sessions"] += 1
            ag["cost"] += s["cost"] or 0
            ag["errors"] += sum(e["skill"] == sk for e in s["errors"])
            ag["corrections"] += sum(c["skill"] == sk for c in s["corrections"])
            ag["prompts_while_active"] += sum(p["skill"] == sk for p in s["prompts"])
            ag["interrupts_in_session"] += s["interrupts"]
    for ag in per_skill.values():
        ag["cost"] = round(ag["cost"], 2)

    out_sessions, seen = [], set()
    for s in sorted(sessions, key=lambda s: s["start"]):
        # resumed/forked sessions replay earlier prompts; keep only the first copy
        fresh = []
        for p in s["prompts"]:
            key = p["text"][:200]
            if key not in seen:
                seen.add(key)
                fresh.append(p)
        s["corrections"] = [c for c in s["corrections"] if any(c["i"] == p["i"] for p in fresh)]
        s["prompts"] = fresh
        out_sessions.append(dict(
            id=os.path.basename(s["file"])[:-6], file=s["file"], project=s["cwd"], title=s["title"],
            start=s["start"].isoformat(timespec="minutes"), end=s["end"].isoformat(timespec="minutes"),
            cost_usd=round(s["cost"], 2) if s["cost"] else None, model_cost=s["models"],
            n_prompts=len(s["prompts"]), n_tool_calls=sum(s["tools"].values()),
            tools=dict(s["tools"].most_common(12)), skills=s["skills"],
            subagents=s["subagents"], subagent_tool_errors=s["subagent_tool_errors"],
            interrupts=s["interrupts"], permission_rejects=s["rejects"], api_errors=s["api_errors"],
            compactions=s["compactions"], tool_errors=s["errors"][:25],
            repeated_bash_failures={k: v for k, v in s["bash_fail"].items() if v >= 2},
            edit_churn={k: v for k, v in s["edits"].items() if v >= 5},
            corrections=s["corrections"], prompts=[{"i": p["i"], "skill": p["skill"], "text": p["text"]}
                                                   for p in s["prompts"][:60]]))
        out_sessions[-1] = {k: v for k, v in out_sessions[-1].items() if v not in (None, [], {}, 0)}

    digest = dict(generated=datetime.now(timezone.utc).isoformat(timespec="minutes"),
                  window_days=a.days, filters=dict(project=a.project, skill=a.skill),
                  totals=dict(sessions=len(sessions),
                              cost_usd=round(sum(s["cost"] or 0 for s in sessions), 2),
                              prompts=sum(len(s["prompts"]) for s in sessions),
                              tool_errors=sum(len(s["errors"]) for s in sessions),
                              corrections=sum(len(s["corrections"]) for s in sessions),
                              interrupts=sum(s["interrupts"] for s in sessions)),
                  per_skill=dict(sorted(per_skill.items(), key=lambda kv: -kv[1]["sessions"])),
                  sessions=out_sessions)
    data = json.dumps(digest, separators=(",", ":"), ensure_ascii=False, default=str)
    if a.out == "-":
        print(data)
    else:
        with open(a.out, "w") as f:
            f.write(data)
        t = digest["totals"]
        print(f"{t['sessions']} sessions, ${t['cost_usd']}, {t['prompts']} prompts, "
              f"{t['tool_errors']} tool errors, {t['corrections']} correction-like prompts, "
              f"{t['interrupts']} interrupts -> {a.out}")
        for k, v in list(digest["per_skill"].items())[:15]:
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
