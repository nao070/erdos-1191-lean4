# Wave 13: exact frontier spectrum and the signed-repayment boundary

Date: 2026-08-29 (Asia/Tokyo)  
Status: **rigorous structural reduction; no resolution of Erdős #1191**

This note continues the Wave 12 cut-renewal identity on one fixed infinite
normalized integer Golomb ruler.  It does not assume that an eventually
critical branch exists.  Whenever that hypothesis is invoked, the conclusion
is conditional and is not an example of such a branch.

Write

\[
D_{p,q}=a_q-a_{p-1},\qquad
C_{ij}=\log\frac{D_{i,j-1}D_{i+1,j}}
                    {D_{i+1,j-1}D_{i,j}},
\]

and retain the Wave 12 identity

\[
Y_m=R_m-R_{2m}+Z_m,\qquad Z_m\geq0.
\tag{1}
\]

The purpose of this note is to expand `Z_m` into a finite signed spectrum of
interval logarithms.  It shows that one whole boundary channel cancels up to
a dyadically summable error.  The only surviving within-epoch upper problem
is a terminal-suffix fan versus its interior descendants.

## 1. Finite log spectrum

For `m>=4`, put `A=D_(1,2m-1)=a_(2m-1)`.  Define the following five
quantities.  These Gothic letters are local to this note and are not the
Wave 11 channels with similar Roman names.

\[
\begin{aligned}
\mathfrak P_m
&=\sum_{q=m}^{2m-2}\frac{2q-1}{4m^2}\log D_{1,q},\\
\mathfrak B_m
&=\sum_{q=m}^{2m-2}\left(
  \sum_{p=2}^{q-2}\frac{1}{2m^2}\log D_{p,q}
  +\frac{1}{4m^2}\log D_{q-1,q}
  +\frac{1}{m^2}\log D_{q,q}\right),\\
\mathfrak U_m
&=\sum_{p=2}^{2m-3}\frac{12m-5-6p}{16m^2}
       \log D_{p,2m-1}
  +\frac{11}{16m^2}\log D_{2m-2,2m-1},\\
\mathfrak F_m
&=\frac{12m^2-28m+15}{16m^2}\log A,\\
\mathfrak e_m
&=\frac{1}{4m^2}\log D_{2m-1,2m-1}.
\end{aligned}
\tag{2}
\]

Empty sums are zero.  Every displayed coefficient is nonnegative.

### Theorem 1.1 (exact frontier spectrum)

For every dyadic `m>=4`,

\[
\boxed{Z_m=\mathfrak P_m+\mathfrak U_m-
             \mathfrak B_m-\mathfrak F_m-\mathfrak e_m.}
\tag{3}
\]

Equivalently, before grouping the terms, the nonzero coefficient of
`log D_(p,q)` is as follows.

For `m<=q<=2m-2`:

\[
\begin{array}{c|c}
(p,q)&\text{coefficient}\\ \hline
p=1&(2q-1)/(4m^2)\\
2\le p\le q-2&-1/(2m^2)\\
p=q-1&-1/(4m^2)\\
p=q&-1/m^2.
\end{array}
\tag{4}
\]

For `q=2m-1`:

\[
\begin{array}{c|c}
(p,2m-1)&\text{coefficient}\\ \hline
p=1&-(12m^2-28m+15)/(16m^2)\\
2\le p\le2m-3&(12m-5-6p)/(16m^2)\\
p=2m-2&11/(16m^2)\\
p=2m-1&-1/(4m^2).
\end{array}
\tag{5}
\]

#### Proof

The Wave 11 finite boundary form is

\[
R_t=\sum_{i=1}^{t-2}\left(\frac{t-i}{2t}\right)^2
 \bigl(\log D_{i,t-1}-\log D_{i+1,t-1}\bigr).
\tag{6}
\]

Substitute `Z_m=Y_m-R_m+R_(2m)` from (1), and in every summand of `Y_m`
substitute

\[
C_{ij}=\log D_{i,j-1}+\log D_{i+1,j}
       -\log D_{i+1,j-1}-\log D_{i,j}.
\tag{7}
\]

For a nonterminal right endpoint, the interior coefficients are the constant
mixed second difference `-1/(2m^2)`.  The two short-interval boundary cases
give `-1/(4m^2)` and `-1/m^2`, while the left boundary first difference is
`(2q-1)/(4m^2)`.  At `q=2m-1`, collecting the final `Y_m` terms with
the two terms from each summand of `R_(2m)` gives the four cases in (5).
This is (3).  No inequality or convergence interchange is used.  ∎

## 2. Exact coefficient masses

Let `P_m,B_m,U_m,F_m` denote the sums of the coefficients in the
corresponding Gothic terms of (2).  Direct finite summation gives

\[
\begin{aligned}
P_m=B_m&=\frac{3(m-1)^2}{4m^2},\\
U_m&=\frac{12m^2-28m+19}{16m^2},\\
F_m&=\frac{12m^2-28m+15}{16m^2}.
\end{aligned}
\tag{8}
\]

The total positive and negative masses agree exactly:

\[
P_m+U_m=B_m+F_m+\frac1{4m^2}
=\frac{24m^2-52m+31}{16m^2}.
\tag{9}
\]

Two small mass imbalances will be used below:

\[
P_m-F_m=\frac{4m-3}{16m^2},\qquad
B_m-U_m=\frac{4m-7}{16m^2}.
\tag{10}
\]

Thus the interior bulk has slightly more coefficient mass than the terminal
suffix fan, even though its interval values are smaller.

## 3. A whole boundary channel is summably removable

Every prefix interval in `mathfrak P_m` is contained in the full interval, so
`D_(1,q)<=A`.  Also the final singleton is a positive integer, hence
`mathfrak e_m>=0`.  Equations (3), (8), and (10) therefore imply

\[
\mathfrak P_m-\mathfrak F_m
\leq\frac{4m-3}{16m^2}\log A
\tag{11}
\]

and the one-sided frontier inequality

\[
\boxed{
0\leq Z_m\leq X_m+\varepsilon_m,
\quad X_m:=\mathfrak U_m-\mathfrak B_m,
\quad \varepsilon_m:=\frac{4m-3}{16m^2}\log A.}
\tag{12}
\]

In particular `X_m>=-epsilon_m`.  If
`a_n<=C n^2 log(2n)` eventually, then

\[
\varepsilon_m=O_C\!\left(\frac{\log m}{m}\right),
\qquad
\sum_{m\in\{4,8,\ldots\}}\varepsilon_m<\infty.
\tag{13}
\]

Consequently the negative parts of `X_m` have finite dyadic sum, and

\[
\sum_{m\in E_J}Z_m
\leq\sum_{m\in E_J}(X_m)_+ +O_{C,\mathbf a}(1).
\tag{14}
\]

This proves the following strictly localized sufficient target:

> If, on a hypothetical eventually `C`-critical branch,
> `sum_(m in E_J)(X_m)_+=o_C(log J)`, then P18 follows.

This target is not claimed equivalent to P18.  The discarded
`mathfrak P_m-mathfrak F_m-mathfrak e_m` term has only a one-sided bound.

## 4. Interaction with the integer new-birth barrier

The separate Wave 13 new-birth theorem proves, with

\[
H_m=a_{2m-1}-a_{m-2},
\]

that every integer Golomb prefix satisfies the two separate bounds

\[
Y_m\geq Z_m^{\rm nb}\geq\frac{m^2}{384H_m},
\qquad
Z_m\geq Z_m^{\rm nb}\geq\frac{m^2}{384H_m}.
\tag{15}
\]

Under an eventual critical cap this gives

\[
Y_m,Z_m\geq\frac{1}{1536C\log(4m)}
\tag{16}
\]

for every sufficiently large dyadic `m`.  Combining (12) and (16) also
localizes the same obstruction in the suffix frontier:

\[
X_m\geq\frac{1}{1536C\log(4m)}
        -O_C\!\left(\frac{\log m}{m}\right).
\tag{17}
\]

Therefore

\[
\sum_{m\in E_J}X_m
\geq\frac{1}{1536C\log2}\log J-O_{C,\mathbf a}(1).
\tag{18}
\]

So the terminal suffix fan necessarily beats its interior descendants by a
harmonic amount on any hypothetical critical branch, despite the small
coefficient-mass advantage `B_m-U_m>0`.  A within-epoch positive packing
cannot make this frontier sparse.  Any proof along this route would have to
derive an upper estimate that contradicts (18), and would thereby already
resolve Question 1.

## 5. The exact signed target and claim boundary

Summing (1) over `E_J={4,8,...,2^J}` gives

\[
\sum_{m\in E_J}Y_m
=R_4-R_{2^{J+1}}+\sum_{m\in E_J}Z_m.
\tag{19}
\]

Thus the exact terminal-tail-faithful algebraic restatement of P17 is the
signed repayment

\[
\sum_{m\in E_J}Z_m-R_{2^{J+1}}=o_C(\log J).
\tag{20}
\]

The constant `R_4` is absorbed by the little-oh notation.  Equation (20) is
not proved here.  Moreover (15)--(16) show that both P17's
`sum Y_m=o(log J)` and P18's `sum Z_m=o(log J)` are incompatible with the
existence of an eventually critical integer branch.  After universally
quantifying over every `C>0` and every fixed branch satisfying that cap, each
little-oh assertion is therefore equivalent to Question 1:

- if Question 1 holds, there is no branch in its hypothesis, so the assertion
  is vacuous;
- if either assertion is proved and Question 1 is false, the branch supplied
  by the negation contradicts (16).

This equivalence is a reformulation, not a proof of Question 1.  No infinite
critical branch and no counterexample to Erdős #1191 has been constructed.
For one fixed `C`, the corresponding statement is equivalent only to the
nonexistence of a branch obeying that particular `C`-cap.

The next useful attack is not another independent interval-order floor.  It
must either obtain a genuinely cross-epoch upper bound contradicting the
suffix-frontier lower bound (18), or replace Route A by an arithmetic product
embedding that retains the same integer obstruction.
