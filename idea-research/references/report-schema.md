# Shared Agent Report Schema

Append this schema verbatim to every research agent's prompt. Every agent returns its report in exactly this structure so the orchestrator can merge them.

---

## Output format (return exactly this structure)

```markdown
## [Agent name] Report

### Summary
[3–5 sentences: the headline findings.]

### Findings
One block per finding:
- **Claim:** [one sentence]
  **Evidence:** [what was actually seen]
  **Source:** [URL] ([date of the source, if visible])
  **Strength:** strong / moderate / weak

### Verbatim quotes
Real user/author words, quoted exactly, each with source URL. No paraphrasing.
> "[quote]" — [source URL]

### Surprises
[Anything that contradicts the obvious narrative or the idea's premise. "None" is acceptable.]

### Could not access
[Every source that was tried and blocked/unfetchable. Name the site and what was tried.]

### Confidence
[high / medium / low] — [one sentence why]
```

## Honesty rules (binding)

1. **"Found nothing" ≠ "couldn't look."** If a search returned no relevant results, say "searched X, found nothing relevant." If a fetch was blocked, that goes under *Could not access*. Never let an access failure masquerade as absence of demand.
2. **No padding.** Thin findings reported thinly. Do not inflate three weak data points into a confident narrative.
3. **Quote verbatim.** User complaints and praise are evidence only in their original words.
4. **Date everything you can.** A 2019 complaint and a last-month complaint are different signals.
5. **Use the current year in trend searches.** Check today's date; never hardcode a past year.
6. **Strength ratings are earned:** *strong* = multiple independent sources or hard numbers; *moderate* = one good source; *weak* = single mention, indirect inference, or stale data.
