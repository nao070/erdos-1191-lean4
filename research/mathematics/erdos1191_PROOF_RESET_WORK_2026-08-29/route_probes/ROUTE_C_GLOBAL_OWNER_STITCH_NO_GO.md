# Route C: exact global coordinate-owner stitching obstruction

Date: 2026-08-31  
Status: `FORMAL_FINITE_GLOBAL_OWNER_STITCH_NO_GO_C058_OPEN`

This note isolates a narrow gap between C111's owner-fiber identity and a
global owner construction.  Local PSD blocks may each be feasible after
assigning their shared coordinate to different owners, while no single global
coordinate owner map retains both local payments.  This is a finite
bookkeeping obstruction, not a failure of every global Gram construction.

## 1. Exact three-coordinate fixture

Use coordinates `s,a,b`, owners `A,B`, and

\[
 q=(1,0,0),
\]

\[
 X_1=\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&0\end{pmatrix},
 \qquad
 X_2=\begin{pmatrix}1&0&-1\\0&0&0\\-1&0&1\end{pmatrix}.
\]

Both matrices are symmetric and have zero row sums.  More strongly,

\[
 q'^{T}X_1q'=(q'_s-q'_a)^2\ge0,
 \qquad
 q'^{T}X_2q'=(q'_s-q'_b)^2\ge0
\]

for every rational vector `q'`; hence each local matrix is positive
semidefinite.  On the displayed test vector, both local energies equal one.

In the first local block, assign the shared coordinate `s` to `A`; in the
second, assign it to `B`.  The corresponding local owner shares are exactly
one.  Thus the two blocks separately meet the two unit demands.

## 2. Why one global owner cannot retain both shares

The summed matrix is

\[
 X=X_1+X_2=
 \begin{pmatrix}2&-1&-1\\-1&1&0\\-1&0&1\end{pmatrix},
 \qquad q^TXq=2.
\]

For any single global map `owner:{s,a,b}->{A,B}`, only the coordinate row at
`s` contributes on `q=(1,0,0)`.  Consequently the two global shares are

\[
 (2,0)\quad\hbox{or}\quad(0,2),
\]

according to the unique owner of `s`.  In either case at least one owner's
share is strictly below its local unit demand.

Therefore the implication

> local block owner feasibility + PSD summation automatically yields one
> global coordinate-owner fiber retaining every local demand

is false, even for two rank-one Laplacian blocks on three coordinates.

## 3. Formal verification

Lean 4.33.0 kernel-checks the fixture in
`lean_kernel/Erdos1191/OwnershipFinite.lean`.  The load-bearing declarations
include:

- `threeCoordinateOwnerStitchMatrixLeft_symmetric` and its right analogue;
- `threeCoordinateOwnerStitchMatrixLeft_rowSum` and its right analogue;
- the two exact square-energy and nonnegativity theorems;
- `threeCoordinateOwnerStitchLocalEnergies` and
  `threeCoordinateOwnerStitchEnergy`;
- `threeCoordinateOwnerStitchLocalLeftShare` and its right analogue;
- `threeCoordinateOwnerStitchShare`; and
- `threeCoordinateTwoOwnerStitchingObstruction`.

The project and explicit axiom audit build cleanly.  The new theorem family
uses only `propext`, `Classical.choice`, and `Quot.sound`; there is no
`sorry`, `admit`, custom axiom, or native-decision trust axiom.

After the Lean statement stabilized, the small self-contained Rocq audit in
`rocq_kernel/OwnershipFiniteAudit.v` independently checks the exact finite
owner obstruction and its fixed local/global values.  Rocq is deliberately
used here only as a second audit, not as a workspace-wide translation.

## 4. Exact scope boundary

The fixture refutes only automatic stitching into one **coordinate-row owner
map**.  It does not refute:

- a different global PSD Gram matrix optimized jointly across blocks;
- extra cross-block or cross-epoch slack;
- a construction whose blocks are genuinely disjoint;
- fractional ownership with a separately proved legal ledger;
- an owner system on larger physical objects rather than coordinates;
- C058, either Erdős question, novelty, or prize eligibility.

Accordingly, future C058 arguments may still use local PSD blocks, but they
must construct the global owner ledger explicitly.  C111's fiber partition
proves exact accounting only after such a genuine global owner map has been
supplied.
