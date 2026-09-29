# Ideation & Scoring (Phase 3)

Purpose: pick the idea most likely to *place*, not the one most interesting in the abstract. Ideas are generated from the user's unfair advantages, then scored against this hackathon's actual rubric plus hackathon-specific risk.

---

## Step 1: Mine the user's unfair advantages (ask, don't guess)

Ask (skip what's already answered):
1. What do you know from work, past jobs, school, family, community, or hobbies that most engineers don't? (Insider knowledge is the strongest winner pattern.)
2. Is there a specific person you know with a costly problem you could talk to this week? (Real-user grounding.)
3. Any data, tools, or access you already have (datasets, APIs, hardware, credits, a domain audience)?
4. Tech you want to use or avoid; anything already built (check the new-work rule).
5. Risk appetite: safe-and-polished vs swing for a wow moment.

If the user has no strong insider angle, generate ideas from the hackathon's theme + sponsor tech + an underserved population, and flag "no insider edge" as a risk to offset with a real-user conversation and stronger evidence.

## Step 2: Generate 6–8 candidates

Use the shapes the evidence says win (`winning-patterns.md`):
- Insider fixes a costly specific workflow, with a number.
- Accessibility tool for a named person/condition.
- Agent + **verification loop** with a measurable accuracy claim.
- Voice / vision / hardware moment that reads in 10 seconds.
- Simulation/forecast scored against ground truth.
- A retellable beat (something two-sentence-tellable, like agents that elect a mayor).

Deliberately include at least one wildcard. Avoid shapes on the weak list (generic chatbot/RAG, "assistant for X" with no angle, feature soup). Each candidate is one sentence: **"[Named user] can [do the thing] in [time] instead of [pain, with number] because [mechanism]."**

## Step 3: Kill filters (drop before scoring)

Drop a candidate if any is true:
- Violates the rules (new-work, required tech missing, ineligible category).
- Needs data, users, or partnerships unobtainable in the window.
- Can't produce a working end-to-end flow on a public URL by the freeze point.
- "Existing product + chatbot" with no defensible difference.
- Requires a live-only demo with fragile hardware and no fallback.
- Ethically unsafe for a hackathon demo (real patient data, scraping personal data, medical/legal claims without guardrails).

## Step 4: Novelty check (mandatory, cheap)

For each survivor: search Devpost (`site:devpost.com <core idea keywords>`), GitHub, and Product Hunt for near-duplicates, with the hackathon's gallery first. Note nearest 2 comparables and the one-sentence difference. If a past *winner* of this same series already did it, the idea needs a clear step beyond, or drop it.

## Step 5: Score against the actual rubric

Build the matrix with the **hackathon's own criteria and weights** from Phase 2 as columns (not generic ones). Score each 1–5, multiply by weight, then add these hackathon-specific columns (unweighted, shown as modifiers):

| Extra column | Question | Scale |
|---|---|---|
| **Insider edge** | Does the user know this domain / have a real person to test with? | 0–2 |
| **Demo moment** | Is there a retellable beat visible in ≤15s? | 0–2 |
| **Evidence potential** | Can we produce a measured claim (eval/before-after) in the window? | 0–2 |
| **Agent-buildability** | Can coding agents build the core with well-documented APIs? Any hard unknowns (hardware, unpublished APIs, heavy training)? | 0–2 |
| **Prize stacking** | Does it qualify for sponsor/category prizes in addition to the grand prize? | 0–2 |
| **Risk** | Probability the core flow fails or a dependency blocks it (subtract 0–3) | −3–0 |

Output the matrix in the brief. Show the arithmetic; don't just assert a winner.

## Step 6: Choose one (and a fallback)

Recommend **one** idea with a 3-sentence justification tied to the criteria, and name the **runner-up** as a fallback if the Day-0 spike fails. Ask the user to confirm before planning. Then define, in the brief:
- **One-sentence pitch** and the **retellable moment**.
- **The one measured claim** the project will make and how it will be measured.
- **Scope cut list:** the 2–3 features that look tempting but are explicitly out. Solo agent-driven builds fail from scope creep because firing off agent tasks is nearly free.
- **The kill test:** the riskiest assumption, tested first (Milestone 0).
