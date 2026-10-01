# Exact mathematical content of the C143 V2 pilot

Date: 2026-09-05. Status: **fixed-history externally certified theorem; not Lean verified here; no Q1 resolution**.

This note extracts the predicates from `c142/master.py`, `c143/geometry.py`,
`oracle/c143_independent_oracle.py`, and the strengthened follow-up
`c143_full_pricing_replay.py`. It does not repeat the main agent's bank/provenance
audit or upgrade a saved replay to a kernel proof.

## 1. Fixed input and literal indexing

The only ruler quantified over in the pilot is this zero-based tuple:

```
(0,36,81,122,173,220,283,316,350,388,452,505,540,602,634,693,
4095,7451,12926,17572,21700,25568,30684,35152,41335,46551,
50437,55826,62050,66475,72003,77562,77721,77811,77934,78049,
78177,78347,78494,78581,78687,78843,78978,79110,79275,79435,
79568,79717,79816,79923,80086,80195,80322,80448,80551,80667,
80801,80963,81000,81164,81310,81338,81390,81712).
```

Write these marks as `a_0,...,a_63` and set `n=16`. The old epoch uses
`a_15,...,a_31` and the new epoch uses `a_31,...,a_63`. Their spans are
`H_old=76869` and `H_new=4150`. The channel set is

\[
 I=\{(r,m):15\le r\le63,\ m\in\{1,2,4,8\}\},\qquad |I|=196.
\]

It is ordered first by `m`, then by `r`, exactly as in the source. The full
graph-root universe is every unordered pair of distinct channels,
`R={{i,j}:i<j}`, of size 19,110. No rank-distance restriction is imposed.

The phase band is

\[
 b=H_{new}/16=2075/8,\qquad t\in[b,2b].
\]

For real `x` define the half-open Haar states

\[
 q_{r,m}(x,t)={8\over m}
 (1_{[a_r,a_r+mt)}(x)-1_{[a_r+mt,a_r+2mt)}(x)).
 \tag{1}
\]

There are nine disjoint owner groups covering `I`:

* `G_0={(15,m):m=1,2,4,8}`;
* `G_(16,m)={(r,m):16≤r≤31}` for each of the four multipliers;
* `G_(32,m)={(r,m):32≤r≤63}` for each multiplier.

In particular the shared direct endpoint `a_31` is assigned to the old
epoch. The preceding endpoint `a_15` is assigned to `G_0`. Direct-demand
coordinate sets contain both endpoints even though owner sets omit their
left endpoint.

## 2. Exact direct matrices, demands and graph prices

For `e∈{16,32}`, let `D_e` be the `e×(e+1)` difference matrix with row
`i` equal to `u_i-u_(i+1)`. Put

\[
 (B_e)_{ij}=\begin{cases}0,&|i-j|\le1,\\
 -(i-j)^2/(8e^2),&|i-j|\ge2,\end{cases}
 \qquad M_e=D_e^TB_eD_e.
 \tag{2}
\]

The local state `q_(e,m)` means the `e+1` entries at ranks
`e-1,...,2e-1`, not the owner group alone. With `w_16=1`, `w_32=ρ`, define

\[
 d_{e,m,\rho}(x,t)=w_e{m\over128}
 q_{e,m}(x,t)^TM_eq_{e,m}(x,t),
 \qquad
 D_\rho(t)=\int_{\mathbb R}\sum_{e,m}d_{e,m,\rho}(x,t)\,dx.
 \tag{3}
\]

For nonnegative root weights `λ=(λ_ij)` let

\[
 X_\lambda=\sum_{i<j}\lambda_{ij}(u_i-u_j)(u_i-u_j)^T,
 \quad
 E_\lambda(x,t)=q(x,t)^TX_\lambda q(x,t),
 \quad P_\lambda(t)=\int_{\mathbb R}E_\lambda(x,t)\,dx.
 \tag{4}
\]

Its owner share is

\[
 S_{G,\lambda}(x,t)
 =\sum_{i<j}\lambda_{ij}
 (1_G(i)q_i-1_G(j)q_j)(q_i-q_j)
 =q^T\Pi_GX_\lambda q.
 \tag{5}
\]

The certified feasibility conditions are exactly

\[
 S_{G_0,\lambda}\ge0,\qquad
 S_{G_{e,m},\lambda}\ge\max(d_{e,m,\rho},0)
 \quad\text{for every }x\in\mathbb R.
 \tag{6}
\]

Because the groups partition the channels, `Σ_G S_G=E_λ` pointwise. This
is an identity for this supplied owner map; it does not construct owners on
an arbitrary sequence of overlapping epoch pairs.

## 3. The fixed-history local theorem

**Externally certified assertion, conditional on the exact replay of the
hash-bound bank.** There is a Borel measurable function

\[
 \lambda:[b,2b]\longrightarrow\mathbb Q_{\ge0}^{19110}
\]

with finite image such that, simultaneously for every
`ρ∈[97/100,1]` and every real `t∈[b,2b]`, (6) holds and

\[
 2D_\rho(t)-P_{\lambda(t)}(t)
 \ge {6975267967\over7664025600}>0.
 \tag{7}
\]

For `ρ=1`, the same selection satisfies the stronger bound

\[
 2D_1(t)-P_{\lambda(t)}(t)
 \ge {18976473121\over3065610240}.
 \tag{8}
\]

The lower bounds on the signed phase integrals are

\[
 \int_b^{2b}(2D_\rho-P_\lambda)\,{dt\over t^2}
 \ge {6975267967\over3975713280000}
 \quad(97/100\le\rho\le1),
 \tag{9}
\]

and at weight one the sign-aware logarithmic enclosure gives

\[
 {4694333\over10^8}
 <\int_b^{2b}(2D_1-P_\lambda)\,{dt\over t^2}
 <{4694335\over10^8}.
 \tag{10}
\]

For each `t`, `λ(t)` minimizes `P_λ(t)` over the full feasible graph-root
cone at `ρ=1`. Optimality at `ρ<1` is not asserted. The graph does not depend
on `ρ`: decreasing `ρ` decreases each new owner right-hand side
`max(ρd,0)`, and

\[
 2D_\rho-P_\lambda=(2D_1-P_\lambda)-2(1-\rho)D_{new}.
 \tag{11}
\]

The source checks the affine extremes of (11) at `ρ=97/100,1` and at all
child limits and collapsed endpoints. This supplies the full rectangle,
including either sign of `D_new`, by two successive affine interpolations.

## 4. Why a continuum follows from finitely many rational checks

Every event line is `x=a_r+smt`, with `s=0,1,2`. All intersections in the
phase band are rational. Their 961 distinct phases cut the band into 960
geometry parents. Inside a parent the order of distinct event lines is
constant. Every spatial cell state is consequently constant, every cell
length is affine in `t`, all gate coefficients and right-hand sides are
rational constants, and `D` and every root objective are rational affines.

The bank subdivides these parents into 1,890 children. On each child its
primal root weights are rational constants. The replay checks all owner
gates directly and checks affine primal-dual equality. Its nonnegative dual
variables are affine in `t`; every one of the 19,110 reduced costs is affine.
Checking their signs at both child ends proves dual feasibility for the
entire child by convex interpolation. Weak duality plus equality proves
optimality there.

The collapsed geometry at each parent endpoint is certified separately:
coincident event lines are merged and zero-length cells discarded. Its
optimal price may be lower than a limiting generic price. Choose these
endpoint certificates there and a fixed adjacent child's certificate at any
interior child boundary. This is a finite piecewise constant Borel selector.
At a spatial event point the half-open state equals the state in the cell
immediately to its right (or the zero state after the final event), so the
cellwise gates imply (6) for all `x`, not just almost every `x`.

On a child `[L,R]`, write its physical margin as `β+αt`. Its integral is

\[
 \beta(1/L-1/R)+\alpha\log(R/L).
 \tag{12}
\]

The saved enclosure bounds `log u` by the rational atanh series with
`z=(u-1)/(u+1)` and the positive geometric remainder
`2z^(2N+1)/((2N+1)(1-z²))`. Negative `α` swaps lower and upper bounds.
Finite endpoint changes do not alter this integral.

## 5. Honest enlarged quantifiers and remaining boundaries

Translation and positive dilation give a genuine immediate corollary. For
any real `c`, `s>0`, use marks `c+sa_r`, phase `t∈[sb,2sb]`, and selector
`λ(t/s)`. Under `x=c+sy`, all states and gates are unchanged, `D` and `P`
scale by `s`, so the pointwise floors (7),(8) scale by `s` and the integrals
(9),(10) are unchanged. Restrict to integer dilations and suitable integer
translations if integer positive Sidon rulers are desired. This is only the
homothetic family of this fixed shape, not all histories.

For `ρ=m²/(m+1)²`, (7) applies at every integer `m≥66`. The alternative
variable `s=J+1-k` has `m=s-1`, hence requires `s≥67`.

No theorem here quantifies over arbitrary `n`, ruler shapes, C116 windows,
critical towers or horizons. No global source pays (4) merely because a
local feasible graph exists. The old same-atom terminal is nonzero, and
the complete Wave mass is not the four-scale demand. With `Q_e` the
nonnegative box-tent density and `W_e=∫_0^∞Q_e`, the literal normalization is

\[
 \int_b^{2b}D_e(t){dt\over t^2}
 =W_e-\int_0^bQ_e+\int_b^{2b}Q_e
 -2\int_{16b}^\infty Q_e+\int_{32b}^\infty Q_e.
 \tag{13}
\]

The negative old terminal and nonzero lower-cutoff terms remain in any
global use. The theorem extracted here is not the requested Q1 theorem.

## Source identity

Primary directory:
`/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/`.
Follow-up directory:
`/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/`.

Expected bank byte SHA-256:
`d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`.
Saved producer payload SHA-256:
`3961c6caa68c9d5dfbfbc0fdd2e433a1cf310618584ef617a892ce9b79a6725c`.
Canonicalization in the actual producer/oracle is JSON with sorted keys,
separators `(',', ':')`, `ensure_ascii=False`, with the `integrity` field
removed. The main task owns current identity/provenance verification.
