import Q1.Target
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

/-- Exact products and output differences of the three old-endpoint matchings. -/
theorem old_quadruple_matching_algebra (A B C : ℝ) :
    (A + B) * (B + C) = A * C + B * (A + B + C) ∧
    (B + C) - (A + B) = C - A ∧
    (A + B + C) - B = A + C := by
  constructor
  · ring
  constructor <;> ring

/-- The two-gap sum is larger than the two-gap absolute difference. -/
theorem plus_output_gt_minus (A C : ℝ) (hA : 0 < A) (hC : 0 < C) :
    |C - A| < A + C := by
  rw [abs_lt]
  constructor <;> linarith

/-- Exact weighted fiber decomposition before the injective images are bounded. -/
theorem weighted_fiber_deficit_identity (F : Finset ι) (p q : ι → ℝ) (L : ℝ) :
    (∑ c ∈ F, (q c - p c)) =
      (∑ c ∈ F, (L - p c)) - (∑ c ∈ F, (L - q c)) := by
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro c _
  ring

/-- A bounded mass at each positive integer forces a lower first moment.
Here `μ i` is the mass at the positive integer `i+1`; no core bound is assumed. -/
theorem bounded_integer_mass_first_moment (n : ℕ) (μ : ℕ → ℝ) (D : ℝ)
    (hμ : ∀ i, 0 ≤ μ i) (hD : ∀ i, μ i ≤ D) :
    (∑ i ∈ range n, μ i)^2 + D * (∑ i ∈ range n, μ i) ≤
      2 * D * ∑ i ∈ range n, ((i : ℝ) + 1) * μ i := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hsum : (∑ i ∈ range n, μ i) ≤ (n : ℝ) * D := by
      calc
        _ ≤ ∑ _i ∈ range n, D := Finset.sum_le_sum fun i _ ↦ hD i
        _ = _ := by simp
    have hcross := mul_le_mul_of_nonneg_right hsum (hμ n)
    have hsquare := mul_le_mul_of_nonneg_left (hD n) (hμ n)
    simp only [sum_range_succ]
    nlinarith

def tripartiteFiber (L R F : Finset ℕ) (s : ℕ) : Finset (ℕ × ℕ × ℕ) :=
  (L.product (R.product F)).filter (fun t ↦ t.1 + t.2.1 + t.2.2 = s)

theorem mem_tripartiteFiber {L R F : Finset ℕ} {s x y z : ℕ} :
    (x,y,z) ∈ tripartiteFiber L R F s ↔
      x ∈ L ∧ y ∈ R ∧ z ∈ F ∧ x+y+z=s := by
  simp [tripartiteFiber, and_assoc]

theorem tripartiteFiber_card_le_min {A : Set ℕ} (hA : Sidon A)
    (L R F : Finset ℕ)
    (hL : ∀ x ∈ L, x ∈ A) (hR : ∀ x ∈ R, x ∈ A)
    (hF : ∀ x ∈ F, x ∈ A)
    (hLR : Disjoint L R) (hLF : Disjoint L F) (hRF : Disjoint R F) (s : ℕ) :
    (tripartiteFiber L R F s).card ≤ min L.card (min R.card F.card) := by
  have pair_unique (X Y : Finset ℕ) (hX : ∀ x ∈ X, x ∈ A)
      (hY : ∀ y ∈ Y, y ∈ A) (hXY : Disjoint X Y)
      {x y x' y' : ℕ} (hx : x ∈ X) (hy : y ∈ Y)
      (hx' : x' ∈ X) (hy' : y' ∈ Y) (heq : x+y=x'+y') :
      x=x' ∧ y=y' := by
    rcases hA x (hX x hx) y (hY y hy) x' (hX x' hx') y' (hY y' hy') heq with h | h
    · exact h
    · exact False.elim (Finset.disjoint_left.mp hXY hx (h.1.symm ▸ hy'))
  have boundL : (tripartiteFiber L R F s).card ≤ L.card := by
    apply Finset.card_le_card_of_injOn (fun t : ℕ × ℕ × ℕ ↦ t.1)
    · rintro ⟨x,y,z⟩ ht
      exact (mem_tripartiteFiber.mp ht).1
    · rintro ⟨x,y,z⟩ ht ⟨x',y',z'⟩ ht' heq
      obtain ⟨hx,hy,hz,hs⟩ := mem_tripartiteFiber.mp ht
      obtain ⟨hx',hy',hz',hs'⟩ := mem_tripartiteFiber.mp ht'
      change x=x' at heq
      obtain ⟨hey,hez⟩ := pair_unique R F hR hF hRF hy hz hy' hz' (by omega)
      simp [heq,hey,hez]
  have boundR : (tripartiteFiber L R F s).card ≤ R.card := by
    apply Finset.card_le_card_of_injOn (fun t : ℕ × ℕ × ℕ ↦ t.2.1)
    · rintro ⟨x,y,z⟩ ht
      exact (mem_tripartiteFiber.mp ht).2.1
    · rintro ⟨x,y,z⟩ ht ⟨x',y',z'⟩ ht' heq
      obtain ⟨hx,hy,hz,hs⟩ := mem_tripartiteFiber.mp ht
      obtain ⟨hx',hy',hz',hs'⟩ := mem_tripartiteFiber.mp ht'
      change y=y' at heq
      obtain ⟨hex,hez⟩ := pair_unique L F hL hF hLF hx hz hx' hz' (by omega)
      simp [heq,hex,hez]
  have boundF : (tripartiteFiber L R F s).card ≤ F.card := by
    apply Finset.card_le_card_of_injOn (fun t : ℕ × ℕ × ℕ ↦ t.2.2)
    · rintro ⟨x,y,z⟩ ht
      exact (mem_tripartiteFiber.mp ht).2.2.1
    · rintro ⟨x,y,z⟩ ht ⟨x',y',z'⟩ ht' heq
      obtain ⟨hx,hy,hz,hs⟩ := mem_tripartiteFiber.mp ht
      obtain ⟨hx',hy',hz',hs'⟩ := mem_tripartiteFiber.mp ht'
      change z=z' at heq
      obtain ⟨hex,hey⟩ := pair_unique L R hL hR hLR hx hy hx' hy' (by omega)
      simp [heq,hex,hey]
  exact le_min boundL (le_min boundR boundF)

/-- Exact fiber-deficit change when a new translate has zero-one coefficients. -/
theorem fiber_deficit_increment (S : Finset ι) (v w : ι → ℝ) (d d' : ℝ)
    (hw : ∀ z ∈ S, w z ^ 2 = w z) :
    (∑ z ∈ S, ((v z+w z)*(d'-v z-w z)-v z*(d-v z))) =
      (d'-d)*(∑ z ∈ S, v z) + (d'-1)*(∑ z ∈ S, w z) -
        2*(∑ z ∈ S, v z*w z) := by
  simp_rw [Finset.mul_sum]
  rw [← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro z hz
  nlinarith only [hw z hz]

/-- Simultaneous exchange against one common bank; added/removed sites never coexist. -/
theorem fiber_exchange_collision_identity (S : Finset ι) (u p m : ι → ℝ)
    (hp : ∀ z ∈ S, p z ^ 2 = p z) (hm : ∀ z ∈ S, m z ^ 2 = m z) :
    (∑ z ∈ S, ((u z + p z) * (u z + p z - 1) -
        (u z + m z) * (u z + m z - 1))) =
      2 * (∑ z ∈ S, u z * (p z - m z)) := by
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro z hz
  nlinarith only [hp z hz, hm z hz]

/-- Exact deficit exchange, with both capacities retained and no monotonicity claim. -/
theorem fiber_exchange_deficit_identity (S : Finset ι) (u p m : ι → ℝ) (d d' : ℝ)
    (hp : ∀ z ∈ S, p z ^ 2 = p z) (hm : ∀ z ∈ S, m z ^ 2 = m z) :
    (∑ z ∈ S, ((u z + p z) * (d' - u z - p z) -
        (u z + m z) * (d - u z - m z))) =
      (d' - d) * (∑ z ∈ S, u z) + (d' - 1) * (∑ z ∈ S, p z) -
        (d - 1) * (∑ z ∈ S, m z) -
          2 * (∑ z ∈ S, u z * (p z - m z)) := by
  simp_rw [Finset.mul_sum]
  rw [← Finset.sum_add_distrib, ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro z hz
  nlinarith only [hp z hz, hm z hz]

/-- An exact open-cut boundary identity; each physical record keeps its own weight. -/
theorem profile_step (R : Finset ι) (v : ι → ℝ) (c i : ι → ℕ) (b : ℕ) :
    profile R v c i (b + 1) - profile R v c i b =
      (∑ h ∈ R, if c h = b ∧ b + 1 < i h then v h else 0) -
        (∑ h ∈ R, if i h = b + 1 ∧ c h < b then v h else 0) := by
  unfold profile
  rw [← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro h hh
  split_ifs <;> simp_all <;> omega

/-- Sum of the three physical matching products at one old quadruple. -/
theorem quadruple_product_sum_bound (A B C : ℝ)
    (hA : 0 ≤ A) (hB : 0 ≤ B) (hC : 0 ≤ C) :
    A * C + (A + B) * (B + C) + B * (A + B + C) ≤
      2 * (A + B + C) ^ 2 := by
  nlinarith [sq_nonneg A, sq_nonneg C, mul_nonneg hA hC,
    mul_nonneg hA hB, mul_nonneg hB hC]

/-- Signed integer layer-cake identity; negative birth-minus-retirement masses are allowed. -/
theorem signed_integer_tail_first_moment (n : ℕ) (μ : ℕ → ℝ) :
    (∑ i ∈ Finset.range n, ((i : ℝ) + 1) * μ i) =
      ∑ s ∈ Finset.range n, ∑ i ∈ Finset.range n, if s ≤ i then μ i else 0 := by
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i hi
  have hin : i < n := Finset.mem_range.mp hi
  have hf : (Finset.range n).filter (fun s => s ≤ i) = Finset.range (i + 1) := by
    ext s
    simp only [Finset.mem_filter, Finset.mem_range]
    omega
  rw [← Finset.sum_filter, hf]
  simp [Nat.cast_add, Nat.cast_one]

/-- A fixed sum or a fixed nonzero difference recovers an ordered pair in the actual Sidon set. -/
theorem sidon_ordered_pair_recovery {A : Set ℕ} (hA : Erdos1191Q1.Sidon A)
    {x y x' y' : ℕ} (hx : x ∈ A) (hy : y ∈ A) (hx' : x' ∈ A) (hy' : y' ∈ A)
    (hxy : x < y) (hxy' : x' < y')
    (heq : x + y = x' + y' ∨ y + x' = y' + x) : x = x' ∧ y = y' := by
  rcases heq with hs | hd
  · rcases hA x hx y hy x' hx' y' hy' hs with h | h
    · exact h
    · omega
  · rcases hA y hy x' hx' y' hy' x hx hd with h | h
    · exact ⟨h.2.symm, h.1⟩
    · omega

/-- Integer decreasing-kernel mass is the sum of exact prefix occupancies. -/
theorem integer_kernel_prefix_identity (S : Finset ℕ) (H : ℕ) :
    (∑ t ∈ S, (H - t)) =
      ∑ j ∈ Finset.range H, (S.filter (fun t => t ≤ j)).card := by
  simp_rw [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t ht
  have hf : (Finset.range H).filter (fun j => t ≤ j) = Finset.Ico t H := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
    omega
  rw [← Finset.sum_filter, hf]
  simp

/-- Selecting at most h allowed labels pays the same prefix capacity, including all holes. -/
theorem selected_integer_kernel_bound (S U : Finset ℕ) (H h : ℕ)
    (hSU : S ⊆ U) (hcard : S.card ≤ h) :
    (∑ t ∈ S, (H - t)) ≤
      ∑ j ∈ Finset.range H, min h ((U.filter (fun t => t ≤ j)).card) := by
  rw [integer_kernel_prefix_identity S H]
  apply Finset.sum_le_sum
  intro j hj
  apply le_min
  · exact (Finset.card_le_card (by intro t ht; exact (Finset.mem_filter.mp ht).1)).trans hcard
  · apply Finset.card_le_card
    intro t ht
    obtain ⟨htS, htj⟩ := Finset.mem_filter.mp ht
    exact Finset.mem_filter.mpr ⟨hSU htS, htj⟩

/-- A physical lower bound on component diameter pays its squared reciprocal cost. -/
theorem priced_component_far_bound (K : Finset ι) (κ Q w A : ι → ℝ) (D L E : ℝ)
    (hD : 0 < D) (hL : 0 < L) (hE : 0 ≤ E)
    (hκ : ∀ k ∈ K, 0 ≤ κ k) (hw : ∀ k ∈ K, 0 ≤ w k)
    (hQ : ∀ k ∈ K, Q k ≤ E * w k)
    (hA : ∀ k ∈ K, D * L ≤ A k) :
    (∑ k ∈ K, κ k * Q k / (A k) ^ 2) ≤
      E / (D * L) ^ 2 * (∑ k ∈ K, κ k * w k) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro k hk
  have hDL : 0 < D * L := mul_pos hD hL
  have hAk : 0 < A k := lt_of_lt_of_le hDL (hA k hk)
  have hsq : (D * L)^2 ≤ (A k)^2 :=
    (sq_le_sq₀ hDL.le hAk.le).mpr (hA k hk)
  calc
    κ k * Q k / (A k)^2 ≤ κ k * (E * w k) / (A k)^2 :=
      div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left (hQ k hk) (hκ k hk))
        (sq_nonneg (A k))
    _ ≤ κ k * (E * w k) / (D * L)^2 :=
      div_le_div_of_nonneg_left (mul_nonneg (hκ k hk) (mul_nonneg hE (hw k hk)))
        (sq_pos_of_pos hDL) hsq
    _ = E / (D * L)^2 * (κ k * w k) := by ring

/-- One deleted allowed label removes exactly the unsaturated prefix capacities above it. -/
theorem integer_capacity_deletion_identity (U : Finset ℕ) (H h c : ℕ)
    (hc : c ∈ U) :
    (∑ j ∈ Finset.range H, min h ((U.filter (fun t => t ≤ j)).card)) =
      (∑ j ∈ Finset.range H, min h (((U.erase c).filter (fun t => t ≤ j)).card)) +
      ((Finset.range H).filter (fun j =>
        c ≤ j ∧ (U.filter (fun t => t ≤ j)).card ≤ h)).card := by
  rw [Finset.card_eq_sum_ones, Finset.sum_filter, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.filter_erase]
  by_cases hcj : c ≤ j
  · have hm : c ∈ U.filter (fun t => t ≤ j) := Finset.mem_filter.mpr ⟨hc, hcj⟩
    have he := Finset.card_erase_add_one hm
    simp only [hcj, true_and]
    split_ifs <;> omega
  · have hm : c ∉ U.filter (fun t => t ≤ j) := by simp [hcj]
    rw [Finset.erase_eq_of_notMem hm]
    simp [hcj]

/-- A fixed shift recovers each old/future rectangle from its upper old/future pair. -/
theorem mixed_shift_fiber_card_bound {S : Set ℕ} (hS : Erdos1191Q1.Sidon S)
    (A F : Finset ℕ) (e : ℕ)
    (hA : ∀ x ∈ A, x ∈ S) (hF : ∀ x ∈ F, x ∈ S)
    (hsep : ∀ x ∈ A, ∀ z ∈ F, x < z) :
    ((((A.product A).product (F.product F)).filter
      (fun q => q.1.1 < q.1.2 ∧ q.2.1 < q.2.2 ∧
        q.1.2 + q.2.1 = q.1.1 + q.2.2 + e)).card) ≤ A.card * F.card := by
  calc
    _ ≤ (A.product F).card := by
      apply Finset.card_le_card_of_injOn
        (fun q : (ℕ × ℕ) × (ℕ × ℕ) => (q.1.2, q.2.2))
      · rintro ⟨⟨x,y⟩,⟨i,r⟩⟩ hq
        have hm := Finset.mem_filter.mp hq
        have hp := Finset.mem_product.mp hm.1
        have ha := Finset.mem_product.mp hp.1
        have hf := Finset.mem_product.mp hp.2
        exact Finset.mem_product.mpr ⟨ha.2, hf.2⟩
      · rintro ⟨⟨x,y⟩,⟨i,r⟩⟩ hq ⟨⟨x',y'⟩,⟨i',r'⟩⟩ hq' heq
        obtain ⟨hq,hxy,hir,he⟩ := Finset.mem_filter.mp hq
        obtain ⟨hq',hxy',hir',he'⟩ := Finset.mem_filter.mp hq'
        obtain ⟨ha,hf⟩ := Finset.mem_product.mp hq
        obtain ⟨ha',hf'⟩ := Finset.mem_product.mp hq'
        obtain ⟨hx,hy⟩ := Finset.mem_product.mp ha
        obtain ⟨hi,hr⟩ := Finset.mem_product.mp hf
        obtain ⟨hx',hy'⟩ := Finset.mem_product.mp ha'
        obtain ⟨hi',hr'⟩ := Finset.mem_product.mp hf'
        have hy_eq : y = y' := congrArg Prod.fst heq
        have hr_eq : r = r' := congrArg Prod.snd heq
        change y + i = x + r + e at he
        change y' + i' = x' + r' + e at he'
        have hsum : i + x' = i' + x := by omega
        rcases hS i (hF i hi) x' (hA x' hx') i' (hF i' hi') x (hA x hx) hsum with h | h
        · simp [hy_eq, hr_eq, h.1, h.2]
        · have hi_gt := hsep x hx i hi
          omega
    _ = A.card * F.card := Finset.card_product A F

/-- Exact weighted bank of distinct ordered source labels, with the diagonal removed. -/
theorem source_pair_product_identity (D : Finset ℕ) (w : ℕ → ℝ) :
    2 * (∑ d ∈ D, ∑ e ∈ D, if e < d then w d * w e else 0) +
      (∑ d ∈ D, (w d)^2) = (∑ d ∈ D, w d)^2 := by
  have hsplit (d e : ℕ) : w d * w e =
      (if e < d then w d * w e else 0) +
      (if d < e then w d * w e else 0) +
      (if d = e then (w d)^2 else 0) := by
    rcases lt_trichotomy d e with hd | hd | hd
    · have hne : d ≠ e := by omega
      have hnot : ¬ e < d := by omega
      simp [hd, hne, hnot]
    · subst e
      simp [pow_two]
    · have hne : d ≠ e := by omega
      have hnot : ¬ d < e := by omega
      simp [hd, hne, hnot]
  have hswap :
      (∑ d ∈ D, ∑ e ∈ D, if d < e then w d * w e else 0) =
      (∑ d ∈ D, ∑ e ∈ D, if e < d then w d * w e else 0) := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro d hd
    apply Finset.sum_congr rfl
    intro e he
    split_ifs <;> ring
  have hdiag :
      (∑ d ∈ D, ∑ e ∈ D, if d = e then (w d)^2 else 0) =
      ∑ d ∈ D, (w d)^2 := by
    apply Finset.sum_congr rfl
    intro d hd
    simp [hd]
  have ht : (∑ d ∈ D, w d)^2 =
      ∑ d ∈ D, ∑ e ∈ D,
        ((if e < d then w d * w e else 0) +
        (if d < e then w d * w e else 0) +
        (if d = e then (w d)^2 else 0)) := by
    rw [pow_two, Finset.sum_mul_sum]
    apply Finset.sum_congr rfl
    intro d hd
    apply Finset.sum_congr rfl
    intro e he
    exact hsplit d e
  simp_rw [Finset.sum_add_distrib] at ht
  rw [hswap, hdiag] at ht
  nlinarith only [ht]

/-- Consecutive mixed-shift edges conserve old span minus future span. -/
theorem mixed_shift_chain_balance (n : ℕ) (A F : ℕ → ℝ) (e : ℝ)
    (h : ∀ j < n, A j - A (j+1) = e + F j - F (j+1)) :
    A 0 - A n = (n : ℝ) * e + F 0 - F n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hi := ih (fun j hj => h j (by omega))
    have hl := h n (by omega)
    simp only [Nat.cast_add, Nat.cast_one] at ⊢
    nlinarith only [hi, hl]

/-- Actual Sidon recovery prevents two edges in a fixed source row from sharing either source endpoint. -/
theorem source_row_endpoint_recovery
    (S : Set ℕ) (hS : Erdos1191Q1.Sidon S)
    (K w z r w' z' r' : ℕ)
    (hw : w ∈ S) (hz : z ∈ S) (hr : r ∈ S)
    (hw' : w' ∈ S) (hz' : z' ∈ S) (hr' : r' ∈ S)
    (hzr' : z < r') (hwr : w < r)
    (h : K + w = z + r) (h' : K + w' = z' + r')
    (hshare : w = w' ∨ z = z') :
    w = w' ∧ z = z' ∧ r = r' := by
  rcases hshare with he | he
  · have hs : z + r = z' + r' := by omega
    rcases hS z hz r hr z' hz' r' hr' hs with hh | hh
    · exact ⟨he, hh.1, hh.2⟩
    · omega
  · have hs : w + r' = w' + r := by omega
    rcases hS w hw r' hr' w' hw' r hr hs with hh | hh
    · exact ⟨hh.1, he, hh.2.symm⟩
    · omega

/-- The common joint bin capacity dominates a sum of identical per-row Sidon window capacities. -/
theorem row_window_capacity_dominated (J rho m : ℝ)
    (hrho : 1 ≤ rho) (hm : 1 ≤ m)
    (hJ : 2 * J ≤ rho * (rho + 1)) :
    min J (m * (m - 1) / 2) ≤ (m - 1) * rho := by
  by_cases hmr : m ≤ rho + 1
  · apply le_trans (min_le_right _ _)
    have hprod : 0 ≤ (m - 1) * (2 * rho - m) :=
      mul_nonneg (by linarith) (by linarith)
    nlinarith only [hprod]
  · apply le_trans (min_le_left _ _)
    have hprod : 0 ≤ rho * (2 * m - rho - 3) :=
      mul_nonneg (by linarith) (by linarith)
    nlinarith only [hJ, hprod]

/-- A fixed birth allowance minus one smaller interval price is nondecreasing in the cut. -/
theorem interval_deficit_mono (w p : ℝ) (hp : 0 ≤ p) (hpw : p ≤ w)
    (c i b b' : ℕ) (hbb' : b ≤ b') :
    (if c < b then w else 0) - (if c < b ∧ b < i then p else 0) ≤
    (if c < b' then w else 0) - (if c < b' ∧ b' < i then p else 0) := by
  have hw : 0 ≤ w := le_trans hp hpw
  split_ifs <;> (first | omega | linarith)

end Erdos1191Q1.U4FProfile
