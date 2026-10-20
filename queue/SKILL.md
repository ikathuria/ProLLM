---
name: queue
description: >
  Keeps a per-repo QUEUE.md of small, well-specified tasks that Claude can run unattended while the
  user is away (class, gym, overnight), then schedules, runs and reviews them. Modes: add (turn a
  request into a queue item with an acceptance check, or refuse it as needing the user), run (do the
  next ready item on a branch, test, push, draft PR, report), schedule (create cloud routines for the
  user's away windows), review (summarise finished auto PRs and merge on approval). Trigger on "queue
  this", "add to the queue", "work on this while I'm away / overnight / at the gym", "run the queue",
  "schedule the queue", "what did the overnight runs do", "review the auto PRs".
---

# Queue Skill

Unattended runs are cheap only when each item is small and checkable. A vague item burns a whole
run and produces a PR the user can't judge. So the work is mostly in **add**: an item goes in only
when a fresh agent with no conversation could finish it and prove it.

Cloud runs start from a fresh clone and do **not** see `~/.claude` (global CLAUDE.md, user skills,
user MCP servers). Everything a run needs must be in the repo: the protocol lives at the top of
`QUEUE.md`, and the repo's own `CLAUDE.md` applies.

## Mode: add

1. Read the repo's `CLAUDE.md`, `HANDOFF.md` (if present) and `QUEUE.md` (create it from
   `${CLAUDE_SKILL_DIR}/references/QUEUE-template.md` if missing; it contains the run protocol).
2. Turn each request into an item using the template's fields. Required:
   - **Goal**: one sentence, the outcome, not the steps.
   - **Files**: where to start (paths, not "the backend").
   - **Done when**: a command or check that passes only if the goal is met (a test, a build, a script
     output, a grep). If none exists, the item's first step is writing one.
   - **Out of scope**: what not to touch.
   - **Where**: `cloud` (CPU, minutes) or `local` (GPU, datasets, long jobs; runs via `long-run`).
   - **Size**: S (< 1 h of agent work) or M (1–3 h). Split anything bigger.
3. Refuse or mark `needs-me` instead of queueing when the item needs a design decision, a research
   judgment (choosing a method, interpreting a result, writing claims), credentials, paid services,
   or anything advisor-facing. Say why in one line.
4. Order by value; mark the top 1–3 `ready`. (Runs skip items that already have an auto branch;
   after its PR is merged or closed, set the item to `done (#PR)` or back to `ready` on the default
   branch.) Show the user the added items in one block; don't
   rewrite existing ones unasked. Commit `QUEUE.md` so cloud runs see it.

## Mode: run

Follow the protocol in the repo's `QUEUE.md` exactly (it is the same for interactive and cloud runs).
When run interactively, still follow it: one item, its branch, its check, its report.

## Mode: schedule

1. Confirm the account matches the repo (`GitHub/Research/` → claude-papa, else claude-beti); routines
   draw from the creating account's usage.
2. Away windows come from the user's weekly schedule in the hub `PROFILE.md` (gym, class, meetings,
   overnight). Prefer windows when the user isn't also using the same account interactively.
   Pick minutes off the hour (e.g. `:07`); runs on the hour start late.
3. Use the `schedule` skill to create one routine per repo, with this prompt (fill in the repo):

   ```
   In this repo, follow the "Run protocol" at the top of QUEUE.md: take the first item marked
   `ready` with Where: cloud, do it on a branch named claude/auto-<yyyy-mm-dd>-<item-slug>, push,
   open a draft PR, and update QUEUE.md. If no item is ready, stop without changes.
   ```
4. Only `cloud` items run on routines. `local` items are started by the user (or `long-run`) on
   the GPU machine.
5. Prerequisites to check once and tell the user: the GitHub connection on claude.ai (Claude GitHub
   App or `/web-setup`); on the Team account an Owner may need to enable it. If the connection
   lapses, runs are skipped and the routine turns off after 72 hours.

## Mode: review

1. `gh pr list --draft --json number,title,headRefName,url,createdAt --jq '.[] | select(.headRefName | startswith("claude/auto-"))'`
   in the repo; read each PR's report (PR body) and `QUEUE.md` changes, not the full diff first.
2. For each: one line (item, result, check passed?, assumptions made). Flag any PR whose check
   didn't pass or whose diff touches files outside the item's scope.
3. Merge, request changes, or close only on the user's word. After merging, mark the item `done`
   with the PR number.

## Rules

- One item per run. Never batch items into one branch.
- Never push to or merge into the default branch, force-push, delete branches, or edit CI,
  secrets, `.env`, licensing or advisor-facing documents in an unattended run.
- A run that can't finish is still useful if it leaves a clear report: what was tried, where it
  stopped, what decision is needed.
