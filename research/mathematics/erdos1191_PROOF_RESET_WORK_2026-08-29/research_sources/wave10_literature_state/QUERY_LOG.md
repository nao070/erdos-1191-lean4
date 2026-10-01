# Wave 10 laminar-weighted literature query log

Cutoff: **2026-08-29**.  This is a targeted delta from the 750-paper,
31-query Wave 9 state.  It does not restart discovery.  The parent state is
`research_sources/wave9_literature_state/research_state.json`, SHA-256
`a25710988602436870a86e7640b6b590248caa99a3fcf2a12b45d86c78c90183`.

## 1. Hard screen

The screen was whether a theorem applies simultaneously to:

1. one fixed nested infinite Golomb/Sidon branch;
2. varying incomplete birth triangles rather than fixed complete rulers;
3. arbitrary hereditary epoch or laminar-box restrictions;
4. the endpoint product `h_i h_j` and the exact kernel `Phi_ij`;
5. cross-epoch survival at `N_(2m)=O(m^2 log m)`.

A paper matching only the words *weighted*, *rank*, *energy*, or *Carleson*
was not accepted without this interface check.

## 2. Exact activity accounting

### Exa

Ten search calls reviewed **100 result slots**:

| Calls | Results/call | Exact semantic target |
|---:|---:|---|
| 2 | 12, 8 | `category:research paper incomplete difference triangle sets nested prefixes weighted inequalities distinct differences hereditary subsets Golomb rulers` |
| 2 | 12, 8 | `category:research paper distinct consecutive interval sums positive sequences weighted product inequalities additive energy unique contiguous sums` |
| 2 | 12, 8 | `category:research paper laminar family Carleson embedding weighted tree energy product kernel testing theorem sparse domination intervals` |
| 2 | 12, 8 | `category:research paper weighted Sidon inequalities hereditary subsets local additive energy ordered differences rank lag` |
| 1 | 10 | `category:research paper positive integer sequences all contiguous interval sums distinct weighted inequalities Golomb ruler gap sequence` |
| 1 | 10 | `category:research paper four parameter Carleson embedding 4-tree tensor product weights box condition Hardy operator 2021 2022 2023 2024 2025 2026` |

The first four 12-result calls were rerun at eight results so that titles and
URLs could be extracted without truncation.  Under the Exa skill's accounting
rule both passes count.  Five fetch calls requested 16 pages, representing 11
unique URLs.  The exact-theorem pages were then checked against official arXiv
metadata or HTML.

One useful data-quality correction resulted.  An Exa fetch labelled
arXiv:2606.15041 as *Power and rank-weighted sums in dense finite Sidon sets*.
The current official arXiv title is *Dense finite Sidon sets on arithmetic
progressions*.  Its Theorem 4 really does contain rank-and-power weights, so
the mathematics was retained but the title and version were corrected from the
official page.

### Firecrawl research index

Five paper-search calls with `k=15` and ceiling `2026-08-29` returned **75
result slots**:

1. `incomplete difference triangle sets nested prefixes weighted inequalities distinct positive differences hereditary subsets Golomb ruler`;
2. `distinct contiguous interval sums positive sequences weighted product endpoint gaps additive energy`;
3. `laminar families weighted Carleson embedding tree product kernel energy testing condition`;
4. `weighted Sidon inequalities rank weighted sums local additive energy hereditary subset constraints`;
5. `four parameter Carleson embedding 4-tree tensor product weights box condition Hardy operator`.

Two related-paper expansions requested `k=15`:

- Ma--Yi `arxiv:2608.13739`, `mode=references`: pool size zero;
- product-weight Carleson `arxiv:1906.11150`, `mode=similar`: pool size 15.

Thus related expansion returned **15 slots**, with **15 requested-but-empty
slots** recorded separately.  Four `inspect_paper` calls fixed canonical IDs and
dates; four `read_paper` calls checked load-bearing theorem passages.

Canonical Firecrawl identifiers:

| arXiv | Firecrawl ID | Created / updated |
|---|---:|---|
| `2606.15041` | `5093957689421454240` | 2026-06-13 / 2026-06-25 |
| `1906.11150` | `7794511930129020075` | 2019-06-26 / 2020-08-18 |
| `2001.02373` | `6331809077363100399` | 2020-01-08 / 2020-08-18 |
| `1903.02478` | `2307604969172512041` | 2019-03-06 / 2019-03-20 |

### Consensus

Two exact searches were attempted:

1. `weighted incomplete difference triangle sets nested Golomb rulers rank lag year:1990-2026`;
2. `laminar Carleson embedding weighted Sidon additive energy interval sums year:1990-2026`.

Both returned the same account-level failure: all 30 monthly searches had been
used, with reset on **2026-09-01**.  No theorem claim rests on Consensus.

### SciSpace

Three full-question searches returned ten items each, **30 result slots**:

1. `Which theorems give weighted inequalities for incomplete or nested difference triangle sets and Golomb rulers with distinct differences?`
2. `Which Carleson embedding theorems for laminar trees control product-weighted energies, and what testing assumptions do they require?`
3. `Which additive-combinatorics results control rank-weighted or hereditary-subset energies of finite Sidon sets?`

The useful leads were the product-weight bi-tree theorem, the restricted-energy
bi-tree theorem, and Ding's dense finite Sidon work.  SciSpace was discovery
only.  Generic weighted inequalities, engineering ruler searches, and
unreviewed Zenodo computations were excluded from theorem evidence.

## 3. Primary-source verification

The following official pages carried the load-bearing checks:

- Ding, [*Dense finite Sidon sets on arithmetic progressions*, Theorem 4](https://arxiv.org/html/2606.15041v2#Thmtheorem4).
- Arcozzi--Mozolyako--Psaromiligkos--Volberg--Zorin-Kranich,
  [*Bi-parameter Carleson embeddings with product weights*, Theorem 2.3](https://arxiv.org/html/1906.11150#S2.Thmtheorem3).
- Mozolyako--Psaromiligkos--Volberg--Zorin-Kranich,
  [*Carleson embedding on tri-tree and on tri-disc*, Theorem 1.3](https://arxiv.org/html/2001.02373#S1.Thmtheorem3).
- Holmes--Psaromiligkos--Volberg,
  [*A comparison of box and Carleson conditions on bi-trees*, Theorem 1.11](https://arxiv.org/html/1903.02478).
- Mozolyako--Psaromiligkos--Volberg,
  [*Multi-parameter Carleson embeddings ... on T^4, and why the proofs fail*](https://arxiv.org/abs/2108.04789).
- Mozolyako--Volberg,
  [*Differences between the potential theories on a tree and on a bi-tree*](https://arxiv.org/abs/2109.00021).

The current arXiv abstract and HTML independently confirmed the title, version,
and formulas of arXiv:2606.15041v2.  Official metadata also showed that the
apparently newer arXiv:2603.25137 concerns matrix-weighted
Besov--Triebel--Lizorkin spaces, not a four-tree one-box theorem.

## 4. False positives and exclusions

- Fixed complete DTS constructions and FPGA searches do not give hereditary
  weighted inequalities for a changing birth triangle.
- Ding's Theorem 4 controls `sum i^s a_i^ell`; it neither controls adjacent-gap
  products nor survives the P15 density loss.  At
  `N_(2m)=O(m^2 log m)`, the ratio `2m/sqrt(N_(2m))` may tend to zero, so its
  Fourier-uniformity error is not a small term.
- The 2026 asymmetric-energy inequality is a mixed Hölder inequality.  It has
  no distinct-difference, rank-lag, or survival gain.
- Arbitrary-set Sidon-subset extraction theorems are orthogonal to a branch
  whose prefixes are already Sidon.
- Consecutive-sum papers found by the query concern representing integers by
  sums of consecutive terms, not uniqueness of every contiguous gap sum.
- Matrix-weighted and analytic-function-space Carleson papers were retained
  only when they contained an explicit finite-tree theorem; the rest were
  excluded as vocabulary matches.

## 5. Saturation qualification

The exact four-tree follow-up converged across Exa and Firecrawl on the
published bi-/tri-tree theorems and the 2021 T^4 obstruction papers.  No later
paper through 2026-08-29 was found that supplies the needed four-parameter
one-box theorem or a Sidon-specific substitute.

This is **targeted convergence, not overall saturation**.  Consensus was quota
blocked, SciSpace was discovery-only, and semantic indexes cannot prove
absence.  The correct conclusion is therefore a qualified null for the logged
interfaces, not a claim that all mathematical literature is exhausted.

## 6. Reproduction and state

The machine-readable exact query list, counts, candidate dispositions, and
lineage are in `research_state.json`.  The theorem comparison and the new
conditional interface are in `PRIMARY_SOURCE_AUDIT.md`.  File hashes are in
`HASHES.sha256`.
