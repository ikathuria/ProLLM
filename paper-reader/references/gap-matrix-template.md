# Gap Analysis — <topic>

## Coverage matrix
Rows = <facet A, e.g. methods>; columns = <facet B, e.g. domains/datasets/eval criteria>.
Cells list the review-table # of papers covering that combination; `—` = none found.

| | Col 1 | Col 2 | Col 3 | Col 4 |
|---|---|---|---|---|
| Row 1 | 1, 4, 7 | 2 | — | 9 |
| Row 2 | — | 3, 5 | — | — |

Optionally a second matrix on another facet pair (e.g. approach × evaluation property such as
robustness, fairness, efficiency, real-world deployment).

## Author-stated gaps
| Gap as stated | Paper # | Locator |
|---|---|---|

## Validated gaps
| ID | Gap | Type | Evidence (matrix cell / author statements) | Validation search (query, date, result) | Status | [Interpretation] Significance & feasibility |
|---|---|---|---|---|---|---|
| G1 | … | methodological | Row 2 × Col 3 empty; #4 §6 | "…" OpenAlex+arXiv 2026-09-28: 0 hits | Open | … |

Types: evidence · methodological · population/domain · evaluation · theoretical · practical.
Status: **Open** (validation search found nothing) · **Partially addressed** (cite paper) · **Closed** (cite paper).

## Why cells may be empty (check before claiming a gap)
- The combination is meaningless or trivially solved
- Covered under different terminology — search synonyms
- Covered in a venue/field outside the search scope
- Covered in very recent work not yet indexed

## Recommended directions
Top 3–5 open gaps, ranked, each with a one-line rationale. **[Interpretation]**
