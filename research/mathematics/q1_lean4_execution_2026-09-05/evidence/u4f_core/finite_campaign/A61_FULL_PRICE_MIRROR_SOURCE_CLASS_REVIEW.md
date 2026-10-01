# A61 independent review: full-price mirror-source class is uniformly paid

Date: 2026-09-09. Status: PASS bounded independent hand proof. No finite search/example, history/profile/pool scan, Lean run or redelegation.

## Exact selected class and unique mirror pair

Fix an original strict-core physical record born at c>=4. Its one old source is g=a_z-a_w with w<z<c, and its fresh source is h=a_c-a_x>0. The larger/smaller ordering of g,h is not fixed; the actual output is t=|h-g|=a_r-a_i>0. Select the full original record if an actual old endpoint x'<c satisfies

    a_x+a_(x')=2(a_c-g).

The mirror endpoint need not produce any eligible or strict-core record. It may violate source endpoint exclusions for the mirror orientation. Existence of the endpoint itself implies h'=a_c-a_(x')>0 and h+h'=2g.

Literal repeated-sum Sidon implies at most one unordered old endpoint pair{x,x'} with this prescribed sum for fixed(c,g). The case x=x' would force h=g and t=0, so it cannot occur for a selected original record. Consequently there are at most two possible fresh labels h,h', exchanged by the mirror relation. Both have the same positive output label|h-g|=|h'-g|, which has at most one actual ordered output pair(i,r) in the history.

Thus all selected original records for this(c,g) lie among these two physical possibilities. If no output pair exists, neither exists. If only one passes endpoint or strict gates, only that original record contributes. Since h,h'>0,

    sum_{selected actual records for(c,g)}g*h <=g(h+h')=2g^2.

The singleton case is covered even when its one product exceeds g^2. The mirror term is an algebraic nonnegative allowance; no nonexistent or ineligible mirror record is given an output price.

## Full original price and birth mass

Whenever a selected record exists, c+2<=r<=T<=M. Both possible original records for a fixed mirror pair, if present, share the same output and full original u_r^[M]. Therefore their total genuine price is at most2g^2u_(c+2)^[M]. This remains an upper bound when only one is present. If c+2>T there are no selected original records; no width at a missing rank is accessed.

Let S_(c-1) be the sum of squared actual old differences. Summing each physical oldg bank once, and using S_(c-1)<=(c-1)^2H_c^2/4 and the original finite tail bound, gives

    E_c <=2S_(c-1)u_(c+2)^[M]
        <=(c-1)^2/(2c^4)<=1/(2c^2).

Here u_(c+2)^[M]<=alpha_(c+2)/H_(c+2)^2<=1/(c^4H_c^2). The underlying finite telescope retains alpha_(M+1)>0 before an upper bound is taken. Every original selected record keeps all components r,...,M, including k>T, and its original physical cuts c+1,...,i-1. This class is a static record selector, not a cut or component reset.

## Dyadic birth coverage and uniform norm

For2^ell<=c<2^(ell+1),ell>=2, the one-price birth mass satisfies

    E_ell<=2^(-ell-1).

Original strict core imposes r<c logc. Combined with c<b<i<r, this places all covered cuts in

    2^ell<b<2^(ell+1)(ell+1)log2.

The harmonic support weight is at most

    W_ell=log[2(ell+1)log2].

Exact once-per-record coverage gives sum_b P_ell(b)/b<=E_ell W_ell. Weighted Cauchy then gives

    sum_b sqrt(P_ell(b))/b<=sqrt(E_ell)W_ell.

Summing the finite actual birth groups and then the positive infinite majorant proves

    N_mirror<=sum_{ell>=2}2^(-(ell+1)/2)
                log[2(ell+1)log2] < infinity.

The geometric factor makes this series convergent. This is a uniformly paid full-price actual subclass for every original finite M,T, with no cap used and no extension or growing-prefix assumption.

## Consequence for the residual common-source graph

If opposite-color parallel edges share the same(i,r) in A59, their fresh labels are g+t and g-t. Their actual old endpoints therefore satisfy the mirror relation. Both original records are paid by this class; the conclusion remains valid if additional selectors retain only one. Removing all mirror-selected original records leaves a simple residual graph: same-color parallel duplication was already impossible, and opposite-color parallel pairs cannot survive.

This does not prove a forest, bipartiteness or triangle-freeness. The degree/cancellation rules permit a triangle consisting of two same-color edges i->j->r and one opposite-color edge i->r; its formal old fresh-endpoint sum is3K, K=a_c-g. No actual triangle existence was tested or claimed. Residual components are paths or possible simple cycles of length at least3, along with isolated vertices. The earlier phrase limiting surviving cycles to length at least4 was corrected by the parent before this note was saved.

## Logical role and remaining gap

The mirror class is an actual new uniformly bounded full-price subclass, proved here by hand; the remaining shared-source graph and frozen norm are still unbounded by the current arguments. No full Lean instantiation, CoreUniform theorem, Q1 result or final clean axiom closure is claimed. Future cap/norm work must keep the simple graph's remaining cycles and signed boundary structure rather than infer a matching or forest.

## Source binding

SHA-256:

- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A58_FIXED_BIRTH_TWO_ORIENTATION_GRAPH_REVIEW.md`: `c776e95213f229b4080a8eaf7df360066801cc92a5c3a8273f482737f2f9e39b`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A59_FIXED_OLD_SOURCE_COLOR_UNION_REVIEW.md`: `8585609a6079310d06072032eeaa6c7b71bf81910e1fd7f76ab03fdd8a713bba`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A42_SOURCE_PAIR_RANK_TAIL_REVIEW.md`: `1f8f530e53de783939ef396490e1fc13168c5babd344e2602bd4add395c9e350`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/lean/Q1/Target.lean`: `04e63cd522197f6f9f756bf277f69d88256ffb7025f8f09c1b4903f7d443b5bb`
- `/Users/USER/Documents/ChatGPT/mathematics/research/NEXT_THEOREM_CONTRACT.md`: `54014f80f1460195a0c48242bc6fb44d357939e8c4942548b47f2486c922270e`
- `/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/A60_SHARED_GRAPH_ALLOWANCE_LIMIT_REVIEW.md`: `99412e8ad753b0de37962701bbb49b25f9b3c718b3662a72675675bfc4214c03`
