# Formal toolchain reachability — 2026-08-30

Status: Lean MCP `REACHABLE`; Rocq/Coq MCP
`REACHABLE_AFTER_CONFIG_REPAIR`; local Rocq compiler `REACHABLE`.  This is an
environment audit, not a new mathematical claim.

## Lean 4

The callable tool surface exposes 23 `mcp__lean_lsp__*` operations.  There is
no separate health endpoint, so reachability was established by actual
compilation and project operations:

- fresh MCP `lean_build(clean=true)` on `lean_kernel/`: `success=true`, 1,054
  jobs, no errors; the following direct incremental `lake build` also
  succeeded with 1,047 jobs;
- MCP `lean_run_code`: a minimal `(2 : Nat) + 2 = 4` proof compiled and
  `Lean.versionString` evaluated to `4.33.0`;
- MCP diagnostics on `Erdos1191/AbelFinite.lean`: success, no diagnostics;
- MCP `lean_verify` on `Erdos1191.finiteAbel_range`: only `propext`,
  `Classical.choice`, and `Quot.sound`; no suspicious-source warnings.

After the finite prefix/scale statement was frozen, the same MCP path rebuilt
the new `Erdos1191/PrefixScaleFinite.lean` module.  Diagnostics were empty.
`lean_verify` reported only `propext` for `prefixScaleCurl`, and only
`propext`, `Classical.choice`, and `Quot.sound` for
`finiteScaleAbel_terminal` and
`finiteEpochScaleAbel_transport_fromPotential`; every source scan was clean.
The final theorem is the unconditional potential specialization of the full
finite two-dimensional identity, with initial and final prefix boundaries,
all interior epoch coefficients, the scale-terminal row, and `n=0` included.

The project pins `leanprover/lean4:v4.33.0`; Lake is
`5.0.0-src+d8b1897`, and mathlib is pinned at
`db584cd6d46c92f209a44c0f1c829460d327499d` (`master-2026-08-10`).  A
clean package build and direct checks of `AbelFinite.lean` and
`AxiomAudit.lean` also exited zero.  Source scans found no `sorry`, `admit`,
custom `axiom`, or extended trust-bypass token.

The first cold MCP build exceeded its 300-second request window while the
child rebuilt mathlib; the child completed, and subsequent MCP builds
succeeded in about two seconds.  This is recorded as a cold-cache operational
caveat, not an MCP reachability failure.

After the finite ownership statements were frozen, MCP rebuilt
`Erdos1191/OwnershipFinite.lean` and the root module successfully.  The fresh
clean MCP gate completed 1,054 jobs.  Diagnostics were empty.  `lean_verify`
reported only `propext`,
`Classical.choice`, and `Quot.sound`, with an empty suspicious-source scan, for
each of `finiteSignedPrimitiveToNetRow`, `ownerFiberPartitionSum`,
`ownerQuadraticShares_sum`, `finiteQuadraticEnergy_eq_doubleSum`,
`fejerRatio_three`, and `fejerRatio_ge_nineSixteenths`.  The source SHA-256 is
`8800ef4f04a478af7a27de80b19806ceda4fd5c34f76415d1134e825a9e41097`.

## Rocq/Coq

The first configured entry,

`opam exec --switch=coq-mcp -- uvx rocq-mcp`,

failed during MCP initialization because `rocq-mcp` is not published under
that name in the package registry.  The entry was repaired to use the
official source and pinned commit
`6983113d0844c0b7f987c79dab13988445109bfb`:

`opam exec --switch=coq-mcp -- uvx --from git+https://github.com/LLM4Rocq/rocq-mcp.git@6983113d0844c0b7f987c79dab13988445109bfb rocq-mcp`.

Rocq 9.1.1 exposes `rocq compile` rather than a `coqc` executable.  The MCP
therefore receives `ROCQ_COQC_BINARY=/Users/USER/.local/bin/coqc-coq-mcp`,
a two-line compatibility wrapper whose SHA-256 is
`33b10624b77fea79521c6a291cc29a055f304b5aa9f427e08937d113b81703bd`.

A fresh direct stdio client initialized this exact pinned command and listed
13 MCP operations.  `rocq_health` returned `success=true`, `ok=true`, no
warnings, server version `0.3.1`, switch `coq-mcp`, Rocq/OCaml version string
`9.1.1 4.14.2`, pet `0.2.5`, and `pytanque_importable=true`.  An MCP
`rocq_compile` of `forall n : nat, n = n` succeeded and printed `Closed under
the global context`; `rocq_verify` independently returned `success=true`,
method `module_m`, and `assumptions=[]`.

Once Lean's curl statement had stabilized, one deliberately small independent
Rocq source audit was added at `rocq_kernel/PrefixScaleFiniteAudit.v`.
Rocq 9.1.1 compiled it, `rocq check` accepted the `.vo`, and
`Print Assumptions prefixScaleCurl` reported `Closed under the global
context`.  The source contains no `Admitted`, `Axiom`, `Conjecture`, or
`Abort`; its SHA-256 is
`d3a17c37795e43b19b4bd42da8cb904c84f29c7f130cada2be54b84748613972`.
The repaired MCP also compiled this file in full.  MCP `rocq_assumptions`
returned an empty assumption list and `Closed under the global context` for
`prefixScaleCurl`.

After the Lean ownership statements stabilized, local Rocq 9.1.1 independently
audited the same three finite mechanisms using explicit finite lists and
algebraic laws valid in every commutative ring.  The theorems are
`finiteSignedPrimitiveToNetRowAudit`, `ownerFiberPartitionSumAudit`,
`ownerQuadraticSharesSumAudit`, and the companion double-sum expansion
`finiteQuadraticEnergyDoubleSumAudit`.  `rocq compile -q` printed `Closed under
the global context` four times and `rocq check -silent` accepted the generated
object.  The source has no `Admitted`, `Axiom`, `Conjecture`, or `Abort`; its
SHA-256 is
`5e090ca8af73523bf75f034be2e235163284d0ef95f3496ea20765c9f6d41a23`.
The repaired MCP also compiled this file in full.  MCP `rocq_assumptions`
returned an empty assumption list and `Closed under the global context` for
all four named theorems.  The complete reachability transcript is summarized
in `evidence/rocq_mcp_reachability_2026-08-30.txt`.

The MCP emits a harmless project-file warning: `rocq_kernel/` has no
`_RocqProject`, `_CoqProject`, or dune project and hence no `-R`/`-Q` aliases.
The audited files are self-contained and use neither aliases nor imports, so
this warning does not weaken the recorded checks.

## Scope and next formal targets

Lean remains a parallel verifier only.  The discrete prefix/scale curl, the
full finite two-dimensional Abel identity, and the frozen generic ownership
and change-of-basis identities are now green.  Any further formal target must
again be a stable, load-bearing finite statement from the C058 search.  Rocq
MCP independently audits the curl and ownership identities after their Lean
statements stabilized.  Neither assistant is a substitute for the
finite-horizon phase-integrated signed-transport/master-inequality search.

C058 remains the sole primary research bottleneck as a priority statement,
not a “one remaining lemma” claim.  No broad translation of the workspace is
authorized or useful at this checkpoint.

## Live refresh — 2026-08-31

Both MCP transports were exercised again before relying on them.  The detailed
transcript and exact operational caveats are in
`evidence/formal_toolchain_refresh_2026-08-31.txt`.

Lean still pins version 4.33.0 and mathlib commit
`db584cd6d46c92f209a44c0f1c829460d327499d`.  A concurrent cold-cache probe
initially raced while materializing the generated mathlib checkout; the
incomplete cache alone was quarantined, a single sequential `lake update`
restored the exact pin, and the project then built successfully.  After the
new frozen owner-stitch fixture, `lake build` completed 1,067 jobs.  The Lean
theorems now additionally prove symmetry, zero row sums, exact square energies,
PSD, fixed local/global energies, the global share formula, and the exact
two-owner obstruction.  Explicit axiom output contains only `propext`,
`Classical.choice`, and `Quot.sound`; no native-decision trust axiom or source
hole remains.  The current OwnershipFinite.lean SHA-256 is
`7a7d691f14b3b65a08dc78a99b7f5482aaa8294a45e52cc2b4cfcca87b0c88ea`.

Rocq MCP health again returned server 0.3.1 and Rocq 9.1.1 with no warning in
the health payload.  Minimal compile and verify probes remained closed under
the global context.  Only after the Lean statement stabilized, Rocq then
independently audited the exact fixed three-coordinate owner obstruction using
Corelib alone: both matrix symmetries, all zero row sums, local energies 1 and
1, global energy 2, local shares, the global 2/0 branch, and the final
obstruction.  All ten new assumption queries returned an empty assumption
list.  The current OwnershipFiniteAudit.v SHA-256 is
`12f54f6d24972777e1fc7f1d01d633f818e0fb7d0ec5d513171fc87eba863952`.

This refresh changes no priority: C058 remains the only primary bottleneck,
and the exact phase-integrated signed transport/master search remains ahead of
any further formalization.
