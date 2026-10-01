# Wave 14: future spatial bins force harmonic rank promotion

Date: 2026-08-29 (Asia/Tokyo)  
Status: **rigorous promotion lemma; the signed allocation step remains open**

This note proves the cap-dependent promotion target left open in Wave 13.
It does **not** prove the frontier allocation inequality, P19, either Erdős
question, or a prize claim.  The new theorem is one-sided: a long old
difference acquires many new numerical ranks in the future.  Turning those
new ranks into negative signed repayment still requires a cross-epoch
bounded-overlap allocation which is not supplied here.

Throughout,

\[
0=a_0<a_1<a_2<\cdots
\]

is one fixed infinite normalized integer Golomb ruler.  Thus all positive
differences `a_j-a_i`, `i<j`, are globally distinct.  For a prefix of `L`
marks put

\[
\Delta_L=\{a_j-a_i:0\leq i<j<L\},\qquad
\rho_L(d)=|\{e\in\Delta_L:e\leq d\}|.
\tag{1}
\]

For fixed integer `d`, these ranks are nondecreasing integers bounded by
`d`.  Thus they stabilize, and
`rho_infinity(d):=lim_(K->infinity) rho_K(d)` is well defined.

## 1. The exact finite spatial-bin inequality

Let `d in Delta_L`, choose an integer `N>=2`, and suppose the ruler is known
through `a_(L+N-1)`.  Partition the future block

\[
 a_L,a_{L+1},\ldots,a_{L+N-1}
\]

into the half-open bins

\[
I_q=[a_L+qd,a_L+(q+1)d),\qquad q=0,1,2,\ldots.
\tag{2}
\]

Let `x_q` be the bin occupancies and `B=|{q:x_q>0}|`.  Every pair in one
bin has difference strictly between `0` and `d`.  It is globally different
from every other such pair difference and from every member of `Delta_L`,
because the corresponding unordered mark pairs are different and the ruler
is Golomb.  Consequently

\[
\begin{aligned}
\rho_{L+N}(d)-\rho_L(d)
&\geq \sum_q {x_q\choose2}\\
&=\frac12\left(\sum_qx_q^2-N\right)\\
&\geq \frac12\left(\frac{N^2}{B}-N\right).
\end{aligned}
\tag{3}
\]

The final step is Cauchy--Schwarz.  Formula (3) is the floor-error-safe
finite theorem; its right side is allowed to be a rational number.  The
left side and the same-bin count are integers.

Since the marks are nonnegative and the last future mark is
`a_t`, `t=L+N-1`,

\[
B\leq \left\lfloor\frac{a_t}{d}\right\rfloor+1
\leq\frac{a_t}{d}+1.
\tag{4}
\]

No growth hypothesis has been used in (3)--(4).

## 2. Explicit consequence of an eventual critical cap

Assume that, for some fixed `C>0` and `n_0`,

\[
a_n\leq Cn^2\log(2n)\qquad(n\geq n_0).
\tag{5}
\]

Let

\[
\lambda=\log d,qquad
N=\left\lfloor\frac d{\lambda^2}\right\rfloor,qquad
t=L+N-1.
\tag{6}
\]

Suppose

\[
d\geq4,\quad N\geq L,\quad t\geq n_0,
\quad \frac{8CN^2\lambda}{d}\geq1,
\quad \lambda\geq32C.
\tag{7}
\]

The condition `N>=L` is the precise safe meaning of
`d/log^2(d) >> L` needed here.  It gives `t<2N`.  Also `N<=d` and `d>=4`
give `log(4N)<=log(4d)<=2lambda`.  Applying (5) only at the last index,

\[
a_t\leq Ct^2\log(2t)
<4CN^2\log(4N)
\leq8CN^2\lambda.
\tag{8}
\]

By (4), the penultimate condition in (7), and (8),

\[
B\leq\frac{8CN^2\lambda}{d}+1
\leq\frac{16CN^2\lambda}{d}.
\tag{9}
\]

Insert this into (3).  Since
`N<=d/lambda^2<=d/(32C lambda)`,

\[
\boxed{
\rho_\infty(d)-\rho_L(d)
\geq\rho_{L+N}(d)-\rho_L(d)
\geq\frac{d}{64C\log d}.}
\tag{10}
\]

All floor errors are visible in (3), (4), and (6).  The constants in (7)
are deliberately safe rather than optimized.  Before the last simplification
one retains the stronger exact lower expression

\[
\frac12\left(
\frac{N^2}{8CN^2\lambda/d+1}-N
\right).
\tag{11}
\]

The hypotheses in (7) hold for every sufficiently large `d` whenever
`N>=L` and (5) holds.  Infinitude without (5) is not enough, as the Wave 13
example `a_n=2^n-1` already shows.

## 3. Application to macroscopic Wave 13 suffix atoms

At dyadic epoch `m`, let

\[
d_{m,p}=a_{2m-1}-a_{p-1},\qquad 2\leq p\leq2m-2,
\tag{12}
\]

with terminal-suffix coefficient

\[
u_{m,p}=\frac{12m-5-6p}{16m^2}
\quad(2\leq p\leq2m-3),
\tag{13}
\]

and the separate last coefficient `u_(m,2m-2)=11/(16m^2)`.
Consider only the macroscopic subfan `2<=p<=m`.  Its interval length
`ell=2m-p` is at least `m`.  The `ell+1` marks inside that interval determine
`binom(ell+1,2)` distinct positive integer differences, all at most its
diameter.  Hence

\[
d_{m,p}\geq D_m:=\frac{m(m+1)}2.
\tag{14}
\]

For all sufficiently large `m`, (5) also gives

\[
d_{m,p}\leq a_{2m-1}
<A_m:=4Cm^2\log(4m).
\tag{15}
\]

For complete explicitness, (7) follows simultaneously for every
`2<=p<=m` once `2m-1>=n_0` and `m` is large enough that

\[
\begin{gathered}
m+1\geq6(\log A_m)^2,\qquad
\log D_m\geq32C,\\
2CD_m\geq(\log A_m)^3.
\end{gathered}
\tag{16}
\]

Indeed, (14)--(16) give

\[
\frac{d_{m,p}}{(\log d_{m,p})^2}
\geq\frac{D_m}{(\log A_m)^2}\geq3m,
\]

so the floor in (6) is at least `2m=L`.  If
`x=d/(log d)^2`, then `x>=3m` and `N>=x/2`; the last condition in (16)
therefore gives `8CN^2 log(d)/d>=1`.  The remaining conditions in (7) are
immediate.  This makes the phrase "sufficiently large depending on `C` and
the onset of the cap" fully quantitative.

Put

\[
\pi_{m,p}=\rho_\infty(d_{m,p})-\rho_{2m}(d_{m,p}).
\tag{17}
\]

Since distinct positive integers not exceeding `d` number at most `d`,

\[
\rho_{2m}(d_{m,p})\leq d_{m,p}.
\tag{18}
\]

Equations (10), (17), and (18) imply

\[
\log\frac{\rho_\infty(d_{m,p})}{\rho_{2m}(d_{m,p})}
\geq
\log\left(1+\frac1{64C\log d_{m,p}}\right).
\tag{19}
\]

If additionally `m>=max{4,4C}` then
`log A_m<=4log m`.  Once `256C log m>=1`, put
`x=1/(64C\log d_(m,p))`.  If `x<=1`, the elementary inequality
`log(1+x)>=x/2` gives the bound below.  If `x>1`, then
`log(1+x)>=log 2>1/2`, while `1/(512C\log m)<=1/2`, so the same bound
still follows.  Thus, in both cases,

\[
\boxed{
\log\frac{\rho_\infty(d_{m,p})}{\rho_{2m}(d_{m,p})}
\geq\frac1{512C\log m}
\qquad(2\leq p\leq m).}
\tag{20}
\]

The exact weight of this subfan is

\[
\sum_{p=2}^{m}u_{m,p}
=\frac{(m-1)(9m-11)}{16m^2}
\geq\frac12\qquad(m\geq20).
\tag{21}
\]

Thus the promised weighted promotion premium is

\[
\boxed{
\Gamma_m:=
\sum_{p=2}^{m}u_{m,p}
\log\frac{\rho_\infty(d_{m,p})}{\rho_{2m}(d_{m,p})}
\geq\frac1{1024C\log m}}
\tag{22}
\]

for every sufficiently large dyadic `m` on the same fixed branch.

## 4. What (22) does and does not buy

Wave 13's new-birth barrier has asymptotic per-epoch coefficient

\[
Z_m\geq \frac1{1536C\log(4m)}.
\tag{23}
\]

The coefficient `1/1024` in (22) is asymptotically `3/2` times
`1/1536`.  This is genuine budget headroom at exactly the required harmonic
scale.  It also proves that eventual ranks contain information absent from
the finite rank/length/containment floor.

The direction, however, is not yet repayment.  In the Wave 13 identity

\[
\log d=\log\rho_\infty(d)+
       \log\frac d{\rho_\infty(d)},
\]

promotion increases the first positive suffix term and decreases the hole
term by the same amount; their sum is unchanged.  Moreover, one future
difference can promote many nested old thresholds and many dyadic epochs.
Nothing above assigns the promoted values to the negative interior bulk or
to the terminal tail with bounded total reuse.

Therefore (22) is a **promotion theorem and a quantified resource**, not an
upper bound for the frontier difference and not a proof of the Wave 13
allocation target.  The remaining falsifiable lemma is:

> map the promoted future differences counted by (10), with the suffix
> weights in (13), to later negative bulk or terminal-tail atoms, while
> proving a cross-epoch bounded-overlap estimate strong enough to retain a
> positive fraction of the `1/1024` coefficient.

Without that signed allocation, subtracting (22) from the positive frontier
would be a sign error.

## 5. Finite verification artifact

`wave14_future_rank_promotion.py` implements (3) exactly with rational
arithmetic after a finite Golomb check.  Its test on the 128-mark
Erdős--Turán fixture uses `L=16`, `d=7935`, and
`N=floor(d/log(d)^2)=98`.  Seven occupied bins give 696 same-bin pairs,
against the Cauchy floor `4459/7`; the observed rank promotion is 1468.
This verifies the finite mechanism only.  It is not evidence for an
infinite branch satisfying (5).
