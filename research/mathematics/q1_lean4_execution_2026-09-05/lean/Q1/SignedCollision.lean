import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Algebraic engine for signed multiset collisions

This module proves the centered-variance bound and the algebraic Born/retirement
comparison, including finite sums and signed-energy arithmetic. The divisor is an
arbitrary positive real parameter. Its interpretation as an automorphism count,
the actual Sidon multiset partition, and the signed convolution expansion are not
formalized here. In particular, this module does not prove original Q1.
-/

namespace Erdos1191Q1.SignedCollision

open scoped BigOperators

/-- Three centered coordinates, the last maximal, have variance at most six times its square. -/
theorem centered_variance_le (X Y c : ℝ) (hX : X ≤ c) (hY : Y ≤ c)
    (hcenter : X + Y = -c) : X ^ 2 + Y ^ 2 + c ^ 2 ≤ 6 * c ^ 2 := by
  have hprod := mul_nonneg (sub_nonneg.mpr hX) (sub_nonneg.mpr hY)
  have hsq : (X + Y) ^ 2 = c ^ 2 := by rw [hcenter]; ring
  nlinarith

/-- The algebraic full Born formula, with a separate positive-divisor hypothesis in theorems. -/
noncomputable def born (varianceU c divisor : ℝ) : ℝ :=
  (4 * varianceU + 12 * c ^ 2) / divisor

/-- The algebraic retirement formula; this definition alone carries no combinatorial meaning. -/
noncomputable def retired (varianceU varianceV c divisor : ℝ) : ℝ :=
  (2 * varianceU + 6 * varianceV - 12 * c ^ 2) / divisor

/-- The full Born formula is nonnegative for a nonnegative variance and positive divisor. -/
theorem born_nonneg (varianceU c divisor : ℝ) (hU : 0 ≤ varianceU)
    (hdivisor : 0 < divisor) : 0 ≤ born varianceU c divisor := by
  unfold born
  exact div_nonneg (by nlinarith [sq_nonneg c]) hdivisor.le

/-- The exact collision total after the common divisor is applied. -/
theorem born_add_retired (varianceU varianceV c divisor : ℝ) :
    born varianceU c divisor + retired varianceU varianceV c divisor =
      6 * (varianceU + varianceV) / divisor := by
  unfold born retired
  ring

/-- An exact expression for the gap in the collision comparison. -/
theorem twice_born_sub_retired (varianceU varianceV c divisor : ℝ) :
    2 * born varianceU c divisor - retired varianceU varianceV c divisor =
      6 * (varianceU + 6 * c ^ 2 - varianceV) / divisor := by
  unfold born retired
  ring

/-- The variance upper bound proves retirement domination without a repeated-endpoint error. -/
theorem retired_le_twice_born (varianceU varianceV c divisor : ℝ)
    (hU : 0 ≤ varianceU) (hV : varianceV ≤ 6 * c ^ 2) (hdivisor : 0 < divisor) :
    retired varianceU varianceV c divisor ≤ 2 * born varianceU c divisor := by
  have hgap : 0 ≤ 2 * born varianceU c divisor -
      retired varianceU varianceV c divisor := by
    rw [twice_born_sub_retired]
    exact div_nonneg (by linarith) hdivisor.le
  linarith

/-- The comparison follows directly from the three centered coordinates of the later triple. -/
theorem retired_le_twice_born_of_centered (varianceU X Y c divisor : ℝ)
    (hU : 0 ≤ varianceU) (hX : X ≤ c) (hY : Y ≤ c) (hcenter : X + Y = -c)
    (hdivisor : 0 < divisor) :
    retired varianceU (X ^ 2 + Y ^ 2 + c ^ 2) c divisor ≤
      2 * born varianceU c divisor :=
  retired_le_twice_born _ _ _ _ hU (centered_variance_le X Y c hX hY hcenter) hdivisor

/-- An assumed finite collision partition and nonnegative Born remainder imply a stage bound. -/
theorem retired_le_twice_born_of_partition {ι : Type*} (s : Finset ι)
    (B R : ι → ℝ) (totalB totalR remainder : ℝ)
    (hB : totalB = (∑ i ∈ s, B i) + remainder) (hR : totalR = ∑ i ∈ s, R i)
    (hremainder : 0 ≤ remainder) (hlocal : ∀ i ∈ s, R i ≤ 2 * B i) :
    totalR ≤ 2 * totalB := by
  have hsum : (∑ i ∈ s, R i) ≤ 2 * ∑ i ∈ s, B i := by
    calc
      _ ≤ ∑ i ∈ s, 2 * B i := Finset.sum_le_sum hlocal
      _ = _ := (Finset.mul_sum s B 2).symm
  linarith

/-- Nonnegative prices preserve the finite comparison; their clock interpretation is external. -/
theorem weighted_retired_le_twice_born {ι : Type*} (s : Finset ι)
    (w B R : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hstage : ∀ i ∈ s, R i ≤ 2 * B i) :
    (∑ i ∈ s, w i * R i) ≤ 2 * ∑ i ∈ s, w i * B i := by
  calc
    _ ≤ ∑ i ∈ s, 2 * (w i * B i) := by
      apply Finset.sum_le_sum
      intro i hi
      nlinarith [mul_le_mul_of_nonneg_left (hstage i hi) (hw i hi)]
    _ = _ := (Finset.mul_sum s (fun i ↦ w i * B i) 2).symm

/-- The exact signed-energy identity is a hypothesis, not an inferred Sidon partition. -/
theorem energy_le_diagonal_add_six_born (E D B R : ℝ)
    (henergy : E = D + 2 * B + 2 * R) (hretired : R ≤ 2 * B) :
    E ≤ D + 6 * B := by
  linarith

/-- The resulting one-sixth lower bound for the full Born term. -/
theorem energy_gap_div_six_le_born (E D B R : ℝ)
    (henergy : E = D + 2 * B + 2 * R) (hretired : R ≤ 2 * B) :
    (E - D) / 6 ≤ B := by
  linarith [energy_le_diagonal_add_six_born E D B R henergy hretired]

/-- Subtracting consecutive signed diagonals produces the coefficient j, not j minus one. -/
theorem signed_diagonal_increment (j previousVariance newVariance : ℝ) :
    j * (previousVariance + newVariance) - (j - 1) * previousVariance =
      previousVariance + j * newVariance := by
  ring

/-- A finite weighted energy-increment bound assuming the exact increment at each index. -/
theorem weighted_energy_gap_div_six_le_born {ι : Type*} (s : Finset ι)
    (w E D B R : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i)
    (henergy : ∀ i ∈ s, E i = D i + 2 * B i + 2 * R i)
    (hretired : ∀ i ∈ s, R i ≤ 2 * B i) :
    ((∑ i ∈ s, w i * E i) - ∑ i ∈ s, w i * D i) / 6 ≤
      ∑ i ∈ s, w i * B i := by
  have hsum : (∑ i ∈ s, w i * E i) ≤
      (∑ i ∈ s, w i * D i) + 6 * ∑ i ∈ s, w i * B i := by
    calc
      _ ≤ ∑ i ∈ s, (w i * D i + 6 * (w i * B i)) := by
        apply Finset.sum_le_sum
        intro i hi
        have h := mul_le_mul_of_nonneg_left
          (energy_le_diagonal_add_six_born _ _ _ _ (henergy i hi) (hretired i hi))
          (hw i hi)
        nlinarith
      _ = _ := by rw [Finset.sum_add_distrib, ← Finset.mul_sum]
  linarith

/-- Exact rational simplification of the maximal normalized signed diagonal. -/
theorem canonical_diagonal_ratio (j H : ℝ) (hj : j ≠ 0) (hj1 : j - 1 ≠ 0)
    (hH : H ≠ 0) :
    ((j - 1) * (3 * j - 2) * H ^ 2) / ((j * (j - 1)) ^ 2 * H ^ 2) =
      2 / j ^ 2 + 1 / (j * (j - 1)) := by
  field_simp
  ring

/-- A pointwise diagonal bound with the normalization supplied as an algebraic denominator. -/
theorem normalized_signed_diagonal_le (j H previousVariance newVariance : ℝ)
    (hj : 2 ≤ j) (hH : 0 < H)
    (hprevious : previousVariance ≤ (j - 1) * (j - 2) * H ^ 2)
    (hnew : newVariance ≤ 2 * (j - 1) * H ^ 2) :
    (previousVariance + j * newVariance) / ((j * (j - 1)) ^ 2 * H ^ 2) ≤
      2 / j ^ 2 + 1 / (j * (j - 1)) := by
  have hj0 : 0 ≤ j := by linarith
  have hnum : previousVariance + j * newVariance ≤
      (j - 1) * (3 * j - 2) * H ^ 2 := by
    nlinarith [mul_le_mul_of_nonneg_left hnew hj0]
  have hden : 0 ≤ (j * (j - 1)) ^ 2 * H ^ 2 := by positivity
  calc
    _ ≤ ((j - 1) * (3 * j - 2) * H ^ 2) / ((j * (j - 1)) ^ 2 * H ^ 2) :=
      div_le_div_of_nonneg_right hnum hden
    _ = _ := canonical_diagonal_ratio j H (by linarith) (by linarith) hH.ne'

end Erdos1191Q1.SignedCollision
