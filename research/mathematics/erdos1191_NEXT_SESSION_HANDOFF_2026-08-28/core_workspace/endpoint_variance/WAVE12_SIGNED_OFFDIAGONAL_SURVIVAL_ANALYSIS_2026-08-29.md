# Wave 12: cut-renewal positivity, containment-floor saturation, and the integer-lattice boundary

Date: 2026-08-29  
Status: **new exact renewal identity and two rigorous no-go theorems; P17 remains open**

This note continues from Wave 11.  It uses the same fixed infinite normalized
Golomb ruler

\[
0=a_0<a_1<a_2<\cdots,
\qquad D_{p,q}=a_q-a_{p-1},
\]

the same positive cross ratios

\[
C_{ij}=\log\frac{D_{i,j-1}D_{i+1,j}}
                       {D_{i+1,j-1}D_{i,j}}>0,
\qquad j-i\geq2,
\]

and the same dyadic birth energy

\[
Y_m=\sum_{j=m}^{2m-1}\sum_{i=1}^{j-2}
       \left(\frac{j-i}{2m}\right)^2 C_{ij}.
\tag{1}
\]

No finite ruler below is promoted to an infinite branch.

## 1. Outcome and claim boundary

Three exact conclusions were obtained.

1. **Positive cut-renewal theorem.**  The Wave 11 future cut tail

   \[
   R_m:=\sum_{i=1}^{m-2}\left(\frac{m-i}{2m}\right)^2
                      \sum_{j=m}^{\infty}C_{ij}
   \tag{2}
   \]

   satisfies

   \[
   \boxed{Y_m=R_m-R_{2m}+Z_m,\qquad Z_m\geq0,}
   \tag{3}
   \]

   where `Z_m` is the sum of four explicit nonnegative sectors.  Unlike
   `R_m`, the future coefficients in `Z_m` are geometrically summable for
   each fixed pair.  Thus the `Theta(log(j/i))` same-pair overlap obstruction
   from Wave 11 is removed at the coefficient level.

2. **Full containment-floor saturation theorem.**  Combine simultaneously:

   - the global numerical rank of every bulk difference;
   - the triangular length floor `D>=binom(ell+1,2)`; and
   - the complete partial order coming from interval containment.

   Even the optimal floor using all three inputs exceeds the Wave 11 length
   floor by only `O(1)` per dyadic epoch.  Consequently this entire class of
   independent cross-length allocation arguments cannot repay the secondary
   `sum log log m` envelope in P17.

3. **Explicit real-Golomb countermodel.**  The real marks

   \[
   a_n=n^2+\sqrt2\,n
   \tag{4}
   \]

   have all positive differences distinct and have quadratic growth, but

   \[
   Y_m\longrightarrow
   \frac32\left(\log2-\frac12\right)>0.
   \tag{5}
   \]

   Hence full difference uniqueness, order, quadratic growth, and the exact
   signed cross-ratio kernel do not imply P17 over the reals.  A successful
   proof must use the integer lattice (unit spacing or a genuinely equivalent
   arithmetic fact), not uniqueness as an abstract order property.

These are structural advances, not a resolution.  P15, P17, Questions 1 and
2, and the prize claim remain open.

## 2. Exact four-sector cut renewal

Define the following four quantities.  Empty index ranges contribute zero.

\[
\begin{aligned}
Z_m^{\rm ob}
&=\sum_{j=m}^{2m-1}\sum_{i=1}^{m-2}
 \frac{(j-i)^2-(m-i)^2}{4m^2}C_{ij},\\
Z_m^{\rm nb}
&=\sum_{j=m}^{2m-1}\sum_{i=m-1}^{j-2}
 \frac{(j-i)^2}{4m^2}C_{ij},\\
Z_m^{\rm of}
&=\sum_{j=2m}^{\infty}\sum_{i=1}^{m-2}
 \frac{i(4m-3i)}{16m^2}C_{ij},\\
Z_m^{\rm mf}
&=\sum_{j=2m}^{\infty}\sum_{i=m-1}^{2m-2}
 \frac{(2m-i)^2}{16m^2}C_{ij}.
\end{aligned}
\tag{6}
\]

Put

\[
Z_m=Z_m^{\rm ob}+Z_m^{\rm nb}+Z_m^{\rm of}+Z_m^{\rm mf}.
\tag{7}
\]

Every coefficient in (6) is nonnegative.  In the first line this follows
from `j>=m`; in the third it follows from `1<=i<=m-2`, hence
`4m-3i>0`.  The other two cases are immediate.

### Theorem 2.1 (coefficientwise cut renewal)

For every dyadic `m>=4`, on every fixed infinite Golomb branch,

\[
Y_m=R_m-R_{2m}+Z_m.
\tag{8}
\]

#### Proof

It is enough to compare the coefficient of each `C_(i,j)`.

- If `m<=j<=2m-1` and `i<=m-2`, the coefficient in
  `Y_m-R_m` is

  \[
  \frac{(j-i)^2-(m-i)^2}{4m^2},
  \]

  which is the first line of (6).
- If `m<=j<=2m-1` and `i>=m-1`, only `Y_m` occurs, giving the
  second line.
- If `j>=2m` and `i<=m-2`, the coefficient in `-R_m+R_(2m)` is

  \[
  \left(\frac{2m-i}{4m}\right)^2
  -\left(\frac{m-i}{2m}\right)^2
  =\frac{i(4m-3i)}{16m^2},
  \]

  which is the third line.
- If `j>=2m` and `m-1<=i<=2m-2`, only `R_(2m)` occurs, giving
  the fourth line.

All other coefficients are zero.  This proves (8) coefficientwise.  The
positive series converge because each `R_m` is the finite Wave 11 boundary
slack represented by its exact future telescope.  ∎

Summing (8) over `E_J={4,8,...,2^J}` gives the exact telescope

\[
\boxed{
\sum_{m\in E_J}Y_m
=R_4-R_{2^{J+1}}+\sum_{m\in E_J}Z_m.}
\tag{9}
\]

Therefore

\[
\sum_{m\in E_J}Z_m=o(\log J)
\tag{10}
\]

is a new sufficient condition for P17.  It is deliberately stated as
sufficient, not equivalent: the terminal positive tail in (9) must not be
silently discarded in the reverse direction.

### 2.2 What the renewal fixes, and what it does not

For a fixed pair `(i,j)`, the old-future coefficient obeys

\[
0\leq\frac{i(4m-3i)}{16m^2}\leq\frac{i}{4m}.
\tag{11}
\]

Its sum over dyadic `m` is geometric.  The middle-future condition
`m-1<=i<=2m-2` holds at only a bounded number of dyadic cuts.  The two birth
sectors occur only at the unique dyadic band containing `j`.  Thus every
fixed pair has uniformly bounded total `Z` coefficient.  This is exactly the
property that failed for the raw future tails `R_m`.

This does **not** prove (10).  There are infinitely many different pairs, and
neither the critical diameter cap nor pairwise coefficient summability yet
gives an arithmetic packing bound for their total cross-ratio mass.  The next
argument must use integer spacing across different pairs on one surviving
branch.

## 3. The strongest rank-length-containment floor still has only constant gain

Let `B_J` be the union of all Wave 11 negative-bulk interval atoms over
`E_J`, and write `ell(e)`, `beta(e)`, and `D_e` for an atom's length,
coefficient, and integer difference.  Put

\[
L_\ell=\binom{\ell+1}{2}.
\tag{12}
\]

All `D_e` are globally distinct.  If `r(e)` is the numerical rank of `D_e`,
then

\[
D_e\geq r(e),\qquad D_e\geq L_{\ell(e)}.
\tag{13}
\]

Moreover, if interval `f` is properly contained in interval `e`, positivity
of the gaps gives `D_f<D_e`; hence the actual rank order is a linear extension
of the complete containment poset.

Let `Lin(B_J)` be all bijections from `B_J` to `{1,...,|B_J|}` that are linear
extensions of that poset, and define

\[
K_J^{\rm inc}
=\min_{\sigma\in\operatorname{Lin}(B_J)}
  \sum_{e\in B_J}\beta(e)
  \log\max\{\sigma(e),L_{\ell(e)}\}.
\tag{14}
\]

The actual rank assignment is feasible, so (13) proves

\[
A_J\geq K_J^{\rm inc}\geq K_J^{\rm len}.
\tag{15}
\]

### Theorem 3.1 (containment-floor saturation)

Uniformly over finite consecutive dyadic epoch sets,

\[
\boxed{0\leq K_J^{\rm inc}-K_J^{\rm len}<5|E_J|.}
\tag{16}
\]

#### Proof

Order endpoint bands by increasing epoch `m`; within one band order atoms by
nondecreasing interval length.  This is a full containment linear extension.
Indeed, proper containment gives both `q_f<=q_e` and
`ell(f)<ell(e)`.  The right-endpoint bands are consecutive and increasing,
so either `f` is in an earlier band or the strict length order puts it first.

The number of all bulk atoms through epoch `m` is exactly

\[
B(m)=\sum_{q=3}^{2m-2}(q-1)=2m^2-5m+2<2m^2.
\tag{17}
\]

Thus every epoch-`m` atom in this witness gets rank below `2m^2`.  Since
`ell<=2m-3` and hence `L_ell<2m^2`, the witness exceeds the length floor by at
most

\[
\Delta_m
=\sum_{e\in\mathcal I_m}\beta(e)
  \log\frac{2m^2}{L_{\ell(e)}}.
\tag{18}
\]

The exact coefficient classes from Wave 11 give the following elementary
bounds for `m>=4`.

- Length one contributes at most `1`, using
  `log(2m^2)<=m`.
- Length two contributes at most `1/2`.
- The lower-band lengths `3<=ell<=m-2` contribute at most

  \[
  \frac38\log4+\frac34.
  \]

- The interior lengths `3<=ell<=m-1` contribute at most

  \[
  \frac12\log4+1.
  \]

- The interior lengths `m<=ell<=2m-3` contribute at most

  \[
  \frac14\log4.
  \]

For the two sums used here,

\[
\ell\log(m/\ell)\leq m-\ell,
\qquad
\sum_{\ell=1}^{m}\log(m/\ell)
\leq m-1,
\tag{19}
\]

the first inequality is `log x<=x-1`, and the second follows from
`log(m!)>=int_1^m log x dx`.  Adding the five displayed bounds gives less
than `5`.  Therefore `Delta_m<5`; using the constructed linear extension in
(14) proves (16).  ∎

The theorem includes the *entire* containment poset, not merely the local
rank lower bound `r>=L_ell`.  Its scope is also exact: it rules out proofs
whose only inputs are integer ranks, triangular floors, and monotone
containment.  It does not rule out crossing-interval additive relations,
unit-spacing packing between different interval sums, or survival coupling.

## 4. A quadratic real Golomb ruler with nondecaying birth energy

The next example identifies an indispensable arithmetic boundary.

### Proposition 4.1 (real uniqueness is insufficient)

Let

\[
a_n=n^2+\sqrt2\,n\qquad(n\geq0).
\tag{20}
\]

Then all positive differences `a_j-a_i`, `j>i`, are distinct, but (5)
holds.

#### Proof of difference uniqueness

Suppose

\[
a_j-a_i=a_\ell-a_k,
\qquad j>i,\quad \ell>k.
\]

Separating rational and irrational parts gives

\[
j-i=\ell-k,
\qquad j^2-i^2=\ell^2-k^2.
\]

The first equality supplies the same positive factor in the second, hence
`j+i=ell+k`.  Solving the sum and difference equations gives
`(j,i)=(ell,k)`.  Thus (20) is a Golomb ruler over the reals.  It also has
`a_n=n^2+O(n)`.

#### Proof of the limit

Put

\[
r=j-i,
\qquad s=i+j-1+\sqrt2.
\]

Direct factorization of the four differences gives

\[
C_{ij}
=\log\left(\frac{r^2}{r^2-1}\frac{s^2-1}{s^2}\right)
=\log\frac{1-s^{-2}}{1-r^{-2}}.
\tag{21}
\]

For `i/m->x` and `j/m->y`, with `1<=y<=2` and `0<=x<=y`, the summand in
(1), multiplied by `m^2`, converges to

\[
\frac14\left(1-\frac{(y-x)^2}{(y+x)^2}\right)
=\frac{xy}{(x+y)^2}.
\tag{22}
\]

There is a uniform Riemann-sum majorant.  Since `s>r>=2`,

\[
0<C_{ij}
\leq-\log(1-r^{-2})
\leq\frac1{r^2-1},
\]

and consequently

\[
0\leq\left(\frac r{2m}\right)^2C_{ij}
\leq\frac1{3m^2}.
\tag{23}
\]

The omitted diagonal strip has vanishing normalized area, so dominated
Riemann convergence applies.  Therefore

\[
\begin{aligned}
\lim_{m\to\infty}Y_m
&=\int_1^2\int_0^y\frac{xy}{(x+y)^2}\,dx\,dy\\
&=\int_1^2 y\,dy\int_0^1\frac{t}{(1+t)^2}\,dt\\
&=\frac32\left(\log2-\frac12\right)>0.
\end{aligned}
\tag{24}
\]

This proves the proposition.  ∎

Along dyadic epochs, the cumulative energy of this real ruler is
`Theta(J)`, not `o(log J)`.  The model is **not** an integer Golomb ruler and
is not a counterexample to Erdős #1191.  Its role is adversarial: any proposed
P17 proof that remains valid after replacing the integers by the reals has
omitted an essential hypothesis.

## 5. Certified finite audit

The companion program
`wave12_cut_renewal_probe.py` has two independent exact oracles.

1. It compares rational pair-coefficient maps for
   `Z_m=Y_m-R_m+R_(2m)` before substituting any ruler.
2. It substitutes integer Golomb rulers and compares canonical rational
   formal-log sums.

The certificate records:

- zero coefficient or formal-log failures on all 1,146 eight-mark all-prefix
  `C=1` rulers;
- exact renewal rows on authenticated/project fixtures and an independent
  128-mark Erdős--Turán ruler;
- a 32,130-atom containment witness through epoch 128;
- containment-witness gain `8.311509216376606` across six epochs, with every
  single-epoch gain below `5`; the looser theorem-level `2m^2` cap totals
  `12.664550630632174`, also with every epoch below `5`;
- the labelled real-model value
  `Y_1024=0.2893858160837208`, approaching the exact limit
  `0.28972077083991793`.

The finite certificate's internal digest and its file SHA-256 are different
by design: the internal digest hashes the payload before inserting its own
field, while the file digest hashes the final pretty-printed JSON.

## 6. Exact next lemma

The strongest next Route A target exposed by Wave 12 is:

> **Integer renewal packing lemma.**  On every fixed infinite normalized
> Golomb ruler satisfying `a_n<=C n^2 log(2n)` eventually, prove
> `sum_(m in E_J) Z_m=o_C(log J)`, where the four nonnegative sectors of
> `Z_m` are exactly (6).

By (9), this lemma implies P17.  It has three advantages over the raw future
tail formulation: no signed cancellation, uniformly summable same-pair
coefficients, and an explicit real countermodel forcing the proof to expose
where integer unit spacing enters.  A proof still has to control the number
of *different* pairs; pairwise summability alone is not enough.

Route B remains separate.  No equivalence between this renewal lemma and a
product-tree embedding theorem is claimed.
