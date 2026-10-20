---
name: weekly-plan
description: >
  Plans the user's week across research, job search, YouTube and side projects, and across their
  AI accounts (claude-papa for research, claude-beti for personal, Codex for simple tasks). Reads
  the fixed weekly schedule, Apple Calendar, the task list and each active repo's HANDOFF.md and
  QUEUE.md, then writes WEEK.md with focus blocks per day, what each account and Codex should do,
  queue items for unattended runs in away windows, and auto PRs to review. Trigger on "plan my
  week", "weekly plan", "what should I work on this week", "Sunday planning", "plan around my
  schedule", "how should I split work between accounts", "plan today", "set up the daily
  check-in".
---

# Weekly Plan Skill

A plan is useful only if it fits the real week and turns into queued work. Keep it to one page.

Hub: `~/Library/Mobile Documents/com~apple~CloudDocs/get to know me/` (`PROFILE.md`, `TASKS.md`,
`WEEK.md`). Repos: `~/GitHub/{Research,Personal,Hacks}`.

## Step 1: Gather (cheap, in parallel)

- `PROFILE.md`: Priorities, Weekly schedule, AI accounts sections only.
- Calendar: `bash ${CLAUDE_SKILL_DIR}/scripts/calendar_week.sh 7` (takes ~20 s; the first run
  needs macOS Calendar permission). The fixed schedule in `PROFILE.md` is the base; calendar events
  add to it. If they conflict, the calendar wins for that day; mention it.
- `TASKS.md`: Active and Waiting On. Treat dated items as unconfirmed.
- Last `WEEK.md`, if present: what was planned vs done (ask the user for the 2–3 items you can't tell).
- For each priority repo (from `PROFILE.md` Priorities): first ~40 lines of `HANDOFF.md`, the
  `ready`/`needs-me`/`review` items in `QUEUE.md`, and
  `git log --since='8 days ago' --oneline | wc -l`. Don't read code.
- Auto PRs: `gh pr list --draft --json title,url,headRefName --jq '.[] | select(.headRefName | startswith("claude/auto-"))'` per repo.
- Deadlines: grep the repos' HANDOFF/PROJECT files and `TASKS.md` for dates in the next 3 weeks.

## Step 2: Plan

1. **Free blocks.** From schedule plus calendar, list the user's working blocks per day (lab
   10:00–14:00 Tue–Fri is research time) and **away windows** (gym, class, meetings, overnight).
2. **Allocate by priority** (research → job search → YouTube → Aura/KeepItUp), but put any deadline
   in the next 10 days first. Give side projects one or two fixed small blocks rather than leftovers.
   Each block names one outcome, not a topic ("RealText: run Gaussian-G test", not "RealText").
3. **Assign the doer** for each piece of work:
   - **User + claude-papa**: research judgment, experiments, paper writing (lab hours).
   - **User + claude-beti**: job applications, `project-deepdive` sessions, YouTube scripts, side
     project features that need decisions.
   - **Unattended** (`queue`, `cloud`): small, checkable code tasks in away windows. Research repo
     items run as claude-papa routines; personal repo items as claude-beti routines.
   - **Local GPU** (`long-run`): training/eval jobs, started before a long away window.
   - **Codex**: mechanical work, first drafts, log summaries.
4. **Usage spread.** Don't stack two heavy Opus sessions on the same account back to back; put
   claude-papa's heavy work in lab hours and claude-beti's in evenings and weekends; let routines
   use each account's otherwise idle windows.
5. **Interview prep.** One `project-deepdive` build or quiz block per week (about 45 min) until
   the résumé projects are covered.

## Step 3: Write and confirm

Write `WEEK.md` in the hub from `${CLAUDE_SKILL_DIR}/references/week-template.md` (overwrite; keep
it to one screen). Show the user the plan and the proposed queue items **before** writing to any
`QUEUE.md`. On approval:
- add the items with the `queue` skill (add mode) in each repo, and create or adjust routines with
  `queue` schedule mode;
- update `TASKS.md` with confirmed changes only, preserving unrelated entries (re-read it first).

## Daily mode

Two parts, because cloud routines can't read Apple Calendar or the iCloud hub:

- **Cloud check-in (6:00, every day, per account).** A read-only Haiku routine over the account's
  repos (claude-papa: `GitHub/Research/*`; claude-beti: the personal repos) reports what overnight
  runs did, what needs the user, and each repo's next step. It also starts that account's usage
  window. To set it up or change it, use the `schedule` skill: update the account's existing 6:00
  routine if there is one (list first; don't create a duplicate), with the prompt in
  `${CLAUDE_SKILL_DIR}/references/checkin-prompt.md`, model `claude-haiku-5-5`, tools
  `Bash, Read, Glob, Grep`, the Default environment, and one `sources` entry per repo. Run it once
  with "run now" and read its log to confirm the repos cloned.
- **Local "today" (when the user sits down, on request: "plan today", "what's today").** Read
  today's row of `WEEK.md`, `calendar_week.sh 1`, and the latest check-in result if the user
  pastes it. Reply in ≤ 10 lines: fixed events, the 1–3 outcomes for today with account/tool,
  what to queue before the next away window. Only update `WEEK.md` if the user changes the plan.

## Rules

- Don't invent deadlines, task status or priorities. Mark guesses `[Guessing]` and ask.
- Leave slack: plan at most ~70% of free blocks.
- Weekly meal prep, gym and class are fixed; never schedule over them.
