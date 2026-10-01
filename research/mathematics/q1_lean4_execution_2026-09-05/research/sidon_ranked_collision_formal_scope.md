# Actual ranked Sidon sources: verified formal scope

The new module `lean/Q1/SidonRankedCollision.lean` connects literal index
cutoffs for a strictly increasing Sidon sequence to the previously verified
value-cutoff collision certificates. Its four declarations passed the targeted
build, explicit axiom audit, and imported-environment checker replay. It derives
the endpoint-index bound and collision from actual old source witnesses; it
does not assume an equal-sum collision or an endpoint orientation.

## Exact sequence and indexing conventions

The sequence is `a : ℕ → ℕ` with hypothesis `StrictMono a`. Its actual values
form `Set.range a`, and Sidonicity means the unchanged predicate
`Erdos1191Q1.Sidon (Set.range a)` from `Q1.Target`.

Indices start at zero. The new definition is literal:

\[
\operatorname{SignedBeforeRank}(a,r,z)
\iff \exists p,q<r:\ p\ne q,\quad z=(a_p:\mathbb Z)-(a_q:\mathbb Z).
\]

Thus the old prefix **through** index `b` has cutoff `b+1`, not `b`. This avoids
a hidden shift when comparing the two output indices `i<r` to the old prefix.
The definition itself is available for arbitrary sequences; its nonzero-label
interpretation uses the `StrictMono a` hypothesis, which makes distinct
indices have distinct values. All theorems in this module impose strict
increase. No growth, cap, density, or final-Q1 hypothesis is included.

The cutoff equivalence is

\[
 \operatorname{SignedBeforeRank}(a,r,z)
 \iff\operatorname{SignedBefore}(\operatorname{range}(a),a_r,z).
\]

Its forward direction uses strict increase and injectivity; its reverse
direction extracts the actual range indices and reflects the strict value
inequalities through the strictly increasing sequence. This equivalence does
not require Sidonicity. Under actual Sidonicity, equality of nonzero signed
differences additionally proves equality of both ordered endpoint indices.

## Derived eligibility certificate

The final theorem assumes actual source witnesses through old index `b`,
output indices `b<i<r`, and the integer equation

\[
 u-v=a_r-a_i.
\]

It extracts indices `p,q,s,t≤b`, retaining `p≠q`, `s≠t` and the exact
identifications `u=a_p-a_q`, `v=a_s-a_t`. It proves

\[
 \max(\max(p,q),\max(s,t))<i.
\]

This index maximum is computed from the actual source endpoints. Ordered
endpoint-index uniqueness makes it independent of a choice of signed-label
representation. The theorem does not assume that `b` is attained by an
endpoint; `b` is the old-prefix upper bound. No equality of a source clock
with `b` is asserted.

Strict increase then puts every source endpoint value below `a_i<a_r`. The
already proved actual Sidon endpoint theorem yields

\[
 U=\{a_p,a_t,a_i\},\qquad V=\{a_q,a_s,a_r\},
\]

with cardinality three, equal sums, unequal multisets, and disjoint supports.
The exact counts of `a_i` in `(U,V)` are `(1,0)`; those of `a_r` are `(0,1)`;
both have total count one in `U+V`. Old slots may repeat. Thus the output
endpoints are the unique largest and second-largest occurrences, on opposite
sides. Integer subtraction is used for signed labels, so no natural
truncation enters the source/output equation.

This supplies the requested rank-to-value bridge for actual increasing
histories. An exhaustive matching-orbit partition, automorphism-weighted sums,
source kernels, energy identities, cap-sensitive demands, and the original Q1
conclusion remain outside this module.

## Exact declaration and axiom inventory

The prefix of every declaration is `Erdos1191Q1.SidonRankedCollision.`.

| Declaration | Kind | Actual audited axioms |
|---|---|---|
| `SignedBeforeRank` | definition | none |
| `signedBeforeRank_iff` | theorem | `propext` |
| `ranked_signed_endpoints_unique` | theorem | `propext`, `Quot.sound` |
| `ranked_eligible_sources_yield_collision` | theorem | `propext`, `Classical.choice`, `Quot.sound` |

The explicit driver contains each of these four names exactly once. The saved
audit stdout covers exactly these names. The source scan found no prohibited
proof escape tokens. The final LSP report had no diagnostics. No custom axiom,
placeholder proof, native decision procedure, or unsafe proof shortcut was
introduced.

## Actual targeted executions

Each instrumented command preserves exact arguments, cwd, UTC start/end,
elapsed time, observed return code, full separate stdout/stderr files, embedded
complete outputs, source hashes before and after, and the runner hash.

| Command | Interval on 2026-09-05, UTC | Observed result |
|---|---|---|
| `lake build Q1.SidonRankedCollision` | 13:07:03.187119–13:07:07.995331 | exit 0 |
| Explicit four-name axiom driver | 13:07:08.012499–13:07:11.144196 | exit 0; exact coverage |
| `lake env leanchecker Q1.SidonRankedCollision` | 13:07:52.223289–13:07:59.978248 | exit 0; empty stdout/stderr |

The source/build/audit snapshot contains 22 files; the checker snapshot
contains 30 source, artifact, and evidence files. All before/after hashes
agree. A separate preservation manifest contains 219 earlier fixed files:
the original 153, the completed triple and eligible modules with their
evidence/scopes, two completed analytical reviews, and the parent's prior
Sidon binding. Every instrumented command also checked these 219 files before
and after execution. The parent deferred governance updates during these
gates.

Runtime probes record the pinned Lean 4.33.0 commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`, Lake
`5.0.0-src+d8b1897`, Python 3.14.6, and resolved executable paths and hashes.
The checker replays this module in the existing imported environment with
Lean's kernel. It is not fresh replay of all imported dependencies and is not
an independent external checker. Its executable path and bytes were also
confirmed by a separately labeled post-replay resolution probe.

The first byte-readback helper invocation failed an incorrect preserved-count
assertion: a textual replacement had changed the intended `219` to `419`.
The failure is retained in `sidon_ranked_collision_readback_failed_attempt.json`,
including the observed exit 1 and exact tool-reported traceback. That helper
failed before any resolution probe; it runs no build, axiom audit, or checker.
Only the new helper assertion was corrected. The Lean source and all successful
substantive execution records were unchanged and were not rerun.

The corrected readback completed at **13:08:51.464838 UTC** with exit 0 and
verified all saved output bytes, source/artifact bytes, runtime executable
bytes, and all 219 preserved files. This is the time of the final preservation
observation, not a promise that subsequent parent-authorized governance updates
cannot change those governance files. The parent was informed that the gates
had ended.

## Frozen source and evidence hashes

Source `lean/Q1/SidonRankedCollision.lean`:
`5c10a6327055f4daf6eb346182c5691f8c68cdef798343faf7d9daaee80330bf`.

All evidence paths below have prefix `lean/evidence/sidon_ranked_collision_`.

| Suffix | SHA-256 |
|---|---|
| `verify.py` | `ce3ec440a170ed959d11ef17840900724312bd22a582c821491ced4b85bad1db` |
| `checker_verify.py` | `3b9fc8653911b4725d7cb58035e45f66d5d1bfc587baaad44cedbc24a68ebc80` |
| `prior_files.json` | `c2e8112440b2911b019924fbc24e2604e0492c95b723e0a776de1f8d9d12e8a5` |
| `result.json` | `9045234648e3244995c17833f97e331bc86c6fa30654281038111f72be861906` |
| `build.run.json` | `dc0759cd089e93945ab7bd9fa4b0edde7f9963fe6348c65e6bf606b67b539dea` |
| `axioms.run.json` | `9a57bf73bf139f424411329520fbe68f332685c7954752d445d782a14619f252` |
| `checker.run.json` | `d4de1670dc0ecd8b1d815650b01f4501707be57af40f56040103e5c00973b5ec` |
| `runtime.json` | `dd5e3dcd0c28b5a686a77a524541754bb067f8a126c4f4eb16a7c2e91070b5a4` |
| `checker_resolution.run.json` | `aa97616132091455645fd1370bb2d0e7a49e0d6726f629f71922cad037fe3ae7` |
| `readback.json` | `a9e9ca6574c54a5ac60b97aa83bd69692f6f29f130a39f87f19b51daee4988e2` |
| `readback_failed_attempt.json` | `80448e30b5175fbe77dbb9092a5e4f8e6971f808611092ae5ea0d857953fdeef` |

No aggregate import, existing aggregate audit, pinned configuration, prior
verified source/evidence, or research status file was edited by this task.
The four declarations are a local actual-combinatorial bridge; the current
research goal and original Q1 remain unresolved.
