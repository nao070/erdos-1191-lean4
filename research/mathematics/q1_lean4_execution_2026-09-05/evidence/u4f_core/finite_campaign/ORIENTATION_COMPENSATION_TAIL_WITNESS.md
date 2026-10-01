# Genuine component tail defeats two-orientation compensation

2026-09-09. Independent exact verification of the main researcher's
candidate counterexample. This rejects the intermediate inequality
below, not the frozen U4-F theorem or Q1. No Lean verification.

## Exact claim rejected

For two opposite orientation records sharing later source birth c,
older label e, and lower output i, the proposed bound is

```
v_minus + v_plus <= e^2 (u_rminus^[M] + u_rplus^[M]).
```

The same fixed-cap actual Sidon prefix changes this inequality from true
to false when the genuine component horizon increases from 24 to 25,
while its output horizon remains fixed at T=24.

## Actual prefix and records

Use C=1,m0=2 and

```
(1,2,4,8,13,21,31,45,66,81,97,123,148,182,204,
 252,290,361,401,475,565,593,662,775,822).
```

Fix c=17, e=a15-a11=204-97=107, and i=22. The records are

```
d_minus = a17-a16 = 290-252 = 38 < e,
t_minus = e-d_minus = 69 = a23-a22 = 662-593,

d_plus  = a17-a1 = 290-1 = 289 > e,
t_plus  = d_plus-e = 182 = a24-a22 = 775-593.
```

Thus s=15, r_minus=23, and r_plus=24. Their six endpoint sets are
{11,15,16,17,22,23} and {1,17,11,15,22,24}. Both cover exactly the
same cuts b=18,19,20,21.

The strict scalar core tests already follow from log17>2 and
log23,log24>3, and the independent rigorous log intervals certify these
lower estimates. In particular 15*2^2>17, 5*2^2>17,
1*3^3>23, 2*3^3>24, 17*2>24, and 69*2^3>17^2; the larger
physical output also passes. The exact evaluator and independent checker
verify all 25-rank positive-difference/two-sum Sidon conditions and the
same all-rank C=1,m0=2 cap.

In the contract's required numerical orientation d>e, the rows are

```
columns = d,e,p(d),q(d),p(e),q(e),c,s,i,r,t
(107,38,11,15,16,17,17,15,22,23,69)
(289,107,1,17,11,15,17,15,22,24,182)
```

## Exact genuine-price arithmetic

Let D_M be the left side minus the right side of the proposed bound.
Because u23^[M]=kappa23/H23^2+u24^[M],

```
D_M = 107*38*u23^[M] + 107*289*u24^[M]
      - 107^2*(u23^[M]+u24^[M])
    = 107*(113*u24^[M] - 69*kappa23/H23^2).
```

Direct rational summation with alpha_(M+1) retained gives

```
u23^[24] = 1140582653 / 502628531391268920000,
u24^[24] = 1 / 1188417015000,

D_24 = -184597358827 / 502628531391268920000 < 0.
```

Appending a25=822 gives H25=821 and

```
kappa25/H25^2 = 1 / 1640346177600,
D_25-D_24 = 107*113*kappa25/H25^2
          = 12091 / 1640346177600 > 0,

u23^[25] = 20603983736776789 / 7156986026218485962983335000,
u24^[25] = 1571535107 / 1083008504416695480000,

D_25 = 200502708371698175071 / 28627944104873943851933340000 > 0.
```

Thus M=25,T=24 is an exact counterexample to the proposed compensation.
For any further actual extension, the difference increments by
107*113*kappa_(M+1)/H_(M+1)^2>0, so a later positive component tail
cannot restore this particular inequality.

The complete record set at fixed T=24 is unchanged: the 675 old records
equal exactly the records from the M=25 enumeration with r<=24. The
new output records at r=25 are irrelevant to the witness. The sign change
is caused by the genuine component tail on unchanged records, not by
adding a new eligible output or altering strict core membership.

## Independent verification and logical scope

Only the requested new M=25 prefix was evaluated. The existing reference
evaluator found 820 records through T=25, and the independent output-based
checker reconstructed all of them exactly, verified all logarithmic
comparisons with UNKNOWN=0, and reproduced prices, profile coefficients,
and I_j. Targeted arithmetic then filtered r<=24, compared the full old
record set, and independently checked both displayed forms of D_M and
the exact increment.

`orientation_compensation_tail_witness.json` stores these exact values,
records, output/component horizons and original source hashes.
`C1_m02_greedy_M25_independent_check.json` binds the independent checker
and full certified M=25 profile by SHA-256.

The rejected premise was two-sign compensation with the older label's
squared weight. Both signs and exact output times must remain in any
replacement estimate. The frozen uniform-profile proposition and Q1
remain unresolved. Next nonduplicate action: seek a bound on the aggregate
compensation excess across actual fibers, including its positive future
component increments, instead of assuming each fiber is nonpositive.
