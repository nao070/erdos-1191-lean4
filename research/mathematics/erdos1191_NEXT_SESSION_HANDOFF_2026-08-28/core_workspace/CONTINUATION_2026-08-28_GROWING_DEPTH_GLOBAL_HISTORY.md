# Wave 4 continuation: growing-depth locality and global profile resets

**Date:** 2026-08-28  
**Global status:** `UNRESOLVED_AT_HARD_LIMIT`  
**Prize-claim status:** not ready

## 1. What changed

Wave 3 reduced Question 1 to the missing arithmetic estimate

\[
\sum_{j\le J}
\left\langle H_{j+1},\frac{Q_j}{N_{j+1}}\right\rangle
=o(\log J)
\tag{1}
\]

for the *actual* covariance innovations of one globally compatible critical
Sidon sequence.  Wave 4 does not prove (1), but it substantially sharpens what
such a proof must use.

1. The fixed-depth Erdős--Turán obstruction now holds for a depth tending to
   infinity like `log_2 J`, where the terminal mark count is `M=2^J`.
2. A genuine global-history packing lemma forces any hypothetical critical
   infinite sequence to reset its prefix-diameter profile on the
   `log log M` scale.
3. The most direct attempt to pay covariance innovation by old--new
   cross-band occupancy is rigorously false, even over those growing windows.
4. Current primary literature still contains no quantitative extension or
   filtration theorem that supplies (1).

## 2. Growing-depth Erdős--Turán obstruction

Let `J>=8`, `M=2^J`, choose a prime `M<=p<2M`, and put

\[
b_i=2pi+(i^2\bmod p),\qquad 0\le i<M.
\]

For

\[
L_J=\lfloor\log_2J\rfloor-2,
\]

every prefix with `n=M/2^ell`, `0<=ell<=L_J`, satisfies the same `C=1`
critical envelope

\[
N_n\le2n^2\log n.
\]

The exact gap CDF has Kolmogorov discrepancy at most `4/n`, uniformly on this
whole window.  Hence, for `f(u)=u(1-u)`,

\[
\sum_{\ell=0}^{L_J}\operatorname{Var}_{\nu_{J,\ell}}f
=\frac{\log J}{180\log2}+O(1),
\tag{2}
\]

while adjacent transitions have

\[
\frac{(Q_n)_{00}}{N_{2n}}=\frac1{360}+o(1)
\]

and same-final-modulus birth shells have

\[
\frac{\operatorname{Var}C_{N_{2n}}(A_{2n})
-\operatorname{Var}C_{N_{2n}}(A_n)}{(2n)^4}
=\frac{19}{3840}+o(1)
\]

uniformly.  The limiting full matrix innovation is

\[
\begin{pmatrix}
1/360&-1/192\\
-1/192&7/96
\end{pmatrix},
\qquad \det=\frac{97}{552960}>0.
\]

Therefore no uniform theorem using only the last
`floor(log_2 J)-1` dyadic prefixes, their Sidon property, and their common
critical envelope can prove (1).  The family changes with `J`; it is not one
infinite globally critical sequence.  Ordinary infinite extension of a
finite Sidon set does not preserve the critical envelope and does not close
this quantifier gap.

Full proof and exact certificate:

- `endpoint_variance/GROWING_DEPTH_ERDOS_TURAN_NO_GO_2026-08-28.md`;
- `endpoint_variance/growing_depth_no_go.py`;
- `endpoint_variance/growing_depth_no_go_certificate_2026-08-28.json`.

## 3. Cross-block packing and a forced profile reset

For an `M`-mark prefix define

\[
N_r=a_{r-1}-a_0+1,
\qquad
\varepsilon_M=max_r\left|\frac{N_r}{N_M}-\frac rM\right|.
\]

If `Delta_M` is the Kolmogorov discrepancy of the gap measure, exact left and
right grid limits give
`epsilon_M<=Delta_M<=epsilon_M+1/M`.

If `M=qm` and the ranks are split into `q` consecutive `m`-mark blocks,
then for every block lag `1<=d<q`, all `(q-d)m^2` cross differences of that
lag lie in one common band.  Exact endpoint bookkeeping gives

\[
(q-d)m^2\le
N_M\left(\frac2q-\frac2M+4\varepsilon_M\right)+1.
\tag{3}
\]

Equation (3) compresses one-lag spectra but does not alone force a positive
discrepancy at terminal diameter `Theta(M^2 log M)`; its rearranged lower
bound can be negative.  The actual global-history reset comes from combining
the next all-block packing inequality with the critical bound on an *old
prefix of the same sequence*.

All differences between distinct blocks also give

\[
N_M-1\ge\binom q2m^2.
\tag{4}
\]

If only the old first block is critical,
`N_m<=K m^2 log m`, then

\[
\varepsilon_M\ge
\frac1q-
\frac{K m^2\log m}{\binom q2m^2+1}.
\tag{5}
\]

For one hypothetical global critical sequence, take `M` dyadic and `q` the
least power of two at least `1+4K log M`.  Equation (5) yields

\[
\boxed{
\varepsilon_M>
\frac1{4(1+4K\log M)}
}
\tag{6}
\]

for all sufficiently large `M`.  Thus its prefix-diameter profile cannot stay
uniform to `o(1/log M)`.  A second exact dyadic-tree argument gives the
cross-spectrum Carleson estimate

\[
\sum_v\frac{m_v^2}{D_v}\le1+\log\binom M2,
\]

which is `O(log M)=O(J)`, not the required `o(log J)`.

Full proof and finite exact audit:

- `endpoint_variance/CROSS_BLOCK_DIAMETER_PROFILE_PACKING_2026-08-28.md`;
- `endpoint_variance/cross_block_profile.py`;
- `endpoint_variance/cross_block_profile_certificate_2026-08-28.json`.

## 4. Direct band-occupancy charging is false

For each transition in the growing Erdős--Turán window, let `W_n` be the
exact containing-band length of its `n^2` old--new differences.  Then

\[
\sum_{\ell<L_J}\frac{n_\ell^2}{W_{n_\ell}}<\frac12,
\qquad
\sum_{\ell<L_J}\frac{(Q_{n_\ell})_{00}}{N_{2n_\ell}}
=\frac{L_J}{360}+o(1).
\tag{7}
\]

Consequently no fixed constants `A,B` can make

\[
\sum_n\frac{(Q_n)_{00}}{N_{2n}}
\le A+B\sum_n
\frac{|\text{old--new spectrum}|}{|\text{containing band}|}
\]

valid for all such finite or growing critical windows.  This rules out a
particularly natural bridge from the new packing lemma to (1).

Covariance moments without Sidon arithmetic also fail.  The nested integer
profile `a_k=k^2` has quadratic diameter and a strictly positive limiting
innovation matrix, but it is not Sidon because, for example,
`5^2-1^2=7^2-5^2`.  The missing theorem must therefore retain cross-epoch
integer difference uniqueness, not merely profile moments.

A scalar discrepancy lower bound is insufficient even for Sidon rulers.  The
family `(0,H,H+1,2H+3)` has discrepancy exactly `1/4` while its gap variance
tends to zero.  The homometric rulers `(0,1,3,7)` and `(0,1,5,7)` have the
same discrepancy, old prefix, and diameter ratio but different exact
innovation matrices.  Thus a reset theorem must retain the reset's location,
sign, persistence, and cross-epoch difference arithmetic.

## 5. Certified finite nested-prefix search

A separate exact/heuristic search retained one `C=1` critical envelope at
**every** prefix from 2 through 32 marks.  Its best minimum-gap-variance
witness has

\[
\min_{m\in\{4,8,16,32\}}G_m
=\frac{103963}{23658496}>0.0043943,
\]

and its best minimum-innovation witness has

\[
\min_{m\in\{4,8,16,32\}}\frac{Q_{m/2,00}}{N_m}
=\frac{743151}{192790528}>0.0038547.
\]

Each 32-mark witness has all 496 positive differences distinct and passes all
31 prefix-envelope checks.  The search is complete only at four marks:
12,341 normalized candidates, 1,672 compatible Golomb rulers, and exact
maximum `G_4=3/448`, attained by one reflection pair.  Sizes 8, 16, and 32
are deterministic beam-search witnesses, not optima.

This finite result refutes dyadic monotone-decay claims and any four-transition
lemma forcing `G` or `Q_00/N` below the respective displayed constants.  It
does not prove infinite extendibility, a positive asymptotic lower bound, or
the failure of (1).

Artifacts:

- `endpoint_variance/wave4_nested_results_2026-08-28.md`;
- `endpoint_variance/wave4_nested_certificate_2026-08-28.json`;
- `endpoint_variance/wave4_nested_search.py` and its tests.

## 6. Focused current literature delta

The dated source audit found no theorem supplying (1).  The closest concrete
gluing result is O'Bryant's Lemma 9: combining an old and a separated new
`g`-Golomb ruler costs at most `g*binom(|V|,2)` deletions from the new block.
Its construction makes that quadratic old-history charge negligible by a
cubic scale jump, so it proves a limsup construction rather than an all-scale
critical envelope.

Ma--Yi's 2026 almost-covering theorem packs the *internal* spectra of separate
finite rulers and omits all cross-block differences.  Hall's qualitative
completion of a finite Sidon set to an infinite perfect difference set has no
density or displacement bound.  Recent finite smoothing, entropy, and Sidon
basis papers likewise lack a nested-prefix innovation budget.

See `research_sources/LITERATURE_DELTA_GLOBAL_HISTORY_2026-08-28.md` for exact
theorem statements, primary links, semantic exclusions, and access limits.

## 7. Precise next theorem

The surviving route is a **flat-profile versus profile-reset amortization**.
At mesoscopic `q` comparable to `log M`:

1. small same-lag oscillation of the errors in (3) compresses many distinct
   differences into a common band, although one epoch alone is insufficient;
2. large oscillation must be recorded as a profile reset; and
3. overlapping bands and cross differences from different epochs must show
   that resets cannot renew independently in one global critical sequence.

The third item is the missing theorem.  It must compare cross differences
between different flat epochs.  A scalar discrepancy lower bound, a
pointwise covariance estimate, a fixed/growing local window, or the occupancy
of one old--new band cannot suffice.

## 8. Verification boundary

All new Python artifacts use exact integer or `Fraction` arithmetic.  The
growing-depth proof received an independent adversarial constant and
quantifier audit.  The cross-block formula was separately checked against
literal difference sets and exact CDF calculations.  The machine checks
support the finite algebra only; they do not turn (2), (3), or (6) into an
infinite resolution.

The global label therefore remains `UNRESOLVED_AT_HARD_LIMIT`.
