# Wave 19: nonnegative sharp-remainder channels and compatibility no-go

Date: 2026-08-29 (Asia/Tokyo)  
Status: **exact four-channel decomposition with a five-channel refinement;
standalone P27 closed by the companion saturation no-go; Erdős #1191 remains
open**

## 1. Claim boundary

The P26 remainder is not merely dilation invariant: it is pointwise
nonnegative.  This note proves that fact by splitting the remainder into four
explicit nonnegative channels; an auxiliary descendant height refines the
last channel into two.  It also constructs a different locally capped finite
Golomb prefix at every scale on which one channel is bounded below by an
absolute constant.

The latter prefixes are not one compatible infinite branch.  The companion
inner-birth memo proves a stronger compatible-branch lower floor, so P27
cannot be used as a standalone small-remainder lemma.  Nothing here
constructs a critical infinite ruler, answers Question 1 or 2, establishes
publication novelty, or supports a prize claim.

## 2. Finite and future renewal sectors

Retain the four nonnegative Wave 12 sectors and put

\[
 Z_n^{\rm fin}:=Z_n^{\rm ob}+Z_n^{\rm nb},\qquad
 Z_n^{\rm fut}:=Z_n^{\rm of}+Z_n^{\rm mf}.
\tag{2.1}
\]

Thus

\[
 Z_n=Z_n^{\rm fin}+Z_n^{\rm fut}.
\tag{2.2}
\]

For a finite-sector atom `C_(i,j)`, write

\[
 x=n-i,\qquad y=j-n.
\]

The cross-ratio term `S_n` is supported on `x>=1`, `y>=1`.  Its coefficient
is

\[
 K_{n,i,j}
 =\sum_{p=i+1}^n\alpha_{n,p}
   \sum_{q=n}^{j-1}\beta_{n,p,q}.
\tag{2.3}
\]

## 3. The cross rectangle fits inside the finite renewal sectors

### Theorem 3.1

For every `n>=4`, coefficientwise,

\[
 \boxed{S_n\le Z_n^{\rm fin}.}
\tag{3.1}
\]

### Proof

If `x>=2`, the relevant coefficient of `Zob` is

\[
 {y(2x+y)\over4n^2}.
\tag{3.2}
\]

For `x,y>=2`, the Wave 19 rectangle audit gives

\[
 K_{n,i,j}\le {xy\over2n^2}
 \le {y(2x+y)\over4n^2}.
\]

For `y=1` and `x>=3`, it gives

\[
 K_{n,i,n+1}\le {2x+1\over4n^2},
\]

which is exactly (3.2).  At the remaining `x=2,y=1` corner,

\[
 K_{n,n-2,n+1}
 ={alpha_{n,n-1}\over4n^2}+{alpha_{n,n}\over n^2}
 <{3\over4n^2}<{5\over4n^2}.
\]

If `x=1`, the relevant coefficient of `Znb` is

\[
 {(y+1)^2\over4n^2}.
\tag{3.3}
\]

For `y=1`, `K=alpha_(n,n)/n^2<1/(2n^2)`, which is below (3.3).  For
`y>=2`,

\[
 K_{n,n-1,n+y}<{2y+1\over8n^2}
 \le{(y+1)^2\over4n^2}.
\]

All `C_(i,j)` are nonnegative, proving (3.1).  `square`

## 4. Exact descendant-cap channel

Define the unthresholded endpoint term

\[
 E_n^0:=\sum_{q=n}^{2n-2}\lambda_{n,q}
          \log{A\over a_q}.
\tag{4.1}
\]

The rectangle identity gives exactly

\[
 E_n^0+S_n
 =\sum_{p=2}^n\alpha_{n,p}
   \sum_{q=n}^{2n-2}\beta_{n,p,q}
   \log{d_{n,p}\over D_{p,q}}.
\tag{4.2}
\]

Since `c_n/L_(n,p)<3<exp(5/2)`, put

\[
 \tau_{n,p}:={5\over2}-\log{c_n\over L_{n,p}}>0.
\]

The definition of `J_n^(5/2)` then gives the exact nonnegative descendant-cap
slack

\[
 \boxed{
 \begin{aligned}
 \mathcal C_n^{\rm desc}
 &: =E_n^0+S_n-J_n^{(5/2)}\\
 &=\sum_{p=2}^n\alpha_{n,p}
   \sum_{q=n}^{2n-2}\beta_{n,p,q}
   \min\!\left(\log{d_{n,p}\over D_{p,q}},\tau_{n,p}\right)\ge0.
 \end{aligned}}
\tag{4.3}
\]

The sharp endpoint coefficient theorem also gives

\[
 \boxed{E_n^0\le {3\over4}\mathcal D_n^{\rm pre}.}
\tag{4.4}
\]

## 5. Optional optimal finite-height refinement

Recall

\[
 c_n={ (n-1)(3n-4)\over2},\qquad
 L_{n,p}={2n-p+1\choose2}.
\]

Since `L_(n,p)>=L_(n,n)` for `2<=p<=n`, define

\[
 h_n^*:=\log{c_n\over L_{n,n}}
 =\log{(n-1)(3n-4)\over n(n+1)}.
\tag{5.1}
\]

For `n>=4`,

\[
 0<h_n^*<\log3<{5\over2}.
\tag{5.2}
\]

Let

\[
 J_n^*:=J_n^{(h_n^*)}
 =\sum_{p=2}^n\alpha_{n,p}
   \sum_{q=n}^{2n-2}\beta_{n,p,q}
   \left[\log{d_{n,p}L_{n,n}\over L_{n,p}D_{p,q}}\right]_+,
\tag{5.3}
\]

The rectangle identity gives

\[
 {d_{n,p}L_{n,n}\over L_{n,p}D_{p,q}}
 ={A\over a_q}X_{n,p,q}{L_{n,n}\over L_{n,p}}.
\]

Here the first two factors are at least one and the last is at most one.
Therefore, term by term,

\[
 \boxed{J_n^*\le E_n^0+S_n.}
\tag{5.4}
\]

Finally, (5.2) and monotonicity of `[u-h]_+` give

\[
 \boxed{J_n^*\ge J_n^{(5/2)}.}
\tag{5.5}
\]

## 6. Exact four-channel decomposition and five-channel refinement

The P26 identity and (2.2) give the primary four-channel decomposition

\[
 \boxed{
 \mathcal R_n^{\rm sharp}
 =\left({3\over4}\mathcal D_n^{\rm pre}-E_n^0\right)
 +(Z_n^{\rm fin}-S_n)+Z_n^{\rm fut}
 +\mathcal C_n^{\rm desc}.}
\tag{6.1}
\]

Every term is nonnegative by (3.1), (4.3), and (4.4).  The auxiliary height
splits `Cdesc` further as

\[
 \mathcal C_n^{\rm desc}
 =(E_n^0+S_n-J_n^*)+(J_n^*-J_n^{(5/2)}).
\tag{6.2}
\]

Thus the refined five-channel identity is

\[
 \boxed{
 \begin{aligned}
 \mathcal R_n^{\rm sharp}={}&
 \left({3\over4}\mathcal D_n^{\rm pre}-E_n^0\right)
 +(Z_n^{\rm fin}-S_n)\\
 &+(E_n^0+S_n-J_n^*)+Z_n^{\rm fut}
 +(J_n^*-J_n^{(5/2)}).
 \end{aligned}}
\tag{6.3}
\]

Every term on the right is nonnegative by (3.1), (5.4), and (5.5).  Hence

\[
 \boxed{\mathcal R_n^{\rm sharp}\ge0\qquad(n\ge4).}
\tag{6.4}
\]

No positive/negative same-scale cancellation remains inside `Rsharp`.

## 7. Historical P27 candidate and its saturation boundary

Because of (6.4), the positive part in P26 is redundant.  The resulting
historical candidate was

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm sharp}
 =o_{C,\mathbf a}(\log J).}
\tag{P27}
\]

Equivalently, since (6.1) has only four nonnegative channels, each channel's
Fejér sum must be `o(log J)`; (6.3) optionally splits the descendant channel
once more.  The stronger finite-window version is

\[
 \sum_{k=L}^{2L}\mathcal R_{2^k}^{\rm sharp}=o_C(1)
\tag{P27-block}
\]

with the same finite-prefix and cap quantifiers as P26-block.

The companion
`WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md` proves that, on any
hypothetical eventual-`C` branch, an untouched inner sector forces

```text
liminf [sum omega Rsharp]/log J >= 1/(1536 C log2),
```

twice the strict sufficient threshold.  It also gives a positive constant
lower bound for the block sum.  Thus P27 and P27-block are closed as
standalone intermediate targets, not proved.

## 8. A compatibility no-go for local-only P27 proofs

For each `n>=4`, choose a prime `P` with

\[
 2n-1<P<4n-2
\]

and set

\[
 b_i=2Pi+(i^2\bmod P),\qquad0\le i\le2n-2.
\]

As in the certified-rank note, these form a Golomb ruler.  Put
`H=b_(2n-2)` and append `X=2H+1`.  The resulting `2n`-mark prefix is Golomb
and obeys the local `C=32` cap for `n<=q<=2n-1`.  For every
`n<=q<=2n-2`,

\[
 {X\over b_q}>2.
\tag{8.1}
\]

The endpoint slack in (6.1) is

\[
 {3\over4}\mathcal D_n^{\rm pre}-E_n^0
 =\sum_{q=n}^{2n-2}
   \left({3\over4}c_{n,q}-\lambda_{n,q}\right)
   \log{X\over b_q}.
\tag{8.2}
\]

All coefficients are nonnegative.  Their total mass is

\[
 {3\over4}P_n^{\rm coef}-R_n^{\rm coef}
 ={(n-1)(3n+1)\over16n^2}\ge{39\over256},
\tag{8.3}
\]

because `sum_q lambda_(n,q)=sum_p r_(n,p)=Rcoef_n`.  Hence

\[
 \boxed{
 \mathcal R_n^{\rm sharp}
 >{(n-1)(3n+1)\over16n^2}\log2
 \ge {39\over256}\log2.}
\tag{8.4}
\]

Choosing a different prefix at every dyadic scale gives an independent-scale
Fejér diagnostic of order `J`.  These rulers are different, and the cap is
asserted only on each displayed local window.  Thus (8.4) rules out a
same-scale Golomb/rank/cap proof.  The companion inner-birth theorem supplies
the stronger compatible-branch saturation boundary without asserting that
such a branch exists.

## 9. Exact next direction and nonclaims

The next valid design obligation is P28: relocate the untouched inner-birth
sector against the negative renewal cuts, enlarge the descendant absorption
without double spending, or derive a new signed carrier.  Attempting merely
to upper-bound the four nonnegative channels is saturated by their known
harmonic floor.

- Pointwise smallness is false under same-scale local facts by (8.4).
- Integer dilation no longer matters; every term in (6.1) is scale free.
- Separate finite prefixes cannot be summed as though they were one branch.
- The decomposition does not provide the missing inner-birth relocation.
- P19/P24/P25/P26/P27/P28, both Erdős questions, novelty, and every prize claim
  remain open.
