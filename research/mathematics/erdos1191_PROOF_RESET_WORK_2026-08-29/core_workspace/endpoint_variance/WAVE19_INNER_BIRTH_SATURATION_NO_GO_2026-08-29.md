# Wave 19: row-exact absorption and inner-birth saturation no-go

Date: 2026-08-29 (Asia/Tokyo)  
Status: **P26/P27 closed as standalone remainder targets; Erdős #1191 remains
open**

## 1. Claim boundary

The sharp remainder is nonnegative, but it cannot have the `o(log J)` Fejér
mass proposed in P26/P27 on any hypothetical eventual-`C` branch.  An inner
new-birth sector untouched by the cross-ratio absorption already has twice
the maximum coefficient allowed by the sharp sufficient threshold.

This is a method no-go, not a counterexample to Erdős #1191.  If no
eventual-`C` infinite branch exists, every conditional branch statement is
vacuous.  Nothing below constructs such a branch, answers Question 1 or 2,
establishes publication novelty, or supports a prize claim.

## 2. Row-exact endpoint extraction

Fix `n>=4` and `h=5/2`.  For `2<=p<=n` and `n<=q<=2n-2`, put

\[
 u_{n,q}:=\log{A\over a_q},\qquad
 v_{n,p,q}:=\log X_{n,p,q},\qquad
 t_{n,p}:={5\over2}-\log{c_n\over L_{n,p}}.
\tag{2.1}
\]

All three quantities are nonnegative, and `t_(n,p)>5/2-log3>0`.  The exact
rectangle identity turns the Wave 18 residual into

\[
 J_n^{(5/2)}
 =\sum_{p,q}\alpha_{n,p}\beta_{n,p,q}
   [u_{n,q}+v_{n,p,q}-t_{n,p}]_+.
\tag{2.2}
\]

Define the row-exact endpoint part

\[
 E_n^{\rm row}:=
 \sum_{p,q}\alpha_{n,p}\beta_{n,p,q}
 [u_{n,q}-t_{n,p}]_+
\tag{2.3}
\]

and the actually absorbed cross increment

\[
 \Delta_n^{\rm abs}:=J_n^{(5/2)}-E_n^{\rm row}.
\tag{2.4}
\]

For `u,v,t>=0`,

\[
 0\le[u+v-t]_+-[u-t]_+\le v.
\]

Therefore, coefficient by coefficient,

\[
 \boxed{0\le\Delta_n^{\rm abs}\le S_n.}
\tag{2.5}
\]

Since `t_(n,p)>5/2-log3`, the row endpoint is at most the Wave 19 endpoint
part, so

\[
 E_n^{\rm row}\le E_n^{\rm end,5/2}
 \le {3\over4}\mathcal D_n^{\rm pre}.
\tag{2.6}
\]

## 3. The saturated profile remainder

Define

\[
 \boxed{
 \mathcal R_n^{\rm prof}:=
 Z_n+E_n^{\rm row}-J_n^{(5/2)}
 =Z_n-\Delta_n^{\rm abs}.}
\tag{3.1}
\]

The P26 remainder splits exactly as

\[
 \boxed{
 \mathcal R_n^{\rm sharp}
 =\mathcal R_n^{\rm prof}
 +\left({3\over4}\mathcal D_n^{\rm pre}-E_n^{\rm row}\right).}
\tag{3.2}
\]

Let `Zfin=Zob+Znb` and `Zfut=Zof+Zmf`.  Wave 19's exact coefficient audit
strengthens `S<=Y/2` to `S<=Zfin`.  Combining this with (2.5) gives

\[
 \boxed{
 \mathcal R_n^{\rm prof}
 =(Z_n^{\rm fin}-S_n)+Z_n^{\rm fut}
 +(S_n-\Delta_n^{\rm abs})\ge0.}
\tag{3.3}
\]

Also

\[
 Z_n=\mathcal R_n^{\rm prof}+\Delta_n^{\rm abs}
 \le\mathcal R_n^{\rm prof}+S_n
 \le\mathcal R_n^{\rm prof}+{1\over2}Y_n.
\tag{3.4}
\]

Thus `Rprof` is the smallest remainder produced by this row-exact absorption;
removing endpoint or pairing slack cannot make it smaller.

## 4. Untouched inner-new-birth sector

Define

\[
 \mathcal W_n:=
 \sum_{j=n+2}^{2n-1}\sum_{i=n}^{j-2}
 { (j-i)^2\over4n^2}C_{ij}.
\tag{4.1}
\]

The cross term `S_n` is supported only on `i<=n-1`.  Hence every atom in
`W_n` remains with its full `Znb` coefficient inside `Zfin-S`, and

\[
 \boxed{
 \mathcal R_n^{\rm sharp}\ge\mathcal R_n^{\rm prof}
 \ge Z_n^{\rm fin}-S_n\ge\mathcal W_n.}
\tag{4.2}
\]

This is a support obstruction, not a loss in a numerical constant.

## 5. Exact layered floor for the inner sector

Let

\[
 G_n'=\{n,n+1,\ldots,2n-1\},\qquad
 H_n'=\sum_{r=n}^{2n-1}h_r=A-a_{n-1}.
\tag{5.1}
\]

The set has `n` distinct positive integer gaps.  Every nonadjacent unordered
pair in `G_n'` occurs exactly once in (4.1).  Repeating the Wave 13 product
floor and layered argument on this smaller gap set gives

\[
 \mathcal W_n\ge {E_n'\over8n^2H_n'},
\tag{5.2}
\]

where

\[
 \begin{aligned}
 E_n'
 &=\sum_{r=2}^{n/2}(2r-1)
   { (n+1-2r)(n+2-2r)\over2}\\
 &={n(n-2)(n^2+4n-14)\over48}.
 \end{aligned}
\tag{5.3}
\]

For dyadic `n>=16`,

\[
 E_n'-{n^4\over48}
 ={n(n^2-11n+14)\over24}\ge0.
\tag{5.4}
\]

Therefore

\[
 \boxed{
 \mathcal W_n\ge {n^2\over384H_n'}
 \ge {n^2\over384A}.}
\tag{5.5}
\]

Only distinctness of adjacent positive integer gaps is used in the layered
lower bound; Golomb uniqueness supplies that distinctness.

## 6. Saturation on a hypothetical eventual-critical branch

Assume one fixed infinite normalized integer Golomb ruler satisfies

\[
 a_m\le Cm^2\log(2m)
\]

for all sufficiently large `m`.  At `m=2n-1`,

\[
 A<4Cn^2\log(4n).
\]

Equations (4.2) and (5.5) imply, for all sufficiently large dyadic `n`,

\[
 \boxed{
 \mathcal R_n^{\rm sharp}\ge\mathcal R_n^{\rm prof}
 \ge\mathcal W_n
 >{1\over1536C\log(4n)}.}
\tag{6.1}
\]

For `n=2^k` and the Wave 16 Fejér weights,

\[
 \sum_{k=k_0}^J{\omega_{k,J}\over k+2}
 =\log J+O_{k_0}(1).
\]

Consequently

\[
 \boxed{
 \liminf_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm sharp}
  \over\log J}
 \ge {1\over1536C\log2}.}
\tag{6.2}
\]

This is twice the exact sufficient threshold
`1/(3072C log2)` obtained from half-absorption.  Thus, on any extant
eventual-`C` branch:

- the P26/P27 `o(log J)` remainder bound cannot hold;
- even the sharp strict-threshold version cannot hold; and
- the uniform exponent-block `o_C(1)` target cannot hold, because its
  conditional lower limit is at least `1/(1536C)`.

These statements do not exhibit a branch.  They show that P26/P27 cannot be
treated as easier standalone packing lemmas on the contradiction branch.

## 7. P28: the next valid proof-design obligation

The half-absorption route is saturated by atoms with `i>=n`, outside every
terminal-to-descendant rectangle used by `S_n`.  A viable next lemma must do
at least one of the following while preserving one fixed branch and exact
ownership:

1. retain the negative intermediate/terminal renewal-cut terms and relocate
   `W_n` against them across dyadic scales;
2. enlarge the descendant allocation to cover inner births `i>=n` without
   reusing the Gothic bulk or the full-span deficit; or
3. derive a new signed identity in which the inner sector has a genuinely
   negative carrier of sufficient coefficient.

Call this open design obligation **P28 (inner-birth relocation/absorption)**.
P28 is not yet a theorem statement with proved sufficient constants; it is
the smallest currently valid design target after the P26/P27 saturation
no-go.

## 8. Nonclaims

- `Rsharp>=0` and the lower floor do not prove that an eventual-`C` branch
  exists.
- The conditional failure of P26/P27 on an extant branch does not refute
  Question 1; it closes that proposed intermediate route.
- The Wave 13 floor is reapplied to a strict inner gap set with its constants
  recomputed; the old `m+1`-gap polynomial is not reused unchanged.
- P19/P24/P25/P26/P27/P28, both Erdős questions, publication novelty, and
  every prize claim remain unresolved.
