# Route C / C131: complete fixed-C120 common-phase primal

## Status

`EXACT_FINITE_COMPLETE_FIXED_C120_COMMON_PHASE_PRIMAL_C058_OPEN`

C131 supplies an exact rational primal witness for every one of the 147 event
chambers of the fixed C120 row on the common completed-shell phase
`[82,164]`, at `rho=9/16`, for the frozen candidate

```text
epsilon = A = 1/1000,  B = 1/2,  C_ordered_suffix = 1/10,  e2 = 0,
DeltaV = -443620417/1928247678,
DeltaVrt_C120 = -13171/58179.
```

This closes the previously incomplete **finite C120 phase-primal
computation**.  It does not close C058 or any infinite-history obligation.

## Factor provenance and storage

- New chambers `0..114` have exactly the same breakpoints as old chambers
  `46..160` in `ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.json`.
  C131 hash-pins that verifier and payload, validates their canonical schema,
  and re-audits those 115 unchanged full 52-dimensional rational-Gram
  factors at their original scale `1/D^2`.  It does not numerically refit or
  rescale them.
- Only new chambers `115..146` are stored in the C131 JSON.  Each epoch is a
  reduced integer factor with denominator `100000000`; its last block
  coordinate is recovered by zero-sum embedding, and its exact Gram scale is
  `1/(D^2 * midpoint)`.
- The accepted payload excludes solver status, floating matrices,
  eigenvalues, clipping data, and numerical margins.  Numerical optimization
  was used only to discover the 32 tail factors.

Pinned hashes:

```text
prefix verifier sha256
6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9

prefix JSON sha256
6d0382b1267aac07e1ba5533a6a8d292dc29ba937911cae2bef9628052c21e74

prefix payload sha256
388daa5b719a6f817f3d2de2f5227340b2ec355ca53e93ba2753edc3d270b10d

temporary tail discovery sha256
c39708a826344077fad6e4910982a45e0e0b1319cbf5ced901f085407baed909

accepted tail factor-bank sha256
bb8629e4248bc6467fe6617f319e74f42457350dd797e821e320a7dc8b0477e8

C131 payload sha256
5012236aa28d76867d94926a26d00ffacf602952e93358818594907f7ea7d477
```

## Exact replay contract

For each chamber the verifier checks:

1. exact chamber order and both rational endpoints;
2. integer factor dimensions, zero-sum epoch support, positive Gram scale,
   and exact modular column rank modulo `1000000007` and `1000000009`;
3. generic owner inequalities at both left and right endpoints;
4. collapsed exact-cell owner inequalities at the left and right endpoints;
5. the exact-cell owner inequalities at the chamber midpoint;
6. structural-zero ownership: zero owned share and nonpositive demand;
7. separate epoch-4 and epoch-8 owner-share recovery, preventing cross-epoch
   cancellation;
8. separate epoch-4, epoch-8, and `rho`-weighted objective reconstruction at
   both endpoints and the midpoint;
9. exact phase integration with a 30-term rational atanh logarithm enclosure.

Frozen exact census:

```text
chambers / factors                         147 / 294
prefix / tail chambers                    115 / 32
rank min / max / sum                      4 / 31 / 3205
prefix / tail rank sum                    1605 / 1600
generic active / structural-zero rows     53312 / 37240
generic endpoint checks                   106624
collapsed active / structural-zero rows   104080 / 73440
midpoint active / structural-zero rows    53312 / 37240
unique state evaluations                  11319
separate-epoch recovery checks            22638
owner context references                  44828
separate-epoch context references         89656
endpoint epoch / weighted objectives      588 / 294
midpoint epoch / weighted objectives      294 / 147
strictly positive / negative pieces       147 / 0
minimum active owner slack                305733/87500000000000
```

The outward exact enclosure proves

```text
raw integrated margin                 > 21/1000
normalized integrated margin          > 3/100
normalized integrated margin          < 31/1000
raw enclosure width                   < 10^-26
```

For orientation only (not used by the verifier), the computed lower values
are approximately `0.02125875830459498` raw and `0.030669905181496242`
normalized.

## Reproduction

From `route_probes/`:

```bash
python3 -B ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_certificate.py --self-check
python3 -B -m unittest -v ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_test.py
```

The executable verifier reports `VERIFY_OK row=C120`, `chambers=147`,
`factors=294`, four rejected mutation classes, and `C058_open`.  The focused
test suite covers normal replay, payload mutation, factor mutation, endpoint
mutation, scope mutation, the frozen census, and the command-line entrypoint.

## Scope boundary

C131 proves only a fixed 16-mark C120 row, one rational coefficient
candidate, the phase `[82,164]`, `rho=9/16`, and the independent epoch-block
cone.  In particular it does **not** prove:

- C103 phase-rule admissibility;
- the C103 Abel boundary and terminal ledger;
- a complete primal for all rows or all phases;
- the finite-horizon local master inequality;
- global phase-representative independence;
- arbitrary-rank owner transport or global owner stitching;
- C058, Q1, Q2, the Erdős problem, publication novelty, or prize readiness.

The global repository status therefore remains `UNRESOLVED_AT_HARD_LIMIT`.
