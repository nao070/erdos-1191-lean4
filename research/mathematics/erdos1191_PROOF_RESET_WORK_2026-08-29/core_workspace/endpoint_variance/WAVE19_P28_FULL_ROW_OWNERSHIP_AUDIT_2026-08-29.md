# Wave 19: P28 full-row allocation and renewal-ownership audit

Date: 2026-08-29 (Asia/Tokyo)  
Status: **exact full-row coefficient no-go and cut-valid residual boundary;
P28 and Erdős #1191 remain open**

## 1. Claim boundary

This note audits the most direct proposed repair of the P27 inner-new-birth
saturation.  It extends the descendant rectangle from the Wave 18 source
range `2<=p<=n` to every Gothic interior row `2<=p<=2n-2` and asks whether
the full Wave 13 terminal coefficient can be spread over its own descendant
row.

There are two distinct conclusions.

1. The natural quotient `alpha_p^u=u_p/w_p` fails coefficientwise.  The
   first failure is `n=6`; the first dyadic failure is `n=8`.  Its global
   worst atom is always `C_(1,n+1)`, not an atom of the inner sector `W_n`.
2. Reserving the Wave 16 cut coefficient and allocating only
   `bar r_p=u_p-v_p` respects every row capacity.  On `W_n`, however, this
   cut-valid cross allocation is always below one half of the available
   coefficient.  At least half of the already unavoidable harmonic `W_n`
   floor remains, exactly reaching the old P26-sharp strict threshold.

Nothing here proves or refutes P28, constructs or rules out an
eventual-critical infinite branch, answers Question 1 or 2, establishes
publication novelty, or supports a prize claim.

## 2. Full Gothic rows and terminal ownership

Retain the Wave 13 terminal suffixes

\[
 d_{n,p}=D_{p,2n-1},\qquad 2\le p\le2n-2,
\]

with coefficients

\[
 u_{n,p}=
 \begin{cases}
 (12n-6p-5)/(16n^2),&2\le p\le2n-3,\\
 11/(16n^2),&p=2n-2.
 \end{cases}
\tag{2.1}
\]

For the complete Gothic interior put

\[
 w_{n,p}:=\sum_{q=\max(n,p)}^{2n-2}\beta_{n,p,q}.
\tag{2.2}
\]

Direct summation of the diagonal, subdiagonal, and bulk cells gives

\[
 w_{n,p}=
 \begin{cases}
 (n-1)/(2n^2),&2\le p\le n-2,\\
 (2n-3)/(4n^2),&p=n-1,\\
 (2n-1)/(4n^2),&p=n,\\
 (4n-2p-1)/(4n^2),&n+1\le p\le2n-3,\\
 1/n^2,&p=2n-2.
 \end{cases}
\tag{2.3}
\]

The proposed full-terminal row quotient is therefore

\[
 \alpha_{n,p}^{u}:={u_{n,p}\over w_{n,p}}=
 \begin{cases}
 (12n-6p-5)/(8(n-1)),&2\le p\le n-2,\\
 (6n+1)/(4(2n-3)),&p=n-1,\\
 (6n-5)/(4(2n-1)),&p=n,\\
 (12n-6p-5)/(4(4n-2p-1)),&n+1\le p\le2n-3,\\
 11/16,&p=2n-2.
 \end{cases}
\tag{2.4}
\]

In particular, many early rows have `alpha_p^u>1`.  For the first bulk
case this is equivalent to `6p<4n+3`.  Thus the full coefficient has more
mass than its own negative descendant row even though the *total* Gothic
mass exceeds the total terminal mass.

## 3. The full rectangle is exactly the finite renewal coefficient

For a finite-band atom `C_(i,j)`, put

\[
 \mathcal A_{n,i,j}
 =\{(p,q):\max(n,i+1)\le q\le j-1,\ i+1\le p\le q\}.
\tag{3.1}
\]

The proposed cross coefficient is

\[
 K^{\rm all}_{n,i,j}
 =\sum_{(p,q)\in\mathcal A_{n,i,j}}
   \alpha^u_{n,p}\beta_{n,p,q}.
\tag{3.2}
\]

The same sum with every `alpha_p^u` replaced by one is exactly the Wave 12
finite-sector coefficient:

\[
 \boxed{
 z^{\rm fin}_{n,i,j}
 =\sum_{(p,q)\in\mathcal A_{n,i,j}}\beta_{n,p,q}.}
\tag{3.3}
\]

Indeed, if `i<=n-2`, put `x=n-i` and `y=j-n`.  The beta mass of the
`q`-column is `(2(q-i)+1)/(4n^2)`, and summing gives

\[
 {y(2x+y)\over4n^2},
\]

the coefficient of `Z_n^ob`.  If `i>=n-1`, the first column has mass
`1/n^2` and the remaining columns telescope to

\[
 {(j-i)^2\over4n^2},
\]

the coefficient of `Z_n^nb`.  Consequently
`Kall/zfin` is precisely a beta-weighted average of the row quotients
`alpha_p^u`.

## 4. Exact global failure theorem

### Theorem 4.1

For every `n>=4`, the maximum of

\[
 {K^{\rm all}_{n,i,j}\over z^{\rm fin}_{n,i,j}}
\]

over `n+1<=j<=2n-1`, `1<=i<=j-2`, occurs at
`(i,j)=(1,n+1)`.  Its exact value is

\[
 \boxed{
 {36n^4-140n^3+167n^2-41n-14
  \over4(n-1)(2n-3)(2n-1)^2}.}
\tag{4.1}
\]

It is below one for `n=4,5` and above one for every `n>=6`.

### Proof

Put `a_p=alpha_(n,p)^u`.  After multiplying a `q`-column by `4n^2`, its
ratio is

\[
 A_{i,q}=
 {2\sum_{p=i+1}^{q-2}a_p+a_{q-1}+4a_q\over2(q-i)+1}
 \quad(q-i\ge2),
 \qquad A_{q-1,q}=a_q.
\tag{4.2}
\]

Every rectangle ratio is a positive weighted average of these column
ratios.  We now bound every column without a stochastic-comparison
shortcut.

The sequence `a_2,...,a_n` is strictly decreasing.  This is immediate in
the first linear range, and the only two junction checks are

\[
 a_{n-2}-a_{n-1}
 ={6n-19\over8(n-1)(2n-3)}>0,
 \qquad
 a_{n-1}-a_n
 ={2(3n-2)\over(2n-3)(2n-1)}>0.
\tag{4.3}
\]

Consequently deleting left entries from the `q=n` column cannot increase
its weighted average, and

\[
 A_{i,n}\le A_{1,n}=:mathcal A_n
 \qquad(1\le i\le n-1).
\tag{4.4}
\]

For `i<=n-2`, passing from `q-1` to `q` increases the denominator in (4.2)
by two and adds twice the effective value

\[
 b_q:={a_{q-2}-3a_{q-1}+4a_q\over2}.
\tag{4.5}
\]

At the first new column,

\[
 b_{n+1}={12n^2-16n-1\over4(2n-3)(2n-1)},
\]

and direct denominator clearing gives

\[
 mathcal A_n-b_{n+1}
 ={(2n^2-11n+13)(6n^2-3n-1)
   \over4(n-1)(2n-3)(2n-1)^2}>0.
\tag{4.6}
\]

For `n+2<=q<=2n-3`, put `t=2n-q>=3`.  Then

\[
 b_q={24t^3+28t^2-26t-29
       \over4(2t-1)(2t+1)(2t+3)},
 \qquad
 {3\over4}-b_q
 ={2t^2+5t+5\over(2t-1)(2t+1)(2t+3)}>0.
\tag{4.7}
\]

The last column has `b_(2n-2)=207/280<3/4`.  Moreover

\[
 mathcal A_n-{3\over4}
 ={12n^4-56n^3+65n^2+10n-23
   \over4(n-1)(2n-3)(2n-1)^2}>0,
\tag{4.8}
\]

because the numerator at `n=4+m` is
`12m^4+136m^3+545m^2+914m+545`.  Equations (4.4)--(4.8) inductively give
`A_(i,q)<=mathcal A_n` for every `i<=n-2`.

For `i=n-1`, the first column is `a_n<3/4`.  The exceptional transition
from gap one to gap two adds one denominator unit with effective value

\[
 4a_{n+1}-3a_n
 ={12n^2-28n-1\over4(2n-3)(2n-1)}<{3\over4},
\tag{4.9}
\]

the positive difference being
`(2n+5)/(2(2n-3)(2n-1))`; all later transitions use (4.5)--(4.7).
Finally, if `i>=n`, every available `a_p`, including
`a_(2n-2)=11/16`, is strictly below `3/4`.  Thus every column ratio is at
most `mathcal A_n`, with equality only at `(i,q)=(1,n)`, and the same is
true of every rectangle ratio.

At that cell only `q=n` occurs.  Substitution of (2.4) gives

\[
 n^2K^{\rm all}_{n,1,n+1}
 ={(n-3)(9n-5)\over16(n-1)}
 +{6n+1\over16(2n-3)}
 +{6n-5\over4(2n-1)}.
\tag{4.10}
\]

Since `zfin_(1,n+1)=(2n-1)/(4n^2)`, simplifying (4.10) proves
(4.1).  The numerator of (4.1) minus its denominator is

\[
 P(n)=4n^4-28n^3+31n^2+27n-26.
\tag{4.11}
\]

Here `P(4)=-190`, `P(5)=-116`, while

\[
 P(6+m)=4m^4+68m^3+391m^2+831m+388>0
\]

for every integer `m>=0`.  This proves the stated boundary.  `square`

The ratio in (4.1) tends to `9/8`.  Thus the failure is not a vanishing
finite-size corner.

## 5. Exact finite enumeration

The accompanying Fraction certificate enumerates every finite atom.

| `n` | worst atom | `Kall` | `zfin` | ratio | excess | violating atoms |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | `(1,5)` | `275/2688` | `7/64` | `275/294` | `-19/2688` | 0 |
| 5 | `(1,6)` | `2239/25200` | `9/100` | `2239/2268` | `-29/25200` | 0 |
| 6 | `(1,7)` | `2771/35640` | `11/144` | `5542/5445` | `97/71280` | 2 |
| 8 | `(1,9)` | `43061/698880` | `15/256` | `43061/40950` | `2111/698880` | 4 |
| 16 | `(1,17)` | `913969/27617280` | `31/1024` | `913969/836070` | `77899/27617280` | 26 |
| 32 | `(1,33)` | `16665449/975937536` | `63/4096` | `16665449/15010758` | `1654691/975937536` | 130 |
| 64 | `(1,65)` | `56796101/6554419200` | `127/16384` | `56796101/50806350` | `5989751/6554419200` | 559 |

The smallest counterexample is therefore `n=6`; the smallest dyadic one is
`n=8`.

## 6. The failure is not in the inner sector

On the support of

\[
 W_n=\sum_{j=n+2}^{2n-1}\sum_{i=n}^{j-2}
 { (j-i)^2\over4n^2}C_{ij},
\tag{6.1}
\]

only rows `p>=n+1` occur.  The exact maximum of the full-terminal weighted
coefficient relative to `W_n` is

\[
 \max_{i\ge n}{K^{\rm all}_{n,i,j}\over z^{\rm fin}_{n,i,j}}
 =\begin{cases}
 11/16,&n=4,5,\\
 (6n-11)/(8n-12),&n\ge6,
 \end{cases}
\tag{6.2}
\]

and is always below `3/4`.  The maximizer for `n>=6` is the two-gap atom
`C_(n,n+2)`, which isolates the row `p=n+1`.  Thus the global no-go is caused
by early old-birth rows whose quotient exceeds one, not by a lack of literal
coefficient capacity inside `W_n`.

## 7. Two independent ownership failures of the full-u allocation

The first failure is rowwise.  Since `alpha_p^u w_p=u_p`, exact algebra gives

\[
 u_p\log d_{n,p}-\sum_q\beta_{p,q}\log D_{p,q}
 =\sum_q\alpha_p^u\beta_{p,q}\log{d_{n,p}\over D_{p,q}}
 +(\alpha_p^u-1)\sum_q\beta_{p,q}\log D_{p,q}.
\tag{7.1}
\]

When `alpha_p^u>1`, the last term is positive.  Dropping it would spend more
than the actual Gothic row coefficient.

The second failure is cross-epoch.  Wave 19 (7.8) gives exactly

\[
 u_{n,p}=v_{n,p}+\bar r_{n,p},
 \qquad
 v_{n,p}={4n-2p+1\over16n^2},
\tag{7.2}
\]

where `v_(n,p)` is the coefficient already owned by the next negative cut
`R_(2n)`.  Allocating all of `u_p` to current descendants while retaining
that cut spends `v_p` twice.  P28 expressly requires the negative renewal
cut, so the full-u allocation is inadmissible independently of Theorem 4.1.

## 8. The cut-valid full-row allocation

Reserve `v_p` and allocate only

\[
 \bar r_{n,p}=u_{n,p}-v_{n,p}.
\]

Then

\[
 \bar\alpha_{n,p}:={\bar r_{n,p}\over w_{n,p}}=
 \begin{cases}
 (4n-2p-3)/(4(n-1)),&2\le p\le n-2,\\
 (2n-1)/(2(2n-3)),&p=n-1,\\
 (2n-3)/(2(2n-1)),&p=n,\\
 (4n-2p-3)/(2(4n-2p-1)),&n+1\le p\le2n-3,\\
 3/8,&p=2n-2.
 \end{cases}
\tag{8.1}
\]

Every quotient in (8.1) lies in `(0,1)`.  Hence the corresponding full-row
cross coefficient is bounded by `zfin` coefficientwise and no Gothic atom
or negative cut is double spent.

On the inner rows, put `t=2n-p`.  For `n+1<=p<=2n-3`,

\[
 \bar\alpha_{n,p}={2t-3\over2(2t-1)},
 \qquad 3\le t\le n-1.
\]

Thus

\[
 {3\over10}\le\bar\alpha_{n,p}<{1\over2},
 \qquad
 \bar\alpha_{n,2n-2}={3\over8}.
\tag{8.2}
\]

Let `S_n^(bar,W)` be the cross energy obtained by restricting this allocation
to the atoms in (6.1).  Since every coefficient ratio is a positive
beta-weighted average of the row quotients, (8.2) gives exactly

\[
 \boxed{
 {3\over10}W_n\le S_n^{\bar r,W}<{1\over2}W_n.}
\tag{8.3}
\]

Consequently

\[
 W_n-S_n^{\bar r,W}>{1\over2}W_n.
\tag{8.4}
\]

## 9. The old strict threshold is still saturated

The P27 inner-sector theorem gives, on any hypothetical fixed
eventual-`C` branch and all sufficiently large dyadic `n`,

\[
 W_n>{1\over1536C\log(4n)}.
\tag{9.1}
\]

Combining (8.4) and (9.1), the unallocated part alone satisfies

\[
 W_n-S_n^{\bar r,W}
 >{1\over3072C\log(4n)}.
\tag{9.2}
\]

Therefore its Fejér liminf is at least

\[
 {1\over3072C\log2},
\tag{9.3}
\]

whereas the old P26-sharp condition required a limsup *strictly below* this
same constant.  Thus the natural cut-valid full-row allocation still cannot
cross the required strict threshold.  This is a saturation no-go for this
specific carrier, not an unconditional disproof of P28.

## 10. What does and does not extend to short rows

The original macro-source range `p<=n` has `c_n/L_(n,p)<3<exp(5/2)`, so

\[
 \tau_{n,p}={5\over2}-\log{c_n\over L_{n,p}}>0
\]

and the old endpoint payment has a nonnegative row cap.

For the final full row `p=2n-2`, however, `L_(n,p)=3` and

\[
 {c_n\over L_{n,2n-2}}
 ={(n-1)(3n-4)\over6}>13>e^{5/2}
\]

for `n>=7`.  The last inequality has an exact rational Taylor-tail
certificate.  Hence `tau_(n,2n-2)<0`.

This does **not** invalidate the row-exact positive-part increment.  For
`v>=0` and every real `u,t`,

\[
 0\le [u+v-t]_+-[u-t]_+\le v.
\tag{10.1}
\]

Thus the coefficientwise `0<=Delta<=S` argument remains valid even on a
short row with negative `tau`.  What fails is the old endpoint payment.
When `tau_(n,p)<0` and `u>=0`,

\[
 [u-\tau_{n,p}]_+=u+(-\tau_{n,p}),
\]

so `Erow<=Eend<=3Dpre/4` no longer follows.  Equivalently, the unshifted
four-channel term `E0+S-J` can lose the extra shift and cannot be declared
nonnegative without paying it.

For `s=2n-p`, the short-tail condition is exactly

\[
 \tau_{n,p}<0
 \quad\Longleftrightarrow\quad
 s(s+1)<(n-1)(3n-4)e^{-5/2}.
\tag{10.2}
\]

Thus only the tail `p\gtrsim1.5038n` is affected.  A companion short-row
calculation reports that the missing shift mass

\[
 M_n:=\sum_{\tau_{n,p}<0}\bar r_{n,p}(-\tau_{n,p})
\tag{10.3}
\]

has limit `3e^(-5/2)/8=0.0307818745...`, and that its dyadic Fejer-weighted
sum is asymptotic to `e^(-5/2)J/8`, hence is `Theta(J)`.  Those asymptotics
belong to the companion short-row audit and are recorded here as a boundary,
not re-certified by the present Fraction certificate.  They identify the
quantitative obstruction: a successful extension of this carrier must pay
the short-row shift while retaining the negative renewal cut.  The
row-exact `Delta` inequality itself needs no repair.

## 11. Reproducible certificate and nonclaims

Artifacts:

- `wave19_p28_full_row_ownership_certificate.py`;
- `test_wave19_p28_full_row_ownership_certificate.py`;
- `wave19_p28_full_row_ownership_certificate_2026-08-29.json`.

The certificate uses exact `Fraction` arithmetic for `n=4,5,6,8,16,32,64`.
It audits all `249` rows, `7,817` finite atoms per allocation, `2,563` inner
atoms per allocation, and `21,009` exact subtests.  Its explicit scope flags
state that P28, both Erdős questions, the existence or nonexistence of an
eventual-critical branch, and every prize claim remain unresolved.
