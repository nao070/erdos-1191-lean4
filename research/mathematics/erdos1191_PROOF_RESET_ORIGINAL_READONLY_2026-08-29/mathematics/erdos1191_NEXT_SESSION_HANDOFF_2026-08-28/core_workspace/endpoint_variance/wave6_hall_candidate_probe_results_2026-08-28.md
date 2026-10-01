# Wave 6 adjacent-epoch Hall-candidate probe

Date: 2026-08-28

Status: **the proposed finite universal inequality is false**.  The result is
an exact finite falsification, not an asymptotic theorem and not an infinite
critical-Sidon construction.

## 1. Statistic and exact scorer

Write a normalized ruler as

```text
0 = a_0 < a_1 < ... < a_(M-1),    N_m = a_(m-1)+1.
```

At a dyadic right-endpoint birth epoch `m`, its newborn rank block is
`m/2 <= i < m`.  For `1 <= ell < m/2`, the newborn--newborn lag family is

```text
F_(m,NN,ell) = {(i,i+ell): m/2 <= i < i+ell < m}.
```

Its demand is `m/2-ell`; the probe retains only demand at least two.  Its
difference hull is the inclusive integer interval

```text
[L_F,U_F] = [min(a_(i+ell)-a_i), max(a_(i+ell)-a_i)].
```

For adjacent epochs `n,2n` and an inclusive integer interval `K`, let `D(K)`
be the sum of the demands of every retained family whose whole hull is
contained in `K`, subject to both epochs being represented.  The tested
quantity is

```text
Lambda_NN(n,2n) = max_K D(K)/|K|,
R_n = 16 n Lambda_NN(n,2n)^2.
```

The proposed inequality was `R_n <= 1`.

The maximization for any fixed ruler is exact.  If an interval has positive
demand, shrink it to the minimum interval spanning the hulls it contains.
This loses no contained family and weakly increases its ratio.  Hence an
optimizer has endpoints among the finitely many family-hull endpoints.  The
independent scorer checks every ordered endpoint pair, uses exact rational
arithmetic, and counts inclusive width as `U-L+1`.

The first dyadic level at which this two-epoch statistic can exist is
`n=8`.  At epoch 4 the newborn block has only two ranks, so every NN lag
family has demand at most one and the old epoch cannot be represented after
the demand-at-least-two filter.  At epoch 8, lags 1 and 2 have demands 3 and
2.  This is a complete feasibility statement about the definition, not an
enumeration or minimality result for Golomb rulers.

## 2. Exact 16-mark refutation at the earliest feasible level

The normalized 16-mark ruler

```text
(0, 1, 18, 34, 79, 127, 171, 218,
 319, 415, 509, 613, 710, 808, 903, 1002)
```

has all 120 positive pair differences distinct.  Its ascending, newline-
serialized differences have SHA-256

```text
20489f245d7935c77e244f4385f4436b8e2696af9844b846c8b2f973a5c1ac3f
```

For every prefix `2 <= m <= 16`, the exact rational logarithm enclosure
certifies

```text
N_m:
(2,19,35,80,128,172,219,320,416,510,614,711,809,904,1003)

floor(2 m^2 log m):
(5,19,44,80,129,190,266,355,460,580,715,866,1034,1218,1419).
```

Thus every one of these finite prefixes satisfies the `C=1` envelope.

The exact maximizing Hall interval at `8 -> 16` is `[91,104]`.  Its contained
families are

```text
epoch 8,  lag 2: differences (92,91),
                  hull [91,92], demand 2;
epoch 16, lag 1: differences (96,94,104,97,98,95,99),
                  hull [94,104], demand 7.
```

Consequently its inclusive width is 14, total demand is 9, and the complete
endpoint scan gives

```text
Lambda_NN(8,16) = 9/14,
R_8 = 16*8*(9/14)^2 = 2592/49 > 1.
```

This alone refutes the proposed universal finite-prefix inequality.

## 3. One exact 64-mark ruler with three consecutive violations

A deterministic targeted beam extended the same prefix to

```text
(0, 1, 18, 34, 79, 127, 171, 218,
 319, 415, 509, 613, 710, 808, 903, 1002,
 1135, 1385, 1636, 1885, 2133, 2380, 2632, 2885,
 3139, 3396, 3651, 3909, 4165, 4424, 4669, 4930,
 5080, 5578, 6074, 6564, 7066, 7569, 8079, 8573,
 9040, 9513, 9970, 10431, 10852, 11311, 11723, 12133,
 12607, 13079, 13488, 13896, 14303, 14708, 15109, 15559,
 15961, 16359, 16765, 17164, 17618, 18051, 18451, 18854).
```

The exact post-search audit, which rebuilds rather than trusts beam state,
finds all 2016 positive differences distinct and all 63 prefixes under their
`C=1` caps.  The sorted-difference SHA-256 is

```text
fd3e33ac286ab6748fdf133a6562ec4f6573723cbac4047ef26b432fee27a836.
```

The exact adjacent-epoch maxima are:

| Epochs | Maximizing interval | Demand / width | `Lambda_NN` | `R_n` |
|---:|---:|---:|---:|---:|
| 8,16 | `[91,104]` | `9/14` | `9/14` | `2592/49` |
| 16,32 | `[488,515]` | `17/28` | `17/28` | `4624/49` |
| 32,64 | `[398,515]` | `45/118` | `45/118` | `259200/3481` |

For `16 -> 32`, the maximizing band contains the epoch-16 lag-5 family
(demand 3, hull `[488,493]`) and epoch-32 lag-2 family (demand 14, hull
`[495,515]`).  For `32 -> 64`, it contains that epoch-32 lag-2 family and the
epoch-64 lag-1 family (demand 31, hull `[398,510]`).  The certificate records
every contributing difference and every prefix modulus and cap.

The 32-mark discovery used beam width 128, 96 proposal-budget units per
state, seed 861191, target gap 250, and generated 528317 valid extension
states.  The modest 64-mark continuation used beam width 16, 32 proposal-
budget units per state, seed 862191, target gap 500, and generated 39716
valid extension states.  These are incomplete heuristic searches.  Their
outputs are exact witnesses after independent audit; neither search proves
optimality, uniqueness, lexicographic minimality, or shortest span.

## 4. Authenticated fixture comparison and selection bias

The probe independently rescored the six authenticated Wave 5 64-mark
fixtures at `8 -> 16`, `16 -> 32`, and `32 -> 64`, and the authenticated
128-mark continuation at all four adjacent transitions.  These are 22
serialized transition instances when repeated prefixes are retained.  Every
one satisfies the candidate, and their largest exact value is

```text
11520000/14417209 < 1.
```

The imported arithmetic-mining certificate is authenticated by canonical
hash

```text
16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a.
```

The endpoint scan is complete for every fixed imported point set, but those
point sets are selected beam outputs and are not an exhaustive sample of
Golomb rulers.  The 64-mark counterexample demonstrates that the earlier
pattern was selection-dependent.

## 5. Logical boundary

The rigorous conclusion is narrow and negative:

```text
Golomb uniqueness plus N_m <= floor(2 m^2 log m) at all prefixes of a
finite ruler does not imply 16 n Lambda_NN(n,2n)^2 <= 1.
```

No infinite extension of the displayed ruler is asserted.  Therefore this
does not by itself refute a differently quantified claim restricted to
prefixes known to lie on one infinite critical Sidon sequence.  It does show
that such a claim would require a genuinely global/infinite hypothesis not
present in the tested finite inequality.  There is no asymptotic result,
innovation-budget bound, reset-renewal exclusion, or solution of Erdős #1191
here.

## 6. Reproducibility

The owned artifacts are:

- `wave6_hall_candidate_probe.py`: independent scorer, exact cap audit, and
  seeded search;
- `test_wave6_hall_candidate_probe.py`: focused regression tests;
- `wave6_hall_candidate_probe_certificate.py`: authenticated certificate
  generator and optional full beam replay;
- `wave6_hall_candidate_probe_certificate_2026-08-28.json`: all points,
  differences by selected family, prefix caps, exact ratios, source hashes,
  and scope flags.

Generate with the deterministic discovery replay using

```text
python wave6_hall_candidate_probe_certificate.py --replay-search
```

The beam replay is not needed to verify the mathematical counterexample:
the exact audit of the recorded points is self-contained.
