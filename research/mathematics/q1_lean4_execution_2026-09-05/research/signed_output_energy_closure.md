# An eligible output budget and its exact energy remainder

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** The output-clock source admits a smaller, literal budget for
strictly future blocks. At every stage its eligible retirement mass is
at most (1+lambda)/8 times the increment of the raw signed diagonal
excess Y. This is an all-history finite inequality, with the exact
multiset factors and without a radius cap. It removes the older unit
background from this particular comparison. The actual moment demands
still have to be compared with this smaller energy budget; no original
Q1 conclusion follows.

This note is analytical. No finite parameter search, prior-test replay,
Lean execution, or modification of an older source is used. The current
output-clock construction and two-sided energy note are the inputs.
The parent pointed out that unusable physical pairs can be removed from
the payment budget without making a PSD claim about their deletion.
The eligibility geometry and the new energy comparison are derived
below. The moment agent independently checked the four-record algebra.

The input bytes read for this derivation were:

- signed_output_clock_source.md:
  b499cad5c00d89d106d6163c10f82beaff49c7c231332c987066fb31cf8cad81;
- signed_energy_two_sided.md:
  1364dd87dc4290f50e3a7367500c1059519beba24eb076202c1a559c87d6dcb2;
- signed_multiset_born_retirement.md:
  324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487.

## 1. Actual clocks, the fixed source, and the permitted payments

Fix one complete increasing integer Sidon history, including repeated
two-sum uniqueness. Put

~~~
P_n={a_1<...<a_n}, F_n=Delta P_n, Fhat_n=F_n union(-F_n),
Q_n=n(n-1), H_n=a_n-a_1,
alpha_n=Q_n^-2, kappa_n=alpha_n-alpha_(n+1),
u_b=sum_(k>=b) kappa_k/H_k^2.
~~~

Sources are the signed nonzero labels; the fixed raw feature is g(d)=d.
Every signed label has its actual positive-label birth tau(d).
For an unordered pair h={d,e} of distinct sources write

~~~
b(h)=max(tau(d),tau(e)), t(h)=|d-e|.
~~~

If t(h) eventually occurs, Sidon uniqueness specifies its endpoints
and their ranks uniquely:

~~~
t(h)=a_(r(h))-a_(i(h)),       i(h)<r(h).
~~~

For a never-used output set r(h)=infinity, without defining i(h).
A pair is retired when b(h)<r(h). The output-clock source Psi_lambda,
0<=lambda<=1, has off-diagonal entries

~~~
Psi_lambda(h)=u_max(b(h),r(h)) W_lambda(h),
W_lambda(h)=|de|+lambda de>=0,                         (1)
~~~

and zero entries for never-used outputs. Its diagonal and its complete
history Gram construction remain exactly those in
signed_output_clock_source.md; in particular the diagonal carries the
factor k in each layer. We do not replace that source by a terminal
normalization or by a matrix with selected entries deleted.

An actual future block B after old rank n has every point at rank >n.
It need not be an interval of consecutive ranks. Let e=maxrank(B),
m=|B|, and L=max(B)-min(B)+1. A payment using sources Fhat_n and an
internal difference of B necessarily satisfies

~~~
b(h)<=n<i(h)<r(h)<=e.
~~~

Thus the exact necessary eligibility condition is

~~~
                         b(h)<i(h).                 (2)
~~~

It is also sufficient to make a pair available to some strictly future
block: use old rank i(h)-1 and the two-point block
{a_(i(h)),a_(r(h))}. This is availability, not a claim that that block's
moment lower bound is positive.

For any fixed entrywise nonnegative source A, define the finite eligible
budget

~~~
Elig_N(A)=sum_(h: b(h)<i(h)<r(h)<=N) A(h).            (3)
~~~

Any collection of actual blocks in P_N with pairwise disjoint difference
sets pays at most (3), provided its row kernels are entrywise dominated
by A on their actual outputs. This follows pair by pair: each paid
physical output occurs in only one selected block, and every paid pair
satisfies (2). The blocks may share one point. No PSD property of an
eligible-entry deletion is asserted or needed.

The literal historical capacity is generally larger:

~~~
C_N(Psi_lambda)
 =Elig_N(Psi_lambda)+Inelig_N(Psi_lambda)+Boundary_N,
0<=Boundary_N<=(1+lambda)/2.                         (4)
~~~

Here Inelig_N sums retired pairs with r<=N and i<=b; Boundary_N sums
retired pairs with sources present by N and r>N. Its bound is the
existing permanent-tail bound. None of that boundary pays a chosen
block contained in P_N. Equation (3), rather than an independent copy
of (4), will be the budget below.

## 2. Which collision records can be eligible

Use the exact equal-three-sum multiset partition. At an active collision
the newest endpoint n occurs once in V={x,y,n}; the other multiset U
is disjoint from V and lies below n. Letters here are point values,
not rank indices. The retirement records with output n-m, m in U,
use the four old endpoints in

~~~
(U minus one occurrence of m) union {x,y}.
~~~

Their latest source endpoint is the largest of those four values.
This remains true with repeated slots, since the source labels have
their unique actual endpoint representations. Consequently (2) holds
if and only if m is the unique second-largest endpoint among the six
slots. Such an endpoint must lie in U. If the second-largest endpoint
lies in V, or occurs more than once in U, no record is eligible.

There is therefore at most one eligible output per active collision.
When it exists, write

~~~
U={ell,u,v}, V={n,x,y}, n>ell>max(u,v,x,y),
aut=aut(U)aut(V).
~~~

All its eligible records have output n-ell and a common latest source
clock, the rank of max(u,v,x,y). Their output price in (1) is nevertheless
the rank of n, shared by every retired record of the collision.

The full formal list has four entries at this output. Dividing by aut
gives their actual sum, including repeated old slots and doubled numeric
Schur labels. This uses exactly the orbit normalization of the multiset
note: repeated formal source pairs and stabilizer multiplicities cancel
together, while their endpoint clocks and eligibility remain identical.
Born-only groups contribute no retirement to (3).

## 3. An exact eligible-output calculation

For the eligible collision introduce the nonnegative distances

~~~
t=n-ell>0, p=ell-u>0, q=ell-v>0,
A=ell-x>0, B=ell-y>0,
s=p+q, h=p-q, d=A-B.
~~~

Equal three-sums give A+B=t+p+q=t+s. Set

~~~
g_1=(A-p)(B-q), g_2=(A-q)(B-p),
P=(g_1)_+ +(g_2)_+.
~~~

Both pairs of factors have sum t. Hence (g_i)_+<=t^2/4 and

~~~
0<=P<=t^2/2,
-2(g_1+g_2)=h^2+d^2-t^2.                            (5)
~~~

The four formal retired products are -g_1,-g_2 and their reflections.
Write H_lambda(U,V) for their total carrier W_lambda after division
by aut. Then exactly

~~~
H_lambda(U,V)
 =2[|g_1|+|g_2|-lambda(g_1+g_2)]/aut
 =[(1+lambda)(h^2+d^2-t^2)+4P]/aut.                  (6)
~~~

No sign has been imposed on the raw eligible sum.

Let B(U,V), R(U,V) be the full raw signed Born and retired sums.
The known exact formulas give the increment of Y assigned to this
collision:

~~~
DeltaY(U,V)=2[B(U,V)+R(U,V)]
 =12(sigma_U^2+sigma_V^2)/aut
 =[6(h^2+d^2)+4s^2+12ts+18t^2]/aut.                 (7)
~~~

For example sigma_U^2=2(p^2+q^2-pq)/3, and the latest centered
coordinate is c=(3t+s)/3, so sigma_V^2=3c^2/2+d^2/2.
Expanding (6)-(7) produces the exact defect

~~~
(1+lambda)DeltaY(U,V)-8H_lambda(U,V)
 =[8(1+lambda)(pq+AB+ts+3t^2)-32P]/aut
 >=[8(1+lambda)(pq+AB+ts)+8(1+3lambda)t^2]/aut
 >=0.                                                (8)
~~~

The equality uses s^2-h^2=4pq and (s+t)^2-d^2=4AB.
The inequality uses only (5). In fact this defect is positive for
every actual eligible collision; no uniform positive relative gap is
claimed. Although this algebra works for lambda>=0, the nonnegative
source and payment statements here retain 0<=lambda<=1.

One also obtains a useful direct Born comparison. Since
|d|<=s+t, (5)-(6) imply

~~~
H_lambda(U,V)
 <=[2(1+lambda)(p^2+q^2+ts)+2t^2]/aut
 <=(1+lambda)B(U,V)/2,                              (9)
~~~

where B(U,V)=4[t^2+(t+p)^2+(t+q)^2]/aut.
Equation (8), rather than (9), yields the smaller energy budget below.

## 4. The all-history stage and weighted energy budgets

Define the actual raw energies and their diagonal excess by

~~~
Z_j=sum_(d in Fhat_j)d^2,
E_j=||1_(P_j)*g_(Fhat_j)||_2^2,
Y_j=E_j-jZ_j,        Y_1=0.
~~~

The exact full-signed identities are

~~~
DeltaY_j=2(B_j+R_j),    (3/2)B_j<=DeltaY_j<=6B_j.
~~~

At stage j, sum (6) over eligible active collisions and call the result
H_(lambda,j). This is exactly the raw eligible carrier sum at output
rank j. Define

~~~
G_(lambda,j)=(1+lambda)DeltaY_j-8H_(lambda,j).        (10)
~~~

It is nonnegative. Its complete decomposition consists of (8) on
eligible collisions, (1+lambda)DeltaY(U,V) on active collisions with
no eligible output, and 2(1+lambda) times the Born-only remainder.
The last remainder is nonnegative. Thus no absent eligible output,
same-birth pair, clock tie, or repeated slot is discarded with the
wrong sign.

For every finite nonnegative sequence omega_j,

~~~
sum_(j<=N) omega_j H_(lambda,j)
 <=(1+lambda)/8 sum_(j<=N) omega_j DeltaY_j,
sum_(j<=N) omega_j H_(lambda,j)
 <=(1+lambda)/2 sum_(j<=N) omega_j B_j.              (11)
~~~

In particular, set

~~~
Ycal_N(u)=sum_(j=2..N)u_j DeltaY_j
        =u_N Y_N+sum_(k=2..N-1) kappa_k Y_k/H_k^2.
~~~

The literal source (1) then satisfies the exact identity and inequality

~~~
Elig_N(Psi_lambda)
 =(1+lambda)Ycal_N(u)/8
       -sum_(j=2..N)u_j G_(lambda,j)/8
 <=(1+lambda)Ycal_N(u)/8.                           (12)
~~~

Every price in (12) is the actual output price. This is not a
source-clock transfer of the exceptional eligible contribution.
No cap, asymptotic regularity, or summability assumption was used.

The corresponding layer identity is also exact:

~~~
Ycal_N(u)=sum_(k>=2) kappa_k Y_min(k,N)/H_k^2.       (13)
~~~

It retains the complete-history tail k>=N. The raw Y is nonnegative
and nondecreasing, so this rearrangement uses nonnegative terms.

## 5. A local demand with its exact projection remainder

For one actual block B after old rank n>=2, define

~~~
A_n=sum_(d in Fhat_n)|d|,  Z_n=sum_(d in Fhat_n)d^2,
f_a(x)=sum_(v in B)|x-v| 1[x-v in Fhat_n],
f_o(x)=sum_(v in B)(x-v)1[x-v in Fhat_n].
~~~

The actual supporting interval is

~~~
J=[min(B)-H_n,max(B)+H_n] intersect Z,
T=|J|=L+2H_n, Omega=J minus B, D=|Omega|=T-m,
c_Omega=D^-1 sum_(x in Omega)x,
V_Omega=sum_(x in Omega)(x-c_Omega)^2,
mu_B=m^-1 sum_(v in B)v.
~~~

Both shadows vanish at every point of B, by actual difference uniqueness.
Their masses and first moments are

~~~
sum f_a=m A_n,  sum x f_a=m A_n mu_B,
sum f_o=0,      sum x f_o=m Z_n.                     (14)
~~~

Here D>0 and V_Omega>0. For the latter, the odd shadow has zero mass
and strictly positive first moment m Z_n, so its support cannot be a
single point. All quantities use the actual span and actual holes.

Project each shadow onto the orthogonal vectors 1_Omega and
(x-c_Omega)1_Omega. Define the raw two-moment pair demand

~~~
J_(n,B)(lambda)
 =1/2{m^2 A_n^2/D
   +m^2[A_n^2(mu_B-c_Omega)^2+lambda Z_n^2]/V_Omega
   -m(1+lambda)Z_n}.                               (15)
~~~

Let eps_(n,B)(lambda)>=0 be the sum of the two squared projection
residuals, with coefficient lambda on the odd residual. Then the
unmasked raw nonnegative carrier pays exactly

~~~
P_(n,B)^raw
 =sum_(h: b(h)<=n, t(h) in Delta B) W_lambda(h)
 =J_(n,B)(lambda)+eps_(n,B)(lambda)/2
 >=J_(n,B)(lambda)^+.                              (16)
~~~

The trace subtraction in (15) is m(1+lambda)Z_n. The source is the
two-feature matrix |d||e|+lambda de. Its shadow energy equals
m times that trace plus twice the physical pair sum. There is no
additional factor k from the output mask in this pair demand: its
diagonal contribution cancels exactly as in the input source note.

In particular,

~~~
P_(n,B)^raw-J_(n,B)(lambda)^+
 =eps_(n,B)(lambda)/2+min(J_(n,B)(lambda),0)
 =min(P_(n,B)^raw,eps_(n,B)(lambda)/2)>=0.            (17)
~~~

This retains the positive-part issue when the raw demand is negative.
Using only the full-interval odd moment bound and omitting the even
linear projection recovers the weaker demand of the input note.
Thus the previously proved good-block divergence also applies to (15).

For an actual component k>=e, the masked kernel restricted to Fhat_n
agrees with this carrier on Delta B. Consequently the full tail pays
u_e P_(n,B)^raw and has lower demand

~~~
delta_(n,B)(lambda)=u_e J_(n,B)(lambda).             (18)
~~~

This equality is on the actual outputs of B. No global PSD ordering
between that unmasked carrier and Psi_lambda has been asserted.

## 6. An exact remainder for any prescribed actual block family

Choose finitely many actual blocks B_i in P_N, after old ranks n_i>=2,
with pairwise disjoint difference sets. Put e_i=maxrank(B_i), and use
their own actual lengths L_i and the projection data above.
For an eligible pair h define

~~~
chi_i(h)=1[b(h)<=n_i]1[t(h) in Delta B_i],
S(h)=sum_i chi_i(h) in {0,1},

Gamma(h)=1[there exists i with
 b(h)<=n_i<i(h)<r(h)<=e_i and t(h)<=L_i-1].
~~~

Then S<=Gamma. The latter gate retains source rank, the time interval
of the row, and the actual span cutoff, without pretending that every
integer in that span is an internal block difference.
All the following sums over h have b(h)<i(h)<r(h)<=N. Define

~~~
U_gate=sum_h [1-Gamma(h)]u_(r(h))W_lambda(h),
U_member=sum_h [Gamma(h)-S(h)]u_(r(h))W_lambda(h),
U_price=sum_i sum_h chi_i(h)[u_(r(h))-u_(e_i)]W_lambda(h),
U_proj=sum_i u_(e_i)[P_(n_i,B_i)^raw-J_(n_i,B_i)(lambda)^+].
~~~

Each term is nonnegative. In U_price, r(h)<=e_i is an actual fact
whenever chi_i=1. Finite pair expansion, not an inequality between
independent envelopes, now gives

~~~
Elig_N(Psi_lambda)-sum_i delta_(n_i,B_i)(lambda)^+
 =U_gate+U_member+U_price+U_proj.                     (19)
~~~

Combining with (12) yields the promised global energy identity:

~~~
(1+lambda)Ycal_N(u)/8-sum_i delta_(n_i,B_i)(lambda)^+
 =sum_(j=2..N)u_j G_(lambda,j)/8
    +U_gate+U_member+U_price+U_proj.                  (20)
~~~

Thus the former background is replaced by an explicit raw-energy
budget. No term in (20) is discarded. In particular the cap controls
some lower demands, but does not by itself bound the eligible pairs
missed by a proposed family, its projection error, or its geometry
defect. The absent r>N boundary has not vanished from the historical
capacity (4); it is correctly absent from the smaller budget (3).

## 7. What adaptive repetition can actually optimize

The fixed nonnegative Gram components allow more flexibility than
requiring the same complete tail for every chosen block. This can
remove U_price by working at its genuine component price. The following
finite packing problem records that flexibility without assuming a
regular radius profile.

For each k>=2, list all rows I=(n,B) with 2<=n<minrank(B), B subset P_k,
and |B|>=2. The list is finite. Put J_I=J_(n,B)(lambda) from (15).
Rows with J_I<=0 may be omitted. For each eligible physical source pair
h with r(h)<=k and W_lambda(h)>0, require

~~~
beta_I>=0,
sum_I beta_I 1[b(h)<=n_I]1[t(h) in Delta B_I]<=1.     (21)
~~~

Define Pi_k(lambda) as the maximum of sum_I beta_I J_I over (21);
set it to zero when there is no positive row. This is a finite linear
program specified entirely by the actual prefix, its blocks, and the
explicit moment lower bounds. It is not defined using the energy
budget that we seek to compare with it.

Every positive row has at least one pair with W_lambda(h)>0, by (16).
The corresponding constraint bounds its beta_I by 1. Hence a maximum
exists. The stricter physical-output constraints
sum_(I: t in Delta B_I)beta_I<=1 give a sufficient smaller feasible
set, including the difference-disjoint families of Section 6. The
pair constraints (21) also allow an actual output to be shared when
different rows use disjoint fractions of its fixed source components.
They never replicate one pair entry.

At component k of Psi_lambda, an allocation beta satisfying (21)
pays the moment demand

~~~
(kappa_k/H_k^2)sum_I beta_I J_I.
~~~

Every row ends by k, so the output mask agrees with its unmasked
carrier on the actual row outputs. All remaining pair entries of
that component stay nonnegative. Summing the allocations therefore
uses precisely one fixed source. Conversely, any iteration which
only takes fractions of these same row restrictions and these same
components is represented by (21) after its fractions are aggregated.
It does not receive a renewed unit budget on restarting.

The exact finite raw residual for any feasible allocation is

~~~
(1+lambda)Y_k/8-sum_I beta_I J_I
 =sum_(j<=k)G_(lambda,j)/8
   +sum_(eligible h,r(h)<=k) W_lambda(h)
       [1-sum_I beta_I 1[b(h)<=n_I]1[t(h) in Delta B_I]]
   +sum_I beta_I[P_I^raw-J_I].                     (22)
~~~

All terms are nonnegative. This proves

~~~
Pi_k(lambda)<=H_(lambda,<=k):=sum_(j<=k)H_(lambda,j)
             <=(1+lambda)Y_k/8.                    (23)
~~~

As k increases, existing rows remain feasible: their masks are zero
on new pairs not present in the former prefix. Thus Pi_k is also
nondecreasing. No monotonicity of either difference in (23) is assumed.

For demand blocks contained in P_N, the best allocation of this type
over all actual components is exactly

~~~
Dstar_N(lambda)
 =sum_(k>=2) kappa_k Pi_min(k,N)(lambda)/H_k^2
 =u_N Pi_N(lambda)
      +sum_(k=2..N-1) kappa_k Pi_k(lambda)/H_k^2.     (24)
~~~

The optimization separates by component; for k>=N its finite row
problem is Pi_N. Optimal allocations are attained in each finite row
problem, and the tail is summable. This statement is an ex post
existence statement on the one fixed complete history. It does not
assert that the optimal rows can be selected online before seeing
their actual future endpoints.

An equivalent row description assigns row I the scalar price
sum_(k>=e_I) beta_(I,k) kappa_k/H_k^2. The local demand is linear
in that nonnegative scalar. Thus (24) can improve on the complete-tail
rule (18); it does not change the underlying source or its PSD proof.

## 8. Exact summability criteria, and the unresolved comparison

Define two finite-prefix residuals

~~~
r_k(lambda)=H_(lambda,<=k)-Pi_k(lambda)>=0,
q_k(lambda)=(1+lambda)Y_k/8-Pi_k(lambda)>=0.
~~~

Combining (12),(13),(23),(24) gives exact identities:

~~~
Elig_N(Psi_lambda)-Dstar_N(lambda)
 =u_N r_N(lambda)+sum_(k=2..N-1)kappa_k r_k(lambda)/H_k^2,

(1+lambda)Ycal_N(u)/8-Dstar_N(lambda)
 =u_N q_N(lambda)+sum_(k=2..N-1)kappa_k q_k(lambda)/H_k^2. (25)
~~~

This is an actual capacity-minus-demand formula, with the smaller
eligible capacity in its first line. It includes all unused eligible
pair mass and the exact local projection loss through (22).

The terminal terms are uniformly bounded without a cap. Young's
inequality and Z_N<=Q_N H_N^2 give

~~~
0<=Y_N=E_N-NZ_N<=(N^2-N)Z_N
                  <=Q_N^2 H_N^2,
0<=u_N q_N(lambda)<=(1+lambda)/8.                  (26)
~~~

The same bound holds for u_N r_N. Nonnegativity of the other terms
in (25) therefore proves the precise equivalences

~~~
sup_N[Elig_N(Psi_lambda)-Dstar_N(lambda)]<infinity
 iff sum_(k>=2) kappa_k r_k(lambda)/H_k^2<infinity,

sup_N[(1+lambda)Ycal_N(u)/8-Dstar_N(lambda)]<infinity
 iff sum_(k>=2) kappa_k q_k(lambda)/H_k^2<infinity.   (27)
~~~

These criteria are noncircular finite block optimization problems and
nonnegative series. No estimate establishing either convergence is
proved here. In particular bounded trace, or divergence of weighted
Born, does not establish them.

A simple check prevents accidentally claiming a smaller order from
(26) alone:

~~~
Ycal_N(u)<=1+sum_(k=2..N-1)kappa_k Q_k^2
          =1+sum_(k=2..N-1)4k/(k+1)^2
          =4 log N+O(1).                            (28)
~~~

The cap-based lower demands grow more slowly in the estimates presently
proved. Their divergence alone is compatible with (28).

If one assumes one fixed eventual cap
H_n<=C n^2 log(2n) for every n beyond one fixed onset, the existing
good-block result implies that Dstar_N(0), Dstar_N(lambda) and
Ycal_N(u) diverge. For Dstar, use its feasible allocations consisting
of the previously chosen disjoint good half-blocks and their full
tails; (15) only strengthens their earlier demands. Finite initial
ranks do not affect that statement. Nothing here assumes
H_n asymptotic to C n^2 log n or a fixed derivative exponent.

The remaining direct energy route is therefore sharply specified:
prove a sufficient comparison for the actual Pi_k under that one cap,
or quantify its residual (22) strongly enough to contradict the cap
through a further argument. For example, a cap-based lower comparison
that forced Dstar_N(lambda)>(1+lambda)Ycal_N(u)/8 for some N would
contradict (23)-(25). Such a comparison has not been established,
and is not inserted as an assumption into a declaration of Q1.

Even proving one of the bounded-margin criteria (27) would need to be
connected to a final contradiction; equality of two divergent budgets
is not itself a contradiction.

## 9. Why the larger historical margin cannot be the target

There is a further literal unused-capacity bound. In the eligible
geometry of Section 3 put f_lambda(z)=|z|-lambda z. The four other
formal retired products, with sign reversed inside f, are

~~~
A(B-p), A(B-q), B(A-p), B(A-q).
~~~

For x=A-p and y=B-q one has x+y=t>0, x<=A and y<=B. If x,y>=0,
then f_lambda(xy)<=[A f_lambda(y)+B f_lambda(x)]. If one factor is
negative, the positive factor is bounded by A or B respectively,
and the same inequality follows, retaining its factor 1+lambda.
Both factors cannot be negative. Apply this also with p,q exchanged.
After summing and dividing by the same orbit factor,

~~~
eligible W_lambda retirement <= ineligible W_lambda retirement
~~~

within that collision. A collision with no eligible output contributes
only to the right. The exact common output price is essential here.
Thus

~~~
Inelig_N(Psi_lambda)>=Elig_N(Psi_lambda),
C_N(Psi_lambda)-Dstar_N(lambda)
 >=[C_N(Psi_lambda)+Boundary_N]/2
 >=C_N(Psi_lambda)/2.                               (29)
~~~

Under the fixed cap and good-block conditions just stated, the last
quantity diverges, since C_N>=Elig_N>=Dstar_N. Hence a uniformly
bounded *literal historical* capacity-minus-demand margin for this
carrier and this entire class of row/component iterations is impossible.
This is not an impossibility result for the eligible-budget route:
the rigorous payment argument permits replacing that larger capacity
by (3). It is also not an impossibility result for arbitrary new PSD
features, different kinds of demands, or original Q1.

## 10. A small optimization reduction and the remaining scope

For any fixed row, divide its raw demand by 1+lambda and set
theta=lambda/(1+lambda) in [0,1/2]. Equation (15) becomes an affine
function of theta before its positive part is taken. Accordingly,
for any fixed feasible packing the normalized objective is convex
in theta, and its maximum over this interval is at lambda=0 or 1.

For 0<=lambda<1 every eligible pair has W_lambda(h)>0, so the feasible
set in (21) is the same as at lambda=0. At lambda=1 it can only enlarge,
because opposite-sign pairs have zero weight. Thus each packing
feasible at an interior lambda is feasible at both endpoints. Its
convex normalized objective is bounded by the corresponding convex
combination of the two endpoint optima. Taking the supremum gives

~~~
Pi_k(lambda)/(1+lambda)
 <=(1-2theta)Pi_k(0)+theta Pi_k(1)
 <=max(Pi_k(0),Pi_k(1)/2).                           (30)
~~~

One may retain every row in the comparison with objective J_I^+:
rows of nonpositive objective can be assigned coefficient zero.
There are finitely many rows; any row with a positive objective has
a nonzero actual carrier pair, so the required bounds on its
coefficient remain valid. No equality of the feasible sets at
lambda=1 is assumed.

The same convex-combination bound holds for Dstar_N after summing
with the nonnegative component weights. Thus for a common lambda,
intermediate choices cannot beat both endpoints after division by
the energy-budget factor 1+lambda. This reduces that scalar choice;
it supplies no missing lower bound for either endpoint optimum.

The established new facts are the exact eligible endpoint condition,
the (1+lambda)/8 output-energy budget, the complete actual-block
residual, and the component-wise packing/summability criterion.
Adaptive repetition can remove the block-end pricing loss while
respecting one source. The eligible unused-pair and projection errors
remain unbounded by the present argument. Original Q1 remains open.
