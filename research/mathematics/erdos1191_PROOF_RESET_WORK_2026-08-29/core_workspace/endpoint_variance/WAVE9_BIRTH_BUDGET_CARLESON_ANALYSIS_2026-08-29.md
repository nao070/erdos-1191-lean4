# Wave 9: rank--magnitude Carleson analysis of the positive birth budget

**Date:** 2026-08-29 (Asia/Tokyo)  
**Scope:** the exact Wave 8 positive birth budget, P15  
**Status:** new deterministic decompositions and a rigorous local-density
no-go; P15 and Erdős Problem #1191 remain open

## 1. Outcome

This note attacks

\[
 \mathcal B_H(J)=
 \sum_{\substack{m\leq 2^J\\m\ \mathrm{dyadic}}}
 \frac1{N_{2m}^2}
 \sum_{0\leq i<j<2m\atop j\geq m}
 h_i h_j\Phi^{(2m)}_{ij}
 =o(\log J)
\tag{1}
\]

on one infinite eventually critical Golomb ruler.  It gives three rigorous
advances and one sharp obstruction.

1. The birth budget at one epoch is, up to the sharp uniform constants
   `16/147` and `36/35`, exactly a scalar **rank-variance birth energy**.
   Globally this energy telescopes to the sum of dyadic gap-rank variances,
   within the constants `3/4` and `1`.
2. For arbitrary positive gaps, all atoms except a long-rank, two-large-
   endpoint core have cumulative cost `O(log log J)` after a canonical choice
   of cutoffs.  Thus only that core can obstruct P15.
3. For a Golomb ruler, every core atom admits a four-parameter
   rank/end-gap/difference-magnitude tile.  A deterministic Carleson-box
   estimate combines endpoint-band capacity, global difference uniqueness,
   and interval-overlap packing.
4. A scaled Erdős--Turán family proves that numerical difference density,
   even together with full contiguous-sum uniqueness and a critical terminal
   diameter, cannot make one local birth budget tend to zero.  The difference
   density tends to zero, while the birth charge is at least `1/2352` at every
   scale.  Hence the missing gain must use compatibility along one fixed
   infinite branch; it cannot be a local occupancy-density estimate.

All theorem statements below are `[RIGOROUS — SELF-CONTAINED]`.  The final
finite numerical table is `[COMPUTATIONAL — EXACT FINITE]` and is used only as
a check, not in any infinite inference.  The existence of the prime selected
in Theorem 7 uses Bertrand's postulate; that theorem is
`[RIGOROUS — MODULO NAMED THEOREM]` only for this harmless choice of scale.

## 2. Notation and the sharp scalar kernel comparison

Fix one update `m -> L=2m`.  As in Wave 8, put

\[
 h_0=1,\qquad h_i=a_i-a_{i-1}\ (i\geq1),\qquad
 N=N_L=\sum_{i=0}^{L-1}h_i,
\tag{2}
\]

and

\[
 \Phi^{(L)}_{ij}
 =\frac{(j-i)^2}{L^2}
 P\!\left(1-\frac{i+j}{L}\right),
 \qquad
 P(w)=\frac{16}{15}w^2+\frac{16}{105}w+\frac4{35}.
\tag{3}
\]

Write the one-epoch contribution to (1) as

\[
 \mathcal B_m=
 \frac1{N^2}\sum_{j=m}^{L-1}\sum_{i=0}^{j-1}
 h_i h_j\Phi^{(L)}_{ij}.
\tag{4}
\]

Set `p_i=h_i/N` and define the scalar rank-birth energy

\[
 \mathcal T_m=
 \sum_{j=m}^{L-1}\sum_{i=0}^{j-1}
 p_i p_j\left(\frac{j-i}{L}\right)^2.
\tag{5}
\]

### Theorem 1 (sharp rank-energy sandwich)

For every positive gap vector,

\[
 \boxed{
 \frac{16}{147}\mathcal T_m
 \leq \mathcal B_m
 \leq \frac{36}{35}\mathcal T_m.}
\tag{6}
\]

These are the optimal uniform lower bound and supremum on the birth-pair
range `-1<1-(i+j)/L<=1/2`.

#### Proof

The quadratic `P` is convex.  Its stationary point is `w=-1/14`, where

\[
 P(-1/14)=\frac{16}{147}.
\]

The relevant endpoint values are `P(-1)=36/35` and `P(1/2)=16/35`.  Since
`1-(i+j)/L` lies in `(-1,1/2]` for a birth pair, substituting these bounds
term by term in (3)--(5) proves (6).  The lower value is attained on the
grid whenever the center rank permits it, and the upper value is approached
as both ranks approach `L`.  `square`

The comparison is useful because `T_m` has an exact probability
interpretation.  Let

\[
 \rho=\frac{N_m}{N_L},\qquad q=1-\rho,
\tag{7}
\]

and let `mu_O`, respectively `mu_S`, be the conditional probability measures
which place masses proportional to `h_i` at `i/L` on
`O={0,...,m-1}`, respectively on `S={m,...,L-1}`.  Denote their means by
`u_O,u_S` and their variances by `V_O,V_S`.

### Theorem 2 (exact conditional-variance form)

One has

\[
 \boxed{
 \mathcal T_m
 =qV_S+\rho qV_O+\rho q(u_S-u_O)^2.}
\tag{8}
\]

Equivalently, if `mu_L=sum_i p_i delta_(i/L)` and `V_L=Var(mu_L)`, then

\[
 \boxed{\mathcal T_m=V_L-\rho^2V_O.}
\tag{9}
\]

Here `V_O` is measured on the common `L`-grid; it is one quarter of the
variance of the old conditional law on its original `m`-grid.

#### Proof

For any probability weights, the unordered pair energy equals the variance:

\[
 \sum_{r<s}w_rw_s(x_s-x_r)^2=\operatorname {Var}_w(x).
\tag{10}
\]

The old--shell cross energy in (5) is therefore

\[
 \rho q\{V_O+V_S+(u_S-u_O)^2\},
\]

while the shell--shell energy is `q^2 V_S`.  Their sum is (8).  The ordinary
two-sample variance formula gives

\[
 V_L=\rho V_O+qV_S+\rho q(u_S-u_O)^2.
\]

Subtracting the old--old pair energy `rho^2 V_O` gives (9).  `square`

Equations (6)--(9) show exactly what a proof based only on rank geometry would
have to do: force the positive conditional variance births to have a
sublogarithmic sum.  No sign cancellation remains available.

### Corollary 3 (global scalarization and indexing audit)

Put

\[
 V_k=\operatorname {Var}_{\nu_{2^k}}(u),
 \qquad
 \rho_k=\frac{N_{2^k}}{N_{2^{k+1}}},
 \qquad V_0=0.
\tag{10a}
\]

Then the scalar energy of the update `2^k -> 2^(k+1)` is exactly

\[
 \mathcal T_{2^k}=V_{k+1}-\frac{\rho_k^2}{4}V_k,
\tag{10b}
\]

and hence

\[
 \boxed{
 \sum_{k=0}^J\mathcal T_{2^k}
 =V_{J+1}+\sum_{k=1}^J
 \left(1-\frac{\rho_k^2}{4}\right)V_k.}
\tag{10c}
\]

In particular,

\[
 \boxed{
 \frac34\sum_{k=1}^{J+1}V_k
 \leq\sum_{k=0}^J\mathcal T_{2^k}
 \leq\sum_{k=1}^{J+1}V_k,}
\tag{10d}
\]

and Theorem 1 gives

\[
 \boxed{
 \frac4{49}\sum_{k=1}^{J+1}V_k
 \leq\mathcal B_H(J)
 \leq\frac{36}{35}\sum_{k=1}^{J+1}V_k.}
\tag{10e}
\]

Thus P15 is quantitatively equivalent, up to absolute constants and a finite
initial term, to

\[
 \sum_{k\leq J}\operatorname {Var}_{\nu_{2^k}}(u)=o(\log J).
\tag{RV}
\]

#### Proof and audit

Equation (10b) is (9), because the old conditional variance on the common
`2^(k+1)` grid is `V_k/4`.  Summing (10b) leaves coefficient `1` on the
terminal variance and coefficient `1-rho_k^2/4` on each intermediate
variance, proving (10c).  Since `0<rho_k<1`, every intermediate coefficient
lies in `(3/4,1)`, proving (10d).  Finally

\[
 \frac{16}{147}\frac34=\frac4{49},
\]

so (10e) follows from Theorem 1.  This independently verifies the constants
and index range in the concurrent Wave 9 rank-variance reduction.  The
artificial mass causes no initial correction: only `V_0=Var_(nu_1)(u)=0` is
needed, so the old term in the first update vanishes exactly.  `square`

There is also a universal lower barrier which clarifies why (RV) still needs
the full, non-adjacent Golomb condition.

### Proposition 4 (distinct-adjacent-gap variance barrier)

For every `n>=8` whose genuine gaps `h_1,...,h_(n-1)` are distinct,

\[
 \boxed{
 \operatorname {Var}_{\nu_n}(u)\geq\frac{n^2}{512N_n}.}
\tag{10f}
\]

#### Proof

Let `c=sum_i h_i i/N_n` be the weighted mean on the unnormalized rank line.
The open interval `|i-c|<n/4` contains at most `n/2+1` integer ranks.  After
also discarding the artificial index `0`, at least `n/2-2>=n/4` genuine
indices remain at distance at least `n/4`.  If their number is `r`, their
distinct positive integer weights have sum at least

\[
 1+\cdots+r\geq r^2/2\geq n^2/32.
\]

Consequently

\[
 \sum_i h_i(i-c)^2\geq\frac{n^2}{16}\frac{n^2}{32}
 =\frac{n^4}{512}.
\]

Division by `N_n n^2` proves (10f).  `square`

Under `N_n<=Cn^2 log(2n)`, Proposition 4 gives, at `n=2^k`,

\[
 V_k\geq\frac1{512C(k+1)\log2}.
\]

Consequently (10e) forces the explicit **lower** barrier

\[
 \boxed{
 \mathcal B_H(J)\geq
 \frac1{6272C\log2}\log J+O_C(1).}
\tag{10g}
\]

Therefore the desired upper implication cannot be obtained from critical diameter,
positivity, covariance recursion, or adjacent-gap distinctness.  A proof of
P15 must use the uniqueness of non-adjacent contiguous sums along the same
infinite history; that extra information is precisely what would contradict
the hypothetical critical branch.

## 3. A universal core reduction

The next decomposition is independent of the Golomb property.  For
`0<theta<=1` and `eta>0`, call a birth pair `(i,j)` **core** if

\[
 j-i>\theta L,
 \qquad
 h_i>\frac{\eta N}{L},
 \qquad
 h_j>\frac{\eta N}{L}.
\tag{11}
\]

Let `B_m^core(theta,eta)` be its contribution to (4).

### Theorem 5 (short-rank and small-endpoint removal)

For every positive gap vector,

\[
 \boxed{
 \mathcal B_m
 \leq
 \mathcal B_m^{\rm core}(\theta,\eta)
 +\frac{18}{35}\theta^2+\frac{36}{35}\eta.}
\tag{12}
\]

#### Proof

For pairs with `j-i<=theta L`, (3) gives
`Phi_(ij)<=36 theta^2/35`.  The total unordered pair mass is at most `1/2`,
so their contribution is at most `18 theta^2/35`.

For the remaining pairs let

\[
 S_\eta=\{k:h_k\leq \eta N/L\}.
\]

Since there are at most `L` indices,

\[
 \sum_{k\in S_\eta}p_k\leq\eta.
\tag{13}
\]

The total unordered pair mass incident with `S_eta` is at most the left side
of (13), and `Phi_(ij)<=36/35`.  Hence all long pairs with at least one small
endpoint cost at most `36 eta/35`.  Every remaining pair is core, proving
(12).  `square`

Now index dyadic updates by `L_j=2^(j+1)`, and for `j>=3` take

\[
 \theta_j^2=\eta_j=\frac1{j\log j}.
\tag{14}
\]

Then

\[
 \sum_{j=3}^J
 \left(\frac{18}{35}\theta_j^2+\frac{36}{35}\eta_j\right)
 =\frac{54}{35}\sum_{j=3}^J\frac1{j\log j}
 =O(\log\log J)=o(\log J).
\tag{15}
\]

Consequently P15 is reduced, without any loss at its target scale, to

\[
 \boxed{
 \sum_{j\leq J}
 \mathcal B_{2^j}^{\rm core}(\theta_j,\eta_j)
 =o(\log J).}
\tag{16}
\]

Thus every genuinely unresolved atom has

\[
 j-i>\frac{L_j}{\sqrt{j\log j}},
 \qquad
 h_i,h_j>\frac{N_{L_j}}{L_jj\log j}.
\tag{17}
\]

For a genuine Golomb atom `i>=1`, the interval difference

\[
 D_{i,j}=\sum_{k=i}^j h_k=a_j-a_{i-1}
\tag{18}
\]

contains `j-i+1` distinct positive adjacent gaps.  Hence

\[
 D_{i,j}\geq
 \frac{(j-i+1)(j-i+2)}2.
\tag{19}
\]

The core therefore consists only of long intervals whose numerical
differences are at least quadratic in the cutoff rank.  The artificial
`i=0` row is not needed here: Wave 8 already proves that its full dyadic sum
is at most `92/315`.

## 4. The deterministic rank--magnitude tile estimate

The reduction above says which pairs matter.  This section gives the
strongest direct packing estimate obtained from the presently available
deterministic information.

Let `R,X,Y,Z` be positive integer powers of two.  Define
`P_m(R,X,Y,Z)` to be the genuine birth pairs `1<=i<j<L`, `j>=m`, satisfying

\[
 \begin{aligned}
 R&\leq j-i<2R,\\
 X&\leq h_i<2X,\\
 Y&\leq h_j<2Y,\\
 Z&\leq D_{i,j}<2Z.
 \end{aligned}
\tag{20}
\]

Put `q_m(R,X,Y,Z)=|P_m(R,X,Y,Z)|` and

\[
 A_X=\#\{1\leq k<L:X\leq h_k<2X\},
 \qquad
 A_Y=\#\{1\leq k<L:Y\leq h_k<2Y\}.
\tag{21}
\]

### Theorem 6 (four-parameter Carleson box)

For every finite Golomb ruler,

\[
 \boxed{
 A_X\leq\min\left(L,X,\left\lfloor\frac NX\right\rfloor\right),
 \quad
 A_Y\leq\min\left(L,Y,\left\lfloor\frac NY\right\rfloor\right),}
\tag{22}
\]

and

\[
 \boxed{
 q_m(R,X,Y,Z)
 \leq
 \min\left(A_XA_Y,\ Z,\
 \left\lfloor\frac{2R^2N}{Z}\right\rfloor\right).}
\tag{23}
\]

The tile contribution satisfies

\[
 \boxed{
 \mathcal B_m(R,X,Y,Z)
 \leq
 \frac{144}{35}\frac{R^2}{L^2}
 \frac{\min(4XY,Z^2)}{N^2}
 \min\left(A_XA_Y,Z,\frac{2R^2N}{Z}\right).}
\tag{24}
\]

Moreover, for fixed `R,X,Y,Z`, difference uniqueness gives the global
cross-epoch count

\[
 \boxed{
 \sum_{m\ \mathrm{dyadic}}q_m(R,X,Y,Z)\leq Z.}
\tag{25}
\]

Every nonempty tile necessarily obeys

\[
 2Z>X+Y,
 \qquad
 2Z>\frac{(R+1)(R+2)}2.
\tag{26}
\]

#### Proof

The actual adjacent gaps of a Golomb ruler are distinct positive integers.
There are only `X` integers in `[X,2X)`, while their total mass is at most
`N`.  This proves (22).

The endpoint-band count gives `q<=A_XA_Y`.  The values `D_(i,j)` are genuine
Golomb differences belonging to distinct mark pairs `(i-1,j)`.  There are
only `Z` integers in `[Z,2Z)`, proving `q<=Z`; the same fact across all birth
epochs proves (25).

For the interval-overlap bound, fix a gap index `k`.  At rank distance `r`,
at most `r+1` intervals `[i,j]` with `j-i=r` contain `k`.  Therefore, over
`R<=r<2R`, it belongs to at most

\[
 \sum_{r=R}^{2R-1}(r+1)
 =\frac{3R^2+R}{2}\leq2R^2
\tag{27}
\]

candidate intervals.  Consequently

\[
 \sum_{(i,j)\in P_m(R,X,Y,Z)}D_{i,j}
 \leq2R^2\sum_{k=1}^{L-1}h_k
 \leq2R^2N.
\tag{28}
\]

Each displayed difference is at least `Z`, so (28) proves the last bound in
(23).

On the tile,

\[
 \Phi_{ij}\leq\frac{36}{35}\left(\frac{2R}{L}\right)^2
 =\frac{144R^2}{35L^2},
\tag{29}
\]

and

\[
 h_i h_j<4XY,
 \qquad
 h_i h_j\leq\frac{(h_i+h_j)^2}{4}
 \leq\frac{D_{i,j}^2}{4}<Z^2.
\tag{30}
\]

Multiplying (29)--(30), dividing by `N^2`, and applying (23) proves (24).
Finally `D_(i,j)>=h_i+h_j>=X+Y`, and (19) with `j-i>=R` proves (26).
`square`

Half-open dyadic bands partition every genuine birth pair exactly once, so
(24) is a literal deterministic decomposition of the genuine part of (4),
not a heuristic sampling scheme.  It also exposes the remaining loss: the
count `q<=Z` is scale-invariantly cancelled by the square weight in (24) on
large tiles.  The next theorem proves that this is a real obstruction.

## 5. A critical-scale local-density no-go

The most natural proposed completion of (24) is that sparse use of the
available numerical difference interval forces a small local birth budget.
The following family refutes every such conclusion.

### Theorem 7 (scaled Erdős--Turán obstruction)

Let `L>=4` be a power of two.  Choose a prime `p` with `L<=p<2L`, and define

\[
 b_k=2pk+[k^2]_p,
 \qquad 0\leq k<L,
\tag{31}
\]

where `[x]_p` is the least residue in `{0,...,p-1}`.  For any positive
integer `s`, the scaled ruler

\[
 A_{L,p,s}=\{sb_0,\ldots,sb_{L-1}\}
\tag{32}
\]

is Golomb.  At its terminal update `m=L/2`, its positive birth charge obeys

\[
 \boxed{\mathcal B_{L/2}(A_{L,p,s})\geq\frac1{2352}.}
\tag{33}
\]

If `s_L=ceil(log L)`, then

\[
 N_L\leq4s_LL^2+1=O(L^2\log L),
\tag{34}
\]

whereas the numerical occupancy of the positive-difference interval tends to
zero:

\[
 \boxed{
 \frac{\binom L2}{N_L}\leq\frac1{4s_L}\longrightarrow0.}
\tag{35}
\]

The same family obeys the fixed envelope

\[
 N_k\leq17k^2\log(2k)\qquad(L/2\leq k\leq L).
\tag{35a}
\]

Nevertheless (33) remains bounded away from zero.

#### Proof

First prove the Golomb property before scaling.  If

\[
 b_j-b_i=b_\ell-b_k,
 \qquad0\leq i<j<L,\quad0\leq k<\ell<L,
\]

then the residue corrections in (31) have absolute value below `p`.  The
intervals of possible values centered at `2p(j-i)` for different positive
rank distances are disjoint.  Hence `j-i=ell-k=:d`.  Reduction modulo `p`
then gives

\[
 (i+d)^2-i^2\equiv(k+d)^2-k^2\pmod p,
\]

so `2d(i-k)=0 mod p`.  Since `1<=d<p` and `p` is odd, `i=k`, and then
`j=ell`.  Integer scaling preserves all difference equalities, proving that
(32) is Golomb.

For `r_k=[k^2]_p`, its actual gaps satisfy

\[
 b_k-b_{k-1}=2p+r_k-r_{k-1}\geq p+1
 \qquad(k\geq1).
\tag{36}
\]

Choose

\[
 I=\{1,\ldots,L/4\},
 \qquad
 J=\{3L/4,\ldots,L-1\}.
\]

There are `L^2/16` pairs `(i,j) in I times J`; all are birth pairs and
`j-i>=L/2`.  By Theorem 1, each has

\[
 \Phi_{ij}\geq\frac{16}{147}\left(\frac12\right)^2
 =\frac4{147}.
\tag{37}
\]

Also

\[
 N_L=sb_{L-1}+1\leq2spL,
\tag{38}
\]

because `b_(L-1)<=2pL-p` and `sp>=1`.  Equations (36)--(38) show that each
selected normalized atom is at least

\[
 \frac{(sp)^2}{(2spL)^2}\frac4{147}
 =\frac1{147L^2}.
\]

Summing `L^2/16` such atoms proves (33).

The upper bound (34) follows from `p<2L` and (38).  Conversely,
`b_(L-1)>=2p(L-1)>=2L(L-1)`, so

\[
 N_L\geq2s_LL(L-1).
\]

There are exactly `binom(L,2)` positive differences, which proves (35).
Every difference is in fact a multiple of `s_L`, making the vanishing
occupancy especially explicit.

Finally, if `L/2<=k<=L`, then `p<2L<=4k`, and

\[
 N_k=sb_{k-1}+1\leq2spk+1\leq8sk^2+1.
\]

For `s=ceil(log L)`, this is at most a universal constant times
`k^2 log(2k)` on the whole recent window.  More explicitly,
`s<=log(2k)+1<=2log(2k)` for `k>=2`, while
`1<=k^2 log(2k)`.  This proves (35a).  `square`

### Corollary 8 (what numerical sparsity cannot prove)

There is no universal function `F(t)->0` as `t->0` such that every finite
Golomb update in a critical terminal envelope satisfies

\[
 \mathcal B_m\leq
 F\!\left(\frac{|\Delta(A_L)|}{N_L}\right).
\tag{39}
\]

In particular, none of the following local data can by itself yield P15:

- the proportion of used or unused numerical differences below `N_L`;
- the fact that each dyadic magnitude band has occupancy `O(1/log L)` after
  a common dilation;
- rank-lag capacity combined only with unweighted difference counts;
- a fixed or terminal-dependent recent critical window.

The obstruction is exactly the square normalization: dilation by `s`
multiplies both endpoint products and `N_L^2` by `s^2`, leaving the genuine
birth energy at constant order while making integer occupancy arbitrarily
sparse.

The family in Theorem 7 changes with `L`, `p`, and `s`.  It is **not** one
compatible infinite critical Golomb branch and does not refute P15.  It
proves that the infinite-branch quantifier is indispensable.

## 6. Exact finite checks

The existing exact `Fraction` implementation was used without changing any
source file.  From the package root:

```bash
PYTHONPATH=core_workspace/endpoint_variance python3 - <<'PY'
from math import ceil, log
from fixed_depth_no_go import least_prime_at_least
from sidon_block_variance import erdos_turan_ruler, is_golomb_ruler
from wave8_pair_telescope import (
    LYAPUNOV_MATRIX, _gap_weights, _modulus, pair_kernel,
)

for L in (16, 32, 64, 128):
    p = least_prime_at_least(L)
    s = ceil(log(L))
    marks = tuple(s*x for x in erdos_turan_ruler(L, p))
    h = _gap_weights(marks)
    N = _modulus(marks, L)
    m = L//2
    B = sum(
        h[i]*h[j]*pair_kernel(LYAPUNOV_MATRIX, i, j, count=L)
        for j in range(m, L) for i in range(j)
    ) / N**2
    print(L, p, s, N, is_golomb_ruler(marks), B, B > 1/2352)
PY
```

Observed exact outputs for `B` were:

| `L` | `p` | `s` | `N_L` | exact `B_(L/2)` | `>1/2352` |
|---:|---:|---:|---:|---:|:---:|
| 16 | 17 | 3 | 1543 | `3735319353/341318512640` | yes |
| 32 | 37 | 4 | 9321 | `93458307121/7473159622656` | yes |
| 64 | 67 | 5 | 42291 | `82481321138611/6563928875728896` | yes |
| 128 | 131 | 5 | 166451 | `20777062425821475/1626899619466182656` | yes |

All four scaled point lists passed the independent Golomb verifier.  These
checks only audit formulas and constants already proved above.

A second exact one-off audit assigned every genuine birth pair to its unique
dyadic `(R,X,Y,Z)` tile and checked (22)--(24) term by term.  For scaled
Erdős--Turán rulers with `L=16,32,64`, it checked respectively
`19,33,40` nonempty tiles containing `84,360,1488` genuine birth pairs, with
no failure.  The core inequality (12) was also checked at
`theta in {1/4,1/2}` and `eta in {1/16,1/4}` for `L=16,32,64,128`.
This is finite sanity evidence only; Theorems 5--7 are established by their
written proofs.

## 7. Consequence for P15

Wave 9 has isolated the precise surviving part of the positive budget.
Up to the already summable `h_0` row and an `O(log log J)` error, it consists
of birth pairs which simultaneously have

1. rank distance greater than `L_j/sqrt(j log j)`;
2. both endpoint gaps greater than `N_(L_j)/(L_j j log j)`;
3. a globally unique interval difference at least quadratic in that rank;
4. a four-parameter tile satisfying (22)--(26).

Theorem 7 proves that no single-epoch summation of (24) can gain the required
vanishing factor from numerical sparsity.  The highest-value next lemma is
therefore the following genuinely global statement.

> **Survival-conditioned core non-saturation.**  On one fixed infinite
> eventually `C`-critical Golomb branch, the core tiles in (17), grouped by
> (20), have cumulative weighted mass `o(log J)`.

A stronger, convenient sufficient form is the epoch-block estimate

\[
 \sum_{K\leq j<2K}
 \mathcal B_{2^j}^{\rm core}(\theta_j,\eta_j)
 \longrightarrow0.
\tag{40}
\]

Indeed, summing (40) over dyadic blocks in the epoch index and using Cesàro
gives (16).  The changing scaled Erdős--Turán rulers show that (40) is false
without the same infinite-branch hypothesis.

Nothing in this note proves survival-conditioned non-saturation.  P15,
Question 1, Question 2, and the prize claim remain open.
