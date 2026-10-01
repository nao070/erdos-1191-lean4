# Formal scope: actual finite ordered Sidon triple fibers

2026-09-05. This record concerns only the new `Q1.SidonTripleFiber` module. Original Q1 remains unresolved. No goal or canonical status was changed by this work.

## Exact mathematical scope

Let `A : Set ℕ` satisfy the unchanged `Erdos1191Q1.Sidon` predicate from `Q1.Target`. Let `K : Finset ℕ` have all its members in `A`, and let `s : ℕ` be arbitrary. The module defines the literal finite set

```
orderedFiber K s = {(a,b,c) in K × K × K : a+b+c=s}.
```

The tuple type is `ℕ × (ℕ × ℕ)`. The membership theorem records exactly the three memberships and the sum equality. It imposes no ordering or distinctness condition: `(a,a,b)` and `(a,a,a)` are included when their sums match. Empty endpoint sets and empty fibers are included. Positivity or infinitude of `A` is not needed for these finite bounds.

For any fixed first endpoint `x`, the proof chooses an actual tuple in the corresponding subfiber if it is nonempty. Any second tuple has the same remaining two-sum, by cancellation of the first endpoint. Actual Sidonicity, applied to the four remaining endpoints in `A`, makes it one of the two ordered pairs `(b,c)` or `(c,b)`. Thus the fixed-first subfiber is contained in the literal two-element finset `{(x,b,c),(x,c,b)}`. If `b=c`, this finset automatically has only one element. No pair-uniqueness or cardinality conclusion is assumed as a separate hypothesis.

The finite map to the first coordinate takes the full fiber into `K`. Summing the proved subfiber bound yields

```
(orderedFiber K s).card <= 2 * K.card.
```

The final definition is directly real-valued:

```
normalizedMass K s = ((orderedFiber K s).card : ℝ) / 6.
```

Casting the proved natural cardinality bound and dividing by the positive constant six gives `normalizedMass K s <= (K.card : ℝ)/3`. This is the actual ordered-triple count version of the analytical fiber-mass bound.

The identification with a sum over three-element multisets weighted by inverse automorphism orders remains outside the module. Analytically, each multiset orbit has `6/aut(U)` ordered realizations, so this identification would make the normalized mass equal to that weighted sum; the permutation-orbit counting assertion itself is not proved here. The module also does not formalize signed numeric-Schur grouping, collision matching multiplicities, energy identities, demand allocation, a growth-cap contradiction, or the final Q1 theorem.

## Exhaustive new declaration inventory

There are six explicitly audited declarations: two definitions and four theorems. Every name below was passed separately to `#print axioms` in `lean/evidence/sidon_triple_fiber_axioms.lean`.

- `Erdos1191Q1.SidonTripleFiber.orderedFiber`
- `Erdos1191Q1.SidonTripleFiber.mem_orderedFiber`
- `Erdos1191Q1.SidonTripleFiber.fixed_first_card_le_two`
- `Erdos1191Q1.SidonTripleFiber.orderedFiber_card_le`
- `Erdos1191Q1.SidonTripleFiber.normalizedMass`
- `Erdos1191Q1.SidonTripleFiber.normalizedMass_le`

The definitions and all four proofs use only the allowed axioms `propext`, `Classical.choice`, and `Quot.sound`, as reported by the actual audit. The explicit audit driver and source declaration inventory agree exactly, with no missing or duplicate declaration. The new source scan found none of `sorry`, `admit`, `axiom`, `native_decide`, or `unsafe`. There are no custom axioms.

## Actual verification and preservation

Development used Lean LSP first. Initial diagnostics identified two unfinished membership simplifications; explicitly reducing the first-coordinate hypothesis closed both. Final LSP diagnostics returned `success=true`, `partial=false`, and no errors or warnings before the command gates began. The fixed source contains 75 lines, all at most 100 characters. No Lean build, audit, or checker command failed or was rerun.

The following three commands each ran once from the Lean project directory. Each run has its own `.run.json`, complete separate `.stdout.txt` and `.stderr.txt`, observed exit code, timestamps, and before/after hashes.

| Command | UTC start | UTC finish | Observed exit |
| --- | --- | --- | --- |
| `lake build Q1.SidonTripleFiber` | 2026-09-05T14:35:06.582037+00:00 | 2026-09-05T14:35:10.881824+00:00 | 0 |
| `lake env lean evidence/sidon_triple_fiber_axioms.lean` | 2026-09-05T14:35:10.909912+00:00 | 2026-09-05T14:35:14.055080+00:00 | 0 |
| `lake env leanchecker Q1.SidonTripleFiber` | 2026-09-05T14:35:39.299491+00:00 | 2026-09-05T14:35:47.990401+00:00 | 0 |

The build command targeted only `Q1.SidonTripleFiber`; the displayed dependency-job count is not a count of newly proved declarations. Existing imported artifacts were used normally. The prior unrelated declaration suites were not run.

The checker used `lake env leanchecker Q1.SidonTripleFiber` in `from_imports` mode. It was a new process checking the target in its existing imported environment with Lean's own kernel. It was not a fresh replay of every imported dependency or an independent external checker. Its stdout and stderr were both empty, and the subprocess returned zero. Empty stdout alone was not used as evidence of success.

Runtime provenance records Lean 4.33.0, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, Lake 5.0.0-src, the actual Python executable/version, launcher hashes, and resolved Lean/Lake executable hashes. The checker executable's bytes were hashed before and after its run; a separate post-replay executable-resolution command confirmed that the executable resolved by the Lake environment is the one recorded. That resolution command was not another checker replay.

The build/audit gate binds a 24-file source snapshot including all current Q1 module sources, the existing aggregate, pinned configuration, the new driver/runner, and the preservation inventory. The checker binds 32 files, adding its runner, compiled target artifacts, and result/runtime records. Final readback at `2026-09-05T14:36:04.320968+00:00` confirmed all bound source, artifact, complete output, runner, and runtime executable bytes.

The preservation inventory was copied from `evidence/goal10_reviewed_research.json`, SHA-256 `85493d97b21274e405dd2db0cf3886afea551822e83d2caf0251f7f7cd630358`. Every one of its 335 files matched before and after every instrumented command and at final readback. The parent was notified before the preservation gates and again at their completion. The preservation statement concerns those observed times; subsequent parent-authorized governance updates are not claimed to leave the old governance hashes current forever.

## Saved records and hashes

| Artifact | SHA-256 |
| --- | --- |
| `lean/Q1/SidonTripleFiber.lean` | `c76585c8943ad3e965de2182d287919869af66dd27ca379117be000e8bfd979b` |
| `lean/evidence/sidon_triple_fiber_prior_files.json` | `694b0c2903e3c35d6b339c0ba4d97ffb77f5fbda237ee1b31cec8ac0ff523409` |
| `lean/evidence/sidon_triple_fiber_verify.py` | `3ec529d5f577e4b40b0c2dcf435788c48bfc8e7e2a178bcc3ea1ea57a9a0c365` |
| `lean/evidence/sidon_triple_fiber_checker_verify.py` | `2f7ca58c68eb1ee5a283b1bd6f389d7fdeb740236221b33ee01c13fb460b5df1` |
| `lean/evidence/sidon_triple_fiber_readback.py` | `1a74fa940f70138b1e410d792a1c1e29de924a571700f69095af8dc6677bb8cd` |
| `lean/evidence/sidon_triple_fiber_build.run.json` | `508ed21af5a9fd2aa7714bb74471415c31c432e33b9285a32e47fd6bf4307ae6` |
| `lean/evidence/sidon_triple_fiber_axioms.run.json` | `1fe29fa9a9d8d4a56640c65c4a18634a2b9bc4b434c069ffc3b75a00096d41d1` |
| `lean/evidence/sidon_triple_fiber_checker.run.json` | `35d727101cf7f6db48bdf33acbb5277bcaf81ce76962d4059fbc42eb68ba8850` |
| `lean/evidence/sidon_triple_fiber_result.json` | `d13c9892a9f8e183bcaf49abe943ab49eb6c4552294c6518cdf00ec40cdf66e6` |
| `lean/evidence/sidon_triple_fiber_runtime.json` | `1c5717efaa43d398da6c3e11c30199b8362988bc5d6cc1c8645e57d06969b4af` |
| `lean/evidence/sidon_triple_fiber_checker_resolution.run.json` | `aeaea99dbac2208cde2fd4d85557bdddb38dc225e4d790b6e903e00439ca79bb` |
| `lean/evidence/sidon_triple_fiber_readback.json` | `0b2b4eb369a1bbcbcc5e952c0338da7575df8c6141be7636db7e2e84dd8ce7c5` |

The per-run records preserve complete outputs and the exact commands as well as output-file hashes. `sidon_triple_fiber_result.json` stores the exact six-name axiom map and compiled-artifact hashes. `sidon_triple_fiber_readback.json` binds the saved evidence files at the final readback without rerunning any substantive verification. All pre-existing authored files, aggregate files, and pinned settings were preserved by this task.
