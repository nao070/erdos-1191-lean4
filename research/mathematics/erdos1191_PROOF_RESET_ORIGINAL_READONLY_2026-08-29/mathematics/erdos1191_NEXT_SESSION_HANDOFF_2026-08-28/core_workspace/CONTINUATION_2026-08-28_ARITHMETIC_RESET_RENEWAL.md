# Wave 5 continuation: arithmetic reset-renewal exclusion

**Date:** 2026-08-28  
**Global status:** `UNRESOLVED_AT_HARD_LIMIT`  
**Prize-claim status:** not ready

## 1. Outcome

Wave 5 does not resolve Erdős Problem #1191. It converts the Wave 4
``profile-reset`` program into a sharper arithmetic target and closes another
large class of non-arithmetic arguments.

1. Old diameter-profile curvature has an exact cross-epoch persistence law.
2. Deep block packing forces a reset at a specified rank with a specified
   negative sign, not merely a large unsigned discrepancy.
3. One endpoint-flat run has length only `O(log log m)`, and there is an exact
   conditional amortization in terms of upward normalized-diameter variation.
4. Critical growth does not bound that upward variation. An infinite nested
   positive-integer gap profile has sparse resets but uniformly positive
   innovations. It is explicitly non-Sidon, so it isolates all-contiguous-sum
   uniqueness as the indispensable missing input.
5. Authenticated Wave 4 rulers extend heuristically from 32 to 64 marks under
   the same `C=1` envelope at every prefix, retaining positive innovation and
   signed reset-profile persistence over five dyadic transitions.

## 2. Exact cross-epoch persistence

For `M=qm`, write

\[
e_n(r)=\frac{N_r}{N_n}-\frac rn,
\qquad \alpha=\frac{N_m}{N_M}.
\]

Then for every `0<=r<=m`,

\[
\boxed{
e_M(r)-\frac rm e_M(m)=\alpha e_m(r),
\qquad e_M(m)=\alpha-\frac1q.
}
\]

After subtracting the chord to the old-prefix endpoint, every non-affine
extremum retains its rank location and sign, scaled only by the positive old
mass `alpha`.

For `z=(u(1-u),u)`, the corresponding arbitrary-`q` covariance transport is

\[
\mathcal M_M=B_q\mathcal M_mB_q^{\mathsf T}+Q_{m,M},
\qquad Q_{m,M}\succeq0,
\]

\[
B_q=
\begin{pmatrix}
q^{-2}&(q-1)q^{-2}\\
0&q^{-1}
\end{pmatrix}.
\]

This is an exact identity, not an asymptotic approximation.

## 3. Signed reset and flat-run restriction

If the `M=qm` prefix is Sidon and the old prefix satisfies
`N_m<=K m^2 log m`, all inter-block differences give

\[
e_M(m)\le
\frac{K m^2\log m}{\binom q2m^2+1}-\frac1q.
\]

Hence `q-1>=4K log m` forces

\[
\boxed{e_M(m)\le-\frac1{2q}.}
\]

For dyadic `m_j=2^j`, put `kappa_j=N_{m_j}/m_j^2`. If
`e_(m_(j+1))(m_j)>=-eta`, `eta<1/4`, for `L` consecutive steps beginning at
index `s`, then

\[
L\le
\frac{\log((16/7)Ks\log2)}{\log(2-4\eta)}.
\]

In particular, a completely endpoint-flat run has length `O(log s)`, or
`O(log log m_s)` generations.

Writing `x_j=log kappa_j` and `U_(S,T)` for its total upward variation, the
number `F_eta(S,T)` of such nearly flat steps satisfies

\[
F_\eta(S,T)\log(2-4\eta)
\le U_{S,T}+\log\frac{\kappa_S}{7/16}.
\]

This is a valid conditional amortization. Its missing term is exactly the
upward reset budget `U_(S,T)`.

## 4. Profile-only amortization is false

The sawtooth construction in
`endpoint_variance/CROSS_EPOCH_RESET_AMORTIZATION_2026-08-28.md` defines one
infinite positive-integer gap profile with

- the dyadic `C=1` envelope;
- the all-prefix bound `N_n<12 n^2 log n`;
- the scalar difference-capacity lower bound;
- exactly rank-uniform newborn shells;
- `o(J)` reset count and total endpoint-reset magnitude; and
- the uniform exact innovation lower bound

  \[
  \frac{(Q_j)_{00}}{N_{j+1}}\ge\frac1{2048}.
  \]

Thus its innovation sum is linear although endpoint resets are sparse. The
construction is **not Sidon**: at four marks its gaps are `(1,3,14,14)`, so
the positive difference 14 is already repeated. It refutes only arguments
using critical growth, scalar capacity, profiles, reset magnitudes, or PSD
dynamics without the full distinct-contiguous-sum condition.

## 5. Certified 64-mark finite calibration

The Wave 4 certificate was authenticated before using its four retained
32-mark rulers as roots. Deterministic beam extension reached 64 marks under
the same `C=1` envelope at every prefix `2<=m<=64`.

The innovation-priority witness satisfies

\[
\min_{m\in\{4,8,16,32,64\}}
\frac{Q_{m/2,00}}{N_m}
=
\frac{100987452359053759}{26579439869661020160}
>0.0037994,
\]

while its latest signed reset-profile persistence is greater than `0.6587`.
The persistence-priority witness has latest persistence greater than `0.7113`
and final innovation greater than `0.0025070`. Every retained 64-mark witness
has all 2,016 positive differences distinct and passes all 63 prefix-envelope
checks.

The search after the authenticated 32-mark roots is heuristic. No 64-mark
optimality, 128-mark extension, infinite extension, or asymptotic conclusion
is claimed.

## 6. Current literature boundary

The focused primary-source delta found no theorem supplying the missing
arithmetic budget. Riblet--Schehr gives a valid compactness corollary: a
uniform family of finite all-prefix Sidon towers at every depth would produce
one infinite tower with the same coordinate envelope. It neither constructs
those towers nor controls innovations. Kraft/antichain and infinite
`K_(s,t)`-free graph results provide genuine Carleson or block-amortization
templates, but no checked source maps persistent Sidon differences to their
charges.

See `research_sources/LITERATURE_DELTA_CROSS_EPOCH_2026-08-28.md`. The search
result is a qualified null, not an absence theorem.

## 7. Precise next theorem

The surviving target is an **arithmetic reset-renewal exclusion**:

> In one globally compatible critical Sidon sequence, repeated nearly
> rank-uniform newborn shells cannot renew over unboundedly many
> reset-to-flat cycles without forcing collisions among contiguous gap sums
> or an extra diameter cost whose total controls the actual adjoint-weighted
> innovations by `o(log J)`.

A successful proof must compare cross differences belonging to several
separated cycles. It cannot use only scalar discrepancy, endpoint reset count,
one local containing band, covariance moments, a recent
`Theta(log J)`-scale window, or abstract PSD recursion.

The first concrete attack should perturb the equal-shell counterprofile into
distinct adjacent gaps and quantify the additional span required to keep
**all** cross-epoch contiguous sums distinct. The charge must then be lifted
from adjacent-gap distinctness to all mark-pair differences and connected to
the two terms of the exact `Q_(m,M)` formula.

## 8. Verification boundary

Wave 5 provides exact identities, one rigorous non-Sidon infinite
counterprofile, and certified finite Sidon witnesses. It provides no proof or
disproof of Q1 or Q2, no novelty certification, and no prize-ready claim.

