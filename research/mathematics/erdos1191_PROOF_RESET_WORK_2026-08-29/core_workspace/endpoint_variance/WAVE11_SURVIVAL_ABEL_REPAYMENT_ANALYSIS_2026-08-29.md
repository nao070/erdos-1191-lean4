# Wave 11: survival Abel repayment, interval ranks, and the remaining moving-frontier obstruction

Date: 2026-08-29  
Status: **new universal main-term repayment proved; secondary survival repayment open; P15 not closed**

This note starts from the canonical Wave 9--10 state.  In particular, it
uses the exact Wave 10 Abel shell, its weighted global rearrangement floor,
and the corrected Route A identity.  It does not infer an infinite branch
from any finite ruler.

## 1. Outcome

There are four conclusions.

1. **Theorem (unconditional interval-consistency repayment).**  Every bulk
   interval of length `ell` is the sum of `ell` globally distinct positive
   adjacent gaps, and hence is at least `ell(ell+1)/2`.  Applying this to the
   exact Abel coefficients gives a self-contained all-length bulk floor

   \[
   K_J^{\rm len}=2\sum_{m\in E_J}\log m+O(|E_J|).
   \]

   Its lower-shell part is `(1/2) log m+O(1)` per epoch and its remaining
   interior part is `(3/2) log m+O(1)`.  Thus the missing leading quarter in
   the Wave 10 `7/4` spectrum floor is rigorously repaid:

   \[
   K_J^{\rm len}-F_{E_J}
   ={1\over4}\sum_{m\in E_J}\log m+O(|E_J|).
   \]

   A distinct mixed floor `K_J^(mix)` applies this length information to the
   lower shell and globally re-sorts only the remaining `q>=m` bulk.  It has
   the same leading term.  The two certificates are kept separate below so
   that no allocation is silently reused.

2. **Theorem (exact finest Route A decomposition).**  For the complete
   dyadic bulk triangle, the actual numerical holes, the coefficient/rank
   assignment premium, the interval-containment rank surplus, and the
   boundary slack admit exact nonnegative decompositions.  In particular,

   \[
   \sum_{m\in E_J}Y_m
   =(T_J-K_J^{\rm len})-(G_J^{\rm len}+S_J),
   \qquad G_J^{\rm len}\geq0,\quad S_J\geq0.
   \tag{W11-EXACT-GAP}
   \]

   There is also an exact rank version in (21) below.

3. **Conditional theorem (eventually critical branch).**  On one fixed
   infinite eventually `C`-critical Golomb branch,

   \[
   0\leq\sum_{m\in E_J}Y_m
   \leq T_J-K_J^{\rm len}=O_C(J\log J).
   \tag{W11-MIXED-UPPER}
   \]

   This removes the old `Theta(J^2)` leading deficit, but it is not the
   required `o(log J)` estimate.

4. **Sharp obstruction to a natural next move.**  The exact lower-shell
   residual is a positive future cross-ratio tail.  After summing dyadic
   epochs, a fixed pair `(i,j)` is counted with multiplicity
   `Theta(log(j/i))`.  Therefore it cannot be charged term by term, with a
   uniform constant, to the pair's single birth-shell atom.  Changing finite
   Erdős--Turán windows also show that the new triangular floor can be sharp
   up to `O(1)` per epoch.  These facts refute the stated local mechanisms;
   they do **not** refute an aggregate theorem on one fixed
   `surv_C=infinity` branch.

Consequently P15, Erdős Problem #1191, and the prize claim remain open.

## 2. Exact Wave 10 shell and Route A quantities

Let

\[
0=a_0<a_1<a_2<\cdots,
\qquad h_r=a_r-a_{r-1},
\qquad D_{p,q}=a_q-a_{p-1}=\sum_{r=p}^q h_r
\]

be a Golomb ruler, so all positive differences `D_(p,q)` are distinct.
Fix a dyadic `m>=4`, put

\[
n=2m,\qquad g=2m-1,\qquad
w_r={r^2\over4m^2},\qquad
\theta_m=w_{g-1}=\left({m-1\over m}\right)^2.
\]

For `j-i>=2`, write

\[
C_{ij}=\log{D_{i,j-1}D_{i+1,j}\over
                   D_{i+1,j-1}D_{i,j}}>0,
\]

and let

\[
Y_m=\sum_{j=m}^{g}\sum_{i=1}^{j-2}
       \left({j-i\over2m}\right)^2C_{ij}.
\tag{1}
\]

The exact positive fan is

\[
\begin{aligned}
Q_m={}&w_{m-1}\log D_{1,m-1}
+\sum_{q=m}^{g-1}(w_q-w_{q-1})\log D_{1,q}\\
&+w_2\log D_{g-1,g}
+\sum_{\ell=3}^{g-1}(w_\ell-w_{\ell-1})
  \log D_{n-\ell,g}.
\end{aligned}
\tag{2}
\]

Put

\[
\mathcal I_m=\{(p,q):2\leq p\leq q,\ m-1\leq q\leq2m-2\}.
\tag{3}
\]

For `ell=q-p+1`, the negative-bulk coefficient is

\[
4m^2\beta_m(p,q)=
\begin{cases}
4,&q=m-1,\ \ell=1,\\
2\ell+1,&q=m-1,\ \ell\geq2,\\
4,&q\geq m,\ \ell=1,\\
1,&q\geq m,\ \ell=2,\\
2,&q\geq m,\ \ell\geq3.
\end{cases}
\tag{4}
\]

Define

\[
A_m=\sum_{(p,q)\in\mathcal I_m}\beta_m(p,q)\log D_{p,q},
\qquad T_m=\theta_m\log D_{1,g}.
\tag{5}
\]

The Wave 10 Abel identity is exactly

\[
Y_m=Q_m-T_m-A_m.
\tag{6}
\]

Now take

\[
E_J=\{4,8,\ldots,2^J\},
\quad A_J=\sum_{m\in E_J}A_m,
\quad Q_J=\sum_{m\in E_J}Q_m,
\quad T_J=\sum_{m\in E_J}T_m.
\]

Here `J` is the last dyadic exponent and `|E_J|=J-1`.  Thus an estimate in
the number of epochs differs from an estimate in `J` only by this fixed
shift.

Let `F_(E_J)` be the Wave 10 floor obtained by sorting all coefficients
`beta_m(p,q)` decreasingly and pairing them with `log 1,log 2,...`.
The remaining Route A quantities are

\[
P_J=A_J-F_{E_J},\qquad
S_J=2T_J-Q_J,\qquad
U_{E_J}=T_J-F_{E_J}.
\tag{7}
\]

Thus

\[
\boxed{\sum_{m\in E_J}Y_m
=U_{E_J}-P_J-S_J=T_J-A_J-S_J.}
\tag{8}
\]

### Exact boundary-slack decomposition

Let

\[
c^L_{m,q}=
\begin{cases}
w_{m-1},&q=m-1,\\
w_q-w_{q-1},&m\leq q\leq g-1,
\end{cases}
\]

and

\[
c^R_{m,\ell}=
\begin{cases}
w_2,&\ell=2,\\
w_\ell-w_{\ell-1},&3\leq\ell\leq g-1.
\end{cases}
\]

Both coefficient families have total mass `theta_m`.  Therefore

\[
\begin{aligned}
S_m:={}&2T_m-Q_m\\
={}&\sum_{q=m-1}^{g-1}c^L_{m,q}
 \log{D_{1,g}\over D_{1,q}}
+\sum_{\ell=2}^{g-1}c^R_{m,\ell}
 \log{D_{1,g}\over D_{n-\ell,g}}\geq0,
\end{aligned}
\tag{9}
\]

and `S_J=sum_(m in E_J) S_m`.  This proves the sign in (7), rather than
merely bounding the two fans separately.

## 3. The complete bulk triangle and its numerical ranks

### Theorem 1 (the dyadic right-end bands tile a complete triangle)

For consecutive dyadic epochs,

\[
\bigcup_{m\in E_J}\mathcal I_m
=\mathcal B_J
:=\{(p,q):2\leq p\leq q,\ 3\leq q\leq2^{J+1}-2\}.
\tag{10}
\]

Indeed, the right-end bands are

\[
[3,6],[7,14],[15,30],\ldots,
[2^J-1,2^{J+1}-2],
\]

which are disjoint and consecutive.  Hence every item in (10) belongs to
exactly one shell, and all its numerical differences are globally distinct.

Order these differences as

\[
d_1<d_2<\cdots<d_M,
\]

and denote by `gamma_r` the Abel coefficient attached to the interval whose
value is `d_r`.  Then

\[
A_J=\sum_{r=1}^M\gamma_r\log d_r.
\tag{11}
\]

Let `beta_1^down>=...>=beta_M^down` be the same coefficient multiset sorted
decreasingly.  Define

\[
H_J^{\rm num}=\sum_{r=1}^M\gamma_r\log{d_r\over r},
\qquad
H_J^{\rm perm}=\sum_{r=1}^M\gamma_r\log r
-\sum_{r=1}^M\beta_r^\downarrow\log r.
\tag{12}
\]

Since distinct positive integers satisfy `d_r>=r`, and decreasing weights
minimize their pairing with the increasing sequence `log r`, both terms in
(12) are nonnegative.  Moreover,

\[
\boxed{P_J=H_J^{\rm num}+H_J^{\rm perm}.}
\tag{13}
\]

Thus `H^num` is the exact weighted premium from unoccupied numerical values,
while `H^perm` is the exact premium from putting the coefficient classes at
their actual ranks rather than at the optimal rearranged ranks.

There is a canonical layer-cake expression for the second term.  For `t>=0`,
put

\[
R_t=\{r:\gamma_r>t\},\qquad N(t)=|R_t|.
\]

Then Tonelli's theorem and the equality of the coefficient distributions give

\[
\boxed{
H_J^{\rm perm}
=\int_0^\infty
 \log\left({\prod_{r\in R_t}r\over N(t)!}\right)\,dt\geq0.}
\tag{14}
\]

This is an identity, not a finite-data heuristic.

### Theorem 2 (contained subintervals force exact rank floors)

For an item `(p,q)` of length `ell=q-p+1`, define

\[
\tau(p,q)=\binom{\ell+1}{2}-{\bf1}_{\{p=2\}}.
\tag{15}
\]

Its rank `r_J(p,q)` inside the ordered set (10) obeys

\[
r_J(p,q)\geq\tau(p,q).
\tag{16}
\]

To see this, take all subintervals `[u,v]` contained in `[p,q]`.  There are
`binom(ell+1,2)` of them.  Every proper subinterval has smaller positive
difference, and the whole interval supplies the rank endpoint itself.  If
`p>=3`, all these intervals are in `B_J`.  If `p=2`, the only missing one is
`[2,2]`, whose right endpoint is 2 rather than at least 3.  This proves (16),
including the endpoint correction.

Set

\[
K_J^{\rm rank}
=\sum_{m\in E_J}\sum_{(p,q)\in\mathcal I_m}
 \beta_m(p,q)\log\tau(p,q),
\tag{17}
\]

and, with `(p_r,q_r)` denoting the interval of value `d_r`, set

\[
C_J^{\rm rank}
=\sum_{r=1}^M\gamma_r
 \log{r\over\tau(p_r,q_r)}\geq0.
\tag{18}
\]

Combining (11), (12), and (16) gives the exact identities

\[
\boxed{
A_J=K_J^{\rm rank}+C_J^{\rm rank}+H_J^{\rm num},}
\tag{19}
\]

\[
\boxed{
P_J=(K_J^{\rm rank}-F_{E_J})
     +C_J^{\rm rank}+H_J^{\rm num}.}
\tag{20}
\]

No sign is asserted for the displayed difference
`K_J^(rank)-F_(E_J)` at a fixed small `J`; the other two summands are
individually nonnegative, and its asymptotic main term is positive by
Section 4.

Substituting (19) into (8) yields the finest rank/hole/slack form

\[
\boxed{
\sum_{m\in E_J}Y_m
=(T_J-K_J^{\rm rank})
 -(C_J^{\rm rank}+H_J^{\rm num}+S_J).}
\tag{21}
\]

## 4. A stronger direct interval-length floor

### Theorem 3 (triangular interval floor)

The adjacent gaps `h_1,h_2,...` are themselves positive differences of the
Golomb ruler, so they are pairwise distinct positive integers.  Consequently
every interval of length `ell` satisfies

\[
\boxed{D_{p,q}=h_p+\cdots+h_q\geq
1+2+\cdots+\ell=\binom{\ell+1}{2}.}
\tag{22}
\]

Define the per-epoch self-contained all-length floor and its sum by

\[
K_m^{\rm len}:=\sum_{(p,q)\in\mathcal I_m}
 \beta_m(p,q)\log\binom{q-p+2}{2},
\qquad
K_J^{\rm len}:=K_J:=\sum_{m\in E_J}K_m^{\rm len},
\tag{23}
\]

and

\[
G_m^{\rm len}:=A_m-K_m^{\rm len}
=\sum_{(p,q)\in\mathcal I_m}
 \beta_m(p,q)
 \log{D_{p,q}\over\binom{q-p+2}{2}}\geq0,
\qquad
G_J^{\rm len}:=G_J:=\sum_{m\in E_J}G_m^{\rm len}.
\tag{24}
\]

Then (6) and (9) give the exact **local nonnegative three-channel
identity**

\[
\boxed{
H_m^{\rm len}:=T_m-K_m^{\rm len}
=Y_m+G_m^{\rm len}+S_m,}
\qquad Y_m,G_m^{\rm len},S_m\geq0.
\tag{W11-THREE-CHANNEL}
\]

Thus `log(D_(p,q)/binom(ell+1,2))` is a canonical, termwise nonnegative
interval-hole variable; it does not require a global fan allocation.  On
summing, (8) becomes the exact mixed identity announced in Section 1:

\[
\boxed{
\sum_{m\in E_J}Y_m=(T_J-K_J)-(G_J+S_J).}
\tag{25}
\]

The only difference between (23) and the containment-rank floor (17) comes
from intervals with `p=2`.  All such intervals in `B_J` have length at least
2, and

\[
0\leq K_m^{\rm len}-K_m^{\rm rank}
=\sum_{\substack{(2,q)\in\mathcal I_m}}
 \beta_m(2,q)
 \log{\binom{q}{2}\over\binom{q}{2}-1}
=O(m^{-3}).
\tag{26}
\]

Thus either floor has the same asymptotics, but (23) is slightly stronger and
requires no allocation of numerical ranks.

### Exact lower-shell and interior sums

Put `L_ell=binom(ell+1,2)`.  On the lower shell `q=m-1`, length `ell`
corresponds to `p=m-ell`, so `1<=ell<=m-2`.  Formula (4) gives

\[
K_m^{\rm low}
={1\over4m^2}
 \left(4\log L_1+
 \sum_{\ell=2}^{m-2}(2\ell+1)\log L_\ell\right).
\tag{27}
\]

The exact coefficient mass in (27) is

\[
{4+\sum_{\ell=2}^{m-2}(2\ell+1)\over4m^2}
={ (m-1)^2\over4m^2}=w_{m-1}.
\tag{28}
\]

For the interior `m<=q<=2m-2`, let

\[
N_m(\ell)=
\begin{cases}
m-1,&3\leq\ell\leq m-1,\\
2m-\ell-2,&m\leq\ell\leq2m-3.
\end{cases}
\tag{29}
\]

This is the exact number of interior intervals of length `ell>=3`.  Hence

\[
K_m^{\rm int}
={1\over4m^2}\left(
 (m-1)\log3
 +2\sum_{\ell=3}^{2m-3}N_m(\ell)\log L_\ell
 \right).
\tag{30}
\]

The omitted length-one contribution is zero because `log L_1=0`.  The
length-two coefficient is exactly the first term in (30).

Writing `log L_ell=2 log m+log((ell/m)(ell/m+1/m)/2)`, the error sums in
(27) and (30) are bounded Riemann sums: near zero the only possible
singularity is a constant multiple of either `|log x|` or `x|log x|`, both
of which are integrable.  The
coefficient masses in (28) and in the length-at-least-three part of (30) are
respectively `1/4+O(1/m)` and `3/4+O(1/m)`.  Therefore, uniformly for
`m>=4`,

\[
\boxed{
K_m^{\rm low}={1\over2}\log m+O(1),\qquad
K_m^{\rm int}={3\over2}\log m+O(1),}
\tag{31}
\]

and

\[
\boxed{K_J=2\sum_{m\in E_J}\log m+O(|E_J|).}
\tag{32}
\]

### A distinct lower-length/interior-rearrangement floor

There is a second valid certificate which should not be conflated with
`K_J^(len)`.  Split

\[
A_J=A_J^{\rm low}+A_J^{\rm int},
\]

where the first sum has `q=m-1` and the second has `q>=m`.  Put

\[
K_J^{{\rm len},{\rm low}}=\sum_{m\in E_J}K_m^{\rm low}.
\]

Sort only the interior coefficients decreasingly as
`eta_1^down>=...>=eta_(M_int)^down`, and define

\[
F_J^{\rm int}=\sum_{r=1}^{M_{\rm int}}
 \eta_r^\downarrow\log r.
\tag{W11-INT-FLOOR}
\]

All interior differences are globally distinct.  Weighted rearrangement
therefore gives `A_J^(int)>=F_J^(int)`, while (22) gives
`A_J^(low)>=K_J^({len},{low})`.  Consequently

\[
\boxed{
K_J^{\rm mix}:=K_J^{{\rm len},{\rm low}}+F_J^{\rm int}
\leq A_J.}
\tag{W11-MIX-FLOOR}
\]

This allocation is disjoint: lower-shell intervals are paid only by their
lengths, and only the remaining interior intervals enter the rearrangement.
For one epoch the interior coefficient multiset consists of

\[
{1\over m^2}\ (m-1\text{ times}),\qquad
{1\over4m^2}\ (m-1\text{ times}),\qquad
{1\over2m^2}\ \left({(m-1)(3m-8)\over2}\text{ times}\right).
\]

The last class has mass `3/4+O(1/m)` and ranks of order `m^2`; the first two
classes have total mass `O(1/m)`.  Stirling's formula therefore gives the
single-epoch interior floor `(3/2) log m+O(1)`.  Pooling epochs cannot lower
the sum of their separate sorted floors: within each epoch its global rank
sequence dominates `1,2,...` termwise after sorting.  Conversely, assigning
successive rank blocks in increasing dyadic order gives every epoch-`m` item
rank `O(m^2)`, hence an upper `(3/2) log m+O(1)`.  Thus

\[
F_J^{\rm int}={3\over2}\sum_{m\in E_J}\log m+O(|E_J|),
\qquad
K_J^{\rm mix}=2\sum_{m\in E_J}\log m+O(|E_J|).
\tag{W11-MIX-ASYM}
\]

Direct numerical evaluation for the audited consecutive horizons
`2<=J<=9` gives `K_J^(mix)>K_J^(len)`.  That finite observation is not
promoted here to an all-`J` ordering theorem.  The uniformly valid
stronger-of-two certificate is

\[
K_J^\star=\max\{K_J^{\rm len},K_J^{\rm mix}\}\leq A_J,
\qquad G_J^\star=A_J-K_J^\star\geq0,
\tag{W11-STAR}
\]

and it has the exact residual identity

\[
\boxed{
\sum_{m\in E_J}Y_m
=(T_J-K_J^\star)-(G_J^\star+S_J).}
\tag{W11-STAR-EXACT}
\]

Wave 10 proved

\[
F_{E_J}={7\over4}\sum_{m\in E_J}\log m+O(|E_J|).
\tag{33}
\]

Combining (26), (32), and (33),

\[
\boxed{
K_J^{\rm rank}-F_{E_J}
={1\over4}\sum_{m\in E_J}\log m+O(|E_J|),
\qquad
K_J^{\rm len}-F_{E_J}
={1\over4}\sum_{m\in E_J}\log m+O(|E_J|).}
\tag{34}
\]

For `E_J={2^2,...,2^J}`, the leading term in (34) is
`(log 2)J^2/8+O(J)`.  This is precisely the leading quarter that the plain
coefficient-spectrum rearrangement did not see.

## 5. The new mixed upper and the exact surviving target

Since all `Y_m`, `G_J`, and `S_J` are nonnegative, (25) implies the universal
finite-prefix estimate

\[
\boxed{
0\leq\sum_{m\in E_J}Y_m\leq T_J-K_J.}
\tag{35}
\]

Suppose now that the marks lie on one fixed infinite eventually
`C`-critical branch.  For all sufficiently large dyadic `m`, its critical
cap gives

\[
\log a_{2m-1}\leq2\log m+\log\log(4m)+O_C(1).
\]

Together with `theta_m=1+O(1/m)` and (31), this proves

\[
T_J-K_J
=O_C\!\left(\sum_{m\in E_J}\log\log(4m)+|E_J|\right)
=O_C(J\log J).
\tag{36}
\]

This proves (W11-MIXED-UPPER), but `O(J log J)` is far larger than
`o(log J)`.  Thus the leading `J^2` deficit of this Abel certificate is
removed, while the remaining repayment problem is genuinely secondary and
still open.

Define the secondary repayment

\[
\mathcal D_J:=G_J+S_J\geq0.
\tag{37}
\]

For the Abel-shell objective, (25) shows that the exact remaining target is:
on one fixed infinite eventually `C`-critical branch, find
`epsilon_J>=0`, `epsilon_J=o(log J)`, such that

\[
\boxed{
\mathcal D_J\geq T_J-K_J-\epsilon_J.}
\tag{38}
\]

Equivalently,

\[
0\leq\sum_{m\in E_J}Y_m\leq\epsilon_J.
\]

Formula (38), not another main-term rank rearrangement, is the corrected
Wave 11 survival-repayment target.  It must recover nearly all of the
remaining endpoint `log log` profile (and any branch-specific excess) through
the triangular-gap premium `G_J`, the boundary-profile slack `S_J`, or an
exactly coupled combination of them.

Equivalently, after the local identity (W11-THREE-CHANNEL), the highest-value
next lemma is simply that survival on one compatible infinite branch forces
the total `Y`-channel to be `o(log J)`.  This is the same as saying that the
`G+S` channels capture all but `o(log J)` of `sum H_m^(len)`.  It introduces
no additional fanwise allocation convention.

## 6. Exact lower-shell mass match and a second Abel transform

Fix one epoch and abbreviate

\[
A=a_{m-1},\qquad
x_\ell=a_{m-1}-a_{m-\ell-1}=D_{m-\ell,m-1}
\quad(1\leq\ell\leq m-2).
\]

The lower-shell coefficients are

\[
\gamma_1=w_2={1\over m^2},\qquad
\gamma_\ell=w_{\ell+1}-w_\ell
={2\ell+1\over4m^2}\quad(2\leq\ell\leq m-2).
\tag{39}
\]

Their sum is exactly

\[
\sum_{\ell=1}^{m-2}\gamma_\ell=w_{m-1}
={ (m-1)^2\over4m^2},
\tag{40}
\]

which equals the coefficient of the first left-prefix term
`log D_(1,m-1)=log A`.

Before pairing it with that boundary term, the lower shell itself has a
finest prefix-rank decomposition.  Let `rho_ell` be the numerical rank of
`x_ell` among all `binom(m,2)` positive differences of the prefix
`a_0,...,a_{m-1}`.  The interval defining `x_ell` contains exactly
`L_ell=binom(ell+1,2)` subintervals.  They give distinct differences no
larger than `x_ell`, so

\[
x_\ell\geq\rho_\ell\geq L_\ell.
\tag{W11-LOW-RANK}
\]

Thus `x_ell-rho_ell` is the exact number of unoccupied positive integers up
to `x_ell` after accounting for all prefix differences.  With
`A_m^(low):=sum_ell gamma_ell log x_ell`, one has

\[
\boxed{
A_m^{\rm low}
=K_m^{\rm low}
+\sum_{\ell=1}^{m-2}\gamma_\ell\log{\rho_\ell\over L_\ell}
+\sum_{\ell=1}^{m-2}\gamma_\ell\log{x_\ell\over\rho_\ell}.}
\tag{W11-LOW-FINE}
\]

The two added terms are respectively the contained-subinterval rank surplus
and the numerical-hole premium, and both are nonnegative.  Their exact
values are prefix-dependent; no universal equality for `rho_ell` is being
asserted.

Now pair the same lower mass with the boundary term.  The residual is

\[
\begin{aligned}
\mathcal R_m^{\rm low}
&:=w_{m-1}\log A-\sum_{\ell=1}^{m-2}\gamma_\ell\log x_\ell\\
&=\sum_{\ell=1}^{m-2}\gamma_\ell
 \log{A\over x_\ell}\geq0.
\end{aligned}
\tag{41}
\]

A second summation by parts gives

\[
\boxed{
\mathcal R_m^{\rm low}
=w_{m-1}\log{A\over x_{m-2}}
+\sum_{\ell=1}^{m-3}w_{\ell+1}
 \log{x_{\ell+1}\over x_\ell}.}
\tag{42}
\]

The endpoints and indices in (42) are exact: the final boundary weight is
`w_(m-1)`, and the last ratio in the sum is `x_(m-2)/x_(m-3)`.

By (22), `x_ell>=L_ell`.  If this prefix obeys
`A<=C m^2 log(2m)`, then (27), (28), and (41) give

\[
0\leq\mathcal R_m^{\rm low}
\leq w_{m-1}\log A-K_m^{\rm low}
\leq {1\over4}\log\log(2m)+O_C(1).
\tag{43}
\]

Thus the old missing quarter is not merely an abstract global premium: after
the exact mass pairing it leaves at most a local `log log` residual.

## 7. The lower residual is exactly a positive future tail

The second Abel transform has an exact cross-ratio interpretation.  For
`1<=i<=m-2`, define

\[
f_{m,i}(t)=
\log{a_{m-1}-a_{i-1}+t\over a_{m-1}-a_i+t}.
\tag{44}
\]

For `j>=m`, put `t_j=a_j-a_{m-1}`.  Direct substitution gives

\[
C_{ij}=f_{m,i}(t_{j-1})-f_{m,i}(t_j).
\tag{45}
\]

On every infinite Golomb sequence, `t_j` tends to infinity and
`f_(m,i)(t_j)` tends to zero.  Hence monotone telescoping proves

\[
\boxed{f_{m,i}(0)=\sum_{j=m}^{\infty}C_{ij}.}
\tag{46}
\]

Matching `i=1` to the boundary term in (42), and
`i=m-ell-1` to its ratio terms, gives

\[
\boxed{
\mathcal R_m^{\rm low}
=\sum_{i=1}^{m-2}\left({m-i\over2m}\right)^2 f_{m,i}(0)
=\sum_{i=1}^{m-2}\left({m-i\over2m}\right)^2
  \sum_{j=m}^{\infty}C_{ij}.}
\tag{47}
\]

This identity needs an infinite branch but no critical cap.

For dyadic epochs through `2^J`, Tonelli's theorem rewrites (47) as

\[
\sum_{m\in E_J}\mathcal R_m^{\rm low}
=\sum_{i<j}\Omega_J(i,j)C_{ij},
\tag{48}
\]

where

\[
\Omega_J(i,j)=
\sum_{\substack{m\in E_J\\ i+2\leq m\leq j}}
\left({m-i\over2m}\right)^2.
\tag{49}
\]

Every summand in (49) is at most `1/4`; whenever `m>=2i`, it is at least
`1/16`.  Therefore, if many dyadic cuts lie between `2i` and `j`,

\[
\Omega_J(i,j)=\Theta\!\left(1+\log_2{j\over i}\right)
\tag{50}
\]

up to truncation at `2^J`.

### Refuted candidate: uniform same-atom birth absorption

Let `mu(j)` be the unique dyadic scale with `mu(j)<=j<=2mu(j)-1`.
The coefficient of `C_(ij)` in its birth shell `Y_(mu(j))` is

\[
v_{ij}=\left({j-i\over2\mu(j)}\right)^2.
\]

If `i<=j/2`, then `1/16<=v_(ij)<1`, while (50) is unbounded as `j/i`
grows.  Hence no universal constant `B` can make

\[
\Omega_J(i,j)C_{ij}\leq Bv_{ij}C_{ij}
\]

hold for all pairs and horizons on an infinite branch.  This rigorously
refutes a term-by-term bounded-overlap charge of the entire future tail to the
pair's single birth atom.  It does not refute a collective estimate that
uses cancellations of endpoint profiles, other pairs, or the
`surv_C=infinity` constraint.

## 8. Finite Erdős--Turán windows show local sharpness

This section is an obstruction only to local finite-window claims.  It is not
an infinite counterexample.

By Bertrand's postulate choose a prime `2m<=P<4m`, and take the classical
Erdős--Turán ruler of length `L=2m` in the standard form

\[
b_k=2Pk+[k^2]_P.
\]

The Golomb property of this finite construction is the standard
Erdős--Turán modular Sidon argument and is also implemented in the canonical
fixture generator.  The estimates below use only its displayed formula and
the named prime bound.

An interval containing `ell` consecutive adjacent gaps obeys

\[
b_v-b_u<P(2\ell+1)<4m(2\ell+1)\leq12m\ell.
\tag{51}
\]

Together with (22),

\[
{D_{p,q}\over L_\ell}\leq{24m\over\ell}.
\tag{52}
\]

Multiplying (52) by the exact coefficients (4) and summing proves

\[
\boxed{A_m-K_m^{\rm len}=O(1)}
\tag{53}
\]

on these changing windows.  For the lower shell the relevant sum is a
bounded Riemann sum with density proportional to
`x log(24/x)`.  For the interior, (29) reduces it to bounded Riemann sums
with density at most a constant multiple of `log(24/x)`; the exceptional
length-one and length-two classes contribute `O((log m)/m)`.

The same construction has all interval lengths comparable to `P ell`.
Using (9), its left-prefix ratios are uniformly bounded and its terminal
suffix contribution is another bounded sum of the form
`sum (ell/m^2) log(O(m/ell))`.  Thus

\[
S_m=O(1),\qquad G_m^{\rm len}+S_m=O(1)
\tag{54}
\]

on the changing finite windows.  The canonical Wave 9 calibration moreover
gives a positive absolute lower bound for their retained cross-ratio state
(and hence for the corresponding unretained shell).  Consequently a theorem
claiming `Y_m=o(1)` from one terminal critical window, numerical sparsity, or
the triangular interval floor alone is false.

The prime, modulus, and finite ruler in this construction change with `m`.
Equations (51)--(54) therefore do not contradict, and must not be promoted to
a statement about, one fixed infinite eventually critical branch.

## 9. Quantifier, sign, and endpoint audit

### Evidence and scope table

| Statement | Evidence | Scope |
|---|---|---|
| Theorems 1--3, (W11-THREE-CHANNEL), and the rank/hole identities | Self-contained counting, Abel algebra, and distinct-positive-gap proof in this note | Every indicated finite Golomb prefix/horizon |
| `K^(mix)` and its `2 sum log m` law | Wave 10 weighted rearrangement, exact interior coefficient multiset, and Stirling/block-rank proof above | Every finite consecutive dyadic horizon |
| Future-tail identity (46)--(49) | Self-contained monotone telescope | One fixed infinite Golomb branch; no criticality needed |
| Erdős--Turán obstruction | Classical modular Sidon construction plus Bertrand's postulate; finite executable calibration is supplementary | Changing finite family only |
| Fixture results | Exact-form/certificate tests, explicitly marked finite | Audit evidence, never infinitude evidence |
| Critical upper (36) | Theorems 1--3 plus an eventual `C`-critical cap | Conditional on one fixed infinite branch |
| Repayment (38), P15, and #1191 | No proof in this note | **Open** |

The following statements are **proved for every finite Golomb prefix and
every indicated finite dyadic horizon**:

- the shell identities (6), (8), (9), and (25);
- the complete-triangle identity (10);
- the numerical-hole and coefficient-assignment identity (13);
- the contained-subinterval rank floor (16) and rank identity (21);
- the triangular interval bound (22), its exact coefficient sums
  (27)--(30), and asymptotics (31)--(34);
- the nonnegative mixed upper (35).

The following statements require **one fixed infinite branch**:

- the future telescope (46)--(49); it needs only infinitude;
- the critical upper (36) and the desired repayment (38); they additionally
  need the eventual `C`-critical cap on that same branch.

The following are **refutations only of explicitly local candidates**:

- (50) refutes uniform same-pair bounded-overlap birth charging;
- (51)--(54) refute a theorem based only on a changing terminal finite
  window, and do not refute a survival-conditioned aggregate inequality.

All signs in the exact final identity are exposed:

\[
\sum Y_m=(T_J-K_J)-\underbrace{G_J}_{\geq0}
                    -\underbrace{S_J}_{\geq0}.
\]

The main-term deficit has been removed, but no lower bound of the strength
(38) is proved.  In particular, finite verification, the tail identity, and
the `O_C(J log J)` upper do not imply `surv_C=infinity`, do not imply
`o(log J)`, and do not close P15.

## 10. Verification boundary

The formulas above were checked against the exact Wave 10 coefficient table,
including the exceptional length-one and length-two weights, the lower-shell
endpoint `q=m-1`, the interior endpoint `q=2m-2`, and the terminal suffix
endpoint `q=g=2m-1`.

The proofs are self-contained, and an independent Wave 11 executable/certificate
now audits the delicate finite algebra:

- `wave11_abel_repayment_probe.py`;
- `test_wave11_abel_repayment_probe.py`;
- `wave11_abel_repayment_certificate_2026-08-29.json`.

It uses exact rational linear forms in logarithms to replay `A,Q,T,F,P,S,U`,
the hole/rearrangement split, the lower-tail telescope, the disjoint mixed
floor, and the exact strengthened residual.  Its certificate explicitly sets
`finite_computation_only=true`, `infinite_survival_inferred=false`, and
`p15_proved=false`.

The analytic worker's focused Wave 11 verification reported on 2026-08-29:

```text
7 passed in 45.83s
Ruff check: clean
Ruff format: clean
py_compile: clean
```

The root integration replay was a separate run and reported `7 passed in
47.85s`; both timings are retained rather than conflated.

Integrity values:

```text
82170ee7333f93ff62d7382561b6d291177d27299a207df7f3abc3413277d72c  wave11_abel_repayment_probe.py
b52c6a4258b12aadd783a9a7dff96e61956d15a35e92e6867cc52e7d4aeafaf8  test_wave11_abel_repayment_probe.py
0ddedc739ce3dd8161c3bd0b8d98222bf9439dfc37ed679afdfa37cb2f907e07  wave11_abel_repayment_certificate_2026-08-29.json
```

Certificate internal digest:

```text
1e9eb7627991687a22b1abf0cb36c52a876846d203374d830f545ddfb44d220b
```

The pre-existing Wave 10 focused suites were also rerun as a regression audit.

Observed focused verification on 2026-08-29:

```text
uv run --no-project --with pytest python -m pytest -q -p no:cacheprovider \
  test_wave10_laminar_triangle_check.py \
  test_wave10_log_product_packing.py \
  test_wave10_laminar_lp_probe.py
30 passed in 1.77s

uvx --from ruff ruff format --check [the six Wave 10 source/test files]
6 files already formatted
```

An independent release audit reran Ruff 0.16.5 both with its configured
default rules and with explicit `--select I` on all six unchanged Wave 10
files; both commands passed.  The earlier transient report of two `I001`
findings was not reproducible and is not used as a release claim.  The pytest
run itself passed completely.

An independent inline arithmetic audit checked, for
`m=4,8,...,2048`, the exact lower-shell mass (28), the interior multiplicity
(29), and the ratios in (31).  A separate direct evaluation checked
`K_J^(mix)>K_J^(len)` for `2<=J<=9`; as stated above, that finite comparison
is not used as an all-horizon theorem.  No finite computation is used to
prove infinitude or eventual criticality.

The final SHA-256 is reported in the handoff message so that the act of
recording it does not change the hashed file.
