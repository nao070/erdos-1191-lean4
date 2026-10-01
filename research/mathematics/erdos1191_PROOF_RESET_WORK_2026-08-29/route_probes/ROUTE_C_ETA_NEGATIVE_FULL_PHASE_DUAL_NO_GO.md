# Route C: eta-negative exact full-phase dual no-go

Date: 2026-08-31  
Status: `EXACT_FINITE_ETA_NEGATIVE_FULL_PHASE_NO_GO_C058_OPEN`

This note records a finite exact obstruction to using only the normalized
shell-span increment

\[
 \eta_k=\log\frac{H_{k+1}}{4H_k}
\]

as the history-sensitive payment in the current four-width independent
epoch-block cone.  The obstruction has a negative `eta` and a negative best
full-phase margin.  It does not construct an eventual critical infinite
history and does not refute C058.

## 1. Exact finite Golomb and envelope fixture

Take

\[
 (a_0,\ldots,a_{15})=
 (0,26,60,77,110,175,326,519,529,543,566,622,724,933,1349,2178).
\]

All 120 positive differences are distinct.  With the canonical convention

\[
 N_m=a_{m-1}-a_0+1\le 2C\,m^2\log m,
\]

the finite dyadic rows satisfy the `C=2` cap:

| `m` | `N_m` | required lower bound for `log m` |
|---:|---:|---:|
| 4 | 78 | `39/32` |
| 8 | 520 | `65/32` |
| 16 | 2179 | `2179/1024` |

The past and current shell spans are

\[
 H_2=a_7-a_3=442,\qquad H_3=a_{15}-a_7=1659.
\]

Hence

\[
 \exp(\eta_2)=\frac{1659}{4\cdot442}
 =\frac{1659}{1768}<1,
 \qquad \eta_2<0.
\]

This is a finite envelope audit only.  No eventual infinite `C=2` ray is
constructed.

## 2. Full log-phase model

Use the same four multipliers `1,2,4,8`, half-open Haar sign convention,
aggregate owner rows, and zero-row-sum independent epoch-block PSD cone as in
C112 and C114.  The past block owns ranks 3 through 7.  The current demand
uses ranks 7 through 15 while the current block owns ranks 8 through 15, so
the shared rank 7 remains assigned to the past block.

At the worst retained Fejér ratio `rho=9/16`, take the full factor-two phase

\[
 \frac{1649}{8}\le t\le\frac{1649}{4}.
\]

The 78 affine event lines produce 88 exact rational breakpoints and 87
gap-free chambers.  On each chamber the integrated physical-price matrix is
affine in `1/t`.

## 3. Exact chamberwise dual proof

For each of the 87 chambers and each epoch, the certificate stores one
nonnegative rational dual vector with 308 integer weights and denominator
`100000`.  There are 174 vectors and 53,592 stored weights in total.

For every chamber endpoint the verifier reconstructs

\[
 S(t)=H(t)-\sum_r y_rA_r
\]

and proves it positive definite by a fraction-free exact
Bareiss/Sylvester calculation.  This gives 348 exact endpoint checks.  Since
`S` is affine in `1/t` and `1/t` ranges between its endpoint values, convexity
covers the complete chamber interior.  Weak SDP duality therefore gives an
upper bound for every feasible phasewise margin in the stated cone.

The verifier recomputes every dual objective and every constant/`1/t` demand
coefficient.  It integrates the resulting upper bound against `dt/t` using a
20-term rational atanh expansion with an explicit positive tail.  Sign-aware
choice of the upper or lower logarithm enclosure proves

\[
 \int_{1649/8}^{1649/4}\Phi(t)\,\frac{dt}{t}< -\frac1{40}.
\tag{1}
\]

The strengthened replay encloses the dual upper integral `I` and `log 2`
separately by rational atanh bounds:

\[
 -\frac{13913}{500000}<I<-\frac{139}{5000},\qquad
 \frac{693}{1000}<\log2<\frac{139}{200}.
\]

Consequently its normalized upper satisfies the sharper exact interval

\[
 -\frac{81}{2000}<\frac{I}{\log2}< -\frac1{25}.
\tag{1.1}
\]

Thus every feasible normalized full log-phase average in the stated cone is
strictly below `-1/25`.  The floating value `-0.040143...` is explanatory
only; (1) and (1.1) are replayed entirely with integers and rational numbers.

## 4. Consequence for the bare eta bridge

At `k=2`, an error-free inequality of the proposed form

\[
 \overline\Phi_2\ge
 \frac{\epsilon-A\eta_2}{3},
 \qquad \epsilon\ge0,\ A\ge0,
\tag{2}
\]

would have a nonnegative right-hand side because `eta_2<0`.  Equation (1)
shows that every feasible correction in this exact independent epoch-block
cone has negative full-phase average.  Therefore (2) cannot hold uniformly
over all finite `C=2`-envelope-compatible 16-mark Golomb geometries in this
cone.

The missing information is visible in the gaps.  The past shell is

`(33,65,151,193)`,

whereas the current shell is

`(10,14,23,56,102,209,416,829)`.

Although the total normalized span decreases, the current shell is internally
near-geometric.  The scalar `eta` forgets this load-bearing shape.

## 5. Exact scope boundary

This certificate does **not** refute:

- a theorem asserted only for sufficiently large `k`;
- an error `e_k` large enough to absorb this finite `k=2` row;
- an eventual infinite critical Sidon history;
- a larger cone with cross-epoch or other global Gram corrections;
- a different legal owner convention;
- C058, Q1, Q2, publication novelty, or prize eligibility.

The strongest honest next target is a storage/dissipation inequality with an
additional bounded nonanticipating gap-profile potential `V`:

\[
 \overline\Phi_k\ge \frac{\epsilon-A\eta_k
 -B(V_{k+1}-V_k)}{k+1}-e_k.
\tag{3}
\]

Its Fejér-weighted signed increments must telescope in the complete C103
ledger, and its local analytic proof must still construct one global owner
system rather than invoking automatic block stitching.

## 6. Reproduction

From `route_probes/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_certificate.py \
  --verify ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_certificate.json \
  --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_test.py
```

The canonical verifier uses only the Python standard library.  It performs no
numerical optimization and imports neither CVXPY nor NumPy.  It also validates
the canonical JSON bytes, strict scope gates, SHA-256 integrity, and 12
semantic mutations.

Payload SHA-256:
`176cc369f21e9002945e4716b66a1a58a1e358e5e92c03572ae00039c2e01b16`.

Canonical source and JSON file SHA-256 values are respectively
`a8ce48b6170000d373bb2f297d85d4474b6c03345054c8892966080a8e4ee790`
and
`331da5cdf1e553c65cace050ffc2ac2ae2dee847f949e2b932aceaa43dafd55f`.
