# Wave 7: complete birth-spectrum renewal potential

**Date:** 2026-08-28  
**Status:** new exact all-history packing and summable weighted potential;
the required bridge to covariance innovation is refuted for finite compatible
windows. Erdős Problem #1191 remains unresolved.

## 1. Outcome

Wave 6 Theorem B used only the first half of the old--new rank
anti-diagonals, namely rank lags $1\leq k\leq m$. The first result below
extends it to the full old--new rhombus $1\leq k<2m$. Adding the pairs
internal to the newborn mark block then partitions **every** rank pair in one
finite dyadic prefix, with no omissions and no repetitions.

The resulting complete threshold ledger strictly contains Wave 6 Theorem C.
Adding the elementary quadratic lower bound for the span of $k+1$ marks
gives a two-parameter wedge ledger. Its first rank moment has a uniform
fractional Carleson bound; in particular the exact potential

\[
 \mathcal W_2=
 \sum_F {q_F\ell_F\over\gamma_F^2}
\tag{1}
\]

is bounded by $8\sqrt2$ over all dyadic epochs of one infinite Golomb
ruler. Here $F$ ranges over the complete birth families, $q_F$ is the
number of differences, $\ell_F$ their common rank lag, and $\gamma_F$ is
the rigorous upper threshold defined below.

This is a genuine summable old-history arithmetic potential, stronger than
the Wave 6 endpoint ledger. It nevertheless does not resolve #1191. An
exact 512-mark Erdős--Turán ruler has normalized matrix innovation larger
than its entire one-step $\mathcal W_2$. More decisively, growing recent
Erdős--Turán windows have divergent adjoint innovation but total
$\mathcal W_2=o(1)$. Thus no fixed-constant affine domination of the
displayed innovation sum by this potential alone is possible on all finite
critical windows. A successful theorem must add a charge that detects
embeddability in one infinite critical history, not merely more complete
integer-band capacity.

## 2. Notation

Let

\[
A=(0=a_0<a_1<a_2<\cdots)
\]

be an integer Golomb ruler and put

\[
N_0=0,\qquad N_r=a_{r-1}+1\quad(r\geq1).
\tag{2}
\]

At a dyadic boundary $m$, use the Wave 6 quantities

\[
\mu_m^-={N_m\over m},\qquad
\mu_m^+={N_{2m}-N_m\over m},
\tag{3}
\]

\[
E_m^-(r)=N_r-r\mu_m^-,\qquad
E_m^+(s)=N_{m+s}-N_m-s\mu_m^+,
\tag{4}
\]

\[
D_m^-=\max_{0\leq r\leq m}|E_m^-(r)|,
\quad
D_m^+=\max_{0\leq s\leq m}|E_m^+(s)|,
\quad
H_m=D_m^-+D_m^+.
\tag{5}
\]

The old mark indices are $0,\ldots,m-1$, and the newborn mark indices are
$m,\ldots,2m-1$.

## 3. Full old--new rhombus

Fix a rank lag $1\leq k<2m$. Write a cross-boundary pair as

\[
i=m-1-t,\qquad j=m-1+(k-t).
\tag{6}
\]

The exact admissible range is

\[
t_0=\max(0,k-m)\leq t\leq
t_1=\min(m-1,k-1).
\tag{7}
\]

It has

\[
q_m^{\rm cr}(k)=t_1-t_0+1=\min(k,2m-k)
\tag{8}
\]

members. Their differences are

\[
d_{m,k,t}=a_j-a_i=N_{m+k-t}-N_{m-t}
\tag{9}
\]

and the exact discrepancy decomposition is

\[
d_{m,k,t}
=t\mu_m^-+(k-t)\mu_m^+
 +E_m^+(k-t)-E_m^-(m-t).
\tag{10}
\]

Since the affine center in (10) takes its extrema at $t_0,t_1$, define

\[
c_{m,k}(t)=t\mu_m^-+(k-t)\mu_m^+,
\tag{11}
\]

\[
K_{m,k}^{\rm cr}=
\left[
 \min(c_{m,k}(t_0),c_{m,k}(t_1))-H_m,
 \max(c_{m,k}(t_0),c_{m,k}(t_1))+H_m
\right]
\tag{12}
\]

and its upper activation threshold

\[
\alpha_{m,k}
=H_m+\max(c_{m,k}(t_0),c_{m,k}(t_1)).
\tag{13}
\]

### Theorem 1 (full-rhombus packing)

For any finite collection of pairs $(m,k)$, the
$\sum q_m^{\rm cr}(k)$ associated differences are distinct positive
integers in the common envelope of their bands (12). Hence their total
demand is at most the exact positive-integer capacity of that envelope.

#### Proof

Equation (10) and (5) put every difference in (12). At one boundary,
$(k,t)$ determines the endpoint pair. At different dyadic boundaries,
the right endpoints belong to disjoint rank blocks
$[m,2m-1]$. Thus all endpoint pairs are distinct. The Golomb property
makes their numerical differences distinct, and exact integer capacity
finishes the count. $\square$

For $k\leq m$, (7) becomes $0\leq t\leq k-1$, recovering Wave 6
Theorem B. Moreover

\[
\alpha_{m,k}\leq H_m+k\max(\mu_m^-,\mu_m^+)=\tau_{m,k}.
\tag{14}
\]

The inequality is strict whenever
$\mu_m^->\mu_m^+$ and $k>1$. Thus even before the new $k>m$
families are added, the activation cutoff improves the Wave 6 cutoff.

## 4. Complete dyadic birth partition

The pairs whose two endpoints are both newborn were not in Theorem 1. For
$1\leq r<m$ and $1\leq v\leq m-r$, they are

\[
(i,j)=(m+v-1,m+v+r-1).
\tag{15}
\]

Their common rank lag is $r$, their demand is

\[
q_m^{\rm in}(r)=m-r,
\tag{16}
\]

and

\[
a_j-a_i
=N_{m+v+r}-N_{m+v}
=r\mu_m^++E_m^+(v+r)-E_m^+(v).
\tag{17}
\]

Therefore they lie in

\[
K_{m,r}^{\rm in}
=[r\mu_m^+-2D_m^+,r\mu_m^++2D_m^+]
\tag{18}
\]

with upper threshold

\[
\beta_{m,r}=r\mu_m^++2D_m^+.
\tag{19}
\]

Let $\mathscr F$ consist of every cross family
$(m,k,{\rm cr})$, $1\leq k<2m$, and every internal family
$(m,r,{\rm in})$, $1\leq r<m$, at the available dyadic boundaries.
For $F\in\mathscr F$, write $q_F,\ell_F,\gamma_F$ for its demand,
rank lag, and upper threshold; thus $\gamma_F$ is respectively
$\alpha_{m,k}$ or $\beta_{m,r}$.

### Theorem 2 (complete birth-spectrum ledger)

For every $T\geq0$,

\[
\boxed{
S_{\rm full}(T)
:=\sum_{F\in\mathscr F}q_F
  \mathbf1_{\{\gamma_F\leq T\}}
\leq\lfloor T\rfloor .}
\tag{20}
\]

For a terminal prefix of $M=2^J$ marks, the underlying endpoint pairs of
the families in $\mathscr F$ partition all
$\binom M2$ positive differences.

#### Proof

Every right endpoint rank $j\geq1$ lies in a unique dyadic block
$[m,2m-1]$. If its left endpoint is below $m$, the pair occurs exactly
once in (6)--(8); otherwise it occurs exactly once in (15)--(16). Hence the
families partition all endpoint pairs. If $\gamma_F\leq T$, every
difference of $F$ is a positive integer at most $\lfloor T\rfloor$.
They are globally distinct, proving (20). The same proof applies to every
finite initial family of epochs in an infinite ruler. $\square$

By (14), every term activated in Wave 6 Theorem C is activated in (20) with
the same demand. Thus (20) is pointwise stronger, in addition to covering
all omitted pairs.

The usual layer-cake argument gives

\[
\sum_{\substack{F\in\mathscr F\\\gamma_F\leq X}}
 {q_F\over\gamma_F}\leq1+\log X,
\qquad X\geq1.
\tag{21}
\]

Completeness alone therefore does **not** improve the reciprocal endpoint:
it still gives a logarithm.

## 5. Quadratic rank floor and wedge ledger

Any difference whose endpoints have rank lag $\ell$ spans $\ell+1$
marks. Those marks have $\binom{\ell+1}{2}$ distinct positive
differences, all at most the spanning difference. Consequently

\[
\boxed{a_{i+\ell}-a_i\geq g(\ell):={\ell(\ell+1)\over2}.}
\tag{22}
\]

This elementary fact becomes useful only after it is combined with the
complete multi-epoch partition.

### Theorem 3 (two-parameter wedge capacity)

For every integer $K\geq1$ and real $T\geq0$,

\[
\boxed{
S_{\geq K}(T)
:=\sum_{\substack{F\in\mathscr F\\
                   \ell_F\geq K}}
 q_F\mathbf1_{\{\gamma_F\leq T\}}
\leq
\max\left(0,\lfloor T\rfloor-{K(K+1)\over2}+1\right).}
\tag{23}
\]

#### Proof

Every counted difference is at most $T$, by activation, and at least
$g(\ell_F)\geq g(K)$, by (22). All are distinct integers. The right side
of (23) is exactly the number of integers in
$[g(K),\lfloor T\rfloor]$. $\square$

Put $n=\lfloor T\rfloor$ and

\[
R(T)=
\begin{cases}
0,&0\leq T<1,\\
\max\{K\geq1:K(K+1)/2\leq n\},&T\geq1.
\end{cases}
\tag{24}
\]

Summing (23) over $K$ counts a family of lag $\ell_F$ exactly
$\ell_F$ times and gives the exact first-rank-moment ledger

\[
\boxed{
A_1(T):=
\sum_{F\in\mathscr F}q_F\ell_F
 \mathbf1_{\{\gamma_F\leq T\}}
\leq
R(T)(n+1)-{R(T)(R(T)+1)(R(T)+2)\over6}.}
\tag{25}
\]

In particular, for $T\geq1$,

\[
A_1(T)\leq2\sqrt2\,T^{3/2}.
\tag{26}
\]

### Corollary 4 (summable renewal potential)

For every $\epsilon>0$, over any finite epoch family,

\[
\boxed{
\sum_{F\in\mathscr F}
{q_F\ell_F\over\gamma_F^{3/2+\epsilon}}
\leq {2\sqrt2(3/2+\epsilon)\over\epsilon}.}
\tag{27}
\]

The same inequality holds over all epochs of one infinite ruler by monotone
convergence. At $\epsilon=1/2$,

\[
\boxed{\mathcal W_2
=\sum_F{q_F\ell_F\over\gamma_F^2}
\leq8\sqrt2<12.}
\tag{28}
\]

#### Proof

Every $\gamma_F\geq1$, because it is an upper bound for a positive
integer difference. Layer cake and (26) give

\[
\begin{aligned}
\sum_F{q_F\ell_F\over\gamma_F^{3/2+\epsilon}}
&=(3/2+\epsilon)\int_1^\infty
 {A_1(T)\over T^{5/2+\epsilon}}\,dT\\
&\leq2\sqrt2(3/2+\epsilon)
 \int_1^\infty {dT\over T^{1+\epsilon}},
\end{aligned}
\]

which is (27). $\square$

Thus full old history really does produce a uniformly summable band
potential. The loss has moved: one must now prove that the adjoint covariance
innovation is controlled by this lag-weighted potential. The next section
shows that no such comparison can be local or uniformly finite-window.

## 6. Exact finite counterexample to the direct bridge

Take

\[
p=1423,\qquad m=256,\qquad
b_i=2pi+(i^2\bmod p),\quad0\leq i<512.
\tag{29}
\]

The prime $1423$ has nonzero remainder modulo every prime at most
$\sqrt{1423}$ (the remainders for
$2,3,5,7,11,13,17,19,23,29,31,37$ are respectively
$1,1,3,2,4,6,12,17,20,2,28,17$). The usual Erdős--Turán argument therefore
makes (29) a 512-mark Golomb ruler.

Its exact dyadic moduli are

\[
N_{256}=726721,\qquad N_{512}=1455019.
\tag{30}
\]

This is not an artificially supercritical step. The rigorous C=1 cap at
256 marks is

\[
N_{256}=726721
\leq\lfloor2\cdot256^2\log256\rfloor=726817.
\tag{31}
\]

For $n\geq257$,

\[
N_n\leq1423(2n-1).
\]

At $n=257$, the right side is $729999$, while the rigorous logarithm cap
is $733021$. The function
$2x^2\log x/(2x-1)$ is strictly increasing for $x>1$; hence every prefix
with $256\leq n\leq512$ obeys the same C=1 envelope.

An exact evaluation of the covariance update gives

\[
I:={Q_{256,00}\over N_{512}}
= {72931155410271048281010903
   \over26431687539869343576651464704}.
\tag{32}
\]

For this step, both means in (3) are at least $p$. Therefore every cross
threshold satisfies $\alpha_{m,k}\geq pk$, and every internal threshold
satisfies $\beta_{m,r}\geq pr$. Consequently its complete one-step
potential obeys

\[
\begin{aligned}
\mathcal W_2(256)
&\leq {1\over p^2}
\left(
 \sum_{k=1}^{511}{\min(k,512-k)\over k}
 +\sum_{r=1}^{255}{256-r\over r}
\right)\\
&< {2304\over1423^2}
= {2304\over2024929}.
\end{aligned}
\tag{33}
\]

The last estimate uses the dyadic grouping
$\mathsf H_{255}:=\sum_{r=1}^{255}1/r<8$. The comparison
between (32) and (33) is exact: cross multiplication leaves the positive
integer

\[
86781803501905775924014152122871.
\tag{34}
\]

Thus

\[
\boxed{Q_{256,00}/N_{512}>\mathcal W_2(256).}
\tag{35}
\]

For the fixed Lyapunov matrix from the adjoint note,

\[
H=\begin{pmatrix}16/15&8/105\\8/105&4/35\end{pmatrix},
\]

one has $H-E\succeq0$, since its determinant is $4/2205$.
Therefore
$\langle H,Q_{256}/N_{512}\rangle\geq Q_{256,00}/N_{512}$, so (35)
also refutes the coefficient-one comparison for the actual sufficient
adjoint charge.

This fixed ruler refutes the natural direct bridge; it does not by itself
refute a comparison with an arbitrary large multiplicative constant.
The next growing-window argument closes that larger class.

## 7. No uniform finite-window domination by the new potential

Let $M=2^J$, choose a prime $M\leq p<2M$, and use the finite
Erdős--Turán ruler

\[
b_i=2pi+(i^2\bmod p),\qquad0\leq i<M.
\tag{36}
\]

Set

\[
R=\left\lfloor{1\over2}\log_2\log M\right\rfloor,
\qquad
m_s={M\over2^{s+1}},\quad0\leq s<R.
\tag{37}
\]

Uniformly over this recent window, $m_s\to\infty$ and the gap measures
converge to Lebesgue measure. Hence the already-audited exact innovation
formula gives

\[
{Q_{m_s,00}\over N_{2m_s}}={1\over360}+o(1)
\quad\hbox{uniformly in }s<R,
\tag{38}
\]

and therefore

\[
\sum_{s<R}{Q_{m_s,00}\over N_{2m_s}}
={R\over360}+o(R)\longrightarrow\infty.
\tag{39}
\]

On the other hand, $\mu_{m_s}^-,\mu_{m_s}^+\geq p$. The same calculation
as (33), now using $\mathsf H_{m-1}\leq1+\log m$, gives

\[
\mathcal W_2(m_s)
\leq {m_s(3+\log m_s)\over p^2}.
\tag{40}
\]

Since $p\geq M$, summing the geometric $m_s$'s yields

\[
\sum_{s<R}\mathcal W_2(m_s)
\leq {3+\log M\over M}=o(1).
\tag{41}
\]

The prefixes in this growing recent window satisfy one common critical
envelope for all sufficiently large $M$: indeed
$N_n<4Mn$, while $M/n\leq2^R\leq\sqrt{\log M}$, so
$N_n/(2n^2\log n)=o(1)$ uniformly.

Equations (39)--(41) prove the following precise no-go:

> For every fixed constants $C_0,C_1<\infty$, there are arbitrarily large
> finite compatible critical windows for which
>
> \[
> \sum_s\langle H,Q_{m_s}/N_{2m_s}\rangle
> >C_0+C_1\sum_s\mathcal W_2(m_s).
> \]

The left side dominates (39), because $H\succeq E$; the right side stays
bounded while $R\to\infty$.

### Exact quantifier boundary

The rulers (36) depend on the terminal $M$. They are arbitrarily deep
finite compatible windows, not prefixes of one fixed infinite critical
Golomb ruler. Therefore the no-go rules out the displayed uniform affine
domination by the complete-band potential alone, with fixed nonnegative
constants $C_0,C_1$. It does **not** rule out nonlinear finite-window
functionals, a bridge using additional arithmetic data, or an inequality
whose hypotheses certify extension through one unbounded global history.

## 8. What remains

The new exact information is now separated cleanly from the missing step.

1. All dyadically born pairs, including the previously omitted long
   old--new lags and newborn-internal pairs, obey the complete ledger (20).
2. Rank-lag geometry upgrades it to the wedge inequality (23), exact moment
   ledger (25), and summable all-history potential (28).
3. Neither the local innovation nor its accumulated adjoint charge is
   controlled by that potential on finite critical windows, by
   (29)--(41).

Thus the displayed lag-weighted potential alone is not the missing theorem.
A viable Wave 7 continuation must attach a nonlocal renewal label to a
family--for example, the first historical epoch at which its numerical band
becomes accessible--and prove that repeated positive innovation forces reuse
of such labels in **one fixed infinite** sequence. For every proposed label,
one must state explicitly whether it vanishes on the terminal-dependent
Erdős--Turán windows; only labels with that property fall to (39)--(41).

## 9. Independent exact verifier

The companion files

- complete_birth_ledger.py;
- test_complete_birth_ledger.py

rebuild (3)--(28) without calling the Wave 6 band implementation. The
targeted audit checks:

- the 64-mark adversarial fixture: 177 families, all 2,016 pairs, 177
  distinct activation thresholds, and all $177\cdot63=11,151$ wedge
  endpoint inequalities;
- the 512-mark ruler (29): 1,515 families, all 130,816 pairs, and all
  $1,515\cdot511=774,165$ wedge endpoint inequalities;
- exact band containment for every pair in both audits;
- all 257 critical caps from 256 through 512 marks;
- the innovation fraction (32), the rational bound (33), and the positive
  cross-product (34);
- a canonical binary numerator/denominator hash of the one-step exact
  $\mathcal W_2$:
  eaff996a08dc4a8082612fe3384de6b7f0ad260732682edebac27c0517a81a0c.

The focused suite has six tests. It passes together with Ruff and
byte-compilation.

No asymptotic conclusion about #1191 is claimed here.
