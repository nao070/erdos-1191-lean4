# Independent review: actual fixed-middle-pair occupancy and genuine prices

2026-09-09. All proposed cardinality, price and fixed-pair norm estimates
pass independent hand review with the nonnegative future-size condition
stated below. No new experiment, history, record enumeration or Lean
build was performed for this review.

## Domains and the three actual equations

Fix an actual increasing integer Sidon history, middle ranks q<s, its
positive middle difference B=a_s-a_q, and a cut b>s. For a component
with t=min(k,T)>=b put

    P=q-1, V=b-1-s, m=t-b.

Thus all three sizes are nonnegative. The component expansion uses
k>=b+1 and b<T, so this condition is automatic there. A nonempty BH
record in the fixed-pair class has ranks

    x<q<s<c<b<i<r<=t.

In particular m>=2 whenever the class is nonempty. If P=0 or V=0 it is
also empty. Write A=a_q-a_x and Cgap=a_c-a_s. The original type-2 minus
and type-3 plus BH channels give precisely these equations:

    plus:        a_c+a_i=a_x+a_r+B;
    minus C>A:   a_x+a_c+a_i=a_r+a_q+a_s;
    minus A>C:   a_x+a_c+a_r=a_i+a_q+a_s.             (1)

These follow respectively from the actual positive output differences
A+Cgap, Cgap-A and A-Cgap. In the actual Sidon history A=Cgap is
impossible for these disjoint old pairs; it would duplicate a positive
difference. It could not create a positive minus output in any case.
Hence the two minus signs partition that matching, rather than
introducing a second minus record for one quadruple.

## Injection after fixing any two of x,c,i,r

Within each sign class, fixing any two coordinates in (1) leaves an
equation for the other two actual point values of one of the forms

    a_u+a_v=constant, or a_u-a_v=constant,

possibly after multiplying the equation by-1. Every variable has
coefficient+1 or-1, so there is no coefficient2 exception.

For the sum case, Sidon two-sum uniqueness fixes the unordered pair.
The strict global order x<c<i<r fixes which of those two values is
assigned to which unknown coordinate, so the swapped possibility is
excluded. Repeated-point sums cannot supply a candidate because the
two unknown ranks occupy distinct ordered positions.

For the difference case, the two unknown values are distinct and their
order is fixed by x<c<i<r. The resulting constant is therefore nonzero
whenever a solution exists. Taking the positive orientation reduces
to unique positive differences. If the constant is zero, the class
fiber is empty, not a family of zero-difference solutions.

This proves the asserted injection for any choice of two fixed
coordinates. In particular, projection to(x,c), (x,i), (c,i), or(i,r)
gives the per-sign bounds

    P*V, P*m, V*m, binom(m,2).

The last bound uses the ordered future ranks i<r, so each unordered
future pair corresponds to only one possible ordered pair. All three
sign classes together have at most3Pm,3Vm,3binom(m,2) records. For the
first projection there is the better bound2PV: for each old quadruple
(x,q,s,c), there is at most one actual plus output and one actual minus
output, by actual positive-difference uniqueness.

Consequently the original strict-core BH count satisfies

    n_B(b,k)<=min(2PV,3Pm,3Vm,3binom(m,2)).           (2)

The type-1 minus record belongs to AC, not BH, and is not added to this
count. Deleting rows by any of the original strict gates, or by a fixed
large-old-gap selection, preserves every upper bound. This estimate
allows the actual repeated middle-pair uses certified in A26; it does
not contradict those records or restore the false one-use shortcut.

## Genuine full-horizon fixed-pair price

For fixed M,T and cut b<T, let w_B be the BH part of the original
profile carried by this actual middle pair. Finite rearrangement of
the unchanged component sums gives exactly

    w_B=B sum_(k=b+2)^M kappa_k/H_k^2
             *sum_(h: middle B, c_h<b<i_h,
                      r_h<=min(k,T), original strict gates) Hquad_h.
                                                               (3)

Here kappa_k=alpha_k-alpha_(k+1)>0 and
alpha_k=1/[k^2(k-1)^2]. All components k>T remain in (3), with their
same output set through T. There is no reset of alpha_(M+1).

Every actual Hquad_h<=H_b and H_k>=H_b>0. Thus its width divided by
H_k^2 is at most1/H_b. Also m_k=min(k,T)-b<=k-b. Applying (2) separately
to its nonnegative component sums yields

    w_B <= (B/H_b) min(
        2PV*(alpha_(b+2)-alpha_(M+1)),
        3min(P,V)*sum_(k=b+1)^M kappa_k(k-b),
        3sum_(k=b+2)^M kappa_k binom(k-b,2)).         (4)

For an empty horizon M<b+2, w_B=0 and the desired conclusion is
immediate; formula (4) is used only when its displayed starting ranks
are available. Adding the k=b+1 term in the second upper bound is
legitimate and nonnegative, even though actual records require r>=b+2.

The two exact finite Abel identities are

    sum_(k=b+1)^M kappa_k(k-b)
      =sum_(k=b+1)^M alpha_k-(M-b)alpha_(M+1),

    sum_(k=b+2)^M kappa_k binom(k-b,2)
      =sum_(k=b+2)^M (k-b-1)alpha_k
         -binom(M-b,2)alpha_(M+1).                 (5)

The terminal subtractions in (5) have the stated coefficients and
signs. Dropping them for upper bounds is not replacing the actual
prices. The reviewed elementary inequality

    alpha_k<=((k-1)^(-3)-k^(-3))/3

then gives

    sum kappa_k(k-b)<=1/(3b^3),
    sum kappa_k binom(k-b,2)<=1/(6b^2).             (6)

For the second inequality, Abel summation first leaves at most
(1/3)sum_(j=b+1)^infinity j^(-3), which is at most1/(6b^2) by the
integral from b to infinity. These infinite sums are numerical
majorants only; no infinite capped history is used.

Equations (4)-(6) prove exactly the proposed estimate

    w_B <= (B/H_b) min(2PV alpha_(b+2),
                       min(P,V)/b^3, 1/(2b^2)).    (7)

No fixed cap was needed for (2)-(7). The labels B are actual integer
differences and their endpoint pairs are fixed by Sidon; the bound is
not a scalar multiplicity construction.

## The fixed-pair square-root harmonic bound

A record involving this middle pair can cover only cuts b>=s+2.
Actual Sidon packing gives H_b>=b(b-1)/2, so the first term of (7)
implies

    w_B <= 4B(q-1)(b-1-s)/[b(b-1)(b+2)^2(b+1)^2]
         <=4B(q-1)/b^5.                            (8)

The denominator is at least b^6 for b>=2. For example,
(b-1)(b+2)>=b^2 and the remaining factors
b(b+2)(b+1)^2>=b^4. Also b-1-s<=b. Therefore

    N_B:=sum_b sqrt(w_B)/b
       <=2sqrt(B(q-1)) sum_(b=s+2)^infinity b^(-7/2)
       <=(4/5)sqrt(B(q-1))/(s+1)^(5/2)
       =: beta_(q,s).                              (9)

The last inequality integrates x^(-7/2) from s+1 to infinity. It is
valid uniformly over both actual horizons. If additionally s>=m0,
the unchanged cap gives B<=H_s<=Ccap*s^2*log(2s), hence

    beta_(q,s) <= (4sqrt(Ccap)/5)
        *sqrt(q-1)*s*sqrt(log(2s))/(s+1)^(5/2).     (10)

No cap is imposed below m0. For q=1 there is no available outer x;
the count, w_B and beta are all zero as required.

## Why summing these separate pair allowances is insufficient

For any available finite increasing integer history of length L and
any8<=s<=L, consider ceil(s/4)<=q<=floor(s/2). There are at least s/8
such q, each has q-1>=s/8, and integer spacing alone gives
B=a_s-a_q>=s-q>=s/2. Since s+1<=2s,

    beta_(q,s)>=[1/(5*2^(5/2))]s^(-3/2),
    sum_(q=ceil(s/4))^(floor(s/2)) beta_(q,s)
       >=[1/(40*2^(5/2))]s^(-1/2).                (11)

Both constants in (11) are correct. In particular the finite sum of
the displayed beta allowances over all pairs through L is at least

    [1/(40*2^(5/2))] sum_(s=8)^L s^(-1/2).         (12)

This grows with the available length in the numerical estimate itself.
It is a lower bound on a proposed sum of UPPER allowances, not on the
actual profile, any w_B, or N_B. Some pairs in (12) may have no actual
strict-core output at all. No lower bound on the sum over only those
pairs that are actually used is asserted.

Equation (12) is stated for every finite prefix that is available.
It does not establish the existence of arbitrarily long prefixes
under the same fixed cap, an infinite capped history, or nonboundedness
of actual capped profiles. Thus the appropriate conclusion is that
unrestricted independent summation of these per-pair allowances has
no summable length-independent numerical envelope. Any successful
use must retain joint occupancy, actual gate support, cancellation,
or other information that (9) forgets.

The fixed-pair estimates are valid mathematical progress, but neither
they nor (12) resolve frozen U4-F or Q1. The next all-pair estimate must
charge actual repeated middle pairs and their physical widths jointly.

## Source binding and verification scope

The source read for this review was
`research/u4f_core/WORKING_PROOF.md` in the execution workspace, whole
SHA-256:

    332eb31866cc5767ae52d53397e3a23a47fe477796518659c52f90df7112a781

Reviewed reused section hashes (UTF-8 heading through before next ##):

    A02: 51612ecf37559cc9ba5b23ca2d3478e7daf4c4fdfedfa02de08b209e03953c0b
    A17: 306723f8f8488d697d855f99267c0d3c2f64f4ae297c1d4d1d95bebcefc97e50

Original root `research/NEXT_THEOREM_CONTRACT.md` SHA-256:

    54014f80f1460195a0c48242bc6fb44d357939e8c4942548b47f2486c922270e

The new estimates above are independently reviewed hand mathematics.
No new Lean formalization, compilation or theorem audit is claimed
by this note. The prior exact seven-pair trace is reused only as a
consistency check on the rejected one-use assumption; it is not
evidence for universal upper bounds.
