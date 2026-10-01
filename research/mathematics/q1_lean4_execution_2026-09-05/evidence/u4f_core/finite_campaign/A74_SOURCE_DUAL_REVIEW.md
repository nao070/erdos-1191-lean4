# A74 independent source-charge / matching review

Status: PASS as a hand-proved upper bound for the positive boundary charge Beta at one fixed actual (c,b,k). No A74 finite optimization certificate is inspected or certified by this note.

## Definition and exact range

Use an actual integer Sidon history, c<b, v=min(k,T), old points a_1,...,a_(c-1), and future points f_1,...,f_m at ranks b+1,...,v. Original strict gates and any selected residual conditions remain fixed at this (b,k). An actual positive boundary record has old g=a_z-a_w>0 with w<z<c, fresh h_x=a_c-a_x>g with x<c distinct from w,z, and output t=f_q-f_j=h_x-g>0, j<q. Its positive boundary weight is g*t, not its complete original product g*h_x.

Define the auxiliary source bank, using each actual source triple once,

    Bsrc = sum_{w<z<c; x<c; x!=w,z} g*max(h_x-g,0).

This bank includes source triples without an actual output or a surviving original record. It is an auxiliary upper allowance, and none of those absent records is assigned a genuine output price.

At fixed right node (z,q), consider w<z and j<q. Set g=a_z-a_w, t=f_q-f_j. Among actual fresh h_x with x<c, x!=w,z and h_x>=g+t, let hmin be the least. If this set is empty, the candidate edge is absent. For a fixed real theta in [0,1], define

    Wtheta(w,j) = max(g*t-theta*g*(hmin-g),0).

Let Mtheta(z,q) be the exact maximum weight of a partial matching on these candidate edges, with each w and each j used at most once, and put

    Dtheta = theta*Bsrc + sum_(z,q) Mtheta(z,q).

## Proof of Beta <= Dtheta

First, a physical source triple (w,z,x) determines g, h_x, and t=h_x-g. Actual Sidon positive-difference uniqueness determines the output pair (i,r), hence also the positive orientation's node (z,q) and left future coordinate j. Thus a physical source triple can be used at most once across all right nodes of this component. Selecting fewer original records preserves this injection. This is the needed common source budget; it is not independently reset at each node.

Second, an actual positive edge has the fresh label h_x=g+t in the defining candidate set. All candidate labels are >=g+t, so its hmin is exactly h_x. Consequently

    Wtheta(actual edge)=(1-theta)*g*t.

The actual positive edges at each fixed right node form a matching by literal Sidon and the six-endpoint exclusions, as in the A73 coordinate-recovery proof. Hence their residual weight is <=Mtheta(z,q). Summing the exact identity

    g*t = theta*g*(h_x-g) + Wtheta(actual edge)

over actual positive records, the first sum is <=theta*Bsrc by source-triple injection and theta>=0; the second sum is <=sum Mtheta. This proves the claimed bound.

## Endpoints and optimization scope

At theta=0, an allowed edge has g+t<=hmin<=H_c=a_c-a_1. Its weight is g*t. The candidate graph is therefore a subset of the A70 feasibility graph, so

    D0=sum M0(z,q) <= Phi_H.

The missing endpoints in the fresh bank may make this subset proper. Equality with Phi_H is not claimed.

At theta=1, hmin-g>=t forces W1=0 on every candidate edge. Thus all node maxima are zero and D1=Bsrc, including empty nodes. No actual mirror or output existence is required for this identity.

For an interior theta, these weights and the source-dependent fresh exclusions are not the unmodified A70 threshold product matrix. The A70 descending greedy theorem must not be applied without a new proof. Exact arbitrary-weight matching, or a checked assignment primal/dual certificate, is appropriate. For theta=p/d with integers d>0 and 0<=p<=d, use the nonnegative integer matrix

    max(d*g*t-p*g*(hmin-g),0).

If its node optimum is V_zq, then

    d*Dtheta=p*Bsrc+sum V_zq.

Dummy or forbidden entries may be encoded by zero weights with free unmatched vertices. A primal matching plus a covering assignment dual of equal value can certify the maximum. This note establishes the mathematical inequality; it does not certify any supplied A74 node matrices or values before their independent checks.

## Convex minimization certificate

PASS for the additional exact one-variable minimization logic. The candidate edge set, hmin, and Bsrc are independent of theta. Write A_e=g*t and C_e=g*(hmin-g). Since unmatched vertices are allowed, maximizing the clipped weights max(A_e-theta*C_e,0) is equivalent to maximizing the raw linear weights A_e-theta*C_e over partial matchings: any negative selected edge can be deleted, and selected zero-weight edges can be discarded. Consequently

    Dtheta = max_J [A_J+theta*S_J],
    A_J=sum_(e in J) A_e,
    S_J=Bsrc-sum_(e in J) C_e,

where J chooses one feasible partial matching independently at each node. There are finitely many choices, so Dtheta is continuous, convex, and piecewise linear on [0,1]. This is a statement about the upper allowance Dtheta, not the actual record mass.

An oracle's optimal positive edges at theta0 produce a fixed affine line A_J+theta*S_J which is <=Dtheta for every theta, and which equals Dtheta0 at theta0. Omitting zero edges at the oracle does not affect this equality. Even where one of those fixed edges later has negative raw weight, its line remains a lower bound; the allowance can discard that edge.

At the left endpoint, a touching line with S_J>=0 proves Dtheta>=D0 for all theta in [0,1]. Thus theta=0 is globally optimal. Symmetrically, a touching line at theta=1 with S_J<=0 certifies the right endpoint.

For two lower-support lines with strictly opposite slopes, their maximum attains its global minimum at their intersection, provided that intersection theta* lies in [0,1]. If a feasible-matching/assignment-dual oracle independently certifies Dtheta* equals the common line value exactly, that value is the global minimum of Dtheta on [0,1]. Merely intersecting two lines without this equality gives a lower bound on the minimum, not its attainment. Intersections outside [0,1] require the corresponding endpoint argument; a zero-slope touching line already gives a global lower bound attained there.

All these checks can be rational/integer: at theta*=p/d, the matching matrices and dual objective are scaled by d. This hand argument does not certify the newly produced A74 numerical files or any optimizer's termination; those require their own exact certificate checks. No additional finite computation was run for this extension.

## Original prices and remaining gap

For each fixed component this is an inequality for the actual selected graph with v=min(k,T). It may be multiplied by the same nonnegative genuine coefficient lambda_k=kappa_k/H_k^2 and then summed finitely over k; k>T components and all component-dependent selectors remain present. It does not authorize replacing the original u_r^[M] by a single path/node price or setting alpha_(M+1)=0.

Bsrc is common across right nodes at this fixed c,b,k. Its reuse as an independent budget across different cuts or components has not been justified by this argument. The bound controls Beta only. Combining it with signed-boundary or base-product identities still requires their actual hypotheses, and no complete Q, uniform square-root harmonic norm, frozen U4F, or Q1 conclusion follows here.

## Source binding and actual work performed

This is a bounded independent hand review of the parent's A74 candidate, using the already verified coordinate recovery and A70 optimization scope. No new history, record enumeration, profile, optimizer, Lean build, or mathematical-source edit was performed.

- A73_FRESH_TAIL_REVIEW.md: fd4dec73116389fb7d71ec61bba883a7a0751b6512a167364994568302e2d1d1.
- A73_FRESH_TAIL_EXACT.json: 055079ad581a28eac328b885a43f3d67145eb17c7a9aa0d9c8b34d5b7e67263c.
- A70_GREEDY_MATCHING_REVIEW.md: afac0172050766a19527d94700167327069e5fb2fb2a4aa6e77b1d33356449e0.

The parent is concurrently integrating the live WORKING_PROOF; this standalone review does not bind or edit that changing file.
