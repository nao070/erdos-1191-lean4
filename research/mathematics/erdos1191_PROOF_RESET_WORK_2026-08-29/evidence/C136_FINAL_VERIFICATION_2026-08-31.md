# C136 final verification — 2026-08-31

## Outcome

The canonical C136 exact verifier, focused tests, and independent stdlib-only
oracle all pass.  The result certifies a fresh positive graph-root capacity
for every direct epoch-8/epoch-16 owner-cell inequality at one explicit
32-mark fixture and one phase midpoint.  It does not certify payment of the
C133 fourteen-row box-carrier ledger or C058.

## Fresh canonical replay

From the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B route_probes/ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate.py --self-check
MUTATION_OK rejected=10/10
C136_EXACT_PARTIAL_OK phase=17745/32 channels=100 roots=57 owner_rows=1192 tight=884 margin=270571186627/9402974208 C133_rows=14 full_14row_payment=UNKNOWN C058_open

PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v route_probes/ROUTE_C_C136_JOINT_GRAPH_MASTER_test.py
Ran 8 tests in 21.301s
OK

PYTHONDONTWRITEBYTECODE=1 python3 -B route_probes/ROUTE_C_C136_JOINT_GRAPH_MASTER_independent_oracle.py
INDEPENDENT_C136_PARTIAL_OK phase=17745/32 channels=100 roots=57 graph_rank=51 owner_rows=1192 tight=884 margin=270571186627/9402974208 residual_sources=63 C133_box_rows=14 pointwise=191 countercell_direct=225/32768 full14=UNKNOWN C058_open
```

## Exact accepted scope

- The explicit 32-mark fixture has 496 distinct positive differences.
- The phase is only `t=17745/32`, not the surrounding interval.
- The graph has 100 channels and 57 strictly positive rational roots; it is
  PSD, has zero row sums, and exact rank 51.
- All 1,192 direct owner rows pass, including 596 full-M16 rows and all 63
  cross-half residual sources.
- `D=457/4`, `P=1878008419901/9402974208`, and
  `2D-P=270571186627/9402974208>0`.
- The separately instantiated C133 box carrier is not the direct-demand
  potential: an exact countercell has carrier total zero and weighted direct
  demand `225/32768`.
- Both scale-4 terminal rows of the separately audited one-sided box carrier
  are nonzero, while the graph has no multiplier-16 channel.  This is only a
  mismatch for that carrier, not a generic direct-`M` terminal obstruction.

## Post-audit scope correction

The cumulative same-`M8/M16`-atom potential makes the C133 prefix increments
exactly `U8` and `U16`.  Its scale-4 terminal states vanish exactly on this
fixture because `16t=17745/2` exceeds the relevant block spans.  The actual
remaining finite obstruction is weighted price:

```text
D_weighted = 1305537/16384
2*D_weighted-P = -379481718413/9402974208 < 0
```

Therefore C136 remains a valid unweighted direct-owner feasibility witness,
but it is not a weighted C133 master.  The explanatory Markdown hash below is
superseded by the corrected hash recorded in the claim registry; the exact
certificate, JSON, oracle, and tests are unchanged.

## SHA-256

```text
explanatory MD      0cba40f97edb27b7dbfb8dcb4332809bfe90ecfee6d805f3ef48007fd2c3f17f
verifier            34255be33f926c848854e5fcd3ac340de06e7b09b3e284fd3ad2ddc9d2887f2c
certificate JSON    ac74cd6930a35d2c0b018741fb8b46b53db946eb3533f8b2e64d961e325ada53
certificate payload ed2717d3afc78ffca0ce523353796d2cd5658abfbde6ab998fa82bbff2ba1fc8
independent oracle  a13e75e86917b644ef846754d41ecbc362a7b1bb00883ce0c9284d4457cc994b
focused tests       7e1ed999e2f60b8a7154df76c3011eda619a72e38464ba6bdcf952faa9e30bdc
```
