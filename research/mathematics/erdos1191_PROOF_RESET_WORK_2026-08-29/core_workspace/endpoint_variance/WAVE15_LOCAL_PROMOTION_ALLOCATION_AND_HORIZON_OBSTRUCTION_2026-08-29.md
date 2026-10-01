# Wave 15: local promotion allocation and the horizon obstruction

Date: 2026-08-29 (Asia/Tokyo)  
Status: **rigorous adjacent-epoch allocation; global signed upper still open**

Wave 14 proved that every macroscopic old suffix difference acquires a
harmonic amount of future rank.  This note localizes a harmonic part of that
promotion to the immediately following dyadic block and maps its complete
nested reuse load into literal negative atoms of the next Wave 13 interior
bulk.

The allocation is valid for the marginal log-rank increment defined below.
It is not a disjoint premium over the existing Wave 10 or Wave 11 floors, and
it does not pay the raw positive term `u_(m,p) log d_(m,p)`.  Reindexing the
negative bulks leaves a terminal fan of order `log M`, so `P19`, Question 1,
Question 2, and the prize claim remain unresolved.

Throughout, work on one fixed infinite normalized integer Golomb ruler which
satisfies

\[
 a_n\leq Cn^2\log(2n)
\tag{1}
\]

eventually.

## 1. A next-block rank increment

Fix a sufficiently large dyadic `m`, and put

\[
 d_p=d_{m,p}=a_{2m-1}-a_{p-1},
 \qquad 2\leq p\leq m.
\tag{2}
\]

Use the next block of `N=2m-1` marks

\[
 V_m=\{a_{2m},a_{2m+1},\ldots,a_{4m-2}\}.
\tag{3}
\]

Partition `V_m` into half-open spatial bins of width `d=d_p`.  If `b(d)` is
the number of occupied bins, then (1) gives, eventually,

\[
 b(d)
 \leq\left\lfloor{a_{4m-2}\over d}\right\rfloor+1
 \leq{2a_{4m-2}\over d}
 <{32Cm^2\log(8m)\over d}.
\tag{4}
\]

The interval in (2) contains `ell+1=2m-p+1` marks, where `ell>=m`.
All of its pair differences are distinct positive integers at most `d_p`, so

\[
 d_p\geq\binom{\ell+1}{2}\geq{m(m+1)\over2}.
\tag{5}
\]

In particular, once

\[
 2m-1\geq128C\log(8m),
\tag{6}
\]

one has `N>=2b(d_p)` simultaneously for every `2<=p<=m`.  If the bin
occupancies are `n_s`, Cauchy--Schwarz gives

\[
 \begin{aligned}
 S(d_p)&:=\sum_s\binom{n_s}{2}
 =\frac12\left(\sum_s n_s^2-N\right)\\
 &\geq\frac12\left({N^2\over b(d_p)}-N\right)
 \geq{N^2\over4b(d_p)}.
 \end{aligned}
\tag{7}
\]

Equations (4)--(7) imply

\[
 \boxed{
 S(d_p)\geq{d_p\over128C\log(8m)}
 \geq{m(m+1)\over256C\log(8m)}.}
\tag{8}
\]

Every same-bin pair has difference strictly below `d_p`, and global Golomb
uniqueness makes all of these new differences distinct.

Let

\[
 r_p=\rho_{2m}(d_p),\qquad
 K_p=\rho_{4m-1}(d_p)-\rho_{2m}(d_p).
\tag{9}
\]

The witnesses in (8) prove

\[
 K_p\geq{d_p\over128C\log(8m)}.
\tag{10}
\]

## 2. Every relevant new difference is a next-bulk atom

A new difference `x=a_j-a_i<=d_p` born between the prefixes of `2m` and
`4m-1` marks has `j>=2m`.  The case `i=0` is impossible, because then

\[
 x=a_j>a_{2m-1}\geq d_p.
\tag{11}
\]

Thus `i>=1`, and

\[
 x=D_{i+1,j},\qquad 2m\leq j\leq4m-2,
\tag{12}
\]

is literally an atom of the Gothic interior bulk `mathfrak B_(2m)`.  Its
coefficient is

\[
 \beta_{2m}(i,j)=
 \begin{cases}
 1/(4m^2),&j-i=1,\\
 1/(16m^2),&j-i=2,\\
 1/(8m^2),&j-i\geq3,
 \end{cases}
\tag{13}
\]

and hence

\[
 \boxed{\beta_{2m}(i,j)\geq{1\over16m^2}.}
\tag{14}
\]

## 3. The nested reuse load is bounded

Use the exact Wave 13 suffix weights

\[
 u_{m,p}={12m-5-6p\over16m^2}
 \qquad(2\leq p\leq m)
\tag{15}
\]

and define the immediately realized promotion

\[
 \Delta_m=\sum_{p=2}^{m}u_{m,p}
 \log\left(1+{K_p\over r_p}\right).
\tag{16}
\]

The thresholds satisfy `d_2>d_3>...>d_m`; no incompatible choice of separate
bin witnesses is needed.  From `log(1+t)<=t`, the load placed on a newly born
numerical difference `x` is

\[
 L_m(x)=\sum_{\substack{2\leq p\leq m\\x\leq d_p}}
 {u_{m,p}\over r_p},
 \qquad
 \Delta_m\leq\sum_xL_m(x).
\tag{17}
\]

Writing `ell=2m-p`, one has

\[
 u_{m,p}={6\ell-5\over16m^2},
 \qquad
 r_p\geq\binom{\ell+1}{2}.
\tag{18}
\]

Therefore every single new difference has total reuse load

\[
 \begin{aligned}
 L_m(x)
 &\leq\sum_{\ell=m}^{2m-2}
 {6\ell-5\over8m^2\ell(\ell+1)}\\
 &<{3\over4m^2}\sum_{\ell=m}^{2m-2}{1\over\ell+1}
 <\boxed{{3\over4m^2}}.
 \end{aligned}
\tag{19}
\]

Let `T=ceil(e^12)`.  For every new `x>=T`, (14) and (19) give

\[
 \beta_{2m}(x)\log x
 \geq{12\over16m^2}
 ={3\over4m^2}>L_m(x).
\tag{20}
\]

There are at most `T-1` distinct positive integer values below `T`.
Discarding their loads yields the exact adjacent-epoch allocation

\[
 \boxed{
 \Delta_m\leq\mathfrak B_{2m}
 +{3(\lceil e^{12}\rceil-1)\over4m^2}.}
\tag{21}
\]

The error is summable over dyadic `m`.

The role of `log x` in (20) is essential.  Equation (21) pays the
dimensionless marginal log-rank term in (16); it does not pay
`u_(m,p) log d_p`.  Since `x<=d_p` gives `log x<=log d_p`, the latter proposed
charge has the wrong inequality direction.

## 4. Harmonic size and exact limitation

Integer spacing gives `r_p<=d_p`.  Hence (10), together with
`log(1+t)>=t/2` in the small-`t` regime (and the trivial complementary case),
implies eventually

\[
 \log\left(1+{K_p\over r_p}\right)
 \geq{1\over256C\log(8m)}.
\tag{22}
\]

The exact macroscopic `u`-mass obeys

\[
 \sum_{p=2}^{m}u_{m,p}
 ={(m-1)(9m-11)\over16m^2}\geq{1\over2}
 \qquad(m\geq20).
\tag{23}
\]

Thus

\[
 \boxed{\Delta_m\geq{1\over512C\log(8m)}}
\tag{24}
\]

for every sufficiently large dyadic `m`.  This identifies a harmonic part of
the positive promotion channel whose complete within-epoch reuse load fits
inside the next negative bulk.

It is important that (21) uses the full literal value of selected
`mathfrak B_(2m)` atoms.  It does **not** prove

\[
 \mathfrak B_{2m}\geq
 \text{(an existing rank/length floor)}+\Delta_m-O(m^{-2}).
\tag{25}
\]

Therefore (21) cannot simply be added to `K^len`, `K^mix`, or the Wave 10
global rearrangement floor.  Proving a disjoint premium such as (25) is a
separate missing inequality.

There is also a genuine horizon obstruction.  For each suffix atom,

\[
 \log d_p
 =\log r_p
 +\log{\rho_{4m-1}(d_p)\over r_p}
 +\log{\rho_\infty(d_p)\over\rho_{4m-1}(d_p)}
 +\log{d_p\over\rho_\infty(d_p)}.
\tag{26}
\]

Only the second term is handled by (21).  Reindexing the immediate-neighbour
allocations over a finite dyadic horizon leaves the terminal fan.  At
`M=2^J`,

\[
 \mathfrak U_M\geq{1\over2}\log{M(M+1)\over2}
 =\Theta(\log M)=\Theta(J),
\tag{27}
\]

which is much larger than the required `o(log J)` scale.  Borrowing
`mathfrak B_(2M)` from beyond the horizon is invalid without an exact
terminal potential.

Nor can one send all earlier loads to a single much later birth epoch.  If
`m=M/2^k`, the source load can be of order `1/m^2`, while the smallest Gothic
bulk coefficient at epoch `M` is `1/(4M^2)`.  Their ratio grows like
`3*4^k`; the current cap does not force the numerical value born at that
later epoch to supply the corresponding logarithmic factor.

Thus Wave 15 solves the nested reuse problem inside one adjacent epoch, but
the all-epoch birth-time allocation and the disjoint-floor problem remain
open.

## 5. Finite calibration and countercheck

The deterministic Wave 15 probe records the following mechanism checks:

| fixture | `m` | minimum future-future count | `Delta_m` | selected literal-`B_(2m)` capacity |
|---|---:|---:|---:|---:|
| Hall 64 | 4 | 6 | 0.116177 | 0.685518 |
| Hall 64 | 8 | 39 | 0.173403 | 0.877240 |
| Hall 64 | 16 | 222 | 0.265625 | 1.476791 |
| Erdős--Turán 128 | 4 | 15 | 0.223784 | 2.131468 |
| Erdős--Turán 128 | 8 | 84 | 0.387305 | 3.358074 |
| Erdős--Turán 128 | 16 | 351 | 0.464170 | 3.996318 |
| Erdős--Turán 128 | 32 | 1465 | 0.504070 | 4.498849 |

Every row has zero atomwise deficit for the valid marginal-rank allocation.
As an adversarial countercheck, equal-share allocation of the raw positive
`u_(m,p) log d_p` fails: Hall 64 at `m=16` leaves an unpaid `2.65023`, and the
Erdős--Turán row at `m=32` leaves an atomwise unpaid `1.60917`.

These finite fixtures do not satisfy the deliberately conservative
asymptotic side condition (6).  They certify the finite mechanism and the
raw-charge failure only; they do not certify an infinite branch or an
asymptotic conclusion.
