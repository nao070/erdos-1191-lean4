# Which Existing Theorems or Techniques Can Prove a Sub-Logarithmic Signed Cyclic-Arc Covariance Budget Across Critical-Density Dyadic Prefixes of an Infinite Additive Sidon Sequence, or Show That This Proposed Route Cannot Work? — A Source-Audited Literature Review

**Question:** Which existing theorem or technique can prove a sub-logarithmic signed cyclic-arc covariance budget across critical-density dyadic prefixes of an infinite additive Sidon sequence, or rigorously show that this proposed route cannot work?
**Date:** 2026-08-28
**Archetype:** `literature_review`
**State-backed sources:** arXiv, Crossref, OpenAlex, and Semantic Scholar citation chasing
**Corpus:** 306 deduplicated records; 16 selected (12 deep tier, 4 skim tier)
**Conclusion status:** **qualified null finding — Erdős Problem #1191 remains unresolved**

---

## Executive summary

- **Null finding, not a nonexistence theorem.** Among the 306 records searched and the primary papers audited most closely, no theorem was found that gives the required uniform `o(log J)` signed or positive cyclic-arc energy budget, and no theorem was found that rules out every possible version of that route. O'Bryant explicitly identifies averaging in the scale, reverse martingales, and entropy as possible extensions, but does not prove such an extension.[^arxiv:2606.28651]
- **The strongest direct universal argument still stops at a constant.** O'Bryant's all-offset, one-scale block-energy method gives a finite normalized bound `2 sqrt(g/log 2)` for a `g`-Golomb ruler; for ordinary Sidon sequences (`g=1`) this is a positive constant, whereas Question 1 requires an unbounded enumeration limsup, equivalently a zero counting-function liminf.[^arxiv:2606.28651] Part II introduces no stronger mechanism when specialized back to `h=2`.[^arxiv:2607.23795]
- **Near-extremal Fourier uniformity is quantitatively in the wrong regime.** The Ortega–Prendiville error is of order `sqrt(n)` when `|S|` is only `sqrt(n/log n)`, and Ding's progression-discrepancy bound inherits that loss. At the critical logarithmic deficit these estimates are larger than the set being controlled, so they do not supply the missing cross-scale cancellation.[^arxiv:2110.13447][^arxiv:2606.15041]
- **Entropy/large-sieve amplification has an unproved premise here.** Croot–Mao–Pohoata–Sheffer–Yip obtain a super-polylogarithmic saving only after assuming a fixed residue-support deficit at every prime. Their entropy argument amplifies modular ill-distribution; it does not derive that ill-distribution from ordinary Sidon uniqueness.[^arxiv:2606.17487]
- **The constructive frontier is still polynomially short of Question 2.** Ruzsa and Cilleruelo attain counting exponent `sqrt(2)-1`, whereas a polylogarithmic perturbation of quadratic enumeration requires counting exponent `1/2`.[^doi:10.1006/jnth.1997.2192][^arxiv:1209.0326] This gap is evidence of a genuine construction barrier, not evidence that Question 2 is false.

## 1. Background, target, and evidence labels

An additive Sidon set is a set of integers whose positive pairwise differences are unique (equivalently, whose nontrivial two-term additive representations are unique up to order). The workspace studies an infinite sequence `A={a_1<a_2<...}` under the contradiction hypothesis

```text
a_m <= C m^2 log m
```

and asks whether information from many dyadic prefixes can be accumulated. O'Bryant's current direct theorem controls one physical scale at a time and obtains a finite constant.[^arxiv:2606.28651] The proposed anti-Eulerian route instead assigns cyclic arcs to prefix differences, centers their load, and seeks a uniform upper bound smaller than logarithmic in the number `J` of dyadic scales. A matching lower bound of order `log J` would then contradict the critical envelope. The exact cyclic-arc functional is a result internal to this workspace; the literature question is whether an established theorem supplies the missing upper budget or proves that no such functional can work.

This is a deliberately narrow review. It includes ordinary additive Sidon sequences, finite Golomb-ruler estimates that might transfer to compatible prefixes, modular/Fourier distribution of finite integer Sidon sets, multiscale zero-sum representation theorems, and entropy or large-sieve mechanisms. It excludes harmonic-analysis Sidon sets, multiplicative Sidon sets, finite-field constructions without an integer-prefix transfer, and other Erdős prize problems that merely share the word “Sidon.” O'Bryant's annotated bibliography was used as a terminology and citation-chasing aid, not as evidence for a new theorem.[^arxiv:0407117]

The report uses the following labels:

- **Verified source result:** a theorem, hypothesis, or proof step checked in the primary paper.
- **Quantitative deduction:** an algebraic substitution made in this audit using a verified published estimate.
- **Null finding:** no qualifying theorem was located in this corpus; this never means that no such theorem exists.
- **Topic mismatch:** the primary source is real and was inspected, but its theorem does not address the target.
- **Unresolved claim:** a possible bridge or new lemma that is not established by any cited source.

## 2. One-scale density arguments saturate at a constant

### 2.1 What is verified

O'Bryant Part I averages interval-block counts over all offsets and bounds a one-scale block energy by the bounded multiplicity of differences. A weighted Cauchy–Schwarz step then yields the normalized constant

```text
2 sqrt(g/log 2),
```

and hence `2/sqrt(log 2)` in the ordinary Sidon case `g=1`.[^arxiv:2606.28651] The important word is **constant**: the paper strengthens the known universal restriction, but the mechanism as proved does not accumulate an unbounded gain over scale.

Part II treats even-order generalized Sidon sets. Its `h=2` specialization recovers the Part I Sidon theorem rather than strengthening it.[^arxiv:2607.23795] Carter–Hunter–O'Bryant couple several finite smoothing windows to improve the secondary coefficient in a finite diameter bound of the form

```text
D >= k^2 - b k^(3/2) - O(k).
```

The leading `k^2` scale remains unchanged, and the paper contains no compatible-infinite-prefix amortization theorem.[^arxiv:2310.20032]

### 2.2 What is only suggested

Section 3.1 of O'Bryant Part I explicitly mentions averaging over `N`, a reverse-martingale viewpoint, and entropy as directions not captured by the optimized one-scale calculation.[^arxiv:2606.28651] This is a verified research suggestion, not a claimed theorem. The literature therefore does **not** show that multiscale averaging is impossible; it shows only that repeating the existing one-scale estimate independently cannot by itself turn a fixed constant into the required divergent gain.

### 2.3 Consequence for the present route

The relevant distinction is between “more windows at one terminal scale” and “one compatible sequence across many scales.” The finite smoothing result belongs to the first category.[^arxiv:2310.20032] The missing anti-Eulerian lemma belongs to the second. No selected source supplies an inequality that prevents the same Sidon differences from paying repeatedly across nested prefixes. That sentence is a corpus-level null finding, not a theorem about all possible martingale or covariance formulations.

## 3. Near-extremal Fourier tools miss the critical logarithmic deficit

### 3.1 Verified estimates

Ortega–Prendiville prove Fourier uniformity for **extremal** finite Sidon sets. The relevant error term has the form

```text
Phi(S,n) = n^(1/2)
           ( |1-|S|/sqrt(n)| + n^(-1/4) )^(1/2).
```

Their proof uses van der Corput differencing together with short-interval control.[^arxiv:2110.13447] Ding uses the same quantitative input to bound discrepancy on arithmetic progressions by `Phi(S,n) log n`, obtaining equidistribution when `|S|` lies sufficiently close to `sqrt(n)`.[^arxiv:2606.15041]

### 3.2 Quantitative substitution at the #1191 scale

For a critical prefix, `|S|` is on the order of `sqrt(n/log n)`, so

```text
|S|/sqrt(n) = 1/sqrt(log n),
|1-|S|/sqrt(n)| -> 1,
Phi(S,n) asymptotic to sqrt(n).
```

Thus the Fourier error is of order `sqrt(n)`, while the set has only order `sqrt(n/log n)` elements. Ding's additional `log n` factor makes the progression-discrepancy upper bound still larger.[^arxiv:2110.13447][^arxiv:2606.15041] This calculation does not refute either theorem; it establishes that their hypotheses and error terms do not become informative in the critical logarithmically subextremal regime.

### 3.3 Remaining possibility

A new dichotomy could still be useful: either some prefix becomes near-extremal inside a shorter interval, activating the Fourier theorem, or failure of every such window forces endpoint variance. No cited paper proves that dichotomy. Accordingly, “Fourier methods fail” would be too broad; the supported statement is narrower: **the present near-extremal estimates do not bridge the critical logarithmic deficit without an additional localization theorem.**

## 4. Entropy, large sieve, and multiscale Fourier blocks

### 4.1 Modular entropy requires external ill-distribution

Croot–Mao–Pohoata–Sheffer–Yip prove combinatorial and entropy-enhanced large-sieve estimates under a uniform local hypothesis of the form

```text
|A_p| <= alpha p^r
```

for every prime, with a fixed `alpha<1` in the relevant ambient dimension. In their principal structured examples, algebraic sets such as squares or norm forms supply this splitting. The method then converts local branching/collision information into a super-polylogarithmic global saving.[^arxiv:2606.17487]

For an arbitrary Sidon prefix, uniqueness of integer differences does not by itself imply a fixed deficit in the number of occupied residue classes modulo each small prime. A critical prefix can therefore fail the theorem's load-bearing hypothesis without violating any result reviewed here. This is a **missing-hypothesis diagnosis**, not a counterexample to the large sieve.

The cleanest possible transfer would be a new theorem asserting either:

1. many critical Sidon prefixes omit a fixed fraction of residues for enough moduli; or
2. the absence of such a deficit already forces the desired cyclic-arc energy.

Neither implication appears in the audited sources. Until one is proved, applying the entropy large sieve directly to arbitrary #1191 prefixes would be an overclaim.

### 4.2 The closest positive multiscale analogue still yields a constant

Táfula studies zero-sum linear forms. For a matched-even vector

```text
(c_1,-c_1,...,c_k,-c_k),
```

the theorem uses disjoint dyadic index blocks and nonnegative Fourier integrals to force many representations when `A(x)/(x/log x)^(1/(2k))` tends to infinity.[^doi:10.1007/s00605-026-02211-4] In the case `k=1`, bounded difference multiplicity recovers the classical critical threshold for a Sidon set. It rules out growth by an **unbounded** multiple of `sqrt(x/log x)`; it does not rule out a fixed positive lower multiple at every sufficiently large scale.[^doi:10.1007/s00605-026-02211-4]

Táfula's proof is genuinely multiscale in the index, while O'Bryant's is shifted in physical space.[^doi:10.1007/s00605-026-02211-4][^arxiv:2606.28651] The audited statements provide no theorem showing that their two positive lower bounds are sufficiently independent to add across scales. Combining them remains an unresolved research proposal.

## 5. Construction side remains polynomially below the target exponent

Ruzsa's construction and Cilleruelo's explicit refinement attain

```text
A(x) = x^(sqrt(2)-1+o(1)).
```

The construction uses arithmetic structure and deletion to preserve unique differences.[^doi:10.1006/jnth.1997.2192][^arxiv:1209.0326] Maldonado gives a streamlined account of Ruzsa's construction but does not change the governing exponent.[^arxiv:1103.5732]

Question 2 asks for quadratic enumeration up to a fixed polylogarithm, which corresponds to counting size `sqrt(x)` up to a polylogarithmic loss. The exponent gap is

```text
1/2 - (sqrt(2)-1) = 3/2 - sqrt(2) approximately 0.0858.
```

This is a polynomial gap, not a missing logarithmic refinement. The audited construction papers contain no all-scale extension theorem that reaches the target. Conversely, a failure of these constructions does not prove that a different construction is impossible.

## 6. Tensions surfaced in synthesis

### 6.1 Can multiscale averaging escape the optimized one-scale constant?

- **Proposal side:** O'Bryant identifies averaging over scale, reverse martingales, and entropy as plausible unexplored directions.[^arxiv:2606.28651]
- **Quantitative side:** current finite smoothing changes secondary constants, while available Fourier bounds require near-extremality and become trivial at critical density.[^arxiv:2310.20032][^arxiv:2110.13447][^arxiv:2606.15041]

**Classification:** this is a methodological tension, not a disagreement between proved theorems. The first side proposes a mechanism; the second records limitations of existing implementations. The corpus supports continued investigation of a genuinely cross-scale invariant, but it does not support claiming that simple averaging already works.

### 6.2 Can modular entropy apply to a critical arbitrary Sidon prefix?

- **Conditional theorem:** a fixed residue-support deficit can be amplified into a super-polylogarithmic saving.[^arxiv:2606.17487]
- **Missing bridge:** the near-extremal distribution theorems do not provide that deficit at size `sqrt(n/log n)`.[^arxiv:2110.13447][^arxiv:2606.15041]

**Classification:** this is a hypothesis-transfer gap, not a theoretical contradiction. The large-sieve theorem is strong where its premise holds; the reviewed literature does not establish that premise for the population relevant to #1191.

## 7. Synthesis

The reviewed methods form a quantitative funnel:

| Method family | Verified gain | Why it stops before the target |
|---|---|---|
| One-scale block energy | A universal finite constant | No accumulation theorem across compatible scales.[^arxiv:2606.28651] |
| Multiple finite windows | Better secondary diameter constant | Still a finite terminal-scale estimate.[^arxiv:2310.20032] |
| Near-extremal Fourier uniformity | Strong control close to `sqrt(n)` | Error becomes order `sqrt(n)` at `sqrt(n/log n)`.[^arxiv:2110.13447][^arxiv:2606.15041] |
| Entropic/combinatorial large sieve | Super-polylogarithmic saving | Requires an external fixed modular deficit.[^arxiv:2606.17487] |
| Dyadic zero-sum Fourier blocks | Critical density restriction | Gives a finite-threshold conclusion in the Sidon case, not zero liminf.[^doi:10.1007/s00605-026-02211-4] |
| Ruzsa–Cilleruelo construction | Counting exponent `sqrt(2)-1` | Remains polynomially below `1/2`.[^doi:10.1006/jnth.1997.2192][^arxiv:1209.0326] |

The dominant conclusion is therefore not that one named technology has been overlooked. Every available technology needs one additional statement precisely at the interface between **nested-prefix compatibility** and **critical logarithmic sparsity**. The universal route needs an amortization or cancellation law that cannot be reduced to a sum of independent one-scale estimates. The sieve route needs a theorem deriving modular ill-distribution from the Sidon condition or a complementary energy alternative. The constructive route needs a mechanism that preserves density across every scale while eliminating cross-scale difference collisions.

This synthesis also limits what may be claimed about the new finite variance and exact covering identities developed in the workspace. They are legitimate incremental advances because none is contradicted by the literature reviewed here. They are **not** a resolution: no cited theorem supplies the remaining `o(log J)` upper budget, and a finite identity alone does not control an infinite compatible sequence.

The appropriate research decision is to keep the anti-Eulerian route active but sharpen its next milestone. Rather than seeking another lower bound at one prefix, seek one of two decisive statements:

1. a cross-scale theorem forcing the total normalized cyclic-arc energy to be `o(log J)` under the critical envelope; or
2. a compatible-prefix construction for which the same functional is `Omega(log J)`, proving that the functional—not merely the proof attempt—must be replaced.

Neither statement is established by this review.

## 8. Open questions and gaps

- **Nested martingale gap:** Can one define a filtration in which differences already present at scale `j` have orthogonal or summably correlated innovations at later scales? O'Bryant suggests the viewpoint, but supplies no square-function theorem.[^arxiv:2606.28651]
- **Birth-edge gap:** How much energy can newly appearing differences cancel from the load inherited from the previous prefix? None of the selected papers quantifies this cancellation across an arbitrary infinite Sidon sequence.
- **Modular alternative gap:** Is there a dichotomy saying that a critical Sidon prefix either has a fixed residue deficit for many moduli or has large endpoint/cyclic discrepancy? Such a result would connect the large sieve to the anti-Eulerian functional.[^arxiv:2606.17487]
- **Localization gap:** Can a logarithmically subextremal set be localized to a shorter interval where it becomes near-extremal, without losing prefix compatibility? That would be needed to activate the Ortega–Prendiville and Ding estimates.[^arxiv:2110.13447][^arxiv:2606.15041]
- **Hybrid-block gap:** Can Táfula's dyadic index blocks and O'Bryant's all-offset physical blocks be combined without charging the same differences at every scale?[^doi:10.1007/s00605-026-02211-4][^arxiv:2606.28651]
- **Construction gap:** What structural saving can raise the Ruzsa–Cilleruelo exponent from `sqrt(2)-1` to `1/2` up to logarithms while checking all cross-scale difference collisions?[^doi:10.1006/jnth.1997.2192][^arxiv:1209.0326]
- **Literature-indexing gap:** The exact cyclic `H^-1`/inverse-Laplacian formulation produced no directly relevant paper in the targeted searches. This is only a search null: terminology could differ, and specialist databases did not expose every newest preprint.

## 9. Recommendations for further reading

Read in this order for the proof route, rather than following the raw automated score:

1. **O'Bryant, Part I** — the direct benchmark, exact one-scale architecture, and explicit list of multiscale ideas not yet made to work.[^arxiv:2606.28651]
2. **Croot–Mao–Pohoata–Sheffer–Yip** — the strongest entropy/collision amplifier in the corpus; focus on the residue-support hypothesis before attempting transfer.[^arxiv:2606.17487]
3. **Ortega–Prendiville, then Ding** — read the error term first; it explains exactly why near-extremal Fourier control does not automatically reach critical density.[^arxiv:2110.13447][^arxiv:2606.15041]
4. **Táfula** — the closest genuinely dyadic Fourier argument; useful for comparing index-scale positivity with physical-offset energy.[^doi:10.1007/s00605-026-02211-4]
5. **Carter–Hunter–O'Bryant** — a useful model of coupled finite windows, but not an infinite-prefix theorem.[^arxiv:2310.20032]
6. **Cilleruelo, with Ruzsa and Maldonado as context** — the construction frontier and its persistent exponent barrier.[^arxiv:1209.0326][^doi:10.1006/jnth.1997.2192][^arxiv:1103.5732]

The raw Phase 2 score placed Niu's *Size-4 Counterexamples to the Sidon-Extension Conjecture* first. Primary-source triage showed that it concerns extension of small finite Sidon sets to perfect difference sets—a different Erdős prize conjecture—and it provides no infinite-density or covariance theorem for #1191.[^arxiv:2604.25214] Likewise, finite vector-space Sidon constructions,[^arxiv:2411.12911] Sidon subsets of weak Sidon sets,[^arxiv:2602.23282] inverse classification of linear forms,[^arxiv:2104.06501] unions of intervals,[^arxiv:2202.01296] and modular Golomb-ruler designs[^doi:10.1109/tit.2025.3566655] are valid papers but topic mismatches for the load-bearing claim in this report.

## Appendix A — Methodology and audit trail

### Search and ranking

The persistent state records 11 scripted search/citation-chase operations across four sources: arXiv (4 queries), Crossref (4), OpenAlex (2), and Semantic Scholar citation chasing (1). The citation chase returned 114 records, of which 87 were new and 27 merged into existing records. After deduplication the corpus contained 306 papers. The ranking formula was

```text
score = 0.55*relevance
      + 0.15*log10(citations+1)/3
      + 0.25*exp(-delta_years/5)
      + 0.05*venue_prior.
```

Sixteen papers were selected: 12 deep tier and 4 skim tier. Five deep-tier papers received full method-level evidence: O'Bryant Part I, Croot et al., Ding, Ortega–Prendiville, and Carter–Hunter–O'Bryant. Seven deep-tier records were explicitly downgraded after primary-scope inspection because they addressed a different finite, finite-field, inverse, containment, or modular-design problem. Four construction/history papers retained shallow abstract or bibliographic evidence. Táfula was found in the citation-chase corpus and then checked separately against the primary preprint and published metadata.

Supplementary plugin searches (Exa, Firecrawl, and SciSpace) were used for discovery and source retrieval only. Their semantic rankings were not treated as theorem verification. Consensus returned no results because its monthly quota was exhausted; therefore no claim in this report depends on Consensus.

### Scope limitations

- The review is mechanism-targeted, not a formal systematic review of every Sidon paper.
- Several 2026 sources are arXiv preprints; versioned statements may change.[^arxiv:2606.28651][^arxiv:2606.17487][^arxiv:2606.15041]
- Missing citation counts in the state reduce the value of citation-weighted ranking for recent preprints.
- A search null is not evidence of nonexistence, especially for a new formulation whose terminology may not match the literature.
- Topic-mismatch records were retained in the audit trail so that later searches do not repeatedly mistake them for #1191 results.

## Appendix B — Self-critique

### Finding 1: recent “Sidon” titles distorted automated ranking

The ranking over-weighted recent papers whose titles contain “Sidon” but whose theorems concern finite extension, finite fields, weak Sidon containment, inverse linear-form classification, or modular designs. This was resolved by inspecting primary scopes and marking seven deep-tier candidates as topic mismatches. The consequence is visible in the recommendations: raw score order is not used as proof relevance.

### Finding 2: the initial scripted selection omitted a close July 2026 analogue

Táfula's zero-sum linear-form paper entered through citation chasing rather than the original selected 16. Targeted source retrieval corrected the omission and its dyadic proof mechanism is now compared directly with O'Bryant's physical-space blocks.[^doi:10.1007/s00605-026-02211-4][^arxiv:2606.28651] The selection statistics above are intentionally left unchanged; silently rewriting them would damage the audit trail.

### Finding 3: strong tools could be misreported without substituting the critical scale

The most serious overclaim risk was to cite “Fourier uniformity” or “entropy large sieve” by name without checking its quantitative regime. Substituting `|S|=sqrt(n/log n)` makes the Fourier error order `sqrt(n)`, while reading the large-sieve hypothesis reveals the missing fixed residue deficit.[^arxiv:2110.13447][^arxiv:2606.15041][^arxiv:2606.17487] Those checks convert an impression of applicability into two precise missing premises.

### Final adversarial assessment

No located paper proves the required `o(log J)` signed or positive gap-energy budget. O'Bryant's theorem yields an optimized finite constant and only suggests multiscale, martingale, or entropy extensions.[^arxiv:2606.28651] Ortega–Prendiville and Ding become quantitatively non-informative at the critical logarithmic deficit.[^arxiv:2110.13447][^arxiv:2606.15041] Croot et al. require modular ill-distribution not supplied by Sidon uniqueness.[^arxiv:2606.17487] Táfula's zero-sum shell method likewise yields only a constant-threshold conclusion in the Sidon case.[^doi:10.1007/s00605-026-02211-4] Finite smoothing and diameter arguments improve secondary constants but provide no compatible-prefix amortization.[^arxiv:2310.20032]

Therefore the literature is consistent with the finite variance lemma and exact covering identity developed in the workspace, but it does not upgrade either to a resolution of Erdős Problem #1191. The defensible status is **active, unresolved research**.

## Bibliography

Machine-exported BibTeX for the selected corpus, plus the supplemental Táfula record, is stored at `scholar_anti_eulerian_2026-08-28.bib` in this directory.

Anchor index:

[^arxiv:2606.28651]: Kevin O'Bryant (2026). *On the Thickness of Infinite Generalized Sidon Sets, I*. arXiv:2606.28651v3.
[^arxiv:2607.23795]: Kevin O'Bryant (2026). *On the Thickness of Infinite Generalized Sidon Sets, II*. arXiv:2607.23795v1.
[^arxiv:2606.17487]: Ernie Croot, Junzhe Mao, Cosmin Pohoata, Adam Sheffer, and Chi Hoi Yip (2026). *A combinatorial large sieve for Sidon sets, distances, and norm forms*. arXiv:2606.17487v2.
[^arxiv:2606.15041]: Yuchen Ding (2026). *Dense finite Sidon sets on arithmetic progressions*. arXiv:2606.15041v2.
[^arxiv:2110.13447]: Miquel Ortega and Sean Prendiville (2021 preprint; published 2023). *Extremal Sidon sets are Fourier uniform, with applications to partition regularity*. arXiv:2110.13447.
[^arxiv:1209.0326]: Javier Cilleruelo (2012 preprint; published 2014). *Infinite Sidon sequences*. arXiv:1209.0326.
[^doi:10.1006/jnth.1997.2192]: Imre Z. Ruzsa (1998). *An Infinite Sidon Sequence*. *Journal of Number Theory* 68, 63–71. DOI: 10.1006/jnth.1997.2192.
[^arxiv:1103.5732]: Juan Pablo Maldonado (2011). *A remark of Ruzsa's construction of an infinite Sidon set*. arXiv:1103.5732.
[^arxiv:0407117]: Kevin O'Bryant (2004). *A Complete Annotated Bibliography of Work Related to Sidon Sequences*. *Electronic Journal of Combinatorics*, Dynamic Survey 11.
[^arxiv:2411.12911]: Ingo Czerwinski and Alexander Pott (2024). *On large Sidon sets*. arXiv:2411.12911.
[^arxiv:2604.25214]: Tong Niu (2026). *Size-4 Counterexamples to the Sidon-Extension Conjecture*. arXiv:2604.25214.
[^arxiv:2310.20032]: Daniel Carter, Zach Hunter, and Kevin O'Bryant (2023 preprint; published 2025). *On the Diameter of Finite Sidon Sets*. arXiv:2310.20032.
[^arxiv:2602.23282]: Jie Ma and Quanyu Tang (2026). *Largest Sidon subsets in weak Sidon sets*. arXiv:2602.23282.
[^arxiv:2104.06501]: Melvyn B. Nathanson (2021). *An inverse problem for finite Sidon sets*. arXiv:2104.06501.
[^arxiv:2202.01296]: Robin Riblet (2022). *Sidon sets in a union of intervals*. arXiv:2202.01296.
[^doi:10.1109/tit.2025.3566655]: Daniel M. Gordon (2025). *Modular Golomb Rulers and Almost Difference Sets*. *IEEE Transactions on Information Theory*. DOI: 10.1109/TIT.2025.3566655.
[^doi:10.1007/s00605-026-02211-4]: Christian Táfula (2026). *Infinite Sidon-type sets for zero-sum linear forms*. *Monatshefte für Mathematik*. DOI: 10.1007/s00605-026-02211-4; arXiv:2607.20753.
