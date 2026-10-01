# C116 final verification checkpoint

Date: 2026-08-31 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Primary research priority: C058 only

This record fixes the evidence boundary for the unsealed C116 handoff.  It is
not a proof of either Erdős question, a release seal, a novelty finding, or a
prize claim.

## Mathematical artifact replay

- Complete Route-C discovery command: 32 suite files, 352 tests, 261.598
  seconds, `OK`.
- Full fixed-history phase/endpoint certificate: 10 tests, 101.026 seconds,
  `OK`.
- Lacunary exact dual obstruction: 4 tests, 2.831 seconds, `OK`.
- C107 whole-stencil regression: 9 tests, 9.056 seconds, `OK`.

The focused counts are subsets of the complete 352-test replay.  They must
not be added to that total.

## Formal toolchains

- Lean project pins Lean 4.33.0 and mathlib
  `db584cd6d46c92f209a44c0f1c829460d327499d`.
- Lean MCP clean build: 1,054 jobs, success.  Following direct Lake build:
  1,047 jobs, success.
- Diagnostics for `PrefixScaleFinite.lean` and `OwnershipFinite.lean` were
  empty.  The frozen theorem verifications reported only standard
  `propext`, `Classical.choice`, and `Quot.sound` where present.  The direct
  axiom audit exited zero, and the source scan found no `sorry`, `admit`, or
  project-defined axiom.
- The pinned Rocq MCP initialized 13 tools.  Health returned
  `success=true`, `ok=true`, and no warnings.  The minimal proof compiled and
  verified with `assumptions=[]`; both canonical audit files compiled; all
  five named theorem audits returned `assumptions=[]` and `Closed under the
  global context`.

These checks certify only the frozen finite identities and ownership/change-
of-basis lemmas.  They do not certify the open C058 master inequality.

## Registry and serialization

- `CLAIM_EVIDENCE_REGISTRY.csv` and `.json` agree field-for-field.
- IDs are exactly C001--C116 with no duplicate or missing index.
- Both registries retain global status `UNRESOLVED_AT_HARD_LIMIT`.
- Every JSON artifact parses.
- Text files contain no forbidden C0 control character other than permitted
  tab, line feed, and carriage return.

## Worktree integrity

- 597 physical regular files.
- 596 verifier-eligible files after the old manifest excludes itself.
- 378 entries in the preserved old Wave 19 manifest.
- 218 current eligible files unlisted by that old manifest.
- Zero old listed files missing.
- 11 intentional old-manifest checksum mismatches.
- Zero cache, bytecode, generated Lean/Rocq object, or lock files.

The old verifier therefore exits 1 as expected.  Its failure is evidence that
the expanded worktree is unsealed; it is not a failed mathematical test.  No
manifest or historical inventory was regenerated to manufacture a green
release result.

## Exact unresolved target

For Wave-shell spans

`H_k = N_(2^(k+1)) - N_(2^k)`,

the live C058 obligation is a legal phase-integrated, one-time-owned finite
master lower bound of the form

`Phi_k >= epsilon_C/(k+1) - A_C log(H_(k+1)/(4H_k))/(k+1) - e_k`,

or a rigorously equivalent parity-paired version, with every C103 initial,
cutoff, final, shared-endpoint, and scale-terminal row retained.  The signed
span term telescopes; the required local master inequality and its arbitrary-
history ownership localization remain open.
