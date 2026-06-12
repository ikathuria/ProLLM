# Research Guide (Phase 2)

Deep methodology for market, feasibility, and monetization research. Run searches in parallel where possible. Always append the **current year** to trend/market searches (check today's date — never hardcode a past year).

---

## 2a. Market Research

### Competitor discovery — run all of these query shapes
- `[idea] existing tools OR apps OR competitors [year]`
- `best [product category] [year]` — listicles surface the established players fast
- `[competitor name] alternatives` — once you find one player, this finds the rest
- `site:reddit.com [problem] tool recommendation` — what real users actually use
- `[product category] open source` — free alternatives are competitors too
- Check Product Hunt for recent launches in the space (`site:producthunt.com [category]`)

### Competitor analysis framework
Build a table with one row per competitor (aim for 3–5):

| Field | What to capture |
|---|---|
| Name + URL | |
| Pricing | Free tier? Entry price? Per-seat or flat? |
| Core strength | The one thing it does best |
| Limitations | Missing features, platform gaps |
| User complaints | Mine Reddit, HN comments, G2/Capterra reviews, App Store reviews — complaints are the gap map |
| Last activity | Dead/stale products signal either a dead market or an open gap — figure out which |

### Demand signals (cheap validation, in rough order of strength)
1. **People already pay** for an inferior/adjacent solution → strongest signal
2. **Recurring complaints** about existing tools in forums ("I wish X did Y")
3. **Search volume** — `[problem] how to` results and forum thread counts
4. **DIY workarounds** — people stitching together spreadsheets/scripts for this means real pain
5. **No results at all** — usually means no demand, not an untapped goldmine. Treat as a red flag unless the idea is genuinely novel tech.

### Positioning verdict
End market research with one of:
- **Crowded, no angle** — recommend not building (or building only as a learning project)
- **Crowded, clear gap** — name the gap and the wedge feature
- **Niche, viable** — small but real audience; fine for portfolio/side income
- **Open** — rare; double-check it isn't open because demand is absent

### Kill criteria — recommend NOT building (or descoping to a weekend prototype) when
- The gap requires resources the user doesn't have (sales team, licensing, regulated data)
- A free, good-enough incumbent exists and the user's only differentiator is "mine will be nicer"
- The core value depends on network effects with zero distribution plan
- Demand evidence is purely hypothetical after honest searching
Say this plainly in the Viability Summary. A respectful "don't build this, here's why" is a valid and valuable output of this skill.

---

## 2b. Feasibility

### Identify the hardest part first
Name the single hardest technical problem (the "spike"). Search:
- `[core challenge] open source solution OR library [year]`
- `[core challenge] free API`
- `how does [competitor] implement [feature]` — engineering blogs often spill the approach

### API & service cost audit
For every external API/service the idea needs:
- Free tier limits (requests/day, rows, seats) — and what happens at the limit (hard stop vs. surprise bill)
- Is a credit card required up front?
- Self-hostable alternative? (e.g. Ollama vs. paid LLM APIs, Plausible self-hosted vs. cloud)
- **Flag any component with no free path** — this goes in the Viability Summary verbatim

### Effort classification
- **Easy** — CRUD + UI over known patterns; no spike
- **Medium** — one spike with a known library/API solution
- **Hard** — spike has no off-the-shelf solution, or requires ML training, realtime sync at scale, OS-level integration, or App Store review cycles
If **Hard**: recommend a milestone-0 prototype that proves only the spike, before any scaffold work.

---

## 2c. Monetization (skip if portfolio project)

### Realistic paths, simplest-first
1. **One-time purchase / lifetime deal** — simplest; no subscription infra; good for tools
2. **Freemium with usage gate** — free tier capped on the dimension that costs you money (API calls, storage, seats)
3. **Subscription** — only when value recurs monthly; needs Stripe + billing portal
4. **Donations/sponsorship** (GitHub Sponsors, Ko-fi) — for open-source; expect low conversion
5. **Ads** — only viable at high traffic; almost never right for a new side project

### Sanity checks
- Search `[similar product] pricing` for 2–3 comparables; anchor within their range
- Compute rough unit economics: if each user costs API money, the free tier must cap below the paid price
- **Recommend the path with the least infrastructure** that matches the value model; monetization can be Milestone N, not Milestone 1

---

## Output of Phase 2
Carry forward into PLAN.md (Research Findings section):
- Competitor table
- Positioning verdict + the gap (if any)
- Hardest technical part + chosen approach
- Cost flags (anything not free)
- Recommended monetization path (or "portfolio project")
