# Route C: parametric physical-cover chambers on one fixed history

**Status:** exact phase-almost-everywhere root-SDDM-plus-two-`J` LP theorem on
one fixed finite Golomb history; exact local cross-chamber transport and an
exact positive phase-integrated cover-excess obstruction; no universal paid
ledger.

This note continues C086--C088 without changing the underlying marks as the
scale changes.  Its purpose is deliberately narrower than C058: determine
exactly what happens to the physical-cover LP on one full dyadic phase, and
separate local parametric transport from a genuine cross-scale payment.

## 1. One fixed compatible finite history

Fix once and for all

\[
 a_k=k(k+100),\qquad 0\le k\le15.
 \tag{1}
\]

All 120 positive differences are distinct.  The two consecutive blocks are

\[
 \{a_3,\ldots,a_7\},\qquad \{a_7,\ldots,a_{15}\},
 \tag{2}
\]

of sizes `n=4` and `n=8`, sharing only `a_7=749`.  Their deduplicated
coordinate vector is

\[
 (309,416,525,636,749,864,981,1100,1221,1344,1469,1596,1725).
 \tag{3}
\]

This is one fixed 16-mark finite history, not the changing quadratic family
used in the C087 three-epoch probe.  Nothing here asserts that (1) extends to
one compatible infinite Sidon history.

For `128<=T<=256`, let `v_c(T)` be the actual half-open Haar state on cell
`c`, let `M=M_4+M_8` be the embedded direct-`B` matrix, and minimize

\[
 P^*(T)=\min_{w,\kappa\ge0}
 \left\{
 \sum_{i<j}\chi_T(a_j-a_i)w_{ij}
 +\Gamma_{4,T}\kappa_4+\Gamma_{8,T}\kappa_8:
 v_c^{\mathsf T}(C+\kappa_4J_4+\kappa_8J_8-M)v_c\ge0
 \ \forall c
 \right\},
 \tag{4}
\]

where

\[
 C=\sum_{i<j}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T}
 \tag{5}
\]

and `chi_T` is the exact C086 tent cost.  Thus (4) is precisely the physical
root-SDDM-plus-two-`J` LP, not a coefficient-trace surrogate.

## 2. Why the parameter space has finitely many exact chambers

The cell endpoints are

\[
 a_i,\qquad a_i+T,\qquad a_i+2T.
\]

Two endpoint functions cross only when

\[
 T=d\quad\hbox{or}\quad T=d/2
 \tag{6}
\]

for a positive coordinate difference `d`.  The same values are exactly the
breakpoints of the root-cost tent.  On each open component of the complement:

1. the ordered cell states and hence the primal constraint matrix are fixed;
2. every root and aggregate objective coefficient is affine in `x=1/T`;
3. every fixed primal vertex therefore has objective `alpha+beta/T`.

Exact enumeration gives the following 23 event breakpoints and 22 open event
chambers:

\[
\begin{gathered}
128,129,\frac{327}{2},\frac{333}{2},\frac{339}{2},
\frac{345}{2},\frac{351}{2},\frac{357}{2},\frac{363}{2},
\frac{369}{2},\frac{375}{2},\frac{381}{2},\\
216,220,224,228,232,236,240,244,248,252,256.
\end{gathered}
\tag{7}
\]

Every generic event chamber has exactly 40 complete real-line atomic cells,
including both zero exteriors.

## 3. Exact optimality-chamber theorem

Some fixed-state chambers contain an objective-basis switch.  After including
those switches, there are exactly 30 open optimality chambers.  The exact
optimal value is as follows.

| open `T` interval | exact `P*(T)` |
|---|---:|
| `(128,129)` | `827/3360-579/(40T)` |
| `(129,577/4)` | `53/224-213/(16T)` |
| `(577/4,6493/44)` | `103/448-22125/(1792T)` |
| `(6493/44,643/4)` | `5/32-189/(128T)` |
| `(643/4,2573/16)` | `1/8+227/(64T)` |
| `(2573/16,327/2)` | `3027/(128T)` |
| `(327/2,333/2)` | `45/448+3795/(448T)` |
| `(333/2,339/2)` | `89/448-13123/(1792T)` |
| `(339/2,345/2)` | `1/5-2879/(384T)` |
| `(345/2,351/2)` | `1/5-2879/(384T)` |
| `(351/2,357/2)` | `23/112-1061/(128T)` |
| `(357/2,363/2)` | `23/112-1061/(128T)` |
| `(363/2,369/2)` | `23/112-1061/(128T)` |
| `(369/2,375/2)` | `23/112-1061/(128T)` |
| `(375/2,381/2)` | `23/112-1061/(128T)` |
| `(381/2,216)` | `53/224-213/(16T)` |
| `(216,220)` | `61/448+939/(112T)` |
| `(220,224)` | `27/160+199/(16T)` |
| `(224,228)` | `27/160+199/(16T)` |
| `(228,232)` | `27/160+199/(16T)` |
| `(232,236)` | `27/160+199/(16T)` |
| `(236,240)` | `37/192+5255/(576T)` |
| `(240,244)` | `323/1664+3557/(384T)` |
| `(244,2197/9)` | `323/1664+3557/(384T)` |
| `(2197/9,248)` | `1655/8576+245417/(25728T)` |
| `(248,1005/4)` | `1655/8576+245417/(25728T)` |
| `(1005/4,252)` | `5/32+1931393/(102912T)` |
| `(252,27355/108)` | `607/2368-28399/(28416T)` |
| `(27355/108,4929829/19428)` | `53/272+31711/(2176T)` |
| `(4929829/19428,256)` | `27977/161664+39000917/(1939968T)` |

The JSON records all 18 distinct sparse primal vertices, including the few
positive `kappa_8` entries, and both exact limiting duals for each of the 30
rows.  No floating output is used by the final verifier.

Here is the exact optimality argument.  In one row of the table, put
`x=1/T`.  The two stored endpoint duals `y_L,y_R` are nonnegative, satisfy all
80 root/aggregate load inequalities, and have zero gap with the displayed
primal.  Since the cost vector is affine in `x`, linearly interpolating the
two duals in `x` gives

\[
 A^{\mathsf T}y(x)\le c(x)
 \tag{8}
\]

throughout the interval, while its dual objective equals the displayed
`alpha+beta/T`.  The primal constraint matrix is constant there, so the same
primal vertex stays feasible.  Equality of the two objectives proves exact
optimality for every `T` in the open row.

At an event breakpoint, a zero-length intermediate state disappears.  The
open-chamber theorem therefore does not silently identify its limiting LP
with the actual breakpoint LP.  Those finitely many values have phase measure
zero.  Only the actual values `T=216` and `T=220`, needed below, are separately
certified in this bundle; the remaining isolated breakpoint optima are not
claimed.

## 4. What transports, and what does not

The C087 `T=200` primal

\[
 w_{02}=\frac{45}{1792},\quad
 w_{24}=\frac{11}{448},\quad
 w_{46}=\frac3{1792},\quad
 w_{10,12}=\frac1{128},\qquad
 \kappa_4=\kappa_8=0
 \tag{9}
\]

is exactly optimal on both adjacent event chambers

\[
 (381/2,216)\quad\hbox{and}\quad(216,220).
 \tag{10}
\]

The objective formula changes at `216`, because the distance `216` crosses
the first tent breakpoint, but the primal vertex does not.  Separate
affine-in-`1/T` endpoint-dual interpolation transports optimality on each
side.  Exact actual-cell duals also give zero gaps at `T=216` and `T=220`.

This is a genuine local cross-chamber transport, but not a full-phase fixed
recurrence.  At `T=221`, the actual cell `[636,637)` has state

\[
 (-1,1,1,1,0,\ldots,0)
\]

and (9) gives

\[
 v^{\mathsf T}Cv=\frac18,qquad
 v^{\mathsf T}Mv=\frac9{32},qquad
 \text{slack}=-\frac5{32}.
 \tag{11}
\]

Thus a primal can cross a chamber wall, but these fixed weights cannot cross
the next wall.  The dual transport is piecewise affine; no single fixed dual
is asserted.

## 5. The phase-integrated excess cannot telescope to zero here

For every `T`, the physical cell-length measure

\[
 \bar y_c=|c|/(2T)
 \tag{12}
\]

is dual feasible and saturates every root and aggregate cost column.  Hence

\[
 P^*(T)\ge D(T):=
 \sum_c\frac{|c|}{2T}v_c^{\mathsf T}Mv_c.
 \tag{13}
\]

On the exact chamber `(381/2,216)`, the certificate gives

\[
 P^*(T)=\frac{53}{224}-\frac{213}{16T},\qquad
 D(T)=\frac{129}{256}-\frac{5021}{64T},
\]

and therefore

\[
 E(T):=P^*(T)-D(T)
 =-\frac{479}{1792}+\frac{4169}{64T}.
 \tag{14}
\]

This is decreasing in `T` and

\[
 E(216)=\frac{3317}{96768}>0.
\]

Using `1/T>=1/216` on an interval of length `51/2` gives the entirely
rational bound

\[
 \int_{381/2}^{216}E(T)\,\frac{dT}{T}
 \ge
 \frac{3317}{96768}\frac{51/2}{216}
 =\boxed{\frac{56389}{13934592}}>0.
 \tag{15}
\]

For reference, the exact unevaluated integral is

\[
 -\frac{479}{1792}\log\frac{144}{127}
 +\frac{70873}{1755648}.
 \tag{16}
\]

Every other chamber has nonnegative excess by (12)--(13).  With
`T=128*2^theta`,

\[
 (\log2)\int_0^1 E(128\,2^\theta)\,d\theta
 =\int_{128}^{256}E(T)\,\frac{dT}{T}
 \ge\frac{56389}{13934592}.
 \tag{17}
\]

Consequently the optimal same-scale root-SDDM-plus-two-`J` cover excess does
not telescope to zero on this fixture and phase.  This is a lower obstruction
to paying only the signed direct-`B` demand.  It is not an impossibility
theorem for a larger signed, cross-scale, or externally owned master ledger.

## 6. Strict scope

The exact certificate proves only:

1. the 22 open event chambers and 30 open optimality chambers for the fixed
   history (1), the fixed n=4/n=8 joint LP (4), and `128<=T<=256`;
2. the piecewise constant primals and affine-in-`1/T` endpoint-dual transport;
3. the local transported primal (9), its actual `T=216,220` optima, and its
   exact `T=221` failure;
4. the rational positive lower bound (17).

It does **not** prove:

- the actual optimum at every isolated event breakpoint;
- a uniform statement over arbitrary finite Golomb histories;
- a compatible infinite Sidon history or arbitrary-depth recurrence;
- a telescoping upper bound or any singly owned payment of the cover;
- payment by Gothic, birth, phase, terminal, final, cross-scale, or external
  reserve rows;
- optimality beyond the root-SDDM-plus-two-`J` class;
- C058, Q1, Q2, Erdős Problem #1191, novelty, publication, or prize
  eligibility.

The result is therefore an exact conditional no-go for *zero same-scale
phase-excess on this fixed finite fixture*, not a no-go for Route C itself.

## 7. Reproducibility

The deterministic bundle consists of

- `ROUTE_C_PARAMETRIC_PHYSICAL_COVER_CHAMBERS_certificate.py`;
- `ROUTE_C_PARAMETRIC_PHYSICAL_COVER_CHAMBERS_certificate.json`;
- `test_ROUTE_C_PARAMETRIC_PHYSICAL_COVER_CHAMBERS_certificate.py`.

The generator reconstructs every cell system, primal constraint, physical
cost, affine formula, endpoint dual, zero gap, transport check, and rational
lower bound with `fractions.Fraction`.  Verification enforces literal
raw-byte JSON replay and rejects scoped semantic mutations.  Numerical LP
software was used only for discovery and is not a verification dependency.
