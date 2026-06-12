# [Project Name]

> [One-sentence description of what this does and who it's for]

---

## Viability Summary

| | |
|---|---|
| **Market** | [crowded/niche/gap] — [1 sentence] |
| **Feasibility** | [easy/medium/hard] — [key challenge] |
| **Free to build** | [yes/mostly/no] — [any costs] |
| **Monetization** | [path or "portfolio project"] |

---

## Research Findings

### Competitors
| Name | Pricing | Strength | Limitations | User complaints |
|---|---|---|---|---|
| | | | | |

**Positioning:** [crowded-no-angle / crowded-with-gap / niche / open] — [the gap or wedge, if any]

### Feasibility
- **Hardest part:** [the spike] — **approach:** [chosen library/API/technique]
- **Cost flags:** [anything with no free path, or "none — fully free to build"]

### Monetization
[Chosen path and why it's the simplest fit, or "portfolio project — not applicable"]

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [e.g. free tier of X removed] | low/med/high | low/med/high | [fallback] |
| [e.g. spike harder than expected] | | | [Milestone 0 proves it before scaffold] |

---

## Tech Stack

> Versions verified against current official docs on [date]. Re-check before coding.

| Layer | Choice | Version | Reason |
|---|---|---|---|
| Frontend | | | |
| Backend | | | |
| Database | | | |
| Auth | | | |
| Hosting | | | |
| Payments | | | (if applicable) |

---

## Project Structure

```
repo-root/
├─ apps/
│  └─ web/                 # primary app — own package.json
│     └─ src/
│        ├─ app/           # routes / entry points
│        ├─ features/      # feature-sliced (types.ts, validation.ts, *.test.ts colocated)
│        └─ lib/           # cross-cutting infra
├─ packages/               # shared code — only once a 2nd consumer exists
├─ docs/                   # 01-..., 02-... (zero-padded kebab-case)
├─ PROJECT.md              # living context tracker
├─ PLAN.md                 # this file
├─ package.json            # root: delegating scripts (npm --prefix apps/web run …)
├─ .env.example
└─ README.md
```

**Conventions**
- `apps/<name>` layout even for a single app; root `package.json` delegates, no workspaces until a 2nd package exists.
- `docs/` filenames: zero-padded kebab-case, no spaces/special chars.
- **Before coding against any library, fetch its latest official docs** (web search / WebFetch / docs MCP). Never code framework APIs from memory.
- Keep `PROJECT.md` in sync whenever structure, stack, or status changes.

---

## Environment Variables

List all env vars needed before starting:

```
# Required
VARIABLE_NAME=        # what it is, where to get it

# Optional
VARIABLE_NAME=        # what it is
```

---

## Milestones

### Milestone 1: Scaffold
**Goal:** Repo runs locally, folder structure in place, all dependencies installed, context tracker created.

Tasks:
- [ ] Initialize `apps/web` with [framework] at its current stable version (verify via official docs) — Done when: `npm --prefix apps/web run dev` starts without errors
- [ ] Set up folder structure per Project Structure section — Done when: `apps/`, `docs/`, root delegating `package.json` exist
- [ ] Create `PROJECT.md` from the tracker outline — Done when: it describes purpose, stack+versions, structure, conventions, status
- [ ] Add root `CLAUDE.md` pointing to `PROJECT.md` — Done when: committed
- [ ] Configure environment variables — Done when: `.env.example` committed

---

### Milestone 2: Core Feature
**Goal:** The primary thing this app does works end-to-end, even without auth or polish.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] [Task] — Done when: [condition]

---

### Milestone 3: UI/UX
**Goal:** A real user could navigate and use the app without confusion.

Tasks:
- [ ] [Task] — Done when: [condition]

---

### Milestone 4: Auth *(if applicable)*
**Goal:** Users can sign up, log in, and access protected routes.

Tasks:
- [ ] [Task] — Done when: [condition]

---

### Milestone 5: Data Layer
**Goal:** All data persists correctly, schema is stable.

Tasks:
- [ ] [Task] — Done when: [condition]

---

### Milestone 6: Monetization *(if applicable)*
**Goal:** Payment flow works in test mode.

Tasks:
- [ ] [Task] — Done when: [condition]

---

### Milestone 7: Deploy
**Goal:** App is live at a public URL.

Tasks:
- [ ] [Task] — Done when: [condition]

---

### Milestone 8: Polish
**Goal:** No obvious errors, loading states present, edge cases handled.

Tasks:
- [ ] [Task] — Done when: [condition]

---

## Claude Code Commands

> In every session, fetch the latest official docs for any library before coding against it, and keep `PROJECT.md` in sync with what you build.

**Start fresh (Milestone 1):**
```
claude "Read PLAN.md and PROJECT.md. Complete Milestone 1, fetching the latest official docs for any library before using it. Update PROJECT.md to reflect what you built. Mark tasks done as you go. Stop after Milestone 1 and commit."
```

**Resume from any point:**
```
claude "Read PLAN.md and PROJECT.md. Find the first incomplete task and continue, fetching the latest official docs for any library before using it. Keep PROJECT.md in sync. Mark tasks done as you go. Commit when a milestone is complete."
```

**Test the current state:**
```
claude "Read PLAN.md and PROJECT.md. Without building anything new, test everything that's marked done. Report what works and what's broken."
```

---

## Notes & Decisions

*Record any decisions made during planning or development here.*

-