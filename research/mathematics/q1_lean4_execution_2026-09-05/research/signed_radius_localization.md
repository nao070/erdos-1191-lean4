# Signed source-radius localization, its boundary, and a finite carrier

Date: 2026-09-05. Owner: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Status: exact radius-cutoff and integrated full-Born formulas, including
all missing-source boundary terms and doubled labels. Lebesgue radius
weight `dD` gives a permanent minimum kernel with nonnegative full Born
sum. A finite PSD, entrywise nonnegative background is constructed and
priced exactly. Its future demand and a normalized good-epoch row gain
are proved against that same background and placed in one actual
physical maximum. The shared maximum and its global baseline margin
are not bounded here. No conclusion about original Q1 or the older
positive-bank birth-linear total follows. No experiment or Lean edit
was needed or performed.

The starting full signed-bank sign theorem and clock convention are
those of `signed_bank_born_positivity.md`. The present source-radius
cutoff is different from discarding an output because it is numerically
large. Output births are always taken from the full actual history.

## 1. The exact missing-source boundary at one radius

Fix an actual integer Sidon prefix `P_N`, its positive difference bank
`F`, signed bank `Fhat=F union(-F)`, and `H=a_N-a_1>0`. Births satisfy
`tau(-d)=tau(d)`. A used unordered source pair `{d,e}` is Born if

```
tau(|d-e|) <= max(tau(d),tau(e)).
```

Same-birth sources are included. Fix any nonnegative source-stage
weights `alpha_b`. At radius D>0 define the odd cutoff feature on the
full terminal bank by

```
phi_D(d) = (d/D) 1[|d|<=D].                              (1)
```

Equivalently its source bank is `Fhat intersect [-D,D]`. The output
is still tested against F and its actual birth. The cutoff feature
in (1) is not a nondecreasing function on the positive labels, so
the odd-monotone theorem cannot simply be applied at each D.

Partition the used pairs by the canonical numeric Schur triples
`0<x<=y`, `z=x+y`, with x,y,z in F. Put
`M=max(tau(x),tau(y),tau(z))`. For x<y let B_lin(x,y,z) denote
the full unnormalized linear Born contribution from that triple:

| Latest-clock case | B_lin |
|---|---:|
| x uniquely latest | `2x^2` |
| y uniquely latest | `2y^2` |
| z uniquely latest | `2z^2` |
| maximum attained at least twice | `2(x^2+xy+y^2)` |

The complete contribution of that triple to the radius-D functional
is exactly

```
alpha_M / D^2 * {
    0,                                D<y;
    -2xy * 1[tau(z)<=max(tau(x),tau(y))], y<=D<z;
    B_lin(x,y,z),                     z<=D.
}.                                                       (2)
```

To prove (2), recall the three source-pair groups. The positive
groups `{y,z}`, `{-z,-y}` and `{x,z}`, `{-z,-x}` require the
source z and therefore appear only at D>=z. The negative group
`{-x,y}`, `{-y,x}` appears at D>=y. It is Born precisely when
the indicator in (2) equals one. In that case its source price is
alpha_M. Thus it cannot be dropped merely because its output z
lies outside the source radius. When z is uniquely latest, that
boundary group is retired and contributes zero to Born; in every
other latest-clock case it is Born.

For the doubled-label relation x=y, z=2x, write

```
B_lin(x,x,2x) = 4x^2  if tau(2x)>tau(x),
               3x^2  otherwise.
```

Its radius contribution is

```
alpha_M / D^2 * {
    0,                              D<x;
    -x^2 * 1[tau(2x)<=tau(x)],       x<=D<2x;
    B_lin(x,x,2x),                  2x<=D.
}.                                                       (3)
```

There is one negative pair `{-x,x}`, not two. Equal clocks in (3)
are a valid formal case but impossible for two actual positive
labels x,2x in one birth star. Equations (2)--(3) exhaust every
used source pair, without deleting any repeated point endpoints.

## 2. General integrated radius weights and their exact sign condition

Let w(D)>=0 and an upper radius D_* in (0,infinity] be such that
the following integrals are finite at every positive label used.
Set

```
A_*(u) = integral_(u..D_*) w(D)/D^2 dD   if u<=D_*,
         0                              if u>D_*.
```

Integrating (1) produces the PSD residual matrix

```
R_*(d,e) = d e A_*(max(|d|,|e|)).                       (4)
```

Its full Born sum is the integral of (2)--(3). For x<y the exact
group totals before the common price alpha_M are

| Latest-clock case | Integrated contribution |
|---|---|
| x uniquely latest | `2x[z A_*(z)-y A_*(y)]` |
| y uniquely latest | `2y[z A_*(z)-x A_*(y)]` |
| z uniquely latest | `2z^2 A_*(z)` |
| tied maximum | `2z^2 A_*(z)-2xy A_*(y)` |

For x=y the two totals are

```
4x^2 A_*(2x),                           tau(2x)>tau(x);
4x^2 A_*(2x)-x^2 A_*(x),                otherwise.       (5)
```

These formulas include z>D_*: the internal positive term then
vanishes, while a negative boundary contribution can remain if
y<=D_*. This finite terminal cutoff must not be replaced by an
infinite integration limit without paying the tail.

A sufficient condition for every group above to be nonnegative is

```
u -> u A_*(u) is nondecreasing on the relevant positive radii.
                                                               (6)
```

Indeed (6) gives `z A_*(z)>=y A_*(y)>=x A_*(y)`. It proves
both unique-small-label cases and then the tied case. For the
doubled case it gives `2A_*(2x)>=A_*(x)`, which is stronger
than the needed condition `4A_*(2x)>=A_*(x)`.

More precisely, the unique-latest-x group itself is nonnegative
if and only if `z A_*(z)>=y A_*(y)`. This is a condition on the
group calculation, not a necessary condition for the sum over an
actual bank to be nonnegative: other groups can compensate. No
negative full-bank claim is inferred from failure of (6).

For example, on (0,infinity) the weights `w(D)=D^p`, `0<=p<1`,
have

```
A(u)=u^(p-1)/(1-p),   u A(u)=u^p/(1-p),
```

so their full Born sums are nonnegative for every actual bank and
every nonnegative alpha. For any such integrable weight a finite
PSD, nonnegative background is also available directly: the matrix

```
V_*(d,e)=|d e| A_*(max(|d|,|e|))
```

is the integral of the outer products of
`|d|/D * 1[|d|<=D]`. Thus `V_*+lambda R_*` is PSD and
entrywise nonnegative for 0<=lambda<=1. This uses a decaying
background feature rather than integrating an unweighted J forever.

In contrast, logarithmic radius weight `dD/D` has
`A(u)=1/(2u^2)`, and the unique-latest-x group equals

```
x(1/z-1/y) = -x^2/(yz) < 0.                            (7)
```

Such a clock pattern is compatible with actual Sidonness: in
`{0,2,5,6}`, the labels x=1,y=2,z=3 have births 4,2,3.
The six positive differences of that four-point set are exactly
1 through 6. This verifies that the local clock case cannot be
excluded, but (7) does not assert a negative full Born sum on that
set or a negative asymptotic family. No finite sign search was run.

## 3. Ordinary radius measure and the indispensable finite-cutoff tail

For w(D)=1 and D_*=infinity, A(u)=1/u. Equation (4) becomes

```
R_min(d,e) = sign(d)sign(e) min(|d|,|e|).                 (8)
```

For x<y the four clock-case totals are, respectively,

```
0,        2(y-x),        2z,        2y.                  (9)
```

For x=y they are 2x when 2x is latest, and x otherwise.
They are all nonnegative. These are exact integrated full-Born
contributions, including the negative boundary intervals in (2)--(3).

For a finite D_*>=H, the uncompleted integral instead has

```
A_*(u)=1/u-1/D_*,
R_*=R_min-(d)_d(d)_d^T/D_* .                            (10)
```

Its unique-latest-x contribution is `-2x^2/D_*`. The missing
tail is exactly the rank-one matrix

```
integral_(D_*..infinity) phi_D phi_D^T dD = (d)_d(d)_d^T/D_*.
                                                               (11)
```

All source labels are present in this tail, since D_*>=H. Its
full Born contribution is B_lin/D_* group by group, so (11)
restores (9) exactly. Omitting (11) would invalidate the stated
nonnegative group theorem. Again, a negative group in the truncated
calculation is not by itself a negative complete-bank result.

An unweighted J background integrated with dD to infinity is not
finite: for D>=H the restricted source bank is already all Fhat,
and every entry of J persists. That divergence is real. A finite
completion can be priced explicitly. Let

```
B_*(d,e)=integral_(0..D_*)1[|d|,|e|<=D]dD
        =D_*-max(|d|,|e|),
T_*(d,e)=[|d||e|+lambda d e]/D_*.
```

The finite-radius integral `B_*+lambda R_*` is PSD and entrywise
nonnegative; the same is true of T_* for 0<=lambda<=1. Adding
T_* supplies the residual tail and its nonnegative background.
If

```
V_min(d,e)=min(|d|,|e|),  u_*(d)=D_*-|d|,
```

the resulting matrix is exactly

```
B_*+lambda R_*+T_*
 = V_min+lambda R_min+u_*u_*^T/D_* .                    (12)
```

This follows by expanding
`D_*-max(u,v)+uv/D_*=min(u,v)+(D_*-u)(D_*-v)/D_*`.
Writing Q=|Fhat| and `A=sum_d |d|`, the extra rank-one
background has exact mass and trace

```
(D_* Q-A)^2/D_*,     sum_d(D_*-|d|)^2/D_*.
```

Thus the background expenditure can be finite, but is not zero.
The next section constructs `V_min+lambda R_min` directly, without
that additional background term.

## 4. Upper-tail thresholds give a permanent finite carrier

For r>0 put

```
a_r(d)=1[|d|>=r],
z_r(d)=sign(d)1[|d|>=r].
```

The signed z_r is odd and nondecreasing on the entire signed line:
it is -1 below -r, zero between the thresholds, and +1 above r.
It does not lose the positive Schur completions in the manner of a
ball cutoff. More formally the reviewed odd-monotone theorem gives
nonnegative full Born sum for each z_r separately, including all
ties and doubled labels.

The identities

```
V_min = integral_(0..infinity) a_r a_r^T dr,
R_min = integral_(0..infinity) z_r z_r^T dr              (13)
```

prove both PSD statements and the nonnegative full Born sum of
R_min with any nonnegative source-stage weights. On a finite
prefix these integrals stop at H, because both features vanish
for r>H. There is no divergent background tail in (13).

Consequently, for 0<=lambda<=1,

```
W=V_min+lambda R_min                                   (14)
```

is a finite PSD, entrywise nonnegative carrier. Its same-sign
entries are `(1+lambda)min(|d|,|e|)` and opposite-sign entries
are `(1-lambda)min(|d|,|e|)`. All entries are permanent functions
of the physical signed labels. Extending the Sidon history does
not change existing entries; no terminal H normalization enters
their definition.

Define the actual terminal tail statistics

```
Q_r=|{d in Fhat:|d|>=r}|,
A=integral_0^H Q_r dr = sum_d |d|,
M=integral_0^H Q_r^2 dr = 1^T V_min 1.
```

Every z_r sums to zero on every signed prefix. Therefore the
exact mass and trace of the background, residual, and carrier are

```
M(V_min)=M,        tr(V_min)=A,
M(R_min)=0,       tr(R_min)=A,
M(W)=M,           tr(W)=(1+lambda)A.                    (15)
```

The finite background cost is bounded and can be computed exactly:

```
A^2/H <= M <= Q A <= Q^2 H.                             (16)
```

The first inequality is Cauchy applied to Q_r on [0,H], and the
second uses Q_r<=Q. If the positive labels are sorted as
`0=d_0<d_1<...<d_q`, an explicit finite sum is

```
M=4sum_(i=1..q)(q-i+1)^2(d_i-d_(i-1)),  A=2sum_i d_i.
```

## 5. One fixed historical capacity and its own future demand

Let B_R be the full Born functional of R_min on the terminal bank,
with unit source-stage prices. It is nonnegative by (9) or (13).
The fixed-matrix historical pair-lifetime identity, with the full
actual old-label mask, gives

```
C_hist(V_min)-C_hist(W)=lambda(B_R+A/2).                 (17)
```

The extra A/2 is the exact total off-diagonal residual charge;
same-birth signed retirements are retained. The full background
capacity itself is
`C_hist(V_min)=(M-A)/2-FullBorn(V_min)`, at most `(M-A)/2`.
No separate capacity is assigned to individual thresholds.

Neither (17) nor full Born positivity assigns a nonpositive sign
to the residual correlation on actually retired outputs. Restricting
the physical budget to those outputs therefore does not permit
discarding their signed residuals. Such an output restriction is
distinct from the source-radius and threshold decompositions proved
above.

For one compatible actual future block B with m points and span
`[b,b+L-1]`, use the full signed interval and all m holes:

```
T=L+2H,       D=T-m>0.
```

For each r the uniform and odd threshold shadows have total mass
`mQ_r` and 0. Define

```
mu_r=sum_(d in Fhat)|d|1[|d|>=r],
I=integral_0^H mu_r^2 dr.
```

The odd shadow has first moment m mu_r. Cauchy on the same actual
support complement for the uniform channels, and on the full
interval for the first moments, gives

```
E_B(V_min) >= m^2 M/D,
E_B(R_min) >= LB_R(B):=12m^2 I/[T(T^2-1)].               (18)
```

These follow by integrating the individual channel inequalities
in (13), not by creating separate physical copies of a difference.
The exact combined expansion and raw demand are

```
E_B(W)=m(1+lambda)A+2sum_(t in Delta B)K_W(t),

delta_mom(B,W)
 =[m^2M/D+lambda LB_R(B)-m(1+lambda)A]/2.                (19)
```

Here K_W is the single nonnegative physical correlation of W.
Compare with the background mass-only demand
`delta_V=[m^2M/D-mA]/2`. Combining (17)--(19) proves

```
[C_hist(V_min)-delta_V]-[C_hist(W)-delta_mom(B,W)]
 =lambda[B_R+(LB_R(B)-(m-1)A)/2].                       (20)
```

In particular the diagonal has not disappeared: it is `(m-1)A/2`
after the A/2 in capacity has been counted exactly once.

## 6. A concrete normalized good-epoch estimate for this carrier

Let `bar_d=A/Q` be the average absolute source magnitude. Removing
all magnitudes below r cannot decrease that average. Thus, whenever
Q_r>0, `mu_r/Q_r>=bar_d`, and hence

```
I >= bar_d^2 M.                                        (21)
```

This also follows by ordering the magnitudes and comparing the
average of an upper tail with the full average. It uses the actual
labels, with their signed multiplicity two.

A direct first-moment bound at a good epoch is stronger than what
is obtained just by converting the variance lower bound. Write
N=2p, p even, and assume

```
H_p>=2H_(p/2),   H=H_N<=K H_p,   H_(2N)<=K H,
```

with K=32 for the previously proved two-lookahead good epochs.
Every cross gap from indices `1,...,p/2` to indices `p+1,...,2p`
is at least `H_p/2`. There are p^2/2 such positive differences,
all distinct by actual Sidonness. Doubling for the signed bank gives

```
A >= p^2 H_p/2 >= N^2 H/(8K) >= Q H/(8K).               (22)
```

Put `kappa=1/(8K)`; at K=32, kappa=1/256. Equations
(16), (21), and (22) imply

```
I/M >= kappa^2 H^2,       A/M <= 1/(kappa Q).            (23)
```

The next actual block has m=N and L<=K H, so T<=(K+2)H.
Under one fixed eventual cap `H<=C N^2 log(2N)`, equation (20),
Born positivity, and (23) yield the proved raw row bound

```
gain/M >= 6lambda kappa^2/[(K+2)^3 C log(2N)]
                         -lambda/(2 kappa N).           (24)
```

For K=32 the first denominator is `34^3 C log(2N)`.
The negative term follows from `(N-1)/Q=1/N`.

For positive-part demands the needed raw positivity also holds
eventually. From (16) and (22), `M/A>=A/H>=kappa Q`, so the
mass-only demand of W is at least

```
(N A/2)[kappa(N-1)/((K+2)C log(2N))-(1+lambda)].         (25)
```

This is eventually positive; the background demand is larger and
the moment term is nonnegative. Thus (24) also applies to the
specified positive-part comparison beyond one fixed initial range.
On the previously proved good dyadic epochs, its positive
reciprocal-log scale is individually nonsummable, while its 1/N
cost is summable. This is a statement about these individual rows,
not a completed global budget comparison.

## 7. The single physical envelope and the baseline boundary

For a finite family of selected old ranks n_i and actual compatible
future blocks B_i, suppose their physical difference sets are
pairwise disjoint. Use the literal restrictions of the permanent
W in (14), their actual masses M_i, diameters H_i, spans L_i,
and demands delta_i from (19). The exact one-budget inequality is

```
sum_i max(delta_i,0)/M_i
 <= sum_(t>0) max_i {
      1[t notin F_(n_i)] 1[t<=L_i-1] K_(W|Fhat_(n_i))(t)/M_i
    }.                                                  (26)
```

Each physical t belongs to at most one actual future block and
its one eligible coefficient is bounded by the displayed maximum.
This proves (26) without summing an independent historical capacity
per row, or per threshold. All source labels, output masks, actual
spans and normalizations remain explicit.

The permanent unnormalized coefficients improve compatibility under
extension. However division by the changing M_i means that the
right side of (26) is not the fixed-terminal historical capacity
from (17), divided by a freely chosen common mass. This note does
not bound that shared maximum or show that the row gains in (24)
beat its baseline margin.

There is also an exact baseline warning. At lambda=1, W has zero
opposite-sign entries and value `2min(d,e)` on the positive block,
with its reflected copy on the negative block. If V_+ is the
positive-bank matrix `min(d,e)`, then at every physical output

```
K_W(t)=4K_(V_+)(t),       M=4M(V_+).
```

Thus the normalized kernel equals the positive-bank weighted-minimum
kernel. This equality persists under common old-label and span
masks, and under maxima over the same row family. The endpoint of
this signed family is an existing type of positive weighted carrier,
not an automatic improvement over every positive-bank baseline.

The established progress is therefore concrete but bounded: the
source-radius boundary is exact; dD integration is repaired at a
finite terminal cutoff; upper-tail features supply a finite coherent
PSD/nonnegative carrier with full Born positivity; its mass, trace,
future demand and actual shared envelope are all specified. The
remaining global physical-margin argument and original Q1 are open.
