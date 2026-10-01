import Q1.SignedCollision

/-!
# Absolute-value algebra for signed collisions

This module proves an inequality for six real cross products. Identifying those
products with actual Sidon retirement records remains an external combinatorial
step. No history partition, clock assignment, or original Q1 conclusion is asserted.
-/

namespace Erdos1191Q1.SignedAbsoluteCollision

/-- The six ordered unequal-slot cross products, counted with their absolute values. -/
noncomputable def crossSum (a b p q r : ℝ) : ℝ :=
  |(a - p) * (b - q)| + |(a - p) * (b - r)| + |(a - q) * (b - p)| +
    |(a - q) * (b - r)| + |(a - r) * (b - p)| + |(a - r) * (b - q)|

/-- A single absolute product bound, multiplied by the total to avoid division. -/
theorem cross_abs_mul_le (a b p q r : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hp : 0 ≤ p) (hq : 0 ≤ q) (hr : 0 ≤ r) (hsum : p + q + r = a + b) :
    (a + b) * |(a - p) * (b - q)| ≤
      -(a + b) * ((a - p) * (b - q)) + 2 * a * b * r := by
  have hidentity : (a + b) * ((a - p) * (b - q)) +
      a * q * (a - p) + b * p * (b - q) = a * b * r := by
    have heq : r = a + b - p - q := by linarith
    rw [heq]
    ring
  have habr : 0 ≤ a * b * r := mul_nonneg (mul_nonneg ha hb) hr
  by_cases hleft : 0 ≤ a - p
  · by_cases hright : 0 ≤ b - q
    · rw [abs_of_nonneg (mul_nonneg hleft hright)]
      have hfirst := mul_nonneg (mul_nonneg ha hq) hleft
      have hsecond := mul_nonneg (mul_nonneg hb hp) hright
      nlinarith
    · have hprod : (a - p) * (b - q) ≤ 0 :=
        mul_nonpos_of_nonneg_of_nonpos hleft (le_of_not_ge hright)
      rw [abs_of_nonpos hprod]
      nlinarith
  · by_cases hright : 0 ≤ b - q
    · have hprod : (a - p) * (b - q) ≤ 0 :=
        mul_nonpos_of_nonpos_of_nonneg (le_of_not_ge hleft) hright
      rw [abs_of_nonpos hprod]
      nlinarith
    · exfalso
      linarith

/-- Summing all six products retains the negative twice-product term. -/
theorem crossSum_le_reduced (a b p q r : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hp : 0 ≤ p) (hq : 0 ≤ q) (hr : 0 ≤ r) (hpositive : 0 < a + b)
    (hsum : p + q + r = a + b) :
    crossSum a b p q r ≤ (a + b) ^ 2 + (p ^ 2 + q ^ 2 + r ^ 2) - 2 * a * b := by
  have h1 := cross_abs_mul_le a b p q r ha hb hp hq hr hsum
  have h2 := cross_abs_mul_le a b p r q ha hb hp hr hq (by linarith)
  have h3 := cross_abs_mul_le a b q p r ha hb hq hp hr (by linarith)
  have h4 := cross_abs_mul_le a b q r p ha hb hq hr hp (by linarith)
  have h5 := cross_abs_mul_le a b r p q ha hb hr hp hq (by linarith)
  have h6 := cross_abs_mul_le a b r q p ha hb hr hq hp (by linarith)
  have hraw : (a - p) * (b - q) + (a - p) * (b - r) + (a - q) * (b - p) +
      (a - q) * (b - r) + (a - r) * (b - p) + (a - r) * (b - q) =
      6 * a * b - (a + b) ^ 2 - (p ^ 2 + q ^ 2 + r ^ 2) := by
    have heq : r = a + b - p - q := by linarith
    rw [heq]
    ring
  have hmul : (a + b) * crossSum a b p q r ≤
      -(a + b) * ((a - p) * (b - q) + (a - p) * (b - r) + (a - q) * (b - p) +
        (a - q) * (b - r) + (a - r) * (b - p) + (a - r) * (b - q)) +
        4 * a * b * (p + q + r) := by
    unfold crossSum
    nlinarith
  rw [hraw, hsum] at hmul
  apply (mul_le_mul_iff_left₀ hpositive).mp
  nlinarith

/-- Cauchy's three-coordinate inequality bounds the six absolute products. -/
theorem crossSum_le_four_squares (a b p q r : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hp : 0 ≤ p) (hq : 0 ≤ q) (hr : 0 ≤ r) (hpositive : 0 < a + b)
    (hsum : p + q + r = a + b) :
    crossSum a b p q r ≤ 4 * (p ^ 2 + q ^ 2 + r ^ 2) := by
  have hc : (a + b) ^ 2 ≤ 3 * (p ^ 2 + q ^ 2 + r ^ 2) := by
    rw [← hsum]
    nlinarith [sq_nonneg (p - q), sq_nonneg (p - r), sq_nonneg (q - r)]
  have hab : 0 ≤ a * b := mul_nonneg ha hb
  linarith [crossSum_le_reduced a b p q r ha hb hp hq hr hpositive hsum]

/-- The algebraic absolute retirement is at most twice its Born expression after division. -/
theorem absolute_retired_le_twice_born (a b p q r divisor : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hp : 0 ≤ p) (hq : 0 ≤ q) (hr : 0 ≤ r)
    (hpositive : 0 < a + b) (hsum : p + q + r = a + b) (hdivisor : 0 < divisor) :
    2 * crossSum a b p q r / divisor ≤
      2 * (4 * (p ^ 2 + q ^ 2 + r ^ 2) / divisor) := by
  have h := crossSum_le_four_squares a b p q r ha hb hp hq hr hpositive hsum
  calc
    _ ≤ (2 * (4 * (p ^ 2 + q ^ 2 + r ^ 2))) / divisor :=
      div_le_div_of_nonneg_right (by linarith) hdivisor.le
    _ = _ := by ring

end Erdos1191Q1.SignedAbsoluteCollision
