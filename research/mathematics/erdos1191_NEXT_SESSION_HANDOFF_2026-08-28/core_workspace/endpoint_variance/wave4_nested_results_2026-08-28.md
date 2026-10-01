# Wave 4: nested critical-envelope Golomb search

## Disposition

This is a finite falsification and structure-discovery computation, not an
asymptotic argument.  It searches one nested ruler through the dyadic sizes
`4,8,16,32`, with the same critical-envelope constant `C=1` at **every**
prefix `2 <= m <= 32`:

\[
N_m=a_m-a_1+1\le 2m^2\log m.
\]

The two exact checkpoint statistics are

\[
G_m=\operatorname{Var}_{\nu_m}(u(1-u)),\qquad
I_m=Q_{m/2,00}/N_m.
\]

All logarithm decisions use rational upper and lower bounds.  Gap-variance
objectives use integer moments followed by `Fraction` reduction; innovation
objectives use the independently tested exact `Fraction` covariance update.

## Completeness boundary

- At `m=4`, the search is complete.  Its branch-and-bound tree exhaustively
  covers all `binom(43,3)=12,341` normalized increasing candidates with
  `N_4<=44`, pruning only after an explicit difference collision, and imposes
  the same envelope at `m=2,3,4`.
  Exactly 1,672 candidates survived.
- The exact maximum is `G_4=3/448`, attained only by
  `(0,1,4,6)` and its reflection `(0,2,5,6)`.
- At `m=8,16,32`, the search is heuristic: seeded beam width 256, at most 48
  proposed extensions per retained state, with deterministic edge/quantile
  proposals plus a seeded random sample.  No global optimality claim is made
  after `m=4`.
- CP-SAT and Z3 were not installed in the environment, so the implemented
  engine is pure-Python branch-and-bound plus beam search.

## Best minimum-`G` witness

Seed `1191`, objective: lexicographically maximize the minimum and then the
sum of the checkpoint `G_m` values.

```text
(0, 2, 5, 6, 28, 36, 43, 75,
 94, 123, 136, 147, 156, 201, 280, 448,
 464, 516, 601, 628, 683, 704, 767, 826,
 866, 1015, 1276, 1553, 1909, 2353, 2890, 4295)
```

| `m` | `N_m` | exact `G_m` | decimal | exact `I_m` | decimal |
|---:|---:|---:|---:|---:|---:|
| 4 | 7 | `3/448` | 0.00669642857142857 | `3/896` | 0.00334821428571429 |
| 8 | 76 | `103963/23658496` | 0.00439431990943127 | `647181/165609472` | 0.00390787430322826 |
| 16 | 449 | `9145155/1651515392` | 0.00553743249642084 | `271361911/52848492544` | 0.00513471431136986 |
| 32 | 4296 | `3001881427/537558777856` | 0.00558428501339464 | `1297038360163/241363891257344` | 0.00537378790757101 |

Thus the certified finite value is

\[
\min_{m\in\{4,8,16,32\}}G_m
=\frac{103963}{23658496}>0.0043943.
\]

The independent all-pairs audit found 496 distinct positive differences out
of 496 pairs.  The canonical difference-list SHA-256 is
`2702d9561006e2064ebd4ad1e2fc365787c34e348d6610ffa9fc8ce921453648`.

## Best minimum-innovation witness

Seed `9119`, objective: lexicographically maximize the minimum and then the
sum of `I_m` over transitions `2->4`, `4->8`, `8->16`, `16->32`.

```text
(0, 1, 4, 6, 28, 36, 43, 81,
 102, 133, 143, 152, 166, 221, 297, 570,
 586, 599, 656, 690, 800, 826, 846, 893,
 918, 1081, 1317, 1588, 1939, 2314, 2840, 4319)
```

| `m` | `N_m` | exact `G_m` | decimal | exact `I_m` | decimal |
|---:|---:|---:|---:|---:|---:|
| 4 | 7 | `3/448` | 0.00669642857142857 | `15/3584` | 0.00418526785714286 |
| 8 | 82 | `120081/27541504` | 0.00436000154530413 | `743151/192790528` | 0.00385470701133201 |
| 16 | 571 | `58070349/10683711488` | 0.00543540969495712 | `9008375897/1752128684032` | 0.00514138943052397 |
| 32 | 4320 | `116666318279/19568944742400` | 0.00596180937780560 | `64092330470429/11173867447910400` | 0.00573591290295955 |

Hence

\[
\min_{m\in\{4,8,16,32\}}I_m
=\frac{743151}{192790528}>0.0038547.
\]

Again all 496 positive differences are distinct.  The canonical difference
list SHA-256 is
`1d2744561f3822f8400d7ee7507df708065d2f4a39d6ed64f1aa8a258428f726`.

## Common envelope at every prefix

The integer cap in the second column is the rigorously determined
`floor(2m^2 log m)`.  Both witnesses pass all 31 rows.

| `m` | cap | `N_m` (gap witness) | `N_m` (innovation witness) |
|---:|---:|---:|---:|
| 2 | 5 | 3 | 2 |
| 3 | 19 | 6 | 5 |
| 4 | 44 | 7 | 7 |
| 5 | 80 | 29 | 29 |
| 6 | 129 | 37 | 37 |
| 7 | 190 | 44 | 44 |
| 8 | 266 | 76 | 82 |
| 9 | 355 | 95 | 103 |
| 10 | 460 | 124 | 134 |
| 11 | 580 | 137 | 144 |
| 12 | 715 | 148 | 153 |
| 13 | 866 | 157 | 167 |
| 14 | 1034 | 202 | 222 |
| 15 | 1218 | 281 | 298 |
| 16 | 1419 | 449 | 571 |
| 17 | 1637 | 465 | 587 |
| 18 | 1872 | 517 | 600 |
| 19 | 2125 | 602 | 657 |
| 20 | 2396 | 629 | 691 |
| 21 | 2685 | 684 | 801 |
| 22 | 2992 | 705 | 827 |
| 23 | 3317 | 768 | 847 |
| 24 | 3661 | 827 | 894 |
| 25 | 4023 | 867 | 919 |
| 26 | 4404 | 1016 | 1082 |
| 27 | 4805 | 1277 | 1318 |
| 28 | 5224 | 1554 | 1589 |
| 29 | 5663 | 1910 | 1940 |
| 30 | 6122 | 2354 | 2315 |
| 31 | 6600 | 2891 | 2841 |
| 32 | 7097 | 4296 | 4320 |

## Finite falsification signal

These witnesses refute the following finite-depth statements at `C=1`:

- dyadic `G_m` must be pointwise nonincreasing (both witnesses increase from
  8 to 16 and again from 16 to 32);
- every four-transition compatible nested ruler must have some
  `G_m<c` for any `c<103963/23658496`;
- every four-transition compatible nested ruler must have some
  `I_m<c` for any `c<743151/192790528`.

The empirical calibration is that a bounded-depth arithmetic lemma cannot
force visible decay merely from Golomb uniqueness and the common critical
envelope.  A viable upper-budget argument still needs genuinely longer
history, amortization, or an invariant not captured by four consecutive
dyadic transitions.

## What this does not show

- It does not construct an infinite critical Golomb sequence, and these
  32-mark rulers may fail to extend indefinitely under the same envelope.
- It does not contradict `sum_{j<=J} G_j=o(log J)` or any other asymptotic
  conclusion.
- It does not prove a positive lower bound for arbitrarily many scales.
- It does not establish optimal values at 8, 16, or 32 marks.
- It does not change the status of Erdős Problem #1191.

## Reproduction and certificate

```bash
cd /Users/USER/Documents/ChatGPT/mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28/core_workspace/endpoint_variance
python3 -m unittest wave4_nested_test.py
python3 wave4_nested_certificate.py \
  --sizes 4,8,16,32 \
  --constant 1 \
  --beam-width 256 \
  --candidates-per-state 48 \
  --retain 2 \
  --seeds 1191,9119 \
  --output wave4_nested_certificate_2026-08-28.json
```

Certificate SHA-256 (canonical payload, excluding its own hash field):
`36437444becc16c7520d0abe4c825dae13e9f7a01dbdaf9e30aa50ffe6fda81b`.
The JSON stores every positive difference for every retained witness, not
only a uniqueness flag.

The full certificate command was also run under Python 3.13.13 and Python
3.14.6; the resulting JSON files were byte-identical.  This is an observed
cross-version reproducibility check for these two interpreters, not a promise
about every future Python random implementation.
