# Erdős Problem #1191 — Wave 8 positive-birth-budget continuation

**Date:** 2026-08-28 (Asia/Tokyo)  
**Global status:** `UNRESOLVED_AT_HARD_LIMIT`  
**Prize status:** no claim is ready

## 1. What Wave 8 changed

Wave 7 left an overlap debt in nested cheap adjacent halves and asked whether
infinite survival forces that debt to be repaid.  Wave 8 removes the artificial
adjacent overcount, decomposes the actual covariance innovation into genuine
Golomb-difference atoms, and then proves that the negative old-pair terms can
save at most a constant factor.  The hard problem is therefore no longer an
unspecified signed cancellation.  It is the following positive arithmetic
budget on one fixed infinite critical branch.

Let

\[
 h_0=1,\qquad h_i=a_i-a_{i-1}\quad(i\ge1),\qquad
 N_L=a_{L-1}+1,
\]

and, at a dyadic birth boundary `m -> 2m`, put

\[
 K^{(2m)}_{ij}
 =\bigl(z(j/(2m))-z(i/(2m))\bigr)
   \bigl(z(j/(2m))-z(i/(2m))\bigr)^{\mathsf T},
 \qquad z(u)=(u(1-u),u).
\]

For the fixed adjoint majorant

\[
 H=\begin{pmatrix}16/15&8/105\\8/105&4/35\end{pmatrix},
\]

define the positive birth budget through terminal dyadic size `M` by

\[
 \mathcal B_H(M)=
 \sum_{\substack{m<M\\m\ \mathrm{dyadic}}}
 \frac1{N_{2m}^2}
 \sum_{\substack{0\le i<j<2m\\j\ge m}}
 h_i h_j\langle H,K^{(2m)}_{ij}\rangle.
\tag{1}
\]

The new exact pair telescope proves

\[
 \boxed{
 \frac12\mathcal B_H(M)
 \le
 \sum_{\substack{m<M\\m\ \mathrm{dyadic}}}
 \left\langle H,\frac{Q_m}{N_{2m}}\right\rangle
 \le \mathcal B_H(M).}
\tag{2}
\]

Consequently the remaining Wave 8 target is exactly

\[
 \boxed{
 N_n\le Cn^2\log(2n)\ \text{eventually on one infinite Golomb ruler}
 \quad\Longrightarrow\quad
 \mathcal B_H(2^{J+1})=o(\log J).}
\tag{PB}
\]

The already proved adjoint identity and critical lower bound would turn (PB)
into the required contradiction for Q1.  Nothing in this continuation proves
(PB); it is the new hard limit.

## 2. Actual adjacent renewal is now exact

For every epoch retain the Wave 6 cross-antidiagonal family and add the actual
newborn internal adjacent family

\[
 I_m=\{(m,m+1),\ldots,(2m-2,2m-1)\},\qquad
 \delta_m=\max_{m+1\le r\le2m-1}h_r.
\]

The endpoint-pair families are globally disjoint.  Hence, for every real `T`,

\[
 \sum_{\tau_{m,k}\le T}k+
 \sum_{\delta_m\le T}(m-1)\le\lfloor T\rfloor.
\tag{3}
\]

Writing

\[
 B_m^-=\mu_m^-+2D_m^-,\qquad
 B_m^+=\mu_m^++2D_m^+,
\]

the exact inequality

\[
 \min(B_m^-,B_m^+)\le\tau_{m,1}
\tag{4}
\]

gives a renewal dichotomy: either the current newborn adjacent family is paid
at birth, or every older adjacent family is cleared.  Along one fixed history,
at most one internal-adjacent family is outstanding.  A new-pay-only event does
not erase an older outstanding family; the implemented state transition keeps
that debt.

This replaces Wave 7's growing certified-set debt.  It does not control the
proper non-adjacent boundary fan or the rank-one mean-shift fan.

## 3. Exact atom structure of the actual innovation

On the common `2m` grid, split old indices `O={0,...,m-1}` and shell indices
`S={m,...,2m-1}`.  Put `N=sum_(O)h_i`, `G=sum_(S)h_i`, and `N'=N+G`.
With `K_ij=(x_j-x_i)(x_j-x_i)^T`, the two pieces of the innovation are

\[
 \mathcal S_m=\frac1G\sum_{r<s\in S}h_rh_sK_{rs},
\]

\[
 \mathcal R_m=
 \frac1{N'}\sum_{i\in O,j\in S}h_ih_jK_{ij}
 -\frac{G}{NN'}\sum_{i<j\in O}h_ih_jK_{ij}
 -\frac{N}{GN'}\sum_{i<j\in S}h_ih_jK_{ij}.
\]

Adding them gives the short signed identity

\[
 \boxed{
 Q_m=\frac1{N'}\sum_{i<j,\,j\in S}h_ih_jK_{ij}
 -\frac{G}{NN'}\sum_{i<j\in O}h_ih_jK_{ij}.}
\tag{5}
\]

The shell term also has an exact square expansion

\[
 \langle H,\mathcal S_m\rangle
 =\frac1{2G}\sum_{m\le p\le q<2m}
 \kappa_{p,q}\mathcal D_{p,q}^2.
\tag{6}
\]

Every strict bulk coefficient and the full-span corner are positive.  The
only negative coefficients are the proper left-prefix and right-suffix fans.
The covariance positivity therefore gives an exact within-shell repayment
inequality.  The negative adjacent part consists only of `h_m` and
`h_(2m-1)`, and under `N_(2m)<=K(2m)^2 log(2m)` its full dyadic sum is at most
`(13/5)K log 2`.  Thus all adjacent `kappa` debt is removed from the hard
limit.  The unresolved shell object is the proper non-adjacent boundary fan.

The positive AM--GM envelope charges the whole innovation to globally unique
non-adjacent Golomb differences plus an artificial `h_0` row.  The latter has
total dyadic cost at most `92/315`.  The first version had within-shell
coefficient `1/(4GN')`; the pair telescope sharpens it to a unified birth
coefficient `1/(4N'^2)`.

## 4. Cross-epoch cancellation is only a constant-factor effect

Fix one pair at its birth epoch and retain every later negative old-pair term
from (5).  If `n_t` are its successive containing moduli, its constant-`H`
coefficient is

\[
 c_p(T)=\frac{\phi_0}{n_0^2}
 -\sum_{t=1}^T
 \frac{n_t-n_{t-1}}{n_{t-1}n_t^2}\phi_t.
\]

Using `H-B^T H B=E>=0`, this coefficient is a positive `E`-atom telescope and

\[
 \frac12\frac{\phi_0}{n_0^2}
 \le c_p(T)\le\frac{\phi_0}{n_0^2}.
\tag{7}
\]

If all future ratios `n_(t-1)/n_t<=r`, the lower factor improves to
`1/(1+r)`.  At the regular critical ratio `r=1/4`, at least `4/5` survives
and the transported tail is `O(64^{-t})`.  The critical upper envelope alone
does not imply this ratio limit.

For exact finite-horizon adjoints, the same signed sum equals the positive
future `E`-energy tail exactly.  Therefore waiting for old-pair cancellation
cannot create the missing `o(log J)` gain.  Equation (2) makes (PB), rather
than a signed-debt statement, the correct next target.

## 5. Falsified local bridges

Wave 8 subjected the most natural repayment inequalities to exact finite
search.  The scope distinctions below are mandatory.

1. The literal local inequality
   `U_global(T)/T >= <H,Q_m/N_(2m)>` is false even for all-prefix `C=1`
   rulers.  Exhaustion of 1,672 four-mark rulers and 3,344 events found 601
   failures; `(0,1,4,6)` has `T=3`, `U=0`, and innovation `137/10976`.
2. The latest-shell version is false at a genuine old-clear/new-unpaid event:
   `(0,4,5,7,78,86,166,199)` has `T=72`, `delta_4=80`, `U_latest=0`, and
   innovation `5539453/1075200000`.  It has 16,030 depth-two leaves, which is
   finite survival only.
3. Raw non-adjacent cardinality cannot always repay even the single actual
   adjacent family.  Exact eight-mark `C=1` witnesses refute certified,
   global, and latest-shell count variants.
4. Dropping the critical envelope is impossible: scaling
   `(0,8,24,56,58,314,318,319)` by 100 gives a negative global density margin.
5. The rank-one term cannot be bounded by a universal constant times newborn
   covariance: for `(0,D,3D,3D+1)` the ratio grows linearly, with normalized
   limit `46/45`.
6. The shell boundary debt cannot be paid using only the full-span corner and
   positive adjacent atoms.  The eight-mark power-gap ruler above has exact
   deficit `1869979/6720` until its positive non-adjacent bulk atom is restored.

These refute universal local shortcuts.  They do not refute a theorem using
the entire one-ray infinite history.

## 6. Finite evidence retained, without asymptotic promotion

The global factor-one density candidate had no failure in the deterministic
`m>=4` samples:

- 5,001 eight-mark rulers and 20,004 activation events;
- 1,201 sixteen-mark rulers and 9,608 activation events;
- all 510 activations through `m=256` in an independently reconstructed
  682-mark modified-greedy fixture.

The long fixture has all 232,221 positive differences distinct and matches
the reported checkpoints

\[
 b_{661}=4,466,351,\quad b_{680}=4,795,424,\quad b_{681}=4,848,816.
\]

Its working envelope `b_k<=k^2 log_2(2k)` holds through `k=680` and fails at
`681`.  The point-list SHA-256 is
`523c509485873262cf5c51c4ee974a8a9cd5b89b46cec24f9ed59c1f05d57a60`.
This is long finite evidence, not an infinite construction and not a theorem
supporting a prize claim.

## 7. Hegyvári finite blocks and the exact gluing obstruction

Hegyvári's construction has partial sums

\[
 s_t=2pt+[t^2]_p,\qquad0\le t\le p,
\]

so it is exactly a finite parabola Golomb ruler with `p+1` marks and diameter
`2p^2`.  The affine/rotated/gap-translated family

\[
 x_t=(2p+u)t+
 [\alpha(c+t)^2+\beta(c+t)+\gamma]_p-r_0
\]

is also Golomb.  Every such full block contains the universal differences
`L=2p+u` and `pL`, and has a larger rigid multiple skeleton.

For normalized finite rulers `A,B`, a sufficiently separated union
`A union (T+B)` exists if and only if

\[
 \Delta(A)\cap\Delta(B)=\varnothing.
\tag{8}
\]

An explicit safe shift is `T=M+max(M,R)+1`.  Any old prefix of diameter `M`
can be made disjoint from a `p`-block by taking `u>=max(0,M-p)`, but the
resulting endpoint guarantee is `M+2p(M+p)+1`.  At critical old diameter and
`p` comparable to the old mark count, this is cubic and violates the desired
intermediate prefix scale.  Physical translation cannot repair a shared
internal difference, and any fixed finite menu of `(p,u)` blocks can be
blocked by a finite Golomb ruler containing their universal spans.

The exact Hegyvári counting inequality for `k` gaps in `[1,n]`, retaining
interval lengths through `t`, is

\[
 K= tk-\frac{t(t-1)}2,\qquad
 \frac{K(K+1)}2\le
 \frac{t(t+1)k(2n-k+1)}4.
\tag{9}
\]

It recovers the asymptotic upper constant `2/3` but only supplies a local
constant-factor restriction.  It does not give the logarithmic gain in (PB).

## 8. Literature boundary through 2026-08-28

The Wave 8 scoping state contains 550 deduplicated records from 22 scripted
OpenAlex/Crossref/arXiv rounds.  Exa, Firecrawl, SciSpace, and Consensus were
also used with their limitations recorded.  Consensus was quota-blocked;
SciSpace was adjacent-only in the decisive queries.  The mechanical
saturation gate was not met, so every null statement remains qualified.

The closest checked facts are:

- every finite Sidon prefix has an elementary greedy infinite continuation
  with `M+O(n^3)` coordinates, which is too large;
- Ruzsa's very small maximal Sidon subsets of `[1,N]` show that many unused
  difference values do not imply even one legal child inside the interval;
- Bennett--Bohman and conflict-free matching theorems require uniformity,
  regularity, and codegree hypotheses absent from the literal prescribed-
  prefix conflict system;
- infinite survival may be a single ray with branching number one, so König's
  lemma supplies no entropy or Kraft slack;
- Fejér/Fourier identities are unsigned and do not retain the birth labels or
  rank-one component of `Q_m`.

No checked primary source supplies (PB), an equivalent survival-conditioned
Carleson estimate, or a compatible all-prefix `O(n^2 polylog n)` construction.
This is not a novelty or absence proof.

## 9. Next-session theorem target

Do not return to raw debt cardinality, latest-shell-only density, fixed-depth
windows, profile-only resets, or old-pair cancellation.  The single primary
target is (PB).  A useful proof must expose a genuinely global arithmetic
mechanism, for example a two-parameter injection or Carleson estimate which:

1. assigns every positive birth atom a magnitude scale and a rank-lag scale;
2. uses uniqueness of all contiguous sums, not merely adjacent-gap
   distinctness or the terminal diameter cap;
3. has bounded overlap across dyadic birth epochs on one fixed infinite ray;
4. controls the exact weights `h_i h_j Phi_(ij)/N_(2m)^2`, not only atom
   cardinality;
5. yields a vanishing average over logarithmic epoch count.

A candidate should first be tested against the exact four-, eight-, 16-, 64-,
128-, and 682-mark witnesses.  Passing them is only a falsification filter;
the proof must still carry the infinite quantifier.

The secondary Q2 route remains uniform finite feasibility under one fixed
coordinate cap, followed by König compactness.  Hegyvári blocks are eligible
only after proving a depth-independent mixed-spectrum and intermediate-prefix
bound; the unconditional splice above is quantitatively insufficient.

## 10. Canonical Wave 8 artifacts

- `endpoint_variance/WAVE8_ACTUAL_ADJACENT_RENEWAL_2026-08-28.md`
- `endpoint_variance/WAVE8_Q_ATOM_DECOMPOSITION_2026-08-28.md`
- `endpoint_variance/WAVE8_PAIR_TELESCOPE_2026-08-28.md`
- `endpoint_variance/WAVE8_SURVIVAL_DEBT_PROBE_RESULTS_2026-08-28.md`
- `endpoint_variance/WAVE8_DENSITY_CANDIDATE_2026-08-28.md`
- `endpoint_variance/WAVE8_HEGYVARI_BRIDGE_2026-08-28.md`
- `endpoint_variance/WAVE8_ADVERSARIAL_AUDIT_2026-08-28.md`
- `research_sources/WAVE8_CONSECUTIVE_SUMS_DELTA_2026-08-28.md`
- `../research_sources/wave8_literature_state/PRIMARY_SOURCE_AUDIT.md`
- `../research_sources/wave8_literature_state/QUERY_LOG.md`

All machine certificates and focused tests are listed in the handoff manifest.
They verify finite identities and bounded searches only.  The package status
must remain `UNRESOLVED_AT_HARD_LIMIT` until P12's solution gate is met.
