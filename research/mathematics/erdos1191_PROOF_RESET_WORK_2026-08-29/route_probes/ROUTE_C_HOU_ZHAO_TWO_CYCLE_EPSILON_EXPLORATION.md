# Route C: two-cycle epsilon interval and boundary-QP exploration

**Status:** exact finite-
`F(N)` exploration for one pinned eight-kernel family.  This memo makes no
global-optimality, novelty, prize, or Erdős Problem #1191 claim.  It does not
modify or supersede the finalized four-file perturbation certificate.

The exact replay is
[`hou_zhao_two_cycle_epsilon_exploration.py`](hou_zhao_two_cycle_epsilon_exploration.py).
It pins the same Hou--Zhao v2 source commit and SHA-256 as the finalized
certificate.  The signed off-diagonal theorem remains the project-internal
generalized master lemma in
[`ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md`](ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md),
not a theorem attributed to Hou--Zhao.

## 1. Full feasible epsilon interval

Keep the finalized row-sum-zero direction

\[
J_{12}=-1, J_{14}=2, J_{17}=-1, J_{28}=1,
J_{45}=-1, J_{48}=-1, J_{57}=1
\]

and put `H(e)=diag(lambda)+eJ`.  Coordinates 3 and 6 are isolated.  The
determinant of the affected six-by-six block is a positive rational constant
times

\[
 D(e)=D_0+D_2e^2+D_4e^4,
\]

where

\[
\begin{aligned}
D_0&=2051707767720157160228913515968431069103,\\
D_2&=-1090358633197796493303909355562500000000000,\\
D_4&=79621528955194140625000000000000000000000000.
\end{aligned}
\]

The positive-definite cone is convex and contains `e=0`; hence its intersection
with this line ends at the first singularities.  Thus

\[
 H(e)\succ0\quad\Longleftrightarrow\quad -\rho<e<\rho,
\]

with

\[
 \rho=\sqrt{\frac{-D_2-\sqrt{D_2^2-4D_4D_0}}{2D_4}}.
\]

Exact sign evaluations isolate it by

\[
 \frac{237277724271}{5000000000000}
 <\rho<
 \frac{474555448543}{10000000000000},
\]

so `rho=0.0474555448542...`.

Every discrete correlation is affine in `e`.  Intersecting all 32 exact
half-lines gives the closed correlation interval

\[
 -\frac{99328875215622458703517433743}
 {266215653825678622228000000000}
 \le e\le
 \frac{1512327642358025296022757086677}
 {2129928656379216904877200000000}.
\]

The lower endpoint comes from shift 29 and the upper endpoint from shift 15.
They are approximately `-0.3731143` and `0.7100368`, far outside the PD
interval.  Consequently the **full combined feasible set of rational
parameters** is exactly

\[
 \boxed{\{e\in\mathbb Q:-\rho<e<\rho\}}.
\]

The block-lift formula from the finalized proof then supplies every integer
shift, not just the 32 discrete ones.

## 2. Fixed published boundary q

This subsection keeps the published rational boundary data fixed:

\[
q_{r,j}=\lambda_rw_{r,j}.
\]

It does **not** solve a new boundary QP.  Exact adjugate computation gives

\[
 \Phi_{\rm pub}(e)=
 \frac{R_\Phi(e)}{6250000000000000000000000000\,D(e)},
\]

and

\[
 f_{\rm pub}(e):=a(e)b_{\rm pub}(e)=
 \frac{P(e)}
 {39062500000000000000000000000000000000000000000000000000000\,D(e)}.
\]

The exact coefficients of the degree-four `R_Phi`, degree-five `P`, and
degree-eight derivative numerator `Q` are embedded and printed by the replay
script.  Thus this is an explicit exact rational function, not a numerical
fit.

Sturm's theorem gives exactly one zero of `Q` in `(-1/20,1/20)`, hence exactly
one stationary point in the full PD interval.  Exact endpoint signs isolate it:

\[
 \frac{80060813}{500000000000}
 <e_*<
 \frac{160121627}{1000000000000}.
\]

The derivative is negative below and positive above this root, so `e_*` is the
constrained fixed-`q` minimum.  Numerically,
`e_*=0.00016012162698045...`.  The nearby rational upper endpoint gives the
fully exact product

\[
\frac{
1826359371282347445248533482923840365408442452208665439211643874895753307448928507585885670230497882572387900751315374709
}{
2051679812137901260152128498213487687220116286815254519287890625000000000000000000000000000000000000000000000000000000000
},
\]

whose square root is

\[
0.9434922260275621102829410752\ldots.
\]

This is only about `2.1e-13` below the finalized coefficient at `e=1/6250`;
the finalized rational was already essentially optimal **for the published
fixed boundary data along this one direction**.

## 3. Reoptimized boundary q: a separate, stronger experiment

Now discard the published `q` while retaining the same kernels, `lambda`, and
cover right-hand side.  At the feasible rational point

\[
 e=1/462,
\]

the generalized exact boundary QP was solved again.  This is a different
claim from Section 2.

The exact active set has 126 of 128 cover constraints; shifts 1 and 15 are
inactive with strictly positive slack.  The replay verifies with rational
arithmetic:

- all 126 active dual coordinates are strictly positive;
- all cover slacks are nonnegative;
- `2Dq=A^Ty` exactly;
- every complementary product is zero;
- primal and dual values agree exactly;
- every coordinate of the reconstructed `q` is positive.

The exact fractions have roughly 3,700 digits, so the memo records canonical
hashes and leaves byte-for-byte reconstruction to the script:

| object | SHA-256 of canonical exact fraction/vector text |
|---|---|
| `Phi` | `48833af26e3e355ec066ba167489021f098dc843d9073a9cca43186b22d94a72` |
| `a` | `790050d486b890c8654a2edfab1c7e22dfc1bc23537c810541081e5a3fbba9a5` |
| `b` | `8b9a03f83c06c7e3ca3f38b20ccf77bb161290341c8bce7b8221dbd1cf52c7d5` |
| product | `fed1b5a8d060f704ddf29a17bd69a0cb37189de3ce8d5ab188f6857536be0b55` |
| primal `q` | `67c241f79156ef8d74fed591f1756e833ddfba712a93a6c11454bec551912287` |
| dual `y` | `b8ad1a0e84b0fd111ba498bd8fdbbe78aa266d990faefea2240d32d621d65099` |
| slack | `1e1f3f5a53b6d3c14c5a2e3203d526c2c1a7ca0391ba3aab69fd96bc56ef5ba8` |

The resulting exact coefficient begins

\[
 \sqrt{a_Hb_H^*}=0.9434876661938243084138620146\ldots
 <\frac{94348767}{100000000}.
\]

Therefore the project-internal finite master lemma certifies the exploratory
finite bound

\[
 \boxed{F(N)\le \sqrt N+0.94348767N^{1/4}+O(1)}.
\]

The script cross-multiplies this bound exactly.  It also proves that the
reoptimized product is strictly smaller than the product obtained from the
published fixed `q` at the same `e=1/462`.  Numerically searching the
reoptimized-QP value suggests a minimum near `e=0.00216279596`, but that
location is **numerical only**; no global or algebraic optimum for the
piecewise-active QP is claimed here.  The exact certified point is `e=1/462`.

### Canonical certificate family

The promoted `e=1/462` result is stored in:

- [`hou_zhao_two_cycle_epsilon_exploration.py`](hou_zhao_two_cycle_epsilon_exploration.py) — generator, raw replay, exact KKT, offline validator, and mutation self-check;
- [`hou_zhao_reoptimized_boundary_certificate.json`](hou_zhao_reoptimized_boundary_certificate.json) — byte-canonical exact payload;
- [`test_hou_zhao_reoptimized_boundary_certificate.py`](test_hou_zhao_reoptimized_boundary_certificate.py) — offline replay and mutations;
- this memo — theorem and scope narrative.

The payload SHA-256 is
`b0095488470697d0c0e38be1e18a427fc6a6e490f2ed8f04bd02a1cb20f25b52`.
Source-backed regeneration was repeated after adding the explicit
`all(q_j>0)` assertion and was byte-identical to the stored JSON.  The offline
suite has 15 tests; the built-in self-check rejects 40 mutations.

### Retained conservative regression point

The earlier conservative point `e=1/500` is retained as an exact regression.
It passed the same PD, all-32-correlation, positive-primal, positive-active-dual,
cover, stationarity, complementarity, and primal--dual gates.  Its coefficient
is

\[
0.9434876940574035151880525370\ldots<0.9434877.
\]

The JSON locks its former payload hash
`f5c4a7743ad638d55c319fa23b75178fc769d7985d6080d342c62299b4872a9e`
and product hash
`f2a43e5968bf0c657cc2793fcaabff90f68543c137edd05ffb7f3a05140080e9`.
For the primary `e=1/462` point, the minimum correlation remains positive at
shift 31:

\[
\frac{140676565613953482417771177563}
{481250000000000000000000000000000}>0.
\]

No optimum claim is attached to either rational point.

## 4. Replay and dependency boundary

Offline fixed-`q` analysis uses the standard library only:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  hou_zhao_two_cycle_epsilon_exploration.py
```

Raw-source/QP replay additionally requires the external pinned Hou--Zhao file
and `python-flint` for the 126-by-126 exact rational solve:

```bash
PYTHONPATH=/path/to/python-flint PYTHONDONTWRITEBYTECODE=1 python3 \
  hou_zhao_two_cycle_epsilon_exploration.py \
  --upstream /path/to/sidon_certificate_8kernel.py \
  --reoptimize --output hou_zhao_reoptimized_boundary_certificate.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  hou_zhao_two_cycle_epsilon_exploration.py \
  --verify hou_zhao_reoptimized_boundary_certificate.json --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_hou_zhao_reoptimized_boundary_certificate.py
```

The upstream source and third-party solver are not bundled.  The exact KKT
checks after the solve are independent `Fraction` computations.  This remains
a finite-Sidon coefficient result only and does not change the unresolved
global status of Erdős Problem #1191.
