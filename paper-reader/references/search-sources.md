# Search Sources & Query Recipes

All free, no key required for light use. Keep request rates modest (≤1 req/s for Semantic
Scholar without a key; back off on HTTP 429). Do not put the user's personal data in query strings.
If an endpoint's behavior differs from what's written here, check its current docs and trust the docs.

## Peer-reviewed first

**OpenAlex** — broadest index; good peer-review signal via venue type.
```
https://api.openalex.org/works?search=<terms>
  &filter=from_publication_date:2019-01-01,primary_location.source.type:journal|conference,is_retracted:false
  &per_page=50&select=id,doi,title,publication_year,primary_location,best_oa_location,type,cited_by_count
```
Abstracts come as `abstract_inverted_index` — reconstruct by ordering words by position.

**Semantic Scholar** — strong for CS/biomed, citation graph, OA PDFs.
```
https://api.semanticscholar.org/graph/v1/paper/search?query=<terms>&year=2019-
  &fields=title,abstract,year,venue,publicationVenue,publicationTypes,externalIds,openAccessPdf,citationCount
```
Snowballing: `/graph/v1/paper/{id}/references` and `/graph/v1/paper/{id}/citations`
(`{id}` can be `DOI:...` or `ARXIV:...`).

**Crossref** — authoritative DOI metadata and retraction/update notices.
`https://api.crossref.org/works?query=<terms>&filter=from-pub-date:2019,type:journal-article&rows=50`

**PubMed** (biomedical) — `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<query>&retmode=json`
then `efetch`/`esummary`. PMC full text for OA papers.

**DBLP** (CS venues) — `https://dblp.org/search/publ/api?q=<terms>&format=json&h=100`

## Preprint fallback

**arXiv** — `http://export.arxiv.org/api/query?search_query=abs:"<phrase>"+AND+cat:cs.CL&max_results=100`
(Atom XML). PDF: `https://arxiv.org/pdf/<id>`, HTML: `https://arxiv.org/html/<id>`.
**bioRxiv/medRxiv** — `https://api.biorxiv.org/` (details by DOI/date range); search via OpenAlex/Semantic Scholar filters.

## Peer-review signal
Treat as peer-reviewed when the venue is a journal or a refereed conference proceedings.
Not peer-reviewed: arXiv/bioRxiv/SSRN, workshop non-archival papers, theses, tech reports, blogs.
Record the signal used in `screening.csv` (`peer_reviewed=yes|no|unclear`).

## Open-access PDF lookup order
1. Semantic Scholar `openAccessPdf.url`  2. OpenAlex `best_oa_location.pdf_url`
3. arXiv / PMC ID from `externalIds`  4. Author or institutional page found via web search.
Never shadow libraries.
