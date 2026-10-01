# Route C: universal actual-Haar star cover

Date: 2026-08-30  
Status: `UNIVERSAL_ACTUAL_STATE_COVER_AND_COEFFICIENT_OPTIMALITY_PROVED_PHYSICAL_PAYMENT_OPEN`

This note gives a geometry-independent root-Laplacian correction for the
direct ordered-`B` matrix on every actual same-scale Haar cell.  Its total
root coefficient is optimal among corrections required to work on every
abstract ordered Haar state.  Its exact physical price is also explicit.

The result is a feasibility baseline, not the missing paid multiscale ledger.
Without an active-scale gate its low-scale dyadic price diverges, and the
fixed-fixture prices below are much larger than the membership-adaptive
optima in C086--C087.  Thus C058, both Erdős questions, novelty, publication,
and every prize claim remain open.

## 1. Direct matrix and actual Haar states

Use the physical point coordinates of C079.  For one Wave epoch `n>=3`, the
ordered current-block endpoints are `b_0<...<b_n`, and

\[
 M_n=D^{\mathsf T}B_nD,
 \qquad
 (B_n)_{ij}=
 \begin{cases}
 -(j-i)^2/(8n^2),&|i-j|\ge2,\\
 0,&|i-j|\le1.
 \end{cases}
 \tag{1.1}
\]

Put

\[
 g_T=\mathbf 1_{[0,T)}-\mathbf 1_{[T,2T)}.
\]

At a fixed spatial point `x`, the translated state

\[
 v(x)=(g_T(x-b_0),\ldots,g_T(x-b_n))
\]

always has the ordered form

\[
 \boxed{v=0^\ell(-1)^b(+1)^c0^d.}
 \tag{1.2}
\]

Indeed, the `-1` coordinates are the marks in `(x-2T,x-T]`, and the `+1`
coordinates are the marks in `(x-T,x]`.  Either sign block may be empty.
The half-open convention only assigns endpoints to one adjacent cell; it does
not change (1.2).

## 2. The universal star

Let

\[
 w_n={n-1\over8n^2}
\]

and define the endpoint-to-interior graph Laplacian

\[
 \boxed{
 C_n^\star=w_n\sum_{k=1}^{n-1}
 \bigl[(e_0-e_k)(e_0-e_k)^{\mathsf T}
      +(e_k-e_n)(e_k-e_n)^{\mathsf T}\bigr].}
 \tag{2.1}
\]

It has `2(n-1)` roots and total root mass

\[
 \sum_{i<j}w_{ij}={ (n-1)^2\over4n^2}.
 \tag{2.2}
\]

### Theorem 2.1

For every `n>=3` and every state of the form (1.2),

\[
 \boxed{v^{\mathsf T}C_n^\star v\ge v^{\mathsf T}M_nv.}
 \tag{2.3}
\]

Moreover, (2.2) is the least possible total root mass among all graph
Laplacians

\[
 C=\sum_{i<j}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T},\qquad w_{ij}\ge0,
\]

that satisfy (2.3) for every abstract ordered Haar state.

### Proof of domination

If both sign blocks are empty, then `v=0` and both quadratic forms vanish.
Assume from now on that at least one sign block is nonempty.

First suppose only one sign block is nonempty.  If it is an internal interval
of length `s`, C079 gives

\[
 v^{\mathsf T}M_nv={s^2\over4n^2}
\]

for `s>=2` and zero for `s=1`.  The star energy is

\[
 v^{\mathsf T}C_n^\star v
 ={(n-1)s\over4n^2}\ge{s^2\over4n^2},
\]

because `s<=n-1`.  If the block touches an endpoint, its direct energy is
zero, so there is nothing to prove.

Now suppose both sign blocks are nonempty, with lengths `b,c>=1`.
If their union is internal, then

\[
 Dv=e_{\ell-1}-2e_{\ell+b-1}+e_{\ell+b+c-1}.
\]

Using (1.1) exactly, including the zero adjacent entries,

\[
 4n^2v^{\mathsf T}M_nv
 =(b-c)^2-2\mathbf1_{b=1}-2\mathbf1_{c=1}.
 \tag{2.4}
\]

Both endpoints of `v` vanish, so

\[
 4n^2v^{\mathsf T}C_n^\star v=(n-1)(b+c).
\]

Since `b+c<=n-1`,

\[
 (b-c)^2\le(b+c)^2\le(n-1)(b+c),
\]

which proves this case.

If the support touches the left endpoint but not the right, the direct energy
is `c^2/(2n^2)` for `c>=2` and zero for `c=1`, while

\[
 v^{\mathsf T}C_n^\star v
 ={(n-1)(n-1+4c)\over8n^2}.
\]

The required inequality is

\[
 (n-1)(n-1+4c)-4c^2
 =(n-1)^2+4c(n-1-c)\ge0.
\]

The right-endpoint case is identical with `b` in place of `c`.  If both
endpoints are touched, `Dv` has only its middle coefficient `-2`; the zero
diagonal of `B_n` makes the direct energy zero.  This exhausts (1.2).

### Proof of coefficient optimality

Test any universal graph-Laplacian cover on the actual Haar state

\[
 u=\mathbf1_{\{1,\ldots,n-1\}}.
\]

C079 gives

\[
 u^{\mathsf T}M_nu={(n-1)^2\over4n^2}.
\]

For a root `(i,j)`, `(u_i-u_j)^2` is either zero or one.  Consequently

\[
 u^{\mathsf T}Cu
 =\sum_{(i,j)\text{ crossing }\{1,\ldots,n-1\}}w_{ij}
 \le\sum_{i<j}w_{ij}.
\]

Every universal cover therefore has total root mass at least (2.2), while
the star attains it.  This proves optimality without LP duality or a limiting
argument.

## 3. Exact physical price

For `d>=0`, C086 gives

\[
 \chi_T(d)=
 \begin{cases}
 3d/T,&d\le T,\\
 4-d/T,&T\le d\le2T,\\
 2,&d\ge2T.
 \end{cases}
\]

Hence the star's normalized physical Haar price is exactly

\[
 \boxed{
 P_n^\star(T)={n-1\over8n^2}
 \sum_{k=1}^{n-1}
 \left[\chi_T(b_k-b_0)+\chi_T(b_n-b_k)\right].}
 \tag{3.1}
\]

Summing the cellwise inequality (2.3) with weight `|cell|/(2T)` proves
physical feasibility and reproduces (3.1) exactly.  No coefficient trace is
used in this step.

The five exact fixture prices are:

| epoch and width | star price | fixed-fixture optimum from C086--C087 |
|---|---:|---:|
| `n=4,T=200` | `207/640` | `29/200` |
| `n=8,T=200` | `5173/12800` | `139/3200` |
| `n=4,T=2000` | `2097/6400` | `299/2000` |
| `n=8,T=2000` | `52423/128000` | `1489/32000` |
| `n=16,T=2000` | `46431/102400` | `1477/128000` |

This gap is informative: coefficient-mass optimality under every abstract
Haar state is much stronger than membership-adaptive optimality on the cells
of one geometry and scale.

## 4. Mandatory active-scale gate

If every star-root distance is at least `2T`, each root has physical cost
`chi_T=2`.  Therefore

\[
 \boxed{P_n^\star(T)={(n-1)^2\over2n^2}>0.}
 \tag{4.1}
\]

This value persists at all sufficiently small dyadic widths.  Thus an
ungated sum over every low scale diverges even though the direct Wave demand
is eventually zero.  The `n=4,T=1` certified fixture gives `P_4^star=9/32`.

Equation (4.1) closes only the ungated use of the universal star.  It does
not rule out activating it only on the exact direct-`B` support, choosing a
membership-adaptive cover, transporting root prices across epochs or phases,
or using a larger signed mixed-scale master.

## 5. Verification and claim boundary

The companion generator exhausts all 5,820 distinct abstract states for
`2<=n<=16`, with no failed inequality and the sharp witness for every
`3<=n<=16`.  It also replays every actual half-open cell in the five fixtures,
checks the root-cost and cell-sum physical objectives agree, and rejects ten
semantic or overclaim mutations.

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_universal_haar_star_cover_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  universal_haar_star_cover_certificate.py \
  --verify universal_haar_star_cover_certificate.json --self-check
```

The theorem supplies a universal feasible actual-state cover and a sharp
coefficient-mass benchmark.  It does **not** pay (3.1), choose the legal
active gates, control continuum phase or terminals, prove the C058
single-ledger inequality, or resolve Erdős Problem #1191.
