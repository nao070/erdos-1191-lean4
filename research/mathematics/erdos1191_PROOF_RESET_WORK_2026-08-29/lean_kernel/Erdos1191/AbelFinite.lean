/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Mathlib.Algebra.BigOperators.Module
import Mathlib.Algebra.Field.Rat

/-!
# Exact finite telescope and Abel summation

These statements contain every endpoint explicitly and make no asymptotic claim.
-/

open scoped BigOperators

namespace Erdos1191

/-- A group-valued finite forward-difference telescope, valid also for `n = 0`. -/
theorem sum_forwardDiff_range {G : Type*} [AddCommGroup G] (x : ℕ → G) (n : ℕ) :
    (∑ i ∈ Finset.range n, (x (i + 1) - x i)) = x n - x 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.sum_range_succ, ih]
      abel

/--
Finite Abel summation over `0, ..., n-1`.  The partial sum multiplying the
coefficient difference at `i` is exactly `sum (range (i+1)) g`.
-/
theorem finiteAbel_range {R : Type*} [CommRing R] (f g : ℕ → R) (n : ℕ) :
    (∑ i ∈ Finset.range n, f i * g i) =
      f (n - 1) * (∑ i ∈ Finset.range n, g i) -
        ∑ i ∈ Finset.range (n - 1),
          (f (i + 1) - f i) * (∑ j ∈ Finset.range (i + 1), g j) := by
  simpa only [smul_eq_mul] using (Finset.sum_range_by_parts f g n)

/--
Exact rational fixture for `finiteAbel_range` at horizon four.  Here
`f i = 2^i` and `g i = 2i+3`: the original sum is `113`, the terminal term is
`192`, and the three repayment coefficients contribute `79`.
-/
theorem finiteAbel_rational_fixture :
    (∑ i ∈ Finset.range 4, (2 : ℚ) ^ i * (2 * i + 3)) = 113 ∧
      (2 : ℚ) ^ 3 * (∑ i ∈ Finset.range 4, (2 * i + 3 : ℚ)) = 192 ∧
      (∑ i ∈ Finset.range 3,
        ((2 : ℚ) ^ (i + 1) - 2 ^ i) *
          (∑ j ∈ Finset.range (i + 1), (2 * j + 3 : ℚ))) = 79 := by
  norm_num [Finset.sum_range_succ, pow_succ]

end Erdos1191
