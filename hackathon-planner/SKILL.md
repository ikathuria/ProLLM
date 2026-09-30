---
name: hackathon-planner
description: >
  Plans a hackathon entry to win, not just to finish: researches the specific hackathon's
  judging criteria, judges (including AI-assisted judging), and past winners, then generates
  and scores project ideas against that rubric, and produces a HACKATHON_PLAN.md with an
  evidence plan (what proves each criterion), demo-video script, and an agent-era timeline
  sized in coding-agent sessions rather than human hours. Built for online hackathons where
  the user builds with Claude Code / Codex / other AI coding tools. Trigger when the user
  mentions a hackathon (Devpost, lablab.ai, MLH, DoraHacks, Kaggle, Cerebral Valley, a
  sponsor's build week), "what should I build for X hackathon", "help me win", hackathon
  ideas, demo video, judging criteria, or submission planning. Use INSTEAD of project-planner
  for hackathons; do not use for ordinary product ideas with no competition or deadline.
---

# Hackathon Planner Skill

Turns "I'm entering hackathon X" into a plan optimized to **score well with that hackathon's actual judges** (human and AI), built by coding agents. Output: `HACKATHON_PLAN.md` (template: `${CLAUDE_SKILL_DIR}/references/brief-template.md`) plus a short summary in chat.

**Principle:** a hackathon is won by *problem choice, demo moment, and legible evidence*, not by feature count. Agents make building cheap, so the differentiators are the parts agents can't supply: real insider knowledge, a real user, taste, honest evidence, and a submission a skimming judge (or LLM) can verify in two minutes.

**How to use the reference files:** read each one when you reach its phase, not up front.

**Composing with other skills:** `idea-research` is used selectively, not as a full run: after the idea is chosen (Phase 3), run only its `feasibility-brief.md` as one subagent (hidden API costs, rate limits, the spike; ~15 searches) and, if the novelty check found close comparables, its `competitor-brief.md`. Run the full `idea-research` only if the user says they want to keep building after the hackathon. If a `RESEARCH.md` already exists for the chosen idea, read it and reuse it (refresh if older than ~3 months) instead of re-researching. For the visual layer invoke `brand-studio` when installed. For `PROJECT.md`/stack details reuse `project-planner`'s `stack-guide.md` and `project-template.md` if installed, but this skill's hackathon rules override its SaaS defaults (no auth/monetization/admin unless a criterion or the demo path needs them; sponsor tech beats "most free"). If a skill matches a chosen technology (e.g. `supabase`), use it. Never treat a `RESEARCH.md`/older plan as current for a different hackathon.

**Honesty rules (non-negotiable):**
- Rules and criteria come from the event's **live** rules page, fetched now. Base rates in these references are context, not the rules.
- Mark unverified facts UNVERIFIED; distinguish "found nothing" from "couldn't load". Cite URLs for hackathon-specific claims.
- **Optimize through clarity and evidence only.** Never put hidden instructions, invisible text, or judge/LLM-directed prompts in the README, repo, video, or metadata; never overstate what works; follow AI-disclosure rules. If the user asks for such tactics, decline and give the legitimate alternative.

---

## Phase 1: Intake

Ask only what's not already known:
1. Which hackathon? (URL preferred.) If none chosen yet, offer to survey open online AI hackathons (Phase 2, Step 0).
2. **Deadline in the user's timezone**, and how many hours they can realistically supervise/review before then. (Agents work while they're away only on well-specified, test-gated tasks.)
3. Solo or team; which coding agents/tools and plan limits (token/rate limits shape parallelism).
4. Their unfair advantages: domain knowledge, a real person with the problem, data/hardware/credits, an audience. (Insider knowledge is the strongest winner pattern.)
5. Any existing code/idea (check the new-work rule), tech to use or avoid, and risk appetite.
6. Goal: grand prize, a specific sponsor prize, or portfolio/learning. (Shapes risk and scope.)

## Phase 2: Hackathon recon

**Read `${CLAUDE_SKILL_DIR}/references/recon-guide.md` now.** Steps: (0) if no event chosen, survey current open online AI hackathons and shortlist by fit/prize/deadline; (1) fetch the rules and extract the Hackathon Facts table; (2) classify the judging model and convert weights into build-effort shares; (3) study past winners of this event/series (5–8 project pages, judge quotes); (4) scan the current field for saturation.

Non-negotiables:
- **Detect whether judging is AI-assisted/automated** (search the rules for "AI", "automated", "LLM"). If yes or unknown, the evidence plan must be text-legible and verifiable (see Phase 4).
- Read **submission requirements** exactly: video cap, repo/URL requirements, disclosure format. A missed field is an instant discard.
- Record what you couldn't access.

## Phase 3: Ideation & selection

**Read `${CLAUDE_SKILL_DIR}/references/winning-patterns.md`, then `${CLAUDE_SKILL_DIR}/references/idea-scoring.md`.**

Generate 6–8 candidates from the user's advantages and the winner patterns, apply the kill filters, run the novelty check, and score each against **this hackathon's own criteria and weights** plus insider edge, demo moment, evidence potential, agent-buildability, prize stacking, and risk. Show the arithmetic.

**Gate:** present the matrix, your recommended pick, and a runner-up, then **ask the user to confirm** before planning. Do not silently pick. If the user already has a firm idea, still run the scoring for it (and one alternative) and say honestly if it scores poorly against the rubric or the field, then respect their choice.

### After the pick: feasibility check
Before locking the pick, read `RESEARCH.md` if one exists for it; otherwise launch the `idea-research` feasibility brief (see "Composing with other skills") and let the result feed Milestone 0. If it reveals a blocker, fall back to the runner-up.

## Phase 4: Evidence plan & judge-legibility

**Read `${CLAUDE_SKILL_DIR}/references/judging-playbook.md` now.**

For each criterion, name the artifact that proves it and where it lives (repo, README, live URL, video narration). Include: the **one measured claim**, a README with a claim→file table, AI-use disclosure in the required format, a no-login live URL with seeded data, sponsor-tech justification, and the demo-video script with key claims spoken aloud (an AI judge may only see a transcript).

## Phase 5: Agent-era timeline & milestones

**Read `${CLAUDE_SKILL_DIR}/references/agent-timeline.md` now.**

Non-negotiables:
- **No human-hours estimates.** Size work in agent sessions (S), human gates (H: keys, decisions, review, recording), and waits (W). The hard constraints are the deadline in wall-clock and the user's supervision windows.
- **Back-plan from the deadline** with a safety margin (submit ≥3–4h early; ≥1 day early for week-long events).
- **Fixed points:** spec/M0 ≈15%, deployed skeleton ≈30%, core flow real ≈55%, **feature freeze 75–80%**, rough-cut video ≈85%, QA ≈92%.
- **Milestone 0 is the kill-test spike** of the riskiest assumption; failure → switch to the runner-up.
- **Deploy on the first day**, spread commits across the event, record a rough-cut video before polish, and tag a demo-safe commit.
- Every task: self-contained, checkable "Done when", sequenced (same rules as `project-planner`), with type S/H/W.

## Phase 6: Output

1. Write `HACKATHON_PLAN.md` using `${CLAUDE_SKILL_DIR}/references/brief-template.md` (repo root if one exists, else the current directory). Include the Agent Rules block and mirror it into `CLAUDE.md` with a `PROJECT.md` pointer.
2. Optionally draft `SUBMISSION.md` (portal fields) if the user wants submission day to be copy-paste.
3. Give the first Claude Code command:
   ```
   claude "Read HACKATHON_PLAN.md. Complete Milestone 0 (the kill-test spike), fetching the latest official docs for any SDK before using it. Report whether the riskiest assumption holds. Stop after Milestone 0 and commit."
   ```
   and the resume command:
   ```
   claude "Read HACKATHON_PLAN.md and PROJECT.md. Find the first incomplete task and continue, fetching current docs for any library first. Respect the FEATURE FREEZE. Mark tasks done and commit at each milestone."
   ```

## Phase 7: Final summary (chat)

Keep it short; point to the file:

```
**Hackathon:** [name] — deadline [date tz], submit by [date]
**Judging:** [criteria + weights] — [human / AI-assisted / unknown]
**Pick:** [idea] — [one-line pitch]; runner-up: [idea]
**Why it should place:** [2 sentences tied to the rubric and winner patterns]
**The moment:** [beat]   **The number:** [measured claim]
**Biggest risk:** [risk] — tested first in Milestone 0
**Timeline:** freeze at [date/time]; [N] agent sessions, [M] human gates
**Unverified / couldn't access:** [list]
Full plan in HACKATHON_PLAN.md.
```

**After the hackathon:** if the project gets traction and the user wants to continue as a real product, offer to run `idea-research` (full, using the hackathon findings as input) and then `project-planner` to plan the post-hackathon roadmap. Point them to `HACKATHON_PLAN.md` as the source of prior decisions.

Be honest: if the user's idea scores poorly, the field is saturated, or the deadline is unrealistic for the scope, say so and recommend a cut or a different idea. That is a successful run.
