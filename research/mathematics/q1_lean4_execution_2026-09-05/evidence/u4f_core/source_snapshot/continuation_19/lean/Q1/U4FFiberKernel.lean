import Mathlib.Tactic
namespace Erdos1191Q1.U4FFiberKernel
noncomputable def kernel (L J t : ℝ) : ℝ :=
  (max ((L+J)^2-t^2) 0 + max ((L-J)^2-t^2) 0) / 4

theorem interlaced (A B C : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B) (hC : 0 ≤ C) :
    kernel (A+B) (B+C) (A+C) = B*(A+B+C) := by
  have h1 : 0 ≤ (A+B+(B+C))^2-(A+C)^2 := by
    nlinarith [mul_nonneg hA hB, mul_nonneg hB hC, sq_nonneg B]
  have h2 : (A+B-(B+C))^2-(A+C)^2 ≤ 0 := by
    nlinarith [mul_nonneg hA hC]
  unfold kernel
  rw [max_eq_left h1, max_eq_right h2]
  ring

theorem nested (A B C : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B) (hC : 0 ≤ C) :
    kernel (A+B+C) B |C-A| = B*(A+B+C)+2*A*C := by
  have h1 : 0 ≤ (A+B+C+B)^2-(C-A)^2 := by
    nlinarith [mul_nonneg hA hB, mul_nonneg hB hC, mul_nonneg hA hC, sq_nonneg B]
  have h2 : 0 ≤ (A+B+C-B)^2-(C-A)^2 := by
    nlinarith [mul_nonneg hA hC]
  unfold kernel
  simp only [sq_abs]
  rw [max_eq_left h1, max_eq_left h2]
  ring

theorem separated (A B C : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B) (hC : 0 ≤ C) :
    kernel A C (A+2*B+C) = 0 := by
  have h1 : (A+C)^2-(A+2*B+C)^2 ≤ 0 := by
    nlinarith [mul_nonneg hA hB, mul_nonneg hB hC, sq_nonneg B]
  have h2 : (A-C)^2-(A+2*B+C)^2 ≤ 0 := by
    nlinarith [mul_nonneg hA hB, mul_nonneg hB hC, mul_nonneg hA hC, sq_nonneg B]
  unfold kernel
  rw [max_eq_right h1, max_eq_right h2]
  norm_num
end Erdos1191Q1.U4FFiberKernel
