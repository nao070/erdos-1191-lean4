import Q1.SidonEligibleCollision

/-!
# Actual ranked Sidon sources and collision eligibility

Indices start at zero. `SignedBeforeRank a r` uses distinct endpoint indices
strictly below `r`; the old prefix through index `b` therefore uses cutoff
`b+1`. For a strictly increasing sequence the rank predicate agrees exactly
with the actual-value cutoff predicate on its range. The final theorem derives
the eligible collision and its source-index maximum from actual witnesses.
It does not prove the exhaustive matching partition, a growth estimate, or Q1.
-/

namespace Erdos1191Q1.SidonRankedCollision

open SidonTripleCollision

/-- A literal nonzero signed label whose distinct endpoint indices precede the cutoff. -/
def SignedBeforeRank (a : ℕ → ℕ) (cutoff : ℕ) (z : ℤ) : Prop :=
  ∃ i j : ℕ, i < cutoff ∧ j < cutoff ∧ i ≠ j ∧ z = (a i : ℤ) - (a j : ℤ)

/-- Strict increase identifies the index cutoff with the actual-value cutoff on the range. -/
theorem signedBeforeRank_iff {a : ℕ → ℕ} (ha : StrictMono a) {r : ℕ} {z : ℤ} :
    SignedBeforeRank a r z ↔ SignedBefore (Set.range a) (a r) z := by
  constructor
  · rintro ⟨i, j, hi, hj, hij, hz⟩
    exact ⟨a i, ⟨i, rfl⟩, a j, ⟨j, rfl⟩, ha hi, ha hj,
      fun h => hij (ha.injective h), hz⟩
  · rintro ⟨x, ⟨i, rfl⟩, y, ⟨j, rfl⟩, hi, hj, hij, hz⟩
    exact ⟨i, j, ha.lt_iff_lt.mp hi, ha.lt_iff_lt.mp hj,
      fun h => hij (congrArg a h), hz⟩

/-- Actual Sidonicity and strict increase make nonzero signed endpoint indices unique. -/
theorem ranked_signed_endpoints_unique {a : ℕ → ℕ} (ha : StrictMono a)
    (hA : Sidon (Set.range a)) {i j p q : ℕ} (hij : i ≠ j)
    (hdiff : (a i : ℤ) - (a j : ℤ) = (a p : ℤ) - (a q : ℤ)) :
    i = p ∧ j = q := by
  have h := signed_difference_endpoints_unique hA
    ⟨i, rfl⟩ ⟨j, rfl⟩ ⟨p, rfl⟩ ⟨q, rfl⟩
    (fun h => hij (ha.injective h)) hdiff
  exact ⟨ha.injective h.1, ha.injective h.2⟩

/-- Old-prefix witnesses and `b<i<r` derive actual eligibility, including its source clock. -/
theorem ranked_eligible_sources_yield_collision {a : ℕ → ℕ} (ha : StrictMono a)
    (hA : Sidon (Set.range a)) {b i r : ℕ} {u v : ℤ}
    (hu : SignedBeforeRank a (b + 1) u) (hv : SignedBeforeRank a (b + 1) v)
    (hbi : b < i) (hir : i < r)
    (houtput : u - v = (a r : ℤ) - (a i : ℤ)) :
    ∃ p q s t : ℕ,
      p ≤ b ∧ q ≤ b ∧ s ≤ b ∧ t ≤ b ∧ p ≠ q ∧ s ≠ t ∧
      u = (a p : ℤ) - (a q : ℤ) ∧ v = (a s : ℤ) - (a t : ℤ) ∧
      max (max p q) (max s t) < i ∧
      (triple (a p) (a t) (a i)).card = 3 ∧
      (triple (a q) (a s) (a r)).card = 3 ∧
      (triple (a p) (a t) (a i)).sum = (triple (a q) (a s) (a r)).sum ∧
      triple (a p) (a t) (a i) ≠ triple (a q) (a s) (a r) ∧
      Disjoint (triple (a p) (a t) (a i)) (triple (a q) (a s) (a r)) ∧
      (triple (a p) (a t) (a i)).count (a i) = 1 ∧
      (triple (a q) (a s) (a r)).count (a i) = 0 ∧
      (triple (a p) (a t) (a i)).count (a r) = 0 ∧
      (triple (a q) (a s) (a r)).count (a r) = 1 ∧
      (triple (a p) (a t) (a i) + triple (a q) (a s) (a r)).count (a i) = 1 ∧
      (triple (a p) (a t) (a i) + triple (a q) (a s) (a r)).count (a r) = 1 := by
  obtain ⟨p, q, hp, hq, hpq, hu⟩ := hu
  obtain ⟨s, t, hs, ht, hst, hv⟩ := hv
  have hpi : p < i := by omega
  have hqi : q < i := by omega
  have hsi : s < i := by omega
  have hti : t < i := by omega
  have hclock : max (max p q) (max s t) < i := by
    simp only [max_lt_iff]
    exact ⟨⟨hpi, hqi⟩, ⟨hsi, hti⟩⟩
  have hout : ((a p : ℤ) - (a q : ℤ)) - ((a s : ℤ) - (a t : ℤ)) =
      (a r : ℤ) - (a i : ℤ) := by simpa [hu, hv] using houtput
  have hcollision := SidonEligibleCollision.eligible_endpoints_collision hA
    ⟨p, rfl⟩ ⟨q, rfl⟩ ⟨s, rfl⟩ ⟨t, rfl⟩ ⟨i, rfl⟩ ⟨r, rfl⟩
    (ha hpi) (ha hqi) (ha hsi) (ha hti) (ha hir) hout
  exact ⟨p, q, s, t, by omega, by omega, by omega, by omega, hpq, hst,
    hu, hv, hclock, triple_card _ _ _, triple_card _ _ _, hcollision⟩

end Erdos1191Q1.SidonRankedCollision
