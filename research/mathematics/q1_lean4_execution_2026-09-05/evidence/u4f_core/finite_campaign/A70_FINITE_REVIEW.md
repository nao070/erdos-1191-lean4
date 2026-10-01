# A70 exact feasible-matching certificate: independent review

Date: 2026-09-09. Status: PASS_INDEPENDENT_PRIMAL_DUAL_AND_ACTUAL_ROW_CHECK.

Scope is the existing C=1,m0=2,M=T=96 history at c=24,b=25,k=48.
The old values are exactly ranks 1..23, the future values are exactly
ranks 26..48, and H_c=a24-a1=713. Only the 125 previously certified
A65-unpaid physical records are reused. No original core enumeration,
new history, other cell, full profile, or Lean build was performed.

## Complete finite optimality certificate

The independent checker imports no reference implementation and runs
no greedy or optimization solver. For every one of the 529 right nodes
(z,q), it reconstructs the whole N-by-N integer weight matrix, with
N=max(z-1,q-1), directly from the actual old/future coordinates:

    W_(w,j) = (a_z-a_w)(f_q-f_j), if w<z, j<q,
              and (a_z-a_w)+(f_q-f_j)<=713;
              0 otherwise, including dummy coordinates.

All 131,813 matrix inequalities dual_left[w]+dual_right[j]>=W_(w,j)
pass. Each assignment is a permutation. At every node, its assignment
weight, the explicit feasible real matching weight, and the total dual
value are the same integer. All primal/dual gaps are zero. The case
N=0 is checked with empty matching, permutation and duals and value 0.

This proves exact optimality without relying on the greedy implementation:
every partial feasible matching extends to a complete permutation of the
padded nonnegative matrix without reducing its weight. Dual feasibility
bounds the latter by the total dual value. The supplied real matching
attains that value. Individual dual variables need not be nonnegative;
the argument uses the complete permutation, not a partial sum of duals.

The existing hand theorem A70_GREEDY_MATCHING_REVIEW.md separately proves
the greedy algorithm for the same single-threshold feasible graph. The
finite certificate establishes the numerical optimum independently of
that algorithm's implementation.

## Actual records and exact totals

I reconstructed each saved physical row's old lower/upper endpoints and
its incoming mixed-sum node independently from the eleven-column row.
Both orientations satisfy the same recovered coordinate equation. The
positive orientation has j<q and g+t=h<=H_c, so it is a feasible edge
of that node's matrix. Every actual incoming coordinate matching has
distinct old and future lower coordinates. The actual positive charge
is at most the certified optimum at every node.

The exact totals are

    actual Beta = 8,716,524,
    Phi_H       = 80,331,512,
    actual UG   = 687,646,260,
    Phi         = 1,181,503,640.

Here U=58,548 and G=11,745. The actual residual product sum remains
21,922,039. Thus Phi_H is a strictly better positive-boundary allowance
than Phi and UG in this one prescribed cell. UG and Phi_H are upper
allowances; neither is identified with actual physical mass. In
particular this finite improvement is not a uniform norm theorem.

The original coefficient was independently computed as

    lambda48=(alpha48-alpha49)/H48^2
            =1/1148518878296832.

The exact component Phi_H allowance is 10041439/143564859787104.
The actual Beta component is 726377/95709906524736. These are fixed
component48 quantities. No original full u_r^[96] tail or alpha97 was
reset, replaced, or recomputed as a different finite price.

## Remaining mathematical boundary

The certificate optimizes precisely the constraint g+t<=H_c with unit
vertex capacities. It does not require g+t to be an actual fresh source
label, nor enforce all original six-endpoint and strict-core gates on
auxiliary matching pairs. Enlarging the matching graph gives an upper
bound and does not turn missing pairs into genuine priced records.

The full CoreUniform norm, an all-history improvement over UG, and
literal Q1 remain unproved. The exact existing-source and A65 bindings
were verified before computation. The checker exited 0; UNKNOWN=0.
All work is complete and no process remains running.

Checked artifact hashes:

- A70_FEASIBLE_MATCHING_EXACT.json:
  2dfe6fffed4d513d156023320f29cbd1cf4bb9e5efeb74c3d73e613eb9a64d39
- A70_FEASIBLE_MATCHING_CHECKER.py:
  1d6c235291717b4d1a72641b9e1dc1e150696da7d59fa8a3598ecd0c8935ce87
- A70_FEASIBLE_MATCHING_CHECK.json:
  2f4acb79fa7c12d246f84aa4f6be8081854c67035cee55b84de06e2bac38248c
- A70_GREEDY_MATCHING_REVIEW.md:
  afac0172050766a19527d94700167327069e5fb2fb2a4aa6e77b1d33356449e0
- A65_SPARSE_FIBER_FOLLOWUP_EXACT.json:
  0fca7f0a59c48f0694afca5b720aa4c4946ad2db2c3f853f69dd26c3917ca6e9
- C1_m02_dense_variant1_M96.json:
  d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e
