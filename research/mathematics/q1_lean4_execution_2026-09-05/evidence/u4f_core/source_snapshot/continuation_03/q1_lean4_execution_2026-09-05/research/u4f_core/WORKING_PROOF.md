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

## A08. Weighted fiber injection: a real deficit, still a rank-sized mass

For one oriented collision from A07 let F be its realized c-fiber and
m=|F|. Put L=a_(i-1) and keep e_c=a_q-a_p=a_c-A. In addition to c-to-p
injectivity, c-to-q is injective: equal q would imply equal two-sums
a_c+a_p=A+a_q, and c>p fixes the Sidon orientation. Therefore

    sum_F e_c
      = sum_{p in image(F)} (L-a_p)
        - sum_{q in image(F)} (L-a_q).                    (A08.1)

The second sum must not be discarded as zero. Since q<c<=i-1, the m
distinct q values are all below i-1. Sidon interval packing implies
that their distances from L, in increasing order, are at least
binom(2,2),binom(3,2),...,binom(m+1,2). Thus

    sum_F e_c <= sum_{p in image(F)}(L-a_p)-binom(m+2,3).

The m distinct p values have distances from a_1 at least
binom(1,2),...,binom(m,2). A further valid consequence is

    sum_F e_c <= m H_(i-1)-binom(m+1,3)-binom(m+2,3)
              = m H_(i-1)-m(m+1)(2m+1)/6.                (A08.2)

Alternatively summing e_c=a_c-A over its distinct c gives

    sum_F e_c <= m(L-A)-binom(m+1,3).                    (A08.3)

These inequalities preserve the actual injective endpoint images. They
give cubic deficits, but do not establish sublinear dependence on m. If
one subsequently substitutes m=O(i), H_(i-1)=O_C(i^2 log i), the positive
term is still of cubic rank scale with a logarithm; no summable bound on
A07's common-tail increments follows from those substitutions.

The candidate sum_F e_c<=H_(i-1)*sqrt(j_minus) was tested exactly by
squaring on the already certified M=96 fibers. No counterexample occurs
among 905 greedy and 858 variant oriented fibers; maximum ratios are
approximately 0.4807 and 0.4722. These are finite absence results only.
A09 proves that such an estimate with any absolute prefactor cannot be
deduced without a fixed-cap hypothesis.

This subclass is small in the available full profiles: paired records
carry about 3.58% / 4.13% of total record mass and 3.43% / 3.94% of total
harmonic coverage mass. Removing them decreases N by about 1.66% / 1.91%.
These numerical fractions are not asymptotic claims. They motivate moving
the principal effort to the whole-profile representation in A10 instead
of treating this subclass as a closure of the frozen theorem.

## A09. Actual Sidon family refuting a cap-free square-root fiber estimate

This is a family of actual strict-core finite histories with unbounded
source-fiber multiplicity, but NOT a family with the same fixed cap C.
It rejects the cap-free shortcut; it does not refute U4-F or Q1.

Fix an integer m>=16. Choose independent parameters in these open rational
intervals (the fractions are exact):

    1<J<11/10, 3<T<31/10, 1<U<11/10, 20<I<201/10,
    2<P_j<21/10, 10<Q_j<101/10,
    15<Z_j<151/10, 203/10<Y_j<204/10    (1<=j<=m).

Use the point linear forms

    J; P_j; J+T+U; Q_j; C_j=J+T+Q_j-P_j;
    Z_j; I; Y_j; I+U; I+T.                              (A09.1)

All unordered two-sums, with repetitions allowed, are distinct formal
linear forms. Here is a direct check. Private-variable signatures of a
P_j, Q_j or C_j are respectively (1,0),(0,1),(-1,1) in (P_j,Q_j).
Sums of two points at different private indices identify their types.
At the same private index the only ambiguity with a single-point signature
is P_j+C_j, whose signature is that of Q_j, but its remaining fixed part
is J+T. A collision with Q_j plus a fixed point would require that missing
fixed point J+T; it is absent. The Z_j,Y_j variables also identify their
points. Finally, the five fixed forms J,J+T+U,I,I+U,I+T have fifteen
distinct two-sums, seen first by their J,I coefficients and then T,U.

Consequently every undesired two-sum equality is a proper rational
hyperplane. A finite union of proper hyperplanes cannot fill this open
box: successively choose coordinates avoiding the finitely many roots,
or use that the product of their nonzero linear polynomials cannot vanish
on an open box. Density of rationals supplies a rational point avoiding
all of them. This is a finite, non-circular existence argument. Scale by
a common denominator D, enlarged so D>=(3m+2)^2, and translate the smallest
point to 1. The result is a positive integer Sidon set.

The interval separation forces the ranks

    j_plus=1, j_minus=m+2,
    q_j in [m+3,2m+2], c_j in [2m+3,3m+2],
    i=4m+3, r_minus=5m+4, r_plus=5m+5=M.

For every j the same oriented repeated collision occurs with
older e_j=D(Q_j-P_j), t_minus=DU and t_plus=DT. Both core records have six
distinct endpoints. Since c>=35, log c>3; since r>=84, log r>4.
The older birth is >c/9, both coverage gaps i-c are at least m+1,
both top lags are at least m+1, and r<c log c. The physical output
condition follows from DU>D>=(3m+2)^2>c^2/(log c)^3, and DT>DU.
Every fixed strict core predicate is therefore satisfied.

There are m rows in this one fiber, e_j>7D and H_(i-1)<15D. Hence

    (sum_F e_c)/H_(i-1) > (7/15)m.

This exceeds K sqrt(j_minus)=K sqrt(m+2) for any fixed absolute K once
m is large. It also disproves any cap-independent constant multiplicity.
The construction is not fixed-cap: its second-point diameter satisfies
H_2>(9/10)D>=(9/10)(3m+2)^2, so a cap with onset 2 requires
C>H_2/(4 log4), which tends to infinity. No C or m0 is silently refitted
inside an asserted campaign or a purported counterexample to Q1.

Logical outcome: actual Sidonness and strict core alone cannot give this
sublinear fiber estimate. A fixed-cap proof would need to exploit the
early-rank constraints in an essential way. The generic family and its
scope were independently reviewed; no constructive bounded-cap search or
Lean verification of the existence construction is claimed.

## A10. Whole-core regrouping by four ordered old endpoints

Take p<q<s<c and define positive physical gaps

    A=a_q-a_p, B=a_s-a_q, C=a_c-a_s, H=A+B+C.

Here H is the span a_c-a_p of this quadruple, not a redefinition of the
global diameter H_c. Every component price still uses the frozen H_k.

All ways to divide these four points into two positive source labels are

| Matching | Labels | Product | Numeric output | Earlier source birth |
|---|---|---|---|---|
| 1 | {A,C} | AC | t_minus=|C-A| | q |
| 2 | {A+B,B+C} | AC+BH | t_minus | s |
| 3 | {B,H} | BH | t_plus=A+C | s |

Distinct positive differences give A!=C, so t_minus>0. Every six-distinct
core record has a unique old quadruple and one of these three matchings.
Conversely a matching produces a core record precisely when its numeric
output has unique actual endpoints c<i<r and the frozen strict conditions
hold. No source-pair representation is duplicated by sorting the old points.

For this quadruple let G_(sigma,z)(b) equal u_(r_sigma)^[M] when the actual
output t_sigma exists, its endpoints satisfy the frozen tests and
c<b<i_sigma, and the earlier-source test z>c/(log c)^2 holds; put it zero
otherwise. For sigma=- use z=q or s; for sigma=+ use z=s. Then exactly

    P_b^core(M,M) = sum_{p<q<s<c}
       [ AC G_(-,q)(b) + (AC+BH) G_(-,s)(b) + BH G_(+,s)(b) ]. (A10.1)

The two minus matchings share the actual output endpoints and price, but
their older-birth tests may differ. The plus output has its own actual
endpoints and price. In particular t_plus>t_minus is not a statement
about which output is born first. The formula addresses every original
core record, not only the small paired-orientation subclass of A07.

This expression preserves the one-copy coverage intervals when summed
over any dyadic cut block. A potential estimate must retain the gates and
both genuine output prices. Replacing them by freely chosen or common
prices, or deleting one output on grounds of its larger numeric value,
would require a new theorem. The next concrete test is simultaneous
realization and chronological ordering of the two outputs on actual
quadruples, followed by a bound on the BH-weighted joint output term.

The full classification was checked coefficientwise at every cut of both
certified M=96 histories. Simultaneous core outputs of both kinds occur
for 5,151 / 5,328 old quadruples. A small exact witness already belongs to
the independently certified M=15 prefix:

    (p,q,s,c)=(2,3,6,8), old values (2,4,21,45),
    A=2, B=17, C=24, H=43,
    t_minus=22, (i_minus,r_minus)=(14,15),
    t_plus=26, (i_plus,r_plus)=(11,12).

The matching products are 48,779,731. The minus records cover cuts 9..13;
the plus record covers cuts 9..10. Although 26>22, the true price is
u_12^[15]>u_15^[15]. Thus ordering the prices by numeric output size is
rigorously rejected. Both output records and prices must remain in A10.1.

## A11. A summable small-middle-gap class inside the unchanged core

Let P_b^smallB restrict the frozen core to old quadruples satisfying

    B=a_s-a_q <= c^2/(log c)^3.

This is an analytical partition for a proof, not a change to the frozen
record set, the localization parameters, or Gate 0's verification status.

At fixed latest birth c, every possible integer B has at most one actual
middle endpoint pair (q,s), by positive-difference uniqueness. There are
at most floor(c^2/(log c)^3) such B and fewer than c choices for p. Each
old quadruple has at most three source-pair matchings, and each of those
has at most one actual output. Therefore

    #small-B records with latest birth c <= 3c^3/(log c)^3.

Each record covering b has genuine weight u_r^[M]de<=alpha_r<=4/b^4.
Since four old endpoints require c>=4, for b>=4 this gives

    P_b^smallB <= (12/b^4) sum_{4<=c<b} c^3/(log c)^3
               <= 12/b^2 + 24/(log b)^3.                 (A11.1)

For completeness split at c=sqrt(b). In the low range log c>1 and
sum_{c<=sqrt(b)}c^3<=b^2. In the high range log c>(log b)/2 and
sum_{c<b}c^3<b^4/4. These give the two displayed terms. Consequently

    sum_{b>=4} sqrt(P_b^smallB)/b
      <= sqrt(12) sum_{b>=4} b^(-2)
        + sqrt(24) sum_{b>=4} 1/[b(log b)^(3/2)] < infinity. (A11.2)

This bound is independent of history, M,T,C and m0. It uses the same
records over their original intervals; no cut has been allocated a new
physical pair budget. The first three cuts are uniformly harmless.
This new subclass is not already removed by the original small-output
test: its B is a middle OLD difference, whereas the actual outputs in
A10 are |C-A| and A+C.

On the remaining records B>c^2/(log c)^3, let Q_b^BH denote exactly the
BH-weighted part of A10.1, with those same remaining quadruples and gates.
For c>=m0 the fixed cap gives

    AC/(BH) <= H/(4B)
       <= (C_cap/4) log(2c)(log c)^3.

The first inequality follows from 4AC<=(A+C)^2<=H^2. The q gate implies
the s gate for the minus output, so its two AC pieces total at most
2AC G_(-,s). On a covered cut c<b, summing proves

    P_b^(remaining,c>=m0)
       <= [1+(C_cap/2)log(2b)(log b)^3] Q_b^BH.          (A11.3)

Records with c<m0 have r<c log c<m0 log m0 in the core; their cuts are
therefore contained in one parameter-dependent finite interval. They
are handled by the original 1/8 pointwise bound without imposing a cap
at those earlier ranks. No history-dependent initial range is discarded.

The logarithmic factor in A11.3 is a limitation: it makes an upper bound
on the BH profile a stronger sufficient task, not an established closure.
Neither the BH part nor the remaining original core is proved uniformly
summable. The exact new whole-core target for an attack is the joint
BH term with BOTH realized output gates and their genuine prices; the
numeric ordering counterexample above forbids a monotone-price shortcut.

## A12. Uniform cost for a small gap anywhere in the old quadruple

A11 extends to the union of all three adjacent old gaps. Let S_b retain
exactly those original core records whose unique old quadruple obeys

    min(A,B,Cgap) <= c^2/(log c)^3.

The frozen definition is unchanged; this is a nonnegative subclass profile.
For every actual Sidon history and both horizons 2<=T<=M,

    S_b <= 1/(2b^2) + 48/(log b)^3,    b>=5;            (A12.1)
    S_b = 0,                          2<=b<=4.

Here is a global-prefix count that also handles the outer gap Cgap.
Split c at sqrt(b). For c<=sqrt(b), put n=floor(sqrt(b)); there are at
most 3 binom(n,4) records, because each old quadruple has three matchings
and each matching has one possible actual output over all future ranks.
Each record has genuine weight at most 4/b^4, so this part is at most
1/(2b^2). This bound includes all low-source quadruples, even without a
small-gap condition.

For c>sqrt(b), any small adjacent old gap has integer value at most
L_b=8b^2/(log b)^3. In the entire prefix of length b-1, positive-difference
uniqueness gives at most floor(L_b) endpoint pairs of such small length.
For each pair there are at most binom(b-3,2) ways to choose the other old
endpoints. This covers every required quadruple, sometimes repeatedly,
and allows at most three actual records per quadruple. Consequently

    S_b^high <= (4/b^4)*3*floor(L_b)*binom(b-3,2)
              <= 48/(log b)^3.

No extra factor for the position A, B or Cgap is needed: the one global
bank of small positive differences already counts all positions. Repeated
coverage of a quadruple in this union count is only an upper bound; it
does not create additional spendable record or cut capacity. A fixed-c
outer-gap count would retain two free old endpoints and is insufficient
for this argument; the whole-prefix count is essential.

The sum starts at b=5 because four old endpoints and c<b are required.
Square-root subadditivity and decreasing integral comparison from 4 give
the explicit absolute estimate

    sum_(b=2..T-1) sqrt(S_b)/b
      <= 1/(4 sqrt(2)) + 8 sqrt(3)/sqrt(log4).           (A12.2)

This subsumes the small-B class of A11, depends on neither cap parameters
nor history/horizons, and retains alpha_(M+1) throughout. The proof was
independently reviewed in SMALL_OLD_GAP_UNION_REVIEW.md. No new finite
enumeration or Lean verification of A12 is claimed.

## Current mathematical frontier

A10 is now the exact whole-core representation. A12 pays the union of the
three small adjacent old-gap subclasses at an absolute finite square-root
cost. The remaining quadruples have ALL three old gaps >c^2/(log c)^3.
Their BH/AC
profile is still unbounded by any proved uniform constant. The comparison
to BH alone in A11.3 incurs approximately log^2(b) after square roots; a
plain unweighted BH norm bound would not close that particular comparison.
No new sufficient criterion replaces the frozen theorem. A11's comparison
remains valid after restricting to these same remaining quadruples.

A08 supplies an exact weighted-fiber deficit, but A09 rules out a
cap-independent square-root bound, and finite paired-subclass fractions
show why the main effort moved to the whole profile. The next attack is
a joint estimate of the actual BH-weighted two-output term, retaining
the independent chronological locations and the original shared component
measure. Either control the AC term directly or account for A11.3's
logarithmic factor. Neither missing outputs nor price ordering can be
replaced by a convenient assumption.

The frozen existential K bound and the original Q1 remain unproved.
No finite profile or cap-free counterfamily refutes them. The final
literal Q1 proof and its clean Lean dependency closure remain absent.

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
Continuation 02 added the weighted-fiber identity, old-quadruple matching
algebra, and the strict ordering of their numeric outputs; its accepted
compiler/type/axiom evidence is `LEAN_VERIFICATION_02.json` and the `c02`
logs. The generic Sidon existence family and the full A11/A12 summability
argument remain hand proofs, independently reviewed but not Lean-verified.

Read this file and `ATTEMPTS.jsonl` at restart; use the source manifest only
to locate unchanged originals. Reuse the already certified finite campaign
when testing a concrete new inequality. Do not repeat Gate 0, the old
declaration inventories, the C143 campaign, or environment design.
