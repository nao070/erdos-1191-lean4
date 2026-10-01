import Q1.Target
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic

/-!
# Actual finite ordered three-sum fibers of a Sidon set

The endpoint tuples below are literal ordered triples from a finite set. Repeated
endpoints are included. The frozen actual `Erdos1191Q1.Sidon` predicate, without an
assumed fiber bound, gives at most two triples for each first endpoint and hence
at most twice the finite-set cardinality in each three-sum fiber.

The final real normalization divides the ordered count by six. Identifying this
quantity with a sum of inverse multiset automorphism orders is not proved here.
Neither the full signed matching partition nor the final Q1 conclusion is proved.
-/

namespace Erdos1191Q1.SidonTripleFiber

/-- Literal ordered three-sum fiber; no distinctness restriction is imposed on the slots. -/
def orderedFiber (K : Finset ℕ) (s : ℕ) : Finset (ℕ × ℕ × ℕ) :=
  (K.product (K.product K)).filter (fun t ↦ t.1 + t.2.1 + t.2.2 = s)

/-- Membership records precisely the three actual endpoints and their sum. -/
theorem mem_orderedFiber {K : Finset ℕ} {s a b c : ℕ} :
    (a, b, c) ∈ orderedFiber K s ↔ a ∈ K ∧ b ∈ K ∧ c ∈ K ∧ a + b + c = s := by
  simp [orderedFiber, and_assoc]

/-- Fixing the first endpoint leaves at most the two orders of one actual Sidon pair. -/
theorem fixed_first_card_le_two {A : Set ℕ} (hA : Sidon A) {K : Finset ℕ}
    (hK : ∀ a ∈ K, a ∈ A) (s x : ℕ) :
    ((orderedFiber K s).filter (fun t ↦ t.1 = x)).card ≤ 2 := by
  classical
  let F := (orderedFiber K s).filter (fun t ↦ t.1 = x)
  by_cases hF : F.Nonempty
  · obtain ⟨⟨a, b, c⟩, habc⟩ := hF
    obtain ⟨habc, hax⟩ := Finset.mem_filter.mp habc
    obtain ⟨_, hb, hc, hsum⟩ := mem_orderedFiber.mp habc
    have hsub : F ⊆ {(x, b, c), (x, c, b)} := by
      rintro ⟨a', b', c'⟩ hmem
      obtain ⟨hmem, ha'x⟩ := Finset.mem_filter.mp hmem
      change a' = x at ha'x
      obtain ⟨_, hb', hc', hsum'⟩ := mem_orderedFiber.mp hmem
      have hpairsum : b' + c' = b + c := by omega
      rcases hA b' (hK b' hb') c' (hK c' hc') b (hK b hb) c (hK c hc)
          hpairsum with ⟨hbb, hcc⟩ | ⟨hbc, hcb⟩
      · simp [ha'x, hbb, hcc]
      · simp [ha'x, hbc, hcb]
    exact (Finset.card_le_card hsub).trans Finset.card_le_two
  · have hempty : F = ∅ := Finset.not_nonempty_iff_eq_empty.mp hF
    change F.card ≤ 2
    simp [hempty]

/-- Every actual ordered three-sum fiber has cardinality at most twice that of the endpoint set. -/
theorem orderedFiber_card_le {A : Set ℕ} (hA : Sidon A) {K : Finset ℕ}
    (hK : ∀ a ∈ K, a ∈ A) (s : ℕ) : (orderedFiber K s).card ≤ 2 * K.card := by
  apply Finset.card_le_mul_card_image_of_maps_to (f := Prod.fst) (t := K)
  · rintro ⟨a, b, c⟩ hmem
    exact (mem_orderedFiber.mp hmem).1
  · intro x _
    exact fixed_first_card_le_two hA hK s x

/-- Real ordered-fiber mass, defined directly by dividing the literal count by six. -/
noncomputable def normalizedMass (K : Finset ℕ) (s : ℕ) : ℝ :=
  (orderedFiber K s).card / 6

/-- The direct real normalization satisfies the one-third finite-set bound. -/
theorem normalizedMass_le {A : Set ℕ} (hA : Sidon A) {K : Finset ℕ}
    (hK : ∀ a ∈ K, a ∈ A) (s : ℕ) : normalizedMass K s ≤ (K.card : ℝ) / 3 := by
  have hcard : ((orderedFiber K s).card : ℝ) ≤ 2 * (K.card : ℝ) := by
    exact_mod_cast orderedFiber_card_le hA hK s
  dsimp [normalizedMass]
  linarith

end Erdos1191Q1.SidonTripleFiber
