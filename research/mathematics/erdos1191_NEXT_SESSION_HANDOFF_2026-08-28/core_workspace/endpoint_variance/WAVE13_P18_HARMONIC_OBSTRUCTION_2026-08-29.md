# Wave 13 adversarial audit: the unavoidable harmonic floor in P18

Date: 2026-08-29  
Status: **P17 and P18 are direct contradiction reformulations, not smaller
packing lemmas; Erdős #1191 remains unresolved**

This note audits the Wave 12 target on one fixed normalized integer Golomb
ruler

\[
0=a_0<a_1<a_2<\cdots,
\qquad h_r=a_r-a_{r-1}.
\]

It proves an unconditional finite lower bound for the `new-birth` part of
`Z_m`.  Under an eventual critical cap, that lower bound is harmonic over
dyadic epochs.  Consequently, on any *actually existing* critical branch,
neither the P17 nor the P18 little-o conclusion can hold.  This does not
construct such a branch and does not disprove either universal statement:
if Question 1 is true, both statements are vacuously true.  Instead, it shows
that each universal little-o statement is already equivalent to Question 1
and must not be presented as a strictly easier intermediate packing lemma.

## 1. Index conventions

For dyadic `m>=4`, Wave 12 defines

\[
Z_m^{\rm nb}
=\sum_{j=m}^{2m-1}\sum_{i=m-1}^{j-2}
  \frac{(j-i)^2}{4m^2}C_{ij},
\tag{1}
\]

where

\[
C_{ij}
=\log\frac{D_{i,j-1}D_{i+1,j}}
              {D_{i+1,j-1}D_{i,j}},
\qquad
D_{p,q}=\sum_{r=p}^q h_r.
\tag{2}
\]

The relevant suffix gap set is

\[
G_m=\{m-1,m,\ldots,2m-1\}.
\tag{3}
\]

It has exactly `m+1` gap indices, not `m`.  Its total mass is

\[
H_m:=\sum_{r=m-1}^{2m-1}h_r
=a_{2m-1}-a_{m-2}.
\tag{4}
\]

Every unordered pair `i<j` in `G_m` with `j-i>=2` occurs exactly once in
(1): its right endpoint obeys `m<=j<=2m-1` and its left endpoint obeys
`m-1<=i<=j-2`.

Adjacent gaps of a Golomb ruler are distinct positive integers.  Indeed,
`h_i=h_j` for `i!=j` would repeat the positive difference represented by the
two one-gap intervals.

## 2. Cross-ratio product floor

For a pair in (1), put

\[
u=h_i,\qquad v=h_j,\qquad M=D_{i+1,j-1},
\qquad D=D_{i,j}=M+u+v.
\]

Then

\[
C_{ij}=\log\left(1+\frac{uv}{MD}\right)
\geq\frac{uv}{D^2}.
\tag{5}
\]

The last inequality is the exact Wave 9 product comparison.  Since the
interval `[i,j]` is contained in the suffix (3),

\[
D_{i,j}\leq H_m,
\qquad
C_{ij}\geq\frac{h_i h_j}{H_m^2}.
\tag{6}
\]

Therefore, with

\[
S_m:=\sum_{\substack{i<j\\i,j\in G_m\\j-i\geq2}}
       (j-i)^2h_i h_j,
\tag{7}
\]

we have

\[
Z_m^{\rm nb}\geq\frac{S_m}{4m^2H_m^2}.
\tag{8}

## 3. Layered distinct-gap lower bound

For each `k in G_m`, define

\[
Q_k:=\sum_{\substack{\ell\in G_m\\|\ell-k|\geq2}}
       |\ell-k|^2h_\ell.
\tag{9}
\]

Fix `2<=r<=m/2`.  At most `2r-1` indices of `G_m` have distance less than
`r` from `k`.  Hence

\[
F_{k,r}:=\{\ell\in G_m:|\ell-k|\geq r\}
\]

contains at least

\[
t_r=(m+1)-(2r-1)=m+2-2r
\tag{10}
\]

indices.  The corresponding gaps are distinct positive integers, so

\[
\sum_{\ell\in F_{k,r}}h_\ell
\geq1+2+\cdots+t_r=\frac{t_r(t_r+1)}2.
\tag{11}

For every integer distance `d>=2`,

\[
d^2\geq\sum_{r=2}^{\min(d,m/2)}(2r-1).
\tag{12}

All terms are nonnegative.  Interchanging the two finite sums in (9), then
using (10)--(12), gives the uniform bound

\[
\begin{aligned}
Q_k
&\geq
\sum_{r=2}^{m/2}(2r-1)
\sum_{\ell\in F_{k,r}}h_\ell\\
&\geq
E_m:=\sum_{r=2}^{m/2}(2r-1)
       \frac{(m+2-2r)(m+3-2r)}2.
\end{aligned}
\tag{13}
\]

Direct polynomial summation yields

\[
E_m=\frac{m(m-2)(m^2+8m+6)}{48}.
\tag{14}
\]

For `m>=4`,

\[
E_m-\frac{m^4}{48}
=\frac{m(6m^2-10m-12)}{48}\geq0.
\tag{15}

Every unordered pair in (7) occurs twice in
`sum_(k in G_m) h_k Q_k`.  Equations (4), (13), and (15) therefore give

\[
S_m
=\frac12\sum_{k\in G_m}h_kQ_k
\geq\frac{H_mE_m}{2}
\geq\frac{H_mm^4}{96}.
\tag{16}

Combining (8) and (16) proves the main finite theorem.

### Theorem 3.1 (unavoidable new-birth floor)

For every dyadic `m>=4` and every finite or infinite normalized integer
Golomb ruler containing `a_(2m-1)`, one has

\[
\boxed{
Z_m^{\rm nb}
\geq\frac{E_m}{8m^2H_m}
\geq\frac{m^2}{384H_m},
\qquad
H_m=a_{2m-1}-a_{m-2}.}
\tag{17}
\]

Only distinctness of the adjacent integer gaps was used in the layered
estimate.  Full contiguous-sum uniqueness was used only to guarantee that
adjacent gaps are distinct.

## 4. Harmonic lower bound on a hypothetical critical branch

Assume one fixed infinite normalized integer Golomb ruler satisfies

\[
a_n\leq Cn^2\log(2n)
\tag{18}
\]

eventually.  For every sufficiently large dyadic `m`,

\[
H_m\leq a_{2m-1}
\leq C(2m-1)^2\log(4m-2)
<4Cm^2\log(4m).
\tag{19}
\]

Thus (17) gives

\[
\boxed{
Z_m\geq Z_m^{\rm nb}
>\frac1{1536C\log(4m)}.}
\tag{20}
\]

The same lower bound holds for `Y_m`, because `Z_m^nb` is literally the
`i>=m-1` subtriangle of `Y_m` with the same coefficient:

\[
Y_m\geq Z_m^{\rm nb}.
\tag{21}
\]

Writing `m=2^k` and summing from the first admissible epoch through `2^J`,

\[
\begin{aligned}
\sum_{m\in E_J}Z_m
&\geq\frac1{1536C\log2}
       \sum_{k=k_0}^J\frac1{k+2},\\
\sum_{m\in E_J}Y_m
&\geq\frac1{1536C\log2}
       \sum_{k=k_0}^J\frac1{k+2}.
\end{aligned}
\tag{22}
\]

Consequently,

\[
\boxed{
\liminf_{J\to\infty}
\frac{\sum_{m\in E_J}Z_m}{\log J}
\geq\frac1{1536C\log2},
\qquad
\liminf_{J\to\infty}
\frac{\sum_{m\in E_J}Y_m}{\log J}
\geq\frac1{1536C\log2}.}
\tag{23}
\]

This is a conditional statement about any branch satisfying (18).  It does
not assert that such a branch exists.

## 5. Logical disposition of P17 and P18

Question 1 is equivalent to the nonexistence of any fixed infinite Golomb
ruler satisfying (18) for some finite `C`.

Consider the universal form of P17:

> for every fixed `C` and every fixed infinite branch satisfying (18),
> `sum_(m in E_J)Y_m=o_C(log J)`.

If Question 1 is true, this statement is vacuous.  Conversely, if this P17
statement were true and a critical branch existed, (23) would contradict its
conclusion.  Hence the universal P17 statement implies Question 1.  The two
statements are equivalent.

Exactly the same argument applies to the universal P18 statement with
`sum Z_m=o_C(log J)`.  Therefore

\[
\boxed{
\text{universal P17}\iff\text{Question 1}
\iff\text{universal P18}.}
\tag{24}
\]

Equation (24) is a reduction, not a proof of any of its three assertions.
In particular:

- no eventually critical infinite branch has been constructed;
- P17 and P18 have not been unconditionally disproved;
- Question 1 and Erdős #1191 remain unresolved; and
- no prize claim is justified.

The important correction is methodological.  P18 is not a smaller
`different-pair packing lemma` that can hold as a compatible property of a
surviving critical branch.  Its little-o conclusion is already a direct
contradiction certificate.

## 6. The terminal renewal tail cannot be discarded

Wave 12 proves

\[
\sum_{m\in E_J}Y_m
=R_4-R_{2^{J+1}}+\sum_{m\in E_J}Z_m.
\tag{25}
\]

Thus the exact signed restatement of P17 is

\[
\boxed{
\sum_{m\in E_J}Z_m-R_{2^{J+1}}=o_C(\log J),}
\tag{26}
\]

where the fixed constant `R_4` is absorbed by the little-o term.  The lower
bound (23) shows that if one studies a hypothetical critical branch, the
terminal tail must absorb harmonic `Z` mass.  Any argument that simply proves
`sum Z_m=o(log J)` has discarded the only channel capable of that absorption
and has jumped directly to the full contradiction.

Because (21) also gives a harmonic lower bound for `Y`, even (26) cannot hold
on an actually existing critical branch.  Proving (26) universally is another
form of proving Question 1, not an estimate expected to coexist with a
counterexample branch.

## 7. Exact integer-cell expansion and its limitation

There is a useful exact transformation that exposes where the integer lattice
enters.  For positive integers `M,u,v`, put

\[
\kappa(n):=\log\frac{(n+1)^2}{n(n+2)}
=\log\left(1+\frac1{n(n+2)}\right)>0.
\tag{27}
\]

Double telescoping gives

\[
\boxed{
\log\frac{(M+u)(M+v)}{M(M+u+v)}
=\sum_{x=0}^{u-1}\sum_{y=0}^{v-1}\kappa(M+x+y).}
\tag{28}
\]

Moreover,

\[
\frac1{(n+1)^2}\leq\kappa(n)\leq\frac1{n(n+2)}.
\tag{29}
\]

For `C_ij`, take `M=D_(i+1,j-1)`, `u=h_i`, and `v=h_j`.
Formula (28) is a genuine integer-lattice positive expansion.  It does not by
itself solve the packing problem: Golomb uniqueness controls the four corner
differences

\[
M,\quad M+u,\quad M+v,\quad M+u+v,
\]

but the internal integers `M+x+y` need not be interval differences.  Many
cells, within one rectangle and across different rectangles, may therefore
occupy the same level.  A successful use of (28) needs a multiplicity theorem
that retains the additive interval structure; corner ranks or numerical-hole
density alone are insufficient.

## 8. Finite Erdős--Turán suffix obstruction

There is also an explicit finite calibration.  Let `2m<=p<4m` be prime and

\[
b_r=2pr+[r^2]_p,
\qquad0\leq r<2m.
\tag{30}
\]

This is a finite Golomb ruler.  Its gaps exceed `p`, while for a new-birth
pair of rank distance `d=j-i`,

\[
D_{i,j}<p(2d+3).
\]

Hence

\[
C_{ij}>\frac1{(2d+3)^2}
\]

and

\[
Z_m^{\rm nb}
>\frac1{4m^2}\sum_{d=2}^m
  (m-d+1)\frac{d^2}{(2d+3)^2}
\geq\frac{m-1}{98m}.
\tag{31}
\]

The left side in fact has lower-limit at least `1/32` under this displayed
product bound.  Scaling all marks by an integer leaves every `C_ij` and every
`Z` coefficient unchanged.  With scale `s=ceil(log(2m))`, the terminal
diameter remains below `32m^2 log(2m)`, while the fraction of occupied
positive differences is at most `1/(4s)`.  Thus no terminal-scale estimate
that makes `Z_m` vanish solely with numerical difference occupancy can work.

This family changes with `m`, does not satisfy one uniform all-prefix cap,
and is not an infinite counterexample.

## 9. Executable audit

The companion files are

- `wave13_p18_harmonic_obstruction_probe.py`;
- `test_wave13_p18_harmonic_obstruction_probe.py`; and
- `wave13_p18_harmonic_obstruction_certificate_2026-08-29.json`.

The probe checks, using exact rational arithmetic:

- the `m+1` suffix-gap endpoint convention;
- the full product-floor sum over every new-birth pair;
- the diameter relaxation `D_(i,j)<=H_m`;
- the layered closed form (14) and the coarse constant in (17);
- all 1,146 bounded eight-mark all-prefix-`C=1` rulers;
- the authenticated 64-mark fixture and an independent 128-mark
  Erdős--Turán fixture; and
- the explicit finite Erdős--Turán suffix lower bound.

Floating logarithms are used only to check that observed `Z_m^nb` values lie
above the exact rational product floor.  They are not used in the theorem or
in any sign decision.

The correct next Route A statement must retain the signed terminal term in
(26) and must be advertised honestly as a Question 1-equivalent target.  A
genuinely smaller next lemma would have to quantify new all-contiguous-sum
information that forces the terminal-tail cancellation, rather than ask for
the impossible-on-survival separate decay of `Z` or `Y`.
