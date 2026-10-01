import Q1.Target
import Mathlib.Data.Multiset.AddSub
import Mathlib.Data.Multiset.UnionInter
import Mathlib.Algebra.BigOperators.Group.Multiset.Basic
import Mathlib.Tactic

/-!
# Actual Sidon triple collisions, with repeated endpoints

The Sidon hypothesis is the frozen `Erdos1191Q1.Sidon` predicate. Equal-sum
three-element multisets sharing a member are equal; distinct ones therefore have
disjoint supports. Actual old signed sources and a new output yield such a
collision, with the newest endpoint counted exactly once. The six-matching orbit
partition and the final Q1 conclusion remain outside this module.
-/

namespace Erdos1191Q1.SidonTripleCollision

/-- A three-slot multiset; equal slot values retain their multiplicities. -/
def triple (a b c : ℕ) : Multiset ℕ := a ::ₘ b ::ₘ {c}

/-- Every triple has cardinality three, even if its endpoint values repeat. -/
theorem triple_card (a b c : ℕ) : (triple a b c).card = 3 := by
  simp [triple]

/-- The multiset sum agrees with the three endpoint slots. -/
theorem triple_sum (a b c : ℕ) : (triple a b c).sum = a + b + c := by
  simp [triple, Nat.add_assoc]

/-- Membership in the triple refers to an actual endpoint in at least one slot. -/
theorem mem_triple (x a b c : ℕ) : x ∈ triple a b c ↔ x = a ∨ x = b ∨ x = c := by
  simp [triple]

/-- The actual Sidon predicate identifies equal-sum two-element multisets. -/
theorem pair_eq_of_sum_eq {A : Set ℕ} (hA : Sidon A) {a b c d : ℕ}
    (ha : a ∈ A) (hb : b ∈ A) (hc : c ∈ A) (hd : d ∈ A)
    (hsum : a + b = c + d) : ({a, b} : Multiset ℕ) = {c, d} := by
  rcases hA a ha b hb c hc d hd hsum with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
  · rfl
  · exact Multiset.pair_comm _ _

/-- Canceling one shared member of equal-sum actual Sidon triples forces equality. -/
theorem triples_eq_of_common_member {A : Set ℕ} (hA : Sidon A)
    {U V : Multiset ℕ} (hUcard : U.card = 3) (hVcard : V.card = 3)
    (hU : ∀ x ∈ U, x ∈ A) (hV : ∀ x ∈ V, x ∈ A) (hsum : U.sum = V.sum)
    {x : ℕ} (hxU : x ∈ U) (hxV : x ∈ V) : U = V := by
  have hUerase : (U.erase x).card = 2 := by
    simpa [hUcard] using Multiset.card_erase_of_mem hxU
  have hVerase : (V.erase x).card = 2 := by
    simpa [hVcard] using Multiset.card_erase_of_mem hxV
  obtain ⟨a, b, hab⟩ := Multiset.card_eq_two.mp hUerase
  obtain ⟨c, d, hcd⟩ := Multiset.card_eq_two.mp hVerase
  have ha : a ∈ A := hU a (Multiset.mem_of_mem_erase (by rw [hab]; simp))
  have hb : b ∈ A := hU b (Multiset.mem_of_mem_erase (by rw [hab]; simp))
  have hc : c ∈ A := hV c (Multiset.mem_of_mem_erase (by rw [hcd]; simp))
  have hd : d ∈ A := hV d (Multiset.mem_of_mem_erase (by rw [hcd]; simp))
  have hpairsum : a + b = c + d := by
    rw [← Multiset.cons_erase hxU, ← Multiset.cons_erase hxV, hab, hcd] at hsum
    simpa using hsum
  have hpairs := pair_eq_of_sum_eq hA ha hb hc hd hpairsum
  rw [← Multiset.cons_erase hxU, ← Multiset.cons_erase hxV, hab, hcd, hpairs]

/-- Distinct equal-sum actual Sidon triples have disjoint supports, with repetitions allowed. -/
theorem distinct_triples_disjoint {A : Set ℕ} (hA : Sidon A)
    {U V : Multiset ℕ} (hUcard : U.card = 3) (hVcard : V.card = 3)
    (hU : ∀ x ∈ U, x ∈ A) (hV : ∀ x ∈ V, x ∈ A)
    (hsum : U.sum = V.sum) (hne : U ≠ V) : Disjoint U V := by
  apply Multiset.disjoint_left.mpr
  intro x hxU hxV
  exact hne (triples_eq_of_common_member hA hUcard hVcard hU hV hsum hxU hxV)

/-- An actual nonzero signed difference with both endpoints strictly before the cutoff. -/
def SignedBefore (A : Set ℕ) (cutoff : ℕ) (z : ℤ) : Prop :=
  ∃ a ∈ A, ∃ b ∈ A, a < cutoff ∧ b < cutoff ∧ a ≠ b ∧ z = (a : ℤ) - (b : ℤ)

/-- The endpoint definition really excludes the zero signed label. -/
theorem signedBefore_ne_zero {A : Set ℕ} {cutoff : ℕ} {z : ℤ}
    (hz : SignedBefore A cutoff z) : z ≠ 0 := by
  obtain ⟨a, _, b, _, _, _, hab, hz⟩ := hz
  omega

/-- Sidonicity makes the ordered endpoints of every nonzero signed difference unique. -/
theorem signed_difference_endpoints_unique {A : Set ℕ} (hA : Sidon A) {a b c d : ℕ}
    (ha : a ∈ A) (hb : b ∈ A) (hc : c ∈ A) (hd : d ∈ A) (hab : a ≠ b)
    (hdiff : (a : ℤ) - (b : ℤ) = (c : ℤ) - (d : ℤ)) : a = c ∧ b = d := by
  have hsum : a + d = c + b := by omega
  rcases hA a ha d hd c hc b hb hsum with hsame | hcross
  · exact ⟨hsame.1, hsame.2.symm⟩
  · exact (hab hcross.1).elim

/-- A positive output using the newest endpoint is not already an old signed label. -/
theorem new_output_not_signedBefore {A : Set ℕ} (hA : Sidon A) {m n : ℕ}
    (hm : m ∈ A) (hn : n ∈ A) (hmn : m < n) :
    ¬ SignedBefore A n ((n : ℤ) - (m : ℤ)) := by
  rintro ⟨a, ha, b, hb, han, _, _, hdiff⟩
  have h := signed_difference_endpoints_unique hA hn hm ha hb (by omega) hdiff
  omega

/-- The source/output equality yields the actual endpoint three-sum equation. -/
theorem endpoint_sum_eq {a b c d m n : ℕ}
    (houtput : ((a : ℤ) - (b : ℤ)) - ((c : ℤ) - (d : ℤ)) =
      (n : ℤ) - (m : ℤ)) : a + d + m = b + c + n := by
  omega

/-- A new positive output orders the two signed source labels strictly. -/
theorem sources_ordered_of_new_output {m n : ℕ} {u v : ℤ} (hmn : m < n)
    (houtput : u - v = (n : ℤ) - (m : ℤ)) : v < u := by
  omega

/-- Strictly old sources put the newest endpoint in just one slot of the right triple. -/
theorem newest_counts {a b c d m n : ℕ} (ha : a < n) (hb : b < n)
    (hc : c < n) (hd : d < n) (hm : m < n) :
    (triple a d m).count n = 0 ∧ (triple b c n).count n = 1 := by
  constructor <;>
    simp [triple, ne_of_lt hc,
      Ne.symm (ne_of_lt ha), Ne.symm (ne_of_lt hb), Ne.symm (ne_of_lt hc),
      Ne.symm (ne_of_lt hd), Ne.symm (ne_of_lt hm)]

/-- Actual retired endpoints give distinct equal-sum triples with disjoint supports. -/
theorem retired_endpoints_collision {A : Set ℕ} (hA : Sidon A) {a b c d m n : ℕ}
    (haA : a ∈ A) (hbA : b ∈ A) (hcA : c ∈ A) (hdA : d ∈ A)
    (hmA : m ∈ A) (hnA : n ∈ A) (ha : a < n) (hb : b < n) (hc : c < n)
    (hd : d < n) (hm : m < n)
    (houtput : ((a : ℤ) - (b : ℤ)) - ((c : ℤ) - (d : ℤ)) =
      (n : ℤ) - (m : ℤ)) :
    (triple a d m).sum = (triple b c n).sum ∧ triple a d m ≠ triple b c n ∧
      Disjoint (triple a d m) (triple b c n) ∧
      (triple a d m).count n = 0 ∧ (triple b c n).count n = 1 ∧
      (triple a d m + triple b c n).count n = 1 := by
  have hsum : (triple a d m).sum = (triple b c n).sum := by
    simpa only [triple_sum] using endpoint_sum_eq houtput
  obtain ⟨hleft, hright⟩ := newest_counts ha hb hc hd hm
  have hne : triple a d m ≠ triple b c n := by
    intro heq
    have hcount := congrArg (Multiset.count n) heq
    omega
  have hU : ∀ x ∈ triple a d m, x ∈ A := by
    intro x hx
    rcases (mem_triple x a d m).mp hx with rfl | rfl | rfl <;> assumption
  have hV : ∀ x ∈ triple b c n, x ∈ A := by
    intro x hx
    rcases (mem_triple x b c n).mp hx with rfl | rfl | rfl <;> assumption
  have hdisjoint := distinct_triples_disjoint hA (triple_card a d m)
    (triple_card b c n) hU hV hsum hne
  exact ⟨hsum, hne, hdisjoint, hleft, hright, by simp [hleft, hright]⟩

/-- Extracting actual old signed-source endpoints proves the retirement collision certificate. -/
theorem retired_sources_yield_collision {A : Set ℕ} (hA : Sidon A) {m n : ℕ} {u v : ℤ}
    (hu : SignedBefore A n u) (hv : SignedBefore A n v)
    (hmA : m ∈ A) (hnA : n ∈ A) (hmn : m < n)
    (houtput : u - v = (n : ℤ) - (m : ℤ)) :
    ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, ∃ d ∈ A,
      u = (a : ℤ) - (b : ℤ) ∧ v = (c : ℤ) - (d : ℤ) ∧
      a < n ∧ b < n ∧ c < n ∧ d < n ∧ a ≠ b ∧ c ≠ d ∧
      (triple a d m).card = 3 ∧ (triple b c n).card = 3 ∧
      (triple a d m).sum = (triple b c n).sum ∧ triple a d m ≠ triple b c n ∧
      Disjoint (triple a d m) (triple b c n) ∧
      (triple a d m).count n = 0 ∧ (triple b c n).count n = 1 ∧
      (triple a d m + triple b c n).count n = 1 := by
  obtain ⟨a, haA, b, hbA, ha, hb, hab, hu⟩ := hu
  obtain ⟨c, hcA, d, hdA, hc, hd, hcd, hv⟩ := hv
  have hout : ((a : ℤ) - (b : ℤ)) - ((c : ℤ) - (d : ℤ)) =
      (n : ℤ) - (m : ℤ) := by simpa [hu, hv] using houtput
  have hcollision := retired_endpoints_collision hA haA hbA hcA hdA hmA hnA
    ha hb hc hd hmn hout
  exact ⟨a, haA, b, hbA, c, hcA, d, hdA, hu, hv, ha, hb, hc, hd, hab, hcd,
    triple_card a d m, triple_card b c n, hcollision⟩

end Erdos1191Q1.SidonTripleCollision
