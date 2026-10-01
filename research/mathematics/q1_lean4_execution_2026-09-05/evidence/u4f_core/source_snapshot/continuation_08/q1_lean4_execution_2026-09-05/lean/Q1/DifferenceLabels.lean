import Q1.Target
import Mathlib.Data.Finset.Prod
import Mathlib.Tactic

/-!
# Actual positive difference labels of a Sidon set

The unordered-sum definition from the frozen target is equivalent to uniqueness of every
positive difference. The differences below are natural-number differences; strict ordering
of each endpoint pair ensures that no truncated negative difference is used.

The finite cardinality inequalities retain the actual labels of actual endpoint pairs.
They neither impose a density assumption nor resolve the logarithmic Q1 challenge.
-/

namespace Erdos1191Q1

open scoped BigOperators

/-- Every positive difference determines its ordered pair of endpoints in `A`. -/
def PositiveDifferenceUnique (A : Set ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A, ∀ d ∈ A,
    a < b → c < d → b - a = d - c → a = c ∧ b = d

/-- The exact sum/difference equivalence, including repeated summands in the sum condition. -/
theorem sidon_iff_positiveDifferenceUnique (A : Set ℕ) :
    Sidon A ↔ PositiveDifferenceUnique A := by
  constructor
  · intro h a ha b hb c hc d hd hab hcd hdiff
    have hsum : b + c = d + a := by omega
    rcases h b hb c hc d hd a ha hsum with hsame | hcross
    · exact ⟨hsame.2.symm, hsame.1⟩
    · omega
  · intro h a ha b hb c hc d hd hsum
    rcases lt_trichotomy a c with hac | hac | hca
    · have hdb : d < b := by omega
      have hdiff : c - a = b - d := by omega
      obtain ⟨had, hcb⟩ := h a ha c hc d hd b hb hac hdb hdiff
      exact Or.inr ⟨had, hcb.symm⟩
    · exact Or.inl ⟨hac, by omega⟩
    · have hbd : b < d := by omega
      have hdiff : a - c = d - b := by omega
      obtain ⟨hcb, had⟩ := h c hc a ha b hb d hd hca hbd hdiff
      exact Or.inr ⟨had, hcb.symm⟩

/-- An ordered positive pair of actual elements of the input set. -/
def IsPositivePair (A : Set ℕ) (p : ℕ × ℕ) : Prop :=
  p.1 ∈ A ∧ p.2 ∈ A ∧ p.1 < p.2

/-- The actual positive-difference label; the positivity premise belongs to the pair. -/
def differenceLabel (p : ℕ × ℕ) : ℕ := p.2 - p.1

/-- Sidonicity gives injection of labels on all actual positive endpoint pairs. -/
theorem differenceLabel_injOn {A : Set ℕ} (hA : Sidon A) :
    Set.InjOn differenceLabel {p | IsPositivePair A p} := by
  intro p hp q hq heq
  obtain ⟨hpA, hpB, hpLt⟩ := hp
  obtain ⟨hqA, hqB, hqLt⟩ := hq
  obtain ⟨hfst, hsnd⟩ := (sidon_iff_positiveDifferenceUnique A).mp hA
    p.1 hpA p.2 hpB q.1 hqA q.2 hqB hpLt hqLt heq
  exact Prod.ext hfst hsnd

/-- Any finite collection of actual positive pairs has at most as many pairs as allowed labels. -/
theorem positivePairs_card_le_labels {A : Set ℕ} (hA : Sidon A)
    (P : Finset (ℕ × ℕ)) (L : Finset ℕ)
    (hP : ∀ p ∈ P, IsPositivePair A p) (hL : ∀ p ∈ P, differenceLabel p ∈ L) :
    P.card ≤ L.card := by
  apply Finset.card_le_card_of_injOn differenceLabel
  · exact hL
  · exact (differenceLabel_injOn hA).mono hP

/-- Counting distinct actual labels loses no information about a finite family of pairs. -/
theorem positivePairs_image_card_eq {A : Set ℕ} (hA : Sidon A)
    (P : Finset (ℕ × ℕ)) (hP : ∀ p ∈ P, IsPositivePair A p) :
    (P.image differenceLabel).card = P.card :=
  Finset.card_image_of_injOn ((differenceLabel_injOn hA).mono hP)

/-- Nonnegative weights on actual difference labels give every corresponding linear constraint. -/
theorem weighted_positivePairs_le_labels {A : Set ℕ} (hA : Sidon A)
    (P : Finset (ℕ × ℕ)) (L : Finset ℕ) (w : ℕ → ℝ)
    (hP : ∀ p ∈ P, IsPositivePair A p) (hL : ∀ p ∈ P, differenceLabel p ∈ L)
    (hw : ∀ d ∈ L, 0 ≤ w d) :
    (∑ p ∈ P, w (differenceLabel p)) ≤ ∑ d ∈ L, w d := by
  have hinj := (differenceLabel_injOn hA).mono hP
  calc
    _ = ∑ d ∈ P.image differenceLabel, w d := (Finset.sum_image hinj).symm
    _ ≤ ∑ d ∈ L, w d := by
      apply Finset.sum_le_sum_of_subset_of_nonneg
      · intro d hd
        obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
        exact hL p hp
      · intro d hd _
        exact hw d hd

/-- Selecting any subset of actual labels preserves their unit-capacity cardinal bound. -/
theorem selectedLabels_card_le {A : Set ℕ} (hA : Sidon A)
    (P : Finset (ℕ × ℕ)) (L : Finset ℕ) (hP : ∀ p ∈ P, IsPositivePair A p) :
    (P.filter (fun p ↦ differenceLabel p ∈ L)).card ≤ L.card := by
  apply positivePairs_card_le_labels hA
  · intro p hp
    exact hP p (Finset.mem_filter.mp hp).1
  · intro p hp
    exact (Finset.mem_filter.mp hp).2

/-- Each specific positive-difference label is used by at most one actual endpoint pair. -/
theorem differenceLabel_fiber_card_le_one {A : Set ℕ} (hA : Sidon A)
    (P : Finset (ℕ × ℕ)) (d : ℕ) (hP : ∀ p ∈ P, IsPositivePair A p) :
    (P.filter (fun p ↦ differenceLabel p = d)).card ≤ 1 := by
  simpa only [Finset.mem_singleton, Finset.card_singleton] using
    selectedLabels_card_le hA P {d} hP

/-- Ordered distinct endpoint pairs from the positive prefix counted in the frozen target. -/
noncomputable def prefixPositivePairs (A : Set ℕ) (H : ℕ) : Finset (ℕ × ℕ) :=
  ((countingSet A H).product (countingSet A H)).filter (fun p ↦ p.1 < p.2)

theorem mem_prefixPositivePairs (A : Set ℕ) (H : ℕ) (p : ℕ × ℕ) :
    p ∈ prefixPositivePairs A H ↔
      p.1 ∈ countingSet A H ∧ p.2 ∈ countingSet A H ∧ p.1 < p.2 := by
  simp only [prefixPositivePairs, Finset.mem_filter, Finset.product_eq_sprod,
    Finset.mem_product, and_assoc]

theorem prefixPositivePairs_are_actual (A : Set ℕ) (H : ℕ) :
    ∀ p ∈ prefixPositivePairs A H, IsPositivePair A p := by
  classical
  intro p hp
  obtain ⟨hfst, hsnd, hlt⟩ := (mem_prefixPositivePairs A H p).mp hp
  exact ⟨(Finset.mem_filter.mp hfst).2, (Finset.mem_filter.mp hsnd).2, hlt⟩

/-- The actual label of a prefix pair belongs to the requested finite codomain `[1,H]`. -/
theorem prefix_differenceLabel_mem_Icc (A : Set ℕ) (H : ℕ)
    (p : ℕ × ℕ) (hp : p ∈ prefixPositivePairs A H) :
    differenceLabel p ∈ Finset.Icc 1 H := by
  classical
  obtain ⟨hfst, hsnd, hlt⟩ := (mem_prefixPositivePairs A H p).mp hp
  have hH : p.2 ≤ H := (Finset.mem_Icc.mp (Finset.mem_filter.mp hsnd).1).2
  simp only [Finset.mem_Icc, differenceLabel]
  omega

/-- A literal map of finite subtypes using the real endpoint difference as its value. -/
noncomputable def prefixDifferenceMap (A : Set ℕ) (H : ℕ) :
    {p // p ∈ prefixPositivePairs A H} → {d // d ∈ Finset.Icc 1 H} :=
  fun p ↦ ⟨differenceLabel p.val, prefix_differenceLabel_mem_Icc A H p.val p.property⟩

theorem prefixDifferenceMap_injective {A : Set ℕ} (hA : Sidon A) (H : ℕ) :
    Function.Injective (prefixDifferenceMap A H) := by
  intro p q heq
  apply Subtype.ext
  apply differenceLabel_injOn hA
  · exact prefixPositivePairs_are_actual A H p.val p.property
  · exact prefixPositivePairs_are_actual A H q.val q.property
  · exact congrArg Subtype.val heq

/-- Every selected actual label set imposes its own cardinality constraint on prefix pairs. -/
theorem prefix_selectedLabels_card_le {A : Set ℕ} (hA : Sidon A) (H : ℕ) (L : Finset ℕ) :
    ((prefixPositivePairs A H).filter (fun p ↦ differenceLabel p ∈ L)).card ≤ L.card :=
  selectedLabels_card_le hA _ L (prefixPositivePairs_are_actual A H)

/-- The elementary finite-prefix bound obtained from the injection into `[1,H]`. -/
theorem prefixPositivePairs_card_le {A : Set ℕ} (hA : Sidon A) (H : ℕ) :
    (prefixPositivePairs A H).card ≤ H := by
  have h := positivePairs_card_le_labels hA (prefixPositivePairs A H) (Finset.Icc 1 H)
    (prefixPositivePairs_are_actual A H) (prefix_differenceLabel_mem_Icc A H)
  simpa using h

end Erdos1191Q1
