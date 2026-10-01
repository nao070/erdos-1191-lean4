# Wave 10: laminar weighted incomplete-difference-triangle analysis

**Date:** 2026-08-29 (Asia/Tokyo)  
**Scope:** the Wave 9 rank-variance reduction, the long-rank/two-large-endpoint
core, and the weighted cross-ratio shell  
**Status:** two new hereditary inequalities, one uniform cross-epoch
product/kernel localization theorem, and a quantified no-go for the strongest
plain log-product rearrangement; **P15 and Erdős Problem #1191 remain open**

## 1. Outcome

This note obtains three rigorous advances.

1. There is a fully weighted, hereditary version of the Wave 9 rank-lag
   packing inequality.  It accepts arbitrary edge-dependent weights in any
   finite collection of dyadic birth triangles and controls their decreasing
   rearrangement by their maximum weighted interval congestion.  The old
   `(W9-RLP)` is its rectangular `0/1` special case.
2. Applying it to the exact endpoint product divided by its contiguous
   difference gives a uniform product/inverse-difference kernel estimate.
   The kernel load at any fixed old gap index has a summable tail over all
   later dyadic epochs.  Thus product mass cannot accumulate forever at one
   fixed part of the ruler; any obstruction must migrate to the advancing
   frontier.
3. The exact dyadic birth-shell Abel formula has a stronger arithmetic use
   than was recorded in Wave 9.  Its negative bulk intervals have disjoint
   right-end bands across epochs, so all of their differences are globally
   distinct.  A simultaneous weighted log-product rearrangement is therefore
   valid for **every** finite epoch set.  However, its rearrangement floor is

   \[
   \frac74\sum_{m\in E}\log m+O(|E|),
   \]

   whereas the positive boundary cost is
   `2 sum_(m in E) log m` to leading order.  The resulting upper certificate
   retains a sharp leading deficit of

   \[
   \frac14\sum_{m\in E}\log m.
   \]

   For consecutive dyadic epochs through `2^J`, this is `Theta(J^2)`, not
   `o(log J)`.  Hence even the full hereditary log-product upgrade of the
   presently exposed Abel bulk does **not** close P15.

The last conclusion is a no-go for this specified rearrangement method, not a
counterexample to P15.  No infinite eventually critical Golomb branch is
constructed or assumed to exist unconditionally.

Throughout, `log` is the natural logarithm.

## 2. Dyadic incomplete difference triangles

Let

\[
0=a_0<a_1<a_2<\cdots,
\qquad h_i=a_i-a_{i-1}\quad(i\geq1)
\]

be one integer Golomb branch, so all differences `a_v-a_u`, `u<v`, are
globally distinct.  For a dyadic `m`, a right endpoint `m<=j<2m`, and a lag
`1<=s<=j`, put

\[
d_{m,j,s}=a_j-a_{j-s}
            =\sum_{t=j-s+1}^{j}h_t,
\qquad I_{m,j,s}=[j-s+1,j].
\tag{1}
\]

The dyadic shell containing `j` determines `m` uniquely.  Hence distinct
triples in (1) determine distinct mark pairs, and the Golomb property makes
all selected values `d_(m,j,s)` distinct even when several epochs are mixed.

### Theorem 1 (laminar weighted incomplete-DTS inequality)

Let `E` be any finite set of dyadic epochs.  At each epoch choose any finite
set `T_m` of pairs `(j,s)` from (1), and attach arbitrary weights
`lambda_(m,j,s)>=0`.  Define the gap load and congestion

\[
L_{m,t}=\sum_{(j,s)\in T_m\atop t\in I_{m,j,s}}
          \lambda_{m,j,s},
\qquad
\Gamma_m=\max_{1\leq t<2m}L_{m,t}.
\tag{2}
\]

List all selected weights in decreasing order as
`beta_1>=...>=beta_M>=0`.  Then

\[
\boxed{
 \sum_{r=1}^{M}r\beta_r
 \leq
 \sum_{m\in E}\sum_{(j,s)\in T_m}
       \lambda_{m,j,s}d_{m,j,s}
 \leq
 \sum_{m\in E}N_{2m}\Gamma_m.}
\tag{LW-IDT}
\]

Both inequalities remain true after deleting any epochs or any selected
edges.

#### Proof

The selected `d` values are distinct positive integers.  After arranging
them increasingly as `d_(1)<...<d_(M)`, one has `d_(r)>=r`.  The
rearrangement inequality pairs the decreasing weights with the increasing
integers in the minimum scalar product, and gives

\[
 \sum\lambda d\geq\sum_{r=1}^{M}r\beta_r.
\]

For the other direction, expand every interval difference into its gaps:

\[
\begin{aligned}
 \sum_{(j,s)\in T_m}\lambda_{m,j,s}d_{m,j,s}
 &=\sum_{t=1}^{2m-1}h_t L_{m,t}\\
 &\leq \Gamma_m\sum_{t=1}^{2m-1}h_t
  =\Gamma_m a_{2m-1}<N_{2m}\Gamma_m.
\end{aligned}
\]

Summation over `E` proves the claim.  The proof did not require `E` or
`T_m` to be maximal, which proves heredity.  `square`

If `lambda_(m,j,s)=lambda_(m,s)` depends only on the lag, then at most `s`
length-`s` intervals contain a fixed gap, so

\[
 \Gamma_m\leq\sum_s s\lambda_{m,s}.
\tag{3}
\]

Taking weight one for `1<=s<=q_m` and zero otherwise gives `M=sum m q_m`
and `Gamma_m<=q_m(q_m+1)/2`.  Thus `(LW-IDT)` specializes exactly to

\[
 \frac{M(M+1)}2
 \leq\sum_{m\in E}N_{2m}\frac{q_m(q_m+1)}2,
\]

the Wave 9 hereditary rank-lag inequality.

## 3. Exact endpoint-product kernel and frontier localization

At an update `m -> L=2m`, let a genuine birth pair have
`1<=i<j<L`, `j>=m`, rank `r=j-i`, and

\[
D_{i,j}=a_j-a_{i-1}=\sum_{t=i}^{j}h_t.
\]

Discarding only the bounded fixed-`H` scalar factor `q(x)`, its exact scalar
rank-product atom is

\[
 \alpha_{i,j}^{(L)}=
 \frac{h_i h_j}{N_L^2}\left(\frac rL\right)^2.
\tag{4}
\]

Use Theorem 1 with

\[
 \lambda_{i,j}^{(L)}=\frac{\alpha_{i,j}^{(L)}}{D_{i,j}}.
\tag{5}
\]

Then `sum lambda D=sum alpha` exactly.  Thus difference uniqueness controls
the decreasing Lorentz moment of the inverse-length-normalized endpoint
energy, rather than merely its unweighted count:

\[
 \boxed{
 \sum_{r\geq1}r\bigl(\lambda^{(L)}\bigr)_r^\downarrow
 \leq\sum_{i,j}\alpha_{i,j}^{(L)}.}
\tag{6}
\]

The next lemma controls the congestion in (5) uniformly.

### Lemma 2 (cut-kernel inequality)

For any positive gap vector `h_1,...,h_g`, total length
`A=a_g`, and any gap index `1<=t<=g`,

\[
 \boxed{
 \sum_{1\leq i<j\leq g\atop i\leq t\leq j}
 \frac{h_i h_j}{D_{i,j}}
 \leq\left(\log2+\frac1e\right)A.}
\tag{7}
\]

The `log 2` constant is separately sharp for the strictly crossing part
among arbitrary positive real gap vectors, and the `1/e` constant is
separately sharp for the intervals ending at the cut.  No claim is made that
their sum is the optimal constant under the Golomb constraint.

#### Proof

Split the pairs into `i<=t<j` and `i<j=t`.  Put

\[
 U_i=a_t-a_{i-1},\qquad V_j=a_j-a_t.
\]

For the first class, the rectangles of side lengths `h_i,h_j` partition
`[0,a_t] x [0,A-a_t]`.  Since `(u+v)^(-1)` is decreasing in both variables,

\[
 \sum_{i\leq t<j}\frac{h_i h_j}{U_i+V_j}
 \leq\int_0^{a_t}\int_0^{A-a_t}\frac{du\,dv}{u+v}.
\]

The integral equals

\[
 A\log A-a_t\log a_t-(A-a_t)\log(A-a_t)
 \leq A\log2.
\tag{8}
\]

For the second class, the same one-dimensional upper-endpoint sum gives

\[
 \sum_{i<t}\frac{h_i h_t}{U_i}
 \leq h_t\int_{h_t}^{a_t}\frac{du}{u}
 =h_t\log\frac{a_t}{h_t}
 \leq\frac{a_t}{e}\leq\frac Ae.
\tag{9}
\]

Equations (8)--(9) prove (7).  Fine balanced partitions approach the first
constant, while a fine left partition with `h_t/a_t ->1/e` approaches the
second one.  `square`

### Corollary 3 (uniform cross-epoch local tail)

Let `c_0=log 2+1/e`.  For epoch `L=2m`, define the load at a gap index `t`
by

\[
 \Lambda_{L,t}=
 \sum_{i<j,\ j\geq m\atop i\leq t\leq j}
 \frac{h_i h_j}{N_L^2D_{i,j}}
 \left(\frac{j-i}{L}\right)^2.
\tag{10}
\]

Then

\[
 \boxed{\Lambda_{L,t}<\frac{c_0}{N_L}.}
\tag{11}
\]

For dyadic epochs `L_k=2^(k+1)` and every `K`, the same fixed branch obeys

\[
 \boxed{
 \sup_t\sum_{k\geq K}\Lambda_{L_k,t}
 \leq\frac{4c_0}{3}\,4^{-K}.}
\tag{12}
\]

#### Proof

Drop the rank factor in (10), enlarge the birth set to all pairs, and apply
(7).  Since `a_(L-1)<N_L`, this proves (11).  The genuine adjacent gaps are
distinct positive integers, so

\[
 N_L>\sum_{r=1}^{L-1}r=\frac{L(L-1)}2,
 \qquad \frac1{N_L}\leq\frac4{L^2}\quad(L\geq2).
\]

Summing `4/L_k^2=4^(-k)` from `k=K` to infinity proves (12).  `square`

This is a genuine uniform cross-epoch product/kernel estimate.  It shows
that a fixed old gap index receives only a summable future load.  It does not
bound the integral of that load over the ever-growing numerical frontier.
Indeed, integrating (10) against `h_t` simply reconstructs
`sum alpha`, and (11) yields only a constant per epoch.  The Wave 9 scaled
Erdős--Turán family proves that a local `o(1)` replacement is false even for
finite critical Golomb windows.  That family changes with `L`, so it does not
refute an infinite-branch theorem.

## 4. Exact sign pattern of the dyadic cross-ratio shell

Now use the primitive cross ratio from Wave 9,

\[
 C_{ij}=\log\frac{D_{i,j-1}D_{i+1,j}}
                       {D_{i+1,j-1}D_{i,j}}>0,
\]

and the unretained shell

\[
 Y_m=\sum_{j=m}^{2m-1}\sum_{i=1}^{j-2}
 \left(\frac{j-i}{2m}\right)^2C_{ij}.
\tag{13}
\]

This shell dominates the retained cross-ratio state termwise because
`(D_(i,j)/N_(2m))^2<1`.  Hence a sufficiently small global upper for `Y_m`
would close the genuine nonadjacent part of P15.

Put `g=2m-1`, `w_r=r^2/(4m^2)`, and

\[
 \theta_m=w_{g-1}=\left(\frac{m-1}{m}\right)^2.
\tag{14}
\]

Direct specialization of the four-indicator shell formula gives the
following exact support.

- **Positive left fan:** `p=1`, `m-1<=q<=g-1`.  Its first coefficient is
  `w_(m-1)`; the remaining coefficients are `w_q-w_(q-1)`.  Its total mass
  is `theta_m`.
- **Positive terminal suffix fan:** `q=g`, `2<=p<=g-1`.  At suffix length
  two the coefficient is `w_2`; thereafter it is `w_ell-w_(ell-1)`.  Its
  total mass is `theta_m`.
- **Negative full span:** `(p,q)=(1,g)`, with coefficient `-theta_m`.
- **Negative bulk:**

  \[
  \mathcal I_m=
  \left\{(p,q):p\geq2,\ m-1\leq q\leq2m-2\right\}.
  \tag{15}
  \]

  Its total absolute coefficient mass is `theta_m`.

All other coefficients vanish.  The absolute negative-bulk coefficient
multiset is exactly

\[
\begin{array}{c|c}
\text{weight}&\text{multiplicity}\\ \hline
(2\ell+1)/(4m^2),\quad 2\leq\ell\leq m-2&1\text{ each}\\
1/m^2&m\\
1/(2m^2)&(m-1)(3m-8)/2\\
1/(4m^2)&m-1.
\end{array}
\tag{16}
\]

Its cardinality is `m(3m-5)/2`.  Formula (16), including the exceptional
length-one and length-two coefficients, is independently checked by the
executable audit named in Section 8.

## 5. Hereditary weighted log-product upgrade

The right endpoints in (15) lie in

\[
 [m-1,2m-2].
\]

For consecutive dyadic scales the next interval starts at `2m-1`; hence
these bands are pairwise disjoint for all dyadic `m`.  Consequently every
`D_(p,q)=a_q-a_(p-1)` appearing in
`union_(m in E) I_m` is a different positive integer.

### Theorem 4 (global bulk-spectrum rearrangement)

Let `E` be any finite set of dyadic `m>=4`.  List all absolute coefficients
from (16), over all `m in E`, in decreasing order as

\[
 \beta^{E}_1\geq\cdots\geq\beta^{E}_{M_E}>0.
\]

Then

\[
 \boxed{
 \sum_{m\in E}\sum_{(p,q)\in\mathcal I_m}
 \beta_{m,p,q}\log D_{p,q}
 \geq
 F_E:=\sum_{r=1}^{M_E}\beta^{E}_r\log r.}
\tag{17}
\]

More generally, every subcollection `T` of these bulk intervals satisfies

\[
 \boxed{\prod_{(m,p,q)\in T}D_{p,q}\geq |T|!.}
\tag{18}
\]

#### Proof

Arrange the selected distinct positive integer differences increasingly as
`d_1<...<d_M`; then `d_r>=r`.  The rearrangement inequality assigns the
largest logarithmic weight to the smallest available integer in the minimum,
so

\[
 \sum\beta\log D\geq\sum_r\beta_r^\downarrow\log d_r
 \geq\sum_r\beta_r^\downarrow\log r.
\]

Taking all weights equal to one gives (18).  The argument applies after any
deletion, proving heredity.  `square`

Since each positive boundary difference is at most the full span
`a_(2m-1)`, the two positive fans cost at most
`2 theta_m log a_(2m-1)`.  The negative full span subtracts exactly one
copy.  Combining the Abel identity with (17) therefore proves

\[
 \boxed{
 \sum_{m\in E}Y_m
 \leq
 U_E:=\sum_{m\in E}\theta_m\log a_{2m-1}-F_E.}
\tag{19}
\]

This is the sought strengthened laminar log-product inequality.  It is
global across epochs, uses actual endpoint-product cross ratios, and is
valid on one nested branch.

## 6. Exact asymptotic strength of the rearrangement floor

The key question is whether the global sorting in (17) is strong enough to
make (19) sublogarithmic.  It is not.

### Theorem 5 (the `7/4` spectrum law)

Uniformly over every finite dyadic epoch set `E`,

\[
 \boxed{
 F_E=\frac74\sum_{m\in E}\log m+O(|E|),}
\tag{20}
\]

with an absolute implied constant.

#### Proof: lower bound

Allowing each epoch to reuse the integer ranks `1,2,...` can only lower the
global rearrangement minimum.  Hence

\[
 F_E\geq\sum_{m\in E}F_{\{m\}}.
\tag{21}
\]

Within one epoch, all `(2ell+1)/(4m^2)` weights precede the `1/m^2` block.
Their contribution is

\[
 \frac14\log m+O(1)
\]

by a bounded Riemann sum.  The `1/m^2` block has total mass `1/m` and
contributes `o(1)`.  The `(m-1)(3m-8)/2` weights equal to `1/(2m^2)` occupy
ranks from order `m` to order `m^2`; Stirling's formula gives contribution

\[
 \frac32\log m+O(1).
\]

The last `1/(4m^2)` block again has mass `O(1/m)`.  Thus

\[
 F_{\{m\}}=\frac74\log m+O(1),
\tag{22}
\]

which proves the lower half of (20).

#### Proof: upper bound

For any threshold `tau>0`, count coefficients from **all** dyadic scales,
not merely from `E`.  The first line of (16) has at most `m` coefficients,
each at most `1/(2m)`; summing dyadic `m<=1/(2tau)` gives at most `1/tau`
such coefficients.  The remaining lines contain at most `2m^2`
coefficients, each at most `1/m^2`; summing dyadic
`m<=tau^(-1/2)` gives at most `8/(3tau)`.  Therefore

\[
 \#\{\beta\geq\tau\}<\frac4\tau.
\tag{23}
\]

An item of weight `beta` consequently has global rank at most `4/beta`, so

\[
 F_E\leq\sum_{m\in E}\sum_{\beta\in(16)}
 \beta\log\frac4\beta.
\tag{24}
\]

The first line of (16) contributes `(1/4) log m+O(1)` to (24), the third
line contributes `(3/2) log m+O(1)`, and the second and fourth lines are
`O((log m)/m)`.  This proves the upper half of (20).  `square`

The coefficient `7/4` has a transparent structural meaning.  Three quarters
of the bulk mass lives on `Theta(m^2)` coefficients of size `Theta(m^-2)`
and earns `2 log m`; this contributes `(3/2) log m`.  The remaining leading
quarter is concentrated on only `Theta(m)` lower-shell coefficients and
earns only `log m`; this contributes `(1/4) log m`.  Global dyadic sorting
changes ranks only enough to alter the bounded remainder, not these leading
coefficients.

## 7. Quantified no-go for the plain laminar spectrum certificate

On an integer Golomb prefix the genuine adjacent gaps are distinct, so

\[
 a_{2m-1}\geq1+2+\cdots+(2m-1)=m(2m-1).
\tag{25}
\]

On one fixed eventually `C`-critical branch,

\[
 a_{2m-1}<N_{2m}\leq C(2m)^2\log(4m)
\tag{26}
\]

for all sufficiently large dyadic `m`.  Since
`theta_m=1+O(1/m)`, (20), (25), and (26) give the two-sided size of the
certificate in (19):

\[
 \boxed{
 \frac14\sum_{m\in E}\log m-O(|E|)
 \leq U_E
 \leq
 \frac14\sum_{m\in E}\log m
 +O_C\!\left(\sum_{m\in E}\log\log(4m)+|E|\right).}
\tag{27}
\]

For `E={4,8,...,2^J}`,

\[
 U_E=\frac{\log2}{8}J^2+O_C(J\log J).
\tag{28}
\]

Thus the numerical upper certificate produced by **all** negative bulk
differences, globally rearranged across **all** selected epochs, is still
quadratic in the epoch depth.  It is far above the P15 target `o(log J)`.

Equation (28) does not say that `sum Y_m` is quadratic; it says the specified
Abel-boundary plus distinct-integer-spectrum proof cannot certify a better
upper bound.  A proof using extra algebraic coupling among interval sums may
still exist.

The missing leading quarter is localized precisely: it comes from the
lower-shell negative intervals

\[
 q=m-1,\qquad p=2,\ldots,m-2,
\]

whose weights are `(2ell+1)/(4m^2)`.  Mere global distinctness gives these
only `log m` worth of rank, not the `2 log m` needed to cancel the boundary.
Any continuation of the Abel route must couple this fan to future triangles,
to the positive boundary fans, or to a genuinely survival-conditioned state;
another independent use of integer distinctness cannot repair the quarter
deficit.

## 8. Counterexamples and quantifier audit

The following boundaries are rigorous and should not be blurred.

1. **Local critical windows do not vanish.**  The Wave 9 scaled
   Erdős--Turán rulers are actual finite Golomb rulers, satisfy one fixed
   recent-prefix critical constant, and have terminal scalar birth charge at
   least `1/2352` and retained cross-ratio birth potential at least `1/4096`.
   They refute any local `o(1)` strengthening of (11).  The ruler changes
   with the scale, so this is not an infinite counterexample.
2. **Full nonadjacent uniqueness is indispensable.**  The nested gaps
   `h_i=i` have critical quadratic diameter and distinct adjacent gaps, while
   their normalized rank variance tends to `1/18`; hence their dyadic state
   sum is linear in the number of epochs.  They are not Golomb because, for
   example, `h_1+h_2=h_3`.  This refutes only weakened hypotheses that omit
   nonadjacent contiguous-sum uniqueness.
3. **The cut constants are geometric, not survival theorems.**  Fine positive
   partitions show the `log 2` and `1/e` terms in Lemma 2 are separately
   sharp without the Golomb constraint.  No claim of simultaneous sharpness
   or Golomb realizability is made.
4. **The `7/4` law is theorem-level, not finite evidence.**  It follows from
   the exact coefficient multiset, dyadic threshold counting, rearrangement,
   and Stirling's formula.  The executable audit only guards the delicate
   boundary conventions.
5. **Survival remains unused.**  Theorems 1--5 hold for arbitrary finite
   Golomb prefixes.  Eventual criticality is used only in (26)--(28).  No
   step extracts extra force from the exact label `surv_C=infinity`; that is
   why P15 remains open.

## 9. Disposition and next exact lemma

Wave 10 does produce a uniform cross-epoch product/kernel statement:
fixed-location inverse-difference loads have the exponentially summable tail
(12).  It also upgrades W9-RLP from rectangular counts to arbitrary weights
and upgrades the cross-ratio shell to the hereditary log-product theorem
(17).  Neither estimate controls mass that continually migrates to the new
frontier.

The next admissible analytic target is now narrower:

> On one fixed infinite eventually `C`-critical Golomb branch, obtain a
> survival-conditioned coupling for the lower-shell fan in (15) that adds at
> least the missing `(1/4-o(1)) log m` per active scale to the bulk logarithmic
> floor, and then controls the secondary `log log m` boundary slack; or work
> directly with the retained `(D/N)^2` product kernel and prove that its
> frontier-migrating mass is `o(log J)`.

The first alternative must use more than the fact that the involved
differences are distinct positive integers: Theorem 5 already computes the
best leading order supplied by that information after global dyadic sorting.
The second must use more than pointwise old-region localization: scaled
Erdős--Turán windows already saturate a constant amount at a moving frontier.

No such survival-conditioned coupling is proved here.  Therefore P15,
Question 1, Question 2, Erdős Problem #1191, and the prize claim all remain
open.

## 10. Independent executable audit

The delicate shell coefficients were independently encoded in

- `core_workspace/endpoint_variance/wave10_laminar_triangle_check.py`;
- `core_workspace/endpoint_variance/test_wave10_laminar_triangle_check.py`.

The code evaluates the four indicator terms directly with
`fractions.Fraction`; it does not import a closed coefficient table from this
note.  The tests check, for `m=4,8,16,32,64`, the complete nonzero support,
all signs, the two positive masses, the full-span mass, the bulk mass, and
the exact multiset (16).  They also check that global rearrangement dominates
separate epoch floors and that the analytic entropy-rank upper bound dominates
the global floor.

Observed focused verification on 2026-08-29:

```text
13 passed
Ruff check: all checks passed
```

These finite checks are audit support only.  The displayed proofs establish
the quantified statements for all admissible scales.
