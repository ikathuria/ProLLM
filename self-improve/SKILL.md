---
name: self-improve
description: >
  Evidence-based retro on how the user's Claude Code sessions and skills actually went, which
  then edits the skills to fix what it found. Mines local session transcripts
  (~/.claude/projects) for friction: user corrections, interrupts, tool errors, retry loops,
  edit churn, permission rejects, compactions, cost outliers, and which skills were involved.
  It ties every finding to quoted session evidence, turns findings into concrete diffs to the
  user's own SKILL.md / reference files (and CLAUDE.md or habit suggestions where a skill
  isn't the cause), applies the approved ones, and logs them so the next run can check whether
  they helped. Trigger on "improve my skills", "self-improve", "what's going wrong in my
  sessions", "review my Claude usage", "retro on my skills", "why does skill X keep failing",
  "tune skill X from my usage", or /self-improve. Use INSTEAD of /insights.
---

# Self-Improve Skill

Generic usage reports ("consider using plan mode more") change nothing. This skill only
reports what it can **point to in a transcript**, and only proposes what it can **write as a
diff** or as a concrete thing to do differently. What to avoid:
- **Vague advice with no evidence.**
- **Over-fitting a skill to one bad session.**
- **Narrow coverage**: building the report from the two or three most dramatic chats.
- **Description instead of diagnosis**: "you mostly use Claude for X" or "an error occurred
  that could have been avoided" is not a finding. Each finding must answer *what keeps going
  wrong*, *why*, and *what changes so it stops*.

## Stage 1 — Scope

From the request, settle (defaults in brackets, don't ask unless it's ambiguous):
- **Window** [last 14 days]. **Project filter** [all]. **Skill focus** [all skills the user owns].
- **Editable skills** = skills whose real path (`readlink -f ~/.claude/skills/<name>`) is inside a
  git repo the user owns. Plugin, marketplace, and `external-skills/` skills are **read-only**:
  findings about them become suggestions only, never edits.
- Read `~/.claude/self-improve/LEDGER.md` if it exists: earlier changes and what they were meant
  to fix. This run has to check them (Stage 5).

## Stage 2 — Mine

```sh
python3 ${CLAUDE_SKILL_DIR}/scripts/mine_sessions.py --days 14 --out <scratchpad>/digest.json
```
Add `--project <substr>` or `--skill <name>` to narrow it. The script prints totals plus
per-skill aggregates. The JSON has, per session: prompts (tagged with the active skill),
correction-like prompts, tool errors with input and message, repeated Bash failures, edit churn,
interrupts, permission rejects, API errors, compactions, subagent counts, and cost.

The script's correction regex only catches the obvious ones. **Read the prompts themselves.**
Signs of friction include: the user repeating or restating a request, "still", pasting an
error back, redirecting scope, asking for the same output in a different format, or abandoning
the task. Resumed and forked sessions can repeat prompts, so dedupe on text.

**Token budget.** Raw transcripts are huge, so never `Read` or `cat` one whole. When a candidate
finding needs context, `grep -n` the transcript (`file` in the digest) for the quote or error and
read about 40 lines around it with `sed -n`. Take **at most 3 excerpts per finding** and about 15
in the whole run. If the digest plus excerpts can't establish a finding, drop it rather than
reading more.

**Coverage is required.** Every session in the window gets read: its prompts, plus the
signals the digest flagged. Sessions without friction count too, because they show what works.
Keep a coverage tally (sessions read / total, per project and per skill) and print it in the
report. Patterns come from counting across sessions. A single vivid chat is an example of a
pattern, never the pattern itself. For more than ~25 sessions, or more than 4 skills, fan out: one subagent per skill
(plus one for "no skill / general usage"). Run these with `model: "sonnet"` (or `"haiku"` for
slices under ~10 sessions): their job is sorting and counting signals, not judgment. Give
each one its slice of the digest (`jq` it out, don't paste the whole file), the
`references/signals.md` path, and the same excerpt cap. Have each return **candidate**
findings in the evidence format below, at most 6 and with no diffs. The main model does
Stage 3 onward: it verifies candidates, assigns layers, and writes every edit.

## Stage 3 — Diagnose

Use `${CLAUDE_SKILL_DIR}/references/signals.md` to turn signals into causes. For each candidate
finding, write down:
- **Evidence**: ≥2 occurrences in different sessions (a single one only if it was costly: >$20
  wasted, or the user abandoned the task), each given as `session-id[:8] · date · project` plus a
  short quote of the user's words or the error.
- **Cause**, placed in one of these layers. Get this right: most mis-fixes come from patching
  the wrong layer.
  1. **Skill instruction**: the skill said to do X, or failed to say Y, and that caused it. Quote
     the line in the SKILL.md.
  2. **Skill trigger**: the skill fired when it shouldn't have, or didn't fire when it should
     have (check the `description:` against what the user typed).
  3. **Skill tooling**: a script, command, or path the skill relies on is broken or outdated.
  4. **Project context**: missing or wrong CLAUDE.md or memory for that repo.
  5. **Usage habit**: how the user prompted (missing context, ambiguous ask, wrong model/effort
     for the task). Report it plainly, without lecturing.
  6. **Environment**: an MCP server that is down, missing CLI, or permissions. Not a skill problem.
- **Cost of the friction**: turns, dollars, or time lost (estimate from the digest).
- **Recurrence**: how many sessions out of how many relevant ones (e.g. "5 of 9 brand-studio
  sessions"). Rank by this times cost, not by how dramatic one instance was.
- **Fix**: what changes so it stops. Either a diff (layers 1–4), or for habits a specific
  before/after: the prompt the user actually sent, and the version that would have avoided the
  problem. Never a generic tip.

Drop any finding with no concrete evidence. Also look for **what works**: skills or habits with
low friction that are worth keeping or copying into other skills.

## Stage 4 — Propose

Write `<scratchpad>/self-improve-report.md` using `references/report-format.md`. For every
finding in layers 1–3 on an editable skill, include the **exact diff**. Edit rules:
- Make the smallest change that would have prevented the evidence. Prefer sharpening an
  existing line over adding a new section. A skill that grows every run is a failure.
- Keep each skill's voice and structure. Read the whole SKILL.md and its references first.
- Don't hard-code one project's details into a general skill. If the fix only makes sense for
  one repo, it belongs in that repo's CLAUDE.md.
- Don't add rules that conflict with other skills in the same repo. Check how they hand off.
- Trigger fixes go in the `description:`. Keep it under ~1000 characters.

Show the user a short summary in chat: coverage, the top 3 things going wrong (each with its
recurrence and its fix), plus the report path. Don't open with usage stats or a description
of how they use Claude; those go in one line at the bottom of the report, if at all. Ask which changes to apply (all / pick by number / none). **Do not edit anything
before they answer.**

## Stage 5 — Apply, verify, log

1. Apply the approved diffs. In the skills repo, use the branch the user prefers. If you're on
   `main` and they haven't said, make a `self-improve/<date>` branch. Commit only if they ask.
2. Sanity check: frontmatter still parses, referenced `${CLAUDE_SKILL_DIR}` files exist, and any
   scripts you touched still run (`--help` or a dry run).
3. **Check last run's changes** against the ledger: for each earlier entry, compare the same
   signal before and after its date (errors or corrections per session with that skill). Mark
   each one *helped*, *no change*, *worse*, or *not enough data*. Suggest reverting anything
   marked *worse*.
4. Append to `~/.claude/self-improve/LEDGER.md` (create it if missing): date, skill, file, the
   one-line change, the signal it targets, and that signal's baseline value.

End with one line: what changed, what was suggested but not applied, and when to run again
(after ~10 more sessions with the affected skills).

## Options

- `--dry-run` / "just report": stop after Stage 4.
- `--skill <name>`: deep dive on one skill. Read every session that used it, not just the flagged ones.
- `--usage`: focus on habits and cost (model/effort choice, session length, compactions)
  instead of skill edits.
