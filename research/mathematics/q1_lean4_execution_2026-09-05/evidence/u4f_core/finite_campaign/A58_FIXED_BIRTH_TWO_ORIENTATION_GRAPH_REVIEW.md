# A58 independent review: fixed-birth future graphs, both source orientations

Date: 2026-09-09. Status: PASS independent hand review, with the component-selector indexing qualification below. No finite computations, history generation, record-pool or profile scan, Lean run, cap-weighted estimate or redelegation was performed.

## Exact hypotheses

Let a_1<...<a_M be an actual positive integer Sidon history in the literal repeated-sum sense of lean/Q1/Target.lean: equality of two sums of two set elements implies equality of the unordered two-element multisets, including repeated summands. Let T<=M. Fix the source birth c, and use only original strict-core records with four distinct old endpoints, two distinct future endpoints c<i<r<=T, and six distinct endpoints in all.

Original strict rank and physical gates remain imposed; the degree proof does not discard them as assumptions on a constructed example. Instead it proves an upper-structure statement that remains valid after deleting edges. The fixed C,m0 and all-rank cap, if imposed, are unchanged but unnecessary for this review.

Two direct consequences of literal Sidon are used:

1. A positive difference determines its ordered endpoint pair. Indeed a_q-a_p=a_r-a_s>0 gives a_q+a_s=a_r+a_p. The nonmatching branch would force a_q=a_p, contradicting positivity.
2. A mixed sum of one old value of rank<c and one future value of rank>c determines both endpoints. The unordered swap branch is impossible because the old and future values lie in disjoint ordered ranges.

No zero-difference recovery or unspecified choice of endpoint orientation is used.

## Larger source new, smaller source fixed and old

Fix e=a_z-a_w>0 with w<z<c. For each allowed x<c distinct from w,z, a physical record has

    d=a_c-a_x>e, t=d-e=a_r-a_i>0,
    a_x+a_r=a_c-e+a_i.

Represent it by a directed edge i->r labeled x on the actual future ranks c+1,...,v. There are no loops because i<r.

If two edges share lower output i, then a_x+a_r is the same mixed sum. Literal Sidon and old/future ordering give the same x and r, hence the same record. Thus outdegree<=1.

If two edges share upper output r, then a_i-a_x=e+a_r-a_c is the same positive mixed difference. It is positive because a_i>a_c>a_x (also e>0 and a_r>a_c). Positive-difference uniqueness gives the same i,x, hence the same record. Thus indegree<=1.

If x repeats anywhere, the fixed positive output label t=a_c-a_x-e repeats. Actual output difference uniqueness gives the same i,r. Therefore each allowed x labels at most one edge globally in this fixed(c,e) graph, and total edges<=c-3 after excluding the two old source endpoints.

A finite directed graph with these degree bounds and strictly increasing future ranks along edges has no cycles. Its nontrivial components are directed paths; isolated vertices contribute zero. For a path with future ranks v_0<...<v_L, put T_path=a_(v_L)-a_(v_0). Each edge has d=e+t, so exactly

    sum_path de=e^2 L+e sum_j(a_(v_j)-a_(v_(j-1)))
               =e^2 L+e T_path.

## Smaller source new, larger source fixed and old

Fix d=a_y-a_x>0 with x<y<c. A record now has e=a_c-a_w with w<c distinct from x,y, 0<e<d, and

    t=d-e=d-a_c+a_w=a_r-a_i>0.

Represent it by i->r labeled w. For fixed i,

    a_r-a_w=d-a_c+a_i>0,

so positive mixed-difference uniqueness determines r,w; outdegree<=1. For fixed r,

    a_i+a_w=a_r-d+a_c,

and mixed-sum uniqueness with w<c<i determines i,w; indegree<=1. Repeated w would repeat the positive output label t and hence the same actual output pair. The same path decomposition and total-edge bound<=c-3 hold.

On a path, e=d-t. Thus the exact unpriced mass is

    sum_path de=d^2 L-d T_path.

Every summand is positive. In particular T_path<dL for a nonempty valid path, so the negative span term introduces no negative record price. The two graph orientations have different recovery equations; no unverified symmetry is used.

## Exact full genuine-price representation

Let lambda_k=(alpha_k-alpha_(k+1))/H_k^2 and u_r^[M]=sum_{k=r}^M lambda_k. For an unselected original fixed-source graph with output horizon T, finite rearrangement gives

    sum_edges de*u_r^[M]
      =sum_{k=c+2}^M lambda_k
         sum_{edges with r<=min(k,T)}de.

At each component k, apply the above path balance to the ACTUAL graph at v=min(k,T). Its paths may have different spans or lengths from the final graph. No whole path is assigned one arbitrary u. For example, on a final larger-new path, the exact original price is e^2 sum_j u_(v_j)^[M]+e sum_j(a_(v_j)-a_(v_(j-1)))u_(v_j)^[M], with upper output ranks retained separately.

For a fixed cut b, keep exactly c<b<i. The contributing graph has vertices b+1,...,v, with no edges if v<=b or c>=b. If a remaining-class selector depends on b or k, write the graph as G_(b,k), with v=min(k,T), and retain that selector INSIDE the k sum. It cannot in general be replaced by a graph depending only on v: for k>T, v=T is frozen while a component-dependent selector may still change. All selected graphs are subgraphs, so the degree and unpriced path balances survive; paths can split when edges are deleted.

The original k>T price tail and alpha_(M+1) are preserved. A finite sum of component balances is an identity, not an independent bank for each cut, component or path.

## Matching question and remaining gap

Indegree<=1 and outdegree<=1 permit a vertex to be the upper endpoint of one edge and the lower endpoint of another. Such a two-edge through-path is compatible with these proved structural restrictions. They therefore do not imply that the graph is an undirected matching. This review neither constructs an actual strict-core two-edge counterexample nor proves one impossible; general matching for these fixed-birth graphs remains unproved here. No new finite task was authorized or run.

The conclusions are exact graph/recovery/price identities, not a cap-weighted summable estimate, CoreUniform or Q1. Parent owns the next cap/norm analysis; it is not duplicated here.

## Source bindings

The literal Sidon definition and the contract's actual one-copy record conventions were read in their minimal relevant dependency range. Prior full-price/source-count review and final proof binding are reused as immutable provenance. SHA-256:

- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/lean/Q1/Target.lean`: `04e63cd522197f6f9f756bf277f69d88256ffb7025f8f09c1b4903f7d443b5bb`
- `/Users/USER/Documents/ChatGPT/mathematics/research/NEXT_THEOREM_CONTRACT.md`: `54014f80f1460195a0c48242bc6fb44d357939e8c4942548b47f2486c922270e`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A55_FULL_PRICE_SHORT_OUTPUT_DELAY_REVIEW.md`: `19258159be0028e98693e6aafb82a89662894e609347fa461ff73fcf25aff51f`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A55_A57_final_review_manifest.json`: `b5ffd9c3eb727e035626e92f8f2bbc7a46f9862bccbe957d42edf81133d5e991`
