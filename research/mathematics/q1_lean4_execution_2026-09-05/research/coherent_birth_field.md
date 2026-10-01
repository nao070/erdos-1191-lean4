# A coherent integer birth field with the same leading bank profile

Status: an abstract physical-label model, not an integer Sidon sequence.
This removes the independent-width limitation of the earlier relaxation.
It does not realize endpoint incidence or the required number of positive
differences. Q1 remains unresolved. Author: `/root/global_route`,
GPT-6 Astra Ultra. The model was proposed by the parent; the arguments
below verify its leading statistics and handle integer birth ties.

## 1. One permanent birth rank for each physical label

Independently for each integer d>=2 choose beta_d with defective finite CDF

\[
 B(s)=\begin{cases}
 0,&s\le1/2,\\
 \frac1{10}\log_2(2s),&1/2<s<1,\\
 1/10,&s\ge1.
 \end{cases}
\tag{1}
\]

The remaining mass 9/10 is at infinity. The finite part has density
1/(10 log(2) s) on (1/2,1), with no finite atoms. Put

\[
 \tau(d)=\lceil d^{\beta_d}\rceil,
 \qquad \tau(d)=\infty\text{ if }\beta_d=\infty,
 \qquad\tau(1)=\infty.
\]

For integer rank p and width D define

\[
 F_p(D)=\{1\le d\le D:\tau(d)\le p\}.
\tag{2}
\]

The same tau(d) is used at every width. In particular all set restrictions
between different widths and ranks are exact, not independently coupled
copies. For integer p, ceiling introduces no error into membership:

\[
 q_d(p):=\Pr(\tau(d)\le p)
       =B\left(\frac{\log p}{\log d}\right)
       \qquad(d\ge2).
\tag{3}
\]

Write p=floor(D^theta), with theta in a compact subinterval of (1/2,1),
and b(theta)=B(theta). For fixed epsilon>0, uniformly for epsilon D<=d<=D,

\[
 q_d(p)\longrightarrow b(\theta).
\tag{4}
\]

Indeed log d=log D+O_epsilon(1), while log p=theta log D+o(1).
This proves the constant spatial profile on the bulk of every large bank.

## 2. The leading statistics retain their strict birth ordering

Use the same definitions of M,W,T,E,R,S00 and the historical envelope C
as in [birth_profile_relaxation.md](birth_profile_relaxation.md), except
that histories now run over integer ranks n<=p. In particular R counts
source pairs d<e for which

\[
 \max\{\tau(d),\tau(e)\}<\tau(e-d)\le p.
\tag{5}
\]

S00 counts ordered x+y=z with
max{tau(x),tau(y)}<tau(z)<=p. Simultaneous births are not declared to be
earlier births. The historical envelope continues to satisfy the exact
identity C=E+R for arbitrary nested unit banks, even with batches.

For bulk labels d_i>=epsilon D and finite beta_d_i,

\[
 \frac{\log\tau(d_i)}{\log D}=\beta_{d_i}+o(1)
\]

uniformly, since beta lies in [1/2,1]. Distinct labels have independent
beta variables. The finite density is bounded, so the probability that
two of them are within o(1) is o(1). Thus strict integer birth comparisons
converge to strict comparisons of independent beta marks. All thresholds
here stay inside the atom-free interval (1/2,1). The atom at infinity
does not create a boundary issue: a source is required to be born by p,
while an infinite target is simply always later.

Terms containing a label below epsilon D number O(epsilon D^2), and
equal-input Schur terms number O(D). Consequently the same computation
as for common uniform marks gives

\[
 \begin{array}{c|c}
 \text{quantity}&\text{limit}\\ \hline
 M/D&b\\
 W/D&b/2\\
 T/D^2&b^3/2\\
 R/D^2&b^3/6\\
 S^{00}/D^2&b^3/6\\
 \Phi/D^2=(2R+S^{00})/D^2&b^3/2\\
 E/D^2&b^2(1-b)/2\\
 \mathcal C/D^2&b^2/2-b^3/3\\
 T_w/D^2&11b^3/120.
 \end{array}
\tag{6}
\]

For example the retirement probability of a bulk pair tends to
integral_(1/2)^theta B(s)^2 dB(s)=b^3/3. The number of unordered
positive source pairs is asymptotic to D^2/2. The old-output-new-input
versus new-output-old-input roles have not been merged before this
calculation.

## 3. Quantitative control of integer birth ties

For d large and any finite integer n, the atom at n is at most

\[
 \Pr(\tau(d)=n)
 \le\frac{C_0}{(n-1)\log d}
 \le\frac{C_1}{\sqrt d\log d},
\tag{7}
\]

whenever that atom is nonzero. The first inequality integrates the
bounded beta density over
(log(n-1)/log d,log n/log d]; the second uses n>=ceil(sqrt d).
All constants are absolute and only large d are used.

Let J_D count unordered pairs of distinct labels at most D having the
same **finite** birth rank. Split labels at D^(2/3). Pairs with a small
label number O(D^(5/3)). For each pair of larger labels, independence
and (7) bound its tie probability by O(D^(-1/3)/log D). Therefore

\[
 \mathbb E J_D=O(D^{5/3}).
\tag{8}
\]

This estimate is uniform in any terminal rank cutoff, since removing a
cutoff only adds finite ties. If G_n(D)={d<=D:tau(d)=n}, then

\[
 \sum_{n<\infty}|G_n(D)|^2
 =|\{d\le D:\tau(d)<\infty\}|+2J_D=o(D^2)
\tag{9}
\]

in probability, and almost surely as justified below. Any non-diagonal
Schur triple with a tied latest birth contains a pair counted by J_D.
A pair of labels belongs to only a bounded number of ordered Schur
triples, because the third label is fixed by a sum or a difference.
Diagonal Schur triples contribute O(D). Thus the entire tied-birth Schur
contribution is o(D^2).

For arbitrary batches the actual endpoint identity
Delta G_n subset F_(n-1) need not hold in this model, so one must not
apply the special actual-Sidon flux law to these batches. Instead, unique
latest births contribute exactly 2R or S00, and all the remaining Schur
contributions are the negligible ties just counted. This proves the
leading Phi=T identity in (6) without pretending to have endpoint stars.

## 4. One realization can satisfy all large widths and compact theta ranges

The counts in (6), apart from harmless diagonal corrections, are sums
of O(D^2) bounded terms, each depending on at most three independent
beta variables. Each variable appears in O(D) terms. Consequently every
such count has variance O(D^3), uniformly in p. The same dependency
count gives Var(J_D)=O(D^3). Weighted counts have bounded weights and
the same variance bound. The one-label quantities M and W have variance
O(D), so their normalizations by D have the same O(1/D) Chebyshev error
as the other quantities normalized by D^2.

Fix a rational theta in (1/2,1). On the subsequence D_k=k^2, Chebyshev's
inequality for an error epsilon D_k^2 has summable probability O(1/k^2).
Borel--Cantelli, followed by epsilon in a countable sequence tending to
zero, gives (6) almost surely along these widths. The same proof and (8)
give J_D/D^2 tending to zero along the subsequence.

All of M,W,T,R,S00,C and T_w are nondecreasing when D and p increase
together. For W and T_w the triangular weights also increase with D.
The quantities E=C-R and Phi=2R+S00 are handled from these counts.
Since D_(k+1)/D_k tends to 1, monotone interpolation yields the limits
at every integer D. The same argument applies to J_D.

Intersect these probability-one events over rational theta. Monotonicity
in p, a finite rational grid in theta, and continuity of the polynomials
in b(theta) give uniform convergence on every compact theta interval
inside (1/2,1). Thus there is a probability-one set of **one coherent
birth fields** for which all the limits in (6) hold in this sense.

In particular any finite collection of diverging widths and exponents
in such a compact interval satisfies these leading limits jointly, with
the same physical tau(d). This does not assert independence between
different widths; their overlaps are exactly the overlaps prescribed
by (2). Their joint indicators obey, for example,

\[
 1[\tau(d)\le p_1]1[\tau(d)\le p_2]
 =1[\tau(d)\le\min(p_1,p_2)].
\]

## 5. Fejer cohort profiles remain consistent

For each threshold the limiting measure is nu_theta=b(theta) dx on [0,1].
For any fixed continuity exponents alpha<beta in (1/2,1),

\[
 2\int_0^1(1-x)\cos(2\pi\xi x)\,
                 d(\nu_\beta-\nu_\alpha)(x)
 =[b(\beta)-b(\alpha)]
   \left(\frac{\sin(\pi\xi)}{\pi\xi}\right)^2\ge0.
\tag{10}
\]

The empirical convergence used here follows from the same independent-mark
variance estimate, first for interval counts and then for continuous tests.
It can be made simultaneous for a countable dense set of test functions
and rational thresholds; bounded mass and monotone interpolation complete
the weak-convergence statement. It uses the same coherent realization as
Section 4.

The finite tied-birth batches therefore change neither the leading
Schur coefficients nor the limiting Fejer increment. For C=10 all the
scalar density and old-mask inequalities checked in the earlier note
remain satisfied by the same b(theta).

## 6. A stronger finite Fourier check for fixed cohort exponents

The following optional check clarifies that the continuum Fourier sign
is not hiding a leading negative fluctuation. Put p_alpha=floor(D^alpha)
and p_beta=floor(D^beta), for fixed 1/2<alpha<beta<1. For all large D,
D<p_alpha^2. For every d between p_beta and D both arguments of B in
(3) are in its logarithmic branch. Hence the expected cohort membership
probability is the exact constant

\[
 q=B\left(\frac{\log p_\beta}{\log d}\right)
   -B\left(\frac{\log p_\alpha}{\log d}\right)
  =\frac1{10\log2}\log\frac{\log p_\beta}{\log p_\alpha}.
\]

For smaller labels that probability lies between 0 and q. Thus the
expected symmetric weighted cohort polynomial is q(F_D(t)-1), where
F_D is the nonnegative Fejer kernel, minus a symmetric polynomial
with nonnegative coefficients, each at most q, supported below p_beta.
It is bounded below by

\[
 -q-2qp_\beta.
\tag{11}
\]

Here q<=1/10 and p_alpha/p_beta tends to zero. Its negative bound has
a strict margin below p_beta-p_alpha. At a fixed t, the centered cohort
polynomial is a sum of D independent bounded variables. Exponential
concentration and a polynomial-size grid, using the deterministic
O(D^2) derivative bound, give uniform fluctuations at most D^(1/2+epsilon)
with summably small failure probability. Choose epsilon<beta-1/2.
It follows that, almost surely for all sufficiently large D,

\[
 h_{F_{p_\beta}(D)}(t)-h_{F_{p_\alpha}(D)}(t)
 \ge-(p_\beta-p_\alpha)\quad\text{for every real }t.
\tag{12}
\]

The same conclusion holds for any fixed finite list of cohort exponents.
This is a scalar Fourier inequality in the abstract model. It does not
give the integer-window Gram representation or any endpoint realization.

## 7. A definite missing condition: the total label cardinality is wrong

The model still cannot be the difference births of an actual p-point
Sidon prefix. Since beta_d>=1/2 whenever it is finite, every label born
by p is at most p^2. Let N(p)=|{d:tau(d)<=p}|. Then

\[
 \mathbb E N(p)=\sum_{2\le d\le p^2}
                    B\left(\frac{\log p}{\log d}\right)=o(p^2).
\tag{13}
\]

To see this without a delicate asymptotic expansion, fix epsilon>0.
For epsilon p^2<=d<=p^2 the argument of B tends uniformly to 1/2,
where B is continuous and zero. The remaining labels contribute at
most epsilon p^2. Let epsilon decrease to zero. Also Var(N(p))<=p^2,
so Chebyshev's inequality has summable error probabilities O(1/p^2)
after normalizing by p^2. Therefore N(p)=o(p^2) almost surely.

An actual p-point Sidon set has exactly binom(p,2) positive difference
labels, not o(p^2). In addition the coherent batches have not been
shown to satisfy Delta G_n subset F_(n-1), nor to come from a common
new endpoint. These are explicit remaining failures, not harmless
rounding details.

The present result removes one previous limitation: the same abstract
label can now carry a fixed integer birth rank across all widths while
retaining the stated leading statistics and Fourier cohort constraints.
It does not resolve the endpoint realization, the total cardinality
deficit, or Q1.
