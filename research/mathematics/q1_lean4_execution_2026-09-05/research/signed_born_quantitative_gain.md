# Quantitative growth of full signed Born mass and its fixed birth prices

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** The full raw signed Born sum has a quantitative lower
bound at actual good epochs. Under one fixed eventual critical cap,
both its direct birth-price sum and its compatible-layer birth-price
sum diverge. This gives a divergent historical saving for the fixed
sources in signed_causal_source.md. It does not bound their remaining
physical capacity-minus-demand margin and does not resolve original Q1.

This note independently derives the finite energy comparison, its
constants, and the monotone Abel argument. The six-endpoint identities
were proposed and independently derived by the parent and the linear
agent; the non-six-endpoint constant 12 was independently checked here
and by /root/moment_evidence_audit. That agent recorded the full
fiber derivation in signed_retirement_fibers.md, whose complete source
was read at SHA256
f0af16b2191f732af18f266425eadb33ac914d37f05d7ccaaf3f767414730d1a.
Its later-source-clock wording was subsequently clarified without
changing formulas; that paragraph was read and the updated source
was hash-bound at
af256edc1cd1812a9069823b906f89328de6fb85aec6e087a7ff6a4a851cc8c9.

The full signed Born theorem is the reviewed
signed_bank_born_positivity.md, SHA256
ff32b2cab2234f21cc727f4b639d57d2cfe136f456526a0adb8d754779cc19e1.
No numerical experiment, previous-test rerun, Lean edit, or formal
verification is used. In particular no positive-bank causal diagonal
or positive-bank energy Abel formula is imported.

## 1. Full signed functionals and an exact energy identity

Let P_N={a_1<...<a_N} be an actual integer Sidon prefix, with
repeated two-sums included in its Sidon property. Set

~~~
F_n=Delta P_n,       Fhat_n=F_n union(-F_n),
Q_n=|Fhat_n|=n(n-1), H_n=a_n-a_1.
~~~

For each nonzero signed label d, use its actual birth
tau(d)=tau(-d), and the permanent feature g(d)=d. Extend g by
zero outside Fhat_N when taking a convolution. For an unordered
pair of distinct signed sources {d,e} whose output t=|d-e| belongs
to F_N, put b=max(tau(d),tau(e)) and r=tau(t). Define

~~~
B_N=sum_(used pairs, r<=b) de,
R_N=sum_(used pairs, b<r) de,
Z_N=sum_(d in Fhat_N)d^2,
E_N=||1_(P_N)*g_(Fhat_N)||_2^2.                  (1)
~~~

The full definitions include same-birth signed source pairs.
Set B_1=0. Actual Sidon uniqueness and expansion of the convolution
give the exact identity

~~~
E_N=N Z_N+2B_N+2R_N.                             (2)
~~~

Indeed each positive difference of P_N occurs once; its correlation
is the sum over all signed source pairs with that output. The
diagonal of the point-pair expansion is exactly N Z_N.

## 2. Six-endpoint fibers and the finite retirement error

For a numeric Schur triple x<=y,z=x+y in F_N, the union of
endpoints in its three actual positive-difference representations
is the same for every associated signed source pair. Hence the
partition into six-distinct-endpoint groups and its complement
retains each full numeric Schur group. In particular

~~~
B_N=B_core+B_non6,             B_non6>=0.         (3)
~~~

This nonnegativity is the full signed Born theorem, not a
termwise assertion about its individual signed source products.

Here is the fiber calculation establishing the needed core bound.
Take disjoint triples U={u_1,u_2,u_3} and V={v_1,v_2,n} of
actual point coordinates, with equal sum and with n their largest
coordinate. Write mu for their common mean, n'=n-mu, and

~~~
sigma_U^2=sum_(u in U)(u-mu)^2,
sigma_V^2=sum_(v in V)(v-mu)^2.
~~~

Each of the six endpoint matchings U->V produces three nonzero
signed gaps summing to zero, hence one numeric Schur triple.
These triples are distinct: their three magnitude labels recover
their endpoint edges by Sidon uniqueness and hence the matching.
Their magnitudes cannot coincide, since the endpoint edges are
distinct. Thus no doubled numeric label occurs in this core.

For a matching in which u is paired to n, the edge magnitude
n-u has the unique latest clock. The full Born contribution of
that Schur triple is 2(n-u)^2. There are two matchings for each
choice of u. Consequently

~~~
B_fiber=4sum_(u in U)(n-u)^2
       =4sigma_U^2+12n'^2.                       (4)
~~~

Every such triple has four Born signed pairs and two retired
signed pairs. This accounts for 24 Born and 12 retired records.
All Born records have later source birth equal to the rank of n;
all retired records have output birth equal to that rank. Their
retired source births may be smaller and are not replaced by n.

For three signed gaps summing to zero, the sum of the full signed
Born and retired contributions is the sum of the three gap squares.
Each endpoint pair u in U,v in V occurs in two of the six
matchings. Therefore

~~~
B_fiber+R_fiber=2sum_(u in U,v in V)(u-v)^2
              =6(sigma_U^2+sigma_V^2),

R_fiber=2sigma_U^2+6sigma_V^2-12n'^2.             (5)
~~~

The other two centered elements of V have sum -n' and each is
at most n'. Each therefore lies in [-2n',n'], and maximizing
their squared sum at the endpoints gives sigma_V^2<=6n'^2.
It follows that

~~~
R_fiber<=2sigma_U^2+24n'^2<=2B_fiber,
R_core<=2B_core.                                (6)
~~~

There is no assertion R_fiber<=0.

For completeness, the repeated-endpoint retirement bound is

~~~
sum_(non6 retired pairs)|de|<=12N^3 H_N^2,
in particular |R_non6|<=12N^3 H_N^2.             (7)
~~~

To verify its counting constant, expand the relation between three
physical differences into equality of two three-term point multisets.
In a retirement, its unique latest endpoint occurs in the output
edge, and is absent from the two source edges. Thus the two
multisets cannot coincide. Distinct equal-sum three-multisets have
disjoint supports: a common element would cancel to equal
two-sums, forcing equality of the remaining multisets by Sidonness.

If the six endpoints are not all distinct, one of those triples
is therefore a repeated multiset {a,a,b}. There are at most N^2
choices of it. At its sum there are at most N partner triples:
their smallest element determines the other unordered pair by
two-sum uniqueness. At most six matchings connect any such
collision, even if its repeated copies are provisionally labeled.
Each matching gives at most two retired signed pairs; doubled
numeric labels can only lower that count. This proves the bound
12N^3 on records, including equal-birth sources. Finally each
product has magnitude at most H_N^2.

This count can overcount collisions with two repeated sides or
matchings with repeated copies. Both overcounts are harmless upper
bounds. It does not discard a potentially positive retirement.

## 3. A full Born lower bound from the energy

Combine (2),(3),(6),(7):

~~~
E_N
 <=N Z_N+6B_core+2B_non6+24N^3 H_N^2
 <=N Z_N+6B_N+24N^3 H_N^2.
~~~

Thus the following finite inequality holds for every actual prefix:

~~~
B_N >= [E_N-N Z_N-24N^3 H_N^2]/6.               (8)
~~~

The complete-Schur nature of (3) is essential for its last step.
An asymmetric deletion of individual source records would not
justify that step.

There is an exact elementary lower bound for E_N. The convolution
in (1) is supported on the integer interval

~~~
[a_1-H_N,a_1+2H_N],       T_N=3H_N+1.
~~~

Its total mass is zero, and its first moment is N Z_N.
Center the interval at a_1+H_N/2 and use its exact coordinate
square sum T_N(T_N^2-1)/12. Cauchy gives

~~~
E_N >=12N^2 Z_N^2/[T_N(T_N^2-1)].               (9)
~~~

No zero-shadow claim at points of P_N is used. This is smoothing
by the old prefix itself, not the compatible future-block problem.
For integer H_N>=1,

~~~
T_N(T_N^2-1)=27H_N^3+27H_N^2+6H_N<=60H_N^3.     (10)
~~~

## 4. Quantitative good-prefix gain

Assume at this rank that

~~~
Z_N>=eta Q_N H_N^2,
H_N<=C_cap N^2 log(2N),                         (11)
~~~

where eta>0 and C_cap>0 are fixed. The elementary upper bound is
Z_N<=Q_N H_N^2. Set

~~~
w_N=1/(Q_N^2 H_N^2).
~~~

Equations (8)-(11) imply

~~~
w_N B_N
 >= eta^2/[30 C_cap log(2N)]
       -1/[6(N-1)]-4N/(N-1)^2.                  (12)
~~~

The error is O(1/N), with explicit constants. For example its
absolute value is at most 49/(3N) for N>=2. Thus the positive
reciprocal-log term eventually dominates at every such good rank.

For the existing two-lookahead good epochs, write N=2p with
p=2^k. Their actual shape assumptions include

~~~
H_p>=2H_(p/2),      H_N<=32H_p,
H_(2N)<=32H_N.                                  (13)
~~~

The reviewed signed-versus-class-variance comparison already
supplies eta=2^-17 in (11). One can also prove a stronger raw
second-moment constant directly: the p^2/2 positive cross gaps
from indices 1,...,p/2 to p+1,...,2p have size at least H_p/2.
After including both signs,

~~~
Z_N>=p^2 H_p^2/4
    >=N^2 H_N^2/(16*32^2)
    >=Q_N H_N^2/(16*32^2).                     (14)
~~~

Thus eta=2^-14 is also valid under (13). Either fixed choice
can be used consistently in (12) and the conclusions below.

## 5. The full Born cumulative sum is monotone

Let ell_b be the full raw Born contribution of all source pairs
whose later source birth is b. In any numeric Schur group, every
Born record has later source birth equal to the maximum clock of
the group's three labels. All of its Born records appear at that
same stage. The reviewed full signed theorem shows their sum is
nonnegative, for every latest-clock pattern and for doubled labels.
Therefore

~~~
ell_b>=0,          B_N=sum_(b=2..N)ell_b,
B_N-B_(N-1)=ell_N>=0.                           (15)
~~~

A source pair whose output appears later is a retirement and
does not become Born on a later prefix. Same-birth source pairs
are retained in this classification. Equation (15) does not
assume that all individual products at a stage are nonnegative.

For any nonnegative decreasing price sequence c_b, finite summation
by parts is exactly

~~~
B_T(c):=sum_(b=2..T)c_b ell_b
 =c_T B_T+sum_(b=2..T-1)(c_b-c_(b+1))B_b.        (16)
~~~

Every term on the right is nonnegative. This is the elementary
Abel identity for the full monotone Born cumulative sum. It is
not an Abel identity for a convolution energy or a retirement
source-clock/output-clock commutator.

## 6. Divergence at the requested fixed birth price

Use one infinite actual Sidon history with one fixed C_cap and
one fixed onset in the cap (11). Let G be its previously proved
two-lookahead good set of indices k, with old ranks N=2^(k+1).
The good-index result in coherent_birth_linear_envelope.md gives

~~~
sum_(k in G)1/k=infinity,
hence sum_(k in G)1/log(2*2^(k+1))=infinity.     (17)
~~~

The onset and constants are not reselected for a terminal horizon.
The dyadic intervals [N,2N) for these ranks are pairwise disjoint.
If 2N<=T, the terms of (16) over b=N,...,2N-1 give at least
(w_N-w_(2N))B_N, by (15). Moreover

~~~
w_(2N)/w_N
 =(Q_N/Q_(2N))^2(H_N/H_(2N))^2<1/16.
~~~

Discarding all other nonnegative terms of (16) proves

~~~
B_T(w)
 >=(15/16) sum_(good N, 2N<=T) w_N B_N
 ->infinity.                                    (18)
~~~

To conclude the limit, insert (12). The reciprocal-log sum
diverges by (17), while its explicit error sums absolutely over
dyadic N. This proof retains the physical birth price w_b on
every original Born pair; it does not replace a source price by
an output price.

A quantitative rate can be retained if desired. The established
good-index bound is sum_(k in G,k<=J)1/k >=(1/6)log log J-O(1).
Replacing k by k+2 changes this sum by a bounded amount.
Thus for T>=2^(J+2), the same derivation yields

~~~
B_T(w)>=eta^2/[192 C_cap log 2] log log J-O(1).  (19)
~~~

The constants in O(1) may depend on the one cap, its onset,
and the initial history. The statement concerns J, the dyadic
exponent bound; it is not a claim of log log T growth.

## 7. The compatible-layer coefficient also gives divergence

For the fixed complete-history alternative of signed_causal_source.md,
put

~~~
alpha_b=Q_b^-2,   kappa_b=alpha_b-alpha_(b+1),
u_b=sum_(k>=b)kappa_k/H_k^2.
~~~

It is decreasing, and

~~~
u_b-u_(b+1)=kappa_b/H_b^2.                       (20)
~~~

Apply (16) with c=u. On the interval [N,2N) from a good rank,
(13),(15),(20) give

~~~
sum_(b=N..2N-1)(u_b-u_(b+1))B_b
 >=B_N(alpha_N-alpha_(2N))/H_(2N)^2
 >=[15/(16*32^2)] w_N B_N.                     (21)
~~~

Consequently

~~~
B_T(u)
 >=[15/(16*32^2)]sum_(good N,2N<=T)w_N B_N
 ->infinity.                                    (22)
~~~

This is a comparison on the specified good intervals, not an
assertion that u_b is uniformly comparable to w_b at every rank.
The source u is fixed from the complete history; determining it
online from the prefix P_b is a different requirement and is
not claimed. No terminally reselected tail appears in (20)-(22).

## 8. A newly derived full-signed energy Abel identity

The parent additionally proposed the following direct consequence
of (2); its coefficients and clocks are independently checked here.
Write

~~~
v_n=Z_n-Z_(n-1),
rho_n=R_n-R_(n-1),       ell_n=B_n-B_(n-1).
~~~

The increment rho_n consists exactly of retired records at output
birth n. A used pair first appears when the latest of its two
source births and its output birth is reached. For a Born pair
that is its later source birth; for a retired pair it is its
output birth. Subtracting (2) at consecutive prefixes gives

~~~
E_n-E_(n-1)=Dhat_n+2ell_n+2rho_n,
Dhat_n=Z_(n-1)+n v_n.                            (23)
~~~

The factor is n, not n-1. This is a fresh full-signed identity
and includes same-birth signed retirements. It is not obtained by
copying the older positive-bank diagonal.

Since v_n<=2(n-1)H_n^2 and Z_(n-1)<=Q_(n-1)H_n^2,

~~~
w_n Dhat_n<=(3n-2)/[n^2(n-1)]
           =1/(n-1)-1/n+2/n^2,
sum_(n=2..T)w_n Dhat_n<=2zeta(2)-1.              (24)
~~~

Young's convolution inequality, or triangle inequality over the
N translates of g, also gives

~~~
E_N<=N^2 Z_N<=N^2 Q_N H_N^2,
w_N E_N<=N/(N-1)<=2.                            (25)
~~~

With E_1=0, finite summation by parts in (23) is exactly

~~~
A_T(w):=w_T E_T+sum_(n=2..T-1)(w_n-w_(n+1))E_n
       =D_T(w)+2B_T(w)+2R_T^out(w),
D_T(w)=sum_(n=2..T)w_n Dhat_n,
R_T^out(w)=sum_(n=2..T)w_n rho_n.                (26)
~~~

The retirement price in (26) is its actual output birth. It is
not the price at its earlier source birth.

The companion fiber note proves the sharper stage complement bound

~~~
sum_(non6 retired, r=n)|de|<=24(n-1)^2H_n^2.
~~~

Here is the counting refinement. The newest endpoint occurs once
in its triple V. If V is distinct, its old partner must repeat:
there are at most (n-1)^2 choices for that old triple, each with
at most one new partner since the remaining pair sum is unique.
If V repeats, it has the form {a,a,a_n}; there are at most n-1
choices and at most n-1 old partners per choice. At most twelve
retired records per collision gives the displayed constant 24.

At each stage, complete core fibers have the same latest source
price for Born and latest output price for retirement, as in (4)-(6).
The non-six Born remainder at that stage is nonnegative. Therefore

~~~
rho_n<=2ell_n+24(n-1)^2H_n^2,
R_T^out(w)<=2B_T(w)+24sum_(n=2..T)1/n^2,
A_T(w)<=6B_T(w)+50zeta(2)-49.                   (27)
~~~

This is an actual output-priced estimate with an absolutely summable
repeated-endpoint error. It does not assert the same inequality for
retirement source prices.

The following Abel lower-bound argument does not require monotonicity
of E_n. Its Abel interior diverges under the same good-shape assumptions.
On N<=n<2N, squares give Z_n>=Z_N and the actual
lookahead gives H_n<=H_(2N)<=32H_N. Equations (9)-(11) imply

~~~
E_n>=N^2 Z_N^2/(5H_(2N)^3)
    >=eta^2 N^2 Q_N^2 H_N/(5*32^3).
~~~

Thus each good interval wholly inside the Abel sum contributes

~~~
sum_(n=N..2N-1)(w_n-w_(n+1))E_n
 >=3eta^2/[16*32^3 C_cap log(2N)].               (28)
~~~

These positive contributions diverge by (17); the terminal boundary
in (25) stays bounded. Equations (26)-(28) give a second valid proof
of weighted Born divergence. The simpler monotone-Born proof
(15)-(18) has the stronger displayed constants and does not require
this weighted stage estimate.

## 9. What this proves for the physical sources, and what remains

For the requested fixed source matrices

~~~
V_de=alpha_maxbirth,
U_de=w_maxbirth de,          W=V+lambda U,
~~~

the literal historical identity is

~~~
C_T(V)-C_T(W)
 =lambda[tr U_T/2+B_T(w)].
~~~

For each fixed lambda>0, (18) proves that this saving diverges
under the stated single capped infinite history assumptions.
Replacing U by U'_de=u_maxbirth de gives the same statement
with tr U'_T and B_T(u), by (22).

Neither conclusion replicates a physical source budget: each is
one exact capacity difference for a fixed matrix and its literal
restrictions. The new result strengthens a nonnegative historical
saving to a divergent one. It does not bound either source's
remaining capacity, its demand slack, or its baseline margin.
The earlier exact one-budget formulas and their unresolved
capacity-minus-demand inequality are still required for Q1.

In particular there is no inferred nonpositive full retirement
sum. The finite core inequality (6), its explicit complementary
error (7), and the monotone Born Abel identity suffice for the
present conclusion. The original problem remains unresolved.
