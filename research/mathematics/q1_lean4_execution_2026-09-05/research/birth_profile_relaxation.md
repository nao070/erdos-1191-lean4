# An explicit birth-profile relaxation satisfying the current leading identities

Status: a bounded countermodel to a collection of relaxed constraints.
This is **not** an actual Sidon endpoint construction, does not realize
integer endpoint ranks, and does not establish compatibility across changing
physical widths. Q1 remains unresolved. Author: `/root/global_route`,
GPT-6 Astra Ultra.

The purpose is to check simultaneously the exact leading Schur flux,
available-pair energy, historical envelope, weighted density, and Fejer
cohort positivity. None of these quantities will be assumed to behave
randomly for an actual Sidon set. The random construction below defines a
separate abstract bank model and proves what that model satisfies.

## 1. Definition at one physical width

For each fixed D, assign independent uniform marks U_d in [0,1] to the
physical labels d=1,...,D. For 1/2<=theta<=1 put

\[
 b(\theta)=\frac1{10}\log_2(2\theta),\qquad
 F_D(\theta)=\{d\le D:U_d\le b(\theta)\}.
\tag{1}
\]

These are genuinely nested subsets of the same interval [1,D], with
0<=b<=1/10. The scalar theta is a continuum parameter. It is not the
logarithm of the birth rank of a realized pair of integer endpoints.

Run the banks from mark threshold 0 to threshold b. With probability one
the D marks are distinct, so one label enters at a time. Define M,W,K,T,E,
R,S00 and the all-time historical envelope exactly as for a finite bank:

\[
 \begin{aligned}
 M&=|F|,& W&=\sum_{d\in F}(1-d/D),\\
 T&=\sum_{x+y=z\atop x,y,z\in F}1,&
 E&=\binom M2-T,\\
 \mathcal C&=\sum_{t>0}\max_{0\le u\le b}
                  1[t\notin F(u)]K_{F(u)}(t).
 \end{aligned}
\]

R and S00 are cumulative up to b, not instantaneous values.
The historical envelope identity C=E+R holds for these nested unit banks
just as it does for actual banks. Its proof requires only increasing
kernels and a one-time retirement mask.

## 2. Exact leading coefficients

The following limits hold in probability as D tends to infinity:

\[
 \begin{array}{c|c}
 \text{quantity}&\text{limit after normalization}\\ \hline
 M/D&b\\
 W/D&b/2\\
 \binom M2/D^2&b^2/2\\
 T/D^2&b^3/2\\
 R/D^2&b^3/6\\
 S^{00}/D^2&b^3/6\\
 \Phi/D^2=(2R+S^{00})/D^2&b^3/2\\
 E/D^2&b^2(1-b)/2\\
 \mathcal C/D^2&b^2/2-b^3/3.
 \end{array}
\tag{2}
\]

Here is a derivation preserving the birth ordering. For a pair of labels
d<e with t=e-d, except for the O(D) pairs with t=d, the three marks are
independent. This pair is retired by t by threshold b exactly when

\[
 \max(U_d,U_e)<U_t\le b.
\]

Its probability is integral_0^b u^2 du=b^3/3. There are D(D-1)/2
candidate pairs, giving R/D^2=b^3/6. Similarly an ordered Schur triple
x+y=z has its output born after both inputs, by threshold b, with
probability b^3/3. Thus S00/D^2=b^3/6. Equal-input cases contribute
only O(D).

The probability for an available pair is b^2(1-b), giving the stated E.
Its contribution to the historical envelope is present precisely when

\[
 \max(U_d,U_e)\le b,\qquad
 \max(U_d,U_e)<U_t.
\]

The probability is integral_0^b 2u(1-u)du=b^2-2b^3/3. This also proves
the stated C directly, as well as through C=E+R.

To justify that the expectations describe actual abstract bank realizations,
each normalized count is a sum of O(D^2) bounded indicators, each depending
on at most three marks. A given mark participates in O(D) such indicators;
only O(D^3) pairs of indicators share a mark. The variance is therefore
O(D^3), so division by D^4 and Chebyshev's inequality give convergence in
probability. M and W are even simpler sums of independent variables.
The bounds are uniform for any fixed finite set of b-values.

One can also obtain uniform convergence in b on [0,1/10]: use a finite
fine grid, monotonicity of M,W,T,R,S00 and C, and continuity of their
limiting polynomials. E=C-R is handled as a difference of two such
quantities. Thus deterministic realizations approximating (2) throughout
this continuum interval exist for arbitrarily large D. They remain
abstract labeled banks.

## 3. Flux and historical-mask identities all agree

The differential identities at leading order are

\[
 d(T/D^2)=\frac32 b^2\,db,
 \qquad d(R/D^2)=d(S^{00}/D^2)=\frac12b^2\,db,
\]

so dT=2dR+dS00. Single-label births have no new-new pair channel, and
the repeated-input S11 channel has at most D events. It disappears after
division by D^2. Consequently Z/D^2=b^3/6 and

\[
 \frac{\mathcal C}{D^2}
 =\frac{b^2}{2}-\frac12\frac{T}{D^2}
                    -\frac12\frac Z{D^2}
 =\frac{b^2}{2}-\frac{b^3}{3}.
\tag{3}
\]

In particular the half-mask historical-envelope saving is retained; it is
not replaced by the terminal mask or omitted from the model.

## 4. Weighted density and the old-mask lower bounds are compatible

Take the numerical cap parameter C=10 in the lower bounds derived by the
parent, without asserting that the model has any integer cap realization.
Their leading weighted-density requirement is

\[
 \frac WD\ge\frac{\log(2\theta)}{10C\log2}.
\]

Our profile instead has

\[
 \frac WD\longrightarrow\frac b2
 =\frac{\log(2\theta)}{20\log2}
 =5\,\frac{\log(2\theta)}{10C\log2}.
\tag{4}
\]

The stronger leading past-carrier lower bound
T/M^2>=log(2theta)/(10C log2) is also satisfied with the same factor-five
margin, because T/M^2 tends to b/2. Thus the density and old-mask
requirements hold simultaneously on every compact theta interval inside
(1/2,1), with one explicit choice of constants.

The same margin holds for weighted birth increments: for alpha<beta,

\[
 \frac{W_\beta-W_\alpha}{D}\longrightarrow
 \frac{b(\beta)-b(\alpha)}2
 =\frac{\log(\beta/\alpha)}{20\log2}
 =5\,\frac{\log(\beta/\alpha)}{10C\log2}.
\]

Thus summing the literal-interval past-block density lower bounds only
over the cohort's logarithmic rank interval does not by itself reject
this profile either.

For example, theta=1/sqrt(2) gives b=1/20 and the exact leading values

\[
 \begin{array}{c|c}
 M/D&1/20\\
 W/D&1/40\\
 T/D^2=\Phi/D^2&1/16000\\
 R/D^2=S^{00}/D^2&1/48000\\
 E/D^2&19/16000\\
 \mathcal C/D^2&29/24000.
 \end{array}
\tag{5}
\]

This is an interior exponent, not the theta=1 endpoint.

## 5. Fejer-weighted cohort positivity, including the cubic coefficient

The limiting physical bank measure is nu_theta=b(theta) dx on [0,1].
For alpha<beta, its symmetric triangularly weighted cohort transform is

\[
 2\int_0^1(1-x)\cos(2\pi\xi x)\,
              d(\nu_\beta-\nu_\alpha)(x)
 =[b(\beta)-b(\alpha)]
       \left(\frac{\sin(\pi\xi)}{\pi\xi}\right)^2\ge0.
\tag{6}
\]

The value at xi=0 is the continuous extension. Thus every continuum
cohort obeys the positivity constraint of the parent's rank-cut lemma.

For the weighted Schur count, independence away from O(D) diagonals and
a Riemann sum give

\[
 \frac{T_w}{D^2}\longrightarrow b^3
 \int_{x,y>0\atop x+y<1}(1-x)(1-y)(1-x-y)\,dx\,dy
 =\frac{11}{120}b^3.
\tag{7}
\]

For an explicit evaluation, substitute z=x+y. The inner integral is
z-z^2+z^3/6; multiplying by 1-z and integrating from 0 to 1 gives
11/120. This is consistent with the cubic identity integral h^3=6T_w
and with the lower bound T_w>=W^3/(36D)-pD/3: the leading lower
coefficient there is b^3/288, smaller than 11b^3/120.

For completeness the finite model can also obey the requisite order of
Fourier error for a fixed finite cohort partition. For one fixed mark
interval of length q, its weighted polynomial has expectation

\[
 q\bigl(\mathcal F_D(t)-1\bigr)\ge-q,
\]

where F_D is the nonnegative Fejer kernel. At each fixed t its centered
part is a sum of D independent bounded terms, so its tail at size L is
at most 2 exp(-cL^2/D). Its deterministic derivative is O(D^2).
A polynomial-size grid and this derivative bound imply, for any fixed
epsilon>0, a uniform fluctuation of at most D^(1/2+epsilon) with
probability tending to one. Choose epsilon<theta_0-1/2 and take a union
over a fixed finite partition. Each cohort then has negative part o(D^theta_0).
This observation concerns the Fourier inequality only; it is not an
endpoint Gram representation of the model.

## 6. The constraints not supplied by this relaxation

The labels have been assigned birth marks directly. No increasing integer
sequence has been produced whose short differences have these births.
In particular, packing the mark births into actual endpoint ranks n<=D^theta
would create multi-label batches. The actual requirement that every pair
of labels in such a batch has its difference in the old bank is not proved
for this model. Single-label mark births do not resolve that requirement.

Nor has this construction made the physical birth rank of one label agree
between different choices of D. The model is specified and checked at
one width, with a continuum of thresholds. It is not an all-width joint
realization or an infinite fixed-onset cap construction.

Equations (2)--(7) therefore show a precise limitation: the current leading
flux identities, historical half-mask saving, scalar density lower bounds,
and Fejer cohort positivity are mutually consistent with a nonzero explicit
profile. A contradiction requires an additional constraint retaining the
endpoint batches or their compatibility across physical widths. This note
does not exclude such a constraint and does not resolve Q1.

Subsequent extension: [coherent_birth_field.md](coherent_birth_field.md)
assigns a single integer birth rank tau(d)=ceil(d^beta_d) to each physical
label and verifies the same leading coefficients jointly across widths,
including a separate estimate for integer birth ties. That abstract
extension removes the independent-width limitation, but proves that its
total label count is o(p^2), so it still cannot be an actual Sidon
difference history. Endpoint incidence remains unfulfilled as well.
