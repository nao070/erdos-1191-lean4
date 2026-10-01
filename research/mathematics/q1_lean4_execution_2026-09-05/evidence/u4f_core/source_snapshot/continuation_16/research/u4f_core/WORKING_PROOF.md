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

## A26. Signed integer middle-gap flux and an exact reuse obstruction

Fix one genuine component k and one cut transition. On the actual
positive integer middle gap B, define the finite signed measure

    mu(B)=sum_(birth records at B) Hquad
             -sum_(retirement records at B) Hquad.

For this measure, including its negative coefficients, finite interchange
and B=sum_(h=1..B)1 give the exact identity

    sum_B B mu(B)=sum_(h>=1) sum_(B>=h) mu(B).       (A26.1)

The unchanged component coefficient kappa_k/H_k^2 multiplies both sides.
All thresholds refer to the SAME records. This identity creates neither
new budgets nor a sign assumption on their tails.

For the eight-record A24 variant witness at b24->25,k48,l6, the actual
measure is

    (B,mu(B))=(14,-184),(48,529),(70,-350),(105,-349),
                (214,-350),(332,713),(422,713).

Its seven constant integer-threshold intervals have lengths
14,34,22,35,109,118,90 and tail values722,906,377,727,1076,1426,713.
Their weighted sum is424373, giving the genuine increment
424373/1148518878296832. These tails all happen to be positive; this is
an exact finite example, not a universal tail sign theorem.

The same seven actual middle pairs were traced through r<=48 in the
existing fixed C=1,m0=2 variant M96 record bank. They have183 original
BH records,68 with all old gaps large. Every strict comparison is
certified with UNKNOWN=0. The record harmonic-coverage sum equals
the cutwise sum exactly as a rational number. No history was generated.

The candidate "a unique Sidon B permits only one use at a fixed cut
and component" is FALSE even with the same latest birth and type:
B=48 has its unique middle ranks(6,9), but at b11,k48 the type3 old
quadruples(2,6,9,10) and(1,6,9,10) both qualify. Their actual outputs
are(17,18) and(19,20), Hquad87 and88, and BH4176 and4224. Both are
strict core and all-large-old-gap records. At b25 this same B has22
simultaneous original BH uses,11 in the large-gap subset.

The exact witness, all183 traced records and their physical intervals
are bound by `finite_campaign/integer_middle_gap_signed_measure_manifest.json`;
the detailed note is `INTEGER_MIDDLE_GAP_SIGNED_MEASURE_REVIEW.md` in
that directory. The generic signed identity A26.1 is additionally
Lean verified, with integer B represented by index i=B-1.
This rejects one-use charging; it does not refute a uniform U4-F bound.

## A27. Actual two-coordinate recovery gives a uniform cost for one middle pair

Fix an actual middle pair q<s and B=a_s-a_q. For a cut b>s and a
component k>=b+1 let t=min(k,T)>=b and put

    p=q-1,  v=b-1-s,  m=t-b.

Count only BH records with old ranks x<q<s<c<b and b<i<r<=t.
The three disjoint sign classes, in terms of actual point values, are

    plus:       a_c+a_i = a_x+a_r+B;
    minus C>A:  a_x+a_c+a_i = a_r+a_q+a_s;
    minus A>C:  a_x+a_c+a_r = a_i+a_q+a_s.          (A27.1)

Here A=a_q-a_x and C=a_c-a_s. The C=A case has zero output and is
excluded. The BH component of the type2 minus record is counted once;
the type1 AC record does not create a second BH contribution.

Within each sign class, fixing any TWO of x,c,i,r fixes the signed
sum of the remaining two point values. If their coefficients have
equal signs, their sum is fixed. If opposite, their nonzero difference
is fixed. The actual Sidon property determines the unordered sum pair
or ordered positive-difference pair uniquely. In the sum case the
strict rank order of the coordinate groups removes the swapped pair.
All six rank pairs are covered by this argument. In particular there
is no zero-difference exception and no coincident-endpoint ambiguity.

Projections onto(x,c),(x,i),(c,i),(i,r) give, respectively, pv,pm,vm,
binom(m,2) possibilities per sign class. The first bound improves
across classes: for each old quadruple there is at most one actual
plus output and at most one actual minus output. Consequently

    n_B(b,k)<=min(2pv,3pm,3vm,3 binom(m,2)).        (A27.2)

This holds for the original strict core, its all-large-gap subset,
or any further subset: deleting records preserves the injections.
It permits the actual repeated uses seen in A26. It assumes no cap,
no maximum prefix length and no existence of an infinite history.

Define the actual fixed-pair subprofile by finite component interchange:

    w_B(b;M,T)=B sum_(k=b+2..M) kappa_k/H_k^2
                      *sum_(same-B records covering b,r<=min(k,T)) Hquad.
                                                        (A27.3)

For k>T, the actual record set stops growing but its genuine component
still contributes. Since Hquad<=H_b<=H_k, A27.2 gives

    w_B <= (B/H_b) min(2pv alpha_(b+2),
                         min(p,v)/b^3, 1/(2b^2)).       (A27.4)

The first term follows from the finite tail
sum_(k=b+2..M)kappa_k=alpha_(b+2)-alpha_(M+1).
For the second term, extend the nonnegative sum to start at b+1 and
use m<=k-b and the exact finite identity from A17,

    sum_(k=b+1..M)kappa_k(k-b)
       =sum_(r=b+1..M)alpha_r-(M-b)alpha_(M+1)<=1/(3b^3).

For the third, the exact finite second difference is

    sum_(k=b+2..M)kappa_k binom(k-b,2)
       =sum_(r=b+2..M)alpha_r(r-b-1)
           -binom(M-b,2)alpha_(M+1)<=1/(6b^2).

The last numerical upper bound is A02's alpha telescope. These are
upper inequalities obtained by dropping NEGATIVE terminal corrections,
not alterations of the frozen u_r^[M]. If the sums are empty, w_B=0.

There is a uniform, full-horizon square-root harmonic cost for this
ONE physical middle pair. Integer Sidon packing gives
H_b>=b(b-1)/2. For b>=s+2, the first term of A27.4 implies

    w_B <= 4B(q-1)(b-1-s)/[b(b-1)(b+2)^2(b+1)^2]
         <=4B(q-1)/b^5.

Indeed the denominator is at least b^6 for b>=2, and b-1-s<=b.
The earlier cuts have no such records. Integrating x^(-7/2) from s+1
therefore gives the explicit bound

    N_B(M,T):=sum_(b=2..T-1) sqrt(w_B(b;M,T))/b
       <= (4/5)sqrt(B(q-1))/(s+1)^(5/2)=:beta_(q,s).  (A27.5)

This is uniform in both horizons for the SAME actual middle pair.
For s>=m0 the fixed cap has the additional legitimate consequence

    beta_(q,s) <= (4sqrt(C)/5)
                  *s sqrt((q-1)log(2s))/(s+1)^(5/2).  (A27.6)

It uses B<=H_s<=C s^2 log(2s), with the original fixed C,m0;
no cap is imposed at ranks below m0.

The proposed proof by summing THESE separate pair budgets fails at a
precise inequality. Finite Minkowski does give N_BH<=sum_(q<s)beta_(q,s),
but the latter explicit majorant has no length-independent numerical
bound. For any available finite increasing integer prefix and s>=8,
take ceil(s/4)<=q<=floor(s/2). There are at least s/8 such q, with
q-1>=s/8 and B>=s-q>=s/2. Thus

    sum_(q=2..s-1)beta_(q,s)
          >=[1/(40*2^(5/2))] s^(-1/2).             (A27.7)

For a finite prefix of length L, summing A27.7 through s=L gives a
growing lower bound on the MAJORANT, not on the actual N_BH. This
does not assert that arbitrarily long prefixes exist in the fixed-cap
class, nor that their true profile norms are unbounded. Appealing to
a cap-dependent maximum prefix length to rescue this estimate would
be the forbidden circular step. The valid per-pair theorem remains
useful, but independent pair budgets cannot by this calculation alone
close the uniform K(C,m0) claim. Joint output/outer-endpoint constraints
were lost when different B-pairs were bounded separately.

The occupancy recovery, finite terminal terms, constants and this
majorant failure have passed independent hand review. The ordered-pair
recovery step is verified from the unchanged literal Lean Sidon
predicate. Full record cardinality, genuine price summation and
A27.5--7 are hand proofs, not complete Lean core-norm theorems.

## A28. Oriented output energy and joint integer-output packing

This attack keeps a common actual output for records with DIFFERENT
middle pairs. Fix b>=3 and write D for the actual positive differences
of the first b-1 points, H=H_b, and S=sum_(d in D)d^2. For one actual
future difference t=a_r-a_i>0, let K_t be the sum de over its original
strict-core edges covering b. Orient every edge by its larger source
d, so e=d-t. At this fixed t a given d occurs in at most one edge:
e is determined, each source label has unique actual endpoints, and
the actual output pair is unique. For 0<t<H,

    d(d-t) <= (1-t/H)d^2,

because the right side minus the left side is td(H-d)/H>=0.
Summing over the subset of used larger labels gives

    K_t<=S(1-t/H)_+.                                (A28.1)

If t>=H there is no edge, since both positive source labels are at
most H. Thus the positive-part formula includes that case correctly.
This links the oriented boundary loss to the gradient loss; it is
stronger than using only the independent nonnegativity of the two
deficits in A04. It is a genuine original-core upper bound, including
AC and both BH channels. Deleting records also preserves it.

The strict core still implies c>b/log b and
t>L_b:=b^2/(log b)^5. Put the positive integer

    ell=floor(L_b)+1.

For one component k>=b+1, let v=min(k,T), m=v-b>=0 and h=binom(m,2).
The h actual future positive differences are all distinct by Sidon.
The decreasing kernel (1-t/H)_+ with integer t>=ell is maximized by
placing at most h labels consecutively at ell,ell+1,...,H-1. Thus,
with z=min(h,max(0,H-ell)), its EXACT numerical packing bound is

    F_(H,ell)(h)=z(1-ell/H)-z(z-1)/(2H),
    sum_(b<i<r<=v) K_(a_r-a_i) <= S F_(H,ell)(h).   (A28.2)

When ell>=H, z=0 and both the possible core mass and F vanish.
The floor keeps the original strict condition t>L_b; equality is
not admitted. No actual future difference is assigned to two slots.
The formula is an upper packing allowance, not a claim that these
consecutive labels are the difference set of an actual Sidon prefix.

Exact finite interchange of the ORIGINAL genuine prices yields

    P_b^core(M,T) <= S sum_(k=b+1..M) kappa_k/H_k^2
                         F_(H,ell)(binom(min(k,T)-b,2)).  (A28.3)

The k=b+1 term is zero. Components k>T are retained with the same
fixed future set through T. No alpha_(M+1) is reset and no terminal
component is replaced. The repeated appearance of a physical record
at k>=r is exactly its defining component price, not an independent
budget for each k.

One immediate fixed-cap corollary improves the earlier scalar saving.
For b>=m0, H<=Cb^2log(2b). If
A_b=sum_(r=b+2..T)(r-b-1)u_r^[M], then

    P_b <= S A_b
       * (1-1/[C log(2b)(log b)^5])_+.              (A28.4)

This follows directly from A28.1 and t>L_b; it also covers the case
where that positive part is zero and the core must be empty.
For fixed C the saving has order (log b)^(-6), whereas the
gradient-only A04 saving had order (log b)^(-12). Both savings tend
to zero, so neither pointwise consequence controls the target norm.

There is a precise limitation even of the sharper output-packing
formula when actual endpoint geometry is discarded. Variance gives
S<=Sbar_b:=(b-1)^2 H_b^2/4. Let U_b denote the right side of A28.3
with S replaced by Sbar_b. This is a valid actual-profile majorant.
Evaluate this NUMERICAL FORMULA on the scalar diameters

    H_n=n(n-1)/2,  M=T>=3b,  b>=8.

These scalar diameters satisfy all rank packing lower bounds and
the C=1,m0=2 scalar cap. They are NOT an asserted actual Sidon
history and there is no assertion that the corresponding Sbar or
integer output slots are simultaneously realized by actual endpoints.
Since log b>=2,

    ell<=b^2/32+1<=b^2/16<=H_b/4.

For 2b<=k<=3b, h=binom(k-b,2)>=H_b, so
F=(H_b-ell)(H_b-ell+1)/(2H_b)>=H_b/4>=b^2/16.
Also Sbar_b>=b^6/256 and, with the unchanged coefficients,

    kappa_k=4/[k(k^2-1)^2]>=4/k^5,
    1/H_k^2>=4/k^4,
    sum_(k=2b..3b)kappa_k/H_k^2>=16/(3^9 b^8).

Therefore this same new numerical majorant satisfies

    U_b >= 1/(256*3^9),   8<=b<=M/3.               (A28.5)

Its square-root harmonic sum grows on these scalar inputs. This is
a lower bound on a discarded-geometry MAJORANT, not on the actual
profile and not on any fixed-cap Sidon family. It locates the failed
step precisely: integer output uniqueness plus scalar diameter/cap
and variance envelopes still forget how future output labels and old
source endpoints can coexist at all ranks. No counterexample to the
frozen theorem or Q1 follows.

The next input must retain that joint information. An actual future
difference cannot belong to the old positive-difference set D: its
distinct future endpoints would duplicate an old positive difference.
A28.2 relaxed this forbidden-label set as well as the endpoint
correspondence. This gives a concrete additional constraint for the
next estimate without invalidating the present upper bound. Also,
at fixed b,k one can subtract the exact nonnegative output-label deficit

    E_(b,k)=F_(H,ell)(h)
       -sum_(b<i<r<=min(k,T), a_r-a_i>=ell)(1-(a_r-a_i)/H)_+.

It refers to the actual common output bank. An increment/potential
bound for its price-weighted accumulation remains unproved; merely
declaring E>=0 would return A28.3. This is a different object from
the old triple-fiber deficit, whose monotonicity was already refuted.
No monotonicity or decay of this new deficit is assumed.
The full A28 proof and its scalar-majorant limit have passed independent
hand review in `../../evidence/u4f_core/finite_campaign/`; none of A28's
full core/price instantiation is asserted Lean-verified.

## A29. Exact packing with the actual old difference set forbidden

Continue A28's notation at a fixed cut: D is the actual positive
difference set of the first b-1 points, H=H_b, S=sum_D d^2, and
ell=floor(b^2/(log b)^5)+1. The actual future difference set of
the points b+1,...,min(k,T) is disjoint from D. Equality would give
two different actual endpoint pairs with the same positive difference.
This is also the existing source theorem `internalLabels_disjoint`
in `../../lean/Q1/SharedDifferenceBudget.lean`; it is reused, not
recounted as a new supporting theorem or rebuilt as a new library.

Let U be the actual allowed integer set [ell,H-1] minus D, ordered
as u_1<...<u_N. For any integer h>=0 define

    F_D(h)=sum_(r=1..min(h,N))(1-u_r/H).

Empty U gives zero. The SAME allowance has the exact prefix form

    F_D(h)=(1/H)sum_(j=ell..H-1)
                      min(h, |[ell,j] minus D|).         (A29.1)

Indeed 1-u/H counts the integer thresholds j=u,...,H-1, divided by
H. Among the first min(h,N) allowed labels, exactly
min(h,|[ell,j] minus D|) lie below or at j. This proves A29.1 without
assigning an independent allowance to each threshold. For ANY selected
subset of U with at most h labels, the same prefix counts are bounded
by that minimum, so its total kernel mass is at most F_D(h).

The actual future kernel L_(b,k), obtained by summing (1-t/H)_+ over
its actual differences t>=ell, therefore satisfies

    sum_(actual future outputs) K_t <= S L_(b,k)
       <= S F_D(h_k) <= S F_0(h_k),
    h_k=binom(min(k,T)-b,2),                         (A29.2)

where F_0 is A28's allowance with no forbidden set. Finite interchange
with the genuine nonnegative coefficients gives the full bound

    P_b^core(M,T) <= U_b^D
        :=S sum_(k=b+1..M) kappa_k/H_k^2 F_D(h_k).   (A29.3)

All components k>T remain with their fixed output bank. Both S and D
belong to the same actual old points, and no terminal alpha is changed.

For a fixed b and k<T, write m=k-b. Appending point k+1 adds exactly
m actual new future differences, all distinct from the old future
bank and D. If J_(b,k+1) is their eligible kernel mass, the exact
deficit increment for E_(b,k):=F_D(binom(m,2))-L_(b,k) is

    E_(b,k+1)-E_(b,k)
       =F_D(binom(m+1,2))-F_D(binom(m,2))-J_(b,k+1). (A29.4)

There is no sign theorem in this identity. For k>=T the future bank
and h_k are fixed, so this deficit is unchanged, even though genuine
price components continue to be added.

Exactly four cells of the saved C=1,m0=2 variant M96 were checked:
(b,k)=(24,47),(24,48),(25,47),(25,48). Rational logarithm intervals
certify ell=2 at both cuts. At b24 the actual H,S,|D|,|U| are
713,21743814,253,459; at b25 they are773,28686807,276,496.
Both forms of F_D and the whole chain A29.2 pass as exact rational
identities/inequalities, with the same genuine component multiplier.
All selected original core rows retain their strict conditions.

For k47->48, the exact deficit increments are +4179/713 at b24
and +5457/773 at b25. The allowance increments are5216/713 and
6674/773; the actual future-kernel increments are1037/713 and1217/773.
The only new differences with positive eligible kernel in either
case are209,344,549. The exact data are bound by
`../../evidence/u4f_core/finite_campaign/A29_forbidden_output_packing_manifest.json`.
These two positive increments are finite data,
not a proof of general monotonicity. No new history or full-profile
rerun was used.

The generic integer-prefix identity and selected-label upper bound
are newly checked in the supporting Lean module. The full actual
core/price correspondence remains a hand proof. Prior
`../global_route.md` already treats positive decreasing-kernel
relaxations; A29 keeps a rank-dependent ACTUAL forbidden set that
those aggregate inequalities discard. That earlier no-go is not
applied as a counterexample to this stronger actual-label estimate.

## A30. Joint squared-source and forbidden-capacity compression

A29 must not maximize S and future capacity using unrelated old sets.
For the SAME actual D put

    q=|D|=binom(b-1,2),
    a=|D intersect [1,ell-1]|.

If ell>=H, there is no eligible output and A29 is already zero.
Otherwise assume 1<=ell<H. The feasible cardinalities satisfy
0<=a<=ell-1 and 0<=q-a<=H-ell. Define the integer comparison set

    D*=[ell-a,ell-1] union [H-(q-a),H-1],            (A30.1)

with empty intervals allowed. This has exactly the same q and a.
It is an UPPER-BOUND comparison set, not a new actual Sidon history.

Within each of the two layers, pushing the sorted forbidden labels
to the largest available positions increases their squared sum. Thus
S(D)<=S(D*). It also increases EVERY F_D(h) simultaneously: for
ell<=j<H, the smallest possible eligible forbidden prefix count is

    |D* intersect [ell,j]|=max(0,q-a-(H-1-j))
                  <=|D intersect [ell,j]|.

Consequently the allowed prefix counts, hence A29.1 for every h,
are larger for D*. Both factors are nonnegative, so using the same
actual a throughout the genuine component sum gives

    U_b^D <= S* sum_(k=b+1..M) kappa_k/H_k^2 F*(h_k),
    S*=sum_(d=ell-a..ell-1)d^2
                    +sum_(d=H-(q-a)..H-1)d^2,
    F*(h)=z(1-ell/H)-z(z-1)/(2H),
    z=min(h,H-ell-q+a).                              (A30.2)

The allowed labels for D* are the initial interval
[ell,H-q+a-1]. The same comparison works for all nonnegative
component weights and does not maximize a separately at each k.
Moving a forbidden label ACROSS the strict threshold can have the
opposite capacity effect: as a grows, S* can decrease while F* grows.
Thus there is no conclusion that a=0 maximizes their product.

This gives a valid joint envelope, but scalar/cardinality compression
still loses actual endpoint geometry. To see the precise numerical
limitation, evaluate the envelope at the RELAXED data

    H_n=n^2 (n>=2), q=binom(b-1,2), a=0,
    b>=8, M=T>=3b, ell=floor(b^2/log^5 b)+1.

These scalar diameters satisfy packing and the C=1,m0=2 scalar cap.
Here ell<=H/16, q>=b^2/8, H-q>H/2, so S*>=b^6/32.
For 2b<=k<=3b, h_k>=b^2/4, and the allowed interval has length
H-ell-q>=7H/16. Its first floor(H/4) labels each have kernel at
least1/2, and floor(H/4)>=H/8. Therefore F*(h_k)>=H/16.
Since sum_(k=2b..3b)kappa_k/H_k^2>=4/(3^9 b^8), the numerical
envelope in A30.2 is at least

    1/(128*3^9).                                    (A30.3)

No actual D or history is asserted by this calculation. In fact this
D* cannot be the difference set of even three old points: all its
labels exceed H/2, whereas three ordered points give positive
differences u,v,u+v<=H. Its compatibility with the sharper old span
H_(b-1), nesting across b, and all actual endpoint equations has also
been discarded. A30.3 is a diagnostic of the relaxed envelope, not
a counterexample to A29, actual profile boundedness, U4-F, or Q1.
It identifies a specific next input: actual short old differences
forced by additive endpoint geometry, rather than arbitrary integer
forbidden sets with the same cardinalities.
The independent proof and limitation review is
`../../evidence/u4f_core/finite_campaign/A30_FIXED_STRATUM_FORBIDDEN_COMPRESSION_REVIEW.md`.

## A31. Actual sliding intervals force a quantitative forbidden-label loss

Let the n=b-1 actual old points be translated into [0,H0], with
H0=H_(b-1). For an integer y>=1 and every integer shift
z in [1-y,H0], let f_z count old points in [z,z+y-1]. These shifts
form an AMBIENT interval of cardinality H0+y; some f_z may be zero.
Each point lies in exactly y such intervals, and each actual pair
with positive difference d<y lies in exactly y-d. Sidon uniqueness
allows the unordered pairs to be indexed by D exactly once. Hence

    sum_z f_z=ny,
    sum_z f_z^2=ny+2G_D(y),
    G_D(y):=sum_(d in D,d<y)(y-d).

Cauchy on this ambient shift interval, including its zero windows,
proves the actual endpoint estimate

    G_D(y)>=(1/2)(n^2 y^2/(H0+y)-ny).              (A31.1)

This corrects the possible mistaken phrase "the nonzero support has
size H0+y"; only its ambient container has that size. The formula
and denominator above use the container, so no support equality is
assumed. This finite proof is independent of Q1 or prefix existence.

Write F_0 for the no-forbidden allowance and F_D for A29. If
ell<=y<=ell+min(h,H-ell), their exact prefix representation gives

    F_0(h)-F_D(h)
       >=(1/H)sum_(d in D,ell<=d<y)(y-d)
       >=[G_D(y)-(ell-1)y]/H.                       (A31.2)

For the first inequality keep only integer thresholds ell<=j<y:
their total available slot count is at most h, so the two minima
differ by exactly the forbidden prefix count there. Interchanging
that finite sum counts a forbidden d exactly y-d times. The second
inequality removes at most ell-1 distinct positive labels below ell,
each contributing at most y. Thresholds are not separate budgets.

There is an explicit noncircular fixed-cap consequence. Suppose

    b>=max(8,m0),   h>=binom(b,2),
    b>=768 C log(2b),
    (log b)^5>=1536 C log(2b).                      (A31.3)

For fixed C>0 these are eventual scalar conditions independent of
any capped-history existence. For example they hold when, in addition
to b>=max(8,m0), log b>=max(2,3072C,(3072C)^(1/4)).
Indeed log(2b)<=2log b, and exp(u)>=u^2/2 for u>=0.

Choose y=floor(b^2/8). Then n>=b/2, y>=b^2/16, H>=b^2/4,
ell<=b^2/16<=y and y<=h,H/2. Thus A31.2 applies. The original cap
gives H0+y<=H+y<=3H/2<=3Cb^2log(2b)/2, whence

    n^2y^2/[2(H0+y)]>=b^4/[3072 C log(2b)].

The two subtractions ny/2<=b^3/16 and
(ell-1)y<=b^4/[8(log b)^5] are each at most one quarter of this
last main lower bound, by A31.3. Dividing the remainder by H and
using the same cap yields the actual forbidden-capacity saving

    F_0(h)-F_D(h)>=b^2/[6144 C^2(log(2b))^2].      (A31.4)

For all k>=2b with T>=2b, h_k=binom(min(k,T)-b,2) meets its
cardinality premise. The SAME lower saving can be inserted in the
exact genuine sum. Define
U_b^0=S sum_k kappa_k/H_k^2 F_0(h_k) and U_b^D as in A29.
If also M>=3b, the intermediate-rank cap is used at EVERY
k=2b,...,3b. Since

    S>=q^3/3>=b^6/1536,
    sum_(k=2b..3b)kappa_k/H_k^2
                 >=4/[3^9 C^2 b^8(log(6b))^2],

finite multiplication gives

    U_b^0-U_b^D
       >=1/[2359296*3^9 C^4(log(2b))^2(log(6b))^2].  (A31.5)

The first line uses the q distinct positive old labels and
q=binom(b-1,2)>=b^2/8. The second uses
kappa_k=4/[k(k^2-1)^2]>=4/k^5 and the unchanged cap at those k.
All terminal components are retained; this is a lower bound on a
selected finite part of their positive sum. A31.5 also applies when
2b<=T<3b: its actual future bank is fixed after T but its genuine
component prices through3b still remain.

This is an actual Sidon/endpoint/fixed-cap input, not an assertion
about the non-Sidon comparison set D*. It proves positive savings
between two valid upper bounds; it is NOT a lower bound for P_b.
The guaranteed scalar LOWER BOUND in A31.5 tends to zero, of order
(log b)^(-4) at fixed C; the actual saving is not asserted to have
that asymptotic size. Subtracting only this guaranteed lower bound
from the existing constant profile
envelope still leaves a positive limiting constant. Thus it does
not yet give a summable square-root profile or the missing K(C,m0).
The full G_D(y), its actual rank evolution and price-weighted
accumulation contain information discarded by this final scalar step.
The independent proof, ambient-container correction and constant review
are saved in
`../../evidence/u4f_core/finite_campaign/A31_ACTUAL_SLIDING_WINDOW_HOLE_BOUND_REVIEW.md`.

## A32. Actual mixed labels and failure of immediate full payment

Fix b, H=H_b and the unchanged integer threshold ell=floor(b^2/log^5 b)+1.
Let D be the positive difference set of the first b-1 points and
S=sum_D d^2, as before. For the forbidden bank only, take the larger
past P consisting of the first b points, and future F_v with ranks
b+1,...,v, where v=min(k,T). Define

    B_v=Delta(P) union {a_f-a_p:p<=b<f<=v},
    U_v={ell,...,H-1} minus B_v,
    h_v=binom(v-b,2), phi(t)=1-t/H,
    F_U(h)=sum of the min(h,card U) largest phi weights in U.

All past-internal, mixed, and future-internal positive labels are
pairwise disjoint by actual Sidon uniqueness. With L_v the sum of
phi(t) over actual future-internal labels ell<=t<H, and Q_bk the
original strict-core component sum of de, A28's source bound gives

    Q_bk<=S L_v<=S F_{U_v}(h_v)<=S F_D(h_v).          (A32.1)

The source S still uses the original first b-1 points. No extra source
records are created by using the cut point b in the forbidden bank.

When the future endpoint v+1 enters, put m=v-b, h=h_v, h'=h+m.
There are b fresh mixed labels and m fresh future-internal labels.
Each new mixed label exceeds every new future-internal label, since
their lower endpoints satisfy p<=b<i. Let C be the eligible new mixed
labels lying in U_v, so U_{v+1}=U_v minus C. Define

    A_v=F_{U_v}(h')-F_{U_v}(h),
    R_v=F_{U_v}(h')-F_{U_{v+1}}(h'),
    J_v=L_{v+1}-L_v, E_v=F_{U_v}(h)-L_v.

All A_v,R_v,J_v are nonnegative, and exactly

    E_{v+1}-E_v=A_v-R_v-J_v.                        (A32.2)

Deleting C from an old maximizing set leaves a feasible new set.
Consequently 0<=R_v<=sum_{c in C}phi(c). The reverse inequality,
which would allow immediate full mixed-label charging, is FALSE.

Independent exact checks use only the existing fixed C=1,m0=2,M=T=96
variant, at b=24,25 and v=29,30,47,48. All eight chains A32.1 and four
identities A32.2 pass, retaining original strict gates and genuine
component coefficients; unresolved strict comparisons are zero.
At the step29->30 the exact counterexamples are

    b=24: H=713, C={547,608,657}, R=0<327/713=sum_C phi,
    b=25: H=773, C={487,547,608,657,721}, R=0<845/773=sum_C phi.

These new forbidden labels lie outside the selected capacity slots.
The four observed deficit increments, respectively29->30 and47->48,
are +912/713,+3250/713 at b24, and +562/773,+4768/773 at b25.
They do not prove deficit monotonicity for general actual histories.
For components k>T the bank is fixed, but the genuine prices continue.

Evidence: `../../evidence/u4f_core/finite_campaign/` contains
`A32_joint_forbidden_eight_cells_exact.json`, its minimal reference
script, and `A32_JOINT_FORBIDDEN_EIGHT_CELL_REVIEW.md`, hash-bound in
`A32_A34_review_manifest.json`. No new history or broad scan was made.
This rejects one concrete charging inequality, not CoreUniform or Q1.

## A33. A uniformly summable far-component part of the original profile

Fix a real p>1 once, independently of C,m0,M,T,b. For 3<=b<T<=M,
partition the ORIGINAL positive component prices, defining

    PFar_b=sum_{k=b+2}^M 1[H_k>=H_b(log b)^p]
                            kappa_k Q_bk/H_k^2,
    PNear_b=sum_{k=b+2}^M 1[H_k< H_b(log b)^p]
                            kappa_k Q_bk/H_k^2.

Thus P_b=PNear_b+PFar_b exactly. This classifies component rank k,
not just output rank r. An early output may retain later far price
components. For k>T, Q_bk is frozen at output horizon T and the
component tail remains present through M.

The actual source-edge bound and number of distinct future outputs give
Q_bk<=S_b binom(min(k,T)-b,2). Nonnegativity and the far condition yield

    PFar_b<=S_b/[H_b^2(log b)^(2p)]
                     sum_{k=b+2}^M kappa_k binom(k-b,2).

A27's exact finite Abel formula, with the terminal alpha unchanged, is

    sum_{k=b+2}^M kappa_k binom(k-b,2)
     =sum_{r=b+2}^M alpha_r(r-b-1)
                       -binom(M-b,2)alpha_{M+1}<=1/(6b^2).

The old-point variance identity gives
S_b<=(b-1)^2 H_{b-1}^2/4<=(b-1)^2 H_b^2/4. Consequently

    PFar_b<=(b-1)^2/[24 b^2(log b)^(2p)],
    sum_{b=3}^{T-1}sqrt(PFar_b)/b
       <=(log 2)^(1-p)/[sqrt(24)(p-1)].              (A33.1)

The last inequality compares the decreasing function1/[x(log x)^p]
with its integral from2 to infinity. It is a numerical upper bound
for each finite actual sum, not an assumption of an infinite capped
history. The b2 core is empty. In particular p=2 gives the absolute
constant1/[sqrt(24)log2], without using the cap.

For b>=m0, the fixed cap at b and integer Sidon packing show that
each remaining near component satisfies

    k(k-1)<2C b^2 log(2b)(log b)^p,
    k<1+sqrt(2C)b sqrt(log(2b))(log b)^(p/2).        (A33.2)

Indeed k(k-1)/2<=H_k<H_b(log b)^p. There is no altered cap, cutoff
or terminal price in this deduction. For p2 the remaining rank strip
has the displayed factor log b sqrt(log(2b)); it is not a fixed-ratio
rank strip.

An exact useful reduction now pays the original small-old-gap records
by A12, the large-gap far components by A33.1, and the finitely many
cuts3<=b<m0 by A02 with cost at most
(1/sqrt(24))sum_{b=3}^{m0-1}1/b. The square-root triangle inequality
then leaves only all-three-old-gaps-large records, b>=max(3,m0), and
near components at p2. Conversely this remainder is pointwise bounded
by the full original profile. Its uniform norm is still unproved; the
reduction does not redefine the frozen statement or establish its K.

The independent hand review is `A33_FAR_COMPONENT_UNIFORM_REVIEW.md`.
The generic denominator step is formalized as
`priced_component_far_bound` in the supporting Lean module. The full
Sidon/Abel/integral theorem A33.1 and the near reduction are not claimed
Lean-verified. No Q1 or maximum-prefix premise is used.

## A34. Exact deferred deletion penalties, with a finite payment threshold

At a fixed cut put U_0={ell,...,H-1} minus Delta(first b points).
List each eligible actual mixed label c_i once, in increasing future
birth f_i and then increasing past endpoint rank. Define sequential
sets U^i=U_0 minus {c_1,...,c_i}. Sidon uniqueness makes each c_i a
member of its pre-deletion set U^{i-1}. Let N_i=card U^{i-1}, let r_i
be its ascending rank there, and w_1>=...>=w_{N_i}>0 the phi weights.
For any integer capacity h>=0 set

    p_i(h)=F_{U^{i-1}}(h)-F_{U^i}(h).

Deleting an unselected label changes nothing. Deleting a selected
label replaces it by the old next label, if any. Therefore exactly

    p_i(h)=0                         if h<r_i,
    p_i(h)=w_{r_i}-w_{h+1}            if h>=r_i,    (A34.1)

where w_{h+1}=0 for h>=N_i. Hence p_i is nondecreasing,
0<=p_i(h)<=phi(c_i), with equality to phi(c_i) when h>=N_i.
Same-birth labels use their own sequential pre-deletion sets, not a
single unchanged bank for the whole batch.

Write d_v for the number of deletions with f_i<=v and use U_v for the
corresponding horizon bank. At one common capacity, telescoping gives

    F_{U_0}(h_v)-F_{U_v}(h_v)=sum_{i<=d_v}p_i(h_v).

For h'=h_v+(v-b), define A_0=F_{U_0}(h')-F_{U_0}(h_v). With A_v,R_v,J_v
as in A32, one has the exact deferred growth decomposition

    g_v=A_0-A_v=sum_{i<=d_v}[p_i(h')-p_i(h_v)]>=0,
    R_v=sum_{d_v<i<=d_{v+1}}p_i(h')>=0,
    Delta F_joint=A_0-g_v-R_v,
    Delta E=A_0-g_v-R_v-J_v.                       (A34.2)

The baseline loss has nonnegative increment g_v+R_v, but this gives
no sign for Delta E. A32's zero immediate payment can be followed by
positive deferred increments. A finite horizon need not reach them.

For both horizons retain h_k=binom(min(k,T)-b,2) and the original
lambda_k=kappa_k/H_k^2. Exact finite interchange gives

    sum_{k=b+1}^M lambda_k[F_{U_0}(h_k)-F_{U_min(k,T)}(h_k)]
      =sum_{i:f_i<=T} Pi_i,
    Pi_i=sum_{k=f_i}^M lambda_k p_i(h_k).          (A34.3)

Multiplying by the same S_b in A32 yields an original-profile upper
bound equal to its U_0 baseline minus S_b sum_i Pi_i. No label is
charged twice at this cut. Components k>T keep the final bank/capacity
but still carry their genuine coefficients.

For one label define d_i=min{m>=0:binom(m,2)>=N_i}, k_i=b+d_i.
If explicitly T>=k_i and f_i<=T, then r_i^*=max(f_i,k_i)<=T and

    Pi_i>=phi(c_i)u_{r_i^*}^{[M]}.                 (A34.4)

For every k>=r_i^*, min(k,T)-b>=d_i, so A34.1 is full; dropping only
earlier nonnegative penalties proves the claim. The auxiliary index
r_i^* is not a replacement of any physical output rank. Neither
alpha_{M+1} nor u_M is changed. Without T>=k_i this conclusion is
not available.

There is also one simultaneous actual-prefix threshold. For b>=8 put
J_b=ceil(4sqrt(H_b)). Every eligible mixed c=a_f-a_p<H_b, p<=b,
satisfies H_f=c+H_p<2H_b. Integer Sidon packing implies
f<1+2sqrt(H_b)<=J_b. Also H_b>=b(b-1)/2>=b^2/4, so

    J_b-b>=2sqrt(H_b),
    binom(J_b-b,2)>=2H_b-sqrt(H_b)>=H_b>=N_i.

If T>=J_b (and thus J_b<=M), all eligible labels have appeared and
all their penalties have reached full weight by J_b; no eligible
mixed labels can appear later. This assumes only the stated finite
prefix, not the existence of any further extension.

For b>=max(10,m0,C), log b>=150C, the cut cap gives H_b<=b^4.
Since J_b<=5sqrt(H_b), the cap at the actual rank J_b gives

    H_{J_b}<=25 C H_b log(10sqrt(H_b))
            <=75 C H_b log b<=H_b(log b)^2/2
            <H_b(log b)^2.                        (A34.5)

Here log(10sqrt(H_b))<=3log b uses b>=10. The cap at J_b is used
ONLY under T>=J_b<=M. Monotonicity of H_k shows that all components
k<=J_b are in A33's p2 near class. Thus full mixed penalties arrive
within that near class whenever the stated size/horizon conditions
hold. This does not evaluate their common sum across different cuts.
The short-horizon case T<J_b is not covered.

The independent hand review, including A34.4 and A34.5, is
`A34_DEFERRED_DELETION_PENALTY_REVIEW.md`, with the same source binding
as A32/A33. These identities are not Lean-verified. A single physical
mixed pair can appear at several cuts with different H, ell and ranks;
assigning independent allowances to those occurrences is unjustified.
The next mathematical obligation is to control that shared cut sum
and to evaluate the unsaturated short-horizon case, keeping Q_bk and
the original source/output correlations. Neither K nor Q1 follows
from the fixed-cut identities alone.

## A35. Exact short-horizon price and the unsaturated-cut obstruction

For 3<=b<T<=M keep the output horizon in the finite Abel transform:

    sum_{k=b+2}^M kappa_k binom(min(k,T)-b,2)
      =sum_{r=b+2}^T (r-b-1)alpha_r
                          -binom(T-b,2)alpha_{M+1}. (A35.1)

For k>=T the capacity is constant, and its remaining genuine tail is
included in the terminal term. Equivalently monotonicity of alpha and
nonnegativity bound this sum by alpha_{b+2}binom(T-b,2).
Using the actual Q_bk bound and H_k>=H_b then gives

    P_b(M,T)<=(b-1)^2(T-b)(T-b-1)
                     /[8(b+2)^2(b+1)^2].          (A35.2)

This is stronger than the proposed denominator8b^2(b+1)^2 bound.
It holds for the entire original core and needs no cap. For each fixed
delta>0 the cuts b>=delta T have a uniform norm bound. For example,
with B=max(3,ceil(delta T)), A35.2 implies

    sum_{b=B}^{T-1}sqrt(P_b)/b
       <=T/sqrt(8) sum_{b=B}^infinity 1/b^2
       <=T/[sqrt(8)(B-1)]<=1/(sqrt(2)delta),

when the cut set is nonempty. The last step uses B-1>=B/2 and
B>=delta T. This does not cover all A34-unsaturated cuts with a
single fixed delta.

Indeed, because T is an integer, T<ceil(4sqrt(H_b)) is equivalent to
T<4sqrt(H_b), hence H_b>T^2/16. For b>=m0 the fixed cut cap forces

    16C b^2 log(2b)>T^2,
    b>T/[4sqrt(C log(2T))].                        (A35.3)

This is a necessary support condition, not an existence assertion.
Using A02's P_b<=1/24 on this support yields only

    sum_{b<T, T<J_b}sqrt(P_b)/b
      <=K_initial(m0)
        +(1/sqrt(24))[1/2+log_+(4sqrt(C log(2T)))], (A35.4)

where K_initial=(1/sqrt(24))sum_{b=3}^{m0-1}1/b and empty ranges
are zero. The numerical harmonic envelope on the right grows like
log log T. Replacing the threshold in A35.3 by a fixed fraction of T,
or replacing that envelope by a constant, is the specific unjustified
step that would falsely pay all short horizons. Neither the envelope
nor A35.2 is an actual profile lower bound. This attack proves the
finite price identity and a uniform terminal-strip estimate, but its
cap/support relaxation fails to close the remaining norm.

The independent hand review is `A35_SHORT_HORIZON_COMPONENT_REVIEW.md`.
No new finite history, computation or Lean theorem is claimed here.
The missing input is the common actual cut dependence of source/output
correlations or mixed penalties, beyond the single-cut support bound.

## A36. One physical mixed pair has an exact cut law

Fix a positive mixed label c=a_f-a_p, and cuts p<=b<b+1<f. For this
section first fix one integer threshold ell>=1, with ell<=c<H_b.
The A34 canonical bank just before deleting this particular label is
the interval{ell,...,H_b-1} with the following physical labels removed:

    D_b^-={a_y-a_x:1<=x<=b, x<y<f}
                union {a_f-a_q:1<=q<p}.           (A36.1)

The first set combines all past-internal labels with mixed labels of
earlier future birth. The second consists exactly of earlier same-birth
labels in canonical order. Intersecting with the interval discards
ineligible labels, so listing all these pairs makes no change. Actual
Sidon uniqueness makes the two sets disjoint and excludes c itself.

When b advances by one, the old pairs ending at b+1 were already in
D_b^-. The only new forbidden pairs are

    G_b={a_y-a_{b+1}:b+1<y<f},
    D_{b+1}^-=D_b^- disjoint-union G_b,
    card G_b=f-b-2.                               (A36.2)

Write A_b(x)=card({ell,...,x} minus D_b^-) for x<H_b, and fix one
output horizon v>=f. Put h_b=binom(v-b,2). The deletion penalty p_b
for this pair is the A34 penalty at this capacity. The integer prefix
formula proves the exact unnormalized identity

    H_b p_b=sum_{x=c}^{H_b-1}1[A_b(x)<=h_b].       (A36.3)

For x<c deletion has no effect. For x>=c, the occupancy drops from
A_b(x)>=1 to A_b(x)-1. The difference of the two minima with h_b
is1 precisely when A_b(x)<=h_b. This includes full capacity, h_b=0,
and a label at the last allowed position. The supporting Lean theorem
`integer_capacity_deletion_identity` proves this generic integer
prefix-minimum step, before real normalization or Sidon instantiation.

On the common interval c<=x<H_b, define Z_b(x)=A_b(x)-h_b as an
integer. Since h_{b+1}=h_b-(v-b-1), A36.2 yields

    Z_{b+1}(x)=Z_b(x)+(v-b-1)-card(G_b intersect[ell,x])
                 >=Z_b(x)+(v-f+1)>Z_b(x).         (A36.4)

Thus the payment indicator cannot increase on the common interval.
If p_b<1-c/H_b, at least one prefix, and therefore the final prefix
x=H_b-1, has Z_b(x)>0. The new final common prefix remains positive.
All further prefixes up to H_{b+1}-1 then have positive Z as well,
so the new span contributes no additional payment. It follows that

    H_{b+1}p_{b+1}<=H_b p_b  whenever p_b<1-c/H_b.

In the remaining case the old payment is full. Define its fraction of
the full eligible-label weight by

    rho_b=p_b/(1-c/H_b)=H_b p_b/(H_b-c).

In the nonfull case the numerator does not increase and its positive
denominator increases. In the full case rho_b=1 and rho_{b+1}<=1.
Consequently, for every such physical pair and fixed v,

    0<=rho_{b+1}<=rho_b<=1.                        (A36.5)

Neither p_b, H_b p_b nor S_b p_b is asserted nonincreasing in the
full case. They can increase in actual fixed-cap histories.

The exact finite test uses only pair(p,f)=(24,30), c=547, in the
existing C=1,m0=2,M=96 variant. The original threshold is ell_b=2
at all six cuts24..29, verified with no UNKNOWN comparisons. At
v47,48 all twelve penalties are zero. The permitted six extra cells
at v60 give the strict counterexample at b24->25:

    p:166/713 ->226/773, increase32820/551149,
    H p:166 ->226,
    S p:3609473124/713 ->6483218382/773,
                    increase1832411981514/551149.

At b26->27, p and H p both decrease but S p increases. Thus even
restricting attention to a decreasing raw penalty does not establish
source-weighted monotonicity. The corresponding relative fractions
at v60 for b24..29 are

    1, 1, 1, 69/94, 307/511, 270/683.

All eighteen cells and the closed pre-deletion bank were independently
checked exactly. The same genuine component coefficient at k60 is
1/10659568914462735. No new history or broad profile scan was made.
This is a counterexample to the three stated monotonicity candidates,
not to the frozen K or Q1.

For the moving original threshold, if ell_{b+1}>=ell_b and the label
is eligible at both cuts, put
L_b=card([ell_b,ell_{b+1}-1] minus D_b^-). The exact common-prefix
law becomes

    Z_{b+1}(x)=Z_b(x)+(v-b-1)-L_b
                           -card(G_b intersect[ell_{b+1},x]).

Hence the same monotonicity argument works if L_b<=v-f+1; it is not
unconditional for moving thresholds. A37 below removes this technical
threshold movement at a uniformly bounded allowance cost, while leaving
every original core condition unchanged.

## A37. Removing the auxiliary integer threshold has uniformly bounded cost

Keep the actual joint past/mixed forbidden bank B_v from A32. At fixed
b,k let F^1_{b,v}(h) use allowed integers{1,...,H_b-1} minus B_v, and
let F^ell_{b,v}(h) use{ell_b,...,H_b-1} minus the same bank, where
ell_b=floor(b^2/log^5 b)+1. In both cases the capacity is the actual
h=binom(min(k,T)-b,2), and the weight is1-t/H_b. Inclusion and deleting
at most ell_b-1 extra labels give

    0<=F^1_{b,v}(h)-F^ell_{b,v}(h)<=ell_b-1.

Define the two original-price upper allowances

    U^a_b=S_b sum_{k=b+2}^M kappa_k/H_k^2 F^a_{b,min(k,T)}(h_k),
                                                     a=1,ell.

Nonnegativity, H_k>=H_b, and the UNCHANGED finite price tail imply

    0<=U^1_b-U^ell_b
      <=(S_b/H_b^2)(ell_b-1)(alpha_{b+2}-alpha_{M+1})
      <=(b-1)^2 b^2/[4(b+2)^2(b+1)^2(log b)^5]
      <=1/[4(log b)^5],                           (A37.1)

for b>=3. This also handles ell_b>=H_b, since it remains an upper
bound for the number of added labels. Summing square roots gives

    sum_{b=3}^{T-1}sqrt(U^1_b-U^ell_b)/b
       <=1/[3(log 2)^(3/2)].                      (A37.2)

The proof compares1/[2x(log x)^(5/2)] with its integral from2 to
infinity. It uses no cap or infinite-history existence premise.
Thus the two allowance norms differ by at most this absolute constant,
using sqrt(x+y)<=sqrt(x)+sqrt(y). A uniform bound for either allowance
is equivalent to one for the other up to this explicit additive cost.

These are auxiliary upper allowances. The actual profile satisfies
P_b<=U^ell_b<=U^1_b, but a uniform norm for P has not been shown to
imply a uniform allowance norm. The allowance route remains a sufficient
condition for the frozen theorem. No original record, strict gate,
genuine coefficient, terminal alpha, C or m0 was changed. This result
permits the fixed threshold1 in A36/A38 without a growing error.

## A38. Genuine mixed-pair payments form one shared interval measure

Use threshold1 as justified by A37. Fix the actual physical pair
(p,f), c=a_f-a_p, with f<=T. Its eligible cuts are exactly

    {b:p<=b<f, H_b>c}={L,...,f-1},

when nonempty, where L is the minimum WITHIN p<=b<f. If the set is
empty its whole contribution is zero; L is not assigned the value f.
For the original cut sum b>=3, replace L by max(3,L), with the same
empty-range convention.

For each eligible b use the same canonical deletion as A36 and put

    lambda_k=kappa_k/H_k^2,
    Pi_b(p,f)=sum_{k=f}^M lambda_k p_b(h_{b,min(k,T)}),
    A_b(p,f)=Pi_b(p,f)/(1-c/H_b)
            =sum_{k=f}^M lambda_k rho_{b,min(k,T)}. (A38.1)

Every component in this sum has min(k,T)>=f. A36 applies to each,
and lambda_k is the SAME nonnegative number at every cut. Hence

    0<=A_{b+1}(p,f)<=A_b(p,f)<=u_f^[M].            (A38.2)

This is genuine-price monotonicity after division by the full label
weight; it is not source-weighted monotonicity. Define one measure
on terminal cuts by

    delta_t=A_t-A_{t+1}  (L<=t<f-1),
    delta_{f-1}=A_{f-1}.

All masses are nonnegative, and exactly

    A_b=sum_{t=b}^{f-1}delta_t,
    sum_{t=L}^{f-1}delta_t=A_L<=u_f^[M].           (A38.3)

Consequently finite interchange gives, for any nonnegative cut weights
w_b, the exact single-pair coverage identity

    sum_{b=L}^{f-1}w_b A_b
       =sum_{t=L}^{f-1}delta_t sum_{b=L}^t w_b.    (A38.4)

In particular choose w_b=S_b(1-c/H_b)/b. The left side is precisely
the original-price harmonic deletion loss of this physical mixed pair.
Its several cut appearances are represented by one positive mixture
of prefix intervals, with total mass at most the single u_f^[M].
They are not independent per-cut allowances. The measure depends on
the actual history and both horizons; for k>T the capacity stays
frozen at T and prices continue to M. The index f is the mixed birth,
not a substituted physical output rank, and alpha_{M+1} is unchanged.

More explicitly, let U^past_b be the threshold1 allowance excluding
only past-internal labels, and U^joint_b=U^1_b that also excludes all
mixed labels through min(k,T). A34 finite telescoping and A38 give

    sum_b (U^past_b-U^joint_b)/b
      =sum_{p<f<=T} sum_{t=L}^{f-1}delta_t(p,f)
                    sum_{b=L}^t S_b(1-(a_f-a_p)/H_b)/b. (A38.5)

Empty eligible ranges are omitted. This is an exact linear loss
representation. It does not by itself bound the remaining baseline
minus loss or the square-root norm. In particular A36's actual example
shows why nonincreasing A_b cannot be promoted to nonincreasing
S_b Pi_b. Summing the u_f budgets while discarding their locations and
their source/output correlations is not a proved uniform estimate.

A36--A38 have independent mathematical review. A36 additionally has
eighteen exact finite checks and one generic integer-deletion Lean
lemma. The full cut monotonicity, A37 allowance/integral bound, and
A38 actual genuine-price measure are not yet Lean-verified.

## A39. A strict record can have no eligible mixed label at either output

The next local charging candidate asserted that a strict-core record
must have an eligible mixed label among the eight pairs joining its
two output endpoints to its four old endpoints. It is FALSE, even in
the already certified fixed C=1,m0=2,M=T=96 variant.

Use the existing A24 birth record with old quadruple(1,6,20,24),
matching type3, output(i,r)=(42,43), cut b25, component k48. Its exact
oriented source data are

    d=a24-a1=713, e=a20-a6=422,
    t=a43-a42=d-e=291, de=300886>0.

The actual diameters satisfy H25=773 and H42=2974>2H25. The mixed
labels to old ranks1,6,20,24 are, respectively,

    output42: 2974,2956,2534,2261,
    output43: 3265,3247,2825,2552.

All exceed H25, so their local eligible kernel mass is exactly zero,
even at threshold1. The original strict record has positive genuine
component contribution300886/1148518878296832 at k48. Its full u43
also retains all original components; none is replaced by this one
component. The saved exact core certificate and source binding are
reused for this one record, without scanning other records or creating
a new history.

For any original record d=a_y-a_x>e=a_z-a_w and t=a_r-a_i=d-e,
define the actual mixed labels

    U=a_r-a_y, V=a_i-a_x. Then V-U=e.             (A39.1)

In this example U=2552,V=2974 and V-U=422. The useful correlation
persists although both individual labels are outside the eligible
forbidden-output interval. In general H_i>=2H_b suffices to put all
eight labels outside that interval because every old endpoint has
diameter at most H_b. The counterexample therefore rejects a specific
localization of charging to this record's two output endpoints. It
does not show that the whole mixed bank has zero loss, and it is not
a counterexample to A38, the frozen K, or Q1.

Evidence and review are in `A39_LOCAL_MIXED_RECORD_OBSTRUCTION_REVIEW.md`
and `A39_A40_review_manifest.json` under the finite campaign directory.

## A40. Actual cross-label recovery uniformly pays distant rank components

This attack uses the correlation A39.1 even when individual mixed
labels are too large for A38's eligible kernel. Put n=b-1,
v=min(k,T), m=v-b, H=H_b, and let D be the positive difference set
of the first n points. At one fixed e in D its ordered old source
pair(w,z) is unique by Sidon. Every original oriented record using e
maps to the actual mixed label U=a_r-a_y, with

    V=U+e=a_i-a_x.

There are exactly nm mixed labels between old ranks1..b-1 and future
ranks b+1..v, all distinct by actual Sidon. The value U recovers(y,r),
the value U+e recovers(x,i), and e recovers(w,z). Thus this map is
injective on the FULL original strict-core records with smaller source
label e. The output orientation i<r and larger-source orientation
d>e are retained, so no additional orientation factor is introduced.
All other strict gates only reduce the set. Since d<=H,

    Q_bk<=H n m sum_{e in D}e.                    (A40.1)

For the actual n ordered old points the exact adjacent-gap expression
is

    sum_{e in D}e
      =sum_{j=1}^{n-1}j(n-j)(a_{j+1}-a_j)
      <=floor(n^2/4)H_{b-1}<=n^2 H/4.

Each physical positive difference appears once. Consequently

    Q_bk<=(b-1)^3 (min(k,T)-b)H_b^2/4.            (A40.2)

This is a linear-future-size bound for the entire original core, not
only BH or a source-orientation subset. Its Sidon recovery step is
formalized by `mixed_shift_fiber_card_bound`: for separated old/future
finite sets in the unchanged literal Sidon set, the number of ordered
rectangles y+i=x+r+e is at most old.card*future.card. The full original
six-endpoint record injection, de weighting and rank summation remain
in the reviewed hand proof.

Fix a real p>2/3 once and define R_b=ceil(b(log b)^p)+1 for b>=3.
Thus R_b>=b+2 and R_b-1>=b(log b)^p. Retain the original component
prices and define P_rankfar_b by selecting precisely k>=R_b. If M<R_b
this component sum is empty. Otherwise H_k>=H_b and A40.2 give

    P_rankfar_b<=(b-1)^3/4 sum_{k=R_b}^M kappa_k(k-b).

For R=R_b the exact finite tail identity is

    sum_{k=R}^M kappa_k(k-b)
       =(R-b)alpha_R+sum_{k=R+1}^M alpha_k
                                  -(M-b)alpha_{M+1}. (A40.3)

The first term is at most(R-1)^(-3); A02's coefficient telescope
bounds the remaining numerical tail by1/(3R^3). Therefore

    P_rankfar_b<=1/[3(log b)^(3p)],
    sum_{b=3}^{T-1}sqrt(P_rankfar_b)/b
       <=(log2)^(1-3p/2)/[sqrt3(3p/2-1)].          (A40.4)

The last step integrates1/[sqrt3 x(log x)^(3p/2)] from2 to infinity.
This numerical tail bound assumes no infinite actual history. The
fixed cap is not needed for A40.1--A40.4. For k>T the original output
bank remains fixed at T and all subsequent genuine coefficients are
retained. Replacing min(k,T) by k occurred only in an upper bound;
alpha_{M+1} was never reset.

In particular fix p=3/4. The absolute norm cost is

    8/[sqrt3(log2)^(1/8)],

and the remaining component ranks satisfy

    k<ceil(b(log b)^(3/4))+1.                     (A40.5)

Together with A12 and A33, one may partition nonnegative original
components by first paying small-old-gap records, then large-gap far
span components, then the remaining far rank components by A40. The
finite initial cuts below m0 are paid by A02. The remaining original
core has all three old gaps large, b>=max(3,m0), H_k<H_b(log b)^2,
and A40.5. The square-root triangle inequality makes this a valid
sufficient reduction. It does not assume or prove a uniform norm for
the remainder, or turn an existence-K statement into a completed Q1.

The independent review is `A40_ACTUAL_CROSS_LABEL_RANK_TAIL_REVIEW.md`.
Its proof specifically checked recovery of every physical oriented
record and the finite tail coefficient. No new finite experiment was
run for A40. The full weighted subclass theorem is not Lean-verified.

## A41. Strict mixed-shift paths, fixed-cap length, and the terminal-budget limit

Fix b, v=min(k,T), n=b-1, m=v-b and one actual old difference
e=a_z-a_w. On the nm distinct mixed labels a_r-a_y, old y<=b-1,
future b<r<=v, direct an edge U->U+e whenever both labels occur.
There are exactly m same-future edges: for each future r they join
a_r-a_z to a_r-a_w. This follows from the unique old representation
of e. These forced edges are not original strict-core records.

For a core edge U=a_r-a_y -> V=a_i-a_x one has

    a_y-a_x=e+(a_r-a_i), x<y, i<r.

Both old and future ranks strictly decrease along the edge. The
six-endpoint condition excludes old rows w,z from every core vertex.
Since a numeric label has at most one predecessor and one successor
at shift e, the strict graph is a disjoint union of directed paths,
with at most(n-2)m vertices. It is not assumed to be a matching.

For one nontrivial path of L edges, write D_path and T_path for its
old and future numerical endpoint spans. Telescoping gives exactly

    sum_edges d=D_path=L e+T_path.                (A41.1)

Every output gap is at least the unchanged
ell_b=floor(b^2/log^5 b)+1. Thus, whenever the graph is nonempty,
n>=4,m>=2 and

    L<=Lmax=min(n-3,m-1,floor(H_{b-1}/(e+ell_b))). (A41.2)

If Lmax=0 there are no edges. For Lmax>=1, writing each component
as L edges and L+1 vertices gives

    edge_count <= [Lmax/(Lmax+1)](n-2)m.          (A41.3)

In particular Lmax<=1 is sufficient for matching. A larger upper
bound establishes neither matching nor a counterexample to it.

For the remaining all-large-old-gap records the smaller source e is
larger than c^2/log^3 c, since any old pair spans at least one of the
three adjacent old gaps. Also r>b and r<c log c imply c>b/log b.
Therefore e>b^2/log^5 b, so e>=ell_b. The original fixed cap at
b>=m0 now implies the actual path-length bound

    L< (C/2)log(2b)(log b)^5.                    (A41.4)

This yields a positive count deficit in A41.3. Its scalar fractional
size is only of inverse-polylogarithmic order. Turning it into a
useful de-weighted saving requires preserving which edges carry the
weight; no summable weighted deficit is claimed from A41.4 alone.

The finite test uses the existing C=1,m0=2,M=T=96 variant at cut25.
The two original cells at v=k48 have552 vertices each and23 forced
same-future edges. The exact counts and weights are:

| e | future decreases | future increases | decreasing after old-source exclusions | strict | all-large | strict sum de | all-large sum de |
|---|---:|---:|---:|---:|---:|---:|---:|
|48 (old6,9)|28|43|27|23|17|358752|248784|
|422 (old6,20)|3|58|3|3|2|789140|548178|

All strict nontrivial paths in these cells have length1. For e422,
H24=713 and ell25=2 give Lmax<=floor(713/424)=1. For e48 the
corresponding numerical bound is14, so the observed matching is only
finite evidence. One subsequently authorized cell, still b25,e48 but
v=k96, has1704 vertices,71 forced edges,47 decreasing/65 increasing
edges,43 decreasing after source exclusions,31 strict and23 all-large
edges. Their de sums are513936 and358752. Again every strict path
has length1. No further cells or shifts were searched. The original
genuine coefficients are1/1148518878296832 at k48 and
1/1259618724663197400 at k96. All strict comparisons were resolved;
UNKNOWN=0. A general matching theorem remains unproved.

### Future evolution and original prices

At fixed b,e, adding future point v+1 adds core edges only with a new
vertex as tail: their upper output is v+1 and lower output was already
present. Such a new vertex has no incoming core edge at this horizon.
Its target had no previous incoming edge either, by uniqueness of the
numeric predecessor at shift e. Thus an existing path can only be
prepended, or a new nontrivial path can begin at an old isolated vertex.
Two existing nontrivial paths never merge. Every path keeps its terminal
(old x0,future i0). Core gates of an existing edge do not depend on v.

Index final paths at the actual finite output horizon T by these
terminals. Along one path, list old values A_j and future ranks f_j
from its terminal j0 to its start jL; both lists increase. Its exact
original-price contribution is

    W_path=e sum_{j=1}^L(A_j-A_{j-1})u_{f_j}^[M]
          =e sum_k lambda_k(A_last_active(k)-A_0), (A41.5)

where the active part is the suffix of the final directed path whose
future endpoints lie at or before min(k,T). Components k>T remain
present with the final path span. In particular

    W_path<=e H_{b-1} u_{i0+1}^[M].

For each terminal future rank i0 there are at most n-2 old rows, and
each physical terminal labels at most one path at this fixed e. Since
u_r^[M]<=alpha_r/H_b^2 and
sum_{r=b+2}^infinity alpha_r<=1/[3(b+1)^3], summing these relaxed
terminal allowances over e gives only

    P_b<=n^2(n-2)H_{b-1}^2/[12(b+1)^3 H_b^2]<1/12. (A41.6)

The final constant is weaker than A02's1/24. The preceding expression
can still improve when H_{b-1}/H_b is small; it is not asserted to be
pointwise dominated in every history. The failed step is replacing
each path's actual span, first-edge birth and strict gap by its full
terminal allowance, then adding all terminal rows and shifts without
their shared correlations. That relaxation leaves a constant-sized
profile envelope and does not control the harmonic square-root norm.
No original coefficient or terminal alpha was reset.

The independent notes and exact cells are bound by
`A41_A42_review_manifest.json` and `A41_A43_followup_review_manifest.json`.
The generic span identity A41.1 is Lean-verified as
`mixed_shift_chain_balance`. The actual path decomposition, cap bound,
lineage and full-price estimate remain independently reviewed hand
proofs. General matching is neither proved nor refuted by these cells.

## A42. The common source-pair bank gives a stronger distant-rank bound

At a fixed cut let D be the actual positive difference set of the
first n=b-1 points and S_b=sum_D d^2. An ordered source pair d>e
recovers both old endpoint pairs by Sidon. Its output difference is
t=d-e; global positive-difference uniqueness then recovers at most
one output pair(i,r). Thus original physical records at this cut
inject into the ordered pairs(d,e), including the original orientation.
The strict gates and six-endpoint condition select a subset. Therefore

    Q_bk<=B_b=sum_{d>e in D}de
       =[(sum_{d in D}d)^2-S_b]/2
       <=n^4 H_b^2/32.                           (A42.1)

The final step uses the actual adjacent-gap bound
sum_D d<=n^2 H_{b-1}/4<=n^2 H_b/4 and drops only the nonnegative
diagonal S_b. No future pair is counted twice. The generic exact
weighted bank identity is Lean-verified as
`source_pair_product_identity`; the actual strict-record injection
and full component instantiation remain hand mathematics.

Fix p>1/2 and R_b=ceil(b(log b)^p)+1, b>=3. If M>=R_b, the original
far component sum satisfies

    P_rankfar_b<=n^4/32 sum_{k=R_b}^M kappa_k
      =n^4[alpha_{R_b}-alpha_{M+1}]/32
      <=1/[32(log b)^(4p)].                      (A42.2)

We used H_k>=H_b and alpha_R<=1/(R-1)^4. If M<R_b the sum is empty.
For k>T its record bank remains frozen at T while the genuine tail
continues. Integrating the decreasing numerical majorant yields

    sum_b sqrt(P_rankfar_b)/b
       <=(log2)^(1-2p)/[sqrt32(2p-1)].            (A42.3)

The cap is not needed. For fixed p=5/8 the norm cost is
1/[sqrt2(log2)^(1/4)], and remaining component ranks have
k<ceil(b(log b)^(5/8))+1. This is an actual uniformly paid subclass,
not a bound for the remaining core or a final Q1 result.

A02 also gives Q_bk<=n^2 m^2 H_b^2/8, m=min(k,T)-b. Taking the
geometric mean of this nonnegative upper bound and A42.1 gives

    Q_bk<=n^3 m H_b^2/16.                         (A42.4)

This numerically dominates A40's coefficient1/4. A40's actual mixed
endpoint recovery remains valid structural information, but its scalar
linear bound is superseded by A42.4. The whole source-pair bank loses
actual future-difference compatibility, gates and endpoint correlations;
it must not be treated as an independent attained budget at every rank.
The independent hand review is `A42_SOURCE_PAIR_RANK_TAIL_REVIEW.md`.

## A43. A uniformly paid short component interval next to the cut

Fix q>2/3 and s_b=floor(b/(log b)^q), b>=3. Select only ORIGINAL
components b+2<=k<=min(M,b+s_b), and call the resulting profile
P_short_b. If s_b<2 the selected sum is empty. By A02,

    Q_bk<=S_b binom(min(k,T)-b,2),
    S_b/H_b^2<=n^2/4, kappa_k<=4/b^5.

The last inequality uses k>=b+2 in the unchanged explicit formula
kappa_k=4/[k(k^2-1)^2]. Hence the exact finite hockey-stick sum gives

    P_short_b<=n^2/b^5 sum_{m=2}^{s_b}binom(m,2)
      =n^2 binom(s_b+1,3)/b^5
      <=s_b^3/(6b^3)<=1/[6(log b)^(3q)].          (A43.1)

Thus

    sum_b sqrt(P_short_b)/b
       <=(log2)^(1-3q/2)/[sqrt6(3q/2-1)].         (A43.2)

This uses no cap and retains every original price coefficient of the
selected components. For k>T only an upper-bound step replaced
min(k,T)-b by k-b. No omitted later component is asserted to vanish.
The full original profile remains the sum of its selected and unselected
nonnegative components.

Fix q=3/4 and A42's p=5/8. At small b the nominal short and far sets
may overlap. Pay short first, then apply A42 to the still-unpaid far
subset. Together with A12 small-old-gap records, A33 far-span components
and A02's finite initial cuts, the remaining original component band is

    b+floor(b/(log b)^(3/4)) < k
           < ceil(b(log b)^(5/8))+1,              (A43.3)

with all three old gaps large, b>=max(3,m0), and H_k<H_b(log b)^2.
Empty central intervals cause no problem. The short norm cost at q3/4
is8/[sqrt6(log2)^(1/8)]. The original strict conditions and fixed cap
at all intermediate ranks remain unchanged. The central component
norm is still unproved, and the master goal remains unresolved.

The independent review is `A43_SHORT_RANK_COMPONENT_REVIEW.md`, bound
in `A41_A43_followup_review_manifest.json`. No finite search or new
Lean theorem was run for this short-component hand proof.

## A44. A shared-terminal matching fails; the actual fixed-source transport

Fix the physical terminal(old x,future i) and allow all old shifts e.
An incoming original record has old upper endpoint y and upper output r,
with d=a_y-a_x and e=d-(a_r-a_i). The proposed joint matching rule,
that each y and each r is used at most once, is false even in the
previous all-large-old-gap, central-rank, near-span setting.

Use the existing fixed C=1,m0=2,M=T=96 variant at b25,k48 and terminal
(x,i)=(1,42), with a_x=1,a_i=2975. The exact restricted check of the
138 possible(y,r) pairs, y2..24,r43..48, finds10 strict records,7 of
them all-large. No other terminal, history or component was scanned.
All comparisons are resolved, UNKNOWN=0. For all strict records,
sum de=1166795,sum e=1907, and there are7 distinct y,2 distinct r and
10 distinct e. The all-large values are655712,1150,5,2,7 respectively.

Two all-large original records refute the row rule:

    y18,r43,d350,e59,(w,z)=(8,11),t291,de20650;
    y18,r44,d350,e36,(w,z)=(12,13),t314,de12600.

The first and the following all-large record refute the column rule:

    y19,r43,d400,e109,t291,de43600.

Every displayed mass retains lambda48=1/1148518878296832. At x=1
there is no outgoing strict edge, so this is a physical path terminal
for every displayed shift. The counterexamples concern DIFFERENT
shifts sharing that terminal. They do not contradict or prove a
matching statement at one fixed e, which remains open beyond A41's
three prescribed finite cells.

### A valid weighted transport after fixing the old source pair

Fix also y, hence d=a_y-a_x, while i stays fixed. Let r vary over the
original records present at one component horizon v=min(k,T). Each
e has its unique old source(w,z). Two such edges cannot share w or
share z unless they are the same edge. Indeed, if r1<r2 then

    e1-e2=a_(r2)-a_(r1)>0.

A shared lower or upper source endpoint would make that positive
quantity an old positive difference. Global Sidon uniqueness forbids
an old and a future pair from representing it. Equivalently the
original equations d+a_i+a_w=a_z+a_r and their companion imply
endpoint recovery directly from the literal two-sum Sidon condition.
This latter statement is Lean-verified as `source_row_endpoint_recovery`.

The graph w->z on the n-2 old points excluding x,y thus has indegree
and outdegree at most1, and w<z excludes cycles. It is a disjoint union
of directed paths. Let B_xy be these remaining old values, N=n-2, and
let T_xy be the sum of the largest floor(N/2) values minus the sum of
the smallest floor(N/2) values. Then, exactly and subsequently bounded,

    sum_row e=sum_paths(a_end-a_start)
       <=T_xy<=floor((n-2)/2)H_(b-1).             (A44.1)

To prove the first inequality, path starts and ends are disjoint,
with equally many of each, at most floor(N/2). The largest difference
of equal-size sums is obtained from opposite ends of the ordered B_xy.
Increasing that size up to floor(N/2) can only increase the difference.
This uses actual shared vertices; it is not an independently assigned
budget for every r. Unlike A41, this is an old SOURCE graph with d,i
fixed and e varying. It is not the graph of mixed labels at fixed e.

Write E_xyi(k) for the actual source edges present at min(k,T), with
every original gate retained. The exact weighted birth measure is

    W_xyi=d sum_{k=i+1}^M lambda_k sum_{E_xyi(k)} e
          =d sum_records e u_r^[M].              (A44.2)

For k>T the source bank remains fixed while the genuine component tail
continues. The graph may merge paths as r grows; no persistent-terminal
claim from A41 is transferred to this different graph. Replacing each
actual transport in A44.2 by T_xy gives W_xyi<=d T_xy u_(i+1)^[M].
Summing this relaxation over i and old pairs, using the same alpha
tail as A41 and sum_D d<=n^2 H_(b-1)/4, gives only

    P_b<= n^2 floor((n-2)/2)H_(b-1)^2 /
               [12(b+1)^3 H_b^2] <1/24.          (A44.3)

For n<4 the original record set is empty. The bound holds for b>=3;
it does not control the harmonic square-root norm. The failed relaxation
replaces the actual simultaneous row transports and their birth ranks
by full ordered endpoint allowances, then sums the old-pair/i allowances
without compatibility. It supplies no actual divergent lower bound.
The fixed-source recovery is formalized; the path transport, full price
and norm limitation remain independently reviewed hand mathematics.

## A45. Small second-source labels are uniformly paid; cap localizes both births

Fix q>1, b>=3 and L_b=floor(b^2/(log b)^q). Select the ORIGINAL records
with smaller source label e<=L_b, through all their genuine components.
Call their profile P_smallsource_b. L_b=0 gives an empty subclass.
Let D be the actual positive difference set on the first n=b-1 points.
By A42's recovery of one physical record from an oriented source pair,
integer uniqueness and the actual old gap-sum bound,

    Q_smallsource_bk
      <=(sum_{d in D}d)(sum_{1<=e<=L_b}e)
      <=n^2 H_b L_b(L_b+1)/8.                    (A45.1)

Dropping e<d or a strict gate in this upper bound introduces no duplicate
physical output into the selected profile. Integer Sidon packing gives
H_b>=b(b-1)/2, and original components start at k>=b+2. Consequently

    P_smallsource_b
      <=n^2 L_b(L_b+1) alpha_(b+2)/(8H_b)
      <=L_b(L_b+1)/[4(b+2)^2(b+1)^2]
      <=1/[2(log b)^(2q)].                       (A45.2)

In the last step, L_b>=1 implies L_b+1<=2L_b; the empty case was
already separated. The price step is the original nonnegative tail
sum_{k=b+2}^M kappa_k/H_k^2<=alpha_(b+2)/H_b^2. In particular the
finite subtraction alpha_(M+1) has only been bounded from above,
never reset. This works with both M,T and all k>T components intact.
The decreasing integrable majorant proves

    sum_{b>=3}sqrt(P_smallsource_b)/b
       <=(log2)^(1-q)/[sqrt2(q-1)].               (A45.3)

No cap is used in A45.1--3. Fixing q=5/4 costs
2sqrt2/(log2)^(1/4). The still-unpaid second source then satisfies
e>L_b, hence e>b^2/(log b)^(5/4); this follows from e being integer.

### The original fixed cap supplies a stronger two-birth support restriction

Let s=min(y,z) be the earlier of the two source upper ranks. Since
e<=H_z and e<d<=H_y, one has e<=H_s. For b>=max(3,m0), s>=m0, the
same all-rank cap therefore yields, in the still-unpaid subclass,

    b^2/(log b)^q < e <= C s^2 log(2b),
    s>b/[sqrt(C log(2b))(log b)^(q/2)]
       >=b/[sqrt(2C)(log b)^((q+1)/2)].           (A45.4)

For q5/4 the final exponent is9/8. Thus BOTH source upper ranks must
lie above this boundary. Only the cap at the actual intermediate s
is used; no cap below m0 is inserted.

For s<m0 and M>=m0 put D0=ceil(C m0^2 log(2m0)) and B=max(3,m0).
The cap at the existing rank m0 gives e<=H_s<=H_m0<=D0. The constant-L
version of A45.2 and the exact telescoping numerical sum give

    sum_{b>=B}sqrt(P_{s<m0,b})/b
       <=sqrt(D0(D0+1))/[4B(B+1)],                (A45.5)

because sum_{b>=B}1/[b(b+1)(b+2)]=1/[2B(B+1)]. If M<m0, or for
b<m0, use the previously paid bounded number of initial cuts. Nothing
assumes that a short prefix extends to m0. There is no new uniform
estimate for the complement in A45.4.

At the one existing A44 terminal, an independent rational log interval
certifies L25=144. The A43 short width is10 and the far ceil is52,
so k48 lies in35<k<53. Also H48=4248<773(log25)^2. Within the seven
previous all-large records, e>144 leaves precisely

    (y,r,e,de)=(22,43,312,188136),(24,43,422,300886).

Their source-weight totals are sum e=734,sum de=489022. This shows
that A44's column-matching failure survives A45's small-source deletion,
while the old-row duplication does not occur in these two remaining
records. This is a check on the same saved ten edges, not a new search
or a statement about every terminal. All arithmetic gates are exact;
the displayed norm theorem remains a reviewed hand proof.

## A46. Uniform cut-relative deletion of small outputs and small old gaps

Fix q>2 and J_b=floor(b^2/(log b)^q), b>=3. The following are two
separate uniformly paid subclasses of the unchanged original records.
Each selection depends on the actual cut b. At every cut the physical
record contribution is split by its predicate. The selected and complementary
pieces TOGETHER retain exactly the original coverage c+1,...,i-1 and
genuine price; a selected piece alone need not be a whole interval.
For a dyadic block its selected coverage is exactly the sum of 1/b over
original covered cuts where the selection holds. The two complementary
coverage sums add to the original one. This also applies to A45's
cut-dependent threshold. There is no fresh independent budget for the
same record at another cut.

First select actual output differences t<=J_b. For every t, A02 gives
the oriented old source correlation K_t<=S_b, and Sidon recovers at
most one actual output pair for this t. Hence

    Q_smalloutput_bk<=J_b S_b,
    P_smalloutput_b<=J_b n^2/[4(b+2)^2(b+1)^2]
         <=1/[4(log b)^q].                       (A46.1)

The same original kappa tail as A45 is used; the output and component
horizons stay separate. This gives

    sum_b sqrt(P_smalloutput_b)/b
       <=(log2)^(1-q/2)/[2(q/2-1)].               (A46.2)

Next select old quadruples having at least one adjacent physical gap
at most J_b. There are at most J_b actual old pairs with such a small
positive difference, since the integer labels are unique. Every selected
quadruple contains at least one such pair, so its count is at most
J_b binom(n-2,2). This is a union bound: a quadruple with several small
pairs may be overcounted in the bound, never in the actual profile.
For one quadruple A10 gives total de across all three possible matchings

    AC+(AC+BH)+BH=2(AC+BH)
       =2(A+B)(B+C)<=2H^2<=2H_b^2.              (A46.3)

Each matching has at most one actual output pair. At a fixed original
component, gates and output births merely select a subset of these
three nonnegative weights. It follows that

    Q_smalloldgap_bk<=2J_b binom(n-2,2)H_b^2,
    P_smalloldgap_b<=J_b(n-2)(n-3)/[(b+2)^2(b+1)^2]
         <=1/(log b)^q,                          (A46.4)

where n<4 is empty and the displayed product bound applies for n>=4.
Thus

    sum_b sqrt(P_smalloldgap_b)/b
       <=(log2)^(1-q/2)/(q/2-1).                 (A46.5)

Neither subclass needs a cap. At q=5/2 their norm costs are respectively
2/(log2)^(1/4) and4/(log2)^(1/4). Pay them in a fixed order after any
previously paid subclasses; a still-unpaid subset satisfies the same
upper bound. No disjointness of the nominal selected sets is assumed.

Together with A43, A33 and A45, the remaining ORIGINAL components have

    b+floor(b/(log b)^(3/4)) < k < ceil(b(log b)^(5/8))+1,
    H_k < H_b(log b)^2,
    e > b^2/(log b)^(5/4),
    min(A,B,C), t > b^2/(log b)^(5/2),
    s > b/[sqrt(2C)(log b)^(9/8)],                (A46.6)

with b>=max(3,m0), after the explicitly paid initial-source/cut cases. Every original
strict condition and the fixed C,m0 cap at all intermediate ranks
remain. These are proved necessary conditions for the unpaid subclass,
not new definitions of CoreUniform and not a proof that it is empty.
The norm of this complement is still unproved.

The same two saved A45 edges were checked against this further selection,
without new candidates. Two independent rational-log calculations give
J25=33. The y22,r43,e312 edge has old gaps(88,312,203) and t291, so
it remains, with de188136. The y24,r43,e422 edge has gaps(18,422,273)
and is paid by the small-old-gap subclass. Thus the A45 column witness
does not survive as a two-edge witness in this still narrower selection.
One edge remains in this specific terminal; no general matching statement
for the new remainder follows. Both earlier counterexamples retain
exactly their stated original and A45 scopes.


## A47. One physical label bin, actual windows and shared row deficits

Fix one original cut b and component k, v=min(k,T), m=v-b, and the
larger actual old source pair (x,y), d=a_y-a_x. Let D_h be the positive
old differences in one half-open integer bin [hJ,(h+1)J), with e<d.
Every label has its unique old endpoints. Put

    B_(d,h)=d sum_(e in D_h)e.

For a fixed lower output i>b the required upper value is
a_r=d+a_i-e. Thus this row uses only actual future points in

    (d+a_i-(h+1)J, d+a_i-hJ].                       (A47.1)

This window contains exactly J integer positions; its maximum possible
occupied span is J-1. Actual source exclusions, six-distinctness and all
original strict gates remain attached to each recovered physical record.
An absent output has no assigned rank or price. Original cut selectors,
including A46.6, may subsequently delete records but never create any.

Let q_i be the sum de of accepted records in this source/bin/row and
component. A given (d,e) determines t=d-e and, by actual Sidon uniqueness,
at most one ordered output pair. Consequently the used e labels of
different i rows are disjoint and

    Q_(d,h)=sum_i q_i <= B_(d,h).                   (A47.2)

For m>=2 there are m-1 possible lower-output rows. Resetting the entire
same bank allowance independently at each row gives the exact identity

    sum_i(B_(d,h)-q_i)
      =(B_(d,h)-Q_(d,h))+(m-2)B_(d,h).             (A47.3)

The last term is an overcount of a common bank, not a physical deficit.
For m<=1 no output pair exists and the row sum is empty. This comparison
does not impose any threshold, cap or finite extension premise.

The original price for this bin is exactly

    sum_accepted d e u_r^[M]
      =sum_(k=b+1..M) (kappa_k/H_k^2)
          Q_(d,h)(min(k,T)).                       (A47.4)

In particular k>T components persist on the same frozen T bank.
The original alpha_(M+1) is retained. An unused label without an actual
eligible output receives no invented full tail. Partitioning old labels
is disjoint for a fixed d; the same label e used with a different d is
not thereby a one-use budget. Original record cut coverage remains
[c+1,i-1]; any cut-dependent selections partition that coverage exactly.
Equation A47.4 is for the original bin, or a fixed record subset. If a
selection also depends on component k, as the central/near part of
A46.6 does, its indicator stays INSIDE the k sum; that selected price
cannot be replaced by the complete u_r tail. The two finite records'
saved full tails describe their original prices, not an assertion that
every one of their components lies in the selected remainder.

The bounded independent test reuses C=1,m0=2,M=T=96, b25,k48, old pair
(1,22),d603,J33,h9. The bin [297,330) has thirteen actual old labels,
sum e4025 and B2427075. At lower output i42 only e312 uses an actual
point, r43, giving de188136 and one-row deficit2238939.
When all possible lower outputs at the SAME cut/component/source/bin
are retained, exactly two labels survive:

    e302, old pair(18,23), output(39,41), de182106;
    e312, old pair(10,19), output(42,43), de188136.

Both are original strict records in A46.6, with UNKNOWN=0. The remaining
eleven labels have four absent differences, six lower outputs not after
the cut and one upper output after k48. Other failures are separate flags.
The joint weight is Q370242 and the true joint deficit2056833.
There are22 rows, so independent reset deficits total53025408,
overcounting by50968575=21B. These exact integer quantities are separately
multiplied by the unchanged lambda48=1/1148518878296832. The two distinct
full tails u41^[96] and u43^[96] are saved separately and independently
checked, preserving alpha97.

This strictly rejects automatic full one-row use and addition of
independently reset row deficits. The finite unused fraction is not
claimed uniform in histories or scales. Original source/cap checks,
reference and independent rational checks and exact prices are bound
by finite_campaign/A47_A48_review_manifest.json. No new history or full
profile scan was performed. The frozen uniform norm remains open.

## A48. Generic row-window packing cannot improve the common bank

Let J>=1 be an integer and define

    rho=max{r in Nat : binom(r,2)<=J-1}.

Every actual integer Sidon set in A47's width-J window has at most rho
points, because its distinct positive differences lie in 1,...,J-1.
Maximality and integrality give rho>=1 and J<=rho(rho+1)/2.

For m actual future points the existing joint output-label allowance
in a width-J bin is h=min(J,binom(m,2)). For m<=1 it is zero. For m>=2,

    min(J,binom(m,2)) <= (m-1)rho.                 (A48.1)

If m<=rho+1 then m/2<=rho and binom(m,2)<=rho(m-1).
If m>rho+1 then J<=rho(rho+1)/2<=rho(m-1).
This proves that replacing each actual row by the SAME generic Sidon
window capacity and adding those capacities is a weaker upper bound
than the already available joint capacity.

For any single common finite nonnegative bin-weight list, let W(s) be
the sum of its largest min(s,N) weights, W(0)=0. Partition its first
min(h,N) weights into at most m-1 groups of at most rho elements. Each
group is at most W(rho), so

    W(h) <= (m-1)W(rho).                            (A48.2)

Ties, zero weights and capacities exceeding N cause no exception.
The unchanged nonnegative component price preserves this inequality.
It does not compare different row-dependent actual lists or different
output birth prices after forgetting those dependencies.

For the A47 cell J33, rho8 and m23. Thus h33 is already below the
independent row capacity176; the actual old bin count13 is still
smaller. This is a comparison of allowances, not an asserted realization
of their maxima or a profile lower bound. The independent hand review
is in finite_campaign/A48_WINDOW_PACKING_DOMINATION_REVIEW.md.
The algebraic real-valued implication A48.1 is formalized as
row_window_capacity_dominated; the full Sidon window and common-weight
instantiation remain hand mathematics.

The lost information has now been isolated exactly: actual windows,
source exclusions, original gates, shared compatibility and first
output ranks. Their joint use is not refuted by A48. A joint estimate
must improve an existing common bank, not sum independent copies of it.

## A49. A targeted higher-energy substitution fails on actual Sidon sets

A targeted source search was used only to check a proposed mathematical
input concerning six-variable additive correlations. The selected
primary paper by Shkredov, arXiv:2103.14670, defines in equation(5)

    E_l(A)=sum_z r_(A-A)(z)^l.

This is not the three-sum energy

    T_3(A)=sum_s r_(A+A+A)(s)^2.

For an n-point integer Sidon set, r_(A-A)(0)=n and every other realized
difference has multiplicity1. Thus

    E_3(A)=n^3+n(n-1).                              (A49.1)

Counting just ordered triples with the same multiset in the two copies
gives

    T_3(A)>=36 binom(n,3)+9n(n-1)+n
           =6n^3-9n^2+4n.

All other equal sums contribute nonnegatively, so for n>=2,

    T_3(A)-E_3(A)>=5n(n-1)^2>0.                    (A49.2)

Even replacing equality by a fixed multiplicative constant fails on
arbitrary finite integer Sidon sets. Reuse the actual family already
proved in causal_fourier_rank_commutator.md section5:

    a_(i+1)=1+2pi+(i^2 mod p), 0<=i<p, p odd prime.

Equality of positive differences forces the index difference to agree;
reduction modulo p then recovers the initial index. Hence this is
integer Sidon and H_p<2p^2. Its ordered triple-sum function has total
mass p^3 on at most3H_p+1<6p^2 integer sites. Cauchy gives

    T_3(A)>p^4/6,   E_3(A)<=2p^3,
    T_3(A)/E_3(A)>p/12 -> infinity.                (A49.3)

Thus no universal T_3<=K E_3 follows from bare finite integer Sidon.
This applies an EXISTING source family to the attempted energy
substitution; it is not a newly found Sidon family or another repetition
of the existing raw quartic counterexample campaign. In particular its
first gap is2p+1, so it does not satisfy one fixed C,m0=2 all-prefix cap
as p grows. For any other fixed m0>=2 the width at m0 is likewise
unbounded as p grows. It is not a counterexample to the frozen
all-prefix-cap statement or Q1.

The second selected primary paper, Ortega--Prendiville,
Extremal Sidon Sets Are Fourier Uniform, with Applications to
Partition Regularity, JTNB35(1)(2023),115--134, Theorem1.2, applies
to arbitrary finite S subset [N], but its useful relative error
depends on | |S|/sqrt(N)-1 | being small. Taking the smallest ambient
N=H_n+1, the original cap only supplies
N/n^2<=C log(2n)+1/n^2. This bound has NOT proved N/n^2->1 or the
required near-extremality. The theorem itself is not declared
inapplicable; the needed small error has not been obtained here.
No external theorem has been adopted as an unproved U4-F input.

Primary links and actual search/fetch metadata are in
TARGETED_SOURCE_CHECK_13.json. External text checks and the independent
A49 hand review are not full Lean verification. The relevant next input
must retain the mixed old/future roles, all-prefix cap and actual
rank/gate/price restrictions; unweighted E_3 substitution loses them.

## A50. A monotone common raw deficit; two actual transfers fail

Fix one physical larger old source pair (x,y), d=a_y-a_x, one fixed
integer bin of positive e<d, M and an output horizon v<=T<=M. For every
actual e label let c_e=max(y,z_e), w_e=de. For b>y let

    B_b=sum_(c_e<b)w_e,
    Q_b=sum_(original strict records, r<=v)w_e 1[c_e<b<i],
    D_b=B_b-Q_b.

The bank includes source pairs failing six-distinctness or other gates;
the original Q does not. One (d,e) determines at most one actual output,
so every bank label supports at most one record. All original gates are
fixed; the bin and v do not move with b.

For consecutive cuts define Delta B_b as the new old-label mass,
A_b as original record mass with c=b and b+1<i, and R_b as mass with
c<b and i=b+1. Exact physical cut exchange gives

    Q_(b+1)-Q_b=A_b-R_b,
    D_(b+1)-D_b=(Delta B_b-A_b)+R_b>=0.             (A50.1)

Here A_b<=Delta B_b by actual source-pair recovery. A label absent from
the old bank cannot already have an active record. After a bank label
becomes available, its original cut interval can end only once. This
proves raw monotonicity for this PARTICULAR common bank. It does not
assert any of the earlier disproved triple-fiber or mixed-label laws.

If B_b,B_(b+1)>0, normalization has the different exact increment

    D_(b+1)/B_(b+1)-D_b/B_b
      =[B_b Delta D_b-D_b Delta B_b]/
          [B_b(B_b+Delta B_b)].                    (A50.2)

Its sign is not guaranteed. The independent bounded test looks up only
the33 integers297,...,329 in the existing certified C1,m02,M=T96
history, with d603,old pair(1,22),v48,cuts23,...,47. It recovers three
original strict records, including e318,output(25,28),which had already
retired at the preceding A47 cut25. In the actual variant history this
record's old quadruple values are(1,33,351,604), not the baseline fixture.

    cut23: B2056230,Q379890,D1676340,D/B=278/341;
    cut24: B2238336,Q561996,D1676340,D/B=695/928.

At23->24 the newly born e302 record adds182106 to both B and Q.
Thus Delta D=0 but Delta(D/B)=-20989/316448<0. All24 tested raw
increments obey A50.1 exactly; UNKNOWN=0. The initial two-record
prediction was corrected by the independent lookup before acceptance.

The FULL DISPLAYED A46.6 selectors give a separate counterexample.
At cut23, k48 is on the paid distant-rank side; at24 it is central.
The old e312/e318 records enter because of this common selector change,
while e302 is an actual source birth. Consequently

    D_selected,23=2056230,
    D_selected,24=1676340,
    Delta D_selected=-379890.                     (A50.3)

J23=30,J24=31,L23=126,L24=135 and the actual e318 gaps(32,318,253)
are independently certified. Displayed support conditions and initial
exception checks are retained; satisfying necessary remainder conditions
is not asserted to prove nonmembership in every previously paid class.

For any zero-one cut selector sigma, the exact selected exchange includes
a further term over records present at BOTH cuts:

    Delta Q_selected
      =A_selected-R_selected
          +sum_staying w_h(sigma_(b+1)-sigma_b).    (A50.4)

This term accounts for A50.3; it must not be called source birth.

The original full priced fixed-record subset is
P_b=sum_(strict,r<=v)de u_r^[M]1[c<b<i].
A moving-cut auxiliary allowance has deficit
Dhat_b=B_b u_(b+1)^[M]-P_b>=0, but it need not increase.
At the first stationary step25->26 in the same trace, B2427075
and P are unchanged, so

    Delta Dhat=-lambda26 B
       =-21574/21751847325<0,
    lambda26=2/4894165648125.                       (A50.5)

This is distinct from the fixed component lambda48. Original full tails
u28,u41,u43 and alpha97 are preserved. The auxiliary allowance is not
an assigned genuine price for an absent output. No new history,
full profile replay or wider bin/source search was used. Exact evidence
and independent rational checks are in finite_campaign/A50_*.

## A51. Birth-fixed price compensation and its precise allowance cost

For the same physical source/bin assign the AUXILIARY allowance

    omega_e=de u_(c_e+2)^[M].

This is indexed by a causal lower bound for the upper output rank, not the
genuine price of a missing output. At relevant cuts c_e<=b-1<=T-2,
so c_e+2<=M exists. For an actual original record c<i<r,
u_r^[M]<=u_(c+2)^[M]. Define

    Bstar_b=sum_(c_e<b)omega_e,
    Dstar_b=Bstar_b-P_b.

Each label contributes zero before its source birth, then omega_e minus
its actual price while its single original interval is active, then
omega_e after retirement. Missing or invalid outputs have active price0.
All steps are nonnegative, hence Dstar is nonnegative and nondecreasing.
This proof retains any fixed original record subset, including r<=v;
it does not apply an arbitrary cut-dependent selector silently.

The difference from A50's moving-cut allowance is exact. With
C_b=Bstar_b-B_b u_(b+1), starting at b0=y+1,

    C_(y+1)=0,
    C_(b+1)-C_b=lambda_(b+1) B_b,
    Dstar_b=Dhat_b+C_b.                            (A51.1)

At the initial cut all available labels have c_e=y. At a later birth
c=b, both allowances add de u_(b+2), while the old moving tail loses
lambda_(b+1)B_b. Thus C is precisely the accumulated missing diagonal
term; no output price or terminal alpha is changed.

The same construction over ALL actual ordered source pairs has a useful
finite Abel form. Let

    F_n=sum_(d>e in actual positive differences of first n points)de,
    F_1=0.

Pair recovery bounds the original core by this common pair bank. Its
birth-fixed allowance is

    Bstar_b=sum_(c=2..b-1)u_(c+2)(F_c-F_(c-1))
      =u_(b+1)F_(b-1)+sum_(c=2..b-2)lambda_(c+2)F_c. (A51.2)

A42 gives F_c<=c^4 H_c^2/32. Consequently, for b>=3,

    Bstar_b < 1/32+(1/8)sum_(s=4..b)1/s.           (A51.3)

The empty sum is zero. Indeed the first term is at most
(b-1)^4/[32b^2(b+1)^2]<1/32, and each summand is at most
c^4/[8(c+2)((c+2)^2-1)^2]<1/[8(c+2)].
This is an upper allowance with a logarithmic envelope, not an actual
profile lower bound or a constant bound on the desired norm.
Monotonicity alone does not pay the harmonic square-root sum.

The generic single-label implication is formalized as
interval_deficit_mono: for0<=p<=w and b<=b', the difference between
w1[c<b] and p1[c<b<i] is nondecreasing. Full actual source/price
instantiation and the Abel/norm statements remain hand mathematics.

## A52. The specific remaining selectors have one common activation

The general warning about fragmented selected coverage in A46 remains
valid for arbitrary selectors. The DISPLAYED A46.6 selector has more
structure. Work beyond B=max(4,m0); the one additional cut3, if needed,
is uniformly paid by A02, at cost at most1/(3sqrt24).

On real b>=4 the following functions are increasing:

    b(log b)^(5/8),
    b+b/(log b)^(3/4),
    b^2/(log b)^(5/4), b^2/(log b)^(5/2),
    b/(sqrt(2C)(log b)^(9/8)).

For b^a/log^q b the derivative has the sign of a log b-q.
The most restrictive displayed case is2log4>5/2.
For b/log^(3/4)b and the source-rank threshold, log4>9/8 suffices.
Floors and ceilings preserve nondecreasing behavior. The actual
H_b(log b)^2 also increases.

Fix k>=6, v_k=min(k,T). If there is a b in[B,v_k-2] satisfying

    k<ceil(b(log b)^(5/8))+1,
    H_k<H_b(log b)^2,                              (A52.1)

let a_k be its first such cut. Otherwise this component's remaining
profile is empty and its auxiliary bank is set to0. These two
conditions, once true, stay true and are COMMON to every record.
No cut beyond the actual finite history is used to define a_k.

All other displayed conditions can only end a record's eligibility
after this activation: k>b+floor(b/log^(3/4)b), large e, large t and
the three old gaps, and the source-rank lower threshold. Initial
source exclusions and every original strict gate are fixed conditions.
Intersecting with the physical interval[c+1,i-1] gives exactly

    [max(c+1,a_k),h_(record,k)]                     (A52.2)

or an empty set. Its end may come from a threshold as well as i.
Thus this particular remaining component does NOT require several
disconnected intervals for the same physical record.

Use the correctly activated common auxiliary bank

    G_(b,k)=1[b>=a_k] F_min(b-1,v_k-2).

It counts each eligible old source pair once; it does not reset a
whole bank independently at each output row. At first activation the
entire existing bank is introduced once. Afterwards, new original
records inject into newly born source pairs, while staying records can
only retire. Equivalently, each pair has one allowance born at
max(c+1,a_k), with an active subinterval beginning there or empty.
Therefore

    G_(b,k)-Q_remaining(b,k) >=0
    and is nondecreasing in b.                    (A52.3)

This covers the frozen bank after b>=v_k-1, when Q is0. Summing over
the FIXED k range6,...,M with the unchanged lambda_k gives

    Gbar_b=sum_k lambda_k G_(b,k),
    Dbar_b=Gbar_b-P_remaining(M,T;b),

both nondecreasing, with Dbar>=0. Components k>T remain present with
v_k=T, and every selector stays within the component sum.

This repairs A50.3 by matching the actual common activation. It is not
yet the norm estimate. In particular its terminal allowance only gives

    Gbar_(T-1) <= (1/8)sum_(k=6..T)1/k+1/32.      (A52.4)

For k<=T use lambda_k F_(k-2)<1/(8k); for k>T the whole tail is at most
F_(T-2)u_(T+1)<1/32, with zero tail if M=T. T<6 has empty core.
This upper bound is uniform in M at fixed T but still grows with T.
No actual lower bound, prefix extension or fixed-cap nonexistence is
inferred. All conclusions in this section are independently reviewed
hand mathematics; only the underlying generic interval lemma is formal.

## A53. A new uniformly paid source-birth distant-component subclass

This pays a strictly larger component subclass than the earlier A42
cut-relative estimate. Fix p>1/2 once and, for each original record
with source birth c=max(y,z), define

    L(c)=ceil(c(log c)^p)+1.

Six-distinctness gives c>=4. Select exactly the original components
k>=L(c). The selected price of one physical record is

    de sum_(k=max(r,L(c))..M)lambda_k,              (A53.1)

with an empty sum if the lower limit exceeds M. This is a component
portion of the original price, not a replacement for u_r^[M].
The original alpha_(M+1), output horizon T and all strict gates persist.
The cutoff depends on c, so this portion retains the entire physical
cut interval[c+1,i-1].

There is an actual source-birth mass bound. Write U for the sum of
positive differences of the first c-1 points, G for the sum of the
c-1 new differences ending at c, and S_new for their squared sum.
Sidon makes the old and new label sets disjoint. Hence

    F_c-F_(c-1)=U G+(G^2-S_new)/2.

The actual old diameter estimate gives U<=(c-1)^2 H_c/4, while
G<=(c-1)H_c and S_new>=0. Consequently

    F_c-F_(c-1)
      <=(c-1)^2(c+1)H_c^2/4
      <=c^3 H_c^2/4.                              (A53.2)

Every original record born at c injects into one of these newly born
ordered source pairs. Thus its total de is at most this increment,
not a separate budget for each cut or each output.

If L(c)<=M, nondecreasing denominators and the original tail give

    u_L(c)^[M]<=alpha_L(c)/H_L(c)^2
      <=1/[c^4(log c)^(4p)H_c^2].                 (A53.3)

Here L(c)-1>=c(log c)^p and H_L(c)>=H_c. If L(c)>M the selected
contribution is0 and the estimate is unnecessary.

Group SOURCE births, rather than cuts, into
2^ell<=c<2^(ell+1), ell>=2. Let E_ell be the sum of A53.1 prices
over all original records in that group, each physical price once.
By A53.2--A53.3 and sum_(c in group)1/c<=1,

    E_ell<=1/[4(ell log2)^(4p)].                   (A53.4)

For this group the original strict inequality r<c log c, together
with c<b<i<r, confines every contributing cut to

    2^ell<b<2^(ell+1)(ell+1)log2.

Its TOTAL harmonic cut weight is at most log(2(ell+1)log2), by the
integer integral comparison from the lower endpoint2^ell; no extra
endpoint term is required. The group's profile at any cut is <=E_ell,
so its entire square-root harmonic norm is at most

    log(2(ell+1)log2)/[2(ell log2)^(2p)].

This uses one common price mass and accounts for its whole cut span.
It does not treat different cuts as independently available budgets.
Finally sqrt subadditivity over the birth groups proves the UNIFORM bound

    N_source-birth-far(M,T)
      <=K_p^birth
      :=[1/(2(log2)^(2p))]
          sum_(ell=2..infinity)log(2(ell+1)log2)/ell^(2p)
      <infinity.                                 (A53.5)

Convergence is elementary since2p>1. This holds for every actual finite
integer Sidon history and both original horizons, without using a cap.
For example p=5/8 is fixed henceforth. This is a proved summable
square-root norm, not merely bounded total block mass.

Since c<b and x(log x)^p increases for x>=4, every A42 cut-distant
component is also source-birth-distant. A53 therefore supersedes that
paid subclass with the same p; overlapping payments need not be added.
After removing A53, remaining components obey

    k<ceil(c(log c)^(5/8))+1,
    c>(k-1)/(log(k-1))^(5/8).                     (A53.6)

Indeed integer k gives k-1<c(log c)^(5/8), while c<k-1.
The cut-distant exclusion now holds automatically for such a record
at every b>c. In A52 the distant-rank condition can no longer delay
this record beyond its source birth; the near-span condition may still
do so. The fixed C,m0 cap, all intermediate ranks, original strict
conditions and previously paid subclasses are unchanged.

The uniform norm of the remaining near-span, short-rank-excluded,
large-label/gap profile with the new source-birth restriction is unproved.
Neither CoreUniform nor original Q1 is proved or refuted. A53's actual
birth-product arithmetic has a supporting Lean statement; the full
source injection, genuine-tail bound, group coverage and convergent norm
are independently reviewed hand proofs, not a final Lean Q1 theorem.

## A54. A new uniformly paid source-birth far-span subclass

Fix q>1 once. Select the original components satisfying

    H_k>=H_c(log c)^q,  c=max(y,z).

The selected price of a physical record is exactly
de sum_(k=r..M, H_k>=H_c(log c)^q)kappa_k/H_k^2.
If there is no such component the sum is0. No first qualifying rank,
continuation of the history or new price convention is assumed.
Since r>=c+2 and the selected denominators are large,

    selected price
      <=de alpha_(c+2)/[H_c^2(log c)^(2q)]
      <=de/[c^4 H_c^2(log c)^(2q)].                (A54.1)

The original terminal alpha_(M+1) remains in every exact price;
discarding it is only an upper inequality in A54.1.

Combining the actual birth increment A53.2 with the SAME single-price
source-birth grouping and physical cut support gives

    E_ell^span<=1/[4(ell log2)^(2q)],
    N_source-birth-far-span(M,T)
      <=K_q^span
      :=[1/(2(log2)^q)]
          sum_(ell=2..infinity)log(2(ell+1)log2)/ell^q
      <infinity.                                 (A54.2)

This proves a uniform square-root harmonic norm for all actual finite
integer Sidon histories and both horizons. No cap is required. The
convergence uses q>1, not bounded total I_ell alone. Take q=2 henceforth.

For every cut b>c, H_b(log b)^2>=H_c(log c)^2. Thus A54 includes
the former A33 cut-far-span subclass. After this new payment the
remaining components obey

    H_k<H_c(log c)^2.                              (A54.3)

Together with A53.6 this makes both A52 common activation conditions
automatic at every physical cut b>c. In the new remainder they cannot
cause a delayed entry after source birth.

More explicitly, at fixed k let v=min(k,T) and restrict the common
old ordered-source-pair bank by the STATIC birth conditions

    c<=v-2, k<L(c), H_k<H_c(log c)^2.

Additional fixed exclusions, such as source overlap or s<m0, may be
kept or omitted only as a nonnegative upper allowance. Let Bnear_(b,k)
sum de over this bank with c<b. The actual remaining Q is a subset.
For b>=max(4,m0), all remaining displayed cut selectors only retire
records, by A52's monotonicity proof. Therefore

    Bnear_(b,k)-Q_new_remaining(b,k)
      is nonnegative and nondecreasing in b.      (A54.4)

Its labels start at their source birth (or the initial cut boundary),
and an accepted component has a single initial active interval or none.
The same fixed-lambda_k sum preserves this assertion, with k>T retained.
This does NOT assert monotonicity after dividing by Bnear or replacing
the fixed component sum by a moving-tail allowance; A50 identifies
the missing terms in those transfers.

The new payments may be taken before overlapping A42/A33 payments,
so there is no repeated physical budget. Original cap, gates and
component prices are unchanged. The near-birth component norm, and
hence CoreUniform and original Q1, remain unproved. A54 and its actual
remaining-bank consequence are reviewed hand mathematics.

## A55. Full genuine prices with a short birth-to-upper-output delay

Fix q>2/3, and retain exactly the original records with

    r-c <= R_c := floor(c/(log c)^q).                       (A55.1)

This is a selected subclass, not a change to the frozen predicate. Its
profile uses the FULL original de*u_r^[M] on c+1,...,i-1, including
every genuine k>T term. Its norm is uniformly bounded, without a cap.

### Actual one-fresh-source count

The four old endpoints are distinct, and their largest rank is c.
Exactly one of the two old differences has upper endpoint c. Fix an
actual ordered output (i,r), hence its positive label t=a_r-a_i.
If the larger old difference is new, choose x<c: d=a_c-a_x and e=d-t
are forced. If the smaller is new, choose w<c: e=a_c-a_w and d=e+t
are forced. Positive-difference uniqueness recovers the other source
endpoints. There are at most2(c-1) records for this fixed output.
The two cases cannot overlap, because both sources ending at c would
violate four-distinctness. Extra gates can only reduce this count.

Under A55.1 both output endpoints belong to the actual ranks
c+1,...,min(c+R_c,T). Hence there are at most binom(R_c,2) output
pairs and the total de of selected records born at c is at most

    (c-1)R_c(R_c-1)H_c^2 <= c R_c^2 H_c^2.                (A55.2)

If R_c<=1 there are no such pairs. Since every existing record has
r>=c+2, the original tail, without changing alpha_(M+1), obeys

    u_r^[M] <= alpha_r/H_r^2
             <= alpha_(c+2)/H_(c+2)^2 <=1/(c^4 H_c^2).

Consequently the sum of full physical prices born at c is at most
R_c^2/c^3 <=1/[c(log c)^(2q)]. This counts one price per record,
not one allowance per cut.

### Coverage supplies the additional summable factor

Group source births in 2^ell<=c<2^(ell+1), ell>=2. Let P_ell be
their selected full-price profile and E_ell their one-price mass.
The elementary sum of1/c over this group is at most1, so

    E_ell <=1/(ell log2)^(2q).

For each record its exact harmonic coverage satisfies

    sum_(b=c+1..i-1)1/b <=(i-c)/c <=R_c/c
                         <=1/(ell log2)^q.                (A55.3)

Because log c>1 and q>0, R_c<=c. The whole birth group's actual
cut support lies in 2^ell<b<2^(ell+2), with harmonic weight at most
2log2. Exact physical coverage, followed by weighted Cauchy, gives

    sum_b P_ell(b)/b <=1/(ell log2)^(3q),
    sum_b sqrt(P_ell(b))/b <=sqrt(2log2)/(ell log2)^(3q/2).

Finite square-root subadditivity over birth groups proves

    N_short-upper <= sqrt(2log2)/(log2)^(3q/2)
                    *sum_(ell>=2)ell^(-3q/2) < infinity.  (A55.4)

This proof retains both original horizons, actual finite cuts and
the original full price. No extension to a missing rank is used.
For q=3/4, the integral upper bound for the series gives the explicit
constant 8sqrt2/(log2)^(5/8).

### Independent exact saved-record check

The previously saved original record
[215,174,14,19,21,24,24,19,27,28,41] has c24,i27,r28 and physical
coverage 1/25+1/26=51/650. Two rational-log implementations certify
R24=10, so its delay4 puts the ENTIRE record in A55, including its
component k48. At cut25 the A43 threshold is also10, while k-b=23;
the A43 component selection alone did not pay this component.
The fixed C1,m02,M=T96 history is reused. There is no new history,
profile sweep or asymptotic inference. UNKNOWN=0. Evidence is
finite_campaign/A55_SAVED_WITNESS_EXACT.json and its saved checker.

The full proof passed independent mathematical review in
finite_campaign/A55_FULL_PRICE_SHORT_OUTPUT_DELAY_REVIEW.md.
The actual fresh-source injection and full norm are not yet Lean
formalized. This removes a genuine class, not the whole frozen core.

## A56. Full prices with a short birth-to-lower-output delay

Fix q>1 and now select original records only by

    i-c <= R_c := floor(c/(log c)^q).                       (A56.1)

No new upper bound on r is imposed. In particular this is a different
full-record class from A55. For each actual upper output r, there are
at most R_c possible lower outputs i and at most2(c-1) source pairs
per output by A55's actual injection. Thus the price mass born at c
is bounded by

    2(c-1)R_c H_c^2 sum_(r=c+2..T)u_r^[M]
      <=2c R_c sum_(r=c+2..T)alpha_r <=2R_c/(3c^2).
                                                               (A56.2)

For the last step, for every real n>=1,

    alpha_(n+2)=1/[(n+2)^2(n+1)^2]
       <=(1/n^3-1/(n+1)^3)/3.                              (A56.3)

After positive common denominators, the difference has numerator
12n^3+25n^2+16n+4. The finite sum for integer n=c,...,T-2 telescopes
to at most1/(3c^3). Empty sums contribute zero. Here alpha_r is an
upper bound on the genuine tail after H_r>=H_c; it is not a replacement
of any original record price. In particular k>T and alpha_(M+1) were
retained before the bound. A56.3 has also passed a concrete Lean check.

In a dyadic birth group, A56.2 gives
E_ell<=(2/3)/(ell log2)^q. The actual physical interval is still short:
its harmonic coverage is at most1/(ell log2)^q and the group support
is still 2^ell<b<2^(ell+2). The size of r does not enlarge the record's
cut interval. Exact coverage and Cauchy now give

    N_short-lower <=2sqrt(log2/3)/(log2)^q
                   *sum_(ell>=2)ell^(-q) < infinity.      (A56.4)

For q=5/4, this is at most8/[sqrt3 (log2)^(3/4)]. The proof holds
for every actual finite integer Sidon history and both original
horizons, without a cap. No growing-prefix assumption enters it.
Independent review is
finite_campaign/A56_FULL_PRICE_SHORT_LOWER_OUTPUT_DELAY_REVIEW.md.
Only the coefficient step A56.3 is formalized; the full record count,
genuine-price bound, coverage and convergent norm remain hand proofs.

## A57. Joint delay product gives a larger uniformly paid class

Fix eta>0, put nu=2+eta and q=nu/2>1. For a physical record put
x=(i-c)/c and y=(r-c)/c. Select the FULL original price precisely when

    x^2 min(1,y) <=1/(log c)^nu.                            (A57.1)

This is a sufficient paid subclass. It is not the frozen statement.
For y>1, A57.1 implies x<=1/(log c)^q, so A56 pays this part.

For 0<y<=1 use the disjoint actual dyadic bins

    2^(-h-1)<x<=2^(-h),  2^(-l-1)<y<=2^(-l),
    h,l nonnegative integers, h>=l.

The last relation follows from x<y. At birth c there are at most
c*2^(-h) lower outputs and c*2^(-l) upper outputs in these bins.
The one-fresh-source injection and the same full-tail bound as A55
therefore bound this cell's full physical price mass by
2^(1-h-l)/c. The eligible A57.1 subcell is a subset, so the same upper
bound applies. In birth group ell, its mass is at most2^(1-h-l),
each record's physical harmonic coverage is at most2^(-h), and its
whole cut support has weight at most2log2. Hence

    N_(ell,h,l) <=2sqrt(log2)*2^(-h-l/2).                 (A57.2)

Put s=2h+l and D_ell=nu*log_2(ell log2)>0. Eligibility and the
STRICT lower ends of the dyadic bins imply

    x^2 y >2^(-s-3),
    s>nu*log_2(log c)-3 >=D_ell-3.

Thus s>=S_ell=max(0,floor(D_ell-3)+1). There are at most s+1
pairs(h,l) for a fixed s, even before imposing h>=l. With rho=1/sqrt2,
the exact geometric-tail identity gives

    sum_(s>=S)(s+1)rho^s
       =rho^S[(S+1)/(1-rho)+rho/(1-rho)^2]
       <=(S+1)rho^S/(1-rho)^2.

Here S_ell+1<=1+D_ell and, since S_ell>D_ell-3,
rho^S_ell<=2^(3/2)/(ell log2)^(nu/2). Consequently

    N_ell,short <=2^(5/2)sqrt(log2)/(1-1/sqrt2)^2
           *[1+nu log_2(ell log2)]/(ell log2)^(1+eta/2).
                                                               (A57.3)

The sum of A57.3 over ell>=2 converges. Adding the finite A56(q)
constant for y>1 proves a uniform bound on the A57 full-price norm
for every eta>0, independently of C,m0,M,T and the actual history.
There are only finitely many occupied bins in each actual history;
the nonnegative infinite geometric majorants do not posit any extra
record or extension. Original six-distinctness, cuts and genuine
prices are retained throughout the selected profile.

Fix eta=1/4. The resulting paid class contains A55(q3/4), since
x<y<=log^(-3/4)c implies x^2 y<=log^(-9/4)c. It also contains
A56(q5/4), since x^2 min(1,y)<=x^2<=log^(-5/2)c<=log^(-9/4)c
for c>=4. Thus the prior saved c24 record is paid by inclusion;
there is no need to rerun its checker for this corollary.

### Exact limit of this estimate and remaining geometry

Setting eta=0 in this argument would leave a numerical majorant
of order (1+log ell)/ell, whose series diverges. Therefore this
particular summation does NOT prove the critical product class.
It does not show that this class, the frozen statement or Q1 is false.
The information relaxed here is the simultaneous compatibility of
all fresh-source/output cells: cell capacities are summed independently
after the valid actual injection. No matching or independence of their
unused budgets is asserted, and bounded total mass is never used as a
substitute for the square-root norm.

After paying A57(eta1/4), the existing A53/A54 near-birth remainder
may be restricted, without changing the original theorem, to

    (i-c)^2 min(c,r-c) > c^3/(log c)^(9/4),              (A57.4)
    k<ceil(c(log c)^(5/8))+1,  H_k<H_c(log c)^2,

together with all original strict gates, every A46.6 surviving
condition and the same all-rank C,m0 cap. A57.4 is a static record
condition, so the retirement-only cut geometry of A54 persists.
The uniform norm of this complement is still unproved. Independent review passed in
finite_campaign/A57_DELAY_PRODUCT_CLASS_REVIEW.md. The full norm is
not Lean verified.

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

A26 now gives the exact signed integer-threshold representation and
rejects one-use charging by a strict-core fixed-cap example. A27 proves
actual two-coordinate occupancy and a genuine horizon-uniform norm
bound for each fixed middle pair. Adding the unrestricted pair budgets
loses joint support and has a growing explicit majorant. A28 retains
common outputs across different middle pairs, proves the oriented
energy kernel and integer-output packing bound, and improves the scalar
cap saving to order log^(-6). The new scalar majorant still does not
control the norm when actual forbidden labels and endpoints are lost.

A29 has now retained the actual forbidden old labels, with an exact
prefix-capacity formula and four certified component checks. A30 proves
simultaneous squared-source/forbidden-capacity compression, but its
relaxed comparison sets lose actual additive endpoint relations. A31
uses those relations through finite sliding-window energy and the
fixed cap, obtaining an actual positive price-weighted loss. Reducing
that loss to its scalar lower bound still leaves the constant norm
obstruction. None of these results supplies CoreUniform.

A32 now retains the actual mixed pair bank and rejects immediate full
payment by exact finite examples. A33 uniformly pays all far components
H_k>=H_b(log b)^2, leaving the original all-large-old-gap near component
norm. A34 proves exact deferred penalties and a conditional finite rank
at which all become full, within the near class after an explicit cap
threshold. A35 retains both horizons in the price transform and pays
fixed terminal strips. Its bound for all unsaturated cuts still grows
like log log T. No result assumes that a given prefix extends further.

A36 proves the exact physical mixed-pair cut law: relative payment
fractions decrease at fixed threshold, while actual examples refute
three stronger raw/source-weighted monotonicity claims. A37 pays the
threshold-removal error uniformly. A38 then represents each physical
pair's genuine harmonic loss by one positive prefix-interval measure.
A39 rejects charging each record solely to its own eligible output
mixed labels. A40 keeps differences BETWEEN mixed labels, obtains a
full-core linear-future-size bound, and uniformly pays far component
ranks k>=ceil(b(log b)^(3/4))+1. The remaining near component norm is
unproved even with the original fixed cap at every intermediate rank.

A41 now gives the actual strict-path decomposition, an explicit
fixed-cap length bound and persistent path terminals. Three exact
cells contain only matching strict graphs; no general matching claim
follows. Adding independent terminal allowances leaves the explicit
constant-profile obstruction A41.6. A42's common ordered source-pair
bank supersedes A40's scalar bound and pays distant ranks for every
fixed p>1/2. A43 also pays the short component interval next to each
cut. The remaining band is A43.3, with unchanged large-old-gap and
near-span conditions. Its full norm is unproved.

A44 now refutes matching across all shifts at one physical terminal,
including an A45-remainder column witness. Fixing the old source pair
instead gives a valid degree-one old-source graph and exact price-weighted
transport. Replacing each row by its independent full transport still
leaves a constant profile bound. A45 pays all small second-source labels
and uses the actual fixed cap to localize both source upper ranks. A46
pays cut-relative small output differences and small adjacent old gaps.
Its narrower remainder is A46.6. The prescribed single terminal still
has one original record after these deletions, so it is not vacuously
removed there; the two-edge matching witness does not survive that last
selection. No matching claim is inferred for this narrower remainder.

A47 has now evaluated the prescribed actual bin and its common use
across output rows. Its strict finite witnesses reject both automatic
one-row use and independent row-deficit addition. A48 proves that generic
Sidon window capacities, even with common top weights, are weaker than
the already available joint bank. A49 rules out confusing difference
higher energy with six-variable three-sum energy, even up to a constant
on bare finite Sidon sets. Neither near-extremal Fourier error nor a
frozen uniform norm was obtained from the checked sources.

A50 proves the raw common-bin moving-cut law and refutes its normalized,
selector-adjusted and moving-tail transfers by exact actual examples.
A51 supplies the missing birth-fixed price compensation. A52 proves
that the displayed remaining selector has one common activation and
one active interval per physical record/component, yielding a correct
positive auxiliary potential but only a logarithmic allowance bound.

A53 now uniformly pays source-birth-distant components k>=L(c), with
p5/8, and A54 uniformly pays Hk>=Hc(logc)^2. These supersede the older
cut-distant and cut-far-span payments. In the new remainder, both common
activation conditions are automatic after source birth. The remaining
static near-birth source bank has a valid nondecreasing raw deficit;
normalized or moving-tail monotonicity is still not inferred.

The residual class is A46.6 together with A53.6 and A54.3. The original
strict gates and fixed all-rank C,m0 cap persist; the uniform residual
norm is still unproved. All three A50 component48 records are newly
paid by A53: L22=46,L23=48. A separate bounded original-pool pass stopped
at its first residual witness, bank index1487:
[215,174,14,19,21,24,24,19,27,28,41], cut25,k48,c24,L24=51,de37410.
Its old gaps are(215,139,174), and H48=4248<713(log24)^2. The independent
checks have UNKNOWN0; the additional span flag uses only this same record.
This is a nonempty finite remainder, not an asymptotic counterexample.

A55 and A56 now pay the full-price short upper/lower output-delay
classes. A57 unifies and enlarges them: with eta=1/4, all records
satisfying (i-c)^2 min(c,r-c)<=c^3/(log c)^(9/4) are uniformly paid.
These are reviewed hand proofs; the A56 coefficient tail step has
one new pinned Lean supporting theorem. The c24,r28 record above is
now paid in its entirety, including k48; it is historical evidence
of the former remainder, not evidence that the new remainder is
nonempty. No new profile search is claimed.

The current remainder is A46.6, A53.6, A54.3 and A57.4 together,
with every original strict gate and the same fixed all-rank cap.
The exact endpoint eta=0 is unproved: the present cell summation
has a divergent (1+log ell)/ell upper majorant. That is a limit of
this estimate and not an actual counterexample.

The next nonduplicate action is an actual fixed-birth source/output
graph attack in this remainder. For the orientation d=a_c-a_x>e,
fix c and one smaller physical old source e=a_z-a_w; vary x and the
actual output (i,r) with a_c-a_x=e+a_r-a_i. Test the degree-one
claims separately in the lower and upper output ranks by literal
Sidon recovery, then derive the original price-weighted path balance.
Use the same fixed cap at actual existing output ranks to test whether
common physical e-banks give a summable bound. Compare against the
independent-bank relaxation explicitly; do not assume a matching
across different e or replace their common unused budget by row sums.
Handle the other orientation separately instead of asserting symmetry
without checking its equation. This is a proposed attack, not an
accepted norm estimate. No new history or full profile scan is needed.

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

Continuation 07 adds A26--A28. Two new supporting statements verify the
signed integer-tail first moment and ordered-pair recovery from the
unchanged literal Sidon predicate. The current pinned source/type/axiom
binding is `LEAN_VERIFICATION_07.json`, with24 supporting theorems.
The reviewed two-coordinate record bound, full genuine fixed-pair norm,
oriented-output bound, integer packing and majorant limits are hand
proofs; they are not full Lean core-norm theorems. The previous22-theorem
source and audit are preserved in `source_snapshot/continuation_07/`;
`LEAN_VERIFICATION_06.json` is the corresponding historical binding.

Continuation 08 adds A29--A31. The two new supporting statements are
the exact integer-kernel prefix identity and the bound for selecting
at most h allowed labels. Their current pinned source/type/axiom binding
is `LEAN_VERIFICATION_08.json`, with26 supporting theorems. Natural
subtraction makes labels above H contribute zero; real normalization
by H and full Sidon/core instantiation remain in the hand proof.
The existing `internalLabels_disjoint` source was located and reused
as mathematics; it was not rebuilt, duplicated or counted as a new
statement here. The actual compression and sliding-window/cap proofs
are independently reviewed hand mathematics, not full Lean core-norm
theorems. The previous24-theorem source/audit are preserved in
`source_snapshot/continuation_08/`, bound historically by
`LEAN_VERIFICATION_07.json`. No old library, Target, toolchain or
default build target was changed.

Continuation 09 adds A32--A35. One new generic supporting statement,
`priced_component_far_bound`, proves the denominator comparison used
in A33 with explicit nonnegativity and far-scale hypotheses. Its current
pinned source/type/axiom binding is `LEAN_VERIFICATION_09.json`, with27
supporting theorems. The full A33 uniform subclass and A34/A35 actual
Sidon/price/cap results are independently reviewed hand proofs; the
generic lemma is not their full formalization. The previous26-theorem
source/audit are preserved under `source_snapshot/continuation_09/`,
with historical binding `LEAN_VERIFICATION_08.json`. The original
Target, toolchain and default build target remain unchanged.

Continuation 10 adds A36--A40. Two new supporting statements verify
integer prefix-capacity deletion and the actual Sidon mixed-shift
rectangle cardinality bound. Their current pinned source/type/axiom
binding is `LEAN_VERIFICATION_10.json`, with29 supporting theorems.
The full actual A36 cut/relative-price theorem, A37 allowance norm,
A38 interval measure and A40 weighted uniform subclass remain reviewed
hand proofs. The previous27-theorem source/audit are preserved under
`source_snapshot/continuation_10/`, with historical binding
`LEAN_VERIFICATION_09.json`. The intermediate28-theorem source and
successful logs were preserved before the new A40 addition. No literal
Q1 theorem, final clean release, target or toolchain change is claimed.

Continuation 11 adds A41--A43. Two new supporting statements verify
the weighted ordered source-pair identity and the finite chain span
balance. Their current pinned source/type/axiom binding is
`LEAN_VERIFICATION_11.json`, with31 supporting theorems. The actual
strict-path/genuine-terminal theorem and the full A42/A43 weighted
subclass norm bounds remain reviewed hand proofs. The previous29-
theorem source/audit are preserved under `source_snapshot/continuation_11/`,
with historical binding `LEAN_VERIFICATION_10.json`. No original
library, Target, toolchain or default build target was changed.

Continuation 12 adds A44--A46. One new supporting statement,
`source_row_endpoint_recovery`, uses the unchanged literal Sidon predicate
to recover all endpoints when two fixed-source-row equations share a
lower or upper old endpoint. Its current pinned type/axiom binding is
`LEAN_VERIFICATION_12.json`, with32 supporting declarations. The actual
row transport, full genuine prices, new uniform subclass norms and cap
birth-support corollary remain reviewed hand mathematics. The previous31-
theorem source/audit are preserved under `source_snapshot/continuation_12/`,
with historical binding `LEAN_VERIFICATION_11.json`. No literal Q1 proof,
final clean closure, original Target, toolchain or default-target change
is claimed. The central complement A46.6 remains unproved.

Continuation 13 adds A47--A49. The new supporting statement
row_window_capacity_dominated verifies the real algebraic capacity
comparison. The current pinned source/type/axiom binding is
LEAN_VERIFICATION_13.json, with33 supporting declarations. The complete
actual bin/window, common-weight and energy arguments remain independent
hand/finite reviews, not full formalizations. The previous32-declaration
source/audit are preserved under source_snapshot/continuation_13/ with
historical binding LEAN_VERIFICATION_12.json. The unchanged Target and
toolchain were reused; no final Q1 clean closure is claimed.

Continuation 14 adds A50--A54. Two new generic supporting statements,
interval_deficit_mono and source_birth_product_bound, are pinned Lean
verified. LEAN_VERIFICATION_14.json binds35 supporting declarations.
The full source-pair injection, actual price potentials, selector geometry,
and the two new convergent uniform subclass norms remain independently
reviewed hand proofs. The previous33-declaration source/audit are in
source_snapshot/continuation_14/; the intermediate34-declaration files
were also preserved before the A53 addition. Original Target, toolchain
and default build target are unchanged. No literal Q1 proof or final
clean dependency/axiom closure is claimed.


Continuation 15 adds A55--A57, three full-price uniform subclass hand
proofs using the actual fresh-source/output count and physical coverage.
Independent review passed. One new supporting lemma alpha_cube_tail_step
formalizes A56's numerical finite-telescope coefficient comparison.
LEAN_VERIFICATION_15.json binds36 supporting declarations and successful
pinned source/type/axiom logs. The complete fresh-source injection,
full-price norm/series and A57 joint-bin summation are not formalized.
Previous35-declaration source/audit and other current mutable sources
are preserved under source_snapshot/continuation_15/. Only the same
saved record was checked with independent exact logs; no new history or
full profile sweep. Original Target, toolchain and default target remain
unchanged; literal Q1 and final clean dependency closure are unproved.

Read this file and `ATTEMPTS.jsonl` at restart; use the source manifest only
to locate unchanged originals. Reuse the already certified finite campaign
when testing a concrete new inequality. Do not repeat Gate 0, the old
declaration inventories, the C143 campaign, or environment design.
