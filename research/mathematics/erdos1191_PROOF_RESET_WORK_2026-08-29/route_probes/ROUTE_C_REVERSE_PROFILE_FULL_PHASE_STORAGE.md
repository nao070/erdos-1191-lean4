# Route C reverse-profile full-phase storage certificate

Status: **exact finite calibration; C058 remains open**.

This note records one deliberately narrow computation for the fixed reverse-concentration
Golomb fixture

```text
(0,22,60,83,102,173,303,513,616,727,772,881,972,1041,1103,1169).
```

The result is positive only after integration over the **complete** factor-two phase.
It is not a pointwise or per-chamber storage inequality.  In fact, an independent exact
dual certificate on chamber 0 proves that the prototype target fails on that chamber
average.  Phase redistribution is therefore load-bearing in this calibration.

## Frozen finite model

The certificate fixes all of the following conventions:

- `k=2`, `C=2`;
- `rho=9/16` (no interval of rho values is claimed here);
- phase `t in [553/8,553/4]`;
- widths/multipliers `1,2,4,8`;
- ranks `3,...,15`;
- epoch 4 owns ranks `3,...,7`;
- epoch 8 demands ranks `7,...,15` and owns ranks `8,...,15`;
- half-open Haar sign `+1` on `[0,t)`, `-1` on `[t,2t)`, and `0` elsewhere;
- the current independent epoch-block, zero-row-sum Gram cone;
- prototype `epsilon=A=1/1000`, `B=1/3`, `e_2=0`.

The 16 marks have 120 distinct positive differences.  The finite fixture data replay to

```text
H2 = 430,  H3 = 656,  exp(eta_2) = 82/215,
V2 = 20177/66402,  V3 = 2143/29039,
V3-V2 = -443620417/1928247678.
```

The three finite `C=2` envelope rows are also checked exactly:

| `m` | `N_m` | required lower bound for `log m` |
|---:|---:|---:|
| 4 | 84 | `21/16` |
| 8 | 514 | `257/128` |
| 16 | 1170 | `585/512` |

These are finite consistency checks.  They do not construct an eventual infinite ray.

## Exact full-phase certificate

The 78 affine event lines generate 162 exact rational breakpoints and hence 161 chambers
covering `[553/8,553/4]` with no gap or overlap.  The single canonical JSON contains all
161 rational Gram factors; it does not depend on 161 loose discovery files.

The independent verifier reconstructs the phase states and checks:

- 2,285 rational zero-row-sum Gram columns, each supported in exactly one epoch block;
- positive semidefiniteness from the explicit rational factors;
- 99,176 generic owner rows at both chamber endpoints, for 198,352 exact comparisons;
- 194,528 owner rows at collapsed breakpoint cells;
- exact recovery of physical energy from the owner shares;
- every phase-polynomial minimum and every phase-boundary contribution;
- logarithmic integrals using a 30-term rational atanh series with an explicit positive
  tail.

Write `Phi_{9/16}(t)` for the supremal finite storage quantity in this frozen cone.  The
piecewise rational Gram factors are feasible primal witnesses for it.  Put

```text
I = integral_[553/8,553/4] Phi_{9/16}(t) dt/t,
Phi_bar = I/log 2.
```

The exact rational enclosures prove

```text
49/1000 < I < 1/20,
719/10000 < Phi_bar < 9/125.
```

Numerically, the enclosed integral of the chosen primal witnesses is approximately

```text
I       = 0.04985454617542759...
Phi_bar = 0.07192490653305922...
```

For the frozen prototype, the verifier evaluates

```text
R = (epsilon - A*eta_2 - B*(V3-V2))/3 - e_2
```

and proves

```text
13/500 < R < 27/1000,
Phi_bar - R > 457/10000.
```

Thus this fixed prototype survives the **complete phase-integrated** comparison at
`rho=9/16` in the current finite cone.

## Exact chamber-0 obstruction

Chamber 0 is `[553/8,277/4]`.  A second, independent eight-subinterval dual payload is
included in the same JSON.  It contains 16 rational epoch duals and the verifier performs
32 exact endpoint positive-definiteness checks using fraction-free Bareiss/LDL-style
elimination.

For the chamber-average normalization, that dual proves

```text
sup Phi_bar_chamber0 < 2601/100000 = 0.02601,
R - sup Phi_bar_chamber0 > 207/1000000.
```

The sharper computed upper enclosure is about `0.02600939942640579`, whereas the
prototype right-hand side is about `0.026217308750090592`.  Consequently a uniform
pointwise lower bound by `R` would be impossible: it would force the chamber average to
be at least `R`, contradicting the dual.  This is why the positive conclusion above must
not be read as pointwise survival, survival in every chamber, or a single-chamber result.

## What this does not prove

This artifact is a finite calibration for one fixed 16-mark reverse fixture.  It does
not prove any of the following:

- C058, Q1, or Q2;
- an eventual critical infinite history;
- global owner stitching between epochs;
- validity outside the independent epoch-block cone;
- the same comparison for any `rho` other than `9/16`;
- publication novelty or eligibility for an Erdős prize.

The useful research conclusion is narrower: a substantial full-phase finite margin is
compatible with this adverse reverse profile, but the margin genuinely uses transfer
between phase chambers.  Any C058 master inequality must preserve that redistribution
rather than replace it with a pointwise chamber bound.

## Reproduction

From the canonical workspace root, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py \
  --verify \
  route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.json \
  --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate_test.py
```

The first command prints

```text
VERIFY_OK chambers_replayed=161 gram_columns=2285 owner_endpoint_checks=198352 local_endpoint_ldl_checks=32 full_phase_prototype_survives_exactly chamber0_pointwise_prototype_fails_exactly mutations_rejected=13
```

The focused suite contains seven tests and replays the exact arithmetic, schema hardening,
canonical JSON bytes, CLI path, and mutation rejection.

## Integrity anchors

The canonical JSON uses schema
`erdos1191.c058_reverse_profile_full_phase_storage.v1` and has payload hash
`388daa5b719a6f817f3d2de2f5227340b2ec355ca53e93ba2753edc3d270b10d`.
The mechanically combined payload also records the two disposable discovery-input hashes:

```text
primal manifest source:
bd8bc014c5e3296bd65f9f1641923c21ebf6fbc187891ec6250202f1e3a3be10

chamber-0 dual source:
efa9d08158b6c55d64978063b57bd59e6658085322f783aa6c120bd73505cb13
```

The verifier recomputes the canonical payload hash after blanking its hash field, rejects
unknown or missing schema keys, and rejects 13 representative fixture, phase, factor,
owner, dual, conclusion, scope, and integrity mutations.
