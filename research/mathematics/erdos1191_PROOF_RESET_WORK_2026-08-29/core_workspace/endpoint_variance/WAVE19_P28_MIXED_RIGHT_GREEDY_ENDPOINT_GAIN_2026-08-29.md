# Wave 19 / P28: mixed right-greedy endpoint gain

Date: 2026-08-29 (Asia/Tokyo)  
Status: **the mixed transport theorem and the `2/3` endpoint bound are
proved; the remaining signed Fejér inequality, P28, Question 1, and Erdős
#1191 remain open**

## 1. Claim boundary

This note gives an explicit feasible transport which keeps the proved
coefficientwise cross bound and improves the adaptive endpoint coefficient:

\[
 \boxed{t={8t^0+t^R\over9},\qquad
        S_t\le {1\over2}Y_n,\qquad
        E_t^{\rm rank}\le {2\over3}\mathcal D_n^{\rm pre}.}
\tag{1.1}
\]

Here `t^0` is the natural row-proportional transport and `t^R` fills every
row from its right endpoint.  All three statements in (1.1) hold for every
integer `n>=4`.  The gain over the preceding natural endpoint theorem is
exactly `Dpre_n/12` in the signed bracket.

That gain does **not** close the proof.  The full mixed signed bracket still
contains an uncontrolled bulk/promotion term.  An explicit eight-mark
Golomb ruler below also disproves the tempting unsigned shortcut
`W_n-S_t<=Dpre_n/12`.  No signed cut-corrected version is refuted here.

Nothing in this note proves P28, either question of Erdős Problem #1191, the
existence of an eventual-critical branch, publication novelty, or a prize
claim.

## 2. Rows, capacities, and demands

Let

\[
 \mathcal A_n=\{(p,q):2\le p\le q\le2n-2,\ q\ge n\}.
\]

The Gothic atom capacity is

\[
 \beta_{p,q}=\begin{cases}
  1/(2n^2),&p\le q-2,\\
  1/(4n^2),&p=q-1,\\
  1/n^2,&p=q,
 \end{cases}
\tag{2.1}
\]

and the cut-valid residual row demand is

\[
 \bar r_p=\begin{cases}
  (4n-2p-3)/(8n^2),&2\le p\le2n-3,\\
  3/(8n^2),&p=2n-2.
 \end{cases}
\tag{2.2}
\]

Put

\[
 w_p=\sum_{q=\max(n,p)}^{2n-2}\beta_{p,q},\qquad
 \alpha_p={\bar r_p\over w_p}.
\tag{2.3}
\]

The five direct row cases give `0<alpha_p<1`; hence

\[
 t^0_{p,q}=\alpha_p\beta_{p,q}
\tag{2.4}
\]

is feasible.

For `t^R`, start with residual mass `bar r_p` and, in decreasing order of
`q`, put as much as possible into `(p,q)` up to `beta_(p,q)`.  Thus `t^R`
also has exact row sum `bar r_p` and obeys every atom cap.  Convexity now
proves the row and cap assertions for

\[
 t={8t^0+t^R\over9}.
\tag{2.5}
\]

## 3. The max-flow prefix lemma

For a fixed row and a row prefix ending at `q`, every feasible vector `x`
with total mass `bar r_p` satisfies

\[
 \sum_{s\le q}x_{p,s}
 =\bar r_p-\sum_{s>q}x_{p,s}
 \ge \max\left(0,\bar r_p-\sum_{s>q}\beta_{p,s}\right).
\tag{3.1}
\]

Right fill attains equality in (3.1).  In particular,

\[
 \boxed{\sum_{s\le q}t^R_{p,s}
       \le\sum_{s\le q}t^0_{p,s}}
\tag{3.2}
\]

for every row and every prefix.  This is exactly the one-row max-flow cut
condition; no monotonicity of the marks is being smuggled into the transport.

For a cross-ratio atom `C_(i,j)`, its transport coefficient is the rectangle

\[
 K_t(i,j)=\sum_{p=i+1}^{j-1}\sum_{q=\max(n,p)}^{j-1}t_{p,q}.
\tag{3.3}
\]

Each summand in (3.3) is a row prefix.  Therefore

\[
 K_{t^R}(i,j)\le K_{t^0}(i,j),\qquad
 K_t(i,j)\le K_{t^0}(i,j).
\tag{3.4}
\]

## 4. The all-case cross bound

For completeness, the natural theorem used with (3.4) has the following
all-parameter sign proof.  When `i<n`, write

\[
 x=n-i,\qquad y=j-n.
\]

Split the natural coefficient into rows `p<=n` and `p>n`.  Apart from the
corner `(x,y)=(1,1)`, the long-row target is

\[
 K^{\rm long}_{x,y}\le{x^2+2xy\over8n^2}.
\tag{4.1}
\]

For `x>=3,y>=2`, multiply the gap in (4.1) by
`8n^2(n-1)(2n-3)(2n-1)`.  Its numerator is linear in `y`, with slope

\[
 -4n(n-2)x(x-2)-3x(x-2)-8(n-1)<0,
\]

and its value at the largest possible `y=n-1` is

\[
 2x(n-1)(2n-3)(2n-1)>0.
\]

For `x>=3,y=1`, set `x=3+a`, `n=x+1+b`.  The corresponding numerator is

\[
\begin{aligned}
 &4a^5+12a^4b+56a^4+12a^3b^2+136a^3b+315a^3\\
 &+4a^2b^3+104a^2b^2+579a^2b+904a^2\\
 &+24ab^3+296ab^2+1122ab+1336a\\
 &+32b^3+288b^2+846b+813>0.
\end{aligned}
\]

The remaining non-corner gaps are

\[
\begin{array}{c|c}
 (x,y)&(x^2+2xy)/(8n^2)-K^{\rm long}_{x,y}\\ \hline
 x=1,\ y\ge2&(2y+1)/(4n^2(2n-1))\\
 x=2,\ y=1&(12n^2-12n-13)/(8n^2(2n-3)(2n-1))\\
 x=2,\ y\ge2&(4n^2-6n-2y+1)/(2n^2(2n-3)(2n-1)).
\end{array}
\tag{4.2}
\]

At `(1,1)`, the complete natural coefficient has gap

\[
 {1\over2n^2}-K_{t^0}(n-1,n+1)
 ={1\over n^2(2n-1)}>0.
\tag{4.3}
\]

For `y>=2`, every short-row quotient is below `1/2`, and the complete short
triangle has beta mass `y^2/(4n^2)`.  Hence

\[
 K^{\rm short}_{x,y}<{y^2\over8n^2}.
\tag{4.4}
\]

For `i>=n`, all contributing rows are short and the same quotient argument
applies directly.  Equations (4.1)--(4.4) prove

\[
 K_{t^0}(i,j)\le{(j-i)^2\over8n^2}.
\tag{4.5}
\]

Combining (3.4) and (4.5), coefficient by coefficient in the positive
cross-ratio basis,

\[
 \boxed{S_t\le S_{t^0}\le{1\over2}Y_n.}
\tag{4.6}
\]

## 5. Exact endpoint columns

Let

\[
 b_0={1\over2n^2},\qquad
 M_q^0={\mu_q^0\over b_0},\qquad
 M_q^R={\mu_q^R\over b_0},\qquad
 C_q={c_{n,q}\over b_0}=q-{1\over2},
\tag{5.1}
\]

where `mu_q=sum_p t_(p,q)` and

\[
 c_{n,q}={2q-1\over4n^2}.
\tag{5.2}
\]

The desired mixed column inequality is equivalent to

\[
 {8M_q^0+M_q^R\over9}\le {2\over3}C_q,
 \quad\text{or}\quad
 8M_q^0+M_q^R\le6C_q.
\tag{5.3}
\]

Write `q=n+s`.  In units `b_0`, a bulk, adjacent, and diagonal beta cell has
capacity `1,1/2,2`, respectively.  The ordinary row demand is
`(4n-2p-3)/4`, and the exceptional last demand is `3/4`.  Splitting the
right-fill threshold by the parity of `p`, with the final three rows kept
separate, gives

\[
 q_0(p)=n+\left\lfloor{p-1\over2}\right\rfloor
 \qquad(2\le p\le2n-4).
\]

In these ordinary rows, all columns strictly to the right of `q_0(p)` get
normalized mass `1`; the threshold column gets `1/4` for even `p` and
`3/4` for odd `p`; all columns to its left get zero.  This follows directly
from

\[
 {\bar r_p\over b_0}=n-{p\over2}-{3\over4}.
\]

For `p=2n-3`, the last adjacent and diagonal cells get `1/2,1/4`; for
`p=2n-2`, its diagonal gets `3/4`.  Counting even and odd thresholds in a
fixed column now gives

\[
 \boxed{
 M_{n+s}^R=\begin{cases}
  1/4,&s=0,\\
  2s,&1\le s\le n-4,\\
  2s+1/4,&n-3\le s\le n-2.
 \end{cases}}
\tag{5.4}
\]

An empty middle range in (5.4) is simply omitted.  In particular,

\[
 M_{n+s}^R\le2s+{1\over4}
\tag{5.5}
\]

for every `s>=1`.  The two terminal columns in (5.4), rather than only the
last column, are essential at `n=4`.

The natural column is

\[
 M_q^0=\sum_{p=2}^{q-2}\alpha_p
       +{1\over2}\alpha_{q-1}+2\alpha_q.
\tag{5.6}
\]

The exact long-row sum and the two boundary quotients are

\[
 \sum_{p=2}^{n-2}\alpha_p={3(n-3)\over4},
\]

\[
 \alpha_{n-1}={2n-1\over2(2n-3)},\qquad
 \alpha_n={2n-3\over2(2n-1)},
\]

so

\[
 \alpha_{n-1}+\alpha_n
 =1+\epsilon_n,qquad
 \epsilon_n={2\over(2n-3)(2n-1)}.
\tag{5.7}
\]

Every later quotient is below `1/2`.  Consequently, for `s>=2`,

\[
 M_{n+s}^0
 \le {3n+2s-4\over4}+\epsilon_n.
\tag{5.8}
\]

The first two columns can be summed exactly.  Their normalized margins in
(5.3) are

\[
 6C_n-(8M_n^0+M_n^R)
 ={76n^2-56n-119\over4(2n-3)(2n-1)}>0,
\tag{5.9}
\]

and, for `n>=5`,

\[
 6C_{n+1}-(8M_{n+1}^0+M_{n+1}^R)
 ={20n^2-16n-5\over(2n-3)(2n-1)}>0.
\tag{5.10}
\]

At the overlapping terminal case `n=4`, the margin in (5.10) loses exactly
`1/4` and is still `969/140>0`.

For `s>=2`, (5.5)--(5.8) give the uniform lower margin

\[
\begin{aligned}
 6C_{n+s}-(8M_{n+s}^0+M_{n+s}^R)
 &\ge {19\over4}-8\epsilon_n\\
 &={76n^2-152n-7\over4(2n-3)(2n-1)}>0.
\end{aligned}
\tag{5.11}
\]

The three numerators in (5.9)--(5.11) are already positive at their first
allowed `n`, and their derivatives are positive thereafter.  Thus all
columns and all `n>=4` satisfy

\[
 \boxed{\mu_q(t)\le{2\over3}c_{n,q}.}
\tag{5.12}
\]

## 6. Actual-rank endpoint bound

For the actual Gothic rank `j_(p,q)`, retain the adaptive nonnegative shift

\[
 \sigma_{p,q}=h_{n,p}-\log{j_{p,q}\over L_{n,p}}\ge0.
\]

The endpoint term is

\[
 E_t^{\rm rank}
 =\sum_{p,q}t_{p,q}
   \left[\log{A\over a_q}-\sigma_{p,q}\right]_+.
\]

Dropping a nonnegative shift and then using (5.12) gives

\[
\begin{aligned}
 E_t^{\rm rank}
 &\le\sum_q\mu_q(t)\log{A\over a_q}\\
 &\le{2\over3}\sum_qc_{n,q}\log{A\over a_q}
 ={2\over3}\mathcal D_n^{\rm pre}.
\end{aligned}
\tag{6.1}
\]

This retains the endpoint; it does not revive the invalid endpoint-free
atom inequality.

## 7. A universal lower bound for `Dpre`

Put `r=2n-1-q`.  The suffix from `q+1` through `2n-1` contains `r`
distinct positive adjacent gaps, because equal adjacent gaps would repeat a
Golomb difference.  Therefore

\[
 A-a_q\ge{r(r+1)\over2}.
\tag{7.1}
\]

Also `log(A/a_q)>= (A-a_q)/A`.  Direct finite summation now gives

\[
\begin{aligned}
 \mathcal D_n^{\rm pre}
 &\ge {1\over A}\sum_{r=1}^{n-1}
 {4n-3-2r\over4n^2}{r(r+1)\over2}\\
 &=\boxed{{(n-1)(n+1)(5n-4)\over48nA}}.
\end{aligned}
\tag{7.2}
\]

On a hypothetical eventual-`C` branch, `A<=4Cn^2 log(4n)` implies

\[
 \mathcal D_n^{\rm pre}\ge
 {(n-1)(n+1)(5n-4)\over192C n^3\log(4n)}.
\tag{7.3}
\]

The saving `Dpre/12` is therefore potentially harmonic.  It is not by
itself a contradiction, because it must be inserted into the full signed
ledger.

## 8. Full signed ledger and the exact remaining bracket

Let

\[
 Q_n^{\rm ad}=\mathcal S_n^{\rm rank}+S_{t,n}
 +E_{t,n}^{\rm rank}-\Theta_n^{\rm exc}\ge0.
\]

The exact ownership identity is

\[
\begin{aligned}
 Z_n-R_{2n}={}&
 \mathfrak P_n-K_n^{\rm int}-\mathcal T_n
 -\Theta_{n/2}^{\rm cap}-\Theta_n^{\rm exc}
 +S_{t,n}+E_{t,n}^{\rm rank}\\
 &-\left[(D_n-\Theta_{n/2}^{\rm cap})
 +Q_n^{\rm ad}+\mathcal P_n^{\rm pair}\right].
\end{aligned}
\tag{8.1}
\]

The final bracket is nonnegative at the established large dyadic scales.
After dropping it, applying (1.1), and performing the one-step Fejér
reindexing of the uniformly bounded cap,

\[
 {1\over2}\sum_{k=k_0}^J\omega_{k,J}Y_{2^k}
 \le O_{\mathbf a,k_0}(1)
 +\sum_{k=k_0}^J\omega_{k,J}\mathcal G^{\rm mix}_{2^k},
\tag{8.2}
\]

where

\[
\boxed{
 \mathcal G_n^{\rm mix}
 =R_n+P_n^{\rm coef}\log A-K_n^{\rm int}-\mathcal T_n
 -\Theta_n^{\rm full}-{1\over3}\mathcal D_n^{\rm pre}.}
\tag{8.3}
\]

Thus, relative to the previous natural bracket,

\[
 \boxed{\mathcal G_n^{\rm mix}
       =\mathcal G_n^{\rm old}-{1\over12}\mathcal D_n^{\rm pre}.}
\tag{8.4}
\]

There is a useful hostile rewrite.  From

\[
 Z=\mathfrak P+\mathfrak U-\mathfrak B-\mathfrak F-\mathfrak e,
\quad
 \mathcal T=\mathfrak F+\mathfrak e+R_{2n}-\mathfrak U,
\quad
 Y=R-R_{2n}+Z,
\]

and `mathfrak P=Pcoef log A-Dpre`, pure algebra yields

\[
 \boxed{
 \mathcal G_n^{\rm mix}
 =Y_n+\mathfrak B_n-K_n^{\rm int}-\Theta_n^{\rm full}
 +{2\over3}\mathcal D_n^{\rm pre}.}
\tag{8.5}
\]

Equivalently, using
`mathfrak B=Kint+D+Srank+Pair`,

\[
 \mathcal G_n^{\rm mix}
 =Y_n+D_n+\mathcal S_n^{\rm rank}+\mathcal P_n^{\rm pair}
 -\Theta_n^{\rm full}+{2\over3}\mathcal D_n^{\rm pre}.
\tag{8.6}
\]

Equations (8.5)--(8.6) are algebraic diagnostics, **not new ownership
grants**.  In (8.1), `D-ThetaPrev`, `Qad`, and `Pair` already entered with
favorable negative sign and were dropped.  They cannot be spent again by
reading (8.6) termwise.  The still-open obligation is the weighted bound

\[
 \limsup_{J\to\infty}
 {\sum_{k=k_0}^J\omega_{k,J}\mathcal G^{\rm mix}_{2^k}\over\log J}
 <{1\over3072C\log2},
\tag{8.7}
\]

or a stronger legally owned estimate.  Endpoint saving alone proves no
such bound.

## 9. `Dpre/12` does not pay the inner residual directly

Take `n=4` and

\[
 a_k=100k+k^2\quad(0\le k\le7),
\]

so the marks are

\[
 (0,101,204,309,416,525,636,749).
\tag{9.1}
\]

This is a Golomb ruler.  Indeed, equality of two differences would give

\[
 d(100+i+j)=e(100+k+l).
\]

If `d!=e`, the absolute size of the `100(d-e)` term is at least `100`,
whereas the remaining product difference has absolute size at most `98`.
If `d=e`, then the endpoint sums agree and the two pairs are identical.

On the inner support `(4,6),(4,7),(5,7)`, the mixed residual coefficients
`(j-i)^2/(4n^2)-K_t(i,j)` are

\[
 {259\over5760},\qquad {3\over32},\qquad {5\over128},
\tag{9.2}
\]

and the corresponding cross ratios are

\[
 {15840\over11881},\qquad
 {108891\over96800},\qquad
 {49280\over36963}.
\tag{9.3}
\]

For `x>=1`,

\[
 {2(x-1)\over x+1}\le\log x\le x-1.
\tag{9.4}
\]

Applying the lower bound to (9.2)--(9.3) gives

\[
 \mathcal W_4-S_t\big|_{\mathcal W_4}
 \ge {6200141034958231\over177031495611818280}.
\tag{9.5}
\]

Applying the upper bound to the three endpoint ratios `749/a_q`,
`q=4,5,6`, gives

\[
 {1\over12}\mathcal D_4^{\rm pre}
 \le {18847349\over1269964800}.
\tag{9.6}
\]

The exact rational difference between the right sides of (9.5) and (9.6)
is

\[
 {12603851354568375534803\over624510466439899109990400}>0.
\tag{9.7}
\]

Therefore

\[
 \boxed{\mathcal W_n-S_t\le\mathcal D_n^{\rm pre}/12}
\]

is not a universal inequality, even for finite integer Golomb rulers.  This
does not rule out an inequality with an additional legally retained whole
cut or adjusted terminal term; that is precisely the missing signed bridge.

## 10. Certificate and exact status

The companion artifacts are:

- `wave19_p28_mixed_transport_certificate.py`;
- `test_wave19_p28_mixed_transport_certificate.py`;
- `wave19_p28_mixed_transport_certificate_2026-08-29.json`.

The certificate audits every atom, row prefix, cross rectangle, and endpoint
column at `n=4,5,8,16,32,64,128` using exact `Fraction` arithmetic.  The
memo's polynomial signs prove the theorem for every `n>=4`; the finite audit
is a reproducible hostile check, not an extrapolation.

The exact conclusion is:

- row sums, atom caps, and all-prefix dominance: **proved**;
- `S_t<=Y_n/2`: **proved**;
- `mu_q<=2c_(n,q)/3` and `E_t^rank<=2Dpre_n/3`: **proved**;
- universal lower bound (7.2): **proved**;
- direct payment `W_n-S_t<=Dpre_n/12`: **false**;
- signed Fejér target (8.7): **open**;
- P28, Question 1, and Erdős #1191: **open**;
- prize claim: **not ready**.
