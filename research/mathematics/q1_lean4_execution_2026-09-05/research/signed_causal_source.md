# One fixed signed source: exact capacity and compatible layer demands

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** The requested birth-fixed linear source is PSD and
entrywise nonnegative, has exact logarithmic mass and bounded trace,
and has a nonnegative full-Born historical saving. Its full-prefix
mass-plus-first-moment demand is nevertheless eventually negative.
A different, explicitly layered source supports nonsummable demands
from actual good future blocks under one physical budget. That
construction has a remaining capacity-minus-demand obligation; the
capacity itself is provably unbounded. Original Q1 is unresolved.

No numerical test, Lean edit, or new formal verification is used.
The signed Born theorem used below is
signed_bank_born_positivity.md, reviewed source SHA256
ff32b2cab2234f21cc727f4b639d57d2cfe136f456526a0adb8d754779cc19e1.
Its exhaustive Schur partition includes same-birth signed retirements.
Nothing below imports the positive-bank causal diagonal D_n.

## 1. The requested fixed source and its exact prefix invariants

Fix one actual increasing integer Sidon history. Put

~~~
F_n=Delta P_n,  Fhat_n=F_n union(-F_n),
Q_n=n(n-1),     H_n=a_n-a_1,        n>=2,
alpha_n=Q_n^-2, w_n=alpha_n/H_n^2.
~~~

Both signs have the same actual birth tau. Zero is absent.
For distinct or equal signed labels d,e, put b=max(tau(d),tau(e))
and define, once and for all,

~~~
V_de=alpha_b,       U_de=w_b d e,
W_de=V_de+lambda U_de,       0<=lambda<=1.          (1)
~~~

These entries depend only on information at b and never change
under extension. All statements below about an infinite matrix
mean compatible finite restrictions; no bounded operator on an
unspecified infinite Hilbert space is asserted.

For a finite restriction to Fhat_N, a decreasing sequence c gives
the exact nested-prefix decomposition

~~~
c_maxbirth
 =sum_(k=2..N-1)(c_k-c_(k+1)) 1_Fhat_k 1_Fhat_k^T
      +c_N 1_Fhat_N 1_Fhat_N^T.                  (2)
~~~

Apply (2) to alpha for V and multiply the analogous decomposition
for w on both sides by the diagonal matrix with entries d for U.
Thus V,U,W are PSD. Also |de|<=H_b^2, so

~~~
(1-lambda)V_de <= W_de <= (1+lambda)V_de.          (3)
~~~

In particular W is entrywise nonnegative, including at lambda=1.
Every signed birth class sums to zero. Consequently U has zero
row sums on every complete prefix, not just zero total mass.

Write M_N=1^T V_N 1=1^T W_N 1 and
t_N=tr V_N, s_N=tr U_N. For harmonic sums h_N^(r),

~~~
M_N=sum_(b=2..N)(Q_b^2-Q_(b-1)^2)/Q_b^2
   =4[h_N^(1)-h_N^(2)] =4 log N+O(1),

t_N=sum_(b=2..N)2/[b^2(b-1)]
   =2[2-1/N-h_N^(2)] ->2[2-zeta(2)],

s_N=sum_(b=2..N) sum_(d in Ghat_b)d^2/(Q_b^2 H_b^2),
1/2<=s_N<=t_N,        tr W_N=t_N+lambda s_N.       (4)
~~~

The lower bounds t_N,s_N>=1/2 are the rank-two contribution,
where the class is {-H_2,H_2}. Matrix mass is M_N, not M_N^2.
None of these formulas uses a growth cap.

## 2. Literal historical capacity, with every signed pair retained

For t>0 let K_n^A(t) be the sum of fixed entries A_de over unordered
signed pairs in Fhat_n with |d-e|=t. Let r=tau(t) if t belongs
to the terminal positive bank F_N, and r=infinity otherwise.
The source-pair birth is b=max(tau(d),tau(e)).

For every fixed nonnegative matrix A, define

~~~
C_N(A)=sum_(t>0) max_(2<=n<=N) 1[t notin F_n] K_n^A(t).
~~~

The kernel increases with source availability until the output is
used. Therefore its literal physical maximum is exactly

~~~
C_N(A)=sum_(d<e in Fhat_N, b<r) A_de
      =[1^T A 1-tr A]/2-L_N(A),                 (5)
~~~

where L_N(A) is the full Born sum over r<=b. A pair of equal
source birth can satisfy b<r; it remains in (5). There is no
new/new cancellation or imported positive-bank diagonal identity.

The signed Schur theorem gives L_N(U)>=0, since the price w_b
is nonnegative and the raw odd feature d is fixed. Consequently

~~~
C_N(V)-C_N(W)
 =lambda[s_N/2+L_N(U)] >=lambda s_N/2.            (6)
~~~

This is one capacity saving, not a saving to be repeated per row.
No sign for the older positive-bank birth-linear source follows.

## 3. Even the full-prefix first-moment demand is too weak here

Use the entire old restriction at N against an actual compatible
future block B of m points, minimum b_0, and interval length L.
Let Delta B be disjoint from F_N. The signed shadows have common
interval

~~~
J=[b_0-H_N,b_0+L-1+H_N] intersect Z,
T=L+2H_N,         D=T-m.                         (7)
~~~

They vanish on all m points of B, including the smallest point.
Let d denote the vector of signed numeric source labels and put

~~~
Z_n=sum_(d in Fhat_n)d^2,
J_N=d^T U_N d
   =sum_(b=2..N) w_b [Z_b^2-Z_(b-1)^2].          (8)
~~~

Applying Hilbert-space Cauchy to the V-feature channels and the
centered U-feature channels separately gives

~~~
E_B(W_N)
 >=m^2 M_N/D
    +lambda 12m^2 J_N/[T(T^2-1)].

delta_full
 =[m^2 M_N/D +lambda 12m^2 J_N/[T(T^2-1)]
                   -m(t_N+lambda s_N)]/2.       (9)
~~~

The positive part of (9) is paid by the actual nonnegative kernel,
because E_B(W_N)=m tr W_N+2 sum_(t in Delta B)K_N^W(t).
This is a lower certificate, not the full energy.

In each birth stratum, d^2 e^2<=H_b^4. Thus (8) implies

~~~
0<=J_N<=sum_b H_b^2(Q_b^2-Q_(b-1)^2)/Q_b^2
       <=H_N^2 M_N.                             (10)
~~~

For m=N, use L>=N, H_N>=Q_N/2, D>=2H_N>=Q_N, and
T>=2H_N+1. Since T(T^2-1)>=8H_N^3, equations (4),(9),(10)
give the actual upper bound on this specified certificate:

~~~
delta_full
 <={ (1+3lambda)N M_N/(N-1)-N(1+lambda)/2 }/2
 <0 for all sufficiently large N.               (11)
~~~

The first-moment addition does not cure the old trace cost.
This is an analytic statement about the requested actual source,
not a finite example or a claim about every possible demand.

## 4. Why its PSD decomposition cannot be spent layer by layer

Write kappa_k=alpha_k-alpha_(k+1)>0. In the two separate
decompositions of (1), the combined kth layer would be

~~~
kappa_k J_Fhat_k +lambda(w_k-w_(k+1)) d_k d_k^T.
~~~

At its pair {-H_k,H_k}, its entry for lambda=1 is

~~~
kappa_k-H_k^2(w_k-w_(k+1))
 =-alpha_(k+1)[1-H_k^2/H_(k+1)^2]<0.              (12)
~~~

The actual diameter increases strictly. Thus these PSD layers are
not individually nonnegative physical sources. Their positive
demands cannot be assigned independent positive kernel budgets.
Equation (12) is the exact obstruction; PSD alone does not repair it.

## 5. A compatible alternative and its quantifier boundary

For a fixed complete infinite history, define

~~~
u_b=sum_(k>=b) kappa_k/H_k^2,
U'_de=u_maxbirth d e,           W'=V+lambda U'.
~~~

Then

~~~
W'=sum_(k>=2) kappa_k
          [J_Fhat_k+lambda d_k d_k^T/H_k^2].      (13)
~~~

Each displayed component is PSD and entrywise nonnegative.
All sums converge on each finite restriction because
0<=u_b<=alpha_b/H_b^2. The source is chosen once from the complete
history, and all its prefix restrictions are literal restrictions.
It is not an online rule that can determine u_b from P_b alone.
Replacing the infinite tail by a newly chosen terminal normalization
at every horizon would change old entries and is not (13).

The alternative has exactly the same M_N and t_N as (4);
tr U'_N=sum_(d in Fhat_N)u_tau(d)d^2<=t_N.
It is centered on every class. The full Born theorem still applies,
since its coefficient u_b is nonnegative. Thus

~~~
C_N(V)-C_N(W')
 =lambda[tr U'_N/2+L_N(U')]>=0.                  (14)
~~~

There is an exact link to the requested linear source:

~~~
U-U'=sum_(k>=2) alpha_(k+1)
       [H_k^-2-H_(k+1)^-2] d_k d_k^T.           (14a)
~~~

Indeed subtract kappa_k/H_k^2 from w_k-w_(k+1) and
telescope; both coefficient sequences vanish at infinity.
The difference is PSD and centered. Its coefficient at a source
pair is a nonnegative function of the later source birth, so the
full Born theorem applies once more. Therefore

~~~
C_N(W')-C_N(W)
 =lambda[tr(U_N-U'_N)/2+L_N(U-U')]>=0.            (14b)
~~~

This favorable historical comparison does not transfer the
future demands below from W' to W. The difference has signed
physical kernels, and PSD ordering alone leaves the diagonal
subtraction in a future energy demand. In particular no
nonpositive-retirement assertion follows from Born positivity.

There is also a genuinely birth-determined alternative:
R_de=alpha_maxbirth sign(d)sign(e).
The source V+lambda R has the same layer form (13) with the fixed
sign vector in place of d_k/H_k. It has residual trace t_N and
requires no future geometry. At lambda=1 its physical kernel is
exactly the earlier positive-bank causal unit-weight kernel:
on each positive source pair its weight is 1/q_maxbirth^2.
The signed sum part cancels. Hence this sign alternative is a
valid accounting device, not a new improvement over that baseline.

## 6. Actual future blocks paid by the current tails, once

Fix finitely many actual blocks B_i, with old ranks n_i, such that
each block occurs after P_(n_i), and their physical difference sets
Delta B_i are pairwise disjoint. All points lie in one terminal
history P_N. Actual disjoint point blocks satisfy the difference
condition by Sidon uniqueness. Let m_i,L_i be their sizes and
interval lengths.

At old rank n, retain just the part of (13) indexed k>=n:

~~~
Ttail_n=alpha_n[J_Fhat_n+lambda gamma_n z_n z_n^T],
z_n(d)=d/H_n,       gamma_n=H_n^2 u_n/alpha_n in (0,1].
                                                               (15)
~~~

This is a literal subsource of W'_n: the remaining components
k<n are individually nonnegative. Its entry at an existing pair
is the sum of that same pair's actual component weights k>=n.
The repeated appearance of a component in different rows does not
create a repeated unit capacity.

Put S_n=sum z_n(d)^2, T_i=L_i+2H_(n_i),
D_i=T_i-m_i, and

~~~
LB_i=12m_i^2 H_(n_i)^2 S_(n_i)^2/[T_i(T_i^2-1)],

d_i^0=[m_i^2/D_i-m_i/Q_(n_i)]/2,
d_i^lambda=d_i^0
       +lambda gamma_(n_i)[LB_i-m_i S_(n_i)]/(2Q_(n_i)^2).
                                                               (16)
~~~

These are exactly the mass and mass-plus-moment raw demands for
the normalized tail (15). Set d_i^+=max(d_i,0). If A_i is the
actual sum of its kernel over Delta B_i, then A_i>=d_i^+.
Disjointness gives the single-budget inequality

~~~
sum_i (d_i^lambda)^+
 <=sum_(t>0) max_i 1[t notin F_(n_i)]1[t<=L_i-1] K_(Ttail_(n_i))(t)
 <=sum_(t>0) max_i 1[t notin F_(n_i)]1[t<=L_i-1] K_(W'_(n_i))(t)
 <=C_N(W').                                      (17)
~~~

Both middle expressions retain the actual future-span masks.
For the sign source the same argument uses gamma=1 and its own
first moment mu=2 sum_(d in F_n)d; no identity mu=H_n S_n
is asserted for the sign vector.

Here is a completely explicit unused-capacity identity for (17).
For component k in (13), use its restriction to Fhat_min(k,N).
For a source pair e={d,e'} of birth b and output t, write

~~~
v_k(e)=1+lambda d e'/H_k^2,
p_k(e)=sum_i 1[t in Delta B_i]1[b<=n_i<=k].
~~~

On every historically eligible pair b<r, p_k(e) is either zero
or one. A pair counted by p_k has r>n_i>=b, since its output is
a difference of a future block and not in the old bank. Expanding
the fixed source, with nonnegative summands, proves

~~~
C_N(W')-sum_i(d_i^lambda)^+
 =sum_(k>=2) kappa_k
    sum_(e in Fhat_min(k,N), b<r) v_k(e)[1-p_k(e)]
       +sum_i[A_i-(d_i^lambda)^+].               (18)
~~~

This retains every source birth, output retirement, actual block
membership, and component coefficient. A component is not spent
twice at one physical label. Unused historical pairs, output labels
outside the selected actual differences, and slack in the moment
inequality are the precise residual budget. Formula (18) also
includes the infinite component tail restricted to the finite bank.

## 7. Good blocks give a nonsummable demand increase for this source

Use the existing two-lookahead good ranks n=2^(j+1). Their actual
inputs are

~~~
S_n>=eta Q_n,  eta=2^-17,
m=n,   L<=32H_n,   H_(2n)<=32H_n,
H_n<=C n^2 log(2n) beyond one fixed onset.        (19)
~~~

The first inequality follows by comparing signed raw second moments
with the existing positive birth-class variances. The good-index
lemma supplies sum_good 1/log(2n)=infinity.

The tail coefficient has a lower bound tied to the actual lookahead:

~~~
gamma_n
 >=(H_n/H_(2n))^2 [1-alpha_(2n)/alpha_n]
 >=gamma_*:=15/(16*32^2).                        (20)
~~~

Indeed Q_n/Q_(2n)=(n-1)/[2(2n-1)]<1/4.
The signed support in (19) has T<=34H_n. Equations (16),(19),(20)
therefore give

~~~
d_n^lambda-d_n^0
 >=6lambda gamma_* eta^2/[34^3 C log(2n)]
                        -lambda/[2(n-1)].       (21)
~~~

The subtraction here is mS, not (m-1)S: no historical diagonal
saving has been credited to each row. Both raw demands are
eventually positive. Indeed D<=34H_n and S_n<=Q_n show that the
mass-only certificate after even the larger trace subtraction is
at least n^2/(68H_n)-(1+lambda)/[2(n-1)]. The cap therefore gives

~~~
1/[68 C log(2n)]-(1+lambda)/[2(n-1)]>0.           (22)
~~~

Thus (21) also compares positive parts for all selected sufficiently
large good blocks. Its sum diverges; the dyadic sum of 1/(n-1)
converges. This is a demand increase under the single allocation
(17), not a sum of separately normalized historical capacities.

## 8. The literal source capacity is nevertheless unbounded

The following lower bounds apply to every finite positive set F
of q elements, not just a counterexample family. Let Q=2q and
Fhat=F union(-F). Write A for the number of ordered positive
solutions x+y=z with all three labels in F.

At the kth smallest possible z there are at most k-1 choices
for its first summand, hence

~~~
A<=q(q-1)/2.
~~~

The signed Schur partition counts exactly 3A unordered source
pairs with used outputs in F: six per unequal Schur triple and
three per doubled triple. There are 2q^2-q total signed pairs.
Consequently the current unused unit capacity obeys

~~~
C_current(J)>=2q^2-q-3A
             >=(q^2+q)/2=Q^2/8+Q/4.             (23)
~~~

Apply (23) to each actual prefix layer of V. Its current unused
capacity at that layer's prefix is no larger than its literal
historical capacity. The linearity (5) then gives

~~~
C_N(V)>=M_N/8+t_N/4.                             (24)
~~~

There is also a uniform bound for the normalized linear feature,
including lambda=1. Assume q>=2, H=max F, and
W_F=J+d d^T/H^2. Let h=#(F intersect(H/2,H]), l=q-h.
Only opposite-sign pairs with both magnitudes above H/2 can have
weight less than 1/2; there are exactly h^2 such pairs.
If h<=7q/10, (23) yields

~~~
C_current(W_F)
 >=[(q^2+q)/2-h^2]/2 >=q^2/200.
~~~

If h>7q/10, the two same-sign high-source groups contain h(h-1)
pairs in total, all with output below H/2. Only l old output labels
can occur there. Each such output is realized at most h-1 times
per sign, so at least

~~~
(h-1)(h-2l)=(h-1)(3h-2q)>7q^2/200
~~~

of these pairs are unused, and their weights are at least one.
Here h>=2, so h-1>=h/2>7q/20. We have proved

~~~
C_current(J+lambda d d^T/H^2)>=Q^2/800,
                    q>=2, 0<=lambda<=1.         (25)
~~~

The endpoints lambda=0,1 imply the intermediate cases by linearity
of the fixed current-unused mask. The exception q=1 is necessary:
at lambda=1 the only opposite pair {-H,H} has zero weight.

For W' in (13), the components k<N have parameters lambda, and
the restricted infinite tail k>=N combines to
alpha_N[J+lambda gamma_N d d^T/H_N^2].
Applying (25) to each, and discarding the possible rank-two
component of mass at most one, proves

~~~
C_N(W')>=(M_N-1)/800.                            (26)
~~~

This applies to the actual capped history itself. Thus even the
fully compatible alternative does not produce a bounded literal
historical source budget. The root's separate annular-envelope
note considers maxima of normalized current rows; (24),(26)
concern this one fixed source. Neither is a lower bound with
arbitrary future-span masks inserted.

## 9. Exact remaining inequality

For the large good blocks above, put

~~~
D_0=sum_i(d_i^0)^+,     D_lambda=sum_i(d_i^lambda)^+,
G_N=D_lambda-D_0,
M_0=C_N(V)-D_0,         M_lambda=C_N(W')-D_lambda.
~~~

Both margins are nonnegative by the one-source allocation.
Equations (14),(17) give the exact relation

~~~
M_0-M_lambda
 =lambda[tr U'_N/2+L_N(U')]+G_N.                 (27)
~~~

Under the fixed cap and selected actual good blocks, G_N diverges.
The first term on the right is nonnegative and is charged once.
An actual sufficient closing estimate would be

~~~
M_0<=G_N-epsilon G_N+O(1),  for one epsilon>0,    (28)
~~~

along unbounded terminal horizons, or any stronger joint estimate
retaining the additional Born saving in (27). No such estimate has
been established. Formula (18) states exactly which actual unused
pairs and demand slack it would have to control.

If one instead tries to replace C_N by the smaller span-restricted
middle capacity in (17), the historical identity (14) no longer
supplies its saving: a separate comparison of those actual maxima
is then required. Born positivity cannot be silently transferred
through a selected-row or future-span maximum.

The requested birth-fixed source is fully accounted for, including
same-birth retirements and its moment obstruction. The compatible
alternative genuinely pays the good-block demand sum once, but its
baseline margin remains unbounded by the present argument. The
birth-determined sign version returns an existing physical source.
These are precise supporting results and unresolved obligations,
not a completion of original Q1.
