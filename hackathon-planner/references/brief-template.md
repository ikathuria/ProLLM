# HACKATHON_PLAN.md Template

Fill every section. Delete guidance in *italics*. Keep it skimmable; it is read by the user, by coding agents, and (in the Milestones section) executed task by task.

---

```markdown
# [Project name] — [Hackathon name]

**Pitch:** [Named user] can [do X] in [time] instead of [pain, with number] because [mechanism].
**The moment:** [the one retellable beat, visible in ≤15s]
**The measured claim:** [what number we'll show] — measured by [method]
**Planned:** [date] · **Deadline:** [date/time + timezone] · **Submit by:** [deadline − margin]

## 1. Hackathon Facts
| Field | Value | Source |
|---|---|---|
| Build window / deadline | | URL |
| Team size | | |
| Required tech | | |
| New-work / AI-assistance rules | | |
| Submission package (video cap, repo, URL, writeup, other) | | |
| Prizes & categories we're targeting | | |
| Judges & method (human / AI-assisted / vote) | | |
*Mark anything unverified as UNVERIFIED.*

## 2. Judging Model
| Criterion (exact wording) | Weight | Build-effort share | Evidence that will score it |
|---|---|---|---|
*AI-assisted judging? [yes/no/unknown] → if yes/unknown, README claim→code table and spoken claims are mandatory.*

## 3. Winner Patterns for This Event
*3–6 bullets from past winners of this series (name, prize, why it fit the rubric, quote+URL where available), then: what this implies for us. If no history: say so.*

## 4. Idea Selection
### Candidates & scoring matrix
| Idea | [criterion 1 ×w] | [criterion 2 ×w] | … | Insider | Moment | Evidence | Buildable | Prizes | Risk | Total |
### Chosen idea — why (3 sentences tied to criteria)
### Runner-up (fallback if M0 fails)
### Novelty check — nearest comparables and our difference
### Scope cut list (explicitly OUT)
### Kill test (riskiest assumption → tested in M0)

## 5. Evidence Plan
| Claim we'll make | Proof artifact | Where it lives | Built in |
|---|---|---|---|
*Includes: eval/measured claim, deployed URL, README claim→code table, AI-use disclosure, sponsor-tech justification, responsible-AI notes.*

## 6. Tech Stack
*Sponsor tech first, then the fastest path to a live public URL. Pin current versions (web-search them). One line reason each. Note free tiers/credits and expected cost per demo run.*

## 7. Timeline (wall-clock, agent-era)
| Fixed point | Target date/time | % of window |
|---|---|---|
| Idea + spec locked, M0 done | | ~15% |
| Skeleton deployed | | ~30% |
| Core flow real on live URL | | ~55% |
| **FEATURE FREEZE** | | ~75–80% |
| Rough-cut video + README draft | | ~85% |
| Final QA / pre-submit audit | | ~92% |
| **Submit** (≥3–4h early) | | |

*Human availability windows: [when the user can review/record]. Human gates (H): [keys, accounts, decisions, recording].*

## 8. Milestones
*Format from `references/agent-timeline.md`; each task: Done when + Type (S/H/W).*

### Milestone 0: Kill-test spike
**Goal:** …
- [ ] … — Done when: … — Type: S — Est: …

### Milestone 1: Skeleton live
…
### Milestone 2: Core flow
…
### Milestone 3: Evidence
…
### Milestone 4: Moment & polish
…
### ⛔ FEATURE FREEZE
### Milestone 5: Submission assets
…
### Milestone 6: Demo video
*Script (from judging-playbook.md §4) pasted here with beats and the claims to speak aloud.*
### Milestone 7: QA & submit
- [ ] Pre-submit audit (checklist in `references/judging-playbook.md` §5)
- [ ] Submit ≥3–4h before deadline — Done when: confirmation page/email received

## 9. Risks & Contingencies
| Risk | Likelihood | Mitigation / fallback |
|---|---|---|

## 10. Notes & Decisions
*Append-only. Include user decisions at gates (e.g. chose idea B over A because…).*

## Agent Rules (also copy into CLAUDE.md)
- Before using any library/SDK/API, fetch its latest official docs; never code from memory.
- Never modify tests to make them pass. Run lint + typecheck + tests before marking a task done.
- After FEATURE FREEZE: bug fixes, polish, evidence and submission assets only.
- Never delete seeded demo data. Never commit secrets.
- Keep PROJECT.md current. Commit at every milestone; small commits throughout.
- Do not put instructions aimed at judges or AI reviewers in the repo, README, or video. Be clear and truthful only.
```

---

## Companion files

- `PROJECT.md` and a one-line root `CLAUDE.md` (`See PROJECT.md for project context.`): use `project-planner/references/project-template.md` if that skill is installed; otherwise a short what/stack/structure/status/decision-log file suffices.
- `SUBMISSION.md` (optional): drafts of the Devpost/portal fields (tagline, What it does, How we built it, Challenges, Accomplishments, What's next, Built with, Try it) so submission-day is copy-paste.
