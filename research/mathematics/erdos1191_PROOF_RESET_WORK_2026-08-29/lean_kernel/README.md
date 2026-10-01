# Erdős Problem 1191: Lean proof kernel

This project formalizes a finite foundational kernel only. It does not state or
prove Q1 or Q2.

Pinned environment:

- Lean: `leanprover/lean4:v4.33.0`
- mathlib: `db584cd6d46c92f209a44c0f1c829460d327499d`

Reproduce from this directory:

```sh
elan toolchain install leanprover/lean4:v4.33.0
lake update
lake build
lake env lean Erdos1191/AxiomAudit.lean
```

The committed `lake-manifest.json` pins mathlib and every inherited dependency.
Generated `.lake/` content is intentionally excluded from the handoff.

`Erdos1191/PrefixScaleFinite.lean` contains only the frozen finite
prefix/scale curl and one- and two-dimensional Abel identities, with all
finite boundary and terminal terms explicit.  It is a parallel verifier for
C058 bookkeeping, not a formalization of C058, Q1, or Q2.

`Erdos1191/AdjacentEpochLedger.lean` expands the two adjacent epoch-8/16
four-scale case into fourteen unique rows: four initial, four net shared, four
final, and two upper scale terminals.  It is the finite C133 bookkeeping
contract only; it does not prove a phase rule, positive capacity, arbitrary
history, C058, Q1, or Q2.

`Erdos1191/SameAtomAdjacentLedger.lean` specializes that frozen ledger to
`C8=B`, `C16=B+U8`, and `C32=B+U8+U16`.  It proves that the two prefix
increments are exactly the same direct atoms `U8` and `U16`, retains both
upper terminal rows, and permits terminal deletion only under explicit
`U8 4 = U16 4 = 0` hypotheses.  It is finite algebra only and makes no
fixture, positivity, phase, ownership, arbitrary-history, C058, Q1, or Q2
claim.

`Erdos1191/OwnershipFinite.lean` contains only frozen finite ownership and
change-of-basis bookkeeping: signed primitive-to-net-row sum interchange,
owner-map fiber partition, and the specialization showing that coordinate-row
owner shares sum exactly to the finite quadratic form.  It does not assert
that a project-specific owner map is legal or that a C058 inequality holds.
The same module also records the isolated finite rational Fejér checks
`((3-1)/3)^2=4/9` and `((m-1)/m)^2>=9/16` for `m>=4`.
