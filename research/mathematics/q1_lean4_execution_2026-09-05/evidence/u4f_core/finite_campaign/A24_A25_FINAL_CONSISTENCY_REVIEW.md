# Independent consistency review of A24-A25

2026-09-09. Reviewer: /root/u4f_finite_attack. The mathematical text of
A24 and A25 passes independent review. No substantive correction was
needed. Final source and verification bindings are recorded in the
companion `A24_A25_final_review_manifest.json`.

## A24: exchange identities and scope of the finite counterexamples

For the two actual zero-one changed banks w_plus and w_minus, the
identity C(f+w)=C(f)+sum f*w is exact even when the two changed banks
overlap each other. Substituting f=v_before-w_minus gives precisely

    Delta C = sum v_before*(w_plus-w_minus)
              +sum w_minus-sum w_plus*w_minus.

The overlap correction therefore has the stated negative sign.
The general capacity parameters give

    Delta delta=(d_after-d_before)sum f
       +(d_after-1)sum w_plus-(d_before-1)sum w_minus
       -2sum f*(w_plus-w_minus),

as in A24.2. No equality of the two total bank sizes or two capacities
is assumed. In the requested transition the old right bank gains a_b
and the future bank loses a_(b+1); both cut and future endpoint indices
are correct.

The record boundary identity has exactly the open coverage convention
c<b<i. Birth is c=b,i>b+1; retirement is c<b,i=b+1. The empty interval
c=b,i=b+1 belongs to neither boundary. The l selector and strict core
predicates are preserved, as are the fixed large-gap quadruple selector
and the genuine component kappa_k/H_k^2.

The saved A24 numbers agree with the independent finite result:

* Variant, large gaps, l6: 3 births and 5 retirements, count84->82;
  birth BH571826, retirement BH147453, coefficient5348845->5773218.
* The positive priced increment is exactly424373/1148518878296832.
* Greedy large-gap l6 loses7 records and gains1163678 in BH coefficient.
* Whole large-gap BH coefficient changes are47682425 and45546481.

All these are for one actual component k48 at cuts24->25 in the two
previously certified C=1,m0=2 histories. The text explicitly prevents
promotion to full-horizon M96 or asymptotic claims. All six raw-bank
cases and all twelve selected weighted identities are accounted for;
the three l-selected cases are not added as independent cut budgets.
The exact data disprove both pointwise retirement domination and the
inference from a decreasing count to a decreasing physical BH weight.
They do not disprove a compensated or summed flux estimate.

## A25: actual full-horizon envelopes

The derivation agrees with the separate full-horizon review. Four old
endpoints with latest birth b admit at most three actual source
matchings. Their products sum to2AC+2BHquad<=2H_b^2, and every birth
has i>=b+2,r>=b+3. Telescoping only as an upper inequality gives

    B_b<=2 binom(b-1,3) alpha_(b+3)<=1/(3b).

For retirement i=b+1, the actual shifted-edge graph on the enlarged
first-b difference set has maximum degree2. Its total source product
is at most S_b for each actual output r. The genuine-price inequality,
the numerical alpha telescope, and actual dispersion imply

    R_b<=S_b/[3(b+1)^3 H_b^2]<=b^2/[12(b+1)^3].

The A02 cap improvement in A25.2 uses point count b, which is correct
for that enlarged difference set. Since A25 assumes b>=3, additionally
requiring b>=m0 suffices for the stated cap refinement. The signed
envelope follows from the exact nonnegative boundary masses and does
not assume the false retirement-domination candidate.

The BH/AC decomposition assigns complementary fixed nonnegative
fractions to the type-2 record. Each component's boundary mass is
termwise dominated by the original record mass. Fixed large-gap
quadruple selections are also legitimate. No full weight is charged
twice and no new cut-dependent selection boundary is omitted.

Both M and T remain fixed through a cut transition. Actual prices
retain the common component tail k>T; the infinite alpha series is
only a numerical majorant, not a claim about an infinite Sidon history.

## A25: the numerical envelope no-go

Put epsilon=1/1000 and x=log b. The abstract profile is epsilon times

    max(0,min(x-log8,1,log(M-1)-x)).

Minimum and maximum preserve the common Lipschitz constant1 of the
three affine functions and zero. Thus

    |Delta p_b|<=epsilon log(1+1/b)<=epsilon/b.

For integer b<=7, both p_b and p_(b+1) vanish. Positive increments
therefore occur only for b>=8. The exact numerical birth envelope is

    E_B(b)=(b-1)(b-2)(b-3)/[3(b+3)^2(b+2)^2].

For b>=8, each numerator factor is at least b/2 and each denominator
factor before squaring is at most2b, proving

    E_B(b)>=1/(384b)>epsilon/b.

For C=1 and b>=3, log(2b)>1 makes the retirement bracket at least11/12.
Also (b/(b+1))^3>=27/64. Consequently its numerical upper envelope is
bounded below by

    E_R(b)>=(1/(12b))*(27/64)*(11/12)
           =33/(1024b)>1/(64b)>epsilon/b.

The positive and negative parts of Delta p_b hence satisfy both
specified numerical boundary envelopes. These parts provide a valid
abstract signed boundary identity. No actual S_b, point sequence,
joint record bank, or component-price realization is inferred.

For M>8e^2+1, the plateau condition is exactly

    ceil(8e)<=b<=floor((M-1)/e).

On this interval p_b=epsilon, so the square-root harmonic sum is at
least sqrt(epsilon) times the harmonic sum on that interval, which
diverges as M tends to infinity. The initial cuts and terminal cut
M-1 are zero as stated. This is a sufficient construction to reject
the displayed numerical envelopes and endpoint conditions as a
standalone route to a uniform norm bound.

The construction is explicitly nonphysical. It does not meet, assert,
or refute actual Sidon, strict-core, common-tail consistency between
different horizons, or fixed-cap record realizability. Therefore it
is not a counterexample to frozen U4-F or Q1.

## Verification boundary and remaining task

This note independently reviews the mathematical statements and saved
A24 evidence. No new history, raw-fiber scan, evaluator run, or Lean
build was performed. The final pinned LEAN_VERIFICATION_06.json was
inspected by readback only: all eight recorded source/log/toolchain
file hashes match; compilation and type/axiom audit exit codes are 0;
all 22 supporting declarations list only propext, Classical.choice,
and/or Quot.sound. The four new declaration types in the saved audit
are the two zero-one exchange identities, generic finite-record
profile_step, and the nonnegative-gap quadruple product bound.
Supporting generic identities are not the actual-core instantiation
or the full all-history price/dispersion estimate.

The saved next action retains the signed boundary measure on the
actual integer middle gap B, starting with the eight-record A24
counterexample. Each mass keeps its physical Hquad and genuine
component price, and repeated uses of the same B-pair across cuts,
births and components must be charged jointly. No first-moment
identity alone is asserted to establish a new bound. The frozen
uniform U4-F estimate and the original Q1 remain unresolved.
