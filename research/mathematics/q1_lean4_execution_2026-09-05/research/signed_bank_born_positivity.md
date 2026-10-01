# Nonnegative full Born sums on the signed difference bank

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** Proved finite full-Born positivity for the actual signed
difference bank, first for the permanent feature g(d)=d and then for
fixed odd nondecreasing features and their symmetric mixed products.
The historical capacity identity and the signed-support future moment
demand are proved with their exact diagonal and support costs. This
removes the earlier Born-sign obstruction for this different source.
It does not bound the shared physical maximum, establish improvement
over every earlier baseline, or resolve original Q1. No numerical
test, Lean declaration, or Lean verification is used.

The signed-source proposal and monotone extension came from the parent.
This note independently derives the exhaustive pair partition, all
clock/tie cases, the capacity comparison, corrected support count,
and good-epoch constants. No six-distinct-endpoint deletion or
separated-clock hypothesis is needed.

## 1. Signed labels and the full Born classification

Let P_N={a_1<...<a_N} be an actual integer Sidon prefix, including
repeated two-sums, with N>=2. Put

~~~
F_n=Delta P_n,       Fhat_n=F_n union (-F_n),
Ghat_n=Fhat_n\Fhat_(n-1),
H_n=a_n-a_1,         q_n=binom(n,2),
tau(-d)=tau(d)       for d>0.
~~~

The signed bank excludes zero. Positive difference uniqueness gives
|Fhat_n|=2q_n and a unique actual birth for every label. For an
unordered pair of distinct signed sources {d,e}, the output is the
positive number t=|d-e|. When this output belongs to the positive
bank, set

~~~
b=max(tau(d),tau(e)),       r=tau(t).
~~~

The pair is Born if r<=b and retired if r>b. This is the **full**
Born definition: source labels of equal birth are included.

For g(d)=d, every signed birth class sums to zero. The same holds
for any fixed odd feature phi, since its labels occur in pairs d,-d.
For arbitrary nonnegative numbers alpha_2,...,alpha_N define

~~~
Lhat_N(phi;alpha)
 =sum_(used Born pairs {d,e} in Fhat_N)
                         alpha_b phi(d)phi(e).             (1)
~~~

No monotonicity of alpha is required for this finite Born-functional
statement. It is not a PSD assertion about a matrix built from
arbitrary birth weights.

## 2. Exhaustive partition into numeric Schur triples

If the two sources have the same sign, their distinct magnitudes
u<v and their output give the unique Schur relation u+(v-u)=v.
If the sources have opposite signs, their magnitudes give u+v=t.
Sorting the two summands yields one canonical triple x<=y, z=x+y,
with every positive label in F_N.

Conversely, for 0<x<y and z=x+y in F_N, the entire associated
list of signed source pairs is:

| Output | Source pairs | Total product for g(d)=d |
|---|---|---|
| x | {y,z}, {-z,-y} | 2yz |
| y | {x,z}, {-z,-x} | 2xz |
| z | {-x,y}, {-y,x} | -2xy |

All six unordered pairs are distinct. The pair {x,y}, if used,
belongs to the different Schur relation with output y-x and largest
numeric label y; it is not a seventh pair here. The preceding
same-sign/opposite-sign construction proves exhaustiveness and
uniqueness of this partition.

Let p_x,p_y,p_z be the three actual clocks and M their maximum.
Every Born pair in this triple has later source birth exactly M:
its output clock is no later than its maximum source clock.
Thus every Born product in this triple is priced at alpha_M in
(1), including when some clocks agree.

If the maximum is unique, the group whose output has that maximum
is retired, and the other two groups are Born. For the raw linear
feature the full Born contributions, before alpha_M, are

~~~
unique latest x:   2xz-2xy = 2x^2,
unique latest y:   2yz-2xy = 2y^2,
unique latest z:   2xz+2yz = 2z^2.                 (2)
~~~

Ties between the lower two clocks do not change this conclusion.
If the maximum occurs at least twice, every output group has a
source at that maximum and is Born. The total is

~~~
2yz+2xz-2xy = 2(x^2+xy+y^2)>0.                    (3)
~~~

Same-birth source pairs occur among the retired groups in the
unique-maximum case when the two lower clocks tie, and can be Born
in the tied-maximum case. They must remain in the partition.
The calculation even covers all-three-clock ties,
although the actual positive birth stars rule that case out.

## 3. The doubled-label case has three pairs, not six

For x=y and z=2x the complete list is

~~~
{x,2x}, {-2x,-x}:   output x,    total product 4x^2;
{-x,x}:            output 2x,   product -x^2.     (4)
~~~

There is only one opposite-sign pair. Its signed sources are
distinct despite having equal magnitude. The full Born sum is

~~~
tau(2x)>tau(x):     4x^2;
tau(x)>tau(2x):     3x^2.                         (5)
~~~

Equal clocks would make all three pairs Born, also giving 3x^2.
That equality is impossible in the actual bank: two distinct
positive labels x,2x in one birth star would have difference x
in the strictly earlier bank, contradicting the birth of x.

Every Born pair in (4) again has later source birth equal to the
maximum clock of its triple. Multiplying (2)–(5) by alpha_M proves

~~~
                      Lhat_N(g;alpha)>=0,   g(d)=d.       (6)
~~~

All actual endpoints and all clock ties are included. There is no
repeated-endpoint error. Taking alpha supported on one stage also
proves nonnegative full Born contribution at every source-birth stage.

## 4. Odd monotone features and mixed products

Let phi be a fixed odd nondecreasing real function on signed
integers, with phi(u)>=0 for positive u. Write f_u=phi(u).
For x<y,z=x+y the output groups in §2 become

~~~
output x:  2f_y f_z,
output y:  2f_x f_z,
output z: -2f_x f_y.
~~~

Unique latest x and y give, respectively,

~~~
2f_x(f_z-f_y)>=0,       2f_y(f_z-f_x)>=0.
~~~

Unique latest z gives 2f_z(f_x+f_y)>=0. With a tied maximum,
the full sum can be written 2f_x(f_z-f_y)+2f_y f_z>=0.
The doubled-label cases give

~~~
tau(2x)>tau(x):   2f_x f_(2x)>=0;
tau(x)>=tau(2x):  2f_x f_(2x)-f_x^2>=f_x^2>=0.    (7)
~~~

Thus the same partition and common Born-stage price prove

~~~
                      Lhat_N(phi;alpha)>=0.               (8)
~~~

This includes sign, odd truncated-linear, and odd nondecreasing
threshold features. Class centering is retained. Strict positivity
is not asserted when a feature vanishes on some or all labels.

There is a symmetric bilinear extension. For two such fixed
features phi,psi use

~~~
R_(d,e)=[phi(d)psi(e)+psi(d)phi(e)]/2.
~~~

At a unique latest x the full Born contribution is

~~~
phi(x)[psi(z)-psi(y)]+psi(x)[phi(z)-phi(y)]>=0.     (9)
~~~

The latest-y case is symmetric. The latest-z case is a sum of
nonnegative products. With a tied maximum, the full sum is (9)
plus phi(y)psi(z)+psi(y)phi(z), again nonnegative. In the
doubled case the possible totals are

~~~
phi(x)psi(2x)+psi(x)phi(2x),
phi(x)psi(2x)+psi(x)phi(2x)-phi(x)psi(x),
~~~

both nonnegative by monotonicity. Arbitrary nonnegative
later-source prices preserve this conclusion. The symmetric mixed
kernel need not itself be PSD; that is not claimed. A nonnegative
sum of outer products of these features is PSD and retains the
proved Born positivity.

## 5. The full signed-bank historical capacity identity

Fix the terminal bank and one normalized odd nondecreasing feature
z_d with |z_d|<=1. For the linear choice take z_d=d/H, H=H_N.
This normalization remains fixed on all earlier restrictions. Set

~~~
Q=|Fhat_N|=2q_N,
S=sum_(d in Fhat_N)z_d^2,
Lhat=Lhat_N(z;1),       Xhat=Lhat+S/2,
W=J+lambda z z^T,      0<=lambda<=1.
~~~

The full matrix is PSD and entrywise nonnegative. Every signed
prefix is centered. At the terminal bank,

~~~
M(W)=Q^2,     tr(W)=Q+lambda S,
sum_(d<e)z_d z_e=-S/2.                            (10)
~~~

For positive t, let K_n^W(t) be the correlation on unordered
signed source pairs in Fhat_n of positive difference t. Use the
physical unused-output mask t notin F_n, equivalently t notin
Fhat_n for positive t. The one historical capacity is

~~~
C_hist(W)=sum_(t>0)max_(n<=N)1[t notin F_n]K_n^W(t).
~~~

For fixed nonnegative W the correlation grows until its output
is used. The maximum counts exactly the source pairs whose output
birth is later than their source availability, or whose output has
not appeared by the terminal horizon. Therefore

~~~
C_hist(W)=sum_(d<e)W_(d,e)-Lhat_N(W).
~~~

Signed sources do not change this pair-lifetime argument: the output
is still positive and each pair is counted once. Using (10),

~~~
C_hist(J)-C_hist(W)=lambda(S/2+Lhat)=lambda Xhat,
                      Xhat>=S/2>=0.              (11)
~~~

Here Xhat is the full historical functional. It is not the older
positive-bank sum over mixed source births only. Signed new classes
can have positive outputs born later than the class; the cancellation
that treated every positive-bank new/new pair as born cannot be
transplanted. Same-birth signed pairs remain in Lhat throughout.

If a convolution identity is desired, its full form is
E_(P_N)(z)=NS+2Lhat+2Rhat, including every used signed pair.
This does not identify the old positive-bank causal increment or
its previous diagonal charge with a signed-bank counterpart.

In particular the positive-bank Abel formula with
D_n=S_(n-1)+(n-1)v_n must **not** be imported unchanged. Actual
same-birth signed pairs can retire later: in the Sidon history
{0,1,3}, the sources {-1,1} appear together at rank two, while
their output 2 appears at rank three. The existing positive-bank
formal declarations do not by themselves formalize these negative
source banks or the shifted support and holes proved below.
Nor does (6) or (8) prove a sign for the older positive-bank
birth-linear feature d-h_(tau(d)); that is a different source vector.

## 6. Exact future support, holes, and moments

Let a compatible actual future block B have m>=1 points, smallest
point b, and largest point b+L-1. Thus L is the integer interval
length used in the existing future-demand note. Assume Delta B
is disjoint from F_N, as it is for blocks of this same actual
Sidon history. Define

~~~
f_0(u)=sum_(a in B)1_(Fhat_N)(u-a),
f_z(u)=sum_(a in B)z_(u-a),
mu=sum_(d in Fhat_N)d z_d.
~~~

A common support interval is exactly bounded by

~~~
J={b-H,...,b+L-1+H},      T=|J|=L+2H.             (12)
~~~

Both extreme source labels -H,+H are present, so neither extreme
of this interval can be dropped from the uniform channel. In
particular its length is not L+2H-1 with this convention for L.

Both shadows vanish on every point of B. A distinct smoothing
point would require a signed difference of B in Fhat_N, and the
equal smoothing point would require the excluded label zero.
All m block points lie inside J. Thus a common support is

~~~
Omega=J\B,      D=|Omega|=L+2H-m>0.               (13)
~~~

There are m holes, including the smallest block point. The moments are

~~~
sum f_0=mQ,     sum f_z=0,
sum_u u f_z(u)=m mu.                              (14)
~~~

For the linear normalized feature,

~~~
S=(1/H^2)sum_(d in Fhat_N)d^2,
mu=(1/H)sum_(d in Fhat_N)d^2=H S>0.               (15)
~~~

For another normalized odd monotone feature mu is still
2sum_(d in F_N)d z_d>=0; the identity mu=HS is specific here
to the linear choice.

Cauchy in the separate feature channels gives

~~~
sum f_0^2>=m^2Q^2/D,
sum f_z^2>=LB(B):=12m^2mu^2/[T(T^2-1)].           (16)
~~~

For the second inequality center J at b+(L-1)/2 and use its
exact squared-coordinate sum T(T^2-1)/12. The zero mass in
(14) removes the centering constant. Here T>=3. A sharper
hole-aware variance may be used, but is not needed. If mu=0,
the additional lower bound is zero.

For the same full matrix W, actual Sidon uniqueness in B gives

~~~
E_B(W)=sum_u[f_0(u)^2+lambda f_z(u)^2]
      =m(Q+lambda S)+2sum_(t in Delta B)K_W(t).
~~~

This expansion remains valid for signed source labels. Hence the
raw demand

~~~
delta_mom(B,W)
 =[m^2Q^2/D+lambda LB(B)-m(Q+lambda S)]/2          (17)
~~~

and its positive part are paid by that actual nonnegative kernel.
Compatible blocks with disjoint physical difference sets must
still be paid by one physical maximum of their actual kernels,
retaining any true span masks. This is not a source budget per block.

## 7. Historical gain and good-epoch constants

Compare (17) with the unit mass-only demand using the same
actual denominator:

~~~
delta_J=[m^2Q^2/D-mQ]/2.
~~~

Equation (11) yields

~~~
[C_hist(J)-delta_J]-[C_hist(W)-delta_mom(B,W)]
 =lambda[Lhat+(LB(B)-(m-1)S)/2]
 >=lambda[LB(B)-(m-1)S]/2.                       (18)
~~~

This compares the specified raw demands. Their positive-part
comparison requires raw positivity, supplied below on good epochs.

At an existing two-lookahead good old rank N, the positive-bank
birth-linear variance is at least eta q_N, eta=2^-17, and the
next actual block has m=N and L<=32H. The old class feature is
(d-mean(G_j))/H. For each positive class,

~~~
sum_(d in G_j)d^2
 =sum_(d in G_j)(d-mean(G_j))^2+|G_j|mean(G_j)^2.
~~~

Thus the signed linear feature satisfies

~~~
eta Q<=S<=Q,      Q=2q_N=N(N-1),
T=L+2H<=34H,
LB(B)>=12N^2S^2/(34^3 H).                        (19)
~~~

If one fixed-onset cap gives H<=C N^2 log(2N), then for every
fixed 0<lambda<=1 the historical raw gain in (18) obeys

~~~
gain/Q^2
 >=6lambda eta^2/[34^3 C log(2N)]-lambda/(2N).     (20)
~~~

The diagonal term uses (N-1)/Q=1/N. It is not charged a second
time after applying Born positivity.

The mass-only raw demand for W itself is at least

~~~
(NQ/2)[(N-1)/(34C log(2N))-(1+lambda)].
~~~

It is eventually positive. The unit demand is then positive too,
and adding the nonnegative moment lower bound preserves positivity.
Thus (18)–(20) also compare positive parts beyond one fixed initial
range. The existing good-epoch reciprocal-log divergence makes
the individually normalized lower bounds (20) nonsummable, while
the dyadic sum of 1/N is finite.

This is a gain relative to the uniform **signed-bank** source.
It is not already a gain over the earlier positive-bank unit source.
For example, the signed sign-feature at lambda=1 has normalized
physical kernel exactly equal to that earlier kernel:

~~~
K_signed_unit=2K_diff+K_sum,
K_signed_sign=2K_diff-K_sum,
(K_signed_unit+K_signed_sign)/Q^2=K_diff/q_N^2.
~~~

Here K_sum counts ordered positive summands, including a repeated
summand once, so doubled labels are retained. The parent is treating
this kernel comparison and the shared maximum separately.

The finite positivity theorem, the odd-monotone extension, the full
historical identity, and the future demand (17) are established.
Summing gains from different terminal normalizations still requires
one physical envelope and its baseline margin. That global obligation
and original Q1 remain open.
