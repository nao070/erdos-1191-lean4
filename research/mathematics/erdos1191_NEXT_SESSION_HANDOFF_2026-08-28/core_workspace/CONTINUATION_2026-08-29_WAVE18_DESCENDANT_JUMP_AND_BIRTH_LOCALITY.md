# Erdős Problem #1191 — Wave 18 descendant-jump continuation

Date: 2026-08-29 (Asia/Tokyo)  
Canonical root: `core_workspace/`  
Claim status: **Questions 1 and 2 remain open; no prize claim is ready**

## 1. What Wave 18 changes

Wave 18 makes two rigorous advances beyond Wave 17.

1. It inserts the entire residual future-rank promotion into the exact signed
   Wave 16 identity, except for one explicit nonnegative descendant-jump
   functional `J_n^(5/2)`.  The insertion uses one local rank floor once;
   it does not add overlapping lower bounds.
2. It decomposes the uncapped promotion into future numerical-difference rank
   layers and proves a summable all-source reuse bound for every fixed future
   difference.  Thus scalar rank-layer source reuse is bounded; authenticated
   reuse of unused signed carrier capacity remains part of the obstruction.

The remaining obstruction is temporal: a future difference may be born much
later than the source epoch, and the current hypotheses do not provide a
uniform relation between its value and its birth scale or authenticate enough
unused capacity at that carrier.  The new primary obligation P23 is therefore
a birth-time Carleson/renewal estimate for `J_n^(5/2)` (or an equivalent signed
cancellation).  Wave 18 does not prove P19, P23, or either Erdős question.

## 2. Exact signed insertion

**[RIGOROUS — SELF-CONTAINED]**

For `2<=p<=n`, put

```text
d_(n,p)=D_(p,2n-1),
L_(n,p)=binom(2n-p+1,2),
Pi_(n,p)=log(rho_infinity(d_(n,p))/rho_(2n)(d_(n,p))),
r_(n,p)=(4n-2p-3)/(8n^2).
```

For `h>0`, split the residual promotion as

```text
Theta_n^[h]=sum_p r_(n,p) min(Pi_(n,p),h),
Theta_n^(exc,h)=sum_p r_(n,p)(Pi_(n,p)-h)_+.
```

The exact residual mass is

```text
R_n=sum_p r_(n,p)=(n-1)(3n-5)/(8n^2)<3/8.
```

The target-epoch Gothic interior contains the disjoint atoms `D_(p,q)`,
`2<=p<=n` and `n<=q<=2n-2`, with coefficients

```text
beta_(n,p,q)=1/(2n^2)  if p<=q-2,
             1/(4n^2)  if p=q-1,
             1/n^2     if p=q.
```

Let `c_n=(n-1)(3n-4)/2` be the total number of interior atoms and

```text
w_(n,p)=sum_(q=n)^(2n-2) beta_(n,p,q).
```

Direct evaluation gives `w_(n,p)>=r_(n,p)` in all three boundary cases.
If `H_n^loc=mathfrak B_n-F_n^(loc,int)`, the exact sorted-rank floor implies

```text
H_n^loc >= sum_(p,q) beta_(n,p,q) log_+(D_(p,q)/c_n)
```

on this selected disjoint atom set.  Since
`rho_infinity(d)<=d`, `rho_(2n)(d)>=L_(n,p)`, and
`log_+(xy)<=log_+x+log_+y`, averaging separately for each `p` proves

```text
Theta_n^(exc,h) <= H_n^loc+J_n^(h),
```

where

```text
J_n^(h)=sum_(p=2)^n [r_(n,p)/w_(n,p)]
 sum_(q=n)^(2n-2) beta_(n,p,q)
 log_+(d_(n,p)c_n/(exp(h)L_(n,p)D_(p,q))).
```

There is no atom reuse in this inequality.  Moreover `c_n/L_(n,p)<3`, so
`J_n^(h)` records only genuine descendant jumps

```text
d_(n,p)/D_(p,q)>exp(h)/3.
```

Wave 17 gives `D_n=F_n^(loc,int)-K_n^int -> delta_0`, with
`delta_0=0.937664855381...>15/16`.  Take `h=5/2`.  Eventually,

```text
Theta_s^[5/2] < 15/16 < D_(2s).
```

The shift is essential: the target epoch `n` pays the cap from source epoch
`n/2`.  Define

```text
U_n=D_n-Theta_(n/2)^[5/2]>=0,
Q_n=H_n^loc+J_n^(5/2)-Theta_n^(exc,5/2)>=0.
```

Substitution into the exact Wave 16 identity gives

```text
Z_n-R_(2n)
 = mathfrak P_n-K_n^int-mathcal T_n
   -Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)
   +J_n^(5/2)-(U_n+Q_n),
mathcal T_n>=0.
```

Thus the complete current residual promotion is inserted with the correct
sign, modulo only `J_n^(5/2)` and a bounded one-step horizon mismatch.  Under
the Wave 16 Fejér weights, reindexing the capped term costs less than `15/16`.

## 3. All-source rank-layer reuse is summable

**[RIGOROUS — SELF-CONTAINED]**

Write `R_(m,p)=rho_(2m)(d_(m,p))` and
`Q_(m,p)=rho_infinity(d_(m,p))`.  For any cap `h>0`,

```text
(log(Q/R)-h)_+
 =1_(Q>exp(h)R) integral_(exp(h)R)^Q dt/t.
```

Assign the successive future numerical differences below `d_(m,p)` to the
successive rank intervals `(R+s-1,R+s]`.  The assigned integrals add exactly
to the excess, and one rank slot receives at most `1/(exp(h)R)`.

With `ell=2m-p`,

```text
r_(m,p)=(2ell-3)/(8m^2),
R_(m,p)>=ell(ell+1)/2.
```

Consequently a fixed future difference `x` receives from one source epoch

```text
lambda_m^(exc,h)(x)<log(2)/(2 exp(h)m^2).
```

Fix the cap onset `n_0`, and let `E_x` be the dyadic `m>=4` with
`2m-1>=n_0`, `x` not yet in `Delta_(2m)`, and
`x<=d_(m,p)` for some `2<=p<=m`.  If `E_x` is empty the load is zero;
otherwise set `m_*(x)=min E_x`.  Summing the containing geometric dyadic
tail gives

```text
Lambda^(exc,h)(x)<2log(2)/(3 exp(h)m_*(x)^2).
```

Since eligibility gives

```text
x<4C m_*(x)^2 log(4m_*(x)),
```

one obtains, for all sufficiently large `x` (using
`4Cx log(4x)>=1` in the case `m_*(x)>x`),

```text
Lambda^(exc,h)(x)
 < [8C log(2)/(3 exp(h))] log(4x)/x.
```

In particular this holds at `h=5/2`.  The finitely many pre-cap source
epochs have finite aggregate excess and disappear from this eventual
pointwise bound.  The uncapped rank layer therefore has a genuine
source-multiplicity bound over all dyadic sources; signed carrier ownership
is still the P23 issue.

## 4. The remaining birth-time debt

**[OPEN — P23]**

If an earlier-source-eligible `x=a_j-a_i` is first born at the dyadic epoch
`n<=j<2n`, then `i>=1`: otherwise
`x=a_j>a_(2m-1)>=d_(m,p)`.  Hence, when `j<=2n-2`, it is a literal local
bulk atom with coefficient at least `1/(4n^2)`.  But the current
eventual-`C` hypothesis bounds values in terms
of indices; it does not bound this birth scale `n` above in terms of `x`.
Pointwise stabilization of `rho_L(x)` is not a uniform birth-locality theorem
for a moving sequence `x=x_m`.

Even granting the whole raw carrier `log x/(4n^2)`, a sufficient comparison
with the all-source load at `h=5/2` would require

```text
n^2 <= [3 exp(5/2)/(64C log 2)] x.
```

No such inequality is currently proved.  More importantly, the raw carrier
already supports `F_n^(loc,int)`; the authenticated unused amount is a local
rank residual such as `log(x/L_s)`, which has no uniform positive lower
bound.  Terminal births `j=2n-1` are outside the interior carrier and must be
handled by the exact renewal ledger.

Equivalently, write `m_k=2^k`, let `q_(k,x)` be the load sent by source
scale index `k`, and put
`b(x)=min{j:x in Delta_(2^(j+1))}`.  The exact Fejér mismatch is

```text
sum_x [sum_(k<=J,b(x)<=J)
          (omega_(k,J)-omega_(b(x),J))q_(k,x)
       +sum_(k<=J,b(x)>J)omega_(k,J)q_(k,x)].
```

Since the first weight difference is at most
`2(b(x)-k)/(J+1)`, an `o(log J)` birth-delay moment of this form, together
with authenticated unused capacity at every nonterminal carrier and the
terminal renewal debt, is sufficient.  It is not implied by the scalar cap.

The sharp current target is therefore either

```text
sum_(k<=J) omega_(k,J) J_(2^k)^(5/2)=o_C(log J),
```

or a sign-faithful cancellation of that sum against
`mathfrak P_n-K_n^int-mathcal T_n`.

## 5. Three exact no-go boundaries

**[RIGOROUS — SELF-CONTAINED]**

First, rank monotonicity and the scalar eventual cap alone cannot improve the
per-epoch leading excess bound.  An abstract rank model with

```text
S_(2m)={K,2K,...,binom(2m,2)K}, S_infinity={1,2,3,...},
d_(m,p)=K L_(m,p)
```

has the exact excess

```text
R_m(log K-h).
```

For `K` of order `C log m`, this is `(3/8)log log m+O_C(1)`.  The model is
not asserted to be a compatible Golomb tower; it refutes only rank-and-cap
proofs that omit birth geometry.

Second, local Golomb distinctness does not force `H_n^loc` to diverge.  For
each odd prime `p`, the `p`-mark Erdős--Turán ruler

```text
a_i=2pi+(i^2 mod p), 0<=i<p, n=(p+1)/2,
```

is strictly increasing and is an ordinary Golomb ruler: in an equality of
two differences, the difference of the two residue corrections has absolute
value below `2p`, forcing equal index gaps, and reduction modulo `p` then
forces equal initial indices.  It has diameter below `8n^2`.  Along this
family of different finite prime rulers, its local bulk satisfies

```text
limsup H_n^loc <= (3/4)(1+log(16/3))=2.00548... .
```

These finite prime rulers are not a nested infinite branch.  They prove that
the remaining theorem must exploit cross-epoch compatibility rather than a
stronger one-epoch distinctness or diameter estimate.

A separate append-a-distant-block construction makes the translation `X`
the new terminal mark and places a scaled finite Golomb block after it.  As
`X` grows, `H_n^loc` and `D_n` stay fixed, the terminal potential tends to
zero, and the block supplies arbitrarily many future differences below every
terminal suffix.  Without the eventual critical cap, this shows that a
terminal-identity-only estimate is false; the cap and nonlocal arithmetic are
essential.

## 6. Midpoint-jump reduction and sharp finite boundary

**[RIGOROUS — SELF-CONTAINED]** The explicit descendant functional has the
one-dimensional upper bound

```text
J_n^(h)<=sum_(p=2)^n r_(n,p)
 [log(d_(n,p)/D_(p,n))-(h-log3)]_+.
```

At `h=5/2`, the threshold `h-log3=1.4013877...` is only
`0.0150933...` above `log4`.  An alternating monotone scalar sequence
`A_k=4^k exp(s_k)`, with `s_(2j)=0`, `s_(2j+1)=eta`, and
`h-log12<eta<log4`, has a positive excess on every other dyadic step.  Its
Fejér sum is `Theta(J)`.  This is not a Golomb construction, but it rules out
scalar-cap telescoping after the positive part is taken.

There is also an actual finite one-epoch boundary.  For prime `p=2n-1`, take
the Erdős--Turán core of exact diameter `H=8n^2-12n+5` and append

```text
X=floor(C(2n-1)^2 log(4n-2)).
```

For fixed `C>0` and large prime rows, `X>2H`, so the append is Golomb.  Exact
row lower bounds give

```text
J_n^(h)>=R_n log((X-H)/(2exp(h)H))
        =(3/8-o(1))log log n+O_(C,h)(1).
```

These prefixes meet the cap at their terminal index but their varying early
cores need not obey one fixed eventual-`C` all-prefix envelope.  They do not
refute P23.  They prove that its new input must be compatible-tower geometry
or signed cancellation before `log_+`, not a stronger one-epoch estimate.

## 7. Primary artifacts and verification scope

- `endpoint_variance/WAVE18_EXCESS_DESCENDANT_JUMP_AND_BIRTH_LOCALITY_2026-08-29.md`
- `endpoint_variance/wave18_excess_birth_locality_certificate.py`
- `endpoint_variance/test_wave18_excess_birth_locality_certificate.py`
- `endpoint_variance/wave18_excess_birth_locality_certificate_2026-08-29.json`

**[COMPUTATIONAL — CERTIFIED FINITE]** The Wave 18 certificate checks exact
coefficient identities, the cap threshold inputs, rank-layer constants, and
finite Erdős--Turán ruler rows.  It is a consistency audit, not a proof of
the asymptotic birth-time estimate, an infinite critical branch, P19/P23,
either Erdős question, publication novelty, or a prize claim.
