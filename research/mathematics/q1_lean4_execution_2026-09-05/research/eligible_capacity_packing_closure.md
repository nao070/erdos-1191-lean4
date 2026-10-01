# The smaller packing margin: a lattice obstruction and an honest repair

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** The frozen two-moment packing has a uniform loss on sparse
lattices, and this loss persists on a primitive Sidon history with one
spectator point. Thus a universal bounded smaller-margin theorem for
that particular packing is as strong as a direct bounded-eligible-capacity
theorem on a dilation-closed class. The one-cap hypothesis does not
presently prove either theorem. A residue-wise projection repairs the
identified loss on the SAME physical source, but unrestricted residue
resolution recovers exact energies and makes the repaired zero residual
tautological. A separate residue-mask PSD source is also constructed
with its actual single-budget accounting.

These are exact analytical statements, not a finite LP experiment or
an original-Q1 proof. No earlier source, formal module, saved evidence,
or goal state was changed. No capped infinite Sidon history is
constructed. Statements obtained by transforming a capped history
are conditional on such a history being given.

The frozen packing Pi and compatible source Psi_lambda are those of
signed_output_energy_closure.md, SHA-256
8a1ac50d3e8744757e93a287d8943cea5aebc4dd542cc0f0b2608134122c9b12.
Its larger energy margin is not a target here: that margin is already
known to diverge under the fixed cap.

## 1. The smaller margin and the exact local objective

Fix 0<=lambda<=1, an actual integer Sidon history P, signed source bank
Fhat_n, and the permanent raw feature d. Put Q_n=n(n-1), H_n=a_n-a_1,
alpha_n=Q_n^-2, kappa_n=alpha_n-alpha_(n+1), and
u_n=sum_(k>=n)kappa_k/H_k^2, for n>=2.

An unordered pair h={d,e} is eligible when its later source birth b
is smaller than the rank i of the lower endpoint of its actual output
a_r-a_i. Define

~~~
W_lambda(h)=|de|+lambda de>=0,
Hcum_k(lambda)=sum_(eligible h, r<=k) W_lambda(h),
Elig_N(Psi_lambda)=sum_(eligible h,r<=N)u_r W_lambda(h).
~~~

The frozen Pi_k optimizes actual future rows I=(n,B), with n>=2,
minrank(B)>n and |B|>=2, under the per-pair constraints

~~~
sum_I beta_I 1[b(h)<=n_I]1[t(h) in Delta B_I]<=1
       for every eligible h with W_lambda(h)>0.      (1)
~~~

For each row let f_a=1_B*(|d|1_Fhat_n), f_o=1_B*(d1_Fhat_n).
Both vanish on B. Their common allowed set is the FULL integer
interval [min B-H_n,max B+H_n] minus B. If Proj denotes orthogonal
projection onto its affine functions, the frozen raw demand is

~~~
J_I(lambda)
 =[||Proj f_a||^2+lambda||Proj f_o||^2
                     -m(1+lambda)Z_n]/2,
P_I^raw=sum_(b(h)<=n,t(h) in Delta B)W_lambda(h)
       =[||f_a||^2+lambda||f_o||^2-m(1+lambda)Z_n]/2. (2)
~~~

The objective is J_I^+; rows of nonpositive demand may be omitted.
Write r_k=Hcum_k-Pi_k>=0. The exact smaller margin is

~~~
Elig_N-Dstar_N
 =u_N r_N+sum_(k=2..N-1)kappa_k r_k/H_k^2.           (3)
~~~

No occurrence of the larger energy budget is needed in (1)-(3).

## 2. An affine sampling lemma

Let L>=2 and M>=3 be integers. In the integer interval [0,LM],
write G={0,L,...,LM} for the lattice nodes. All norms here use
counting measure. For an affine function v, center its expression
at LM/2. Both G and its integer complement are symmetric about
that center. Their constant and linear squared-norm coefficients
are respectively

~~~
G:     M+1,        L^2 M(M+1)(M+2)/12;
not G: (L-1)M,     L M(L-1)(L M^2-2)/12.            (4)
~~~

The cross terms vanish. For the linear coefficient ratio divided by
L-1, one has

~~~
(M^2-2/L)/[(M+1)(M+2)]
 >=(M^2-1)/[(M+1)(M+2)]
 =(M-1)/(M+2)>=2/5.
~~~

The constant coefficient ratio divided by L-1 is M/(M+1)>=3/4.
Consequently

~~~
||v||_(not G)^2 >=[2(L-1)/5]||v||_G^2.             (5)
~~~

The moment agent independently checked these exact coefficients and
supplied the sharper factor 2/5, improving the author's initial 1/3.

For any one residue class modulo L inside [0,LM], its squared norm
is at most ||v||_G^2. For a nonzero residue, interpolate between
the adjacent lattice nodes and use convexity of the square, then
sum over the M intervals. The endpoint coefficients are at most
one and the interior coefficients equal one. The zero class is G.

Let Omega be [0,LM] minus any subset of G. Suppose f is supported
on Omega and on at most rho residue classes modulo L. All nonlattice
points remain in Omega. Combining (5) with Cauchy on the support
of f and the variational formula for affine projection gives

~~~
||Proj_Omega f||^2
 <=theta_(L,rho)||f||^2,
theta_(L,rho)=5rho/[2(L-1)].                        (6)
~~~

Indeed |<f,v>|^2<=rho||f||^2||v||_G^2 while
||v||_Omega^2>=2(L-1)||v||_G^2/5. This proves (6) for the entire
two-dimensional affine subspace, not merely its constant vector.
Translations of the interval and residues make no difference.

## 3. A uniform loss for every row of a dilated history

Translate the given history so that a_1=0 and dilate it by an integer
L. For a future row of the dilated history, the old radius and both
block endpoints are multiples of L. Its supporting interval is a
translate of [0,LM], with

~~~
M=(max B_original-min B_original)+2H_n_original>=3.
~~~

Its holes are lattice nodes, and both shadows are supported on the
zero residue. Thus (6) applies with rho=1. When theta=5/[2(L-1)]<=1,
(2) gives the stronger local inequality

~~~
J_I
 <=theta P_I^raw-(1-theta)m(1+lambda)Z_n/2,
J_I^+<=theta P_I^raw.                              (7)
~~~

Sum (7) under the SAME constraints (1), using
sum_I beta_I P_I^raw<=Hcum_k. Therefore, uniformly over every
finite prefix and all actual future rows,

~~~
Pi_k(LP)<=theta Hcum_k(LP),
Elig_N(Psi_lambda on LP)-Dstar_N(LP)
 >=(1-theta)Elig_N(Psi_lambda on LP).                (8)
~~~

In particular L=6 gives theta=1/2. This is not an assertion about
one unfavorable tested block: it bounds the complete frozen optimum.

Under dilation, H_k becomes L H_k, u_k becomes u_k/L^2, and every
raw carrier entry becomes L^2 W_lambda. Birth and endpoint ranks
are unchanged. Hence the entire normalized eligible capacity is
exactly invariant, with physical labels relabeled t to Lt:

~~~
Elig_N(Psi_lambda on LP)=Elig_N(Psi_lambda on P).    (9)
~~~

The same cancellation holds in each compatible infinite tail.

## 4. What a universal bounded-margin theorem would actually mean

Let C be any class of actual histories closed under dilation by 6.
The following two qualitative statements are equivalent:

~~~
(i)  for every P in C, sup_N[Elig_N(P)-Dstar_N(P)]<infinity;
(ii) for every P in C, sup_N Elig_N(P)<infinity.     (10)
~~~

The implication (ii)=>(i) follows from 0<=Dstar<=Elig. Conversely,
apply (i) to 6P and use (8)-(9):
Elig_N(P)<=2[Elig_N(6P)-Dstar_N(6P)].
The bound may depend on the particular history; no uniform constant
over C is needed for this equivalence.

The class of histories satisfying SOME one fixed eventual cap
H_n<=C_0 n^2 log(2n) is dilation-closed: the transformed constant is
6C_0 and the same onset works. The previously proved good-block
result forces Elig_N to diverge on any such hypothetical history.
Therefore proving (i) on this whole capped class would indeed
contradict the existence of that history, by applying it to its
dilate. This supplies a concrete further contradiction mechanism.

It is not a counterexample to a theorem whose capped class may be
empty. No capped infinite history is constructed here. It also shows
that bounding the frozen residual universally cannot be easier
merely because an optimized demand was subtracted: in a
dilation-closed class, (10) makes it equivalent to direct boundedness
of eligible capacity.

## 5. Primitive histories do not remove the limitation

Given any increasing integer Sidon history A={0=a_1<a_2<...}, form

~~~
P={0,1,L a_2,L a_3,...},             L>=16.          (11)
~~~

This is an actual Sidon history. Its positive gaps are:
the distinct multiples of L from the dilated A; the gap 1; and
the distinct gaps L a_j-1, j>=2. Their residue classes are 0,1,-1,
which are distinct for L>=3. Thus no two gaps coincide.
The gcd of all differences of P is 1 because it contains 0 and 1.
If the original target uses strictly positive integers, translate
this entire history by 1. Its gaps, ranks, radius, source labels,
eligibility, and all capacity and projection statements are unchanged.

For an old rank n>=3, its radius H_n and all future points are
multiples of L. The signed source labels occupy only residues
0,1,-1, so both shadows of EVERY future block occupy at most three
residues. The interval in the sampling lemma again has M>=3.
Equation (6) applies with

~~~
theta=15/[2(L-1)]<=1/2.
~~~

At old rank n=2 the signed source bank is {-1,1}, whose only
positive source-pair output is 2. All future block differences are
multiples of L, so that row has P_I^raw=0 and J_I^+=0.
Thus (8) applies to all rows of the primitive history (11), with
theta<=1/2.

Bulk source and output ranks from A are shifted by one in P.
For l>=2,

~~~
kappa_(l+1)/kappa_l
 =(l-1)^2(l+1)/[l(l+2)^2]>=3/32.                   (12)
~~~

After clearing denominators, the last inequality is
(l-2)(29l^2+14l-16)>=0. Also H_(l+1)(P)=L H_l(A).
For every bulk output of rank r in A this gives

~~~
L^2 u_(r+1)(P)
 =sum_(l>=r)kappa_(l+1)/H_l(A)^2
 >=(3/32)u_r(A).
~~~

Every eligible bulk pair remains eligible after the rank shift.
All extra entries are nonnegative. Hence for every N,

~~~
Elig_(N+1)(P)>=3 Elig_N(A)/32,
Elig_(N+1)(P)-Dstar_(N+1)(P)>=3 Elig_N(A)/64.        (13)
~~~

If A hypothetically satisfies a fixed cap with constant C_0, then P
satisfies one with constant L C_0 after the shifted onset. Thus even
restricting a proposed universal bounded frozen-margin theorem to
primitive capped histories would contradict the known cap-forced
eligible divergence through (11)-(13).

Again this is conditional, not a constructed capped example. Its
unconditional content is the actual Sidon transformation, the
uniform row bound, and the exact finite capacity comparison.

## 6. A residue-wise projection of the SAME two shadows

The preceding loss comes from assigning all ambient integer sites to
an affine projection, including many residue classes where the actual
shadows vanish. It can be repaired without adding a source or a trace.
Fix a positive integer q and any actual row (n,B), with B not required
to be monochromatic modulo q.

For c modulo q, record the four old-feature statistics

~~~
A_c=sum_(d in Fhat_n,d=c mod q)|d|,
B_c=sum_(d in Fhat_n,d=c mod q)d,
M_c=sum_(d in Fhat_n,d=c mod q)d|d|,
Z_c=sum_(d in Fhat_n,d=c mod q)d^2.
~~~

For the actual future block let m_z count its points in residue z
and T_z be their coordinate sum. The mass and first moment of each
original shadow restricted to output residue s are exactly

~~~
a_s=sum_z m_z A_(s-z),
a1_s=sum_z[T_z A_(s-z)+m_z M_(s-z)],

o_s=sum_z m_z B_(s-z),
o1_s=sum_z[T_z B_(s-z)+m_z Z_(s-z)].                 (14)
~~~

The sums over source and block residues are taken BEFORE squaring.
In particular B_c and M_c need not vanish: global odd centering
cannot be imposed on every residue class.

Partition the ACTUAL Omega=J minus B into
Omega_s={x in Omega:x=s mod q}. For each nonempty class write its
size D_s, mean c_s and centered variance V_s. Orthogonal projection
onto affine functions separately on these disjoint supports gives

~~~
Eproj^(q)
 =sum_s[(a_s^2+lambda o_s^2)/D_s
       +((a1_s-c_s a_s)^2+lambda(o1_s-c_s o_s)^2)/V_s],
J_I^(q)=[Eproj^(q)-m(1+lambda)Z_n]/2.               (15)
~~~

An empty class contributes zero. If V_s=0, its singleton mass term
is used and the centered-moment term is zero, as follows from the
actual support; no division by zero is performed.

The global affine subspace is contained in this piecewise affine
subspace. Therefore

~~~
J_I^(q)>=J_I^(1)=J_I,
P_I^raw=J_I^(q)+eps_I^(q)/2,       eps_I^(q)>=0.     (16)
~~~

This is projection of the original two shadows, not independent
payment of q different kernels. There is ONE trace subtraction
m(1+lambda)Z_n and the SAME actual pair payment P_I^raw.
At q=L it removes the support defect of a completely dilated
history exactly: J^(L) on LA equals L^2 J^(1) on A.
It also resolves the three occupied classes in the primitive
construction, without replacing gcd 1 by a false uniformity claim.

## 7. Different moduli must share the original pair constraints

To use a prescribed finite modulus family, replace each row objective
by max_q(J_I^(q))^+ and retain (1) unchanged. Equivalently one may
list rows (I,q), but all of them use the SAME mask for each h in (1).
Fractions assigned to several copies of one row can be aggregated
onto a best modulus. Adding their projection bounds as independent
payments would violate that constraint.

A fixed finite nonempty family of positive integer moduli still has
a uniform dilation obstruction. Choose an integer L divisible by
every permitted q and satisfying L>=6 max_q q. On the dilated
history LA, both shadows are supported on its one active residue
modulo q. Dividing the coordinates of that residue by q reduces
its affine projection to the sampling problem with spacing L/q,
with the same original lattice holes. Thus

~~~
||Proj^(q) f||^2 <=[5/(2(L/q-1))]||f||^2
                 <=||f||^2/2,
max_q(J_I^(q))^+ <=P_I^raw/2.                       (16a)
~~~

The same shared-constraint argument gives Pi_k^(finite family)
<=Hcum_k/2 on LA. Consequently the equivalence mechanism of
(10) persists for every fixed finite family on a class closed
under its chosen dilation. This is again conditional on an
actual history being given, and constructs no capped history.
Only unbounded or growing resolutions escape this particular
fixed-family obstruction.

Likewise different components of the one fixed Psi may choose
different allowed moduli. Their actual weights remain
kappa_k/H_k^2, and every physical source-pair component is charged
at most once. This permits growing or history-dependent moduli
without q independent capacity resets.

There is an exact warning about taking this repair without restriction.
If q is greater than the width of J, each Omega_s contains at most
one point. Projection is then the full shadow itself, so

~~~
J_I^(q)=P_I^raw.                                    (17)
~~~

For every actual output a_r-a_i with eligible pairs, take the row
n=i-1, B={a_i,a_r}. Its pair mask consists exactly of all eligible
pairs on that output. Choose a sufficiently large q to make (17)
hold for that row. Different outputs have disjoint pair masks, so
assigning coefficient one to all these rows is a valid shared
allocation. It attains every eligible raw entry exactly.

Consequently the modified optimum allowing arbitrary q satisfies

~~~
Pi_k^(all q)=Hcum_k, Dstar_N^(all q)=Elig_N.          (18)
~~~

This holds on EVERY finite actual history, irrespective of a cap.
It is an exact-information identity, not a new contradiction.
At that resolution the residue moments in (14) encode the actual
shadow overlaps which define the capacity. The closing implication
for the FROZEN Pi in (10) cannot be transferred to this changed
objective: its all-q residual is identically zero even before the
cap hypothesis enters.

A productive coarse-residue version must therefore specify its
permitted information or moduli and prove an additional cap-based
comparison. Boundedness of an unrestricted repaired residual
supplies no such comparison.

## 8. A distinct residue-mask PSD source

There is also a genuine alternative source, separate from the
same-shadow repair. For a FIXED q let

~~~
D_q(d,e)=1[d=e mod q]
        =sum_(c mod q)1[d=c]1[e=c].
~~~

This is a PSD, entrywise nonnegative Gram mask, with diagonal one.
For the existing Gram K_k(d,e)=autocorr(1_Pk)(d-e), define
each component on Fhat_k and embed it by zero outside
Fhat_k x Fhat_k:

~~~
Psi_lambda^[q]
 =sum_(k>=2) kappa_k/H_k^2
    K_k circ W_lambda circ D_q.                     (19)
~~~

Each term is a sum of Gram feature products and is PSD and
entrywise nonnegative. Its diagonal and trace are exactly those
of Psi_lambda. For distinct source pairs its entry is

~~~
u_max(b,r) W_lambda(h)1[q divides t(h)],             (20)
~~~

with zero entry for never-used outputs. Thus its eligible capacity
is the literal original eligible capacity restricted to positive
labels divisible by q; it is not q copies of that capacity.

If B is contained in one residue class modulo q, every internal
output is divisible by q. On those ACTUAL outputs, (19) agrees
with the original carrier. Its residue feature shadows are
supported on disjoint output classes, so (15) gives a valid demand
for this masked source too. For a general multicolored B, that
equality is not asserted: its nondivisible outputs have been
removed by the new source.

Actual monochromatic point blocks of different residues have
disjoint difference sets by Sidon uniqueness, even though all their
outputs are divisible by q. Their actual demands may be paid from
this ONE masked source. Splitting residue features never supplies
an independent budget for each residue.

One may instead fix a modulus q_k for each genuine component, or
nonnegative fractions theta_(k,q) with sum_q theta_(k,q)<=1:

~~~
Xi_lambda
 =sum_k kappa_k/H_k^2
    K_k circ W_lambda circ [sum_q theta_(k,q)D_q].    (21)
~~~

This defines a compatible fixed source, with trace at most the
original trace and every entry at most the original entry.
Its off-diagonal coefficient at h is

~~~
W_lambda(h)sum_(k>=max(b,r)) kappa_k/H_k^2
                              sum_(q divides t(h))theta_(k,q).
~~~

The complete-history choices must be fixed consistently under
restriction. They cannot be reselected independently at every
terminal horizon. A row paid by a q component must be an actual
q-monochromatic future block ending by that component index.
Several moduli in the same component use the fractions in (21);
they do not restart its normalization.

The pure output-price formula u_r generally no longer factors out
when q_k varies. In particular no unmodified signed Born or
collision cancellation identity is imported for this new source.
Its PSD, trace, and pairwise dominance follow directly from (21).

## 9. The exact remaining task

The direct smaller-residual question has not been bounded here.
Instead (8)-(13) show a specific all-row obstruction to explaining
its universal boundedness by optimization alone. They also supply
a rigorous further contradiction if boundedness of the frozen
margin were proved on all capped histories, even only primitive
ones.

Residue projection repairs that particular defect and keeps a
single physical allocation. Unrestricted refinement, however,
collapses to the exact identity (18); it is not a route to Q1.
The separate masked source (19)-(21) is concrete and compatible,
but no cap-forced demand surplus has been proved for it. A choice
of modulus which deletes every useful label would have zero
capacity and zero demand, not a successful bounded-budget proof.

What is still needed is a genuine upper bound on actual eligible
capacity, or a sufficiently strong comparison for explicitly
restricted residue data and a source retaining nontrivial actual
demands. That comparison must contradict the one-cap hypothesis,
rather than merely equate two divergent quantities or resolve
every point of the shadow exactly. Original Q1 remains open.
