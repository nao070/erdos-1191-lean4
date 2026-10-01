# Harness Change Contract

This project-specific contract combines the change-manifest idea of Agentic Harness Engineering with the weakness/proposal/validation loop of Self-Harness, while keeping mathematical truth criteria fixed.

For each candidate create one record:

```yaml
change_id:
parent_harness_hash:
model_and_effort:
trigger:
  failure_cluster_ids: []
  supporting_trace_ids: []
observation:
  terminal_failure:
  causal_behavior:
  reusable_mechanism:
proposal:
  surface:
  files: []
  minimal_diff_summary:
prediction:
  fixes: []
  regressions_at_risk: []
validation:
  held_in_cases: []
  protected_cases: []
  repeats:
  current_results: {}
  candidate_results: {}
verdict: ACCEPT | REJECT | INCONCLUSIVE | INVALID
reason:
rollback_pointer:
```

The evaluator, Q1 contract, final verifier, and protected cases are not editable surfaces.
