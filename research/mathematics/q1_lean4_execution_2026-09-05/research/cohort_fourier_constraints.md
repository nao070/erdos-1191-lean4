# Rank-boundary control and Fourier positivity of birth cohorts

Date: 2026-09-05. Author: `/root`, GPT-6 Astra Ultra.
Status: exact supporting constraints, not a resolution of original Q1.
No new Lean verification is claimed.

Let `A={a_1<a_2<...}` be an actual positive integer Sidon sequence,
including uniqueness of sums with repeated summands. Fix an integer `D>=1`.
There are at most `D` pairs of endpoints with positive difference at most
`D`, across the **entire** infinite sequence. Write this finite edge set as
`E_D={(i,j):i<j, a_j-a_i<=D}`. This is a use of actual difference
injectivity, not an assumption on a difference-counting model.

## 1. Exact amortized bound on labels crossing rank cuts

For a rank cut `k`, let

\[
 c_D(k)=|\{(i,j)\in E_D:i\le k<j\}|.
\]

Every edge `(i,j)` encloses `j-i+1` points of a Sidon set in an integer
interval of diameter at most `D`. Distinct positive differences imply

\[
 \binom{j-i+1}{2}\le D,\qquad j-i\le\sqrt{2D}.
\]

Counting the cuts crossed by each edge gives the finite identity and bound

\[
 \boxed{\quad
 \sum_{k\ge1}c_D(k)=\sum_{(i,j)\in E_D}(j-i)
                    \le\sqrt2 D^{3/2}.
 \quad}                                             \tag{1}
\]

In particular, any set of `L>=1` candidate cuts contains a cut `k` with

\[
 c_D(k)\le\sqrt2D^{3/2}/L.                          \tag{2}
\]

The sum in (1) is finite even when `A` is infinite: `E_D` has at most `D`
edges. No assumption about the largest rank where a short label is born
is needed.

For a fixed finite list `1/2<theta_1<...<theta_s<1`, take candidate cuts
in the rank interval beginning at `floor(D^theta_i)` of length
`L_i=floor(D^theta_i/log D)`. For all sufficiently large `D`, these
intervals are nonempty and disjoint. Choose cuts `k_i` by (2). They obey

\[
 k_i=D^{\theta_i}(1+O(1/\log D)),\qquad
 c_D(k_i)/D\le O(D^{1/2-\theta_i}\log D)=o(1).        \tag{3}
\]

Thus boundary labels can be controlled at finitely many selected rank
scales without assuming that a particular deterministic cut is good.

## 2. Cohort increments have a uniform Fourier lower bound

For a finite Sidon set `B` of size `m`, let

\[
 h_{B,D}(t)=\sum_{d\in\pm(\Delta B\cap[1,D])}
                  (1-|d|/D)e^{2\pi i d t}.
\]

The integer-window Gram identity, proved in
[short_three_sum_flux.md](short_three_sum_flux.md), is

\[
 m+h_{B,D}(t)
 =\frac1D\sum_{\ell\in\mathbb Z}
       \left|\sum_{b\in B\cap[\ell,\ell+D-1]}
                    e^{2\pi i b t}\right|^2\ge0.   \tag{4}
\]

Here the diagonal `m` is essential. Set `F_n=Delta P_n cap [1,D]` and
take ranks `u<v`. The new bank labels partition exactly as

\[
 F_v\setminus F_u
 =\bigl(\Delta\{a_{u+1},...,a_v\}\cap[1,D]\bigr)
   \ \dot\cup\
   \{a_j-a_i\le D:i\le u<j\le v\}.                 \tag{5}
\]

All labels in this partition have distinct endpoint pairs. The cross set
has size at most `c_D(u)`. The absolute value of its symmetric weighted
Fourier contribution is at most `2 c_D(u)`. Applying (4) to the actual
new block, of size `v-u`, proves, uniformly in real `t`,

\[
 \boxed{\quad h_{P_v,D}(t)-h_{P_u,D}(t)
              \ge-(v-u)-2c_D(u).\quad}              \tag{6}
\]

For consecutive selected cuts in (3), `v-u=O(D^theta_s)=o(D)` and
`c_D(u)=o(D)`. Hence

\[
 \inf_t\frac{h_{P_{k_{i+1}},D}(t)-h_{P_{k_i},D}(t)}D
 \ge-o(1).                                         \tag{7}
\]

This is a constraint on each birth cohort, not just on the terminal bank.
No claim is made that a difference of two arbitrary positive-semidefinite
matrices is positive-semidefinite. The cross-boundary error in (6) is what
justifies the limiting statement.

## 3. A precise limiting interpretation and its continuity requirement

The labels of each bank define subprobability measures
`D^(-1) sum_(d in F_n) delta_(d/D)` on `[0,1]`. One can pass to a subsequence
of `D` using the joint measures of physical label `d/D` and logarithmic
birth rank `log(tau(d))/log D`, restricted to `[0,b]` for a fixed exponent
`b<1` larger than all exponents under consideration. Their total mass is
at most one. A weak limit is a positive
measure; its rank marginal has at most countably many atoms.

At a rank exponent `theta` at which the limiting rank marginal has no
atom, restricting that joint measure to birth exponents at most `theta`
defines a limiting physical bank measure `nu_theta`. A selected cut from
(3) has logarithmic rank tending to the same `theta`, so its bank has this
same limit. This follows by squeezing between restrictions at
`theta-epsilon` and `theta+epsilon`, then letting `epsilon` decrease to
zero. The absence of an atom is necessary for that argument.

For two such continuity exponents `alpha<beta` in `(1/2,1)`, substitute
`t=xi/D` into (7) and use weak convergence against the continuous function
`2(1-x)cos(2 pi xi x)`. It follows that

\[
 \boxed{\quad
 2\int_0^1(1-x)\cos(2\pi\xi x)\,
                  d(\nu_\beta-\nu_\alpha)(x)\ge0
 \quad\text{for every real }\xi.\quad}              \tag{8}
\]

The measures themselves are nested. Equation (8) additionally says that
every such cohort's symmetrized triangularly weighted profile has a
nonnegative Fourier transform. One must not assert that a small relative
change in rank automatically changes only `o(D)` labels; (3) alone does
not imply this. The continuity-exponent restriction handles that issue.

If the fixed-onset critical cap holds, the weighted density lower bound
in [fixed_width_bank_density.md](fixed_width_bank_density.md) is uniform
in exponent on compact subintervals. It therefore survives these selected
cuts and this limiting interpretation. Its hypotheses are not replaced by
moving-onset finite caps.

## 4. Why this additional positivity is still only a constraint

A spatially constant bank-density profile with increasing scalar density
`b(theta)` satisfies (8): its cohort transform is

\[
 [b(\beta)-b(\alpha)]
       \left(\frac{\sin(\pi\xi)}{\pi\xi}\right)^2\ge0,
\]

with the value at zero defined by continuity. This is the Fourier transform
of the triangular function. It shows that (8) alone cannot exclude all
nonzero increasing density profiles. Such a profile is an abstract
relaxation, not an actual integer Sidon sequence or a construction of one.

The unresolved issue is a constraint that simultaneously retains these
cohort profiles, the endpoint realization, and the same physical labels
when the width `D` changes. The preceding exact estimates do not provide
a new independent source budget at each width. Original Q1 remains
unresolved.
