# Wave 13: the cross-length `n^2` no-go and an eventual-rank frontier target

Date: 2026-08-29 (Asia/Tokyo)  
Status: **rigorous no-go example and an explicitly unproved survival target**

This note isolates which part of contiguous-sum uniqueness is still absent
from the Wave 13 frontier analysis.  It proves that integer unit spacing,
distinct adjacent gaps, and uniqueness within every fixed interval length do
not control the birth energy.  It then records an exact eventual-rank
decomposition for the moving frontier.  No rank-promotion estimate or
allocation inequality is proved, and Erdős Problem #1191 remains open.

Throughout, for marks `a_0<a_1<...` put

\[
D_{p,q}=a_q-a_{p-1},\qquad
C_{ij}=\log\frac{D_{i,j-1}D_{i+1,j}}
                    {D_{i+1,j-1}D_{i,j}},
\]

and

\[
Y_m=\sum_{j=m}^{2m-1}\sum_{i=1}^{j-2}
       \left(\frac{j-i}{2m}\right)^2C_{ij}.
\tag{1}
\]

## 1. An integer quadratic model with all fixed-length rows injective

Consider

\[
a_n=n^2\qquad(n\geq0).
\tag{2}
\]

This is an increasing normalized sequence of integers.  Its adjacent gaps
are

\[
h_k=a_k-a_{k-1}=2k-1,
\tag{3}
\]

so all adjacent gaps are distinct positive integers.

More is true.  For every fixed positive length `r`, the consecutive
`r`-gap window starting at `u` has value

\[
W_{u,r}=a_{u+r}-a_u=2ru+r^2.
\tag{4}
\]

For fixed `r`, (4) is strictly increasing in `u`.  Hence every row of fixed
interval length is injective, for every length, not merely for lengths one
or two.

The sequence is nevertheless not a Golomb ruler.  Cross-length uniqueness
fails, for example,

\[
a_5-a_1=25-1=24=49-25=a_7-a_5.
\tag{5}
\]

Thus the missing distinction is genuinely **across different interval
lengths**.  Within-length sorting, even simultaneously for every length,
does not recover the Golomb condition.

## 2. Its birth energy has a positive limit

Let

\[
r=j-i,\qquad s=i+j-1.
\]

For (2), direct factorization of the four interval differences gives

\[
\begin{aligned}
D_{i,j-1}&=r(s-1),& D_{i+1,j}&=r(s+1),\\
D_{i+1,j-1}&=(r-1)s,& D_{i,j}&=(r+1)s.
\end{aligned}
\]

Consequently

\[
C_{ij}
=\log\left(\frac{r^2}{r^2-1}\frac{s^2-1}{s^2}\right)
=\log\frac{1-s^{-2}}{1-r^{-2}}.
\tag{6}
\]

Here `r>=2` and `s-r=2i-1>=1`, so `s>r` and `C_(i,j)>0`.
For `i/m -> x` and `j/m -> y`, with `1<=y<=2` and `0<=x<=y`, one has

\[
m^2\left(\frac r{2m}\right)^2C_{ij}
\longrightarrow
\frac14\left(1-\frac{(y-x)^2}{(y+x)^2}\right)
=\frac{xy}{(x+y)^2}.
\tag{7}
\]

There is a uniform summable Riemann majorant.  From `s>r>=2`,

\[
0<C_{ij}\leq-\log(1-r^{-2})\leq\frac1{r^2-1},
\]

and therefore

\[
0\leq\left(\frac r{2m}\right)^2C_{ij}
\leq\frac1{3m^2}.
\tag{8}
\]

The diagonal strip omitted by `r>=2` has vanishing normalized area, so
dominated Riemann convergence yields

\[
\begin{aligned}
\lim_{m\to\infty}Y_m
&=\int_1^2\int_0^y\frac{xy}{(x+y)^2}\,dx\,dy\\
&=\int_1^2 y\,dy\int_0^1\frac{t}{(1+t)^2}\,dt\\
&=\frac32\left(\log2-\frac12\right)>0.
\end{aligned}
\tag{9}
\]

This is the same limiting integral as the Wave 12 real-Golomb model, but
the present example is entirely integral.  It is **not** a counterexample to
#1191 because of the explicit cross-length collision (5).

Equations (2)--(9) prove the following method boundary:

> Integer unit spacing, distinct adjacent gaps, quadratic growth, the exact
> cross-ratio kernel, and injectivity of every individual fixed-length row
> still allow nondecaying `Y_m`.  Any successful upper estimate must use
> cross-length contiguous-sum uniqueness, and must use it in a way that is
> coupled across an unbounded history on one fixed branch.

## 3. Exact eventual-rank decomposition of a frontier atom

Now return to a genuine infinite integer Golomb ruler.  For a prefix with
marks `a_0,...,a_(L-1)`, define

\[
\Delta_L=\{D_{r,s}:1\leq r\leq s\leq L-1\}.
\]

All members of `Delta_L` are distinct positive integers.  For `d` which is
already a difference in this prefix, let

\[
\rho_L(d)=|\{e\in\Delta_L:e\leq d\}|.
\tag{10}
\]

For fixed `d`, `rho_L(d)` is nondecreasing in `L` and is at most `d`.
It therefore stabilizes, and we may define

\[
\rho_\infty(d)=\lim_{L\to\infty}\rho_L(d)\leq d.
\tag{11}
\]

For the terminal suffix atoms in the Wave 13 frontier, put

\[
d_{m,p}=D_{p,2m-1}\qquad(2\leq p\leq2m-2)
\tag{12}
\]

and use their exact coefficients

\[
u_{m,p}=
\begin{cases}
(12m-5-6p)/(16m^2),&2\leq p\leq2m-3,\\
11/(16m^2),&p=2m-2.
\end{cases}
\tag{13}
\]

Each atom has the exact decomposition

\[
\boxed{
\log d_{m,p}
=\log\rho_\infty(d_{m,p})
 +\log\frac{d_{m,p}}{\rho_\infty(d_{m,p})}.}
\tag{14}
\]

The second term is nonnegative.  It is the logarithmic premium of the
integer holes at or below `d_(m,p)` which are never filled by any future
interval difference.  The genuinely new survival datum is the promotion

\[
\pi_{m,p}=\rho_\infty(d_{m,p})-\rho_{2m}(d_{m,p})\geq0,
\tag{15}
\]

which counts future, necessarily cross-epoch differences below the old
frontier value.

This decomposition is an identity, not an estimate.  In particular, no
claim is made that the eventual hole premium is small.

## 4. A precise, unproved allocation target

Let `mathfrak B_m` and `X_m=mathfrak U_m-mathfrak B_m` be the exact Wave 13
interior bulk and frontier difference.  For a finite dyadic horizon define

\[
\begin{aligned}
\mathcal A_J
&=\sum_{m\in E_J}\sum_{p=2}^{2m-2}
 u_{m,p}\log\rho_\infty(d_{m,p})
 -\sum_{m\in E_J}\mathfrak B_m,\\
\mathcal H_J
&=\sum_{m\in E_J}\sum_{p=2}^{2m-2}
 u_{m,p}\log\frac{d_{m,p}}{\rho_\infty(d_{m,p})}.
\end{aligned}
\tag{16}
\]

Summing (14) with the exact coefficients gives the exact identity

\[
\boxed{\sum_{m\in E_J}X_m=\mathcal A_J+\mathcal H_J.}
\tag{17}
\]

Thus a fully specified sufficient frontier allocation theorem would have to
prove, on the same hypothetical eventually `C`-critical branch, that for
some `eta_C>0`,

\[
\mathcal A_J+\mathcal H_J
\leq
\left(\frac{1}{1536C\log2}-\eta_C\right)\log J+O_C(1).
\tag{18}
\]

Equation (18), together with the proved Wave 13 lower bound on `sum X_m`,
would contradict the existence of that branch.  Neither (18) nor separate
upper estimates of the required strength for `mathcal A_J` and
`mathcal H_J` are proved here.  Writing (18) down does not advance the claim
status by itself; its value is to identify exactly where future cross-length
rank promotion would have to enter a valid allocation.

Current numerical ranks, triangular length floors, and the complete
containment order cannot be substituted for `rho_infinity`: Wave 12 already
proves that their jointly optimized gain is only `O(1)` per epoch.  The new
quantity in (15) explicitly records differences born after the frontier
atom.

## 5. Infinitude alone does not promote ranks

The polynomial-log cap is indispensable to any proposed promotion theorem.
Consider the normalized integer sequence

\[
a_n=2^n-1.
\tag{19}
\]

It is a Golomb ruler.  Indeed,

\[
2^j-2^i=2^i(2^{j-i}-1),
\]

and equality of two positive differences first identifies the lower index
by the `2`-adic valuation and then identifies the length from the remaining
odd factor.

For every fixed `d`, once the next adjacent gap `2^(n-1)` exceeds `d`, every
new difference involving a later mark also exceeds `d`.  Hence the rank of
`d` receives no further promotion after that point; old numerical holes can
remain unfilled forever.

This example is exponentially sparse and violates the critical cap.  It is
not a counterexample to the proposed cap-dependent program.  It proves only
the necessary guardrail:

> Infinite survival by itself gives no eventual-rank filling.  Any proof of
> (18), or of a stronger separated allocation bound, must quantitatively use
> the assumed `O(n^2 log n)` growth as well as full cross-length Golomb
> uniqueness.

## 6. Claim boundary

The `n^2` computations and the `2^n-1` Golomb proof are exact.  The
eventual-rank decomposition (14)--(17) is also exact on every infinite
integer Golomb ruler.  No useful upper bound for either term in (16) is
proved.  In particular, this note does not prove P17, P18, the frontier
allocation inequality (18), Question 1, Question 2, or a prize claim.
