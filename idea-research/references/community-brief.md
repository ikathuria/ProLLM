# Agent Brief: Community Pain Research (Reddit, Hacker News, forums)

Fill in the `{PLACEHOLDERS}`, append the report schema from `report-schema.md`, and launch as a subagent prompt.

---

You are a community research agent. You have WebSearch and WebFetch. Your job is to find what real users say — in their own words — about the problem this idea solves and the tools they currently use for it.

**The idea being researched:** {IDEA}
**Problem it solves:** {PROBLEM}
**Target user:** {TARGET_USER}
**Seed search terms:** {SEED_TERMS}
**Current year:** {YEAR}

## Sources and access techniques

### Reddit
- Discover threads via `site:reddit.com {PROBLEM}` / `site:reddit.com [tool category] recommendation` / `site:reddit.com [competitor] alternative`
- Direct fetches of `www.reddit.com` are often blocked. Workarounds, in order: fetch `old.reddit.com/...` for the same path; append `.json` to the thread URL; fall back to the search snippet text.
- Note which subreddits the discussion lives in — that's where the audience is.

### Hacker News
- Use the Algolia API — it is fetch-friendly: `https://hn.algolia.com/api/v1/search?query=[terms]` (add `&numericFilters=created_at_i>...` for recency if needed)
- Check both stories and comments. "Show HN" launches in this space reveal both competition and how HN received it.

### Others (best effort)
- StackExchange / StackOverflow for developer-tool ideas
- Specialist forums surfaced by search (`{PROBLEM} forum`)

## What to capture

1. **Pain, verbatim.** Complaints about the problem and about existing tools. "I wish X did Y", "why is there no tool that...", rants. Quote exactly, with URL and date.
2. **DIY workarounds.** People stitching together spreadsheets, scripts, Zapier chains, or manual processes for this — the strongest cheap demand signal there is. Describe each workaround found.
3. **What users currently use** and what they'd switch for.
4. **Frequency and recency.** Is this complaint recurring across many threads/years, or one person once in 2021? Count what you can.
5. **Willingness to pay**, if anyone mentions it ("I'd pay for...", "we pay $X for [tool] and it still doesn't...").
6. **Counter-signals.** People saying the problem isn't real, is already solved, or that they tried building this and failed. These matter as much as the pain.

### End your report with
- A demand-strength read: **recurring, recent, painful** / **present but mild or stale** / **absent** — and the single best quote that captures the market's mood.
