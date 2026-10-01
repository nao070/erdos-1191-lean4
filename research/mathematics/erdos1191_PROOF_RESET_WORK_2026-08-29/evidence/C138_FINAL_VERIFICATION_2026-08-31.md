# C138 final verification — 2026-08-31

Status: `EXACT_FIXED_PHASE_SAME_ATOM_WEIGHTED_GRAPH_FEASIBLE_C058_OPEN`

The canonical verifier, its mutation suite, six focused tests, and a
stdlib-only independent reconstruction all pass. The accepted computation
uses exact rational arithmetic; numerical discovery coefficients and solver
status are not evidence.

Exact frozen result:

- fixture: the explicit C132 32-mark Golomb ruler;
- phase: `t=17745/32` only;
- channels/roots: 100 channels, 4,950 candidate roots, 57 positive stored
  roots, exact graph rank 51;
- weighted owner rows: 1,192, with 884 tight and 308 strict;
- current-owner capacity census: 807 zero and 385 positive;
- direct-demand sign census: 40 negative, 971 zero, 181 positive;
- pre8/rank-7 owner: 149 nonnegative rows, 145 zero and 4 positive, integral
  `6489/256`;
- weighted demand `D=1305537/16384`;
- single unweighted physical price
  `P=2367807877181/16716398592`;
- exact positive margin
  `2D-P=296239592131/16716398592`.

The potential is not free: `C8=B`, `C16=B+U8`, and
`C32=B+U8+U16`, with the finite fixture using the reconstructed direct
epoch-4 atom for `B`. The verifier checks 2,020 same-atom increment equalities
and the exact C133 identity on 202 cells. All fourteen formal rows are
retained, including both upper terminals; only five integrated rows are
nonzero. The two same-M scale-4 terminals are checked pointwise and are
exactly zero. Therefore `2D-P` is valid only in this frozen zero-terminal
instance; no terminal is silently discarded.

The graph price is never epoch-weighted a second time. The weights
`w8=1,w16=9/16` occur only on the owner-demand right-hand sides and in `D`.
All coordinate fibers, including pre8/rank 7, recover the one physical price.

Fresh reproduction from `route_probes/`:

```text
MUTATION_OK rejected=14/14
C138_EXACT_OK phase=17745/32 roots=57 rank=51 owner_rows=1192
tight=884 strict=308 D=1305537/16384
P=2367807877181/16716398592
margin=296239592131/16716398592 C133_cells=202
formal_rows=14 nonzero_rows=5 terminals=0/0 pre8=nonnegative
fixed_fixture_only C058_open

Ran 6 tests in 8.539s
OK

INDEPENDENT_C138_OK roots=57 rank=51 rows=1192
D=1305537/16384 P=2367807877181/16716398592
margin=296239592131/16716398592 ledger_cells=202
increment_checks=2020 terminal_checks=606 formal_rows=14 C058_open
```

Canonical SHA-256 values:

```text
report       49a12cdd3bda8b91ce23ea1aa00d10beaaf40f1395592e8cf27eda3747e290ef
verifier     b97c893d925bfddc03533c799f39e86b4a447095f5aaacbc26b85c8056acc365
certificate  9008c8639f13906abfb4866f8fa6e7b260c9e2fed76804656e1f773d534e70b9
payload      2dcd5099a449587a27cddbea0785ef862c73e62e90573bfb39c3f3776f9fd760
oracle       3f4dbb14f41b94c8cb6ee84a79161ddd80afc20d25d9f644921aa55f94ae63e3
test         800416302c2c473877a10955a83024eef1a1296be1c74c3563bc19673a333c2e
Lean module  97607dd6425a93a2845e8c55e55c5b106e61ed6d2f2fbd61de06c764ff68e0c9
```

The frozen cumulative same-atom ledger is also independently checked by Lean
4 in `Erdos1191/SameAtomAdjacentLedger.lean`. `lake build` completed 1,070
jobs; its audit reports only `propext`, `Classical.choice`, and `Quot.sound`.

Scope boundary: this proves one exact fixed-fixture, fixed-phase weighted
master in the declared graph-root cone. The boundary instance is degenerate:
all four integrated A8 rows and both terminals vanish. It proves no phase
interval, nonanticipating phase rule, nonzero-history/terminal case, global
C103 owner/boundary ledger, arbitrary history or rank, C058, Q1, Q2,
publication novelty, or prize eligibility. Global status remains
`UNRESOLVED_AT_HARD_LIMIT`.
