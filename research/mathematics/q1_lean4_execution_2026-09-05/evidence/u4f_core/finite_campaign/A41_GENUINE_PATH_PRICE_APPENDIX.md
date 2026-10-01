# A41 review appendix: exact path prices and the terminal-budget obstruction

Date: 2026-09-09. Status: PASS hand corollary. This appendix adds
the price calculation to the existing A41 path review without changing
its previously bound finite evidence. No new finite calculation or
Lean build was performed.

Fix b>=3 and e in the actual old difference set, with unique old
source endpoints w,z. Let H0=H_{b-1}, n=b-1, and take the final
strict-core graph at output horizon T. Index each nontrivial path
once by its terminal vertex (old endpoint x0, future rank i0).
A41's prepend law shows that at any smaller output horizon its
active edges form a suffix of that final directed path.

List its vertices from the terminal backwards as j=0,...,L. Write
A_j for the old physical value at vertex j and f_j for its future
rank, so f_0=i0 and both A_j and f_j strictly increase with j.
The edge j to j-1 has larger source difference A_j-A_{j-1},
smaller source difference e, and upper output rank f_j. Therefore
the path's exact original-price contribution is

    W_path=e sum_{j=1}^L (A_j-A_{j-1})u_{f_j}^{[M]}
          =e sum_{k=b+2}^M lambda_k
                           (A_{last_active(k)}-A_0),
    lambda_k=kappa_k/H_k^2.

If no edge is active the span is zero. The last active index is
the largest j with f_j<=min(k,T). This is an exact finite interchange
and telescope, not an independent price allowance for each vertex.
For k>T all final path edges remain active and the original genuine
component tail continues through M.

Every active old span is at most H0. Moreover the first edge only
appears at f_1>=i0+1. It follows that

    W_path<=e H0 u_{f_1}^{[M]}
           <=e H0 u_{i0+1}^{[M]}.

For each terminal future rank i0, at most n-2 old rows are available:
the fixed smaller-source rows w,z are excluded by the six-endpoint
condition. Distinct paths have distinct terminal vertices. A
nontrivial path has b+1<=i0<=T-1. Consequently

    P_b(e)<=e H0(n-2) sum_{i=b+1}^{T-1}u_{i+1}^{[M]}.

Here P_b(e) is the original full-price profile contribution from
records with this fixed smaller source label. The original bound

    u_r^[M]<= (alpha_r-alpha_{M+1})/H_b^2
            <= alpha_r/H_b^2

holds for r>=b+2; the first inequality retains the terminal term.
The existing numerical alpha telescope gives
sum_{r=b+2}^infinity alpha_r<=1/[3(b+1)^3]. Thus

    P_b(e)<= e H0(n-2)/[3(b+1)^3 H_b^2].

Finally the actual old-gap identity gives sum_e e<=n^2 H0/4.
Summing over the same physical smaller-source labels yields

    P_b <= n^2(n-2)H0^2/[12(b+1)^3 H_b^2] < 1/12.

The b2 core is empty and is not inserted into the expression n-2.
Empty path sets contribute zero. The relaxed constant1/12 is worse
than A02's1/24 constant. The span-sensitive displayed formula need
not be numerically dominated by A02 in every finite history; a large
diameter jump can make H0/H_b small. No stronger uniform norm follows
from the present independent terminal allowances.

The losses are explicit: replace every actual path span by H0,
replace its first edge rank and strict output gap by i0+1, replace
the actual terminal-row distribution by n-2 at every i0, and replace
joint source-label information by the unrestricted sum_e e. This
leaves a constant pointwise obstruction after summing the separate
terminal budgets. A general matching assumption, improved path count,
uniform central norm or Q1 is not used or proved.

This appendix is bound together with the A41 cap corollary and A43
review by A41_A43_followup_review_manifest.json.
