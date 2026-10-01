import Q1.DifferenceLabels

/-!
# Shared budget of actual Sidon difference labels

All sums are finite and keep their physical endpoint labels. The kernel counts pairs
of selected labels with multiplicity; the selected label set is not assumed to be Sidon.
These are supporting finite identities and budget bounds, not a resolution of Q1.
-/

namespace Erdos1191Q1

open scoped BigOperators

/-- Strictly increasing ordered pairs of a finite set. -/
def internalPairs (B : Finset ℕ) : Finset (ℕ × ℕ) :=
  (B ×ˢ B).filter (fun p ↦ p.1 < p.2)

@[simp] theorem mem_internalPairs (B : Finset ℕ) (p : ℕ × ℕ) :
    p ∈ internalPairs B ↔ p.1 ∈ B ∧ p.2 ∈ B ∧ p.1 < p.2 := by
  simp [internalPairs, and_assoc]

/-- The actual internal positive difference labels, with endpoint uniqueness proved separately. -/
def internalLabels (B : Finset ℕ) : Finset ℕ := (internalPairs B).image differenceLabel

theorem internalPairs_actual {A : Set ℕ} (B : Finset ℕ) (hB : ∀ b ∈ B, b ∈ A) :
    ∀ p ∈ internalPairs B, IsPositivePair A p := by
  intro p hp
  obtain ⟨h₁, h₂, hlt⟩ := (mem_internalPairs B p).mp hp
  exact ⟨hB _ h₁, hB _ h₂, hlt⟩

/-- Disjoint actual blocks in a single Sidon set have disjoint internal label sets. -/
theorem internalLabels_disjoint {A : Set ℕ} (hA : Sidon A) (B C : Finset ℕ)
    (hB : ∀ b ∈ B, b ∈ A) (hC : ∀ c ∈ C, c ∈ A) (hBC : Disjoint B C) :
    Disjoint (internalLabels B) (internalLabels C) := by
  apply Finset.disjoint_left.mpr
  intro d hdB hdC
  obtain ⟨p, hp, hpd⟩ := Finset.mem_image.mp hdB
  obtain ⟨q, hq, hqd⟩ := Finset.mem_image.mp hdC
  have heq : p = q := differenceLabel_injOn hA (internalPairs_actual B hB p hp)
    (internalPairs_actual C hC q hq) (hpd.trans hqd.symm)
  subst q
  exact Finset.disjoint_left.mp hBC (mem_internalPairs B p |>.mp hp).1
    (mem_internalPairs C p |>.mp hq).1

/-- A symmetric finite matrix splits into its diagonal and twice its strict upper triangle. -/
theorem symmetric_sum_eq_diagonal_add_twice (B : Finset ℕ) (f : ℕ → ℕ → ℝ)
    (hsym : ∀ i j, f i j = f j i) :
    (∑ i ∈ B, ∑ j ∈ B, f i j) =
      (∑ i ∈ B, f i i) + 2 * ∑ p ∈ internalPairs B, f p.1 p.2 := by
  have hsplit (i j : ℕ) : f i j =
      (if i = j then f i i else 0) + (if i < j then f i j else 0) +
        (if j < i then f j i else 0) := by
    rcases lt_trichotomy i j with h | h | h
    · simp [h, h.ne, not_lt_of_ge h.le]
    · subst j
      simp
    · simp [h, h.ne', not_lt_of_ge h.le, hsym]
  have hdiag : (∑ i ∈ B, ∑ j ∈ B, if i = j then f i i else 0) = ∑ i ∈ B, f i i := by
    apply Finset.sum_congr rfl
    intro i hi
    simp [hi]
  have htri : (∑ i ∈ B, ∑ j ∈ B, if i < j then f i j else 0) =
      ∑ p ∈ internalPairs B, f p.1 p.2 := by
    simp [internalPairs, Finset.sum_filter, Finset.sum_product]
  have hswap : (∑ i ∈ B, ∑ j ∈ B, if j < i then f j i else 0) =
      ∑ p ∈ internalPairs B, f p.1 p.2 := by
    rw [Finset.sum_comm]
    exact htri
  calc
    _ = (∑ i ∈ B, ∑ j ∈ B, if i = j then f i i else 0) +
        (∑ i ∈ B, ∑ j ∈ B, if i < j then f i j else 0) +
        (∑ i ∈ B, ∑ j ∈ B, if j < i then f j i else 0) := by
      conv_lhs => arg 2; ext i; arg 2; ext j; rw [hsplit]
      simp only [Finset.sum_add_distrib]
    _ = _ := by rw [hdiag, htri, hswap]; ring

/-- Correlation mass at a positive difference of selected labels. No collision is discarded. -/
noncomputable def labelKernel (F : Finset ℕ) (u : ℕ → ℝ) (t : ℕ) : ℝ :=
  ∑ p ∈ internalPairs F, if differenceLabel p = t then u p.1 * u p.2 else 0

/-- The total internal-label expenditure of one physical block. -/
noncomputable def labelExpenditure (F : Finset ℕ) (u : ℕ → ℝ) (B : Finset ℕ) : ℝ :=
  ∑ t ∈ internalLabels B, labelKernel F u t

/-- For positive shifts the fiber definition is exactly the usual zero-extended correlation. -/
theorem labelKernel_eq_shift_sum (F : Finset ℕ) (u : ℕ → ℝ) {t : ℕ} (ht : 0 < t) :
    labelKernel F u t = ∑ d ∈ F, if d + t ∈ F then u d * u (d + t) else 0 := by
  unfold labelKernel
  simp only [internalPairs, Finset.sum_filter, Finset.sum_product]
  apply Finset.sum_congr rfl
  intro d hd
  have heq (e : ℕ) : (if d < e then if differenceLabel (d, e) = t then u d * u e else 0 else 0) =
      if e = d + t then u d * u e else 0 := by
    by_cases he : e = d + t
    · subst e
      have hlt : d < d + t := by omega
      simp [hlt, differenceLabel]
    · have hnot : ¬(d < e ∧ e - d = t) := by omega
      simp only [differenceLabel]
      split_ifs <;> simp_all
  simp_rw [heq]
  simp

theorem labelKernel_nonneg (F : Finset ℕ) (u : ℕ → ℝ) (hu : ∀ d ∈ F, 0 ≤ u d) (t : ℕ) :
    0 ≤ labelKernel F u t := by
  apply Finset.sum_nonneg
  intro p hp
  obtain ⟨h₁, h₂, _⟩ := (mem_internalPairs F p).mp hp
  split_ifs
  · exact mul_nonneg (hu _ h₁) (hu _ h₂)
  · rfl

theorem labelKernel_eq_zero_of_notMem (F : Finset ℕ) (u : ℕ → ℝ) (t : ℕ)
    (ht : t ∉ internalLabels F) : labelKernel F u t = 0 := by
  apply Finset.sum_eq_zero
  intro p hp
  have hne : differenceLabel p ≠ t := by
    intro heq
    exact ht (Finset.mem_image.mpr ⟨p, hp, heq⟩)
  simp [hne]

/-- The common total kernel budget is `(U²-S)/2`, including repeated label differences. -/
theorem total_labelKernel (F : Finset ℕ) (u : ℕ → ℝ) :
    (∑ t ∈ internalLabels F, labelKernel F u t) =
      ((∑ d ∈ F, u d) ^ 2 - ∑ d ∈ F, u d ^ 2) / 2 := by
  have hfib : (∑ t ∈ internalLabels F, labelKernel F u t) =
      ∑ p ∈ internalPairs F, u p.1 * u p.2 := by
    unfold labelKernel internalLabels
    simp only [← Finset.sum_filter]
    exact Finset.sum_fiberwise_of_maps_to (fun p hp ↦ Finset.mem_image_of_mem differenceLabel hp)
      (fun p ↦ u p.1 * u p.2)
  have hs := symmetric_sum_eq_diagonal_add_twice F (fun i j ↦ u i * u j)
    (fun i j ↦ mul_comm _ _)
  rw [hfib]
  simp only [← Finset.mul_sum, ← Finset.sum_mul, ← pow_two] at hs
  linarith

/-- Any set of used labels spends at most the same total kernel budget. -/
theorem labelKernel_sum_le_total (F D : Finset ℕ) (u : ℕ → ℝ)
    (hu : ∀ d ∈ F, 0 ≤ u d) :
    (∑ t ∈ D, labelKernel F u t) ≤ ∑ t ∈ internalLabels F, labelKernel F u t := by
  have hrestrict : (∑ t ∈ D ∩ internalLabels F, labelKernel F u t) =
      ∑ t ∈ D, labelKernel F u t := by
    apply Finset.sum_subset Finset.inter_subset_left
    intro t ht hnot
    apply labelKernel_eq_zero_of_notMem
    intro hmem
    exact hnot (Finset.mem_inter.mpr ⟨ht, hmem⟩)
  rw [← hrestrict]
  exact Finset.sum_le_sum_of_subset_of_nonneg Finset.inter_subset_right
    (fun t _ _ ↦ labelKernel_nonneg F u hu t)

/-- Disjoint blocks from one actual Sidon history share one total label budget. -/
theorem shared_label_budget {ι : Type*} {A : Set ℕ} (hA : Sidon A)
    (J : Finset ι) (B : ι → Finset ℕ) (P F : Finset ℕ) (u : ℕ → ℝ)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ j ∈ J, ∀ b ∈ B j, b ∈ A)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (B i) (B j))
    (hPB : ∀ j ∈ J, Disjoint P (B j)) (hu : ∀ d ∈ F, 0 ≤ u d) :
    (∑ j ∈ J, labelExpenditure F u (B j)) ≤
      ((∑ d ∈ F, u d) ^ 2 - ∑ d ∈ F, u d ^ 2) / 2 - labelExpenditure F u P := by
  classical
  let D := J.biUnion (fun j ↦ internalLabels (B j))
  have hpairs : (J : Set ι).PairwiseDisjoint (fun j ↦ internalLabels (B j)) := by
    intro i hi j hj hij
    exact internalLabels_disjoint hA _ _ (hB i hi) (hB j hj) (hdisj i hi j hj hij)
  have hsum : (∑ t ∈ D, labelKernel F u t) = ∑ j ∈ J, labelExpenditure F u (B j) := by
    exact Finset.sum_biUnion hpairs
  have hold : Disjoint (internalLabels P) D := by
    apply Finset.disjoint_left.mpr
    intro t htP htD
    obtain ⟨j, hj, htj⟩ := Finset.mem_biUnion.mp htD
    exact Finset.disjoint_left.mp (internalLabels_disjoint hA P (B j) hP (hB j hj) (hPB j hj))
      htP htj
  have hcap := labelKernel_sum_le_total F (internalLabels P ∪ D) u hu
  rw [Finset.sum_union hold, hsum, total_labelKernel] at hcap
  change labelExpenditure F u P + _ ≤ _ at hcap
  linarith

/-- One translated copy of the selected-label weights, with zero extension made explicit. -/
noncomputable def shadowRow (F : Finset ℕ) (u : ℕ → ℝ) (b z : ℕ) : ℝ :=
  ∑ d ∈ F, if b + d = z then u d else 0

/-- The actual finite convolution shadow of a point block and selected labels. -/
noncomputable def labelShadow (B F : Finset ℕ) (u : ℕ → ℝ) (z : ℕ) : ℝ :=
  ∑ b ∈ B, shadowRow F u b z

/-- An explicit finite support container for the convolution shadow. -/
def shadowLocations (B F : Finset ℕ) : Finset ℕ :=
  (B ×ˢ F).image (fun p ↦ p.1 + p.2)

theorem add_mem_shadowLocations (B F : Finset ℕ) {b d : ℕ} (hb : b ∈ B) (hd : d ∈ F) :
    b + d ∈ shadowLocations B F :=
  Finset.mem_image.mpr ⟨(b, d), Finset.mem_product.mpr ⟨hb, hd⟩, rfl⟩

/-- The matrix of pairwise translated-label correlations before using Sidonicity. -/
noncomputable def shadowCorrelation (F : Finset ℕ) (u : ℕ → ℝ) (b c : ℕ) : ℝ :=
  ∑ d ∈ F, ∑ e ∈ F, if b + d = c + e then u d * u e else 0

theorem shadowRow_inner (B F : Finset ℕ) (u : ℕ → ℝ) (b c : ℕ) (hb : b ∈ B) :
    (∑ z ∈ shadowLocations B F, shadowRow F u b z * shadowRow F u c z) =
      shadowCorrelation F u b c := by
  unfold shadowRow shadowCorrelation
  simp_rw [Finset.sum_mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro d hd
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro e he
  have hdelta (z : ℕ) : (if b + d = z then u d else 0) * (if c + e = z then u e else 0) =
      if b + d = z then (if b + d = c + e then u d * u e else 0) else 0 := by
    split_ifs <;> simp_all
  simp_rw [hdelta]
  simp [add_mem_shadowLocations B F hb hd]

theorem shadowCorrelation_symm (F : Finset ℕ) (u : ℕ → ℝ) (b c : ℕ) :
    shadowCorrelation F u b c = shadowCorrelation F u c b := by
  unfold shadowCorrelation
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro d hd
  apply Finset.sum_congr rfl
  intro e he
  simp only [eq_comm, mul_comm]

theorem shadowCorrelation_diag (F : Finset ℕ) (u : ℕ → ℝ) (b : ℕ) :
    shadowCorrelation F u b b = ∑ d ∈ F, u d ^ 2 := by
  unfold shadowCorrelation
  apply Finset.sum_congr rfl
  intro d hd
  simp [hd, pow_two]

theorem shadowCorrelation_eq_kernel (F : Finset ℕ) (u : ℕ → ℝ) {b c : ℕ} (hbc : b < c) :
    shadowCorrelation F u b c = labelKernel F u (c - b) := by
  unfold shadowCorrelation labelKernel
  rw [Finset.sum_comm]
  simp only [internalPairs, Finset.sum_filter, Finset.sum_product]
  apply Finset.sum_congr rfl
  intro d hd
  apply Finset.sum_congr rfl
  intro e he
  have heq : b + e = c + d ↔ d < e ∧ e - d = c - b := by omega
  simp only [differenceLabel, heq, ite_and, mul_comm]
  rfl

theorem shadowRow_sum (B F : Finset ℕ) (u : ℕ → ℝ) (b : ℕ) (hb : b ∈ B) :
    (∑ z ∈ shadowLocations B F, shadowRow F u b z) = ∑ d ∈ F, u d := by
  unfold shadowRow
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro d hd
  simp [add_mem_shadowLocations B F hb hd]

/-- Exact first moment of the actual finite convolution shadow. -/
theorem sum_labelShadow (B F : Finset ℕ) (u : ℕ → ℝ) :
    (∑ z ∈ shadowLocations B F, labelShadow B F u z) = (B.card : ℝ) * ∑ d ∈ F, u d := by
  unfold labelShadow
  rw [Finset.sum_comm]
  calc
    _ = ∑ _b ∈ B, ∑ d ∈ F, u d := by
      apply Finset.sum_congr rfl
      intro b hb
      exact shadowRow_sum B F u b hb
    _ = _ := by simp

/-- Exact convolution second moment; its off-diagonal terms keep their six-point relations. -/
theorem sum_sq_labelShadow {A : Set ℕ} (hA : Sidon A) (B F : Finset ℕ) (u : ℕ → ℝ)
    (hB : ∀ b ∈ B, b ∈ A) :
    (∑ z ∈ shadowLocations B F, labelShadow B F u z ^ 2) =
      (B.card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u B := by
  have hmatrix : (∑ z ∈ shadowLocations B F, labelShadow B F u z ^ 2) =
      ∑ b ∈ B, ∑ c ∈ B, shadowCorrelation F u b c := by
    unfold labelShadow
    simp_rw [pow_two, Finset.sum_mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro b hb
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro c hc
    exact shadowRow_inner B F u b c hb
  have hupper : (∑ p ∈ internalPairs B, shadowCorrelation F u p.1 p.2) =
      labelExpenditure F u B := by
    have hinj := (differenceLabel_injOn hA).mono (internalPairs_actual B hB)
    calc
      _ = ∑ p ∈ internalPairs B, labelKernel F u (differenceLabel p) := by
        apply Finset.sum_congr rfl
        intro p hp
        exact shadowCorrelation_eq_kernel F u (mem_internalPairs B p |>.mp hp).2.2
      _ = _ := (Finset.sum_image hinj).symm
  rw [hmatrix, symmetric_sum_eq_diagonal_add_twice B _ (shadowCorrelation_symm F u), hupper]
  simp [shadowCorrelation_diag]

/-- Cauchy--Schwarz on the exact finite shadow support container. -/
theorem shadow_cauchy_capacity {A : Set ℕ} (hA : Sidon A) (B F : Finset ℕ) (u : ℕ → ℝ)
    (hB : ∀ b ∈ B, b ∈ A) :
    ((B.card : ℝ) * ∑ d ∈ F, u d) ^ 2 ≤
      ((shadowLocations B F).card : ℝ) *
        ((B.card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u B) := by
  have h := Finset.sum_mul_sq_le_sq_mul_sq (shadowLocations B F)
    (fun _ ↦ (1 : ℝ)) (labelShadow B F u)
  simpa only [one_mul, one_pow, Finset.sum_const, nsmul_eq_mul, mul_one,
    sum_labelShadow, sum_sq_labelShadow hA B F u hB] using h

theorem internalLabels_pos (B : Finset ℕ) {d : ℕ} (hd : d ∈ internalLabels B) : 0 < d := by
  obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
  have hpLt := (mem_internalPairs B p).mp hp |>.2.2
  unfold differenceLabel
  omega

/-- Old selected labels cannot translate a future block point onto another point of that block. -/
theorem shadowLocations_disjoint_of_actual_labels {A : Set ℕ} (hA : Sidon A)
    (P B F : Finset ℕ) (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A)
    (hPB : Disjoint P B) (hF : F ⊆ internalLabels P) :
    Disjoint B (shadowLocations B F) := by
  have hd := internalLabels_disjoint hA P B hP hB hPB
  apply Finset.disjoint_left.mpr
  intro z hz hzShadow
  obtain ⟨⟨b, d⟩, hbd, hsum⟩ := Finset.mem_image.mp hzShadow
  obtain ⟨hb, hdF⟩ := Finset.mem_product.mp hbd
  have hdpos := internalLabels_pos P (hF hdF)
  have hdiff : d ∈ internalLabels B := by
    apply Finset.mem_image.mpr
    refine ⟨(b, z), ?_, ?_⟩
    · apply (mem_internalPairs B (b, z)).mpr
      exact ⟨hb, hz, by dsimp at hsum; omega⟩
    · dsimp [differenceLabel] at *
      omega
  exact Finset.disjoint_left.mp hd (hF hdF) hdiff

/-- Excluding the actual block from its shadow improves Cauchy's capacity by its cardinality. -/
theorem shadow_cauchy_ambient_capacity {A : Set ℕ} (hA : Sidon A)
    (P B F V : Finset ℕ) (u : ℕ → ℝ)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hF : F ⊆ internalLabels P) (hBV : B ⊆ V) (hZV : shadowLocations B F ⊆ V) :
    ((B.card : ℝ) * ∑ d ∈ F, u d) ^ 2 ≤
      ((V.card : ℝ) - B.card) *
        ((B.card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u B) := by
  have hd := shadowLocations_disjoint_of_actual_labels hA P B F hP hB hPB hF
  have hcard : B.card + (shadowLocations B F).card ≤ V.card := by
    rw [← Finset.card_union_of_disjoint hd]
    exact Finset.card_le_card (Finset.union_subset hBV hZV)
  have hcardR : (B.card : ℝ) + (shadowLocations B F).card ≤ V.card := by exact_mod_cast hcard
  have hZcap : ((shadowLocations B F).card : ℝ) ≤ (V.card : ℝ) - B.card := by linarith
  have henergy : 0 ≤ (B.card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u B := by
    rw [← sum_sq_labelShadow hA B F u hB]
    exact Finset.sum_nonneg (fun z _ ↦ sq_nonneg _)
  exact (shadow_cauchy_capacity hA B F u hB).trans (mul_le_mul_of_nonneg_right hZcap henergy)

/-- The exact interval-length version of the selected-label capacity inequality (9). -/
theorem shadow_interval_capacity {A : Set ℕ} (hA : Sidon A)
    (P B F : Finset ℕ) (u : ℕ → ℝ) (n L H : ℕ) (hL : 0 < L)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hF : F ⊆ internalLabels P) (hBF : B ⊆ Finset.Icc n (n + L - 1))
    (hFH : F ⊆ Finset.Icc 1 H) :
    ((B.card : ℝ) * ∑ d ∈ F, u d) ^ 2 ≤
      ((L : ℝ) + H - B.card) *
        ((B.card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u B) := by
  let V := Finset.Icc n (n + L + H - 1)
  have hBV : B ⊆ V := by
    intro b hb
    have hbI := Finset.mem_Icc.mp (hBF hb)
    apply Finset.mem_Icc.mpr
    omega
  have hZV : shadowLocations B F ⊆ V := by
    intro z hz
    obtain ⟨⟨b, d⟩, hbd, rfl⟩ := Finset.mem_image.mp hz
    obtain ⟨hb, hd⟩ := Finset.mem_product.mp hbd
    have hbI := Finset.mem_Icc.mp (hBF hb)
    have hdI := Finset.mem_Icc.mp (hFH hd)
    apply Finset.mem_Icc.mpr
    dsimp
    omega
  have hVcard : V.card = L + H := by
    dsimp [V]
    rw [Nat.card_Icc]
    omega
  have h := shadow_cauchy_ambient_capacity hA P B F V u hP hB hPB hF hBV hZV
  simpa only [hVcard, Nat.cast_add] using h

/-- The finite shared lower-demand/upper-budget inequality (13), for one actual Sidon history. -/
theorem shared_interval_demand_budget {ι : Type*} {A : Set ℕ} (hA : Sidon A)
    (J : Finset ι) (B : ι → Finset ℕ) (P F : Finset ℕ) (u : ℕ → ℝ)
    (n L : ι → ℕ) (H : ℕ) (hH : 0 < H)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ j ∈ J, ∀ b ∈ B j, b ∈ A)
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (B i) (B j))
    (hPB : ∀ j ∈ J, Disjoint P (B j)) (hu : ∀ d ∈ F, 0 ≤ u d)
    (hF : F ⊆ internalLabels P) (hFH : F ⊆ Finset.Icc 1 H)
    (hL : ∀ j ∈ J, 0 < L j) (hBounds : ∀ j ∈ J, B j ⊆ Finset.Icc (n j) (n j + L j - 1)) :
    (∑ j ∈ J, max (0 : ℝ)
      ((((B j).card : ℝ) * ∑ d ∈ F, u d) ^ 2 / ((L j : ℝ) + H - (B j).card) -
        ((B j).card : ℝ) * ∑ d ∈ F, u d ^ 2)) ≤
      (∑ d ∈ F, u d) ^ 2 - (∑ d ∈ F, u d ^ 2) - 2 * labelExpenditure F u P := by
  have hlocal (j : ι) (hj : j ∈ J) :
      max (0 : ℝ) ((((B j).card : ℝ) * ∑ d ∈ F, u d) ^ 2 /
        ((L j : ℝ) + H - (B j).card) - ((B j).card : ℝ) * ∑ d ∈ F, u d ^ 2) ≤
        2 * labelExpenditure F u (B j) := by
    have hcard : (B j).card ≤ L j := by
      have hc := Finset.card_le_card (hBounds j hj)
      rw [Nat.card_Icc] at hc
      have heq : n j + L j - 1 + 1 - n j = L j := by have := hL j hj; omega
      simpa only [heq] using hc
    have hcardR : ((B j).card : ℝ) ≤ L j := by exact_mod_cast hcard
    have hHR : (0 : ℝ) < H := by exact_mod_cast hH
    have hden : (0 : ℝ) < (L j : ℝ) + H - (B j).card := by linarith
    have hc := shadow_interval_capacity hA P (B j) F u (n j) (L j) H (hL j hj)
      hP (hB j hj) (hPB j hj) hF (hBounds j hj) hFH
    have hquot : (((B j).card : ℝ) * ∑ d ∈ F, u d) ^ 2 /
        ((L j : ℝ) + H - (B j).card) ≤
        ((B j).card : ℝ) * (∑ d ∈ F, u d ^ 2) + 2 * labelExpenditure F u (B j) :=
      (div_le_iff₀ hden).mpr (hc.trans_eq (mul_comm _ _))
    have hpsi : 0 ≤ labelExpenditure F u (B j) :=
      Finset.sum_nonneg (fun t _ ↦ labelKernel_nonneg F u hu t)
    apply max_le
    · linarith
    · linarith
  have hsum := Finset.sum_le_sum hlocal
  have hbudget := shared_label_budget hA J B P F u hP hB hdisj hPB hu
  rw [← Finset.mul_sum] at hsum
  linarith

end Erdos1191Q1
