# A30 independent hand review: simultaneous fixed-stratum compression

2026-09-09. The proposed simultaneous S and forbidden-kernel upper
bound is valid. No new finite experiment, history or Lean run was
performed for this review.

## Precisely fixed parameters

Let H,ell,q,a be integers satisfying

    1<=ell<H, 0<=a<=ell-1, 0<=q-a<=H-ell.

Take any D subset of{1,...,H-1} with card D=q and
card(D intersect{1,...,ell-1})=a. Put d=q-a and define

    D*={ell-a,...,ell-1} union {H-d,...,H-1}.        (1)

An interval of length zero denotes the empty set. The two parts in
(1) are disjoint and lie in their prescribed strata: H-d>=ell.
Thus D* has exactly the same q and a as D. The a=0, d=0 and d=H-ell
endpoint cases are all included.

## The squared-label sum is maximized simultaneously

List the a low labels increasingly as x_1<...<x_a. Then

    x_j<=ell-a+j-1.

Similarly, for the d eligible forbidden labels y_1<...<y_d,

    y_j<=H-d+j-1.

All labels are positive, so squaring and summing these coordinatewise
inequalities proves

    S(D):=sum_(x in D)x^2<=S(D*).                   (2)

No source endpoint realization is needed for this finite-set argument.

## The available-label kernel is also maximized, for every h

For any integer j in[ell,H-1], a set of d eligible forbidden labels
can place at most H-1-j labels after j. Hence

    card(D intersect[ell,j])>=max(0,d-(H-1-j))
       =card(D* intersect[ell,j]).                 (3)

Let U_D=[ell,H-1] minus D and similarly U_*. Subtracting (3) from the
common interval length j-ell+1 gives

    card(U_D intersect[ell,j])<=card(U_* intersect[ell,j]).

For every nonnegative integer h, min(h,.) is increasing. Applying
the exact cumulative formula from A29 therefore proves, simultaneously
for all h,

    F_D(h)<=F_D*(h).                               (4)

This supplies a direct proof of the claimed majorization; no ambiguous
pairwise swaps or reordered cutoffs are required. Moving low labels
within the low stratum affects S but never the available set U_D.

The available labels of D* are precisely

    U_*={ell,...,H-q+a-1},
    card U_*=H-ell-q+a.

Writing z=min(h,H-ell-q+a), the exact expression is

    F_D*(h)=z(1-ell/H)-z(z-1)/(2H).                (5)

If q-a=H-ell, the available set is empty, z=0 and F=0. If h=0 the
same conclusion holds. The cutoff remains the original strict
integer ell; (1)-(5) do not weaken it.

## Nonnegative common-price summation

For any finite collection of nonnegative coefficients lambda_k and
integer capacities h_k, (2) and (4), with nonnegativity, give

    S(D) sum_k lambda_k F_D(h_k)
       <=S(D*) sum_k lambda_k F_D*(h_k).            (6)

In the research application lambda_k=kappa_k/H_k^2 is the unchanged
genuine component coefficient and h_k=binom(min(k,T)-b,2). All these
coefficients and actual rank horizons stay fixed while deriving (6).
The same D, H, ell, q and a belong to the fixed cut b and are used for
every component, including k>T. There is no independent choice of a
or forbidden labels per component and no reset of alpha_(M+1).

Combining (6) with the actual A29 upper bound is legitimate for every
actual Sidon input D satisfying the stated integer constraints. D*
is an extremal set in a larger class of integer label sets. It is not
asserted to be the difference set of a point sequence, to preserve
actual source endpoints, or to be realizable simultaneously with the
given diameters and future outputs. Such realization is unnecessary
for this upper inequality, but cannot be assumed in later arguments.

## Changing a is a separate optimization

The result fixes a. When a is increased by one within its feasible
range, D* replaces the eligible label H-q+a by the low label ell-a-1.
The latter is smaller, so S(D*) decreases. Its available interval
gains one label and F_D*(h) is nondecreasing for every h. The product
therefore has competing changes; this proof does not make a=0 a
maximizer. Any later optimization over a must keep its allowed range
and the same choice across all components.

The nonnegative finite-set envelope is now justified. Whether it is
small enough after retaining actual additive geometry, prices and
all cuts remains unresolved. It is not a fixed-cap Sidon counterexample,
a uniform U4-F estimate or a Q1 result.

## Nondecay of this joint envelope on a nonphysical scalar input

Consider only the numerical compressed upper formula with scalar
diameters H_n=n^2 for n>=2. Fix b>=8, set H=b^2,
q=binom(b-1,2), a=0, and retain the original strict ell. Assume
M>=3b and T>=2b; in particular M=T>=3b is sufficient.

The diameter profile satisfies the C=1,m0=2 scalar cap and the scalar
rank packing lower bounds. The fixed-stratum constraints hold because

    b^2/8<=q<H/2, ell<=H/16,
    D*={H-q,...,H-1}, min D*>H/2>ell.

The compressed square sum obeys

    S*>=q(H-q)^2>=b^6/32.

There are R=H-ell-q>=7H/16 consecutive available labels. At every
component2b<=k<=3b, min(k,T)>=2b and hence
h_k>=binom(b,2)>=H/4. The first floor(H/4) available labels can
therefore be used in F*. Each is below H/2, so its kernel is at
least1/2; floor(H/4)>=H/8. Thus

    F*>=H/16.

The original coefficients satisfy kappa_k>=4/k^5 and here
1/H_k^2=1/k^4. Summing at least b integer components in2b..3b gives

    sum kappa_k/H_k^2>=4/(3^9 b^8).

Consequently this numerical joint envelope is bounded below by

    S* sum_(k=b+1)^M (kappa_k/H_k^2)F*(h_k)
       >=1/(128*3^9)=1/2519424.                   (7)

All constants and the onset b>=8 are valid. A future-horizon condition
such as T>=2b is necessary for the displayed h_k lower bound; M>=3b
alone would not suffice.

This is not an actual forbidden-difference construction. Any three
ordered old points require positive differences u,v,w with u+v=w.
Every label of D* is greater than H/2 while all are less than H, so
that relation is impossible. Also D*'s maximum H-1 exceeds the scalar
old span H_(b-1)=(b-1)^2; neither old-span compatibility nor nesting
of D* across b was imposed. These are explicit absent endpoint
constraints, not overlooked asserted hypotheses.

Equation (7) shows nondecay of the simultaneous S/F compressed
FORMULA on a larger scalar/cardinality class. It is not a lower
bound on actual F_D or actual core mass and does not establish a
nonbounded same-cap Sidon family. The same a=0 and same D* are used
throughout each cut's component sum; no component chooses its own
forbidden-label set.

## Source and verification scope

The exact forbidden-label kernel and its genuine-price scope are those
of A28 in the execution-workspace WORKING_PROOF.md, previously bound
at whole SHA-256

    feb47de100cec436b90a146b4dede3f1ce1f153487a0181cbb664393246e30f4

and A28 section SHA-256

    8424500559aea434a3c4f1a7f83ab39b318d2be4d029e5a4ebf624d627c4e0e0

A29's cumulative representation is independently derived above and
checked in its separate four-cell evidence; no finite sample is used
as evidence for the universal proof (1)-(6). This note records hand
mathematics only. No full actual-core or norm formalization is claimed.
