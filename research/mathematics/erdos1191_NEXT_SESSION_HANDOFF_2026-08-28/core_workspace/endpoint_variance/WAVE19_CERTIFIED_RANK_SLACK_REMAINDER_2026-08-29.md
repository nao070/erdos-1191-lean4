# Wave 19: certified rank slack, dilation-invariant remainder, and local no-go

Date: 2026-08-29 (Asia/Tokyo)  
Status: **new exact signed reduction and local obstruction; P28 and Erdős
#1191 remain open**

## 1. Claim boundary

This note retains a part of the Wave 18 local remainder that Wave 19's first
P24 reduction discarded.  It splits the actual Gothic interior slack into a
rank slack that can pay the promotion excess and an explicitly unspent
pairing slack.  The resulting signed remainder is finite-prefix computable
and exactly invariant under integer dilation.  It is therefore a cleaner
target than the bare current-scale `widehat G` expression.  The companion
sharp-bulk note subsequently removes the dyadically summable pairing term and
supersedes P25 by the equivalent rank-free P26 target.

The note also gives a family of different finite Golomb prefixes on which
bare `widehat G` grows like `log log n`.  This refutes local-only proofs of
the bare P24 target, not P24 on one compatible infinite branch.

Nothing below proves P24/P25/P26, constructs an eventual-critical infinite
branch, answers Question 1 or 2, establishes novelty, or supports a prize
claim.

## 2. Exact rank-slack split

Fix `n>=4` and `h=5/2`.  Let

\[
 \mathcal A_n=\{(p,q):n\le q\le2n-2,\ 2\le p\le q\}.
\]

For `(p,q)` in this set, let `beta_(n,p,q)` be the exact Gothic interior
coefficient.  The number of atoms is

\[
 c_n={ (n-1)(3n-4)\over2}.
\tag{2.1}
\]

Because the ruler is Golomb, their values `D_(p,q)` are distinct positive
integers.  Sort them as

\[
 x_{n,1}<\cdots<x_{n,c_n}.
\]

If `x_(n,j)=D_(p_j,q_j)`, carry its actual coefficient

\[
 \gamma_{n,j}:=\beta_{n,p_j,q_j}.
\]

Define

\[
 \mathcal S_n^{\rm rank}
 :=\sum_{j=1}^{c_n}\gamma_{n,j}\log{x_{n,j}\over j},
\tag{2.2}
\]

and

\[
 \mathcal P_n^{\rm pair}
 :=\sum_{j=1}^{c_n}\gamma_{n,j}\log j
   -F_n^{\rm loc,int}.
\tag{2.3}
\]

Since `x_(n,j)>=j`, the rank slack is nonnegative.  The pairing slack is
nonnegative by the rearrangement inequality used to define the Wave 17
sorted-rank floor.  Moreover,

\[
 \boxed{
 H_n^{\rm loc}=\mathfrak B_n-F_n^{\rm loc,int}
 =\mathcal S_n^{\rm rank}+\mathcal P_n^{\rm pair}.}
\tag{2.4}
\]

This is an exact ownership decomposition, not two lower bounds added to the
same atom set.

## 3. The rank slack alone pays the Wave 18 spent row

Let

\[
 \mathcal M_n=\{(p,q):2\le p\le n,\ n\le q\le2n-2\}.
\]

Immediately before Wave 18 applies its local-slack majorant, its proof gives

\[
 \Theta_n^{\rm exc,5/2}
 \le\sum_{(p,q)\in\mathcal M_n}
 \alpha_{n,p}\beta_{n,p,q}
 \log_+{D_{p,q}\over c_n}+J_n^{(5/2)}.
\tag{3.1}
\]

If `D_(p,q)=x_(n,j)`, then `j<=c_n`, `x_(n,j)>=j`, and
`0<alpha_(n,p)<1`.  Hence

\[
 \alpha_{n,p}\beta_{n,p,q}\log_+{D_{p,q}\over c_n}
 \le\gamma_{n,j}\log{x_{n,j}\over j}.
\tag{3.2}
\]

Summation proves the sharper local theorem

\[
 \boxed{
 \Theta_n^{\rm exc,5/2}
 \le\mathcal S_n^{\rm rank}+J_n^{(5/2)}.}
\tag{3.3}
\]

Thus

\[
 Q_n^{\rm cert}:=
 \mathcal S_n^{\rm rank}+J_n^{(5/2)}
 -\Theta_n^{\rm exc,5/2}\ge0,
\tag{3.4}
\]

and the old Wave 18 remainder splits exactly as

\[
 Q_n=Q_n^{\rm cert}+\mathcal P_n^{\rm pair}.
\tag{3.5}
\]

The rank slack is spent once in `Qcert`; the pairing slack remains visible.

## 4. Dilation-invariant certified remainder

Use the Wave 19 notation

\[
 C_n=\Theta_n^{[5/2]},\qquad
 E_n=\Theta_n^{\rm exc,5/2},\qquad
 D_n=F_n^{\rm loc,int}-K_n^{\rm int}.
\]

Define the finite-prefix remainder

\[
 \boxed{
 \begin{aligned}
 \mathcal R_n^{\rm cert}:={}&
 \mathfrak U_n-F_n^{\rm loc,int}
 -\mathcal S_n^{\rm rank}-J_n^{(5/2)}\\
 &-{1\over4}\mathcal D_n^{\rm pre}
 -\mathfrak e_n+\varepsilon_n.
 \end{aligned}}
\tag{4.1}
\]

This depends only on the first `2n` marks; no rank at infinity occurs.

In the Wave 19 inequality, the previous-scale cap cancels exactly against
the retained cap surplus:

\[
 \mathcal G_n-U_n^{\rm cap}
 =\mathfrak U_n-F_n^{\rm loc,int}-E_n
  -{1\over4}\mathcal D_n^{\rm pre}.
\tag{4.2}
\]

Using `Q_n>=Q_n^cert` and (3.4), with every other sign unchanged, gives

\[
 \boxed{Z_n\le {1\over2}Y_n+\mathcal R_n^{\rm cert}.}
\tag{4.3}
\]

There is no current/previous cap reindexing error in (4.3).  With the Wave 16
Fejér weights and a fixed onset `k_0`, the cut-renewal signs give

\[
 {1\over2}\sum_{k=k_0}^J\omega_{k,J}Y_{2^k}
 \le O_{\mathbf a,k_0}(1)
 +\sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm cert}.
\tag{4.4}
\]

The `O(1)` is only the fixed initial cut and finite onset adjustment.

The exact relation to the earlier spectrum is

\[
 \boxed{
 \mathcal R_n^{\rm cert}
 =Z_n+{3\over4}\mathcal D_n^{\rm pre}
 -J_n^{(5/2)}+\mathcal P_n^{\rm pair}.}
\tag{4.5}
\]

Indeed, use (2.4), the Wave 13 exact spectrum, and
`mathfrak P_n-mathfrak F_n=-Dpre_n+epsilon_n`.  Equation (4.5) is also a
complete sign audit: the only returned positive slack is the unspent pairing
term.

Now multiply the whole infinite ruler by an integer `L`.  The changes are

```text
mathfrak U_n:        +Ucoef_n log L,
Srank_n:             +Bcoef_n log L,
mathfrak e_n:        +(1/(4n^2))log L,
epsilon_n:           +((4n-3)/(16n^2))log L.
```

The other terms in (4.1) are invariant, and the coefficient checksum is

\[
 U_n^{\rm coef}-B_n^{\rm coef}-{1\over4n^2}
 +{4n-3\over16n^2}=0.
\tag{4.6}
\]

Therefore

\[
 \boxed{
 \mathcal R_n^{\rm cert}(L\mathbf a)
 =\mathcal R_n^{\rm cert}(\mathbf a).}
\tag{4.7}
\]

## 5. P25: the certified intermediate signed theorem

Wave 19 already proves

\[
 {1\over2}\sum_{k=k_0}^J\omega_{k,J}Y_{2^k}
 \ge {1\over3072C\log2}\log J+O_{C,k_0}(1).
\]

Consequently the exact weakest directly sufficient certified-remainder
condition is

\[
 \boxed{
 \limsup_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm cert}
  \over\log J}
 <{1\over3072C\log2}.}
\tag{P25-sharp}
\]

The certified clean target is

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}
 (\mathcal R_{2^k}^{\rm cert})_+
 =o_{C,\mathbf a}(\log J).}
\tag{P25}
\]

For a genuinely uniform finite statement, the stronger block form is

\[
 \sum_{k=L}^{2L}(\mathcal R_{2^k}^{\rm cert})_+=o_C(1),
\tag{P25-block}
\]

uniformly over finite Golomb rulers through index `2^(2L+1)-1` satisfying
the fixed `Cj^2 log(2j)` cap throughout the required index window.
Dyadically partitioning the exponent variable and applying Cesàro summation
turns this block form into (P25).

P25 and P25-block were valid sufficient candidates.  The companion P26
reduction is equivalent up to a bounded dyadic pairing contribution; the
later inner-birth saturation theorem closes both as standalone intermediate
upper targets.

## 6. Bare current-scale P24 has a local dilation obstruction

For every `n>=4`, Bertrand's theorem supplies a prime

\[
 2n-1<P<4n-2.
\]

Set

\[
 b_i=2Pi+(i^2\bmod P),\qquad0\le i\le2n-2,
\]

let `H=b_(2n-2)`, append `X=2H+1`, and scale by

\[
 s_n=\lfloor\log(2n)\rfloor.
\]

Thus `a_i=s_n b_i` for `i<=2n-2` and `a_(2n-1)=s_nX`.  The standard
residue argument proves the `b_i` form a Golomb ruler, and `X>2H` separates
every appended difference from every old difference.  A superincreasing
infinite completion exists, but it is not claimed to satisfy a critical cap.

The elementary bounds are

\[
 H+1>2n^2,\qquad X<32n^2,\qquad {X\over b_q}<4
 \quad(n\le q\le2n-2).
\tag{6.1}
\]

Consequently the displayed prefix obeys the fixed local cap

\[
 a_q<32q^2\log(2q),\qquad n\le q\le2n-1.
\tag{6.2}
\]

For every infinite completion, elementary integer rank bounds give

\[
 \Theta_n^{\rm tot}\le R_n\log(64s_n).
\]

Also

\[
 \mathfrak U_n\ge U_n^{\rm coef}\log(s_n(H+1)),
\]

\[
 K_n^{\rm int}\le B_n^{\rm coef}\log(2n^2),
 \qquad
 \mathcal D_n^{\rm pre}\le P_n^{\rm coef}\log4.
\]

Using

\[
 U_n^{\rm coef}-R_n
 ={6n^2-12n+9\over16n^2}\ge{7\over32},
\]

`Bcoef-Ucoef=(4n-7)/(16n^2)`, and `log(2n^2)<n`, one obtains

\[
 \boxed{
 \widehat{\mathcal G}_n
 \ge {7\over32}\log s_n
 -\left({1\over4}+{3\over8}\log64+{3\over16}\log4\right).}
\tag{6.3}
\]

Thus bare `widehat G_n` can be `Omega(log log n)` even after allowing the
largest promotion compatible with elementary rank bounds.  Taking different
constructions at `n=2^k`, all with the same local constant `32`, gives an
independent-scale Fejér sum `Omega(J log J)`.

These prefixes differ with `k`, and their cap window begins at their chosen
scale.  They are not one compatible branch and do not refute P24.  They prove
that a pointwise or block bound for bare `widehat G` cannot follow from
same-scale Golomb uniqueness, integer rank bounds, and a local cap alone.
P25 removes this precise dilation defect.

## 7. Ownership and nonclaims

- `Srank` is spent exactly once in `Qcert`; `Pair` is the explicit unused
  remainder.
- The previous-source cap cancels against `Ucap`; no `15/16` error is needed
  in the P25 reduction.
- `mathfrak F_n` is not reintroduced through the contracted terminal
  potential.
- The local family in Section 6 uses Bertrand's theorem and a separate ruler
  at each scale.  It is a no-go, not a critical construction.
- A finite certificate can audit the ranks, coefficient masses, dilation
  checksum, and fixed fixtures.  It cannot prove the asymptotic P25/P26
  theorem.

The current highest-value P28 question is how to relocate or absorb the
untouched inner-new-birth sector while retaining the negative renewal cuts
and exact carrier ownership.  See
`WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`.
