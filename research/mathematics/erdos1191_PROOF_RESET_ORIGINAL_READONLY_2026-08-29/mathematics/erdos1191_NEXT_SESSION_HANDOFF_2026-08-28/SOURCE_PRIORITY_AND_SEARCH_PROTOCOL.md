# Source Priority and Search Protocol

## Priority table

| Priority | Site/tool | Mathematical specialization | Main strength | Use for open-problem audit |
|---|---|---:|---|---:|
| S | zbMATH Open | ★★★★★ | Mathematics database, reviews, MSC, citations, author and arXiv links | ★★★★★ |
| S | MathSciNet | ★★★★★ | AMS database, expert reviews, citation graph, MR identifiers | ★★★★★ |
| S | arXiv Mathematics | ★★★★★ | Fastest access to current public preprints and version history | ★★★★★ |
| S | MathOverflow | ★★★★★ | Research-level discussion of whether a result/problem is known | ★★★★★ |
| A | EuDML | ★★★★★ | European and historical mathematical literature | ★★★★☆ |
| A | Numdam | ★★★★★ | French and European full-text mathematical literature | ★★★★☆ |
| A | Project Euclid | ★★★★☆ | Mathematics/statistics journal archive | ★★★★☆ |
| A | Math-Net.Ru | ★★★★★ | Russian/Soviet mathematical literature | ★★★★☆ |
| B+ | Google Scholar | ★★☆☆☆ | Forward citations and “cited by” trails | ★★★★☆ |
| B+ | SciSpace | ★★☆☆☆ | Semantic discovery and structured paper triage | ★★★★☆ |
| B+ | Exa Complex / Exa | ★★☆☆☆ | Semantic web/paper discovery and page extraction | ★★★★☆ |
| B | Consensus | ★☆☆☆☆ | Natural-language research discovery | ★★☆☆☆ |
| Auxiliary | Firecrawl | — | Search/scrape dynamic pages, full-page extraction, research index, site mapping | ★★★★☆ |
| Mandatory | Ordinary web search | — | Exact-title/formula search, official pages, recent changes | ★★★★★ |

## Search order

1. Verify the exact current public problem statement and cited original source.
2. Search exact titles/formulas on arXiv and journal sites.
3. Search zbMATH and MathSciNet for reviews, MR/Zbl identifiers, and citation links.
4. Search backward/forward citations through Google Scholar and bibliographies.
5. Search MathOverflow for “known?”, “open?”, and adjacent theorem discussions.
6. Search EuDML, Numdam, Project Euclid, and Math-Net.Ru for older or regional literature.
7. Use SciSpace, Exa, Consensus, and Firecrawl to discover missed vocabulary or papers.
8. Fetch and verify every load-bearing claim in a primary source.
9. Repeat the search using the distinctive statement of any proposed new lemma before claiming novelty.

## Required exact queries and variants

Search at least the following classes of query:

### Problem formulations

- `"Erdős Problem #1191"`
- `"liminf" "infinite Sidon" "log x"`
- `"limsup" a_n "n^2 log n" Sidon`
- `infinite B_2 sequence a_n n^2 log n`
- `dense infinite Sidon sequence polylogarithmic`
- `A(x) sqrt(log x/x) Sidon`

### Current frontier

- `"On the Thickness of Infinite Generalized Sidon Sets, I" O'Bryant`
- `arXiv 2606.28651`
- `arXiv 2607.23795`
- `"Infinite Sidon-type sets for zero-sum linear forms"`
- `arXiv 2607.20753`
- `"Infinite Sidon sequences" Cilleruelo`
- `Ruzsa "An Infinite Sidon Sequence"`

### Endpoint-variance novelty audit

- `cyclic interval coverage variance endpoint imbalance`
- `directed graph divergence H^{-1} cycle`
- `negative Sobolev norm graph imbalance cycle`
- `circular discrepancy arc coverage variance`
- `Eulerian residue graph additive combinatorics`
- `Golomb ruler residue graph cycles`
- `homometric sets endpoint incidence variance`
- `Sidon offset block energy variance`
- `inverse Laplacian cycle graph discrepancy`
- `martingale entropy Sidon sequence density`

### Finite uniformity connection

- `extremal Sidon sets Fourier uniform`
- `dense finite Sidon residue classes equidistribution`
- `Sidon set arithmetic progression local density`
- `Sidon gaps finite Fourier coefficients`

## Relevance filters

For every result, explicitly answer:

1. Additive integer Sidon set, or a different meaning of “Sidon”? 
2. Infinite set, compatible finite prefixes, or an isolated finite set?
3. `g=1`, or only bounded representation with `g>1`?
4. Liminf or limsup?
5. Infinitely many scales or all sufficiently large scales?
6. The same normalization as #1191?
7. A theorem, conjecture, heuristic, review, or semantic summary?
8. Full text checked, or metadata only?
9. Does it resolve, strengthen, merely reprove, or not affect Q1/Q2?
10. Does it contain a mechanism relevant to endpoint imbalance, all offsets, multiscale covariance, martingales, entropy, or compatible construction?

## Tool-specific cautions

### zbMATH Open / MathSciNet

Use authoritative bibliographic metadata and expert reviews, but do not infer absence from a failed public search. Record subscription or indexing limits.

### arXiv

Record the exact version and date. Search the abstract page and source/PDF. A superseded title or earlier version may have weaker constants or missing discussion.

### MathOverflow

Treat posts as expert discussion, not peer-reviewed proof. Follow cited papers.

### SciSpace / Consensus / Exa

Use for discovery. Check every formula and metadata field. Semantic tools may conflate harmonic-analytic, multiplicative, finite-field, or generalized Sidon notions.

### Firecrawl

Use:

- `search` when the URL is unknown;
- research-paper search for abstract discovery;
- `scrape` for a known page requiring clean extraction;
- map/crawl only when the relevant section spans several pages;
- feedback when results are empty or miss obvious primary sources.

### PDFs

Prefer native text. If formula extraction is corrupted, inspect rendered pages. OCR is a fallback, not the default.

## Ledger format

Every search entry in `core_workspace/literature_ledger.md` should include:

- date/time and timezone;
- tool/database;
- exact query;
- result URL/title;
- source type and version;
- full text checked: yes/no;
- relevance to Q1, Q2, endpoint theorem, or novelty audit;
- disposition: used / background / rejected false positive / inaccessible / quota-limited;
- verification notes.
