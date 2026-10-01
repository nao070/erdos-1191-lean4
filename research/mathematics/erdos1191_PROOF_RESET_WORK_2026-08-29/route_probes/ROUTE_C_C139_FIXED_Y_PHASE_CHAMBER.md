# C139: maximal exact fixed-Y phase chamber

## Status

**Classification:** `EXACT_MAXIMAL_CONNECTED_FIXED_Y_PHASE_CHAMBER_C058_OPEN`.

This is the canonical exact finite continuation of the hardened C138 witness.  The graph matrix `Y` is
bit-for-bit the same 57-root graph encoded by the finalized canonical C138
certificate:

- canonical C138 file SHA-256:
  `9008c8639f13906abfb4866f8fa6e7b260c9e2fed76804656e1f773d534e70b9`;
- canonical C138 semantic payload SHA-256:
  `2dcd5099a449587a27cddbea0785ef862c73e62e90573bfb39c3f3776f9fd760`;
- support-only canonical SHA-256:
  `9733c946ef369b797dee487c7693af56b101d5909bc8abf11da7d1a56549e680`.

The ancestry path stored in the certificate is repo-relative:
`route_probes/ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.json`.

## Exact phase result

For the frozen 32-mark fixture, 100 active channels, full `M16`, and the same
fixed C138 graph `Y`, the maximal connected closed phase interval containing

```text
t0 = 17745/32
```

on which every weighted epoch-8/16 owner inequality and every pre8/rank-7
owner inequality is nonnegative is

```text
[4425/8, 555].
```

The x-cell convention is always
`[event_i,event_(i+1))`.  Coincident event endpoints are collapsed and
zero-length cells are omitted.  Thus both displayed phase endpoints are
included: the cells responsible for the adjacent failures have exactly zero
width at the corresponding endpoint, and every remaining noncollapsed row was
replayed exactly.

The generic open chamber has 150 distinct global events, 149 x-cells, and
1,192 weighted owner rows.  Its exact census is

```text
tight / strict rows       = 884 / 308
zero / positive capacity = 807 / 385
pre8 zero / positive     = 145 / 4
minimum positive slack   = 5/65536
minimum positive capacity= 5/65536
integrated pre8 share    = 6489/256.
```

At the collapsed lower endpoint there are 148 events, 147 cells, and 1,176
rows; at the collapsed upper endpoint there are 147 events, 146 cells, and
1,168 rows.  Every retained owner row and pre8 share is nonnegative at both
endpoints.

## Maximality for this fixed Y

All 150 global event lines were crossed exactly over the ambient critical band
`[5915/16,5915/8]`, giving 564 exact phase breakpoints including the band
ends.  There is no global event crossing inside `(4425/8,555)`.  The two
immediately adjacent chambers fail:

| side | adjacent open chamber | countercell | owner | capacity | weighted demand | slack |
|---|---:|---|---|---:|---:|---:|
| left | `(553,4425/8)` | `[2659+8t,7084)` | `(16,8)` | `45/32768` | `729/131072` | `-549/131072` |
| right | `(555,557)` | `[6739+t,6184+2t)` | `(16,1)` | `3/8192` | `9/4096` | `-15/8192` |

The left countercell has width `4425-8t` and collapses at `t=4425/8`; the
right countercell has width `t-555` and collapses at `t=555`.  Their exact
100-coordinate state hashes and line adjacency are stored and independently
replayed.  Since either extension of a connected interval containing `t0`
must enter one of these failing chambers, the displayed closed interval is
maximal for this fixed `Y`.

## Exact affine objective throughout the chamber

On the whole closed interval,

```text
D(t) = -(99/512)t + 765573/4096,

P(t) = (36082193/435322880)t
       + 1599473659439/16716398592,

2D(t)-P(t)
     = -(204429713/435322880)t
       + 4649365900753/16716398592.
```

The margin is decreasing, so its exact chamber minimum is attained at the
upper endpoint and is still positive:

| phase | `D` | `P` | `2D-P` |
|---:|---:|---:|---:|
| `4425/8` | `163749/2048` | `2365859438759/16716398592` | `307278796633/16716398592` |
| `17745/32` | `1305537/16384` | `2367807877181/16716398592` | `296239592131/16716398592` |
| `555` | `326013/4096` | `2368457356655/16716398592` | `292559857297/16716398592` |

No floating-point value or numerical solver status is used by either replay.

## Full M16 and the same-atom fourteen-row ledger

Every epoch-16 demand is rebuilt from the full exact 17-by-17 `M16` matrix.
The replay separately reconstructs the difference from the quarter-scaled two
`M8` blocks: it has 63 cross-half sources, 160 ordered nonzero off-diagonal
entries, zero row sums, and mixed signs.  The two-`M8` replacement is never
used.

The larger same-atom ledger geometry has 203 event lines and two internal phase
crossings inside the owner chamber:

```text
4425/8 < 554 < 1664/3 < 555.
```

Accordingly the replay audits the three parameter pieces
`[4425/8,554)`, `[554,1664/3)`, and `[1664/3,555]`, plus all four collapsed
phase boundaries.  These splits are retained because the x-cell topology does
change.  Nevertheless, exact cancellation makes the integrated affine formula
for each formal row agree on all three pieces.  The five nonzero rows are

| formal row | slope in `t` | intercept |
|---|---:|---:|
| `band:A16:s0` | `-63/512` | `85659/1024` |
| `band:A32:s0` | `-5121/32768` | `13790619/131072` |
| `band:A32:s1` | `-3483/65536` | `6142905/262144` |
| `band:A32:s2` | `441/2048` | `-3510675/32768` |
| `band:A32:s3` | `-4995/65536` | `21429225/262144` |

The four `band:A8` rows, `band:A16:s1,s2,s3`, and both terminal rows have the
identically zero affine formula.  They are not omitted: all fourteen formal
rows, including `terminal:e8:s4` and `terminal:e16:s4`, are present in every
subchamber table and checked at every collapsed boundary.  The fourteen row
functions sum coefficientwise to the exact `D(t)` above.

The distinct ledger event/cell counts at the four collapsed phases are

```text
t=4425/8 : 201 / 200
t=554    : 201 / 200
t=1664/3 : 202 / 201
t=555    : 200 / 199.
```

## Verification bundle

- `ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.json`: frozen support, exact phase chamber,
  affine functions, endpoint values, adjacent countercells, all three ledger
  tables, and a canonical semantic-payload hash;
- `ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.py`: exact replay using the already-certified C136
  finite primitives and independently checking the finalized canonical C138
  ancestry;
- `ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_independent_oracle.py`: stdlib-only reconstruction which
  imports none of the C136/C138/C139 verifier code;
- `ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_test.py`: 13 tests, including both positive replays and 11
  adversarial metadata/support/scope mutations (mutated semantic hashes are
  recomputed for all but the raw-integrity test).

Fresh results:

```text
C139_EXACT_PHASE_CHAMBER_OK ... C058_open
INDEPENDENT_C139_OK ... C058_open
Ran 13 tests in 22.061s
OK
```

## Exact scope boundary

C139 upgrades C138 from a single phase to a nontrivial, maximal closed phase
chamber **for one frozen fixture and one frozen graph Y**.  It does not prove a
nonanticipating phase-selection rule, feasibility on all phase chambers,
arbitrary history, arbitrary rank, a horizon-uniform C103 ledger, C058, Q1,
Q2, or prize eligibility.  C058 therefore remains open.
