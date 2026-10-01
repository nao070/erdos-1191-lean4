# Wave 9 P15 targeted literature-search log

Cutoff: **2026-08-29**. This is a delta from the 550-record
`research_sources/wave8_literature_state/research_state.json`; it does not
restart discovery. The hard screen was whether a primary theorem controls, on
one nested infinite additive Sidon/Golomb branch, the exact P15 birth weights

\[
N_{2m}^{-2}h_i h_j\Phi_{ij}
\]

with bounded overlap in both difference magnitude and rank lag. Results about
harmonic-analysis Sidon sets were excluded unless they also contained a theorem
about distinct integer differences.

## 1. State lineage and accounting

- Wave 8 input: 550 papers and 22 logged queries.
- Eight new scripted rounds first enlarged the corpus to 747 raw records.
- Idempotent deduplication reduced 747 to 742 records: five duplicate clusters,
  including four arXiv/publisher bridges.
- A primary-full-text batch then added eight manually verified papers that the
  broad indexes had missed, producing the present **750-paper, 31-query** state.
- All 750 papers were reranked for P15 with
  `alpha=0.65`, `beta=0.15`, `gamma=0.10`, `delta=0.10` and five-year recency
  half-life. The lexical ranker remained noisy, so theorem screening, not rank,
  determines the audit.
- The schema-protected top-level `question` remains the inherited Wave 8/P13
  lineage text. The ranking command used an explicit P15 question override, and
  the two Wave 9 reports state the P15 target. The JSON was not edited directly
  merely to relabel its ancestry.
- The state deliberately remains in phase 1. Overall mechanical saturation is
  false.

SHA-256 provenance at completion:

```text
7b25611de3dcbf30c7c34497f6481852931fa43957609edccbc1b8f7e23717dc  wave8 research_state.json
4486eec7e881def19815168ac7d572a250f4e5797f73957c930509716f62dc40  wave9 research_state.json before final critique append
a25710988602436870a86e7640b6b590248caa99a3fcf2a12b45d86c78c90183  wave9 research_state.json after final critique append
a9252f24c07454e95a9f3201c4fa9ee9a8876d07c0b1564214ed963ca84a176c  primary_verified_ingest.json
```

The intermediate Wave 9 hash makes the ranking/ingest checkpoint recoverable;
the final hash includes the self-critique and independent-plugin audit. The Wave
8 and ingest-manifest hashes are stable lineage checks.

## 2. Scripted delta rounds

The `scholar-deep-research` scripts were run with the required interpreter
`/Users/USER/miniforge3/bin/python3`. Exact state entries follow.

| # | Source | Exact query | Round | Hits | New | Merged |
|---:|---|---|---:|---:|---:|---:|
| 23 | OpenAlex | `infinite Sidon sequence density every prefix nested construction` | 8 | 1 | 1 | 0 |
| 24 | Crossref | `distinct consecutive sums infinite sequence weighted interval packing` | 8 | 50 | 49 | 1 |
| 25 | arXiv | `infinite Sidon sequence density all prefixes` | 9 | 50 | 16 | 34 |
| 26 | arXiv | `Sidon sequence local distribution intervals` | 10 | 50 | 12 | 38 |
| 27 | Crossref | `Sidon sequence local density short intervals difference distribution` | 9 | 50 | 45 | 5 |
| 28 | OpenAlex | `Sidon sequence local density short intervals difference distribution` | 9 | 50 | 43 | 7 |
| 29 | OpenAlex | `weighted ordered difference energy Golomb ruler multiscale packing` | 10 | 0 | 0 | 0 |
| 30 | Crossref | `weighted ordered difference energy Golomb ruler multiscale packing` | 10 | 50 | 31 | 19 |
| 31 | primary full text | `Wave9 targeted primary-source verification: nested infinite Sidon prefixes; ordered differences; Golomb-ruler packing; local density; extension mechanisms` | 1 | 8 | 8 | 0 |

The last row is a reproducible ingest manifest,
`primary_verified_ingest.json`, not an assertion that a database returned those
eight records in one search.

## 3. Saturation and hard limits

The final state reports:

| Source | Rounds | Last hits/new | Axes passed | Mechanical status | Qualification |
|---|---:|---:|---:|---|---|
| OpenAlex | 10 | 0/0 | 4/4 | saturated | The exact weighted query returned no records. |
| arXiv | 10 | 50/12 | 4/4 | saturated | New fraction 24%; still broad lexical drift. |
| Crossref | 10 | 50/31 | 2/4 | **not saturated** | Hard ten-round cap reached while 62% of the last page was new and mostly off-topic. |
| primary full text | 1 | 8/8 | 1/4 | **not saturated** | Curated verification lane, not designed to satisfy a discovery gate. |

Thus the overall status is **not saturated**. The negative result is a qualified
null for the logged clusters, full-text checks, and citation trails. It is not a
claim that all mathematical literature has been exhausted. Repeating broad
Crossref queries to force a formal gate would have added lexical noise rather
than evidence and was not done.

## 4. Exa workstreams

Four semantic workstreams were run at 12 results each. A compact rerun at eight
results each was needed because the combined first response was truncated. Under
the plugin's counting rule, this is **80 reviewed result slots** across four
workstreams:

1. infinite Sidon sequences with nested/all-prefix density;
2. weighted ordered-difference energy and Golomb packing across scales;
3. local density of Sidon sets in intervals or unions of intervals;
4. prescribed-prefix extension, maximality, and extension trees.

High-signal leads were Ma--Yi, Shearer, Riblet, Cilleruelo, O'Bryant, Ruzsa, and
Kohayakawa--Lee--Moreira--Rodl. Exa full-text retrieval successfully exposed
Shearer's official EJC paper and an institutional open copy of the SIAM paper.
The SIAM publisher page itself returned a crawler error, so theorem text was
checked in the institutional copy bearing the journal pagination and DOI.

## 5. Firecrawl research index

Four paper searches with `k=15` and date ceiling 2026-08-29 produced **60 result
slots** for the same four mathematical axes. Five primary candidates were sent to
the paper reader. Ma--Yi's theorem and proof were returned cleanly; some combined
long responses for O'Bryant, Riblet, and the large-sieve paper were interleaved or
truncated, so no load-bearing formula was accepted from that output alone.
Relevant formulas were rechecked in arXiv HTML, publisher text, or downloaded
primary PDFs. The related-paper expansion for arXiv:2608.13739 returned a pool of
size zero.

## 6. Consensus and SciSpace

- One Consensus query returned the exact account-level limit: all 30 searches
  had been used, with reset on 2026-09-01. No theorem claim rests on Consensus.
- One SciSpace query returned ten papers. `k-fold Sidon sets` and `Gaps in Dense
  Sidon Sets` were useful neighbors; the remainder was largely generic or
  computational. SciSpace was used only for discovery. A Zenodo computational
  item labelled as work on an Erdos problem was excluded from theorem evidence.

Quota and retrieval failures are logged limitations, not mathematical evidence.

## 7. Parallel main-agent plugin audit

The main research agent independently repeated the plugin screen on 2026-08-29.
These counts are recorded separately because the workstreams overlap and should
not be presented as unique papers.

- **Exa:** three workstreams at ten results each, or **30 reviewed slots**:
  infinite Sidon density, DTS/rank-lag packing, and nested compatible critical
  rulers. Ma--Yi and O'Bryant were the only strong P15-adjacent hits; the rest
  were adjacent or irrelevant. Exa fetch reverified the official arXiv pages and
  Shearer's EJC page.
- **Firecrawl research index:** three semantic queries requested `k=15` each but
  returned zero search results. Direct inspect/read by known identifier did work.
  Ma--Yi resolved as canonical ID `6133858862546596750` (created 2026-08-13,
  updated 2026-08-17), and the returned passage reproduced the Theorem 4.1 proof.
  O'Bryant resolved as ID `590804915137747311` (updated 2026-07-28). Search
  emptiness was not treated as evidence of absence.
- **Consensus:** two searches both failed at the monthly 30-search quota, with
  reset on 2026-09-01.
- **SciSpace:** two full-question searches returned ten results each. The 20
  results were mostly older or adjacent and contained no P15 theorem. Semantic
  summaries were treated only as leads.

Across both independent plugin passes, the activity totals are **110 Exa reviewed
slots**, **60 returned Firecrawl search slots plus 45 requested-but-empty slots**,
**three quota-blocked Consensus searches**, and **30 SciSpace result slots**.
Because of overlap, truncation, quota failures, and empty semantic searches,
these totals describe audit effort, not independent evidence or saturation. The
independent pass converged on the same qualified null and the same two strongest
2026 interfaces, Ma--Yi and O'Bryant.

## 8. Primary sources actually checked

- Ma and Yi, [*An Almost-Covering Threshold for Golomb-Ruler Difference Packings*](https://arxiv.org/html/2608.13739), arXiv:2608.13739v1.
- Shearer, [*Improved LP Lower Bounds for Difference Triangle Sets*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v6i1r31), DOI `10.37236/1463`; official PDF text was also fetched.
- O'Bryant, [*On the Thickness of Infinite Generalized Sidon Sets, I*](https://arxiv.org/html/2606.28651v3), arXiv:2606.28651v3.
- Kohayakawa, Lee, Moreira, and Rodl, [*Infinite Sidon Sets Contained in Sparse Random Sets of Integers*](https://doi.org/10.1137/17M1114934), DOI `10.1137/17M1114934`; theorem text checked in the [institutional journal copy](https://repositorio.usp.br/bitstreams/ba7fd00d-e405-4f8a-99df-a8224edecfce).
- Riblet, [*Sidon Sets in a Union of Intervals*](https://arxiv.org/abs/2202.01296), DOI `10.1007/s10474-022-01246-x`; primary PDF checked locally.
- Cilleruelo, [*Gaps in Dense Sidon Sets*](https://emis.muni.cz/journals/INTEGERS/papers/a11/a11.pdf), INTEGERS 0 (2000), A11.
- Croot, Mao, Pohoata, Sheffer, and Yip, [*A Combinatorial Large Sieve for Sidon Sets, Distances, and Norm Forms*](https://arxiv.org/abs/2606.17487), arXiv:2606.17487v2.
- Nathanson, [*Sidon Sets with Delta-Separated Sumsets in Additive Number Theory*](https://arxiv.org/abs/2608.07416), arXiv:2608.07416v2.

Previously verified Wave 8 sources on maximal Sidon sets, greedy continuation,
conflict hypergraphs, and tree flows remain in scope by reference and were not
needlessly re-fetched.

## 9. False positives and exclusions

The high new-record counts were not high mathematical yield. Representative
exclusions were:

- harmonic-analysis Sidon sets in groups, orthonormal systems, and interpolation;
- Fefferman--Stein/Carleson-operator papers using “Carleson” with no integer
  difference-packing theorem;
- signal-processing Golomb rulers, optical channel allocation, FPGA searches,
  and heuristic optimization;
- ordered weighted averaging, fuzzy-set extensions, energy systems, and
  multiscale image filters retrieved by the literal words “weighted”,
  “difference”, and “energy”;
- finite-field, cyclic-design, and cryptographic Sidon sets without an embedding
  that preserves the P15 nested prefix and weights;
- arXiv:2604.25214, whose own abstract calls the proposed dilation family
  apparent and leaves a complete proof open;
- Nathanson's globally Delta-separated pair-sum problem, which does not control
  contiguous-sum birth weights;
- the Croot et al. large sieve, whose Sidon theorem is for the algebraically
  structured set of squares, not an arbitrary integer branch.

The automatic top ranks included unrelated TOPSIS, stock-market, signal-filter,
and soccer-packing papers. The ranking is therefore retained only as provenance.

## 10. Reproduction

From the handoff root:

```text
PY=/Users/USER/miniforge3/bin/python3
SCRIPTS=/Users/USER/.agents/skills/scholar-deep-research/scripts
STATE=research_sources/wave9_literature_state/research_state.json

$PY $SCRIPTS/research_state.py --state "$STATE" status
$PY $SCRIPTS/research_state.py --state "$STATE" saturation
$PY $SCRIPTS/research_state.py --state "$STATE" query queries
jq '.papers | length, .queries | length' "$STATE"
```

The theorem-screened conclusion and the exact new P15 interface are in
`PRIMARY_SOURCE_AUDIT.md`.
