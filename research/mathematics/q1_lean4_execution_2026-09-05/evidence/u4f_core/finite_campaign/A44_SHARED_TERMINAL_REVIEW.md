# A44: shared-terminal counterexample and corrected row transport

Date: 2026-09-09. Independent bounded finite certification and hand review.
Status: PASS within the stated scope. U4-F and Q1 remain unresolved.

## Frozen finite input and exact scope

Use only the previously certified `C1_m02_dense_variant1_M96.json`, with fixed
C=1, m0=2, M=T=96. The sole prescribed cell is cut b=25, component k=48,
and the sole shared physical terminal is (old x=1, future i=42).
Here a1=1, a42=2975, V=a42-a1=2974, H25=773, H48=4248, and

    lambda48 = kappa48/H48^2 = 1/1148518878296832.

The reference check filters the existing A29 pool and reads the selected
original record-bank indices. The independent checker reconstructs exactly
the prescribed 138 pairs y=2,...,24 and r=43,...,48 from integer endpoints.
It does not generate a history or enumerate a full profile. Its statuses are
123 nonpositive e, 5 positive e not in the old difference bank, and 10 strict
core edges. Both original-gate and all-large-gap comparisons use rational
log enclosures, with no UNKNOWN comparisons. Existing all-rank Sidon/cap
certification is bound by content hash rather than rerun.

Record columns are [d,e,x,y,w,z,c,s,i,r,t]. Every listed edge has
d=a_y-a_x>e=a_z-a_w>0, t=d-e=a_r-a_i, six distinct endpoints, original
strict gates, and its original cut coverage c+1,...,i-1. Since x=1, the
vertex (1,42) is terminal for each individual fixed-e strict graph.

| original bank index | y | r | e | (w,z) | d | t | de | all large old gaps |
|---|---:|---:|---:|---|---:|---:|---:|---|
| 3127 | 17 | 43 | 20 | (5,7) | 311 | 291 | 6220 | no |
| 3910 | 18 | 43 | 59 | (8,11) | 350 | 291 | 20650 | yes |
| 3906 | 18 | 44 | 36 | (12,13) | 350 | 314 | 12600 | yes |
| 4984 | 19 | 43 | 109 | (12,15) | 400 | 291 | 43600 | yes |
| 4981 | 19 | 44 | 86 | (6,11) | 400 | 314 | 34400 | yes |
| 5944 | 20 | 44 | 126 | (14,17) | 440 | 314 | 55440 | yes |
| 9681 | 22 | 43 | 312 | (10,19) | 603 | 291 | 188136 | yes |
| 11006 | 23 | 44 | 338 | (5,18) | 652 | 314 | 220376 | no |
| 12711 | 24 | 43 | 422 | (6,20) | 713 | 291 | 300886 | yes |
| 12710 | 24 | 44 | 399 | (2,19) | 713 | 314 | 284487 | no |

All strict edges: count 10, sum de=1166795, sum e=1907, distinct y=7,
distinct r=2, distinct e=10. The exact priced mass is
166685/164074125470976. All-large subset: count 7, sum de=655712,
sum e=1150, distinct y=5, distinct r=2, distinct e=7, priced mass
20491/35891214946776. Full by-y sums and each exact gate margin are stored
in `A44_SHARED_TERMINAL_EXACT.json`.

## Precisely rejected matching candidates

Across different shifts e, these incoming first edges need not form a
matching in (old y, future r). The lexicographically first repeated-y
witness consists of original rows

    [350,59,1,18,8,11,18,11,42,43,291]
    [350,36,1,18,12,13,18,13,42,44,314].

Both are all-large. Their mixed tails 2915 and 2938 enter V=2974 with
different shifts 59 and 36. A repeated-r witness inside all-large is
indices 3910 and 4984, with respective (y,r,e)=(18,43,59),(19,43,109).
Thus both row and column matching restrictions fail even in that subclass.
This does not assert a two-edge chain in one fixed-e graph; the earlier
finite observations about fixed-e matching are a different statement.

The authorized further check only reclassifies these saved ten edges.
The two independent rational log enclosures certify

    L25=floor(625/(log25)^(5/4))=144,
    floor(25/(log25)^(3/4))=10,
    ceil(25*(log25)^(5/8))=52.

The first identity is proved using
144^4*(log25)^5 <= 625^4 < 145^4*(log25)^5; the others use the
corresponding fourth/eighth-power integer comparisons. Thus 35<48<53 is
inside the A43/A42 central band. Also H48=4248<773*(log25)^2, so this
component is A33 near-span.

After e>144 and all-large selection, indices 9681 and 12711 remain:
(y,r,e,de)=(22,43,312,188136),(24,43,422,300886). Their sum de is 489022
and sum e is 734. The column r=43 is repeated; old y is not repeated.
`A44_SHARED_TERMINAL_REMAINDER_EXACT.json` preserves these decisions.

The subsequent A46 check is even narrower: only these two saved rows are
tested against J25=floor(625/(log25)^(5/2))=33. Index 9681 has old gaps
(88,312,203) and t=291, so remains. Index 12711 has gaps (18,422,273)
and t=291, so is paid by the small-old-gap subclass. Exactly one edge
remains in this cell/terminal after all those restrictions. The earlier
two-edge counterexample does not refute matching in this final smaller
remainder. This single survivor does not prove such matching either.

## Correct replacement: a different fixed-row source graph

Fix cut b, n=b-1, H0=H_(b-1), a source pair (x,y), its d=a_y-a_x,
and lower output i. For varying valid upper outputs r, write
e=d-(a_r-a_i)=a_z-a_w. View each such old source as a directed edge w->z
on the old vertices excluding x,y.

Two distinct edges cannot have the same w: their e difference would be
both a difference of two old z-values and the equal positive difference
of the two future output values. Actual positive-difference uniqueness
forbids this. The same argument forbids a repeated z. Equality of e
would already force equality of r. All edges increase old rank, so this
is a disjoint union of directed paths, with isolated vertices allowed.

Let the remaining n-2 old values be b1<...<bN, N=n-2, and put j=floor(N/2).
Define T_xy as the sum of the largest j values minus the sum of the
smallest j values. Along each path the sum of e telescopes to its endpoint
span. Path starts and ends are distinct, so their number is at most j.
Consequently

    sum_edges e = sum_paths(endpoint span)
                <= T_xy <= floor((n-2)/2) H0.

This is the graph for fixed (x,y,i), across shifts e. It is not A41's
graph for one fixed e across mixed vertices. Its no-branching property
does not restore matching in y or r across different d rows.

At each genuine component, the row's exact unpriced weight is
d times its current sum e. Integrating against the original lambda_k,
then relaxing the entire row transport to T_xy and all upper births to
i+1, gives the valid hand-proof bound

    P_b <= (sum_old d) floor((n-2)/2) H0
             * sum_{i=b+1}^{T-1} u_(i+1)^[M]
        <= n^2 floor((n-2)/2) H0^2
             / [12 (b+1)^3 H_b^2] < 1/24.

Use sum_old d<=n^2 H0/4, u_r^[M]<=alpha_r/H_b^2, and
sum_{r=b+2}^infinity alpha_r<=1/[3(b+1)^3]. For n<4 the six-endpoint core
is empty and should be treated as such rather than applying a negative
combinatorial factor. No output price is reset, and k>T still contributes
the same genuine tail. Dropping the detailed row transport, actual births,
and endpoint spans leaves a constant pointwise bound; its square-root
harmonic sum is not uniformly controlled.

## Evidence, limitations, and next action

Exact finite checks: the one prescribed 138-candidate cell, then saved
10-row and 2-row subclassifications only. The A46 subclass script's first
run stopped at a JSON-key typo; changing `record` to `original_record`
produced the saved successful run. No mathematical comparison was replaced.
No process, search, or build is left running. Row transport above is hand
review only; this note makes no Lean claim.

All original gates, six endpoints, genuine prices, and the fixed C/m0 are
retained. This refutes specified finite matching shortcuts and verifies a
replacement row bound. It neither refutes U4-F/Q1 nor controls the full
remaining norm. The next nonduplicate action is to retain the joint
terminal/source transport in the remaining component strip, using the
A45/A46 small-value payments rather than continuing terminal searches.
Content hashes for sources, all scripts, exact evidence, and this note are
in `A44_A46_review_manifest.json`.
