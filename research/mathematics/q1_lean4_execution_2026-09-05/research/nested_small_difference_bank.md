# Nested small-difference banks: exact birth and retirement identities

Status: Q1 unresolved. These are exact identities for actual integer Sidon
sets, with an additional conditional consequence of the fixed-onset cap.
No uniformity or randomness of the correlations is assumed. No Lean proof
of Q1 is supplied. Author: `/root/global_route`, GPT-6 Astra Ultra.

## 1. A single physical bank throughout the history

Let a_1<a_2<... be a positive integer Sidon sequence, including uniqueness
of sums with repeated summands. Fix an integer D>=1 once and for all, and put

\[
 P_n=\{a_1,\ldots,a_n\},\qquad
 F_n=\Delta P_n\cap[1,D],\qquad F_0=\varnothing.
\]

Every positive difference has one physical endpoint pair. Its birth is the
larger endpoint rank. Hence

\[
 F_n=F_{n-1}\sqcup G_n,\qquad
 G_n=\{a_n-a_i: i<n,\ a_n-a_i\le D\}.
\tag{1}
\]

For finite H contained in the positive integers define, for t>0,

\[
 K_H(t)=\sum_x1_H(x)1_H(x+t),\qquad
 T(H)=\sum_{t\in H}K_H(t),\qquad
 E(H)=\sum_{t\notin H}K_H(t).
\tag{2}
\]

Thus T counts ordered Schur triples (x,y,z) in H with x+y=z, including
x=y. Also

\[
 T(H)+E(H)=\binom{|H|}{2}.
\tag{3}
\]

Here E is exactly the positive pair weight whose difference label has not
yet entered the same bank. The bank and its mask evolve together.

## 2. The special structure of one actual birth batch

Write F=F_(n-1), G=G_n, f=|F|, g=|G|. For distinct g_1,g_2 in G,

\[
 |g_1-g_2|=|a_i-a_j|\in F.
\tag{4}
\]

The difference is positive and less than D, and both endpoints precede n.
This proves two facts that arbitrary nested subsets of [1,D] need not have:

* K_G is supported on F.
* G is sum-free. Indeed, g_1+g_2=g_3 would make g_3-g_1 a member of both
  F and G; the diagonal g_1=g_2 is covered by the same argument.

Equivalently, the latest-point equation a_n+a_k=a_i+a_j would violate
Sidonness if a Schur triple lay wholly in G.

Define the positive cross-pair kernel

\[
 J_{F,G}(t)=\#\{(x,y)\in F\times G: |x-y|=t\}.
\]

The pointwise correlation increment is exact:

\[
 K_{F\cup G}(t)-K_F(t)=K_G(t)+J_{F,G}(t).
\tag{5}
\]

There is no averaging or model assumption in (4) or (5).

## 3. Three distinguished fluxes, with all diagonals retained

Set

\[
 R_n=\sum_{t\in G}K_F(t),
\tag{6}
\]

the number of previously available old pairs retired by new difference
labels. For H define r_(H+H)(z)=sum_x 1_H(x)1_H(z-x), an **ordered**
representation count. Define

\[
 S^{00}_n=\sum_{z\in G}r_{F+F}(z),\qquad
 S^{11}_n=\sum_{z\in F}r_{G+G}(z).
\tag{7}
\]

The first is the formation of a new output label from two old labels; the
second is the formation of an old output from two new labels. Repeated
inputs are included, so neither quantity may silently be divided by two.

Then

\[
 \boxed{T(F_n)-T(F_{n-1})
       =2R_n+S^{00}_n+2\binom g2+S^{11}_n.}
\tag{8}
\]

Proof: partition the new ordered Schur triples x+y=z by membership in F
or G. If exactly one input lies in G and the other input and output lie
in F, the count is 2R_n. If only the output lies in G, the count is
S00_n. If one input and the output lie in G and the other input lies in
F, each unordered pair of distinct members of G supplies its positive
difference in F, giving exactly 2 binom(g,2). If both inputs lie in G
and the output lies in F, the count is S11_n. Three members in G are
impossible by sum-freeness. This exhausts all cases.

Combining (3) and (8) gives the available-pair balance

\[
 \boxed{E(F_n)-E(F_{n-1})
       =fg-\binom g2-2R_n-S^{00}_n-S^{11}_n.}
\tag{9}
\]

In particular

\[
 \Delta E\le fg-\binom g2-2R_n.
\tag{10}
\]

The coefficient 2 on retirement is substantive: one contribution retires
an old pair, and the same Schur relation immediately masks a new cross
pair. To see the complete accounting directly from (5),

\[
 \sum_{t\in F\cup G}J_{F,G}(t)
 =\binom g2+R_n+S^{00}_n+S^{11}_n.
\tag{11}
\]

All new-new pairs are immediately masked by (4); their entire
binom(g,2) source cancels from the first form
Delta E=fg-R_n-sum_(t in F union G)J_(F,G)(t).

The potential E need not be monotone. Formula (9), rather than a monotonicity
assertion, is the exact discrete differential law.

## 4. Fixed-bank summation and the size of the automatic triangle channel

For N finite, write M=|F_N|. Summing (8) yields

\[
 T(F_N)=2\sum_{n\le N}R_n
       +\sum_{n\le N}(S^{00}_n+S^{11}_n)
       +2\sum_{n\le N}\binom{|G_n|}{2}.
\tag{12}
\]

Each G_n is a reflection of a subset of A inside an interval of diameter
at most D-1. Its positive differences are distinct, so

\[
 \binom{|G_n|}{2}\le D-1,\qquad
 |G_n|\le\sqrt{2D}+1.
\]

Since the new labels are globally disjoint within the fixed bank,
sum_(n<=N)|G_n|=M<=D. It follows that

\[
 2\sum_{n\le N}\binom{|G_n|}{2}
 \le \sqrt{2D}\,M\le\sqrt2 D^{3/2}.
\tag{13}
\]

Consequently a bound T(F_N)>=lambda D^2, with fixed lambda>0, forces

\[
 2\sum_{n\le N}R_n+
 \sum_{n\le N}(S^{00}_n+S^{11}_n)
 \ge\lambda D^2-\sqrt2D^{3/2}.
\tag{14}
\]

The automatic three-point difference triangles cannot alone account for
such an old-mask mass. This conclusion uses the actual endpoint births,
not merely the cardinalities of arbitrary nested sets.

## 5. How the fixed-onset cap makes (14) relevant at early ranks

Assume, only in this section,

\[
 a_n\le Cn^2\log(2n)\quad(n\ge n_0),
\tag{15}
\]

with C and n_0 fixed. Let p=floor(D^theta), where theta lies in a fixed
compact interval [theta_0,theta_1] contained in (1/2,1). Set F=F_p and
M=|F|. The cardinality lower bound M>=cD, uniformly in this range, is
being treated by the parent task. The following implication is explicit:

\[
 M\ge cD\quad\Longrightarrow\quad T(F_p)\ge c' D^2
 \quad\text{for all sufficiently large }D,
\tag{16}
\]

where c'>0 depends only on C,c,theta_0. No unproved assertion that K_F
is spatially uniform is used to prove this implication.

Here is a direct verification of (16), also independently reviewing the
localized-carrier calculation from `/root/c143_mathematics`. Take disjoint
past dyadic blocks B_m={a_(m+1),...,a_(2m)}, with m a power of two and
sqrt D<=m<=p/2. Let L_m be their integer interval length. Then

\[
 mM+2\sum_{t\in\Delta B_m}K_F(t)
      =\|1_{B_m}*1_F\|_2^2
      \ge\frac{m^2M^2}{L_m+\operatorname{diam}F}.
\]

The support has the indicated length; using a possibly longer interval
only weakens the lower bound. For sufficiently large D, uniformly in m,

\[
 L_m\le4Cm^2\log(4m),\qquad
 \operatorname{diam}F\le D\le m^2,
 \qquad 1\le C\log(4m),
\]

so the denominator is at most 5Cm^2 log(4m). Therefore

\[
 \sum_{t\in\Delta B_m}K_F(t)
 \ge\frac{M^2}{10C\log(4m)}-\frac{mM}{2}.
\]

The labels in the different Delta B_m are disjoint. Every such label that
has nonzero K_F is less than D and lies in F_p. Summing gives

\[
 T(F_p)\ge\frac{M^2}{10C}
       \sum_{\sqrt D\le m\le p/2\atop m\text{ dyadic}}
          \frac1{\log(4m)}-\frac{pM}{2}.
\tag{17}
\]

By comparison of a harmonic sum with its integral, uniformly for the
specified theta range,

\[
 \sum_m\frac1{\log(4m)}
 =\frac{\log(2\theta)}{\log2}+O(1/\log D).
\]

Also p/M<=c^(-1)D^(theta_1-1) tends to zero. It follows, for example, that

\[
 T(F_p)\ge
 \frac{\log(2\theta_0)}{20C\log2}\,M^2
 \ge\frac{c^2\log(2\theta_0)}{20C\log2}\,D^2
\tag{18}
\]

once D is sufficiently large. Thus a completed proof of the parent's
bank-density lower bound supplies the hypothesis of (14) by an elementary
past-block argument. The onset in (15) is uniform throughout this deduction.

## 6. The additional relations are actual three-sum equalities

The three nonautomatic fluxes have a concrete endpoint meaning. For an old
label x=a_b-a_a, another old label y=a_d-a_c, and a new label
z=a_n-a_i:

* S00 contains z=x+y, equivalent to
  a_n+a_a+a_c=a_i+a_b+a_d.
* R contains z=y-x, equivalent to
  a_n+a_b+a_c=a_i+a_d+a_a.
* S11 contains (a_n-a_i)+(a_n-a_j)=a_b-a_a, equivalent to
  2a_n+a_a=a_b+a_i+a_j.

The latest a_n occurs only on the displayed left side, so these are
nontrivial three-sum equalities. Indices among the old points can coincide;
the statement is not that all six endpoints are distinct. Positive-difference
uniqueness makes each involved label's endpoint representation unambiguous.

Therefore (14) and (18), conditional on M>=cD, force order D^2 of these
rank-tagged relation contributions by rank D^theta. Simply counting the
automatic relations among three original points gives only the lower-order
quantity in (13).

## 7. What is established, and what still needs a coupled argument

Equations (5), (8), (9), (11), and (12) give exact correlation, retirement,
and energy identities for one bank shared by all prefixes. In particular,
retirement by the newly born physical labels is coupled to immediate
cross-pair masking with coefficient 2. Equation (13) separates the automatic
endpoint triangles from the additional three-sum relations that (18) needs.

This does not yet give a contradiction: T(F)<=binom(|F|,2) still permits
a positive constant proportion of masked mass. Nor is a separate copy of
the fixed-D budget automatically available at every D. The same relation
can occur in many banks, so summing (14) over D requires its physical
multiplicity to be accounted for.

The identities also hold in very sparse infinite Sidon sequences. For
example, an infinite Sidon set in which every positive difference eventually
appears will eventually have F_n(D)=[1,D] for each fixed D, and hence
T(F_n(D))=binom D2. That fact alone says nothing about the rank of this
event. The cap-relevant new requirement is that the forced flux in (14)
already occurs by p=D^theta with one fixed onset and constants, uniformly
over large D.

No bound excluding that early flux, and no simultaneous multi-kernel
envelope separation, has been proved in this note. Q1 remains unresolved.

## 8. Independent review and two refinements

`/root/c143_mathematics` independently expanded every membership case in
(8), and confirmed (8)--(11), including the factor 2 and diagonal terms.
The parent subsequently proved the density premise in
[fixed_width_bank_density.md](fixed_width_bank_density.md), equations
(2)--(10). I independently checked its support lengths, Cauchy--Schwarz
coefficients, disjoint dyadic labels, uniform harmonic-sum limit, and error
terms. Thus (14) together with (18) is now a proved conditional consequence
of the single fixed-onset cap (15), rather than a consequence of an additional
unproved density premise. This still does not prove Q1.

First, the two-new-input channel is also lower order:

\[
 S^{11}_n\le |G_n|^2,\qquad
 \sum_{n\le N}S^{11}_n
 \le(\sqrt{2D}+1)M\le\sqrt2D^{3/2}+D.
\tag{19}
\]

Hence the principal required flux is already

\[
 \boxed{\quad
 2\sum_{n\le p}R_n+\sum_{n\le p}S^{00}_n
 \ge\kappa c^2D^2-2\sqrt2D^{3/2}-D,
 \quad}                                                    \tag{20}
\]

where c and kappa may be taken from the parent's density note. Only one
new positive label appears in each relation counted on the left.

Second, C143 derived the following exact historical envelope, which I
independently checked. For the unit-weight nested kernels let

\[
 \mathcal C_N(D)=\sum_{t>0}\max_{0\le n\le N}
                    1[t\notin F_n]K_{F_n}(t).
\]

For each physical t the unmasked kernel increases until t is born, and
then its eligibility disappears. A born t attains its peak just before
birth; a surviving t attains its peak at N. Therefore

\[
 \mathcal C_N(D)=E(F_N)+\sum_{n\le N}R_n.
\tag{21}
\]

Writing Z=sum_n(S00_n+2 binom(|G_n|,2)+S11_n), equation (12) gives

\[
 \boxed{\mathcal C_N(D)
 =\binom M2-\frac12T(F_N)-\frac12 Z.}
\tag{22}
\]

A maximum over a subset of the prefixes is at most this all-prefix
envelope. The identity is for nested **unit** kernels; independent arbitrary
row weights need not preserve kernel monotonicity. It accounts for historical
retirement and does not pretend that the final mask alone was always active.
