# Short three-sum flux: a finite boundary example and a positivity constraint

Status: Q1 unresolved. The actual finite family below does not satisfy the
full past range of the fixed-onset cap. It refutes a weaker local upper
bound on flux, not the cap-dependent upper bound still needed for Q1.
All statements are proved symbolically; no parameter search was performed.
Author: `/root/global_route`, GPT-6 Astra Ultra.

Use the fixed-bank notation and exact identities of
[nested_small_difference_bank.md](nested_small_difference_bank.md).
In particular, write

\[
 \Phi_N(D)=2\sum_{n\le N}R_n+\sum_{n\le N}S^{00}_n.
\]

The two-new-input channel satisfies sum S11<=sqrt(2)D^(3/2)+D, while
the automatic triangle channel is at most sqrt(2)D^(3/2). Therefore

\[
 T(F_N(D))-(2\sqrt2D^{3/2}+D)
 \le\Phi_N(D)\le T(F_N(D)).
\tag{1}
\]

This retains short labels and their actual latest-endpoint births, instead
of replacing them by an unrestricted sixth-moment count.

## 1. An actual finite Sidon family with nearly all short differences

Let Q tend to infinity through prime powers and put N=Q^2-1. Fix a
primitive element xi in F_(Q^2). For a in F_Q choose s_a in Z/N with
xi^(s_a)=xi+a, and let S={s_a:a in F_Q}.

This is the classical finite construction. A primary modern account is
Eberhard--Manners, [The apparent structure of dense Sidon sets,
Construction 3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p33/pdf/),
published 2023. The precise facts needed here have the following direct proof.

Equality of two pair sums in S gives
(xi+a)(xi+b)=(xi+c)(xi+d). Comparing the coefficients of xi and 1 after
cancelling xi^2 gives a+b=c+d and ab=cd, hence equality of the unordered
pairs, with multiplicity. Thus S is Sidon, including diagonal sums.

No nontrivial ratio (xi+a)/(xi+b) belongs to F_Q^*: comparing its xi
coefficient would force the ratio to be 1 and a=b. There are Q(Q-1)
distinct nontrivial ratios, exactly the number of elements outside F_Q^*.
Consequently the nonzero cyclic differences of S are precisely

\[
 (\mathbb Z/N)\setminus (Q+1)(\mathbb Z/N).
\tag{2}
\]

Each such difference has one ordered endpoint pair.

For a cyclic translation h, take the representatives of S+h in
{0,...,N-1} and then add 1. Denote the increasing integer Sidon set by
P_Q(h), contained in [1,N]. For an allowed cyclic difference d with
1<=d<=D<N, its unique pair is represented by an integer difference d
unless it wraps around the cut. Exactly d of the N cuts wrap that pair.

The number of forbidden subgroup labels in [1,D] is floor(D/(Q+1)).
Averaging the number of wrapped short pairs over cuts proves that some
h has

\[
 e:=D-|\Delta P_Q(h)\cap[1,D]|
 \le\left\lfloor\frac D{Q+1}\right\rfloor
      +\frac{D(D+1)}{2N}.
\tag{3}
\]

This is a simultaneous estimate for the whole short bank at the selected
width D. It does not appeal to an unproved distribution law for the
individual difference pairs.

## 2. Nearly maximal flux at the requested rank-width relation

Fix theta in (1/2,1), let D=ceil(Q^(1/theta)), and choose a cut given
by (3). Since 0<=D^theta-Q<=O(Q^(1-1/theta))=o(1), we have
floor(D^theta)=Q for all sufficiently large Q. Also D/Q tends to
infinity and D/N tends to zero. Equation (3) gives e=o(D).

The full set [1,D] has D(D-1)/2 ordered Schur triples. Deleting one
label removes at most 2D such triples: for a deleted t there are D-t
possibilities in either input position, and t-1 in the output position.
The union bound, including diagonals, therefore gives

\[
 T(F_Q(D))\ge\frac{D(D-1)}2-2De
             =\left(\frac12-o(1)\right)D^2.
\tag{4}
\]

Combining (1) and (4), along the actual ascending endpoint history of
P_Q(h), proves

\[
 \boxed{\Phi_Q(D)=\left(\frac12-o(1)\right)D^2.}
\tag{5}
\]

Every label in these fluxes is at most D, every label has its unique
physical endpoint pair, and every birth occurs by rank Q. Thus an
o(D^2) upper bound based only on Sidonness, short labels, and the
terminal relation p=floor(D^theta) is false. This conclusion is
stronger than merely observing that a general O(p^4) estimate permits
D^2 relations.

## 3. Exactly which compatible-cap hypotheses this family does not meet

Let m_0=ceil(Q/sqrt(log Q)). All prefixes of the **same** integer set
P_Q(h) satisfy, for Q sufficiently large,

\[
 a_m\le N\le2m^2\log(2m)\qquad(m_0\le m\le Q).
\tag{6}
\]

Indeed log(2m)>=log Q/2 on this range. This gives a compatible finite
history with about (1/2)log_2 log Q dyadic epochs, tending to infinity.
It has a moving onset.

There is an essential additional gap, emphasized by the parent review:

\[
 \frac{m_0}{\sqrt D}
 \asymp\frac{Q^{1-1/(2\theta)}}{\sqrt{\log Q}}
 \longrightarrow\infty.
\tag{7}
\]

The required past-block argument uses the entire interval of ranks from
sqrt D to D^theta. Equation (6) does not cover that interval. The family
therefore **does not refute** an upper bound which assumes the critical
cap for every rank in [sqrt D,D^theta], let alone one infinite history
with fixed onset.

It cannot even be extended by another Q points under a fixed terminal
critical cap. To see this, suppose B consists of Q later compatible points
and a_(2Q)<=4CQ^2 log(4Q), with C fixed. All short internal differences
of B must avoid F_Q(D). The interval-carrier inequality gives, for large Q,

\[
 \sum_{t\in\Delta B}(1-t/D)_+
 \ge\frac{D}{10C\log(4Q)}-\frac Q2
 \ge\frac{D}{20C\log(4Q)}.
\tag{8}
\]

Here the convolution denominator is at most 5CQ^2 log(4Q), because
the span of B has the assumed bound and D=o(Q^2). But all terms on
the left are supported on the e missing bank labels. By (3),

\[
 e=O(D/Q+D^2/N)=o(D/\log Q),
\]

contradicting (8). Thus (5) is a rigorous finite boundary example, not
evidence for an infinite counterexample or for the compatibility needed
by the current affirmative route.

Independent review: `/root/c143_mathematics` read Sections 1--3 and
confirmed the subgroup complement, cut average, ceiling choice, deletion
bound, moving-onset gap, and failed next-extension calculation. Later
sections were outside that particular review.

## 4. A further exact constraint: Fejer-weighted birth-bank positivity

For an arbitrary actual Sidon prefix P_p, define

\[
 w_D(d)=(1-|d|/D)_+,
\qquad
 h_{p,D}(t)=\sum_{d\in\pm F_p(D)}w_D(d)e^{2\pi i d t}.
\tag{9}
\]

This is a real trigonometric polynomial. Difference uniqueness and the
overlap of integer intervals give the exact Gram identity

\[
 \begin{aligned}
 p+h_{p,D}(t)
 &=\sum_{i,j\le p}w_D(a_i-a_j)e^{2\pi i(a_i-a_j)t}\\
 &=\frac1D\sum_{\ell\in\mathbb Z}
       \left|\sum_{a_i\in[\ell,\ell+D-1]}
                       e^{2\pi i a_i t}\right|^2\ge0.
 \end{aligned}
\tag{10}
\]

Each pair with displacement d is in exactly (D-|d|)_+ of the windows.
In particular h>=-p pointwise. If p=D^theta with theta<1, then

\[
 h_{p,D}(t)/D\ge-D^{\theta-1}= -o(1)
\tag{11}
\]

uniformly in t. This constrains a scaled limiting birth-bank profile; it
does not follow merely from an arbitrary nested subset of [1,D].

Let W=sum_(d in F_p(D))w_D(d), and define the weighted ordered Schur count

\[
 T_w=\sum_{x+y=z\atop x,y,z\in F_p(D)}w_D(x)w_D(y)w_D(z).
\]

Orthogonality gives

\[
 \int_0^1h^2=2\sum_{d\in F_p(D)}w_D(d)^2\le2D,
 \qquad \int_0^1h^3=6T_w.
\tag{12}
\]

For |t|<=1/(12D), viewed on the unit circle, every cosine in h is at
least 1/2, so h>=W. This interval has measure 1/(6D). The negative
cubic contribution is bounded in magnitude by p integral h^2, using
(10). It follows that

\[
 \boxed{T_w\ge\frac{W^3}{36D}-\frac{pD}{3}.}
\tag{13}
\]

The parent's fixed-onset weighted density theorem gives W>=cD and
p=o(D), so this is another direct proof that the short Schur flux has
order D^2. More useful than this redundant lower bound may be the
pointwise spectral restriction (11), especially when applied to birth
cohorts after controlling labels crossing rank boundaries.

No claim is made here that (11) alone excludes a limiting bank profile.
For instance a constant-density profile b on the physical scale has
Fejer-weighted transform b times the nonnegative transform of
(1-|s|)_+. Additional relations between births, actual endpoint blocks,
and different widths remain necessary.

## 5. Current scope

The finite example (5) shows that shortness and latest-endpoint birth alone
cannot force the desired o(D^2) upper bound. Its incompatible early past
and failed next extension are proved explicitly, so it does not settle
the full fixed-cap problem in either direction.

Equations (10)--(13) add an exact positivity constraint, without assuming
a random or spatially uniform correlation kernel. The current target is
to couple such constraints across the actual history, not to claim an
upper bound directly contradicted by the already proved density lower
bound. No proof or counterexample of Q1, and no new Lean verification,
is asserted.

## 6. Full terminal-bank retirement can be of order p^4

This answers an additional bounded question from C143. Let R(P) be the
cumulative retirement count for the full bank Delta P, in the increasing
endpoint order of a finite p-point integer Sidon set P. There is no
universal O(p^3) bound on R(P).

Suppose P is contained in [1,H], and let Q3(P) count unordered pairs of
distinct three-element subsets of P having the same sum. If two such
subsets shared a vertex, cancellation and Sidon uniqueness of two-sums
would make them equal. Thus each collision uses six distinct vertices.
Writing r(s) for the number of three-element subsets with sum s,
Cauchy--Schwarz over at most 3H possible sums gives

\[
 Q_3(P)=\frac12\left(\sum_s r(s)^2-\binom p3\right)
 \ge\frac{\binom p3^2}{6H}-\frac12\binom p3.
\tag{14}
\]

Let P*=H+1-P, also a positive integer Sidon set. Then

\[
 \boxed{Q_3(P)\le R(P)+R(P^*).}
\tag{15}
\]

To prove this, consider a six-vertex equal-sum collision. Write the side
containing its largest vertex as {m,u,v}, with u<v, and the other side
as {a,b,c}. If a>u and b<v can be achieved with distinct members a,b
of the other side, then

\[
 t=m-c=(a-u)-(v-b)>0.
\tag{16}
\]

The two source differences a-u and v-b are already present before m,
while the target t has the later endpoint m. Hence (16) is an actual
retirement record.

For completeness, this choice fails only when all three members of the
other side exceed v. Indeed the two candidate sets {x:x>u} and {x:x<v}
cover the other side. If both are nonempty, they have distinct choices:
otherwise their union would have only one member. The first candidate set
cannot be empty, because then the other sum is less than 3u whereas
m+u+v is greater than 3u. Thus failure means that the second set is empty.
The ordered membership pattern is then U,U,V,V,V,U. Reflection reverses
it to U,V,V,V,U,U, in which the required choices exist. Every collision
therefore gives a retirement record in P or in P*.

This assignment can be made injectively. A retirement record consists of
its target and its two positive source labels. Sidonness supplies their
unique endpoint pairs, so the two endpoint triples in (16) are recovered
from the record: if the larger source is a-u, the smaller source is v-b,
and the target is m-c, the recovered unordered pair of triples is
{{m,u,v},{c,a,b}}. The relative sizes of the source labels fix their roles.
For a reflected record apply the same reconstruction and reflect back.
Choose, for example, the lexicographically first valid record in the first
available orientation. One record cannot arise from two different
collisions. This proves (15), without discarding latest-endpoint orientation.

Take any dense finite Sidon family with H<=C p^2, for example the integer
representatives of the finite construction in Section 1, with C=1. Equations
(14)--(15) give

\[
 \max\{R(P),R(P^*)\}
 \ge\frac{\binom p3^2}{12Cp^2}-\frac14\binom p3
 =\left(\frac1{432C}+o(1)\right)p^4.
\tag{17}
\]

Thus actual latest-birth retirement, and not only the unrestricted sixth
moment, can have order p^4. This statement concerns the full terminal
difference bank, with physical width at most H=O(p^2). It does not assert
the full early-past cap or its infinite fixed-onset analogue.

## 7. Centering alone does not bound the retirement operator by O(p log p)

Let P be an m-point Sidon set with R(P)>=c m^4, obtained from Section 6
by choosing the appropriate orientation. Append m new points successively,
always choosing the next point x>3 max(old set). This preserves Sidonness:
every new difference exceeds the old span and distinct new differences
have distinct old endpoints. All points remain positive integers.

At such an appended point, every newly born target difference is greater
than the old span. A difference between two already existing positive
source labels is at most the old span. Hence **no** retirement occurs
during any of the appended steps. The terminal retirement graph is exactly
the old graph on the q0=binom(m,2) original labels, together with isolated
vertices for all newly created labels.

The terminal point count is p=2m. The number of added labels is

\[
 q_1=\binom{2m}{2}-\binom m2=\frac{3m^2-m}{2}\ge q_0.
\]

Define a vector on all terminal positive labels by v_d=1 on the original
labels and v_d=-q0/q1 on the added labels. Then

\[
 \sum_d v_d=0,\qquad
 R=vv^T\succeq0,\qquad R\mathbf1=0,
 \qquad\operatorname{tr}R
 =q_0+q_0^2/q_1\le2q_0\le m^2.
\tag{18}
\]

All retired pairs have both labels in the old block, where v is 1. Thus

\[
 \sum_{\{d,e\}\text{ retired}}R_{de}
 =R(P)\ge c m^4,
 \qquad
 \frac{\sum_{\{d,e\}\text{ retired}}R_{de}}
      {\operatorname{tr}R}\ge c m^2=\frac c4p^2.
\tag{19}
\]

This disproves a universal Sidon-only estimate of order
p log(p) tr(R) for centered positive-semidefinite matrices. If the
retirement convention sums both matrix orientations, both sides of the
retirement count simply acquire the corresponding factor 2.

The padding is deliberately sparse and destroys the terminal critical
growth bound. Equation (19) does not disprove a theorem that additionally
uses the full fixed-onset cap. It shows precisely that matrix centering,
Sidonness, and latest-endpoint retirement alone are insufficient.
