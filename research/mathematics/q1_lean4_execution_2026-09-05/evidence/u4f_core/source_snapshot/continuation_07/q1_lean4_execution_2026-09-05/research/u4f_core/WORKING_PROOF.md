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

## A13. An actual cap-free infinite Sidon history with divergent BH norm

Status: hand proof independently reviewed; not Lean verified.
This attacks the cap-free candidate that the exact BH part alone has a
uniform square-root harmonic norm. It is NOT a counterexample to the
frozen fixed-(C,m0) theorem. The construction expressly violates every
eventual fixed cap, and retains every genuine component price.

### A13.1. A dense quadratic block and a weighted raw lower bound

For an odd prime p put x_j=2pj+(j^2 mod p), 0<=j<p. These form an
increasing integer Sidon block: equal positive differences force equal
index differences (residue corrections differ by less than 2p), and
reduction modulo p then forces equal starting indices. Also

    x_j-x_i >= p(j-i),  H_block < 2p^2.

This is the actual quadratic family of the unchanged commutator source,
section 5. Here we choose separated old/future rank intervals to leave
room for genuine terminal components. Put n=floor(p/3), and use old
indices 0,...,n-1. Use future indices f=ceil(p/2),...,g=floor(3p/4),
of number m. For sufficiently large p, n>=p/4 and m>=p/8.
Let D be the positive difference bank of the old block, with
U=sum_(d in D)d and S=sum_(d in D)d^2. Then

    U >= p*n*(n^2-1)/6 >= p*n^3/8 >= p^4/512,
    mU >= p^5/4096,    mS <= 2p^7.

Consider the integer weighted shadow at sites x_i+d, i in the future
interval and d in D. Its mass is mU and its support has fewer than
4p^2 sites. Cauchy and the exact old/future autocorrelation identity give

    mS + 2 sum_(t in Delta(future)) K_D^+(t)
      >= (mU)^2/(4p^2) >= p^8/2^26.

Each positive future difference occurs once; each source pair in K is
unordered and occurs once. Consequently, for p>=2^28,

    sum_(t in Delta(future)) K_D^+(t) >= p^8/2^28.       (A13.1)

This is one actual old/future block, with no independent output budgets.

### A13.2. Sidon concatenation with a genuine finite-horizon price

Suppose an already constructed finite positive integer Sidon prefix has
N points and maximum V. Choose p>=16(N+1), and append the p new points

    Q(1+x_j),    0<=j<p,

where Q is an integer >2V. The union remains Sidon. Differences inside
the new block are positive multiples of Q; old differences are <Q.
Cross differences exceed V and have residue -a_old modulo Q, which is
nonzero. Equality between two cross differences first forces the old
endpoint to be the same (distinct old points lie strictly between 0 and
Q), then the new endpoint. This covers every possible equality of
positive differences; no previous point is moved or scaled.

Set M=N+p and retain the full genuine definition of u_r^[M]. An output
from the chosen future interval has actual rank r<=13p/16. Put
ell=ceil(7p/8); then r<=ell<=15p/16<=p<=M. All global diameters through
M satisfy H_k<3Qp^2. Therefore

    u_r^[M]
      >= (alpha_ell-alpha_(p+1))/(9Q^2p^4)
      >= 1/(36Q^2p^8),                                (A13.2)

because alpha_ell>=ell^-4, alpha_(p+1)<=p^-4, and
(16/15)^4-1>1/4. The component sum is exactly k=ell,...,p; neither
alpha_(M+1) nor any component boundary is reset.

Each original d,e is scaled by Q. Equations A13.1 and A13.2 imply
that the eligible profile contributed by this one block is at least

    eta = 1/(36*2^28)

at EVERY cut in the actual interval

    N+n+1 <= b <= N+f.                                (A13.3)

The interval lies below all chosen lower output endpoints and above all
chosen source endpoints. Its harmonic length is at least 1/4: it has
f-n>=p/6 cuts and largest cut <=9p/16.

### A13.3. Retaining strict core and a fixed fraction of every old gap

The six excluded-class estimates of the fixed Gate 0 source bound the
NON-core part of any eligible profile by a universal function F(b)->0,
independently of cap, history and both horizons. Only those already
proved bounds are used here, not a putative core estimate. Select an
absolute p0 so b>=p/4, p>=p0 implies F(b)<=eta/4. This is an elementary
limit threshold of those displayed bounds, not a maximum-prefix or Q1
assumption. Finite genuine prices satisfy the same upper comparisons
used in those bounds.

Next choose epsilon=eta/384. Remove the block quadruples whose minimum
adjacent unscaled old gap is <=epsilon p^2. Positive-difference
uniqueness in THIS unscaled block gives at most floor(epsilon p^2)
small endpoint pairs. Each admits at most p^2/2 pairs of remaining
endpoints and at most three matching records. Every chosen future output
has r>=p/2, hence genuine record weight <=alpha_r<=64/p^4.
Thus the total removed profile at each cut is at most

    (3 epsilon p^4/2)*(64/p^4) = 96 epsilon = eta/4.

The remaining strict-core subprofile from this block is at least eta/2,
and each of its old gaps A,B,Cgap is >epsilon Q p^2.
Choose Q additionally with epsilon Q>=1. Since c<=N+n<p/2 and c>=4,
these gaps exceed c^2/(log c)^3. Thus they belong to the still-unpaid
all-large-old-gap subclass of A12, not its finite-cost complement.

For a retained quadruple Hquad<2Qp^2 and B>epsilon Qp^2. Therefore
ACgap/(BHquad)<1/(2epsilon). Keep only the chosen actual future
endpoints when defining its G gates. The implication G_minus,q<=
G_minus,s is preserved. Its full contribution is at most

    (1+1/epsilon) * BHquad*(G_minus,s+G_plus,s).

All matchings with a chosen output remain eligible in this comparison;
both minus matchings share that output and differ only by older-birth
gates. Missing plus outputs are not invented. Summing shows that the
exact full-core BH profile, restricted even to the all-large-old-gap
class, satisfies at every cut in A13.3

    Q_BH(b) >= (eta/2)*epsilon/(1+epsilon)
             >= delta := eta*epsilon/4 > 0.            (A13.4)

### A13.4. Infinitely many actual blocks, same prices, and scope

Begin with the one-point history {1}. Recursively choose any odd prime
p>=max(p0,2^28,16(N+1)), and an integer

    Q>2V,    Q>=1/epsilon,    Q>=(N+1)^4.

The verified concatenation gives an infinite positive integer Sidon
history. A13.3's cut intervals for distinct blocks are disjoint. When
a finite prefix is extended, every existing core record remains present
and its genuine price only increases by positive components. The old
lower bounds therefore persist at later terminal horizons. At the end
M_L of L blocks,

    N(Q_BH^large; M_L,M_L) >= (L/4)*sqrt(delta) -> infinity. (A13.5)

This proves a multiscale failure on one actual history of any cap-free
uniform bound for the BH term, and therefore for the full core profile.
It is stronger than the earlier one-block raw upper-scale obstruction:
strict core, all large adjacent old gaps, shared genuine prices, and
arbitrarily many disjoint cut intervals all survive.

It is expressly outside the frozen theorem. At the first point of each
new block, k=N+1, H_k=Q-1>=(k^4-1), so

    H_k/[k^2 log(2k)] -> infinity

along those infinitely many ranks. No fixed C,m0 works. In fact the
count at x=Q-1 equals N and is sparse enough to have the original Q1
expression tend to zero along these x. The result must not be promoted
to a fixed-cap counterfamily, a negation of Q1, or a completed master goal.

No large numerical evaluation of the quadratic blocks was performed.
The proof is symbolic, uses the already verified original Sidon input,
and has passed independent mathematical review; it is not Lean verified.

## A14. Exact fixed-cap counterexamples to aggregate AC<=BH

The candidate that Q_AC(b)<=Q_BH(b), or its dyadic aggregate
I_AC<=I_BH, would have removed A11's logarithmic comparison loss.
Both are now rigorously rejected on actual finite capped histories.

The initially checked all-large-old-gap profiles of both existing M96
histories satisfied every cut comparison. The cut candidate nevertheless
fails in an earlier existing variant prefix: M=T=12,b=10,

    Q_AC-Q_BH = 40/309372921 > 0.

The dyadic comparison passed the 900 actual block/horizon comparisons
of both existing histories, M=T=2,...,96. This was finite absence of a
counterexample only, and was not used as a theorem.

A separate targeted campaign fixed C=1000000,m0=2,M=T=12 BEFORE any
padding trial. Its first deterministic trial produced

    (1,14512,30001,30629,31694,32001,
     63361,67001,71675,84375,100001,105001).

The original evaluator and independent simple checker certify all 66
positive differences unique, the cap at every required intermediate
rank, and exactly two strict core records, with UNKNOWN=0. The one old
quadruple has ranks (1,3,6,8), physical gaps (30000,2000,35000), and
all three old gaps are strictly above 8^2/(log8)^3. Its two minus
matchings share the actual output (i,r)=(11,12), value 5000. The plus
output is absent. The genuine price, including alpha_13, is

    u_12^[12] = 1/676350675000000.

The original records cover precisely cuts 9 and 10. At each such cut,

    Q_AC = 4/1288287,
    Q_BH = 134/676350675,
    Q_AC/Q_BH = 1050/67 > 15,
    Q_AC-Q_BH = 1966/676350675 > 0.

The actual j=3 cut block is 8<=b<12, not an untruncated block. Hence

    I_AC-I_BH = 18677/30435780375 > 0.

The actual square-root harmonic contributions of that block are about
0.000371993006329 (AC), 0.0000939674684475 (BH), and
0.000383677836060 (full). These three displays are approximations;
rational enclosures computed using integer square roots are saved.

The forced six-distinct triple collision is exactly

    a_1+a_8+a_11 = a_3+a_6+a_12 = 167003.

The anchor construction concentrated the two minus matchings while
leaving the plus output unrealized. This is the information discarded
by the proposed aggregate domination. It is not a numerical price-order
mistake or a violation inferred merely from a single summand.

The fixed-C campaign rejects the constant-one cut and dyadic inequalities,
and even constants below 1050/67 for these components. It does NOT
reject a different parameter-dependent comparison, existence of K(C,m0),
any fixed-cap infinite-prefix assertion, or original Q1. No C or m0 was
changed during the one-trial campaign. Detailed certified evidence is in
finite_campaign/C1000000_m02_M12_target/.

## A15. A cap-sensitive first-moment bound for the AC part

Status: all-history hand proof independently reviewed. The finite integer
first-moment lemma is additionally verified in the pinned Lean module;
the complete Sidon/core instantiation remains a hand proof.
The pointwise or blockwise comparison AC<=BH is not assumed. Write
P=Q_AC(b), Q=Q_BH(b) for the exact A10 parts at one cut b>=5. They may
both be restricted to the same collection of old quadruples, including
the all-large-old-gap class; retain both minus older-birth gates and the
actual plus gate. No individual matching can be removed arbitrarily
without checking the G_minus,q<=G_minus,s implication used below.

For each positive integer middle difference B, let mu_B be the sum of
ACgap*(G_minus,q+G_minus,s) over its quadruples. Sidon uniqueness gives
at most ONE middle endpoint pair (q,s) with that B. At the covered cut
c<b, its remaining endpoints have at most

    (q-1)(b-1-s) <= (b-3)^2/4 <= b^2/4

possibilities. For each quadruple ACgap<=Hquad^2/4, and all contributing
components have H_k>=Hquad. Each AC term is therefore at most alpha_r/4.
Coverage gives integer r>=b+2, so alpha_r<=b^-4. The two minus terms
per quadruple give the uniform physical-difference mass capacity

    0<=mu_B<=D_b:=1/(8b^2),    sum_B mu_B=P.             (A15.1)

This is a cap on mass at each distinct INTEGER old difference B, not a
new assumption on the original profile or an independently renewed cut
budget. Every quadruple is placed in its unique middle difference fiber.

Let L=sum_B B*mu_B. Expanding the square and bounding the smaller-index
mass by its available integer positions gives

    P^2 = sum_B mu_B^2 + 2 sum_(A<B) mu_A mu_B
        <= D_b sum_B mu_B + 2D_b sum_B (B-1)mu_B
        = D_b(2L-P).                                  (A15.2)

Indeed mu_B^2<=D_b mu_B and sum_(A<B)mu_A<=(B-1)D_b;
missing integer values carry zero mass. Finite support suffices. No
integral theorem, ordering of positive output values, or independence
between fibers is used.

For an old quadruple write Hquad=A+B+Cgap. Its AC mass mu_h obeys
mu_h<=2ACgap G_minus,s, while its BH mass nu_h is at least
BHquad G_minus,s. Since 4ACgap<=Hquad^2 and Hquad<=H_b,

    H_b nu_h >= 2B mu_h.

Thus H_b Q>=2L. Combining with A15.2 proves the new exact inequality

    8b^2 Q_AC(b)^2 + Q_AC(b) <= H_b Q_BH(b).             (A15.3)

It holds on every actual history, at both horizons, with original
strict-core gates and genuine prices. The left linear term also records
the integrality B>=1. The cap is now inserted ONLY at the actual cut
rank b>=m0, yielding

    Q_AC(b)^2 <= (Ccap/8) log(2b) Q_BH(b).              (A15.4)

No cap at an earlier birth c<m0 is needed for A15.4. Cuts below m0 form
one parameter-dependent finite range paid by the original pointwise
bound. This respects every intermediate-rank cap and does not replace
H_b by a local quadruple span in the genuine prices.

### Exact dyadic consequence and what it does not prove

On the actual cut block J_j={b:2^j<=b<min(2^(j+1),M)}, restrict to
b>=max(5,m0), and put I_AC=sum_J Q_AC(b)/b and I_BH similarly. Weighted
Cauchy applied to A15.4 proves

    I_AC^2 <= D_j I_BH,
    D_j=(Ccap/8) sum_(b in J_j) log(2b)/b
        <= (Ccap/8)(j+2)log2 * W_j.                   (A15.5)

Consequently the actual block contribution of P=AC+BH is at most

    sqrt(W_j)*[sqrt(I_BH) + D_j^(1/4)*I_BH^(1/4)].      (A15.6)

This provides a different sufficient criterion from A11's direct
logarithmic multiplier. For example the STILL UNPROVED candidate
I_BH<=A(C,m0)/(1+j)^(5+eta), eta>0, would suffice in A15.6. The previous
A11 multiplier would require exponent >6 for this power-decay test.
Neither power law is assumed, and convergence of sum I_BH or even of
sum sqrt(I_BH) does not imply the fourth-root series here.

The estimate changes the use of the cap and retains actual Sidon
correlations at each middle difference. It does not establish the
remaining BH bound, a uniform bound for the frozen whole profile, or Q1.
The constants, counting and first-moment argument have passed independent
mathematical review. The bounded integer-mass first-moment lemma is Lean
verified; the complete statement is not yet Lean verified.

## A16. Exact adjacent-gap kernel, and a failed PSD shortcut

Put g_l=a_(l+1)-a_l>0. For an old quadruple h=(p,q,s,c), let
x_h(l)=1[q<=l<s], y_h(l)=1[p<=l<c], and w_h=G_minus,s+G_plus,s.
Then g dot x_h=B, g dot y_h=Hquad, and exactly

    Q_BH(b)=sum_h w_h(g dot x_h)(g dot y_h)=g^T K_b g,
    (K_b)_lm=sum_h w_h[x_h(l)y_h(m)+y_h(l)x_h(m)]/2.    (A16.1)

This retains each actual BH matching once, all strict gates, and the
original genuine prices. K_b is symmetric and entrywise nonnegative;
it need not be positive semidefinite.

The certified A14 M12 history proves the failure for the COMPLETE
kernel, not merely a subkernel. At b=9 or10 it has one BH quadruple
(1,3,6,8), x=1[3..5], y=1[1..7], and w=u_12^[12]. Hence

    K_11=0, K_13=w/2, K_33=w,
    (2e_1-e_3)^T K_b(2e_1-e_3)=-w<0,
    K_13^2>K_11*K_33=0.

Thus PSD and diagonal Schwarz cannot justify a charging argument.
The ACTUAL positive gap vector instead gives exactly

    g^T K_b g=2000*67000*w=134/676350675>0.

No negative physical profile is asserted. Exact matrix multiplication,
record/genuine-price identity, and the old input/checker source hashes
were independently checked without generating another history.

## A17. Diagonal domination and actual tripartite Sidon fibers

A valid consequence of A16 is LINEAR in the positive diagonal weights:
write D_l(b)=K_ll=sum_h x_h(l)w_h. Since Hquad<=H_b,

    Q_BH(b)<=H_b sum_(l=1..b-2) g_l D_l(b).             (A17.1)

No quadratic diagonal bound or PSD hypothesis is used. Each quadruple
is counted over its original middle interval; sum of its g_l is B.

Fix b>=5, n=b-1 and l in1,...,b-2. At component k>=b+1 use actual
point sets

    L={a_1,...,a_l}, R={a_(l+1),...,a_(b-1)},
    F_k={a_(b+1),...,a_min(k,T)}, m_k=min(k,T)-b.

The sets are disjoint. Let v_z count triples in L x R x F_k of sum z.
Actual Sidon two-sum uniqueness makes every coordinate projection
injective on one fiber: if a coordinate agrees, the other two sum to
the same value, and their separate sets forbid the swapped Sidon case.
Therefore, with d_lk=min(l,n-l,m_k),

    0<=v_z<=d_lk,  sum_z v_z=l(n-l)m_k,
    C_all(l,k):=sum_z binom(v_z,2)
      <=l(n-l)m_k(d_lk-1)/2.                           (A17.2)

The collision count has an exact relation to the BH channels. Sort the
two left indices as p<q, the two right indices as s<c, and the future
indices as i<r. Every two different triples in one fiber have all six
points distinct. A parallel old pairing satisfies

    a_p+a_s+a_r=a_q+a_c+a_i,

and yields t=A+C, the plus BH matching. A crossed pairing yields
t=|Cgap-A|, the type-2 minus BH matching (the order of the future
endpoints selects its sign). The fully ordered pairing cannot
have equal sums. Conversely each ungated BH matching supplies exactly
one unordered pair of triples. Type-1 minus belongs to AC and is NOT
an extra BH collision.

Let C_core(l,k) retain only these collisions whose corresponding
quadruple and output satisfy the selected original strict gates.
Then C_core<=C_all and, with both original horizons still present,

    D_l(b)=sum_(k=b+1..M) (kappa_k/H_k^2) C_core(l,k).
                                                               (A17.3)

For k>T the same fixed future set F_T and collision count remain; those
components continue to increase the genuine price. No terminal alpha
or diameter has been replaced. When T=M only, m_k=k-b.

Using A17.1--3 and then m_k<=k-b gives the actual gap/fiber upper bound

    Q_BH(b)<=U_b(M,T)
      :=(H_b/2)sum_(k=b+1..M) kappa_k/H_k^2
           *sum_(l=1..b-2) g_l*l(n-l)m_k(d_lk-1).       (A17.4)

Since l(n-l)min(l,n-l,m_k)<=n^3/8, sum_l g_l=H_(b-1)<=H_b, and
H_k>=H_b, it follows that

    Q_BH(b)<=(n^3/16)sum_(k=b+1..M) kappa_k(k-b).

The finite Abel identity, including its terminal subtraction, is

    sum_(k=b+1..M)kappa_k(k-b)
      =sum_(r=b+1..M)alpha_r-(M-b)alpha_(M+1)
      <=1/(3b^3).

The last step uses the previously proved alpha telescope inequality.
Consequently every selected BH subprofile satisfies

    Q_BH(b)<=(b-1)^3/(48b^3)<1/48.                    (A17.5)

This all-history bound is independently reviewed, and the exact
tripartite fiber cardinal bound from the literal Sidon predicate is
verified in the pinned Lean module. The full core correspondence and profile
estimate remain hand proofs. The upper bound tends to 1/48 and gives
no uniform square-root harmonic sum. It does not close A15 or Q1.

## A18. Exact capacity deficits and failure of their scalar deletion

The actual triple fibers contain information discarded in A17.2. Put
N_lk=l(n-l)m_k and define the nonnegative capacity deficit

    delta_lk=sum_z v_z(d_lk-v_z).

There is the exact finite identity

    2C_all(l,k)=(d_lk-1)N_lk-delta_lk.                (A18.1)

Let E_lk=C_all(l,k)-C_core(l,k)>=0 account for the actual strict gates
and any common quadruple restriction. Define also the positive outer
width loss over the selected BH matching channels

    O_b=sum_h B_h(H_b-Hquad_h)u_(r_h)^[M].

The selected channels here are type-2 minus and plus, once each; their
original coverage at b and upper output horizon T remain in the sum.
Combining A17 with A18.1 yields the exact decomposition

    Q_BH(b)=U_b-Gamma_b-Gate_b-O_b,                    (A18.2)
    Gamma_b=(H_b/2)sum_k kappa_k/H_k^2 sum_l g_l delta_lk,
    Gate_b=H_b sum_k kappa_k/H_k^2 sum_l g_l E_lk.

Every subtracted term is nonnegative. In particular this identity does
not assert that discarded capacities can be spent separately at each
cut. U_b, Gamma_b and Gate_b all use the same actual adjacent gaps,
fibers, output sets and common genuine components.

The identity was independently checked on ONE component k=48 at b=24,
T=96 of each of the two existing M96 histories. The following are the
exact UNPRICED component coefficients; multiplication by kappa_48/H_48^2
would apply the same genuine component price to all columns.

| Existing history / selection | U | Capacity deficit | Gate deletion | Outer loss | Actual BH coefficient |
|---|---:|---:|---:|---:|---:|
| Greedy / full core | 3205864656 | 2979944118 | 7310430 | 76941442 | 141668666 |
| Greedy / all large old gaps | 3205864656 | 2979944118 | 54205542 | 60114562 | 111600434 |
| Variant / full core | 3009983688 | 2778975966 | 9102871 | 66734919 | 155169932 |
| Variant / all large old gaps | 3009983688 | 2778975966 | 57579028 | 52169120 | 121259574 |

Thus the capacity deficit is about 93% / 92% of the upper coefficient
in these two observed components. These finite proportions are not a
uniform estimate or an asymptotic law.

### A fixed-cap scalar test shows exactly why U_b alone is insufficient

Consider ONLY the scalar relaxation H_k=k(k-1)/2, g_l=l. It satisfies
the fixed scalar cap C=1,m0=2 and the usual packing-scale lower diameter.
It is NOT Sidon: for a_k=1+H_k, a_4-a_3=a_3-a_1=3. We use it solely
to evaluate the relaxed formula U_b, not an actual core profile.

For b>=16, M=T>=3b, retain in U_b only components 2b<=k<=3b and
indices ceil(b/4)<=l<floor(b/2). There are at least b/8 such l, and

    g_l,l>=b/4, n-l>=b/2, k-b>=b, d_lk-1>=b/8,
    sum_l g_l*l(n-l)(k-b)(d_lk-1)>=b^6/2048.

Also H_b>=b^2/4 and the unchanged Abel coefficients satisfy

    kappa_k=4/[k(k^2-1)^2]>=4/k^5,
    kappa_k/H_k^2>=16/(3^9 b^9),  2b<=k<=3b.

At least b components contribute. Inserting only those positive terms
therefore gives the explicit lower bound

    U_b(M,M)>=1/(1024*3^9)=1/20155392.                 (A18.3)

Hence the square-root harmonic cost of this scalar majorant diverges
as M grows, even though its scalar cap has the same fixed C,m0 at
every rank. The scalar relaxation does not satisfy Sidon, and the
actual deficits cannot be set to zero in this history. A18.3 rejects
only a proof that deletes those actual correlations and then tries to
sum U_b using these scalar cap/packing conditions alone.

Both A18.2 and the scalar no-go have passed independent mathematical
review. The next useful object is the actual deficit evolution when
future points enter a fixed tripartite fiber, not another count-only
upper bound or a new frozen theorem. No Q1 conclusion follows here.

## A19. Exact future-fiber evolution and a raw monotonicity counterexample

Fix b,l and the two old groups. Their actual pair-sum bank
U=L+R has zero-one coefficients by Sidon uniqueness and disjointness.
Let S=|U|=l(n-l). For a new future point a_(k+1), k+1<=T, its translated
bank has indicator w_z=1[z in a_(k+1)+U]. The old triple-fiber values v_z
become v_z+w_z, and the number of newly created unordered collisions is

    J=sum_z v_z w_z.

With m=k-b, d=min(l,n-l,m), d'=min(l,n-l,m+1), direct finite expansion
using w_z^2=w_z gives

    delta_(k+1)-delta_k
      =(d'-d)Sm+(d'-1)S-2J.                           (A19.1)

Before the minimum saturates, d=m,d'=m+1 and J<=mS, so the raw deficit
is nondecreasing in this PROVED range. After saturation, the exact
condition for nondecrease is

    J<=(d-1)S/2.                                     (A19.2)

It must not be assumed. For k>=T no further future point is inserted;
v,m,d and the deficit stay fixed while the later genuine price
components remain in A18.2.

### Finite tests and an actual counterexample

The two already certified M96 histories showed no negative increment
in 9,108 exact checks at b=12,24,48. There were 804 trivial zeros and
8,304 positive increments. This was finite evidence only.

A targeted construction then disproved global raw monotonicity. Before
checking it, the bounded case fixed C=1000000,m0=2,M=T=11. Its history is

    (1,18,1000,1011,1024,2000,
     99959,99993,99994,99996,100000).

All 55 positive differences, repeated two-sum Sidonness, and every
required rank cap passed the existing evaluator and independent checker.
Strict comparisons have UNKNOWN=0. At b=6,l=2, the actual old pair bank is

    U={1001,1012,1018,1025,1029,1042}, S=6, d=2.

Before the last point, m=4 and all 24 triple sums are distinct, so
delta=24 and C_all=0. Appending a_11 produces four double fibers and
22 single fibers, so delta'=22, C_all'=4, and

    J=4,  delta'-delta=6-8=-2<0.                      (A19.3)

The four genuine future output differences are 41,6,7,4, comprising
one plus and three minus tripartite collisions. All fibers and endpoint
triples were independently reconstructed.

The original strict core of this M11 history is exactly EMPTY, with
N=0. This example is solely a counterexample to monotonicity of the
raw tripartite deficit used in A18; it is not a large core example,
a negative profile, a failure of the frozen bound, or a Q1 counterexample.
Only this one specified auxiliary instance was checked; no campaign of
empty-core histories was generated.

### Keeping the gates changes the potential obligation

Define the gate-adjusted deficit

    D_eff(l,k)=delta_lk+2E_lk=(d_lk-1)N_lk-2C_core(l,k).

Every previously present core output retains its own strict tests when
future points are appended. Let J_core be the count of newly admitted
BH core collisions at the new upper output rank. Then exactly

    D_eff(l,k+1)-D_eff(l,k)
      =(d'-d)Sm+(d'-1)S-2J_core.                      (A19.4)

Here J_core<=J, so pre-saturation monotonicity survives. In the M11
counterexample J_core=0 and the effective deficit INCREASES by6.
Thus the raw counterexample does not refute gate-adjusted monotonicity.
After saturation, that further candidate requires the genuine inequality
J_core<=(d-1)S/2. It remains unproved in this work.

Even proving this monotonicity would not by itself close Q1: a lower
bound strong enough to pay A18.2 in the required weighted cut/component
norm is still necessary. This is the next concrete potential test, not
a replacement frozen theorem or an assumed closing estimate.

The generic finite zero-one deficit-increment identity is verified
in the pinned Lean module. The actual triple-bank/core instantiation and all global
potential/summability assertions remain separate mathematical tasks.

## A20. Saturated strict-core test and the remaining factor two

The candidate J_core<=(d-1)S/2 was tested on the two already certified
C=1,m0=2,M=T=96 histories, using their original BH record banks. There
were 82,335 nontrivial saturated (b,l,r) cells in each history, 164,670
in total, and no violation. The exact largest ratio to the proposed
upper bound was 3/8 in the greedy history and 1/3 in the variant.
The first maximizers were respectively (b,l,r)=(11,2,14) with S=16,
d=2,J_core=3, and (12,9,17) with S=18,d=2,J_core=3. Their original
records and every strict gate were independently rechecked, UNKNOWN=0.
This is finite evidence only; neither observed ratio is assumed globally.

There is a precise gap in the elementary argument. At a new translated
pair-sum site z, the AFTER-addition Sidon fiber bound gives
v_old(z)+1<=d, hence only

    J_core<=J<= (d-1)S.                              (A20.1)

This is twice the desired bound. Writing R_new=J-J_core for the actual
newly deleted noncore collisions, the saturated identity is

    Delta D_eff=(d-1)S-2J+2R_new.

When J>(d-1)S/2, nondecrease requires the genuine compensation
R_new>=J-(d-1)S/2. Nonnegativity R_new>=0 does not prove it. No raw
fiber sweep or new empty-core fixture was used in the 164,670-cell test.

### A structural constraint for an actual two-point left group

For L={x,x+h}, let the right points be R_u, and let X be the newly
added future point. Each new raw BH collision can be oriented as

    t_e=X-f_e=R_v-R_u+epsilon*h>0, epsilon in {+1,-1},

with distinct old right endpoints and f_e an actual previous future
point. For each fixed epsilon, two distinct such edges cannot share a
source u or a target v. For example, shared u would give
t_e-t_e'=R_v-R_v', and therefore the difference between two distinct
future points would equal a difference between two old right points,
contradicting Sidon uniqueness. Shared v is identical with signs
reversed. Thus each sign class has in-degree and out-degree at most one.

If the same ordered edge occurs with BOTH signs, its two future points
have difference 2h. There can be at most one such double-signed edge:
two would give the same positive future difference with distinct
endpoint pairs. These constraints are necessary, not sufficient, for
the entire old/future union to be Sidon. Four-term collisions between
different edges must still be checked. The original strict gates are
additional requirements; a symbolic edge is not automatically core.

This supplies a concrete construction route for adversarial testing,
not an assertion that the missing half or a counterexample exists.

## A21. Monotonicity alone still leaves a nonsummable scalar relaxation

This tests the STRENGTH of the candidate in A19/A20, not its truth on
actual Sidon histories. Keep the scalar diameters H_k=k(k-1)/2 and gaps
g_l=l from A18. They obey the fixed scalar C=1,m0=2 cap but are NOT
Sidon. At each b,l,m put n=b-1, S=l(n-l), d=min(l,n-l,m), and define
the integer capacity

    B(m)=(d-1)Sm/2, B(0)=0.

B(m) is a nonnegative nondecreasing INTEGER: if d is odd then d-1
is even; if d is even it equals one of l,n-l,m, so Sm is even.
Define abstract collision counts and their effective deficit by

    C_*(m)=floor(B(m)/2),
    D_*(m)=2B(m)-2C_*(m)=2ceil(B(m)/2).

Both C_* and D_* are nondecreasing. At saturation d is fixed and
Delta B=(d-1)S/2 is an integer, so the new abstract count obeys

    0<=Delta C_*<=Delta B=(d-1)S/2.                  (A21.1)

Thus these INTEGER count arrays satisfy exactly the desired saturated
increment bound as well as global effective-deficit monotonicity.
For B>=2, floor(B/2)>=B/4. Form the diagonal relaxed profile

    V_b=H_b sum_(k=b+1..M) kappa_k/H_k^2
                   sum_(l=1..b-2) g_l C_*(k-b).

For b>=16,M=T>=3b retain the same l and k ranges used in A18.3.
Every retained B is at least 2, so the retained V mass is at least
one quarter of that retained U mass. With the unchanged genuine
alpha differences and terminal convention this proves

    V_b>=1/(4096*3^9)=1/80621568.                    (A21.2)

Consequently sum_(b=16..floor(M/3)) sqrt(V_b)/b diverges with M,
although D_* is nondecreasing and A21.1 holds everywhere it applies.

The arrays are a relaxation, not asserted realizable by triple fibers,
original gates, outer widths, or one actual Sidon history. This is NOT
a counterexample to gate-adjusted monotonicity, the frozen uniform
profile, or Q1. It specifically rules out closing the weighted norm
from scalar cap/packing, capacity, and that monotonicity alone. A proof
must additionally use quantitative actual correlations or the exact
width losses; qualitative monotonicity cannot replace that obligation.

## A22. Fixed cap excludes a short left group from the remaining profile

This is an actual-record support bound for the all-three-old-gaps-large
remainder from A12, not a change to the frozen core. Write its sorted
old quadruple as p<q<s<c. Its first physical gap obeys

    a_q-a_p>c^2/(log c)^3.                           (A22.1)

If q>=m0, the all-rank cap and q<=c, c>=3 give

    a_q-a_p<=H_q<=C q^2 log(2q)<=2C q^2 log c.

Hence q>c/(sqrt(2C)(log c)^2). At any actually covered cut c<b<i<r,
the original far-output gate r<c log c also gives c>b/log b. Since
log c<log b, this proves the cut-relative support condition

    q>b/(sqrt(2C)(log b)^3).                         (A22.2)

The ranks below m0 need a separate, finite, cap-dependent treatment.
Put B0=C m0^2 log(2m0), choose

    c0=max(m0,3,ceil((B0+1)^2)),
    b0=ceil(c0 log c0).

If c>=c0 and q<m0, then m0<=M and
a_q-a_p<=H_m0<=B0. But log c<sqrt(c) for c>=1 yields
c^2/(log c)^3>sqrt(c)>=B0+1, contradicting A22.1.
If c<c0, original coverage and the strict far-output gate instead give
b<r<c log c<c0 log c0. Thus every remaining record at b>=b0 has q>=m0
and satisfies A22.2. No finite-prefix maximum or infinite extension is
used; b0 is the explicit displayed function of C,m0.

For the large-gap BH diagonal in A16--18, each channel requires q<=l<s.
Consequently, at every b>=b0,

    D_l(b)=0 whenever l<=b/(sqrt(2C)(log b)^3).        (A22.3)

The same conclusion holds component by component for every original
M,T, including genuine price components k>T. No weight, cut endpoint,
or core comparison is changed. In particular, fixed l=2 constructions
can test the universal monotonicity candidate only within finitely many
cut scales for each fixed cap. They cannot supply an unbounded family
in this remaining profile by keeping the same small left group.

This removes an early-rank region exactly. It does not estimate the
diagonal mass on the surviving region l>b/(sqrt(2C)(log b)^3), and
does not pay the required BH square-root or AC fourth-root norm.

## A23. Strict-core counterexample to saturated effective-deficit monotonicity

The still-open candidate in A19/A20 is FALSE in general, even when the
71 offending new collisions all have three large old physical gaps.
Before construction, this campaign fixed C=10^14,m0=2. Exactly one
history was tested (t=64, trial 1); no t=96 history or later trial was run.
Its complete positive integer sequence and graph specification are in

    evidence/u4f_core/finite_campaign/
      C100000000000000_m02_colored_star/candidate_t64_trial1.json
    SHA-256 cb26b78d3c4768ea022cf734a44414cf27090ae90d0a5e2f65c03187cc1982e0.

Here L={1,6000000001}, the 64 old right points occupy ranks3..66,
the rank-67 cut point is 31442910617, and the final point is X=10^12.
The 88 earlier future points are X-t_e for actual positive outputs
t_e=R_v-R_u+epsilon*6000000000, arranged increasingly. The graph uses
64 plus-sign edges in one alternating low/high directed cycle and
24 minus-sign long edges. The actual whole sequence, not the graph
heuristic, passes all 12,090 distinct-positive-difference checks,
independent repeated two-sum Sidon checks, and every rank cap from2
through156 by both rational-log implementations.

At b=67,l=2,M=T=156, S=2*64=128,d=2 and m_before=88, so the stage is
saturated. The complete new raw collision count is 88. Original strict
gates delete17; the remaining count is

    J_core=71>64=(d-1)S/2, ratio=71/64.              (A23.1)

All comparisons have UNKNOWN=0. The admitted new BH channels comprise
47 type-2 minus and24 plus records. Every one also passes the A12
all-three-old-gaps-large restriction. An independent root reconstruction
queried the two actual numeric BH outputs of every old quadruple
(1,2,s,c), and obtained precisely the same71 channels.

The root reconstruction also computed complete raw fibers at this
one (b,l), on the same actual history, before and after the final point:

| Upper future rank | Triple mass | Single fibers | Double fibers | Raw collisions | Core collisions | Effective deficit |
|---:|---:|---:|---:|---:|---:|---:|
| 155 | 11264 | 11264 | 0 | 0 | 0 | 11264 |
| 156 | 11392 | 11216 | 88 | 88 | 71 | 11250 |

Thus the actual effective deficit decreases by14, directly as well as
through A19.4. The 17 newly deleted collisions contribute +34, while
the raw deficit decreases by48; their compensation is insufficient.
The saved root evidence is `evidence/u4f_core/colored_star_root_review.json`.

The SAME M156 history then passed the unchanged complete reference
evaluator and independent output-based checker: 2,435 original core
records, all2,435 in the three-large-gap remainder, with UNKNOWN=0.
Every rational profile coefficient, genuine price, I_j and original
physical-record coverage agrees. The canonical profile input SHA-256 is
9234ad0557a920d67144c5d190c2663084be18e9a8ec986fe9598b0b7250d157.
Its final genuine price is exactly

    u_156^[156]=1/23095496774953809006450023095496775.

The displayed decimal quantities below are approximations, not certified
square-root enclosures:

    N(156,156) approximately 0.00001033069026003723572692681037.

| Dyadic block j | I_j, approximate | Actual block contribution, approximate |
|---:|---:|---:|
| 1--4 | 0 (exact) | 0 (exact) |
| 5 | 3.77214275927645e-11 | 3.94726347138112e-6 |
| 6 | 6.67095592355844e-11 | 6.12407080733922e-6 |
| 7 | 4.90935985866081e-13 | 2.59355981316901e-7 |

The maximal cap usage is approximately0.00001240460794390624 at rank3.
All individual ranks are nevertheless certified against the SAME fixed
C=10^14,m0=2. The leading total-I birth/output interval is
(c,i,r)=(38,71,72), cuts39..70; the next two are (44,70,71), cuts45..69,
and (43,68,71), cuts44..67. Exact values, complete records and the full
interval ranking are retained in the canonical JSON and record bank.

This is one finite fixed-cap counterexample to saturated gate-adjusted
monotonicity, including its large-gap version. It is not an unbounded
profile family, a counterexample at C=1, or a refutation of U4-F or Q1.
A22 also explains why keeping this same fixed left-group size cannot
sustain an asymptotic counterexample in the large-gap remainder.

The signed increment identity in A19 remains valid. Future work must
allow negative increments and prove a quantitative compensated estimate;
the rejected monotonicity premise must not be reused. A21 separately
shows why a bare monotonicity premise would have been too weak anyway.

## A24. Exact cut exchange and failed retirement compensation

Fix one genuine component k and t=min(k,T), with b+2<=t, and keep
1<=l<=b-2 fixed as the cut moves b to b+1. The actual groups are
L={a_1,...,a_l}, R={a_(l+1),...,a_(b-1)} and
F0={a_(b+2),...,a_t}. Write additive convolution on integer sums as *:

    f=1_L*1_R*1_F0,
    w_plus=1_L*delta_(a_b)*1_F0,
    w_minus=1_L*1_R*delta_(a_(b+1)),
    v_before=f+w_minus, v_after=f+w_plus.

The common f can have multiplicity. Actual Sidon two-sum uniqueness
and disjointness of the respective two groups make each w zero-one.
Consequently, for C(v)=sum_z v_z(v_z-1)/2,

    C(v_after)-C(v_before)=sum_z f_z(w_plus,z-w_minus,z). (A24.1)

The two changed banks need NOT have disjoint supports. If one instead
uses v_before in the inner product, the correct expression is

    sum_z v_before,z(w_plus,z-w_minus,z)
      +sum_z w_minus,z-sum_z w_plus,z*w_minus,z.

The overlap subtracts hypothetical pairs between a point being removed
and one being added; those two triples never coexist at either cut.
For d_before=min(l,b-1-l,t-b) and
d_after=min(l,b-l,t-b-1), exact expansion gives

    Delta delta=(d_after-d_before)sum f
      +(d_after-1)sum w_plus-(d_before-1)sum w_minus
      -2 sum f(w_plus-w_minus).                     (A24.2)

Both identities were verified from the complete actual triple banks
at b24->25,k48,T96,l6/12/18 in both existing C=1,m0=2 histories.
The changed-bank overlap is2/3 in the greedy/variant l18 cases and
zero in their l6/l12 cases. Capacity changes and the direct deficits
also agree exactly. No common-tail component or terminal alpha is reset.

### The original core has an exact physical boundary law

For any fixed original record bank, the open-cut indicator changes only
at a birth c=b with b+1<i or a retirement i=b+1 with c<b. The empty
coverage case c=b,i=b+1 belongs to neither boundary. Thus for the
original BH count at a fixed l and component, or for any fixed nonnegative
record weight,

    quantity_(b+1)-quantity_b=Birth_b-Retirement_b.   (A24.3)

All strict predicates and the selected large-gap quadruples remain
the same on both sides. In the count version, retain q<=l<s; in the
weighted version each physical BH matching retains its B*Hquad, then
the same genuine kappa_k/H_k^2. One may also omit the l filter to obtain
the entire BH coefficient, counting each matching once. The separate
l-filtered diagnostics are not independent budgets to be added.

### A precise failure of replacing the weights by record counts

The candidate Retirement>=Birth is false in the tested actual histories.
More sharply, in the variant history's all-large-gap selection, b24->25,
k48,l6, there are only3 births and5 retirements, but the complete weights
are

    Birth_BH=571826, Retirement_BH=147453,
    BH_count:84->82, BH_coefficient:5348845->5773218.

All8 boundary records pass the independently rechecked original strict
gates. The exact genuinely priced component increase is

    424373/1148518878296832>0.                        (A24.4)

The greedy large-gap l6 case also loses7 records but gains1163678 in
unpriced BH coefficient. For the WHOLE large-gap BH coefficient, with
each matching counted once, the changes are +47682425 (greedy) and
+45546481 (variant). The latter increases are still single-component
facts, not claims about the complete M96 horizon or an asymptotic norm.

All6 raw-bank cases and all12 specified original-core/large-gap weighted
boundary identities passed. The complete banks, original record rows,
explicit small counterexamples and source/checker bindings are in
`finite_campaign/CUT_SHIFT_B24_COMPONENT48_REVIEW.md` and its JSONs.
No additional history or broader cut scan was generated. This rejects
pointwise retirement domination, and even a count-to-weight implication;
it does not reject a correctly compensated signed-flux estimate.

## A25. A valid full-horizon signed-flux envelope, and its limit

Write B_b and R_b for the ORIGINAL full record masses on the two
boundaries in A24.3, using u_r^[M] and upper output horizon T exactly
as frozen. At two valid cuts 3<=b<b+1<T<=M, the following bounds hold
uniformly in M,T:

    B_b<=2 binom(b-1,3) alpha_(b+3)<=1/(3b),
    R_b<=S_b/[3(b+1)^3 H_b^2]<=b^2/[12(b+1)^3],      (A25.1)

where S_b is the sum of squared actual positive differences among the
first b points. These bounds also apply to the boundary masses of the
BH, AC or common large-gap subprofiles by termwise domination.

For the birth bound, a record with c=b covering b+1 must have i>=b+2
and r>=b+3. There are binom(b-1,3) possible old quadruples. The unique
actual output for each numeric difference allows at most the three
matchings in A10. Their products sum to

    AC+(A+B)(B+C)+BHquad=2AC+2BHquad<=2Hquad^2<=2H_b^2.

Every actual matching has u_r^[M]<=alpha_(b+3)/H_b^2, obtained only as
an UPPER inequality from the unchanged telescoping coefficients.
This proves the first bound, and b(b-1)(b-2)(b-3)<=(b+3)^2(b+2)^2
proves the displayed simpler envelope. Absent core matchings only
decrease the birth sum; no enlarged record set becomes a premise.

For retirement, fix the actual lower output i=b+1. For each r>=b+2,
its t=a_r-a_i selects the shift graph on actual old difference labels.
The degree-two argument A02.1 bounds the sum of d*e on its edges by
S_b. Sidon uniqueness retains the one actual output for each t, and
the original core is a subset of those edges. The genuine-price bound
u_r^[M]<=alpha_r/H_b^2 and the proved alpha telescope give

    sum_(r=b+2..infinity)alpha_r<=1/[3(b+1)^3].

This numerical upper series assumes no infinite admissible extension.
The actual dispersion bound S_b/H_b^2<=b^2/4 yields A25.1. If also
b>=m0, the cap-sensitive A02 dispersion estimate sharpens retirement to

    R_b<=b^2/[12(b+1)^3]
         *[1-(1-4/b^2)/(12C log(2b))].               (A25.2)

The bracket is nonnegative on each actual admissible history by the
same packing argument used in A02. No cap is imposed at b<m0.

Combining these nonnegative boundary masses with the exact boundary
identity proves the full-horizon signed estimate

    -1/(12b)<=P_(b+1)-P_b<=1/(3b).                   (A25.3)

The explicit lower side may be sharpened to minus the bound A25.2.
It is essential that this is a bound on CHANGES, not a claimed decay
of P_b. On a multiplicative cut interval, summing 1/b gives a constant
depending on that interval's ratio; it does not give an absolute
summable envelope for sqrt(P_b)/b or the fourth-root BH cost in A15.
The failed retirement premise is not used anywhere in A25.

There is also a precise numerical no-go for using just these envelopes.
For M>8e^2+1 define an ABSTRACT profile on2<=b<=M-1 by

    p_b=1/1000 * max(0,min(log(b/8),1,log((M-1)/b))).

It vanishes at the initial cuts and at M-1, and never exceeds1/1000.
As a function of log b, its Lipschitz constant is1/1000, so
|p_(b+1)-p_b|<=1/(1000b). Set abstract boundary masses to the positive
and negative parts of this difference. Positive changes occur only
at b>=8, where the exact birth envelope in A25.1 is at least1/(384b):
use b-j>=b/2 for j=1,2,3 and b+j<=2b for j=2,3. For C=1 and b>=3,
the cap-refined retirement envelope A25.2 is at least1/(64b), since
its bracket is at least11/12 and (b/(b+1))^3>=27/64. Thus this profile
obeys even those more precise numerical upper envelopes.

Nevertheless p_b=1/1000 throughout
ceil(8e)<=b<=floor((M-1)/e), so its square-root harmonic sum diverges
as M grows. This profile and its boundary masses are NOT asserted to
arise from an actual Sidon history, any strict-core record bank, or
the original component prices. It refutes only sufficiency of the
displayed flux envelopes, cap coefficient and endpoint conditions by
themselves. The remaining task must retain the actual joint records.

The generic exact collision exchange, deficit exchange, physical-record
cut boundary and old-quadruple product inequality are formalized in
the supporting Lean module. The actual core instantiation and the full
A25 all-history price/dispersion estimate remain hand mathematics.

## Current mathematical frontier

The frozen whole profile still decomposes as A10; A12 pays all small
adjacent old gaps, and A15 supplies the cap-sensitive nonlinear AC/BH
comparison. Its fourth-root cost must still be paid unless AC is
controlled jointly by another valid argument.

A16 rules out a PSD/diagonal-Schwarz shortcut for the actual BH kernel.
A17 instead uses positive linear diagonal domination and actual
tripartite Sidon fibers, giving Q_BH<1/48 at every cut. That constant
upper bound is insufficient for the required square-root harmonic sum.
A18 retains the exact physical capacity deficit, gate deletion and
outer-width loss. Deleting these correlations leaves a scalar majorant
whose norm diverges even under a fixed scalar cap; that scalar sequence
is not Sidon and is not a frozen-theorem counterexample.

A19's signed future-point increment is valid, but A23 now refutes even
the strict-core gate-adjusted monotonicity candidate on one independently
certified fixed-cap M156 history. All71 offending channels also belong
to the all-large-old-gap remainder. The earlier M96 scan in A20 and the
empty-core raw M11 counterexample retain only their stated finite scopes.
A21 separately shows that qualitative monotonicity would not pay the
norm in the scalar/count relaxation. Neither monotonicity is assumed.

A22 uses the cap to remove the exact early-left-index support region
l<=b/(sqrt(2C)(log b)^3), beyond an explicit C,m0-dependent cut. It does
not bound the surviving diagonal mass. In particular, continuing a
fixed-l=2 construction is not the next asymptotic attack.

A24 now establishes simultaneous cut exchange, including the common
triple bank and exact original record boundaries. It refutes pointwise
retirement domination, and shows that even decreasing core counts can
have increasing genuine BH mass. A25 instead proves signed full-horizon
flux envelopes with the actual Sidon/cap dispersion improvement. A
nonphysical profile shows exactly why those envelopes still do not
control the target norm.

The next nonduplicate action is to retain the signed boundary measure
on the ACTUAL integer middle gap B: birth and retirement masses at B
carry their own Hquad and common component price. Expand their first
moment by exact integer gap thresholds, starting with the eight-record
A24 weighted counterexample, and seek an occupancy/charging bound using
Sidon uniqueness of each old B-pair and the fixed cap. This must track
repeated uses of the same B-pair across births, cuts and components;
no threshold or cut gets an independent budget. A moment identity
alone would not be a new uniform estimate, and none is assumed proved.

No unproved decay, maximum-prefix length, cap-free operator bound,
AC<=BH comparison, PSD structure, raw-deficit monotonicity or effective-
deficit monotonicity is assumed.
The frozen K(C,m0) estimate and original Q1 remain open. The final
literal Lean theorem and full clean dependency/axiom closure are absent.
The master goal remains active.

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

Continuation 03 adds `bounded_integer_mass_first_moment`; its accepted
pinned compiler and type/axiom evidence is `LEAN_VERIFICATION_03.json`.
A13 and the full A15 Sidon instantiation are independently reviewed hand
proofs; A14 has independent exact finite certification, not a final Lean
Q1 theorem.

Continuation 04 adds the actual disjoint-tripartite fiber definition,
its membership and cardinal bound using the unchanged literal Sidon
predicate, and the generic zero-one deficit-increment identity. The
accepted pinned source/type/axiom binding is `LEAN_VERIFICATION_04.json`
(18 supporting theorems total). The full original core/triple collision
bijection, profile upper bound and weighted deficit potential remain
hand mathematics rather than a literal Q1 proof.

Continuation 05 adds the A20--A23 mathematical/finite attacks. Its new
statements are not Lean-verified. The support module remains unchanged
at18 theorems with the current accepted LEAN_VERIFICATION_04 binding;
no repeat build, new default target, or final Q1 verification is claimed.

Continuation 06 adds A24--A25. Four new supporting statements formalize
the two generic zero-one exchange identities, exact physical-record cut
boundary and old-quadruple product bound. The full actual core/price
instantiation, the full flux estimate and all remaining weighted norm
claims are not covered by those supporting statements.
The accepted current source/type/axiom binding is
`LEAN_VERIFICATION_06.json`, with22 supporting theorems total and
successful pinned compiler/type/axiom logs. The previous18-theorem
source/audit are preserved in `source_snapshot/continuation_06/`;
the old `LEAN_VERIFICATION_04.json` is its historical binding.

Read this file and `ATTEMPTS.jsonl` at restart; use the source manifest only
to locate unchanged originals. Reuse the already certified finite campaign
when testing a concrete new inequality. Do not repeat Gate 0, the old
declaration inventories, the C143 campaign, or environment design.
