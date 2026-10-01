---
name: harness-evolution
description: Use when explicitly asked to improve this research harness or when repeated execution traces show the same reusable operational failure in routing, context, verification, recovery, delegation, or Skill behavior.
---

# Harness Evolution

## Boundary
This is a meta-workflow. Do not run it merely because the mathematics is difficult or a conjectured inequality is false. Ordinary proof search stays under the research Skills.

Immutable: Q1/negation semantics, Lean target, completion criterion, trusted verifier/axiom policy, protected evals, resource authority, and frozen theorem semantics. These are read-only to the evolver.

Mutable: tool routing, context-selection rules, project-local Skill text, role prompts, failure taxonomy, and non-truth bookkeeping.

## 1. Weakness mining
Use verifier-grounded traces, not anecdotes. Cluster recurring failures by terminal failure, causal agent behavior, and reusable mechanism. Preserve raw traces for drill-down; summaries are navigation aids.

If the evidence indicates model/mathematical capability rather than an editable harness mechanism, emit `NO_HARNESS_CHANGE`.

## 2. Minimal proposals
Generate at most three materially distinct candidates. Each candidate changes one smallest useful surface and includes:

```yaml
failure_evidence:
root_cause:
target_surface:
minimal_change:
predicted_fixes:
predicted_regressions:
```

No broad rewrites, “best practice” edits without evidence, or task-specific theorem answers embedded into generic Skills.

## 3. Validation
Evaluate the current harness and each candidate under the same model/budget/evaluator. Use failure-targeted cases plus protected regression cases that the proposer does not optimize against.

Promote only if the candidate fixes at least one targeted/protected metric **without degrading any protected passing behavior**. If evaluation is stochastic, repeat before promotion. Rejected proposals stay logged.

For new Skills, run the pressure-test protocol: baseline without Skill, candidate with Skill, regression set, then mark `HOT` only when the trace shows a genuine improvement. Otherwise keep `COLD`/`WARM` or reject.

## 4. Decision record
Every accepted edit is a falsifiable state transition: evidence → diagnosis → edit → prediction → evaluation → verdict. Never let the same agent alter the verifier or hidden/protected tests used to judge its edit.

Default mode is `PROPOSE_ONLY`; applying an evolution candidate requires explicit project authority or an already-approved automation policy.
