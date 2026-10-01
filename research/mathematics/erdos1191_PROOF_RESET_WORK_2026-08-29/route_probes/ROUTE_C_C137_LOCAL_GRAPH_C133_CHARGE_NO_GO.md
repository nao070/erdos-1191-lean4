# C137 local graph-to-C133 charge-map no-go

Date: 2026-08-31 (Asia/Tokyo)  
Status: `EXACT_LOCAL_GRAPH_TO_C133_BOX_CARRIER_CHARGE_NO_GO_C058_OPEN`

This is an exact finite no-go for a specified bridge class.  It concerns only
the explicit 32-mark fixture, phase `t=17745/32`, current 100-channel/57-root
graph, and the one-sided box-pair carrier used to instantiate the frozen C133
fourteen-row identity.  It is not a no-go for C058.

## 1. Objects compared

The graph state has coordinates

```text
q_(r,m)(x) = (8/m) Haar_(m t)(x-P_r),
7 <= r <= 31,  m in {1,2,4,8}.
```

Thus `q(x)` has 100 coordinates.  The exact graph energy is a positive sum of
57 supported root squares `(q_i-q_j)^2`.  The direct owner demands use the
same graph state with the full `M8` and `M16` point matrices.

The audited C133 potential is the different one-sided box-pair carrier

```text
C_(P,s)(x) = (a_(P,s)(x)^2-a_(P,s)(x))/(2^s t)^2,
a_(P,s)(x) = sum_(r<P) 1_[P_r,P_r+2^s t)(x).
```

The exact Abel identity produces 12 band rows and two scale-4 terminal rows.

## 2. Decisive full-state collision

On the adjacent exact carrier cells

```text
I_a = [616,20401/32),
I_b = [20401/32,21009/32),
```

the complete 100-coordinate graph states are equal.  Their common exact hash
is

```text
652c2c363064464469d8d7ca1eb6931d7dd8cc1dc6e0703ac16e24d847c345d3.
```

All 57 supported root-square features and all eight direct demands vanish on
both cells.  Nevertheless the C133 totals are

```text
L(I_a) = 64/104961675,
L(I_b) = 176/314885025,
```

and the fourteen-row vectors have different exact hashes.

Therefore no pointwise memoryless function of the complete graph state can
equal either the C133 total or the fourteen-row vector.  This immediately
rules out fixed scalar, owner-block, multiplier-diagonal, affine, and linear
root-feature maps as special cases.

The obstruction is structural: the box carrier changes at carrier-only
endpoints that the graph state does not record.

## 3. Both terminal rows fail the same locality gate

On

```text
J_a = [35101/4,17745/2),
J_b = [17745/2,17789/2),
```

the complete graph state is again identical, but both terminal rows change:

```text
terminal:e8:s4   23/83969340    -> 1/3998540,
terminal:e16:s4  141/223918240 -> 27/44783648.
```

There are also individual zero-capacity witnesses:

```text
[616,20401/32):
  all supported root features = 0,
  all direct demands           = 0,
  terminal:e8:s4               = 1/41984670;

[23063/2,25163/2):
  all supported root features = 0,
  all direct demands           = 0,
  terminal:e16:s4              = 27/358269184.
```

Thus neither nonzero terminal can be paid by a pointwise homogeneous charge
from the present root/direct feature bank.

## 4. Scalar countercells

No constant pointwise scalar identifies the graph energy or weighted direct
demand with the C133 total:

```text
[513,17745/32):
  graph energy = 21/256,
  C133 total   = 0;

[616,20401/32):
  graph energy = 0,
  C133 total   = 64/104961675;

[44701/4,46081/4):
  weighted direct demand = 225/32768,
  C133 total             = 0.
```

The middle countercell also rules out any finite pointwise domination of the
positive C133 total by the graph energy.

## 5. Integrated values are not a bridge

Exact integration over all 191 joint cells gives

```text
graph price P                = 1878008419901/9402974208,
unweighted direct D          = 457/4,
weighted direct Dw           = 1305537/16384,
box-carrier C133 integral I  = 10229179/1007632080.
```

The exact ratios are

```text
P/I  = 13141260627794152945/667949349347328,
D/I  = 115121965140/10229179,
Dw/I = 82218810176685/10474679296.
```

These are post-hoc fixture ratios.  Any two nonzero finite integrals admit a
fitted scalar; no universal charge identity follows.

## 6. Exact claim boundary and next hypothesis

Proved here:

- no arbitrary pointwise function of the current full graph state recovers
  the box-carrier C133 total, fourteen-row vector, or both terminal rows;
- consequently no local scalar, diagonal, owner-block, affine, or linear
  supported-root charge map works;
- exact countercells and exact integrated values replay with rational
  arithmetic only.

Not ruled out:

- nonlocal cross-cell or phase-integrated signed transport;
- an enlarged channel bank carrying initial A8 history and extra boundary
  data;
- a new potential built from the same signed M8/M16 atoms as the direct
  demands.

The next missing hypothesis is precisely such a same-atom potential or a
genuinely nonlocal transport identity.  It must produce the frozen C133 rows,
carry the initial A8 history and both scale-4 terminal balances, and avoid
fixture-fitted coefficients and future information.

C058, Q1, and Q2 remain open.

## 7. Reproduction

The primary verifier is standalone and stdlib-only.  The independent oracle
does not import it and reconstructs the load-bearing state collisions and
terminal values from the fixture formulas.

```bash
python3 route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_certificate.py \
  --verify --self-check
python3 route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_independent_oracle.py
python3 route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_test.py
```
