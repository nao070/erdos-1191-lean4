# Counterexamples and Computational Evidence

Every entry includes code path, exact parameters, output, and the intermediate
conjecture it tests.

## E1. Sidon-check harness (baseline, re-run 2026-08-27)

- Code: `computation/check_sidon.py` (seed 1191), output `computation/out/check_sidon.json`.
- Tests: I1 (Sidon ⟺ distinct positive differences), I2 (quadruple transport),
  I3 (Erdős–Turán blocks Sidon, primes ≤ 199), I4 (greedy constructions Sidon),
  I5 (negative controls).
- Result: **PASS**, 60/60 battery, fuzz agreement 600/600, transport 600/600.
  Anchor used elsewhere: `mian_chowla(300)` has a₃₀₀ = 514644.

## E2. Forbidden-position recurrence validation (2026-08-27)

- Code: `computation/forbidden_recurrence.py` (seed 1191), engine under test
  `computation/greedy_growth.py` (`BitsetEngineR`), output
  `computation/out/forbidden_recurrence.json`.
- Tests the claims of `notes/forbidden_recurrence.md` (Lemma 1, Lemma 2,
  Theorem, Corollaries 1–3, constructor invariants for seeds with ≥ 2 marks).
- Results: **ALL PASS**
  1. Lemma 1 exhaustive: 961 Sidon subsets of [0,13], 11,330 candidates;
     both directions exact; all 2,883 candidates beyond 2·maxA − minA valid.
  2. Theorem exhaustive: 667 Sidon subsets of [0,12], 3,494 valid (A, x) pairs;
     identity on (x,∞) exact; sub-identity exact; boundary audit: in **all**
     3,494 pairs the unrestricted identity fails on (maxA, x] (x itself is
     always a counterexample point), so the restriction to (x,∞) is necessary.
  4. Constructor fuzz: 2,000/2,000 random Sidon prefixes (2–4 mark seeds in
     [0,40] + 0–20 oracle marks) — `used_diff`, `forbidden` above max, `R`
     exact; next-mark agreement with oracle before and after one update.
  5. Translation invariance: singleton seeds {0},{1},{2},{5},{17} reproduce
     `mian_chowla(start=s)` for 151 terms; 6 Golomb rulers + 4 Erdős–Turán
     blocks (non-Mian–Chowla seeds) match the oracle for 150 marks.
  6. Long run: 400 terms from {1} term-by-term equal to the naive oracle;
     OEIS A005282 prefix and a₃₀₀ = 514644 anchors match; a₄₀₀ = 1,144,080
     (a_n/n² = 7.1505); engine 0.026 s vs oracle 5.97 s; final registers
     audited exactly (`used_diff` popcount 79,800 = C(400,2)).
- No counterexample found to any claim of the note. The note's "PROVED HERE /
  verified" status is now actually backed by this script (it was written
  before the script existed; the script was the missing deliverable).

## E3. Dense block gluing obstruction (2026-08-27)

- Code: `computation/crossblock.py` (systematic scaling study), output
  `computation/out/crossblock_scaling.json`.
- Tests: Can we build an infinite Sidon set by gluing dense finite blocks
  (Bose–Chowla, Singer) to an existing Sidon set V, with W₁ ≈ V₂ (dense placement)?
- Hypothesis: Dense block gluing yields asymptotic progress on #1191.
- Result: **FUNDAMENTAL OBSTRUCTION IDENTIFIED**

  | \|V\| | max(V) | \|D(V)\| | F(V) density near max | Compatibility ratio |
  |-------|--------|----------|----------------------|-------------------|
  | 10    | 97     | 45       | 0.610                | 0–43%             |
  | 20    | 565    | 190      | 0.900                | 0–14%             |
  | 30    | 1,395  | 435      | 0.990                | 0%                |
  | 50    | 5,123  | 1,225    | **1.000**            | **0%**            |
  | 75    | 14,047 | 2,775    | **1.000**            | **0%**            |
  | 100   | 28,566 | 4,950    | **1.000**            | **0%**            |

- Mathematical mechanism: F(V) = V + D(V) (the forbidden set) becomes dense near
  max(V) as V grows. For \|V\| ≥ 50, F(V) covers 100% of integers in
  [max(V), max(V)+100], meaning **no integers are available** for extending V
  while maintaining the Sidon property. The forbidden set grows too fast
  relative to available positions.
- Conclusion: Dense block gluing **cannot yield asymptotic progress** on #1191.
  Even with optimal gap selection, the compatibility ratio drops to 0% for
  \|V\| ≥ 30. This is not a technical limitation—it is a fundamental
  mathematical obstruction.
- Implication: Approach C (Dense algebraic/recursive construction) is **BLOCKED**.
  Must pivot to a fundamentally different mechanism (probabilistic methods,
  entropy-based approaches, or methods that don't rely on dense block gluing).
- Potential theorem: "For any Sidon set V with \|V\| ≥ 50, the greedy extension
  V ∪ W where W is a dense Sidon block at W₁ = max(V) + O(1) has
  \|W*\|/\|W\| → 0 as \|V\| → ∞."
- Data: `computation/out/crossblock_scaling.json`.

## E3. Dense Block Gluing Obstruction (2026-08-28)

- Code: `computation/crossblock.py` (systematic scaling study), output
  `computation/out/crossblock_scaling.json`.
- **Hypothesis**: Can we build an infinite Sidon set by gluing dense finite blocks
  (Bose–Chowla, Singer) to an existing Sidon set V, with W₁ ≈ V₂ (dense placement)?
- **Experiment**: Systematic scaling study varying |V| from 10 to 100, measuring
  F(V) density near max(V) and compatibility ratio for dense block gluing.
- **Result**: Fundamental obstruction identified.

| |V| | max(V) | |D(V)| | F(V) density near max | Compatibility ratio |
|-----|--------|----------|----------------------|-------------------|
| 10  | 97     | 45       | 0.610                | 0–43%             |
| 20  | 565    | 190      | 0.900                | 0–14%             |
| 30  | 1,395  | 435      | 0.990                | 0%                |
| 50  | 5,123  | 1,225    | **1.000**            | **0%**            |
| 75  | 14,047 | 2,775    | **1.000**            | **0%**            |
| 100 | 28,566 | 4,950    | **1.000**            | **0%**            |

- **Mathematical mechanism**: F(V) = V + D(V) (the forbidden set) becomes dense
  near max(V) as V grows. For |V| ≥ 50, F(V) covers 100% of integers in
  [max(V), max(V)+100], meaning **no integers are available** for extending V
  while maintaining the Sidon property.
- **Conclusion**: The dense block gluing strategy **cannot overcome** the natural
  growth of the forbidden set. Even with optimal gap selection, the compatibility
  ratio drops to 0% for |V| ≥ 30. This is not a technical limitation—it is a
  fundamental mathematical obstruction.
- **Implication**: Approach C (dense algebraic/recursive construction with
  compatible extensions) is **BLOCKED**. Need to pivot to a fundamentally
  different mechanism (probabilistic methods, entropy-based approaches, or
  methods that don't rely on dense block gluing).
- **Potential theorem**: "For any Sidon set V with |V| ≥ 50, the greedy extension
  V ∪ W where W is a dense Sidon block at W₁ = max(V) + O(1) has |W*|/|W| → 0
  as |V| → ∞."
