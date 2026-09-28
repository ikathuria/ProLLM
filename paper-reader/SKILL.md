---
name: paper-reader
description: >
  Grounded research-paper reading and literature reviews, with every claim tied to a
  quoted passage and section/table locator — no hallucinated papers, numbers, or findings.
  Two modes. SINGLE PAPER: the user shares a paper (PDF, arXiv ID/link, DOI, pasted text)
  and asks to read, summarize, explain, critique, or extract results from it. LITERATURE
  REVIEW: the user asks for a lit review, related work, state of the art, "what research
  exists on X", a gap analysis / gap matrix, or "find papers on X" — runs a scoped,
  logged search (peer-reviewed first, preprints as fallback), title/abstract then
  full-text screening, downloads open-access PDFs, and produces a literature review table
  plus a validated gap analysis matrix.
---

# Paper Reader Skill

Core rule for every mode: **nothing goes in the output that can't be pointed to in a source
you actually fetched.** Never cite a paper from memory — every paper must come from a search
API result with a resolvable DOI/arXiv ID/URL. Invented citations are the #1 failure to prevent.

## Mode selection

- One or a few specific papers given → **Single paper**: follow `${CLAUDE_SKILL_DIR}/references/single-paper.md`.
- A topic/question given → **Literature review**: follow the stages below.

---

# Literature Review Mode

Outputs go in `lit-review/<topic-slug>/`:
`PROTOCOL.md`, `search-log.md`, `screening.csv`, `papers/` (PDFs), `notes/` (per-paper notes),
`LIT_REVIEW.md` (review table + synthesis), `GAP_MATRIX.md`.

## Stage 1 — Scope the question (ask before searching)

Draft the scope, then ask the user only what you can't infer (use AskUserQuestion, max 4):
- **Research question** in one sentence; break into PICO-style facets or concept blocks
  (e.g. *method* × *task* × *domain* × *evaluation*).
- **Purpose:** related-work section, thesis chapter, project scoping, or finding a gap to work on
  — this sets depth (≈15, 30, or 50+ included papers).
- **Boundaries:** year range, languages, venues/fields, study types to include/exclude.
- **Known seed papers** the user already trusts (great for snowballing and for testing recall).

Write `PROTOCOL.md` from `${CLAUDE_SKILL_DIR}/references/protocol-template.md`: question,
facets, synonyms, **inclusion/exclusion criteria fixed before screening**, sources, and the
stopping rule. Show it to the user; proceed on approval (or immediately if they said not to ask).

## Stage 2 — Search, peer-reviewed first

Follow `${CLAUDE_SKILL_DIR}/references/search-sources.md` for APIs and query syntax.
1. Build a boolean query per source from the facet synonyms.
2. Search **peer-reviewed** sources first (OpenAlex filtered to journal/conference venues,
   Semantic Scholar with venue present, Crossref, PubMed for biomedical, DBLP for CS venues).
3. **Preprint fallback:** if fewer than the target number of candidates pass title/abstract
   screening, add arXiv / bioRxiv / medRxiv / SSRN. In fast-moving fields (ML, LLMs) state
   that preprints are necessary and add them anyway, flagged.
4. For every preprint, check whether a peer-reviewed version now exists (same title in
   OpenAlex/Semantic Scholar/DBLP); cite the published version if so.
5. **Snowball:** backward (references) and forward (citing papers) from seed papers and the
   top ~5 included papers, via Semantic Scholar citations/references endpoints.
6. De-duplicate by DOI, then normalized title.
7. Log every query, source, date, filters, and hit count in `search-log.md` — the review must
   be reproducible.

Stop when the stopping rule is met: new searches/snowball rounds return mostly already-seen
papers (saturation), or the target count is reached.

## Stage 3 — Screen in two passes

Record every decision in `screening.csv` (`id,title,year,venue,peer_reviewed,stage,decision,reason`).
1. **Title/abstract screen** against the protocol criteria. Keep borderline ones for pass 2.
   Reasons must reference a criterion (e.g. `EX2: not an empirical study`).
2. **Full-text screen** (after Stage 4) — abstracts oversell; exclude papers whose full text
   doesn't meet the criteria.
3. Check retractions (Crossref `update-to` / Retraction Watch data via OpenAlex `is_retracted`).
Report PRISMA-style counts: identified → deduplicated → screened → full-text assessed → included.

## Stage 4 — Get the full texts (legally)

Download to `papers/<firstauthor><year>-<shortslug>.pdf` from open-access locations only:
arXiv, PubMed Central, OpenAlex `best_oa_location`, Semantic Scholar `openAccessPdf`, author
or institutional repositories. **Never use shadow libraries (Sci-Hub, LibGen, etc.).**
Paywalled with no OA copy → list it in `LIT_REVIEW.md` under "Needs access" with the DOI and
ask the user to supply the PDF; screen/extract it from the abstract only, flagged `abstract-only`.

## Stage 5 — Extract and appraise each paper

For each included paper, read the full text using `single-paper.md` (stages 1–2 evidence map)
and save `notes/<id>.md`. Also record a quick quality appraisal: peer-reviewed?, sample/dataset
size, baselines adequate?, code/data released?, stated limitations. Every extracted field
carries a locator (§, Table, Fig.).

## Stage 6 — Literature review table + synthesis

Write `LIT_REVIEW.md` from `${CLAUDE_SKILL_DIR}/references/lit-review-template.md`:
- The **review table** (one row per paper, fixed columns, locators in cells).
- A **thematic synthesis** grouping papers by approach, not a paper-by-paper list:
  where they agree, where they conflict, and why (different data, metrics, setups).
- A timeline/trajectory of how the area evolved, if relevant.

## Stage 7 — Gap analysis matrix

Write `GAP_MATRIX.md` from `${CLAUDE_SKILL_DIR}/references/gap-matrix-template.md`:
1. Pick the matrix axes from the protocol facets (e.g. methods × datasets/domains, or
   approaches × evaluation criteria). Cells = papers covering that combination.
2. Empty or thin cells are **candidate** gaps. Also collect gaps the authors themselves name
   in limitations/future-work sections (with locators).
3. **Validate each candidate gap** before reporting it: run a targeted search for that exact
   combination (including the last 12 months of preprints). A gap is only reported as open if
   that search finds nothing; otherwise note the paper that fills it.
4. Classify each gap (evidence, methodological, population/domain, evaluation, theoretical,
   practical) and rate it: how well-evidenced is the gap, and is it a gap *because it doesn't
   matter* or because it's hard/overlooked? Label this judgement **[Interpretation]**.

## Stage 8 — Verify and report

Before delivering, check: every cited paper resolves (DOI/arXiv link works), every number and
quote matches its source (`references/verification-checklist.md`), every gap has its validation
search logged. End in chat with PRISMA counts, the top 3–5 validated gaps, the "Needs access"
list, and the file paths.
