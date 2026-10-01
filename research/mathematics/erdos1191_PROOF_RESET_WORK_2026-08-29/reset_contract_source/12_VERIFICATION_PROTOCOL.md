# Verification Protocol

## Claim tiers

1. `FORMAL_THEOREM` — Lean-checked, no sorry, axiom report recorded.
2. `HUMAN_PROOF_AUDITED` — complete prose proof independently checked.
3. `HUMAN_PROOF_PENDING_AUDIT` — plausible prose proof, not independently checked.
4. `COMPUTATIONAL_FINITE` — exact finite scope only.
5. `CONDITIONAL_NO_GO` — theorem under explicitly named assumptions or for a named method class.
6. `HEURISTIC` — experiment or analogy.
7. `LITERATURE_QUALIFIED_NULL` — no result found in a documented but incomplete search.
8. `OPEN` / `REFUTED`.

## Tier FAST

Run after each edit:

- parse/type/syntax check;
- focused unit tests;
- hand cases for smallest legal indices;
- mutation check for changed sign/index;
- no cache provider and no bytecode in the research tree.

Target: under 30 seconds.

## Tier FOCUSED

Run when a theorem candidate stabilizes:

- independent slow oracle;
- optimized implementation comparison;
- exact rational arithmetic where possible;
- randomized and adversarial fixtures;
- minimized counterexample on failure;
- deterministic JSON certificate with schema and self-hash;
- explicit finite scope statement.

## Tier FORMAL

Run for proof-kernel theorems:

- clean `lake build`;
- no `sorry` grep;
- `#print axioms` output;
- theorem statement diff against prose;
- clean rebuild after deleting build artifacts.

## Tier RELEASE

Only after a genuine theorem milestone:

1. remove caches from release candidate;
2. full pytest;
3. regenerate every included deterministic certificate;
4. compare byte-for-byte where determinism is promised;
5. generate inventory and self-excluding SHA-256 manifest last;
6. create ZIP;
7. `unzip -t`;
8. extract into a clean directory;
9. repeat full runner and manifest verification;
10. record software versions and exact commands.

## Independent-oracle rule

The certificate generator cannot be the sole oracle for its own theorem. Use at least one of:

- a literal enumerator with a different derivation;
- a formal proof;
- a symbolic algebra derivation checked at random exact points;
- hand-computed base cases;
- a second implementation in a different language/library.

## Quantifier checklist

For every asymptotic statement record:

- order of `forall` and `exists`;
- dependence of constants;
- “eventually” threshold dependencies;
- liminf vs limsup;
- subsequence vs all sufficiently large scales;
- one fixed infinite branch vs terminal-scale-dependent finite witnesses;
- integer vs real hypotheses.

## Resolution checklist

A solution package must include:

- exact official theorem statement;
- complete proof;
- source audit;
- formal kernel;
- independent red-team report;
- clean release evidence;
- expert review notes;
- honest unresolved limitations, if any.
