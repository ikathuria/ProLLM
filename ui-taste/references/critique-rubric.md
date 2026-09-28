# Visual Critique Rubric

Score each 1–5 from the screenshots (not from the code). Anything < 3 must be fixed.

| # | Criterion | 5 looks like |
|---|---|---|
| 1 | **Distinctiveness** | Couldn't be mistaken for a default template; the signature move is visible |
| 2 | **Hierarchy** | Squint test: the one most important thing per screen is obvious |
| 3 | **Typography** | Clear scale, comfortable line length, pairing matches the brief |
| 4 | **Color discipline** | Neutrals + one accent, accent used only for meaning/action |
| 5 | **Spacing & alignment** | Consistent unit, strong alignment edges, varied section rhythm |
| 6 | **Content realism** | Specific copy/data, no filler phrases from the ban list |
| 7 | **Slop count** | Zero patterns from slop-patterns.md (score 5 − count, min 1) |
| 8 | **Mobile** | 375px layout is designed, not just stacked; no horizontal scroll |
| 9 | **States & a11y** | Focus visible, contrast passes, empty/loading/error exist |

Output format:

```
Brief: <reference · type · accent · signature move>
Scores: Distinct 4 · Hierarchy 3 · Type 4 · Color 5 · Spacing 3 · Content 2 · Slop 4 · Mobile 3 · A11y 4
Fixes applied: <bullets>
Remaining: <bullets or "none">
```
