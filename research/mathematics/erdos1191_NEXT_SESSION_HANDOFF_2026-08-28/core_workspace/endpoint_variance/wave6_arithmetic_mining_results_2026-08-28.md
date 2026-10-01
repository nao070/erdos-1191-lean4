# Wave 6 arithmetic mining: exact finite results

**Date:** 2026-08-28  
**Status:** exact finite certificate complete; 128-mark discovery heuristic  
**Canonical certificate internal SHA-256:**
`16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a`  
**Canonical JSON file SHA-256:**
`573098370f4def5593230bdacb8f9488325eaf67b0e7949c8adb606e1e71e15d`

## Outcome

All six retained 64-mark records in the authenticated Wave 5 certificate were
mined successfully.  They are six distinct Golomb rulers: each has exactly
`2016` distinct positive differences, no difference collision, and satisfies
the common `C=1` envelope at every prefix.

The authorized heuristic continuation also reached 128 marks.  Its final mark
is `136282`, its modulus is `136283`, all `8128` positive pair differences are
distinct, and all `127` prefix rows from 2 through 128 marks satisfy the exact
integer-safe `C=1` envelope.  The 128-prefix cap is `158991`; prefix 57 is the
unique tight recorded row, with modulus and cap both `26271`.

The 128-mark search used one Wave 5 persistence parent,
`beam_width=32`, `candidates_per_state=16`, `seed=601191`, and `retain=1`.
It generated `32003` extension states.  This search was not exhaustive.  The
existence and stated audits of the retained witness are exact finite facts;
optimality, uniqueness, and failure or success of other search paths are not.

## Certified 128-mark witness

```text
(0, 1, 4, 6, 28, 36, 43, 81, 102, 133, 143, 152, 166, 221, 297, 570,
 586, 599, 656, 690, 800, 826, 846, 893, 918, 1081, 1317, 1588, 1939,
 2314, 2840, 4094, 4154, 4205, 4288, 4457, 4468, 4758, 4823, 5168,
 5323, 5335, 13902, 14642, 14737, 14754, 15036, 15125, 15186, 15204,
 20423, 20549, 22091, 22164, 23713, 23886, 26270, 26679, 26903,
 26947, 27075, 27320, 27360, 27562, 28439, 28668, 28980, 30077,
 30295, 31011, 31621, 32212, 32945, 33406, 33650, 34523, 34982,
 35975, 36935, 37343, 38213, 38816, 39567, 40191, 48052, 50709,
 51583, 52048, 52454, 55934, 56108, 57381, 57702, 58174, 59390,
 60243, 60628, 63547, 65219, 65764, 77015, 78242, 79185, 79310,
 81294, 82030, 106992, 109220, 111473, 113749, 114585, 114653,
 120726, 123099, 125493, 127925, 128936, 129058, 129572, 129749,
 131441, 131934, 132173, 132946, 133818, 134586, 135788, 136282)
```

Its sorted-difference SHA-256 is
`04b84d0da915073cb46eb1351536f63fe532302df5bdfc1764271a0f31bc03b3`.
The exact minimum adjoint-relevant innovation over the recorded dyadic rows is

```text
2044607601929603 / 815542875732049920.
```

At the new 64-to-128 epoch, the normalized signed profile persistence is

```text
245589681743053 / 402372206022787.
```

These profile scores explain the beam ranking; they are not the arithmetic
Hall statistic below.

## Exact birth-lag Hall theorem

For each rank pair `(i,r)`, the certificate records its right-endpoint birth
epoch `n`, category `ON` or `NN`, and lag `ell=r-i`.  These
`F_(n,c,ell)` families partition every one of the `binom(M,2)` pairs.  Each
row stores all ranks, their exact differences, demand, distinct count,
collision deficit, and integer hull `[L_F,U_F]`.

For an integer interval `K`, let `D(K)` be the total demand of selected family
hulls contained in `K`, and put `Lambda=max_K D(K)/|K|`.  If the ruler is
Golomb, the differences contributed by all contained families are distinct
integers in `K`; hence the exact finite theorem is

```text
D(K) <= |K|, and therefore Lambda <= 1.
```

Scanning family-band endpoints is complete.  Any positive-demand interval
can be shrunk to the smallest interval spanning its contained family hulls;
this cannot lose a contained family and cannot reduce the ratio.  Thus this is
an exact maximizer, not a sampled interval search.

The principal recorded statistic restricts to `NN` families of demand at
least two and requires two represented epochs.  The adjacent-epoch values are:

| Source records | Epochs | Exact `Lambda_NN` | Demand / width |
|---|---:|---:|---:|
| all six 64-mark records | 8,16 | `32/431` | `32/431` |
| all six 64-mark records | 16,32 | `72/1715` | `144/3430` |
| persistence 0 and 1 | 32,64 | `339/11465` | `339/11465` |
| persistence 2 | 32,64 | `113/3847` | `339/11541` |
| innovation 0, 1, and 2 | 32,64 | `150/3797` | `150/3797` |
| retained 128 continuation | 64,128 | `858/34429` | `858/34429` |

## Recorded scaling pattern and its exact refutation

The retained-beam data initially suggested testing the stronger
adjacent-epoch quantity

```text
R_n = 16 n Lambda_NN(n,2n)^2.
```

For every one of the 22 serialized Golomb transition instances (including
repeated shared prefixes), the finite inequality

```text
R_n <= 1,
equivalently Lambda_NN(n,2n) <= 1/(4 sqrt(n)),
```

holds exactly.  The largest recorded value is
`11520000/14417209 < 1`, attained by each innovation witness at the 32-to-64
transition.  Along the continued leading persistence chain, the four exact
values of `R_n` are

```text
n=8:   131072/185761
n=16:  1327104/2941225
n=32:  58839552/131446225
n=64:  753831936/1185356041.
```

This 22-record pattern is real but selection-dependent.  An independent exact
probe subsequently **refuted** the proposed universal inequality under the
same finite Golomb and all-prefix `C=1` hypotheses.  Its 16-mark witness is

```text
(0, 1, 18, 34, 79, 127, 171, 218,
 319, 415, 509, 613, 710, 808, 903, 1002).
```

All 120 differences are distinct, and every prefix modulus is at most its
integer-safe `C=1` cap.  At epochs 8 and 16, the family
`F_(8,NN,2)` has demand 2 and band `[91,92]`, while
`F_(16,NN,1)` has demand 7 and band `[94,104]`.  Their containing interval
`[91,104]` has demand 9 and width 14, so

```text
Lambda_NN(8,16) = 9/14,
R_8 = 16*8*(9/14)^2 = 2592/49 > 1.
```

The same exactly audited nested chain extends through 64 marks and violates
the proposal at three consecutive transitions:

| Epochs | Exact pressure | Interval | Demand / width | Exact `R_n` |
|---:|---:|---:|---:|---:|
| 8,16 | `9/14` | `[91,104]` | `9/14` | `2592/49` |
| 16,32 | `17/28` | `[488,515]` | `17/28` | `4624/49` |
| 32,64 | `45/118` | `[398,515]` | `45/118` | `259200/3481` |

The 64-mark extension has all 2016 differences distinct and satisfies every
prefix `C=1` cap.  Its discovery was a seeded beam search, while these final
difference, prefix, and pressure audits are exhaustive for the retained
finite point set.

The independent scorer, full point set, difference hash, prefix moduli and
caps, and regression tests are in the
[`wave6_hall_candidate_probe.py`](wave6_hall_candidate_probe.py) and
[`test_wave6_hall_candidate_probe.py`](test_wave6_hall_candidate_probe.py)
sources.  The complete exact artifact and interpretation are
[`wave6_hall_candidate_probe_certificate_2026-08-28.json`](wave6_hall_candidate_probe_certificate_2026-08-28.json)
and
[`wave6_hall_candidate_probe_results_2026-08-28.md`](wave6_hall_candidate_probe_results_2026-08-28.md).
Consequently `R_n<=1` is not a candidate invariant under only Golomb plus the
critical envelope.  The authenticated 22-row observation remains useful as a
warning about beam-selection bias and as calibration for a richer invariant;
it cannot support reset-renewal by itself.

## Non-Sidon sawtooth control

The 64-mark sawtooth is explicitly and intentionally non-Sidon.  It has 2016
pairs but only 621 distinct differences, 1395 total collision deficit, 253
repeated difference values, and smallest repeated difference 8.  Its first
non-Sidon dyadic prefix is the four-mark ruler `(0,3,17,31)`, where difference
14 is represented by both rank pairs `(1,2)` and `(2,3)`.  Its summed
within-family collision deficit is 1242.

The two rank-lag-one newborn families at epochs 32 and 64 both have band
`[64,64]`, with demands 15 and 31.  Therefore their exact cross-epoch pressure
is `46`.  Here 64 is the repeated value causing that particular two-epoch
Hall overload; it is not the globally smallest repeated difference.  The
three adjacent values and scaled quantities are:

| Epochs | `Lambda_NN` | `R_n` |
|---:|---:|---:|
| 8,16 | `12/113` | `18432/12769 > 1` |
| 16,32 | `7/3` | `12544/9 > 1` |
| 32,64 | `46` | `1083392 > 1` |

Thus the sawtooth sharply separates the recorded arithmetic statistic, but it
is not a counterexample to any claim assuming the Sidon/Golomb property.

## Descriptive whole-shell packing

For the leading 64-mark Golomb ruler at the 32-to-64 transition, all 1024
`ON` and all 496 `NN` differences are individually and globally distinct;
there are zero actual cross-category collision values.  The hull overlap has
width 23349 and contains 745 occupied `ON` values and 489 occupied `NN`
values.

For the 64-to-128 transition, the exact descriptive row is:

- `ON`: 4096 pairs and 4096 distinct values, range `[877,136282]`;
- `NN`: 2016 pairs and 2016 distinct values, range `[68,107843]`;
- hull overlap: `[877,107843]`, width 106967;
- occupied values in the overlap: 3048 `ON` and 1970 `NN`;
- actual cross-category collisions: zero.

By contrast, sawtooth32-to-64 has 1024 `ON` pairs but only 403 distinct
values, 496 `NN` pairs but only 31 distinct values, and 31 actual
cross-category collision values.  These whole-shell overlap rows are
descriptive only; no density theorem is claimed from them.

## Six authenticated 64-mark records

All records below are distinct even when their terminal mark or displayed
scalar scores agree.  The full points and exact family data are in the JSON.

| Objective/index | Last mark | Sorted-difference SHA-256 |
|---|---:|---|
| persistence/0 | 27562 | `b9a0ca3bcd89b2300f12b0de86df5cc5c74fc1a73eb397252ded66d888f1f517` |
| persistence/1 | 27562 | `2c150ead90e8d115fc7128b9e96902a665586cc2c4d65d77a02bffeb5035c1f3` |
| persistence/2 | 27796 | `959bb0568a0bf426383db542475270d6e4aa82b4c451645b1d8f7f23b9065163` |
| innovation/0 | 34067 | `15f0e299cbf8a56b417ce7be829f3ef53144c6b11996de6702490adcc9fc7e0c` |
| innovation/1 | 34067 | `3658c0972552355442a02cd5fcc26f8e4f3cd8e4f57c89285540b86ab2163ab3` |
| innovation/2 | 34067 | `9eab7ea068fdf258f5440d54615f47c51a0d776df1eb8ea9c46fc453ed8d0b5e` |

## Completeness boundary

The certificate is exhaustive for each retained finite point set in the
following senses: every pair difference, every birth-lag family, every family
band endpoint candidate, every requested Hall maximizer, every dyadic ON/NN
transition, and every `C=1` prefix row is recomputed exactly.  All rational
fields are serialized as strings; no binary float enters the payload.

It is not exhaustive over 64- or 128-mark rulers, beam states discarded by
the heuristic, alternative interval-family definitions, or longer epochs.
It does not prove asymptotic renewal, summability, an infinite Sidon
construction, or Erdős Problem #1191.

## Reproduction and verification

Canonical generation was run with CPython 3.13.13 and took 95.43 seconds of
wall time on the recorded host:

```sh
cd /Users/USER/Documents/ChatGPT/mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28/core_workspace/endpoint_variance
/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python wave6_arithmetic_mining_certificate.py \
  --beam-width 32 --candidates-per-state 16 --seed 601191 --retain 1 \
  --output wave6_arithmetic_mining_certificate_2026-08-28.json
shasum -a 256 wave6_arithmetic_mining_certificate_2026-08-28.json
/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python -m unittest -v \
  wave6_arithmetic_mining_test.py
```

The certificate authenticates the Wave 5 internal hash
`a26c13574002eb442731bcbec465a5fa7553a25728e2225ddba942e6df4d3ceb`,
records SHA-256 values for the generator, test, search module, and their local
dependency closure, and aborts if generator sources change during a run.
Canonical byte identity is claimed only for the recorded Python runtime; no
cross-runtime byte-identity claim is made.
