# An all-rank Haar correction with summable physical cost

Date: 2026-09-05. Status: **new informal theorem; independent hand review agrees;
not a proof of Q1; not yet kernel verified**.

This advances the C143 interface from one finite optimized history to a
uniform algebraic statement at every rank. It removes the negative part of
the literal direct Haar demand at a summable cost. It does not prove the
remaining opposite-sign global capacity bound for the resulting nonnegative
carrier. In particular, actual-state nonnegativity is not asserted to imply
positive semidefiniteness on arbitrary vectors.

The strongest final error estimate is in section 11: a local sign-transition
correction has exact cost `2 log2·(e−2)/e²`, with no cap or integer-spacing
assumption. Sections 3--8 retain two useful quadratic representations and
their explicitly owned cutoff costs.

## 1. Definitions and normalization

Let `e≥3` and let `b_0<...<b_e` be integers. Put

\[
 h_i=b_{i+1}-b_i\ge1\quad(0\le i<e),\qquad
 H=b_e-b_0=\sum_{i=0}^{e-1}h_i.
\]

Define raw Haar states, with unit amplitude, by

\[
 q_i(x,T)=1_{[b_i,b_i+T)}(x)-1_{[b_i+T,b_i+2T)}(x),
 \quad T>0,
\]

and put `δ_i=q_i-q_(i+1)`, `0≤i<e`. Let `D` be this difference map and

\[
 B_{ij}=\begin{cases}0,&|i-j|\le1,\\
 -(i-j)^2/(8e^2),&|i-j|\ge2,\end{cases}
 \quad M=D^TBD,\quad L=D^TD.
 \tag{1}
\]

Thus `L` is the unweighted nearest-neighbor graph Laplacian, with
`q^TLq=Σ_iδ_i²`. This is the same direct matrix as C143's `point_matrix(e)`.

The physical scale measure used throughout this note is

\[
 dx\,{dT\over T^2}.
 \tag{2}
\]

The C143 channel at multiplier `m` is `(8/m)q(x,mt)`, and its direct
normalization `m/128` gives

\[
 d_{e,m}(x,t)={1\over2m}q(x,mt)^TMq(x,mt).
 \tag{3}
\]

Consequently its integral over any phase interval `[u,v]` equals one half
of the raw integral (2) restricted to widths `[mu,mv]`:

\[
 \int_u^v\int_{\mathbb R}d_{e,m}(x,t)\,dx\,{dt\over t^2}
 ={1\over2}\int_{mu}^{mv}\int_{\mathbb R}q^TMq\,dx\,{dT\over T^2}.
 \tag{4}
\]

This exact factor is necessary when inserting the new statement into the
existing C143 four-multiplier ledger.

## 2. Moment identity and all actual Haar states

For every real vector `q`, write `s_j=Σ_(i=0)^(e−1) i^j δ_i`. Expanding
`(i-j)²` and then restoring the removed adjacent entries gives exactly

\[
 4e^2q^TMq=s_1^2-s_0s_2+\sum_{i=0}^{e-2}\delta_i\delta_{i+1}.
 \tag{5}
\]

Here `s_0=q_0-q_e`. If `S=Σ_(i=1)^(e−1)q_i`, then
`s_1=S−(e−1)q_e`.

For actual Haar states, increasing the origin `b_i` makes the entries follow
the ordered pattern

\[
 0,\ -1,\ +1,\ 0,
 \tag{6}
\]

with any of the initial/final blocks truncated by the finite ruler and with
zero-length sign blocks allowed. This follows immediately by solving the
two interval membership conditions for `b_i`. There can be at most three
nonzero jumps in `δ`.

**State classification.**

1. If the two endpoint values coincide and are nonzero, every entry is that
   same value, so `δ=0` and `q^TMq=0`.
2. If `q_0≠q_e`, there are at most two nonzero jumps. A single jump has zero
   quadratic energy because `B` has zero diagonal. If there are two, their
   values are `(+1,−2)` or `(−2,+1)`, whose product is negative. Every
   relevant off-diagonal entry of `B` is nonpositive. Hence `q^TMq≥0`.
3. If both endpoints vanish and there is one sign block of length `ell`,
   the two jumps have opposite signs and are separated by `ell` ranks. Thus

\[
 4e^2q^TMq=\ell^2\,1_{\ell\ge2}\ge0.
 \tag{7}
\]

4. If both endpoints vanish and the negative and positive blocks have
   lengths `a,b≥1`, the jumps are `(1,−2,1)` at rank distances `a,b`.
   Evaluating their three off-diagonal interactions gives

\[
\begin{aligned}
 4e^2q^TMq
 &=2a^2 1_{a\ge2}+2b^2 1_{b\ge2}-(a+b)^2\\
 &=(a-b)^2-2\,1_{a=1}-2\,1_{b=1}.
\end{aligned}
 \tag{8}
\]

The only negative cases are `(a,b)=(1,1),(1,2),(2,1)`. Their exact energies
are respectively `−1/e²,−1/(4e²),−1/(4e²)`. In every negative case
`q^TLq=1²+(−2)²+1²=6`.

This classification is independent of the history, rank, gap ratios, phase,
or Sidon property. Integer spacing will enter the integration bound only.

## 3. Explicit actual-state correction

**Theorem 1.** For every increasing real ruler and every actual Haar state,

\[
 \boxed{q^T\left(M+{1\over6e^2}L\right)q\ge0.}
 \tag{9}
\]

**Proof.** In all nonnegative cases the correction is nonnegative because
`L=D^TD`. In the three negative cases its value is `6/(6e²)=1/e²`, at least
the magnitude of the negative energy. This exhausts (6). ∎

The scalar `1/(6e²)` is sharp for this particular uniform multiple of `L`
on the actual-state class: the state `(0,−1,+1,0)` forces it. For example,
the Sidon ruler `(0,1,4,6)` realizes that state at `T=2,x=9/2`.

The matrix in (9) is **not claimed PSD on all vectors**. It is a rank-aware,
long-range matrix certified only on the explicitly described physical state
class. The correction itself is a nonnegative sum of `e` adjacent graph
roots. Nothing in (9) supplies the nine separate C143 owner inequalities.

In fact arbitrary-vector PSD is false: at `e=3`, the vector
`q=(3,2,1,0)` has `δ=(1,1,1)` and gives
`qᵀ(M+L/(6e²))q=−1/18`. This independent-review witness prevents an
unjustified upgrade of the state-restricted theorem.

## 4. Exact integrated correction cost

For a single adjacent gap `h≥1`, put
`r_h(T)=∫_R(q_b(x,T)−q_(b+h)(x,T))²dx`. The Haar autocorrelation gives

\[
 r_h(T)=\begin{cases}
 4T,&0<T\le h/2,\\
 8T-2h,&h/2\le T\le h,\\
 6h,&h\le T.
 \end{cases}
 \tag{10}
\]

Direct integration on the three intervals proves

\[
 \int_{1/2}^{\infty}r_h(T){dT\over T^2}
 =4\log h+8\log2+4.
 \tag{11}
\]

The contributions are `4 log h`, `8 log2−2`, and `6`, respectively. There
is no unowned upper terminal: the last integral is included explicitly.

For `T<1/2`, an integer ruler has at most one active mark in a Haar support
of length `2T`; since `M` has zero diagonal, `q^TMq=0`. Define the correction
to be used only at `T≥1/2`. Its total physical price is exactly

\[
\begin{aligned}
 R_e
 &:=\int_{1/2}^{\infty}\int_{\mathbb R}{q^TLq\over6e^2}
                  \,dx\,{dT\over T^2}\\
 &=\boxed{{4\sum_{i=0}^{e-1}\log h_i+e(8\log2+4)\over6e^2}}.
\end{aligned}
 \tag{12}
\]

The arithmetic-geometric mean inequality yields the upper bound

\[
 R_e\le {2\over3e}\log(H/e)+{4\log2+2\over3e}.
 \tag{13}
\]

Thus the correction is not free, but its exact source and price are known.
The lower cutoff `1/2` is justified by integer separation; extending the
correction unchanged down to `T=0` would introduce a logarithmic divergence.

## 5. The signed Wave mass and a nonnegative Haar carrier

Let `K_T=T^−1 1_[0,T)` be the normalized box. With the same `M`, define

\[
 Q_e(T)=\sum_{i,j}M_{ij}
       \langle\delta_{b_i}*K_T,\delta_{b_j}*K_T\rangle.
\]

The existing box-dipole identity, or direct mixed differencing, writes
`Q_e` as the nonnegative weighted sum of the cross-ratio tents. Thus

\[
 Q_e(T)\ge0,\quad W_e:=\int_0^\infty Q_e(T)dT
 =\sum_{0\le i<j<e,\ j-i\ge2}{(j-i)^2\over4e^2}
 \log{(M_{ij}+h_i)(M_{ij}+h_j)\over
          M_{ij}(M_{ij}+h_i+h_j)},
 \tag{14}
\]

where the scalar middle span in this display is
`M_(ij)=h_(i+1)+...+h_(j−1)`; it is unrelated to the matrix notation.
All sums are finite, so the box/tent representation needs no infinite-rank
limit interchange. It has compact width support.

Raw Haar is `2T(K_T−K_(2T))`. The box refinement identity therefore gives

\[
 U_e(T):=\int_{\mathbb R}q^TMq\,dx
 =4T^2(Q_e(T)-Q_e(2T)).
 \tag{15}
\]

Integrating with the literal measure (2), including both width tails,

\[
 \boxed{\int_0^\infty U_e(T){dT\over T^2}=2W_e.}
 \tag{16}
\]

Define the nonnegative actual-state carrier

\[
 \mathcal H_e(x,T)=
 1_{T\ge1/2}\,q(x,T)^T\left(M+{L\over6e^2}\right)q(x,T).
\]

Equations (9),(12),(16) prove the exact all-rank bridge

\[
 \boxed{\mathcal H_e\ge0,\qquad
 \int_0^\infty\int_{\mathbb R}\mathcal H_e\,dx\,{dT\over T^2}
 =2W_e+R_e.}
 \tag{17}
\]

There is also an exact positive-part version. Put

\[
 \nu_e:=\int_0^\infty\int_{\mathbb R}(-q^TMq)_+\,dx\,{dT\over T^2},
 \quad P_e^+:=\int_0^\infty\int_{\mathbb R}(q^TMq)_+\,dx\,{dT\over T^2}.
\]

Theorem 1 pointwise implies `0≤ν_e≤R_e`. Hence

\[
 \boxed{P_e^+=2W_e+\nu_e,\qquad0\le\nu_e\le R_e.}
 \tag{18}
\]

A second direct check on integrability comes from the classification:
negative states have both endpoints zero and at least two active marks.
Their possible scales lie in `[1/2,H/2]`, their spatial support has measure
at most `2(e−1)T`, and their magnitude is at most `1/e²`. Thus also

\[
 \nu_e\le {2(e-1)\over e^2}\log H.
 \tag{19}
\]

The sharper source-price bound (12) is preferable for the global account.

## 6. Uniform bounded total cost on capped dyadic towers

Suppose `e=2^k`, `k≥k_0≥1`, and the actual shell spans satisfy

\[
 H_e\le4Ce^2\log(4e)
\]

with one fixed `C>0` through the horizon considered. Set
`A=max(0,log(4C log2))`. Since `log(k+2)≤(k+1)log2`, (13) implies

\[
 R_{2^k}\le {2^{-k}\over3}
      \{4k\log2+2A+6\log2+2\}.
 \tag{20}
\]

For any weights `0≤ω_(k,J)≤1`, including the actual Fejér weights,

\[
\boxed{
 \sum_{k=k_0}^{J}\omega_{k,J}R_{2^k}
 \le {2^{1-k_0}\over3}
       \{4k_0\log2+10\log2+2A+2\}.}
 \tag{21}
\]

This follows from the exact geometric sums
`Σ_(k≥k0)2^−k=2^(1−k0)` and
`Σ_(k≥k0)k2^−k=(k0+1)2^(1−k0)`. Its constants do not depend on the horizon
or on the individual history. No existence of an infinite capped Sidon tower
is assumed by this finite conditional estimate.

Equations (17),(18),(21) identify the full Fejér sums of the signed Wave
mass and the two nonnegative Haar carriers up to an explicitly bounded
same-source adjacent-root correction. The result retains all original
long-range entries of `M`; it is not a fixed-window positive-pasting scheme.

## 7. Exact remaining global obligation

The following implication would be invalid:

> a nonnegative carrier has the same mass as the harmonic Wave sector up to
> bounded error, therefore its total mass is bounded.

The existing positive `Q_e` already demonstrates why a nonnegative
representation alone cannot supply the opposite sign. We have proved a new
actual-state Haar representation and removed its negative-part obstacle;
we have not constructed the missing upper capacity.

To finish the Route-C contradiction with this carrier one needs an
independently derived whole-tower source identity implying, uniformly on
all capped finite towers,

\[
 \sum_{k=k_0}^{J}\omega_{k,J}
  \int\!\int\mathcal H_{2^k}(x,T)\,dx\,{dT\over T^2}
 \le K_C
 \tag{22}
\]

or another precise opposite-sign inequality adequate for the known harmonic
floor. Equation (22) is **unproved**, and with the Wave floor it is already a
contradiction target. It is not a consequence of Theorem 1, (21), C115's
signed span telescope, or the finite C143 bank.

The next analytic target is to place the long-range part of `M` under a
single physical source/owner system, using the explicit adjacent correction
as a proved summable error. Enlarging the cone to actual-state positive
matrices requires proving its associated global source rule; it cannot
silently inherit the rule for arbitrary PSD Gram matrices or the C143
graph-root owner constraints.

## Source relations

The formula for `M` comes directly from the literal C143 implementation
`c142/master.py:point_matrix`; the moment expansion was proposed independently
by the main task. The present plateau classification, adjacent-root
correction, exact cost, and all-rank bridges were derived during this run.
The box/tent representation is already proved in
`erdos1191_PROOF_RESET_WORK_2026-08-29/route_probes/ROUTE_C_CROSS_RATIO_BOX_DIPOLE_BRIDGE.md`.
The signed-span Fejér telescope and all-boundary caveats remain as in
`ROUTE_C_CRITICAL_SPAN_POTENTIAL_AND_GOOD_WINDOWS.md` and the current follow-up
`GLOBAL_OBSTRUCTION_ANALYSIS.md`.

## 8. A simpler positive carrier by restoring adjacent entries

There is an exact alternative to the graph-root correction. Define

\[
 \widetilde B_{ij}=-(i-j)^2/(8e^2),\qquad
 \widetilde M=D^T\widetilde BD.
\]

Only adjacent entries differ from `B`. Equation (5) becomes

\[
 4e^2q^T\widetilde Mq=s_1^2-s_0s_2,
 \qquad
 q^T(\widetilde M-M)q=-{1\over4e^2}
                       \sum_i\delta_i\delta_{i+1}.
 \tag{23}
\]

On every actual Haar state the nonzero jumps of `δ` alternate in sign.
Hence each nonzero adjacent product is negative, and the second expression
in (23) is nonnegative. The first expression is also nonnegative: when both
endpoints are zero, `s_0=0`; constant endpoint states give zero; in the
remaining cases there is a single jump or two oppositely signed jumps, and
the original full-distance quadratic is zero or positive. Therefore

\[
 \boxed{q^T\widetilde Mq\ge\max(q^TMq,0)}
 \tag{24}
\]

on all actual states. This is again a state-restricted theorem. The same
arbitrary vector `e=3,q=(3,2,1,0)` gives
`qᵀ Mtilde q=−1/6`.

For two consecutive gaps `h,h'`, the polarization identity is

\[
 \delta_i\delta_{i+1}={1\over2}
 [(q_i-q_{i+2})^2-(q_i-q_{i+1})^2-(q_{i+1}-q_{i+2})^2].
\]

Using (11) for distances `h+h',h,h'` proves

\[
 \int_{1/2}^\infty\int_{\mathbb R}\delta_i\delta_{i+1}
                  \,dx\,{dT\over T^2}
 =2\log{h+h'\over hh'}-4\log2-2.
 \tag{25}
\]

Consequently the exact positive price of replacing `M` by `Mtilde` on
`T≥1/2` is

\[
 \boxed{A_e={1\over2e^2}\sum_{i=0}^{e-2}
 \left[\log{h_i h_{i+1}\over h_i+h_{i+1}}+2\log2+1\right].}
 \tag{26}
\]

Every bracket is positive since `h_i,h_(i+1)≥1` implies their harmonic
product `hh'/(h+h')≥1/2`. The inequalities
`hh'/(h+h')≤(h+h')/4` and
`Σ_(i=0)^(e−2)(h_i+h_(i+1))≤2H`, followed by arithmetic-geometric mean,
give

\[
 0<A_e\le {e-1\over2e^2}
              \left[\log{2H\over e-1}+1\right].
 \tag{27}
\]

It follows that

\[
 \boxed{\int_{1/2}^\infty\int_{\mathbb R}q^T\widetilde Mq
                 \,dx\,{dT\over T^2}=2W_e+A_e,\qquad
       0\le\nu_e\le A_e.}
 \tag{28}
\]

As a finite dyadic sum, `Σω A_e=O_C(1)` follows either directly from (27)
or from the same elementary geometric summation as (20),(21). This gives
the simplest moment-based nonnegative carrier found here, with an exact
signed same-source relation to the original Wave mass and a proved
summable local price. It still supplies no opposite-sign capacity theorem.

## 9. A critical-cap family refuting a local upper-storage shortcut

This section tests the proposed upper bound before using it as a global
premise. The onset dependence is essential to its scope.

For any dyadic `e=2^k≥4`, choose a prime `4e<p<8e` and put

\[
 \ell=\lceil\log(8e)\rceil,\quad L=4p\ell,\quad
 a_i=Li+[i^2]_p\quad(0\le i<4e),
 \tag{29}
\]

where `[i²]_p∈{0,...,p−1}`. Bertrand's theorem provides the prime.

**Sidon proof.** Equality of two positive differences first fixes their
rank difference `d`, since the difference of the residue perturbations has
absolute value less than `2p<L`. Modulo `p`, the remaining equality is
`2d(i-u)=0`. Here `0<d<4e<p` and `p` is odd, hence `i=u`, and both pairs
are identical. The ruler is strictly increasing since every gap exceeds
`L-p>0`.

**Cap and shell geometry.** For every integer `e≤m≤4e`, writing
`N_m=a_(m−1)+1`, the bounds `p<8e≤8m` and
`ell≤log(8m)+1≤3 log(2m)` imply

\[
 N_m\le32\ell m^2+8m\le100m^2\log(2m).
 \tag{30}
\]

Thus one fixed constant `C=100` controls every intermediate prefix rank in
this interval. Its two shells have `e` and `2e` gaps respectively. Since
all gaps lie between `L-p` and `L+p`,

\[
 {3\over10}\le{H_{2e}\over4H_e}\le{5\over6},\qquad
 \eta_k=\log(H_{2e}/(4H_e))<0,
 \tag{31}
\]

and `eta_k` is bounded uniformly in `e`.

For any old-shell primitive of rank separation `d≥2`, its outer span is at
most `(d+1)(L+p)` and its endpoint gaps are at least `L-p`. The product
floor and `d²/(d+1)²≥4/9`, together with `(L-p)/(L+p)≥3/5`, yield

\[
 {d^2\over4e^2}C_{ij}\ge{1\over25e^2}.
\]

There are `(e−1)(e−2)/2` primitive pairs. Hence

\[
 \boxed{W_e\ge{(e-1)(e-2)\over50e^2}\ge{3\over400}.}
 \tag{32}
\]

It follows that no estimate of the form

\[
 W_{2^k}\le
 {A\eta_k+V_{k+1}-V_k\over k+1}+r_k
 \tag{33}
\]

can hold uniformly on all these locally capped adjacent-epoch rulers when
`A` is fixed, the profile values are uniformly bounded, and `r_k=o(1)`
uniformly on the class. The right-hand side tends to zero while (32) does
not. Finite or absolutely summable combinations of uniformly bounded
profiles have the same obstruction.

This is a failure of a **local upper-storage theorem**, not of the proposed
whole-tower sum estimate and not of Q1. The onset in (30) is `m_0=e`, which
changes with the ruler. The construction does not supply arbitrarily deep
capped towers with one fixed onset. Any genuine upper capacity must use
that long-term compatibility, or additional source structure that is absent
from a two-epoch cap and bounded profile increments. The same-source
equivalences (17),(18),(28) do not themselves use that structure.

## 10. Whole-tower pointwise ownership by the actual jump pattern

There is a direct finite-tower identity that does not come from stitching
locally optimized C143 owners. Let a finite increasing ruler contain all
epochs `e=2^k`, `k_0≤k≤J`. For a common physical pair `(x,T)`, form the
global raw Haar state at every mark. Its global adjacent difference vector
has at most three nonzero entries, by (6).

The epoch `e` uses global gap indices `e−1,...,2e−2`. These gap-index blocks
are disjoint over dyadic epochs. Both `B_e` and `Btilde_e` have zero diagonal,
so an epoch containing zero or one nonzero global jump has zero direct
energy. There cannot be two disjoint blocks each containing at least two
of at most three nonzero jumps. Therefore:

**Theorem 2.** For every actual finite tower and common `(x,T)`, at most one
epoch has nonzero `q_eᵀ M_e q_e`, and at most one epoch has nonzero
`q_eᵀ Mtilde_e q_e`. The same unique candidate block works for both.

This is a pointwise ownership statement for direct demand. It is not a
construction of the separate C143 graph-price owner map.

The exact nonzero values of the unnormalized moment form
`4e² q_eᵀ Mtilde_e q_e` are:

* `(a−b)²` when both physical endpoint states vanish, where `a,b` are the
  negative and positive block lengths and one may be zero;
* `2b²` when the left endpoint is negative, the right endpoint is zero,
  and there are `b` positive states;
* `2a²` when the left endpoint is zero, the right endpoint is positive,
  and there are `a` negative states.

All other endpoint patterns give zero. These formulas follow either from
the explicit jump products or from `s_1²−s_0s_2`. Since the distances
between jump indices are at most `e−1`, each epoch energy is at most `1/2`.
Thus for arbitrary weights `0≤ω_(k,J)≤1`,

\[
 \boxed{0\le\sum_{k=k_0}^{J}\omega_{k,J}
          q_{2^k}(x,T)^T\widetilde M_{2^k}q_{2^k}(x,T)
       \le {1\over2}.}
 \tag{34}
\]

Equation (34) is a genuine all-history, all-rank pointwise bound. Its
integrating measure is not a probability measure: the size of the active
region in `dx dT/T²` depends on the whole tower. Integrating `1/2` over an
uncontrolled region would be a gap. The critical remaining capacity problem
can now be posed as control of the integral of this single active-epoch
function using *global positive-difference uniqueness and the cap from one
fixed onset*, rather than as an unspecified local-owner stitching problem.

The correction (26) and the direct tower localization are compatible: each
adjacent-jump product is already assigned to its unique epoch, and the sum
of its integrated prices is bounded by (27). The root-Laplacian correction
of Theorem 1 includes single-jump states and therefore does not itself enjoy
the same one-active-epoch statement; the restored-adjacency carrier is the
more suitable representation for this whole-tower interface.

## 11. Cap-free transition correction and an exact finite-cost carrier

The independent mathematical reviewer found a sharper bound using the unique
negative-to-positive transition. It avoids the small-width diagonal price
of `Mtilde` completely.

For any increasing **real** ruler and `1≤r≤e−2`, define

\[
 J_r(x,T)=1_{\{q_r(x,T)=-1,\ q_{r+1}(x,T)=+1\}},\qquad
 G_e(x,T)={1\over e^2}\sum_{r=1}^{e-2}J_r(x,T).
 \tag{35}
\]

Every negative direct state in (8) has exactly one such internal
transition. Since its negative magnitude is at most `1/e²`,

\[
 \boxed{q^TMq+G_e\ge0.}
 \tag{36}
\]

For the adjacent gap `h=b_(r+1)−b_r>0`, the length of the intersection of
the two required spatial intervals is

\[
 \int_{\mathbb R}J_r(x,T)dx
 =\begin{cases}
 0,&0<T\le h/2,\\
 2T-h,&h/2\le T\le h,\\
 h,&T\ge h.
 \end{cases}
\]

Consequently

\[
 \int_0^\infty\int_{\mathbb R}J_r(x,T)\,dx\,{dT\over T^2}
 =(2\log2-1)+1=2\log2.
 \tag{37}
\]

No integer lower cutoff or upper tail is omitted. The result is scale
invariant and independent of the adjacent gap. Combining (16),(35)--(37)
gives the exact all-rank positive carrier

\[
\boxed{
 \mathcal P_e:=q^TMq+G_e\ge0,\qquad
 \int_0^\infty\int_{\mathbb R}\mathcal P_e\,dx\,{dT\over T^2}
 =2W_e+{2\log2(e-2)\over e^2}.}
 \tag{38}
\]

In particular the positive-part identity improves to

\[
 \boxed{P_e^+=2W_e+\nu_e,\qquad
 0\le\nu_e\le {2\log2(e-2)\over e^2}.}
 \tag{39}
\]

For every dyadic finite tower and `0≤ω_(k,J)≤1`, the sum of exact correction
prices is at most

\[
 2\log2\sum_{k=k_0}^J\omega_{k,J}
                    {2^k-2\over4^k}
 \le2^{2-k_0}\log2.
 \tag{40}
\]

Thus the error is universally summable even without a cap or the Sidon
condition. Its exact finite sum is retained if a sharper bound is needed.

`G_e` is an indicator/positive-part function of adjacent physical states,
not a PSD quadratic form. No quadratic- or Gram-cone source rule is thereby
inherited. The full positive carrier still has all the long-range original
interactions in `M`, so this is not the fixed-window original-capacity
pasting scheme excluded by the earlier obstruction.

The restored-adjacency carrier in section 8 must continue to be integrated
only from `T=1/2`: near zero its internal diagonal produces
`(e−1)/(2e²)·dT/T`, which diverges. Formula (38) has no such divergence,
because each transition indicator vanishes below half its positive gap.

Finally, universal summability does not produce the missing capacity. The
independent review gives a real infinite Sidon example with shell gap ratios
below two and `W_e≥3/256` for every `e≥4`: the correction (40) stays bounded
while the Wave sum diverges linearly in the number of epochs. That example
does not obey a fixed critical cap. Hence a successful proof must use the
critical cap in a further arithmetic/global source estimate, rather than
only to justify error summability.

## 12. Exact finite sanity checks performed in this run

An independent integer-only Python enumeration checked all cut triples
`0≤u≤v≤w≤e+1` representing states `0^u (−1)^(v−u) (+1)^(w−v) 0^(e+1−w)`
for every `3≤e≤24`: **23,716 pattern triples**. It computed the direct
form from the literal nonadjacent gap pairs and checked the moment identity,
`Adj≤0`, moment positivity, path correction positivity, transition correction
positivity, and the exhaustive three-case negative classification. All
checks passed with exact integers.

A second enumeration of all **47,905 cut triples** on 64 marks checked the
whole-tower theorem for gap blocks at epochs `4,8,16,32`: at most one moment
energy was nonzero, and each lay in `[0,1/2]` after normalization. All checks
passed; the process exited zero. These counts include duplicate states from
different empty-block cut triples. They are finite sanity checks of the
displayed proof, not its universal justification and not Lean checks.
