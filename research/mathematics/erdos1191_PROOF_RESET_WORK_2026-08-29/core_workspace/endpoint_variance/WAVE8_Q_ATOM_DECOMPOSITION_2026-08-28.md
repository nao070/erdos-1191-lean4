# Wave 8: exact atom decomposition of the actual covariance innovation

**Date:** 2026-08-28  
**Status:** proved finite identities, a universal non-adjacent-difference
upper envelope with a summable boundary error, an exact within-shell debt
repayment inequality, a critical-density summability theorem for all
adjacent `kappa`-debt, and two finite Golomb no-go examples.  The
infinite-survival-conditioned `o(log J)` atom budget is still open, so this
does not resolve Erdős Problem #1191.

## 1. Purpose and scope

P13 asks for a quantitative link between the complete Wave 7 birth families
and both nonnegative parts of the actual innovation

\[
 Q_m
 =G\operatorname {Cov}_{\sigma_m}z
 +\frac{N_mG}{N_{2m}}d_md_m^{\mathsf T}.
\tag{1}
\]

This note supplies that link at the level of exact difference atoms.  There
are three complementary forms.

1. The newborn covariance has an exact signed expansion in squares of
   contiguous differences.  Every bulk coefficient is positive; the only
   negative coefficients are two boundary fans.  Positivity of covariance
   therefore proves an exact boundary-debt repayment inequality.
2. The rank-one term has both an exact signed old--new pair expansion and an
   exact Abel expansion supported on boundary fans.
3. After one controlled AM--GM loss, the complete adjoint charge
   `\<H,Q_m/N_(2m)\>` is bounded above by a positive sum over globally unique
   **non-adjacent** Golomb differences, plus a boundary-row error whose sum
   over every dyadic history is at most `92/315`.
4. The actual-adjacent renewal interfaces with only the two endpoint terms of
   the signed boundary fan.  Those adjacent terms are nevertheless globally
   summable under the critical cap; the unresolved shell debt is purely
   non-adjacent.

The third form is a genuine universal inequality.  What is not proved is
that its two positive atom sums are `o(log J)` on the subtree
`surv_C=infinity`.  The Wave 7 inverse-threshold potential does not by itself
give that square-moment estimate.  Thus the result is a reduction of P13,
not its completion.

All statements through Section 8 are finite and unconditional except where a
Golomb hypothesis is explicitly invoked for numerical distinctness.  No
finite extension calculation is used to infer infinite survival.

## 2. Common-grid notation

Put

\[
 L=2m,\qquad
 h_0=1,\qquad h_k=a_k-a_{k-1}\quad(1\leq k<L),
\tag{2}
\]

and split the gap indices into

\[
 O=\{0,\ldots,m-1\},\qquad S=\{m,\ldots,L-1\}.
\tag{3}
\]

Write

\[
 N=\sum_{i\in O}h_i=N_m,\qquad
 G=\sum_{j\in S}h_j=N_L-N_m,\qquad N'=N+G=N_L.
\tag{4}
\]

On the common `L`-grid set

\[
 x_k=z(k/L),\qquad z(u)=\binom{u(1-u)}u,
\tag{5}
\]

and define the old and newborn means

\[
 \bar x_O=\frac1N\sum_{i\in O}h_ix_i,
 \qquad
 \bar x_S=\frac1G\sum_{j\in S}h_jx_j,
 \qquad d=\bar x_O-\bar x_S.
\tag{6}
\]

Thus `bar x_O=B bar z_(nu_m)`, `bar x_S=bar z_(sigma_m)`, and `d=d_m`
in (1).  For `i<j` put

\[
 \Delta_{ij}=x_j-x_i,
 \qquad K_{ij}=\Delta_{ij}\Delta_{ij}^{\mathsf T}.
\tag{7}
\]

The fixed adjoint majorant is

\[
 H=\begin{pmatrix}16/15&8/105\\8/105&4/35\end{pmatrix},
 \qquad
 \Phi_{ij}:=\langle H,K_{ij}\rangle.
\tag{8}
\]

Direct substitution gives the useful exact kernel

\[
 \boxed{
 \Phi_{ij}=\frac{(j-i)^2}{L^2}
 P\!\left(1-\frac{i+j}{L}\right)},
 \qquad
 P(w)=\frac{16}{15}w^2+\frac{16}{105}w+\frac4{35}.
 }
\tag{9}
\]

Since `P` is convex and `P(1)=4/3`,

\[
 0\leq\Phi_{ij}\leq\frac43\frac{(j-i)^2}{L^2}.
\tag{10}
\]

## 3. Exact pair decompositions of both parts of `Q_m`

Let

\[
 \mathcal S_m=G\operatorname {Cov}_{\sigma_m}z,
 \qquad
 \mathcal R_m=\frac{NG}{N'}dd^{\mathsf T}.
\tag{11}
\]

The pairwise covariance formula gives, as a matrix identity,

\[
 \boxed{
 \mathcal S_m=\frac1G
 \sum_{\substack{r<s\\r,s\in S}}h_rh_sK_{rs}.}
\tag{12}
\]

The corresponding two-sample identity gives the rank-one part exactly:

\[
 \boxed{
 \begin{aligned}
 \mathcal R_m={}&\frac1{N'}
   \sum_{\substack{i\in O\\j\in S}}h_ih_jK_{ij}
 -\frac{G}{NN'}
   \sum_{\substack{i<j\\i,j\in O}}h_ih_jK_{ij}\\
 &-\frac{N}{GN'}
   \sum_{\substack{i<j\\i,j\in S}}h_ih_jK_{ij}.
 \end{aligned}}
\tag{13}
\]

Indeed, the first sum before division by `N'` is

\[
 NG\left(\operatorname {Cov}_O x+\operatorname {Cov}_S x
             +dd^{\mathsf T}\right),
\]

and the last two sums remove the two within-sample covariances.  Adding
(12) to (13) also yields the particularly short signed decomposition of the
actual innovation:

\[
 \boxed{
 Q_m=\frac1{N'}
 \sum_{\substack{i<j\\j\in S}}h_ih_jK_{ij}
 -\frac{G}{NN'}
 \sum_{\substack{i<j\\i,j\in O}}h_ih_jK_{ij}.}
\tag{14}
\]

Equations (12)--(14) are exact.  In particular, the rank-one mixture term is
not an unexplained extra PSD matrix: it is cross-block pair energy minus the
two within-block energies with their exact mass factors.

Taking the `H`-inner product in (13) and dropping the two nonnegative
subtractions gives the first universal inequality

\[
 \boxed{
 0\leq\langle H,\mathcal R_m\rangle
 \leq\frac1{N'}\sum_{i\in O,\ j\in S}h_ih_j\Phi_{ij}.}
\tag{15}
\]

## 4. Exact Abel boundary-fan form of the rank-one term

For `1<=t<m` and `1<=s<m`, define the left prefix and right suffix
atoms

\[
 P_t=\sum_{k=0}^{t-1}h_k=N_t,
 \qquad
 R_s=\sum_{k=m+s}^{L-1}h_k=N'-N_{m+s}.
\tag{16}
\]

Here `R_s=a_(L-1)-a_(m+s-1)` is a genuine Golomb difference.  The atom
`P_t=a_(t-1)-a_0+1` is the old boundary modulus; its harmless extra unit is
the convention `h_0=1`.

Discrete summation by parts in each block gives

\[
 \boxed{
 d=-\left[
 \sum_{t=1}^{m-1}\frac{P_t}{N}(x_t-x_{t-1})
 +(x_m-x_{m-1})
 +\sum_{s=1}^{m-1}\frac{R_s}{G}(x_{m+s}-x_{m+s-1})
 \right].}
\tag{17}
\]

Thus the mean-shift vector is an exact positive-coefficient boundary fan of
adjacent **rank** increments.  In particular, if

\[
 C_m=1+\sum_{t=1}^{m-1}\frac{P_t}{N}
       +\sum_{s=1}^{m-1}\frac{R_s}{G},
\tag{18}
\]

then the second coordinate of (17) is

\[
 d_1=-\frac{C_m}{L}.
\tag{19}
\]

There is no cancellation in this coordinate.  Indexing the two coordinates
by `0,1`, the Schur complement of the `00` entry of `H` is

\[
 H_{11}-\frac{H_{01}^2}{H_{00}}
 =\frac4{35}-\frac{(8/105)^2}{16/15}
 =\frac{16}{147}.
\tag{20}
\]

Consequently the rank-one adjoint charge has the rigorous lower bound

\[
 \boxed{
 \left\langle H,\frac{\mathcal R_m}{N'}\right\rangle
 \geq\frac{16NG}{147N'^2L^2}C_m^2
 \geq\frac{16NG}{147N'^2L^2}.}
\tag{21}
\]

The same fan also gives a useful adjacent-increment upper bound.  Weighted
Cauchy--Schwarz applied to (17) yields

\[
 \boxed{
 \begin{aligned}
 \left\langle H,\frac{\mathcal R_m}{N'}\right\rangle
 \leq\frac{NG}{N'^2}C_m\Bigg(&
 \sum_{t=1}^{m-1}\frac{P_t}{N}\Phi_{t-1,t}
 +\Phi_{m-1,m}\\
 &+\sum_{s=1}^{m-1}\frac{R_s}{G}
       \Phi_{m+s-1,m+s}\Bigg).
 \end{aligned}}
\tag{22}
\]

Equations (17), (21), and (22) separate the rank-one mean shift from the
newborn covariance.  Any future upper budget must control this fan as well;
newborn covariance alone cannot do so, as Section 8 shows.

## 5. A positive non-adjacent-difference upper envelope for the complete `Q_m`

For `1<=i<=j<L`, let

\[
 D_{i,j}=\sum_{k=i}^{j}h_k=a_j-a_{i-1}.
\tag{23}
\]

This is one actual positive Golomb difference.  For `i<j`, AM--GM gives

\[
 h_ih_j\leq\frac{(h_i+h_j)^2}{4}\leq\frac{D_{i,j}^2}{4}.
\tag{24}
\]

Combining (12), (15), and (24), while isolating the artificial row `i=0`,
proves

\[
 \left\langle H,\frac{\mathcal S_m}{N'}\right\rangle
 =\frac1{GN'}\sum_{m\leq r<s<L}h_rh_s\Phi_{rs},
 \qquad
 \left\langle H,\frac{\mathcal R_m}{N'}\right\rangle
 \leq\frac1{N'^2}\sum_{i\in O,\ j\in S}h_ih_j\Phi_{ij}.
\tag{24a}
\]

Thus the first coefficient below is exactly `1/(4GN')`: it is the
`1/(GN')` in the shell covariance from (24a), followed by the factor `1/4`
in (24).  The cross coefficient is analogously `1/(4N'^2)`.

\[
 \boxed{
 \begin{aligned}
 I_m:=\left\langle H,\frac{Q_m}{N'}\right\rangle
 \leq{}&\frac1{4GN'}
 \sum_{m\leq r<s<L}\Phi_{rs}D_{r,s}^2\\
 &+\frac1{4N'^2}
 \sum_{\substack{1\leq i<m\\m\leq j<L}}
       \Phi_{ij}D_{i,j}^2
 +\frac{23G}{105N'^2}.
 \end{aligned}}
\tag{25}
\]

For the last term, `|Delta f|<=1/4`, `|Delta u|<=1`, and the entries of `H`
give

\[
 \Phi_{0j}\leq\frac1{15}+\frac4{105}+\frac4{35}=\frac{23}{105},
\]

so

\[
 \frac1{N'^2}\sum_{j\in S}h_j\Phi_{0j}
 \leq\frac{23G}{105N'^2}.
\tag{26}
\]

Every difference charged in the two displayed sums of (25) is
non-adjacent.  More precisely:

- a shell atom `D_(r,s)` corresponds to the mark pair `(r-1,s)` and has
  rank lag `ell=s-r+1>=2`;
- a cross atom `D_(i,j)` corresponds to `(i-1,j)` and has rank lag
  `ell=j-i+1>=2` because `i<m<=j`.

The two sets are disjoint: the shell left endpoint is at least `m-1`, while
the cross left endpoint is at most `m-2`.  They are also globally disjoint
over all dyadic epochs, because their right endpoint lies in the epoch's
newborn block `[m,2m-1]`, and those blocks are disjoint.  Finally, on a
Golomb ruler distinct endpoint pairs give distinct numerical differences.
Thus (25) charges no positive difference twice anywhere in one dyadic
history.  These are exactly subsets of the complete Wave 7 birth partition.

Using (10), the fully explicit lag form is

\[
 \boxed{
 \begin{aligned}
 I_m\leq{}&\frac1{12m^2GN'}
 \sum_{m\leq r<s<L}(s-r+1)^2D_{r,s}^2\\
 &+\frac1{12m^2N'^2}
 \sum_{\substack{1\leq i<m\\m\leq j<L}}
       (j-i+1)^2D_{i,j}^2
 +\frac{23G}{105N'^2}.
 \end{aligned}}
\tag{27}
\]

Only the last term is currently known to be summable over every infinite
dyadic history.  Indeed, `G<=N'`, while the `L=2m` Golomb prefix has
`binom(L,2)` distinct positive integers below `N'`; hence

\[
 N'\geq\binom{2m}{2}+1\geq m^2.
\]

For `m=2^j`, therefore,

\[
 \boxed{
 \sum_{j\geq0}\frac{23G_{2^j}}{105N_{2^{j+1}}^2}
 \leq\frac{23}{105}\sum_{j\geq0}4^{-j}
 =\frac{92}{315}.}
\tag{28}
\]

The two atom sums in (27) are **not** proved summable or `o(log J)`.
Numerical uniqueness and the Wave 7 bound
`sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)` control inverse activation
thresholds, whereas (27) contains positive square moments `D^2`.  Replacing
`D` by its family upper threshold moves in the wrong direction.  This is the
precise remaining loss.

A stronger but potentially lossy sufficient version of P13 is now explicit:
on a single branch with `surv_C(A_(2m))=infinity`, prove that the sum through
epoch `J` of the first two right-hand terms of (27) is `o(log J)`.  Equation
(28) would then give the required adjoint innovation budget.  Nothing here
proves that proposed atom budget.

## 6. Exact signed square-atom expansion of the newborn covariance

The safe upper envelope (25) discards cancellation.  The exact cancellation
has a rigid and unexpectedly simple form.

For `m<=p<=q<L`, define the contiguous shell span

\[
 \mathcal D_{p,q}=\sum_{k=p}^{q}h_k=a_q-a_{p-1}.
\tag{29}
\]

Extend `Phi_(r,s)` by zero unless `m<=r<s<L`, and put

\[
 \kappa_{p,q}
 =\Phi_{p,q}-\Phi_{p-1,q}-\Phi_{p,q+1}+\Phi_{p-1,q+1}.
\tag{30}
\]

The elementary polarization

\[
 2h_rh_s
 =\mathcal D_{r,s}^2-\mathcal D_{r+1,s}^2
  -\mathcal D_{r,s-1}^2+\mathcal D_{r+1,s-1}^2
\tag{31}
\]

for `r<s` (with an empty span equal to zero) turns (12) into

\[
 \boxed{
 \langle H,\mathcal S_m\rangle
 =\frac1{2G}\sum_{m\leq p\leq q<L}
       \kappa_{p,q}\mathcal D_{p,q}^2.}
\tag{32}
\]

### Theorem 1 (complete sign classification)

For every `m>=2`, all coefficients in (32) are nonzero and

\[
 \boxed{
 \begin{array}{ll}
 \kappa_{p,q}<0
 &\Longleftrightarrow
 \bigl[p=m,\ q<L-1\bigr]
 \text{ or }
 \bigl[q=L-1,\ p>m\bigr],\\[2mm]
 \kappa_{p,q}>0
 &\Longleftrightarrow
 \bigl[m<p\leq q<L-1\bigr]
 \text{ or }(p,q)=(m,L-1).
 \end{array}}
\tag{33}
\]

Thus the negative atoms are precisely the proper left-prefix and
right-suffix fans of the newborn shell.  The positive atoms are the full
shell span and every strict bulk interval.

#### Proof

For an interior atom write `p=m+a`, `q=m+b`, where
`1<=a<=b<=m-2`.  Substitution of (9) into (30) gives

\[
 \kappa_{p,q}=\frac8{105L^4}F_m(a,b),
\tag{34}
\]

\[
 F_m(a,b)
 =28(2a-1)(2b+1)-8m(a+b)+12m^2.
\tag{35}
\]

For fixed `b`, this is affine in `a`, with slope
`8(14b+7-m)`.  If the slope is nonnegative, the minimum is at `a=1`.
When `m>=7`, the resulting affine expression in `b` is minimized at
`b=m-2` and equals

\[
 4m^2+64m-84>0,
\]

For `m<=7`, it is instead minimized at `b=1` and equals
`12m^2-16m+84>0`.  If the slope is negative, the minimum is at `a=b`, where

\[
 F_m(b,b)
 =112\left(b-\frac m{14}\right)^2+\frac{80}{7}m^2-28>0.
\]

Hence every bulk coefficient is positive.

On the left boundary, put `t=(q-m)/L`.  Then

\[
 \Phi_{m,q}=t^2P(-t),
\]

whose derivative is

\[
 \frac{8t}{105}(56t^2-6t+3)>0.
\]

Therefore
`kappa_(m,q)=Phi_(m,q)-Phi_(m,q+1)<0` for `q<L-1`.

For the right boundary, fix `y=(L-1)/L`, let `x=p/L`,
`d=y-x`, and `s=2x-1`.  Differentiating
`(y-x)^2P(1-x-y)` with respect to `x` shows that its negative derivative,
apart from a positive factor, is

\[
 E(s,d)=(112s-8)d+112s^2-16s+12.
\]

If `s>=1/14`, then `E>=112s^2-16s+12>0`.  If `s<1/14`, use
`d<=(1-s)/2` and the negative coefficient of `d` to get

\[
 E\geq56s^2+44s+8>0.
\]

Hence `Phi_(p,L-1)` strictly decreases with `p`, giving the second negative
fan.  Finally `kappa_(m,L-1)=Phi_(m,L-1)>0`.  This exhausts (33).
\(\square\)

### Corollary 2 (automatic boundary-debt repayment)

Let

\[
 \mathcal B^-=
 \{(m,q):m\leq q<L-1\}
 \cup\{(p,L-1):m<p<L\}
\tag{36}
\]

and let

\[
 \mathcal P=
 \{(p,q):m<p\leq q<L-1\}\cup\{(m,L-1)\}.
\tag{37}
\]

Since the left side of (32) is nonnegative,

\[
 \boxed{
 \sum_{(p,q)\in\mathcal B^-}
   (-\kappa_{p,q})\mathcal D_{p,q}^2
 \leq
 \sum_{(p,q)\in\mathcal P}
   \kappa_{p,q}\mathcal D_{p,q}^2.}
\tag{38}
\]

This is an unconditional, exact debt-repayment inequality.  It distinguishes
the atom types precisely:

- the negative adjacent atoms are the two endpoint gaps `h_m` and
  `h_(L-1)`;
- the positive adjacent atoms are the strict interior gaps
  `h_(m+1),...,h_(L-2)`;
- the negative non-adjacent atoms are the proper boundary prefixes and
  suffixes;
- the positive non-adjacent atoms are all strict bulk intervals together
  with the full-span atom `G=\mathcal D_{m,L-1}`.

Equation (38) is local to one shell.  It does not say that the right side has
a sublogarithmic sum across an infinite history.  Its value is that the
unpaid object is now an explicit pair of boundary fans and the only possible
repayment atoms are known exactly.

### 6.1 Exact interface with the actual-adjacent single-debt renewal

The separate Wave 8 actual-adjacent theorem uses

\[
 \tau_m=D_m^-+D_m^++\max(\mu_m^-,\mu_m^+),
 \qquad
 \delta_m=\max_{m+1\leq r<L}h_r,
\tag{38a}
\]

and the internal adjacent family
`I_m={h_(m+1),...,h_(L-1)}`.  Its single-debt conclusion and the boundary
debt in (38) are related, but they are **not the same debt**.

Put `U=L-1`.  The adjacent part of the negative side of (38) is exactly

\[
 \boxed{
 B_m^{\rm adj}=b_m^-h_m^2+b_m^+h_U^2,}
\tag{38b}
\]

where

\[
 b_m^-=-\kappa_{m,m}=\Phi_{m,m+1}
       =\frac1{L^2}P(-1/L),
 \qquad
 b_m^+=-\kappa_{U,U}=\Phi_{U-1,U}
       =\frac1{L^2}P(-1+3/L).
\tag{38c}
\]

The gap `h_m` is the first cross-boundary difference and always satisfies
`h_m<=tau_m`.  Of the gaps in `I_m`, only the last gap `h_U` is a negative
adjacent atom in (32); the gaps `h_(m+1),...,h_(U-1)` are positive bulk
assets.  Since `h_U<=delta_m` and `P(w)<=36/35` on `-1<=w<=0`,

\[
 \boxed{
 B_m^{\rm adj}
 \leq b_m^-\tau_m^2+b_m^+\delta_m^2
 \leq\frac{36}{35L^2}(\tau_m^2+\delta_m^2).}
\tag{38d}
\]

After the factors in the exact shell identity and the innovation
normalization are restored, this becomes

\[
 \boxed{
 \frac{B_m^{\rm adj}}{2GN'}
 \leq\frac{18}{35L^2GN'}(\tau_m^2+\delta_m^2).}
\tag{38e}
\]

### Corollary 3 (the adjacent `kappa`-debt is globally summable at critical density)

Suppose the terminal moduli at the dyadic updates satisfy

\[
 N'=N_{2m}\leq K(2m)^2\log(2m),
 \qquad m=2^j,\quad j\geq1.
\tag{38e.1}
\]

Then

\[
 \boxed{
 \sum_{j\geq1}\frac{B_{2^j}^{\rm adj}}
                         {2G_{2^j}N_{2^{j+1}}}
 \leq\frac{13}{5}K\log2.}
\tag{38e.2}
\]

#### Proof

Every discrepancy from its chord is bounded by the total mass on that
block, so

\[
 D_m^-\leq N,\qquad D_m^+\leq G,
 \qquad\max(\mu_m^-,\mu_m^+)\leq\frac{N'}m.
\]

Consequently, for `m>=2`,

\[
 \tau_m\leq\left(1+\frac1m\right)N'\leq\frac32N',
 \qquad \delta_m\leq G\leq N'.
\tag{38e.3}
\]

Equation (38e) therefore gives

\[
 \frac{B_m^{\rm adj}}{2GN'}
 \leq\frac{117}{280}\frac{N'}{m^2G}.
\tag{38e.4}
\]

The `m` shell gaps `h_m,...,h_(2m-1)` are distinct positive integers,
because they are distinct adjacent differences of a Golomb ruler.  Their sum
is `G`, so

\[
 G\geq1+2+\cdots+m=\frac{m(m+1)}2.
\tag{38e.5}
\]

Combining (38e.1), (38e.4), and (38e.5) yields

\[
 \frac{B_m^{\rm adj}}{2GN'}
 \leq\frac{117K}{35}\frac{\log(2m)}{m^2}.
\tag{38e.6}
\]

Finally,

\[
 \sum_{j\geq1}\frac{j+1}{4^j}=\frac79,
\]

so the sum of (38e.6) is

\[
 \frac{117K\log2}{35}\frac79=\frac{13}{5}K\log2.
\]

This proves (38e.2).  If the critical cap is only eventual, the same argument
proves summability of the tail; the finitely many earlier adjacent debts add
only a finite constant.  In the canonical notation `K=2C`, the displayed
bound is `(26/5)C log 2`. \(\square\)

The single-debt renewal can replace `delta_m` in (38d)--(38e) by a payment
cutoff `pi_m`: take `pi_m=tau_m` when `delta_m<=tau_m`, take the first later
ancestry-clearing `tau_n` when it exists, and take `pi_m=delta_m` for the at
most one family never cleared later.  Then `delta_m<=pi_m`, and at most one
`pi_m` is not a birth or later clearing threshold.  This is the exact extent
of the match.

What remains outside that single adjacent debt is the proper non-adjacent
boundary fan

\[
 \boxed{
 \begin{aligned}
 B_m^{\rm fan}={}&
 \sum_{q=m+1}^{U-1}(-\kappa_{m,q})\mathcal D_{m,q}^2\\
 &+\sum_{p=m+1}^{U-1}(-\kappa_{p,U})\mathcal D_{p,U}^2.
 \end{aligned}}
\tag{38f}
\]

It is not controlled by the statement that at most one adjacent family is
outstanding.  The exact local repayment assertion is

\[
 B_m^{\rm fan}+B_m^{\rm adj}
 \leq P_m^{\rm corner}+P_m^{\rm adj}+P_m^{\rm nonadj},
\tag{38g}
\]

where the three terms on the right are respectively the full-span corner,
the positive interior adjacent atoms, and the positive interior
non-adjacent atoms from (38).  No `o(log J)` bound is presently known for the
non-adjacent fan in (38f); in contrast, Corollary 3 has completely removed
the adjacent `kappa`-debt from the infinite-history obstruction.  The next
section proves that the last class on the right of (38g) cannot be deleted.

## 7. Exact eight-mark no-go: non-adjacent bulk repayment is necessary

A tempting strengthening of (38) is that the full-span corner plus the
positive adjacent atoms always pay the two boundary fans.  This is false even
for a genuine eight-mark Golomb ruler.

Take

\[
 A=(0,8,24,56,58,314,318,319).
\tag{39}
\]

Its seven actual gaps are

\[
 (8,16,32,2,256,4,1),
\]

which are distinct powers of two.  Every positive difference is the sum of
a different consecutive subset of these powers, so binary uniqueness proves
that all 28 differences are distinct.  At `m=4`, the newborn gaps are

\[
 (h_4,h_5,h_6,h_7)=(2,256,4,1),\qquad G=263.
\]

The following table is a direct exact evaluation of (29)--(30).  Its last
column is `\kappa_{p,q}\mathcal D_{p,q}^2` before division by `2G`.

| `(p,q)` | `\mathcal D_{p,q}` | `\kappa_{p,q}` | signed term |
|---:|---:|---:|---:|
| `(4,4)` | 2 | `-47/26880` | `-47/6720` |
| `(4,5)` | 258 | `-193/26880` | `-1070571/2240` |
| `(4,6)` | 262 | `-181/8960` | `-3106141/2240` |
| `(4,7)` | 263 | `261/8960` | `18053109/8960` |
| `(5,5)` | 256 | `53/13440` | `27136/105` |
| `(5,6)` | 260 | `59/13440` | `49855/168` |
| `(5,7)` | 261 | `-271/26880` | `-6153597/8960` |
| `(6,6)` | 4 | `121/13440` | `121/840` |
| `(6,7)` | 5 | `-47/3840` | `-235/768` |
| `(7,7)` | 1 | `-61/8960` | `-61/8960` |

Grouping this table gives

\[
 \begin{array}{c|c}
 \text{atom class}&\text{unsigned or positive total}\\ \hline
 \text{boundary debt}&68589931/26880\\
 \text{full-span corner}&18053109/8960\\
 \text{positive adjacent bulk}&72403/280\\
 \text{positive non-adjacent bulk}&49855/168.
 \end{array}
\tag{40}
\]

The corner and all positive adjacent atoms miss the debt by the exact amount

\[
 \boxed{
 \frac{68589931}{26880}
 -\frac{18053109}{8960}
 -\frac{72403}{280}
 =\frac{1869979}{6720}>0.}
\tag{41}
\]

The one positive non-adjacent bulk interval `(5,6)` is therefore genuinely
needed.  After adding it, the exact positive surplus is

\[
 \frac{41407}{2240}>0,
\]

and (32) gives

\[
 \langle H,\mathcal S_4\rangle
 =\frac{41407}{1178240}.
\tag{42}
\]

Thus any P13 proof that tries to repay old-cheap overlap using only adjacent
gaps and the shell diameter is too narrow.  Interior non-adjacent differences
are not optional.

## 8. Exact four-mark no-go: the rank-one term is not controlled by newborn covariance

A second tempting bridge is

\[
 \langle H,\mathcal R_m\rangle
 \leq K\langle H,\mathcal S_m\rangle
\tag{43}
\]

with an absolute constant `K`.  It is false on finite Golomb rulers.

For every integer `D>=2`, let

\[
 A_D=(0,D,3D,3D+1).
\tag{44}
\]

Its differences are

\[
 1,D,2D,2D+1,3D,3D+1,
\]

so it is Golomb.  At `m=2`,

\[
 (h_0,h_1,h_2,h_3)=(1,D,2D,1),
 \quad N=D+1,\quad G=2D+1,\quad N'=3D+2.
\]

The newborn shell has two atoms, and `Phi_(2,3)=1/112`, so

\[
 \langle H,\mathcal S_2\rangle
 =\frac{2D}{2D+1}\frac1{112}.
\tag{45}
\]

The two coordinates of the mean difference are exactly

\[
 d_f=-\frac{2D^2+8D+3}{16(D+1)(2D+1)},
 \qquad
 d_u=-\frac{2D^2+6D+3}{4(D+1)(2D+1)}.
\tag{46}
\]

Hence

\[
 \langle H,\mathcal R_2\rangle
 =\frac{(D+1)(2D+1)}{3D+2}\,d^{\mathsf T}Hd,
\tag{47}
\]

and, since `d -> z(1/4)-z(1/2)` with squared `H`-norm `23/1680`,

\[
 \boxed{
 \lim_{D\to\infty}
 \frac1D
 \frac{\langle H,\mathcal R_2\rangle}
      {\langle H,\mathcal S_2\rangle}
 =\frac{46}{45}.}
\tag{48}
\]

The same ratio holds after both terms are divided by `N'`.  Thus newborn
covariance cannot pay the rank-one mixture term by any universal constant.
This family is not claimed to lie under one fixed critical envelope; it is a
no-go only for the unconditional local comparison (43).

## 9. Consequence for P13

The actual innovation now has two rigorously exposed accounting systems.

1. The exact system (13), (17), and (32) preserves cancellations.  Its only
   shell debts are two boundary fans, and (38) proves that the full span and
   bulk intervals repay them within the same shell.  The eight-mark ruler
   proves that genuinely non-adjacent bulk repayment must be retained.
   Corollary 3 removes the adjacent endpoint part of those fans from the
   infinite-history obstruction.
2. The positive system (25)--(27) discards cancellation but charges the whole
   innovation to globally unique non-adjacent differences.  The only
   non-Golomb boundary row is already globally summable by (28).

This makes the next missing theorem precise.  On one branch satisfying
`surv_C(A_(2m))=infinity`, one must either

- amortize the exact boundary-fan debts in (32) against positive bulk atoms
  without repeatedly spending the same historical capacity, while also
  controlling the Abel fan (17); or
- prove the stronger positive square-atom budget obtained by summing the
  first two terms of (27) is `o(log J)`.

The complete birth ledger guarantees that the numerical atoms used at
different epochs are distinct, but its present inverse-threshold moment does
not prove either assertion.  The four-mark family also shows that the
rank-one term must be budgeted separately from newborn covariance.  These are
the remaining infinite-history issues; no solution or prize claim is made.

## 10. Verification status

The displayed identities were additionally checked with exact rational
arithmetic on positive integer gap vectors for:

- 155 shell instances (`m=2,...,32`, five deterministic pseudorandom vectors
  each), including equality in (32) and the complete sign classification;
- 115 full-update instances (`m=2,...,24`, five vectors each), including
  (13) and the Abel identity (17);
- every entry of the eight-mark table and the Golomb property of (39);
- the ratios for (44) at `D=2,3,10,100,1000`.

Those finite checks are sanity evidence only; the proofs above establish the
identities.  A separate persistent verifier was then added:

- `wave8_q_atom_verifier.py` independently rebuilds the matrix pair forms,
  Abel fan, signed square expansion, sign classification, positive envelope,
  adjacent-debt bound, and both no-go families;
- `test_wave8_q_atom_verifier.py` runs five exact tests, including 44
  deterministic gap-vector audits for `m=2,...,12`.

The verifier uses only integer and `Fraction` arithmetic.  Release-manifest
integration is performed at the package level rather than asserted here.
