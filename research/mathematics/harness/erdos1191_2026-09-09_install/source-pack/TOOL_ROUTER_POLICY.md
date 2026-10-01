# Tool Router Policy — Erdős #1191

Status: project policy candidate, 2026-09-09. This document governs **selection and exposure**, not installation.

## 1. Base registry

The user-reported Codex base environment contains 8 MCP servers / 85 tools:

| Server | Tools | Primary role |
|---|---:|---|
| `lean-lsp` | 23 | Lean goal state, diagnostics, proof exploration |
| `arxiv` | 19 | primary preprint search/retrieval/reading |
| `semantic-scholar` | 14 | citation/related-paper graph |
| `context-mode` | 11 | local long-context indexing/retrieval |
| `lean-explore` | 8 | Lean theorem/code retrieval |
| `zbmath` | 5 | mathematical bibliography |
| `mcp-oeis` | 3 | integer sequence identification |
| `exa` | 2 | broad web discovery/fetch |

Do not infer additional user-local MCPs from tools visible in some other ChatGPT/runtime.

## 2. Governing principle

`installed registry size != per-turn visible tool surface`.

Empirical tool-retrieval work supports adaptive shortlists and shows that over-presentation can reduce downstream tool-choice accuracy. Therefore:

- where the host supports per-tool deferred/dynamic loading, target a **small adaptive shortlist**, normally about 5–12 schemas;
- treat 20 visible schemas as a **soft engineering ceiling**, not a theorem or hard prohibition;
- if an MCP server is atomic and exposes more than that by itself (e.g. the current 23-tool `lean-lsp`), keep it when needed but avoid simultaneously activating overlapping servers without a named reason;
- expand the shortlist when retrieval confidence is weak or the first shortlist demonstrably misses the needed capability.

Never hard-code “7 tools” as optimal. Published values are benchmark-dependent observations.

## 3. Route by phase

### A. Local research-state recovery
Start with: `context-mode` only.

Use it to locate the exact contract, attempt, or evidence path. Once the needed files are identified, read the files directly. Do not replace source artifacts with context summaries.

### B. Informal mathematical proof search
Default: no external MCP unless a named operation requires one.

Escalate to:
- `exa` for broad/obscure web discovery;
- `zbmath` for mathematical bibliography;
- `arxiv` for the primary preprint once a candidate is identified;
- `semantic-scholar` only when citation graph, related work, or author lineage is the unresolved need.

Do not issue the same broad query to all literature servers simultaneously. Search by purpose, inspect results, then escalate.

### C. Literature saturation for a specific gap
Use `math-literature-gap-search`.

Preferred progression:
1. `zbmath` or `exa` to discover terminology/primary candidates;
2. `arxiv` to read exact statements and proofs;
3. `semantic-scholar` for citation graph/backward-forward expansion;
4. a second Exa query only for unresolved terminology, repositories, or non-arXiv sources.

Current Exa schema is assumed to support `query` and `numResults`; do not invent an `additionalQueries` argument. If multiple expansions are needed, issue separate explicit queries.

### D. Lean theorem retrieval
Start with `lean-explore` when the task is “find a declaration/theorem.”

Use `lean-lsp` when the task needs actual project state: goal, diagnostics, hover, local context, trial proof, or compilation-aware feedback. If both are needed, retrieve first, then keep the LSP surface for editing.

### E. Lean proof editing
Use `lean-lsp` as the primary server. Avoid literature MCPs in the same proof-edit turn unless a precise external theorem applicability question blocks progress.

### F. Exact finite computation
Prefer local exact integer/rational code and independent replay. Use `mcp-oeis` only when an actual integer sequence has appeared and identification would change the mathematics.

A CAS server is **optional** and may be used only after a runtime probe confirms it exists. It is not part of the 85-tool base contract.

### G. Final verification
Expose only the minimal local verification surface. No web research, no literature search, no theorem-authoring helper, and no write authority toward the candidate under judgment.

## 4. Tool-call acceptance rule

Before calling a nontrivial tool, the agent should be able to state internally:

1. **Question:** What exact unknown will this tool resolve?
2. **Artifact:** What result would count as useful evidence?
3. **Next action:** What will change if the result is positive, negative, or unavailable?

If those answers are missing, do not call the tool yet.

## 5. Duplicate and escalation control

- Reuse a source/result already retrieved when it answers the same question.
- A second search must change terminology, source class, time window, or mathematical formulation.
- Tool failure is not mathematical evidence.
- Timeout is not “no result exists.”
- Search hit is not a theorem dependency until primary-source applicability is checked.
- Tool output must record provenance sufficient to reproduce a load-bearing claim.

## 6. Router logging

For expensive or route-changing tool use, append a small route record:

```yaml
question: <named gap>
role: <math-lead|literature|falsifier|lean|verifier>
selected_servers: [..]
selected_tools: [..]        # if host exposes names
why: <why these and not broader tools>
result_artifacts: [..]
remaining_gap: <one sentence>
```

Do not log every trivial filesystem read.
