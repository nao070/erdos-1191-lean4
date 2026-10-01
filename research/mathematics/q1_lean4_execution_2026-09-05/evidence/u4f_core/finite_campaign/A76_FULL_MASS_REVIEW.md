# A76 independent hand review: shared-source penalty for full original mass

Status: PASS under the exact fixed-component hypotheses below. This is a hand proof, not a finite A76 matrix-certificate check or a uniform norm theorem.

## Actual common-node equation for both orientations

Fix an actual integer Sidon history, source birth c, cut b>c, and genuine component k, and put v=min(k,T). The old bank is a_1,...,a_(c-1); the future bank f_1,...,f_m is the actual rank interval b+1,...,v. Preserve all original strict gates and selected conditions at this (b,k). Original six-endpoint records have exactly one fresh source ending at c. Write its label as h_x=a_c-a_x and the other physical old label as g=a_z-a_w, with w<z<c and x<c distinct from w,z.

Let the actual output pair be i<r. If h_x>g, use right future q=r-b and left future j=i-b. If h_x<g, use q=i-b and j=r-b. Then in both cases

    y = g+f_q-f_j = h_x > 0,
    a_w+f_j = a_z+f_q+a_x-a_c.

Thus j<q is the fresh-larger orientation, and j>q is the fresh-smaller orientation. They must both be included. The case j=q is excluded by the original nonzero output condition: it would give h_x=g and t=0.

The original product de is exactly g*h_x in both orientations. It is not g*|f_q-f_j|, and no separate old-g-square term is needed in the full-product formulation.

## Literal-Sidon matching and one-copy source use

At fixed right node (z,q), fixing w fixes the positive mixed difference f_j-a_x, so literal Sidon determines j,x. Fixing j fixes the signed old difference a_w-a_x. The six-endpoint restriction gives w!=x, so this difference is nonzero; orienting its sign and applying positive-difference uniqueness determines w,x. Consequently actual records at this node form a matching between w<z and all future j!=q. Fixing x also fixes the actual two-sum a_w+f_j; old/future separation resolves the unordered pair, so x is injective too, though this third capacity is not required in the proposed matching upper bound.

Across nodes, fixing the physical source (w,z,x) fixes g,h_x and the positive output difference |h_x-g|. The actual output pair is unique by Sidon, and its orientation determines which endpoint is q. Therefore that physical source is used at most once across all future nodes. No independent copy of its budget is granted to the two orientations.

Any restriction to original strict-core or residual records remains a subset of these actual edges. No missing output is added by this proof.

## Candidate matrices and full-mass upper bound

For every physical old source g=a_z-a_w, choose theta_g in [0,1], constant across its occurrences in the fixed component. Define the auxiliary source bank

    S_g = g*sum_(x<c; x!=w,z) (a_c-a_x).

There is no positive-part truncation in S_g; it covers both orientations.

For a right node (z,q), candidate w<z and j!=q, compute y=g+f_q-f_j. If y<=0, omit the edge. Otherwise find the least actual fresh h_x>=y with x<c and x distinct from w,z. If no such h_x exists, omit the edge. Denote the least by hmin and set

    W_gtheta(w,j)=g*max(y-theta_g*hmin,0).

Let the node allowance be the exact maximum weight of a partial matching on these candidate edges. The candidate has all future columns other than q, including j>q; restricting to j<q would lose actual smaller-fresh records and would not prove a full-mass bound.

For an actual edge, y=h_actual occurs in the candidate fresh bank, and every candidate fresh value is >=y. Hence hmin=h_actual and

    W_gtheta(actual edge)=(1-theta_g)*g*h_actual,
    g*h_actual=theta_g*g*h_actual+W_gtheta(actual edge).

Summing over actual original records, source injectivity bounds the first sum by sum_g theta_g*S_g. Matching capacity bounds the second sum by the sum of node maxima. Therefore

    Q_(c,b,k) <= sum_g theta_g*S_g
                + sum_(z,q) maximum_matching(W_gtheta).

Nonnegative theta_g permits inclusion of unused source triples in the auxiliary source allowance. The source bank and candidate matrix may contain pairs with no actual original output record; this does not assign such pairs a genuine record price.

## Endpoints and optimization boundaries

If every theta_g=1, each candidate has hmin>=y, so every W is zero and the upper allowance is sum_g S_g. If every theta_g=0, candidate weights are g*y in the full signed mixed-node threshold graph. Actual y is positive in both orientations; a negative future difference f_q-f_j is not itself a reason to omit a candidate when y remains positive.

Arbitrary-weight matching certificates are needed unless an additional optimization theorem is proved for this new matrix. The A70 greedy theorem for weights g*t with g+t<=H does not automatically apply. Padded assignments must encode j!=q and the complete candidate domain correctly.

The argument does not claim optimality for any vector theta_g, nor improvement over every previous upper allowance. This review contains no new A76 finite calculation.

## Genuine prices, coverage, and unresolved scope

The result bounds full original unpriced mass at the fixed actual component v=min(k,T), including both source orientations. It may be multiplied by the same genuine nonnegative lambda_k and summed over the actual finite components with all selectors retained. Components k>T still use v=T and are not removed. No u_r^[M] or terminal alpha_(M+1) is changed.

The one-copy argument shares a source budget across future nodes of this component. It does not provide independent budgets for different cuts, change the original cut coverage [c+1,i-1], or prove that a source allowance can be reset across horizons. Although the formulation removes the separate old-g-square term algebraically, control of the resulting allowance over every birth, cut, and component remains unproved. The original frozen uniform norm and Q1 remain unresolved.

## Scope and supporting review hashes

Only this hand-review file was created for A76. No history, original-record enumeration, full-profile scan, optimizer, Lean build, or root mathematical-source edit was performed.

- `A73_FRESH_TAIL_REVIEW.md`: `fd4dec73116389fb7d71ec61bba883a7a0751b6512a167364994568302e2d1d1`
- `A74_SOURCE_DUAL_REVIEW.md`: `d7c62f0badb11eb796ee28ab29a64d557a96624dde38193f563ce23f6222ce56`
- `A75_ONE_SOURCE_CHECK.json`: `29fe09a50d7ea768a7aa63511631cdaebc99b68fb75a4ab10e4bcaabfae900ff`

These references support the prior recovery/one-copy framework and its finite scope. The actual A76 proof is given explicitly above; no A76 numerical certificate is implicitly certified by those older artifacts. The live WORKING_PROOF remains concurrently owned by the root researcher.
