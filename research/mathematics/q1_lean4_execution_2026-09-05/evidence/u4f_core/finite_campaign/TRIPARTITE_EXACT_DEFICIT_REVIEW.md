# Exact tripartite deficit identity: one component of two existing histories

2026-09-09. All four requested finite checks PASS exactly. The scalar
nondecay argument also passes as a proof about a relaxation, explicitly
not about an actual Sidon history.

## Exact identity and the role of each loss

Fix the original b,l,k,T and let n=b-1, m=min(k,T)-b,
d=min(l,n-l,m), N=l(n-l)m. For the actual three-part sum fibers v_z,
positive-difference/repeated-sum Sidon gives 0<=v_z<=d and sum_z v_z=N.
Thus the nonnegative capacity deficit

    delta_lk=sum_z v_z(d-v_z)

satisfies the exact equality

    C_all=sum_z binom(v_z,2)=((d-1)N-delta_lk)/2.     (1)

Here C_all counts one BH matching per actual unordered triple collision:
type-2 minus or type-3 plus. The type-1 minus matching is an AC term
and is not counted a second time. As established in the independent
tripartite review, each collision has six distinct endpoints and the
correct old/future order. C_core is the subset satisfying the ORIGINAL
strict core gates and the chosen collection of old quadruples. Set
E_lk=C_all-C_core>=0. For the all-large-gap selection, E additionally
removes collisions whose old quadruple is outside that selection.

At component k let R_BH be the unpriced sum of B*Hquad over those
selected core matching records with upper output r<=min(k,T). Define

    U=(H_b/2)*sum_l g_l(d-1)N,
    Delta_cap=(H_b/2)*sum_l g_l delta_lk,
    Delta_gate=H_b*sum_l g_l E_lk,
    Delta_width=sum_core B(H_b-Hquad).

Then, with the same selected quadruples and gates throughout,

    U-Delta_cap=H_b*sum_l g_l C_all,
    U-Delta_cap-Delta_gate=H_b*sum_l g_l C_core
                         =H_b*sum_core B,
    R_BH=U-Delta_cap-Delta_gate-Delta_width.           (2)

Every loss is nonnegative. No cancellation estimate or cap assumption
is needed for the identity. To recover this component's priced BH mass,
multiply EVERY term of (2) by the same genuine kappa_k/H_k^2.
The full profile would sum such identities over k; the present finite
check does not purport to control that sum.

## Precisely bounded finite verification

Inputs are ONLY the two existing independently certified C=1,m0=2,M=96
histories. The fixed indices are b=24,k=48,T=96, so n=23,m=24. The
unchanged original record bank is filtered by c<24<i<r<=48, then by
matching type 2 or 3. A separate direct fiber enumeration forms the
triples from L={1,...,l}, R={l+1,...,23}, F={25,...,48} for each
1<=l<=22. It reconstructs every unordered collision's quadruple,
matching and output, and verifies that the selected original core
record keys are its exact core subset. It also checks (1) at every l.

The all-large-gap selection requires min(A,B,Cgap)>c^2/log(c)^3.
Previously certified integer thresholds were reused and their needed
c=4,...,23 floors independently reconfirmed from fixed-point rational
log enclosures. No comparison was UNKNOWN. Original input hashes were
checked against the existing independent certificates; no new history
or full-horizon enumeration was performed.

The exact unpriced terms are:

| History / selection | U | Delta_cap | Delta_gate | Delta_width | R_BH |
|---|---:|---:|---:|---:|---:|
| Greedy / all core | 3205864656 | 2979944118 | 7310430 | 76941442 | 141668666 |
| Greedy / all large gaps | 3205864656 | 2979944118 | 54205542 | 60114562 | 111600434 |
| Variant 1 / all core | 3009983688 | 2778975966 | 9102871 | 66734919 | 155169932 |
| Variant 1 / all large gaps | 3009983688 | 2778975966 | 57579028 | 52169120 | 121259574 |

The greedy history has H_24=774,H_48=4432; variant 1 has H_24=713,
H_48=4248. Greedy selected BH records number 2112 (948 minus,1164 plus)
for all core and 1615 (702 minus,913 plus) for all large gaps. Variant 1
has 2259 (1021 minus,1238 plus) and 1738 (756 minus,982 plus), respectively.

As fractions of U, Delta_cap is approximately 92.95289845% and
92.32528326%. The surviving R_BH is approximately 4.41904700% and
5.15517518% for all core, or 3.48113367% and 4.02857911% for all large
gaps. These percentages are presentation approximations only; every
ratio and every priced term is saved as an exact rational number.

The large observed capacity loss identifies information discarded by
the rank-only bound at this component. It is NOT a lower bound on that
loss for arbitrary rank, arbitrary history or either varying horizon.
In particular it does not justify replacing the actual deficits by a
fixed percentage throughout a proof of U4-F.

## Scalar relaxation lower bound: exact independent review

Set H_j=j(j-1)/2 and g_l=l. These are the diameters and gaps of the
integer sequence a_j=1+j(j-1)/2. They satisfy the fixed scalar cap
H_j<=j^2 log(2j), j>=2. But the sequence is NOT Sidon:

    a_4-a_3=7-4=3=4-1=a_3-a_1.

It cannot be used as an input history for the frozen theorem. We only
evaluate the explicit relaxed scalar expression

    U_b^[M]=(H_b/2)*sum_(k=b+1)^M (kappa_k/H_k^2)
       *sum_(l=1)^(b-2) g_l*l*(b-1-l)*(k-b)
                         *(min(l,b-1-l,k-b)-1).      (3)

For b>=16,M>=3b, retain only 2b<=k<=3b and
ceil(b/4)<=l<=floor(b/2)-1. There are at least b values of k and
at least b/8 values of l: floor(b/2)-ceil(b/4)>=b/4-2>=b/8.
On this range,

    H_b/2>=b^2/8,
    g_l>=b/4, l>=b/4, b-1-l>=b/2, k-b>=b,
    min(l,b-1-l,k-b)-1=l-1>=b/8.

Also kappa_k=4/[k(k^2-1)^2]>=4/k^5 and H_k^2<=k^4/4, so

    kappa_k/H_k^2>=16/k^9>=16/(3^9*b^9).

Multiplying these lower bounds, including BOTH the l-count and k-count,
gives

    U_b^[M] >= (b^2/8)*b*(16/(3^9*b^9))*(b/8)
                    *(b/4)*(b/4)*(b/2)*b*(b/8)
             =1/(1024*3^9)=1/20155392.               (4)

The constant and onset are therefore valid. All components in (3) use
the actual alpha_k-alpha_(k+1) difference; the demonstration does not
reset a terminal alpha. On this one scalar diameter sequence, (4)
holds simultaneously for every 16<=b<=floor(M/3), so the scalar
square-root harmonic majorant itself has an unbounded harmonic lower
bound as M grows.

The conclusion is only that keeping diameter caps and scalar gap sizes
while discarding actual Sidon deficits is insufficient for this bound.
The scalar model lacks the Sidon injectivity needed for (1)-(2); it does
not supply actual admissible fibers or an actual core mass, and it does
not refute U4-F or Q1. The finite genuine examples above and the scalar
calculation serve different logical roles and must remain separate.

## Reproduction and remaining action

- `tripartite_deficit_b24_k48.py`: minimal exact counter/fiber check of
  this one component in the two saved histories; no search procedure.
- `tripartite_deficit_b24_k48_exact.json`: every l's fiber-size
  distribution, N,d,delta,C_all,C_core,E, each selected record key,
  all exact loss terms/ratios and genuine priced terms, and source hashes.
- `tripartite_deficit_review_manifest.json`: claim, assumptions, scope,
  proof/evidence binding and next action.

The exact deficit identity is a valid additional mathematical tool.
The remaining task is an all-history cap-sensitive use of its actual
fiber deficits or width/gate losses that sums across the genuine shared
components and cuts. No such summability theorem is established by
these finite observations or by the scalar no-go. Neither the full
identity's Sidon instantiation nor this finite check is claimed Lean
verified, and the frozen uniform theorem and Q1 remain unresolved.
