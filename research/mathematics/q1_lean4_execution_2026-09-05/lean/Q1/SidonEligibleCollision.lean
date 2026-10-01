import Q1.SidonTripleCollision

/-!
# Actual eligible collision: the two newest endpoints are opposite

This module uses the literal old signed-source predicate with cutoff `m`, not
cutoff `n`. Therefore all four source endpoint slots are strictly below `m<n`.
The two actual output endpoints occur once each and on opposite collision sides.
Rank clocks, the exhaustive matching-orbit partition, and Q1 remain external.
-/

namespace Erdos1191Q1.SidonEligibleCollision

open SidonTripleCollision

/-- Strictly earlier source endpoints place the two newest actual endpoints opposite. -/
theorem eligible_endpoints_collision {A : Set ℕ} (hA : Sidon A) {a b c d m n : ℕ}
    (haA : a ∈ A) (hbA : b ∈ A) (hcA : c ∈ A) (hdA : d ∈ A)
    (hmA : m ∈ A) (hnA : n ∈ A) (ha : a < m) (hb : b < m) (hc : c < m)
    (hd : d < m) (hmn : m < n)
    (houtput : ((a : ℤ) - (b : ℤ)) - ((c : ℤ) - (d : ℤ)) =
      (n : ℤ) - (m : ℤ)) :
    (triple a d m).sum = (triple b c n).sum ∧ triple a d m ≠ triple b c n ∧
      Disjoint (triple a d m) (triple b c n) ∧
      (triple a d m).count m = 1 ∧ (triple b c n).count m = 0 ∧
      (triple a d m).count n = 0 ∧ (triple b c n).count n = 1 ∧
      (triple a d m + triple b c n).count m = 1 ∧
      (triple a d m + triple b c n).count n = 1 := by
  obtain ⟨hsum, hne, hdisjoint, hnleft, hnright, hnall⟩ :=
    retired_endpoints_collision hA haA hbA hcA hdA hmA hnA
      (lt_trans ha hmn) (lt_trans hb hmn) (lt_trans hc hmn) (lt_trans hd hmn)
      hmn houtput
  have hmleft : (triple a d m).count m = 1 := by
    simp [triple, Ne.symm (ne_of_lt ha), Ne.symm (ne_of_lt hd)]
  have hmright : (triple b c n).count m = 0 := by
    simp [triple, Ne.symm (ne_of_lt hb), Ne.symm (ne_of_lt hc), ne_of_lt hmn]
  exact ⟨hsum, hne, hdisjoint, hmleft, hmright, hnleft, hnright,
    by simp [hmleft, hmright], hnall⟩

/-- Actual source witnesses below the lower output endpoint yield the eligibility certificate. -/
theorem eligible_sources_yield_collision {A : Set ℕ} (hA : Sidon A)
    {m n : ℕ} {u v : ℤ} (hu : SignedBefore A m u) (hv : SignedBefore A m v)
    (hmA : m ∈ A) (hnA : n ∈ A) (hmn : m < n)
    (houtput : u - v = (n : ℤ) - (m : ℤ)) :
    ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, ∃ d ∈ A,
      u = (a : ℤ) - (b : ℤ) ∧ v = (c : ℤ) - (d : ℤ) ∧
      a < m ∧ b < m ∧ c < m ∧ d < m ∧ a ≠ b ∧ c ≠ d ∧
      (triple a d m).card = 3 ∧ (triple b c n).card = 3 ∧
      (triple a d m).sum = (triple b c n).sum ∧ triple a d m ≠ triple b c n ∧
      Disjoint (triple a d m) (triple b c n) ∧
      (triple a d m).count m = 1 ∧ (triple b c n).count m = 0 ∧
      (triple a d m).count n = 0 ∧ (triple b c n).count n = 1 ∧
      (triple a d m + triple b c n).count m = 1 ∧
      (triple a d m + triple b c n).count n = 1 := by
  obtain ⟨a, haA, b, hbA, ha, hb, hab, hu⟩ := hu
  obtain ⟨c, hcA, d, hdA, hc, hd, hcd, hv⟩ := hv
  have hout : ((a : ℤ) - (b : ℤ)) - ((c : ℤ) - (d : ℤ)) =
      (n : ℤ) - (m : ℤ) := by simpa [hu, hv] using houtput
  have hcollision := eligible_endpoints_collision hA haA hbA hcA hdA hmA hnA
    ha hb hc hd hmn hout
  exact ⟨a, haA, b, hbA, c, hcA, d, hdA, hu, hv, ha, hb, hc, hd, hab, hcd,
    triple_card a d m, triple_card b c n, hcollision⟩

end Erdos1191Q1.SidonEligibleCollision
