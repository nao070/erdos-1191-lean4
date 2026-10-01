# A73 independent fresh-tail review

Status: PASS as a hand-proved upper allowance and a bounded two-input arithmetic check. This does not close the original uniform norm.

## Exact hypotheses and coordinate recovery

Fix an actual integer Sidon history, a source birth c, a cut b>c, and a genuine component k. Put v=min(k,T), take old points a_1,...,a_(c-1), and future points f_1,...,f_m at ranks b+1,...,v. Keep the original strict core and any selected residual conditions at this particular (b,k); deleting records only restricts the argument.

Write the older source g=a_z-a_w (w<z<c) and fresh source h_x=a_c-a_x, with x<c and x distinct from w,z. At a fixed right mixed-sum vertex R=a_z+f_q, both orientations of a physical original record satisfy

    a_w+f_j = R+a_x-a_c.

Fixing x fixes an actual two-sum. Literal Sidon and separation of old and future index ranges determine w,j uniquely. Fixing w gives the actual positive difference f_j-a_x, so determines j,x. Fixing j gives the signed old difference a_w-a_x; it is nonzero because x!=w, and positive-difference uniqueness after orienting its sign determines w,x. The six-endpoint exclusion is essential to this last zero-difference exception. Thus the original records at this right vertex cannot repeat w, j, or x. No hypothetical edge is asserted to be an original record.

The positive boundary charge Beta uses h_x>g, so j<q and

    t=f_q-f_j>0,   h_x=g+t,   charge=g*t.

The statements below bound this positive charge, rather than the complete original product g*h_x or the other orientation's signed charge.

## Three-coordinate layer count

For positive integers u,v, let A_z(u) count w<z with a_z-a_w>=u, let B_q(v) count j<q with f_q-f_j>=v, and let C(u+v) count x<c with a_c-a_x>=u+v. The number of actual positive edges simultaneously satisfying g>=u and t>=v is at most

    min(A_z(u),B_q(v),C(u+v)).

The fresh restriction follows from the actual equality h_x=g+t; the three bounds can be combined because all three coordinate projections are injective. Enlarging the fresh bank to all x<c, including indices excluded for an individual source, is harmless for this upper bound.

Order all three lists decreasingly:

    G_l=a_z-a_l,  T_l=f_q-f_l,  h_l=a_c-a_l.

Integer layer cake, followed by min(A,B,C)=sum_l 1[l<=A,B,C], proves exactly

    Beta_zq <= sum_{l=1}^{min(z-1,q-1,c-1)} R(G_l,T_l,h_l),

where R(G,T,H) counts positive integer pairs u<=G,v<=T,u+v<=H. No simultaneous realization of the different layer maxima is needed or claimed.

For all nonnegative integer parameters, put choose2(n)=n(n-1)/2 for n>=0. Inclusion-exclusion gives

    R(G,T,H) = choose2(H)
             - choose2(max(H-G,0)) - choose2(max(H-T,0))
             + choose2(max(H-G-T,0)).

For example, violating u<=G means writing u=G+u' with u'>=1, which explains H-G without an extra shift. H=0 or 1 gives zero. Equivalently, r=max(0,min(G,H-1)) and f=min(r,max(0,H-T)) give

    R=f*T+(r-f)*H-[r(r+1)-f(f+1)]/2.

This latter row sum is an independent exact arithmetic check on the inclusion-exclusion formula.

Since R(G,T,H)<=G*T termwise, the total Psi_tail is at most the previous unrestricted Phi. It need not improve the constrained optimal matching allowance Phi_H: layerwise maximization is a relaxation, not an exact feasible matching calculation.

## Two existing inputs only

A70, fixed C=1,m0=2,c=24,b=25,k=48,M=T=96:

- All 529 nodes and 3,795 nonempty summands were recomputed using both integer formulas.
- Psi_tail=379,365,663; unrestricted Phi=1,181,503,640.
- The existing independent primal/dual certificate proves the exact Phi_H optimum is 80,331,512. Thus Psi_tail-Phi_H=299,034,151>0.

A72, fixed C=2^67,m0=2,c=24,b=25,k=M=T=50:

- All 575 nodes and 4,301 nonempty summands were recomputed using both integer formulas.
- Psi_tail=3,488,820,998,664,914,397,395,949,868,545,764,005,164,882.
- Unrestricted Phi=5,502,376,642,547,971,018,799,290,300,376,852,757,229,760.
- The already certified feasible matching lower bound is 2,498,101,079,407,809,411,484,738,706,689,307,741,019,104; its difference from Psi_tail is 990,719,919,257,104,985,911,211,161,856,456,264,145,778.
- This lower-bound comparison alone does not prove Psi_tail exceeds the A72 optimum. Such a statement would additionally require an optimality argument. The A70 exact optimum already suffices to reject automatic improvement.

Every node satisfied Psi_tail_node<=Phi_node. All input-declared source hashes matched. No logarithmic comparison was introduced; UNKNOWN=0 for this integer calculation. Existing history and matching certifications were reused by hash, with no new history, profile, original-record scan, or optimizer run.

## Prices and unresolved scope

This is a coefficient bound at the fixed actual component v=min(k,T). Multiplication by the original nonnegative lambda_k and finite summation over k is allowed with all selectors retained inside that sum. In particular, k>T components use the unchanged final output bank; no terminal alpha_(M+1) is reset. The computed auxiliary allowances assign no genuine price to a missing physical record.

The A70 inequality rejects the claim that this fresh-tail relaxation automatically sharpens Phi_H. It does not refute the fresh-tail upper bound, a different joint estimate retaining more information, the frozen U4F proposition, or Q1. No uniform square-root harmonic norm follows here.

## Evidence binding

- A73_FRESH_TAIL_EXACT.json: 055079ad581a28eac328b885a43f3d67145eb17c7a9aa0d9c8b34d5b7e67263c.
- A70_FEASIBLE_MATCHING_EXACT.json: 2dfe6fffed4d513d156023320f29cbd1cf4bb9e5efeb74c3d73e613eb9a64d39.
- A70_FEASIBLE_MATCHING_CHECK.json: 2f4acb79fa7c12d246f84aa4f6be8081854c67035cee55b84de06e2bac38248c.
- A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json: 5c43800cf7470ce5ce5fdb7b4974c4d68c0b4564c79a83d5fbab632d4ca4f87a.
- A72_SOURCE_ALLOWANCE_CHECK.json: f3d64eea70c6f90935c1cb55ca110f165698995af929ada146e92538b7d93b07.
- A70_GREEDY_MATCHING_REVIEW.md: afac0172050766a19527d94700167327069e5fb2fb2a4aa6e77b1d33356449e0.

The JSON also binds all original source files declared by the two certificates, and records exact row totals and calculation scope. The live WORKING_PROOF is concurrently owned by the root researcher and is not bound or edited by this standalone review.
