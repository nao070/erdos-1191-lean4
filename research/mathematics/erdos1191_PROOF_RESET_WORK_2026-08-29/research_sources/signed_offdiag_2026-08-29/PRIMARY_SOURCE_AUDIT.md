# Primary-source audit: signed off-diagonal and nonlinear Route C

Date: 2026-08-29 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Scope: primary-source mechanism audit and qualified novelty check.  This is
not evidence that an unlocated theorem does not exist.

## Question and method

The search asked which proved mechanisms can turn a common-shift signed
off-diagonal/cross-kernel energy, aggregate correlation positivity,
reverse-martingale deficit, or entropy into an order-changing critical-density
bound on one compatible infinite Sidon history.

The persistent `research_state.json` records 17 discovery queries across
arXiv, OpenAlex, and Crossref, 194 papers before citation chasing, exact-title
saturation rounds, ranking, a manually protected ten-paper selection, six
full-text evidence records, and one OpenAlex/Semantic Scholar citation chase.
That chase added 16 records; two Semantic Scholar calls returned HTTP 429, so
the citation graph is explicitly partial.  Exact primary records and current
versions were then checked directly.  Discovery metadata was never treated as
theorem evidence.

## 1. Hou--Zhao: the proved joint mechanism is diagonal in energy

Primary source: Jianfeng Hou and Hongbin Zhao,
[*Vector-valued smoothing for finite Sidon sets*, arXiv:2607.01169v2](https://arxiv.org/html/2607.01169v2).

Theorem 1.1 proves

\[
 F(N)\le N^{1/2}+0.9435N^{1/4}+O(1).
\]

The exact constant certified in Section 4 is
`0.943492590...`.  Lemma 2.1 lets several probability kernels cooperate in a
weighted boundary-cover constraint.  Crucially, the proved energy is still

\[
 \mathcal E=\sum_r\lambda_r\|1_A*K^{(r)}\|_2^2,
\]

so every autocorrelation is individually nonnegative.  Proposition 3.1 gives
the explicit strictly convex boundary primal and its dual

\[
 \Phi_*=\max_{y\ge0}\left(c^{\mathsf T}y-\frac14y^{\mathsf T}Gy\right).
\]

The transferable mechanism is therefore **joint boundary feasibility before
Cauchy--Schwarz**, plus an exact primal/dual certificate.  It is not an average
of separately valid scalar bounds.

Section 5 names “controlled cross-kernel terms” as future work and states the
exact warning relevant here: PSD of the coefficient matrix is insufficient;
the combined correlation must be nonnegative at every nonzero shift.
Interpreting those terms through signed off-diagonal coefficients is the
present Route-C proposal, not wording or a construction from Hou--Zhao.  The
paper contains no such signed construction, compatible infinite filtration,
or order-changing theorem.  Its result is a finite `N^(1/4)` secondary-term
improvement.

## 2. O'Bryant I and II: proved constants, unproved nonlinear suggestions

Primary sources:

- Kevin O'Bryant,
  [*On the Thickness of Infinite Generalized Sidon Sets, I*, arXiv:2606.28651v3](https://arxiv.org/html/2606.28651v3);
- Kevin O'Bryant,
  [*On the Thickness of Infinite Generalized Sidon Sets, II*, arXiv:2607.23795v1](https://arxiv.org/abs/2607.23795v1).

Part I, Theorem 1 proves

\[
 \liminf_{n\to\infty}{A(n)\over\sqrt{n/\log n}}
 \le {2\sqrt g\over\sqrt{\log2}}.
\]

For ordinary Sidon sets this gives the positive universal **upper bound**
`2/sqrt(log 2)` for the displayed liminf, rather than the zero upper bound
required by Question 1.  It does not assert that the liminf is positive or
equal to this constant.  The proof averages a scalar block collision energy
over offsets, selects an `N`-dependent offset, and applies weighted
Cauchy--Schwarz.

Section 3.1 is explicitly nonrigorous.  It suggests averaging several `N`, an
infinite-energy formulation, reverse-martingale conditional expectations,
entropy, and exploiting instability away from the Cauchy equality profile.
These are valuable design instructions, not theorems.

Part II proves explicit liminf constants for even-order `B_h` sets through a
half-sumset block energy.  At `h=2` it supplies no new Sidon conclusion beyond
Part I and contains no cross-kernel covariance or entropy deficit.

## 3. Goh: the proved fixed-prefix Sidon entropy is geometry-blind

Primary source: Marcel K. Goh,
[*On an entropic analogue of additive energy*, arXiv:2406.18798v4](https://arxiv.org/abs/2406.18798v4),
[publisher DOI](https://doi.org/10.2140/ent.2026.5.243).

Proposition 11 proves that a random variable supported on a Sidon set obeys

\[
 \mathsf s(X)\ge H(X)-1.
\]

Its proof uses only that `X+X'` identifies the unordered pair; recovering the
order costs at most one bit.  Proposition 12 gives a conditional version only
when the conditional law is already Sidon in Goh's entropic sense.  It does
not say that arbitrary geometry-based conditioning preserves that hypothesis.

There is an exact stronger geometry-blind calculation for the uniform law on
an `m`-point Sidon set.  The `m` diagonal sums have probability `1/m^2`, and
the `binom(m,2)` off-diagonal unordered sums have probability `2/m^2`.
Therefore

\[
 \boxed{H(X+X')=2\log_2m-{m-1\over m}.}
\]

This depends only on `m`, not on gaps, endpoints, birth scales, or a critical
envelope.  Consequently an entropy argument that evaluates each uniform
prefix separately has no geometry-sensitive deficit to accumulate.  A
surviving entropy route must introduce one common geometry-sensitive
conditioning/filtration and prove a strict chain-rule loss.  Goh does not
prove such a reverse-martingale telescope.

## 4. Táfula: common Fourier parameter, but only nonnegative squares

Primary source: Christian Táfula,
[*Infinite Sidon-type sets for zero-sum linear forms*, arXiv:2607.20753v1](https://arxiv.org/abs/2607.20753v1),
[publisher DOI](https://doi.org/10.1007/s00605-026-02211-4).

Theorem 1.1 obtains average representation growth for matched zero-sum forms.
Lemma 2.1 inserts a nonnegative Fejér kernel and integrates a product
`prod_j |F_N(c_j alpha)|^2` at one common Fourier parameter.  Summing over
dyadic index blocks gives the density conclusion.

The common parameter is transferable architecture.  The signed mechanism is
not: every factor is a nonnegative absolute square, and the conclusion is
average representation growth rather than an `o(log J)` compatible-prefix
deficit.

## 5. Closest additional precedents

- Carter--Hunter--O'Bryant,
  [*On the diameter of finite Sidon sets*, arXiv:2310.20032](https://arxiv.org/abs/2310.20032),
  proves an exact missing-difference/occupancy-variance identity and combines
  several window sizes.  It is a real finite precedent for “one profile
  cannot optimize every window,” but remains unsigned and near the finite
  `sqrt(N)` extremal regime.
- Matolcsi--Vinuesa,
  [*Improved bounds on supremum of autoconvolutions*, arXiv:0907.1379v2](https://arxiv.org/abs/0907.1379v2),
  discusses using different kernel pairs or Fourier coefficients to exclude
  different regions of one profile.  It concerns continuous nonnegative
  autoconvolution, not one infinite critical Sidon history.
- Kocuk--van Hoeve,
  [*A Computational Comparison of Optimization Methods for the Golomb Ruler Problem*, arXiv:1902.08660](https://arxiv.org/abs/1902.08660),
  gives a finite lifted SDP relaxation and reports it as very weak.  It is a
  certificate/red-team precedent, not an asymptotic method.
- Ortega--Prendiville,
  [*Arithmetic progressions in sets of small doubling*, arXiv:2110.13447](https://arxiv.org/abs/2110.13447),
  uses Fejér/van der Corput positivity for finite near-extremal Sidon sets.
  The critical `sqrt(N/log N)` regime is far below that hypothesis.

## 6. Withdrawn-record correction

The current [arXiv:2604.25214v3](https://arxiv.org/abs/2604.25214v3),
*Size-4 Counterexamples to the Sidon-Extension Conjecture*, is withdrawn.  Its
official record says a MathOverflow answer already gave a stronger result.
The prior named “main empirical theorem” was finite computational evidence
with conjectural continuation.  It must not be used as theorem-level support,
and in any case concerns finite perfect-difference-set extension rather than
critical-density infinite Sidon energy.

## 7. Synthesis and qualified novelty

The strongest defensible architecture is:

1. use Hou--Zhao-style cooperation in a boundary or feasibility constraint;
2. keep one common shift/conditioning variable across scales;
3. use a Carter--Hunter--O'Bryant-type profile incompatibility or a genuinely
   geometry-sensitive entropy chain-rule deficit;
4. certify the finite kernel/dual subproblem exactly;
5. prove uniformity over compatible finite horizons before invoking any
   infinite branch.

The new internal positive-part and zero-mass-contrast theorem shows why the
most obvious signed quadratic realization fails: a PSD contrast with zero
total mass and nonzero effective energy cannot be nonnegative at every
off-shift, while any negative off-shift carries an exact positive-part
payment.  A subsequent internal probe shows that nonzero-mass overlap can
pass the sign gate and reduce pure upper energy, but only an as-yet-unfixed
boundary/lower-energy normalization can determine whether that gain is
useful.  These are internal theorems, not literature novelty claims.

The bounded primary-source search found no executed theorem combining all of

- signed off-diagonal cross-kernel energy;
- the required sign/payment at every common nonzero shift;
- one compatible infinite critical-density history; and
- a sublogarithmic or order-changing deficit.

This is only a **qualified null**.  Joint kernels, multiscale profile
incompatibility, entropy, Fejér positivity, and SDP certificates all have
prior art.  Only the precise geometry-sensitive signed combination remains a
plausible novel slice, subject to broader database coverage and expert review.

No checked source proves or disproves Question 1 or Question 2.

## 8. Centered multiband follow-up

The later internal box audit changes the exact missing interface.  Full
dyadic box covariance is dominated by diagonal Parseval mass, but a
prefix-changing one- or two-band path produces a centered harmonic carrier
with exact internal ownership.  Firecrawl, Exa, Consensus, and SciSpace were
then queried for the remaining **common signed capacity** step.  They
resurfaced the already relevant finite Sidon/Fourier/smoothing literature and
general harmonic-analysis analogies, but no checked theorem placed this
carrier and a critical-history harmonic floor into one opposite-sign,
disjoint-owner inequality.

This follow-up narrows the project bottleneck; it does not strengthen the
qualified null into an absence or novelty claim.  The carrier theorem is
project-internal, and Question 1, Question 2, publication, and prize status
remain unresolved.
