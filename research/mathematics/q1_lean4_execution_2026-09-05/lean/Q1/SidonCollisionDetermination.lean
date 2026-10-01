import Q1.SidonEligibleCollision

/-!
# Actual Sidon collision determination and finite counting

Fix the newest value `n`. A record is `(((ell,v),y),(u,x))`, representing
`U={u,v,ell}` and `V={x,y,n}`. Its near coordinates `ell,v,y` belong to a
finite set `K`; all four old slots are strictly below `ell<n`. Equal slots
within either multiset are allowed by the definition. Actual Sidonicity
determines the ordered far pair `(u,x)` from the near coordinates, so projection
injects these literal finite records into `K cubed`. No orbit-count formula,
geometric clustering estimate, growth hypothesis, or final Q1 claim is assumed.
-/

namespace Erdos1191Q1.SidonCollisionDetermination

open SidonTripleCollision

/-- Actual Sidonicity makes the ordered far gap forced by these top endpoints nonzero. -/
theorem far_gap_ne_zero {A : Set ℕ} (hA : Sidon A) {n ell v y : ℕ}
    (hn : n ∈ A) (hell : ell ∈ A) (hv : v ∈ A) (hy : y ∈ A)
    (helln : ell < n) (hvn : v < n) :
    (n : ℤ) + (y : ℤ) - (ell : ℤ) - (v : ℤ) ≠ 0 := by
  intro hz
  have hsum : n + y = ell + v := by omega
  rcases hA n hn y hy ell hell v hv hsum with hsame | hcross <;> omega

/-- Two actual equal-three-sum records with the same near endpoints have the same far pair. -/
theorem far_pair_unique {A : Set ℕ} (hA : Sidon A) {n ell v y u x u' x' : ℕ}
    (hn : n ∈ A) (hell : ell ∈ A) (hv : v ∈ A) (hy : y ∈ A)
    (hu : u ∈ A) (hx : x ∈ A) (hu' : u' ∈ A) (hx' : x' ∈ A)
    (helln : ell < n) (hvn : v < n)
    (hsum : ell + u + v = n + x + y) (hsum' : ell + u' + v = n + x' + y) :
    u = u' ∧ x = x' := by
  have hgap := far_gap_ne_zero hA hn hell hv hy helln hvn
  have hux : u ≠ x := by omega
  have hdiff : (u : ℤ) - (x : ℤ) = (u' : ℤ) - (x' : ℤ) := by omega
  exact signed_difference_endpoints_unique hA hu hx hu' hx' hux hdiff

/-- Literal finite endpoint records; repeated old slots are not excluded. -/
noncomputable def collisions (A : Set ℕ) (K : Finset ℕ) (n : ℕ) :
    Finset (((ℕ × ℕ) × ℕ) × (ℕ × ℕ)) := by
  classical
  exact (((K ×ˢ K) ×ˢ K) ×ˢ (Finset.range n ×ˢ Finset.range n)).filter fun T =>
      n ∈ A ∧ T.1.1.1 ∈ A ∧ T.1.1.2 ∈ A ∧ T.1.2 ∈ A ∧
      T.2.1 ∈ A ∧ T.2.2 ∈ A ∧
      T.2.1 < T.1.1.1 ∧ T.1.1.2 < T.1.1.1 ∧
      T.2.2 < T.1.1.1 ∧ T.1.2 < T.1.1.1 ∧ T.1.1.1 < n ∧
      T.1.1.1 + T.2.1 + T.1.1.2 = n + T.2.2 + T.1.2

/-- Membership is exactly the actual set, near-set, order, and endpoint-sum conditions. -/
theorem mem_collisions_iff {A : Set ℕ} {K : Finset ℕ} {n ell v y u x : ℕ} :
    (((ell, v), y), (u, x)) ∈ collisions A K n ↔
      ell ∈ K ∧ v ∈ K ∧ y ∈ K ∧
      n ∈ A ∧ ell ∈ A ∧ v ∈ A ∧ y ∈ A ∧ u ∈ A ∧ x ∈ A ∧
      u < ell ∧ v < ell ∧ x < ell ∧ y < ell ∧ ell < n ∧
      ell + u + v = n + x + y := by
  classical
  simp only [collisions, Finset.mem_filter, Finset.mem_product, Finset.mem_range]
  constructor
  · rintro ⟨⟨⟨⟨hellK, hvK⟩, hyK⟩, huN, hxN⟩,
      hn, hellA, hvA, hyA, huA, hxA, hu, hv, hx, hy, helln, hsum⟩
    exact ⟨hellK, hvK, hyK, hn, hellA, hvA, hyA, huA, hxA,
      hu, hv, hx, hy, helln, hsum⟩
  · rintro ⟨hellK, hvK, hyK, hn, hellA, hvA, hyA, huA, hxA,
      hu, hv, hx, hy, helln, hsum⟩
    exact ⟨⟨⟨⟨hellK, hvK⟩, hyK⟩, lt_trans hu helln, lt_trans hx helln⟩,
      hn, hellA, hvA, hyA, huA, hxA, hu, hv, hx, hy, helln, hsum⟩

/-- A counted actual Sidon record represents disjoint triple multisets, even with repeats. -/
theorem collision_multisets_disjoint {A : Set ℕ} (hA : Sidon A)
    {K : Finset ℕ} {n ell v y u x : ℕ}
    (hT : (((ell, v), y), (u, x)) ∈ collisions A K n) :
    Disjoint (triple u v ell) (triple x y n) := by
  obtain ⟨_, _, _, hn, hellA, hvA, hyA, huA, hxA,
    hu, hv, hx, hy, helln, hsum⟩ := mem_collisions_iff.mp hT
  have hout : ((u : ℤ) - (x : ℤ)) - ((y : ℤ) - (v : ℤ)) =
      (n : ℤ) - (ell : ℤ) := by omega
  have h := SidonEligibleCollision.eligible_endpoints_collision hA
    huA hxA hyA hvA hellA hn hu hx hy hv helln hout
  exact h.2.2.1

/-- Projection to the three near coordinates is injective on the actual finite collisions. -/
theorem near_projection_injective {A : Set ℕ} (hA : Sidon A) (K : Finset ℕ) (n : ℕ) :
    Set.InjOn Prod.fst (collisions A K n : Set (((ℕ × ℕ) × ℕ) × (ℕ × ℕ))) := by
  rintro ⟨⟨⟨ell, v⟩, y⟩, ⟨u, x⟩⟩ hT
    ⟨⟨⟨ell', v'⟩, y'⟩, ⟨u', x'⟩⟩ hT' heq
  change ((ell, v), y) = ((ell', v'), y') at heq
  have hell : ell = ell' := congrArg (fun T => T.1.1) heq
  have hv : v = v' := congrArg (fun T => T.1.2) heq
  have hy : y = y' := congrArg Prod.snd heq
  subst ell'
  subst v'
  subst y'
  obtain ⟨_, _, _, hn, hellA, hvA, hyA, huA, hxA,
    _, hvell, _, _, helln, hsum⟩ := mem_collisions_iff.mp hT
  obtain ⟨_, _, _, _, _, _, _, huA', hxA',
    _, _, _, _, _, hsum'⟩ := mem_collisions_iff.mp hT'
  obtain ⟨rfl, rfl⟩ := far_pair_unique hA hn hellA hvA hyA huA hxA huA' hxA'
    helln (lt_trans hvell helln) hsum hsum'
  rfl

/-- The actual finite collision count is at most the cube of the near-set cardinality. -/
theorem collisions_card_le_cube {A : Set ℕ} (hA : Sidon A) (K : Finset ℕ) (n : ℕ) :
    (collisions A K n).card ≤ K.card ^ 3 := by
  classical
  have hmap : Set.MapsTo Prod.fst
      (collisions A K n : Set (((ℕ × ℕ) × ℕ) × (ℕ × ℕ)))
      (↑((K ×ˢ K) ×ˢ K : Finset ((ℕ × ℕ) × ℕ)) : Set ((ℕ × ℕ) × ℕ)) := by
    intro T hT
    exact (Finset.mem_product.mp (Finset.mem_filter.mp hT).1).1
  have hcard := Finset.card_le_card_of_injOn Prod.fst hmap
    (near_projection_injective hA K n)
  simpa [Finset.card_product, pow_succ, Nat.mul_assoc] using hcard

end Erdos1191Q1.SidonCollisionDetermination
