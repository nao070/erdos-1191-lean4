# Wave 19: P28 adaptive row cap and the endpoint-retaining boundary

Date: 2026-08-29 (Asia/Tokyo)  
Status: **the adaptive cap is paid and the full-row coefficient theorem is
proved; the remaining signed Fejér inequality, P28, and Erdős #1191 remain
open**

## 1. Claim boundary

This note tests the strongest surviving version of the P28 full-row idea.
It preserves the Wave 16 negative renewal cut, gives every residual row an
adaptive cap height, and allows actual sorted ranks of Gothic atoms in the
excess split.

Four conclusions are rigorous.

1. The deterministic adaptive cap profile is eventually smaller than the
   next-scale Wave 17 rank surplus.  In the target epoch notation, the
   comparison holds for every `N>=2048`.
2. The natural cut-valid full-row cross allocation satisfies
   `Sbar_n<=Y_n/2` coefficientwise for every `n>=4`.  Its constant `1/2` is
   asymptotically sharp.
3. Actual atom ranks improve the endpoint profile but do **not** remove it.
   The proposed endpoint-free inequality
   `Excess<=Srank+Sbar` is invalid at the atomic level.
4. Even an arbitrary feasible row transport cannot cover a uniform fraction
   greater than `1/3` of every inner `W_n` coefficient.

The first conclusion uses an upper bound, not a false equality:

\[
 \Theta_n^{\rm cap}
 :=\sum_p\bar r_{n,p}\min(\Pi_{n,p},h_{n,p})
 \ \le\ 
 \mathcal C_n^{\rm det}:=\sum_p\bar r_{n,p}h_{n,p}.
\tag{1.1}
\]

Equality in (1.1) need not hold; for example, if every `Pi_(n,p)=0`, its
left side is zero and its right side is positive.  This correction matters
for the ownership ledger below.

Nothing here proves or refutes P28, constructs an eventual-critical infinite
Golomb ruler, resolves Question 1 or 2, establishes publication novelty, or
supports a prize claim.

## 2. Full cut-valid residual and adaptive height

Put

\[
 c_n={ (n-1)(3n-4)\over2},\qquad
 L_{n,p}={ (2n-p)(2n-p+1)\over2},
 \qquad 2\le p\le2n-2.
\tag{2.1}
\]

Reserve the Wave 16 cut coefficient `v_(n,p)` and use only
`bar r_(n,p)=u_(n,p)-v_(n,p)`.  With `s=2n-p`,

\[
 \bar r_{n,p}=
 \begin{cases}
 (2s-3)/(8n^2),&s\ge3,\\
 3/(8n^2),&s=2.
 \end{cases}
\tag{2.2}
\]

The exceptional last coefficient in (2.2) is essential.  Direct summation
gives

\[
 \boxed{
 \overline R_n:=\sum_{p=2}^{2n-2}\bar r_{n,p}
 ={4n^2-12n+11\over8n^2}< {1\over2}.}
\tag{2.3}
\]

For `h_0=3/2`, define the row-dependent height

\[
 h_{n,p}:=\max\left\{h_0,\log{c_n\over L_{n,p}}\right\}.
\tag{2.4}
\]

Then

\[
 \tau_{n,p}:=h_{n,p}-\log{c_n\over L_{n,p}}\ge0
\tag{2.5}
\]

on every row, including the short tail where the fixed height `5/2` had a
negative threshold.

For

\[
 \Pi_{n,p}:=log{
 \rho_\infty(d_{n,p})\over\rho_{2n}(d_{n,p})},
 \qquad d_{n,p}=D_{p,2n-1},
\]

split the full residual promotion exactly as

\[
 \Theta_n^{\rm full}
 =\Theta_n^{\rm cap}+\Theta_n^{\rm exc},
 \qquad
 \Theta_n^{\rm exc}
 =\sum_p\bar r_{n,p}(\Pi_{n,p}-h_{n,p})_+.
\tag{2.6}
\]

The actual cap satisfies (1.1), while the deterministic capacity is

\[
 \boxed{
 \mathcal C_n^{\rm det}
 =h_0\overline R_n+M_n(h_0),}
 \qquad
 M_n(h_0):=
 \sum_p\bar r_{n,p}
 \left[\log{c_n\over L_{n,p}}-h_0\right]_+.
\tag{2.7}
\]

Thus (2.7) is an equality for the deterministic profile, not for the actual
capped promotion.

## 3. A rigorous deterministic cap bound

Let

\[
 B_n=(n-1)(3n-4)e^{-h_0},\qquad
 f(x)=\log_+{B_n\over x}.
\]

Using `s=2n-p`, formula (2.2) rewrites the extra mass as

\[
 M_n(h_0)={1\over8n^2}
 \left(
  \sum_{s=2}^{2n-2}(2s-3)f(s(s+1))+2f(6)
 \right).
\tag{3.1}
\]

The function `f` is decreasing.  Since the interval
`[s(s-1),s(s+1)]` has length `2s`,

\[
 (2s-3)f(s(s+1))
 \le\int_{s(s-1)}^{s(s+1)} f(x)\,dx.
\]

These intervals concatenate.  Extending their union to `[0,B_n]` gives

\[
 \sum_s(2s-3)f(s(s+1))
 \le\int_0^{B_n}\log{B_n\over x}\,dx=B_n.
\tag{3.2}
\]

Moreover, `B_n/6<n^2/2` and
`log(n^2/2)<n` for `n>=4`; the latter follows at `n=4` and then from the
positive derivative of `n-2log n`.  Hence `f(6)<n`, and (3.1)--(3.2) imply

\[
 M_n(3/2)
 <{3e^{-3/2}\over8}+{1\over4n}.
\tag{3.3}
\]

Combining (2.3), (2.7), and (3.3),

\[
 \boxed{
 \mathcal C_n^{\rm det}
 <{3\over4}+{3e^{-3/2}\over8}+{1\over4n}
 <0.8336738101+{0.3009853\over n}.}
\tag{3.4}
\]

The constants in the second inequality are certified with rational Taylor
bounds.  In particular,

\[
 {3\over4}+{3e^{-3/2}\over8}
 =0.833673810055661\ldots<0.8336738101.
\]

The finite deterministic profiles are:

| `n` | `Cdet_n` |
|---:|---:|
| 4 | 0.316406250000000 |
| 8 | 0.521157269942411 |
| 16 | 0.658397616827746 |
| 32 | 0.739984096886761 |
| 64 | 0.785023950556576 |
| 128 | 0.808833196029032 |
| 256 | 0.821105941692858 |
| 512 | 0.827349355982125 |
| 1024 | 0.830500281861568 |

These rows are computational checks of the formula; the all-`n` conclusion
is (3.4).

## 4. The next-scale rank surplus pays the cap

Wave 17 proved

\[
 D_N\ge\delta_0-{18(1+\log N)\over N},
 \qquad
 \delta_0={3\over2}+{3\over4}\log3-2\log2.
\tag{4.1}
\]

The target epoch `N` pays the actual cap from source epoch `N/2`.  By
(1.1) and (3.4),

\[
 \Theta_{N/2}^{\rm cap}
 \le\mathcal C_{N/2}^{\rm det}
 <0.8336738101+{0.6019706\over N}.
\tag{4.2}
\]

At `N=2048`, rational lower and upper bounds for `log 2`, `log 3`, and
`e^(3/2)` give the strict margin

\[
 \left[\delta_0-{18(1+\log2048)\over2048}\right]_{\rm lower}
 -\left[0.8336738101+{0.6019706\over2048}\right]
 >0.0278947990161.
\tag{4.3}
\]

The left side of (4.1) increases as a function of real `N>1`, because
`(1+log N)/N` decreases, while the right side of (4.2) decreases.  Therefore

\[
 \boxed{D_N>\mathcal C_{N/2}^{\rm det}
 \ge\Theta_{N/2}^{\rm cap}\qquad(N\ge2048).}
\tag{4.4}
\]

This closes the adaptive-cap capacity question with the required scale
alignment.  It does not pay the current adaptive excess.

## 5. Natural full-row transport and `Sbar<=Y/2`

Let

\[
 w_{n,p}=\sum_{q=\max(n,p)}^{2n-2}\beta_{n,p,q},
 \qquad
 \bar\alpha_{n,p}={\bar r_{n,p}\over w_{n,p}}.
\tag{5.1}
\]

The exact five row cases are those in the full-row audit.  Every quotient
lies in `(0,1)`, and every short-row quotient with `p>n` is strictly below
`1/2`.

Use the natural feasible transport

\[
 t_{n,p,q}:=\bar\alpha_{n,p}\beta_{n,p,q},
 \qquad \sum_qt_{n,p,q}=\bar r_{n,p}.
\tag{5.2}
\]

Let `Sbar_n` be its cross-ratio energy.  For the coefficient of `C_(i,j)`,
first suppose `i<n` and put

\[
 x=n-i,\qquad y=j-n.
\]

Split the coefficient into rows `p<=n` and `p>n`:

\[
 K_{n,i,j}^{\rm bar}=K^{\rm long}_{x,y}+K^{\rm short}_{x,y}.
\]

Except at `(x,y)=(1,1)`, exact summation gives

\[
 K^{\rm long}_{x,y}
 \le {x^2+2xy\over8n^2}.
\tag{5.3}
\]

Here is an all-parameter sign audit of (5.3).  For `x>=3,y>=2`, after
multiplication by the positive denominator
`8n^2(n-1)(2n-3)(2n-1)`, the gap has numerator `G(n,x,y)`.  It is linear in
`y`, with slope

\[
 -4n(n-2)x(x-2)-3x(x-2)-8(n-1)<0,
\]

and its value at the largest possible `y=n-1` is

\[
 G(n,x,n-1)=2x(n-1)(2n-3)(2n-1)>0.
\]

For `x>=3,y=1`, put `x=3+a`, `n=x+1+b`.  The numerator is

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
\]

All are positive on the stated ranges.  At `(x,y)=(1,1)`, the complete
coefficient has gap

\[
 {1\over2n^2}-K_{n,n-1,n+1}^{\rm bar}
 ={1\over n^2(2n-1)}>0.
\tag{5.4}
\]

For `y>=2`, the unweighted beta mass of the short triangle is
`y^2/(4n^2)`.  Since every short-row quotient is below `1/2`,

\[
 K^{\rm short}_{x,y}<{y^2\over8n^2};
\tag{5.5}
\]

for `y=1` it is zero.  Equations (5.3)--(5.5) give

\[
 K_{n,i,j}^{\rm bar}
 \le{(x+y)^2\over8n^2},
\]

which is one half of the `Y_n` coefficient.  If `i>=n`, all contributing
rows have quotient below `1/2`, while their complete beta rectangle has
coefficient `(j-i)^2/(4n^2)`.  This proves

\[
 \boxed{\overline S_n\le {1\over2}Y_n}
\tag{5.6}
\]

coefficientwise for every `n>=4`.

The constant is asymptotically sharp at `C_(1,2n-1)`.  That coefficient of
`Sbar_n` uses every row and equals `Rbar_n`, so its ratio to the `Y_n`
coefficient is

\[
 {4n^2-12n+11\over8(n-1)^2}\longrightarrow {1\over2}.
\tag{5.7}
\]

The absolute gap from `Y_n/2` is only

\[
 {4n-7\over8n^2}.
\tag{5.8}
\]

Thus there is no uniform strict saving below one half.

## 6. The adaptive endpoint profile is still present

The old `c_n`-based adaptive atom is

\[
 \left[
 \log{A\over a_q}+\log X_{n,p,q}-\tau_{n,p}
 \right]_+,
 \qquad
 X_{n,p,q}={a_qd_{n,p}\over A D_{p,q}}\ge1.
\tag{6.1}
\]

For nonnegative `e,x,t`,

\[
 [e+x-t]_+\le[e-t]_++x.
\tag{6.2}
\]

Consequently adaptive heights repair the negative short-row threshold, but
they do not remove the endpoint part

\[
 E^{\rm full}_n
 =\sum_{p,q}t_{n,p,q}
 \left[\log{A\over a_q}-\tau_{n,p}\right]_+.
\tag{6.3}
\]

On every row where `h_(n,p)=log(c_n/L_(n,p))`, one has `tau_(n,p)=0`, so
the endpoint term is unshifted.

For the natural transport, dropping its nonnegative shift gives

\[
 E_n^{\rm full}\le E_n^0
 :=\sum_{p,q}t_{n,p,q}\log{A\over a_q}.
\]

The exact column coefficients satisfy

\[
 \boxed{E_n^0\le{3\over4}\mathcal D_n^{\rm pre}.}
\tag{6.4}
\]

For completeness, if `a_p=bar alpha_(n,p)` and

\[
 L_q=4n^2\sum_{p=2}^q a_p\beta_{n,p,q}
 =2\sum_{p=2}^{q-2}a_p+a_{q-1}+4a_q,
\]

then the midpoint ratio `L_n/(2n-1)` is the Wave 19 endpoint ratio

\[
 {12n^3-40n^2+29n+10\over
  2(2n-3)(2n-1)^2}<{3\over4}.
\]

Passing from `q` to `q+1` adds
`a_(q-1)-3a_q+4a_(q+1)` to `L_q`, while the comparison denominator grows
by two.  Direct substitution shows this increment is below `3/2`: the gaps
are

\[
 {4n^2-8n+15\over2(2n-3)(2n-1)}
\]

at the first transition,

\[
 {8n^3-20n^2+22n+9\over
  2(2n-5)(2n-3)(2n-1)}
\]

at the next nonterminal transition, and, with `t=2n-q`,

\[
 {8t^3+4t^2+6t+19\over
  2(2t-3)(2t-1)(2t+1)}
\]

on the ordinary short tail.  The final exceptional transition has gap
`19/35`.  This proves (6.4), including the `n=4` overlap by using the final
case directly.

## 7. Correct actual-rank split

Let `j_(p,q)` be the actual rank of `D_(p,q)` among the `c_n` Gothic
interior values.  Allow any feasible transport

\[
 \mathcal T_n=\left\{t:
 0\le t_{p,q}\le\beta_{n,p,q},\quad
 \sum_{q=\max(n,p)}^{2n-2}t_{p,q}=\bar r_{n,p}
 \right\}.
\tag{7.1}
\]

Since `j_(p,q)<=c_n`, define

\[
 \sigma_{p,q}:=h_{n,p}-\log{j_{p,q}\over L_{n,p}}\ge0.
\tag{7.2}
\]

The exact atom identity is

\[
 \log{d_{n,p}\over e^{h_{n,p}}L_{n,p}}
 =\log{D_{p,q}\over j_{p,q}}
  +\log X_{n,p,q}
  +\log{A\over a_q}-\sigma_{p,q}.
\tag{7.3}
\]

The first two logarithms on the right are nonnegative.  Therefore

\[
\begin{aligned}
 \left[\log{d_{n,p}\over e^{h_{n,p}}L_{n,p}}\right]_+
 \le{}&\log{D_{p,q}\over j_{p,q}}+\log X_{n,p,q}\\
 &+\left[\log{A\over a_q}-\sigma_{p,q}\right]_+.
\end{aligned}
\tag{7.4}
\]

After multiplying by a feasible `t` and summing,

\[
 \boxed{
 \Theta_n^{\rm exc}
 \le\mathcal S_n^{\rm rank}
   +S_{t,n}+E_{t,n}^{\rm rank},}
\tag{7.5}
\]

where

\[
 S_{t,n}=\sum_{p,q}t_{p,q}\log X_{n,p,q},\qquad
 E_{t,n}^{\rm rank}=\sum_{p,q}t_{p,q}
 \left[\log{A\over a_q}-\sigma_{p,q}\right]_+.
\tag{7.6}
\]

The endpoint-free claim would drop the last term of (7.4).  At the level of
nonnegative logarithmic variables, take

```text
log(D/j)=0, log X=0, log(A/a_q)=1, sigma=0.
```

Then the left side of (7.4) is `1`, while the proposed endpoint-free right
side is `0`.  Thus `h_p>=log(j/L_p)` is insufficient.  Endpoint removal
would require the stronger, presently unavailable condition

\[
 j_{p,q}\le e^{h_{n,p}}L_{n,p}{a_q\over A}.
\tag{7.7}
\]

This is the precise failure of the proposed
`Excess<=Srank+Sbar` shortcut.

## 8. Exact signed ownership ledger

The local Gothic bulk has the exact ownership split

\[
 \mathfrak B_n=F_n^{\rm loc,int}
 +\mathcal S_n^{\rm rank}+\mathcal P_n^{\rm pair},
 \qquad
 F_n^{\rm loc,int}=K_n^{\rm int}+D_n.
\tag{8.1}
\]

For a feasible transport, put

\[
 Q_n^{\rm ad}:=mathcal S_n^{\rm rank}
 +S_{t,n}+E_{t,n}^{\rm rank}-\Theta_n^{\rm exc}\ge0.
\tag{8.2}
\]

Then, purely algebraically,

\[
 \boxed{
 \mathfrak U_n-\mathfrak B_n
 =\mathfrak U_n-F_n^{\rm loc,int}-\Theta_n^{\rm exc}
 +S_{t,n}+E_{t,n}^{\rm rank}
 -\mathcal P_n^{\rm pair}-Q_n^{\rm ad}.}
\tag{8.3}
\]

Thus `S_t` and `E_t^rank` have positive sign; `Pair` and `Qad` have
favorable negative sign.  The rank slack is spent exactly once inside
`Qad`.  The `v_p` part is not in `bar r_p` and remains owned by the complete
negative renewal cut.

Using the exact Wave 16 terminal identity

\[
 Z_n-R_{2n}=\mathfrak P_n-\mathfrak B_n-\mathcal T_n,
 \qquad \mathcal T_n\ge0,
\tag{8.4}
\]

and adding/subtracting the actual preceding cap gives the exact ledger

\[
\begin{aligned}
 Z_n-R_{2n}={}&
 \mathfrak P_n-K_n^{\rm int}-\mathcal T_n
 -\Theta_{n/2}^{\rm cap}-\Theta_n^{\rm exc}
 +S_{t,n}+E_{t,n}^{\rm rank}\\
 &-\left[
   (D_n-\Theta_{n/2}^{\rm cap})
   +Q_n^{\rm ad}+\mathcal P_n^{\rm pair}
  \right].
\end{aligned}
\tag{8.5}
\]

Every term in the final bracket is nonnegative for sufficiently large
dyadic `n` by (4.4), (7.5), and (8.1).  This ledger contains no duplicated
Gothic coefficient and no duplicated cut coefficient.

For the natural transport, (5.6) and (6.4) give

\[
 S_{t,n}\le{1\over2}Y_n,
 \qquad
 E_{t,n}^{\rm rank}\le E_n^0
 \le{3\over4}\mathcal D_n^{\rm pre}.
\tag{8.6}
\]

The one-step Fejér reindexing of the uniformly bounded cap costs `O(1)`.
Since

\[
 \Theta_n^{\rm full}
 =\Theta_n^{\rm cap}+\Theta_n^{\rm exc},
 \qquad
 \mathfrak P_n=P_n^{\rm coef}\log A-\mathcal D_n^{\rm pre},
\]

(8.5)--(8.6) reduce the remaining signed problem to

\[
 {1\over2}\sum_{k=k_0}^{J}\omega_{k,J}Y_{2^k}
 \le O_{\mathbf a,k_0}(1)
 +\sum_{k=k_0}^{J}\omega_{k,J}\mathcal G_{2^k},
\tag{8.7}
\]

where

\[
 \boxed{
 \mathcal G_n=
 R_n+P_n^{\rm coef}\log A-K_n^{\rm int}-\mathcal T_n
 -\Theta_n^{\rm full}-{1\over4}\mathcal D_n^{\rm pre}.}
\tag{8.8}
\]

Here

\[
 R_n=\sum_{i=1}^{n-2}\left({n-i\over2n}\right)^2
       \sum_{j\ge n}C_{ij},
 \qquad
 P_n^{\rm coef}={3(n-1)^2\over4n^2},
 \qquad A=a_{2n-1}.
\]

The smallest exact sufficient target is

\[
 \boxed{
 \limsup_{J\to\infty}
 {\sum_{k=k_0}^{J}\omega_{k,J}\mathcal G_{2^k}\over\log J}
 <{1\over3072C\log2}.}
\tag{8.9}
\]

A cleaner stronger target is

\[
 \sum_{k=k_0}^{J}\omega_{k,J}(\mathcal G_{2^k})_+
 =o_{C,\mathbf a}(\log J).
\tag{8.10}
\]

Neither (8.9) nor (8.10) is proved here.  The old `Dpre`, `Y`, and `W`
payments cannot simply be counted again; (8.7)--(8.8) are the signed
starting point for the next attack.

## 9. Two coefficient obstructions that remain

### 9.1 Natural transport leaves half of `W_n`

On the inner support of `W_n`, every natural short-row quotient is below
`1/2`.  Therefore

\[
 \overline S_n\big|_{W_n}<{1\over2}W_n,
 \qquad
 W_n-\overline S_n\big|_{W_n}>{1\over2}W_n.
\tag{9.1}
\]

On a hypothetical eventual-`C` branch, the known `W_n` floor makes the
Fejér liminf of the right side at least
`1/(3072 C log 2)`, exactly the old strict threshold.  Thus the natural
coefficient allocation alone cannot finish the proof.  This does not rule
out cancellation inside the signed quantity `G_n`.

### 9.2 No feasible transport covers uniformly above `1/3`

Consider the inner atom `C_(2n-4,2n-1)`.  Its full `W_n` coefficient is

\[
 {9\over4n^2}.
\]

Only rows `p=2n-3,2n-2` can contribute.  Their complete row demands are

\[
 \bar r_{n,2n-3}+\bar r_{n,2n-2}
 ={3\over8n^2}+{3\over8n^2}
 ={3\over4n^2}.
\]

Hence every feasible transport in (7.1), regardless of how it redistributes
each row, has coefficient ratio at this atom at most

\[
 {3/(4n^2)\over9/(4n^2)}={1\over3}.
\tag{9.2}
\]

Thus uniform coverage strictly above `1/3` is impossible.  Finite linear
programs suggest `1/3` may be attainable, but no all-`n` attainment theorem
is claimed or used.

## 10. Reproducible certificate and exact status

Artifacts:

- `wave19_p28_adaptive_row_cap_certificate.py`;
- `test_wave19_p28_adaptive_row_cap_certificate.py`;
- `wave19_p28_adaptive_row_cap_certificate_2026-08-29.json`.

The certificate uses exact `Fraction` arithmetic for the proof comparisons,
rational atanh/Taylor intervals for the transcendental constants, and
high-precision decimals only for the displayed finite cap profiles.  It
audits the coefficient theorem at
`n=4,5,8,16,32,64,128`, including every finite atom at those epochs.

The exact result is therefore:

- adaptive cap capacity: **proved and paid from target epoch 2048**;
- natural full-row `Sbar<=Y/2`: **proved**;
- natural endpoint `E0<=3Dpre/4`: **proved**;
- endpoint-free actual-rank split: **invalid**;
- uniform inner transport above `1/3`: **impossible**;
- signed Fejér bounds (8.9)/(8.10): **open**;
- P28 and Erdős #1191: **open**;
- prize claim: **not ready**.
