import Q1.PhysicalLabelEnvelope

/-!
# A first-moment demand on one actual physical-label budget

A signed, zero-mass label vector gives a second Cauchy lower bound for its actual
convolution shadow. The full kernel is `J + lam zzᵀ`; its residual is never separately
assumed nonnegative or assigned another copy of the physical difference budget.
These are finite supporting theorems. They do not prove Q1 or a uniform envelope gap.
-/

namespace Erdos1191Q1

open scoped BigOperators

/-- The centered coordinate square sum on the specified finite support container. -/
noncomputable def coordinateVariance (T : Finset ℕ) (c : ℝ) : ℝ :=
  ∑ x ∈ T, ((x : ℝ) - c) ^ 2

/-- The actual signed first moment of the selected physical labels. -/
noncomputable def labelFirstMoment (F : Finset ℕ) (z : ℕ → ℝ) : ℝ :=
  ∑ d ∈ F, (d : ℝ) * z d

/-- Translation preserves every term of the weighted shadow first moment. -/
theorem shadowRow_firstMoment (B F : Finset ℕ) (z : ℕ → ℝ) (b : ℕ) (hb : b ∈ B) :
    (∑ x ∈ shadowLocations B F, (x : ℝ) * shadowRow F z b x) =
      ∑ d ∈ F, ((b + d : ℕ) : ℝ) * z d := by
  unfold shadowRow
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro d hd
  simp only [mul_ite, mul_zero]
  simp [add_mem_shadowLocations B F hb hd]

/-- The point-coordinate contribution vanishes when the label coefficients sum to zero. -/
theorem labelShadow_firstMoment (B F : Finset ℕ) (z : ℕ → ℝ)
    (hz : ∑ d ∈ F, z d = 0) :
    (∑ x ∈ shadowLocations B F, (x : ℝ) * labelShadow B F z x) =
      (B.card : ℝ) * labelFirstMoment F z := by
  unfold labelShadow
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  calc
    _ = ∑ b ∈ B, ∑ d ∈ F, ((b + d : ℕ) : ℝ) * z d := by
      apply Finset.sum_congr rfl
      intro b hb
      exact shadowRow_firstMoment B F z b hb
    _ = ∑ _b ∈ B, labelFirstMoment F z := by
      apply Finset.sum_congr rfl
      intro b hb
      simp only [Nat.cast_add, add_mul, Finset.sum_add_distrib,
        ← Finset.mul_sum, hz, mul_zero, zero_add, labelFirstMoment]
    _ = _ := by simp

/-- Centering the coordinates does not change a zero-mass shadow's first moment. -/
theorem labelShadow_centered_firstMoment (B F : Finset ℕ) (z : ℕ → ℝ) (c : ℝ)
    (hz : ∑ d ∈ F, z d = 0) :
    (∑ x ∈ shadowLocations B F, ((x : ℝ) - c) * labelShadow B F z x) =
      (B.card : ℝ) * labelFirstMoment F z := by
  simp_rw [sub_mul]
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum, labelShadow_firstMoment B F z hz,
    sum_labelShadow, hz]
  ring

/-- Centered Cauchy on any literal finite container of the actual shadow locations. -/
theorem shadow_firstMoment_cauchy (B F T : Finset ℕ) (z : ℕ → ℝ) (c : ℝ)
    (hz : ∑ d ∈ F, z d = 0) (hT : shadowLocations B F ⊆ T) :
    ((B.card : ℝ) * labelFirstMoment F z) ^ 2 ≤
      coordinateVariance T c * ∑ x ∈ shadowLocations B F, labelShadow B F z x ^ 2 := by
  have hc := Finset.sum_mul_sq_le_sq_mul_sq (shadowLocations B F)
    (fun x ↦ (x : ℝ) - c) (labelShadow B F z)
  rw [labelShadow_centered_firstMoment B F z c hz] at hc
  have hv : (∑ x ∈ shadowLocations B F, ((x : ℝ) - c) ^ 2) ≤
      coordinateVariance T c :=
    Finset.sum_le_sum_of_subset_of_nonneg hT (fun _ _ _ ↦ sq_nonneg _)
  exact hc.trans (mul_le_mul_of_nonneg_right hv
    (Finset.sum_nonneg (fun _ _ ↦ sq_nonneg _)))

/-- The extra energy lower bound, with value zero when the coordinate variance is zero. -/
noncomputable def shadowMomentLowerBound (B F T : Finset ℕ) (z : ℕ → ℝ) (c : ℝ) : ℝ :=
  ((B.card : ℝ) * labelFirstMoment F z) ^ 2 / coordinateVariance T c

/-- A zero denominator adds zero demand; otherwise the lower bound follows by division. -/
theorem shadowMomentLowerBound_le (B F T : Finset ℕ) (z : ℕ → ℝ) (c : ℝ)
    (hz : ∑ d ∈ F, z d = 0) (hT : shadowLocations B F ⊆ T) :
    shadowMomentLowerBound B F T z c ≤
      ∑ x ∈ shadowLocations B F, labelShadow B F z x ^ 2 := by
  have hv : 0 ≤ coordinateVariance T c := Finset.sum_nonneg (fun _ _ ↦ sq_nonneg _)
  have he : 0 ≤ ∑ x ∈ shadowLocations B F, labelShadow B F z x ^ 2 :=
    Finset.sum_nonneg (fun _ _ ↦ sq_nonneg _)
  unfold shadowMomentLowerBound
  by_cases hzero : coordinateVariance T c = 0
  · simpa [hzero] using he
  · have hpos : 0 < coordinateVariance T c := lt_of_le_of_ne hv (Ne.symm hzero)
    apply (div_le_iff₀ hpos).mpr
    exact (shadow_firstMoment_cauchy B F T z c hz hT).trans_eq (mul_comm _ _)

/-- The physical matrix kernel of `J + lam zzᵀ`, expressed as two orthogonal channels. -/
noncomputable def momentKernel (F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) (t : ℕ) : ℝ :=
  labelKernel F (fun _ ↦ 1) t + lam * labelKernel F z t

/-- Its fiber contains the full matrix entry, including every repeated relation label. -/
theorem momentKernel_eq_pairs (F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) (t : ℕ) :
    momentKernel F z lam t = ∑ p ∈ internalPairs F,
      if differenceLabel p = t then 1 + lam * z p.1 * z p.2 else 0 := by
  unfold momentKernel labelKernel
  rw [Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro p hp
  split_ifs <;> ring

/-- Only the full matrix entries are required to be nonnegative. -/
theorem momentKernel_nonneg (F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ)
    (hW : ∀ d ∈ F, ∀ e ∈ F, 0 ≤ 1 + lam * z d * z e) (t : ℕ) :
    0 ≤ momentKernel F z lam t := by
  rw [momentKernel_eq_pairs]
  apply Finset.sum_nonneg
  intro p hp
  obtain ⟨hd, he, _⟩ := (mem_internalPairs F p).mp hp
  split_ifs
  · exact hW p.1 hd p.2 he
  · rfl

/-- The full matrix kernel has finite support without assuming a sign on its residual. -/
theorem momentKernel_supported (F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) (t : ℕ)
    (ht : t ∉ internalLabels F) : momentKernel F z lam t = 0 := by
  simp [momentKernel, labelKernel_eq_zero_of_notMem F _ t ht]

/-- The one-copy physical expenditure of the full matrix on an actual point block. -/
noncomputable def momentExpenditure (B F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) : ℝ :=
  ∑ t ∈ internalLabels B, momentKernel F z lam t

/-- Channel decomposition is an identity for one expenditure, not two source budgets. -/
theorem momentExpenditure_eq (B F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) :
    momentExpenditure B F z lam =
      labelExpenditure F (fun _ ↦ 1) B + lam * labelExpenditure F z B := by
  simp [momentExpenditure, momentKernel, labelExpenditure, Finset.sum_add_distrib,
    Finset.mul_sum]

/-- Signed energy and its diagonal cost are retained in the same physical kernel. -/
theorem moment_shadow_energy {A : Set ℕ} (hA : Sidon A) (B F : Finset ℕ)
    (z : ℕ → ℝ) (lam : ℝ) (hB : ∀ b ∈ B, b ∈ A) :
    (∑ x ∈ shadowLocations B F, labelShadow B F (fun _ ↦ 1) x ^ 2) +
      lam * (∑ x ∈ shadowLocations B F, labelShadow B F z x ^ 2) =
        (B.card : ℝ) * ((F.card : ℝ) + lam * ∑ d ∈ F, z d ^ 2) +
          2 * momentExpenditure B F z lam := by
  rw [sum_sq_labelShadow hA B F _ hB, sum_sq_labelShadow hA B F z hB,
    momentExpenditure_eq]
  simp only [one_pow, Finset.sum_const, nsmul_eq_mul, mul_one]
  ring

/-- The old mass-only raw demand for the same matrix, including its full diagonal. -/
noncomputable def matrixMassRawDemand (B F : Finset ℕ) (z : ℕ → ℝ) (lam D : ℝ) : ℝ :=
  (((B.card : ℝ) * F.card) ^ 2 / D -
    (B.card : ℝ) * ((F.card : ℝ) + lam * ∑ d ∈ F, z d ^ 2)) / 2

/-- A raw demand with the extra first-moment energy of its second feature coordinate. -/
noncomputable def momentRawDemand (B F T : Finset ℕ) (z : ℕ → ℝ) (lam D c : ℝ) : ℝ :=
  (((B.card : ℝ) * F.card) ^ 2 / D + lam * shadowMomentLowerBound B F T z c -
    (B.card : ℝ) * ((F.card : ℝ) + lam * ∑ d ∈ F, z d ^ 2)) / 2

/-- The raw improvement is exactly half the weighted extra energy, without any sign assumption. -/
theorem momentRawDemand_sub_mass (B F T : Finset ℕ) (z : ℕ → ℝ) (lam D c : ℝ) :
    momentRawDemand B F T z lam D c - matrixMassRawDemand B F z lam D =
      lam * shadowMomentLowerBound B F T z c / 2 := by
  unfold momentRawDemand matrixMassRawDemand
  ring

/-- The nonnegative demand which can be charged to the full physical matrix kernel. -/
noncomputable def momentDemand (B F T : Finset ℕ) (z : ℕ → ℝ) (lam D c : ℝ) : ℝ :=
  max 0 (momentRawDemand B F T z lam D c)

/-- The moment contribution is proved from the actual shadow; it is not a payment hypothesis. -/
theorem momentRawDemand_le {A : Set ℕ} (hA : Sidon A) (P B F T : Finset ℕ)
    (z : ℕ → ℝ) (lam c : ℝ) (n L H : ℕ) (hL : 0 < L) (hH : 0 < H)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hF : F ⊆ internalLabels P) (hFH : F ⊆ Finset.Icc 1 H)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1))
    (hz : ∑ d ∈ F, z d = 0) (hlam : 0 ≤ lam) (hT : shadowLocations B F ⊆ T) :
    momentRawDemand B F T z lam ((L : ℝ) + H - B.card) c ≤
      momentExpenditure B F z lam := by
  have hden := intervalCapacity_pos B n L H hL hH hBounds
  have hbase := shadow_interval_capacity hA P B F (fun _ ↦ 1) n L H hL
    hP hB hPB hF hBounds hFH
  simp only [one_pow, Finset.sum_const, nsmul_eq_mul, mul_one] at hbase
  have hmass : ((B.card : ℝ) * F.card) ^ 2 / ((L : ℝ) + H - B.card) ≤
      (B.card : ℝ) * F.card + 2 * labelExpenditure F (fun _ ↦ 1) B :=
    (div_le_iff₀ hden).mpr (hbase.trans_eq (mul_comm _ _))
  have hmoment := shadowMomentLowerBound_le B F T z c hz hT
  rw [sum_sq_labelShadow hA B F z hB] at hmoment
  have hweighted := mul_le_mul_of_nonneg_left hmoment hlam
  rw [momentExpenditure_eq]
  unfold momentRawDemand
  nlinarith

/-- Taking a positive part uses only nonnegativity of the full matrix entries. -/
theorem momentDemand_le {A : Set ℕ} (hA : Sidon A) (P B F T : Finset ℕ)
    (z : ℕ → ℝ) (lam c : ℝ) (n L H : ℕ) (hL : 0 < L) (hH : 0 < H)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hF : F ⊆ internalLabels P) (hFH : F ⊆ Finset.Icc 1 H)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1))
    (hz : ∑ d ∈ F, z d = 0) (hlam : 0 ≤ lam) (hT : shadowLocations B F ⊆ T)
    (hW : ∀ d ∈ F, ∀ e ∈ F, 0 ≤ 1 + lam * z d * z e) :
    momentDemand B F T z lam ((L : ℝ) + H - B.card) c ≤
      momentExpenditure B F z lam := by
  apply max_le
  · exact Finset.sum_nonneg (fun t _ ↦ momentKernel_nonneg F z lam hW t)
  · exact momentRawDemand_le hA P B F T z lam c n L H hL hH hP hB hPB hF hFH
      hBounds hz hlam hT

/-- An explicit interval container; no assumed moment lower bound appears in this choice. -/
theorem shadowLocations_subset_interval (B F : Finset ℕ) (n L H : ℕ) (hL : 0 < L)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1)) (hFH : F ⊆ Finset.Icc 1 H) :
    shadowLocations B F ⊆ Finset.Icc (n + 1) (n + L + H - 1) := by
  intro x hx
  obtain ⟨⟨b, d⟩, hbd, rfl⟩ := Finset.mem_image.mp hx
  obtain ⟨hb, hd⟩ := Finset.mem_product.mp hbd
  have hbI := Finset.mem_Icc.mp (hBounds hb)
  have hdI := Finset.mem_Icc.mp (hFH hd)
  apply Finset.mem_Icc.mpr
  dsimp
  omega

/-- The stronger demand with a concrete full-interval squared-coordinate denominator. -/
theorem interval_momentDemand_le {A : Set ℕ} (hA : Sidon A) (P B F : Finset ℕ)
    (z : ℕ → ℝ) (lam : ℝ) (n L H : ℕ) (hL : 0 < L) (hH : 0 < H)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hF : F ⊆ internalLabels P) (hFH : F ⊆ Finset.Icc 1 H)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1))
    (hz : ∑ d ∈ F, z d = 0) (hlam : 0 ≤ lam)
    (hW : ∀ d ∈ F, ∀ e ∈ F, 0 ≤ 1 + lam * z d * z e) :
    momentDemand B F (Finset.Icc (n + 1) (n + L + H - 1)) z lam
        ((L : ℝ) + H - B.card) ((n : ℝ) + ((L : ℝ) + H) / 2) ≤
      momentExpenditure B F z lam :=
  momentDemand_le hA P B F _ z lam _ n L H hL hH hP hB hPB hF hFH hBounds hz hlam
    (shadowLocations_subset_interval B F n L H hL hBounds hFH) hW

/-- The full matrix kernel with literal span and already-used-old-label masks. -/
noncomputable def maskedMomentKernel (P F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ)
    (L t : ℕ) : ℝ :=
  if 1 ≤ t ∧ t ≤ L - 1 ∧ t ∉ internalLabels P then momentKernel F z lam t else 0

/-- Nonnegativity is imposed on the full matrix, not on its signed rank-one channel. -/
theorem maskedMomentKernel_nonneg (P F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) (L t : ℕ)
    (hW : ∀ d ∈ F, ∀ e ∈ F, 0 ≤ 1 + lam * z d * z e) :
    0 ≤ maskedMomentKernel P F z lam L t := by
  unfold maskedMomentKernel
  split_ifs
  · exact momentKernel_nonneg F z lam hW t
  · exact le_rfl

/-- Every masked matrix kernel is supported on the actual relation labels of its bank. -/
theorem maskedMomentKernel_supported (P F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ)
    (L t : ℕ) (ht : t ∉ internalLabels F) :
    maskedMomentKernel P F z lam L t = 0 := by
  unfold maskedMomentKernel
  split_ifs
  · exact momentKernel_supported F z lam t ht
  · rfl

/-- Actual future differences survive both masks, by the original Sidon condition. -/
theorem maskedMomentKernel_eq_on_actual {A : Set ℕ} (hA : Sidon A)
    (P B F : Finset ℕ) (z : ℕ → ℝ) (lam : ℝ) (n L : ℕ) (hL : 0 < L)
    (hP : ∀ p ∈ P, p ∈ A) (hB : ∀ b ∈ B, b ∈ A) (hPB : Disjoint P B)
    (hBounds : B ⊆ Finset.Icc n (n + L - 1)) {t : ℕ} (ht : t ∈ internalLabels B) :
    maskedMomentKernel P F z lam L t = momentKernel F z lam t := by
  have hspan := internalLabels_mem_interval B n L hL hBounds ht
  have hd := internalLabels_disjoint hA P B hP hB hPB
  have hnot : t ∉ internalLabels P := fun hp ↦ Finset.disjoint_left.mp hd hp ht
  exact if_pos ⟨hspan.1, hspan.2, hnot⟩

/-- Multiple moment-strengthened demands spend each actual physical difference at most once.
The old bank, signed vector, coefficient, and moment container may vary with the block.
The right side contains the same full matrix kernel, with no extra moment-payment hypothesis. -/
theorem shared_momentDemand_envelope {ι : Type*} {A : Set ℕ} (hA : Sidon A)
    (J : Finset ι) (P B F T : ι → Finset ℕ) (z : ι → ℕ → ℝ) (lam c : ι → ℝ)
    (n L H : ι → ℕ) (hL : ∀ j ∈ J, 0 < L j) (hH : ∀ j ∈ J, 0 < H j)
    (hP : ∀ j ∈ J, ∀ p ∈ P j, p ∈ A) (hB : ∀ j ∈ J, ∀ b ∈ B j, b ∈ A)
    (hPB : ∀ j ∈ J, Disjoint (P j) (B j))
    (hdisj : ∀ i ∈ J, ∀ j ∈ J, i ≠ j → Disjoint (B i) (B j))
    (hF : ∀ j ∈ J, F j ⊆ internalLabels (P j))
    (hFH : ∀ j ∈ J, F j ⊆ Finset.Icc 1 (H j))
    (hBounds : ∀ j ∈ J, B j ⊆ Finset.Icc (n j) (n j + L j - 1))
    (hz : ∀ j ∈ J, ∑ d ∈ F j, z j d = 0) (hlam : ∀ j ∈ J, 0 ≤ lam j)
    (hT : ∀ j ∈ J, shadowLocations (B j) (F j) ⊆ T j)
    (hW : ∀ j ∈ J, ∀ d ∈ F j, ∀ e ∈ F j, 0 ≤ 1 + lam j * z j d * z j e) :
    (∑ j ∈ J, momentDemand (B j) (F j) (T j) (z j) (lam j)
        ((L j : ℝ) + H j - (B j).card) (c j)) ≤
      ∑ t ∈ J.biUnion (fun j ↦ internalLabels (F j)),
        physicalEnvelope J (fun j ↦ maskedMomentKernel (P j) (F j) (z j) (lam j) (L j))
          t := by
  classical
  apply actual_blocks_envelope_budget hA J B _ _ _ hB hdisj
  · intro j hj t
    exact maskedMomentKernel_nonneg (P j) (F j) (z j) (lam j) (L j) t (hW j hj)
  · intro j hj t ht
    apply maskedMomentKernel_supported
    exact fun hf ↦ ht (Finset.mem_biUnion.mpr ⟨j, hj, hf⟩)
  · intro j hj
    have heq : (∑ t ∈ internalLabels (B j),
        maskedMomentKernel (P j) (F j) (z j) (lam j) (L j) t) =
        momentExpenditure (B j) (F j) (z j) (lam j) := by
      apply Finset.sum_congr rfl
      intro t ht
      exact maskedMomentKernel_eq_on_actual hA (P j) (B j) (F j) (z j) (lam j)
        (n j) (L j) (hL j hj) (hP j hj) (hB j hj) (hPB j hj) (hBounds j hj) ht
    rw [heq]
    exact momentDemand_le hA (P j) (B j) (F j) (T j) (z j) (lam j) (c j)
      (n j) (L j) (H j) (hL j hj) (hH j hj) (hP j hj) (hB j hj) (hPB j hj)
      (hF j hj) (hFH j hj) (hBounds j hj) (hz j hj) (hlam j hj) (hT j hj) (hW j hj)

end Erdos1191Q1
