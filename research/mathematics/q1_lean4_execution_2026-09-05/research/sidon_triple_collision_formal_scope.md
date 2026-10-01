# Actual Sidon triple collision: verified formal scope

The new `lean/Q1/SidonTripleCollision.lean` proves cancellation and support
disjointness for actual Sidon triple multisets, including repeated endpoints. It
also extracts the actual endpoint collision from an old signed source pair whose
positive output uses the newest point. All sixteen new declarations passed the
targeted build, explicit axiom audit, and imported-environment kernel replay.
This is a local combinatorial bridge; the complete matching-orbit partition and
the original Q1 conclusion are still unformalized.

## Actual hypotheses and conclusions

The Sidon hypothesis is exactly `Erdos1191Q1.Sidon A` from the unchanged
`Q1.Target`. The endpoint set is `A : Set ℕ`; signed labels live in `ℤ`, so no
truncated natural subtraction is used in the source/output equation. Neither
infinitude, positivity of every member, nor a growth cap is required for these
local theorems.

For arbitrary `U V : Multiset ℕ`, the cancellation theorem assumes cardinality
three, membership of every endpoint in `A`, equality of the two multiset sums,
and a shared member. It erases one occurrence of that member, applies the actual
Sidon predicate to the remaining two-element multisets, and restores the erased
occurrence. Consequently, unequal equal-sum triple multisets have disjoint
supports. Multiplicity is retained throughout; distinct slots need not have
different values.

`SignedBefore A n z` is the literal existence of distinct actual endpoints
`a,b ∈ A` with `a<n`, `b<n`, and `z=(a:ℤ)-(b:ℤ)`. The cutoff `n` is an endpoint
**value**, not a rank. The module proves that these labels are nonzero and that
their ordered endpoints are unique under the actual Sidon hypothesis. It also
proves that `n-m`, for `m<n` and `m,n∈A`, cannot already be a `SignedBefore A n`
label.

Given two such actual old signed sources `u=a-b`, `v=c-d` with
`u-v=n-m`, the module proves `v<u` and reconstructs

\[
 U=\{a,d,m\},\qquad V=\{b,c,n\},\qquad a+d+m=b+c+n.
\]

The endpoint certificate derives `U≠V`, `Disjoint U V`, and the exact counts
`count n U=0`, `count n V=1`, `count n (U+V)=1`. The sums, disjointness, and
newest-point multiplicity are conclusions, not premises. Each triple has
cardinality three even when old endpoints repeat.

The remaining formal bridge is substantial: construction of the history/rank
clock, exhaustive six-matchings and automorphism multiplicities, complete
signed-pair grouping, coefficient identification with the previously verified
algebraic modules, the full convolution energy identity, and the uniform
physical budget needed by Q1. This module does not assert those results.

## Exhaustive new declaration inventory

Every name below has prefix `Erdos1191Q1.SidonTripleCollision.`. There are two
definitions and fourteen theorems; the audit driver names all sixteen exactly
once.

1. `triple` — three-slot multiset definition.
2. `triple_card` — cardinality three, allowing repetitions.
3. `triple_sum` — sum of the three slots.
4. `mem_triple` — exact slot membership.
5. `pair_eq_of_sum_eq` — actual Sidon equality of pair multisets.
6. `triples_eq_of_common_member` — cancellation of one shared occurrence.
7. `distinct_triples_disjoint` — disjoint supports of distinct representations.
8. `SignedBefore` — actual old signed-difference predicate.
9. `signedBefore_ne_zero` — nonzero label.
10. `signed_difference_endpoints_unique` — actual ordered endpoint uniqueness.
11. `new_output_not_signedBefore` — the new positive output is absent earlier.
12. `endpoint_sum_eq` — integer label equation gives natural endpoint equation.
13. `sources_ordered_of_new_output` — the two sources are strictly ordered.
14. `newest_counts` — exact newest endpoint counts.
15. `retired_endpoints_collision` — endpoint collision certificate.
16. `retired_sources_yield_collision` — extraction from actual signed sources.

Every explicitly audited dependency set is a subset of
`{propext, Classical.choice, Quot.sound}`. `SignedBefore` uses no axioms. The
source scan found no prohibited proof escape tokens. No custom axiom, placeholder
proof, native decision procedure, or unsafe proof shortcut was introduced.

## Actual verification and provenance

All times below are observed UTC on 2026-09-05. Each instrumented command saves
its exact arguments, working directory, start/end times, elapsed time, observed
exit code, separate complete stdout/stderr files, embedded complete outputs,
and byte hashes.

| Check | Actual interval UTC | Observed result |
|---|---|---|
| `lake build Q1.SidonTripleCollision` | 12:35:42.918695–12:35:48.484958 | exit 0 |
| Explicit sixteen-name `#print axioms` driver | 12:35:48.497610–12:35:51.764605 | exit 0; exact coverage |
| `lake env leanchecker Q1.SidonTripleCollision` | 12:36:20.728802–12:36:28.932265 | exit 0; empty stdout/stderr |

The build and axiom commands each bind an unchanged nineteen-file source,
configuration, driver, and runner snapshot. The checker binds an unchanged
twenty-seven-file source/artifact/evidence snapshot and unchanged checker
executable. Each command separately binds all 153 files in the prior frozen
`evidence/goal8_reviewed_research.json` before and after execution. All 153 were
unchanged. The checker is one new process replaying this module in its imported
environment with Lean's kernel. It is not fresh replay of every imported
dependency and is not an independent external checker.

Runtime probes record Lean 4.33.0, commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`, Lake
`5.0.0-src+d8b1897`, resolved executable paths and hashes, and Python 3.14.6.
`sidon_triple_collision_checker_resolution.run.json` is explicitly a
**post-replay** `lake env which leanchecker` resolution probe, not a second
checker execution. Its resolved path and executable bytes match the saved
checker record.

At 12:43:29.616109 UTC, `sidon_triple_collision_readback.py` verified all saved
output bytes, source and artifact hashes, runtime executables, and all 153
previous frozen files against their records. This readback performs no build,
axiom-audit, or checker rerun. The unchanged aggregate `Q1.lean` and existing
`AxiomAudit.lean` were neither edited nor invoked as a new aggregate suite.

All new evidence paths have prefix `lean/evidence/sidon_triple_collision_`.
The principal records are:

| Path suffix | SHA-256 |
|---|---|
| `verify.py` | `cd9e0fe3a309bcdc7ab9b1fe03a938f9cc66fcac57a8b4f4454d75d9ea0dcd6d` |
| `checker_verify.py` | `3129ef4be7857d01fbc8b5ec209017f4fd05d143cd0aa7c3a1064dffe414189a` |
| `result.json` | `f75ab413c21b68d8d344c2ca84c08d3044d8c6f070764eaf430ae3a3042eed93` |
| `build.run.json` | `991dbfedf45013a303daedeeccb07bf1a4b1c691088dc77b3b271b122e4904d8` |
| `axioms.run.json` | `cac275c134136a1164a05c01b20ac1c6a0f487bc15257abf2d4dd44582e33c56` |
| `checker.run.json` | `c1ba499921e4cfc799d8d7a901a4c3eab475dd6c6b083c8b1301da3c287d0b31` |
| `runtime.json` | `6dbe3dad8b6ff1d9bc53e89f51a28cc27b49091077fcc837cb4e1d3397118965` |
| `checker_resolution.run.json` | `9afc968dede237b2dfda26d5d72e7fbbb6475c5409daabda495475e719754e1a` |
| `readback.json` | `7c2effd2880cea3bd365dfb3ff8782a93e67b5722d6c9962d9eb5ebb9a105ce0` |

The final source SHA-256 is
`d4f042ca3fe5a729ec6785988d5b2c819257bfaadf372c730353276000cf532e`.
It was not changed after these successful executions. The original Q1 and the
current research goal remain unresolved.
