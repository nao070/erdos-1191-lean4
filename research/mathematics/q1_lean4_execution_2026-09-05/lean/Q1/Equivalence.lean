import Q1.Target
import Mathlib.Tactic

namespace Erdos1191Q1

open Filter

/-- The floor-based count has exactly the intended inclusive real-cutoff membership. -/
theorem mem_countingSet_real (A : Set ℕ) (x : ℝ) (a : ℕ) :
    a ∈ countingSet A ⌊x⌋₊ ↔ a ∈ A ∧ 1 ≤ a ∧ (a : ℝ) ≤ x := by
  classical
  simp only [countingSet, Finset.mem_filter, Finset.mem_Icc]
  constructor
  · rintro ⟨⟨ha, hax⟩, hA⟩
    exact ⟨hA, ha, (Nat.le_floor_iff' (by omega)).mp hax⟩
  · rintro ⟨hA, ha, hax⟩
    exact ⟨⟨ha, (Nat.le_floor_iff' (by omega)).mpr hax⟩, hA⟩

@[simp] theorem realCount_natCast (A : Set ℕ) (N : ℕ) : realCount A N = count A N := by
  simp [realCount]

theorem normalized_nonneg (A : Set ℕ) (x : ℝ) : 0 ≤ normalized A x := by
  exact mul_nonneg (Nat.cast_nonneg _) (Real.sqrt_nonneg _)

/-- The normalization is safely squared only in the range where log(x)/x is nonnegative. -/
theorem normalized_sq (A : Set ℕ) {x : ℝ} (hx : 1 ≤ x) :
    normalized A x ^ 2 = (realCount A x : ℝ) ^ 2 * Real.log x / x := by
  have hq : 0 ≤ Real.log x / x := div_nonneg (Real.log_nonneg hx) (by linarith)
  rw [normalized, mul_pow, Real.sq_sqrt hq, mul_div_assoc]

/-- Exact arbitrary-epsilon interpretation of the extended real lower limit. -/
theorem original_iff_frequently (A : Set ℕ) :
    Original A ↔ ∀ ε : ℝ, 0 < ε → ∃ᶠ x : ℝ in atTop, normalized A x < ε := by
  constructor
  · intro h ε hε
    have hh : liminf (fun x : ℝ ↦ (normalized A x : EReal)) atTop < (ε : EReal) := by
      rw [show liminf (fun x : ℝ ↦ (normalized A x : EReal)) atTop = 0 from h]
      exact_mod_cast hε
    simpa only [EReal.coe_lt_coe_iff] using frequently_lt_of_liminf_lt (h := hh)
  · intro h
    apply le_antisymm
    · apply (liminf_le_iff (by isBoundedDefault) (by isBoundedDefault)).mpr
      intro y hy
      obtain ⟨ε, hε, hεy⟩ := EReal.exists_between_coe_real hy
      have hεpos : 0 < ε := by exact_mod_cast hε
      exact (h ε hεpos).mono fun x hx ↦ (EReal.coe_lt_coe_iff.mpr hx).trans hεy
    · apply le_liminf_of_le (by isBoundedDefault)
      exact Eventually.of_forall fun x ↦ by exact_mod_cast normalized_nonneg A x

/-- Arbitrarily late small values after squaring on the real domain. -/
def RealSquared (A : Set ℕ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∀ B : ℝ, ∃ x : ℝ,
    max B 2 ≤ x ∧ (realCount A x : ℝ) ^ 2 * Real.log x < ε * x

theorem original_iff_realSquared (A : Set ℕ) : Original A ↔ RealSquared A := by
  rw [original_iff_frequently]
  constructor
  · intro h ε hε B
    obtain ⟨x, hx, hsmall⟩ := frequently_atTop.mp (h (Real.sqrt ε) (Real.sqrt_pos.mpr hε))
      (max B 2)
    have hx1 : 1 ≤ x := le_trans (by norm_num) ((le_max_right B 2).trans hx)
    have hxx : 0 < x := by linarith
    have hs : normalized A x ^ 2 < ε := by
      nlinarith [normalized_nonneg A x, Real.sqrt_nonneg ε, Real.sq_sqrt hε.le]
    refine ⟨x, hx, ?_⟩
    rw [normalized_sq A hx1] at hs
    exact (div_lt_iff₀ hxx).mp hs
  · intro h ε hε
    rw [frequently_atTop]
    intro B
    obtain ⟨x, hx, hsmall⟩ := h (ε ^ 2) (sq_pos_of_pos hε) B
    have hx1 : 1 ≤ x := le_trans (by norm_num) ((le_max_right B 2).trans hx)
    have hxx : 0 < x := by linarith
    have hs : normalized A x ^ 2 < ε ^ 2 := by
      rw [normalized_sq A hx1]
      exact (div_lt_iff₀ hxx).mpr hsmall
    exact ⟨x, (le_max_left B 2).trans hx, by nlinarith [normalized_nonneg A x]⟩

/-- Moving a real cutoff down to its floor loses at most a factor of two for x ≥ 2. -/
theorem realSquared_iff_integerSquared (A : Set ℕ) : RealSquared A ↔ IntegerSquared A := by
  constructor
  · intro h ε hε M
    obtain ⟨x, hx, hsmall⟩ := h (ε / 2) (by positivity) ((max M 2 : ℕ) : ℝ)
    have hxM : (max M 2 : ℕ) ≤ ⌊x⌋₊ := Nat.le_floor ((le_max_left _ _).trans hx)
    have hN2 : 2 ≤ ⌊x⌋₊ := (le_max_right M 2).trans hxM
    have hN2r : (2 : ℝ) ≤ ⌊x⌋₊ := by exact_mod_cast hN2
    have hx2 : (2 : ℝ) ≤ x := (le_max_right _ _).trans hx
    have hfloor : (⌊x⌋₊ : ℝ) ≤ x := Nat.floor_le (by linarith)
    have hlog : Real.log (⌊x⌋₊ : ℝ) ≤ Real.log x := Real.log_le_log (by linarith) hfloor
    have htwice : x < 2 * (⌊x⌋₊ : ℝ) := by
      have := Nat.lt_floor_add_one x
      linarith
    refine ⟨⌊x⌋₊, hxM, ?_⟩
    have hprod := mul_le_mul_of_nonneg_left hlog (sq_nonneg (count A ⌊x⌋₊ : ℝ))
    change (count A ⌊x⌋₊ : ℝ) ^ 2 * Real.log x < ε / 2 * x at hsmall
    have hloss : ε / 2 * x < ε * (⌊x⌋₊ : ℝ) := by nlinarith
    exact hprod.trans_lt (hsmall.trans hloss)
  · intro h ε hε B
    obtain ⟨N, hN, hsmall⟩ := h ε hε ⌈B⌉₊
    have hNB : B ≤ (N : ℝ) :=
      (Nat.le_ceil B).trans (by exact_mod_cast (le_max_left ⌈B⌉₊ 2).trans hN)
    have hN2 : (2 : ℝ) ≤ N := by exact_mod_cast (le_max_right ⌈B⌉₊ 2).trans hN
    exact ⟨N, max_le hNB hN2, by simpa only [realCount_natCast] using hsmall⟩

/-- Full bridge between the original real-cutoff liminf and the integer squared condition. -/
theorem original_iff_integerSquared (A : Set ℕ) : Original A ↔ IntegerSquared A :=
  (original_iff_realSquared A).trans (realSquared_iff_integerSquared A)

/-- This is an equivalence of challenge statements, not a proof of either challenge. -/
theorem q1_iff_q1Integer : Q1 ↔ Q1Integer := by
  simp only [Q1, Q1Integer, original_iff_integerSquared]

/-- An eventual positive lower bound, required for a counterexample to Q1. -/
def EventualLowerBound (A : Set ℕ) : Prop :=
  ∃ ε : ℝ, 0 < ε ∧ ∃ M : ℕ, 2 ≤ M ∧ ∀ N : ℕ, M ≤ N →
    ε * N ≤ (count A N : ℝ) ^ 2 * Real.log N

/-- Negating the integer formulation gives precisely an eventual lower bound. -/
theorem not_integerSquared_iff (A : Set ℕ) : ¬IntegerSquared A ↔ EventualLowerBound A := by
  classical
  simp only [IntegerSquared, not_forall, not_exists, not_and, not_lt]
  constructor
  · rintro ⟨ε, hε, M, h⟩
    exact ⟨ε, hε, max M 2, le_max_right M 2, h⟩
  · rintro ⟨ε, hε, M, hM, h⟩
    exact ⟨ε, hε, M, fun N hN ↦ h N ((le_max_left M 2).trans hN)⟩

/-- The real-cutoff negation is exactly the required integer eventual lower bound. -/
theorem not_original_iff (A : Set ℕ) : ¬Original A ↔ EventualLowerBound A := by
  rw [original_iff_integerSquared, not_integerSquared_iff]

/-- A counterexample to Q1 must be an actual positive infinite Sidon set with this bound. -/
theorem not_q1_iff : ¬Q1 ↔ ∃ A : Set ℕ,
    Positive A ∧ A.Infinite ∧ Sidon A ∧ EventualLowerBound A := by
  classical
  simp only [Q1, not_forall, not_original_iff, exists_prop]

end Erdos1191Q1
