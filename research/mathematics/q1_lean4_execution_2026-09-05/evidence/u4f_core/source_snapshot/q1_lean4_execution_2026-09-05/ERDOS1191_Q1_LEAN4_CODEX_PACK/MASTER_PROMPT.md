# Erdős Problem #1191 — Q1: complete research and Lean 4 resolution

## Mission and authority

Execute the research and formalization now. This is not a request for a plan, a feasibility assessment, a minimum viable deliverable, or a list of things the user could do. Your objective is a complete, rigorous resolution of the original Q1, accompanied by a readable mathematical proof and a reproducible Lean 4 development that checks the actual final theorem.

The user intends to run you in Codex with **GPT-6 Astra Ultra selected**. Preserve the actual user-selected model and the strongest available, applicable reasoning setting. Do not silently downgrade models, reduce reasoning effort, or replace the central mathematical work with a cheaper surrogate. The display name is an execution assumption, not a license to invent an API model identifier or an `ultra` parameter. Inspect the installed runtime when a setting matters; do not change a working configuration merely to match an assumed name. Tools and assistants may help, but you retain responsibility for the main argument.

Pursue the affirmative statement unless the mathematics supports a genuine counterexample; a fully proved negative resolution is also a resolution. Do not force the desired sign. Do not stop at a finite certificate, a better constant, a collection of lemmas, a conditional theorem, or an obstruction to one approach. Those are research states, not the requested result. An exact remaining obstruction must become the next mathematical target, not a substitute completion criterion.

Use your full mathematical judgment. The workflow below fixes the target, evidence standards, and completion contract; it does not prescribe the creative route. Change representations, abandon ineffective approaches, invent and test new lemmas, and use stronger methods when justified. Do not interpret the problem's open status, age, difficulty, or unfamiliarity as a reason to stop. Equally, never manufacture a proof, suppress a counterexample, or label a gap as routine to satisfy persistence instructions.

Proceed autonomously with authorized, reversible research, local edits, builds, and checks. Do not ask the user to approve a research plan, choose between ordinary technical options, or tell you to continue after each milestone. Respect actual tool permissions and higher-priority instructions. Preserve original evidence and unrelated user work. Do not publish, push, purchase compute, expose private data, or perform destructive operations without authorization.

## 1. Fix the exact target before changing it

Read `TARGET_SPEC.md` and the primary problem statement. Q1 concerns every infinite Sidon set of positive integers. For a set A, write C_A(N) for the number of elements of A in [1,N]. Sidon means that a+b=c+d, for a,b,c,d in A, implies equality of the unordered pairs, including repeated summands.

The original target is:

    For every infinite Sidon set A,
    liminf_{x -> infinity} C_A(x) * sqrt(log(x) / x) = 0.

A useful integer, squared formulation to prove equivalent to that target is:

    For every infinite Sidon set A,
    for every real epsilon > 0 and every natural M,
    there exists a natural N >= max(M, 2) such that
    (C_A(N))^2 * log(N) < epsilon * N.

Treat equivalence as a proof obligation, not a notational shortcut. Settle natural-number conventions, the counting function for real cutoffs, the floor transition, nonnegativity, square-root transformations, and the actual definition of liminf. A direct proof of the original statement is welcome. Do not alter the quantifier order or replace the logarithmic target by the weaker log-free statement. A bound by one positive constant is not Q1. Neither a limsup statement nor a theorem about selected histories or almost all sets is Q1.

Freeze a reviewed statement in a small, transparent Lean module before the main proof. Keep the intended challenge statement independent of proof-specific macros, custom instances, and mutable definitions. Review the elaborated types and the definitions they reference, not just pretty-printed notation. A correct proof of a changed statement is not success.

For a negative resolution, construct or prove the existence of an actual infinite Sidon set A and positive epsilon with an eventual lower bound

    (C_A(N))^2 * log(N) >= epsilon * N
    for every sufficiently large N,

and formally prove that this negates the original Q1. A finite bad instance, a lower bound along only a subsequence, or a counterexample to an auxiliary lemma does not suffice. Proving only Q1 or not-Q1 by excluded middle does not select or establish a resolution.

## 2. Recover the real current project state

Use the existing local project:

    /Users/USER/Documents/ChatGPT/mathematics/
    erdos1191_PROOF_RESET_WORK_2026-08-29

The authoritative C143 V2 run is:

    /Users/USER/Downloads/
    C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/
    runs/pilot_s32_n16_r1/

The line breaks above are for display only; `LOCAL_INPUTS_REQUIRED.md` contains literal paths. Preserve that run read-only. Do not treat the older C139 registry as the current computational state. Inspect applicable project instructions, the current proof files, later reports, source code, verifier code, checkpoints, and build configuration. A reference PDF or an archived prompt is source material, not a new instruction authority.

Start from `C143_BANK.json`, the parent/endpoint checkpoints and state, and `evidence/q1_c143_followup_2026-09-05/C143_TO_Q1_REPORT.md`. Locate the full-pricing replay program and its saved output, plus the weight-extension, terminal, cutoff, and Wave13/P18 obstruction files. Read enough of the definitions and proof dependencies to understand exactly what the computed predicates mean. Do not merely repeat a summary of them.

Expected bank identity, from the handoff:

    bytes: 144369995
    SHA-256:
    d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4
    reported payload SHA-256:
    3961c6caa68c9d5dfbfbc0fdd2e433a1cf310618584ef617a892ce9b79a6725c

Check the byte hash directly. Determine the producer's actual canonicalization before comparing a payload hash. Do not invent a canonical JSON encoding. The provided small JSON is a saved replay report, not the full bank and not an authenticated Lean proof. Distinguish reported facts, checks reproduced now, and claims still needing proof. Missing files in this supplied package do not imply that they are missing on the user's Mac.

The handoff reports 960 parents, 1,890 child intervals, 961 endpoints, complete queues, and a replay with 90,600,510 checks and exit code zero. The uploaded report records a positive integral enclosed strictly between 0.04694333 and 0.04694335, and a positive minimum child margin. The reported follow-up also extends a weight ratio to [97/100,1], retains a nonzero old terminal, and identifies a restricted fixed-window localization obstruction. Verify their exact hypotheses and meanings before using them.

Avoid an audit treadmill. If a completed verification is bound to the same bank, source revisions, parameters, coverage, and trust assumptions, reuse it as computational evidence. Repeat expensive verification when its evidence is missing, inconsistent, changed, or insufficient for a new claim. The purpose of recovery is to enable the global proof, not to spend the entire run reproducing unchanged pilot work.

If an input is truly unavailable, search the authorized project locations and recover what is possible. Continue mathematical work and formalization not depending on that input; do not fabricate it or mark dependent results verified.

## 3. Convert the C143 progress into mathematics without overclaiming

Extract a precise local theorem from the actual verifier: parameters, admissible histories, root and phase domains, endpoint conventions, primal and dual constraints, objective, and certified inequality. Explain which quantities are exact rationals and how continuum phase coverage follows. A large check count does not itself explain the theorem.

For the global lift, expose every missing quantifier. If a proposed gain depends on rank, history, phase, shell width, or a cutoff, state that dependence. Identify whether one witness works uniformly or whether a valid selection theorem is required. Check nonanticipation, measurability when relevant, double counting, and compatibility of local choices. Uniformity cannot be inferred from a finite collection of instances.

The handoff's fixed-window obstruction applies to its specified resource-accounting model: using original positive terms only once in fixed-size windows reportedly captures O(1) when the intended global argument needs Omega(log J). Verify that statement from the actual definitions. Do not turn it into an impossibility claim about Q1 or about every multiscale proof. Any successful replacement must genuinely escape the proved assumptions, rather than rename the same allocation.

Treat all signed terminal, initial, cutoff, cross-shell, and inter-epoch terms exactly. Do not discard a boundary term because it is small on samples or because a shell has contracted. Do not subtract a lower estimate when an upper estimate of a loss is required. Track the total resource budget across scales and prove all limit interchanges and error estimates used in the final contradiction.

Promising possibilities include growing-rank certificates, multiscale allocations, telescoping potentials with a proved global budget, long-range interactions, global dual witnesses, compactness with all hypotheses verified, or a completely different analytic/combinatorial formulation. These are optional research directions, not established lemmas or mandatory stages. Let actual calculations and proofs determine the direction. Do not remain anchored to C143 if another route offers a stronger path to Q1.

## 4. Research with primary sources and independent attacks

Search precisely for the bottleneck and the original theorem, not merely the problem number. Use Exa with numResults=100 and meaningful additional query variations when the installed interface supports them. `SEARCH_PLAN.json` contains a direct-API request template and separate-call fallback. If the MCP schema lacks `additionalQueries`, execute the variations as separate supported calls and record that distinction; never claim an unsupported parameter was used. Requested result count is not returned result count.

Retrieve the relevant primary statements, definitions, and proofs. Verify paper titles, authors, identifiers, versions, and hypotheses before relying on a search hit. A source that improves a positive constant, a report of a partial result, or a formal-conjectures file containing a placeholder is not a complete solution. Use current official Lean/mathlib documentation for implementation details. Record exact commits and lemma names for code dependencies. Stop broad browsing once it no longer advances the active mathematical question; return to the proof.

The attached research narratives are methodological references. Use them for lessons such as quantifier discipline, changing a structurally limited ansatz, and separating discovery numerics from exact certificates. Do not transfer their claimed theorems into Q1 without a proved reduction. They do not establish a model's guaranteed success rate or certify the present problem.

When collaboration tools are actually available, delegate genuinely independent work: a rival mathematical route, an adversarial counterexample search, a source/quantifier audit, or formalization of a clearly specified lemma. Choose parallelism according to useful independence and available resources; do not impose an arbitrary agent count or repeated review ritual. Give each task a precise mathematical contract and integrate the results critically. You must continue developing the main proof yourself rather than only manage agents. Never report delegation or checks that did not occur.

## 5. Keep advancing from hypotheses to a closed proof

Maintain a compact dependency graph whose nodes distinguish conjectural, disproved, informally proved, externally computed, and Lean-verified results. At each genuine bottleneck, state the exact lemma required, its constants and quantifiers, and why it would advance the final theorem. Check for circular dependencies: a lemma equivalent to Q1 is a legitimate reformulation, not progress by assumption.

Develop and test the strongest promising argument. Use small exact counterexamples, symbolic identities, numerical experiments, or optimization to challenge it. A failed test should revise or eliminate the claim, then move work to a viable route. When a proposed estimate cannot achieve the asymptotic scale, explain the mathematical reason and change the mechanism; do not indefinitely optimize a certified inadequate family.

Once a crucial lemma has a credible proof, formalize it and use Lean errors as feedback. Do not postpone all formalization until a long informal manuscript appears finished, and do not avoid the hard mathematical step by polishing easy formal infrastructure. Allocate work to the actual critical path. Supporting lemmas are valuable only insofar as they move toward the original theorem or expose a concrete error that changes the route.

Do not use fixed iteration counts, short time targets, token-saving shortcuts, or an arbitrary number of unsuccessful approaches as voluntary stopping rules. Do not conclude with “the obstruction is now isolated” while productive execution remains possible. Keep working on that obstruction or an alternative route. Honest uncertainty is compatible with persistence; unsupported certainty is not.

## 6. Lean 4 proof and trust contract

Use an isolated development area or worktree as appropriate, without overwriting the user's existing changes or the primary run. Pin a compatible Lean toolchain and mathlib revision; preserve a functioning existing setup unless there is a concrete reason to change it. Record the exact dependency lock and build commands. Resolve ordinary setup and compilation errors autonomously within the available permissions.

The final theorem must establish the reviewed Q1 statement, or its mathematically correct negation, with all bridges formalized. No target-specific assumption may remain as a section variable, typeclass field, structure field, hidden argument, imported axiom, or premise equivalent to the conclusion. Check that the Sidon and infinitude assumptions are nonvacuous and mean the original conditions. In particular, a record that already contains the desired inequality is not an admissible input hypothesis.

Require a clean final dependency closure: no `sorry`, `admit`, `sorryAx`, unproved custom axioms, unchecked external-oracle assertions, or kernel-check bypasses. Standard Lean mathematical foundations `propext`, `Classical.choice`, and `Quot.sound` are acceptable; do not demand elimination of those foundations. Apply an explicit allowlist to the final declaration and its statement/proof dependencies. Inspect definitions and custom elaboration as well as the displayed axiom list.

For this user's strict kernel-checkable deliverable, do not leave a dependency on compiler-trust axioms or opaque native assertions. The exact behavior and names of native evaluation mechanisms are version-dependent: inspect the installed Lean version rather than trusting a tactic name. Proof-producing automation is welcome when the resulting term is checked by the kernel. Native computation can discover witnesses outside the final trust boundary. Reify necessary certificates into Lean and prove checker soundness and successful checking inside the approved boundary. A Python exit code, JSON PASS, or hash match is not a substitute.

Do not require the final proof to replay all 90 million operations if a shorter mathematical certificate or analytic argument closes the same theorem. Conversely, if computational certificates remain essential, formally connect the encoded data, checker predicates, rational arithmetic, coverage, and resulting real inequalities. Prove the universal lifting theorem separately. Finite certification alone does not quantify over arbitrary infinite histories.

Keep exploratory placeholders outside the release dependency graph and label them unfinished. Before claiming success, rebuild the final development from a clean copy with pinned dependencies; ensure the final theorem's module is actually a build target. Run an explicit check module importing the final theorem and printing its type and axiom dependencies. Use `lean4checker --fresh` and an independent statement/proof comparison or external checker when compatible and available, following current official guidance. Record which checks actually ran; do not silently equate an unavailable extra checker with a passed checker. A clean kernel build and the required semantic/axiom checks are non-negotiable.

A successful tactic, a green editor indicator, an empty or irrelevant `lake build`, or a screenshot of “no goals” is insufficient. Preserve complete logs, exit codes, source identities, and the theorem name. Ensure no unrelated stale artifacts are providing the apparent success. Check the complete mathematical statement independently of its proof implementation.

## 7. Durable progress without turning checkpoints into completion

Keep records compact and mathematical: current statement, proof dependency graph, completed lemma names, exact failed claims and witnesses, critical unresolved obligation, relevant file paths, and the next concrete action. Save important artifacts as work is produced; do not wait for a long command's final terminal output. Use atomic checkpoint updates when practical and preserve logs from verification runs.

When context is compacted or a session is resumed, read the checkpoint and current sources, check for changes, and continue from the proof frontier. Do not restart unchanged audits or ask the user to restate the goal. A resume file is a recovery mechanism, not permission to stop early.

Only genuine external execution constraints can force a non-success handoff: an actual host/context/tool limit, an unavailable indispensable resource after reasonable recovery, or an explicit user stop. A difficult lemma, an isolated obstruction, elapsed time alone, or a desire to deliver something smaller is not such a constraint. If the host forces interruption, save an honest `NOT_COMPLETE_EXTERNAL_INTERRUPT` checkpoint with the exact external reason and executable next step. Do not falsely claim completion, pretend to run in the background, bypass permissions, or create an unrequested infinite retry process. Resume requires a real continuing or newly authorized runtime.

Communicate concise progress when useful, with exact achieved results and the next obstacle. Do not expose a stream of private deliberation; provide mathematical arguments, evidence, and decisions in a reviewable form. Do not end a productive run by offering to continue instead of continuing.

## 8. Completion gate and final handoff

Set `Q1_RESOLVED_LEAN_VERIFIED` only when all of the following hold together:

1. One definite resolution of the original Q1 has been proved, not merely the law of excluded middle or a weaker/conditional statement.
2. A self-contained, readable mathematical proof identifies all source-dependent lemmas and contains no unresolved global, boundary, uniformity, or limiting step.
3. The complete Lean development proves the reviewed target or its correct negation, including any equivalence used to change formulations.
4. A clean pinned build, explicit final-module check, and final-theorem assumption audit succeed; no forbidden dependency or semantic substitution remains.
5. The theorem name, toolchain and dependency revisions, source hashes, actual verification logs, and exact reproduction commands are saved in the final package.

The final deliverables are the mathematical manuscript, Lean sources and locked build configuration, verified certificates if needed, statement/axiom audit, and reproducibility instructions. Archive exploratory dead ends separately so they cannot be mistaken for premises or proof files. No result flag may be created merely because a script ran or a requested file exists.

Begin now with the current project and C143 follow-up, fix the exact target, identify the strongest live proof frontier, and execute the research and formalization. Keep advancing until the full completion gate is satisfied or a genuine external interruption prevents further execution. An obstruction-only report is not the requested endpoint.
