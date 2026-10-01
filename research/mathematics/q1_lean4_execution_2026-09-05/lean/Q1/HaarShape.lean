import Q1.DirectMoment

/-!
# Algebra of the three jumps of an interior Haar state

The exact coefficient here is the direct matrix coefficient, not a numerical approximation.
The geometric assertion that an actual translated Haar state has the listed jump patterns
is proved in the accompanying mathematical note; that geometric bridge is not formalized here.
-/

namespace Erdos1191Q1

theorem directGapCoefficient_shift_gap (p a : ℕ) :
    directGapCoefficient p (p + a) = -(a : ℝ) ^ 2 / 2 +
      if a = 1 then (1 : ℝ) / 2 else 0 := by
  rw [directGapCoefficient_eq]
  have h : (p + 1 = p + a ∨ p + a + 1 = p) ↔ a = 1 := by omega
  simp only [h, Nat.cast_add]
  ring

/-- The symmetric quadratic form for jumps `1,-2,1` at `p,p+a,p+a+b`.
This equals `4*e^2*qᵀMq` when those are the nonzero jumps of `Dq`. -/
noncomputable def threeJumpCore (p a b : ℕ) : ℝ :=
  -4 * directGapCoefficient p (p + a) +
    2 * directGapCoefficient p (p + (a + b)) -
    4 * directGapCoefficient (p + a) ((p + a) + b)

theorem threeJumpCore_eq (p a b : ℕ) (ha : 0 < a) (hb : 0 < b) :
    threeJumpCore p a b = ((a : ℝ) - (b : ℝ)) ^ 2 -
      (if a = 1 then 2 else 0) - (if b = 1 then 2 else 0) := by
  have hab : a + b ≠ 1 := by omega
  simp only [threeJumpCore, directGapCoefficient_shift_gap, if_neg hab, Nat.cast_add]
  split_ifs <;> ring

/-- The unscaled numerator of every interior three-jump Haar state is at least -4. -/
theorem threeJumpCore_lower (p a b : ℕ) (ha : 0 < a) (hb : 0 < b) :
    -4 ≤ threeJumpCore p a b := by
  rw [threeJumpCore_eq p a b ha hb]
  split_ifs <;> nlinarith [sq_nonneg ((a : ℝ) - (b : ℝ))]

/-- The path correction contributes 4 to this numerator, since `1²+(-2)²+1²=6`. -/
theorem corrected_threeJumpCore_nonneg (p a b : ℕ) (ha : 0 < a) (hb : 0 < b) :
    0 ≤ threeJumpCore p a b + (2 : ℝ) / 3 * (1 ^ 2 + (-2) ^ 2 + 1 ^ 2) := by
  have h := threeJumpCore_lower p a b ha hb
  norm_num at *
  linarith

theorem directGapCoefficient_nonpos (i j : ℕ) : directGapCoefficient i j ≤ 0 := by
  unfold directGapCoefficient
  split_ifs
  · nlinarith [sq_nonneg ((i : ℝ) - (j : ℝ))]
  · rfl

/-- Every two-jump form with opposite signs has nonnegative direct energy. -/
theorem opposite_two_jump_nonneg (i j : ℕ) (u v : ℝ) (h : u * v ≤ 0) :
    0 ≤ 2 * directGapCoefficient i j * u * v := by
  have hc := directGapCoefficient_nonpos i j
  nlinarith [mul_nonneg_of_nonpos_of_nonpos hc h]

end Erdos1191Q1
