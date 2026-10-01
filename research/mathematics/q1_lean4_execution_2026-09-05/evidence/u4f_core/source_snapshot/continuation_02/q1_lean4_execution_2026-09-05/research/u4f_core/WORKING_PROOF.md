# U4-F proof and counterexample search

Date: 2026-09-09. Status: **Q1191-U4F-CORE-UNIFORM-01 NEEDS-PROOF; Q1 unresolved.**
The root `research/NEXT_THEOREM_CONTRACT.md`, section 6, is the unchanged
statement. Gate 0 is MATH-REVIEWED, not Lean-verified. Source copies and hashes
are in `../../evidence/u4f_core/SOURCE_MANIFEST.json`.
The initial goal read returned null, but the later read in this same turn
returned the existing original-Q1 master goal as ACTIVE. Both observations
are saved in RUNTIME.json. This turn created, cleared or completed no goal.
Session metadata identifies gpt-6-astra/ultra.

## A01. Exact horizon reduction and one-record coverage

Fix one finite actual Sidon history and its component horizon M. Write
v_h = u_r^[M] d e, with u_r^[M] = sum_{k=r}^M kappa_k/H_k^2.
All these numbers are nonnegative: H_k>0 and alpha_k>alpha_{k+1}>0.
No terminal alpha is reset. Increasing T to T' only admits records whose
upper output was previously beyond T. The endpoints, strict core predicates,
and v_h of every old record remain unchanged. Thus

    R_core(M,T) subset R_core(M,T'),
    P_b(M,T) <= P_b(M,T')                 (2 <= b < T <= T' <= M).

The square root is increasing. Sum over the old cuts, then add the
nonnegative new cuts, obtaining N(M,T)<=N(M,T')<=N(M,M). Consequently the
uniform theorem is equivalent to its restriction T=M, with exactly the same
K, C, m0 and finite histories.

This does not replace the downstream double limit: for a fixed infinite
history first FIX T, then let M tend to infinity. The record set through T
is finite and stable and u_r^[M] increases to u_r. Along a fixed extension,
N(M,M) also increases; that assertion compares extensions of the same
history only.

For j>=1 set B_j={b:2^j<=b<min(2^(j+1),M)}. Exact finite interchange gives

    I_j = sum_{b in B_j} P_b/b
        = sum_{h in R_core(M,M)} v_h ell_j(c,i),
    ell_j(c,i) = sum_{b in B_j, c<b<i} 1/b.

In particular a record contributes once at each b=c+1,...,i-1, and its
single total coverage is sum_j ell_j = sum_{b=c+1}^{i-1}1/b <= log(i/c).
This follows from 1/b<=integral_{b-1}^b dx/x; empty intervals cause no issue.
It is not a separate physical allowance in each block.

With W_j=sum_{b in B_j}1/b and Q_j=sum_{b in B_j}sqrt(P_b)/b,
weighted Cauchy gives Q_j<=sqrt(W_j I_j). If L=2^j and the block is nonempty,

    W_j <= 1/L + integral_L^(2L) dx/x = 2^(-j)+log 2.

For an empty block W_j=I_j=Q_j=0. The last cut remains M-1. Therefore
N=sum_j Q_j<=sum_j sqrt((log 2+2^(-j))I_j). This is a sufficient estimate,
not a second frozen theorem. Bounded sum I_j alone does not control this
last sum (the scalar example I_j=1/j^2 shows the precise logical failure).

Scope: direct finite mathematical proof, independent of the cap; generic
finite-sum formalization is recorded separately when checked. This elementary
reduction by itself is not an advance on the missing uniform estimate.

## A02. A Sidon dispersion bound for the actual profile

This attack retains the real output differences while estimating their
correlations individually. It gives a new explicit cap-sensitive upper
bound, but its limiting scale does not close U4-F.

Fix a cut b, put n=b-1, D=F_n, H=H_n, and S=sum_{d in D}d^2. For a positive
integer t let E_t={{e,e+t}:e,e+t in D}, and let

    K_D(t)=sum_{e:e,e+t in D} e(e+t).

Every vertex in this graph has degree at most two. Hence

    2 K_D(t) <= sum_{edges {d,e}} (d^2+e^2) <= 2 S.       (A02.1)

The actual records with output t form a subset of these edges. Sidon
uniqueness identifies the one actual output (i,r); it DOES NOT make the
edge unique. At a fixed r there are at most r-b-1 eligible i>b. Thus, using
the genuine price only by a valid upper inequality,

    P_b^core(M,M) <= S sum_{r=b+2}^M (r-b-1)u_r^[M]
                  <= (S/H^2) sum_{r=b+2}^infty (r-b-1)alpha_r
                  <= S/(6 b^2 H^2).                      (A02.2)

Here u_r^[M]<=alpha_r/H^2, without altering u_M^[M]. To verify the last
constant, for r>=2,

    alpha_r <= ((r-1)^(-3)-r^(-3))/3,

because the difference of the right side and alpha_r equals
1/[3 r^3(r-1)^3]. Summing against r-b-1 gives
(1/3)sum_{k=b+1}^infty k^(-3)<=1/(6b^2). This is an upper bound by an
infinite numerical series, not an assumption of an infinite capped extension.

Now translate x_j=a_j-a_1, j=1,...,n, so x_1=0, x_n=H. Positive difference
uniqueness gives the exact identity

    S = n sum_j x_j^2 - (sum_j x_j)^2
      = n^2 H^2/4 - n sum_j x_j(H-x_j)
        - (sum_j x_j-nH/2)^2.                            (A02.3)

Thus S<=n^2H^2/4 and already P_b<1/24 for b>=3. The Sidon property gives
a quantitative loss from the extreme two-cluster variance. The j(j-1)/2
positive differences among the first j points are distinct integers in
[1,x_j], and the analogous assertion holds in the suffix. Therefore

    x_j >= j(j-1)/2,   H-x_j >= (n-j)(n-j+1)/2.

Consequently, if J_n=sum_{j=1}^n min(j(j-1)/2,(n-j)(n-j+1)/2), then

    sum_j x_j(H-x_j) >= (H/2) J_n,
    J_(2m)   = (m^3-m)/3,
    J_(2m+1) = m(m+1)(2m+1)/6,
    J_n >= n(n^2-4)/24.

The product inequality uses max(x,H-x)>=H/2; the formulas follow by summing
j(j-1)/2 on each half. Insert these inequalities into (A02.3). For n>=3,

    S/H^2 <= (n^2/4)[1-(n^2-4)/(12H)],
    P_b^core(M,M)
      <= n^2/(24b^2) [1-(n^2-4)/(12H_n)].                (A02.4)

If ALSO n>=m0, the unchanged cap H_n<=C n^2 log(2n) yields

    P_b^core(M,M)
      <= n^2/(24b^2) [1-(1-4/n^2)/(12 C log(2n))].       (A02.5)

No cap is imposed below m0. For those finitely many cuts use (A02.2) or the
original 1/8 bound. The bracket is nonnegative on an actual admissible
history: H_n>=n(n-1)/2 from Sidon packing already guarantees this for n>=3.

**Failure location.** For fixed C the right side of (A02.5) tends to 1/24,
not zero. On full dyadic blocks the resulting upper majorant for I_j tends
to (log 2)/24. Summing its square roots therefore has a positive constant
cost per block. This precise majorant fails to prove uniform N; it does not
prove that the actual profiles fail to decay. Information lost in (A02.1)
is the joint dependence of K_D(t) over different actual future outputs;
(A02.2) then also forgets which outputs belong to the strict core. There is
no circular use of Q1, infinite capped histories, or maximum prefix lengths.

Logical role: valid pointwise upper bound with a cap-sensitive improvement;
neither a proof nor a counterexample to U4-F. Next distinct attack: retain
the exact graph boundary deficit jointly over actual outputs instead of
replacing every K_D(t) by its separate maximal norm.

## A03. Rejected single-sign incidence saving

Candidate: for fixed (c,e,i), where e is the older positive label, at most
one eligible strict six-endpoint record has a new source a_c-a_j.
Even fixing r as well does not make this true.

The finite worker found an actual fixed-cap greedy prefix with

    c=10, e=58=a_9-a_4, i=14, r=15, t=a_15-a_14=22,
    d_minus=36=a_10-a_8, d_plus=80=a_10-a_1.

Both |d_minus-e|=|d_plus-e|=22. Each record separately has six distinct
endpoints, and both satisfy every strict core condition, with s=9. The
existing factor 2 for the two sign cases cannot be replaced by 1. The
full prefix, rational log enclosures, price and independent check are
saved under `../../evidence/u4f_core/finite_campaign/`.

In contrast the older fixed-(c,r) incidence count 3 binom(c-1,2) can be
reduced to 2 binom(c-1,2) WHEN eligibility i>c is retained. In the d<e
case the Sidon unordered pair is the pair (source lower endpoint j,
output lower endpoint i). Its orientation is forced by j<c<i, leaving
one assignment. The d>e case has one ordered difference assignment.
This is a scoped improvement, not a new summability estimate; the example
above shows that the remaining factor 2 is necessary even at fixed e,i,r.

## A04. Exact output graph deficit, with its unsummed obstruction

Retain a cut b and D=F_(b-1). For each actual future output t=a_r-a_i,
b<i<r<=M, take ONLY its strict-core edges covering b. Let E_t be this
edge set, m_t its cardinality, and deg_t(d) its vertex degrees. Since a
numeric positive label has at most neighbors d-t,d+t, deg_t(d)<=2.
Put

    B_t = (1/2) sum_{d in D} (2-deg_t(d)) d^2 >= 0,
    G_t = (t^2/2) m_t >= 0.

For every such actual output, including outputs with no core edges,

    K_t^core + B_t + G_t = S,                             (A04.1)

because d^2+e^2-2de=(d-e)^2=t^2 on each edge. Thus the exact common-price
identity is

    P_b + sum_{b<i<r<=M} u_r^[M] B_(a_r-a_i)
        + sum_{b<i<r<=M} u_r^[M] G_(a_r-a_i)
      = S sum_{r=b+2}^M (r-b-1) u_r^[M].                 (A04.2)

The large nonnegative boundary term is retained. This is an identity on
the same graph for every actual output, not a budget obtained by making
independent copies of a source record. Its precise limitation is that
nonnegativity alone gives A02 again; a useful upper bound on P_b requires
a quantitative LOWER bound on the sum of both deficits, sufficiently
close to the entire right side. No such aggregate cancellation is assumed.

There is a further valid explicit bound from the strict core and cap.
For a covered record, r<c log c and b<r imply c>b/log b, hence

    t>c^2/(log c)^3 > b^2/(log b)^5 =: L_b.

On each edge de<=H^2, so G_t>=t^2 K_t/(2H^2). Therefore, for b-1>=m0,

    P_b <= S A_b/(1+rho_b),
    A_b=sum_{r=b+2}^M(r-b-1)u_r^[M],
    rho_b=1/[2 C^2 (log b)^10 (log(2b))^2].              (A04.3)

For an output with no core edges the inequality still holds with K_t=0.
Use H<=C b^2 log(2b) to obtain rho_b. This preserves every strict core
condition; it only relaxes them in an upper estimate. Since rho_b tends
to zero, applying this pointwise saving to A02 still leaves the same
positive limiting constant. The gradient term alone therefore does not
close the required dyadic sum.

Exact rational evaluation of (A04.2) at b=8,16,32,64 on both certified
M=96 histories is saved in `../../evidence/u4f_core/graph_defect_checks.json`.
All eight identities pass. The boundary term accounts for about 0.868--0.882
of the right side, the gradient for about 0.028--0.059, and the actual
profile for about 0.062--0.092 in these finite samples. Ratios are decimal
presentations; they are not asserted universal or asymptotic constants.

## A05. Listed scalar clock bounds cannot provide the missing sum

A hand countermodel shows why combining the scalar inequalities used in
A02 cannot, by itself, close the estimate. This is explicitly a relaxation,
NOT an actual Sidon construction and NOT a counterexample to U4-F.

For each dyadic N>=64 use c in [N,9N/8), i in [5N/4,11N/8),
r in [3N/2,13N/8), and one abstract record for each additional integer
l in [0,N/16). Give it s=3N/4+l, d=3N^2/4, e=N^2/4, t=N^2/2.
Use the single scalar diameter sequence H_k=k^2 (k>=2) and its genuine
partial prices through the same global M. Every artificial record has
one coverage interval c<b<i.

These records satisfy all strict scalar core tests, the C=1,m0=2 scalar
cap at every rank, t<=H_c and top-gap packing, and the bounds

    count(c)<=c^3/2,
    count(c,s)<=(c-1)(s-1),
    count(c,i),count(c,r)<=2 binom(c-1,2),
    count(i,r)<=binom(i-1,2).

There are N^4/8192 records at a scale. For M>=2N, summing only components
13N/8<=k<=2N gives u_r^[M]>=3/(1024N^8). Thus every cut
9N/8<=b<5N/4 has P_b>=9/2^27. Its harmonic cut weight is at least 1/10.
Taking L dyadic scales under M=2^(J+1) proves

    N_abstract(M,M)>=3 L/(81920 sqrt(2)).

The full proof and independently checked constants are in
`../../evidence/u4f_core/finite_campaign/SCALAR_CLOCK_RELAXATION_NO_GO.md`.
The missing assumptions are explicit: the numbers d,e are reused under
different artificial identifiers; they do not have unique actual endpoints,
the pairs do not have unique actual outputs, and fixed-(c,e,i,sign)
uniqueness and the numeric degree-two graph do not hold. It would be
incorrect to call this an actual capped history or to assert that every
possible scalar refinement has failed. It rejects exactly an inference
from the listed inequalities. The earlier-birth count was retained by
spreading s across l; concentrating it at one s would invalidate that count.

Next action: retain integer endpoint equations and the actual label graph.
Improving only constants in these particular marginal bounds is insufficient.

## A06. A two-orientation price cancellation changes sign with M

After A03 rules out single-sign uniqueness, a distinct possibility is to
combine both orientations into the old-label square. If both outputs have
the same t and price, e(e+t)+e(e-t)=2e^2 is exact. They need not have the
same upper output. Generally the residual is

    D_M = (v_plus+v_minus)-e^2(u_(r_plus)^[M]+u_(r_minus)^[M])
        = e(t_plus u_(r_plus)^[M]-t_minus u_(r_minus)^[M]). (A06.1)

The candidate D_M<=0 is false even for the fixed cap C=1,m0=2. In the
greedy prefix use c=17,e=107=a_15-a_11,i=22. The two core records are

    new d_minus=38=a_17-a_16, r_minus=23, t_minus=69,
    new d_plus=289=a_17-a_1,  r_plus=24, t_plus=182.

Keep OUTPUT horizon T=24 fixed. For component M=24 and M=25 respectively,
the diameters relevant here are H_23=661,H_24=774,H_25=821. In both cases

    D_M=107[113 u_24^[M]-69 kappa_23/H_23^2].

With the genuine partial price this yields the exact values

    D_24 = -184597358827/502628531391268920000 < 0,
    D_25 = 200502708371698175071/28627944104873943851933340000 > 0.

The records and their strict core membership through T=24 are unchanged.
The common additional component price changes their residual by

    D_(M+1)-D_M = e(t_plus-t_minus) kappa_(M+1)/H_(M+1)^2 > 0

for M>=24. Thus even a negative residual observed at M=T cannot be
passed to the fixed-T, M-to-infinity limit. This is an exact refutation
of an intermediate compensation inequality, not U4-F or Q1. Independent
finite witness verification is recorded in the campaign directory.

Next mathematical action after this failure: keep the positive residual
in (A06.1). If pairing is used, charge its actual common-tail increments
jointly over the real source fibers; monotonicity of u_r alone gives the
wrong inference for the product t u_r.

## A07. Paired orientations induce a repeated collision, with genuine multiplicity

There is additional actual additive structure after the failure in A06.
Write the new source endpoints as d_plus=a_c-a_(j_plus) and
d_minus=a_c-a_(j_minus). Eliminating c and the older e from the two
orientation equations gives

    a_(j_minus)+2a_i = a_(j_plus)+a_(r_plus)+a_(r_minus),  (A07.1)
    a_(j_minus)-a_(j_plus) = t_plus+t_minus > 0.

Thus j_plus<j_minus<c<i and the pair of six-endpoint core records induces
a repeated-triple collision. This does not make either original record a
member of the repeated-endpoint class deleted by Gate 0.

One cannot pay an arbitrary number of these paired rows as one copy of
that repeated collision. Already the independently checked M=25,T=24
prefix has the same identity

    a_16+2a_22 = a_1+a_24+a_23 = 1438

for BOTH (c,e)=(17,107) and (18,178). For c=18, e=a_14-a_3,
d_plus=a_18-a_1=360 and d_minus=a_18-a_16=109. Both rows have positive
residual. At one fixed oriented collision,

    D_(c,M)=e_c [t_plus u_(r_plus)^[M]-t_minus u_(r_minus)^[M]],

so the bracket is independent of c; multiple positive contributions add.
The M=96 records have further actual multiplicity examples, saved in the
finite worker's repeated-collision note. A finite multiplicity never
disproves a yet-unspecified constant upper bound.

There IS a useful exact injectivity refinement. Put
A=a_(j_plus)+t_plus=a_(j_minus)-t_minus, so e_c=a_c-A. If e_c=a_v-a_p
with p<v<c, then a_c-a_v=A-a_p>0. Sidon difference injectivity makes
p determine (c,v); also a_p<A<a_(j_minus). The six-endpoint conditions
exclude p=j_plus. Thus the number of c values for a fixed oriented
collision is at most

    min(i-j_minus-1, j_minus-2).

This is a rank-dependent bound, not constant multiplicity.

A direct non-circular bound can now be derived for the positive COMMON
TAIL INCREMENTS, without improperly pricing an earlier output by u_R.
Restrict to r_plus>r_minus, and let R=r_plus. At fixed j_minus<i<R,
equation (A07.1) fixes the unordered pair {j_plus,r_minus} by Sidonness;
its orientation is fixed by j_plus<i<r_minus. Ignoring the additional
p-injection, c has at most i-j_minus-1 choices. Hence

    #paired rows with r_plus>r_minus and r_plus=R
      <= sum_{j_minus<i<R}(i-j_minus-1) = binom(R-1,3).

At a new component k, the already-present rows have R<k. Every such
positive tail increment is e(t_plus-t_minus) kappa_k/H_k^2 and satisfies
e(t_plus-t_minus)<=H_k^2. It follows that

    J_k := (kappa_k/H_k^2)
           sum_{old paired rows, r_plus>r_minus} e(a_(r_plus)-a_(r_minus))
         <= kappa_k binom(k,4)
          = (k-2)(k-3)/[6(k-1)(k+1)^2]   (k>=4).          (A07.2)

The sharper count binom(k-1,4) is available because R<k; the displayed
weaker form makes the exact asymptotic loss transparent. Its right side
is asymptotic to 1/(6k), and its series diverges. Thus the repeated
collision count plus this valid weight estimate still fails to prove a
finite tail budget. This is a failure of the explicit majorant, not a
lower bound on the actual J_k. The initial residual when a pair first
appears, and all unpaired records, also remain to be controlled.

Next specific action: use the injective map c to p BEFORE summing the
weights e_c over a fixed repeated collision. Seek an aggregate bound on
sum_c (a_c-A), jointly across the real collisions, retaining the integer
equations a_c+a_p=A+a_v and the common component measure. Merely dropping
c multiplicity, or transferring the existing repeated-class bound to
these paired six-endpoint records, is invalid.

## Current mathematical frontier

The horizon/coverage identities are exact. A02 gives a valid new bound;
A03 rigorously rules out one stronger incidence bound. The dyadic decay
estimate with an unspecified A(C,m0), and the frozen existential K bound,
remain unproved. A finite increasing sample or an increasing sequence of
observed I_j does not refute either statement. The final literal Q1 proof
and its clean Lean dependency closure remain absent.

## Formal verification scope and restart

`../../lean/Q1/U4FProfile.lean` contains verified generic finite-record
nonnegativity, monotonicity, exact coverage, weighted Cauchy, finite variance
algebra, the edge identity, the alpha coefficient inequality, and the
orientation tail increment/sign-flip arithmetic. The dedicated compiler
and theorem-type/axiom logs are under `../../evidence/u4f_core/`.
These are supporting lemmas. The full strict-core enumeration, A02's
Sidon dispersion/counting proof, A04's actual-graph instantiation, and A07's
counting theorem are not claimed Lean-verified. No literal Q1 theorem,
final release clean build, or final Q1 dependency closure exists.

Read this file and `ATTEMPTS.jsonl` at restart; use the source manifest only
to locate unchanged originals. Reuse the already certified finite campaign
when testing a concrete new inequality. Do not repeat Gate 0, the old
declaration inventories, the C143 campaign, or environment design.
