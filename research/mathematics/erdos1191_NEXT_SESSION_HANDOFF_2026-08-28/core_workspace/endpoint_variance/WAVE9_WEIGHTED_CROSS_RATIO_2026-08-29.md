# Wave 9: weighted cross-ratio telescope for genuine birth gaps

**Date:** 2026-08-29 (Asia/Tokyo)  
**Scope:** a logarithmic potential for the genuine nonadjacent part of P15  
**Status:** exact finite identities, a sharp unconditional bound, a valid
cross-epoch potential, and a rigorous local no-go; P15 remains open

## 1. Outcome

For two nonadjacent genuine gap indices `i<j`, write

\[
 a=h_i,\qquad b=h_j,\qquad
 M=D_{i+1,j-1},\qquad D=D_{i,j}=M+a+b,
\tag{1}
\]

and introduce the positive cross-ratio defect

\[
 C_{ij}=\log\frac{(M+a)(M+b)}{M(M+a+b)}.
\tag{2}
\]

This note proves the following.

1. `C_(ij)` is the negative mixed discrete derivative of `log D_(p,q)`.
   The full weighted triangular sum with weight `((j-i)/n)^2` has an exact
   Abel formula.  All interior coefficients are negative; the only positive
   coefficients are prefix and suffix boundary increments.
2. If `h_n^circ=min(h_2,...,h_(n-2))` is the smallest strict-interior genuine
   gap and `g=n-1`, then the sharp estimate for arbitrary positive gap vectors
   is

   \[
   0\leq\sum_{1\leq i<j\leq g\atop j-i\geq2}
   \left(\frac{j-i}{n}\right)^2 C_{ij}
   \leq
   \left(\frac{n-2}{n}\right)^2
   \log\frac{D_{1,g}}{h_n^\circ}.
   \tag{3}
   \]

   Its logarithmic order and leading coefficient are asymptotically sharp
   even on four-mark Golomb rulers.  For an integer Golomb ruler, however,
   the negative strict-interior terms and rearrangement give the stronger
   exact factorial bound

   \[
   S_n\leq \left(\frac{n-2}{n}\right)^2
   \log\frac{D_{1,g}}{\delta_n^\circ}
   -\frac{2\log((n-3)!)+\log((K-n+4)!)+\log(K!)}{n^2},
   \quad K=\binom{n-2}{2},\quad
   \delta_n^\circ=\gcd(h_2,\ldots,h_{n-2}).
   \tag{3a}
   \]

   Under a critical diameter cap this is `O_C(log log n)`, rather than
   `O_C(log n)`.
3. The original endpoint product satisfies

   \[
   \frac{h_ih_j}{D_{i,j}^2}\leq C_{ij}.
   \tag{4}
   \]

   Therefore retaining `(D_(i,j)/N_n)^2` gives a valid positive majorant for
   every genuine nonadjacent birth atom.
4. That retained potential has an exact cross-epoch recursion.  Unfortunately
   the birth sum is between `3/4` and `1` times the sum of the full state
   potentials, so the recursion gives no cancellation or little-`o` gain.
5. Scaled Erdős--Turán rulers obey one fixed recent-prefix critical envelope
   and have vanishing numerical difference density, yet their retained
   terminal cross-ratio birth potential is at least `1/4096`.  Thus neither
   retaining `(D/N)^2` nor dyadic birth partitioning yields a local vanishing
   estimate.  A theorem conditioned on one fixed infinite branch is still
   required.

All displayed exact identities and inequalities are `[RIGOROUS]` and proved
below.  Two classical inputs are named explicitly: Stirling's factorial
estimate in (19e), and Bertrand's postulate for choosing a prime in every
interval `[L,2L)`.  The decimal evaluations in Section 8 are
`[COMPUTATIONAL — EXPERIMENTAL]` and are not used in an infinite inference.

## 2. Cross ratio as a mixed logarithmic derivative

Let an `n`-mark prefix have genuine gaps `h_1,...,h_g`, where `g=n-1`, and
put

\[
 D_{p,q}=\sum_{k=p}^q h_k=a_q-a_{p-1}
 \qquad(1\leq p\leq q\leq g).
\tag{5}
\]

For `j-i>=2`, the interior mass `M=D_(i+1,j-1)` is positive.  Directly from
(1),

\[
 \boxed{
 C_{ij}
 =\log D_{i,j-1}+\log D_{i+1,j}
 -\log D_{i+1,j-1}-\log D_{i,j}.}
\tag{6}
\]

Moreover,

\[
 (M+a)(M+b)-M(M+a+b)=ab>0,
\]

so `C_(ij)>0`.

### Lemma 1 (product comparison, optimal constant one)

For every `a,b,M>0`, with `D=M+a+b`,

\[
 \boxed{
 \frac{ab}{D^2}
 \leq
 \log\frac{(M+a)(M+b)}{MD}
 \leq\frac{ab}{MD}.}
\tag{7}
\]

#### Proof

Set `x=ab/(MD)`.  Then the cross ratio is `log(1+x)`.  The elementary bounds

\[
 \frac{x}{1+x}\leq\log(1+x)\leq x
\]

give the right inequality and

\[
 \log(1+x)\geq\frac{ab}{(M+a)(M+b)}.
\]

Since `(M+a)(M+b)<=D^2`, the left inequality follows.  When `M` dominates
`a+b`, the ratio of the middle term to `ab/D^2` tends to one, so the constant
cannot be improved.  `square`

## 3. Exact full-prefix Abel formula

Define

\[
 S_n=\sum_{1\leq i<j\leq g\atop j-i\geq2}
 \left(\frac{j-i}{n}\right)^2 C_{ij}.
\tag{8}
\]

For integer `r>=0`, put

\[
 v_0=v_1=0,
 \qquad v_r=\frac{r^2}{n^2}\quad(r\geq2).
\tag{9}
\]

### Theorem 2 (all boundary coefficients)

The following identity is exact:

\[
 \boxed{
 \begin{aligned}
 S_n={}&
 \sum_{\ell=1}^{g-1}(v_\ell-v_{\ell-1})
 \bigl(\log D_{1,\ell}+\log D_{g-\ell+1,g}\bigr)\\
 &-v_{g-1}\log D_{1,g}\\
 &+\sum_{2\leq p\leq q\leq g-1}
 \bigl(2v_\ell-v_{\ell-1}-v_{\ell+1}\bigr)
 \log D_{p,q},
 \qquad \ell=q-p+1.
 \end{aligned}}
\tag{10}
\]

The two first-line sums are respectively every proper prefix and proper
suffix.  The second line is the full span.  The last line contains every
strictly interior interval, including the one-gap intervals.

The coefficients are

\[
 v_\ell-v_{\ell-1}=
 \begin{cases}
 0,&\ell=1,\\
 4/n^2,&\ell=2,\\
 (2\ell-1)/n^2,&\ell\geq3,
 \end{cases}
\tag{11}
\]

and

\[
 2v_\ell-v_{\ell-1}-v_{\ell+1}=
 \begin{cases}
 -4/n^2,&\ell=1,\\
 -1/n^2,&\ell=2,\\
 -2/n^2,&\ell\geq3.
 \end{cases}
\tag{12}
\]

Thus every interior coefficient is strictly negative, and every nonzero
proper-prefix or proper-suffix coefficient is positive.

#### Proof

Expand every `C_(ij)` using (6).  Fix an interval `[p,q]` of length
`ell=q-p+1`.  It can occur in four ways:

\[
 \begin{array}{c|c|c}
 \text{term in (6)}&\text{originating pair}&\text{coefficient}\\ \hline
 \log D_{i,j-1}&(i,j)=(p,q+1)&+v_\ell\\
 \log D_{i+1,j}&(i,j)=(p-1,q)&+v_\ell\\
 -\log D_{i+1,j-1}&(i,j)=(p-1,q+1)&-v_{\ell+1}\\
 -\log D_{i,j}&(i,j)=(p,q)&-v_{\ell-1}.
 \end{array}
\tag{13}
\]

For `1<p<=q<g`, all four allowed contributions give the last-line
coefficient in (10).  On `p=1` only the first and fourth remain, giving
`v_ell-v_(ell-1)`; on `q=g` only the second and fourth remain.  For the full
span only the fourth contribution survives.  The convention `v_0=v_1=0`
exactly records the exclusion of the undefined adjacent cross ratio.  This
proves (10).  Substitution of (9) gives (11)--(12).  `square`

The coefficient sum in (10) is zero, as it must be: scaling every gap by the
same positive factor leaves all cross ratios unchanged.

More precisely, after multiplication by `n^2`, the total positive
coefficient mass and the absolute total negative coefficient mass are both

\[
 2(n-2)^2.
\tag{12a}
\]

Indeed, the two boundary fans each telescope to `(n-2)^2`; the full span has
weight `(n-2)^2`, and equality of the two total masses then also follows from
scale invariance.  This is a useful checksum on every boundary convention.

## 4. Exact birth-shell coefficient formula

For later use it is helpful to record the lower shell boundary as well.  Let
`1<=m<=g`, and define

\[
 S_{n,m}^{\rm birth}
 =\sum_{j=m}^g\sum_{i=1}^{j-2}
 \left(\frac{j-i}{n}\right)^2 C_{ij}.
\tag{14}
\]

Let `w_r=r^2/n^2`.  For an interval `[p,q]`, `ell=q-p+1`, define

\[
 \begin{aligned}
 c_{p,q}^{(m,g)}={}&
 \mathbf1_{\{\ell\geq2,\ m-1\leq q\leq g-1\}}w_\ell\\
 &+\mathbf1_{\{p\geq2,\ \ell\geq2,\ m\leq q\leq g\}}w_\ell\\
 &-\mathbf1_{\{p\geq2,\ m-1\leq q\leq g-1\}}w_{\ell+1}\\
 &-\mathbf1_{\{\ell\geq3,\ m\leq q\leq g\}}w_{\ell-1}.
 \end{aligned}
\tag{15}
\]

### Theorem 3 (birth-shell Abel identity)

Including every lower-shell, upper-shell, left, and right boundary term,

\[
 \boxed{
 S_{n,m}^{\rm birth}
 =\sum_{1\leq p\leq q\leq g}
 c_{p,q}^{(m,g)}\log D_{p,q}.}
\tag{16}
\]

#### Proof

Use the four origins in (13), now requiring the originating right endpoint
`j` to lie in `[m,g]`.

- The first origin has `j=q+1`, giving
  `ell>=2` and `m-1<=q<=g-1`.
- The second has `j=q` and `i=p-1`, giving
  `p>=2`, `ell>=2`, and `m<=q<=g`.
- The third has `j=q+1` and `i=p-1`, giving
  `p>=2` and `m-1<=q<=g-1`.
- The fourth has `j=q` and rank distance `ell-1`, giving
  `ell>=3` and `m<=q<=g`.

These are exactly the four indicators in (15).  `square`

Unlike the full-prefix formula, (16) has a genuine lower-shell boundary and
does not have a uniform all-interior sign pattern.  Since every `C_(ij)` is
positive, the safe upper comparison is simply

\[
 0\leq S_{n,m}^{\rm birth}\leq S_n.
\tag{17}
\]

For the dyadic shell itself there is also a simpler state identity.  Set
`Y_m=S_(2m,m)^birth` and write `Sigma_k=S_(2^k)`, with the empty states taken
as zero.  Old pairs keep their cross ratios and acquire exactly one quarter
of their old rank weight.  Therefore

\[
 \boxed{Y_m=S_{2m}-\frac14S_m,\qquad
 \sum_{k=0}^JY_{2^k}
 =\Sigma_{J+1}+\frac34\sum_{k=1}^J\Sigma_k.}
\tag{17a}
\]

Thus even the unretained cross-ratio shell reconstructs a positive sum of
state potentials; it does not telescope to one terminal state.

## 5. Best unconditional upper bounds

Let

\[
 h_n^\circ:=\min_{2\leq k\leq n-2}h_k,
 \qquad D_*:=D_{1,g}=a_{n-1}.
\tag{18}
\]

### Theorem 4 (sharp scale-invariant logarithmic bound)

For every positive genuine gap vector with `n>=4`,

\[
 \boxed{
 0\leq S_n\leq
 v_{g-1}\log\frac{D_*}{h_n^\circ}
 =\left(\frac{n-2}{n}\right)^2
 \log\frac{a_{n-1}}{h_n^\circ}.}
\tag{19}
\]

At `n=4`, the logarithmic order and the displayed coefficient are
asymptotically sharp.  Hence no smaller universal multiplicative constant
works simultaneously for all `n`, even after restricting to Golomb rulers.

#### Proof

Replace every `log D_(p,q)` in (10) by
`log(D_(p,q)/h_n^circ)`.  The identity is unchanged because its total
coefficient is zero.  Every strict-interior interval contains at least one of
`h_2,...,h_(n-2)`, so its normalized logarithm is nonnegative.  By (12), the
complete interior sum can only decrease the right side and may be discarded
for an upper bound.  A boundary interval need not exceed `h_n^circ`, but that
is irrelevant: it is always at most `D_*`, which is the upper estimate used
next.

Each proper prefix and suffix is at most `D_*`, and the sum of its positive
coefficients on either side telescopes to

\[
 \sum_{\ell=1}^{g-1}(v_\ell-v_{\ell-1})=v_{g-1}.
\]

The two sides therefore cost at most
`2v_(g-1) log(D_*/h_n^circ)`.  Retaining the negative full-span term subtracts
exactly one copy, proving (19).

For sharpness take the four-mark ruler with genuine gaps

\[
 (h_1,h_2,h_3)=(H,1,2H),\qquad H\geq2.
\tag{20}
\]

Its six positive differences are

\[
 1,H,H+1,2H,2H+1,3H+1,
\]

so it is Golomb.  There is one nonadjacent gap pair and

\[
 S_4=\frac14\log\frac{(H+1)(2H+1)}{3H+1},
 \qquad
 v_2\log\frac{D_*}{h_4^\circ}=\frac14\log(3H+1).
\tag{21}
\]

The ratio of these quantities tends to one as `H->infinity`.  `square`

In particular, no bound depending only on `n` can control `S_n`.  Under a
critical cap `N_n<=Cn^2 log(2n)`, (19) gives only `S_n=O_C(log n)` if one
does not use difference uniqueness.

### Theorem 4b (exact Golomb spectrum bound)

Suppose now that the marks form an integer Golomb ruler.  Put

\[
 K=\binom{n-2}{2},\qquad A=n-3,\qquad B=n-4,
 \qquad R=K-B=K-n+4,
 \qquad \delta_n^\circ=\gcd(h_2,\ldots,h_{n-2}),
 \qquad q_n=\frac{h_n^\circ}{\delta_n^\circ}\in\mathbb N.
\tag{19a}
\]

For `q,t` positive integers, write
`(q)_(overline t)=q(q+1)...(q+t-1)`, and define

\[
 \Phi_n(q)=
 2\log\frac{(q)_{\overline A}}{q^A}
 +\log\frac{(q)_{\overline R}}{q^R}
 +\log\frac{(q)_{\overline K}}{q^K}.
\tag{19a'}
\]

Then the strongest spectrum-and-lattice bound obtained here is

\[
 \boxed{
 S_n\leq
 \left(\frac{n-2}{n}\right)^2\log\frac{D_*}{h_n^\circ}
 -\frac{\Phi_n(q_n)}{n^2}.}
\tag{19b}
\]

A convenient weaker corollary, independent of `h_n^circ/delta_n^circ`, is

\[
 \boxed{
 S_n\leq
 \left(\frac{n-2}{n}\right)^2\log\frac{D_*}{\delta_n^\circ}
 -\frac{2\log(A!)+\log(R!)+\log(K!)}{n^2}.}
\tag{19c}
\]

Bound (19b) is the strongest estimate obtainable from only the exact
coefficient multiset, the lattice spacing `delta_n^circ`, the minimum
`h_n^circ`, and distinctness of the `K` interior differences.  It is not a
claim that the abstract rearrangement minimizer is realizable by interval
sums.

#### Proof

Subtract `log(h_n^circ)` from every logarithm in (10).  The total coefficient
is zero, so `S_n` is unchanged.  The strict-interior intervals are `[p,q]`
with `2<=p<=q<=g-1`; they are the `K` differences between the `n-2` internal
marks.  Their quotients by `delta_n^circ` are distinct integers, and their
smallest possible value is
`h_n^circ/delta_n^circ=q_n`, because every multi-gap interval is larger than
each of its positive constituent gaps.

After ordering these integer quotients increasingly as `z_0,...,z_(K-1)`, one
has `z_r>=q_n+r`.  By (12), `A` logarithms have weight four, `B` have weight
one, and the other `K-A-B` have weight two.  The minimizing assignment gives
weight four to ranks `0,...,A-1`, weight two to ranks `A,...,R-1`, and weight
one to ranks `R,...,K-1`.  Indeed, if `x<y` are assigned weights `u<v`,
swapping them changes the sum by `(v-u)(log x-log y)<0`; and replacing a
selected integer by a missing smaller admissible integer also decreases it.
Thus the absolute strict-interior logarithmic contribution is at least
`Phi_n(q_n)`.

As in Theorem 4, the two positive boundary fans minus the negative full span
cost at most `((n-2)/n)^2 log(D_*/h_n^circ)`.  This proves (19b).  Repeating
the same argument after normalization by `delta_n^circ`, and using only the
integer lower ranks `1,...,K`, gives (19c), since

\[
 4\log(A!)+2\log\frac{R!}{A!}+\log\frac{K!}{R!}
 =2\log(A!)+\log(R!)+\log(K!).
\tag{19d}
\]

Moreover, (19b) really dominates (19c).  For every rank `r>=0`,

\[
 \log\frac{1+r}{1+r/q_n}\leq\log q_n,
\]

and the total strict-interior weight is
`2A+R+K=(n-2)^2`.  Comparing the two right sides term by term proves the
claim.  `square`

The standard form `log(t!)=t log t-t+O(log(t+1))`, applied to
`A=n-3`, `K=(n-2)(n-3)/2`, and `R=K-n+4`, gives

\[
 \frac{2\log(A!)+\log(R!)+\log(K!)}{n^2}
 =2\log n-1-\log2+o(1).
\tag{19d'}
\]

If `log(D_*/delta_n^circ)=o(n)`, the prefactor
`((n-2)/n)^2` changes its logarithm by `o(1)`.  Hence the convenient
corollary (19c) becomes

\[
 \log\frac{D_*}{\delta_n^\circ n^2}+1+\log2+o(1).
\tag{19e}
\]

In particular, `D_*<N_n<=C n^2 log(2n)` and `delta_n^circ>=1` give

\[
 S_n\leq \log\!\bigl(C\log(2n)\bigr)+1+\log2+o_C(1)
 =O_C(\log\log n).
\tag{19f}
\]

This is a genuine improvement, but summing it over `n=2^k`, `k<=J`, still
costs `O_C(J log(J+2))`, far above `o(log J)`.

On one fixed infinite integer branch, `delta_(n+1)^circ` divides
`delta_n^circ`, because the former gcd merely adds the next internal gap.
Therefore this positive-integer gcd sequence eventually stabilizes.  The gcd
normalization correctly removes artificial common rescaling (including the
scale `s` in Section 8), but it cannot by itself create a decaying
cross-epoch factor.

## 6. Retaining the exact `(D/N)^2` factor

At one update `m -> n=2m`, define the retained genuine nonadjacent birth
potential

\[
 X_m=\sum_{j=m}^{n-1}\sum_{i=1}^{j-2}
 \left(\frac{j-i}{n}\right)^2
 \left(\frac{D_{i,j}}{N_n}\right)^2 C_{ij}.
\tag{22}
\]

The corresponding full state potential is

\[
 P_n=\sum_{1\leq i<j\leq n-1\atop j-i\geq2}
 \left(\frac{j-i}{n}\right)^2
 \left(\frac{D_{i,j}}{N_n}\right)^2 C_{ij}.
\tag{23}
\]

Let `B_m^na` be the part of the Wave 8 one-epoch birth budget with
`i>=1` and `j-i>=2`.

### Theorem 5 (valid cross-ratio majorant)

For every update,

\[
 \boxed{
 \mathcal B_m^{\rm na}\leq\frac{36}{35}X_m.}
\tag{24}
\]

The omitted genuine adjacent-rank part has total dyadic sum at most `6/35`.
The artificial `i=0` row has the independent Wave 8 bound `92/315`.

#### Proof

For each nonadjacent genuine pair, Lemma 1 gives

\[
 \frac{h_ih_j}{N_n^2}
 =\left(\frac{D_{i,j}}{N_n}\right)^2
 \frac{h_ih_j}{D_{i,j}^2}
 \leq\left(\frac{D_{i,j}}{N_n}\right)^2C_{ij}.
\]

The fixed `H` kernel is at most
`(36/35)((j-i)/n)^2` on every birth pair, proving (24).

For a genuine adjacent pair, the rank factor is `1/n^2`.  The sum of its
endpoint products is at most the sum over all unordered gap pairs, hence at
most `N_n^2/2`.  Its epoch cost is therefore at most `18/(35n^2)`.  For
`n=2^(k+1)`,

\[
 \sum_{k\geq0}\frac{18}{35\,2^{2k+2}}=\frac6{35}.
\]

The `i=0` assertion is the previously proved Wave 8 artificial-row theorem.
`square`

Thus a proof of `sum_m X_m=o(log J)` would close P15.  The next section shows
that the exact cross-epoch algebra does not supply such a bound.

## 7. Exact cross-epoch recursion and no cancellation

Let

\[
 \rho_m=\frac{N_m}{N_{2m}}.
\tag{25}
\]

### Theorem 6 (retained-potential recursion)

For every positive gap vector,

\[
 \boxed{
 X_m=P_{2m}-\frac{\rho_m^2}{4}P_m.}
\tag{26}
\]

Consequently, writing `Pi_k=P_(2^k)` and
`rho_k=N_(2^k)/N_(2^(k+1))`,

\[
 \boxed{
 \sum_{k=0}^JX_{2^k}
 =\Pi_{J+1}+\sum_{k=1}^J
 \left(1-\frac{\rho_k^2}{4}\right)\Pi_k,}
\tag{27}
\]

and therefore

\[
 \boxed{
 \frac34\sum_{k=1}^{J+1}\Pi_k
 \leq\sum_{k=0}^JX_{2^k}
 \leq\sum_{k=1}^{J+1}\Pi_k.}
\tag{28}
\]

#### Proof

Split `P_(2m)` according to whether the right gap index is below `m` or at
least `m`.  The latter part is exactly `X_m`.  For an old pair, `D_(i,j)` and
`C_(ij)` are unchanged, while

\[
 \left(\frac{j-i}{2m}\right)^2
 \left(\frac{D_{i,j}}{N_{2m}}\right)^2
 =\frac14\rho_m^2
 \left(\frac{j-i}{m}\right)^2
 \left(\frac{D_{i,j}}{N_m}\right)^2.
\]

This proves (26).  Summing it over dyadic epochs gives (27); only
`Pi_0=P_1=0` is needed for the initial boundary (in fact `Pi_1=P_2=0` as
well).  The four-mark state `Pi_2=P_4` need not vanish.  Finally
`0<rho_k<1` gives (28).  `square`

This is a genuine cross-epoch potential, but it is a no-go for telescoping:
the birth sum is comparable to the **sum** of all positive state potentials,
not to one terminal boundary.  Old-pair aging can save at most a constant
factor, exactly as in the Wave 8 pair telescope and the Wave 9 rank-variance
reduction.

The obstruction persists for scalar epoch reweightings.  For arbitrary
nonnegative weights `w_0,...,w_J`, (26) gives the exact identity

\[
 \sum_{k=0}^Jw_kX_{2^k}
 =w_J\Pi_{J+1}+
  \sum_{k=1}^J\left(w_{k-1}-\frac{\rho_k^2}{4}w_k\right)\Pi_k.
\tag{28a}
\]

To cancel every internal state coefficient one must have

\[
 \frac{w_k}{w_{k-1}}=\frac4{\rho_k^2}>4,
 \qquad\text{hence}\qquad \frac{w_J}{w_0}>4^J.
\tag{28b}
\]

Thus an exact scalar-weight telescope exists only with exponentially
distorted epoch weights.  Such weights are not uniformly comparable to the
unweighted birth sum required by P15.  This is a rigorous no-go only for
scalar reweightings of `P_(2^k)`; it does not rule out a new potential with
additional branch-dependent state.

Combining (19c), (23), and (28) gives only

\[
 \sum_{k\leq J}X_{2^k}=O_C(J\log(J+2))
\tag{29}
\]

under the critical cap.  Difference uniqueness has not yet entered this
bound, and the next obstruction shows that no local numerical-density repair
is possible.

## 8. Critical-scale local no-go, even with the retained factor

Let `L>=4` be a power of two, choose a prime `p` with `L<=p<2L`, and put

\[
 b_k=2pk+[k^2]_p\quad(0\leq k<L),
 \qquad A_{L,p,s}=\{sb_0,\ldots,sb_{L-1}\}.
\tag{30}
\]

These facts are short enough to recheck here.  If two differences of the
unscaled points are equal, the residue corrections have absolute value below
`p`, so the `2p`-separated rank-distance intervals force the same rank
distance `d`.  Reduction modulo `p` then gives `2d(i-k)=0 mod p`; since
`0<d<p`, the two left endpoints, and hence the two pairs, agree.  Thus the
ruler is Golomb, and scaling preserves it.  Also

\[
 b_k-b_{k-1}=2p+[k^2]_p-[(k-1)^2]_p\geq p+1,
\]

so every scaled genuine gap exceeds `sp`, while

\[
 N_L=sb_{L-1}+1\leq2spL.
\]

For `s=ceil(log L)` and `L/2<=k<=L`, one has `p<2L<=4k` and
`s<=2 log(2k)`.  Hence

\[
 N_k\leq2spk+1\leq8sk^2+1\leq17k^2\log(2k).
\]

Conversely `N_L>=2sL(L-1)`, so
`binom(L,2)/N_L<=1/(4s)->0`.

### Theorem 7 (retained cross ratio does not vanish locally)

At the terminal update `m=L/2`,

\[
 \boxed{X_{L/2}(A_{L,p,s})\geq\frac1{4096}.}
\tag{31}
\]

#### Proof

Use the `L^2/16` pairs

\[
 1\leq i\leq L/4,
 \qquad3L/4\leq j\leq L-1.
\]

They have rank weight at least `1/4`.  Their interval contains at least
`L/2` genuine gaps, so

\[
 \frac{D_{i,j}}{N_L}\geq\frac{spL/2}{2spL}=\frac14.
\]

Also `h_i,h_j>=sp` and `D_(i,j)<=N_L<=2spL`; Lemma 1 gives

\[
 C_{ij}\geq\frac{h_ih_j}{D_{i,j}^2}\geq\frac1{4L^2}.
\]

Thus every selected term of (22) is at least
`(1/4)(1/16)(1/(4L^2))=1/(256L^2)`.  Summing `L^2/16` terms proves (31).
`square`

The rank factor and cross ratio are exactly scale-invariant.  Because
`N_L=s b_(L-1)+1`, the retained `D/N_L` factor is not exactly invariant, but
the proof above bounds it uniformly below by `1/4`, independently of `s`.
Meanwhile increasing `s` makes the integer-difference occupancy tend to
zero.  Therefore no theorem of the form

\[
 X_m\leq F\!\left(\frac{|\Delta(A_{2m})|}{N_{2m}}\right),
 \qquad F(t)\longrightarrow0,
\tag{32}
\]

can hold locally, even under one fixed recent-prefix critical constant.  The
family changes with `L` and is not one infinite compatible branch, so it does
not refute the survival-conditioned P15 target.

Exact floating evaluations, used only as a sanity check, give

| `L` | unretained terminal cross ratio | retained `X_(L/2)` |
|---:|---:|---:|
| 16 | `0.3007408795...` | `0.0875158643...` |
| 32 | `0.3546188304...` | `0.0860760349...` |
| 64 | `0.3591489094...` | `0.0808779747...` |
| 128 | `0.3669383950...` | `0.0794542125...` |
| 256 | `0.3705198475...` | `0.0787281481...` |
| 512 | `0.3728132057...` | `0.0784487954...` |

These decimals are not theorem evidence; (31) is the rigorous bound.

## 9. Disposition and next lemma

The cross ratio produces a real and exact arithmetic potential:

\[
 \mathcal B_m^{\rm na}\leq\frac{36}{35}X_m,
 \qquad
 X_m=P_{2m}-\frac{\rho_m^2}{4}P_m.
\]

It nevertheless fails in both available summation modes.

- Dropping `(D/N)^2` gives the sharp arbitrary-gap bound (19), improved by
  Golomb uniqueness to the spectrum bounds (19b)--(19c), but still only
  `O_C(log log n)` per critical state.
- Retaining `(D/N)^2` preserves a constant terminal cost on critical scaled
  Erdős--Turán windows.
- Summing dyadic epochs reconstructs a positive sum of state potentials by
  (17a) and (27)--(28); it does not telescope to a bounded terminal term.

The only surviving use is therefore survival-conditioned: on one fixed
infinite eventually critical Golomb branch, prove

\[
 \sum_{k\leq J}P_{2^k}=o(\log J),
\tag{33}
\]

or prove a strictly smaller global potential which still majorizes the exact
endpoint products.  By (28), (33) is quantitatively equivalent to the needed
cross-ratio birth estimate.  Theorem 7 shows that its proof must use
unbounded compatibility of the same branch, not local difference density,
finite critical windows, or scale invariance.

No such survival-conditioned estimate is proved here.  P15 and Erdős
Problem #1191 remain unresolved.

## 10. Independent executable audit

The coefficient algebra and inequalities were independently encoded in
`core_workspace/endpoint_variance/wave9_cross_ratio_telescope.py` and tested
in `core_workspace/endpoint_variance/test_wave9_cross_ratio_telescope.py`.
The direct four-term coefficient enumerator and the closed formula agree
exactly for every `4<=n<=64`; both coefficient sign masses equal
`2(n-2)^2`.  The numerical layer separately checks the cross-ratio identity,
the product lower bound, the weaker integer corollary of (19) obtained from
`h_n^circ>=1`, and (19c) on a four-mark ruler, an irregular vector, and an
authenticated 64-mark Golomb fixture.  It also checks that
both `S_n` and the primitive bound (19c) are unchanged after multiplying
every mark by `17`.

On 2026-08-29, the combined command covering these seven tests and the eight
independent rank-variance tests returned `15 passed in 0.34s`.  The final Ruff
rerun reported only `I001` import-order findings in the two independently
owned test files; it reported no analytic or runtime failure, and this note
did not edit those files.  These are finite verification results; the
displayed proofs, not the tests, establish the general identities.

Additional one-off finite checks compared the direct four-origin shell map
with (15) for every `3<=n<=100` and every shell boundary `m`, tested (26) on
700 deterministic-seed random positive-gap fixtures, and verified the sharp
shifted spectrum bound (19b) on 1,302 exhaustively generated small Golomb
fixtures.  All focused mathematical checks passed.
