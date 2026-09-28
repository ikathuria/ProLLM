# Research Guide (Phase 2 fallback)

Condensed playbook for when the `idea-research` skill isn't installed. (If it is, use it instead — it runs this research far more thoroughly, with parallel agents and a full `RESEARCH.md`.) Run searches in parallel where possible, append the **current year** to trend/market searches, and date what you cite.

---

## 2a. Market

**Competitor discovery** — run these query shapes:
- `best [category] [year]` · `[category] existing tools OR apps [year]` · `[first competitor] alternatives`
- `[category] open source` · `site:producthunt.com [category]`
- `site:reddit.com [problem] tool recommendation` (reddit.com itself can't be fetched — quote search snippets) · HN via `https://hn.algolia.com/api/v1/search?query=[terms]&tags=comment`

**Per competitor (3–5):** name + URL · pricing (fetch the real pricing page) · core strength · limitations · verbatim user complaints · last activity.

**Demand signals, strongest first:** people already pay for an inferior solution → recurring complaints ("I wish X did Y") → DIY workarounds (spreadsheets, scripts) → search/tutorial volume. No results at all usually means no demand, not a goldmine.

**Positioning verdict:** crowded-no-angle / crowded-with-gap (name the wedge) / niche-viable / open (check it isn't open because demand is absent).

## 2b. Feasibility

- **The spike:** name the single hardest technical problem; search `[challenge] open source library [year]`, `[challenge] free API`, `how does [competitor] implement [feature]`.
- **Cost audit:** for every external service — free-tier limit, hard stop vs. surprise bill at the limit, card required up front, self-hostable alternative. **Flag anything with no free path.**
- **Classify:** easy (CRUD, no spike) / medium (spike with a known solution) / hard (no off-the-shelf solution, ML training, realtime at scale, OS-level, App Store review) → hard means Milestone 0: Spike.
- **Prior-art failures:** `[idea] postmortem OR "why we shut down"`.

## 2c. Monetization (skip if portfolio project)

Simplest-first: one-time purchase → freemium with a usage gate → subscription (only if value recurs monthly) → donations → ads (almost never). Anchor against 2–3 comparables' pricing; if each user costs API money, the free tier must cap below the paid price. Monetization can be a late milestone.

## Kill criteria — recommend NOT building (or a weekend prototype only) when

- The gap needs resources the user doesn't have (sales team, licensing, regulated data)
- A free, good-enough incumbent exists and the only differentiator is "mine will be nicer"
- Core value depends on network effects with zero distribution plan
- Demand evidence is purely hypothetical after honest searching

## Output

Fill PLAN.md's Viability Summary table and Research Findings — including the competitor table, since there's no RESEARCH.md to link to. Say "searched X, found nothing" vs. "couldn't access X" honestly. Then apply the Phase 2 gate in SKILL.md.
