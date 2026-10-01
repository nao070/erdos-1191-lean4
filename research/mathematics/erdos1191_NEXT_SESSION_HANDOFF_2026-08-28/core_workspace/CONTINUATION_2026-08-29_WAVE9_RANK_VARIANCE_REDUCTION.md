# Erdős Problem #1191 — Wave 9 rank-variance reduction

**Date:** 2026-08-29 (Asia/Tokyo)  
**Status:** rigorous scalar reduction, core isolation, cross-ratio potential,
exact no-go probes, and current literature delta; P15 and Problem #1191 remain open  
**Prize status:** no claim is ready

## 1. Outcome

Wave 8 left the positive fixed-`H` birth budget

\[
 \mathcal B_H(J)=
 \sum_{k=0}^{J}{1\over N_{2m_k}^2}
 \sum_{\substack{0\le i<j<2m_k\\j\ge m_k}}
 h_i h_j\Phi^{(2m_k)}_{ij},
 \qquad m_k=2^k,
\tag{1}
\]

and asked for `B_H(J)=o(log J)` on one infinite eventually critical Golomb
ruler.  The matrix kernel and its separation into shell and rank-one pieces
are not needed in the statement of the remaining theorem.  Define

\[
 \nu_n={1\over N_n}\sum_{i=0}^{n-1}h_i\delta_{i/n},
 \qquad
 V_n=\operatorname {Var}_{\nu_n}(u),
\tag{2}
\]

where `h_0=1`, `h_i=a_i-a_(i-1)` and `N_n=a_(n-1)+1`.  Then the new global
comparison is

\[
 \boxed{
 {4\over49}\sum_{k=1}^{J+1}V_{2^k}
 \le \mathcal B_H(J)
 \le {36\over35}\sum_{k=1}^{J+1}V_{2^k}.}
\tag{3}
\]

Consequently P15 is equivalent, up to absolute constants and a finite
initial term, to the scalar statement

\[
 \boxed{
 \sum_{k\le J} \operatorname {Var}_{\nu_{2^k}}(u)=o(\log J).}
\tag{RV}
\]

This is a genuine simplification: `RV` includes all rank-one births and all
shell births automatically.  It also exposes the exact missing mechanism.
The critical envelope and distinct adjacent gaps alone force the same sum to
be `Omega(log J)`; therefore the desired upper must use uniqueness of
**non-adjacent contiguous sums** on the one fixed infinite branch.

Nothing below proves `RV`.  Thus this note is not a solution or a prize
claim.

## 2. One-step scalar birth identity

For one update `m -> 2m`, set

\[
 \rho_m={N_m\over N_{2m}}
\]

and define the scalar birth increment

\[
 R_m={1\over N_{2m}^2}
 \sum_{\substack{0\le i<j<2m\\j\ge m}}
 h_i h_j\left({j-i\over2m}\right)^2.
\tag{4}
\]

The weighted pair identity gives

\[
 V_n={1\over N_n^2}
 \sum_{0\le i<j<n}h_i h_j\left({j-i\over n}\right)^2.
\tag{5}
\]

The old pairs in the common `2m` grid contribute exactly
`rho_m^2 V_m/4`.  Removing them from the complete `2m` pair sum proves

\[
 \boxed{R_m=V_{2m}-{\rho_m^2\over4}V_m.}
\tag{6}
\]

This identity is algebraic and does not use the Golomb property.

## 3. The fixed-`H` kernel is uniformly scalar

For `u=i/(2m)`, `v=j/(2m)` and `x=1-u-v`, direct multiplication by the
Wave 8 Lyapunov matrix gives

\[
 \Phi^{(2m)}_{ij}
 =(v-u)^2q(x),
 \qquad
 q(x)={16\over15}x^2+{16\over105}x+{4\over35}.
\tag{7}
\]

Every birth pair has `-1<x<=1/2`.  The quadratic has its minimum at
`x=-1/14`, and its maximum on the closed envelope at `x=-1`.  Hence

\[
 \boxed{{16\over147}\le q(x)\le {36\over35}.}
\tag{8}
\]

If `B_m` denotes the summand of (1), (4), (7), and positivity of every
birth-pair weight give

\[
 {16\over147}R_m\le B_m\le {36\over35}R_m.
\tag{9}
\]

Unlike the signed shell-square expansion, no boundary fan remains in (9).

## 4. Global telescope and proof of (3)

Write `W_k=V_(2^k)` and `rho_k=N_(2^k)/N_(2^(k+1))`.  Summing (6) from
`k=0` through `J`, and using `W_0=V_1=0`, gives the exact formula

\[
 \sum_{k=0}^{J}R_{2^k}
 =W_{J+1}+\sum_{k=1}^{J}
 \left(1-{\rho_k^2\over4}\right)W_k.
\tag{10}
\]

Since `0<rho_k<1`,

\[
 {3\over4}\sum_{k=1}^{J+1}W_k
 \le\sum_{k=0}^{J}R_{2^k}
 \le\sum_{k=1}^{J+1}W_k.
\tag{11}
\]

Combining (9) and (11) yields (3), because
`(16/147)(3/4)=4/49`.  This proves both directions of the equivalence
between P15 and `RV`.

## 5. A universal distinct-gap lower barrier

The scalar formulation admits a short lower bound which uses only adjacent
difference uniqueness.

### Theorem

Let the first `n>=8` marks form a Golomb ruler.  Then

\[
 \boxed{V_n\ge {n^2\over512N_n}.}
\tag{12}
\]

### Proof

Let `c` be the weighted mean of the integer ranks `0,...,n-1`.  Among those
ranks, the open interval `|i-c|<n/4` contains at most `n/2+1` integers.
After removing the artificial index `i=0`, at least

\[
 n-(n/2+1)-1=n/2-2\ge n/4
\]

genuine gap indices remain at distance at least `n/4` from `c`.  Put their
number equal to `q`.  Their weights are distinct positive integers, because
the genuine adjacent gaps of a Golomb ruler are distinct.  Their total weight
is therefore at least

\[
 1+\cdots+q={q(q+1)\over2}\ge{q^2\over2}\ge {n^2\over32}.
\]

It follows that

\[
 \sum_i h_i(i-c)^2
 \ge {n^2\over16}{n^2\over32}={n^4\over512}.
\]

Dividing by `N_n n^2` proves (12).  `square`

If one hypothetical infinite Golomb ruler obeyed

\[
 N_n\le Cn^2\log(2n)
\]

eventually, then at every sufficiently large dyadic `n=2^k`,

\[
 V_{2^k}\ge {1\over512C(k+1)\log2}.
\tag{13}
\]

Equations (3) and (13) give the explicit necessary lower barrier

\[
 \boxed{
 \mathcal B_H(J)
 \ge {1\over6272C\log2}\log J+O_C(1).}
\tag{14}
\]

Thus the missing `o(log J)` upper cannot follow from the critical diameter
cap, adjacent-gap distinctness, positivity, or the covariance recursion.  It
must contradict (14) by exploiting the rest of the Golomb condition: all
non-adjacent contiguous sums are distinct across the same infinite history.

## 6. Exact verification

The executable audit is

- `core_workspace/endpoint_variance/wave9_rank_variance_reduction.py`;
- `core_workspace/endpoint_variance/test_wave9_rank_variance_reduction.py`.

It checks (5)--(11) with `fractions.Fraction` on the perfect four-mark ruler,
the authenticated 64- and 128-mark fixtures, and a non-Golomb control showing
that the reduction itself is algebraic.  It separately checks (12) on the
authenticated Golomb fixtures and rejects duplicate genuine gaps.

Observed focused result on 2026-08-29:

```text
8 passed
Ruff check: all checks passed
```

For `(0,1,4,6)`, the exact values are

\[
 \sum V_k={97\over784},\qquad
 \sum R_k={6\over49},\qquad
 \mathcal B_H={1199\over27440}.
\]

## 7. Next admissible target

The highest-value next lemma can now be stated without matrices:

> On one infinite eventually critical Golomb ruler, charge the dyadic
> rank-variance mass `V_(2^k)` to globally distinct non-adjacent contiguous
> sums with bounded overlap simultaneously in numerical magnitude and rank
> lag, strongly enough to prove `sum_(k<=J)V_(2^k)=o(log J)`.

A proof must use an unbounded history or the exact infinite-survival label.
Finite Erdős--Turán windows, local density, adjacent-gap uniqueness, and a
fixed number of recent prefixes remain ineligible for the reasons already
certified in Waves 4--8.

## 8. Long-rank/two-large-endpoint core

The concurrent Carleson analysis converts the scalar formulation into a
literal positive core.  At an update `m -> L=2m`, write `p_i=h_i/N_L`.  For
`0<theta<=1` and `eta>0`, call a birth pair core when

\[
 j-i>\theta L,
 \qquad h_i>{\eta N_L\over L},
 \qquad h_j>{\eta N_L\over L}.
\]

The short-rank and small-endpoint terms satisfy the deterministic estimate

\[
 \boxed{
 \mathcal B_m\leq\mathcal B_m^{\rm core}(\theta,\eta)
 +{18\over35}\theta^2+{36\over35}\eta.}
\tag{15}
\]

Taking `theta_j^2=eta_j=1/(j log j)` makes the sum of the discarded terms
`O(log log J)=o(log J)`.  Thus P15 is reduced without target-scale loss to
long-rank pairs whose two endpoint gaps are both large.

For dyadic bands

\[
 R\leq j-i<2R,\quad X\leq h_i<2X,\quad
 Y\leq h_j<2Y,\quad Z\leq D_{i,j}<2Z,
\]

the exact tile count `q=q_m(R,X,Y,Z)` obeys

\[
 \boxed{
 q\leq\min\left(A_XA_Y,\ Z,\ {2R^2N_L\over Z}\right),}
\tag{16}
\]

where `A_X<=min(L,X,floor(N_L/X))` and likewise for `A_Y`.  Its charge is at
most

\[
 \boxed{
 {144\over35}{R^2\over L^2}{\min(4XY,Z^2)\over N_L^2}
 \min\left(A_XA_Y,Z,{2R^2N_L\over Z}\right).}
\tag{17}
\]

These are valid bounded-overlap constraints, but their direct summation loses
the full logarithm.  Scaled Erdős--Turán rulers make this obstruction exact:
for a changing `L`-mark family with dilation `s_L=ceil(log L)`, numerical
difference occupancy tends to zero while the terminal birth charge remains
at least `1/2352`.  Hence local numerical sparsity, even with a recent-prefix
critical constant, cannot prove P15.  The family changes with `L`, so this is
not an infinite counterexample.

Full proof: `endpoint_variance/WAVE9_BIRTH_BUDGET_CARLESON_ANALYSIS_2026-08-29.md`.

## 9. Exact finite probe and closed pointwise surrogates

The Wave 9 probe computes every positive birth atom with `Fraction`, partitions
it simultaneously by rank lag and difference magnitude, and regenerates a
byte-stable JSON certificate.

- All `1,672` normalized four-mark all-prefix-`C=1` rulers were exhausted.
  Every one has `Delta B_2<Delta B_1`, but the literal one-atom-per-cell and
  occupancy-at-most-rank-band-lower claims already fail on `(0,1,4,6)`.
- All `1,468` normalized eight-mark rulers with terminal at most `40` were
  exhausted; `1,146` satisfy every `C=1` prefix cap.  Of those, `128` have
  `Delta B_4>Delta B_2`, so pointwise monotone decay is false.  All `1,146`
  refute the stronger literal harmonic schedule `2 Delta B_4<=Delta B_2`.
- The minimum-diameter monotonicity witness is
  `(0,4,12,13,19,30,33,35)`, with exact positive margin
  `446533/341397504`.
- At the terminal 512-mark epoch, the macroscopic core quadrant contributes
  more than `3/5` of the full birth increment on both the reconstructed
  modified-greedy prefix and the Erdős--Turán fixture.  The exact shares are
  `13242199924089976348090/20619808566184045294713` and
  `2738923201748154301783/4115217089595122117052`.
- Static cell occupancy divided by its rank-band lower endpoint reaches
  `553/4` on the all-prefix-`C=1` modified-greedy 512 prefix and `647/2` on
  the Erdős--Turán 512 fixture.

These are finite falsifications and calibrations.  They neither certify
infinite survival nor refute a history/Cesaro theorem.

Executable artifacts:

- `endpoint_variance/wave9_birth_budget_probe.py`;
- `endpoint_variance/test_wave9_birth_budget_probe.py`;
- `endpoint_variance/wave9_birth_budget_certificate_2026-08-29.json`;
- `endpoint_variance/WAVE9_BIRTH_BUDGET_PROBE_2026-08-29.md`.

## 10. A weighted cross-ratio potential

For genuine nonadjacent gaps `i<j`, put

\[
 M=a_{j-1}-a_i,\qquad D=a_j-a_{i-1},\qquad
 C_{ij}=\log{(M+h_i)(M+h_j)\over MD}.
\tag{18}
\]

Then `C_(ij)>0` and

\[
 \boxed{{h_i h_j\over D^2}\leq C_{ij}.}
\tag{19}
\]

The quadratic-rank sum

\[
 S_n=\sum_{1\leq i<j\leq n-1\atop j-i\geq2}
 \left({j-i\over n}\right)^2C_{ij}
\]

has an exact Abel expansion.  After multiplication by `n^2`, the positive
coefficients occur only on the two outer boundaries: they are `4` at length
two and `2r-1` at length `r>=3`.  The full-span coefficient is
`-(n-2)^2`; strict-interior coefficients are `-4` at length one, `-1` at
length two, and `-2` thereafter.  The positive and negative coefficient
masses both equal `2(n-2)^2`.

Let `delta_n^circ=gcd(h_2,...,h_(n-2))`, `K=binom(n-2,2)`, `A=n-3`,
`B=n-4`, and

\[
 I_{\min}=2\log(A!)+\log((K-B)!)+\log(K!).
\]

All strict-interior differences divided by `delta_n^circ` are distinct positive
integers.  The rearrangement inequality therefore yields the scale-invariant
Golomb bound

\[
 \boxed{
 S_n\leq\left({n-2\over n}\right)^2
 \log{a_{n-1}\over\delta_n^\circ}-{I_{\min}\over n^2}
 =\log{a_{n-1}\over\delta_n^\circ n^2}+1+\log2+o(1).}
\tag{20}
\]

There is a strictly sharper version which uses the strict-interior minimum as
well as the lattice.  Put

\[
 h_n^\circ=\min(h_2,\ldots,h_{n-2}),\qquad
 q={h_n^\circ\over\delta_n^\circ}\in\mathbb N,qquad R=K-B,
\]

write `(q)_t=q(q+1)...(q+t-1)`, and define

\[
 \Phi_n(q)=2\log{(q)_A\over q^A}
 +\log{(q)_R\over q^R}+\log{(q)_K\over q^K}.
\]

The normalized strict-interior quotients are distinct integers at least `q`,
so the same rearrangement argument gives

\[
 \boxed{
 S_n\leq\left({n-2\over n}\right)^2
 \log{a_{n-1}\over h_n^\circ}-{\Phi_n(q)\over n^2}.}
\tag{20a}
\]

Term by term, (20a) dominates (20); at `q=1` its correction is exactly
`I_min`.  This is the strongest bound available from the Abel coefficient
multiset, strict-interior minimum, and lattice gcd alone.

For one fixed infinite integer branch, `delta_n^circ` is a nonincreasing divisor
sequence and hence eventually stabilizes.  Formula (20) is stronger than the
unconditional boundary bound, and (20a) strengthens it further.  Together they
make explicit that common dilation is not the missing mechanism.  Under the
critical cap the single-state estimate is still only `O_C(log log n)`, whose
sum through `J` dyadic epochs can be `O_C(J log J)`, so it does not prove P15.

Retaining the factor `(D/N_n)^2` gives a closer state potential `P_n` and a
birth potential `X_m` which majorizes the genuine nonadjacent birth charge up
to `36/35`.  They satisfy the exact recursion

\[
 \boxed{X_m=P_{2m}-{1\over4}\left({N_m\over N_{2m}}\right)^2P_m.}
\tag{21}
\]

Consequently `sum X_m` is between `3/4` and `1` times the sum of the dyadic
state potentials.  This is a valid cross-epoch potential, but it recreates a
positive state sum rather than telescoping to a terminal boundary.  A changing
scaled Erdős--Turán family has terminal `X_(L/2)>=1/4096`; hence no local
occupancy-density repair is available.

The exact coefficient and factorial identities are independently executable
in `endpoint_variance/wave9_cross_ratio_telescope.py` and
`endpoint_variance/test_wave9_cross_ratio_telescope.py`.  The full proof and
local no-go are in
`endpoint_variance/WAVE9_WEIGHTED_CROSS_RATIO_2026-08-29.md`.

## 11. Current primary literature and a hereditary rank-lag constraint

A 2026-08-29 delta search continued the Wave 8 state rather than restarting it.
The scripted state now contains `750` deduplicated records over `31` logged
queries; overall mechanical saturation is false.  Independent Exa,
Firecrawl, Consensus, and SciSpace passes converged on the same closest sources.
Consensus was quota-blocked, Firecrawl semantic searches were empty but known-ID
reads succeeded, and semantic results were used only for discovery.

Ma--Yi Theorem 4.1 and Shearer's difference-triangle LP give the closest exact
rank-lag/magnitude interface.  Transplanted to one nested branch, they prove the
following new project lemma.  For any finite dyadic epoch set `E` and
`1<=q_m<=m`, let

\[
 M_E=\sum_{m\in E}m q_m.
\]

Selecting `a_j-a_(j-s)` for `1<=s<=q_m` and `m<=j<2m` gives globally distinct
birth differences, so

\[
 \boxed{
 {M_E(M_E+1)\over2}
 \leq\sum_{m\in E}N_{2m}{q_m(q_m+1)\over2}.}
\tag{W9-RLP}
\]

This is hereditary and valid on one branch, but it controls difference lengths
linearly.  It does not control `h_i h_j Phi_ij`, the two-large-endpoint core,
or the independent rank-one weight.  No checked primary source supplies that
upgrade.  See
`research_sources/WAVE9_P15_LITERATURE_DELTA_2026-08-29.md` and
`../research_sources/wave9_literature_state/PRIMARY_SOURCE_AUDIT.md`.

## 12. Narrowed Wave 10 target

The surviving theorem is now free of matrix ambiguity:

> On one fixed infinite eventually `C`-critical Golomb branch, prove that the
> long-rank/two-large-endpoint core tiles have cumulative exact product/kernel
> mass `o(log J)`.  Equivalently, prove a survival-conditioned non-saturation
> estimate for the dyadic rank-variance or retained primitive cross-ratio state
> potentials.

A concrete next attack is a laminar weighted incomplete-difference-triangle LP.
Its constraint set should contain `(W9-RLP)` for every epoch subset and lag
cutoff, the four-parameter tile inequalities (16)--(17), and the primitive
cross-ratio coefficients.  Its objective must remain the exact
`h_i h_j Phi_ij/N_(2m)^2` core.  Any finite dual certificate is exploratory
unless it is made uniform under the exact `surv_C=infinity` label.

Pointwise decay, local numerical density, static rank/magnitude cells, common
dilation, and positive-state telescoping are now rigorously closed routes.
P15, Question 1, Question 2, and the prize claim remain open.
