/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Order

/-!
# Sidon sums and positive differences

The values are natural numbers, while differences are taken in `Int`.  This is
intentional: it rules out silent truncation by natural-number subtraction.
Indices are zero-based natural numbers.
-/

namespace Erdos1191

/-- Unique unordered two-term sums, stated directly in the natural numbers. -/
def AdditiveSidonNat (a : ℕ → ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄,
    a i + a j = a k + a l →
      (i = k ∧ j = l) ∨ (i = l ∧ j = k)

/-- Unique unordered two-term sums for an enumerated natural-number set. -/
def AdditiveSidon (a : ℕ → ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄,
    (a i : ℤ) + a j = (a k : ℤ) + a l →
      (i = k ∧ j = l) ∨ (i = l ∧ j = k)

/-- Every nonzero positive difference has a unique ordered pair of endpoints. -/
def PositiveDifferenceUnique (a : ℕ → ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄, i < j → k < l →
    (a j : ℤ) - a i = (a l : ℤ) - a k → i = k ∧ j = l

/-- The finite-prefix version of `AdditiveSidon`; all four indices are at most `N`. -/
def AdditiveSidonNatUpTo (a : ℕ → ℕ) (N : ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄, i ≤ N → j ≤ N → k ≤ N → l ≤ N →
    a i + a j = a k + a l →
      (i = k ∧ j = l) ∨ (i = l ∧ j = k)

/-- The finite-prefix version with the sum equality cast to `Int`. -/
def AdditiveSidonUpTo (a : ℕ → ℕ) (N : ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄, i ≤ N → j ≤ N → k ≤ N → l ≤ N →
    (a i : ℤ) + a j = (a k : ℤ) + a l →
      (i = k ∧ j = l) ∨ (i = l ∧ j = k)

/-- The finite-prefix positive-difference (Golomb-ruler) property. -/
def PositiveDifferenceUniqueUpTo (a : ℕ → ℕ) (N : ℕ) : Prop :=
  ∀ ⦃i j k l : ℕ⦄, i < j → j ≤ N → k < l → l ≤ N →
    (a j : ℤ) - a i = (a l : ℤ) - a k → i = k ∧ j = l

/-- Casting the sum equation to `Int` does not change the additive Sidon property. -/
theorem additiveSidonNat_iff_additiveSidon (a : ℕ → ℕ) :
    AdditiveSidonNat a ↔ AdditiveSidon a := by
  constructor
  · intro hNat i j k l hsum
    apply hNat
    exact_mod_cast hsum
  · intro hInt i j k l hsum
    apply hInt
    exact_mod_cast hsum

/-- Finite-prefix natural sums and integer-cast sums define the same property. -/
theorem additiveSidonNatUpTo_iff_additiveSidonUpTo (a : ℕ → ℕ) (N : ℕ) :
    AdditiveSidonNatUpTo a N ↔ AdditiveSidonUpTo a N := by
  constructor
  · intro hNat i j k l hiN hjN hkN hlN hsum
    apply hNat hiN hjN hkN hlN
    exact_mod_cast hsum
  · intro hInt i j k l hiN hjN hkN hlN hsum
    apply hInt hiN hjN hkN hlN
    exact_mod_cast hsum

private theorem index_lt_of_value_lt {a : ℕ → ℕ} (ha : StrictMono a)
    {i j : ℕ} (h : a i < a j) : i < j := by
  by_contra hnot
  have hji : j ≤ i := Nat.le_of_not_gt hnot
  have hval : a j ≤ a i := ha.monotone hji
  omega

/--
For a strictly increasing natural enumeration, unique unordered sums are
equivalent to uniqueness of nonzero positive differences.
-/
theorem additiveSidon_iff_positiveDifferenceUnique {a : ℕ → ℕ} (ha : StrictMono a) :
    AdditiveSidon a ↔ PositiveDifferenceUnique a := by
  constructor
  · intro hSidon i j k l hij hkl hdiff
    have hsum : (a j : ℤ) + a k = (a l : ℤ) + a i := by omega
    rcases hSidon hsum with hsame | hcross
    · exact ⟨hsame.2.symm, hsame.1⟩
    · exfalso
      exact (Nat.ne_of_lt hij) hcross.1.symm
  · intro hDiff i j k l hsum
    rcases lt_trichotomy i k with hik | hik | hki
    · have haik : a i < a k := ha hik
      have haikZ : (a i : ℤ) < a k := by exact_mod_cast haik
      have haljZ : (a l : ℤ) < a j := by omega
      have halj : a l < a j := by exact_mod_cast haljZ
      have hlj : l < j := index_lt_of_value_lt ha halj
      have hdiff : (a k : ℤ) - a i = (a j : ℤ) - a l := by omega
      have hpairs := hDiff hik hlj hdiff
      exact Or.inr ⟨hpairs.1, hpairs.2.symm⟩
    · subst k
      have hcast : (a j : ℤ) = a l := by omega
      have hnat : a j = a l := by exact_mod_cast hcast
      exact Or.inl ⟨rfl, ha.injective hnat⟩
    · have haki : a k < a i := ha hki
      have hakiZ : (a k : ℤ) < a i := by exact_mod_cast haki
      have hajlZ : (a j : ℤ) < a l := by omega
      have hajl : a j < a l := by exact_mod_cast hajlZ
      have hjl : j < l := index_lt_of_value_lt ha hajl
      have hdiff : (a i : ℤ) - a k = (a l : ℤ) - a j := by omega
      have hpairs := hDiff hki hjl hdiff
      exact Or.inr ⟨hpairs.2, hpairs.1.symm⟩

/-- Direct natural-sum formulation of the Sidon/positive-difference equivalence. -/
theorem additiveSidonNat_iff_positiveDifferenceUnique {a : ℕ → ℕ} (ha : StrictMono a) :
    AdditiveSidonNat a ↔ PositiveDifferenceUnique a :=
  (additiveSidonNat_iff_additiveSidon a).trans
    (additiveSidon_iff_positiveDifferenceUnique ha)

/-- Finite-prefix version of `additiveSidon_iff_positiveDifferenceUnique`. -/
theorem additiveSidonUpTo_iff_positiveDifferenceUniqueUpTo {a : ℕ → ℕ}
    (ha : StrictMono a) (N : ℕ) :
    AdditiveSidonUpTo a N ↔ PositiveDifferenceUniqueUpTo a N := by
  constructor
  · intro hSidon i j k l hij hjN hkl hlN hdiff
    have hiN : i ≤ N := (Nat.le_of_lt hij).trans hjN
    have hkN : k ≤ N := (Nat.le_of_lt hkl).trans hlN
    have hsum : (a j : ℤ) + a k = (a l : ℤ) + a i := by omega
    rcases hSidon hjN hkN hlN hiN hsum with hsame | hcross
    · exact ⟨hsame.2.symm, hsame.1⟩
    · exfalso
      exact (Nat.ne_of_lt hij) hcross.1.symm
  · intro hDiff i j k l hiN hjN hkN hlN hsum
    rcases lt_trichotomy i k with hik | hik | hki
    · have haik : a i < a k := ha hik
      have haikZ : (a i : ℤ) < a k := by exact_mod_cast haik
      have haljZ : (a l : ℤ) < a j := by omega
      have halj : a l < a j := by exact_mod_cast haljZ
      have hlj : l < j := index_lt_of_value_lt ha halj
      have hdiff : (a k : ℤ) - a i = (a j : ℤ) - a l := by omega
      have hpairs := hDiff hik hkN hlj hjN hdiff
      exact Or.inr ⟨hpairs.1, hpairs.2.symm⟩
    · subst k
      have hcast : (a j : ℤ) = a l := by omega
      have hnat : a j = a l := by exact_mod_cast hcast
      exact Or.inl ⟨rfl, ha.injective hnat⟩
    · have haki : a k < a i := ha hki
      have hakiZ : (a k : ℤ) < a i := by exact_mod_cast haki
      have hajlZ : (a j : ℤ) < a l := by omega
      have hajl : a j < a l := by exact_mod_cast hajlZ
      have hjl : j < l := index_lt_of_value_lt ha hajl
      have hdiff : (a i : ℤ) - a k = (a l : ℤ) - a j := by omega
      have hpairs := hDiff hki hiN hjl hlN hdiff
      exact Or.inr ⟨hpairs.2, hpairs.1.symm⟩

end Erdos1191
