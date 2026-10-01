# Independent hand review of A66–A68

Date: 2026-09-09. Status: PASS; no mathematical correction required.
Scope is the three new sections and their stated finite A66 evidence.
No new history, record scan, Phi evaluation, build, or Skill invocation
was performed. The root independently handles the new Phi computation
and formal supporting theorem.

## A66: exact cancellation and the finite common-budget failure

For one fixed actual (c,b,k) selected graph and one old g component D,
h-g=sigma*t and t>0 give

    sum_edges g*max(h-g,0) = (g/2)*(B_D+sum_edges t).

Every cycle has B_D=0. Thus including cycles in the difference of
positive edge and positive path-boundary sums is valid and yields

    Beta-Bplus = (1/2)*sum_D g*(sum_edges t-|B_D|) >= 0.

The factor 1/2, the absolute value, and the nonnegative sign are all
necessary and correct. The original product mass remains
sum_D g^2*L_D + sum_paths g*B_D. It is not equal to the positive
boundary mass alone. Multiplication by each original lambda_k and
finite summation preserve these identities on the actual graph at k.
No single full u_r is assigned to a path whose edges or selectors change.

The displayed 14 finite violations and the x10/x13 values agree with
A66_BOUNDARY_EXACT.json and its independent checker. In the prescribed
125-record cell, Beta=Bplus=8,716,524 and Q=21,922,039; the exact
cancellation slack is zero there. Every single-edge parabola bound
still holds. This refutes beta_x<=h^2 in that actual residual cell,
without disproving arbitrary constants or a uniform full-core norm.

## A67: both orientations enter one actual translation graph

The old and future value domains are disjoint and ordered. Literal
repeated-two-sum Sidon therefore makes (old point,future point) -> sum
injective: the crossed equality alternative would identify an old
point with a future point. Hence the mixed-sum vertex set has exactly
nm elements.

Writing the old source as g=a_z-a_w>0, the positive orientation gives
(a_z+a_r)-(a_w+a_i)=g+t=h; the negative orientation gives
(a_z+a_i)-(a_w+a_r)=g-t=h. Thus both maps use the same positive
fresh-shift set H. Recovering each mixed sum recovers its actual old
and future endpoints; the order of those two future endpoints fixes
the orientation. The shift h then recovers the fresh lower x. There
is consequently no missing orientation factor or duplicate record in
this injection.

The set H inherits unordered two-sum uniqueness by subtracting from
2a_c. In a bipartite rectangle the four shifts obey
h11+h22=h12+h21. The two Sidon alternatives respectively collapse
the two right or the two left vertices. This proves C4-freeness of
the enlarged translation graph, and therefore of the actual subgraph.

For N=nm>=1, pair counting gives sum d(d-1)<=N(N-1). Cauchy gives
E^2<=NE+N^2(N-1), whose nonnegative root is the stated
N*(1+sqrt(4N-3))/2. The existing fresh/output count is
2n*binom(m,2)=nm(m-1); the old-g count is binom(n,2)*m.
Both constants are correct. The two cases m<=n and m>=n show that
their minimum is <=N*sqrt(N), while the new root is >=N*sqrt(N).
Thus the generic C4 bound is numerically dominated as claimed, even
though the physical representation itself remains useful. Empty
domains give zero records and are excluded from the square-root step.

## A68: coherent stars, recovery, and weighted matching

The new-row sum a_c+f_j cannot equal any old-row sum a_w+f_q by
literal Sidon and old/future separation. Thus W is disjoint from V.
Each of its n forced incidences has shift a_c-a_x in H, and the
corresponding left stars partition V by future position. C4-freeness
is unaffected by adding these right vertices because the shift set
remains the same. A right vertex in V cannot have two neighbors in
one star group. It cannot have an original incoming edge from its
own future group either: that would equate a wholly old difference
with a fresh difference ending at c. Positive-difference uniqueness
would require the same endpoint pair, contrary to z<c.

For fixed right vertex a_z+f_q, both source orientations satisfy

    a_c+a_w+f_j = a_x+a_z+f_q.

Fixing w fixes the positive mixed difference f_j-a_x, which uniquely
recovers (j,x). Fixing j fixes the signed old difference a_w-a_x.
It is nonzero because the original six-distinct condition excludes
w=x. Nonzero signed-difference uniqueness recovers (w,x), regardless
of that difference's sign. The fixed-right incoming records therefore
form an actual matching between w<z and j!=q. The formula

    m*sum_(z=1..n) min(z-1,m-1)

equals m(m-1)(n-m/2) for m<=n, and mn(n-1)/2 for m>=n.
At m=n the formulas agree; empty or singleton future domains contribute
zero. This is a count upper bound, not an unproved uniform contraction.

For Beta only h>g contributes, so j<q and the weight is
(a_z-a_w)*(f_q-f_j). The old and future gap lists are positive and
decrease as their respective lower ranks increase. An actual matching
of any size is bounded by matching the largest available values in the
same order. The exchange increment (G1-G2)*(T1-T2) is nonnegative;
adding missing pairs in the enlarged complete matching also increases
the bound. Consequently the displayed sum over l<=min(z-1,q-1) is
valid.

Interchanging these finite sums gives exactly

    Beta <= sum_l [sum_(z>l)(a_z-a_l)]
                  [sum_(q>l)(f_q-f_l)] = Phi(O,F).

Combining with A66 gives Bplus<=Beta<=Phi. The expression Phi is a
numerical common allowance obtained by enlarging matchings; its summands
need not be feasible original records. The proof does not assign such
missing records genuine prices. Multiplying the inequality by the
actual nonnegative lambda_k is an upper-bound operation, with every
original k>T term retained. Even when v=min(k,T) is fixed, the actual
selected graph may still depend on k; the left side keeps that dependence.

The simple endpoint envelope follows from
O_l<=(n-l)H_c and F_l<=(m-l)H_F. It loses the actual tail gaps and
the source feasibility equation g+t=h. Its comparable-window cubic
count scale supplies no global uniform norm by itself. In particular,
neither the sum over old g nor the sum over different cuts is treated
as independent copies of a physical budget.

## Remaining scope

These conclusions are new hand results. This review does not claim
that the complete graph constructions, rearrangement, genuine-price
sum, or full norm are Lean-verified. The whole frozen CoreUniform
estimate, literal Q1, and final clean dependency closure remain open.
The exact source/section and finite-evidence bindings are recorded in
A66_A68_review_manifest.json. The bounded review is complete, with no
process left running.
