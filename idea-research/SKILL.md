---
name: idea-research
description: >
  Multi-agent viability research for a product or project idea: competitors, real user pain
  (Reddit/HN), video demand (YouTube), news and search-interest trends (Google Trends),
  technical feasibility, and monetization — synthesized into a RESEARCH.md with an honest
  build / don't-build verdict. Trigger when the user asks "is this feasible", "is there a
  market for this", "who are the competitors", "can this make money", "validate this idea",
  or wants market/demand research on any idea or existing product. Runs DEEP mode by
  default — parallel research subagents — whether invoked explicitly (/idea-research) or
  by another skill (e.g. project-planner). Runs QUICK mode (inline, no subagents) only
  when the user explicitly asks for a quick/light check.
---

# Idea Research Skill

Researches whether an idea is worth building. Output: a `RESEARCH.md` report (template in `references/research-template.md`) plus a short verdict in chat.

## Mode selection — decide this first

- **DEEP (default)** — fan out parallel research subagents (Phase 2A). This is the default whether the user invoked `/idea-research` directly or another skill (e.g. project-planner) invoked it.
- **QUICK** — only when the user explicitly asked for a quick/light check, or subagents are unavailable in the environment. No subagents; run the condensed inline flow (Phase 2B). Same output files, lighter evidence — and say in the verdict that it was a quick pass.

Deep mode is a multi-minute, search-heavy run — that's the contract. Don't silently downgrade to quick; if you must (e.g. no subagent capability), tell the user.

---

## Phase 1: Frame the research

Everything downstream inherits this framing, so get it right before launching anything. Distill from the conversation (ask only if genuinely missing):

- **IDEA** — one sentence, concrete ("an app that X for Y"), not the user's whole pitch
- **PROBLEM** — the underlying problem, phrased the way a *user* would say it (this phrasing drives community searches)
- **TARGET_USER** — who feels the problem
- **CATEGORY** — the product category name people actually search for
- **SEED_TERMS** — 3–5 search phrases, mixing product-category terms and problem-phrased terms
- **COMPONENTS** — likely technical pieces (for the feasibility agent)
- **YEAR** — today's year (check the date; never assume)

---

## Phase 2A: DEEP mode — fan out research agents

Read `references/report-schema.md`. Then build five prompts by filling the placeholders in each brief and appending the report schema to each:

| Agent | Brief | Covers |
|---|---|---|
| Competitor | `references/competitor-brief.md` | Players, pricing, complaints, category pricing models |
| Community | `references/community-brief.md` | Reddit + HN + forums: verbatim pain, DIY workarounds, willingness to pay |
| Video demand | `references/video-brief.md` | YouTube metadata as demand signal |
| News & trends | `references/trends-brief.md` | Funding/shutdowns/regulation, Google Trends (with proxies), momentum |
| Feasibility | `references/feasibility-brief.md` | The spike, cost audit, prior-art failures |

Launch rules:
- **All five in a single message** so they run in parallel (general-purpose agents; they need WebSearch/WebFetch).
- Each prompt must be fully self-contained — subagents do not see this conversation.
- Do not edit the schema or honesty rules when composing prompts; they're what makes reports mergeable and trustworthy.

### Model and effort per agent

Pass a `model` on each Agent launch and append a budget line to each prompt. Defaults:

| Agent | Model | Budget line to append |
|---|---|---|
| Competitor | sonnet | "Budget: ~20–25 searches/fetches. Depth on the top 3–5 players beats breadth." |
| Community | sonnet | "Budget: ~20–25 searches/fetches. Prioritize fetching full threads over collecting more links." |
| Video demand | haiku | "Budget: ~10–15 searches. Metadata collection only — don't over-analyze." |
| News & trends | sonnet | "Budget: ~15–20 searches/fetches." |
| Feasibility | sonnet | "Budget: ~20–25 searches/fetches. Fetch real pricing pages; secondhand pricing is stale." |

- Every budget line ends with: "Stop early when marginal results start repeating what you already have."
- Rationale: video work is mechanical metadata collection (haiku is enough); the others need judgment about evidence quality (sonnet). There is no native "effort" knob on subagents — the budget line IS the effort control.
- **Escalation:** if the user signals high stakes ("considering quitting my job", "about to raise money"), omit `model` so agents inherit the main session's model, and raise budgets ~50%.
- If a named model is unavailable in the environment, omit `model` and let agents inherit.

## Phase 2B: QUICK mode — inline research

No subagents. Run a condensed pass yourself with web search, using the briefs as query playbooks:
1. Competitor sweep — discovery queries from `competitor-brief.md`; profile the top 3 players (pricing, complaints, activity)
2. Community sweep — `site:reddit.com` + HN Algolia queries from `community-brief.md`; collect 3–5 verbatim pain quotes
3. Trend check — 2–3 news/trend queries from `trends-brief.md`
4. Feasibility check — spike identification + cost audit from `feasibility-brief.md` (this part is not optional even in quick mode; hidden costs sink projects)

Skip the video agent's work in quick mode unless the domain is obviously consumer/visual. Apply the same honesty rules: distinguish "found nothing" from "couldn't access", and date what you cite.

---

## Phase 3: Synthesize

Merge the reports (or your inline findings). Synthesis is where the value is — do not just concatenate:

1. **Cross-reference.** Do community complaints match competitor weaknesses? (That's the wedge.) Does news momentum contradict dead forums? Do the same competitor names recur across agents? Conflicts go in the report's *Conflicts & unknowns* — a disagreement between sources is a finding, not noise.
2. **Weigh evidence by strength rating**, and read everything net of the *Could not access* lists.
3. **Positioning verdict:** crowded-no-angle / crowded-with-gap (name it) / niche-viable / open (and whether "open" = absent demand).
4. **Monetization (skip if portfolio project).** From the competitor agent's pricing data: pick the simplest path that matches the value model — one-time → freemium-with-usage-gate → subscription → donations (ads almost never, for a new project). Anchor against 2–3 comparables; if usage costs money (e.g. LLM calls), the free tier must cap below the paid price. Monetization can be a late milestone — recommend the least infrastructure that works.
5. **Kill criteria — recommend NOT building (or a weekend prototype only) when:**
   - The gap requires resources the user doesn't have (sales team, licensing, regulated data)
   - A free, good-enough incumbent exists and the only differentiator is "mine will be nicer"
   - Core value depends on network effects with zero distribution plan
   - Demand evidence is purely hypothetical after honest searching
   A respectful "don't build this, here's why" is a successful run of this skill, not a failure.

---

## Phase 4: Output

1. **Write `RESEARCH.md`** using `references/research-template.md` — in the project repo root if one exists, else the current directory. Keep the verbatim quotes; they are the evidence. Fill the *Could not access* section honestly.
2. **Give the verdict in chat** — short: the Verdict table's "Build it?" line, the two-sentence bottom line, and the single strongest piece of evidence for it. Point to RESEARCH.md for everything else. Do not duplicate the whole report into chat.
3. If invoked by another skill (project-planner), also hand back the verdict block so it can flow into PLAN.md's Research Findings.
