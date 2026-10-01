# Two-sided signed retirement and monotone raw energy

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** On every actual integer Sidon history, with the permanent
raw signed feature g(d)=d, retirement at output stage j lies between
-B_j/4 and 2B_j. Consequently the raw full signed convolution energy
is strictly increasing from rank two, and its excess over the exact
diagonal is nondecreasing. Arbitrary nonnegative stage prices give
two-sided Born-energy comparisons. These finite analytical theorems
do not settle the shared physical margin or original Q1.

The parent proposed the lower collision identity. It is independently
derived here, including the multiset normalization, the Born-only
remainder, the energy increment, and its weighted consequences.
No numerical experiment, previous-check rerun, Lean edit, or new
formal verification is used.

The exact multiset source is signed_multiset_born_retirement.md,
read at SHA256
324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487.
Its collision formulas and full-group exhaustion are the finite
inputs used below. All source and output clocks remain distinct
where the actual history makes them distinct.

## 1. Definitions and the existing exact collision formulas

Let P_N={a_1<...<a_N} be an actual integer Sidon prefix, including
repeated two-sum uniqueness. Put

~~~
F_n=Delta P_n,       Fhat_n=F_n union(-F_n),
Q_n=n(n-1),         H_n=a_n-a_1,
g_(Fhat_n)(d)=d for d in Fhat_n and 0 otherwise.
~~~

Zero is excluded from the source bank. For a used unordered pair
of distinct signed sources {d,e}, put b=max(tau(d),tau(e)) and
r=tau(|d-e|). It is Born if r<=b and retired if b<r.
Define the stage sums

~~~
B_j=sum_(Born records, b=j)de,
R_j=sum_(retired records, r=j)de.
~~~

Same-birth signed sources are included in both definitions when
their actual output clocks permit it. Write B_(<=N)=sum_(j<=N)B_j.
Each complete numeric Schur group's Born total is nonnegative, so
B_j>=0. Its Born price is the latest source clock, whereas its
retirement price below is the output clock.

For an active collision, let U,V be disjoint equal-sum triple
multisets, with latest endpoint n occurring once in
V={x,y,n}. Here endpoint letters are point values, not ranks or
numeric Schur magnitudes. Let mu be the common mean and put

~~~
c=n-mu,       X=x-mu,       Y=y-mu,
sigma_U^2=sum_(u in U, with multiplicity)(u-mu)^2,
sigma_V^2=X^2+Y^2+c^2,
A=aut(U)aut(V)>0.
~~~

The reviewed matching/stabilizer calculation gives

~~~
B(U,V)=(4sigma_U^2+12c^2)/A,
R(U,V)=(2sigma_U^2+6sigma_V^2-12c^2)/A.           (1)
~~~

These are actual sums. The division by A already accounts for
repeated slots and the doubled formal source-pair list when the
numeric Schur group has two equal magnitudes.

## 2. The exact lower bound, with all repeated slots

Since X+Y=-c, the elementary square identity gives

~~~
2sigma_V^2-3c^2
 =2(X^2+Y^2)-c^2
 =(X-Y)^2=(x-y)^2.
~~~

Substitution into (1) yields the new exact identity

~~~
R(U,V)+B(U,V)/4
 =3[sigma_U^2+(x-y)^2]/A>=0.                    (2)
~~~

No distinctness of x and y was assumed. Together with the
already proved upper collision bound, this gives

~~~
-B(U,V)/4<=R(U,V)<=2B(U,V).                      (3)
~~~

The lower constant can be attained by an actual collision.
For P={0,1,3}, take U={1,1,1}, V={0,0,3}. Then A=12,
sigma_U^2=0, sigma_V^2=6 and c=2, so (B,R)=(4,-1).
This is an exact hand evaluation of the stated collision, not a
new numerical run or a sharpness assertion about the full stage,
which has additional Born-only groups.

At stage j, the complete multiset partition has

~~~
B_j=sum_(active collisions with latest endpoint a_j)B(U,V)+B_j^0,
R_j=sum_(same active collisions)R(U,V),     B_j^0>=0.
~~~

A collision-free automatic group or a group with no retirement
belongs to B_j^0. Therefore summing (3) and retaining that
nonnegative remainder proves, for every actual stage,

~~~
                         -B_j/4<=R_j<=2B_j.     (4)
~~~

The lower step uses
-sum_active B(U,V)/4 >=-B_j/4. Thus no Born-only term is lost
with the wrong sign. Clock ties and doubled numeric labels remain
inside the exhaustive partition.

## 3. Both the raw energy and its diagonal excess are monotone

Define

~~~
Z_N=sum_(d in Fhat_N)d^2,
E_N=||1_(P_N)*g_(Fhat_N)||_2^2,
v_j=Z_j-Z_(j-1),      Z_1=E_1=0.
~~~

The full signed pair expansion and its exact increment are

~~~
E_N=N Z_N+2sum_(j<=N)(B_j+R_j),

E_j-E_(j-1)=Dhat_j+2B_j+2R_j,
Dhat_j=Z_(j-1)+j v_j
      =jZ_j-(j-1)Z_(j-1).                       (5)
~~~

This diagonal is derived for the full signed source. It is not
the earlier positive-bank term with coefficient j-1 on v_j.
Every used pair first appears at its later source clock when Born,
or at its output clock when retired; this accounts for all terms
in the increment, including equal source births.

Combining (4) and (5) proves the two-sided increment estimate

~~~
Dhat_j+(3/2)B_j
 <=E_j-E_(j-1)
 <=Dhat_j+6B_j.                                  (6)
~~~

In particular E_j is nondecreasing. In fact it increases strictly
at each actual j>=2: the new signed class has 2(j-1) nonzero
labels, so v_j>0 and Dhat_j>0.

There is a slightly stronger convenient formulation. Set

~~~
Y_N=E_N-N Z_N,          Y_1=0.
~~~

Then

~~~
(3/2)B_j<=Y_j-Y_(j-1)<=6B_j,
0<=(3/2)B_(<=N)<=Y_N<=6B_(<=N).                 (7)
~~~

Thus the exact diagonal excess Y_N is itself nondecreasing.
In particular E_N>=N Z_N for every prefix.

These statements concern the raw feature d while both P_N and
Fhat_N grow together. They do not claim monotonicity of E_N/H_N^2,
of an energy with a frozen earlier source bank, of arbitrary odd
features, or of an output-masked physical maximum.

## 4. Arbitrary nonnegative prices give two-sided comparison

For any finite nonnegative sequence omega_j, define

~~~
B_T(omega)=sum_(j=2..T)omega_j B_j,
R_T^out(omega)=sum_(j=2..T)omega_j R_j,
A_T(omega)=sum_(j=2..T)omega_j(E_j-E_(j-1)),
D_T(omega)=sum_(j=2..T)omega_j Dhat_j.
~~~

No monotonicity of omega is needed to sum (4) or (6):

~~~
-B_T(omega)/4<=R_T^out(omega)<=2B_T(omega),

(3/2)B_T(omega)
 <=A_T(omega)-D_T(omega)
 <=6B_T(omega),

[A_T(omega)-D_T(omega)]/6
 <=B_T(omega)
 <=(2/3)[A_T(omega)-D_T(omega)].                 (8)
~~~

The middle quantity is nonnegative. These comparisons keep the
Born source price and retired output price at their exact common
stage. They do not transfer a retired record to its earlier source
price.

When omega is also nonincreasing, summation by parts gives

~~~
A_T(omega)
 =omega_T E_T
   +sum_(j=2..T-1)(omega_j-omega_(j+1))E_j,

A_T(omega)-D_T(omega)
 =omega_T Y_T
   +sum_(j=2..T-1)(omega_j-omega_(j+1))Y_j.       (9)
~~~

Every term in the second line is nonnegative by (7).
Equations (8)-(9) provide a two-sided comparison of weighted
Born mass with the actual signed-energy Abel expression after
its exact diagonal is removed.

For the direct prices w_j=1/(Q_j^2H_j^2), and for the compatible
prices u_j=sum_(k>=j)(Q_k^-2-Q_(k+1)^-2)/H_k^2, one has
0<=u_j<=w_j. The signed diagonal estimate already derived from
(5) gives

~~~
0<=D_T(omega)<=2zeta(2)-1       for omega=w or u,

[A_T(omega)-(2zeta(2)-1)]/6
 <=B_T(omega)<=(2/3)A_T(omega).                 (10)
~~~

Consequently A_T and B_T diverge together for either of these
fixed prices whenever one of their previously proved divergent
lower bounds applies. This statement does not require summing
independent physical capacities. The u coefficients remain those
of a source fixed from the complete history, with their existing
prefix-only determination caveat.

## 5. A current-row consequence and its boundary

Let k_N(t) be the raw correlation of g(d)=d on Fhat_N.
The total off-diagonal raw source product is -Z_N/2, whereas
the used output sum is Y_N/2. Thus

~~~
sum_(t>0,t notin F_N)k_N(t)
 =-[Z_N+Y_N]/2<=-Z_N/2.                         (11)
~~~

For the single current row z_d=d/H_N and 0<=lambda<=1,
let C_cur denote the sum of the kernel on positive outputs
outside F_N. Equation (11) gives the exact current capacity saving

~~~
C_cur(J)-C_cur(J+lambda z z^T)
 =lambda[Z_N+Y_N]/(2H_N^2).                     (12)
~~~

Inserting (7) gives two-sided bounds on this same row saving:

~~~
lambda[Z_N/2+(3/4)B_(<=N)]/H_N^2
 <=C_cur(J)-C_cur(J+lambda z z^T)
 <=lambda[Z_N/2+3B_(<=N)]/H_N^2.                (13)
~~~

One may divide all three expressions by Q_N^2 to compare the
prescribed normalized kernels. The price and the mask must stay
common within this comparison.

These are current-prefix totals. They do not transfer through
maxima of different rows, a future-span cutoff, or the fixed
source-clock matrix U^c_de=c_maxbirth de evaluated against the
larger terminal unused set. In particular the unresolved
terminal-unused quantity p_T(c) in signed_clock_commutator.md
has not been assigned a sign by (11).

## 6. Minimal correction to the earlier quantitative note

The earlier proof in signed_born_quantitative_gain.md used a
windowwise moment lower bound and did not need energy monotonicity.
Its sentence asserting that E_n need not be monotone was nevertheless
too strong, and is superseded by (6).

Only that passage was minimally corrected to say:

> The following Abel lower-bound argument does not require monotonicity
> of E_n.

The earlier equations, constants, explicit-error argument, and
conclusions are unchanged. Its independently saved review should
retain its original binding as an older snapshot and append a
follow-up binding to the corrected source. No old numerical
evidence is rerun or presented as a check of this new theorem.

The newly established facts are the full-stage lower retirement
bound, raw-energy monotonicity, monotonicity of the exact diagonal
excess, and the two-sided weighted comparisons. The physical-margin
obligation and original Q1 remain open.
