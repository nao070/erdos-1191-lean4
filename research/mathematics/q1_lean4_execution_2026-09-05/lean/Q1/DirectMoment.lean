import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Moment compression of the direct quadratic form

This identity applies at arbitrary finite rank, without a fixture or Sidon hypothesis.
It exposes the endpoint moment product that must be retained in a global use of C143.
It is an algebraic identity, not a proof of the global capacity bound or of Q1.
-/

namespace Erdos1191Q1

open scoped BigOperators

/-- The all-pairs squared-distance quadratic form is determined by three moments. -/
theorem distance_quadratic_moments {ι : Type*} (s : Finset ι) (x w : ι → ℝ) :
    (∑ i ∈ s, ∑ j ∈ s, (x i - x j) ^ 2 * w i * w j) =
      2 * (∑ i ∈ s, w i) * (∑ i ∈ s, x i ^ 2 * w i) -
      2 * (∑ i ∈ s, x i * w i) ^ 2 := by
  calc
    _ = ∑ i ∈ s, ∑ j ∈ s,
        ((x i ^ 2 * w i) * w j + w i * (x j ^ 2 * w j) -
          (2 * (x i * w i)) * (x j * w j)) := by
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j hj
      ring
    _ = ∑ i ∈ s,
        ((x i ^ 2 * w i) * (∑ j ∈ s, w j) + w i * (∑ j ∈ s, x j ^ 2 * w j) -
          (2 * (x i * w i)) * (∑ j ∈ s, x j * w j)) := by
      simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum]
    _ = (∑ i ∈ s, x i ^ 2 * w i) * (∑ j ∈ s, w j) +
        (∑ i ∈ s, w i) * (∑ j ∈ s, x j ^ 2 * w j) -
        (2 * (∑ i ∈ s, x i * w i)) * (∑ j ∈ s, x j * w j) := by
      simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib,
        ← Finset.sum_mul, ← Finset.mul_sum]
    _ = _ := by ring

/-- Signed C143 all-pairs core, before the omitted adjacent entries are restored. -/
theorem negative_distance_quadratic_moments {ι : Type*}
    (s : Finset ι) (x w : ι → ℝ) :
    -(∑ i ∈ s, ∑ j ∈ s, (x i - x j) ^ 2 * w i * w j) / 2 =
      (∑ i ∈ s, x i * w i) ^ 2 -
      (∑ i ∈ s, w i) * (∑ i ∈ s, x i ^ 2 * w i) := by
  rw [distance_quadratic_moments]
  ring

/-- A zero zeroth moment removes the signed endpoint product, with no positivity assumption. -/
theorem zero_mass_negative_distance_quadratic {ι : Type*}
    (s : Finset ι) (x w : ι → ℝ) (h : ∑ i ∈ s, w i = 0) :
    -(∑ i ∈ s, ∑ j ∈ s, (x i - x j) ^ 2 * w i * w j) / 2 =
      (∑ i ∈ s, x i * w i) ^ 2 := by
  rw [negative_distance_quadratic_moments, h]
  ring

/-- This is `4 * n^2 * B[i,j]` for C143's actual gap matrix at rank n. -/
noncomputable def directGapCoefficient (i j : ℕ) : ℝ :=
  if i + 1 < j ∨ j + 1 < i then -((i : ℝ) - (j : ℝ)) ^ 2 / 2 else 0

theorem directGapCoefficient_eq (i j : ℕ) :
    directGapCoefficient i j = -((i : ℝ) - (j : ℝ)) ^ 2 / 2 +
      if i + 1 = j ∨ j + 1 = i then (1 : ℝ) / 2 else 0 := by
  by_cases h : i + 1 = j ∨ j + 1 = i
  · have hn : ¬(i + 1 < j ∨ j + 1 < i) := by omega
    rw [directGapCoefficient, if_neg hn, if_pos h]
    rcases h with h | h
    · subst j
      push_cast
      ring
    · subst i
      push_cast
      ring
  · by_cases hl : i + 1 < j ∨ j + 1 < i
    · simp [directGapCoefficient, hl, h]
    · have he : i = j := by omega
      subst j
      simp [directGapCoefficient]

/-- Exact moment decomposition including every omitted adjacent entry of the direct matrix. -/
theorem direct_gap_quadratic_moments (s : Finset ℕ) (w : ℕ → ℝ) :
    (∑ i ∈ s, ∑ j ∈ s, directGapCoefficient i j * w i * w j) =
      (∑ i ∈ s, (i : ℝ) * w i) ^ 2 -
      (∑ i ∈ s, w i) * (∑ i ∈ s, (i : ℝ) ^ 2 * w i) +
      (∑ i ∈ s, ∑ j ∈ s, if i + 1 = j ∨ j + 1 = i then w i * w j else 0) / 2 := by
  have he (i j : ℕ) : directGapCoefficient i j * w i * w j =
      -(((i : ℝ) - (j : ℝ)) ^ 2 * w i * w j) / 2 +
      (if i + 1 = j ∨ j + 1 = i then w i * w j else 0) / 2 := by
    rw [directGapCoefficient_eq]
    split_ifs <;> ring
  simp_rw [he]
  simp only [Finset.sum_add_distrib, ← Finset.sum_div, Finset.sum_neg_distrib]
  rw [negative_distance_quadratic_moments]

/-- `4*n^2` times the actual direct point-matrix form, using its gap-coordinate definition. -/
noncomputable def scaledDirectForm (n : ℕ) (q : ℕ → ℝ) : ℝ :=
  ∑ i ∈ Finset.range n, ∑ j ∈ Finset.range n,
    directGapCoefficient i j * (q i - q (i + 1)) * (q j - q (j + 1))

/-- All endpoint information is retained by the zeroth moment `q 0 - q n`. -/
theorem direct_point_quadratic_moments (n : ℕ) (q : ℕ → ℝ) :
    scaledDirectForm n q =
      (∑ i ∈ Finset.range n, (i : ℝ) * (q i - q (i + 1))) ^ 2 -
      (q 0 - q n) * (∑ i ∈ Finset.range n, (i : ℝ) ^ 2 * (q i - q (i + 1))) +
      (∑ i ∈ Finset.range n, ∑ j ∈ Finset.range n,
        if i + 1 = j ∨ j + 1 = i then
          (q i - q (i + 1)) * (q j - q (j + 1)) else 0) / 2 := by
  rw [scaledDirectForm, direct_gap_quadratic_moments, Finset.sum_range_sub']

/-- The tiny path correction is not positive semidefinite on arbitrary vectors.
The witness is not an actual raw Haar state and hence does not refute Haar-state positivity. -/
theorem path_correction_not_psd_witness :
    scaledDirectForm 3 (fun i ↦ 3 - (i : ℝ)) / (4 * (3 : ℝ) ^ 2) +
      (∑ i ∈ Finset.range 3, ((3 - (i : ℝ)) - (3 - ((i + 1 : ℕ) : ℝ))) ^ 2) /
        (6 * (3 : ℝ) ^ 2) = -(1 : ℝ) / 18 := by
  norm_num [scaledDirectForm, directGapCoefficient, Finset.sum_range_succ]

end Erdos1191Q1
