# Fixed-width difference density forced by one critical cap

Date: 2026-09-05. Author: `/root`, GPT-6 Astra Ultra.
Status: supporting mathematical result only; original Q1 is unresolved.
This note is not a Lean verification or a proof release.

Let `a_1<a_2<...` be a positive integer Sidon sequence, with repeated
summands included. Assume, conditionally throughout,

\[
 a_n\le Cn^2\log(2n)\quad(n\ge n_0),\qquad C>0,       \tag{1}
\]

with one fixed onset. Put `P_p={a_1,...,a_p}` and, for an integer `D>=2`,

\[
 F_p(D)=\Delta P_p\cap[1,D],\qquad M_p(D)=|F_p(D)|.
\]

All positive differences have unique endpoint pairs. Thus the internal
difference sets of disjoint rank blocks are disjoint, even if their
integer intervals overlap. Fix `1/2<theta_0<=theta_1<1`; all errors below
are uniform for `theta` in this closed interval and `p=floor(D^theta)`.

## 1. Exact short-label inequality with a literal interval carrier

For any finite Sidon block `B` of cardinality `m` and integer interval
length `L=max B-min B+1`, convolve its indicator with that of
`I_D={0,...,D-1}`. Its total mass is `mD`, its support is contained in an
interval of length `L+D-1`, and its squared norm is exactly

\[
 \|1_B*1_{I_D}\|_2^2
 =mD+2\sum_{t\in\Delta B}(D-t)_+ .                 \tag{2}
\]

The diagonal term is `mD`; Sidon difference uniqueness supplies every
off-diagonal term once in each orientation. Cauchy--Schwarz therefore gives

\[
 Q_D(B):=\sum_{t\in\Delta B}(1-t/D)_+
 \ge\frac{m^2D}{2(L+D-1)}-\frac m2.                 \tag{3}
\]

This requires neither old-label support nor a forbidden-point exclusion.
In particular the denominator is not silently shortened by `m`.

## 2. A positive proportion of one fixed physical interval appears early

Take the disjoint dyadic rank blocks
`B_m={a_(m+1),...,a_(2m)}`, where `m` is a power of two and
`sqrt D<=m<=p/2`. For sufficiently large `D`, all these ranks exceed the
fixed onset in (1), and their interval lengths obey

\[
 L_m\le4Cm^2\log(4m),\qquad
 L_m+D-1\le5Cm^2\log(4m).                           \tag{4}
\]

The second inequality uses `D<=m^2` and `1<=C log(4m)`; both hold uniformly
in the selected range. No bound on the span of `F_p(D)` is needed here.
Every nonzero term of (3) belongs to `F_p(D)`, and distinct blocks use
disjoint physical labels. Summing (3) and using `sum m<p` gives

\[
 \sum_{t\in F_p(D)}(1-t/D)
 \ge\frac D{10C}
       \sum_{\sqrt D\le2^r\le p/2}\frac1{\log(4\cdot2^r)}
       -\frac p2.                                  \tag{5}
\]

For integer endpoints `r_- = ceil(log_2 sqrt D)` and
`r_+ = floor(log_2(p/2))`, the sum equals
`(log 2)^(-1) sum_(r_-<=r<=r_+) 1/(r+2)`. Integral comparison gives

\[
 \sum_{\sqrt D\le2^r\le p/2}\frac1{\log(4\cdot2^r)}
 =\frac{\log(2\theta)}{\log2}+O(1/\log D).          \tag{6}
\]

Indeed `r_-=(log D)/(2 log 2)+O(1)` and
`r_+=(theta log D)/(log 2)+O(1)`; these errors and the harmonic-sum
error are uniform on the specified compact interval. Since
`p/D<=D^(theta_1-1)`, (5) proves the stronger, weighted conclusion

\[
 \boxed{\quad
 \frac1D\sum_{t\in F_{\lfloor D^\theta\rfloor}(D)}(1-t/D)
 \ge\frac{\log(2\theta)}{10C\log2}-o(1).
 \quad}                                             \tag{7}
\]

Consequently, with the explicit positive constant

\[
 c=\min\left\{\frac12,
              \frac{\log(2\theta_0)}{20C\log2}\right\},
\]

we have `M_p(D)>=cD` for every sufficiently large `D`, uniformly in
`theta`. These are nested banks in the **same** interval `[1,D]` as `p`
varies. They are not independently chosen dense subsets, and the onset
does not move with `D`.

## 3. The dense bank must already contain quadratically many Schur relations

Fix `F=F_p(D)`, `M=|F|`, and write
`K_F(t)=sum_x 1_F(x)1_F(x+t)`. Convolving this carrier with each of the
same past rank blocks gives the exact squared norm

\[
 mM+2\sum_{t\in\Delta B_m}K_F(t)
 =\|1_{B_m}*1_F\|_2^2
 \ge\frac{m^2M^2}{L_m+\operatorname{diam}F}.          \tag{8}
\]

Its support length is exactly bounded by the displayed denominator.
Because `diam F<=D-1`, (4) applies again. Every label with a nonzero
kernel value is at most `D-1`; if it also belongs to a past block's
differences then it belongs to `F`. Thus

\[
 T(F):=\sum_{t\in F}K_F(t)
 \ge\frac{M^2}{10C}
       \sum_{\sqrt D\le2^r\le p/2}\frac1{\log(4\cdot2^r)}
       -\frac{pM}{2}.                               \tag{9}
\]

The bound `M>=cD` makes `p/M=o(1)`. Combining (6) and (9), for all
sufficiently large `D`, gives

\[
 \boxed{\quad T(F_p(D))\ge\kappa M_p(D)^2
                   \ge\kappa c^2D^2,\qquad
 \kappa=\frac{\log(2\theta_0)}{20C\log2}>0.
 \quad}                                             \tag{10}
\]

If a chosen constant forced a lower bound exceeding an elementary total
capacity, that would already exclude that cap; no existence assertion is
made for every numerical `C`. The proof of (10) never assumes that
`K_F` is spatially uniform. It uses the entire capped past to force its
correlation with actual old labels.

## 4. What this does and does not imply for the birth law

Equations (7)--(10) establish the density premise used conditionally in
[nested_small_difference_bank.md](nested_small_difference_bank.md), §5.
Combining (10) with that note's exact birth identity gives

\[
 2\sum_{n\le p} R_n+
   \sum_{n\le p}(S^{00}_n+S^{11}_n)
 \ge\kappa c^2D^2-\sqrt2D^{3/2}.                   \tag{11}
\]

This is an early-rank requirement for real three-sum equalities, with their
physical difference labels and latest endpoints retained. It is compatible
with the ordinary `O(p^4)` bound for a Sidon set's sixth moment because
`theta>1/2`. An additional localized or coupled bound is required to turn
it into a contradiction.

The argument does not supply another independent budget for each width
`D`: a label and a relation recur when `D` is enlarged. Nor does a positive
proportion of old labels by itself force pointwise correlation estimates.
No proof or counterexample of original Q1, and no new Lean theorem, is
asserted here.
