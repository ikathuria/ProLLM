# Single-Paper Reading Procedure

Used directly for one-paper asks, and for every full-text read inside a literature review.

## Stage 1 — Get the full text (never summarize from memory)

- **Local PDF:** use the `pdf` skill / `pdftotext -layout` to extract text. Read the whole
  thing in chunks; for >20 pages read with the Read tool's `pages` param in ranges.
  If text extraction is empty/garbled (scanned PDF), say so and OCR or read pages as images.
- **arXiv ID/URL:** fetch `https://arxiv.org/abs/<id>` for metadata and the PDF from
  `https://arxiv.org/pdf/<id>` (download to the scratchpad). Prefer the HTML version
  (`https://arxiv.org/html/<id>`) when available — cleaner tables.
- **DOI / publisher page:** fetch it; if paywalled, say so and ask the user for the PDF.
  Do not fall back to what you "know" about the paper.
- Record exact title, authors, venue/year, and version (arXiv v1/v2…) from the source itself.

If you recognize the paper from training data, **ignore that memory** — papers get revised,
and recalled numbers are the main hallucination source. Only the fetched text counts.

## Stage 2 — Build an evidence map before writing

Go section by section and extract into a working list (scratchpad, not the final output):

- Research question / claimed contributions (usually end of intro) — verbatim
- Method: architecture, data, training/eval setup — with section numbers
- Every headline number: value, metric, dataset, baseline, table/figure number
- Limitations the **authors** state
- Anything ambiguous or under-specified

Each entry carries a locator: `§3.2`, `Table 2`, `Fig. 4`, `p. 7`.

## Stage 3 — Write with provenance tags

Use the template in `${CLAUDE_SKILL_DIR}/references/notes-template.md`. Every factual line gets
a locator. Mark statement types:

- `"quoted text" (§4.1)` — verbatim, for key claims and definitions
- plain text + `(Table 3)` — faithful paraphrase
- **[Interpretation]** — your own reading, inference, or critique; always labeled

Hard rules:
1. **Numbers are copied, never computed or rounded** unless you show the arithmetic and label it.
2. **No invented baselines, datasets, or comparisons.** If the paper doesn't compare to X, say "not compared".
3. **"Not stated in the paper"** is a valid and required answer when something is missing.
4. Don't upgrade hedged claims ("suggests" ≠ "proves"); preserve the authors' certainty level.
5. Distinguish what the authors *claim* from what their experiments *show*.
6. External context (related work, later papers) only if fetched and cited with a link, in its own section.

## Stage 4 — Verify before delivering

Run the checklist in `${CLAUDE_SKILL_DIR}/references/verification-checklist.md`: re-open the
source and confirm every number and every quote against it. Delete or fix anything that
doesn't match. State at the end: `Verified: N numbers, M quotes checked against source.`

## Single-paper modes

- **Quick summary** (user asks "tl;dr", "what's this about"): the TL;DR + Key results sections only, in chat, still with locators.
- **Full notes** (default for "read/summarize this paper"): `PAPER_NOTES.md` (or `notes/<first-author><year>.md` if a notes folder exists).
- **Q&A** ("does it say X?"): answer with the quote + locator, or "the paper does not address this" and where you looked.
- **Compare papers**: build the evidence map per paper, then a table where each cell has its own locator; never align metrics that aren't actually comparable — flag differing datasets/setups.
- **Critique**: after full notes, add a labeled critique section (threats to validity, missing ablations, reproducibility — code/data availability as stated in the paper).
