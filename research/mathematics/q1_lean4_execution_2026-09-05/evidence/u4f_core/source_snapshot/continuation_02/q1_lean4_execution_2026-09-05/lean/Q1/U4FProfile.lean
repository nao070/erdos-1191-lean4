import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic

/-!
Finite algebra used by the U4-F attack of 2026-09-09.
These lemmas do not define or prove CoreUniform or Q1. A record set and its
nonnegative physical weights are explicit inputs. The actual strict-core
enumeration and the Sidon dispersion bound are not yet formalized here.
-/

namespace Erdos1191Q1.U4FProfile

open Finset

variable {ι : Type*}

/-- One record retains its one weight throughout its open interval of cuts. -/
noncomputable def profile (R : Finset ι) (v : ι → ℝ) (c i : ι → ℕ) (b : ℕ) : ℝ :=
  ∑ h ∈ R, if c h < b ∧ b < i h then v h else 0

theorem profile_nonneg (R : Finset ι) (v : ι → ℝ) (c i : ι → ℕ)
    (hv : ∀ h ∈ R, 0 ≤ v h) (b : ℕ) : 0 ≤ profile R v c i b := by
  unfold profile
  exact Finset.sum_nonneg fun h hh ↦ by split_ifs <;> simp_all

theorem profile_mono (R S : Finset ι) (v : ι → ℝ) (c i : ι → ℕ)
    (hRS : R ⊆ S) (hv : ∀ h ∈ S, 0 ≤ v h) (b : ℕ) :
    profile R v c i b ≤ profile S v c i b := by
  unfold profile
  exact Finset.sum_le_sum_of_subset_of_nonneg hRS fun h hh _ ↦ by
    split_ifs <;> simp_all

/-- The cut set is also allowed to grow when the output horizon grows. -/
theorem sqrt_profile_mono (R S : Finset ι) (B D : Finset ℕ)
    (v : ι → ℝ) (c i : ι → ℕ) (hRS : R ⊆ S) (hBD : B ⊆ D)
    (hv : ∀ h ∈ S, 0 ≤ v h) :
    (∑ b ∈ B, Real.sqrt (profile R v c i b) / (b : ℝ)) ≤
      ∑ b ∈ D, Real.sqrt (profile S v c i b) / (b : ℝ) := by
  calc
    _ ≤ ∑ b ∈ B, Real.sqrt (profile S v c i b) / (b : ℝ) := by
      apply Finset.sum_le_sum
      intro b _
      exact div_le_div_of_nonneg_right
        (Real.sqrt_le_sqrt (profile_mono R S v c i hRS hv b)) (by positivity)
    _ ≤ _ := Finset.sum_le_sum_of_subset_of_nonneg hBD fun b _ _ ↦ by positivity

/-- Exact coverage with the same physical records on both sides. -/
theorem coverage_identity (R : Finset ι) (B : Finset ℕ)
    (v : ι → ℝ) (c i : ι → ℕ) :
    (∑ b ∈ B, profile R v c i b / (b : ℝ)) =
      ∑ h ∈ R, v h * ∑ b ∈ B, if c h < b ∧ b < i h then 1 / (b : ℝ) else 0 := by
  unfold profile
  simp_rw [Finset.sum_div]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro h _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro b _
  split_ifs <;> simp [div_eq_mul_inv]

/-- Weighted Cauchy; no assertion about summing this bound over all blocks. -/
theorem weighted_sqrt_bound (B : Finset ι) (p w : ι → ℝ)
    (hp : ∀ b, 0 ≤ p b) (hw : ∀ b, 0 ≤ w b) :
    (∑ b ∈ B, w b * Real.sqrt (p b)) ≤
      Real.sqrt ((∑ b ∈ B, w b) * (∑ b ∈ B, w b * p b)) := by
  have h := Real.sum_sqrt_mul_sqrt_le B hw (fun b ↦ mul_nonneg (hw b) (hp b))
  calc
    _ = ∑ b ∈ B, Real.sqrt (w b) * Real.sqrt (w b * p b) := by
      apply Finset.sum_congr rfl
      intro b _
      rw [Real.sqrt_mul (hw b), ← mul_assoc, Real.mul_self_sqrt (hw b)]
    _ ≤ Real.sqrt (∑ b ∈ B, w b) * Real.sqrt (∑ b ∈ B, w b * p b) := h
    _ = _ := (Real.sqrt_mul (Finset.sum_nonneg fun b _ ↦ hw b) _).symm

/-- The exact dispersion identity before any Sidon packing estimate. -/
theorem variance_deficit (B : Finset ι) (x : ι → ℝ) (H : ℝ) :
    (B.card : ℝ) * (∑ j ∈ B, x j ^ 2) - (∑ j ∈ B, x j) ^ 2 =
      (B.card : ℝ) ^ 2 * H ^ 2 / 4 -
        (B.card : ℝ) * (∑ j ∈ B, x j * (H - x j)) -
        ((∑ j ∈ B, x j) - (B.card : ℝ) * H / 2) ^ 2 := by
  have hs : (∑ j ∈ B, x j * (H - x j)) =
      H * (∑ j ∈ B, x j) - ∑ j ∈ B, x j ^ 2 := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [hs]
  ring

/-- A pair separated by t contributes the exact t^2 energy loss. -/
theorem edge_defect (e t : ℝ) :
    e ^ 2 + (e + t) ^ 2 - 2 * (e * (e + t)) = t ^ 2 := by ring

/-- Numerical Abel coefficient bound; no terminal price is reset. -/
theorem alpha_telescope_bound (r : ℝ) (hr : 1 < r) :
    1 / (r ^ 2 * (r - 1) ^ 2) ≤ ((r - 1)⁻¹ ^ 3 - r⁻¹ ^ 3) / 3 := by
  have h0 : 0 < r := by linarith
  have h1 : 0 < r - 1 := by linarith
  apply (sub_nonneg.mp ?_)
  have heq : ((r - 1)⁻¹ ^ 3 - r⁻¹ ^ 3) / 3 - 1 / (r ^ 2 * (r - 1) ^ 2) =
      1 / (3 * r ^ 3 * (r - 1) ^ 3) := by
    field_simp
    ring
  rw [heq]
  positivity

/-- A common genuine tail increment need not improve an orientation residual. -/
theorem orientation_defect_increment (e tPlus tMinus uPlus uMinus z : ℝ) :
    e * (tPlus * (uPlus + z) - tMinus * (uMinus + z)) -
      e * (tPlus * uPlus - tMinus * uMinus) = e * (tPlus - tMinus) * z := by
  ring

/-- Eliminating the common source and older label yields a repeated triple. -/
theorem paired_orientation_repeated_collision
    (aC aJPlus aJMinus aI aRPlus aRMinus e : ℤ)
    (hplus : aC - aJPlus - e = aRPlus - aI)
    (hminus : e - (aC - aJMinus) = aRMinus - aI) :
    aJMinus + 2 * aI = aJPlus + aRPlus + aRMinus := by
  omega

/-- Exact arithmetic of the M=24 to M=25 witness; endpoint/core checks are external. -/
theorem orientation_component_flip :
    let k23 : ℝ := 1 / (23^2 * 22^2) - 1 / (24^2 * 23^2)
    let k24 : ℝ := 1 / (24^2 * 23^2) - 1 / (25^2 * 24^2)
    let k25 : ℝ := 1 / (25^2 * 24^2) - 1 / (26^2 * 25^2)
    107 * (113 * (k24 / 774^2) - 69 * k23 / 661^2) < 0 ∧
      0 < 107 * (113 * (k24 / 774^2 + k25 / 821^2) - 69 * k23 / 661^2) := by
  norm_num

end Erdos1191Q1.U4FProfile
