# Erdős Problem #1191 — proof-reset checkpoint

Date: 2026-08-29 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`

This checkpoint distinguishes three states that must not be conflated:

1. the original tree extracted from `01_ORIGINAL_MATHEMATICS.zip` and preserved read-only;
2. the later Wave 19 seed copied into this reset worktree;
3. new reset outputs and exploratory files, which are intentionally outside the old Wave 19 manifest.

No manifest was regenerated in this audit.

The historical `FILE_INVENTORY.txt` was not regenerated either. Its old 379-file body was retained and only a reset-warning banner was added so that it cannot be mistaken for the current 445-file worktree inventory.

## 1. Exact target statements and quantifiers

Let `A` be an infinite additive Sidon subset of the positive integers and

```text
A(x) = |A intersect [1,x]|.
```

Question 1 is

```text
for every infinite additive Sidon set A subset N,
liminf_(x -> infinity) A(x) sqrt(log(x)/x) = 0.
```

Equivalently, if `A={a_1<a_2<...}`, there do not exist an infinite Sidon `A`, a finite constant `C>0`, and an index `n_0` such that

```text
for every n >= n_0,  a_n <= C n^2 log(2n).
```

The order of quantifiers in the negated counterexample form is therefore

```text
not exists A, C>0, n_0, for all n>=n_0: a_n <= C n^2 log(2n).
```

Question 2 is

```text
there exist an infinite additive Sidon set A subset N and c>0 such that
liminf_(x -> infinity) A(x) (log(x))^c / sqrt(x) > 0.
```

Spelling out the positive liminf, this means that there also exist `epsilon>0` and `x_0` such that the displayed quantity is at least `epsilon` for every `x>=x_0`. It is an all-sufficiently-large-scales assertion, not a limsup/subsequence assertion. Q1 and Q2 are separate questions; neither answer follows formally from an answer to the other.

## 2. Original read-only forensic snapshot

Original root:

```text
/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_ORIGINAL_READONLY_2026-08-29/mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28
```

Direct checks gave:

- 345 regular files total;
- 294 entries in the self-excluding `integrity/PACKAGE_SHA256SUMS.txt`;
- 32 forbidden cache files;
- 18 non-cache files absent from that manifest;
- six listed files with checksum mismatches;
- zero owner-writable files and zero owner-writable directories; root mode `dr-xr-xr-x`.

The preserved contract-script output is [evidence/forensic_original_audit/audit.log](evidence/forensic_original_audit/audit.log). That script correctly returned manifest exit 1, but two later sections did not run portably: BSD `find` rejected `-printf`, and bare `pytest` was not on `PATH`, producing collection/focused exit 127. Those are audit-script/environment failures, not test failures.

The failed `find` section must not be used as the artifact inventory. Direct inspection shows that this original tree contains only the Wave 15 prose memo `WAVE15_LOCAL_PROMOTION_ALLOCATION_AND_HORIZON_OBSTRUCTION_2026-08-29.md`; it has no Wave 15 probe, test, or JSON certificate.

The original top-level entrypoints are stale relative to their own later canonical notes:

- `00_START_HERE_PROMPT.txt`, `HANDOFF_MANIFEST.md`, `README_START_HERE_JA.md`, and `NEW_SESSION_LAUNCH_MESSAGE.txt` direct the next session to Wave 12/P18;
- `core_workspace/1191_MASTER_STATUS.md` and `core_workspace/proof_obligations.md` later reclassify universal P17/P18 as Question-1-equivalent.

Thus the original extracted tree is an `UNSEALED` post-Wave-12 worktree layered over the last sealed Wave 12 checkpoint. A green Wave 12 release record does not seal Wave 13–15.

## 3. Tests actually run during this reset

The following commands were actually executed against the original read-only tree, with bytecode and pytest cache disabled where pytest was used:

| Scope | Command (abbreviated only for paths) | Result |
|---|---|---|
| Original manifest | `python3 integrity/verify_package.py` | exit 1; 32 cache files, 18 unlisted files, six checksum mismatches |
| Original collection | `PYTHONDONTWRITEBYTECODE=1 uv run --no-project --with pytest -- python -m pytest --collect-only -q -p no:cacheprovider` | exit 0; 293 tests collected in 0.52 s |
| Original Wave 13/14 focus | same runner on the two Wave 13 and two Wave 14 test files named by the reset pack | exit 0; 18 passed, 65,331 subtests passed in 19.70 s |

The following were actually executed against the later Wave 19 reset seed:

| Scope | Command | Result |
|---|---|---|
| Wave 15 focused | `... pytest -q -p no:cacheprovider core_workspace/endpoint_variance/test_wave15_local_promotion_allocation_probe.py` | exit 0; 5 passed, 26 subtests passed in 1.82 s |
| Wave 15 deterministic replay | run `wave15_local_promotion_allocation_probe.py` to a temporary file and `cmp` with the committed JSON | generator exit 0; byte comparison exit 0; internal hash `3844b51b...c908ec8` |
| Gmix no-go first focus | `... pytest -q -p no:cacheprovider core_workspace/endpoint_variance/test_wave19_p28_gmix_no_go_certificate.py` | exit 1; 9 passed, 3 failed; missing generator functions `dyadic_current_gap_lower` and `weighted_gmix_floor` |
| Gmix no-go repaired focus | same command after the generator was completed | exit 0; 12 passed in 0.07 s |
| Gmix deterministic replay | run the repaired generator to a temporary file and `cmp` with the dated JSON | generator exit 0; byte comparison exit 0; JSON SHA-256 `596c046c...ccec091f` |
| Reset-worktree manifest | `python3 integrity/verify_package.py` | exit 1; old listed files matched, but reset/exploratory files were unlisted |
| Final listed-path checksum after stale-directive reconciliation | `shasum -a 256 -c integrity/PACKAGE_SHA256SUMS.txt` | exit 1; nine intentional mismatches: `00_START_HERE_PROMPT.txt`, `FILE_INVENTORY.txt`, `HANDOFF_MANIFEST.md`, `NEW_SESSION_LAUNCH_MESSAGE.txt`, `NEXT_LEMMA_TARGETS_ANTI_EULERIAN.md`, `README_START_HERE_JA.md`, `core_workspace/1191_MASTER_STATUS.md`, `core_workspace/approach_registry.md`, and `core_workspace/proof_obligations.md` |
| Lean clean build | from `lean_kernel/`: `lake clean erdos1191 && lake build` | exit 0; build completed successfully, 1,009 jobs |
| Lean axiom audit | `lake env lean Erdos1191/AxiomAudit.lean` | exit 0; only standard `propext`, `Classical.choice`, `Quot.sound` where reported; no project axiom |
| Lean forbidden-token scan | project `.lean` sources for singular `sorry`, `admit`, or `axiom` declarations | zero matches; normalized exit 0 |

The supplied outer ZIP was also tested with `unzip -t` and had no compressed-data errors. All five member SHA-256 values matched its supplied outer checksum list.

Not rerun in this reset checkpoint:

- the present Wave 19 full suite;
- every historical certificate replay;
- a clean extracted-copy release runner.

Those must not be reported as current executions. The prior record [integrity/WAVE19_TEST_VERIFICATION_2026-08-29.json](integrity/WAVE19_TEST_VERIFICATION_2026-08-29.json) records a pre-reset run of 401 tests and 78,844 subtests, seven Wave 19 byte replays, and a 378-entry closing manifest. It is preserved evidence, not a substitute for a new release run after reset outputs stabilize.

## 4. Evidence-tier reconciliation

### Formal theorem

The pinned Lean 4 project formally checks the exact exported L1 family

```text
additiveSidonNat_iff_additiveSidon
additiveSidonNatUpTo_iff_additiveSidonUpTo
additiveSidon_iff_positiveDifferenceUnique
additiveSidonNat_iff_positiveDifferenceUnique
additiveSidonUpTo_iff_positiveDifferenceUniqueUpTo
sum_adjacentGap_Ico
positiveDifferenceUniqueUpTo_iff_contiguousGapSumsUniqueUpTo
additiveSidonUpTo_iff_contiguousGapSumsUniqueUpTo
additiveSidonNatUpTo_iff_contiguousGapSumsUniqueUpTo
adjacentGap_pos
adjacentGap_injectiveUpTo
adjacentGaps_positive_and_distinct
emptyInterval_endpointMutation_is_false
```

and the generic finite L3 family

```text
sum_forwardDiff_range
finiteAbel_range
finiteAbel_rational_fixture
```

under namespace `Erdos1191`. The complete theorem signatures, zero-based index conventions, build evidence, and theorem-by-theorem axiom report are in `LEAN_KERNEL_STATUS.md` and `lean_kernel/evidence/`. Independent theorem-by-theorem natural-language derivations are in `LEAN_KERNEL_PROSE_AUDIT.md`. This formalizes L1 and the generic algebraic engine of L3 only; it does not formalize Q1/Q2, L2, the Wave-specific L3 instantiation, L4, or L5. A literal new-directory extracted-copy Lean replay remains pending for a future release tier.

### Human proof audited, with finite executable support but not yet Lean kernel certification

- the Question-1/eventual-critical-cap equivalence;
- the Wave 12 finite Abel/cut-renewal identities;
- the Wave 13 new-birth floor and its conditional harmonic consequence;
- the Wave 14 promotion/rebate identities;
- the stabilized Wave 16 terminal-potential, Wave 17 ownership/rank-surplus, Wave 18 descendant, and committed Wave 19 coefficient/transport identities listed in the claim registry.
- the finite cross-kernel expansion and nonnegative-shift gate in `route_probes/ROUTE_C_CROSS_KERNEL_GATE.md`; its two-point counterexample proves that positive semidefiniteness of the kernel-coupling matrix alone is insufficient.

These labels concern the exact statements and hypotheses recorded in the corresponding proof memos. They do not elevate their stronger open targets.

### Computational finite only

- exact finite certificates, enumerations, fixture tables, byte replays, and regression tests;
- the 512-mark sparse-spike/cooldown chain;
- the Wave 15 seven-row calibration and its present deterministic replay;
- package hashes and manifest checks.

None of these proves an infinite compatible branch or an asymptotic target.

### Human proof pending audit

- the general asymptotic/all-epoch Wave 15 adjacent-allocation theorem: the later seed repairs the old artifact-absence claim, but its certificate explicitly limits itself to finite fixtures and does not certify the asymptotic lemma;
- no additional global/all-epoch Wave 15 theorem is upgraded by the finite certificate alone.

The Gmix self-cancellation no-go moved out of this category during the reset: its first focused run exposed two missing generator functions, the implementation was repaired, a proof memo and dated JSON were added, and the fresh rerun passed all 12 tests. The exact identity and current-index bound also received independent human audits. A fresh generator replay then matched the dated JSON byte-for-byte. The result is a human-proof-audited `CONDITIONAL_NO_GO` for the named bare-`Gmix` route with finite executable support; it is not a proof of abstract P28 or Q1.

### Conditional no-go

- named-method obstructions such as duplicate charging, isolated P26/P27 saturation, arbitrary-transport residual floors, and finite counterexamples apply only to their exact stated architecture and hypotheses. They do not refute Q1 or Q2.
- a nonnegative linear combination of the already available independent one-scale upper/lower inequalities cannot beat the best constituent ratio, by an exact convex-combination identity. This closes only the naive linear multi-`N` implementation, not multi-scale covariance, martingale, entropy, or inverse-theorem mechanisms.
- a PSD cross-kernel coupling without pointwise nonnegative combined correlations is invalid for the usual fill-all-unrepresented-differences upper bound. This is a finite analytic gate, not a rejection of the joint direct-sum mechanism in Hou--Zhao v2.

### Open

- P28 and any corrected post-Gmix signed mechanism;
- Question 1;
- Question 2;
- L2, the Wave-specific L3 instantiation, L4, and L5; therefore the full L1–L5 kernel remains incomplete despite the formal L1/generic-L3 subset;
- publication novelty and every prize-claim gate.

## 5. Non-circularity correction

Universal P17 and universal P18 are `TARGET_EQUIVALENT`, not intermediate lemmas. On a hypothetical eventual-`C` branch, the Wave 13 harmonic lower bound contradicts the requested little-oh estimate; if Q1 is true, the quantified branch class is empty and the universal statement is vacuously true. This is an exact reduction/reclassification, not a proof of Q1.

The Wave 19 entrypoints are newer than the reset bundle's original tree and no longer revive P18, but they name the bare `Gmix` inequality as the primary target. The separate quantifier/reduction audit and repaired Gmix focus now close that bare target as a named-method no-go; this does not close abstract P28 or Q1. `UPDATED_START_HERE.md` supersedes the old Gmix instruction. The focused Gmix artifact family is green, while the full reset worktree intentionally remains unsealed.

## 6. Historical controlled-file snapshot and required outputs

The following forensic count at `2026-08-29T15:48:13+0900` is a historical
checkpoint.  It predates the later Route-C continuation and is therefore
superseded as a description of the current worktree:

- 445 regular files in the reset worktree;
- zero `__pycache__`, `.pytest_cache`, `.ruff_cache`, `.scholar_cache`, or `*.lock` files;
- 14 controlled files in `lean_kernel/` and no generated `lean_kernel/.lake/` directory;
- 378 entries in the preserved old self-excluding Wave 19 manifest;
- 66 current files unlisted by that old manifest;
- zero listed paths missing;
- nine intentionally modified listed paths, all carrying reset-supersession, historical-inventory warning, or stale-directive corrections.

Here “66 unlisted” followed `verify_package.py`, which intentionally excludes
`integrity/PACKAGE_SHA256SUMS.txt` itself.  Counting that self-excluded
manifest as physically not listed gave 67; the historical total was
`378 + 1 + 66 = 445`.  These numbers must not be reused as a current release
claim; the active integrity status is maintained in `INTEGRITY_STATUS.md`.

All reset-contract deliverables are present:

- `RESET_CHECKPOINT_2026-08-29.md`;
- `CLAIM_EVIDENCE_REGISTRY.csv` and `.json`;
- `QUANTIFIER_AND_REDUCTION_AUDIT.md`;
- `LEAN_KERNEL_STATUS.md`, `LEAN_KERNEL_PROSE_AUDIT.md`, and `lean_kernel/`;
- `ROUTE_PORTFOLIO.md`;
- `UPDATED_START_HERE.md`;
- `INTEGRITY_STATUS.md`;
- `LITERATURE_DELTA.md`;
- `FINAL_STATUS.txt` containing only the global status label.

The route evidence also includes `route_probes/ROUTE_C_MULTI_N_CONVEXITY_NO_GO.md` and `route_probes/ROUTE_C_CROSS_KERNEL_GATE.md`. `LITERATURE_DELTA.md` includes the Hou--Zhao arXiv:2607.01169v2 correction: its joint direct-sum mechanism is not the naive convex average closed by the first probe, while a PSD-only cross-kernel extension still fails the second probe's pointwise sign gate.

## 7. Checkpoint decision

- Original tree: preserved read-only; `UNSEALED` post-Wave-12 snapshot.
- Later Wave 19 seed: preserved 378-entry manifest baseline with prior release evidence.
- Current reset worktree: intentionally `UNSEALED`; the nine-path/66-file
  figures above are historical and have been superseded by later Route-C
  edits.  See `INTEGRITY_STATUS.md` for the current delta.  No manifest
  refresh was performed.
- Mathematical resolution: absent.
- Prize readiness: absent.

`UNRESOLVED_AT_HARD_LIMIT`
