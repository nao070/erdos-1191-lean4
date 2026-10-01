# Search Tool Log — 2026-08-28

This log records the handoff literature search. It is not a substitute for the canonical `core_workspace/literature_ledger.md`, which should be extended in later sessions.

## Consensus

**Query:** `infinite additive Sidon sequence density counting function liminf sqrt(log x / x) Ruzsa Cilleruelo O'Bryant year:1990-2026`

**Outcome:** quota error; all 30 monthly searches had been used, with reset stated for 2026-09-01. No search results were available.  
**Disposition:** quota-limited; no evidence used.

## SciSpace

### Query 1

`Which papers establish the strongest known density bounds and constructions for infinite additive Sidon sequences, especially results concerning whether liminf A(x) sqrt(log x/x) is zero, whether a_n can be O(n^2 polylog n), and whether multiscale, Fourier-uniformity, discrepancy, martingale, or entropy methods have been applied?`

**Outcome:** broad semantic results, many adjacent/generalized papers.  
**Disposition:** discovery only.

### Query 2

`Find and summarize papers directly relevant to Erdős Problem #1191 on infinite additive Sidon sequences, especially Kevin O'Bryant's 2026 papers, Javier Cilleruelo's Infinite Sidon sequences, Ruzsa's dense infinite Sidon construction, and finite Sidon residue/Fourier-uniformity results that could support a multiscale endpoint-imbalance argument. Exclude harmonic-analysis Sidon sets and multiplicative Sidon sets.`

**Useful surfaced paper:** Javier Cilleruelo, `Infinite Sidon sequences`, arXiv:1209.0326. Also surfaced Maldonado’s account of Ruzsa’s construction.  
**Limitation:** did not surface the newest O’Bryant papers in the returned set.  
**Disposition:** discovery only; primary sources checked separately.

## Exa

### Search query

A semantically rich request for primary/current sources on Erdős #1191, the exact problem statement, Ruzsa/Cilleruelo constructions, O’Bryant 2026, and multiscale/Fourier/discrepancy/entropy methods.

**Useful results:**

- Erdős Problems #1191 page;
- O’Bryant arXiv:2606.28651;
- O’Bryant arXiv:2607.23795;
- Ding arXiv:2606.15041;
- Táfula arXiv:2607.20753;
- Ortega–Prendiville on Numdam;
- Cilleruelo arXiv:1209.0326.

### Fetch batch

Fetched full content/metadata for:

- https://www.erdosproblems.com/1191
- https://arxiv.org/abs/2606.28651
- https://arxiv.org/abs/2607.23795
- https://arxiv.org/abs/2606.15041
- https://arxiv.org/abs/2607.20753
- https://numdam.org/articles/10.5802/jtnb.1239/
- https://arxiv.org/abs/1209.0326

**Limitation:** some Exa-parsed metadata and titles were imperfect.  
**Disposition:** page discovery and extraction; official pages override parsed metadata.

## Firecrawl ordinary search

### Exact research-category query

`"Erdős Problem #1191" infinite Sidon set liminf sqrt log x 2026`

**Outcome:** zero results.  
**Feedback:** submitted as bad, noting the missing exact problem page and primary papers.

### Broader ordinary query

`"Erdős Problem #1191" OR ("infinite Sidon" "log x" liminf)`

**Useful results:** Táfula arXiv:2607.20753, Cilleruelo-related metadata, historical Erdős material.  
**Missing:** exact #1191 page and O’Bryant I/II.  
**Feedback:** submitted as partial.

### Endpoint-analogue query

`("H^{-1}" OR "negative Sobolev") cyclic graph divergence endpoint imbalance interval discrepancy Eulerian residue graph additive combinatorics`

**Outcome:** zero results.  
**Feedback:** submitted as bad.

## Firecrawl research-paper index

**Query:** infinite additive Sidon sequence density, #1191-equivalent liminf, O’Bryant thickness papers, Ruzsa construction, endpoint/residue/discrepancy methods; categories `math.NT`, `math.CO`; date range 1990-01-01 through 2026-08-28.

**Useful returned records:**

- arXiv:1209.0326 — Cilleruelo;
- arXiv:2606.28651 — O’Bryant I;
- arXiv:2607.23795 — O’Bryant II;
- arXiv:2607.20753 — Táfula;
- arXiv:1103.5732 — Maldonado;
- arXiv:2608.07416 — recent delta-separated finite Sidon work;
- several generalized/adjacent papers.

**Disposition:** useful discovery index; theorem statements verified on primary pages.

## Ordinary web / arXiv

Opened and checked official arXiv abstract/HTML pages for O’Bryant I/II, Táfula, Ding, and Cilleruelo. The O’Bryant Part I discussion was searched for references to:

- averaging over values of `N`;
- reverse martingales;
- entropy;
- all offsets;
- further problems and fine distribution.

These passages motivated the anti-Eulerian multiscale target.

## Site-restricted specialist searches

Queries were run against:

- zbMATH Open;
- MathSciNet;
- EuDML;
- MathOverflow;
- Numdam;
- Project Euclid;
- Math-Net.Ru.

**Outcome:**

- Numdam directly returned Ortega–Prendiville.
- EuDML and Math-Net.Ru returned many false positives from harmonic analysis, compact groups, dynamics, or generalized uses of Sidon.
- MathOverflow results were adjacent but did not provide a direct #1191 resolution.
- Public web indexing did not expose reliable exact MathSciNet/zbMATH pages for the newest preprints.
- No specialist-site negative result was used to infer nonexistence.

## File-library search

Searched conversation and library files for a complete older `erdos1191-research` workspace, `computation/crossblock.py`, and related ZIPs. The search located older prompt/report exports but not a complete workspace containing the referenced computation code and raw data.

**Disposition:** legacy computation artifacts remain missing; see `MISSING_REFERENCED_ARTIFACTS.md`.

---

## Continuation search — anti-Eulerian / quartic phase

The continuation used a second, independent search wave.  The natural-language
payloads are grouped below exactly by submitted research topic; result counts
are counts reviewed, not counts of relevant papers.

### Consensus retry

**Query topic:** infinite additive Sidon sets; Erdős #1191; density near
`sqrt(x/log x)`; strongest theorem or resolution.

**Outcome:** failed before returning evidence because all 30 monthly searches
were used; reset date reported as 2026-09-01.  No retry loop and no inference.

### SciSpace (three searches, ten returned abstracts each)

1. Infinite additive Sidon density near `sqrt(x/log x)` and the current
   #1191 frontier.
2. Interval/circle-arc coverage variance, endpoint measures, inverse cycle
   Laplacians, and negative Sobolev (`H^-1`) norms.
3. Homometric Golomb rulers and equal-distance-spectrum pairs.

**Outcome:** 30 abstracts reviewed.  Results were predominantly older or
adjacent; none was used without a primary-source check.

### Firecrawl research-paper index (four searches, `k=12` each)

1. Infinite additive Sidon sequence density, Erdős #1191, O’Bryant, Ruzsa,
   Cilleruelo, Táfula.
2. Interval/circle arc coverage variance, endpoint imbalance, and `H^-1`.
3. Cycle-graph divergence, Eulerian flow, inverse Laplacian, and negative
   Sobolev norms.
4. Homometric sets, Golomb rulers, endpoint incidence, and variance.

**Outcome:** O’Bryant I/II, Cilleruelo, Táfula, and adjacent records were
found.  The O’Bryant index metadata did not reliably match official arXiv v3;
the indexed paper body and official page were checked instead.

### Firecrawl known-paper inspection and related records

- Inspected O’Bryant I under canonical research-index id
  `590804915137747311` and checked its section 3.1 discussion.
- Queried citations, references, and similar papers from that record and from
  a mixed seed.  Citation/reference outputs were empty or uninformative;
  similar results were adjacent finite papers.

### Firecrawl ordinary searches

1. Exact endpoint-reconstruction / cyclic-arc covariance formula.
2. `H^-1` or negative-Sobolev endpoint imbalance together with Sidon sets.
3. Exact O’Bryant title/arXiv id `2606.28651v3`.
4. Exact wording of Erdős Problem #1191.

The exact O’Bryant search found the primary record.  Searches 1 and 2 were
empty; search 4 missed the official page and returned secondary sites.  Search
quality feedback was submitted where the feedback window remained open.

### Firecrawl public specialist-site searches

The infinite-Sidon, endpoint/cycle, and homometric queries were restricted in
turn to zbMATH, MathSciNet, MathOverflow, EuDML, Numdam, Project Euclid, and
Math-Net.Ru.  Public zbMATH/MathSciNet indexing returned nothing usable;
MathOverflow returned one adjacent discussion; most other hits concerned
Costas arrays, harmonic-analysis Sidon sets, or unrelated topics.  These are
access/index failures, not negative mathematical evidence.

### Exa (ten workstreams; 102 returned records reviewed)

1. Current official status and possible 2026 resolution of Erdős #1191.
2. O’Bryant Part I v3, theorem constant, and multiscale suggestions.
3. Current strongest infinite additive Sidon density bounds/constructions.
4. Exact cyclic-arc covariance and endpoint-reconstruction analogues.
5. Cycle Green functions, effective resistance, graph divergence, and
   negative Sobolev norms for interval indicators.
6. Homometric Golomb rulers and endpoint-sensitive invariants.
7. Bekir--Golomb 2007 and Piccard counterexample classification.
8. Martingale/entropy/multiscale methods for Sidon sequences.
9. Ortega--Prendiville, Ding, finite Sidon Fourier uniformity, and its exact
   applicability hypotheses.
10. Recent combinatorial large-sieve methods, including arXiv:2606.17487.

Primary fetches included the official #1191 page, O’Bryant v3 HTML,
arXiv:2608.13739, and the principal known frontier papers.  The Bekir--Golomb
DOI endpoint returned HTTP 406.  Duplicate, harmonic-analysis, multiplicative,
and generalized-`B_h[g]` false positives were rejected.

### Disposition

No checked source stated a complete resolution of either question.  This is a
dated public-literature observation only.  Direct subscription-grade
MathSciNet/zbMATH coverage and an expert novelty audit remain open.

<!-- WAVE 6 ARITHMETIC-BANDS SEARCH LOG START -->

## Wave 6 continuation — arithmetic bands and forbidden shadows

**Date:** 2026-08-28

### Record-provenance limitation

This section records already-run Firecrawl, Exa, and SciSpace searches. The
exact raw payloads and returned-record counts did not survive session
compaction. The wording below is reconstructed, near-exact topic wording from
the retained notes; it is not a verbatim transcript. Every count is therefore
reported as **unavailable**, and no count was reconstructed from memory.

### Reconstructed search families

#### Family 1 — disjoint difference packings

**Grouped topic wording:** “disjoint difference sets / difference triangle
sets / nested Golomb rulers / distinct contiguous sums”

**Tools used:** Firecrawl, Exa, SciSpace.  
**Returned-record count:** unavailable.

**Retained outcome:** Ma--Yi and disjoint-Golomb-ruler adjacency. The checked
sources concern pairwise-disjoint internal spectra of separate rulers or
disjoint mark sets. They do not control all differences between marks from
different component rulers, so taking a union need not produce a Golomb
ruler.

#### Family 2 — one-point forbidden shadows

**Grouped topic wording:** “A+A-A / forbidden next points / maximal Sidon
sets / one-point extension shadow”

**Tools used:** Firecrawl, Exa, SciSpace.  
**Returned-record count:** unavailable.

**Retained outcome:** finite Sidon sumset/distribution, maximality, and
extension-adjacent material. No primary candidate retained from this bounded
pass states a uniform density estimate for A+Delta^+(A) in the extension band
x > diam(A) under a compatible all-prefix critical envelope. Empty or
adjacent retrieval is not used as evidence that no such theorem exists.

#### Family 3 — Singer and finite-field nesting

**Grouped topic wording:** “nested Singer difference sets / finite-field
extensions / compatible Sidon rulers / projective norm graph”

**Tools used:** Firecrawl, Exa, SciSpace.  
**Returned-record count:** unavailable.

**Retained outcome:** Singer/norm-graph, subdifference-set, and nested-design
adjacency. The primary records checked below do not give compatible ordered
integer embeddings across sizes, nor uniqueness of every mixed difference in
one growing ruler.

### Consensus

The corresponding Consensus search could not return evidence because the
monthly quota was exhausted: **30/30 searches used**, with reset reported for
**2026-09-01**. No retry result is claimed and no negative inference is made.

### Primary-source validation

1. [Ma--Yi, arXiv:2608.13739v1](https://arxiv.org/html/2608.13739v1):
   official HTML checked. The definition of P_t(U) uses pairwise-disjoint
   internal positive-difference sets of separate t-mark rulers. Theorem 1.1
   states P_t(U)=U-o(U) exactly for 3 <= t <= 5. Mixed cross-ruler differences
   are outside the definition.
2. [Alexeev--Mixon, arXiv:2510.19804v2](https://arxiv.org/html/2510.19804v2):
   official HTML checked. Theorem 9 is a finite cyclic non-extension result.
   Claim 10 says every finite Sidon set extends to some infinite perfect
   difference set. It supplies no quantitative coordinate, density,
   displacement, cumulative-cost, or compatible ordered-prefix estimate.
3. [Mészáros--Rónyai--Szabó, arXiv:1908.05591](https://arxiv.org/abs/1908.05591):
   official arXiv record checked. The abstract gives a norm-one description
   of Singer difference sets and a projective norm-graph application, not a
   compatible integer-ruler tower.
4. [Momihara--Xiang, arXiv:1706.05460](https://arxiv.org/abs/1706.05460):
   official arXiv record checked. The abstract constructs strongly regular
   Cayley graphs over finite-field additive groups from Singer subdifference
   partitions, not nested integer Sidon prefixes.
5. [Xu--Xiu--Fan--Liang, arXiv:2409.14409v1](https://arxiv.org/abs/2409.14409):
   official arXiv record checked. “Disjoint” concerns the component mark sets;
   the definition does not assert that their union is a Golomb ruler.

### Wave 6 disposition

No checked source in this bounded delta supplies either:

- a compatible all-prefix O(n² polylog n) integer Sidon tower; or
- an o(log J) innovation, arithmetic-band, forbidden-shadow, or reset-renewal
  theorem for a single globally compatible sequence.

This is a qualified null, not an exhaustive literature search, an absence
theorem, or a novelty claim. See
research_sources/LITERATURE_DELTA_WAVE6_ARITHMETIC_BANDS_2026-08-28.md for the
full source-by-source boundary.

<!-- WAVE 6 ARITHMETIC-BANDS SEARCH LOG END -->
