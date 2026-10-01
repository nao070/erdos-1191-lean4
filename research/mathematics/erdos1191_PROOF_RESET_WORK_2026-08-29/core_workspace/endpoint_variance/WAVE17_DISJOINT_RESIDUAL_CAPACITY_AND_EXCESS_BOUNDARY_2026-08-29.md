# Wave 17: disjoint residual capacity and the promotion-excess boundary

Date: 2026-08-29 (Asia/Tokyo)  
Status: **the local P21 capacity-overlap gate is solved; P19 and Erdős #1191 remain open**

## 1. Purpose and claim boundary

Wave 15 put the adjacent promotion `Delta_m` into literal atoms of the next
Gothic interior bulk `mathfrak B_(2m)`, but spent each selected atom's whole
value.  Wave 16 repaired the terminal horizon and upgraded future promotion
to constant size, leaving one precise question: can an existing triangular
floor and a positive promotion premium be paid by one bulk without counting
the same capacity twice?

This note answers that local question affirmatively in two independent ways:

1. a same-atom diameter residual pays an explicit positive fraction of
   `Delta_m`, with a dyadically summable error;
2. a stronger within-epoch rank rearrangement leaves an eventual constant
   surplus over the triangular floor and pays either `3 Delta_m/8` or the
   residual `u-v` promotion truncated at height two.

Neither statement is a signed global upper.  The promotion excess above the
fixed truncation, together with the remaining endpoint/descendant residual,
is not controlled here.  No contradiction, infinite critical construction,
answer to Question 1 or 2, or prize claim follows from this note alone.

## 2. Notation

At source epoch `m`, put

```text
d_p=D_(p,2m-1),
r_p=rho_(2m)(d_p),
K_p=rho_(4m-1)(d_p)-rho_(2m)(d_p),
u_(m,p)=(12m-5-6p)/(16m^2),       2<=p<=m,
Delta_m=sum_p u_(m,p) log(1+K_p/r_p).
```

Every new numerical difference `x<=d_p` counted by `K_p` is uniquely
`x=a_j-a_i` with `2m<=j<=4m-2` and `i>=1`.  Hence

```text
x=D_(i+1,j)
```

is a literal interior atom of `mathfrak B_(2m)`.  If `s=j-i` is its number of
gaps and `L_s=binom(s+1,2)`, its Gothic coefficient is

```text
beta_x = 1/(4m^2)   for s=1,
         1/(16m^2)  for s=2,
         1/(8m^2)   for s>=3.
```

The Wave 11 interior triangular floor spends exactly
`beta_x log L_s` on this same atom.  Its unused same-atom value is therefore

```text
beta_x log(x/L_s).
```

## 3. A uniform local diameter premium

### Lemma 3.1

Let `b_0<...<b_(n-1)` be consecutive marks cut from an integer Golomb ruler,
let `s=n-1`, and let `x=b_(n-1)-b_0`.  If `x>=2147`, then

```text
x/L_s >= 3/2.
```

For `n>=55`, collect all interval differences of gap lengths at most ten.
There are

```text
N=sum_(h=1)^10 (n-h)=10n-55
```

distinct positive integers.  Their sum is at least `N(N+1)/2`.  Every gap is
used at most `1+...+10=55` times, so their sum is at most `55x`.  Thus

```text
x >= N(N+1)/110.
```

The desired comparison is equivalent to

```text
35n^2-2015n+5940 >= 0,
```

which holds at `n=55` and increases thereafter.  For `n<=54`, use
`L_s<=binom(54,2)=1431` and `2147>(3/2)1431`.  This proves the lemma.

### Theorem 3.2: conservative independently audited form

**[RIGOROUS — SELF-CONTAINED]**

Set

```text
c_0=log(3/2)/12,
E_m=2146 log(3/2)/(16m^2).
```

Then every finite integer Golomb ruler containing the required prefixes obeys

```text
mathfrak B_(2m) >= K_(2m)^int + c_0 Delta_m - E_m.
```

Indeed, the exact Wave 15 layer load on a selected new difference is bounded
by

```text
lambda_m(x)<3/(4m^2),
Delta_m<=sum_x lambda_m(x).
```

For `x>=2147`, Lemma 3.1 and the three coefficient cases give at least
`log(3/2)/(16m^2)>c_0 lambda_m(x)` of unused triangular residual.  There are
at most 2146 distinct positive values below 2147.  Discarding their loads
costs at most `E_m`.  Summing the remaining same-atom residuals proves the
inequality.  The error is summable over dyadic `m`.

Retaining `sum_(ell=m)^(2m-2)1/(ell+1)<log2` and the sharper coefficient case
analysis improves the constants to

```text
c_0=log(3/2)/(6log2),
E_m=2146 log(3/2)/(8m^2),
```

but the conservative form already proves a genuine disjoint premium.

## 4. A stronger local rank floor

**[RIGOROUS — SELF-CONTAINED]**

Now write `n` for the target epoch.  The interior Gothic coefficient multiset
has

```text
n-1                         atoms of weight 1/n^2,
(n-1)(3n-8)/2               atoms of weight 1/(2n^2),
n-1                         atoms of weight 1/(4n^2).
```

Put

```text
a=n-1,
b=3(n-1)(n-2)/2,
c=(n-1)(3n-4)/2.
```

All corresponding numerical differences are distinct positive integers.
Sorting the weights decreasingly and pairing them with `log1,...,log c`
therefore gives the valid within-epoch floor

```text
F_n^(loc,int)=[2log(a!)+log(b!)+log(c!)]/(4n^2),
mathfrak B_n>=F_n^(loc,int).
```

The triangular floor on exactly the same atom set is

```text
K_n^int = ((n-1)/(4n^2))log3
 + (1/(2n^2))[
     (n-1) sum_(ell=3)^(n-1) log L_ell
     +sum_(ell=n)^(2n-3)(2n-ell-2)log L_ell
   ].
```

Let `D_n=F_n^(loc,int)-K_n^int`.  The elementary bounds

```text
N(log N-1)+1 <= log(N!)
             <= N(log N-1)+1+log N
```

give

```text
F_n^(loc,int)
 = (3/2)log n+(3/4)log(3/2)-3/4+o(1).
|F_n^(loc,int)-[(3/2)log n+(3/4)log(3/2)-3/4]|
 <=6(1+log n)/n.
```

For `K_n^int`, scale `ell=nx`.  The two triangular ranges give the Riemann
integral

```text
(1/2) integral_0^1 log(x^2/2) dx
 +(1/2) integral_1^2 (2-x)log(x^2/2) dx
 = (5/4)log2-9/4.
```

Hence

```text
D_n -> delta_0
     =3/2+(3/4)log3-2log2
     =0.937664855381... .
|D_n-delta_0|<=18(1+log n)/n
                <=20(1+log n)/sqrt(n)  for n>=16.
```

Here is a constant-tracked derivation of the error term.  Put `L=log n`,

```text
q_b=b/n^2=3/2-9/(2n)+3/n^2,
q_c=c/n^2=3/2-7/(2n)+2/n^2,
H(q)=q(2L+log q-1).
```

Since `H'(q)=2L+log q` and
`|q_b-3/2|+|q_c-3/2|<=8/n`, the two large factorial
perturbations, the `a=n-1` term, and the factorial remainders in the
elementary bounds above give

```text
|F_n^(loc,int)-[(3/2)L+(3/4)log(3/2)-3/4]|
 <=6(1+L)/n.
```

For the triangular floor set

```text
f(x)=2log x-log2,
w(x)=1/2                 for 0<x<=1,
     =(2-x)/2            for 1<=x<=2,
M=(n-1)(3n-7)/(4n^2).
```

After writing
`log L_ell=2L+f(ell/n)+log(1+1/ell)`, the exact sum has the form
`K_n^int=2ML+S+R`.  Compare `S` with

```text
Q=(1/n)sum_(ell=1)^(n-1) f(ell/n)/2
 +(1/n)sum_(ell=n)^(2n-1) w(ell/n)f(ell/n).
```

The missing `ell=1`, exceptional `ell=2`, and exact coefficient offsets give
`|S-Q|<=3(1+L)/n`.  Applying the same factorial bounds to the first sum and
using `|(wf)'|<=1+(log2)/2<1.35` on `[1,2]` gives
`|Q-integral_0^2 wf|<=3(1+L)/n`.  Finally,

```text
|2ML-(3/2)L|<=5L/n,
0<=R<= (1+L)/n
```

by `log(1+1/ell)<=1/ell`.  These inequalities yield the displayed
`12(1+L)/n` error for `K_n^int` and hence the `18(1+L)/n` error for `D_n`.

In particular, direct substitution in the weaker displayed error bound gives

```text
D_n>81/128 for n>=2^20,
D_n>3/4    for n>=2^22.
```

The error majorant is decreasing on these ranges.  This conclusion uses only
the deterministic coefficient multiset and integer distinctness; it does not
assume an eventual critical branch.

Wave 15 also gives

```text
Delta_m < ((m-1)(9m-11)/(16m^2))log13
        < (9/16)log13.
```

Since `log13<3`, for `2m>=2^20`

```text
boxed: mathfrak B_(2m)>=K_(2m)^int+(3/8)Delta_m.
```

This is one stronger rearrangement floor for one atom set, not the illegal
sum of two independently spent copies of `mathfrak B_(2m)`.

With Fejer weights, the one-step reindexing changes the displayed premium by
only `O(1)`, because `Delta_m` is uniformly bounded and
`sum_k(omega_(k,J)-omega_(k+1,J))<=1`.  Thus the local weighted and
unweighted capacity statement requested in P21 is complete when the chosen
existing floor is the triangular length floor.  It must not be added again
to `K^mix` or another interior rearrangement floor.

## 5. The capped residual `u-v` promotion

**[RIGOROUS — SELF-CONTAINED]**

For the Wave 14 residual coefficient, put

```text
r_(m,p)=u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2),
P_(m,p)=log(rho_infinity(d_p)/rho_(2m)(d_p)).
```

Its exact macroscopic mass is

```text
sum_(p=2)^m r_(m,p)=(m-1)(3m-5)/(8m^2)<3/8.
```

Define

```text
Theta_m^[2]=sum_(p=2)^m r_(m,p) min(P_(m,p),2),
Theta_m^exc=sum_(p=2)^m r_(m,p)(P_(m,p)-2)_+.
```

Then `Theta_m^[2]<3/4`.  Since `D_(2m)>3/4` for `2m>=2^22`,

```text
mathfrak B_(2m)>=K_(2m)^int+Theta_m^[2]
```

eventually.  The lower shell is disjoint from the Gothic interior, so the
legal Wave 14 `v`-weighted rebate may be included simultaneously:

```text
A_(2m)>=K_(2m)^len+Phi_m+Theta_m^[2].
```

Wave 16 gives `P_(m,p)>=kappa_C` uniformly on the macroscopic suffix, hence

```text
Theta_m^[2] >= (1/3)min(kappa_C,2)
```

eventually.  A constant portion of the formerly unallocated residual
promotion therefore has a genuinely disjoint carrier.

## 6. The exact obstruction now exposed

**[CONDITIONAL]** The following is the remaining target, not a proved
repayment theorem.

The capped theorem does not pay

```text
Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+.
```

The available general estimate remains `O_C(log log m)` per epoch because
`rho_(2m)(d_p)>=binom(m+1,2)`, `rho_infinity(d_p)<=d_p`, and the eventual cap
allows `d_p=O_C(m^2 log m)`.  Fejer weights alone therefore do not make the
dyadic sum of this excess `o(log J)`.

Let

```text
H_n^loc=mathfrak B_n-F_n^(loc,int)>=0.
```

The smallest surviving capacity question is whether the actual local slack,
the unused part of `D_n`, and the exact renewal terms can pay
`Theta_m^exc` with bounded reuse.  A falsifiable weighted subtarget is to
control

```text
sum_k omega_(k,J) Theta_(m_k)^exc
```

by the next-epoch quantities

```text
H_(m_(k+1))^loc + D_(m_(k+1)) - Theta_(m_k)^[2]
```

up to `o(log J)`, and then insert that comparison into the full terminal
identity

```text
Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m,
mathcal T_m>=0.
```

The endpoint/descendant residual must remain in that final audit.  Merely
lower-bounding the already nonnegative bulk surplus, even harmonically, does
not give a signed upper and does not contradict the Wave 13 lower bound.

## 7. Exact status

Wave 17 proves that the former coefficient-capacity overlap is not the final
barrier.  A same-atom residual pays a fixed fraction of `Delta_m`, and the
stronger local-rank surplus pays a constant capped portion of the residual
`u-v` promotion.  The remaining object is the unbounded promotion excess
coupled to the exact endpoint/descendant renewal residual.

P15, P17, P18, P19, the resulting excess-control obligation, Questions 1 and
2, and the prize claim remain open.
