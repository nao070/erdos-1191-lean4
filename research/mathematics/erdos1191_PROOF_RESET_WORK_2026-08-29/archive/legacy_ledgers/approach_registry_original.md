# Approach Registry — Erdős #1191

Statuses: ACTIVE, BLOCKED, MERGED, ABANDONED, PROVED.

## A. Direct combinatorial inequalities
- Status: ACTIVE (initial exploration)
- Mechanism: bound Sidon sets at finite scales and aggregate across scales.
- Proposed intermediate theorem: TBD.
- Gap: TBD.

## B. Multiscale universal sparsity
- Status: ACTIVE
- Mechanism: compare representations/differences across dyadic or geometric scales.
- Gap: unknown whether current methods beat constant-level liminf bounds.

## C. Dense algebraic/recursive construction
- Status: **BLOCKED** (2026-08-28)
- Mechanism: use dense finite Sidon objects and compatible extensions/pasting.
- **Obstruction identified**: F(V) = V + D(V) becomes dense near max(V) as V grows.
  - For |V| ≥ 30, compatibility ratio drops to 0%
  - For |V| ≥ 50, F(V) covers 100% of integers in [max(V), max(V)+100]
  - No integers available for extension while maintaining Sidon property
- **Experiment**: `computation/crossblock.py` systematic scaling study
- **Data**: `computation/out/crossblock_scaling.json`
- **Documentation**: `counterexamples.md` entry E3, `research_log.md` Wave 2
- **Conclusion**: This mechanism cannot yield asymptotic progress on #1191
- **Pivot needed**: Probabilistic methods, entropy-based approaches, or other mechanisms that avoid the deterministic obstruction

## D. Probabilistic/random-greedy construction
- Status: ACTIVE
- Mechanism: random Sidon process plus alteration.
- Gap: determine whether it can approach sqrt(x)/polylog(x).

## E. Neighboring-field transfer
- Status: ACTIVE
- Mechanism: coding theory, graph independence, containers, entropy, finite fields.
- Gap: verify transfer does not merely restate #1191.

## Registry rule
A route terminating at a lemma equivalent in strength to Q1 or Q2 is BLOCKED unless a genuinely new ingredient appears.
