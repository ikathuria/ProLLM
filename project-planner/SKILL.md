---
name: project-planner
description: >
  Turns a raw idea into an actionable, Claude Code-ready plan: a PLAN.md plus a living
  PROJECT.md tracker for autonomous execution. Trigger whenever the user describes a new app,
  tool, service, SaaS idea or side project, even without asking for a plan: "I have an idea",
  "I want to build X", "help me plan this", "what stack should I use". Always use it for
  new-project ideation. Research-only asks ("is this feasible", "can this make money") go to
  idea-research; hackathon entries go to hackathon-planner. Do NOT trigger for features, fixes
  or refactors inside an existing codebase. EXECUTE mode: when PLAN.md/PROJECT.md exist and the
  user says "continue the project", "do the next milestone", "finish what's left" or "finish
  everything without me", run bounded milestone batches instead of open-ended work.
---

# Project Planner Skill

Turns a raw idea into a complete, actionable plan. Outputs a `PLAN.md` (build plan) and a `PROJECT.md` (living context tracker) committed to the project's GitHub repo, structured for autonomous Claude Code execution.

**How to use the reference files:** each phase below has core rules inline and, where noted, a detailed guide in `${CLAUDE_SKILL_DIR}/references/`. Read the referenced file when you reach that phase — don't load them all up front.

**Composing with other skills:** if a skill is installed that matches a technology or task in the plan (e.g. a `supabase` skill when Supabase is the chosen database), invoke it for that part instead of working from general knowledge. If no matching skill exists, the guidance in `${CLAUDE_SKILL_DIR}/references/` is self-sufficient. For the visual layer of any project with a UI, the plan hands off to `brand-studio` when it's installed (see Phase 4).

## Execute mode: bounded milestone runs

Use when `PLAN.md`/`PROJECT.md` exist and the user wants the project built rather than planned.
Open-ended asks ("finish everything without my intervention") tend to drift, rewrite the same
files repeatedly, and end with the user asking what's left. Run in bounded batches instead:

1. **Read state.** `PROJECT.md` (status, decisions), `PLAN.md` (milestones), `HANDOFF.md` if present,
   `git log --oneline -10`. Find the first incomplete milestone.
2. **Propose a batch.** List the next 1–3 milestones with their tasks and "Done when" checks,
   anything that needs the user (keys, accounts, decisions, payments), and a rough size in agent
   sessions. **Wait for the user's OK.** If they said "without my intervention", still show the
   batch, then proceed unless they object; batch size stays capped at 3.
3. **Build one milestone at a time.** Fetch current docs before using any library. After each
   milestone: run its "Done when" checks and the test suite, update `PROJECT.md`, commit with
   the milestone name. If a check fails twice, stop and report rather than looping.
4. **Stop at the batch end.** Report what's done (with commits), what's verified, what needs
   the user, and the next batch. If the session is long, offer `handoff` before continuing.

Never mark a task done without its check passing. Never expand scope beyond PLAN.md without
asking; note new ideas in PROJECT.md's backlog instead.

## Phase 1: Idea Intake

**Hackathon check first.** If the project is for a hackathon or similar judged competition, stop and use the `hackathon-planner` skill instead (it plans around the event's judging criteria and an agent-session timeline, and skips SaaS scaffolding like auth and monetization). If a `HACKATHON_PLAN.md` already exists and the user now wants to grow the project into a real product, read it and `RESEARCH.md` as inputs and continue below rather than re-asking what they already answered.

Ask the user these questions (only the ones not already answered in the conversation):

1. What does it do, in one sentence?
2. Who is it for? (target user)
3. What problem does it solve, and is this for personal use, a small audience, or potentially many people?
4. Any tech preferences or constraints? (languages, platforms, "must be free to host", etc.)
5. Is monetization a goal, or is this a portfolio/personal project?

Do NOT proceed to Phase 2 until you have enough to answer these. It's OK to infer from context — don't ask redundant questions.

---

## Phase 2: Research

**If `RESEARCH.md` already exists** for this idea (repo root or current directory), read it instead of re-researching — unless it's stale (older than ~3 months) or the idea has materially changed; then ask whether to refresh it.

**If the `idea-research` skill is installed, invoke it now and skip the rest of this phase.** It runs deep mode by default — four or five parallel research subagents — falling back to quick mode only if the user explicitly asked for a fast pass. Pass it the answers from Phase 1 so it doesn't re-ask. It writes `RESEARCH.md` and hands back its verdict block without announcing it in chat — you own the single user-facing summary (Phase 6).

**Fallback (idea-research not installed): read `${CLAUDE_SKILL_DIR}/references/research-guide.md`** — a condensed playbook covering market (competitors, demand, positioning), feasibility (the spike, cost audit, easy/medium/hard), monetization, and kill criteria.

Non-negotiables either way:
- Append the **current year** to trend searches (check today's date; never hardcode a past year).
- Apply the **kill criteria** honestly — "don't build this, here's why" is a valid outcome of this skill.

### Gate: stop before planning a "no"

If the verdict is **no** or **weekend-prototype-first**, do NOT continue to Phase 3. Show the user the verdict (Phase 6 format, stack/milestone lines omitted) and ask how to proceed:
- **Stop here** — the research is the deliverable.
- **Prototype plan** — a stripped-down plan: Milestone 0 (the spike / the riskiest assumption) plus the smallest scaffold to test it; skip Auth, Monetization, and Polish.
- **Full plan anyway** — proceed, recording the verdict and the user's decision in PLAN.md's Risks and Notes & Decisions.

For **yes** / **yes-with-changes**, continue; for yes-with-changes, bake the changes into the plan's scope.

---

## Phase 3: Tech Stack Selection

**Read `${CLAUDE_SKILL_DIR}/references/stack-guide.md` now** — it has the full decision trees: frontend, backend, database, ORM, auth, hosting, file storage, email, background jobs, testing, CI/CD, analytics, error monitoring, payments, and AI/LLM.

Non-negotiables:
- **Choose the most free, self-hostable, open-source stack possible.** Paid services only with explicit user acceptance.
- **No server-side logic → GitHub Pages.** Always.
- **Pin current versions.** Web-search the latest stable version of every chosen framework before finalizing — never plan against a remembered version.
- **Delegate layers to installed skills** when one matches the chosen technology (per "Composing with other skills" above).
- Record each layer's choice + version + one-line reason in PLAN.md, and list layers deliberately skipped.

---

## Phase 3.5: Project Structure

Bake a consistent structure into every plan so any LLM (or human) can navigate the repo cold. The default layout (`apps/web/src/{app,features,lib}`, `packages/`, `docs/`, root `PROJECT.md` + `PLAN.md`) is the Project Structure section of `${CLAUDE_SKILL_DIR}/references/plan-template.md` — adapt that tree to the chosen stack.

Rules:
- **Use `apps/<name>` even for a single app.** It costs nothing now and leaves a clean home for a second surface (mobile, admin, marketing site) later.
- **Root `package.json` delegates, it does not hoist.** Scripts call the primary app via `npm --prefix apps/web run <script>` (`dev`, `build`, `lint`, `test`). Do **not** adopt npm/pnpm workspaces until a real second package exists — workspaces hoist `node_modules` and migrate the lockfile, which is churn with no payoff for one app.
- **`packages/` only once a second consumer exists.**
- **`docs/` filenames are zero-padded kebab-case, no spaces or special chars** (`01-...`, `02-...`). Spaces and `&`/`()` fight the CLI and tooling.
- **No throwaway scaffolding committed** (no `test.txt`, no stray placeholders).
- **Scale down for tiny projects:** a purely static single-page site can flatten (skip `apps/`), but keep `docs/` + `PROJECT.md`.

---

## Phase 4: Build Plan

**Read `${CLAUDE_SKILL_DIR}/references/milestones-guide.md` now** — it has task-sizing rules, "Done when" patterns per task type, per-task testing requirements, the standard milestone skeleton, and worked example breakdowns for common app types (CRUD SaaS, static site, AI app, CLI tool).

Non-negotiables:
- Every task is **self-contained** (one Claude Code session, no questions), **testable** (checkable "Done when", not a judgment call), and **sequenced** (depends only on tasks before it).
- Logic tasks include their own unit tests; every milestone ends with a lint + typecheck + test gate.
- Projects classified **Hard** in Phase 2 start with **Milestone 0: Spike** — prove the hardest piece before scaffolding anything.
- **Projects with a UI get a brand & UI task** right after scaffolding and before any feature screens are built. If `brand-studio` is installed, the task is: *"Run the `brand-studio` skill: propose 3–5 directions, get the user's pick, write `BRAND.md` + tokens, confirm with the user."* Done when `BRAND.md` and the token files exist and the user has approved them. Mark it as a **human gate**, since it needs the user's choice and approval. Every later UI task then says "build per `BRAND.md`". Add a closing task in the final milestone: re-run `brand-studio` Phase 6 (rubric + accessibility/SEO audits) across the finished screens. If `brand-studio` isn't installed, note it as optional and keep a plain design-tokens task instead.

---

## Phase 5: Output Files

Generate **two** files.

### 5a. `PLAN.md`
The build plan — use the template in `${CLAUDE_SKILL_DIR}/references/plan-template.md`. It includes Viability Summary (the full verdict table), Research Findings (plan-shaping conclusions only — link to `RESEARCH.md` for the evidence rather than copying it), Risks, Tech Stack (with pinned versions), Project Structure, Environment Variables, Milestones, and the Claude Code commands.

### 5b. `PROJECT.md` — the living project tracker
A single source-of-truth context map so **any LLM or human can understand the whole project cold**, without reading every file. Use the template in `${CLAUDE_SKILL_DIR}/references/project-template.md`. Milestone 1 creates the first version; every later session keeps it current. It must contain:

- **What it is** — one paragraph: what the app does and who it's for.
- **Stack** — chosen technologies *with pinned current versions*.
- **Architecture** — request/data flow in a few bullets or a small diagram.
- **Project structure** — annotated tree (what lives where), kept in sync with reality.
- **Key conventions** — naming, where new code goes, testing approach.
- **Current status** — which milestones/features are done, what's in progress.
- **Decision log** — append-only list of direction-changing decisions with the why.
- **Glossary / domain terms** — anything project-specific an outsider wouldn't know.

> For Claude Code specifically, add a one-line root `CLAUDE.md` that says `See PROJECT.md for project context.` so it's auto-loaded each session.

### Always fetch current docs before coding
Both files must state this standing rule, and you should follow it during planning: **before writing code against any framework/library, fetch its latest official docs** (web search, `WebFetch` on the official docs site, or a docs MCP like Context7 if available). Model training data lags real releases — verify current APIs, don't code from memory.

### Then tell the user:
- The GitHub repo name to create (kebab-case, descriptive)
- Where to save the files (`/PLAN.md` and `/PROJECT.md` in repo root)
- The Claude Code command to start the first session:
  ```
  claude "Read PLAN.md and PROJECT.md. Complete Milestone 1, fetching the latest official docs for any library before using it. Update PROJECT.md to reflect what you built. Mark tasks done as you go. Stop after Milestone 1 and commit."
  ```
- The command to resume from any future session:
  ```
  claude "Read PLAN.md and PROJECT.md. Find the first incomplete task and continue, fetching the latest official docs for any library before using it. Keep PROJECT.md in sync. Mark tasks done as you go. Commit when a milestone is complete."
  ```

---

## Phase 6: Final Summary

This is the **only** verdict the user sees in chat for the whole run (idea-research, when invoked from here, doesn't post its own). Keep it short and point to the files for detail:

```
**Idea:** [name]
**Build it?** [yes / yes-with-changes / weekend-prototype-first / no] — [1–2 sentences why]
**Market:** [positioning] — [1 sentence on competition]
**Demand:** [strength] — [single strongest piece of evidence]
**Feasibility:** [easy/medium/hard] — [the spike]
**Free to build:** [yes/mostly/no] — [any unavoidable costs]
**Monetization:** [path if applicable, or "portfolio project"]
**Recommended stack:** [list]
**Milestones:** [N] — first up: [Milestone 0 or 1 name]
Full evidence in RESEARCH.md; build plan in PLAN.md.
```

Be honest. If the kill criteria fired, say "don't build this (or build it only to learn), because [reason]" — that is a successful run of this skill, not a failure.
