# A70: exact maximum matching with one sum constraint

Date: 2026-09-09. Status: HAND-PROOF PASS.

Let G and T be finite indexed lists of positive real numbers and H a
fixed real threshold. Distinct list positions are distinct vertices,
even if their values agree. Every pair (g,t) with g+t<=H is feasible,
and there are no further edge restrictions. A matching uses each
vertex at most once and has weight sum g*t. Partial matchings are
allowed.

The following greedy procedure attains the exact maximum weight:
process the remaining g values in decreasing order; for each g choose
a largest remaining t satisfying g+t<=H, if one exists, and remove
those two vertices. Otherwise leave g unmatched. An infeasible t is
retained for later smaller g values; it is not deleted.

## Exchange proof, including unmatched cases

A maximum exists because there are finitely many matchings. Let g be
a maximum remaining left value. If it has no feasible t, every matching
leaves it unmatched and the greedy step is forced.

Otherwise choose the largest feasible t*. Starting from any optimal
matching, there is an optimal matching containing (g,t*):

1. If that edge is already present, there is nothing to change.
2. If g is matched to t' and t* is unmatched, replace (g,t') by
   (g,t*). Feasibility of t' implies t'<=t*, so weight does not decrease.
3. If g is unmatched and t* is matched to g', replace (g',t*) by
   (g,t*). Since g>=g', weight does not decrease. The old g' may be
   left unmatched; partial matchings are allowed.
4. If both g and t* are unmatched, add (g,t*). This is feasible and
   increases weight because the values are positive. In particular
   this case cannot occur in an optimum, but gives the required
   improvement from an arbitrary matching.
5. Otherwise g is matched to t' and t* to another g'. Replace those
   edges by (g,t*) and (g',t'). The first is feasible by choice. The
   second is feasible since g'+t'<=g'+t*<=H. The gain is exactly

       (g-g')*(t*-t') >= 0.

These cases concern indexed vertices, so ties cause no exception.
For example distinct t vertices of the same value can be exchanged
with zero gain. Thus some optimum contains the greedy edge. Removing
that edge leaves an optimum on the remaining vertices: a strictly
better remainder would improve the original optimum. Induction proves
the entire greedy procedure optimal.

The proof crucially uses that ALL pairs satisfying the single threshold
are permitted. It does not prove greedy exactness when edges also require
membership of g+t in a prescribed discrete fresh-source set, six-endpoint
exclusions, or other core gates; the swapped edges might then be missing.

## Application to the actual A68 positive charges

At each fixed right vertex (a_z,f_q), the actual positive records form
a matching between old gaps g=a_z-a_w and future gaps t=f_q-f_j with
w<z and j<q. Every such record satisfies

    g+t=h=a_c-a_x <= H_c.

Hence this actual matching is a submatching of the graph in the theorem
with threshold H_c. Let M_H(z,q) denote its threshold-constrained
maximum and Phi_H=sum_(z,q) M_H(z,q). Then

    Bplus <= Beta <= Phi_H <= Phi.

The final inequality holds because the constrained feasible graph is a
subgraph of the unrestricted matching problem used in A68. The greedy
formula can compute each M_H exactly. It does not establish Phi_H<=UG
for all histories, nor a uniform norm bound.

The expression Phi_H is an upper allowance. Its selected pairs need
not represent physical core records or actual fresh labels. Only the
original actual records receive original genuine prices. At every fixed
k the nonnegative inequality may be multiplied by lambda_k; summing
keeps all actual k>T components and the nonreset alpha_(M+1). It does
not assign one u_r to an auxiliary matching or to a changing path.

This note proves only the matching theorem and the stated upper-bound
application. The root's separate exact finite Phi_H certificate is not
reproduced here, and its reported number is not needed in the proof.
No finite scan, new history, profile, external theorem, or Lean build
was used for this hand review. Full CoreUniform and Q1 remain open.
