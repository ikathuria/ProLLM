# [Project Name]

> [One-sentence description of what this does and who it's for]

---

## Viability Summary

| | |
|---|---|
| **Build it?** | [yes / yes-with-changes / weekend-prototype-first / no] |
| **Market** | [crowded-no-angle / crowded-with-gap / niche / open] — [1 sentence] |
| **Demand** | [strong / moderate / weak / absent] — [strongest single piece of evidence] |
| **Direction** | [tailwind / neutral / headwind / hype-peak-passed] |
| **Feasibility** | [easy / medium / hard] — [the spike] |
| **Free to build** | [yes / mostly / no] — [unavoidable costs] |
| **Monetization** | [path or "portfolio project"] |

**In two sentences:** [the honest bottom line]

---

## Research Findings

> Full evidence (competitor table, verbatim user quotes, demand signals, cost audit, sources): see [`RESEARCH.md`](RESEARCH.md). Only the plan-shaping conclusions are repeated here.

- **Positioning / wedge:** [the gap this plan builds toward, or why there's no angle]
- **The spike:** [hardest technical problem] — **approach:** [chosen library/API/technique]
- **Cost flags:** [anything with no free path, or "none — fully free to build"]
- **Monetization:** [chosen path and why, or "portfolio project — not applicable"]
- **Open questions a prototype should answer:** [from RESEARCH.md's Conflicts & unknowns]

*(If RESEARCH.md doesn't exist — research ran inline via the fallback guide — put the competitor table here instead: Name | Pricing | Strength | Limitations | User complaints.)*

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

**Deliberately skipped:** [layers not used and why, e.g. "no auth — single-user tool"]

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

### Milestone 0: Spike *(only if Feasibility = hard)*
**Goal:** The hardest technical piece is proven in isolation, before any scaffolding.

Tasks:
- [ ] [Minimal prototype of the spike] — Done when: [measurable result, e.g. works on N real examples at ≤ $X per call]

---

### Milestone 1: Scaffold
**Goal:** Repo runs locally, folder structure in place, CI green, context tracker created.

Tasks:
- [ ] Initialize `apps/web` with [framework] at its current stable version (verify via official docs) — Done when: `npm --prefix apps/web run dev` starts without errors
- [ ] Set up folder structure per Project Structure section — Done when: `apps/`, `docs/`, root delegating `package.json` exist
- [ ] Add lint, typecheck, and test tooling with one passing placeholder test — Done when: `npm run lint`, `npm run typecheck`, `npm test` all pass
- [ ] Add GitHub Actions CI workflow (install, lint, typecheck, test on push/PR) — Done when: the workflow passes on the first push
- [ ] Create `PROJECT.md` from the tracker outline — Done when: it describes purpose, stack+versions, structure, conventions, status
- [ ] Add root `CLAUDE.md` pointing to `PROJECT.md` — Done when: committed
- [ ] Configure environment variables — Done when: `.env.example` committed
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 2: Core Feature
**Goal:** The primary thing this app does works end-to-end, even without auth or polish.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] E2E test of the core happy path — Done when: it passes locally and in CI
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 3: Data Layer
**Goal:** All data persists correctly, schema is stable. *(Merge into Core Feature for small apps; swap order with Milestone 2 if the core can't run on mock data.)*

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 4: UI/UX
**Goal:** A real user could navigate and use the app without confusion.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 5: Auth *(if applicable)*
**Goal:** Users can sign up, log in, and access protected routes.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 6: Monetization *(if applicable)*
**Goal:** Payment flow works in test mode.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 7: Deploy
**Goal:** App is live at a public URL.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

---

### Milestone 8: Polish
**Goal:** No obvious errors, loading states present, edge cases handled.

Tasks:
- [ ] [Task] — Done when: [condition]
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally

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