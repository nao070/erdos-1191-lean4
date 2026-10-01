# Route C: cross-ratio box-dipole bridge and fixed-prefix no-go

Date: 2026-08-29  
Status: `COMMON_SCALE_DENSITY_MAP_PROVED_SIGNED_FINITE_HORIZON_INSERTION_OPEN`

This note gives an exact common scale coordinate system for the Wave-19
inner-birth atoms and the centered uniform-box carrier.  It also proves that
the previously natural comparison with one fixed-prefix critical multiband
increment cannot hold uniformly.  The surviving target is consequently a
rank-aware, phase-integrated, finite-horizon signed ledger with legal terminal
ownership.  No Question 1, Question 2, publication novelty, complete-proof,
or prize claim is made.

## 1. Conventions and epoch alignment

Let

\[
 0=a_0<a_1<\cdots<a_{2n-1},\qquad
 h_r=a_r-a_{r-1},\qquad
 D_{p,q}=a_q-a_{p-1}=\sum_{r=p}^q h_r.
\]

For `n <= i <= j-2` and `j <= 2n-1`, put

\[
 M=D_{i+1,j-1},\qquad u=h_i,\qquad v=h_j,
 \qquad D=D_{i,j}=M+u+v.
\]

The primitive positive cross ratio and the Wave-19 inner-birth mass are

\[
 C_{ij}
 =\log\frac{D_{i,j-1}D_{i+1,j}}
 {D_{i+1,j-1}D_{i,j}}
 =\log\frac{(M+u)(M+v)}{M(M+u+v)},
 \tag{1.1}
\]

\[
 \mathcal W_n
 =\sum_{j=n+2}^{2n-1}\sum_{i=n}^{j-2}
 \alpha_{ij}C_{ij},
 \qquad
 \alpha_{ij}={ (j-i)^2\over4n^2}.
 \tag{1.2}
\]

Thus Wave epoch `n` uses the `2n`-mark prefix and the new gap block
`h_n,...,h_(2n-1)`.  In the centered multiband carrier notation the matching
current cardinality is `k_j=2n`; the two ledgers see the same new gap block.
They do not yet see the same atoms: the proved carrier birth floor uses the
singleton differences `D_(t,t)=h_t`, whereas (1.2) uses nonadjacent gap-pair
cross ratios.

## 2. Uniform-box dipole identity

For real `T>0`, let

\[
 K_T(x)=T^{-1}{\bf1}_{[0,T]}(x),\qquad
 R_T(d)=\langle K_T,\tau_dK_T\rangle
 ={(T-d)_+\over T^2}\quad(d\ge0).
 \tag{2.1}
\]

Orient the two endpoint-gap dipoles by

\[
 e_i=\delta_{a_{i-1}}-\delta_{a_i},\qquad
 e_j=\delta_{a_{j-1}}-\delta_{a_j}.
\]

Define

\[
 \psi_T(M,u,v)
 =R_T(M)+R_T(D)-R_T(M+u)-R_T(M+v).
 \tag{2.2}
\]

Translation invariance gives the exact sign and factor

\[
 \boxed{\psi_T(M,u,v)
 =-\langle e_i*K_T,e_j*K_T\rangle.}
 \tag{2.3}
\]

There is no factor `2` in (2.3).  A factor `1/2` appears only if the
alternative normalization `phi_T=2R_T` is used.

Assume without loss that `u<=v` and write `y=T-M`.  The numerator
`T^2 psi_T` is exactly

\[
 \begin{cases}
 0,&y\le0,\\
 y,&0<y\le u,\\
 u,&u<y\le v,\\
 u+v-y,&v<y\le u+v,\\
 0,&y>u+v.
 \end{cases}
 \tag{2.4}
\]

Consequently `psi_T>=0`, and its positive support is precisely

\[
 M<T<M+u+v=D.
 \tag{2.5}
\]

For `0<a<b`, direct integration at the two break points gives

\[
 \int_0^\infty\{R_T(a)-R_T(b)\}\,dT=\log{b\over a}.
 \tag{2.6}
\]

Applying (2.6) twice to (2.2) proves the exact continuum representation

\[
 \boxed{
 C_{ij}
 =\int_0^\infty\psi_T(M,h_i,h_j)\,dT
 =-\int_0^\infty
 \langle e_i*K_T,e_j*K_T\rangle\,dT.}
 \tag{2.7}
\]

This is a common *box-scale coordinate system*.  It is not by itself the
existing translation-invariant point-indicator master theorem: the channels
`e_i` depend on ranks, and the matrix with zero diagonal and positive
off-diagonal coefficients `alpha_(i,j)` is generally indefinite.

## 3. Exact Wave scale density

Extend `alpha_(i,j)` by zero outside the support in (1.2), and define

\[
 Q_n(T)=\sum_{i,j}\alpha_{ij}\psi_T(M,h_i,h_j)\ge0.
 \tag{3.1}
\]

Then Tonelli's theorem and (2.7) give

\[
 \boxed{\mathcal W_n=\int_0^\infty Q_n(T)\,dT.}
 \tag{3.2}
\]

Expanding (2.2) in suffix interval differences yields

\[
 Q_n(T)=\sum_{n\le p\le q\le2n-1}
 \lambda_{p,q}R_T(D_{p,q}),
 \tag{3.3}
\]

where the exact discrete mixed derivative is

\[
 \boxed{\lambda_{p,q}
 =\alpha_{p,q}+\alpha_{p-1,q+1}
 -\alpha_{p,q+1}-\alpha_{p-1,q}.}
 \tag{3.4}
\]

Writing `ell=q-p`, its complete coefficient table is:

- full span `(p,q)=(n,2n-1)`:
  \((n-1)^2/(4n^2)>0\);
- left boundary `p=n`, excluding the full span: `0` for `ell=0`,
  `-1/n^2` for `ell=1`, and `-(2ell+1)/(4n^2)` for `ell>=2`;
- right boundary `q=2n-1`, excluding the full span: the same values;
- strict interior `n+1<=p<=q<=2n-2`: `1/n^2` for `ell=0`,
  `1/(4n^2)` for `ell=1`, and `1/(2n^2)` for `ell>=2`.

The signs in this table are not an error: the full sum (3.3) is nonnegative
because it is the sum of the tents (3.1), not because every interval
coefficient is nonnegative.

## 4. A pointwise common capacity map

Let

\[
 \Delta^{\rm suf}_{n,T}
 =2\sum_{n\le p\le q\le2n-1}R_T(D_{p,q}).
 \tag{4.1}
\]

For a finite set of marks define the centered continuous-box energy

\[
 C_T(A)=\left\|\sum_{a\in A}\delta_a*K_T\right\|_2^2
       -{|A|\over T}
 =2\sum_{x<y\,\in A}R_T(y-x).
 \tag{4.2}
\]

When the marks and `T` are integers, its correlation values are exactly the
same `(T-d)_+/T^2` values as the discrete uniform box used in C061--C062;
thus this is not a change of normalization.

This is a subset of the centered first-use increment

\[
 \widetilde\Delta_{n,T}
 =C_T(\{a_0,\ldots,a_{2n-1}\})
  -C_T(\{a_0,\ldots,a_{n-1}\}),
 \tag{4.3}
\]

so `Delta^suf_(n,T)<=tilde Delta_(n,T)`.

Set `H'_n=D_(n,2n-1)`.  By (2.5), `Q_n(T)=0` for `T>=H'_n`.
For `T<=H'_n`, the positive full-span coefficient in (3.3) multiplies
`R_T(H'_n)=0`.  Every other positive coefficient in the table is at most
`1/n^2`.  Dropping only the negative terms in (3.3) therefore proves the
pointwise inequality

\[
 \boxed{
 0\le Q_n(T)
 \le {\Delta^{\rm suf}_{n,T}\over2n^2}
 \le {\widetilde\Delta_{n,T}\over2n^2}.}
 \tag{4.4}
\]

This is the previously missing atom-to-capacity map at each *continuous
scale*.  It does not close the common signed ledger.  Integrating (4.3) gives
only

\[
 \mathcal W_n
 \le {1\over2n^2}\int_0^{H'_n}
 \widetilde\Delta_{n,T}\,dT,
 \tag{4.5}
\]

whereas the proved centered carrier owns selected finite differences
`C_(T_j)-C_(T_(j+1))`.  Replacing the integral in (4.4) by those signed
differences would be an unproved and, in the fixed-prefix form below, false
step.

There is also an ownership boundary.  The interval differences with
`q<=2n-2` belong to the current Wave-11 bulk shell.  Those with `q=2n-1`
are current point-difference births but appear in the next epoch's lower
shell.  A finite-horizon use of (4.3) must assign these terminal atoms to
exactly one of birth capacity, next-shell capacity, or terminal reserve.

### 4.1 Finite-horizon potential and exact Gothic coefficient match

The continuous integral has a sharper finite-horizon form.  For `0<d<=H`
define

\[
 F_H(d):=\int_0^H R_T(d)\,dT
 =\log{H\over d}+{d\over H}-1.
 \tag{4.6}
\]

Take `H=H'_n`.  The mixed-difference coefficients satisfy the two exact
moment cancellations

\[
 \sum_{p,q}\lambda_{p,q}=0,
 \qquad
 \sum_{p,q}\lambda_{p,q}D_{p,q}=0.
 \tag{4.7}
\]

One proof is to note that, for every `T>=H'_n`, each tent is zero while
`R_T(d)=1/T-d/T^2`; the two coefficients in this affine tail must vanish.
Equivalently, (4.6) follows directly by taking two discrete mixed
differences in (3.4).  Therefore

\[
 \boxed{
 \mathcal W_n
 =\sum_{p,q}\lambda_{p,q}F_{H'_n}(D_{p,q})
 =-\sum_{p,q}\lambda_{p,q}\log D_{p,q}.}
 \tag{4.8}
\]

The full-span positive coefficient contributes nothing because
`F_(H'_n)(H'_n)=0`.  Every remaining positive coefficient is strict
interior, namely `n+1<=p<=q<=2n-2`, and there it is **exactly** the Wave-11
Gothic coefficient

\[
 \lambda_{p,q}=\beta_n(p,q)=
 \begin{cases}
 1/n^2,&q-p=0,\\
 1/(4n^2),&q-p=1,\\
 1/(2n^2),&q-p\ge2.
 \end{cases}
 \tag{4.9}
\]

It follows that

\[
 \boxed{
 \mathcal W_n\le
 \sum_{p=n+1}^{2n-2}\sum_{q=p}^{2n-2}
 \beta_n(p,q)F_{H'_n}(D_{p,q}).}
 \tag{4.10}
\]

No positive term on the right of (4.10) has `q=2n-1`; terminal/next-shell
atoms occur only with nonpositive lambda and may be dropped for this upper
bound.  This removes the *positive terminal-capacity* ambiguity in (4.5).
It does not create free capacity: the same strict-interior `beta` atoms are
already owned by the exact Gothic bulk split.  Any use of (4.10) must rewrite
that signed ledger in the scale-potential basis and may not add (4.10) on top
of the existing `mathfrak B_n` payment.

## 5. Why finitely many dyadic phases do not integrate the tents

Unshifted dyadic sampling has no uniform atomwise lower comparison with
(2.7).  The four-point Golomb ruler

\[
 \{0,1,5,7\}
\]

has `(M,u,v)=(4,1,2)`.  Its tent is supported on `(4,7)`, which contains no
dyadic width, but

\[
 C_{ij}=\log(15/14)>0.
 \tag{5.1}
\]

It has no uniform upper comparison either.  For a dyadic integer `T>=4`,
the Golomb ruler

\[
 \{0,1,T,T+2\}
\]

has `(M,u,v)=(T-1,1,2)`.  Only the sample at width `T` is nonzero, and

\[
 \sum_{r\in\mathbb Z}2^r\psi_{2^r}={1\over T},
 \qquad
 C_{ij}=\log{T(T+1)\over(T-1)(T+2)}\sim{2\over T^2}.
 \tag{5.2}
\]

Thus the ratio is unbounded.  More generally, any fixed finite collection of
logarithmic phases leaves a multiplicative gap between consecutive sample
widths.  At sufficiently large scale that gap contains the full support of a
translated `(M,1,2)` tent, so a finite set of phases still cannot give an
atomwise lower comparison.

There is, however, an exact continuum log-phase formula.  Substituting
`T=2^(r+theta)` and using `dtheta=dT/(T log 2)` gives

\[
 \boxed{
 \int_0^1\sum_{r\in\mathbb Z}
 2^{r+\theta}\psi_{2^{r+\theta}}\,d\theta
 ={C_{ij}\over\log2}.}
 \tag{5.3}
\]

The intervals `[2^r,2^(r+1))` partition `(0,infinity)`, and every summand is
nonnegative, so the interchange is justified by Tonelli.  Summing the atoms
also gives

\[
 \boxed{
 \int_0^1\sum_{r\in\mathbb Z}
 2^{r+\theta}Q_n(2^{r+\theta})\,d\theta
 ={\mathcal W_n\over\log2}.}
 \tag{5.4}
\]

The surviving scale interface is therefore phase-integrated or adaptive;
no fixed finite phase grid works atomwise.

## 6. ET finite-family no-go for fixed-prefix comparison

The obstruction above is not merely a narrow-tent artifact.  Fix `C>0` and
let `k=2n` be dyadic.  By Bertrand's theorem choose a prime `k<p<2k`, let
`rho_m` be the representative of `m^2 mod p` in `{0,...,p-1}`, and put

\[
 a_m=2pm+\rho_m,\qquad0\le m<k.
 \tag{6.1}
\]

### 6.1 Sidon property and span

If `a_j-a_i=a_v-a_u`, the perturbations in (6.1) have absolute difference
less than `2p`; hence `j-i=v-u=:d`.  Reduction modulo `p` then gives

\[
 d(2i+d)\equiv d(2u+d)\pmod p.
\]

Since `1<=d<k<p` and `p` is odd, this forces `i=u` and then `j=v`.
Thus (6.1) is an integer Sidon set.  Moreover

\[
 N_k=a_{k-1}+1<2pk<4k^2,
 \tag{6.2}
\]

so for every fixed `C` it satisfies
`N_k<C k^2 log(2k)` for all sufficiently large `k`.

The adjacent gaps obey

\[
 p+1\le h_m\le3p-1.
 \tag{6.3}
\]

For separation `r=j-i>=2`, the outer span is less than `3p(r+1)`.
Using

\[
 C_{ij}\ge {h_ih_j\over D_{i,j}^2}
\]

and (6.3), one obtains

\[
 \boxed{
 \mathcal W_n>
 {1\over36n^2}\sum_{r=2}^{n-1}(n-r){r^2\over(r+1)^2}
 \ge{(n-2)(n-1)\over162n^2}.}
 \tag{6.4}
\]

In particular `liminf W_n>=1/162`.

### 6.2 Uniform-box energy is almost scale-flat

Compare (6.1) with the arithmetic progression
`B={0,2p,...,2p(k-1)}`.  The hinge in the definition of `C_S` is
1-Lipschitz.  For every `S<2p(k-1)`, grouping by rank separation and summing
the progression exactly gives

\[
 \boxed{
 \left|C_S(A)-{k\over2p}\right|
 \le {2k\over S}+{4pk\over S^2}
      +{S\over4p^2}+{1\over2p}.}
 \tag{6.5}
\]

For completeness, the perturbation from `A` to `B` contributes at most
`k/S+2pk/S^2`.  If `R=floor(S/(2p))`, writing
`S/(2p)=R+delta` and evaluating

\[
 {2\over S^2}\sum_{r=1}^R(k-r)(S-2pr)
\]

shows that the progression differs from `k/(2p)` by at most
`k/S+2pk/S^2+S/(4p^2)+1/(2p)`, proving (6.5).

Use the canonical critical schedule

\[
 T_k=k\,2^{\lceil\log_2(8C\log(2k))\rceil},
\]

and let `T_k^+` be the corresponding width for cardinality `2k`.  Then
`T_k^+/T_k` is `2` or `4`.  For all sufficiently large `k`, both widths are
below `2p(k-1)`, and (6.5) yields, with `L=log(2k)`,

\[
 \boxed{
 |C_{T_k}(A)-C_{T_k^+}(A)|
 \le {3\over8CL}+{5\over32C^2L^2}
      +{20CL\over k}+{1\over k}\longrightarrow0.}
 \tag{6.6}
\]

The constant-cover boundary ratio also tends to one, so the normalized
centered retained gain tends to zero while (6.4) stays positive.

Consequently, for every fixed `C>0` and `K<infinity`, arbitrarily large
finite critical Sidon prefixes satisfy

\[
 \mathcal W_{k/2}>K|C_{T_k}(A)-C_{T_k^+}(A)|,
 \tag{6.7}
\]

and the analogous inequality for the normalized fixed three-channel gain.
This refutes a uniform fixed-prefix domination, its absolute-value version,
and any coefficientwise comparison implying them.

It does **not** refute a telescope along one fixed infinite Sidon branch,
adaptive widths, the continuum phase average (5.3), rank-aware dipole
channels, or a finite-horizon signed theorem that includes Wave-19 floors and
terminal ownership.  The family (6.1) changes with `k`.

## 7. Exact remaining obligation

The new state is

\[
 \boxed{
 \texttt{COMMON\_SCALE\_DENSITY\_MAP\_PROVED;}\quad
 \texttt{FINITE\_HORIZON\_SIGNED\_INSERTION\_OPEN}.}
\]

A successful continuation must simultaneously:

1. integrate or discretize the phase continuum without the false finite-grid
   comparison closed in Section 5;
2. place the rank-dependent dipole cross terms inside a legal positive
   master inequality, paying any diagonal/PSD-completion price;
3. couple that gain with the Wave-19 negative-sign floor in one inequality,
   rather than subtracting two unrelated positive estimates;
4. respect the existing Gothic use of interval atoms and give every
   `q=2n-1` terminal atom exactly one owner; and
5. telescope on one compatible infinite spatial-prefix history.

Until these five items are proved, C058 and the global problem remain open.
