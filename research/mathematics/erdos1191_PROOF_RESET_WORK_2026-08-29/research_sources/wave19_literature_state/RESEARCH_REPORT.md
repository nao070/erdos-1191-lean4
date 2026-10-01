# Which Primary Theorems Quantitatively Constrain Repeated Dyadic Endpoint Upcrossings a_(2n-1)/a_n, or Absorb Terminal-to-Descendant Cross-Ratio Rectangles Into Signed Multiscale Energy, on One Fixed Infinite Integer Sidon/Golomb Branch Satisfying a_n <= C n^2 log(2n), Strongly Enough to Close P23 — A Literature Review

**Question:** Which primary theorems quantitatively constrain repeated dyadic endpoint upcrossings a_(2n-1)/a_n, or absorb terminal-to-descendant cross-ratio rectangles into signed multiscale energy, on one fixed infinite integer Sidon/Golomb branch satisfying a_n <= C n^2 log(2n), strongly enough to close P23?
**Date:** 2026-08-29
**Archetype:** `literature_review`
**Sources consulted:** arxiv, crossref, openalex, openalex_citation_chase, s2_citation_chase
**Papers in corpus:** 345 (10 selected — 7 deep, 3 skim)

**Frontier update:** The search question was fixed while P23 was the active
formulation.  The first Wave 19 coefficient proof reclassified it as the
signed P24 frontier bound.  The later certified-rank-slack reduction retains
the singly owned payment `Qcert`, cancels the previous-source cap exactly,
and makes the dilation-invariant remainder `Rcert` the recommended P25
target.  The subsequent exact pairing bound makes `Pair` dyadically
summable and replaces `Rcert` by the sharper rank-free
`Rsharp=Rcert-Pair`, giving the intermediate P26 target.  The subsequent
five-channel decomposition proves `Rsharp>=0`, so the P26 positive part is
redundant and yields the standalone P27 upper target.  A final
compatible-branch audit then isolates an untouched inner-new-birth sector
`W>=1/[1536C log(4n)]`; its Fejér liminf coefficient
`1/(1536C log2)` is twice the former strict threshold.  Thus P27 is not
proved but is saturated as a standalone upper-bound route.  The current P28
direction is to move or retain `W` against the negative renewal cut, or to
enlarge descendant absorption with exact ownership.  P24/P25 remain open
historical reductions, while P26/P27 remain unproved and are closed as
standalone routes.  The fixed-branch, birth-delay, terminal-ownership,
and compatibility filters audited here are unchanged; none of the scoped
search findings below has been reinterpreted as a theorem-nonexistence or
novelty claim.

A targeted P28 plugin refresh on 2026-08-29 did not change that scoped
assessment.  Exa resurfaced the already-audited O'Bryant
`arXiv:2606.28651v3` and adjacent strong, multiplicative, and finite Sidon
records; Firecrawl returned `arXiv:1911.13275`, `arXiv:2607.20753`,
`arXiv:1209.0326`, and adjacent material; and SciSpace returned mostly
asymptotic-basis or finite adjacent records.  None of those retrievals stated
the exact P28 renewal/cross-ratio carrier.  Consensus was exhausted at
`30/30` requests and resets on 2026-09-01.  These are connector-bounded
retrieval results, not nonexistence or novelty evidence.  Because the refresh
was not ingested and deduplicated into the structured state, the corpus count
remains 345.

---

## Executive summary

- The federated search and citation chase produced 345 deduplicated records; 10 manually verified Sidon/Golomb records were selected after the initial semantic ranking proved unreliable. The evidence base for those 10 consists of six full primary-text reads, one documented `paywall_no_oa` exception, and three abstract-level skim records. This supports only the scoped applicability assessment below, not theorem nonexistence or novelty.
- The closest exact quantitative input is the Erdős–Turán Sidon Set Equality of Carter–Hunter–O'Bryant: it decomposes the diameter of one finite Sidon set into missing-difference slack and sliding-window variance. Its statements do not compare the same differences across a nested sequence of prefixes, so they do not themselves control a fixed branch's repeated dyadic upcrossings.[^arxiv:2310.20032]
- The closest birth mechanisms are qualitative. Cilleruelo–Nathanson realize each missing difference using pairs placed at scales governed by an arbitrarily fast auxiliary function, while Alexeev–Mixon give a greedy finite-to-infinite extension claim without a location or delay bound; neither preserves the quantitative ordered-prefix structure required by P23.[^arxiv:0609244][^arxiv:2510.19804]
- The selected explicit infinite constructions are too sparse for the critical envelope: Cilleruelo's strongest stated counting exponent is `sqrt(2)-1`, while the accessible statement of Ruzsa's almost-polynomial construction has fifth-degree growth.[^arxiv:1209.0326][^doi:10.1556/sscmath.38.2001.1-4.27]
- Consensus contributed no evidence because its monthly quota was exhausted. SciSpace returned adjacent Sidon, Golomb, perfect-difference-set, and packing material, but no returned result stated the required fixed-branch quantitative theorem; this is a connector-limited scoped null, not a negative theorem.

## 1. Background

A strictly increasing integer Sidon sequence has unique nontrivial pairwise sums; in the equivalent Golomb-ruler formulation used here, its positive pairwise differences are distinct. Finite Sidon-set diameter identities therefore quantify how efficiently one finite prefix packs distinct differences, but the target in P23 is stronger: it concerns the ordered history of one fixed infinite branch, not an unrelated optimal set at each size.[^arxiv:2310.20032]

The critical hypothesis is an eventual all-prefix envelope `a_n <= C n^2 log(2n)` with one fixed `C` and onset. The desired conclusion must quantitatively limit repeated endpoint upcrossings `a_(2n-1)/a_n`, or equivalently absorb the terminal-to-descendant cross-ratio cost into signed multiscale energy without changing branches. Thus a relevant theorem must preserve six features simultaneously: one infinite branch, its prescribed prefixes, dyadic scale compatibility, controlled first-birth delay, terminal atoms, and the sign/ownership of the carrier terms. A finite extremal estimate, a `limsup` density result, or a qualitative completion theorem can be useful without meeting that quantifier package.

This review is deliberately narrow. It reports what was found in a 345-record federated corpus and what was verified in the 10 selected primary records. The conclusion is only that no theorem in that audited slice supplies the complete P23 bridge; it does not assert that such a theorem is absent from mathematics or that the project's formulation is novel.

## 2. Qualitative extension versus quantitative birth locality

The audited extension constructions can realize missing differences or embed finite Sidon data, but provide no critical-scale insertion-time, displacement, or ordered-prefix bound.[^arxiv:2510.19804][^arxiv:0609244]

Contributing papers:

- Alexeev et al. (2025) — Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof [^arxiv:2510.19804]
- Cilleruelo et al. (2006) — Perfect difference sets constructed from Sidon sets [^arxiv:0609244]

Alexeev–Mixon's Claim 10 extends every finite integer Sidon set to an infinite perfect difference set by greedily inserting a pair for each missing difference. The same paper also observes that an already infinite Sidon set need not admit such an extension. Consequently, the claim is a genuine qualitative birth result, but it supplies neither a bound on where the new pair is placed nor a theorem that preserves an already specified infinite branch.[^arxiv:2510.19804]

Cilleruelo–Nathanson prove a different qualitative embedding: after scaling and pruning an input Sidon sequence, they construct a perfect difference set whose counting function retains a shifted shadow of the input. Missing differences are realized by pairs near `4^{g(k)}`, where the auxiliary function `g` may grow arbitrarily fast; the resulting density statement is a `limsup`, and the paper explicitly describes the witness as irregular.[^arxiv:0609244]

The two approaches converge on existence and realization, not locality. Neither gives a uniform insertion-delay estimate, survival of every prescribed prefix, or a summable cost over dyadic scales. Those are exactly the additional quantitative properties needed before an extension theorem can constrain P23.[^arxiv:2510.19804][^arxiv:0609244]

## 3. Finite energy and density versus one compatible branch

The audited finite diameter identities, interval-packing results, and near-extremal coordinate estimates constrain individual rulers but do not control a nested dyadic history on one infinite branch.[^arxiv:2310.20032][^arxiv:2202.01296][^doi:10.1016/j.jnt.2025.07.007]

Contributing papers:

- Carter et al. (2023) — On the Diameter of Finite Sidon Sets [^arxiv:2310.20032]
- Riblet (2022) — Sidon sets in a union of intervals [^arxiv:2202.01296]
- Balasubramanian et al. (2026) — The m-th element of a Sidon set [^doi:10.1016/j.jnt.2025.07.007]
- Cilleruelo (2012) — Infinite Sidon sequences [^arxiv:1209.0326]

Carter–Hunter–O'Bryant provide the strongest exact energy identity in the audited set. Their Theorem 1.1 expresses the diameter of a finite Sidon set using missing-difference slack and sliding-window variance; their subsequent corollary and multi-window lemmas turn sufficiently large variance into improved finite diameter lower bounds.[^arxiv:2310.20032] Riblet similarly uses short windows, Cauchy–Schwarz, and uniqueness of small differences to bound the size of Sidon subsets in finite unions of intervals.[^arxiv:2202.01296] These results rigorously control finite geometry, but neither labels when a difference first appears nor matches the same carrier across nested prefixes.

Balasubramanian–Dutta obtain coordinate regularity for near-extremal finite Sidon sets in an interval, including an asymptotic location formula for the `m`-th element. That hypothesis is substantially stronger than the bare upper envelope in P23: a prefix bounded by `C n^2 log(2n)` need not be near extremal in its ambient interval.[^doi:10.1016/j.jnt.2025.07.007] Cilleruelo's infinite construction does maintain one branch, but its collision control is specific to an engineered mixed-radix architecture and does not become an arbitrary-branch upcrossing theorem.[^arxiv:1209.0326]

The missing operation is therefore not another separate finite estimate. It is a compatibility theorem that transports finite slack/variance through a single nested branch while retaining first-birth labels and the signs needed for terminal-to-descendant cancellation.[^arxiv:2310.20032][^arxiv:2202.01296]

## 4. Sparse constructions versus critical all-scale density

The selected explicit infinite Sidon constructions achieve subcritical density through irregular scale separation, well below the near-quadratic-logarithmic envelope relevant to P23.[^arxiv:1209.0326][^doi:10.1556/sscmath.38.2001.1-4.27]

Contributing papers:

- Cilleruelo (2012) — Infinite Sidon sequences [^arxiv:1209.0326]
- Ruzsa (2001) — An almost polynomial Sidon sequence [^doi:10.1556/sscmath.38.2001.1-4.27]

Cilleruelo's explicit construction reaches counting exponent `sqrt(2)-1`; after inversion, its ordered elements grow like `n^(1+sqrt(2)+o(1))`, still faster than `n^2 log n`. The construction's useful collision inequalities apply to its own separated scales, not to every branch satisfying the critical envelope.[^arxiv:1209.0326]

For Ruzsa's almost-polynomial construction, only the primary theorem statement was accessible in this audit: a sequence of the form `n^5 + floor(alpha n^4)` is Sidon for a suitable `alpha` and all sufficiently large `n`. The proof was paywalled and is not summarized here. The stated fifth-degree growth alone places this example far outside the P23 scale.[^doi:10.1556/sscmath.38.2001.1-4.27]

These papers show why sparse scale separation is a powerful construction device, but they do not decide whether critical all-scale density forces regularity or whether sparse terminal spikes can coexist indefinitely with that density. Treating their construction-specific collision control as a universal fixed-branch theorem would change the quantifiers.[^arxiv:1209.0326][^doi:10.1556/sscmath.38.2001.1-4.27]

## Tensions surfaced in synthesis

### Finite completion does not imply critical prescribed-prefix completion

- **Side 1:** Every finite integer Sidon set has a qualitative infinite completion or embedding mechanism. [^arxiv:2510.19804][^arxiv:0609244]
- **Side 2:** The available constructions leave insertion delay and critical all-prefix density uncontrolled; finite multiscale estimates do not repair that quantifier gap. [^arxiv:2310.20032][^arxiv:1209.0326]

This is a theoretical and methodological quantifier gap, not a contradiction between results. The extension papers establish existence after allowing rescaling, pruning, or uncontrolled insertion locations; the finite-energy papers establish strong inequalities after freezing one finite set.[^arxiv:2510.19804][^arxiv:0609244][^arxiv:2310.20032] Within the audited corpus, the second side is the better description of applicability to P23: none of those operations yields the required prescribed-prefix, fixed-branch bound. That assessment does not show that such a bridge is impossible or absent elsewhere.


## Synthesis

The corpus supplies two halves of a plausible strategy but not their interface. Finite Sidon energy identities can make excess diameter pay through missing-difference slack and window variance.[^arxiv:2310.20032] Qualitative completion constructions can force missing differences to be born in an infinite perfect difference set.[^arxiv:0609244][^arxiv:2510.19804] P23, however, needs the birth event and the energy charge to refer to the same difference, on the same ordered branch, at compatible dyadic scales. Once that genealogy is discarded, summing otherwise sharp finite estimates can double-count carriers or lose the sign required for absorption.

The selected construction literature does not repair the interface. Its sparsity is achieved through deliberately separated or irregular scales, and the strongest audited counting exponent remains below the critical density implicit in `a_n <= C n^2 log(2n)`.[^arxiv:1209.0326][^doi:10.1556/sscmath.38.2001.1-4.27] Conversely, near-extremal finite coordinate regularity requires hypotheses not supplied by the P23 envelope.[^doi:10.1016/j.jnt.2025.07.007] The audited literature therefore points to a specific missing lemma rather than a ready-made theorem: a branch-compatible first-birth or signed-carrier estimate that converts uniqueness of differences plus eventual critical growth into a summable dyadic cost.[^arxiv:2310.20032][^arxiv:0609244]

The defensible conclusion is a scoped null. Among the 10 selected records from the 345-record corpus—with six full reads, one explicit access exception, and three abstract-level skims—no verified theorem closes that interface. Consensus could not be used because its quota was exhausted, and SciSpace's returned items did not state the target fixed-branch theorem. These coverage limits prevent any inference of theorem nonexistence or novelty.

## Open questions and gaps

- **Quantitative birth locality on a prescribed branch.** Existing completion mechanisms realize missing differences without bounding insertion displacement or delay and may rescale or prune the seed.[^arxiv:0609244][^arxiv:2510.19804] A next search should target prescribed-prefix Sidon completion, online Golomb-ruler extension, and quantitative perfect-difference-set insertion.
- **Nested transport of finite energy.** The audited diameter and interval-packing theorems freeze one finite set and do not track first-birth labels or signed carriers across prefixes.[^arxiv:2310.20032][^arxiv:2202.01296] The mathematical target is a monotone or telescoping coupling of their window/slack terms along one dyadic tower.
- **Critical-density obstruction or construction.** The selected infinite constructions use subcritical counting exponents or fifth-degree growth.[^arxiv:1209.0326][^doi:10.1556/sscmath.38.2001.1-4.27] Progress could come either from proving that repeated terminal spikes force a violation of the fixed all-prefix envelope, or from constructing a compatible tower that preserves such spikes indefinitely.
- **Hypothesis transfer from finite near-extremality.** Coordinate regularity is known under a near-extremal ambient-interval assumption, not from the P23 cap alone.[^doi:10.1016/j.jnt.2025.07.007] One concrete question is whether the all-prefix cap plus Sidon uniqueness yields enough local near-extremality on a positive proportion of dyadic scales to activate those estimates.

## Recommendations for further reading

Top-scored papers from the corpus, ranked by Phase 2 score (see Methodology appendix for the formula):

1. **Ajtai et al. (1981)** — A Dense Infinite Sidon Sequence [^doi:10.1016/s0195-6698(81)80014-5]
2. **Ruzsa (1998)** — An Infinite Sidon Sequence [^doi:10.1006/jnth.1997.2192]
3. **Alexeev et al. (2025)** — Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof [^arxiv:2510.19804]
4. **Balasubramanian et al. (2026)** — The m-th element of a Sidon set [^doi:10.1016/j.jnt.2025.07.007]
5. **Carter et al. (2023)** — On the Diameter of Finite Sidon Sets [^arxiv:2310.20032]

Start with Carter–Hunter–O'Bryant for the exact finite energy identity and Alexeev–Mixon for the cleanest qualitative extension statement.[^arxiv:2310.20032][^arxiv:2510.19804] Read Balasubramanian–Dutta next to see precisely what an additional near-extremality hypothesis buys.[^doi:10.1016/j.jnt.2025.07.007] Ajtai–Komlós–Szemerédi and Ruzsa are historical density benchmarks in this state, but they were only abstract-level skim records here; consult their primary texts before using proof details.[^doi:10.1016/s0195-6698(81)80014-5][^doi:10.1006/jnth.1997.2192]
The third skim record, Ruzsa's *A Small Maximal Sidon Set*, is retained in the bibliography for corpus traceability but is not used as evidence for the fixed-branch assessment.[^doi:10.1023/a:1009757824153]

## Appendix A — Methodology

**Search strategy:** 14 queries across 5 federated sources — arxiv (3 queries), crossref (5 queries), openalex (4 queries), openalex_citation_chase (1 queries), s2_citation_chase (1 queries).

**Saturation:** see `python scripts/research_state.py --state <state.json> saturation` for the per-source breakdown
that gated Phase 1 → Phase 2.

**Ranking formula (Phase 2):**
```
score = 0.55·relevance + 0.25·log10(citations+1)/3 + 0.1·exp(-Δyears/5.0) + 0.1·venue_prior
```
Weights: alpha=0.55, beta=0.25, gamma=0.1, delta=0.1.

**Selection:** top 10 by score, triaged into deep (full-text agent fan-out) and skim (abstract-only stub)
tiers via `skim_papers.py`. Per-paper `score_components` and
`triage_components` are preserved in state.

## Appendix B — Self-critique

Adversarial review: this audit establishes only a scoped null over the searched and citation-chased corpus, not theorem nonexistence or novelty. Six selected sources have full primary evidence; one deep-tier source has an explicit paywall_no_oa exception, and three are abstract-level skim records. Consensus supplied no evidence because its quota was exhausted. SciSpace and the citation chase broaden coverage but do not validate a fixed-branch theorem. The initial relevance ranking produced serious semantic false positives and was manually overridden before triage. Any later paper must be checked for exact quantifiers: one fixed infinite branch, eventual cap with fixed onset, prescribed-prefix compatibility, birth delay, terminal atoms, and signed carrier ownership.

## Bibliography

Full BibTeX for the selected records is at [`SELECTED_REFERENCES.bib`](SELECTED_REFERENCES.bib).
It was generated via:

```bash
/Users/USER/miniforge3/bin/python3 /Users/USER/.agents/skills/scholar-deep-research/scripts/export_bibtex.py \
  --state research_state.json --format bibtex --output SELECTED_REFERENCES.bib
```

Anchor index:

[^arxiv:2510.19804]: Alexeev et al. (2025). Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof
[^doi:10.1023/a:1009757824153]: Ruzsa (1998). A Small Maximal Sidon Set — doi:10.1023/a:1009757824153
[^doi:10.1016/s0195-6698(81)80014-5]: Ajtai et al. (1981). A Dense Infinite Sidon Sequence — doi:10.1016/s0195-6698(81)80014-5
[^doi:10.1006/jnth.1997.2192]: Ruzsa (1998). An Infinite Sidon Sequence — doi:10.1006/jnth.1997.2192
[^doi:10.1556/sscmath.38.2001.1-4.27]: Ruzsa (2001). An almost polynomial Sidon sequence — doi:10.1556/sscmath.38.2001.1-4.27
[^arxiv:1209.0326]: Cilleruelo (2012). Infinite Sidon sequences
[^arxiv:0609244]: Cilleruelo et al. (2006). Perfect difference sets constructed from Sidon sets
[^arxiv:2202.01296]: Riblet (2022). Sidon sets in a union of intervals
[^arxiv:2310.20032]: Carter et al. (2023). On the Diameter of Finite Sidon Sets
[^doi:10.1016/j.jnt.2025.07.007]: Balasubramanian et al. (2026). The m-th element of a Sidon set — doi:10.1016/j.jnt.2025.07.007
