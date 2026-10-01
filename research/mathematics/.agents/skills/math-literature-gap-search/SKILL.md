---
name: math-literature-gap-search
description: "Use when a named mathematical gap in the active Erdős #1191 proof route may depend on known literature, equivalent terminology, a no-go result, or an existing formal analogue."
---

# Mathematical Literature Gap Search

## Search from the gap, not from the topic
Write the exact missing implication first. Then generate a small query family:

1. literal/near-literal formulation;
2. equivalent or dual formulation;
3. theorem-family terminology;
4. counterexample/no-go/optimality formulation;
5. formalized/Lean analogue when relevant.

Do not run a general “Sidon sets AI proof” survey when the unresolved object is a specific weighted six-endpoint correlation bound.

## Route sources by purpose
Follow `TOOL_ROUTER_POLICY.md`:

- `zbmath` / Exa: terminology, obscure sources, broad discovery;
- arXiv: primary preprint text;
- Semantic Scholar: backward/forward citation graph;
- LeanExplore: formal-library analogue, not informal literature.

Current Exa calls use the actual exposed schema. If it has no `additionalQueries` parameter, issue separate explicit query expansions rather than inventing one.

## Applicability gate
A search result becomes a usable dependency only after recording:

```yaml
source_title:
source_url_or_id:
exact_result:
ambient_objects:
hypotheses:
constants_and_uniformity:
definitions_that_must_match:
application_mapping:
status: MATCH | PARTIAL | MISMATCH | DISCOVERY_ONLY
```

Read the primary source for load-bearing claims. Check finite group vs integers, weighted vs unweighted, distinct vs repeated summands, asymptotic vs uniform, and dependence of constants. Similar wording is not equivalence.

## Stop rule
Stop searching when either:

- a source supplies a result whose assumptions can be mapped exactly into the current proof obligation; or
- the query families and citation expansion converge without a new usable theorem.

Record negative search scope honestly; “not found” is not a proof of novelty or impossibility.
