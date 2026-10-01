# A45: uniform small-source payment and source-birth localization

Date: 2026-09-09. Independent hand-proof review: PASS.
No new finite history, scan, or Lean execution. U4-F/Q1 are unresolved.

## Exact claim and hypotheses

Use an actual finite integer Sidon history with the unchanged strict core,
cut b>=3, n=b-1, component horizon M and output horizon T<=M. Write
lambda_k=kappa_k/H_k^2, alpha_k=1/[k^2(k-1)^2], and
u_r^[M]=sum_{k=r}^M lambda_k. In particular alpha_(M+1) is not reset.
Fix one real q>1 and set L_b=floor(b^2/(log b)^q). Select the original
records whose smaller numerical source e obeys e<=L_b. This is a
cut-dependent nonnegative subclass of the original profile.
The selected part of one physical record uses only those cuts in its
original interval where this selector holds. On a block its selected
coverage is the sum of 1/b over exactly those cuts; selected and
complementary coverage add to the original once-per-cut coverage.

Actual Sidon uniqueness makes each physical record inject into its ordered
source labels (d,e), d>e. Dropping order and gates only in a nonnegative
upper sum yields, for every genuine component,

    Q_small(b,k) <= (sum_{d in D} d)(sum_{e in D,e<=L_b} e)
                 <= n^2 H_b L_b(L_b+1)/8.

Here D is the actual difference bank of the first n points,
sum_D d<=n^2 H_b/4, and integer uniqueness gives
sum_{e in D,e<=L} e<=L(L+1)/2. Therefore

    P_small(b;M,T)
      <= n^2 L_b(L_b+1)/(8H_b)
           * (alpha_(b+2)-alpha_(M+1))
      <= L_b(L_b+1)/[4(b+2)^2(b+1)^2]
      <= 1/[2(log b)^(2q)].

The first displayed line is interpreted as zero if no components exist.
For the second use integer Sidon packing H_b>=b(b-1)/2 and
n^2/(8H_b)<1/4. For the last, L_b=0 is empty; otherwise L_b+1<=2L_b
and L_b<=b^2/(log b)^q. These operations are upper bounds, not replacement
of the terminal component price.

Since x->1/[x(log x)^q] is decreasing on x>=2,

    sum_{b=3}^{T-1} sqrt(P_small(b;M,T))/b
      <= (log 2)^(1-q)/[sqrt(2)(q-1)].

For q=5/4 the constant is 2sqrt(2)/(log 2)^(1/4). This subclass theorem
does not use cap. It holds for every finite M,T without assuming an
infinite capped history or a maximum prefix length.

## What remains after this payment

For an integer e excluded from the small-source subclass,
e>L_b implies strictly e>b^2/(log b)^q. Fixing such an e on an A41 path,
the balance sum d=L_path*e+future endpoint span<=H_(b-1) gives

    L_path < H_(b-1)/e
           < H_b (log b)^q/b^2
           <= C log(2b)(log b)^q,

provided b>=m0 and the fixed cap holds there. A path has a single e, so
this selection does not remove arbitrary interior edges of that path.
The stronger A41 denominator e+ell_b can also be retained. This statement
holds in particular for the all-large-old-gap remainder. A polylogarithmic
length bound alone does not control total de-weight or the remaining norm.

## Localization of both source births

Let the oriented source pairs of d and e have upper ranks y and z, and
put s=min(y,z). The assertion e<=H_s needs both inequalities:
e<=H_z and e<d<=H_y. If s>=m0, the all-rank cap gives

    e <= C s^2 log(2s) <= C s^2 log(2b).

Consequently a remaining e satisfies

    s > b/[sqrt(C log(2b)) (log b)^(q/2)]
      >= b/[sqrt(2C) (log b)^((q+1)/2)].

The last comparison uses log(2b)<=2log b for b>=2. For q=5/4 the
power is 9/8. Since s is the smaller birth, both source births satisfy
this lower bound. Cap below m0 is not being assumed.

If M>=m0 but s<m0, define the fixed integer
D0=ceil(C m0^2 log(2m0)). Then e<=H_s<=H_m0<=D0. Applying the same
small-source estimate with the fixed integer cutoff D0 and summing from
B=max(3,m0) gives

    sum_{b=B}^{T-1} sqrt(P_{s<m0}(b))/b
       <= sqrt(D0(D0+1))/[4B(B+1)].

Indeed each summand is at most
sqrt(D0(D0+1))/[2b(b+1)(b+2)], and the numerical infinite tail sums to
1/[2B(B+1)]. This remains a finite-history statement. If M<m0, the
entire available cut range is finite; if b<m0, use the existing finite
initial-cut payment. Neither extension beyond M nor cap at absent ranks
is used. Early-source and other subclasses may overlap; pay them in a
fixed order or use nonnegative domination, without counting any physical
record as multiple independent resources.

## Finite illustration and logical scope

Only the already saved A44 edges were reclassified: at b25 the exact
threshold is L25=144. The all-large, central-component, near-span
remainder contains two edges with e=312 and 422, which repeat future
r43. The following A46 gap payment removes the e422 edge from this
particular example. Exact enclosures and original rows are in the A44/A46
evidence; they do not provide asymptotic information.

The subclass and localization claims above are noncircular hand proofs
from actual Sidon differences, integer packing, and the explicitly stated
cap instances. Their full statements are not Lean-verified here. The
remaining central/near components with larger source labels and later
source births still require a joint weighted estimate. The next action is
to study that retained information, not sum independent per-source bounds
or infer uniform K from finite samples. Source/reference/evidence hashes
are in `A44_A46_review_manifest.json`.
