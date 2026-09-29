# Agent-Era Timeline (Phase 5)

The user builds with Claude Code / Codex / similar agents. Typing speed is not the constraint, so **do not size milestones in human working hours**. Size them in **agent sessions**, and schedule around the things that *are* scarce: human decisions, human review, external waits, and the deadline.

---

## What the bottleneck actually is (evidence)

- **Spec and scoping.** Anthropic Opus 4.7 winners: two days of spec "felt slow… but were what let the rest of the week move fast." Humans owned design decisions; the agent owned infrastructure.
- **Demo video and writeup.** Winners called the video unexpectedly time-consuming. Treat it as a first-class build item.
- **Verification under time pressure.** A small interview study of 28-hour events found verification was limited by time; agents produce plausible-looking wrong output.
- **Scope creep.** Launching agent tasks is so cheap that solo builders keep adding features. Cut list + feature freeze are the counter.
- **Integration & external constraints:** API keys, rate limits, deployment, auth callbacks. (Named as risks in general workflow guides; not verified as top hackathon bottlenecks — plan a buffer anyway.)
- Reported speed claims (e.g. "8-hour build", "65% faster with a harness") come from promotional sources and are UNVERIFIED. Don't promise them.

## Units

- **Agent session (S):** one focused Claude Code / Codex run on a bounded task, ~15–60 min wall-clock including human review. Milestone tasks in this skill are sized to one S (same rule as `project-planner`: ≤~5 files, checkable "Done when", zero open questions).
- **Human gate (H):** a step only the user can do: a decision, account/API-key setup, recording narration, reviewing output, submitting. Schedule these explicitly; they gate everything else.
- **Wait (W):** deploy, DNS, model rate limits, slow evals, sponsor approvals.

Every milestone lists its S tasks, H gates and expected W.

## Back-plan from the deadline (wall-clock)

1. Get the **submission deadline in the user's timezone** and subtract a **safety margin**: submit ≥3–4 hours early (≥1 day early if the window is a week). Late submission is an instant discard.
2. Get the **actual hours the user can supervise** (sleep, job, class). Agents run while they're away only for well-specified, test-gated tasks; anything needing review waits for them. Ask; don't assume.
3. Allocate the remaining wall-clock by the proportions below, then place the fixed points: **feature freeze**, **rough-cut video**, **final QA**, **submit**.

### Time allocation (synthesis of sourced evidence, not a measured figure)

| Phase | Share | Notes |
|---|---|---|
| Idea lock + spec (brief, PLAN, CLAUDE.md, contracts) | 15–20% | Spec quality is the leverage point |
| Scaffold + **deployed skeleton** (URL live with hello-world) | 5–10% | Deploy on day 0, not day N |
| Core build (the one flow, end-to-end) | 30–35% | Ugly is fine; must run |
| Integration + debug | 10–15% | External APIs, rate limits, model quirks |
| Polish (UX, seeded data, empty/error states, the "moment") | ~10% | |
| Demo video + writeup + README | 10–15% | Start the rough cut earlier |
| Buffer | ~10% | Something *will* break |

**Fixed points (as % of the total window):**
- **~15%** idea and spec locked; Milestone 0 spike done (kill test passed or pivot to runner-up).
- **~30%** deployed skeleton live; first end-to-end (even faked) path works.
- **~55%** core flow works for real on the live URL.
- **~75–80%** **FEATURE FREEZE.** No new features after this. Only bugs, polish, evidence, video.
- **~85%** rough-cut video recorded; README/writeup drafted.
- **~92%** final QA on fresh incognito window; pre-submit audit (`judging-playbook.md` §5).
- **Submit ≥3–4h before deadline** (or ≥1 day for week-long events), then only fix if something is provably broken.

Short events (≤48h): compress spec to ≤2h but never skip it. Long events (weeks): add mid-point check-ins and a real-user test session; the extra time should buy *evidence and polish*, not extra features.

## Session-level workflow (what to put in PLAN.md and CLAUDE.md)

- **Spec first.** `PLAN.md` (milestones), `PROJECT.md`/`CLAUDE.md` (context ≤ ~200 lines), shared **contracts** (types, API schemas) before parallel work.
- **Fetch current docs before coding** against any SDK/API; agents hallucinate APIs and use stale versions. Sponsor SDKs move fast; this rule is not optional.
- **Guardrails in CLAUDE.md:** never modify tests to make them pass; run the full suite before declaring done; no new features after freeze; no deleting seeded demo data.
- **Parallelism:** 3–5 parallel agents in git worktrees is a documented pattern; assign disjoint file ownership; shared files (schema, config, routes) are the main conflict vector; merge in dependency order; watch shared DBs/MCP servers and pre-commit hooks across worktrees. Only parallelize after the contracts exist. If the user is solo and new to it, one agent + one reviewer pass is safer.
- **Demo-safe branch:** tag a known-good commit after the first end-to-end success; the video and live URL run from it. (Practical advice; no hackathon source, but cheap insurance.)
- **Test gates:** each S ends with lint + typecheck + tests green; the core milestone ends with one E2E test of the demo path; the demo path gets a scripted smoke test you can re-run before submitting.
- **Commit early, often, spread across the event** (thin/late commit history is a red flag for judges and AI reviewers).
- **Token/rate-limit budget:** estimate sponsor API cost per demo run and per eval; get credits/keys on day 0.
- **Rehearse the demo journey** several times on the live build; seed the data.

## Milestone skeleton for hackathons

Replace `project-planner`'s SaaS skeleton with this one:

| M | Name | Goal | Typical size |
|---|---|---|---|
| 0 | **Kill-test spike** | Prove the riskiest assumption (API works, model can do the task, data obtainable) in isolation. Fail → switch to runner-up idea | 1–2 S + H (keys) |
| 1 | **Skeleton live** | Repo, CLAUDE.md/PROJECT.md, CI, hello-world **deployed to a public URL**, seeded demo data path | 1–2 S |
| 2 | **Core flow** | The one end-to-end flow works for real (may be ugly). E2E test of the demo path | 3–6 S |
| 3 | **Evidence** | The measured claim: eval script + results table + sample outputs saved in repo | 1–2 S + W |
| 4 | **Moment & polish** | The retellable beat; UX states; seeded data; sponsor-feature depth; responsible-AI notes | 2–4 S |
| — | **FEATURE FREEZE** | | |
| 5 | **Submission assets** | README (claim→code table, disclosure), architecture diagram, writeup, thumbnail/gallery images | 1–2 S + H |
| 6 | **Demo video** | Script → record → cut; captions optional | H-heavy |
| 7 | **QA & submit** | Fresh-browser check, pre-submit audit, submit early | H |

Skip auth, monetization, admin panels, and multi-user features unless a criterion or the demo path needs them.

## Task format

```
- [ ] [Task, files named] — Done when: [checkable] — Type: S | Est: ~30m | Needs: [H gates]
```
