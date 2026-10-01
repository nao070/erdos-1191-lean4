# Wave 10: hereditary log-product packing and the exact birth-shell spectrum

**Date:** 2026-08-29 (Asia/Tokyo)  
**Status:** rigorous logarithmic strengthening of W9-RLP, exact dyadic-shell
Abel signs, and a quantified relaxation barrier; P15 and Erdős Problem #1191
remain open

## 1. Outcome

Wave 9 imported a hereditary **linear** rank-lag inequality from the
difference-triangle literature.  The primitive cross-ratio state, however,
is a signed sum of logarithms of interval differences.  This note aligns the
two objects exactly.

1. Every selected family of `M` birth differences on one Golomb branch has
   product at least `M!`.  With arbitrary nonnegative rational weights, an
   exact rearrangement floor is available after clearing denominators.
2. The dyadic genuine cross-ratio birth shell has a complete sign
   classification simpler than the general four-indicator formula.  Its
   negative non-full-span intervals have right endpoints in
   `[m-1,2m-2]`; these ranges are disjoint over dyadic `m`.  Hence all of
   their differences may be placed in **one global weighted product
   inequality**, for every finite epoch subset.
3. This is a real hereditary logarithmic upgrade of W9-RLP and is directly
   dual to the Abel objective.  Nevertheless the exact coefficient
   multiset exposes a barrier: the one-shell rearrangement floor is only

   \[
   \mathcal L_m={7\over4}\log m+O(1).
   \]

   After the critical diameter cap, the direct shell relaxation still loses
   `1/4 log m+log log m+O_C(1)` at one scale.  The companion analysis
   `WAVE10_LAMINAR_WEIGHTED_TRIANGLE_ANALYSIS_2026-08-29.md`, Theorem 5,
   separately proves that simultaneous global sorting over arbitrary dyadic
   epoch sets retains the same `7/4` leading coefficient up to `O(|E|)`.
   Thus global distinctness plus the shell coefficient multiset is not the
   missing P15 theorem.  One must also use interval consistency or infinite-
   survival information governing where new differences can lie among old
   holes.

No infinite construction, asymptotic contradiction, or prize claim is made.

## 2. Hereditary factorial packing

Let

\[
 A=\{a_0=0<a_1<a_2<\cdots\}
\]

be a Golomb ruler, so every positive difference `a_v-a_u`, `u<v`, is unique.
For a finite dyadic epoch set `E` and integers `1<=q_m<=m`, put

\[
 \mathcal F(E,q)=
 \{(j-s,j):m\in E,\ 1\leq s\leq q_m,\ m\leq j<2m\},
 \qquad
 M_E=\sum_{m\in E}m q_m.
\]

The right-endpoint shells are disjoint, so the mark pairs in `F(E,q)` are
distinct.

### Theorem 1 (W10-HLP)

For every finite `E`,

\[
 \boxed{
 \prod_{m\in E}\prod_{s=1}^{q_m}\prod_{j=m}^{2m-1}
 (a_j-a_{j-s})\ \geq\ M_E!.}
\tag{HLP}
\]

Equivalently,

\[
 \sum_{m\in E}\sum_{s=1}^{q_m}\sum_{j=m}^{2m-1}
 \log(a_j-a_{j-s})\geq\log(M_E!).
\tag{1}
\]

#### Proof

The selected mark pairs are distinct, and the Golomb property makes their
`M_E` positive integer differences distinct.  If their increasing ordering
is `d_1<...<d_(M_E)`, then `d_r>=r`.  Multiplication proves (HLP).  `square`

This statement is not obtained by taking logarithms of W9-RLP: it is a
strictly different consequence of the same global injection and is exactly
in the functional language needed by the cross-ratio Abel expansion.

## 3. Weighted version

The form needed below allows unequal Abel coefficients.

### Theorem 2 (weighted rearrangement floor)

Let `d_1,...,d_M` be distinct positive integers, and attach arbitrary
nonnegative weights `lambda_1,...,lambda_M`.  Write
`lambda_1^down>=...>=lambda_M^down` for the decreasing rearrangement.  Then

\[
 \boxed{
 \sum_{t=1}^M\lambda_t\log d_t
 \geq\sum_{r=1}^M\lambda_r^\downarrow\log r.}
\tag{2}
\]

If all weights are rational, (2) is an exact integer product inequality after
multiplication by their common denominator.

#### Proof

Order the values increasingly.  The ordinary rearrangement inequality says
that the weighted logarithmic sum is minimized when the largest weight is
assigned to the smallest value.  The `r`th increasing distinct positive
integer is at least `r`.  Applying the monotonicity of `log` proves (2).
After clearing denominators, exponentiation gives an inequality between two
integers.  `square`

Because the conclusion holds for the full selected family, it automatically
holds for every subfamily.  It is therefore a hereditary constraint suitable
for an exact LP dual; no averaging or asymptotic limiting step is involved.

## 4. Exact Abel signs for one dyadic birth shell

Fix `m>=4`, put `n=2m`, `g=n-1`, and write

\[
 D_{p,q}=a_q-a_{p-1}=\sum_{r=p}^q h_r,
 \qquad
 w_0=w_1=0,\quad w_r={r^2\over n^2}\quad(r\geq2).
\]

For genuine nonadjacent gaps, let

\[
 C_{ij}=\log{D_{i,j-1}D_{i+1,j}\over D_{i+1,j-1}D_{i,j}},
\]

and define the unretained birth shell

\[
 Y_m=\sum_{j=m}^{g}\sum_{i=1}^{j-2}w_{j-i}C_{ij}.
\tag{3}
\]

Define the positive boundary functional

\[
\begin{aligned}
 U_m={}&w_{m-1}\log D_{1,m-1}
 +\sum_{q=m}^{g-1}(w_q-w_{q-1})\log D_{1,q}\\
 &+w_2\log D_{g-1,g}
 +\sum_{\ell=3}^{g-1}(w_\ell-w_{\ell-1})
   \log D_{n-\ell,g}.
\end{aligned}
\tag{4}
\]

Let

\[
 \mathcal I_m=\{(p,q):2\leq p\leq q,\ m-1\leq q\leq g-1\}.
\tag{5}
\]

For `(p,q) in I_m`, put `ell=q-p+1` and define the positive coefficient
`beta_m(p,q)` by

\[
 n^2\beta_m(p,q)=
 \begin{cases}
 4,&q=m-1,\ \ell=1,\\
 2\ell+1,&q=m-1,\ \ell\geq2,\\
 4,&q\geq m,\ \ell=1,\\
 1,&q\geq m,\ \ell=2,\\
 2,&q\geq m,\ \ell\geq3.
 \end{cases}
\tag{6}
\]

Finally set

\[
 \alpha_m=w_{g-1}=\left({m-1\over m}\right)^2.
\]

### Theorem 3 (closed shell decomposition)

The exact shell identity is

\[
 \boxed{
 Y_m=U_m-\alpha_m\log D_{1,g}
 -\sum_{(p,q)\in\mathcal I_m}\beta_m(p,q)\log D_{p,q}.}
\tag{7}
\]

Moreover,

\[
 \boxed{
 \sum_{(p,q)\in\mathcal I_m}\beta_m(p,q)=\alpha_m,}
\tag{8}
\]

and the total positive and absolute negative coefficient masses in (7) are
both `2 alpha_m`.

#### Proof

Expand every `C_(ij)` into its four logarithms.  A strict bulk interval
ending at `q=m,...,g-1` receives respectively the scaled coefficients
`-4,-1,-2` at lengths `1,2,>=3`.  At the lower boundary `q=m-1`, it receives
`-4` at length one and `-(2ell+1)` thereafter.  A left prefix has coefficient
`w_(m-1)` at `q=m-1` and `w_q-w_(q-1)` thereafter.  A terminal suffix has
coefficient `w_2` at length two and `w_ell-w_(ell-1)` thereafter.  The full
span has coefficient `-w_(g-1)`.  These are exactly (4)--(7).

The left-prefix coefficients telescope to `alpha_m`, as do the terminal-
suffix coefficients.  The complete coefficient sum is zero by scale
invariance, so the non-full negative mass is `alpha_m`; this proves (8) and
the sign-mass assertion.  Direct summation of (6) gives the same checksum.
`square`

## 5. One global product floor for all dyadic shells

For dyadic `m`, the right endpoints occurring in `I_m` lie in

\[
 [m-1,2m-2].
\]

These integer intervals are pairwise disjoint over distinct dyadic epochs.
Consequently all mark pairs `(p-1,q)` represented by the union of the
`I_m` are distinct.  The Golomb property then makes all corresponding
`D_(p,q)` globally distinct.

### Corollary 4 (hereditary Abel-bulk floor)

For every finite dyadic epoch set `E`, collect all coefficients
`beta_m(p,q)`, `(p,q) in I_m`, and sort them decreasingly as
`beta_1^down>=...>=beta_M^down`.  Then

\[
 \boxed{
 \sum_{m\in E}\sum_{(p,q)\in\mathcal I_m}
 \beta_m(p,q)\log D_{p,q}
 \geq
 \sum_{r=1}^{M}\beta_r^\downarrow\log r.}
\tag{9}
\]

Combining (7) and (9) gives a single, globally coupled upper bound for
`sum_(m in E)Y_m`.  This is stronger than applying a separate factorial
floor after forgetting cross-epoch distinctness.

The important limitation is equally precise: (9) knows only that the new
differences avoid all old values.  It does not know the additive interval
relations among them, nor which holes remain compatible with infinite
critical survival.

## 6. Exact coefficient multiset and the remaining logarithmic loss

The negative bulk at one shell contains

\[
 M_m={m(3m-5)\over2}
\tag{10}
\]

intervals.  After multiplication by `4m^2=n^2`, its decreasing coefficient
multiset consists of

- one ramp `2ell+1`, `ell=2,...,m-2`;
- `m` copies of `4`;
- `(m-1)(3m-8)/2` copies of `2`;
- `m-1` copies of `1`.

Put

\[
 R_m={3m^2-7m+2\over2}.
\]

The one-shell rearrangement floor therefore has the exact closed form

\[
\boxed{
\begin{aligned}
 \mathcal L_m={1\over4m^2}\Bigg[&
 \sum_{r=1}^{m-3}(2m-1-2r)\log r
 +4\log{(2m-3)!\over(m-3)!}\\
 &+2\log{R_m!\over(2m-3)!}
 +\log{M_m!\over R_m!}\Bigg].
\end{aligned}}
\tag{11}
\]

Stirling's formula and the Riemann sum for the first term give

\[
 \boxed{\mathcal L_m={7\over4}\log m+O(1).}
\tag{12}
\]

Indeed, the ramp contributes `(1/4)log m+O(1)`, the weight-two block
contributes `(3/2)log m+O(1)`, and the weight-four and weight-one blocks
together contribute `o(log m)`.

Every positive boundary difference is at most the full span `D_(1,g)`, so
`U_m<=2alpha_m log D_(1,g)`.  Equations (7), (9) for one epoch, and (11)
therefore give

\[
 \boxed{Y_m\leq\alpha_m\log D_{1,g}-\mathcal L_m.}
\tag{13}
\]

Under the hypothetical critical cap

\[
 D_{1,g}<N_{2m}\leq C(2m)^2\log(4m),
\]

this direct relaxation yields only

\[
 Y_m\leq {1\over4}\log m+\log\log m+O_C(1).
\tag{14}
\]

Thus the shellwise log-product upgrade is structurally aligned with the
objective but quantitatively insufficient.  Equation (14) alone does not
decide whether the stronger global floor (9) could gain across epochs.  That
remaining point is proved in the companion laminar-triangle analysis: for
every finite dyadic `E`, the globally sorted floor equals
`(7/4) sum_(m in E) log m+O(|E|)`.  Consequently the global certificate also
retains the leading quarter deficit.  A future dual must add an exclusion
theorem saying that the high-weight new terminal differences cannot repeatedly
occupy the smallest surviving numerical holes on a branch with
`surv_C=infinity`.

## 7. Finite executable audit

The exact implementation is:

- `endpoint_variance/wave10_log_product_packing.py`;
- `endpoint_variance/test_wave10_log_product_packing.py`.

It independently checks the four-origin and closed shell coefficients, all
sign masses, the coefficient-multiset formula, direct cross-ratio versus Abel
evaluation, HLP, and the weighted inequality after clearing rational
denominators.  The initial focused run gave:

```text
13 passed
Ruff check: all checks passed
Ruff format: clean
```

For calibration only, with `C=1` in the relaxed critical cap:

| `m` | `L_m` | `alpha_m log((2m)^2 log(4m))-L_m` |
|---:|---:|---:|
| 8 | 2.1235524386 | 3.0735884892 |
| 16 | 3.5340987836 | 3.8106732074 |
| 32 | 4.9220201909 | 4.3662356907 |
| 64 | 6.2598533590 | 4.8031422299 |
| 128 | 7.5535912049 | 5.1663723153 |
| 256 | 8.8159862080 | 5.4843557491 |
| 512 | 10.0581536665 | 5.7741457182 |

These decimals audit the relaxation only.  They are neither counterexamples
to P15 nor evidence for an infinite critical ruler.

## 8. Disposition

W10-HLP and the hereditary weighted bulk floor (9) should be retained as
legal constraints in the Wave 10 laminar LP.  They close the gap between the
linear W9-RLP language and the logarithmic Abel objective.  Together with the
companion Theorem 5, they prove that a dual using only global distinctness,
numerical rank, and the current shell coefficient multiset cannot close P15
without an additional survival-conditioned hole-exclusion or interval-
consistency inequality.

The exact next theorem remains:

> On one fixed infinite eventually critical Golomb branch, prove that the
> long-rank, two-large-endpoint core has sublogarithmic cumulative mass by
> controlling how each new translated prefix avoids the complete old
> difference spectrum across unboundedly many epochs.

P15, Question 1, and Question 2 remain open.
