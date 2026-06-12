# [Project Name] — Project Tracker

> Living context map. Any LLM or human should be able to read this file alone and understand
> what the project is, how it's built, and where things are. **Keep it in sync** — update it
> whenever the stack, structure, conventions, or status changes.

_Last updated: [date]_

---

## What it is

[One short paragraph: what the app does and who it's for.]

---

## Stack

| Layer | Choice | Version | Notes |
|---|---|---|---|
| Frontend | | | |
| Backend | | | |
| Database | | | |
| Auth | | | |
| Hosting | | | |

> Versions verified against official docs on [date]. Re-verify before coding against a library.

---

## Architecture

[Request/data flow in a few bullets or a small diagram.]

1. …
2. …

---

## Project structure

```
repo-root/
├─ apps/web/        # [what it is]
│  └─ src/
│     ├─ app/       # [routes / entry points]
│     ├─ features/  # [feature-sliced modules]
│     └─ lib/       # [cross-cutting infra]
├─ docs/            # [numbered kebab-case docs]
├─ PROJECT.md       # this file
└─ PLAN.md          # build plan
```

[Annotate anything non-obvious. Update the tree as the repo grows.]

---

## Conventions

- **Where new code goes:** [e.g. new feature → `apps/web/src/features/<name>/`]
- **Naming:** [files, components, branches]
- **Testing:** [framework, where tests live, how to run]
- **Docs:** `docs/` filenames are zero-padded kebab-case, no spaces.
- **Before coding any library:** fetch its latest official docs — never code APIs from memory.

---

## Current status

| Milestone | Status | Notes |
|---|---|---|
| 1. Scaffold | ☐ todo / ◐ in progress / ✅ done | |
| 2. Core feature | | |
| … | | |

**In progress now:** [what's being worked on]
**Next up:** [next task]

---

## Decision log

Append-only. One line per decision that changed direction, with the why — this is what keeps future sessions from re-litigating settled questions.

- [date] — [decision] — [reason]

---

## Glossary

- **[Term]** — [domain-specific meaning an outsider wouldn't know]
