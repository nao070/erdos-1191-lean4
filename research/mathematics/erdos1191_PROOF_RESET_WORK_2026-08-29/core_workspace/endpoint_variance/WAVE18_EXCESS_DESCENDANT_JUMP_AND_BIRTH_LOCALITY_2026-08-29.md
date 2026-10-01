# Wave 18: exact excess insertion, descendant jumps, and birth locality

Date: 2026-08-29 (Asia/Tokyo)  
Status: **P22 is partially closed; the birth-time/descendant-jump theorem P23 and Erdős #1191 remain open**

## 1. Claim boundary

This note makes the Wave 17 residual promotion sign-faithful.  It proves an
exact local carrier inequality, inserts the capped and uncapped pieces into
the Wave 16 terminal identity, and leaves one named positive functional.  It
also proves an all-source rank-layer source-multiplicity estimate and three no-go theorems
which show why local or rank-only repairs cannot finish the argument.

Nothing below proves the required tapered bound for the remaining functional,
constructs an infinite critical Golomb ruler, resolves Question 1 or 2, or
supports a prize claim.

## 2. Notation and exact coefficient capacity

For `2<=p<=n`, set

```text
d_(n,p)=D_(p,2n-1),
L_(n,p)=binom(2n-p+1,2),
Pi_(n,p)=log(rho_infinity(d_(n,p))/rho_(2n)(d_(n,p))),
r_(n,p)=(4n-2p-3)/(8n^2).
```

For a fixed height `h>0`, write

```text
Theta_n^[h]=sum_(p=2)^n r_(n,p)min(Pi_(n,p),h),
Theta_n^(exc,h)=sum_(p=2)^n r_(n,p)(Pi_(n,p)-h)_+.
```

The coefficient mass telescopes to

```text
R_n=sum_(p=2)^n r_(n,p)
   =(n-1)(3n-5)/(8n^2)<3/8.                 (2.1)
```

The target Gothic interior `mathfrak B_n` contains atoms `D_(p,q)` for
`n<=q<=2n-2`, `2<=p<=q`, with

```text
beta_(n,p,q)=1/(2n^2),  p<=q-2,
             1/(4n^2),  p=q-1,
             1/n^2,     p=q.                (2.2)
```

There are

```text
c_n=(n-1)(3n-4)/2                          (2.3)
```

such atoms.  Restrict to the disjoint rectangle `2<=p<=n` and
`n<=q<=2n-2`, and put

```text
w_(n,p)=sum_(q=n)^(2n-2) beta_(n,p,q).
```

The exact rows are

```text
w_(n,p)=(n-1)/(2n^2),    2<=p<=n-2,
         (2n-3)/(4n^2),  p=n-1,
         (2n-1)/(4n^2),  p=n.               (2.4)
```

Subtracting `r_(n,p)` gives respectively

```text
(2p-1)/(8n^2), (2n-5)/(8n^2), (2n+1)/(8n^2),
```

so every row has enough literal coefficient capacity:

```text
w_(n,p)>=r_(n,p).                            (2.5)
```

## 3. The local slack lemma

**Lemma 3.1 [RIGOROUS — SELF-CONTAINED].** Let

```text
H_n^loc=mathfrak B_n-F_n^(loc,int)>=0.
```

For every subset `S` of interior atoms,

```text
H_n^loc >= sum_((p,q) in S)
 beta_(n,p,q) log_+(D_(p,q)/c_n).            (3.1)
```

**Proof.** Sort the actual atom values as
`x_1<...<x_(c_n)` and carry their coefficients `gamma_j`.  Positive integer
distinctness gives `x_j>=j`.  The rearrangement defining
`F_n^(loc,int)` is the minimum pairing of the decreasing coefficient
multiset with the increasing ranks.  Therefore

```text
H_n^loc
 =sum_j gamma_j log(x_j/j)
  +[sum_j gamma_j log j-F_n^(loc,int)],
```

and both displayed terms are nonnegative.  If an atom in `S` has value
above `c_n`, its first summand is at least
`beta log(D/c_n)`; otherwise its right-hand contribution in (3.1) is zero.
Summing proves the lemma.  `square`

## 4. Exact descendant-jump residual

Integer rank bounds give

```text
rho_infinity(d_(n,p))<=d_(n,p),
rho_(2n)(d_(n,p))>=L_(n,p),
```

and hence

```text
(Pi_(n,p)-h)_+
 <=log_+(d_(n,p)/(exp(h)L_(n,p))).           (4.1)
```

For positive `x,y`, `log_+x<=log_+y+log_+(x/y)`.  In (4.1), average this
inequality over the row (2.4), with

```text
y=D_(p,q)/c_n.
```

Multiply by `r_(n,p)`, use (2.5), and then apply Lemma 3.1.  This proves

```text
Theta_n^(exc,h)<=H_n^loc+J_n^(h),            (4.2)
```

where the only residual is

```text
J_n^(h)=sum_(p=2)^n [r_(n,p)/w_(n,p)]
 sum_(q=n)^(2n-2) beta_(n,p,q)
 log_+(d_(n,p)c_n/
        (exp(h)L_(n,p)D_(p,q))).             (4.3)
```

Every `(p,q)` atom is used at most once.  Since

```text
c_n/L_(n,p)<3,                               (4.4)
```

a nonzero term of `J_n^(h)` requires

```text
d_(n,p)/D_(p,q)>exp(h)/3.                    (4.5)
```

Thus the missing functional is not a generic rank loss: it records a large
jump from an interior descendant to its common terminal ancestor.

## 5. Raising the cap and inserting the whole residual

Wave 17 proved

```text
D_n=F_n^(loc,int)-K_n^int ->
delta_0=3/2+(3/4)log3-2log2
       =0.937664855381...>15/16.             (5.1)
```

Choose `h=5/2` and restrict from now on to sufficiently large dyadic `n`, so
that `n/2` is the preceding source epoch and (5.1) is above `15/16`.  From
(2.1),

```text
Theta_s^[5/2] <=(5/2)R_s<15/16<D_(2s).       (5.2)
```

This index alignment is mandatory.  In the epoch-`n` identity, `D_n` pays
the cap from source epoch `n/2`, not the current cap.  Define

```text
U_n=D_n-Theta_(n/2)^[5/2]>=0,
Q_n=H_n^loc+J_n^(5/2)-Theta_n^(exc,5/2)>=0. (5.3)
```

Using `mathfrak B_n=K_n^int+D_n+H_n^loc` in the exact Wave 16 formula gives

```text
Z_n-R_(2n)
 =mathfrak P_n-K_n^int-mathcal T_n
  -Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)
  +J_n^(5/2)-(U_n+Q_n),                      (5.4)
mathcal T_n>=0.
```

Equation (5.4) retains all endpoint and descendant terms and has no hidden
positive-to-negative sign reversal.  For

```text
omega_(k,J)=((J+1-k)/(J+1))^2,
```

the exact one-step reindexing error is

```text
E_J=sum_(k=k0)^(J-1)(omega_(k,J)-omega_(k+1,J))
       Theta_(2^k)^[5/2]
    +omega_(J,J)Theta_(2^J)^[5/2]<15/16,     (5.5)
```

because the coefficient sum is `omega_(k0,J)<1`; the initial previous-source
cap has the favorable sign and may be dropped.  Therefore the entire current
residual promotion has entered the
signed dyadic ledger, up to `J_n^(5/2)` and a bounded horizon term.

## 6. Exact all-source rank-layer allocation

**Lemma 6.1 [RIGOROUS — SELF-CONTAINED].** Put

```text
R_(m,p)=rho_(2m)(d_(m,p)),
Q_(m,p)=rho_infinity(d_(m,p)).
```

For any `h>0`, assign the future numerical differences counted between
these two ranks, in their rank order, to unit rank intervals.  Then

```text
(log(Q/R)-h)_+
 =1_(Q>exp(h)R) integral_(exp(h)R)^Q dt/t,  (6.1)
```

so a single assigned rank slot has load at most `1/(exp(h)R)`.

With `ell=2m-p`,

```text
r_(m,p)=(2ell-3)/(8m^2),
R_(m,p)>=ell(ell+1)/2.
```

Consequently the total load which one future difference can receive from
source epoch `m` obeys

```text
lambda_m^(exc,h)(x)
 <=exp(-h) sum_(ell=m)^(2m-2)
      (2ell-3)/(4m^2 ell(ell+1))
 <log(2)/(2exp(h)m^2).                       (6.2)
```

Fix a cap-onset index `n_0` and define

```text
E_x={dyadic m>=4: 2m-1>=n_0, x notin Delta_(2m),
                    and x<=d_(m,p) for some 2<=p<=m}.
```

If `E_x` is empty set `Lambda^(exc,h)(x)=0`; otherwise put
`m_*(x)=min E_x`.  A nonzero assigned load can arise only from `E_x`.
Summing (6.2) over the containing dyadic tail gives

```text
Lambda^(exc,h)(x)
 <2log(2)/(3exp(h)m_*(x)^2).                 (6.3)
```

Eligibility and the cap give

```text
x<4C m_*(x)^2 log(4m_*(x)).                 (6.4)
```

If `m_*(x)<=x`, (6.4) gives
`m_*^(-2)<4C log(4x)/x`; if `m_*(x)>x`, the same comparison holds for all
sufficiently large `x` because `m_*^(-2)<x^(-2)` and
`4Cx log(4x)>=1`.  Hence

```text
Lambda^(exc,h)(x)
 <[8C log(2)/(3exp(h))]log(4x)/x             (6.5)
```

eventually.  Pre-cap source epochs have finite aggregate excess mass and are
eligible for only finitely many `x`, so they disappear from the displayed
large-`x` pointwise estimate.  This proves the all-source rank-layer
multiplicity estimate, including at `h=5/2`; authenticated reuse of unused
signed carrier capacity remains open.

## 7. Why birth locality is the remaining issue

Let `x=a_j-a_i` be eligible for an earlier source and choose its dyadic birth
epoch `n<=j<2n`.  Eligibility forces `i>=1`: if `i=0`, then
`x=a_j>a_(2m-1)>=d_(m,p)`, contradicting `x<=d_(m,p)`.  If `j<=2n-2`, then
`x` is therefore a literal interior bulk atom with coefficient at least
`1/(4n^2)`.  If the complete raw carrier were unused, (6.5) and
`log(4x)<=2log x` would be paid by the sufficient condition

```text
n^2 <=[3exp(h)/(64C log2)]x.                 (7.1)
```

At the operative `h=5/2`, no theorem currently supplies (7.1).  The cap
controls `x` from above by its birth index, not that index from above by
`x`.  Pointwise rank stabilization for a fixed integer is not uniform for
a moving family of future differences.

Also, the raw atom value is not free: the sorted-rank floor has already spent
part of it.  The authenticated carrier is a rank residual such as
`beta log(x/L_s)`, which may be arbitrarily small.  A terminal birth
`j=2n-1` is not in the interior rectangle and must be paid through the
endpoint/renewal identity.

Write the dyadic epochs as `m_k=2^k`, let `q_(k,x)` denote source-scale load,
and define the birth-scale index
`b(x)=min{j:x in Delta_(2^(j+1))}`.  The exact Fejér weight mismatch is

```text
sum_x [sum_(k<=J,b(x)<=J)
          (omega_(k,J)-omega_(b(x),J))q_(k,x)
       +sum_(k<=J,b(x)>J)omega_(k,J)q_(k,x)]. (7.2)
```

For `b(x)<=J`,

```text
omega_(k,J)-omega_(b(x),J)
 =(b(x)-k)(2J+2-k-b(x))/(J+1)^2
 <=2(b(x)-k)/(J+1).
```

Thus an `o(log J)` birth-delay moment with the harmless factor two is a
sufficient target, together with authenticated nonterminal slack and
terminal renewal capacity.  The scalar cap does not presently imply it.

## 8. Exact no-go theorems

### 8.1 Rank-and-cap information alone

Let `N=binom(2m,2)`, choose an integer `K>exp(h)`, and define the abstract
rank model

```text
S_(2m)={K,2K,...,NK}, S_infinity={1,2,3,...},
d_(m,p)=K L_(m,p).
```

Then the finite and infinite ranks are exactly `L_(m,p)` and `d_(m,p)`, so

```text
Theta_m^(exc,h)=R_m(log K-h).                (8.1)
```

For `K` of order `C log m`, (8.1) has leading size
`(3/8)log log m`.  This model satisfies the abstract rank inequalities but
is not claimed to be the difference spectrum of one compatible Golomb
tower.  It precisely refutes attempts using only rank monotonicity and the
scalar cap.

### 8.2 One-epoch Golomb slack can remain bounded

For every odd prime `p`, set `n=(p+1)/2` and

```text
a_i=2pi+(i^2 mod p), 0<=i<p.                 (8.2)
```

This is a strictly increasing ordinary integer Golomb ruler, since
`a_(i+1)-a_i>=2p-(p-1)=p+1`.  Indeed, in an equality of two positive
differences, the difference between the two residue corrections has absolute
value at most `2(p-1)<2p`; this first forces equal index gaps.  Reducing
modulo `p` then gives
`2s(i-k)=0 mod p`, and hence the two pairs coincide.  Its diameter is

```text
a_(p-1)=2p(p-1)+1<2p^2<8n^2.                (8.3)
```

The total local bulk coefficient mass is

```text
M_n=3(n-1)^2/(4n^2),
```

so (8.3) gives `mathfrak B_n<=M_n log(8n^2)`.  Wave 17's exact floor has

```text
F_n^(loc,int)
 =(3/2)log n+(3/4)log(3/2)-3/4+o(1).
```

Therefore, as `p` tends to infinity through odd primes and hence along a
family of different finite rulers,

```text
limsup H_n^loc
 <=(3/4)(1+log(16/3))=2.00548... .          (8.4)
```

Thus complete one-epoch Golomb distinctness and quadratic diameter do not
force enough growing slack.  The rulers (8.2) are not nested; the surviving
route must use single-branch cross-epoch compatibility.

### 8.3 Terminal identity without the cap

Fix a core `A^0={a_0,...,a_(2n-2)}` and a finite Golomb block
`B={0=b_0<...<b_K}`.  Choose `Q>diam(A^0)` and form

```text
A^0 union (X+QB).
```

Here `X=X+Qb_0` is the new terminal mark `a_(2n-1)`.  Choose an arbitrarily
large admissible `X` such that
`Qb_K<min_(2<=p<=n)(X-a_(p-1))`.  The inequality `Q>diam(A^0)` rules out
`X`-independent cross-cross collisions; cross/internal and cross/core
collisions exclude only finitely many translations.  Then extend the result
superincreasingly.

The local `H_n^loc,D_n` stay fixed and `mathcal T_n(X)->0`, while the block
contributes `K(K+1)/2` new future differences below every suffix threshold.
The promotion excess is therefore arbitrarily large.  This refutes any
unconditional terminal-identity-only upper.  The extension is supercritical,
so it does not refute a theorem which uses the eventual-`C` cap.

## 9. Midpoint-jump reduction and sharp one-epoch boundary

### 9.1 Exact q-collapse

**[RIGOROUS — SELF-CONTAINED]** Since `q>=n` implies
`D_(p,q)>=D_(p,n)`, while `c_n/L_(n,p)<3`, each row of (4.3) gives

```text
J_n^(h)
 <=M_n^(h)
 :=sum_(p=2)^n r_(n,p)
   [log(d_(n,p)/D_(p,n))-(h-log3)]_+.        (9.1)
```

At `h=5/2`, the threshold is

```text
h-log3=1.4013877...=log4+0.0150933... .      (9.2)
```

Thus the two-dimensional descendant remainder reduces rigorously to positive
dyadic growth of a moving-left midpoint-to-terminal ratio.  This simplifies
P23, but taking the positive part destroys ordinary endpoint telescoping.

### 9.2 Scalar positive-part telescoping is insufficient

Let `A_k=4^k exp(s_k)`, with `s_(2j)=0`, `s_(2j+1)=eta`, and at
`h=5/2` choose

```text
h-log12<eta<log4
```

(for example `eta=1`).  Then `A_k` is increasing, has a quadratic dyadic
envelope, and

```text
[log(A_(k+1)/A_k)-(h-log3)]_+
```

is a fixed positive constant on every even-to-odd step and zero on every
return step.  Its Fejér sum is `Theta(J)`.  This is a scalar real model, not
a Golomb construction.  It proves that the terminal telescope and scalar cap
cannot control (9.1) after positive parts are taken.

### 9.3 An actual finite Golomb prefix attains the log-log one-epoch size

Take an odd prime `p=2n-1` and the Erdős--Turán core (8.2).  Its exact
diameter is

```text
H=8n^2-12n+5.
```

Append the integer terminal mark

```text
X=floor(C(2n-1)^2 log(4n-2)).
```

For every fixed `C>0` and all sufficiently large prime rows, `X>2H`.
The append is automatically Golomb: old differences are at most `H`, all new
differences are greater than `H`, and two new differences are equal only when
their old endpoints coincide.

All descendants `D_(p,q)` in (4.3) lie in the core and are at most `H`, while
`d_(n,p)>=X-H`.  For `n>=4`, the ratio needed here is the lower bound

```text
c_n/L_(n,p)>=c_n/L_(n,2)
             =(3n-4)/(4n-2)>1/2.            (9.3)
```

Therefore, once its logarithm is positive,

```text
J_n^(h)>=R_n log((X-H)/(2exp(h)H))
        =(3/8-o(1))log log n+O_(C,h)(1).     (9.4)
```

The same core has bounded `H_n^loc`, and the terminal potential tends to zero
as `X/H` grows.  These are terminal-cap-compatible one-epoch finite prefixes,
not one compatible eventual-`C` branch: their varying early core coordinates
need not obey one fixed all-prefix cap.  Thus (9.4) does not refute P23.  It
does prove that one-epoch Golomb uniqueness, local slack, the terminal
identity, and a cap at the terminal index cannot improve the
`O_C(log log n)` envelope.

## 10. Exact next theorem — P23

The moving band `n/2<p<=n` has residual mass

```text
sum_(p=n/2+1)^n r_(n,p)=5/32-1/(4n),
```

so a fixed-left-index telescope cannot remove the renewal.  Elementary cap
bounds yield only `J_n^(5/2)=O_C(log log n)` per epoch, which is too large.

The primary next lemma is

```text
sum_(k<=J) omega_(k,J)J_(2^k)^(5/2)=o_C(log J),
```

on one fixed infinite normalized integer Golomb ruler satisfying the
eventual-`C` envelope, or an exact signed cancellation of this functional
against `mathfrak P_n-K_n^int-mathcal T_n`.  The proof must account for
birth delay, unused carrier capacity, terminal births, and moving-band
renewal without reusing any atom already spent by the local rank floor.

## 11. Computational audit boundary

The companion generator, tests, and dated JSON audit exact formulas in
Sections 2, 5, 6, and finite rows of Section 8.2.  They do not prove an
`o(log J)` bound for (7.2), P23, an infinite branch, either Erdős question,
publication novelty, or a prize claim.
