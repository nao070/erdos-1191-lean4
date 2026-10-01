# Independent review: full-horizon original-core cut flux

2026-09-09. The proposed identities and constants are valid by hand proof.
They retain the original strict core, actual source/output correlations,
and genuine two-horizon component prices. No new history or finite scan
was run for this review. This is a bounded-variation estimate per unit
logarithmic cut scale, not a uniform square-root harmonic-sum estimate.

## Exact signed identity

Fix one actual finite Sidon history and M,T with T<=M. Each original
strict-core physical record h has fixed positive weight

    w_h=d_h e_h u_[r_h]^[M],
    u_r^[M]=sum_(k=r)^M (alpha_k-alpha_(k+1))/H_k^2,
    alpha_k=1/[k^2(k-1)^2].

Its sole cut dependence is the interval c_h<b<i_h. For 2<=b<=T-2 put

    B_b=sum_{h:c_h=b, i_h>b+1} w_h,
    R_b=sum_{h:i_h=b+1, c_h<b} w_h.

Then, record by record and hence after summation,

    P_(b+1)^core(M,T)-P_b^core(M,T)=B_b-R_b.       (1)

The case c=b,i=b+1 covers neither cut and is in neither boundary. One
may also include b=T-1 by defining P_T=0; the same formulas then hold.
All strict gates remain fixed. The finite component tail k>T is retained
in every u_r^[M] and in both sides of (1).

## Birth envelope

A birth at c=b has four ordered old endpoints p<q<s<b, giving at most
binom(b-1,3) old quadruples. For a fixed quadruple write

    A=a_q-a_p, B=a_s-a_q, Cgap=a_b-a_s,
    Hquad=A+B+Cgap<=H_b.

The three possible disjoint source matchings have products ACgap,
ACgap+B*Hquad, and B*Hquad. Their sum is

    2ACgap+2B*Hquad=2(A+B)(B+Cgap)<=2Hquad^2<=2H_b^2. (2)

Actual output difference uniqueness allows at most one output per
matching. The two minus matchings can share that output, but they are
already two distinct physical records among these three. Distinct
outputs of the plus/minus matchings need not have ordered prices.
Every birth in (1) satisfies i>=b+2 and r>=b+3. Monotonicity of actual
diameters and telescoping of positive kappa_k=alpha_k-alpha_(k+1) give

    u_r^[M] <= (alpha_r-alpha_(M+1))/H_b^2
             <= alpha_(b+3)/H_b^2.                    (3)

This is only an upper inequality; it never resets alpha_(M+1) or
substitutes a different terminal component price. Equations (2)-(3)
yield, for b>=4,

    B_b <= 2 binom(b-1,3) alpha_(b+3)
         = (b-1)(b-2)(b-3)/[3(b+3)^2(b+2)^2]
         <= 1/(3b).                                 (4)

For b=2,3 no four old endpoints exist, so B_b=0. Thus the final bound
holds for all relevant b>=2.

## Retirement envelope and the actual Sidon dispersion improvement

At retirement i=b+1, original source endpoints have c<b. Enlarge their
positive labels to the actual difference set D of the first b points;
this enlargement is legitimate and only increases a nonnegative bound.
Put S=sum_(d in D)d^2 and H_b=a_b-a_1.

For each fixed future endpoint r>=b+2, t=a_r-a_(b+1)>0. The graph on D
with edges {e,e+t} has degree at most two, so

    sum_{e:e,e+t in D} e(e+t) <= S.                  (5)

Positive-difference uniqueness ensures that each graph edge supplies
at most one physical source-pair record for that actual output. The
six-distinct and strict-core conditions select a subset; they cannot
create multiplicity. Therefore

    R_b <= (S/H_b^2) sum_(r=b+2)^T alpha_r
         <= (S/H_b^2)/[3(b+1)^3].                   (6)

For the last step use, for r>=2,

    alpha_r <= ((r-1)^(-3)-r^(-3))/3,

whose right side minus alpha_r is 1/[3r^3(r-1)^3]. The infinite sum is
a numerical upper bound; it does not posit an infinite extension.

The exact variance identity for the b actual old point values gives
S/H_b^2<=b^2/4. Consequently

    R_b <= b^2/[12(b+1)^3] <= 1/(12b).              (7)

For b>=max(3,m0), the reviewed A02 packing/dispersion calculation and
the unchanged all-rank cap imply the sharper bound

    R_b <= b^2/[12(b+1)^3]
           * [1-(1-4/b^2)/(12 Ccap log(2b))].        (8)

Here the point count is b, not b-1: (6) deliberately used the enlarged
first-b difference set. The bracket is nonnegative on an actual
admissible history. No cap below m0 is used. For completeness the
underlying diameter form is

    S/H_b^2 <= (b^2/4)[1-(b^2-4)/(12H_b)],

so (8) has exactly the A02 constant after replacing H_b by its cap.

## BH, AC, and fixed quadruple selections

No correction to the constants is needed for the A10 decomposition.
For each physical record, assign its BH fraction theta_h as follows:

    type 1: theta=0;
    type 2: theta=B*Hquad/(ACgap+B*Hquad);
    type 3: theta=1.

Then 0<=theta_h<=1, and the AC fraction is 1-theta_h. These coefficients
are fixed for the record and independent of the cut. Multiplying (1)
recordwise by either fraction proves the corresponding exact BH or AC
boundary identity; its two nonnegative boundary masses are termwise
bounded by the full original B_b and R_b. The type-2 record is split
into complementary masses, not counted twice at its full weight.

The same reasoning permits any fixed subset of old quadruples, including
the selection that all three old gaps exceed c^2/(log c)^3. That threshold
is tied to the record's latest birth c, and hence does not change as the
cut moves. Arbitrary cut-dependent re-selection would instead have an
extra selection boundary and is not asserted here.

## Consequence and limitation

For the full profile, or either component or fixed selection above,

    -1/(12b) <= P_(b+1)-P_b <= 1/(3b).              (9)

In particular |P_v-P_u|<=sum_(b=u)^(v-1) 1/(3b), at fixed M,T.
This logarithmic-scale regularity allows a profile that remains of
positive size on each successive dyadic block. It neither implies
decay of I_j nor summability of sum_j sqrt(I_j). The exact A24 finite
counterexamples are consistent with (9): positive net birth is allowed,
including on all-large-gap records and when unweighted counts decrease.

Logical role: a valid actual-record flux envelope and an explicit
location of the lost summability. The frozen U4-F estimate and Q1 remain
unresolved. The next nonduplicate task is a compensated or summed
cut/future-group estimate retaining the real correlations. This note
contains hand proof only; no new Lean verification is claimed.
