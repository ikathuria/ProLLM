# Build Plan Guide (Phase 4)

How to break a project into milestones and tasks that Claude Code can execute autonomously, one session at a time.

---

## Task sizing rules

A well-sized task:
- **Fits one session** — completable without human input, roughly ≤ 2 hours of focused work
- **Touches a bounded surface** — ideally ≤ ~5 files; if a task description needs "and" twice, split it
- **Has zero open questions** — every decision the task needs is already in PLAN.md or PROJECT.md. If writing the task surfaces a decision, make the decision in the plan, not in the task
- **Is sequenced** — depends only on tasks listed before it. No forward references, no "in parallel"
- **Names its files** when non-obvious — "Create `apps/web/src/features/billing/checkout.ts`" beats "add checkout logic"

## "Done when" patterns

Every task ends with `— Done when: [condition]`. The condition must be checkable by running something, not by judgment. Good patterns:

| Task type | Done-when pattern |
|---|---|
| Scaffold/config | `npm --prefix apps/web run dev` starts clean; `npm run lint` passes |
| Feature logic | named unit tests pass (`vitest run src/features/x`) |
| API endpoint | a specific `curl`/fetch returns the expected shape and status |
| UI | the flow works in the browser: list the exact click path and expected result |
| Schema/migration | migration applies on a fresh DB; CRUD round-trip test passes |
| Deploy | public URL serves the app; health endpoint returns 200 |

Bad: "Done when: auth works", "Done when: code is clean". If you can't phrase a checkable condition, the task is too vague — split or respecify it.

## Testing requirements per task

- Every **logic** task includes writing its unit tests in the same task (colocated `*.test.ts`)
- Every **milestone** ends with an implicit gate: lint + typecheck + full test suite green before marking the milestone done
- The **core feature milestone** ends with one E2E test of the happy path
- UI polish tasks don't need automated tests but must list the manual click path

## Standard milestone skeleton

1. **Scaffold** — repo setup, dependencies, folder structure (per Phase 3.5), env vars, CI workflow, initial `PROJECT.md` + root `CLAUDE.md`
2. **Core feature** — the single thing that makes the app worth existing, end-to-end, ugly is fine
3. **Data layer** — schema, migrations, CRUD (merge into Core feature for small apps)
4. **UI/UX** — real navigation, responsive if needed, empty/loading states
5. **Auth** *(if needed)* — sign up, login, protected routes
6. **Monetization** *(if applicable)* — Stripe in test mode, gating
7. **Deploy** — live URL, env config, Sentry, smoke test
8. **Polish** — error handling, edge cases, perf passes

Adjust freely: order Core feature before Data layer only when the core can run on mock data; if it can't, swap them. If research flagged the project **Hard**, insert **Milestone 0: Spike** — prove the hardest technical piece in isolation before any scaffold work.

## Example breakdowns by app type

### CRUD SaaS (e.g. invoice tracker)
- M1 Scaffold → M2 Data layer (schema: `users`, `invoices`, `clients`; migrations; CRUD with tests) → M3 Core feature (create/send/track invoice flow) → M4 UI → M5 Auth → M6 Stripe → M7 Deploy → M8 Polish

### Static content/marketing site
- M1 Scaffold (Astro, GitHub Pages workflow) → M2 Content structure + layouts → M3 Pages + styling → M4 Deploy (often just merging the workflow) → M5 Polish (SEO meta, lighthouse pass). No auth/data milestones — say so explicitly.

### AI chat/assistant app
- M0 Spike (prompt + model choice proven against real examples, cost measured per interaction) → M1 Scaffold → M2 Core chat loop with streaming → M3 Data layer (conversation persistence) → M4 UI → M5 Auth + usage caps (caps before launch, not after) → M7 Deploy → M8 Polish

### CLI/dev tool
- M1 Scaffold (package bin entry, arg parsing) → M2 Core command end-to-end → M3 Secondary commands → M4 DX polish (help text, errors, colors) → M5 Publish (npm/PyPI + release workflow). No UI/auth/deploy milestones.

## Milestone format (as written in PLAN.md)

```
## Milestone N: [Name]
**Goal:** [What demonstrably works when this is done]

Tasks:
- [ ] [Specific task, files named if non-obvious] — Done when: [checkable condition]
- [ ] …
- [ ] Gate: lint, typecheck, and full test suite pass — Done when: all green locally
```
