# A71: three prescribed near-birth allowance comparisons

Date: 2026-09-09.
Status: NO_COUNTEREXAMPLE_FOUND_IN_THREE_PRESCRIBED_CELLS.

Only the certified C=1,m0=2,M=T=96 dense_variant1 history was used.
The three requested cells give the following exact values:

| (c,b,k) | Phi_H | Actual UG | Phi_H-UG |
| --- | ---: | ---: | ---: |
| (24,25,50) | 84,911,377 | 687,646,260 | -602,734,883 |
| (48,49,96) | 26,214,010,784 | 209,468,951,490 | -183,254,940,706 |
| (40,41,80) | 6,322,146,917 | 48,568,447,840 | -42,246,300,923 |

For each cell, both existing rational logarithm methods certify

    c^8*(log c)^5 > (k-1)^8,

equivalently k<ceil(c*(log c)^(5/8))+1. All strict lower margins are
positive and UNKNOWN=0. The full intervals are saved in the JSON.

The exact matching algorithm processes old gaps in decreasing order,
chooses the largest remaining future gap t<=H_c-g, and removes only
that selected gap. Larger currently infeasible gaps remain available
for later smaller g. The existing A70 hand proof gives exact optimality
under this one sum constraint. The calculation uses integer weights
and saves every right-node optimum. This does not extend the earlier
A70 cell's separate dual certificate to these different cells; that
certificate was not used as their numerical evidence.

The source history and its existing fixed-cap independent-check binding
were verified. Each cell's genuine lambda_k was recomputed with the
alpha_(k+1) subtraction and recorded separately from its allowance.
No history, original core record set, or full profile was generated or
scanned. No other cell was tested.

These three successes do not prove Phi_H<=UG for all near-birth cells.
They do not establish that any original strict-core record exists or
passes every other residual selector in the tested cells. Phi_H and
UG are upper allowances, not actual profile masses. The candidate and
the full CoreUniform/Q1 problem remain unresolved.

Evidence: A71_THREE_CELL_ADVERSARIAL.json, SHA256
f9da3e5f9ddcb4b622b8279ecad63ace3b5a7c060710adf1e62a42bcb6d4e3a2.
All source hashes, actual old/future inputs, rational intervals, node
values and exact ratios are included there. The bounded task is complete;
no process remains running.
