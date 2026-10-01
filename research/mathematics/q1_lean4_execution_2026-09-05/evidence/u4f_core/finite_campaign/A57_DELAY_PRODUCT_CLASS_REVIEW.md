# A57 independent review: one uniformly paid delay-product class

Date: 2026-09-09. Status: PASS independent hand proof. No additional finite work, source pool scan, history, Lean run or redelegation.

## Exact selected class

Fix eta>0, nu=2+eta and q=nu/2>1. For each original strict-core physical record of birth c>=4 put

    x=(i-c)/c, y=(r-c)/c,

and select its full original price de*u_r^[M] precisely when

    x^2 min(1,y) <= (log c)^(-nu).

All original physical coverage c+1,...,i-1 is retained. Since i<r, 0<x<y. All widths, gates, Sidon conditions, horizons and genuine component tails are unchanged. This is a new selected part of the original profile, not a redefinition of the frozen core.

## Long upper-output delay y>1

Here the selector becomes x<=(log c)^(-nu/2), equivalent for integer i-c to

    i-c <= floor(c/(log c)^q), q=nu/2>1.

This part is a subset of A56 and has its valid uniformly finite norm bound. No y>1 restriction was needed for A56. The selected class with y<=1 will be handled separately, so there is no equality decomposition that double-counts their intersection.

## Strict dyadic delay bins for 0<y<=1

Use the unique half-open bins

    2^(-h-1)<x<=2^(-h),
    2^(-l-1)<y<=2^(-l), h,l>=0.

Actual x<y forces h>=l: otherwise y<=2^(-h-1)<x. This endpoint convention also assigns x or y that is an exact dyadic boundary exactly once.

At fixed birth c, the number of possible lower output indices is at most floor(c2^(-h))<=c2^(-h), and the upper output indices at most c2^(-l). Each actual pair(i,r) gives at most2(c-1)<=2c records by the actual one-fresh-source recovery proof in A55. Invalid output order, unavailable labels, endpoint overlap and strict gates only reduce this count. Hence the total product de is bounded by

    2c^3 2^(-h-l) H_c^2.

Every actual record has c+2<=r<=T<=M, so its full original u_r^[M]<=1/(c^4H_c^2), with finite alpha_(M+1) retained before the upper bound. The full price born at c in this bin is at most2^(1-h-l)/c.

For the dyadic birth block2^ell<=c<2^(ell+1), ell>=2, this gives

    E_(ell,h,l)<=2^(1-h-l).

Every physical harmonic coverage is at most(i-c)/c=x<=2^(-h). Also i<r<=2c for y<=1, so covered cuts satisfy2^ell<b<2^(ell+2), whose harmonic weight is at most2log2. Exact coverage and Cauchy therefore give

    I_(ell,h,l)<=2^(1-2h-l),
    N_(ell,h,l)<=2 sqrt(log2) 2^(-h-l/2).

These are bounds on selected subprofiles whose physical record components are each counted once. No row/cut is assigned an independent common budget.

## Eligible bins and summation constants

Put s=2h+l and D=nu*log_2(ell log2)>0; the logarithm in D is explicitly base2. The strict lower bin endpoints give

    x^2 y >2^(-s-3).

For a record eligible for A57, log c>=ell log2 implies x^2y<=2^(-D). Consequently s>D-3. The smallest allowed nonnegative integer is exactly

    S=max(0,floor(D-3)+1).

For fixed s, the number of nonnegative pairs(h,l) with h>=l and2h+l=s is at mosts+1. (The sharper range is ceil(s/3)<=h<=floor(s/2); no sharp count is needed.) Put rho=1/sqrt2. Then

    sum_{s>=S}(s+1)rho^s
      =rho^S*((S+1)-S rho)/(1-rho)^2
      <=(S+1)rho^S/(1-rho)^2.

For D>0 the above definition of S gives both S+1<=1+D and

    rho^S<=2^(3/2)(ell log2)^(-nu/2).

The latter follows from S>D-3; when S=0 the same inequality is valid because D<3. Thus the short-y part of each birth block obeys

    N_ell_short <= 2^(5/2)sqrt(log2)/(1-1/sqrt2)^2
                  *[1+nu log_2(ell log2)]/(ell log2)^(1+eta/2).

The sum over ell>=2 converges for every fixed eta>0. Together with the finite A56 bound at q=nu/2, this proves a uniform norm for the complete A57 selected class, for all finite original M,T and without cap. The harmless overcounts only enlarge the explicit upper bound; no actual arbitrarily long capped prefix is presumed.

## eta=1/4 and earlier selected classes

For eta=1/4, nu=9/4. The exact complementary condition is

    (i-c)^2 min(c,r-c) > c^3/(log c)^(9/4).

A55 with q=3/4 is contained in the A57 paid class: its y<=(log c)^(-3/4)<1 and x<y give x^2y<=y^3<=(log c)^(-9/4). A56 with q=5/4 is also contained: x^2min(1,y)<=x^2<=(log c)^(-5/2)<=(log c)^(-9/4), since log c>1. No extra finite classifications are needed for these inclusions.

At eta=0, this displayed short-y majorant has order(log ell)/ell and is not summable; the A56 long-y bound reaches its q=1 boundary as well. This establishes failure of these sufficient majorants at the endpoint only. It does not refute uniformity of the eta=0 class, the frozen estimate or Q1.

## Logical role and scope

A57 is a proved uniformly paid full-record subclass by an independent hand argument; the final complementary profile norm is unproved. Original u_r^[M] includes components k>T when M>T, its terminal alpha_(M+1) is unchanged, and all cut support/coverage remains physical. No full Lean proof, CoreUniform theorem, literal Q1 proof/counterexample or clean final axiom closure is claimed. No finite operation was performed for A57. A next estimate may use the exact residual delay-product lower bound but must continue to control the unchanged remaining profile.

## Source binding

This review uses only the already proved local source-count, full-price and birth-group results. SHA-256:

- `A55_FULL_PRICE_SHORT_OUTPUT_DELAY_REVIEW.md`: `19258159be0028e98693e6aafb82a89662894e609347fa461ff73fcf25aff51f`
- `A56_FULL_PRICE_SHORT_LOWER_OUTPUT_DELAY_REVIEW.md`: `d949daf8f3bbaf26bda14920611ccba522c47325a28a30701b99b2ba5f1dcb96`
- `A53_BIRTH_RELATIVE_COMPONENT_TAIL_REVIEW.md`: `befdce4b639afa97044cb66628797a00e60387dd2df53169585453a2f57db208`
