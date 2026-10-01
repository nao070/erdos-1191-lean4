# Moment-demand verification review

The preserved MomentDemand gate evidence passes an independent binding audit against the current 14-file Lean source/configuration snapshot. The finite statements reviewed expose their required hypotheses; no semantic defect was identified. Q1 remains unresolved.

Review time: 2026-09-05T07:20:59.467711+00:00. Reviewer: `/root/moment_evidence_audit`. Machine-readable record: `evidence/goal5_moment_parent_binding.json`.

## Source and saved execution binding

The actual saved `Q1/MomentDemand.lean` is **313 lines**, with SHA-256 `12682e7d6036aac886c3d53b88909159c260eaac015e8346ad1017ec63900319`. The dispatch description of 327 lines was stale. The module contains 28 explicitly named definitions/theorems.

All 14 current hashes match `verification.json`, the source scan, and the before/after source maps of each run below. All three commands have preserved exit code 0; their log hashes, runner hashes, working directory, and unchanged-source assertions match the actual files.

| Saved gate | Started UTC | Completed UTC | Evidence assessed |
| --- | --- | --- | --- |
| `lake build` | 01:53:03.292910 | 01:53:14.426595 | Explicit `Built Q1.MomentDemand`, `Built Q1.AxiomAudit`, `Built Q1`, then success at 3089 jobs |
| `lake env lean Q1/AxiomAudit.lean` | 01:53:14.428375 | 01:53:17.957816 | 82 unique explicit audit requests and 82 unique parsed results |
| `lake env leanchecker Q1.MomentDemand` | 01:53:17.961038 | 01:53:26.616887 | Empty log bound to the successful recorded exit code and unchanged source |

No successful build or checker gate was repeated; no C143 calculation was run. The rechecks were direct hashes, log parsing, source review, a lexical source scan, and read-only runtime/version/revision observations.

## Axioms, source hygiene and runtime

The 82 requests in `AxiomAudit.lean` exactly equal the 82 distinct declarations parsed from the saved explicit audit log and the entries of the saved allowlist. Every one of the 28 new named MomentDemand declarations occurs. Eighty declarations depend only on `Classical.choice`, `Quot.sound`, `propext`; two use only `Quot.sound`, `propext`. No other axiom was reported. The count is **82 audited declarations**, including definitions, not 82 new theorems.

The saved source scan matches all 11 current project Lean files and the full source snapshot. An independent nested-comment and string-aware scan also found no `sorry`, `admit`, `sorryAx`, `native_decide`, `Lean.ofReduceBool`, `debug.skipKernelTC`, custom `axiom`, or project `unsafe`/`implemented_by`/`extern`/`elab`/`macro` tokens. This lexical hygiene check supplements the transitive axiom audit.

The actual checker binary matches saved SHA-256 `257f505f8241ab595c6b557d661fd832dbdace6839ab35d9d1600b3dcbce5880`. All ten recorded `Q1/*.olean` hashes match current files; no project `.olean.server` or `.olean.private` parts exist. Read-only checks returned Lean 4.33.0 at commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, the recorded checker path, and clean mathlib checkout `db584cd6d46c92f209a44c0f1c829460d327499d`.

The reproduction runner matches SHA-256 `3409dce30aaeafa5d16cf0b89e15ea0d7dba0415c1ebf9c7df3e652f67e55ae9` in all three run records and `verification.json`. Its source records each subprocess, before/after hashes, exit code and combined log hash, refuses existing gate log/metadata paths, checks exact audit coverage, and scans source. Runtime provenance and the aggregate verification summary were recorded separately; the runner alone does not regenerate those records.

## Replay trust scope

The actual local `LeanChecker.lean` implements default replay by importing the target module's environment and replaying the new target constants (lines 12–34). Its separate `--fresh` branch starts from an empty environment (lines 36–38). The executed command lacked `--fresh`.

Consequently this is a successful replay of **Q1.MomentDemand in its imported environment**. The empty checker log alone is not a success certificate; its preserved zero-exit run record, source binding, built-module hashes and checker provenance supply the evidence. Older Q1, DirectMoment and HaarShape fresh records retain their older scopes and source snapshots. This review establishes no current whole-project fresh replay, separate kernel implementation, or clean reproducible rebuild of every dependency.

## Mathematical scope and assumptions

1. A literal finite container T must contain every B+F location, including locations where signed convolution cancels to zero. Removing zero-shadow holes is not formalized.

2. coordinateVariance is the actual finite sum of squared centered coordinates; c is arbitrary. A zero variance gives zero extra demand through real division by zero.

3. The mass denominator L+H-|B| is strictly positive from L>0, H>0 and the interval containment. H bounds all of F, including zero-weight labels.

4. The full kernel is J+lam zz^T with the diagonal |B|*(|F|+lam*sum z^2) retained. lam>=0 and entrywise nonnegativity are explicit hypotheses for the payable positive-part demand; the signed residual needs no nonnegativity or separate source budget.

5. The exact increment lam*LB/2 compares two raw demands for the same full matrix and diagonal cost. Positive-part increments can be smaller; this is not an asserted gain relative to the lam=0 kernel.

6. The shared bound is finite, on pairwise disjoint actual blocks contained in one Sidon set A. Each old set P_j is disjoint from its own B_j; nested prefixes, chronological availability, and nonanticipating selection are not proved or required.

7. The one physical maximum is over full masked kernels, with span and already-used-old-label masks. Relation-pair multiplicities in F are retained; actual block labels are spent once by Sidon difference injectivity.

8. No explicit positive-demand instance, uniform envelope gap, infinite-history transport theorem, fixed-onset density-cap contradiction, or proof of Q1 follows from these supporting inequalities.

The main dependency chain was inspected in source: actual additive shadows and Sidon difference injection; first-moment cancellation and centered Cauchy; the signed channel energy with diagonal; local raw and positive-part demand bounds; then the existing finite actual-block maximum-envelope theorem. The demand bound derives the first-moment payment from the actual shadow. It does not posit an LB-payment hypothesis.

The concrete interval container is `[n+1,n+L+H-1]` with center `n+(L+H)/2`. Its variance is evaluated as a finite sum; the cubic closed form and an optimized container deleting holes are not formalized. The broad theorem allows varying `P_j,F_j,z_j,lam_j,T_j,c_j`; it proves a finite envelope inequality without an asymptotic gain or a construction of a sequence of choices.

Status: **supporting finite theorems and their preserved verification evidence accepted within the stated scope; Q1 unresolved**.
