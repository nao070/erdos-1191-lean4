# Growing residue data: exact Sidon counts and a surviving arithmetic loss

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** Endpoint residue counts and all signed-feature moments are
derived exactly from one actual Sidon prefix. Under the fixed cap,
moduli of order N log N force linearly many occupied endpoint residues.
Nevertheless an explicit growing family of moduli has a uniform
one-half loss for EVERY actual future row on a fixed dilation of any
actual history. The loss also persists on a primitive history. Thus
unbounded modulus size and broad endpoint residue support do not by
themselves repair the frozen packing. The unrestricted interval of
all moduli is not ruled out by this result.

Everything below is analytic. No finite search, LP run, formal-module
run, prior-file change, or construction of a capped infinite history
is involved. The one-cap consequences are conditional on a hypothetical
history satisfying that cap.

Notation for the fixed output-clock source Psi_lambda and its genuine
component packing is from signed_output_energy_closure.md, SHA-256
8a1ac50d3e8744757e93a287d8943cea5aebc4dd542cc0f0b2608134122c9b12.
The same-shadow residue objective is the one explicitly defined in
eligible_capacity_packing_closure.md, SHA-256
1bbe91da5091f59c1ecaf32cd70a8e48fd22bc7e174dd09c2831614d41e34964.
Throughout the source and packing statements fix 0<=lambda<=1.

## 1. Endpoint counts and signed-label counts

Let P_N={a_1<...<a_N} be an actual integer Sidon prefix, N>=2.
Set H=a_N-a_1, Q=N(N-1), and take any positive integer modulus q.
Write N_c for the number of endpoints in residue c modulo q.
Every unordered endpoint pair in one residue gives a distinct
positive multiple of q at most H. Therefore

~~~
sum_c binom(N_c,2)<=floor(H/q),
sum_c N_c^2<=N+2floor(H/q),                         (1)
#{c:N_c>0}>=N^2/[N+2floor(H/q)],
N_c<=(1+sqrt(1+8floor(H/q)))/2.
~~~

These statements use actual difference uniqueness, not modular
Sidon uniqueness or assumed equidistribution.

Let Fhat_N consist of every nonzero ordered endpoint difference,
and let L_c count its labels congruent to c. The ordered-difference
map is injective away from the N self-pairs. Hence

~~~
L_c=sum_z N_z N_(z-c)-N 1[c=0],
sum_c L_c=Q,
L_0<=2floor(H/q),
L_c<=floor(2H/q)+1            for c!=0.             (2)
~~~

The last two bounds also follow by counting nonzero integers in
[-H,H] in one residue. In particular

~~~
#{c:L_c>0}>=Q/[floor(2H/q)+1].                     (3)
~~~

For one fixed eventual cap H_N<=C N^2 log(2N), every N beyond its
one fixed onset satisfies

~~~
sum_c N_c^2<=N+2C N^2 log(2N)/q,
#{c:N_c>0}>=N/[1+2C N log(2N)/q],
#{c:L_c>0}>=N(N-1)/[1+2C N^2 log(2N)/q].          (4)
~~~

At q comparable to N log(2N), both lower bounds are of order N,
with constants depending on C and the comparison constants. At
q comparable to N the endpoint bound is only of order N/log N.
Neither assertion forces every residue to be occupied or its count
to be close to N/q. Moreover q of order N log N is still much smaller
than 2H, since Q<=2H and log(2N)/N tends to zero; such projection
classes have growing ambient size. The actual-hole bound below
shows that their allowed supports also remain larger than singletons.

## 2. Exact signed-feature statistics from actual endpoints

Use one common coordinate origin for every residue. Let
T_c=sum_(a in P_N,a=c mod q)a and U_c=sum a^2 on that same class.
Define the signed-label feature statistics

~~~
A_c=sum_(d in Fhat_N,d=c mod q)|d|,
B_c=sum_(d in Fhat_N,d=c mod q)d,
M_c=sum_(d in Fhat_N,d=c mod q)d|d|,
Z_c=sum_(d in Fhat_N,d=c mod q)d^2.
~~~

Expansion of a-b and (a-b)^2 gives

~~~
B_c=sum_z[T_z N_(z-c)-N_z T_(z-c)],
Z_c=sum_z[U_z N_(z-c)+N_z U_(z-c)-2T_z T_(z-c)].
                                                               (5)
~~~

Self-pairs contribute zero, so neither formula needs a diagonal
correction. The moment agent independently checked (2) and (5),
including the common-origin requirement.

Absolute moments also have an exact ordered-endpoint expression.
For h=0,1,2 put

~~~
E_c^(h)=sum_(i<j,a_j-a_i=c mod q)(a_j-a_i)^h.
~~~

At each j, write N_<j,z, T_<j,z, U_<j,z for the actual preceding
endpoint statistics in residue z. With z=a_j-c modulo q, the
contribution to E_c^(0), E_c^(1), E_c^(2) is respectively
N_<j,z, a_j N_<j,z-T_<j,z, and
a_j^2 N_<j,z-2a_j T_<j,z+U_<j,z. Consequently

~~~
L_c=E_c^(0)+E_(-c)^(0),
A_c=E_c^(1)+E_(-c)^(1),  B_c=E_c^(1)-E_(-c)^(1),
M_c=E_c^(2)-E_(-c)^(2),  Z_c=E_c^(2)+E_(-c)^(2).
                                                               (6)
~~~

This includes c=-c without merging the two distinct signed labels.
It implies B_0=M_0=0 and also vanishing on a self-opposite residue,
but general B_c and M_c need not vanish. Useful immediate bounds are
A_c<=H L_c, Z_c<=H^2 L_c, |B_c|<=A_c, and |M_c|<=Z_c.

## 3. The SAME actual shadows and an exact refinement surplus

Fix an actual old rank n>=2 and a finite actual future block B,
minrank(B)>n and m=|B|>=2. In this section the endpoint and source
statistics above are taken at n. For B, let m_z be its residue
counts and T^B_z its residue coordinate sums. For the original
shadows f_a=1_B*(|d|1_Fhat_n) and f_o=1_B*(d1_Fhat_n), their
residue masses and first moments are

~~~
a_s=sum_z m_z A_(s-z),
a1_s=sum_z[T^B_z A_(s-z)+m_z M_(s-z)],
o_s=sum_z m_z B_(s-z),
o1_s=sum_z[T^B_z B_(s-z)+m_z Z_(s-z)].              (7)
~~~

All contributions are summed BEFORE squaring. Actual Sidon
uniqueness makes both shadows zero on B. Let
J=[min B-H_n,max B+H_n], Omega=J minus B, and partition Omega
into its actual residue classes Omega_s. Their sizes, means, and
centered second moments are D_s, c_s, V_s.

There is a uniform actual-hole bound. Write l=max B-min B and
x=l/q. Actual Sidon uniqueness gives
binom(m_s,2)<=floor(l/q), so m_s<=1+sqrt(2x).
An ambient q-residue has at least x+2H_n/q-1 integer sites.
Since x-sqrt(2x)>=-1/2,

~~~
D_s>=2H_n/q-5/2.
If q<=n log(2n), then D_s>=(n-1)/log(2n)-5/2.      (7a)
~~~

This holds for EVERY actual future block, however large its span,
using Q_n<=2H_n. Hence the full growing range is uniformly far
from singleton resolution at large n even after actual holes.
The refined objective is

~~~
Eproj^q=sum_s[(a_s^2+lambda o_s^2)/D_s
       +((a1_s-c_s a_s)^2+lambda(o1_s-c_s o_s)^2)/V_s],
J_(n,B)^q=[Eproj^q-m(1+lambda)Z_n]/2.              (8)
~~~

Empty classes are omitted. A singleton class contributes its mass
term and zero centered-moment term; no zero denominator is used.
There is ONE trace subtraction and ONE original raw pair payment

~~~
Praw_(n,B)=sum_(b(h)<=n,t(h) in Delta B)(|de|+lambda de),
Praw_(n,B)=J_(n,B)^q+epsilon_(n,B)^q/2,
epsilon_(n,B)^q>=0.                               (9)
~~~

There is also an exact computable expression for the improvement
over the original global affine projection. For either shadow f,
let v(x)=alpha+beta(x-c) be that global projection on Omega.
For its residue mass F_s and first moment F1_s set

~~~
r_s=F_s-D_s[alpha+beta(c_s-c)],
t_s=F1_s-c_s F_s-beta V_s.
~~~

Because the global affine space is contained in the residue-wise
space, orthogonal projection gives

~~~
||Proj_q f||^2-||Proj_1 f||^2
 =sum_s[r_s^2/D_s+t_s^2/V_s].                      (10)
~~~

The same singleton convention applies. Summing (10) for f_a and
lambda times f_o proves a nonnegative exact gain. Count bounds
(1)-(4) alone do not lower-bound these centered residual statistics:
they also depend on the actual block and on the endpoint moments.

For a prescribed family Q_n of moduli, use max_(q in Q_n)(J^q)^+
as each row objective, with zero for an empty family. Equivalently
list (n,B,q) as separate rows under the SAME physical constraints

~~~
sum_rows beta_(n,B,q)
    1[b(h)<=n]1[t(h) in Delta B]<=1                (11)
~~~

for every eligible pair h of positive weight. Its raw finite
optimum is denoted Pi_k^Q. Separate moduli do not supply separate
copies of a pair or of a component.

## 4. An affine leverage lemma inside a residue class

Consider K>=2 consecutive integer sites, with any affine function
v on them. The diagonal leverage of the two-dimensional affine
subspace at site j, 0<=j<K, is

~~~
ell_j=1/K+(j-(K-1)/2)^2/[K(K^2-1)/12]
     <=(4K-2)/[K(K+1)]<4/K.
~~~

Thus v(j)^2<=4||v||^2/K. Let S be a union of at most rho arithmetic
progressions of spacing D in this index interval, and suppose K>=D.
There are at most rho(K/D+1) selected sites, giving

~~~
||v||_S^2<=eta||v||^2,        eta=8rho/D.           (12)
~~~

Remove arbitrary holes contained in S, obtaining Omega. If f is
supported on S intersect Omega and D>8rho, Cauchy and the
variational characterization of affine projection imply

~~~
||Proj_Omega f||^2
 <=[eta/(1-eta)]||f||^2
 =[8rho/(D-8rho)]||f||^2.                         (13)
~~~

Indeed the removed norm is at most eta times the original norm,
whereas the inner product with f only uses S. This proof allows
truncated periods at BOTH interval boundaries and arbitrary
placement of the actual holes.

For a history supported on rho residues modulo L, intersect an
ambient q-residue with this support. Each compatible support
residue becomes a progression of spacing D=L/gcd(L,q) in the
q-residue index. If every ambient class has at least D sites,
(13) applies before summing the projected energies over q-residues.
This is the missing within-residue information not provided by
the number of occupied endpoint residues modulo q.

## 5. A uniform obstruction for an explicit growing family

At old rank n prescribe the growing family

~~~
Q_n={q integer: n<=q<=n log(2n), gcd(q,6)=1}.       (14)
~~~

The theorem below also holds for ANY subfamily, including all
prime moduli in this range once n>=5. No theorem about the
distribution of primes is needed; an empty family has zero demand.

Given ANY actual integer Sidon history A with first point 0, form
P=24A. For n>=5 and q in Q_n, gcd(q,24)=1 and
q<=n(n-1)=Q_n^(rank). The last inequality follows from
log(2n)<=n-1 for n>=3. Here Q_n^(rank) distinguishes n(n-1)
from the modulus family in (14).

Sidon uniqueness on the original prefix gives 2H_n(A)>=n(n-1).
Every supporting interval of an actual future block on P has
at least 2H_n(P) integer sites. Each of its q-residues therefore
has at least

~~~
floor(2H_n(P)/q)>=24
~~~

sites. In that residue the two shadows and every removed hole
lie on one progression of spacing 24. Apply (13) with rho=1,D=24:
its projection fraction is at most 1/2. Uniformly over every such
old rank, every actual future block, and every q in the WHOLE
growing family,

~~~
(J_(n,B)^q)^+<=Praw_(n,B)/2.                      (15)
~~~

This does not select a bad block after optimizing. It bounds the
entire admissible row set simultaneously.

Let R_0 be the finite sum of W_lambda(h)=|de|+lambda de over all
unordered distinct source pairs h contained in Fhat_4(P).
Rows with n<5 can only use these pairs, and (11) pays each at most
once. Decomposing early and late row payments gives, for every k,

~~~
Pi_k^Q(P)<=Hcum_k(P)/2+R_0/2.                     (16)
~~~

The early term is not repeated per row, output, modulus, or k.
For alpha_k=[k(k-1)]^-2, kappa_k=alpha_k-alpha_(k+1),
u_k=sum_(l>=k)kappa_l/H_l^2, define the compatible packed demand

~~~
Dstar_N^Q=u_N Pi_N^Q
          +sum_(k=2..N-1)kappa_k Pi_k^Q/H_k^2.
~~~

Since u_N+sum_(k=2..N-1)kappa_k/H_k^2=u_2, (16) proves

~~~
Elig_N(Psi on P)-Dstar_N^Q(P)
 >=Elig_N(Psi on P)/2-u_2(P)R_0/2
  =Elig_N(Psi on A)/2-u_2(P)R_0/2.                (17)
~~~

The last equality is the exact normalized dilation invariance:
source/output ranks stay fixed, W scales by 24^2, and u scales
by 24^-2. The initial cost in (17) is one finite constant.

Thus on a class closed under dilation by 24, boundedness of this
growing-family margin for every history is equivalent to boundedness
of eligible capacity for every history. The class of histories
satisfying SOME one fixed eventual cap is dilation-closed, with
constant C changed to 24C. On a hypothetical capped history the
already proved actual good-block demands force eligible capacity
to diverge. A universal bounded-margin theorem for (14) would
therefore contradict that history; (17) does not construct one.

Notice that for gcd(q,24)=1 the endpoint residue counts on 24A
are merely a permutation of those on A. They may satisfy the
linear occupied-residue lower bounds in (4), while every class
still has the within-class sampling loss (15).

## 6. A primitive version of the same growing-family obstruction

For any actual A={0=a_1<a_2<...}, instead take

~~~
P={0,1,72a_2,72a_3,...}.
~~~

It is Sidon: its distinct positive gaps occupy the disjoint
residue types 0, 1, and -1 modulo 72. Its difference gcd is 1.
If strictly positive integers are required, translate all points
by 1; all claims depend on unchanged gaps and ranks.

For n>=8 and q in (14), q<=(n-1)(n-2). This follows, for example,
from log(2n)<=n/2 and n^2/2<=(n-1)(n-2) in this range.
Now H_n(P)=72H_(n-1)(A), so every q-residue in an actual row's
ambient interval has at least 72 sites. All future block points
are multiples of 72. Its shadows occupy at most the three
residues 0,1,-1 modulo 72, and holes lie in the zero residue.
Since gcd(q,72)=1, (13) with rho=3,D=72 again gives (15).
Early ranks n<8 are paid from one finite bank Fhat_7(P).

The bulk rank shift has the exact price comparison

~~~
kappa_(l+1)/kappa_l
 =(l-1)^2(l+1)/[l(l+2)^2]>=3/32       for l>=2.
~~~

Together with H_(l+1)(P)=72H_l(A), this gives
72^2 u_(r+1)(P)>=3u_r(A)/32. Every original eligible bulk
pair stays eligible. With one finite constant C_initial,

~~~
Elig_(N+1)(P)-Dstar_(N+1)^Q(P)
 >=3 Elig_N(A)/64-C_initial.                      (18)
~~~

If A hypothetically has one eventual cap, P has one with constant
72C and shifted onset. Thus restricting a universal bounded-margin
claim to primitive histories does not avoid this obstruction.
All finite-history transformations and inequalities above are
unconditional; the existence of a capped infinite input is not.

## 7. Precisely what this does and does not resolve

Equations (1)-(10) give exact actual-history data and a nonnegative
refinement surplus. Equations (14)-(18) prove that a substantial
growing modulus family can still leave a fixed proportion of all
eligible capacity unpaid, even at moduli where (4) forces many
occupied endpoint residues. The obstruction uses realizable
histories and the single original allocation constraints.

It does NOT bound the optimum when EVERY integer modulus in
[n,n log(2n)] is allowed. That full interval eventually contains
multiples of 24, or of 72 in the primitive construction. For those
moduli the spacing D in (13) can equal 1, and this proof supplies
no projection loss. More generally the relevant quantity in (13)
is L/gcd(L,q), not the numerical size of q alone.

A productive growing-modulus theorem must exploit that extra
arithmetic adaptability, together with actual endpoint moments
and actual future blocks, under the shared constraints (11).
The fixed cap and residue count bounds derived here do not prove
such a comparison. No eligible capacity-minus-demand upper bound
for the full adaptive range, no cap-forced surplus for a new
source, and no original-Q1 contradiction have been established.
