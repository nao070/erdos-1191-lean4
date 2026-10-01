# A60 independent review: exact graph allowance and its relaxed long-window limit

Date: 2026-09-09. Status: PASS bounded independent hand review. No finite task, history/profile/pool scan, Lean run, model change or redelegation.

## Actual shared-source upper bounds

Fix an actual original component k, output horizon v=min(k,T), and covered cut c<b<v. Put m=v-b and H_future=a_v-a_(b+1). All remaining selectors, if present, stay in the actual graph G_(b,k). Let D_(c-1) be the actual positive differences among ranks1,...,c-1, and set

    U=sum_{g in D_(c-1)}g,
    S=sum_{g in D_(c-1)}g^2,
    G=sum_{x<c}(a_c-a_x).

Each original six-distinct record born at c has exactly one old g in this set and one fresh h=a_c-a_x. Actual positive output uniqueness gives at most one record for fixed(g,h). Hence the selected unpriced mass obeys Q_(c,b,k)<=U*G. The bank may contain incompatible endpoints or nonexistent outputs; it is only a joint upper bound and prices none of those absent records.

For each actual old g, A59 gives L_g<=min(c-3,m), with exact mass g^2L_g+g sum_path B_path. Nontrivial path components are vertex-disjoint and each has at least2 vertices, so their number is at mostfloor(m/2). Each signed path boundary is at most H_future; cycles have boundary0. Thus

    Q_(c,b,k) <= min[U*G,
       min(c-3,m)S+floor(m/2)H_future U].

Negative signed boundaries are safely replaced by an upper bound, not by an identity. Parallel cycles and simple cycles remain counted in L_g. Cases with m<=1 have no output edge; v<=b is empty and does not require this displayed positive-m notation.

## Endpoint-derived scalar envelopes

Write n=c-1 and H=H_c. The old label sum has the exact gap expansion

    U=sum_{j=1}^{n-1}j(n-j)(a_(j+1)-a_j)
      <=floor(n^2/4)H_(c-1)<=n^2H/4.

For old coordinates0<=X_j=a_j-a_1<=H,

    S=n sum_j X_j^2-(sum_j X_j)^2
      <=nH sum_jX_j-(sum_jX_j)^2<=n^2H^2/4.

Also G<=nH. These are genuine upper bounds from actual endpoints; they do not assert simultaneous saturation or realization of any independent scalar data.

## Cap-based comparison of the two relaxed allowances

Assume m>=c>=max(4,m0), fixed all-rank cap H_c<=C c^2log(2c), and

    c-1>=12C log(2c).

The m future points form an actual integer Sidon set, so their distinct positive differences imply H_future>=m(m-1)/2. Since m>=4, floor(m/2)>=m/3. Therefore

    floor(m/2)H_future
       >=m^2(m-1)/6 >=c^2(c-1)/6
       >=2C c^2log(2c) >=2H_c.

After independently substituting the U and S envelopes into the graph bound (and using min(c-3,m)=c-3), its scalar allowance is

    A=(c-1)^2H_c^2/4
       *[(c-3)+floor(m/2)H_future/H_c].

The source-product envelope from U*G is

    B=(c-1)^3H_c^2/4.

The previous inequality proves A>=B. Accordingly min(A,B)=B in this specified long-window range. The factor12C and the two missing units between c-3 and c-1 are correct.

## Exact limitation

This is a conditional theorem about upper envelopes for each actual finite prefix satisfying the displayed cap and rank conditions. It assumes no arbitrarily long fixed-cap family. It gives no lower bound on actual Q and no Sidon/Q1 counterexample. Crucially, it does NOT prove that the unrelaxed quantity min(c-3,m)S+floor(m/2)H_future U cannot improve actual U*G: the comparison A>=B applies only after their separate U/S/G scalar relaxations. Common endpoint, sign, cycle and path-boundary information can still improve the actual allowance. No summability or full norm is obtained here.

## Source binding

SHA-256 of the reused actual graph, source-bank and literal Sidon conventions:

- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A58_FIXED_BIRTH_TWO_ORIENTATION_GRAPH_REVIEW.md`: `c776e95213f229b4080a8eaf7df360066801cc92a5c3a8273f482737f2f9e39b`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A59_FIXED_OLD_SOURCE_COLOR_UNION_REVIEW.md`: `8585609a6079310d06072032eeaa6c7b71bf81910e1fd7f76ab03fdd8a713bba`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A42_SOURCE_PAIR_RANK_TAIL_REVIEW.md`: `1f8f530e53de783939ef396490e1fc13168c5babd344e2602bd4add395c9e350`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/lean/Q1/Target.lean`: `04e63cd522197f6f9f756bf277f69d88256ffb7025f8f09c1b4903f7d443b5bb`
- `/Users/USER/Documents/ChatGPT/mathematics/research/NEXT_THEOREM_CONTRACT.md`: `54014f80f1460195a0c48242bc6fb44d357939e8c4942548b47f2486c922270e`
