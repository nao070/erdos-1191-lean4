# AGENTS.md — Erdős Problem #1191 Q1

This repository is a long-horizon research workspace for resolving the literal original Erdős Problem #1191 Q1. The model may discover mathematics, falsify routes, run exact finite experiments, retrieve literature, and formalize results in Lean. It may **not** redefine success.

## 1. Read order and authority

At the beginning of a fresh or compacted research session, read only what is needed in this order:

1. `MASTER_PROMPT.md` — binding research objective and completion condition.
2. `research/PROBLEM_CONTRACT.md` — authoritative mathematical semantics of Q1 and its exact negation.
3. `q1_lean4_execution_2026-09-05/lean/Q1/Target.lean` — literal Lean target.
4. `research/NEXT_THEOREM_CONTRACT.md` — authoritative active mathematical obligation.
5. `research/STATE.md` and `research/UNRESOLVED_CORE.md` — checkpoint state and unresolved dependency graph.
6. `research/LEAN_CLAIM_LEDGER.md` — scope of existing Lean evidence.
7. Only then read source files directly required by the current attack.

If an authoritative file is missing or two authoritative files materially disagree, do not reconstruct the missing contract from memory. Record the conflict and recover the source before making mathematical promotion claims.

## 2. Immutable truth surface

The following are outside the authority of researchers, subagents, Skills, and harness evolution:

- the literal original Q1 and its exact negation;
- quantifier order, positivity, infinity, liminf, normalization, natural-log convention, and Sidon convention;
- the literal final Lean proposition;
- the distinction between finite evidence, mathematical proof, and Lean verification;
- the final completion criterion;
- the trusted verifier and its axiom/escape policy;
- protected regression/evaluation cases.

Do not weaken, specialize, rename away, or silently replace these objects to make a proof easier.

## 3. Current checkpoint, not a permanent axiom

As of the 2026-09-09 checkpoint, the active route is U4-F and the frozen next theorem is `Q1191-U4F-CORE-UNIFORM-01`. Gate 0 six-endpoint localization was reported mathematically reviewed, not Lean-verified. The active contract file, not this paragraph, is authoritative if later research legitimately advances the frontier.

U4-E, U4-R, and U4-G remain dormant alternative lineages. Do not erase them. Do not restart them merely because one stronger sufficient estimate inside U4-F fails.

## 4. Research loop

For an active theorem:

1. **Recover minimally.** Load its contract, direct dependencies, last nonduplicate attempts, and relevant evidence. Do not rerun whole-project preflight without a concrete inconsistency.
2. **State one attack.** Write one fully quantified candidate lemma/estimate or one explicit counterexample mechanism. A research theme is not an attack.
3. **Check before investing.** Test boundary cases, signs, quantifier dependence, exact finite fixtures, and known failure classes when applicable.
4. **Do substantive mathematics.** Derive, falsify, or sharply localize the candidate. Do not stop at planning if an executable mathematical step remains.
5. **Persist the attempt.** Keep the load-bearing derivation or counterexample artifact and an append-only attempt record. A summary is an index, not a replacement for raw evidence.
6. **Adversarially review important candidates.** Route-changing lemmas, global uniform estimates, limiting bridges, and claimed counterexamples receive a fresh falsification pass.
7. **Promote only with evidence.** Use the evidence-promotion contract; worker self-reports do not change project truth status.
8. **Formalize stable interfaces.** Use Lean when a statement is stable or when Lean feedback can decide a fragile point. Do not create custom axioms to bypass the research gap.
9. **Continue the critical path.** A checkpoint is not Q1 completion.

Never retry a failed mechanism under new notation unless a mathematically relevant ingredient changed. Record that change explicitly.

## 5. Role contracts

### Math Lead / Integrator
Owns theorem fidelity, route selection, synthesis, and the final status report. May read broadly. Must not accept its own major claim without external evidence.

### Falsifier
Fresh or deliberately minimized context. Read-only toward the candidate statement and authoritative contracts. Tries to break one claim. Returns a witness, a precise gap, or bounded `NO_COUNTEREXAMPLE_FOUND`; it does not silently repair the claim.

### Exact-computation worker
Receives one checkable question. Uses integer/rational/certified interval arithmetic where the claim requires exactness. Reports the verified scope and what the computation does **not** prove.

### Lean formalizer
Works on a stable statement or a named conditional interface. Uses Lean/LSP feedback as evidence. It may refine proof decomposition, but it must not silently alter an authoritative mathematical statement.

### Independent verifier
Read-only toward the candidate. Checks literal target identity, clean build, dependency/axiom footprint, escape tokens, and evidence/source identity. It does not repair what it judges.

Parallelize only genuinely independent work. Default to one Math Lead plus at most one focused worker; use a second worker only when the tasks have no shared state or sequential dependency. Delegation depth is one.

## 6. Evidence vocabulary

Use these labels literally unless a more specific project ledger already defines them:

- `CONJECTURE` — proposed claim, no adequate proof.
- `NUMERICAL` — floating/heuristic experimental evidence.
- `EXACT_FINITE` — exact computation on a bounded domain or explicit finite certificate.
- `MATH_PROVED` — complete mathematical proof reviewed against its stated hypotheses, not yet Lean-verified.
- `INDEPENDENT_REVIEW` — a fresh reviewer found no unresolved fatal gap in the stated scope.
- `LEAN_VERIFIED` — current source was freshly checked by Lean with an audited allowed-axiom footprint.
- `TARGET_CONNECTED` — the verified result is formally/logically connected to the literal Q1 or literal negation through checked dependencies.
- `REJECTED` — claim or route was disproved/invalidated within the recorded scope.

`LEAN_VERIFIED` is not `TARGET_CONNECTED`. `EXACT_FINITE` is not `MATH_PROVED`. “No counterexample found” is never a proof label.

## 7. Completion gate

The master research goal is complete **only** when one of the following is established under the project trust policy:

- a complete proof of literal `Erdos1191Q1.Q1`; or
- a complete proof of literal `¬ Erdos1191Q1.Q1`;

and the final pinned Lean development passes a fresh clean build, target/type check, transitive axiom/escape audit, and independent verification tied to the candidate source hashes.

Finite bounds, a frozen next theorem, a checkpoint, an obstacle, a reviewer saying “solved,” or a Lean proof of an auxiliary theorem do not satisfy this gate.

## 8. Tool policy

Follow `TOOL_ROUTER_POLICY.md`. Installed tool count is not a target for per-turn exposure or usage. Prefer the smallest tool surface that can answer the current named question, and escalate only when the remaining gap is explicit.

## 9. Skills

Project-local reusable workflows live under `skills/`:

- `critical-path-proof-research`
- `open-math-falsifier`
- `math-evidence-promotion`
- `math-literature-gap-search`
- `harness-evolution` (meta-only; dormant during ordinary proof search)

For Lean proof editing, prefer the upstream Lean FRO `lean-proof` Skill if installed and version-compatible rather than copying a stale local fork. Local project contracts override generic Skills when they conflict.

## 10. Harness evolution boundary

Ordinary mathematical failure is not evidence that the harness is broken. Invoke harness evolution only on explicit request or when repeated trace evidence identifies a reusable operational failure (routing, context selection, verification behavior, state recovery, or delegation).

Harness evolution may change prompts, routing rules, Skill text, context-selection policy, and non-truth bookkeeping. It may not modify the immutable truth surface, evaluator, final verifier, protected tests, resource authority, or theorem semantics. Every accepted change requires an auditable failure-to-edit hypothesis and non-regression evidence.
