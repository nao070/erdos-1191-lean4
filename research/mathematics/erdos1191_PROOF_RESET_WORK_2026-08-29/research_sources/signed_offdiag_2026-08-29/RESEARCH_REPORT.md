# Which Primary Theorems or Exact Kernel Mechanisms Can Turn Common-Shift Signed Off-Diagonal or Cross-Kernel Energy, Aggregate Nonnegative Correlation, Reverse-Martingale Deficit, or Entropy Into an Order-Changing Critical-Density Bound for One Compatible Infinite Sidon Sequence, and What Exact No-Go Reductions Delimit These Methods — A Literature Review

**Question:** Which primary theorems or exact kernel mechanisms can turn common-shift signed off-diagonal or cross-kernel energy, aggregate nonnegative correlation, reverse-martingale deficit, or entropy into an order-changing critical-density bound for one compatible infinite Sidon sequence, and what exact no-go reductions delimit these methods?
**Date:** 2026-08-29
**Archetype:** `literature_review`
**Sources consulted:** arxiv, crossref, openalex, openalex_s2_citation_chase
**Papers in corpus:** 210 (10 selected — 6 deep, 4 skim)

---

## Executive summary

- Hou--Zhao's actual joint mechanism is a cooperative boundary cover with
  diagonal direct-sum energy; it proves the finite coefficient
  `0.943492590...` and leaves “controlled cross-kernel terms” as future work,
  explicitly requiring nonnegative combined correlation at every nonzero
  shift.  The signed off-diagonal interpretation is the present Route-C
  proposal, not Hou--Zhao's wording or construction.[^doi:10.48550/arxiv.2607.01169]
- O'Bryant proves the positive universal upper bound
  `liminf A(n)/sqrt(n/log n) <= 2/sqrt(log 2)` for ordinary Sidon sets; it
  does not prove that the liminf is positive or equals this constant.  Multi-`N`, reverse martingales,
  entropy, and Cauchy-stability appear only in the paper's explicitly
  nonrigorous discussion, not in the theorem.[^arxiv:2606.28651]
- Goh supplies conditional entropy infrastructure, but the proved Sidon
  inequality uses only recovery of an unordered pair.  For a uniform
  `m`-point Sidon law, direct multiplicity counting gives exactly
  `H(X+X')=2 log_2(m)-(m-1)/m`, so the fixed-prefix entropy is independent of
  the set's geometry.[^doi:10.2140/ent.2026.5.243]
- Táfula provides a genuinely common Fourier parameter over dyadic blocks,
  but all factors are nonnegative absolute squares and the conclusion is
  average representation growth, not a signed compatible-history
  deficit.[^doi:10.1007/s00605-026-02211-4]
- No checked primary source executes the complete combination needed here:
  signed off-diagonal kernels, legal payment at every common shift, one
  compatible infinite history, and an order-changing bound.  This is a dated
  qualified null, not an absence or novelty theorem.

## 1. Background

A Sidon set of integers has at most one representation of every positive
difference.  Erdős Problem #1191 asks, among other things, whether every
infinite Sidon set must have zero lower density after normalization by
`sqrt(x/log x)`.  The strongest current theorem in the selected corpus gives
only an explicit positive universal upper bound for the normalized
liminf.[^arxiv:2606.28651]  Therefore a
finite secondary-term improvement or a better constant is not enough: the
missing mechanism must change the asymptotic order along one compatible
infinite history.

For finitely supported kernels `K_r`, a symmetric matrix `H` produces a
combined shift correlation `C_H(d)` and a quadratic energy.  Sidon uniqueness
allows represented differences to be filled by all shifts only when the
correlation has the correct sign, or when every negative shift is paid
explicitly.  Hou--Zhao demonstrates that several kernels can cooperate before
Cauchy--Schwarz, but its proved energy has no signed cross terms.[^doi:10.48550/arxiv.2607.01169]
The present review therefore distinguishes three things that are easy to
conflate: joint boundary feasibility, signed quadratic coupling, and a
uniform compatible-chain theorem.

The review is mechanism-centered rather than exhaustive history.  It checks
current primary versions, includes exact theorem/section scope, and treats
metadata searches only as discovery.  Finite constructions such as
Cilleruelo's explicit sequence are important benchmarks but remain below the
critical all-prefix density sought in Question 2.[^arxiv:1209.0326]

## 2. Critical infinite density bounds

Current primary theorems give explicit upper bounds for the liminf or average representation growth, but not the zero liminf or compatible construction in #1191.

Contributing papers:

- O'Bryant (2026) — On the Thickness of Infinite Generalized Sidon Sets, I [^arxiv:2606.28651]
- O’Bryant (2026) — On the Thickness of Infinite Generalized Sidon Sets, II [^arxiv:2607.23795]
- Táfula (2026) — Infinite Sidon-type sets for zero-sum linear forms [^doi:10.1007/s00605-026-02211-4]

Part I converts a scalar block-collision upper bound into the explicit liminf
upper bound through offset averaging and weighted Cauchy--Schwarz; its Section
3.1 then lists multi-`N`, martingale, entropy, and equality-profile ideas as
unproved possibilities.[^arxiv:2606.28651]  Part II extends the block method
to even-order `B_h` sets through half-sumsets, but at `h=2` gives no stronger
Sidon conclusion and introduces no cross-kernel sign mechanism.[^arxiv:2607.23795]

Táfula's matched zero-sum-form theorem is structurally closer to a common
parameter argument: one Fejér variable controls several nonnegative Fourier
factors and the result is summed over dyadic index blocks.  The output,
however, is average representation growth under density/gap assumptions, not
a negative covariance or sublogarithmic prefix budget.[^doi:10.1007/s00605-026-02211-4]
The corpus therefore converges on dyadic block energy as useful infrastructure
but supplies no proved signed order-changing interaction.

## 3. Joint kernels and correlation sign

Hou--Zhao proves cooperative boundary cover with diagonal direct-sum energy
and explicitly leaves controlled cross-kernel terms as future work; the
signed interpretation is our Route-C proposal.

Contributing papers:

- Hou--Zhao (2026) — Vector-valued smoothing for finite Sidon sets [^doi:10.48550/arxiv.2607.01169]

Lemma 2.1 allows individual kernels to fail the boundary-cover condition as
long as their weighted combination covers it.  Cauchy--Schwarz is then applied
in a Hilbert direct sum, and Proposition 3.1 turns the fixed-kernel boundary
problem into a strictly convex quadratic program with an explicit dual.
Section 4 verifies the final eight-kernel data with exact rational
arithmetic.[^doi:10.48550/arxiv.2607.01169]

This is a genuine escape from convexly averaging separately valid scalar
bounds, but not yet the desired signed escape.  Section 5 says that any future
cross-kernel coefficient matrix must satisfy an additional shiftwise
correlation-positivity constraint; matrix PSD by itself is not enough.
[^doi:10.48550/arxiv.2607.01169]  The internal positive-part audit sharpens
that interface: every negative off-shift contributes a mandatory explicit
penalty, and a PSD zero-mass scale contrast becomes trivial if it passes the
cost-free sign gate.  That is a scoped algebraic closure, not a claim that
Hou--Zhao's wider boundary mechanism is exhausted.

## 4. Entropy infrastructure and geometry loss

Goh supplies conditional entropy tools, but the fixed Sidon-support inequality depends only on the distribution and forgets spacings unless an extra geometry-sensitive conditioning variable is supplied.

Contributing papers:

- Goh (2026; arXiv first posted 2024) — On an entropic analogue of additive energy [^doi:10.2140/ent.2026.5.243]
- O'Bryant (2026) — On the Thickness of Infinite Generalized Sidon Sets, I [^arxiv:2606.28651]

O'Bryant identifies conditional expectations on block partitions and entropy
as possible replacements for the scalar energy method, but labels the whole
discussion nonrigorous.[^arxiv:2606.28651]  Goh proves entropy analogues of
additive energy and a conditional Sidon inequality.  Its Sidon proof only
uses that a sum determines the unordered input pair, so it contains no gaps,
endpoints, or scale births.[^doi:10.2140/ent.2026.5.243]

For the uniform distribution on an `m`-point Sidon set, diagonal sums occur
with probability `1/m^2` and off-diagonal unordered sums with probability
`2/m^2`; hence the entropy formula in the executive summary is exact.  This
closes only a naive route that sums independent fixed-prefix entropies.  Goh's
conditional formulation applies when the conditional law is already Sidon in
the paper's entropic sense; it does not establish that arbitrary geometric
conditioning preserves that hypothesis.  Subject to that extra obligation,
it leaves room for a common conditioning variable whose chain-rule deficit
remembers geometry.[^doi:10.2140/ent.2026.5.243]

## 5. Finite-to-infinite and source-quality gate

Explicit constructions remain below critical density, while a withdrawn finite extension record cannot support any theorem-level or infinite-history inference.

Contributing papers:

- Cilleruelo (2012) — Infinite Sidon sequences [^arxiv:1209.0326]
- Niu (2026) — Size-4 Counterexamples to the Sidon-Extension Conjecture [^arxiv:2604.25214]

Cilleruelo constructs an explicit infinite Sidon sequence with counting
function `x^(sqrt(2)-1+o(1))`, a genuine compatible infinite object but still
polynomially below the critical target.[^arxiv:1209.0326]  It is therefore a
construction benchmark, not a Question-2 solution.

The selected Niu record is a source-quality counterexample: the current arXiv
version is withdrawn, and its earlier named result was empirical over finite
ranges with conjectural continuation.[^arxiv:2604.25214]  It must not be used
as theorem evidence.  More generally, finite feasibility, SDP output, or a
large isolated ruler does not establish a compatible infinite history; every
transfer in this review is stopped at its actual quantifiers.

## Tensions surfaced in synthesis

### Suggested entropy route versus geometry-blind proved entropy

- **Side 1:** O'Bryant explicitly suggests entropy/reverse-martingale structure as a possible improvement, without a theorem. [^arxiv:2606.28651]
- **Side 2:** Goh's proved Sidon entropy inequality is fixed-distribution and geometry-blind unless additional conditioning carries geometry. [^doi:10.2140/ent.2026.5.243]

This is a methodological tension rather than a contradiction.  The corpus
supports entropy as language and supplies valid conditional inequalities, but
the only proved Sidon entropy in the selected papers is geometry-blind at a
fixed prefix.  The burden is therefore on a new theorem: define one
geometry-sensitive filtration and prove a strict, uniformly accumulating
chain-rule deficit.  Neither side currently supplies that theorem.

### Finite joint feasibility versus infinite signed order change

- **Side 1:** Hou-Zhao obtains a genuine cooperative multi-kernel finite secondary-term improvement. [^doi:10.48550/arxiv.2607.01169]
- **Side 2:** Current infinite-density theorems remain scalar/nonnegative and give only finite liminf constants or representation growth. [^arxiv:2606.28651][^doi:10.1007/s00605-026-02211-4]

This is a scope tension.  The finite joint theorem is proved and exact; the
infinite order-changing conclusion is simply outside its quantifiers.  The
corpus supports transferring the *architecture*—cooperative cover and exact
dual certification—but not transferring the finite `N^(1/4)` gain as evidence
for Question 1.  A successful extension must add compatible history and the
shiftwise sign/payment theorem that the finite diagonal energy does not need.


## Synthesis

The literature does not point to “more averaging” as the missing idea.  The
proved multi-kernel success comes from imposing feasibility only after
channels cooperate, while the current infinite arguments still discard the
relations between scales before their main inequality.  This suggests that
the next object should combine three layers at once: a common shift or
conditioning variable, a joint boundary/profile constraint, and an exact
dual whose slack measures incompatibility of near-equality profiles.

Signed quadratic coupling is the most literal realization, but it has a
hard algebraic cost.  Negative correlation cannot be filled over
unrepresented Sidon differences for free; zero-mass PSD contrasts with
nonzero effective energy necessarily develop negative lobes.  Therefore the
promising use of a signed term is not
as an isolated smaller energy.  It must be paired with a theorem that the
*actual compatible difference history* represents enough of the negative
shifts, or with a boundary/profile deficit carrying information not visible
in the aggregate correlation.

Entropy reaches the same fork.  For the uniform law on a finite Sidon prefix,
`H(X+X')` is determined by cardinality, so any gain must live in conditional
dependence between scales, not in that marginal sum distribution.  For a
nonuniform law the value depends on the probability vector, though still not
on the spacing geometry.  The most defensible research target is
therefore a finite-horizon inverse theorem: too many near-equality scales on
one compatible critical-cap chain force a uniform common-shift covariance,
boundary-dual slack, or conditional-entropy deficit.  No checked source proves
that statement; it is the precise gap left after the current method closures.

## Open questions and gaps

- **Shift-payment theorem.**  No source proves that a compatible critical
  Sidon difference set must represent enough of the negative correlation
  shifts of a designed joint kernel.  Start with exact finite primal/dual
  searches where every represented and omitted shift appears explicitly.
- **Boundary-normalized overlapping kernels.**  A subsequent exact internal
  probe shows that nonzero-mass overlap can satisfy PSD and every-shift
  positivity while improving the pure upper-energy expression.  The ratio can
  be made arbitrarily small only by collapsing mass and a Gram eigenvalue.
  The open task is therefore to fix the Hou--Zhao-style boundary/lower-energy
  normalization and retain a strict certified gain after that denominator is
  included.
- **Geometry-sensitive entropy.**  No checked theorem supplies a conditioning
  variable whose Sidon entropy deficit remembers gaps and telescopes across
  one nested history.  Begin from common dyadic partitions and audit terminal
  entropy/boundary terms before claiming a martingale.
- **Uniform inverse theorem.**  Finite multi-window instability is precedent,
  but no theorem prevents `1-o(1)` of the scales of a compatible critical-cap
  chain from being near equality.  This is the order-changing statement to
  formulate with all horizon quantifiers explicit.
- **Novelty and expert gate.**  The search is saturated only within its logged
  sources and suffered two rate-limited citation calls.  MathSciNet/zbMATH
  coverage and specialist review remain required before any novelty claim.

## Recommendations for further reading

Top-scored papers from the corpus, ranked by Phase 2 score (see Methodology appendix for the formula):

1. **O'Bryant (2026)** — On the Thickness of Infinite Generalized Sidon Sets,
   I: start here for the exact current Q1-scale theorem and its explicitly
   nonrigorous list of possible escapes.[^arxiv:2606.28651]
2. **Hou--Zhao (2026)** — Vector-valued smoothing for finite Sidon sets:
   the cleanest proved joint-kernel architecture, exact dual, and explicit
   cross-correlation caveat.[^doi:10.48550/arxiv.2607.01169]
3. **Goh (2026; arXiv first posted 2024)** — On an entropic analogue of additive energy: the
   relevant conditional entropy toolkit and the precise geometry-loss
   boundary.[^doi:10.2140/ent.2026.5.243]
4. **Táfula (2026)** — Infinite Sidon-type sets for zero-sum linear forms:
   a current common-Fourier-parameter dyadic mechanism whose nonnegative scope
   is easy to audit.[^doi:10.1007/s00605-026-02211-4]
5. **O'Bryant (2026)** — On the Thickness of Infinite Generalized Sidon Sets,
   II: useful for the structured half-sumset extension and for confirming what
   does not improve the `h=2` case.[^arxiv:2607.23795]

The Niu record is intentionally omitted from recommendations because it is
withdrawn; its inclusion in the ranked corpus is retained only as a
source-quality audit fixture.[^arxiv:2604.25214]

## Appendix A — Methodology

**Search strategy:** 18 queries across 4 federated sources — arxiv (7 queries), crossref (5 queries), openalex (5 queries), openalex_s2_citation_chase (1 queries).

**Saturation:** the per-query hit/new/merged counts and the search diagnostics
that gated Phase 1 → Phase 2 are preserved directly in
`research_state.json`.  The research-skill helper that originally rendered
the saturation view is not bundled in this workspace, so the report does not
claim a local command-level replay of that view.

**Ranking formula (Phase 2):**
```
score = 0.65·relevance + 0.1·log10(citations+1)/3 + 0.2·exp(-Δyears/5.0) + 0.05·venue_prior
```
Weights: alpha=0.65, beta=0.1, gamma=0.2, delta=0.05.

**Selection:** top 10 by score, triaged into deep (full-text agent fan-out) and
skim (abstract-only stub) tiers.  Per-paper `score_components` and
`triage_components` are preserved in state.  The skill-runtime triage helper
named in some state annotations is not included in this workspace.

## Appendix B — Self-critique

## Self-critique findings

The 2026-08-29 adversarial pass checked all fourteen required items. External theorem statements are anchored to exact primary versions, while the new positive-part and zero-mass results are self-contained internal deductions rather than novelty claims. The corpus is preprint-heavy (6/10 arXiv-hosted) because the frontier is moving in 2026; publisher versions were used where available. No author exceeds 20% of the selection. Citation-count metadata are mostly zero or missing, so citation rank was not used as a quality proxy.

Two tensions are surfaced rather than buried: O'Bryant's entropy/reverse-martingale suggestions versus the geometry-blind proved Sidon entropy inequality, and Hou-Zhao's finite joint feasibility versus the absent infinite signed order change. The search reached script-certified saturation after exact-title zero-novelty rounds, but the Semantic Scholar citation chase had two rate-limited calls and the novelty conclusion remains a dated qualified null. The withdrawn arXiv:2604.25214 record is explicitly barred from theorem use.

The strongest counter-argument is preserved: the new no-go closes only free negative-shift completion, cost-free PSD zero-mass contrasts with nonzero effective energy, and point-mass channel couplings. Pure-energy overlap is feasible, but boundary-normalized overlapping-kernel gains, actual difference-set payment, geometry-sensitive conditioning, profile incompatibility, and compatible infinite histories remain open.

## Bibliography

Full selected bibliography is stored beside this report as
`SELECTED_BIBLIOGRAPHY.bib`.  The selected identifiers and metadata needed to
audit it are preserved in `research_state.json`; the skill-runtime export
helper used during generation is not bundled here, so no unavailable local
replay command is asserted.

Anchor index:

[^arxiv:2606.28651]: O'Bryant (2026). On the Thickness of Infinite Generalized Sidon Sets, I
[^doi:10.48550/arxiv.2607.01169]: Hou--Zhao (2026). Vector-valued smoothing for finite Sidon sets — doi:10.48550/arxiv.2607.01169
[^arxiv:2607.23795]: O’Bryant (2026). On the Thickness of Infinite Generalized Sidon Sets, II — arXiv:2607.23795v1
[^doi:10.1007/s00605-026-02211-4]: Táfula (2026). Infinite Sidon-type sets for zero-sum linear forms — doi:10.1007/s00605-026-02211-4
[^arxiv:1209.0326]: Cilleruelo (2012). Infinite Sidon sequences
[^doi:10.1016/j.jnt.2025.07.007]: Balasubramanian et al. (2026). The m-th element of a Sidon set — doi:10.1016/j.jnt.2025.07.007
[^doi:10.2140/ent.2026.5.243]: Goh (2026; arXiv first posted 2024). On an entropic analogue of additive energy — doi:10.2140/ent.2026.5.243
[^arxiv:2411.12911]: Czerwinski et al. (2024). On large Sidon sets
[^arxiv:2104.06501]: Nathanson (2021). An inverse problem for finite Sidon sets
[^arxiv:2604.25214]: Niu (2026). Size-4 Counterexamples to the Sidon-Extension Conjecture
