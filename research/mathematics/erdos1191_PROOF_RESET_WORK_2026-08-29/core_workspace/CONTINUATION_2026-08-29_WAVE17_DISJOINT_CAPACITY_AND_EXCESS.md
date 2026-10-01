# Erdős Problem #1191 — Wave 17 disjoint capacity continuation

Date: 2026-08-29 (Asia/Tokyo)  
Canonical root: `core_workspace/`  
Claim status: **Questions 1 and 2 remain open; no prize claim is ready**

## 1. What Wave 17 changes

Wave 17 closes the local coefficient-capacity overlap left by Wave 16.  It
does so without adding two lower bounds that spend the same Gothic atoms:

1. a same-atom diameter residual pays a fixed fraction of the Wave 15
   promotion, up to a dyadically summable error;
2. a stronger sorted-rank floor on the same interior atom set leaves an
   explicit eventual constant surplus over the Wave 11 triangular floor.

The second statement pays the promotion after a fixed pointwise truncation.
It does not pay the part above that truncation and does not itself enter the
signed terminal identity.  The exact remaining obstruction is therefore the
uncapped promotion excess together with the endpoint/descendant renewal
residual.  Wave 17 does not prove P19 or either Erdős question.

## 2. Same-atom residual theorem

**[RIGOROUS — SELF-CONTAINED]**

For the Wave 15 quantity

```text
Delta_m=sum_(p=2)^m u_(m,p)
  log(rho_(4m-1)(d_(m,p))/rho_(2m)(d_(m,p))),
```

every newly counted difference is a literal interior atom of the target bulk
`mathfrak B_(2m)`.  The Wave 11 triangular floor spends
`beta_x log L_s` from such an atom `beta_x log x`, leaving
`beta_x log(x/L_s)` on that same atom.

Ten layers of near differences in any consecutive integer Golomb interval
give, for interval diameter `x` and `s` gaps,

```text
x/L_s >= 3/2 whenever x>=2147.
```

The exact Wave 15 load on one selected value is less than `3/(4m^2)`, while
the smallest target-bulk coefficient is `1/(16m^2)`.  Since there are at most
2146 positive integers below the cutoff, one obtains

```text
mathfrak B_(2m)
 >= K_(2m)^int + c_0 Delta_m - E_m,
c_0=log(3/2)/12,
E_m=2146 log(3/2)/(16m^2).
```

The error is summable on dyadic epochs.  This is a genuine residual above the
triangular floor; the selected atoms are not spent twice.

## 3. Stronger local sorted-rank floor

**[RIGOROUS — SELF-CONTAINED]**

At target epoch `n`, the interior Gothic weights have multiplicities

```text
n-1                         at 1/n^2,
(n-1)(3n-8)/2               at 1/(2n^2),
n-1                         at 1/(4n^2).
```

Set

```text
a=n-1,
b=3(n-1)(n-2)/2,
c=(n-1)(3n-4)/2.
```

All interior differences are distinct positive integers.  Rearranging the
decreasing weights against ranks `1,...,c` gives the single valid floor

```text
F_n^(loc,int)=[2log(a!)+log(b!)+log(c!)]/(4n^2),
mathfrak B_n>=F_n^(loc,int).
```

For `D_n=F_n^(loc,int)-K_n^int`, elementary factorial integral bounds and a
constant-tracked Riemann-sum comparison give

```text
|D_n-delta_0| <= 18(1+log n)/n  for n>=16,
delta_0=3/2+(3/4)log3-2log2
       =0.937664855381... .
```

The weaker bound `20(1+log n)/sqrt(n)` is convenient for explicit thresholds:

```text
D_n>81/128  for n>=2^20,
D_n>3/4     for n>=2^22.
```

Wave 15 gives `Delta_m<(9/16)log13` and `log13<3`.  Consequently, once
`2m>=2^20`,

```text
mathfrak B_(2m)>=K_(2m)^int+(3/8)Delta_m.
```

This completes the local P21 floor-plus-promotion capacity gate for the
triangular floor.  It cannot also be added to another interior rearrangement
floor, and it is not yet a signed global upper.

## 4. Capped residual promotion

**[RIGOROUS — SELF-CONTAINED]**

For

```text
r_(m,p)=u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2),
P_(m,p)=log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p))),
```

write

```text
Theta_m^[2]=sum_p r_(m,p) min(P_(m,p),2),
Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+.
```

The exact coefficient mass is below `3/8`, so `Theta_m^[2]<3/4`.  Therefore,
once `2m>=2^22`, the local sorted-rank surplus pays the whole capped charge:

```text
mathfrak B_(2m)>=K_(2m)^int+Theta_m^[2].
```

The Wave 14 lower shell is disjoint from the Gothic interior, hence the legal
combined lower bound is

```text
A_(2m)>=K_(2m)^len+Phi_m+Theta_m^[2].
```

Wave 16 gives `P_(m,p)>=kappa_C` on the macroscopic suffix.  Thus eventually

```text
Theta_m^[2] >= (1/3)min(kappa_C,2).
```

The constant promotion signal now has a disjoint local carrier.

## 5. Exact remaining theorem — P22

**[CONDITIONAL]** This is the next proof obligation, not an established
signed repayment.

The unallocated term is

```text
Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+.
```

The present general envelope is only `O_C(log log m)` per epoch.  A Fejer
taper does not by itself turn its dyadic sum into `o(log J)`.  Put

```text
H_n^loc=mathfrak B_n-F_n^(loc,int)>=0.
```

The highest-value next theorem is a signed promotion-excess repayment: with
bounded reuse and every endpoint term retained, control

```text
sum_k omega_(k,J) Theta_(m_k)^exc
```

by unused local slack, unused `D_(m_(k+1))`, and exact renewal terms up to
`o(log J)`, and insert that inequality into

```text
Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m,
mathcal T_m>=0.
```

Any proof must keep the endpoint/descendant residual, authenticate each
carrier, and forbid double spending across dyadic sources.  Merely
lower-bounding the nonnegative bulk surplus does not yield the needed signed
upper and cannot contradict the Wave 13 harmonic lower bound.

## 6. Primary artifacts and verification scope

- `endpoint_variance/WAVE17_DISJOINT_RESIDUAL_CAPACITY_AND_EXCESS_BOUNDARY_2026-08-29.md`
- `endpoint_variance/wave17_residual_capacity_certificate.py`
- `endpoint_variance/test_wave17_residual_capacity_certificate.py`
- `endpoint_variance/wave17_residual_capacity_certificate_2026-08-29.json`

**[COMPUTATIONAL — CERTIFIED FINITE]** The deterministic certificate checks the integer and rational inputs of the
same-atom theorem, including the ten-layer threshold, coefficient/load
identity, and literal ownership on Hall-64 and Erdős--Turán-128 fixtures.  It
does not certify the asymptotic sorted-floor derivation, construct an infinite
branch, prove P19 or P22, resolve Questions 1 or 2, or support a prize claim.
