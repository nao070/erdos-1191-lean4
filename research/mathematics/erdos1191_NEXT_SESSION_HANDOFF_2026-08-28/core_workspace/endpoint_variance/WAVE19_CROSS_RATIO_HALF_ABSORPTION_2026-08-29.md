# Wave 19: cross-ratio half absorption and endpoint-deficit cancellation

Date: 2026-08-29 (Asia/Tokyo)  
Status: **two new rigorous coefficientwise absorptions and a sharper signed
frontier target; Erdős #1191 remains open**

## 1. Claim boundary

This note returns upstream of the Wave 18 midpoint majorant and keeps the
two-dimensional descendant geometry.  It proves that the cross-ratio part of
the Wave 18 functional costs at most one half of the exact Wave 12 birth
energy.  It also proves that the remaining endpoint part is absorbed, with a
strict quarter left over, by the negative full-span/prefix deficit already
present in the Wave 13 frontier spectrum.

The result removes `J_n^(5/2)` as a standalone positive error from the
recommended signed route.  It does **not** yet control the surviving terminal
suffix/frontier expression, prove P19, construct an eventual-critical branch,
answer Question 1 or Question 2, or support a prize claim.

Throughout,

\[
 0=a_0<a_1<a_2<\cdots,\qquad D_{p,q}=a_q-a_{p-1},
\]

and `n>=4`.  The coefficient statements need only strict increase; the
integer Golomb and eventual-cap hypotheses enter later, when the Wave 18
signed identity and dyadic error summability are invoked.

## 2. Exact rectangle identity

Put

\[
 A=a_{2n-1},\qquad d_{n,p}=D_{p,2n-1},
\]

and, for `2<=p<=n`, `n<=q<=2n-2`, define

\[
 X_{n,p,q}:={a_qd_{n,p}\over A D_{p,q}}\ge1.
\tag{2.1}
\]

For the positive primitive cross ratios

\[
 C_{ij}=\log{D_{i,j-1}D_{i+1,j}\over
                   D_{i+1,j-1}D_{i,j}},\qquad j-i\ge2,
\]

two finite telescopes give

\[
 \boxed{
 \log X_{n,p,q}
 =\sum_{i=1}^{p-1}\sum_{j=q+1}^{2n-1} C_{ij}.}
\tag{2.2}
\]

Indeed, first telescope in `j` and then in `i`:

\[
 \prod_{i=1}^{p-1}\prod_{j=q+1}^{2n-1}e^{C_{ij}}
 ={D_{1,q}D_{p,2n-1}\over D_{p,q}D_{1,2n-1}}
 ={a_qd_{n,p}\over AD_{p,q}}.
\]

In particular,

\[
 {d_{n,p}\over D_{p,q}}={A\over a_q}X_{n,p,q}.
\tag{2.3}
\]

## 3. Splitting the Wave 18 descendant functional

Retain the Wave 18 coefficients

\[
 \alpha_{n,p}:={r_{n,p}\over w_{n,p}},\qquad
 \beta_{n,p,q}\in\left\{{1\over2n^2},{1\over4n^2},{1\over n^2}\right\}.
\]

For `h>log 3`, set `tau=h-log 3>0`.  Since `c_n/L_(n,p)<3`, (2.3) and
`[u+v]_+<=[u]_++v` for `v>=0` give

\[
 J_n^{(h)}\le E_n^{(h)}+S_n,
\tag{3.1}
\]

where

\[
 \begin{aligned}
 E_n^{(h)}
 &=\sum_{p=2}^n\sum_{q=n}^{2n-2}
   \alpha_{n,p}\beta_{n,p,q}
   \left[\log{A\over a_q}-\tau\right]_+,\\
 S_n
 &=\sum_{p=2}^n\sum_{q=n}^{2n-2}
   \alpha_{n,p}\beta_{n,p,q}\log X_{n,p,q}.
 \end{aligned}
\tag{3.2}
\]

This is sharper than replacing every `q` by the midpoint `q=n`: the endpoint
profile and the positive rectangle atoms remain separately visible.

## 4. Cross-ratio half-absorption theorem

Recall the exact Wave 12 birth energy

\[
 Y_n=\sum_{j=n}^{2n-1}\sum_{i=1}^{j-2}
       \left({j-i\over2n}\right)^2 C_{ij}.
\tag{4.1}
\]

### Theorem 4.1

For every strictly increasing real sequence and every `n>=4`,

\[
 \boxed{S_n\le {1\over2}Y_n.}
\tag{4.2}
\]

#### Proof

By (2.2), the coefficient of `C_(i,j)` in `S_n` is

\[
 K_{n,i,j}
 =\sum_{p=i+1}^n\alpha_{n,p}
   \sum_{q=n}^{j-1}\beta_{n,p,q},
\tag{4.3}
\]

on `1<=i<=n-1`, `n+1<=j<=2n-1`, and zero otherwise.  Put

\[
 x=n-i,\qquad y=j-n.
\]

All `0<alpha_(n,p)<=1`; moreover

\[
 \alpha_{n,n}={2n-3\over2(2n-1)}<{1\over2}.
\tag{4.4}
\]

If `x,y>=2`, the unweighted beta mass of the rectangle in (4.3) is exactly
`xy/(2n^2)`.  Hence AM--GM gives

\[
 K_{n,i,j}\le {xy\over2n^2}
 \le{(x+y)^2\over8n^2}.
\]

If `x=1,y=1`, only `p=q=n` occurs, so
`K=alpha_(n,n)/n^2<1/(2n^2)`.  If `x=1,y>=2`, only `p=n` occurs and

\[
 K=\alpha_{n,n}{2y+1\over4n^2}
 <{2y+1\over8n^2}
 \le{(y+1)^2\over8n^2}.
\]

If `y=1,x>=3`, dropping the alpha factors gives

\[
 K\le{2x+1\over4n^2}
 \le{(x+1)^2\over8n^2},
\]

because `x^2-2x-1>=0`.  The remaining corner `x=2,y=1` is

\[
 K={\alpha_{n,n-1}\over4n^2}+{\alpha_{n,n}\over n^2}
 <{3\over4n^2}<{9\over8n^2}.
\]

In every case this is one half of the coefficient `(x+y)^2/(4n^2)` in
`Y_n`.  Positivity of `C_(i,j)` proves (4.2).  `square`

The constant `1/2` is asymptotically sharp for this coefficientwise theorem:
at `(i,j)=(n-1,n+1)`, the ratio of the two coefficients is exactly
`alpha_(n,n)`, which tends to `1/2`.

## 5. Endpoint weights fit the Wave 13 boundary deficit

Define

\[
 \lambda_{n,q}=\sum_{p=2}^n\alpha_{n,p}\beta_{n,p,q},
 \qquad
 c_{n,q}={2q-1\over4n^2}.
\tag{5.1}
\]

The `c_(n,q)` are exactly the coefficients of `log a_q` in the Wave 13
prefix term

\[
 \mathfrak P_n=\sum_{q=n}^{2n-2}c_{n,q}\log a_q.
\]

Their mass is

\[
 P_n^{\rm coef}=\sum_qc_{n,q}={3(n-1)^2\over4n^2}.
\tag{5.2}
\]

### Lemma 5.1

For `n>=4` and every `n<=q<=2n-2`,

\[
 \boxed{\lambda_{n,q}\le {3\over4}c_{n,q}.}
\tag{5.3}
\]

#### Proof

The exact bulk alpha sum is

\[
 \sum_{p=2}^{n-2}\alpha_{n,p}={3(n-3)\over4},
\tag{5.4}
\]

while `alpha_(n,n-1)<1` and `alpha_(n,n)<1/2`.

For `q=n`, multiply (5.3) by `4n^2`.  The left side becomes

\[
 2\sum_{p=2}^{n-2}\alpha_{n,p}
 +\alpha_{n,n-1}+4\alpha_{n,n}
 <{3n\over2}-{3\over2}
 <{3(2n-1)\over4}.
\]

For `q=n+1`, it is

\[
 2\sum_{p=2}^{n-1}\alpha_{n,p}+\alpha_{n,n}
 <{3n\over2}-2
 <{3(2n+1)\over4}.
\]

For `q>=n+2`, all selected beta cells are bulk cells, and it is

\[
 2\sum_{p=2}^{n}\alpha_{n,p}
 <{3n\over2}-{3\over2}
 <{3(2q-1)\over4}.
\]

This proves all cases.  `square`

The constant `3/4` is the sharp uniform supremum for this endpoint
coefficient comparison.  The maximum over `q` occurs at `q=n` and equals

\[
 {12n^3-40n^2+29n+10\over
  2(2n-3)(2n-1)^2},
\tag{5.4a}
\]

whose gap from `3/4` is

\[
 {20n^2-16n-29\over4(2n-3)(2n-1)^2}>0.
\tag{5.4b}
\]

It tends to `3/4`, so a smaller universal constant cannot replace (5.3)
without using additional geometry of the marks.

Put

\[
 \mathcal D_n^{\rm pre}
 :=P_n^{\rm coef}\log A-\mathfrak P_n
 =\sum_{q=n}^{2n-2}c_{n,q}\log{A\over a_q}\ge0.
\tag{5.5}
\]

Since `tau>0`, Lemma 5.1 yields

\[
 \boxed{E_n^{(h)}\le {3\over4}\mathcal D_n^{\rm pre}.}
\tag{5.6}
\]

The Wave 13 full-span coefficient is

\[
 F_n^{\rm coef}={12n^2-28n+15\over16n^2},
\]

and

\[
 P_n^{\rm coef}-F_n^{\rm coef}={4n-3\over16n^2}.
\tag{5.7}
\]

Consequently

\[
 \boxed{
 (\mathfrak P_n-\mathfrak F_n)+E_n^{(h)}
 \le-{1\over4}\mathcal D_n^{\rm pre}+\varepsilon_n,}
\tag{5.8}
\]

where

\[
 \varepsilon_n={4n-3\over16n^2}\log A.
\tag{5.9}
\]

On an eventual-`C` branch, `sum_k epsilon_(2^k)<infinity`.

## 6. Signed Wave 19 frontier inequality

At `h=5/2`, for all sufficiently large dyadic `n`, retain the Wave 18
nonnegative remainders

\[
 U_n^{\rm cap}=D_n-\Theta_{n/2}^{[h]}\ge0,
 \qquad
 Q_n=H_n^{\rm loc}+J_n^{(h)}-\Theta_n^{\rm exc,h}\ge0.
\]

Insert

\[
 \mathfrak B_n=K_n^{\rm int}+D_n+H_n^{\rm loc}
\]

into the **uncontracted** Wave 13 spectrum

\[
 Z_n=\mathfrak P_n+\mathfrak U_n-
     \mathfrak B_n-\mathfrak F_n-\mathfrak e_n.
\]

Equations (3.1), (4.2), and (5.8) then give the rigorous signed inequality

\[
 \boxed{
 \begin{aligned}
 Z_n\le{}&{1\over2}Y_n+\mathfrak U_n-K_n^{\rm int}
 -\Theta_{n/2}^{[5/2]}-\Theta_n^{\rm exc,5/2}\\
 &-{1\over4}\mathcal D_n^{\rm pre}+\varepsilon_n
 -(U_n^{\rm cap}+Q_n+\mathfrak e_n).
 \end{aligned}}
\tag{6.1}
\]

No term in (6.1) is inferred from a lower bound with the wrong sign.  The
same local floor is used once, and the boundary deficit is a pre-existing
negative term of the exact frontier spectrum.

For a compact remaining target, define

\[
 \mathcal G_n:=\mathfrak U_n-K_n^{\rm int}
 -\Theta_{n/2}^{[5/2]}-\Theta_n^{\rm exc,5/2}
 -{1\over4}\mathcal D_n^{\rm pre}.
\tag{6.2}
\]

Then

\[
 Z_n\le{1\over2}Y_n+\mathcal G_n+\varepsilon_n.
\tag{6.3}
\]

## 7. The exact new sufficient theorem

Fix one eventual-`C` branch and choose `k_0` after the cap onset and every
asymptotic onset used above, including the preceding source scale
`2^(k_0-1)`.  Let `n_k=2^k` and retain the Wave 16 Fejér weights

\[
 \omega_{k,J}=\left({J+1-k\over J+1}\right)^2.
\]

The weighted cut-renewal identity has nonpositive intermediate and terminal
cut coefficients.  Therefore (6.3) implies

\[
 {1\over2}\sum_{k=k_0}^J\omega_{k,J}Y_{n_k}
 \le O_{C,\mathbf a,k_0}(1)
 +\sum_{k=k_0}^J\omega_{k,J}\mathcal G_{n_k}.
\tag{7.1}
\]

The `O(1)` contains the fixed initial cut and the summable epsilon tail.
Hence the following is a sufficient contradiction theorem on any fixed
eventual-`C` branch:

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}\mathcal G_{2^k}
 =o_{C,\mathbf a}(\log J).}
\tag{P24}
\]

Indeed, the Wave 13 integer new-birth theorem gives

\[
 {1\over2}\sum_{k=k_0}^J\omega_{k,J}Y_{2^k}
 \ge {1\over3072C\log2}
      \sum_{k=k_0}^J{\omega_{k,J}\over k+2}
 ={\log J\over3072C\log2}+O_{C,k_0}(1).
\tag{7.2}
\]

Thus the weakest directly sufficient version exposed by the present
constants is

\[
 \boxed{
 \limsup_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}\mathcal G_{2^k}\over\log J}
 <{1\over3072C\log2}.}
\tag{P24-sharp}
\]

The cleaner little-oh statement (P24) is stronger.  Either statement, proved
for every `C` and every fixed compatible infinite eventual-`C` branch, rules
out the hypothetical branch and settles Question 1.

(P24) is **open**.  It is sign-faithful and materially narrower than asking
for a positive bound on `J` in isolation: the complete descendant functional
has disappeared, a half-copy of `Y` is retained on the left, and the endpoint
overshoot has become a favorable prefix deficit.  What remains is the exact
terminal-suffix/current-interior-floor promotion expression `mathcal G_n`, with the
Wave 16 taper and Wave 14--18 ownership constraints still mandatory.

There is a useful current-scale reformulation.  Put

\[
 C_k=\Theta_{2^k}^{[5/2]},\qquad
 E_k=\Theta_{2^k}^{\rm exc,5/2},
\]

and

\[
 \widehat{\mathcal G}_{2^k}
 =\mathfrak U_{2^k}-K_{2^k}^{\rm int}-C_k-E_k
  -{1\over4}\mathcal D_{2^k}^{\rm pre}.
\tag{7.3}
\]

Here `C_k+E_k=sum_(p=2)^(2^k) r_(2^k,p)Pi_(2^k,p)` is the complete
current-scale promotion over the Wave 18 macroscopic source range.  Exact
reindexing gives

\[
\begin{aligned}
 \sum_{k=k_0}^J\omega_{k,J}
  (\mathcal G_{2^k}-\widehat{\mathcal G}_{2^k})
 ={}&-\omega_{k_0,J}C_{k_0-1}\\
 &+\sum_{k=k_0}^{J-1}
   (\omega_{k,J}-\omega_{k+1,J})C_k
   +\omega_{J,J}C_J.
\end{aligned}
\tag{7.4}
\]

Since every `C_k<15/16` and the positive coefficients in (7.4) sum to
`omega_(k_0,J)<1`,

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}\mathcal G_{2^k}
 \le\sum_{k=k_0}^J\omega_{k,J}\widehat{\mathcal G}_{2^k}
 +{15\over16}.}
\tag{7.5}
\]

Consequently any of the following is a concrete sufficient next lemma:

\[
 \sum_{k=k_0}^J\omega_{k,J}
  (\widehat{\mathcal G}_{2^k})_+=o_{C,\mathbf a}(\log J),
\tag{7.6}
\]

or, more strongly,

\[
 (\widehat{\mathcal G}_{2^k})_+=o_{C,\mathbf a}(1/k),
 \qquad
 \sum_{k=L}^{2L}(\widehat{\mathcal G}_{2^k})_+
 =o_{C,\mathbf a}(1).
\tag{7.7}
\]

A direct one-step shift does not already prove any of these statements.  On
the full suffix range `2<=p<=2n-2`, write

\[
 u_{n,p}=v_{n,p}+\bar r_{n,p},\qquad
 v_{n,p}={4n-2p+1\over16n^2},
\]

where

\[
 \bar r_{n,p}=
 \begin{cases}
 (4n-2p-3)/(8n^2),&2\le p\le2n-3,\\
 3/(8n^2),&p=2n-2.
 \end{cases}
\tag{7.8}
\]

Wave 18's `r_(n,p)` is defined only on `2<=p<=n`, where it equals
`bar r_(n,p)`.  After Fejer reindexing the exact full-range coefficient is

\[
 \omega_{k,J}u_{n_k,p}-\omega_{k+1,J}v_{n_k,p}
 =\omega_{k,J}\bar r_{n_k,p}
  +\delta_{k,J}v_{n_k,p},
 \qquad
 \delta_{k,J}={2(J-k)+1\over(J+1)^2}.
\tag{7.9}
\]

This is a genuine linear obstruction.  The full `v`-mass is

\[
 V_n={4n^2-4n-3\over16n^2}\longrightarrow{1\over4},
\]

and the triangular rank floor plus the eventual cap give

\[
 B_n^v:=\sum_{p=2}^{2n-2}v_{n,p}\log d_{n,p}
 ={1\over2}\log n+O_C(\log\log n).
\]

Since `sum_(k<J)delta_(k,J)k=J/3+O(1)`,

\[
 \boxed{
 \sum_{k=k_0}^{J-1}\delta_{k,J}B_{2^k}^v
 ={\log2\over6}J+O_C(\log J).}
\tag{7.10}
\]

Even `2<=p<=n` alone contributes `(log2/8)J+O_C(log J)`.  Thus the bounded
mismatch theorem for the Wave 15 marginal `Delta_n` cannot be substituted:
`Delta_n` is uniformly bounded, whereas the raw `v log d` fan has an exact
linear base channel.  The Wave 14 rebate `Phi_n` adds only a nonnegative
weighted mismatch of size `O_C(log J)` and cannot cancel (7.10).  Moreover,
`K^low+Phi` belongs to the next lower shell, while `mathcal G_n` contains the
same-epoch Gothic interior floor `K_n^int`; they cannot be merged without a
new disjoint ownership theorem.

The next proof must therefore retain more of the exact rank split inside the
global Abel/renewal identity.  The companion certified-remainder note does
this and supersedes bare `\widehat{\mathcal G}` as the recommended local target.
Expanding the terminal potential and simultaneously retaining its
`-\mathfrak F_n` term would still double-spend the same full-span coefficient.

## 8. Certified rank-slack refinement and P25

Sort the complete Gothic interior atom values increasingly as `x_(n,j)` and
carry their actual coefficients `gamma_(n,j)`.  The exact local slack splits
as

\[
 H_n^{\rm loc}=\mathcal S_n^{\rm rank}+\mathcal P_n^{\rm pair},
\]

where

\[
 \mathcal S_n^{\rm rank}
 =\sum_j\gamma_{n,j}\log{x_{n,j}\over j},
 \qquad
 \mathcal P_n^{\rm pair}
 =\sum_j\gamma_{n,j}\log j-F_n^{\rm loc,int},
\]

and both terms are nonnegative.  The Wave 18 spent row is bounded by
`Srank`, not all of `Hloc`, so

\[
 Q_n^{\rm cert}=\mathcal S_n^{\rm rank}+J_n^{(5/2)}
 -\Theta_n^{\rm exc,5/2}\ge0,
 \qquad
 Q_n=Q_n^{\rm cert}+\mathcal P_n^{\rm pair}.
\]

Retaining `Ucap`, `Qcert`, and `mathfrak e_n` in (6.1) gives the exact
finite-prefix remainder

\[
 \mathcal R_n^{\rm cert}
 =\mathfrak U_n-F_n^{\rm loc,int}-\mathcal S_n^{\rm rank}
 -J_n^{(5/2)}-{1\over4}\mathcal D_n^{\rm pre}
 -\mathfrak e_n+\varepsilon_n,
\]

and

\[
 \boxed{Z_n\le{1\over2}Y_n+\mathcal R_n^{\rm cert}.}
\tag{8.1}
\]

The previous cap cancels exactly; no cap-shift error remains.  Moreover,

\[
 \mathcal R_n^{\rm cert}
 =Z_n+{3\over4}\mathcal D_n^{\rm pre}-J_n^{(5/2)}
 +\mathcal P_n^{\rm pair},
\tag{8.2}
\]

and `Rcert` is exactly invariant under integer dilation of the entire ruler.
The recommended target P25 is

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}
 (\mathcal R_{2^k}^{\rm cert})_+
 =o_{C,\mathbf a}(\log J).}
\tag{P25}
\]

Its exact weaker sufficient signed threshold is the same
`1/(3072C log2)` as in (P24-sharp).  P25 is open.

A scaled Erdős--Turán append family proves that bare
`\widehat{\mathcal G}_n` can be `Omega(log log n)` under the same-scale Golomb,
rank, and local `C=32` cap facts.  Different scales use different prefixes,
so this does not refute P24 on one compatible branch.  It does show that
bare pointwise/block `\widehat{\mathcal G}` is locally scale-obstructed, whereas
`Rcert` has no dilation defect.  Full formulas and constants are in
`WAVE19_CERTIFIED_RANK_SLACK_REMAINDER_2026-08-29.md`.

## 9. Summable pairing slack and the sharper P26 target

The coefficient multiset has `n-1` entries of weight `1/n^2`, `n-1`
entries of weight `1/(4n^2)`, and all remaining entries of weight
`1/(2n^2)`.  If `c_n=(n-1)(3n-4)/2`, reverse rearrangement gives

\[
 0\le\mathcal P_n^{\rm pair}
 \le {3\over4n^2}\log{c_n\choose n-1}
 \le {3\over4n}\log{3en\over2}.
\tag{9.1}
\]

Therefore `sum_k Pair_(2^k)<infinity`.  Define the actual-bulk remainder

\[
 \mathcal R_n^{\rm sharp}:=
 \mathfrak U_n-\mathfrak B_n-J_n^{(5/2)}
 -{1\over4}\mathcal D_n^{\rm pre}-\mathfrak e_n+\varepsilon_n.
\tag{9.2}
\]

Equations (3.1) and (5.8), without any rank-floor insertion, give

\[
 \boxed{Z_n\le{1\over2}Y_n+\mathcal R_n^{\rm sharp}.}
\tag{9.3}
\]

Moreover,

\[
 \boxed{
 \mathcal R_n^{\rm sharp}
 =Z_n+{3\over4}\mathcal D_n^{\rm pre}-J_n^{(5/2)},
 \qquad
 \mathcal R_n^{\rm cert}
 =\mathcal R_n^{\rm sharp}+\mathcal P_n^{\rm pair}.}
\tag{9.4}
\]

Thus P25 differs by only `O(1)` in dyadic Fejér mass from the sharper,
rank-free target

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}
 (\mathcal R_{2^k}^{\rm sharp})_+
 =o_{C,\mathbf a}(\log J).}
\tag{P26}
\]

The signed threshold and uniform block forms are equivalent as well; the
block pairing tail is `o(1)`.  P26 was the resulting sharp candidate.  The
complete proof and the explicit dyadic tail bound are in
`WAVE19_SHARP_BULK_REMAINDER_AND_PAIR_SUMMABILITY_2026-08-29.md`.

## 10. Nonnegative refinement and the saturated P27 candidate

Let `Zfin=Zob+Znb`, `Zfut=Zof+Zmf`, and put

\[
 h_n^*=\log{c_n\over L_{n,n}},\qquad
 J_n^*=J_n^{(h_n^*)},\qquad
 E_n^0=\sum_q\lambda_{n,q}\log{A\over a_q}.
\]

A second exact corner audit gives `S_n<=Zfin_n`.  Directly from the
definition of `Jstar`,

\[
 J_n^*\le E_n^0+S_n,\qquad
 E_n^0\le{3\over4}\mathcal D_n^{\rm pre},\qquad
 J_n^*\ge J_n^{(5/2)}.
\]

Consequently

\[
 \boxed{
 \begin{aligned}
 \mathcal R_n^{\rm sharp}={}&
 ({3\over4}\mathcal D_n^{\rm pre}-E_n^0)
 +(Z_n^{\rm fin}-S_n)\\
 &+(E_n^0+S_n-J_n^*)+Z_n^{\rm fut}
 +(J_n^*-J_n^{(5/2)})\ge0.
 \end{aligned}}
\tag{10.1}
\]

Thus P26 is exactly the nonnegative packing target

\[
 \boxed{
 \sum_{k=k_0}^J\omega_{k,J}\mathcal R_{2^k}^{\rm sharp}
 =o_{C,\mathbf a}(\log J).}
\tag{P27}
\]

Different locally `C=32` prime Erdős--Turán append prefixes have
`Rsharp_n>(39/256)log2` at every selected scale, so a same-scale pointwise
proof is impossible; these prefixes are not one compatible branch.  Full
details are in
`WAVE19_NONNEGATIVE_SHARP_REMAINDER_DECOMPOSITION_2026-08-29.md`.

The stronger row-exact audit defines
`Rprof=Z+Erow-J=(Zfin-S)+Zfut+(S-Delta_abs)>=0`.  Its untouched inner sector
`W_n` satisfies, on any hypothetical eventual-`C` branch,

\[
 \liminf_{J\to\infty}
 {\sum_k\omega_{k,J}\mathcal R_{2^k}^{\rm sharp}\over\log J}
 \ge {1\over1536C\log2},
\]

twice the allowed P26/P27 sharp threshold.  Thus P26/P27 are closed as
standalone intermediate upper targets, not proved.  The current P28 design
obligation is to relocate this inner-birth sector against the negative
renewal cuts or absorb it with a new disjoint carrier.  See
`WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`.

## 11. What must not be claimed

- The coefficientwise half-absorption is not an upper bound
  `sum Y=o(log J)`; half of the harmonic signal remains.
- The endpoint cancellation must be performed before replacing the Wave 13
  spectrum by the contracted terminal potential.  Using both versions at
  once would double count `mathfrak F_n`.
- The summable `epsilon_n` uses one fixed eventual cap and onset.  It is not
  a uniform statement over arbitrary delayed finite prefixes.
- Finite coefficient certificates audit (2.2)--(5.8), but do not prove
  (P24), (P25), (P26), (P27), (P28), an infinite branch theorem, or Erdős
  #1191.
