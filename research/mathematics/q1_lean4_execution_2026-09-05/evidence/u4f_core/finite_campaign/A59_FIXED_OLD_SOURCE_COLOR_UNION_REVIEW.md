# A59 independent review: two-color union for one physical old source

Date: 2026-09-09. Status: PASS independent hand review. No finite work, profile or record-pool scan, new history, Lean run, cap/norm derivation or redelegation.

## Exact common-source graph

Use the actual finite positive integer Sidon history, original strict-core records and genuine prices of A58. Fix c and a physical old source g=a_z-a_w>0, w<z<c, and put K=a_c-g. For every allowed fresh endpoint x<c distinct from w,z, let h=a_c-a_x>0. Exclude h=g because its output difference would be zero. Every original eligible record gives

    t=|h-g|=a_r-a_i>0, i<r,
    sigma=sign(h-g) in{+1,-1},
    a_x=K-sigma*t,
    gh=g^2+sigma*g*t.

Make an undirected multigraph from the directed colored edge i->r. The two colors use A58's two different source orientations. Each color has indegree and outdegree at most1. The physical record is unique for a given x: h,g and positive t then determine the color and actual output pair. There are at most c-3 allowed distinct x values, so the entire colored union has at most c-3 edges.

## Cross-color through-connections are impossible

Suppose a color+ edge i_1->j has gap t_1 and a color- edge j->r_2 has gap t_2. Their fresh endpoints obey

    a_(x_plus)=K-t_1,
    a_(x_minus)=K+t_2.

Hence the positive OLD difference a_(x_minus)-a_(x_plus)=t_1+t_2 equals the positive FUTURE difference a_(r_2)-a_(i_1). These are two distinct ordered endpoint pairs in disjoint old/future rank ranges, contrary to literal Sidon difference uniqueness. For the reversed colors the same argument exchanges the two x endpoints. Thus no incoming edge and outgoing edge of opposite colors can meet at a future vertex.

Together with A58's same-color degree bounds, this leaves precisely three possible degree2 forms:

- A through-chain with one incoming and one outgoing edge of the same color.
- Two outgoing edges of opposite colors.
- Two incoming edges of opposite colors.

Any third incident edge violates one of these restrictions, so undirected degree, counted with edge multiplicity, is at most2. Loops never occur because i<r.

Parallel edges of opposite colors with the same(i,r) must be retained if actual records provide them. They have different fresh x values, so they do not contradict x-injectivity. Same-color parallel duplication is impossible by A58. This review does not assume existence or nonexistence of an opposite-color parallel pair; it is handled correctly as a possible length2 multicycle. No finite example is generated.

## Component decomposition and exact cancellation

A finite undirected multigraph with no loops and maximum degree2 has components that are isolated vertices, paths or cycles, allowing length2 parallel-edge cycles. Let

    B_component=sum_edges sigma*(a_r-a_i).

The coefficient of a vertex value in this signed sum is the sum of sigma on incoming edges minus the sum of sigma on outgoing edges. At every degree2 vertex it vanishes:

- Same-color through-chain: sigma-sigma=0.
- Opposite-color incoming pair: (+1)+(-1)=0.
- Opposite-color outgoing pair: -(+1)-(-1)=0.

Therefore every cycle has B_component=0, including the length2 parallel cycle. In a nontrivial path only its two degree1 endpoints remain. Each coefficient is+1 or-1, and their sum is zero since every edge contributes opposite incidence coefficients. Thus

    B_component=plus or minus(a_endpoint2-a_endpoint1).

The endpoint ordering here is arbitrary; no positivity of B_component is asserted. For a component with L edges,

    sum_edges gh=g^2 L+g B_component.

A cycle contributes exactly g^2L. For a path the signed boundary can increase or decrease that baseline. Individual products remain positive because they are the actual g*h, not an abstract signed replacement.

## Actual cut and component scope

For a covered cut c<b, use only actual selected edges with b<i<r<=v=min(k,T). This graph has m=v-b vertices when v>b; if v<=b it is empty. Its total edge number obeys both

    L_total<=c-3,
    L_total<=m,

the latter by2L_total=sum_degrees<=2m. Combining them gives L_total<=min(c-3,m). This retains cycles and multiplicities; a path-only improvement to m-1 is not generally available from this structure.

Any original cut or remaining-class selection simply deletes actual colored edges, so these structural statements and the component cancellation remain valid on each selected graph. Such deletions may turn cycles into paths or split paths. The correct notation is G_(b,k), with v=min(k,T); component-dependent predicates keep k even when k>T. Consequently the exact genuine selected weight for this fixed(c,g) bank is

    sum_k lambda_k sum_{components of G_(b,k)}
       [g^2 L_component+g B_component].

Each lambda_k is the original (alpha_k-alpha_(k+1))/H_k^2; it is not a path-reset price. The original terminal alpha and k>T tails persist. Combining the two colors in this identity does not create independent unused budgets for the colors, components or cuts.

## Logical boundary

The union need not be asserted to be a matching or a simple graph. The permitted same-color through-chain and opposite-color degree2 fork forms are part of the proved classification; no actual witness for them is claimed without a prescribed finite check. This review proves the degree, multigraph and cancellation identities only. It supplies no cap-sensitive summable norm, frozen CoreUniform result, literal Q1 theorem or final Lean closure. Parent's distinct cap/norm analysis remains separate.

## Source bindings

This argument uses A58's literal-Sidon recovery in both colors and the same actual-record conventions. SHA-256:

- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A58_FIXED_BIRTH_TWO_ORIENTATION_GRAPH_REVIEW.md`: `c776e95213f229b4080a8eaf7df360066801cc92a5c3a8273f482737f2f9e39b`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/lean/Q1/Target.lean`: `04e63cd522197f6f9f756bf277f69d88256ffb7025f8f09c1b4903f7d443b5bb`
- `/Users/USER/Documents/ChatGPT/mathematics/research/NEXT_THEOREM_CONTRACT.md`: `54014f80f1460195a0c48242bc6fb44d357939e8c4942548b47f2486c922270e`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A55_FULL_PRICE_SHORT_OUTPUT_DELAY_REVIEW.md`: `19258159be0028e98693e6aafb82a89662894e609347fa461ff73fcf25aff51f`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A55_A57_final_review_manifest.json`: `b5ffd9c3eb727e035626e92f8f2bbc7a46f9862bccbe957d42edf81133d5e991`
