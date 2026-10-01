# Cyclic Arc Kernel, Critical Dyadic Functional, and Obstructions

**Date:** 2026-08-28 (Asia/Tokyo)  
**Global status:** `UNRESOLVED_AT_HARD_LIMIT`  
**Wave:** 1, Target A with a fixed-modulus Target C byproduct

This note continues the canonical endpoint-imbalance work. It proves an exact
pair-pair kernel and isolates the precise signed upper-budget lemma that would
advance Question 1. It also records counterexamples that rule out the obvious
positivity, monotonicity, and unconditional-budget variants.

## 1. Exact cyclic-arc covariance

`[RIGOROUS — SELF-CONTAINED]`

Let `p=(a,b)` and `q=(c,d)` be short pairs modulo `N`, with

\[
L=b-a,\qquad M=d-c,\qquad 1\le L,M<N.
\]

Their bad-offset arcs are

\[
B_p=\{a+1,\ldots,a+L\}\pmod N,
\qquad
B_q=\{c+1,\ldots,c+M\}\pmod N.
\]

Put

\[
x=[c-a]_N\in\{0,\ldots,N-1\},
\qquad u_+=\max(u,0).
\]

After translating `a` to zero, cutting the second arc at its possible wrap
gives

\[
\boxed{
I_N(L,M;x)
=(L-x)_+-(L-x-M)_+
 +(x+M-N)_+-(x+M-N-L)_+ .
}
\]

Therefore the unnormalized covariance is

\[
\boxed{
K_N(p,q)=|B_p\cap B_q|-\frac{|B_p||B_q|}{N}
=I_N(L,M;x)-\frac{LM}{N}.
}
\]

The formula includes all wrap and endpoint-equality cases. Exhaustive tests
compare it with literal residue-set intersection for every start and every
nonempty proper arc at moduli `2<=N<=12`.

### Resistance representation

Define the unit-cycle effective-resistance kernel

\[
\Phi_N(t)=\frac{r(N-r)}N,
\qquad r=[t]_N.
\]

Then

\[
\boxed{
K_N((a,b),(c,d))
=\frac12\bigl(
\Phi_N(a-d)+\Phi_N(b-c)
-\Phi_N(a-c)-\Phi_N(b-d)
\bigr).
}
\]

Indeed, the centered arc indicator has cyclic derivative `e_a-e_b`.
Applying the inverse cycle Laplacian and polarizing gives the formula. The
implementation verifies the overlap and resistance formulas agree exhaustively
for every start and arc length at moduli `2<=N<=17`.

### Sign structure

`[RIGOROUS — SELF-CONTAINED]`

- Nested arcs have positive covariance.
- Disjoint arcs have covariance `-LM/N<0`.
- If neither contains the other and their union is the full cycle, then

  \[
  K_N=-\frac{(N-L)(N-M)}N<0.
  \]

- Partial crossing does not determine the sign. In the nonwrapping case
  `x<L<x+M`,

  \[
  K_N=L-x-\frac{LM}{N},
  \]

  which can be positive, zero, or negative.

The first sign test deliberately used `(N,L,M,x)=(17,9,4,7)` as a supposed
positive crossing. Exact evaluation returned `-2/17`, refuting that test
expectation. Replacing `x=7` by `x=6` gives `15/17`. This is retained as an
audit reminder that cyclic order alone is insufficient.

Cauchy--Schwarz gives

\[
|K_N(p,q)|
\le
\sqrt{L(1-L/N)M(1-M/N)}
\le \frac N4.
\]

## 2. Exact quartic expansion

`[RIGOROUS — SELF-CONTAINED]`

For `P=P_N(A)`,

\[
C_N(r)=\sum_{p\in P}1_{B_p}(r),
\qquad
\overline C_N=\frac1N\sum_{p\in P}|B_p|.
\]

Expanding the square before applying inequalities gives

\[
\boxed{
N\operatorname{Var}C_N
=\sum_{p,q\in P}K_N(p,q).
}
\]

Equivalently,

\[
N\operatorname{Var}C_N
=\sum_{p\in P}\frac{L_p(N-L_p)}N
+2\sum_{\{p,q\}\subset P}K_N(p,q).
\]

For prefixes `A_{m_j}`, moduli `N_j`, and weights `w_j`, let a global pair
`p=(a_u,a_v)` have length `L_p`, and similarly `q=(a_s,a_t)`. Then

\[
\sum_{j\le J}w_j\operatorname{Var}C_{N_j}(A_{m_j})
=\sum_{p,q}\Gamma_J(p,q),
\]

where the exact boundary terms are

\[
\boxed{
\Gamma_J(p,q)
=\sum_{j\le J}\frac{w_j}{N_j}
1_{\{\max(v,t)\le m_j\}}
1_{\{L_p,L_q<N_j\}}
K_{N_j}(p,q).
}
\]

The first indicator is the prefix-birth condition; the second is the
short-pair condition. Omitting either silently changes the functional.

## 3. Critical dyadic functional

`[RIGOROUS — SELF-CONTAINED]` for the lower bound; `[CONDITIONAL]` for the
upper lemma.

Take

\[
m_j=2^j,
\qquad N_j=D_{m_j}+1,
\qquad w_j=m_j^{-3},
\]

and define

\[
\mathcal F_J(A)
=\sum_{j=j_0}^{J}\frac{\operatorname{Var}C_{N_j}(A_{m_j})}{m_j^3}.
\]

Assume for contradiction that, eventually,

\[
a_m\le C m^2\log m.
\]

Then eventually `N_j<=2 C m_j^2 log(m_j)`. The mandatory-level theorem gives

\[
\frac{\operatorname{Var}C_{N_j}(A_{m_j})}{m_j^3}
\ge
\frac{(m_j^2-1)(m_j^2+11)}
     {360C\,m_j^4\log m_j}.
\]

Consequently,

\[
\boxed{
\mathcal F_J(A)
\ge
\frac{1+o(1)}{360C\log 2}\log J.
}
\]

The power `m^{-3}` is critical for this dyadic argument: an additional fixed
factor `m^{-epsilon}` makes the forced sum converge.

For every fixed ordered pair-pair interaction whose first eligible scale is
`s`,

\[
\sum_{j\ge s}\frac{w_j}{N_j}|K_{N_j}(p,q)|
\le \frac14\sum_{j\ge s}m_j^{-3}
=\frac{2}{7m_s^3}.
\]

The entire diagonal contribution is absolutely summable:

\[
\sum_j\frac{w_j}{N_j}\sum_pK_{N_j}(p,p)
\le\sum_j\frac1{8m_j}<\infty.
\]

However, `O(m_s^4)` off-diagonal interactions may be born near scale `m_s`;
absolute summation loses `O(m_s)` and is useless. The logarithmic lower gain is
therefore necessarily a net signed off-diagonal phenomenon.

### Surviving candidate lemma

`[CONDITIONAL]`

The following is a clean sufficient little-`o` statement for this functional:

> **Critical-density signed quartic budget.** For every `C>0` and fixed `j_0`,
> there is an explicit `B_{C,j_0}(J)=o(log J)`, independent of the ruler, such
> that every compatible finite Sidon ruler whose dyadic prefixes satisfy
> `D_{m_j}+1<=2 C m_j^2 log(m_j)` for every `j_0<=j<=J` obeys
> `F_J(A)<=B_{C,j_0}(J)`.

An `O(log J)` upper bound supplies only another fixed constant and is not
enough. No `o(log J)` budget is proved here.

## 4. Fixed-modulus prefix second difference

`[RIGOROUS — SELF-CONTAINED]`

Set `A_0` to the empty set, and for `m>=1` let

\[
A_M=\{a_1<\cdots<a_M\},\qquad D_M<N,
\]

and keep this same `N` for every prefix. Let `C_m` be the crossing-load vector
of `A_m={a_1,...,a_m}`; thus `C_0=C_1` is identically zero. For `2<=m<=M`,

\[
\boxed{
C_m-2C_{m-1}+C_{m-2}
=(m-1)1_{(a_{m-1},a_m]}.
}
\]

For a phase in the final gap `(a_k,a_{k+1}]`, the prefix load is zero for
`m<=k` and is `k(m-k)` for `m>k`. Its second prefix difference is therefore
the single impulse asserted above.

After centering `f_m=C_m-mean(C_m)` and writing `g_{m-1}=a_m-a_{m-1}`,

\[
f_m-2f_{m-1}+f_{m-2}
=(m-1)\left(1_{(a_{m-1},a_m]}-\frac{g_{m-1}}N\right),
\]

so, for the normalized `L^2` norm on the cycle,

\[
\left\|f_m-2f_{m-1}+f_{m-2}\right\|_2^2
=(m-1)^2\frac{g_{m-1}}N
\left(1-\frac{g_{m-1}}N\right).
\]

The uncentered impulses have disjoint supports. The centered impulses for
distinct gaps have explicit negative covariance. This identity retains one
common offset space across prefixes, but for `N>D_M` it reconstructs exactly
the already-known gap profile. By itself it supplies no Sidon-specific upper
budget; a useful continuation must introduce shorter moduli, length slices, or
another mechanism.

## 5. Exact zero modes and refutations

### Complementary two-cycle

`[REFUTED]`

For `A={0,1,N}` at modulus `N`, the two short arcs are complementary. Their
two positive diagonal terms cancel their two negative cross terms exactly.
This refutes the proposed lower bound obtained by retaining the positive
diagonal terms and discarding the cross terms, as well as prefix monotonicity.

### A genuine three-cycle Sidon zero mode

`[RIGOROUS — SELF-CONTAINED]`

\[
A=\{0,3,7,12\},\qquad N=6
\]

is Sidon, with positive differences `{3,4,5,7,9,12}`. Its only short edges
are

\[
0\to3,\qquad3\to1,\qquad1\to0,
\]

of lengths `3,4,5`. Their bad-offset arcs cover every residue exactly twice,
so the variance is zero. Distinct edge lengths do not prevent a longer
Eulerian zero mode.

### Covariance sign can flip when the modulus doubles

`[REFUTED]`

For the Sidon ruler `A={0,1,3,7}` and pairs `p=(0,3)`, `q=(1,7)`,

\[
K_8(p,q)=-\frac14,
\qquad
K_{16}(p,q)=\frac78.
\]

Divisibility or nesting of moduli does not preserve the sign of an individual
interaction.

### One dominant gap can suppress variance

`[RIGOROUS — SELF-CONTAINED]`

For `G>=3`,

\[
A_G=\{0,1,G+1,G+3\},\qquad N=G+4
\]

is Sidon and has

\[
\boxed{
\operatorname{Var}C_N(A_G)=\frac{19G+27}{(G+4)^2}\longrightarrow0.
}
\]

Thus a dominant central gap, even though it carries the maximal split level,
does not force large variance.

### Unconditional raw-variance budget is false

`[RIGOROUS — SELF-CONTAINED]` for the construction; `[REFUTED]` for the
unconditional budget.

There is an infinite sparse Sidon sequence with diameter-regime variance
`Omega(m^4)` on every stage of a dyadic subsequence. Start with a normalized
`h`-mark Sidon ruler `A` contained in `[0,D]`, with `min(A)=0`, `max(A)=D`, and
`h>=2`. Choose `M>D` and set

\[
P_h=\{2^i-1:0\le i<h\},
\qquad G=M(2^{h-1}-1),
\]

\[
T=D+2G+1,
\qquad A^+=A\cup(T+MP_h).
\]

The set `P_h` is Sidon: if
`2^j-2^i=2^{j'}-2^{i'}`, the 2-adic valuations give `i=i'`, and then
`j=j'`. Old differences are below `M`, new internal differences are
nonzero multiples of `M`, and all cross differences exceed `G`. Equality of
two cross differences would give

\[
M(P_i-P_j)=a-a',
\]

whose right side has absolute value at most `D<M`; both sides must vanish.
Hence `A^+` is Sidon.

At the `2h`-mark stage, a central gap of length `2G+1` has load `h^2`, while
a final gap of length `M2^{h-2}>G/2` has load `2h-1`. With
`N=D(A^+)+1<=5G`, the two-group variance identity gives

\[
\operatorname{Var}C_N(A^+)\ge\frac{(h-1)^4}{25}.
\]

Iteration gives the claimed infinite union. Therefore an unconditional

\[
\sum_{j\le J}m_j^{-3}V_j=o(\log J)
\]

is false. The critical-envelope hypothesis in the surviving lemma is
essential.

### Homometric off-diagonal sign separation

`[RIGOROUS — SELF-CONTAINED]`

For the certified homometric rulers at `N=14`, the common diagonal sum is
`65/2`. Their ordered off-diagonal sums are respectively `7` and `-5`.
Thus the distinct-pair contribution need not be nonnegative and cannot be an
exact nonnegative function of the difference spectrum.

## 6. Literature position

`[LITERATURE STATUS — PUBLIC RECORD ONLY]`

The identity is an elementary instance of inverse-Laplacian/effective-
resistance theory on a cycle, and the homometric ruler pair itself is
classical. Searches through Firecrawl, Exa, SciSpace, public specialist-site
indexes, and exact formulas did not locate the complete arc-covariance plus
Sidon multiscale formulation. This is only a preliminary negative search. No
novelty claim is made without a fuller zbMATH/MathSciNet and expert audit.

## 7. Reproduction

From `core_workspace/endpoint_variance/`, with `pytest` installed:

```text
python -m pytest -q test_multiscale_variance.py
```

Expected result at this checkpoint:

```text
8 passed
```

Implementation and exhaustive oracle tests:

- `multiscale_variance.py`
- `test_multiscale_variance.py`
- `TDD_MULTISCALE_RED_2026-08-28.log`
- `TDD_MULTISCALE_GREEN_2026-08-28.log`

## 8. Highest-value next lemma

The surviving target is the critical-density signed off-diagonal budget

\[
\mathcal F_J(A)=o(\log J).
\]

It must exploit the critical envelope, or a consequence that excludes the
sparse construction, and likely group the signed kernels by endpoint
quadruple, birth shell, or another structure that forces cancellation.
Absolute-value estimates, diagonal-only truncation, and termwise sign
preservation under doubled moduli are ruled out. Aggregate nested-modulus
identities and other unconditional functionals remain open; only the specific
unconditional raw-variance budget above is refuted.
