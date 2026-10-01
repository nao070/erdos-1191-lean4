import Q1.Target
import Mathlib.Tactic

namespace Erdos1191Q1

private theorem power_three_separation {i j : ℕ} (hij : i < j) :
    2 * 3 ^ i < 3 ^ j := by
  have hpow : 3 ^ (i + 1) ≤ 3 ^ j := pow_le_pow_right' (by norm_num) hij
  have hpos : 0 < 3 ^ i := by positivity
  rw [pow_succ] at hpow
  omega

private theorem sorted_power_three_sum {i j k l : ℕ} (hij : i ≤ j) (hkl : k ≤ l)
    (h : 3 ^ i + 3 ^ j = 3 ^ k + 3 ^ l) : i = k ∧ j = l := by
  have hmono : StrictMono (fun n : ℕ ↦ 3 ^ n) := pow_right_strictMono₀ (by norm_num)
  have hjl : j = l := by
    rcases lt_trichotomy j l with hjl | hjl | hlj
    · have hsep := power_three_separation hjl
      have hupper := hmono.monotone hij
      nlinarith [Nat.zero_le (3 ^ k)]
    · exact hjl
    · have hsep := power_three_separation hlj
      have hupper := hmono.monotone hkl
      nlinarith [Nat.zero_le (3 ^ i)]
  subst l
  exact ⟨hmono.injective (by omega), rfl⟩

/-- Powers of three satisfy the challenge's Sidon condition, including equal summands. -/
theorem powers_three_sidon : Sidon (Set.range (fun n : ℕ ↦ 3 ^ n)) := by
  rintro _ ⟨i, rfl⟩ _ ⟨j, rfl⟩ _ ⟨k, rfl⟩ _ ⟨l, rfl⟩ h
  change (3 : ℕ) ^ i + 3 ^ j = 3 ^ k + 3 ^ l at h
  rcases le_total i j with hij | hji <;> rcases le_total k l with hkl | hlk
  · obtain ⟨rfl, rfl⟩ := sorted_power_three_sum hij hkl h
    exact Or.inl ⟨rfl, rfl⟩
  · obtain ⟨rfl, rfl⟩ := sorted_power_three_sum hij hlk (by omega)
    exact Or.inr ⟨rfl, rfl⟩
  · obtain ⟨rfl, rfl⟩ := sorted_power_three_sum hji hkl (by omega)
    exact Or.inr ⟨rfl, rfl⟩
  · obtain ⟨rfl, rfl⟩ := sorted_power_three_sum hji hlk (by omega)
    exact Or.inl ⟨rfl, rfl⟩

/-- The input hypotheses of Q1 are simultaneously inhabited. This does not prove Q1. -/
theorem admissible_exists : ∃ A : Set ℕ, Positive A ∧ A.Infinite ∧ Sidon A := by
  refine ⟨Set.range (fun n : ℕ ↦ 3 ^ n), ?_, ?_, powers_three_sidon⟩
  · rintro a ⟨n, rfl⟩
    exact Nat.one_le_pow n 3 (by norm_num)
  · exact Set.infinite_range_of_injective (pow_right_strictMono₀ (by norm_num : 1 < (3 : ℕ))).injective

end Erdos1191Q1
