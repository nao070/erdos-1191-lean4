/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Erdos1191.Sidon
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Gap vectors and contiguous sums

For the zero-based enumeration `a`, gap `r` is `a (r+1) - a r`.  Gaps live in
`Int`, even though `a` is natural-valued, so no truncated subtraction occurs.
-/

open scoped BigOperators

namespace Erdos1191

/-- The `r`-th adjacent gap of a natural-valued enumeration, represented in `Int`. -/
def adjacentGap (a : ℕ → ℕ) (r : ℕ) : ℤ := (a (r + 1) : ℤ) - a r

/-- Exact telescope: gaps with indices `i, ..., j-1` sum to `a j - a i`. -/
theorem sum_adjacentGap_Ico (a : ℕ → ℕ) {i j : ℕ} (hij : i ≤ j) :
    (∑ r ∈ Finset.Ico i j, adjacentGap a r) = (a j : ℤ) - a i := by
  induction j with
  | zero =>
      have hi : i = 0 := Nat.eq_zero_of_le_zero hij
      subst i
      simp
  | succ j ih =>
      by_cases h : i ≤ j
      · rw [Finset.sum_Ico_succ_top h, ih h]
        simp [adjacentGap]
      · have hi : i = j + 1 := by omega
        subst i
        simp

/-- All nonempty contiguous gap sums through endpoint `N` are unique. -/
def ContiguousGapSumsUniqueUpTo (a : ℕ → ℕ) (N : ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄, i < j → j ≤ N → k < l → l ≤ N →
    (∑ r ∈ Finset.Ico i j, adjacentGap a r) =
      (∑ r ∈ Finset.Ico k l, adjacentGap a r) →
    i = k ∧ j = l

/-- A finite ruler is Golomb exactly when its nonempty contiguous gap sums are unique. -/
theorem positiveDifferenceUniqueUpTo_iff_contiguousGapSumsUniqueUpTo
    (a : ℕ → ℕ) (N : ℕ) :
    PositiveDifferenceUniqueUpTo a N ↔ ContiguousGapSumsUniqueUpTo a N := by
  constructor
  · intro hDiff i j k l hij hjN hkl hlN hsum
    rw [sum_adjacentGap_Ico a (Nat.le_of_lt hij),
      sum_adjacentGap_Ico a (Nat.le_of_lt hkl)] at hsum
    exact hDiff hij hjN hkl hlN hsum
  · intro hGap i j k l hij hjN hkl hlN hdiff
    apply hGap hij hjN hkl hlN
    simpa [sum_adjacentGap_Ico a (Nat.le_of_lt hij),
      sum_adjacentGap_Ico a (Nat.le_of_lt hkl)]

/-- For an increasing prefix, additive Sidon sums are equivalent to unique contiguous gap sums. -/
theorem additiveSidonUpTo_iff_contiguousGapSumsUniqueUpTo {a : ℕ → ℕ}
    (ha : StrictMono a) (N : ℕ) :
    AdditiveSidonUpTo a N ↔ ContiguousGapSumsUniqueUpTo a N :=
  (additiveSidonUpTo_iff_positiveDifferenceUniqueUpTo ha N).trans
    (positiveDifferenceUniqueUpTo_iff_contiguousGapSumsUniqueUpTo a N)

/-- Direct natural-sum version of the finite Sidon/contiguous-gap equivalence. -/
theorem additiveSidonNatUpTo_iff_contiguousGapSumsUniqueUpTo {a : ℕ → ℕ}
    (ha : StrictMono a) (N : ℕ) :
    AdditiveSidonNatUpTo a N ↔ ContiguousGapSumsUniqueUpTo a N :=
  (additiveSidonNatUpTo_iff_additiveSidonUpTo a N).trans
    (additiveSidonUpTo_iff_contiguousGapSumsUniqueUpTo ha N)

/-- Every adjacent gap of a strictly increasing natural enumeration is positive. -/
theorem adjacentGap_pos {a : ℕ → ℕ} (ha : StrictMono a) (i : ℕ) :
    0 < adjacentGap a i := by
  have hNat : a i < a (i + 1) := ha (by omega)
  have hInt : (a i : ℤ) < a (i + 1) := by exact_mod_cast hNat
  simp only [adjacentGap]
  omega

/-- Under the finite Golomb property, adjacent gaps before `N` are pairwise distinct. -/
theorem adjacentGap_injectiveUpTo {a : ℕ → ℕ} {N i k : ℕ}
    (hGolomb : PositiveDifferenceUniqueUpTo a N)
    (hiN : i + 1 ≤ N) (hkN : k + 1 ≤ N)
    (hgap : adjacentGap a i = adjacentGap a k) : i = k := by
  have hpairs := hGolomb (Nat.lt_succ_self i) hiN (Nat.lt_succ_self k) hkN (by
    simpa [adjacentGap, Nat.succ_eq_add_one] using hgap)
  exact hpairs.1

/-- Combined L1 endpoint: adjacent gaps are positive integers and equality forces equal indices. -/
theorem adjacentGaps_positive_and_distinct {a : ℕ → ℕ} (ha : StrictMono a)
    {N i k : ℕ} (hGolomb : PositiveDifferenceUniqueUpTo a N)
    (hiN : i + 1 ≤ N) (hkN : k + 1 ≤ N) :
    0 < adjacentGap a i ∧ 0 < adjacentGap a k ∧
      (adjacentGap a i = adjacentGap a k → i = k) := by
  exact ⟨adjacentGap_pos ha i, adjacentGap_pos ha k,
    adjacentGap_injectiveUpTo hGolomb hiN hkN⟩

/--
Endpoint red-team: replacing the two strict nonempty-interval hypotheses by
weak inequalities makes the uniqueness claim false as soon as indices `0,1`
exist.  The two empty intervals have the same sum but different endpoints.
-/
theorem emptyInterval_endpointMutation_is_false (a : ℕ → ℕ) {N : ℕ} (hN : 1 ≤ N) :
    ¬(∀ ⦃i j k l : ℕ⦄, i ≤ j → j ≤ N → k ≤ l → l ≤ N →
      (∑ r ∈ Finset.Ico i j, adjacentGap a r) =
        (∑ r ∈ Finset.Ico k l, adjacentGap a r) →
      i = k ∧ j = l) := by
  intro hMutated
  have hcollision := hMutated (i := 0) (j := 0) (k := 1) (l := 1)
    (by omega) (by omega) (by omega) hN (by simp)
  omega

end Erdos1191
