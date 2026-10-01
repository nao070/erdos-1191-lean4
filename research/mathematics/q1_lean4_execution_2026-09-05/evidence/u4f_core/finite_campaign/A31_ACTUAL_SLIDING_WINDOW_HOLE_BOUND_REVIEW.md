# A31 independent review: actual endpoint windows force forbidden-label loss

2026-09-09. The proposed estimate and constants pass independent hand
review after one wording correction: the NONZERO support of the window
count need not have cardinality H0+y. Rather, it is contained in a
shift interval of cardinality H0+y, with zero windows included when
applying Cauchy. This correction leaves all formulas unchanged.
No finite experiment, new history, record scan or Lean run was used.

## Exact window identities on the actual old endpoints

Let the old n=b-1 integer points have minimum a_1 and maximum a_n,
and span H0=a_n-a_1. For integer y>=1 define

    f_z=card{old points in {z,z+1,...,z+y-1}}.

All nonzero f_z occur for

    a_1-y+1<=z<=a_n,

an integer interval of exactly H0+y possible starting positions.
Some of these windows can have f_z=0. Summing over this whole interval
is equivalent to summing over all integer starts. Every old point is
contained in exactly y windows, giving

    sum_z f_z=ny.                                  (1)

Two distinct old points at positive distance d belong together to
exactly(y-d)_+ windows. Expanding f_z^2 gives the diagonal contribution
ny plus twice the unordered-pair contribution. Actual Sidon uniqueness
makes each old positive difference occur once in the set D, hence

    sum_z f_z^2=ny+2G_D(y),
    G_D(y)=sum_(d in D, d<y)(y-d).                  (2)

The strict d<y is correct for a window containing y consecutive
integers: two points at distance y cannot both belong to it.
Cauchy on the ambient H0+y starts, including zero counts, now gives

    G_D(y)>=[n^2 y^2/(H0+y)-ny]/2.                 (3)

This uses actual endpoint incidences. It would not be valid for an
arbitrary integer set D with only its cardinality specified, because
such a set need not arise from these point-pair overlaps.

## A direct proof of the hole contribution to F-F_D

Let H=H_b, ell>=1 and ell<H. For h>=0 put
z=min(h,H-ell), and suppose y is an integer with

    ell<=y<=ell+z.

The cumulative representations of the old unrestricted packing F
and the forbidden packing F_D give

    H(F-F_D)=sum_(j=ell)^(H-1)
       [min(h,j-ell+1)
          -min(h,j-ell+1-card(D intersect[ell,j]))]. (4)

Every bracket is nonnegative. For ell<=j<y, the condition y<=ell+z
ensures j-ell+1<=h, so that bracket is exactly
card(D intersect[ell,j]). Keeping just these brackets proves

    F-F_D >= (1/H)sum_(ell<=d<y, d in D)(y-d).      (5)

Thus no informal matching of deleted top slots with replacement slots
is needed. Equation (5) includes y=ell, when its right side is zero.
At most ell-1 distinct positive integer labels lie below ell, and
each contributes at most y to G_D(y). Therefore

    F-F_D >= [G_D(y)-(ell-1)y]/H.                  (6)

The right side can be negative without invalidating the bound; the
large-b conditions below make the retained lower bound positive.

## Checking the stated choices and all numerical constants

Assume b>=max(8,m0), the unchanged fixed cap
H_b<=Ccap*b^2*log(2b), and

    (log b)^5>=1536 Ccap log(2b),
    b>=768 Ccap log(2b).                            (7)

Set

    ell=floor(b^2/(log b)^5)+1,
    y=floor(b^2/8).

Actual integer Sidon packing and the cut order imply

    H>=b(b-1)/2>=b^2/4,
    H0<=H,
    b^2/16<=y<=b^2/8<=H/2,
    n=b-1>=b/2.

Since b>=8, log b>=2 and

    ell<=b^2/32+1<=b^2/16<=y.                     (8)

Also y<=binom(b,2). If h>=binom(b,2), then y<=h and y<=H. Hence
y<=min(ell+h,H)=ell+min(h,H-ell), which is the upper condition
needed for (5). In particular ell<H follows from ell<=y<=H/2.

Because H0+y<=3H/2, the main term in (3) satisfies

    A:=n^2 y^2/[2(H0+y)]
      >=b^6/(3072H)
      >=b^4/[3072 Ccap log(2b)] =:A0.             (9)

The two subtracted errors satisfy

    ny/2<=b^3/16<=A0/4,
    (ell-1)y<=b^4/[8(log b)^5]<=A0/4.             (10)

The first comparison to A0/4 is exactly the second condition in(7):
12288/16=768. The second is exactly the first condition in(7):
12288/8=1536. There is no missing factor2 from the unordered pairs
or from Cauchy.

Combining (3), (6), (9) and (10) yields

    F-F_D >= A0/(2H)
       >=b^2/[6144 Ccap^2 (log(2b))^2].           (11)

The final division uses the same actual fixed-cut cap on H. All
constants, the floor choices, and the strict window/output endpoints
are therefore consistent.

## Horizons and logical role

For the original component capacities
h_k=binom(min(k,T)-b,2), the condition h_k>=binom(b,2) holds whenever
T>=2b and k>=2b. If M>=3b, the integer components2b,...,3b are
available and can all be weighted by their original nonnegative
kappa_k/H_k^2. The same D,H,ell,y and cap constants are used for all
of them. Components after T retain the fixed output horizon, and no
terminal coefficient is reset.

This is a noncircular bound using actual old endpoint windows and
actual Sidon difference uniqueness, together with the fixed cap at b.
It does not assert the existence of arbitrarily long capped histories;
it applies to each finite admissible history meeting the stated rank
and horizon conditions. It proves a positive difference between two
upper packing formulas, not a lower bound on the true core profile.
The full uniform square-root harmonic estimate and Q1 remain open.

## Exact genuine-price consequence

Define the two actual-input upper formulas at the same cut by

    U0=S sum_(k=b+1)^M (kappa_k/H_k^2)F(h_k),
    UD=S sum_(k=b+1)^M (kappa_k/H_k^2)F_D(h_k).

Assume the conditions above, M>=3b and T>=2b. Let
q=card D=binom(b-1,2). For b>=8, q>=b^2/8. Since D contains q
distinct positive integers,

    S>=sum_(j=1)^q j^2>=q^3/3>=b^6/1536.

For all k in2b..3b, the fixed all-rank cap and unchanged coefficients
give

    kappa_k/H_k^2
      >=4/[Ccap^2*k^9*(log(2k))^2],
    sum_(k=2b)^(3b) kappa_k/H_k^2
      >=4/[3^9*Ccap^2*b^8*(log(6b))^2].

Apply (11) at those same components and retain only their nonnegative
loss contributions. Then

    U0-UD >=
      1/[2359296*3^9*Ccap^4*(log(2b))^2*(log(6b))^2]. (12)

The numerical factor is exact: 1536*6144/4=2359296. The all-rank cap
is used at k>=2b>=m0, so it is available at every retained component.

Equation (12) is a guaranteed genuine-price saving between two valid
upper formulas on an actual finite Sidon input. It is neither a lower
bound on the true profile nor a uniform-norm theorem. Its displayed
lower bound decreases as(log b)^(-4) for fixed Ccap; no matching upper
bound or asymptotic equality for the actual saving is claimed. It
remains a conditional finite-M,T theorem and assumes no arbitrary-
length capped-prefix or infinite-history existence.

## Source and verification scope

The strict cutoff and genuine-price convention are the unchanged A28
ones, previously bound at section SHA-256

    8424500559aea434a3c4f1a7f83ab39b318d2be4d029e5a4ebf624d627c4e0e0

The underlying frozen NEXT_THEOREM_CONTRACT.md source SHA-256 is

    54014f80f1460195a0c48242bc6fb44d357939e8c4942548b47f2486c922270e

A29's cumulative representation and the actual source-set convention
are used as stated; no finite values supply the universal proof here.
This note records independent hand mathematics only. The next step is
to use actual joint source/output information in the accumulated
genuine-price estimate, without treating components or hole thresholds
as independent budgets.
