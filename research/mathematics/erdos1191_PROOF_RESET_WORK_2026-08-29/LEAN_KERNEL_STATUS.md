# Lean kernel status — 2026-08-30

## Outcome

**Kernel status: `L1_FORMALIZED_L3_GENERIC_PARTIAL`**

The project in `lean_kernel/` builds with no `sorry`, `admit`, or project-defined
axiom. It formalizes Module L1, the general finite identities from L3, and a
selective generic finite ownership/change-of-basis kernel. It does **not**
formalize, prove, or assert Q1 or Q2. L2, the Wave-specific part of L3, L4, and
L5 remain open formalization work.

## Pinned environment and verification

- Lean toolchain: `leanprover/lean4:v4.33.0`
- Lean binary commit: `d8b18978322de05a8f3dba51ef03cf5461676c17`
- mathlib commit: `db584cd6d46c92f209a44c0f1c829460d327499d`
- mathlib tag at that commit: `master-2026-08-10`
- Final MCP command: `lean_build(clean=true)`
- Final direct command: `lake build`
- Final build exit: `0`
- Final MCP clean result: `Build completed successfully (1054 jobs).`
- Final direct result: `Build completed successfully (1047 jobs).`
- Axiom-audit command: `lake env lean Erdos1191/AxiomAudit.lean`
- Axiom-audit exit: `0`
- Forbidden source token scan (`sorry|admit|axiom`, singular, project Lean
  sources only): no matches, normalized exit `0`

Evidence is preserved in:

- `lean_kernel/evidence/environment.txt`
- `lean_kernel/evidence/clean_build.txt`
- `lean_kernel/evidence/axioms.txt`
- `lean_kernel/evidence/source_scan.txt`

An independent theorem-by-theorem natural-language derivation is preserved in
`LEAN_KERNEL_PROSE_AUDIT.md`.  It covers every theorem listed below and uses
the same zero-based, half-open-interval conventions.

The recorded build starts from cleaned generated targets in the pinned local
dependency checkout.  A second literal copy/extract into a new directory was
not performed, so that release-style extracted-copy replay remains pending
even though the formal clean-build and axiom gates passed.

The `.lake/` directory was a generated dependency/build cache, not a proof
artifact. It is intentionally removed from the handoff after verification.
`lake-manifest.json` preserves the resolved revisions of mathlib and every
inherited dependency.

## L1 statements actually formalized

Source modules:

- `lean_kernel/Erdos1191/Sidon.lean`
- `lean_kernel/Erdos1191/GapVector.lean`

Exported theorem names and their precise roles:

1. `Erdos1191.additiveSidonNat_iff_additiveSidon`
   - Proves that the direct natural-number sum equation and its integer-cast
     version define the same unique-unordered-sum property.
2. `Erdos1191.additiveSidonNatUpTo_iff_additiveSidonUpTo`
   - The same cast-invariance theorem for a finite prefix through index `N`.
3. `Erdos1191.additiveSidon_iff_positiveDifferenceUnique`
   - For a strictly increasing natural enumeration, unique unordered sums are
     equivalent to uniqueness of every nonzero positive endpoint difference.
4. `Erdos1191.additiveSidonNat_iff_positiveDifferenceUnique`
   - Direct natural-sum formulation of theorem 3.
5. `Erdos1191.additiveSidonUpTo_iff_positiveDifferenceUniqueUpTo`
   - Finite-prefix version of the sum/difference equivalence.
6. `Erdos1191.sum_adjacentGap_Ico`
   - Exact telescope
     `sum_{r in [i,j)} (a_(r+1)-a_r) = a_j-a_i`, including the empty case
     `i=j`.
7. `Erdos1191.positiveDifferenceUniqueUpTo_iff_contiguousGapSumsUniqueUpTo`
   - A finite ruler is Golomb exactly when all nonempty contiguous gap sums are
     unique.
8. `Erdos1191.additiveSidonUpTo_iff_contiguousGapSumsUniqueUpTo`
   - Finite integer-cast sum version of the Sidon/contiguous-gap equivalence.
9. `Erdos1191.additiveSidonNatUpTo_iff_contiguousGapSumsUniqueUpTo`
   - Direct natural-sum version of theorem 8; this is the closest literal Lean
     match to L1's finite-ruler claim.
10. `Erdos1191.adjacentGap_pos`
    - Every adjacent gap of a strictly increasing natural enumeration is a
      positive `Int` (hence a positive integer).
11. `Erdos1191.adjacentGap_injectiveUpTo`
    - Under the finite Golomb property, equality of two adjacent gaps forces
      equality of their indices.
12. `Erdos1191.adjacentGaps_positive_and_distinct`
    - Packages positivity and pairwise distinctness.
13. `Erdos1191.emptyInterval_endpointMutation_is_false`
    - Red-team theorem: replacing the strict nonempty interval hypotheses by
      weak inequalities is false, because `[0,0)` and `[1,1)` are distinct
      empty intervals with equal sums.

### Index and arithmetic conventions

- Lean indices are zero-based. Lean `a r` corresponds to the paper's
  one-based `a_{r+1}` when the prose enumeration starts at `a_1`.
- `adjacentGap a r = (a (r+1) : Int) - a r`.
- `Finset.Ico i j` contains `i,...,j-1`; therefore the telescope's right
  endpoint is `a j`.
- A prefix through endpoint index `N` contains values `a 0,...,a N` and gaps
  with indices `0,...,N-1`.
- Differences are deliberately represented in `Int`. Natural subtraction is
  never used in the kernel, so no negative quantity can be silently truncated.
- The finite-prefix equivalence assumes global `StrictMono a`, matching an
  increasing infinite enumeration. It does not claim that a merely unordered
  finite array is covered.

## L3 finite telescope / Abel work

Source module: `lean_kernel/Erdos1191/AbelFinite.lean`.

Formalized:

- `Erdos1191.sum_forwardDiff_range`: exact group-valued finite forward-
  difference telescope, valid also at `n=0`.
- `Erdos1191.finiteAbel_range`: exact finite summation-by-parts formula over
  `0,...,n-1`, with terminal and coefficient-difference terms exposed.
- `Erdos1191.finiteAbel_rational_fixture`: exact horizon-four rational fixture;
  original sum `113`, terminal term `192`, repayment contribution `79`.

`finiteAbel_range` is proved against mathlib's primary theorem
`Finset.sum_range_by_parts` from `Mathlib.Algebra.BigOperators.Module` at the
pinned commit. This avoids re-proving a standard algebraic identity while the
wrapper fixes the exact multiplication/coefficient convention used here.

Not formalized in L3:

- the project-specific arrays `Y_m`, `R_m`, and `Z_m`;
- the Wave 12 identity
  `sum Y = R_4 - R_terminal + sum Z`;
- the project-specific dyadic epoch schedules, weights, and boundary
  instantiations.

Those are not marked complete because the reset package does not yet provide a
single stable Lean definition of each project-specific array and coefficient
map. The generic algebraic engine is certified; the research-specific
instantiation remains a separate obligation.

## Standard axioms reported by Lean

`#print axioms` reports only Lean/mathlib standard axioms among
`propext`, `Classical.choice`, and `Quot.sound`; one theorem
(`adjacentGap_injectiveUpTo`) reports no axioms. There is no custom axiom and no
`sorry`. The exact theorem-by-theorem output is in
`lean_kernel/evidence/axioms.txt`.

## Exact blockers for L2, L4, and L5

### L2 — critical-cap equivalence: not implemented

A correct implementation still needs a stable formal definition of the
counting function for the enumerated set, explicit eventual quantifiers, and
the analytic inversion between
`A(x)*sqrt(log x/x)` and `a_n <= C*n^2*log(2*n)`. The two directions require
explicit logarithm-domain and monotonicity constants. Weakening this to a
sequence-only or subsequence-only statement would not certify E0, so no such
weaker theorem was substituted.

### L4 — triangular floor: not implemented

The current kernel proves only the input fact that adjacent gaps are distinct
positive integers. It does not yet prove the exact sum lower bound, interior
coefficient arrays, Wave 11 nonnegative decomposition, or explicit replacement
for every `O(1)` term. These require the canonical Wave 11 coefficient
definitions before a theorem statement can be frozen.

### L5 — Wave 13 harmonic obstruction: not implemented

None of the cross-ratio, layered `E_m`, polynomial lower bound, critical-cap
consequence, harmonic dyadic accumulation, or P17/P18 target-equivalence nodes
is claimed Lean-complete. The quantifier audit must first freeze their exact
eventual-branch statements. Formalizing a target-equivalent weakened version
would be misleading and was not done.

## Reproduction from a cache-free handoff

From `lean_kernel/`:

```sh
elan toolchain install leanprover/lean4:v4.33.0
lake update
lake clean erdos1191
lake build
lake env lean Erdos1191/AxiomAudit.lean
rg -n '\b(sorry|admit|axiom)\b' --glob '*.lean' .
```

For the last command, `rg` exit `1` means no forbidden declaration/token was
found; the recorded verification normalizes that expected empty result to exit
`0`.

## Claim boundary

This is a verified finite proof kernel, not a solution of Erdős Problem #1191.
Its safe registry label is `FORMAL_THEOREM` only for the theorem names listed
in this document. Q1, Q2, E0/L2, Wave-specific L3, L4, and L5 remain `UNRESOLVED` or
`NOT_FORMALIZED` as specified above.

## MCP reachability refresh — 2026-08-30

Lean MCP is actually reachable: project build, minimal-code compilation,
file diagnostics, and `lean_verify` all succeeded on the pinned toolchain.
The fresh clean MCP gate rebuilt 1,054 jobs, the following direct Lake gate
reported 1,047 jobs, and the source/axiom scans remain clean.  Exact details
are in `FORMAL_TOOLCHAIN_REACHABILITY_2026-08-30.md`.

The original Rocq/Coq MCP command was not reachable because `uvx rocq-mcp`
looked for a nonexistent registry package.  The entry is now repaired and
pinned to official source commit
`6983113d0844c0b7f987c79dab13988445109bfb`, with a small `rocq compile`
compatibility wrapper for Rocq 9.1.1.  A fresh direct stdio session exposed 13
tools; `rocq_health`, a minimal `rocq_compile`, `rocq_verify`, both canonical
file compiles, and five `rocq_assumptions` calls all succeeded.  Exact evidence
is in `../evidence/rocq_mcp_reachability_2026-08-30.txt`.

## C133 adjacent-epoch ledger refresh — 2026-08-31

Source module: `lean_kernel/Erdos1191/AdjacentEpochLedger.lean`.

The new exported theorem

`Erdos1191.adjacentEpochTwoEdgeFourScaleLedger`

proves the fully expanded adjacent epoch-8/epoch-16 four-scale ledger over an
arbitrary commutative ring.  It has four initial-prefix rows, four net shared
rows, four final-prefix rows, and two explicit upper scale terminals.  This is
the `L=0,m=1,n=4` finite C103 specialization used by C133; it contains no
phase, sign, positivity, owner-capacity, physical-history, or arbitrary-rank
claim.

The module is imported by `Erdos1191.lean` and its theorem is printed by
`AxiomAudit.lean`.  The current direct `lake build` completed 1,069 jobs, and
the theorem reports only `propext`, `Classical.choice`, and `Quot.sound`.
Independent exact arithmetic checks 512 deterministic rational fixtures, the
18-to-14 shared-row stitch, the 100-coordinate owner partition, both birth
cases, and the live rank-15 row.  See
`evidence/C132_C134_FINAL_VERIFICATION_2026-08-31.md`.

Rocq MCP is currently reachable on Rocq 9.1.1.  A minimal sandbox theorem and
the existing independent `prefixScaleCurl` audit both pass with empty
assumptions.  C133 was not expanded into a second full Rocq polynomial proof,
because the main research budget remains the finite joint C058 master rather
than whole-workspace proof-assistant translation.

## Selective C066 finite transport kernel — 2026-08-30

After the prose formulation was frozen, `Erdos1191/PrefixScaleFinite.lean`
formalized exactly the finite algebraic layer needed to protect C058 from
sign and boundary transcription errors:

- `prefixScaleCurl`;
- `finiteScaleAbel_terminal`, including `n=0` and the terminal scale row;
- `finiteEpochFlux_range` and `finiteGridDivergence_range`;
- `finiteEpochScaleAbel_transport`, with the initial prefix boundary, final
  prefix boundary, every interior epoch coefficient difference, and every
  scale-terminal term explicit; and
- `finiteEpochScaleAbel_transport_fromPotential`, which defines the prefix
  increment and retained scale band from one potential `C` and discharges the
  curl hypothesis algebraically.

MCP diagnostics are empty.  `lean_verify` reports only `propext` for the curl
and only `propext`, `Classical.choice`, and `Quot.sound` for the finite-sum
theorems, with no suspicious-source warnings.  The source SHA-256 is
`6c88a6c065c23a780f32b49913d9418720e00f168412b6fbab948e95d22ad744`.

As a deliberately small independent audit, Rocq 9.1.1 proves only the curl in
`../rocq_kernel/PrefixScaleFiniteAudit.v`; `Print Assumptions` reports `Closed
under the global context`.  Both the local CLI and the repaired Rocq MCP full
compile/assumption paths are green.

These are `FORMAL_THEOREM` results only for the displayed finite identities.
They prove no positivity, analytic limit, project-specific ownership
allocation, C058, Q1, or Q2.  Further finite statements become eligible for
Lean only after their mathematical formulation stabilizes; C058 research
remains primary.

## Selective finite ownership/change-of-basis kernel — 2026-08-30

After their mathematical formulation was frozen,
`Erdos1191/OwnershipFinite.lean` added only the generic finite identities
needed to protect C058 bookkeeping from a sign or ownership transcription
error:

- `finiteSignedPrimitiveToNetRow` commutes a signed primitive sum with the
  net-row sum over an arbitrary commutative ring, before any inequality;
- `ownerFiberPartitionSum` proves that owner-map fibers count every finite
  coordinate exactly once;
- `ownerQuadraticShares_sum` specializes that partition to coordinate rows of
  a finite quadratic form; and
- `finiteQuadraticEnergy_eq_doubleSum` identifies the row-expanded form with
  the usual finite double sum `sum_i sum_j q_i X_(i,j) q_j`;
- `fejerRatio_three` checks the exact rational value `4/9` at `m=3`; and
- `fejerRatio_ge_nineSixteenths` proves the finite rational bound
  `((m-1)/m)^2 >= 9/16` for every natural number `m>=4`.

MCP diagnostics are empty.  `lean_verify` reports only `propext`,
`Classical.choice`, and `Quot.sound` for all six theorems and no suspicious
source pattern.  The source SHA-256 is
`8800ef4f04a478af7a27de80b19806ceda4fd5c34f76415d1134e825a9e41097`.

Rocq 9.1.1 independently proves the corresponding finite-list theorems
in `../rocq_kernel/OwnershipFiniteAudit.v` from explicit algebraic laws valid
in every commutative ring.  All four `Print Assumptions` checks report `Closed
under the global context`; `rocq compile` and `rocq check` both exit zero.  Its
source SHA-256 is
`5e090ca8af73523bf75f034be2e235163284d0ef95f3496ea20765c9f6d41a23`.
The repaired Rocq MCP also compiles the file in full and returns
`assumptions=[]` for all four theorems.

These theorems do not select a project-specific owner, prove a birth/gate
condition, establish project transport positivity, or prove C058.  They
certify only frozen finite algebra.  C058 remains the sole primary research
bottleneck.

## Frozen global-owner stitching obstruction — 2026-08-31

The exact three-coordinate countermodel to automatic local-owner stitching is
now part of `Erdos1191/OwnershipFinite.lean`.  Lean proves:

- symmetry and zero row sums for both local rank-one Laplacian matrices;
- `q^T X_1 q=(q_0-q_1)^2` and `q^T X_2 q=(q_0-q_2)^2` for every rational
  vector, hence both PSD inequalities;
- fixed local energies `1` and `1`, and summed energy `2`;
- the two exact local owner shares;
- the global share formula `2` or `0` according to the owner of the shared
  coordinate; and
- `threeCoordinateTwoOwnerStitchingObstruction`.

The pinned Lean 4.33.0 project completed 1,067 jobs.  The expanded explicit
axiom audit reports only `propext`, `Classical.choice`, and `Quot.sound`, with
no native-decision trust axiom or source hole.  The current source SHA-256 is
`7a7d691f14b3b65a08dc78a99b7f5482aaa8294a45e52cc2b4cfcca87b0c88ea`.

After that statement stabilized, Rocq 9.1.1 independently audited the fixed
integer matrix/share obstruction using Corelib alone.  Both symmetries, both
row-sum facts, local energies, global energy, local shares, the `2/0` global
branch, and the final obstruction compile closed under the global context;
all ten new assumption queries are empty.  The current Rocq source SHA-256 is
`12f54f6d24972777e1fc7f1d01d633f818e0fb7d0ec5d513171fc87eba863952`.

This formal result refutes only automatic stitching into one coordinate-row
owner map.  It does not refute a jointly optimized global Gram, cross-block
slack, fractional ownership with a new legal ledger, C058, Q1, or Q2.
Formalization remains secondary to the enriched phase-integrated C058 search.


## Frozen C121 scalar coefficient barrier — 2026-08-31

After the exact finite C121 statement stabilized,
`Erdos1191/CoefficientBarrier.lean` added only three rational/sign theorems:

- `c118CoefficientBarrier_value`, the exact reduced rational identity;
- `c118NecessaryCoefficientBarrier`, the implication from the frozen master
  row and sign hypotheses to the strict lower bound on `B`; and
- `c118OneThirdCoefficientBoxNoGo`, the contradiction with `B<=1/3`.

A test-first consumer failed on the missing theorem before implementation.
The pinned Lean 4.33.0 project then completed 1,068 jobs.  MCP diagnostics are
empty, theorem verification reports only `propext`, `Classical.choice`,
and `Quot.sound`, and minimal-hypothesis checks show the stated sign and row
hypotheses are load-bearing.  Source SHA-256 is
`12fd7dc86110684048bd591cbafe678956bb08506fbd8a033449b39ae1a45f98`.

After the Lean statement froze, Rocq 9.1.1 independently checked the
denominator-cleared ratio identity and the strict comparison with `1/3` in
`../rocq_kernel/CoefficientBarrierAudit.v`.  Full MCP compile succeeds and
both assumption queries return empty assumptions.  Its source SHA-256 is
`11594493ce15c078bc3d823f50bbb8d010840f00bd68928219b3d274d61d5018`.

These files audit only the finite rational consequence of the exact
certificate.  They do not formalize the dual/LDL/atanh replay, a larger cone,
C058, Q1, or Q2.  Formalization remains subordinate to the complete-phase
outer coefficient-bank search.

## C138 same-atom adjacent-ledger refresh — 2026-08-31

After the cumulative potential was mathematically frozen,
`lean_kernel/Erdos1191/SameAtomAdjacentLedger.lean` added only the finite
algebra needed to guard the C138 formulation.  It defines

`C8=B`, `C16=B+U8`, and `C32=B+U8+U16`,

proves that the adjacent prefix increments are exactly `U8` and `U16`, and
specializes C133's exact `4+4+4+2` ledger without dropping either terminal.
The terminal-zero theorem is hypothesis-guarded by `U8 4 = 0` and
`U16 4 = 0`; it does not infer those fixture facts.

The module is imported by the root and its load-bearing ledger theorem is in
`AxiomAudit.lean`.  Direct `lake build` completed 1,070 jobs.  The audit
reports only `propext`, `Classical.choice`, and `Quot.sound`; source scans find
no `sorry`, `admit`, or project-defined axiom.  The module SHA-256 is
`97607dd6425a93a2845e8c55e55c5b106e61ed6d2f2fbd61de06c764ff68e0c9`.

This is a parallel finite verifier only.  It proves no owner inequality,
terminal vanishing on an arbitrary history, phase interval, arbitrary-rank
promotion, C058, Q1, or Q2, and it does not change the main research priority.
