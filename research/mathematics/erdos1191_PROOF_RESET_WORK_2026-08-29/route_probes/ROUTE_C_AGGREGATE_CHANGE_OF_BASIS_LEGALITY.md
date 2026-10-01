# Route C: aggregate signed change-of-basis legality

Date: 2026-08-30  
Status: `FORMAL_FINITE_IDENTITY_WITH_AUDITED_ROUTE_C_INSTANTIATION`

This note resolves one narrow bookkeeping question raised by C107--C110:
primitive-occurrence nonnegativity is not required to replace a finite signed
four-corner expansion by its net Gothic rows.  The conclusion is algebraic
and finite.  It does not choose a global owner for rows shared by different
epoch pairs and does not prove C058.

## 1. Signed primitive aggregation

Let `P` be a finite set of primitive occurrences, `C` a finite set of physical
coordinates, `a(p,c)` a signed coefficient, and `v(c)` a value in a
commutative ring.  Define the net physical row

\[
 A(c)=\sum_{p\in P}a(p,c).
\]

Then finite distributivity gives

\[
 \sum_{p\in P}\sum_{c\in C}a(p,c)v(c)
 =\sum_{c\in C}A(c)v(c).
\tag{1}
\]

No sign condition occurs in (1).  A positive primitive occurrence may cancel
with a negative occurrence before the net row is paid.  Therefore C109's
primitive countercell refutes only the stronger primitivewise-capacity
interpretation; it does not refute the aggregate equality.

For the whole-stencil fixture, the certificate independently verifies all 24
primitives, 96 signed corners, 42 nonzero net Gothic rows, 28 mixed-sign reused
rows, and all 46 identities `lambda=2M`.  Thus (1) instantiates exactly to the
C107/C112 finite Gothic replacement.

## 2. One-time coordinate ownership

Let `o:C->O` be any owner map.  Its fibers partition `C`, so

\[
 \sum_{u\in O}\sum_{c:o(c)=u}v(c)=\sum_{c\in C}v(c).
\tag{2}
\]

For a finite quadratic form, define the coordinate row share

\[
 S(c)=q_c\sum_d X_{c,d}q_d.
\]

Then

\[
 \sum_{u\in O}\sum_{c:o(c)=u}S(c)
 =\sum_{c,d}q_cX_{c,d}q_d=q^TXq.
\tag{3}
\]

Neither symmetry, positive semidefiniteness, nor zero row sums is needed for
the equality (3); those hypotheses enter elsewhere when a nonnegative master
price is required.  The C107/C112 owner convention assigns the shared
coordinate `a_7` once, to the past block, so its eight finite owner rows sum
cellwise to the one physical quadratic energy.

## 3. Formal verification

Lean 4 proves (1)--(3) as

- `finiteSignedPrimitiveToNetRow`;
- `ownerFiberPartitionSum`;
- `ownerQuadraticShares_sum`; and
- `finiteQuadraticEnergy_eq_doubleSum`

in `lean_kernel/Erdos1191/OwnershipFinite.lean`.  The project builds on the
pinned Lean 4.33.0 toolchain, and `lean_verify` reports only standard logical
foundations (`propext`, `Classical.choice`, and `Quot.sound`) with no suspicious
source pattern.

After those statements stabilized, Rocq 9.1.1 independently proved the four
finite-list counterparts in `rocq_kernel/OwnershipFiniteAudit.v`.  The repaired
Rocq MCP compiles the file in full and reports `assumptions=[]` and `Closed
under the global context` for each theorem.

## 4. Exact boundary of the conclusion

Equations (1)--(3) justify replacing one already singly owned finite Gothic
ledger by its net signed row basis and then partitioning the resulting
quadratic energy by a genuine coordinate owner map.  They do not show that a
row appearing in two adjacent epoch-pair constructions may be used twice.
They also do not provide a birth, initial, cutoff, final, or scale-terminal
owner, an arbitrary-history PSD witness, a phase-integrated margin, or a
horizon-uniform master inequality.

Thus aggregate signed change of basis is legal; the remaining ownership
problem is global selection across overlapping finite blocks, not
primitivewise positivity inside one block.
