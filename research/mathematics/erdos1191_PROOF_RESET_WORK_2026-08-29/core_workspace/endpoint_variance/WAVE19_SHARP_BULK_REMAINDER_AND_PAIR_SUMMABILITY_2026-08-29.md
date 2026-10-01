# Wave 19: sharp actual-bulk remainder and summable pairing slack

Date: 2026-08-29 (Asia/Tokyo)  
Status: **exact rank-free reduction; standalone P26/P27 closed by inner-birth
saturation; P28 and Erdős #1191 remain open**

## 1. Claim boundary

This note sharpens the certified-rank remainder without adding a new
assumption.  It retains the actual Gothic bulk instead of replacing it by a
sorted-rank floor.  The resulting remainder is determined by the first `2n`
marks, is invariant under integer dilation, and differs from the P25
remainder by a universally dyadically summable pairing slack.  The companion
channel note subsequently proves that this sharp remainder is nonnegative.
The inner-birth saturation note then shows that P26/P27 cannot be smaller
standalone remainder lemmas on an extant eventual-`C` branch.

Nothing here proves P28, constructs an eventually critical infinite Golomb
ruler, answers Question 1 or 2, establishes publication novelty, or supports
a prize claim.

## 2. Direct sharp remainder

Fix `n>=4` and `h=5/2`.  Retain the Wave 19 endpoint/cross-ratio split

\[
 J_n^{(5/2)}\le E_n^{(5/2)}+S_n,
 \qquad S_n\le {1\over2}Y_n,
\tag{2.1}
\]

where `E_n^(5/2)` is the endpoint part of the descendant functional, not
the promotion excess `Theta_n^(exc,5/2)`.  The sharp endpoint estimate is

\[
 (\mathfrak P_n-\mathfrak F_n)+E_n^{(5/2)}
 \le-{1\over4}\mathcal D_n^{\rm pre}+\varepsilon_n.
\tag{2.2}
\]

Define

\[
 \boxed{
 \mathcal R_n^{\rm sharp}:=
 \mathfrak U_n-\mathfrak B_n-J_n^{(5/2)}
 -{1\over4}\mathcal D_n^{\rm pre}
 -\mathfrak e_n+\varepsilon_n.}
\tag{2.3}
\]

From (2.1),

\[
 -E_n^{(5/2)}\le {1\over2}Y_n-J_n^{(5/2)}.
\]

Apply this to (2.2), then add
`mathfrak U_n-mathfrak B_n-mathfrak e_n`.  The exact Wave 13 spectrum gives

\[
 \boxed{Z_n\le {1\over2}Y_n+\mathcal R_n^{\rm sharp}.}
\tag{2.4}
\]

This proof uses no promotion cap, cap reindexing, local rank floor, or
nonnegative `Q` remainder.  In particular, there is no ownership overlap
with the Wave 17--18 rank ledger.

The exact endpoint identity

\[
 \mathfrak P_n-\mathfrak F_n
 =-\mathcal D_n^{\rm pre}+\varepsilon_n
\tag{2.5}
\]

also gives

\[
 \boxed{
 \mathcal R_n^{\rm sharp}
 =Z_n+{3\over4}\mathcal D_n^{\rm pre}-J_n^{(5/2)}.}
\tag{2.6}
\]

Every term in (2.6) is a scale-free ratio or cross-ratio expression.
Therefore `Rsharp` is exactly invariant when the entire ruler is multiplied
by a positive integer.

## 3. The pairing slack is dyadically summable

Write

\[
 a=n-1,\qquad
 b={3(n-1)(n-2)\over2},\qquad
 c={ (n-1)(3n-4)\over2}=a+b.
\tag{3.1}
\]

The Gothic interior coefficient multiset has

- `a` high coefficients equal to `1/n^2`;
- `c-2a` middle coefficients equal to `1/(2n^2)`; and
- `a` low coefficients equal to `1/(4n^2)`.

Sort the atom values and carry their actual coefficients as in the P25 note.
The pairing slack is

\[
 \mathcal P_n^{\rm pair}
 =\sum_{j=1}^{c}\gamma_{n,j}\log j-F_n^{\rm loc,int}\ge0.
\tag{3.2}
\]

The rearrangement inequality puts the high coefficients on the first `a`
ranks and the low coefficients on the last `a` ranks in the minimum.  Its
maximum over all permutations reverses those two blocks; the middle block is
unchanged.  Hence

\[
 \boxed{
 0\le\mathcal P_n^{\rm pair}
 \le {3\over4n^2}\log{c\choose a}.}
\tag{3.3}
\]

The upper bound is sharp for the abstract coefficient-permutation problem;
no claim is made that every extremal permutation is realized by a Golomb
ruler.  Using `binom(c,a)<=(ec/a)^a` and `c/a=(3n-4)/2` gives

\[
 \mathcal P_n^{\rm pair}
 \le {3(n-1)\over4n^2}\log{e(3n-4)\over2}
 \le {3\over4n}\log{3en\over2}.
\tag{3.4}
\]

Consequently, for every `k_0>=2`,

\[
 \boxed{
 \sum_{k=k_0}^{\infty}\mathcal P_{2^k}^{\rm pair}
 \le {3\over4}2^{1-k_0}
 \left(\log{3e\over2}+(k_0+1)\log2\right)<\infty.}
\tag{3.5}
\]

In particular, the tail over `L<=k<=2L` is `O(L2^{-L})=o(1)`, uniformly
over all finite Golomb prefixes for which the terms are defined.

## 4. P25 and P26 differ by only a bounded dyadic amount

The P25 ownership identity is

\[
 \mathfrak B_n=F_n^{\rm loc,int}
 +\mathcal S_n^{\rm rank}+\mathcal P_n^{\rm pair}.
\]

Comparing its certified remainder with (2.3) gives exactly

\[
 \boxed{
 \mathcal R_n^{\rm cert}
 =\mathcal R_n^{\rm sharp}+\mathcal P_n^{\rm pair}.}
\tag{4.1}
\]

Since the pairing slack is nonnegative,

\[
 0\le
 (\mathcal R_n^{\rm cert})_+
 -(\mathcal R_n^{\rm sharp})_+
 \le\mathcal P_n^{\rm pair}.
\tag{4.2}
\]

Thus the P25 and P26 positive-part Fejér sums differ by a uniformly bounded
quantity, and their finite-window sums differ by `o(1)`.  The same is true
for their signed Fejér sums.

## 5. P26: the sharp intermediate sufficient theorem

The Wave 16 tapered renewal identity, (2.4), and the favorable cut signs give

\[
 {1\over2}\sum_{k=k_0}^J\omega_{k,J}Y_{2^k}
 \le O_{\mathbf a,k_0}(1)
 +\sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm sharp}.
\tag{5.1}
\]

The left side is at least

\[
 {1\over3072C\log2}\log J+O_{C,k_0}(1)
\]

on a fixed eventual-`C` branch.  Therefore the exact weakest directly
sufficient signed condition is

\[
 \boxed{
 \limsup_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm sharp}
  \over\log J}
 <{1\over3072C\log2}.}
\tag{P26-sharp}
\]

The recommended clean target is

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}
 (\mathcal R_{2^k}^{\rm sharp})_+
 =o_{C,\mathbf a}(\log J).}
\tag{P26}
\]

A stronger uniform finite-window target is

\[
 \sum_{k=L}^{2L}(\mathcal R_{2^k}^{\rm sharp})_+=o_C(1),
\tag{P26-block}
\]

with the same finite-prefix and cap quantifiers as P25-block.  By (3.5),
P25 and P26 are equivalent at all three stated asymptotic levels.

The companion channel decomposition proves `Rsharp>=0`, so P26 became the
nonnegative P27 candidate.  The later inner-birth theorem proves that its
Fejér lower constant is at least `1/(1536C log2)` on any extant critical
branch, twice the allowed sharp threshold.  Thus P26/P27 are closed as
standalone intermediate targets, not proved.  The remaining P28 design issue
is relocation or absorption of that untouched inner sector.

## 6. Nonclaims and proof-design gates

- The direct reduction (2.4) is a sufficient-theorem reduction, not a bound
  on the Fejér mass of `Rsharp`.
- Formula (2.6) alone does not display a sign, but
  `WAVE19_NONNEGATIVE_SHARP_REMAINDER_DECOMPOSITION_2026-08-29.md` proves
  `Rsharp>=0` by an exact channel decomposition.
- The summability of `Pair` removes a bookkeeping slack; it does not prove
  P25/P26/P27.
- Finite rulers can test (2.3)--(4.2), but cannot certify the asymptotic
  compatible-branch statement.
- Any solution or prize claim still requires a successful P28 repair (or a
  different complete proof), formula-level independent review, and a
  current primary-source novelty audit.
