# Wave 7 adversarial audit: complete birth ledger and finite-window boundary

**Date:** 2026-08-28  
**Audit target:** `WAVE7_GLOBAL_BAND_RENEWAL_POTENTIAL_2026-08-28.md`
and `complete_birth_ledger.py`  
**Verdict:** the complete-birth partition, wedge ledger, summable potential,
the exact 512-mark comparison, and the growing-window comparison are
mathematically sound.  Two statements need narrow repairs; no certificate-
affecting software defect was found.  None of the audited material resolves
Erdős Problem #1191.

## 1. Claim-by-claim classification

| Claim | Classification | Adversarial finding |
|---|---|---|
| Cross-family indices (6)--(8) | **PROVED** | Solving `j-i=k` with `i<m<=j<2m` gives exactly `t_0=max(0,k-m)` through `t_1=min(m-1,k-1)`, hence `min(k,2m-k)` pairs.  There is no endpoint off-by-one. |
| Difference identity (9)--(10) | **PROVED** | Since `a_j=N_(j+1)-1`, the difference is `N_(m+k-t)-N_(m-t)`.  Substitution of both discrepancy profiles gives (10), including the sign of `E^-`. |
| Full-rhombus bands and thresholds (12)--(14) | **PROVED** | Both discrepancy errors contribute at most `D^-+D^+`.  The affine center is linear in `t`, so its extrema occur at the two admissible endpoints.  Its coefficients are nonnegative and sum to `k`, proving `alpha<=tau`. |
| Cross-family global injectivity | **PROVED** | For dyadic `m`, the right endpoints lie in the pairwise disjoint blocks `[m,2m-1]`.  Thus endpoint pairs cannot repeat between epochs, and Golomb uniqueness converts pair injectivity into numerical-difference injectivity. |
| Newborn-internal indices (15)--(19) | **PROVED** | The range `1<=v<=m-r` gives precisely all pairs `m<=i<j<2m` of lag `r`; the discrepancy difference has absolute value at most `2D^+`. |
| Complete birth partition and threshold ledger (20) | **PROVED** | Every right rank `j>=1` has one dyadic birth block.  Within it, `i<m` is cross and `i>=m` is internal.  These alternatives are exhaustive and disjoint.  Activated differences are distinct positive integers at most `floor(T)`. |
| Reciprocal endpoint (21) | **PROVED** | For `gamma>=1`, `1/gamma=1/X+int_gamma^X t^-2 dt`; using `S_full(t)<=floor(t)<=t` gives `1+log X`. |
| Quadratic lag floor (22) | **PROVED** | The `ell+1` consecutive marks determine `binom(ell+1,2)` distinct positive integer differences, all no larger than their total span. |
| Wedge ledger (23) | **PROVED** | A counted lag at least `K` lies in the exact integer interval `[K(K+1)/2,floor(T)]`.  Global Golomb uniqueness supplies the capacity bound. |
| Exact first moment (24)--(25) | **NEEDS MINOR REPAIR** | The summation is correct for `floor(T)>=1`, but `R(T)=max{K:K(K+1)/2<=floor(T)}` is undefined when `0<=T<1`.  Define `R(T)=0` when this set is empty; then (25) holds for every stated `T>=0`. |
| Coarse `2 sqrt(2) T^(3/2)` bound (26) | **PROVED** | `R<=sqrt(2 floor(T))` and `floor(T)+1<=2T` for `T>=1`; dropping the negative cubic term gives the displayed constant. |
| Fractional Carleson bound (27)--(28) | **PROVED** | Every nonempty family's upper threshold is at least one because it bounds an actual positive integer difference.  Tonelli/layer cake with exponent `3/2+epsilon` gives the stated constant; monotone convergence handles infinitely many epochs. |
| E–T Golomb property (29) | **PROVED** | Equal integer differences first force equal rank increments because the residual difference has absolute value strictly below `2p`; reduction modulo odd `p` then forces equal left endpoints. |
| Moduli and all `256<=n<=512` critical caps (30)--(31) | **PROVED** | The exact values and 257 rationally certified logarithmic caps are reproduced by the verifier.  The minimum slack is 96.  This is only a recent compatible window, not a `C=1` claim for the early prefixes. |
| Covariance normalization and fraction (32) | **PROVED** | The gap weights sum to each prefix's own modulus.  Under rank halving, `f(u/2)=(f(u)+u)/4`, so the transported `00` entry is `(M00+2M01+M11)/16`; division is by `N_512`, as required. |
| One-step `W_2` upper bound and strict comparison (33)--(35) | **PROVED** | `mu^-,mu^+>=p` implies `alpha_(m,k)>=pk` and `beta_(m,r)>=pr`.  The cross sum is less than 511 and `H_255<8` makes the internal sum less than 1793, giving the strict numerator 2304.  The recorded positive cross-product has the correct orientation. |
| Passage from `Q00` to the fixed adjoint charge | **PROVED** | `H-E` has positive diagonal and determinant `4/2205`, hence is PSD.  Since `Q` is PSD, `tr((H-E)Q) >= 0`, so `<H,Q/N> >= Q00/N`. |
| Uniform E–T innovation limit (38)--(39) | **PROVED** | The smallest recent prefix is `M/2^R>=M/sqrt(log M)`, so its size tends to infinity.  The exact Kolmogorov error is uniform, as is `N_m/N_(2m)=1/2+o(1)`, giving `Q00/N=1/360+o(1)` uniformly and hence the divergent sum. |
| Uniform potential bound (40)--(41) | **PROVED** | At epoch `m`, the cross contribution is less than `2m/p^2` and the internal contribution is at most `m(1+log m)/p^2`.  Geometric summation with `p>=M` yields `(3+log M)/M`. |
| Common critical envelope in the recent window | **PROVED** | Uniformly, `N_n<4Mn` and `M/n<=sqrt(log M)`, while `log n=log M-O(log log M)`; therefore `N_n/(2n^2 log n)=O(1/sqrt(log M))`. |
| No inequality `sum <H,Q/N> <= C_0+C_1 sum W_2` with fixed finite constants | **PROVED** | Along the changing terminal rulers, the left side grows like `R/360` while the potential is `o(1)`.  The construction correctly stops short of claiming a single infinite critical ruler. |
| "Every uniform local or finite-window bridge based on the listed local data is ruled out" | **NEEDS REPAIR / TOO BROAD** | The calculation rules out the displayed affine domination by `W_2` (and any other proposed statistic separately shown to vanish on these windows).  It cannot quantify over every possible nonlinear finite-window functional; for example, a functional may explicitly encode terminal size or an extension certificate.  Narrow the prose to the precise displayed class. |

No audited mathematical claim is false after the two narrow repairs above.

## 2. Independent implementation audit

The exact focused commands were rerun in an isolated `uv` environment:

```text
uv run --with pytest==9.1.1 pytest -q -p no:cacheprovider test_complete_birth_ledger.py
...... [100%]
6 passed

uv run --with ruff ruff check complete_birth_ledger.py test_complete_birth_ledger.py
All checks passed!
```

Byte compilation also passed.  The suite independently checks all pairs,
bands, activation endpoints, wedge cutoffs, exact caps, covariance fraction,
strict rational comparison, and the canonical `W_2` hash stated in the
target note.

The mathematics fixes `a_0=0`, while `_validated_marks` also accepts a
translated ruler.  This is not a defect: `_prefix_modulus` subtracts the
first mark, all subsequent gaps are translation invariant, and the leading
gap 1 is exactly the gap after implicit translation of the first mark to
zero.  Thus the covariance and band calculations consistently normalize a
translated input without mutating it.

The tests are exhaustive for their serialized fixtures, not a finite proof
of the asymptotic statements.  The asymptotic conclusions rest on the
separate exact arguments audited above.

## 3. A concrete extension-sensitive label

The E–T windows expose exactly why a genuinely nonlocal label is needed.  The
following label makes that quantifier explicit without pretending to provide
the missing innovation estimate.

Fix a positive rational `C` and a normalized finite Golomb prefix

\[
 P=(0=a_0<a_1<\cdots<a_{n-1}),\qquad n\ge2,
\]

whose terminal modulus satisfies the chosen critical cap

\[
 N_n\le U_C(n):=\lfloor 2Cn^2\log n\rfloor.
\]

Earlier ranks of `P` are deliberately irrelevant: the target contradiction
only assumes an eventual critical envelope.  Let `T_C(P)` be the rooted tree
whose level-`L` nodes are length-`n+L` Golomb extensions of `P` satisfying
`N_r<=U_C(r)` at every rank `n<=r<=n+L`.  Define the **critical survival
height**

\[
 \operatorname{surv}_C(P)
 :=\sup\{L:\mathcal T_C(P)\text{ has a node at level }L\}
 \in\mathbb N\cup\{\infty\}.
\tag{A1}
\]

For a birth family `F` at epoch `m`, its extension label is

\[
 \lambda_C(F):=\operatorname{surv}_C(A_{2m}).
\tag{A2}
\]

This label is sensitive to the entire future extension tree, not merely to
the endpoint band or a bounded recent history.

### Proposition (exact compactness/embeddability criterion)

For every fixed prefix `P`,

\[
 \boxed{\operatorname{surv}_C(P)=\infty}
\]

if and only if `P` is the initial segment of one infinite Golomb sequence
obeying the same critical cap at every later prefix.

#### Proof

The forward implication from an infinite sequence is immediate.  Conversely,
at a node of length `r`, the next mark is an integer strictly between the
last mark and `U_C(r+1)`, so the node has finitely many children.  Thus
`T_C(P)` is a finitely branching rooted tree.  Infinite survival height means
that it has nodes at arbitrarily large levels.  König's infinity lemma gives
an infinite branch.  Every finite prefix on that branch is Golomb and obeys
the cap by the definition of the tree, so their union is the required
infinite critical sequence.  The converse has already been noted.  `square`

Two useful exact consequences are worth recording.

1. For every fixed finite `L`, the predicate `surv_C(P)>=L` is decidable by a
   finite exhaustive tree search, because every coordinate has the explicit
   finite cap `U_C(r)`.  Infinite survival is deliberately not certified by
   any one bounded search.
2. If `P'` extends `P` by `d` marks, then
   `surv_C(P)>=d+surv_C(P')`, with the usual interpretation at infinity.
   Hence the label is a genuine monotone future resource along a fixed
   history.

### Why the terminal-dependent E–T windows do not refute this label

For one E–T ruler ending at `M`, the displayed window only certifies a finite
lower bound on `surv_1(A_(2m_s))`: the ruler supplies the remaining marks up
to `M`.  It does not certify that this survival height is infinite.  When
`M` changes, the prime `p` and therefore the prefix coordinates change, so
the witnesses are not nodes at increasing depths of one fixed finitely
branching tree.  König's lemma cannot diagonalize them.

Consequently a future theorem explicitly restricted to families with
`lambda_C(F)=infinity` is outside the scope of the terminal-dependent no-go.
This is the precise sense in which (A2) evades those windows.  It is not yet
the needed theorem: no bound here controls

\[
 \sum_F \langle H,Q_F/N\rangle
\]

on the infinite-survival subtree.  The next substantive target is to turn
infinite survival into an arithmetic collision or diameter charge, rather
than merely using it as a hypothesis.

## 4. Safe promoted statement

The following is the strongest wording supported by this audit:

> The complete dyadic birth ledger and its lag-weighted potential are valid
> for one infinite Golomb history, with total `W_2<=8 sqrt(2)`.  Changing
> finite Erdős--Turán rulers rule out every fixed-nonnegative-constant affine domination
> of their recent adjoint innovation by this potential alone.  They do not
> rule out a theorem conditioned on infinite critical survival of the same
> prefix, and no such theorem has yet been proved.

Accordingly the project status remains **UNRESOLVED** and no prize claim is
ready.
