# Lean 4 Proof Kernel Plan

## Goal

Formalize only the fragile core that separates established reductions from the genuinely open theorem. Do not formalize hundreds of infrastructure files.

## Project contract

- Pin Lean and mathlib versions.
- Clean `lake build` from an empty cache-compatible checkout.
- No `sorry`.
- Record `#print axioms` for every exported theorem.
- Prefer explicit finite inequalities over opaque asymptotic notation.
- Each Lean theorem has a matching prose statement and an index-convention note.

## Module 1 — Sidon basics

Suggested files:
- `Erdos1191/Sidon.lean`
- `Erdos1191/GapVector.lean`

Definitions:
- additive Sidon set via unique unordered sums;
- positive-difference Golomb property;
- finite prefix and increasing enumeration;
- gap vector and contiguous sums.

Theorems:
1. additive Sidon iff nonzero positive differences are unique.
2. finite increasing ruler is Golomb iff all contiguous gap sums are unique.
3. adjacent gaps are distinct positive integers.

## Module 2 — Q1 / critical cap equivalence

Suggested file: `Erdos1191/CriticalCap.lean`

Formal theorem shape:

- From `liminf A(x)*sqrt(log x/x) > 0`, derive explicit `C`, `N` with `a_n <= C*n^2*log(2*n)` for `n>=N`.
- From an eventual cap, derive a positive lower bound along `x=a_n` (or a controlled interval) for the normalized counting function.

Avoid handwaving in inversion of logarithms. Use explicit monotonicity lemmas and constants.

## Module 3 — finite Abel/telescope

Suggested files:
- `Erdos1191/AbelFinite.lean`
- `Erdos1191/CutRenewal.lean`

Formalize:
- finite summation by parts;
- exact coefficient arrays;
- all boundary terms;
- `sum Y = R_4 - R_terminal + sum Z` for finite dyadic horizon.

Acceptance test: instantiate small `m` and compute exact rational coefficients.

## Module 4 — triangular floor

Suggested file: `Erdos1191/TriangularFloor.lean`

Formalize:
- distinct positive adjacent gaps imply interval length lower bound;
- exact lower and interior coefficient sums;
- explicit constants replacing `O(1)`;
- nonnegative decomposition used in Wave 11.

## Module 5 — Wave 13 harmonic obstruction

Suggested file: `Erdos1191/HarmonicObstruction.lean`

Formalize:
1. cross-ratio inequality `log(1+uv/(MD)) >= uv/D^2` for positive reals;
2. suffix index set has `m+1` gaps;
3. layered distinct-gap bound `E_m`;
4. polynomial identity and lower bound `E_m >= m^4/48` for dyadic `m>=4`;
5. `Z_m^nb >= E_m/(8m^2H_m) >= m^2/(384H_m)`;
6. critical-cap consequence `Z_m,Y_m >= 1/(1536 C log(4m))` eventually;
7. harmonic dyadic sum is `Omega_C(log J)`;
8. universal P17 and P18 equivalence with Q1.

## Module 6 — Optional Wave 14/15

Do not begin until Modules 1–5 pass.

Wave 14:
- rank promotion counts;
- legal lower-shell rebate;
- exact ownership scope.

Wave 15:
- only after independent prose audit;
- formalize the nested load bound and literal bulk capacity;
- keep the missing disjoint-premium and terminal-horizon statements explicitly open.

## Red-team obligations

For every theorem:
- mutate one index endpoint and verify the theorem/test fails;
- test smallest legal dyadic `m`;
- separate integer and real hypotheses;
- verify all uses of positivity;
- verify no `Nat` subtraction silently truncates a negative quantity;
- confirm `log` base and domain;
- confirm eventual quantifiers are in the correct order (`forall C`, branch, `exists N`, `forall n>=N`).

## Completion definition

The kernel is complete when Modules 1–5 build with no sorry, their axiom reports are acceptable, and the natural-language claim registry references exact Lean theorem names. This formalizes the reduction and obstruction only; it does not solve Q1.
