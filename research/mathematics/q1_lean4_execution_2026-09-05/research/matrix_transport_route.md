# Centered PSD transport and an affine carrier with a proved row gain

Date: 2026-09-05. Owner: `/root/lean_target`.

Status: Q1 is unresolved. This note constructs a closed centered PSD cone and
an explicit rank-two carrier that improves a single productive row, including
its diagonal cost. Under the critical cap the guaranteed normalized row gain
has order at least `log(2p)^(-5)`. A uniform improvement of the physical-label
envelope over growing prefixes is **not** proved. The distinction is essential.
No result in this note is claimed to have been verified by Lean.

The starting convolution and envelope identities are those of
[envelope_selection_route.md](envelope_selection_route.md), §§1–4, and
[growing_label_budget.md](growing_label_budget.md), §6. All additional
claims used here are proved below. The exact finite checks, including the
entire 34-point history, are in [the reproducible script](evidence/matrix_transport_exact_checks.py),
[its output](evidence/matrix_transport_exact_checks.log), and
[execution provenance](evidence/matrix_transport_exact_checks.run.json).

## 1. Definitions and the stronger zero-old-edge obstruction

Let `P={a_1<...<a_p}` be one finite Sidon set, with repeated summands included
in its Sidon condition. Let `F` be a nonempty subset of its actual positive
difference labels. Write `q=|F|`, `H=diam P`, and assume `p>=2`.
For a real symmetric PSD matrix `W` indexed by `F`, put

\[
 M(W)=\mathbf1^TW\mathbf1,\quad S(W)=\operatorname{tr}W,\quad
 K_W(t)=\sum_{d<e,\ e-d=t}W_{de},\quad
 T_P(W)=\sum_{t\in\Delta P}K_W(t).                    \tag{1}
\]

These definitions retain every pair in a physical-label fiber, including
distinct relations with the same numeric `t`. Always

\[
 \sum_{t>0}K_W(t)=\frac{M(W)-S(W)}2.                  \tag{2}
\]

Suppose every off-diagonal entry at an old difference is zero. Express `W`
as a Gram matrix of vectors `v_d`. Partition `F` by the larger endpoint of
its unique representation `d=a_j-a_i`. There are at most `p-1` groups.
Within each group, the difference of two distinct labels is another old
difference, so its two Gram vectors are orthogonal. If `s_j` is the sum of
the vectors in group `j`, then

\[
 M(W)=\left\|\sum_j s_j\right\|^2
 \le(p-1)\sum_j\|s_j\|^2=(p-1)S(W).                 \tag{3}
\]

This needs no entrywise nonnegativity. It is stronger than the earlier
`M/S <= |P+F|/p` obstruction whenever the latter is larger.
It is sharp: take `P={1,10,...,10^(p-1)}`, take its `p-1` consecutive gaps
as `F`, and set `W=11^T`. No difference of two such gaps is an old label.
Indeed, after removing its largest common power of ten, a difference of
gaps is `9(10^r-1)`, whose last digit is `1`, whereas a similarly normalized
old label `10^s-1` has last digit `9`. Thus `M/S=p-1` and every old edge is zero.

For a diagonal repair of an already surviving matrix with mass `M`, trace
`S`, and added diagonal trace `tau`, both mass and trace increase by `tau`.
For `p>2`, (3) therefore forces

\[
 \tau\ge\left(\frac{M-(p-1)S}{p-2}\right)_+.         \tag{4}
\]

This does not suggest another zeroing strategy; it strengthens the reason
to retain and account for old expenditure.

## 2. A closed centered cone with an exact signed cost

For every PSD `W` with `M>0`, define

\[
 v=\frac{W\mathbf1}{\sqrt M},\qquad R=W-vv^T.
 \quad R\succeq0,\quad R\mathbf1=0.                 \tag{5}
\]

PSD follows from the Gram Cauchy inequality
`(x^T W1)^2 <= (x^T Wx)M`; the zero-row-sum claim follows directly.
The rank-one part has the same mass `M` and no larger trace.
The residual entries can have either sign even when `W` is entrywise
nonnegative. They must not be discarded or called a nonnegative kernel.

The cone

\[
 \mathcal Z_F=\{R=R^T:R\succeq0,\ R\mathbf1=0\}     \tag{6}
\]

is closed and convex. Zero-padding into a larger label set preserves it.
More generally `R -> Q R Q^T` preserves the corresponding centered cone
whenever `Q^T1=1`. This is a precise algebraic transport rule; it makes no
claim that transport preserves the numeric relation label `e-d`.

The signed source carried by a residual satisfies

\[
 \sum_{t>0}K_R(t)=-\frac{S(R)}2.                    \tag{7}
\]

For any actual Sidon block `B` of size `m`, direct convolution gives

\[
 E_B(R):=mS(R)+2\sum_{t\in\Delta B}K_R(t)\ge0.       \tag{8}
\]

Thus negative expenditure on an actual block cannot be credited without
the matching `m S(R)/2` diagonal cost. For the raw interval demand
`d_B(W)=(m^2 M/D-mS)/2`, adding `R` preserves `M` and gives exactly

\[
 [\Psi_B-d_B](W+R)-[\Psi_B-d_B](W)=E_B(R)/2\ge0.     \tag{9}
\]

The actual shadow inequality becomes weaker. A possible gain must come
from reducing an overestimate on other physical labels or on envelope slack.

For signed kernels, the safe general capacity is
`sum_t max(0,max_j G_j(t))`. The raw demands remain valid; replacing them
by positive parts requires either nonnegative expenditures or coefficients
supported on nonnegative raw demands. PSD alone does not justify that replacement.
The carrier below remains entrywise nonnegative, so it avoids this issue.

## 3. A rank-two affine carrier that keeps its mass and its signs

Set

\[
 \bar d=\frac1q\sum_{d\in F}d,\quad z_d=d-\bar d,
 \quad V=\sum_{d\in F}z_d^2,
 \quad W^{\rm aff}_{de}=1+\frac{z_dz_e}{H^2}.         \tag{10}
\]

This is the Gram matrix of `(1,z_d/H)`, hence PSD at every finite prefix.
It is also the exact mean of two nonnegative rank-one carriers:
`u^+_d=1+z_d/H`, `u^-_d=1-z_d/H`, and
`W^aff=(u^+(u^+)^T+u^-(u^-)^T)/2`. Thus this particular affine improvement
does not require expressive power beyond mixtures of the original nonnegative
scalar weights. The stronger centered Fourier selection in
[centered_spectral_gain.md](centered_spectral_gain.md) obtains a non-summable
single-row guarantee while retaining an analogous nonnegative decomposition.
Since the range of `F` has length at most `H`, the largest positive and
negative deviations from its mean have product at most `H^2/4`. Therefore

\[
 \tfrac34\le W^{\rm aff}_{de}\le2,\qquad
 M(W^{\rm aff})=q^2,\qquad
 S(W^{\rm aff})=q+V/H^2\le\tfrac54q.                \tag{11}
\]

For the variance bound, if all labels are in `[l,r]`, summing
`(d-l)(r-d)>=0` gives `V/q <= (bar d-l)(r-bar d) <= (r-l)^2/4`.
The effective ratio is at least `4q/5`; no hidden diagonal repair occurs.
The added residual is exactly `zz^T/H^2` in (6).

This lies in the finite affine Gram cone

\[
 \{( (1,d) C(1,e)^T )_{d,e\in F}:
    C\succeq0,\ (1,d)C(1,e)^T\ge0\text{ for all }d,e\in F\}. \tag{12}
\]

The parameter cone is a closed intersection of the two-by-two PSD cone
with finitely many linear half-spaces. For `q>=2` its map to Gram matrices
is injective onto a finite-dimensional subspace, so its matrix image is
closed as well. The explicit parameter in (10) is

\[
 C=\begin{pmatrix}1+\bar d^2/H^2&-\bar d/H^2\\
                  -\bar d/H^2&1/H^2\end{pmatrix},
 \qquad\det C=1/H^2>0.                              \tag{13}
\]

This construction works for arbitrary prefix size; it is not a claim that
rank two captures every useful PSD carrier.

## 4. A cap-dependent old-energy gain from a first moment

Use the unscaled centered residual `R=zz^T`, so `S(R)=V`. Define
`f(x)=sum_(a in P) z_(x-a)`, extending the label vector by zero.
Then

\[
 \sum_xf(x)=0,\qquad \sum_x x f(x)=pV,\qquad
 E_P(R)=\sum_x f(x)^2=pV+2T_P(R).                    \tag{14}
\]

The support is in an integer interval of at most `2H` points, each within
distance `H` of its midpoint `c`. Since `sum f=0`, Cauchy gives

\[
 p^2V^2=\left(\sum_x(x-c)f(x)\right)^2
 \le2H^3 E_P(R),\qquad
 \boxed{E_P(R)\ge p^2V^2/(2H^3).}                   \tag{15}
\]

For `q` distinct integer labels, ordered as `d_1<...<d_q`,

\[
 V=\frac1q\sum_{i<j}(d_j-d_i)^2
 \ge\frac1q\sum_{i<j}(j-i)^2
 =\frac{q(q^2-1)}{12}.                              \tag{16}
\]

Thus the old adjacency matrix, tested on this centered vector, has

\[
 \frac{2T_P(R)}{S(R)}
 \ge\frac{p^2q(q^2-1)}{24H^3}-p.                    \tag{17}
\]

For the full label bank `q=p(p-1)/2`, under
`H <= C p^2 log(2p)`, the first term has asymptotic lower size
`p^2/(192 C^3 log(2p)^3)`. It eventually exceeds every fixed multiple of
`p`. This is a proved conditional estimate at each such prefix, not a
numerical extrapolation.

## 5. Exact single-row improvement and its logarithmic rate

For entrywise nonnegative PSD `W`, its available old-masked row capacity is

\[
 \mathcal C_P(W)=\sum_{t\notin\Delta P}K_W(t)
                =(M-S)/2-T_P(W).                   \tag{18}
\]

For a compatible future block `B` of size `m`, interval length `L`, and
positive denominator `D=L+H-m`, let `d_B(W)=(m^2M/D-mS)/2`.
The exact improvement over `W^0=11^T` in capacity minus raw demand is

\[
\begin{split}
 \mathcal I
 &:=[\mathcal C_P-d_B](W^0)-[\mathcal C_P-d_B](W^{\rm aff})\\
 &=\frac{2T_P(R)-(m-1)V}{2H^2}
   =\frac{E_P(R)-(p+m-1)V}{2H^2}\\
 &\ge\frac{p^2V^2}{4H^5}-\frac{(p+m-1)V}{2H^2}.     \tag{19}
\end{split}
\]

The factor `m-1` is essential: the diagonal cost of the future demand has
been subtracted from the reduction of available capacity. The correction
is not free.

For the full bank, fixed `C>0`, and `p <= m <= R_0 p` with fixed `R_0`,
(15)–(17) show `I>0` for all sufficiently large `p` meeting the cap.
Dividing by the unchanged mass `M=q^2`, and using both variance bounds,
gives the explicit lower bound

\[
 \boxed{\quad
 \frac{\mathcal I}{M}
 \ge\frac{p^2(q^2-1)^2}{576H^5}
       -\frac{p+m-1}{8q}.
 \quad}                                             \tag{20}
\]

In particular its guaranteed asymptotic size is at least

\[
 \frac{1+o(1)}{9216C^5\log(2p)^5}-O_{R_0}(1/p),     \tag{21}
\]

which is positive eventually. This is a lower guarantee of order
`log(2p)^(-5)`, not a claim that every actual gain has exactly that order.
For the productivity assertion, take the actual rank shell
`B={a_(m+1),...,a_(2m)}` and impose the same cap at rank `2m` as well.
Then the carrier also remains productive: `M/S >= 4q/5`, whereas
`D/m <= 4 C m log(4m) + C p^2 log(2p)/m` is
`O_(C,R_0)(p log p)` for these near shells. Consequently both raw demands
are positive for sufficiently large capped prefixes, so the same comparison
applies to their positive-part demands there. An arbitrary far-away block
of the same cardinality is not being given this rank-dependent span bound.

At dyadic `p=2^k`, the guaranteed lower term in (21) has order `k^(-5)`.
Its sum converges. It therefore does not itself supply a divergent gain,
even before addressing the separate physical-label charging problem.

## 6. One exact productive finite comparison

The checked seed, displayed with minimum zero for compactness, is

```
P = [0,1,3,7,12,20,36,46,61,83,101,131,173,200,251,279,335].
```

Choose each next point to be the least integer above the last point whose
differences with all current points are unused. The next 17 points are

```
B = [356,387,453,521,596,698,751,813,880,989,1075,
     1213,1316,1339,1432,1574,1707].
```

Adding one to all 34 numbers gives the positive Sidon history. The checker
verifies both unique positive differences and unique unordered sums with
repeated summands. Here `q=136`, `H=335`, `L=1352`, `D=1670`, and

\[
 \bar d=8223/68,\quad V=40522331/34,\quad
 2T_P(zz^T)=31065351025/1156.                         \tag{22}
\]

The exact comparison is:

| Quantity | Uniform carrier | Affine carrier |
|---|---:|---:|
| `M` | `18496` | `18496` |
| Available row capacity | `4026` | `1012159758921/259464200` |
| Raw demand | `371076/835` | `26547974003/74966300` |
| Actual internal expenditure | `1196` | `152501253349/129732100` |

The affine demand is approximately `354.132 > 0`; the actual expenditure
is approximately `1175.509`. Capacity minus demand improves by exactly

\[
 \mathcal I=9021202961/259464200\approx34.7686>0.      \tag{23}
\]

Here the future-span mask is inactive on the kernel support, so the
available capacity is also the literal one-epoch masked envelope.
This is a real finite improvement, with the diagonal cost retained. It
does not provide a bound for a family of growing-prefix envelopes.

All displayed exact values were recomputed with `fractions.Fraction` in
the linked script. It independently expands the vector-valued future
convolution, verifies its support exclusion, and checks the matrix moment
identity. Decimal displays are not used by any assertion. The run exited
with code zero; source hashes before and after execution agree.

## 7. What is transported, and the remaining injection term

The affine family uses the fixed coordinate features `(1,d)`. Its parameter
matrix changes with the exact scalars `q`, `sum d`, `sum d^2`, and `H`.
For disjoint additions of `r` labels, with means `mu,nu`, the exact variance
update is

\[
 V_{\rm new}=V_{\rm old}+V_{\rm added}
              +\frac{qr}{q+r}(\mu-\nu)^2.           \tag{24}
\]

This gives an algebraic carrier at every prefix. It does not make its
physical-label kernel monotone or permit its source budget to be reset.
For nested `P` and nested full label banks, normalize each matrix by `q^2`
if mass one is desired. Writing `b_k(t)=1[t notin Delta P_k] K_k(t)`,
the exact masked transport is

\[
 b_{k+1}(t)-b_k(t)
 =1[t\notin\Delta P_{k+1}](K_{k+1}(t)-K_k(t))
  -1[t\in\Delta P_{k+1}\setminus\Delta P_k]K_k(t).    \tag{25}
\]

The first term includes both new relation pairs and changes to weights on
old pairs. It has no proved favorable sign. The second is actual retirement.
The row gain in (19) does not remove the first term from (25).

There is an exact obstruction to an unconditional bounded-envelope claim
for this very carrier. On the actual, uncapped Sidon sequence `10^i`, take
full banks at dyadic prefix sizes `p`. Four distinct endpoints create three
unordered pairs of positive labels, with two distinct numeric relation
labels (one of multiplicity two). Their coefficient patterns in powers of
ten uniquely identify their four endpoints. These labels are never old
differences. The source mass on four-endpoint labels born after size `p/2`
for the normalized uniform carrier is exactly

\[
 \frac{3\{\binom p4-\binom{p/2}4\}}{\binom p2^2}
 \longrightarrow15/32.                             \tag{26}
\]

The birth supports of different dyadic epochs are disjoint. The affine
carrier's entrywise lower bound in (11) makes its normalized kernel at
least `3/4` of the uniform kernel. Its maximum-over-epoch physical-label
cost therefore also grows at least linearly with the number of epochs.
Finite cases of the exact count are checked in the script; the general
count follows from the four-endpoint classification just described.
This sequence violates the critical cap. It excludes a bound from cone
closure and normalization alone, and does not refute a cap-dependent theorem.

## 8. Mathematical outcome and unresolved task

The credible carrier is (10), inside the explicit closed cone (12).
Its signed centered correction, diagonal cost, old-mask expenditure,
and source injection are all retained. Equations (19)–(21) prove a
cap-dependent, productive, single-row gain at arbitrary large prefix sizes;
(23) verifies a nonvacuous exact finite instance.

What remains is to couple that gain to the actual maxima in the physical
envelope, including the injection term in (25). Neither a uniformly
summable injection bound nor an aggregate positive envelope gap is proved.
The logarithmic rate in (21) is summable over dyadic ranks as a lower-bound
mechanism, so repeating the local gain is not a justified closure argument.
The original Q1 remains unresolved.
