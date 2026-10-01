---
name: math-evidence-promotion
description: "Use when changing the status of a mathematical claim, reporting that something is proved or verified, or deciding whether Erdős #1191 has reached a completion gate."
---

# Mathematical Evidence Promotion

## Principle
Evidence, source identity, and logical scope determine status. Agent confidence does not.

## Promotion ladder
Use the narrowest justified status:

1. `CONJECTURE`
2. `NUMERICAL`
3. `EXACT_FINITE`
4. `MATH_PROVED`
5. `INDEPENDENT_REVIEW`
6. `LEAN_VERIFIED`
7. `TARGET_CONNECTED`

`REJECTED` is orthogonal and records a disproved/invalid claim in its stated scope.

Do not require every claim to visit every rung; do require evidence for any rung claimed.

## Required evidence
- `NUMERICAL`: parameters, code/version, precision and search range.
- `EXACT_FINITE`: exact arithmetic/certificate, complete bounded domain, reproducible checker.
- `MATH_PROVED`: full quantified statement and complete derivation with every imported theorem justified.
- `INDEPENDENT_REVIEW`: fresh review artifact identifying the exact version reviewed.
- `LEAN_VERIFIED`: current source hash/toolchain, fresh successful check/build, and allowed-axiom/escape result.
- `TARGET_CONNECTED`: explicit checked dependency path to literal `Erdos1191Q1.Q1` or its literal negation.

Stale logs do not verify edited source. A worker saying `SOLVED` is an artifact to inspect, not promotion authority.

## Q1 completion
Do not mark the master goal complete unless literal Q1 or literal `¬Q1` has a complete proof and the final pinned Lean development passes fresh clean build, target identity, transitive axiom/escape audit, and independent verification.

The following are never sufficient by themselves: finite search, no-counterexample search, a positive constant bound, a selected-history theorem, an auxiliary Lean declaration, a conditional `CoreUniform -> Q1`, a checkpoint, or an obstacle report.

If evidence is mixed, preserve separate axes rather than averaging confidence. State exactly what is proved, what is only computed, and what remains open.
