# Reset handoff manifest

This compatibility manifest intentionally does not reproduce the historical
release inventory.  The historical Wave 12 inventory artifact remains in the
frozen read-only original, while this directory is an unsealed research
workspace.

Canonical entrypoint: `UPDATED_START_HERE.md`.

Required reset outputs:

- `RESET_CHECKPOINT_2026-08-29.md`
- `CLAIM_EVIDENCE_REGISTRY.csv` and `.json`
- `QUANTIFIER_AND_REDUCTION_AUDIT.md`
- `LEAN_KERNEL_STATUS.md`, `LEAN_KERNEL_PROSE_AUDIT.md`, and `lean_kernel/`
- `ROUTE_PORTFOLIO.md`
- `UPDATED_START_HERE.md`
- `INTEGRITY_STATUS.md`
- `LITERATURE_DELTA.md`
- `FINAL_STATUS.txt`

Latest continuation outputs:

- `core_workspace/CONTINUATION_2026-08-30_C058_FULL_PHASE_AND_HISTORY_DICHOTOMY.md`
- `route_probes/ROUTE_C_AGGREGATE_CHANGE_OF_BASIS_LEGALITY.md`
- `route_probes/ROUTE_C_EPOCH_BLOCK_FULL_PHASE_FEJER_MASTER.md` and its exact
  certificate/test bundle
- `route_probes/ROUTE_C_FEJER_TERMINAL_EXCISION.md`
- `route_probes/ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO.md` and its exact
  certificate/test bundle
- `route_probes/ROUTE_C_CRITICAL_SPAN_POTENTIAL_AND_GOOD_WINDOWS.md`
- `lean_kernel/Erdos1191/OwnershipFinite.lean`
- `rocq_kernel/OwnershipFiniteAudit.v`
- `evidence/C116_FINAL_VERIFICATION_2026-08-31.md`

Current handoff gate: 32 Route-C suites / 352 tests pass; registries are
field-for-field synchronized through C116; the global status is unchanged.
The preserved Wave 19 manifest is expected to fail against this expanded
unsealed worktree and must not be described as a current release seal.

Do not generate a new release manifest until the mathematics and evidence
labels stabilize and a genuine release gate is authorized.

Global status: `UNRESOLVED_AT_HARD_LIMIT`.
