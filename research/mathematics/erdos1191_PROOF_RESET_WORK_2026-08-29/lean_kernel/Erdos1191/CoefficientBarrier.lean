/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Exact finite coefficient barrier for the C118 fixture

This file checks only the frozen rational sign calculation extracted from the
finite C118 certificate. It makes no claim about C058, arbitrary fixtures, or
Erdos Problem #1191.
-/

namespace Erdos1191

/-- The displayed C118 threshold is exactly `(249 / 2000) / DeltaV`. -/
theorem c118CoefficientBarrier_value :
    (249 / 2000 : ℚ) / (3440812085 / 9234857208 : ℚ) =
      287434930599 / 860203021250 := by
  norm_num

/--
For the certified C118 dual upper bound, any master row whose remaining two
terms are nonnegative needs the concentration coefficient to exceed the exact
displayed barrier.
-/
theorem c118NecessaryCoefficientBarrier
    (epsilon shapeCharge coefficient dualUpper : ℚ)
    (epsilon_nonnegative : 0 ≤ epsilon)
    (shapeCharge_nonnegative : 0 ≤ shapeCharge)
    (strict_dual_upper : dualUpper < -(83 / 2000 : ℚ))
    (master_row :
      (epsilon + shapeCharge -
        coefficient * (3440812085 / 9234857208 : ℚ)) / 3 ≤ dualUpper) :
    (287434930599 / 860203021250 : ℚ) < coefficient := by
  norm_num at strict_dual_upper master_row ⊢
  linarith

/-- The coefficient box `coefficient <= 1/3` is incompatible with that row. -/
theorem c118OneThirdCoefficientBoxNoGo
    (epsilon shapeCharge coefficient dualUpper : ℚ)
    (epsilon_nonnegative : 0 ≤ epsilon)
    (shapeCharge_nonnegative : 0 ≤ shapeCharge)
    (coefficient_at_most_one_third : coefficient ≤ 1 / 3)
    (strict_dual_upper : dualUpper < -(83 / 2000 : ℚ))
    (master_row :
      (epsilon + shapeCharge -
        coefficient * (3440812085 / 9234857208 : ℚ)) / 3 ≤ dualUpper) :
    False := by
  have coefficient_barrier :=
    c118NecessaryCoefficientBarrier epsilon shapeCharge coefficient dualUpper
      epsilon_nonnegative shapeCharge_nonnegative strict_dual_upper master_row
  norm_num at coefficient_at_most_one_third coefficient_barrier
  linarith

end Erdos1191
