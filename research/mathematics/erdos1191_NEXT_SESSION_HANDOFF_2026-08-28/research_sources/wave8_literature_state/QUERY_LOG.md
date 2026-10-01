# Wave 8 targeted literature-search log

Cutoff: **2026-08-28**. This is a delta search from
`research_sources/wave7_literature_state/`; it does not restart Wave 7. The hard
screen was whether a result preserves a prescribed integer Sidon/Golomb prefix,
controls old--new as well as new--new differences, produces a quantitative weight
on the infinite-survival extension tree, or contains the signed ordered-difference
covariance needed by P13.

## 1. Local scripted discovery

The `scholar-deep-research` OpenAlex/Crossref/arXiv scripts used the required
Python interpreter `/Users/USER/miniforge3/bin/python3`. Four mathematical
keyword clusters were separated:

1. online/extendable Sidon and prescribed-prefix completion;
2. maximality, saturation, greedy growth, and coordinate bounds;
3. mixed-difference conflict hypergraphs, random greedy, and nibble theorems;
4. survival trees, branching flows, Kraft/Carleson budgets, and ordered-difference
   energy/covariance.

The state contains the following rounds. Broad queries were intentionally retained
as provenance even when they drifted into unrelated uses of “Sidon”, “ruler”,
“extension”, or “Carleson”.

| # | Source | Exact query | Round | Hits | New | Merged |
|---:|---|---|---:|---:|---:|---:|
| 1 | OpenAlex | `prescribed prefix Sidon sequence quantitative extension bound` | 1 | 0 | 0 | 0 |
| 2 | Crossref | `maximal Sidon set saturation extension interval` | 1 | 50 | 50 | 0 |
| 3 | arXiv | `random greedy Sidon set` | 1 | 50 | 49 | 1 |
| 4 | arXiv | `maximal Sidon set` | 2 | 50 | 12 | 38 |
| 5 | OpenAlex | `Sidon set hypergraph matching nibble prescribed vertices mixed differences` | 2 | 0 | 0 | 0 |
| 6 | Crossref | `Golomb ruler extension prescribed marks` | 2 | 50 | 50 | 0 |
| 7 | arXiv | `Sidon set process` | 3 | 50 | 4 | 46 |
| 8 | Crossref | `Sidon Fourier correlation ordered differences interval` | 3 | 50 | 46 | 4 |
| 9 | OpenAlex | `ordered pair differences covariance additive energy Sidon set` | 3 | 3 | 3 | 0 |
| 10 | arXiv | `greedy Sidon sequence` | 4 | 50 | 19 | 31 |
| 11 | OpenAlex | `greedy Sidon sequence extension gaps quantitative upper bound` | 4 | 8 | 8 | 0 |
| 12 | Crossref | `greedy Sidon sequence upper bound` | 4 | 50 | 41 | 9 |
| 13 | arXiv | `Sidon sequence additive energy` | 5 | 50 | 26 | 24 |
| 14 | Crossref | `random greedy Sidon set process hypergraph` | 5 | 50 | 38 | 12 |
| 15 | OpenAlex | `random greedy independent set Sidon hypergraph process` | 5 | 38 | 33 | 5 |
| 16 | OpenAlex | `tree Carleson packing extension survival branching combinatorial potential` | 6 | 0 | 0 | 0 |
| 17 | Crossref | `Kraft inequality infinite tree survival capacity stopping time Carleson` | 6 | 50 | 50 | 0 |
| 18 | arXiv | `tree Carleson packing Kraft inequality` | 6 | 50 | 50 | 0 |
| 19 | OpenAlex | `Infinite Sidon-type sets for zero-sum linear forms` | 7 | 25 | 23 | 2 |
| 20 | arXiv | `Conflict-free hypergraph matchings` | 7 | 25 | 25 | 0 |
| 21 | Crossref | `Random walks and percolation on trees branching number` | 7 | 25 | 25 | 0 |
| 22 | arXiv | `Bellman function sitting on a tree` | 8 | 10 | 10 | 0 |

The first deduplication reduced 479 records to 469. After the exact-title rounds,
the final machine corpus contains **550 records**. Automatic ranking was rerun on
all 550 records, but its top ranks still contained lexical false positives. Manual
theorem screening therefore overrides the ranking; the ranking is discovery
provenance only.

### Saturation status

The state remains at phase 1 because the mechanical saturation gate is not met.
The last exact-title/broad-index rounds were mostly new records, many off-topic:

- OpenAlex: 7 rounds; last round 92% new; one of four saturation axes passed.
- Crossref: 7 rounds; last round 100% new; two of four axes passed.
- arXiv: 8 rounds; last round 100% new; the exact Bellman query itself returned
  ten broadly related records rather than a stable exact-title cluster.

This was not gamed by repeating queries. Consequently every negative statement in
the audit is a **qualified null for the logged clusters and citation trails**, not a
claim that all mathematical literature has been exhausted.

## 2. Exa workstreams

Six semantic queries were run at ten results each, then repeated once only because
the first combined response was truncated and a compact title/URL extraction was
needed. Under Exa's counting rule this is **120 reviewed result slots across six
workstreams**:

1. arbitrary prescribed finite Sidon-prefix extension with coordinate bounds;
2. small maximal/saturated Sidon sets;
3. random-greedy Sidon/conflict hypergraphs;
4. ordered differences, Fejer kernels, and additive energy;
5. branching number, cutsets, flows, and survival;
6. tree Carleson embeddings and stopping-time packing.

High-signal leads that survived primary screening were Ruzsa's small maximal set,
Cilleruelo's greedy and explicit infinite constructions, Bennett--Bohman,
Glock--Joos--Kim--Kuehn--Lichev, Ortega--Prendiville, and Lyons. Search results
about dense finite Sidon sets, finite-field Sidon sets, unrelated harmonic-analysis
Sidon sets, and generic Carleson embeddings were not treated as P13 evidence.

Exa then fetched the official Springer pages for Ruzsa and Tafula, the primary
arXiv HTML for Ortega--Prendiville, and Lyons's author-hosted paper.

## 3. Firecrawl research index and citation expansion

Four abstract searches, each with `k=12` and date ceiling 2026-08-28, produced
48 result slots:

1. quantitative completion of a prescribed finite Sidon/Golomb prefix;
2. maximal/saturated Sidon sets;
3. Sidon constraints as random-greedy/nibble hypergraph problems;
4. Fourier/additive-energy identities for ordered differences.

Three structural expansions evaluated citation pools of sizes 18, 30, and 3:

- references of Ortega--Prendiville and Balasubramanian--Dutta, ranked for exact
  difference/Fourier identities;
- references of Bennett--Bohman and conflict-free matchings, ranked for
  regularity/codegree hypotheses;
- references of the small maximal finite-field construction and Cilleruelo's
  infinite construction, ranked for extension/completion.

Canonical metadata was inspected for arXiv:2110.13447, 1308.3732, 1601.00928,
1209.0326, 2205.05564, and 1911.13275. In-body retrieval was attempted for all six.
The combined long response interleaved/truncated some passages, so no load-bearing
formula was accepted from that output alone. Every formula in the audit was
rechecked in author-submitted arXiv LaTeX or an official publisher page.

## 4. Consensus and SciSpace

- Three Consensus queries all returned the exact quota error: all 30 monthly
  searches had already been used, resetting 2026-09-01. No theorem claim rests on
  Consensus.
- Three SciSpace natural-language questions were run twice (the second pass emitted
  compact identifiers after the first combined output was truncated), for 60 result
  slots. Results were mostly finite extremal Sidon, generalized ruler, and generic
  forbidden-difference papers. A methodology-column request for three candidates
  returned data for `0/3`. SciSpace was therefore used only as a lead generator.

These retrieval failures are not evidence that a theorem does not exist.

## 5. arXiv primary verification and citation chase

Exact arXiv catalog searches returned:

- `online Sidon` or `online Golomb ruler`: 0;
- `Sidon extension` or `extendable Sidon`: one record, arXiv:2604.25214;
- `prescribed Sidon set` or `prescribed Golomb ruler`: 0.

arXiv:2604.25214 was excluded from theorem evidence. Its own abstract calls the
claimed dilation family “apparent” and says a complete proof remains open. Its
extension target is also a finite cyclic perfect difference set, not an infinite
integer branch.

The arXiv citation graph for Ortega--Prendiville returned 3 citing papers and 25
references. The Bennett--Bohman graph was rate-limited, and Cilleruelo's greedy
paper was not resolved by Semantic Scholar. Firecrawl's structural reference pools
were used as the backup trail; failures are recorded rather than silently retried.

Author-submitted LaTeX was read section-wise for:

- Bennett--Bohman, Theorem 1.1 and the definitions of `Delta_l` and `Gamma`;
- Cilleruelo, the classical forbidden-value count and the strong `B_h[g]` greedy
  theorem;
- Glock et al., the main conflict-free matching theorem;
- Cilleruelo's explicit infinite Sidon construction;
- Arcozzi--Holmes--Mozolyako--Volberg, the dyadic-tree Carleson testing condition.

## 6. Official primary pages checked

- Imre Z. Ruzsa, [A Small Maximal Sidon Set](https://link.springer.com/chapter/10.1007/978-1-4757-4507-8_6).
- Christian Tafula, [Infinite Sidon-type sets for zero-sum linear forms](https://link.springer.com/article/10.1007/s00605-026-02211-4).
- Miquel Ortega and Sean Prendiville, [Extremal Sidon Sets are Fourier Uniform](https://www.numdam.org/articles/10.5802/jtnb.1239/).
- Javier Cilleruelo, [A greedy algorithm for B_h[g] sequences](https://arxiv.org/abs/1601.00928).
- Patrick Bennett and Tom Bohman, [A note on the random greedy independent set algorithm](https://arxiv.org/abs/1308.3732).
- Stefan Glock et al., [Conflict-free hypergraph matchings](https://arxiv.org/abs/2205.05564).
- Russell Lyons, [Random Walks and Percolation on Trees](https://rdlyons.pages.iu.edu/pdf/rwpt.pdf), DOI `10.1214/aop/1176990730`.
- Nicola Arcozzi et al., [Bellman function sitting on a tree](https://arxiv.org/abs/1809.03397).

## 7. Reproduction

From the handoff root:

```text
PY=/Users/USER/miniforge3/bin/python3
SCRIPTS=/Users/USER/.agents/skills/scholar-deep-research/scripts
STATE=research_sources/wave8_literature_state/research_state.json

$PY $SCRIPTS/research_state.py --state "$STATE" status
$PY $SCRIPTS/research_state.py --state "$STATE" saturation
$PY $SCRIPTS/research_state.py --state "$STATE" query queries
$PY $SCRIPTS/research_state.py --state "$STATE" query diagnostics
```

The state deliberately remains in discovery phase because the mechanical
saturation gate is false. `PRIMARY_SOURCE_AUDIT.md` is the theorem-screened result
and records exactly how far the qualified null extends.
