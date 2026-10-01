# Erdős Problem #1191 — Wave 15 future-rank promotion continuation

Date: 2026-08-29 (Asia/Tokyo)  
Canonical root: `core_workspace/`  
Claim status: **Questions 1 and 2 remain open; no prize claim is ready**

## 1. What changed after Wave 13

Wave 13 proved that an eventual-`C` critical integer branch, if it existed,
would have an unavoidable harmonic lower bound in both the birth energy and
the cut-renewal remainder.  It then isolated the positive terminal suffix fan
`mathfrak U_m` versus the negative interior bulk `mathfrak B_m`.

Waves 14--15 make three further rigorous advances:

1. a long old difference must acquire quantitatively many future ranks under
   the polynomial-log cap;
2. the part of that promotion carried by the same difference's next lower-row
   copy is a legal addition to the Wave 11 floor;
3. the promotion realized in the immediately following block has bounded
   nested reuse and fits into literal next-epoch negative bulk atoms.

None of these statements is yet a global signed upper.  The endpoint horizon
and disjoint use of the old floors remain open.

## 2. Wave 14 promotion theorem

For a prefix of `L` marks and an old difference `d`, place

```text
N=floor(d/log(d)^2)
```

future marks into half-open bins of width `d`.  If `x_q` are the bin
occupancies and `B` is the number of occupied bins, Golomb uniqueness gives

```text
rho_(L+N)(d)-rho_L(d)
  >= sum_q binom(x_q,2)
  >= (N^2/B-N)/2.
```

Applying the eventual cap at the last future index and retaining all floor
errors proves, under the explicit side conditions in the primary memo,

```text
rho_infinity(d)-rho_L(d) >= d/(64C log d).
```

For

```text
d_(m,p)=D_(p,2m-1),  2<=p<=m,
```

the interval contains at least `binom(m+1,2)` distinct subdifferences.  Hence
the side conditions hold for all sufficiently large `m`, and

```text
log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p)))
  >= log(1+1/(64C log d_(m,p)))
  >= 1/(512C log m).
```

The `u`-weighted macroscopic resource is at least
`1/(1024C log m)`.  This is a positive rank channel; it must not be subtracted
from the frontier without a negative carrier.

## 3. Legal next-shell rebate

At epoch `2m`, the same `d_(m,p)` occurs in the Wave 11 lower shell with

```text
v_(m,p)=(4m-2p+1)/(16m^2).
```

Let `L_(m,p)=binom(2m-p+1,2)`.  The exact identity

```text
log d
 = log L
 + log(rho_(2m)/L)
 + log(rho_infinity/rho_(2m))
 + log(d/rho_infinity)
```

has four nonnegative channels.  Therefore

```text
A_J >= K_J^star+Phi_(J-1),
K_J^star=max(K_J^len,K_J^mix).
```

The macroscopic `v`-mass is

```text
(m-1)(3m-1)/(16m^2) -> 3/16.
```

Using the sharper promotion formula gives

```text
Phi_m >= (3/2048-o_C(1))/(C log m).
```

This rebate is disjoint from the interior rearrangement in `K^mix`.  It is
not legal to add the same premium blindly to the old all-atom global floor.
Nor does the lower bound imply `Phi_m>=Y_m` or `Phi_m>=Z_m`.

The positive frontier coefficient left after the next lower-row copy is

```text
u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2),
sum_(p=2)^m (u-v) -> 3/8.
```

## 4. Wave 15 adjacent-epoch load theorem

Use only the next block

```text
V_m={a_(2m),...,a_(4m-2)}.
```

For each macroscopic suffix threshold, the same bin argument now yields

```text
K_p=rho_(4m-1)(d_(m,p))-rho_(2m)(d_(m,p))
    >=d_(m,p)/(128C log(8m))
```

eventually.  Every new difference at most `d_(m,p)` is a literal Gothic
`mathfrak B_(2m)` atom with coefficient at least `1/(16m^2)`.

Set

```text
Delta_m=sum_(p=2)^m u_(m,p) log(1+K_p/r_p),
r_p=rho_(2m)(d_(m,p)).
```

For one new numerical difference `x`, the complete load over all nested
thresholds is

```text
L_m(x)=sum_(p:x<=d_(m,p)) u_(m,p)/r_p < 3/(4m^2).
```

Consequently

```text
1/(512C log(8m)) <= Delta_m
Delta_m <= mathfrak B_(2m)+3(ceil(e^12)-1)/(4m^2).
```

The error is dyadically summable.  Within this project, this is the first
fully bounded nested reuse allocation in the promotion route, but it spends the selected bulk
atoms' full values.  It is not yet a premium beyond `K^len`, `K^mix`, or the
global rank floor.

## 5. Exact unresolved obstruction

Two obstructions remain.

First, shifting `mathfrak B_(2m)` backward by one epoch over a finite horizon
leaves the terminal positive fan.  At `M=2^J`,

```text
mathfrak U_M >= (1/2)log(M(M+1)/2)=Theta(J),
```

which is much larger than `o(log J)`.  Any valid shift therefore needs an
exact terminal potential rather than an unbounded loan from beyond the
horizon.

Second, an atom born `k` dyadic epochs after its source can have source load
of order `1/m^2` but negative birth coefficient only of order `1/M^2`, a
ratio of order `4^k`.  The current cap does not provide the logarithmic value
needed to pay this factor uniformly.

The next theorem should prove one of the following:

1. a disjoint inequality
   `mathfrak B_(2m)>=existing_floor+c Delta_m-summable_error`, together with
   a terminal potential whose horizon cost is `o(log J)`; or
2. an all-epoch birth-time allocation for the residual `u-v` channel, with
   bounded total reuse and an explicit terminal ledger.

Do not attempt to replace `Delta_m` by the raw term
`u_(m,p)log d_(m,p)`.  The direction `x<=d` gives `log x<=log d`, and the
finite Hall-64 and Erdős--Turán-128 audits contain explicit failures of that
raw allocation.

## 6. Primary artifacts

- `endpoint_variance/WAVE14_FUTURE_RANK_PROMOTION_2026-08-29.md`
- `endpoint_variance/WAVE14_PROMOTION_REBATE_AND_ALLOCATION_BOUNDARY_2026-08-29.md`
- `endpoint_variance/WAVE15_LOCAL_PROMOTION_ALLOCATION_AND_HORIZON_OBSTRUCTION_2026-08-29.md`
- `endpoint_variance/wave14_future_rank_promotion.py`
- `endpoint_variance/wave14_future_rank_promotion_certificate.py`
- `endpoint_variance/wave14_future_rank_promotion_certificate_2026-08-29.json`
- `endpoint_variance/wave15_local_promotion_allocation_probe.py`
- `endpoint_variance/wave15_local_promotion_allocation_certificate_2026-08-29.json`

The certificates are finite algebra and mechanism checks.  Their scope flags
must continue to say that no infinite branch, signed global allocation,
resolution, or prize claim has been certified.
