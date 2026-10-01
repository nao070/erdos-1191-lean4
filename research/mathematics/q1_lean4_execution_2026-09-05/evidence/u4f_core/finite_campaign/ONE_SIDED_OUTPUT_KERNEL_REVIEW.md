# A28 independent review: one-sided output kernel and its scalar limit

2026-09-09. The actual-record bounds, strict integer cutoff, finite
component-price formulas, and proposed scalar nondecay constant all
pass independent hand review. No new finite search, record enumeration,
history generation or Lean run was performed.

## A fixed actual output uses each larger source label at most once

Fix a valid cut 2<=b<T<=M. Let D be the actual positive difference set
of the first b-1 points, H=H_b=a_b-a_1>0, and S=sum_(d in D)d^2.
In particular H is a positive integer and every d in D is strictly
less than H. Use tau for a numeric output difference, to distinguish
it from an output-rank horizon.

For fixed tau>0, orient each original strict-core edge by its larger
source label d; its smaller label is exactly d-tau. Thus d can label
at most one edge for this particular tau. Actual positive-difference
uniqueness fixes the endpoint pair of each source label, and it fixes
the actual output endpoint pair of tau. Consequently the same edge
cannot produce two copies of a physical record in this sum.

If 0<tau<H, every retained edge satisfies

    d(d-tau)=d^2(1-tau/d)<=d^2(1-tau/H).

Summing over distinct larger labels and enlarging to all of D gives

    K_tau^core<=S(1-tau/H).                         (1)

If tau>=H there is no edge, because d<H and its smaller label is
positive. Therefore the complete statement is

    K_tau^core<=S(1-tau/H)_+.                       (2)

An empty output class also satisfies (2). The argument bounds a
subset of the unchanged actual edges. It does not remove an original
strict condition or insert new records.

The one-use statement is for the larger source label at fixed tau.
Different tau may reuse that label, and their S bounds have not been
turned into a common independent-record budget. Via A04.1, (2) also
gives a joint lower bound on boundary plus gradient loss; discarding
their relation would lose this linear-in-tau/H improvement.

## The strict cutoff and the exact integer packing

Every core record covering b has c<b<i<r, r<c log c, and
tau>c^2/(log c)^3. Since c>=4 for four distinct old endpoints,

    r<c log c<c log b, hence c>b/log b,
    tau>b^2/(log b)^5=:L_b.                         (3)

The conclusion is vacuous at cuts that have no records. Since tau is
an integer, its exact minimum allowed value is

    ell=floor(L_b)+1.

This is not interchangeable with ceil(L_b) at an integral L_b.

At component k>=b+1, put t_rank=min(k,T), m=t_rank-b>=1 and
h=binom(m,2). The m future points have exactly h distinct positive
differences by actual Sidon uniqueness. Strict core selects some of
those outputs. Only integer outputs ell,...,H-1 can have positive
kernel (2), and this interval has max(0,H-ell) elements. Set

    z=min(h,max(0,H-ell)).

The kernel is nonnegative and decreasing on that integer interval.
The largest sum over at most h distinct eligible integers is obtained
by its first z integers. Consequently

    sum_(actual component outputs) K_tau^core
      <= S F_(H,ell)(h),

    F_(H,ell)(h)
      =z(1-ell/H)-z(z-1)/(2H).                     (4)

If h=0 or ell>=H, then z=0 and the right side is zero. The endpoint
H itself has zero kernel and need not be included. Formula (4) uses
the genuine strict integer cutoff without a rounding ambiguity.

This is an upper relaxation of the actual output set. It also forgets
the extra actual Sidon exclusion tau not in D: a future endpoint pair
cannot repeat a positive difference already represented by two old
endpoints. Allowing those forbidden integers in the packed interval
only increases the bound; it does not invalidate (4).

## Both genuine horizons and the cap improvement

Finite interchange of the unchanged component sums gives the upper
bound, with m_k=min(k,T)-b,

    P_b^core(M,T)
      <=S sum_(k=b+1)^M (kappa_k/H_k^2)
                       F_(H,ell)(binom(m_k,2)).     (5)

For k>T, the future set remains the one through T, while every such
component still contributes its genuine price. The terminal
kappa_M=alpha_M-alpha_(M+1) remains unchanged.

Alternatively define the exact numerical output-pair price sum

    A_b(M,T)=sum_(r=b+2)^T (r-b-1)u_r^[M]
      =sum_(k=b+1)^M (kappa_k/H_k^2)binom(m_k,2).    (6)

Using only tau>L_b in (2), rather than the refined packing in (4),
and writing rho=L_b/H, yields

    P_b^core(M,T)<=S A_b(M,T)(1-rho)_+.             (7)

If rho>=1, every record would require tau>H and the profile is zero,
so the positive part in (7) is essential and handles that case.
For b>=m0 the unchanged cap H_b<=Ccap*b^2*log(2b) implies

    rho>=1/[Ccap*log(2b)*(log b)^5]=:delta_b,
    P_b^core(M,T)<=S A_b(M,T)(1-delta_b)_+.         (8)

No cap is imposed at b<m0. At fixed positive Ccap the guaranteed
relative improvement delta_b is of order(log b)^(-6). This improves
the gradient-only A04 factor of order(log b)^(-12), but (1-delta_b)
still tends to1. Combining only this factor with a constant profile
majorant does not establish the required uniform norm.

## Review of the scalar nondecay witness for the numerical majorant

The actual variance estimate permits

    S<=Sbar_b:=(b-1)^2 H_b^2/4.

Indeed it first bounds S by (b-1)^2 H_(b-1)^2/4 and then uses
H_(b-1)<=H_b. Thus replacing S by Sbar_b in (5) defines a valid upper
formula U_b for actual histories.

Now evaluate only that numerical formula on the scalar diameter
profile H_n=n(n-1)/2, with M=T>=3b and b>=8. This profile meets the
scalar packing bound and C=1,m0=2 diameter cap. It is not Sidon: the
translated point sequence a_n=1+H_n has

    a_4-a_3=a_3-a_1=3.

No actual D or S realizing the substituted Sbar_b is claimed.

For b>=8, log b>=2, and

    ell<=b^2/32+1<=b^2/16<=H_b/4.                  (9)

The middle inequality uses b^2>=32, and the last uses b>=2. On the
integer component interval2b<=k<=3b,

    h=binom(k-b,2)>=binom(b,2)=H_b,
    z=H_b-ell,
    F_(H_b,ell)(h)=(H_b-ell)(H_b-ell+1)/(2H_b)
       >=H_b/4>=b^2/16.                            (10)

For example ell<=H_b/4 already gives
F>=9H_b/32, which is stronger than the displayed H_b/4. Also

    Sbar_b>=b^6/256.                               (11)

The exact coefficients satisfy

    kappa_k=4/[k(k^2-1)^2]>=4/k^5,
    1/H_k^2>=4/k^4.

There are b+1, and hence at least b, integer components in2b..3b.
Therefore

    sum_(k=2b)^(3b) kappa_k/H_k^2
       >=16/(3^9 b^8).                             (12)

Combining (10)-(12), while retaining only those genuine components,
proves exactly

    U_b>=1/(256*3^9)=1/5038848.                     (13)

For the same scalar profile this holds simultaneously for
8<=b<=floor(M/3), so its numerical square-root harmonic majorant is
not uniformly summable as M grows. The product constants, component
count and onset b>=8 are all valid.

Equation (13) evaluates an actual-valid upper formula on a larger
non-Sidon scalar input class. It is not a lower bound on an actual
profile and does not prove that U_b is nondecaying on admissible fixed-
cap Sidon histories. In particular it does not supply an unbounded
actual same-cap history family or a Q1 counterexample. The missing
source/output realizability and the forbidden output values in D are
specific information absent from this scalar evaluation.

## Source binding, role and next action

Reused source: execution-workspace
`research/u4f_core/WORKING_PROOF.md`, read at whole SHA-256

    6ab16366b7da047c18717a0d0876457085cb6ce1b980260b5812d408841fcd87

The reviewed A04 section hash, from its heading to before the next ##,
is

    7b5a67ac00a9e7c8a7a85a5b4ac870da4573d15019300037ab34c2a9802443fd

All new results in this note are hand proofs, not new Lean checks.
The actual one-sided bound and exact integer kernel are valid upper
estimates. Their scalar nondecay exposes the limit of this relaxation,
not failure of the frozen theorem. A next estimate must retain more
of the actual available-output and source-edge correlations when
summing components and cuts. Frozen U4-F and original Q1 remain open.
