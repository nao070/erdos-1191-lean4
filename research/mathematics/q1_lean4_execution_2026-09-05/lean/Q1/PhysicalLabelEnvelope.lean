import Q1.SharedDifferenceBudget

/-!
# One envelope charge for each physical difference label

This module proves finite max-over-shell capacity bounds. All old label vectors may
vary with the prefix; their contributions at one numeric label are summed before
taking the maximum over possible spending shells. No uniform gap, asymptotic bound,
or conclusion of Q1 is assumed or proved.
-/

namespace Erdos1191Q1

open scoped BigOperators

/-- The literal maximum over a finite shell family; the empty-family value is zero. -/
noncomputable def physicalEnvelope {ι : Type*} (J : Finset ι)
    (G : ι → ℕ → ℝ) (t : ℕ) : ℝ :=
  if h : J.Nonempty then J.sup' h (fun j ↦ G j t) else 0

theorem le_physicalEnvelope {ι : Type*} (J : Finset ι) (G : ι → ℕ → ℝ)
    {j : ι} (hj : j ∈ J) (t : ℕ) : G j t ≤ physicalEnvelope J G t := by
  simp only [physicalEnvelope, dif_pos (show J.Nonempty from ⟨j, hj⟩)]
  exact Finset.le_sup' (fun j ↦ G j t) hj

theorem physicalEnvelope_nonneg {ι : Type*} (J : Finset ι) (G : ι → ℕ → ℝ)
    (hG : ∀ j ∈ J, ∀ t, 0 ≤ G j t) (t : ℕ) : 0 ≤ physicalEnvelope J G t := by
  by_cases hJ : J.Nonempty
  · obtain ⟨j, hj⟩ := hJ
    exact (hG j hj t).trans (le_physicalEnvelope J G hj t)
  · simp [physicalEnvelope, hJ]

theorem physicalEnvelope_eq_zero_of_notMem {ι : Type*} (J : Finset ι)
    (G : ι → ℕ → ℝ) (T : Finset ℕ)
    (hT : ∀ j ∈ J, ∀ t ∉ T, G j t = 0) {t : ℕ} (ht : t ∉ T) :
    physicalEnvelope J G t = 0 := by
  unfold physicalEnvelope
  split_ifs with hJ
  · exact Finset.sup'_eq_of_forall hJ _ (fun j hj ↦ hT j hj t ht)
  · rfl

/-- Pairwise disjoint physical-label sets can spend at most one envelope value per label.
The sets need not lie in `T`: all kernels vanish outside that finite support. -/
theorem disjoint_label_envelope_budget {ι : Type*} (J : Finset ι)
    (D : ι → Finset ℕ) (G : ι → ℕ → ℝ) (T : Finset ℕ)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (D i) (D j))
    (hG : ∀ j ∈ J, ∀ t, 0 ≤ G j t)
    (hT : ∀ j ∈ J, ∀ t ∉ T, G j t = 0) :
    (∑ j ∈ J, ∑ t ∈ D j, G j t) ≤ ∑ t ∈ T, physicalEnvelope J G t := by
  classical
  have hrestrict (j : ι) (hj : j ∈ J) :
      (∑ t ∈ D j, G j t) = ∑ t ∈ D j ∩ T, G j t := by
    symm
    apply Finset.sum_subset Finset.inter_subset_left
    intro t ht hnot
    exact hT j hj t (fun htT ↦ hnot (Finset.mem_inter.mpr ⟨ht, htT⟩))
  have hd : Set.PairwiseDisjoint (J : Set ι) (fun j ↦ D j ∩ T) := by
    intro i hi j hj hij
    exact (hdisj i hi j hj hij).mono Finset.inter_subset_left Finset.inter_subset_left
  calc
    (∑ j ∈ J, ∑ t ∈ D j, G j t) = ∑ j ∈ J, ∑ t ∈ D j ∩ T, G j t :=
      Finset.sum_congr rfl hrestrict
    _ ≤ ∑ j ∈ J, ∑ t ∈ D j ∩ T, physicalEnvelope J G t := by
      apply Finset.sum_le_sum
      intro j hj
      exact Finset.sum_le_sum (fun t _ ↦ le_physicalEnvelope J G hj t)
    _ = ∑ t ∈ J.biUnion (fun j ↦ D j ∩ T), physicalEnvelope J G t :=
      (Finset.sum_biUnion hd).symm
    _ ≤ ∑ t ∈ T, physicalEnvelope J G t := by
      apply Finset.sum_le_sum_of_subset_of_nonneg
      · intro t ht
        obtain ⟨j, _, htj⟩ := Finset.mem_biUnion.mp ht
        exact (Finset.mem_inter.mp htj).2
      · exact fun t _ _ ↦ physicalEnvelope_nonneg J G hG t

/-- A finite family of local demands obeys the same one-copy physical-label budget. -/
theorem disjoint_label_demand_envelope {ι : Type*} (J : Finset ι)
    (D : ι → Finset ℕ) (G : ι → ℕ → ℝ) (T : Finset ℕ) (δ : ι → ℝ)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (D i) (D j))
    (hG : ∀ j ∈ J, ∀ t, 0 ≤ G j t)
    (hT : ∀ j ∈ J, ∀ t ∉ T, G j t = 0)
    (hδ : ∀ j ∈ J, δ j ≤ ∑ t ∈ D j, G j t) :
    (∑ j ∈ J, δ j) ≤ ∑ t ∈ T, physicalEnvelope J G t :=
  (Finset.sum_le_sum hδ).trans (disjoint_label_envelope_budget J D G T hdisj hG hT)

/-- General demand-to-envelope bridge, using difference injectivity in one actual Sidon set. -/
theorem actual_blocks_envelope_budget {ι : Type*} {A : Set ℕ} (hA : Sidon A)
    (J : Finset ι) (B : ι → Finset ℕ) (G : ι → ℕ → ℝ) (T : Finset ℕ) (δ : ι → ℝ)
    (hB : ∀ j ∈ J, ∀ b ∈ B j, b ∈ A)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (B i) (B j))
    (hG : ∀ j ∈ J, ∀ t, 0 ≤ G j t)
    (hT : ∀ j ∈ J, ∀ t ∉ T, G j t = 0)
    (hδ : ∀ j ∈ J, δ j ≤ ∑ t ∈ internalLabels (B j), G j t) :
    (∑ j ∈ J, δ j) ≤ ∑ t ∈ T, physicalEnvelope J G t := by
  apply (Finset.sum_le_sum hδ).trans
  apply disjoint_label_envelope_budget J (fun j ↦ internalLabels (B j)) G T
  · intro i hi j hj hij
    exact internalLabels_disjoint hA (B i) (B j) (hB i hi) (hB j hj) (hdisj i hi j hj hij)
  · exact hG
  · exact hT

/-- The half positive-part demand in equation (25); all division is in the reals. -/
noncomputable def intervalLabelDemand (B F : Finset ℕ) (u : ℕ → ℝ) (L H : ℕ) : ℝ :=
  max 0 ((((B.card : ℝ) * ∑ d ∈ F, u d) ^ 2 / ((L : ℝ) + H - B.card)) -
    (B.card : ℝ) * ∑ d ∈ F, u d ^ 2) / 2

theorem intervalCapacity_pos (B : Finset ℕ) (n L H : ℕ) (hL : 0 < L) (hH : 0 < H)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1)) : (0 : ℝ) < (L : ℝ) + H - B.card := by
  have hc := Finset.card_le_card hBounds
  rw [Nat.card_Icc] at hc
  have hcard : B.card ≤ L := by omega
  have hcardR : (B.card : ℝ) ≤ L := by exact_mod_cast hcard
  have hHR : (0 : ℝ) < H := by exact_mod_cast hH
  linarith

/-- A local interval demand is paid by its actual internal difference labels. -/
theorem intervalLabelDemand_le {A : Set ℕ} (hA : Sidon A)
    (P B F : Finset ℕ) (u : ℕ → ℝ) (n L H : ℕ) (hL : 0 < L) (hH : 0 < H)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hu : ∀ d ∈ F, 0 ≤ u d) (hF : F ⊆ internalLabels P)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1)) (hFH : F ⊆ Finset.Icc 1 H) :
    intervalLabelDemand B F u L H ≤ labelExpenditure F u B := by
  have hden := intervalCapacity_pos B n L H hL hH hBounds
  have hc := shadow_interval_capacity hA P B F u n L H hL hP hB hPB hF hBounds hFH
  have hquot : ((B.card : ℝ) * ∑ d ∈ F, u d) ^ 2 / ((L : ℝ) + H - B.card) ≤
      (B.card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u B :=
    (div_le_iff₀ hden).mpr (hc.trans_eq (mul_comm _ _))
  have hpsi : 0 ≤ labelExpenditure F u B :=
    Finset.sum_nonneg (fun t _ ↦ labelKernel_nonneg F u hu t)
  unfold intervalLabelDemand
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 2)).mpr
  apply max_le <;> linarith

/-- Positive internal labels of an interval block lie in its exact span bound. -/
theorem internalLabels_mem_interval (B : Finset ℕ) (n L : ℕ) (hL : 0 < L)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1)) {t : ℕ} (ht : t ∈ internalLabels B) :
    1 ≤ t ∧ t ≤ L - 1 := by
  obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp ht
  obtain ⟨h₁, h₂, hlt⟩ := (mem_internalPairs B p).mp hp
  have hb₁ := Finset.mem_Icc.mp (hBounds h₁)
  have hb₂ := Finset.mem_Icc.mp (hBounds h₂)
  dsimp [differenceLabel]
  omega

/-- The two literal masks and the sum of all selected prefix contributions eligible at shell `j`.
The finite index set `I` selects old vectors; eligibility is the integer inequality `k ≤ j`. -/
noncomputable def maskedEpochKernel (I : Finset ℕ) (P F : ℕ → Finset ℕ)
    (u α : ℕ → ℕ → ℝ) (L : ℕ → ℕ) (j t : ℕ) : ℝ :=
  if 1 ≤ t ∧ t ≤ L j - 1 ∧ t ∉ internalLabels (P j) then
    ∑ k ∈ I.filter (fun k ↦ k ≤ j), α k j * labelKernel (F k) (u k) t
  else 0

/-- A finite support containing every relation label of every selected old vector. -/
def epochLabelSupport (I : Finset ℕ) (F : ℕ → Finset ℕ) : Finset ℕ :=
  I.biUnion (fun k ↦ internalLabels (F k))

theorem maskedEpochKernel_nonneg (I : Finset ℕ) (P F : ℕ → Finset ℕ)
    (u α : ℕ → ℕ → ℝ) (L : ℕ → ℕ) (j : ℕ)
    (hu : ∀ k ∈ I, ∀ d ∈ F k, 0 ≤ u k d)
    (hα : ∀ k ∈ I, k ≤ j → 0 ≤ α k j) (t : ℕ) :
    0 ≤ maskedEpochKernel I P F u α L j t := by
  unfold maskedEpochKernel
  split_ifs
  · apply Finset.sum_nonneg
    intro k hk
    obtain ⟨hkI, hkj⟩ := Finset.mem_filter.mp hk
    exact mul_nonneg (hα k hkI hkj) (labelKernel_nonneg (F k) (u k) (hu k hkI) t)
  · rfl

theorem maskedEpochKernel_supported (I : Finset ℕ) (P F : ℕ → Finset ℕ)
    (u α : ℕ → ℕ → ℝ) (L : ℕ → ℕ) (j t : ℕ)
    (ht : t ∉ epochLabelSupport I F) : maskedEpochKernel I P F u α L j t = 0 := by
  unfold maskedEpochKernel
  split_ifs
  · apply Finset.sum_eq_zero
    intro k hk
    have hkI := (Finset.mem_filter.mp hk).1
    have htF : t ∉ internalLabels (F k) := by
      intro htF
      exact ht (Finset.mem_biUnion.mpr ⟨k, hkI, htF⟩)
    rw [labelKernel_eq_zero_of_notMem (F k) (u k) t htF, mul_zero]
  · rfl

/-- Both masks equal one on an actual internal label of the future shell. -/
theorem maskedEpochKernel_eq_on_actual_labels {A : Set ℕ} (hA : Sidon A)
    (I : Finset ℕ) (P F : ℕ → Finset ℕ) (u α : ℕ → ℕ → ℝ) (L : ℕ → ℕ)
    (j : ℕ) (B : Finset ℕ) (n : ℕ) (hL : 0 < L j)
    (hP : ∀ p ∈ P j, p ∈ A) (hB : ∀ b ∈ B, b ∈ A)
    (hPB : Disjoint (P j) B) (hBounds : B ⊆ Finset.Icc n (n + L j - 1))
    {t : ℕ} (ht : t ∈ internalLabels B) :
    maskedEpochKernel I P F u α L j t =
      ∑ k ∈ I.filter (fun k ↦ k ≤ j), α k j * labelKernel (F k) (u k) t := by
  have hspan := internalLabels_mem_interval B n (L j) hL hBounds ht
  have hd := internalLabels_disjoint hA (P j) B hP hB hPB
  have hnot : t ∉ internalLabels (P j) := fun hp ↦ Finset.disjoint_left.mp hd hp ht
  exact if_pos ⟨hspan.1, hspan.2, hnot⟩

/-- Each shell pays all its eligible, nonnegatively weighted old-prefix demands simultaneously. -/
theorem weighted_interval_demand_le_epoch {A : Set ℕ} (hA : Sidon A)
    (I : Finset ℕ) (P F : ℕ → Finset ℕ) (u α : ℕ → ℕ → ℝ) (L H : ℕ → ℕ)
    (j : ℕ) (B : Finset ℕ) (n : ℕ) (hL : 0 < L j)
    (hH : ∀ k ∈ I, 0 < H k) (hP : ∀ k ∈ I, ∀ p ∈ P k, p ∈ A)
    (hPj : ∀ p ∈ P j, p ∈ A) (hB : ∀ b ∈ B, b ∈ A)
    (hPB : ∀ k ∈ I, k ≤ j → Disjoint (P k) B) (hPjB : Disjoint (P j) B)
    (hu : ∀ k ∈ I, ∀ d ∈ F k, 0 ≤ u k d)
    (hα : ∀ k ∈ I, k ≤ j → 0 ≤ α k j)
    (hF : ∀ k ∈ I, F k ⊆ internalLabels (P k))
    (hFH : ∀ k ∈ I, F k ⊆ Finset.Icc 1 (H k))
    (hBounds : B ⊆ Finset.Icc n (n + L j - 1)) :
    (∑ k ∈ I.filter (fun k ↦ k ≤ j),
      α k j * intervalLabelDemand B (F k) (u k) (L j) (H k)) ≤
        ∑ t ∈ internalLabels B, maskedEpochKernel I P F u α L j t := by
  calc
    (∑ k ∈ I.filter (fun k ↦ k ≤ j),
      α k j * intervalLabelDemand B (F k) (u k) (L j) (H k)) ≤
        ∑ k ∈ I.filter (fun k ↦ k ≤ j), α k j * labelExpenditure (F k) (u k) B := by
      apply Finset.sum_le_sum
      intro k hk
      obtain ⟨hkI, hkj⟩ := Finset.mem_filter.mp hk
      exact mul_le_mul_of_nonneg_left
        (intervalLabelDemand_le hA (P k) B (F k) (u k) n (L j) (H k) hL (hH k hkI)
          (hP k hkI) hB (hPB k hkI hkj) (hu k hkI) (hF k hkI) hBounds (hFH k hkI))
        (hα k hkI hkj)
    _ = ∑ t ∈ internalLabels B, ∑ k ∈ I.filter (fun k ↦ k ≤ j),
        α k j * labelKernel (F k) (u k) t := by
      simp only [labelExpenditure, Finset.mul_sum]
      rw [Finset.sum_comm]
    _ = ∑ t ∈ internalLabels B, maskedEpochKernel I P F u α L j t := by
      apply Finset.sum_congr rfl
      intro t ht
      exact (maskedEpochKernel_eq_on_actual_labels hA I P F u α L j B n hL
        hPj hB hPjB hBounds ht).symm

/-- Equation (27), including both inequalities and the literal masks of (26).

All selected `P k` and `B j` belong to the same Sidon set. The old/future disjointness
is required for exactly the eligible pairs and for each shell's own masking prefix.
Nestedness and dyadic cardinalities are unnecessary for this finite inequality;
actual growing prefixes satisfy the displayed conditions. `H k` bounds every label
in `F k`, including zero-weight labels. No positivity of the total weight is needed.
-/
theorem growing_prefix_interval_envelope {A : Set ℕ} (hA : Sidon A)
    (I J : Finset ℕ) (P B F : ℕ → Finset ℕ) (u α : ℕ → ℕ → ℝ)
    (n L H : ℕ → ℕ)
    (hP : ∀ k ∈ I ∪ J, ∀ p ∈ P k, p ∈ A)
    (hB : ∀ j ∈ J, ∀ b ∈ B j, b ∈ A)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (B i) (B j))
    (hPB : ∀ j ∈ J, ∀ k ∈ insert j I, k ≤ j → Disjoint (P k) (B j))
    (hu : ∀ k ∈ I, ∀ d ∈ F k, 0 ≤ u k d)
    (hα : ∀ j ∈ J, ∀ k ∈ I, k ≤ j → 0 ≤ α k j)
    (hF : ∀ k ∈ I, F k ⊆ internalLabels (P k))
    (hFH : ∀ k ∈ I, F k ⊆ Finset.Icc 1 (H k)) (hH : ∀ k ∈ I, 0 < H k)
    (hL : ∀ j ∈ J, 0 < L j)
    (hBounds : ∀ j ∈ J, B j ⊆ Finset.Icc (n j) (n j + L j - 1)) :
    ((∑ j ∈ J, ∑ k ∈ I.filter (fun k ↦ k ≤ j),
      α k j * intervalLabelDemand (B j) (F k) (u k) (L j) (H k)) ≤
        ∑ j ∈ J, ∑ t ∈ internalLabels (B j), maskedEpochKernel I P F u α L j t) ∧
    ((∑ j ∈ J, ∑ t ∈ internalLabels (B j), maskedEpochKernel I P F u α L j t) ≤
      ∑ t ∈ epochLabelSupport I F, physicalEnvelope J (maskedEpochKernel I P F u α L) t) := by
  constructor
  · apply Finset.sum_le_sum
    intro j hj
    apply weighted_interval_demand_le_epoch hA I P F u α L H j (B j) (n j) (hL j hj) hH
    · exact fun k hk ↦ hP k (Finset.mem_union_left J hk)
    · exact hP j (Finset.mem_union_right I hj)
    · exact hB j hj
    · exact fun k hk hkj ↦ hPB j hj k (Finset.mem_insert_of_mem hk) hkj
    · exact hPB j hj j (Finset.mem_insert_self j I) le_rfl
    · exact hu
    · exact hα j hj
    · exact hF
    · exact hFH
    · exact hBounds j hj
  · apply disjoint_label_envelope_budget J (fun j ↦ internalLabels (B j))
      (maskedEpochKernel I P F u α L) (epochLabelSupport I F)
    · intro i hi j hj hij
      exact internalLabels_disjoint hA (B i) (B j) (hB i hi) (hB j hj) (hdisj i hi j hj hij)
    · exact fun j hj ↦ maskedEpochKernel_nonneg I P F u α L j hu (hα j hj)
    · exact fun j _ t ht ↦ maskedEpochKernel_supported I P F u α L j t ht

/-- Exact finite partition into selected-label spending, other used labels, unused labels,
and envelope slack. The identity is algebraic and does not discard any nonnegative term. -/
theorem label_envelope_accounting {ι : Type*} (J : Finset ι)
    (D : ι → Finset ℕ) (G : ι → ℕ → ℝ) (T V : Finset ℕ)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (D i) (D j))
    (hV : ∀ j ∈ J, D j ⊆ V) :
    (∑ t ∈ T, physicalEnvelope J G t) =
      (∑ j ∈ J, ∑ t ∈ D j ∩ T, G j t) +
      (∑ t ∈ (T ∩ V) \ J.biUnion D, physicalEnvelope J G t) +
      (∑ t ∈ T \ V, physicalEnvelope J G t) +
      (∑ j ∈ J, ∑ t ∈ D j ∩ T, (physicalEnvelope J G t - G j t)) := by
  classical
  have hd : Set.PairwiseDisjoint (J : Set ι) (fun j ↦ D j ∩ T) := by
    intro i hi j hj hij
    exact (hdisj i hi j hj hij).mono Finset.inter_subset_left Finset.inter_subset_left
  have hselected : (T ∩ V) ∩ J.biUnion D = J.biUnion (fun j ↦ D j ∩ T) := by
    ext t
    simp only [Finset.mem_inter, Finset.mem_biUnion]
    constructor
    · rintro ⟨⟨htT, _⟩, j, hj, htD⟩
      exact ⟨j, hj, htD, htT⟩
    · rintro ⟨j, hj, htD, htT⟩
      exact ⟨⟨htT, hV j hj htD⟩, j, hj, htD⟩
  have hinner := Finset.sum_inter_add_sum_sdiff (T ∩ V) (J.biUnion D) (physicalEnvelope J G)
  rw [hselected, Finset.sum_biUnion hd] at hinner
  have houter := Finset.sum_inter_add_sum_sdiff T V (physicalEnvelope J G)
  have hslack :
      (∑ j ∈ J, ∑ t ∈ D j ∩ T, (physicalEnvelope J G t - G j t)) =
      (∑ j ∈ J, ∑ t ∈ D j ∩ T, physicalEnvelope J G t) -
        (∑ j ∈ J, ∑ t ∈ D j ∩ T, G j t) := by
    simp only [Finset.sum_sub_distrib]
  linarith

theorem physicalEnvelope_slack_nonneg {ι : Type*} (J : Finset ι)
    (D : ι → Finset ℕ) (G : ι → ℕ → ℝ) (T : Finset ℕ) :
    0 ≤ ∑ j ∈ J, ∑ t ∈ D j ∩ T, (physicalEnvelope J G t - G j t) := by
  apply Finset.sum_nonneg
  intro j hj
  exact Finset.sum_nonneg (fun t _ ↦ sub_nonneg.mpr (le_physicalEnvelope J G hj t))

/-- The accounting identity for actual shells within a finite terminal Sidon history `W`.
The second sum includes all used labels outside selected shells (old and cross labels);
the third includes labels unused by `W`. All three source sums are restricted to finite `T`. -/
theorem actual_blocks_envelope_accounting {ι : Type*} {A : Set ℕ} (hA : Sidon A)
    (J : Finset ι) (B : ι → Finset ℕ) (G : ι → ℕ → ℝ) (T W : Finset ℕ)
    (hW : ∀ w ∈ W, w ∈ A) (hB : ∀ j ∈ J, B j ⊆ W)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (B i) (B j)) :
    (∑ t ∈ T, physicalEnvelope J G t) =
      (∑ j ∈ J, ∑ t ∈ internalLabels (B j) ∩ T, G j t) +
      (∑ t ∈ (T ∩ internalLabels W) \ J.biUnion (fun j ↦ internalLabels (B j)),
        physicalEnvelope J G t) +
      (∑ t ∈ T \ internalLabels W, physicalEnvelope J G t) +
      (∑ j ∈ J, ∑ t ∈ internalLabels (B j) ∩ T, (physicalEnvelope J G t - G j t)) := by
  apply label_envelope_accounting
  · intro i hi j hj hij
    exact internalLabels_disjoint hA (B i) (B j) (fun b hb ↦ hW b (hB i hi hb))
      (fun b hb ↦ hW b (hB j hj hb)) (hdisj i hi j hj hij)
  · intro j hj t ht
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp ht
    obtain ⟨h₁, h₂, hlt⟩ := (mem_internalPairs (B j) p).mp hp
    exact Finset.mem_image.mpr ⟨p, (mem_internalPairs W p).mpr
      ⟨hB j hj h₁, hB j hj h₂, hlt⟩, rfl⟩

end Erdos1191Q1
