/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Mathlib.Algebra.BigOperators.Module
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Exact finite ownership and change-of-basis identities

These are generic finite algebraic identities. They certify only rearrangement,
fiber ownership, and coordinate bookkeeping before any inequality is applied.
They make no positivity, birth-rule, C058, or Erdős Problem #1191 claim.
-/

open scoped BigOperators

namespace Erdos1191

private theorem mul_finset_sum {R α : Type*} [NonUnitalNonAssocSemiring R]
    (a : R) (f : α → R) (s : Finset α) :
    a * (∑ x ∈ s, f x) = ∑ x ∈ s, a * f x := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert x s hx ih => simp [hx, mul_add, ih]

private theorem finset_sum_mul {R α : Type*} [NonUnitalNonAssocSemiring R]
    (f : α → R) (s : Finset α) (a : R) :
    (∑ x ∈ s, f x) * a = ∑ x ∈ s, f x * a := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert x s hx ih => simp [hx, add_mul, ih]

/--
Interchanging a finite signed primitive sum with a finite net-row sum is an
exact change of basis. The ring-valued incidence coefficients may have either
sign; no absolute value or inequality is used.
-/
theorem finiteSignedPrimitiveToNetRow {R Primitive Row : Type*}
    [CommRing R] [Fintype Primitive] [Fintype Row]
    (coefficient : Primitive → R) (incidence : Primitive → Row → R)
    (test : Row → R) :
    (∑ primitive, coefficient primitive *
      ∑ row, incidence primitive row * test row) =
      ∑ row, (∑ primitive, coefficient primitive * incidence primitive row) * test row := by
  calc
    _ = ∑ primitive, ∑ row,
        coefficient primitive * incidence primitive row * test row := by
      apply Finset.sum_congr rfl
      intro primitive hprimitive
      rw [mul_finset_sum]
      apply Finset.sum_congr rfl
      intro row hrow
      simp only [mul_assoc]
    _ = ∑ row, ∑ primitive,
        coefficient primitive * incidence primitive row * test row := Finset.sum_comm
    _ = _ := by
      apply Finset.sum_congr rfl
      intro row hrow
      rw [finset_sum_mul]

/--
Every element of a finite coordinate type belongs to exactly one fiber of an
owner map, so summing the owner fibers counts every coordinate exactly once.
-/
theorem ownerFiberPartitionSum {M Owner Coordinate : Type*}
    [AddCommMonoid M] [Fintype Owner] [Fintype Coordinate] [DecidableEq Owner]
    (owner : Coordinate → Owner) (value : Coordinate → M) :
    (∑ o, ∑ i ∈ Finset.univ with owner i = o, value i) = ∑ i, value i := by
  exact Finset.sum_fiberwise Finset.univ owner value

/-- The contribution of one coordinate row to the finite quadratic form. -/
def quadraticCoordinateRow {R Coordinate : Type*}
    [CommRing R] [Fintype Coordinate]
    (matrix : Coordinate → Coordinate → R) (q : Coordinate → R)
    (i : Coordinate) : R :=
  q i * ∑ j, matrix i j * q j

/-- The finite row-expanded quadratic form `qᵀ X q`. -/
def finiteQuadraticEnergy {R Coordinate : Type*}
    [CommRing R] [Fintype Coordinate]
    (matrix : Coordinate → Coordinate → R) (q : Coordinate → R) : R :=
  ∑ i, quadraticCoordinateRow matrix q i

/-- The share of the quadratic coordinate rows owned by one owner. -/
def ownerQuadraticShare {R Owner Coordinate : Type*}
    [CommRing R] [Fintype Coordinate] [DecidableEq Owner]
    (owner : Coordinate → Owner) (matrix : Coordinate → Coordinate → R)
    (q : Coordinate → R) (o : Owner) : R :=
  ∑ i ∈ Finset.univ with owner i = o, quadraticCoordinateRow matrix q i

/--
Specializing the owner-fiber partition to coordinate rows proves that the sum
of all owner shares is exactly `qᵀ X q`; every coordinate row occurs once.
-/
theorem ownerQuadraticShares_sum {R Owner Coordinate : Type*}
    [CommRing R] [Fintype Owner] [Fintype Coordinate] [DecidableEq Owner]
    (owner : Coordinate → Owner) (matrix : Coordinate → Coordinate → R)
    (q : Coordinate → R) :
    (∑ o, ownerQuadraticShare owner matrix q o) = finiteQuadraticEnergy matrix q := by
  exact ownerFiberPartitionSum owner (quadraticCoordinateRow matrix q)

/-- The row-expanded quadratic energy is the corresponding finite double sum. -/
theorem finiteQuadraticEnergy_eq_doubleSum {R Coordinate : Type*}
    [CommRing R] [Fintype Coordinate]
    (matrix : Coordinate → Coordinate → R) (q : Coordinate → R) :
    finiteQuadraticEnergy matrix q =
      ∑ i, ∑ j, q i * matrix i j * q j := by
  apply Finset.sum_congr rfl
  intro i hi
  rw [quadraticCoordinateRow, mul_finset_sum]
  apply Finset.sum_congr rfl
  intro j hj
  simp only [mul_assoc]

/-- The exact three-coordinate test vector `q = (1, 0, 0)`. -/
def threeCoordinateOwnerStitchVector : Fin 3 → ℚ :=
  fun i ↦ if i = 0 then 1 else 0

/-- The first local matrix, supported on coordinates zero and one. -/
def threeCoordinateOwnerStitchMatrixLeft : Fin 3 → Fin 3 → ℚ :=
  fun i j ↦
    if i = 0 then
      if j = 0 then 1 else if j = 1 then -1 else 0
    else if i = 1 then
      if j = 0 then -1 else if j = 1 then 1 else 0
    else
      0

/-- The second local matrix, supported on coordinates zero and two. -/
def threeCoordinateOwnerStitchMatrixRight : Fin 3 → Fin 3 → ℚ :=
  fun i j ↦
    if i = 0 then
      if j = 0 then 1 else if j = 2 then -1 else 0
    else if i = 2 then
      if j = 0 then -1 else if j = 2 then 1 else 0
    else
      0

/-- The global matrix is the exact sum of the two local matrices. -/
def threeCoordinateOwnerStitchMatrix : Fin 3 → Fin 3 → ℚ :=
  fun i j ↦
    threeCoordinateOwnerStitchMatrixLeft i j +
      threeCoordinateOwnerStitchMatrixRight i j

/-- A local owner map assigning the shared coordinate to owner zero. -/
def threeCoordinateOwnerStitchLocalLeft : Fin 3 → Fin 2 :=
  fun _ ↦ 0

/-- A local owner map assigning the shared coordinate to owner one. -/
def threeCoordinateOwnerStitchLocalRight : Fin 3 → Fin 2 :=
  fun _ ↦ 1

/-- The first local matrix is symmetric. -/
theorem threeCoordinateOwnerStitchMatrixLeft_symmetric (i j : Fin 3) :
    threeCoordinateOwnerStitchMatrixLeft i j =
      threeCoordinateOwnerStitchMatrixLeft j i := by
  fin_cases i <;> fin_cases j <;>
    norm_num [threeCoordinateOwnerStitchMatrixLeft]

/-- The second local matrix is symmetric. -/
theorem threeCoordinateOwnerStitchMatrixRight_symmetric (i j : Fin 3) :
    threeCoordinateOwnerStitchMatrixRight i j =
      threeCoordinateOwnerStitchMatrixRight j i := by
  have h10 : (1 : Fin 3) ≠ 0 := by decide
  have h12 : (1 : Fin 3) ≠ 2 := by decide
  have h20 : (2 : Fin 3) ≠ 0 := by decide
  fin_cases i <;> fin_cases j <;>
    simp [threeCoordinateOwnerStitchMatrixRight, h10, h12, h20]

/-- Every row of the first local matrix sums to zero. -/
theorem threeCoordinateOwnerStitchMatrixLeft_rowSum (i : Fin 3) :
    (∑ j, threeCoordinateOwnerStitchMatrixLeft i j) = 0 := by
  have h20 : (2 : Fin 3) ≠ 0 := by decide
  have h21 : (2 : Fin 3) ≠ 1 := by decide
  fin_cases i <;>
    simp [threeCoordinateOwnerStitchMatrixLeft, Fin.sum_univ_three, h20, h21]

/-- Every row of the second local matrix sums to zero. -/
theorem threeCoordinateOwnerStitchMatrixRight_rowSum (i : Fin 3) :
    (∑ j, threeCoordinateOwnerStitchMatrixRight i j) = 0 := by
  have h10 : (1 : Fin 3) ≠ 0 := by decide
  have h12 : (1 : Fin 3) ≠ 2 := by decide
  fin_cases i <;>
    simp [threeCoordinateOwnerStitchMatrixRight, Fin.sum_univ_three, h10, h12]

/-- The first local quadratic energy is the square `(q 0 - q 1)^2`. -/
theorem threeCoordinateOwnerStitchMatrixLeft_energy (q : Fin 3 → ℚ) :
    finiteQuadraticEnergy threeCoordinateOwnerStitchMatrixLeft q =
      (q 0 - q 1) ^ 2 := by
  simp [finiteQuadraticEnergy, quadraticCoordinateRow,
    threeCoordinateOwnerStitchMatrixLeft, Fin.sum_univ_three, pow_two]
  ring

/-- The second local quadratic energy is the square `(q 0 - q 2)^2`. -/
theorem threeCoordinateOwnerStitchMatrixRight_energy (q : Fin 3 → ℚ) :
    finiteQuadraticEnergy threeCoordinateOwnerStitchMatrixRight q =
      (q 0 - q 2) ^ 2 := by
  simp [finiteQuadraticEnergy, quadraticCoordinateRow,
    threeCoordinateOwnerStitchMatrixRight, Fin.sum_univ_three, pow_two]
  ring

/-- The first local matrix is positive semidefinite as a quadratic form. -/
theorem threeCoordinateOwnerStitchMatrixLeft_nonnegative (q : Fin 3 → ℚ) :
    0 ≤ finiteQuadraticEnergy threeCoordinateOwnerStitchMatrixLeft q := by
  rw [threeCoordinateOwnerStitchMatrixLeft_energy]
  exact sq_nonneg _

/-- The second local matrix is positive semidefinite as a quadratic form. -/
theorem threeCoordinateOwnerStitchMatrixRight_nonnegative (q : Fin 3 → ℚ) :
    0 ≤ finiteQuadraticEnergy threeCoordinateOwnerStitchMatrixRight q := by
  rw [threeCoordinateOwnerStitchMatrixRight_energy]
  exact sq_nonneg _

/-- Each local matrix has unit energy on the fixed test vector. -/
theorem threeCoordinateOwnerStitchLocalEnergies :
    finiteQuadraticEnergy threeCoordinateOwnerStitchMatrixLeft
        threeCoordinateOwnerStitchVector = 1 ∧
      finiteQuadraticEnergy threeCoordinateOwnerStitchMatrixRight
        threeCoordinateOwnerStitchVector = 1 := by
  constructor
  · rw [threeCoordinateOwnerStitchMatrixLeft_energy]
    norm_num [threeCoordinateOwnerStitchVector]
  · rw [threeCoordinateOwnerStitchMatrixRight_energy]
    have h20 : (2 : Fin 3) ≠ 0 := by decide
    norm_num [threeCoordinateOwnerStitchVector, h20]

/-- The summed matrix has energy two on the fixed test vector. -/
theorem threeCoordinateOwnerStitchEnergy :
    finiteQuadraticEnergy threeCoordinateOwnerStitchMatrix
      threeCoordinateOwnerStitchVector = 2 := by
  simp [finiteQuadraticEnergy, quadraticCoordinateRow,
    threeCoordinateOwnerStitchMatrix, threeCoordinateOwnerStitchMatrixLeft,
    threeCoordinateOwnerStitchMatrixRight, threeCoordinateOwnerStitchVector]
  norm_num

/-- The first local matrix pays owner zero exactly one unit. -/
theorem threeCoordinateOwnerStitchLocalLeftShare :
    ownerQuadraticShare threeCoordinateOwnerStitchLocalLeft
        threeCoordinateOwnerStitchMatrixLeft threeCoordinateOwnerStitchVector 0 = 1 := by
  classical
  simp only [ownerQuadraticShare, threeCoordinateOwnerStitchLocalLeft, Finset.filter_true]
  have hrow (i : Fin 3) :
      quadraticCoordinateRow threeCoordinateOwnerStitchMatrixLeft
          threeCoordinateOwnerStitchVector i =
        if i = 0 then 1 else 0 := by
    by_cases hi : i = 0
    · simp [quadraticCoordinateRow, threeCoordinateOwnerStitchMatrixLeft,
        threeCoordinateOwnerStitchVector, hi]
    · simp [quadraticCoordinateRow, threeCoordinateOwnerStitchMatrixLeft,
        threeCoordinateOwnerStitchVector, hi]
  simp_rw [hrow]
  simp only [Finset.sum_ite_eq', Finset.mem_univ, ↓reduceIte]

/-- The second local matrix pays owner one exactly one unit. -/
theorem threeCoordinateOwnerStitchLocalRightShare :
    ownerQuadraticShare threeCoordinateOwnerStitchLocalRight
        threeCoordinateOwnerStitchMatrixRight threeCoordinateOwnerStitchVector 1 = 1 := by
  classical
  simp only [ownerQuadraticShare, threeCoordinateOwnerStitchLocalRight, Finset.filter_true]
  have hrow (i : Fin 3) :
      quadraticCoordinateRow threeCoordinateOwnerStitchMatrixRight
          threeCoordinateOwnerStitchVector i =
        if i = 0 then 1 else 0 := by
    by_cases hi : i = 0
    · simp [quadraticCoordinateRow, threeCoordinateOwnerStitchMatrixRight,
        threeCoordinateOwnerStitchVector, hi]
    · simp [quadraticCoordinateRow, threeCoordinateOwnerStitchMatrixRight,
        threeCoordinateOwnerStitchVector, hi]
  simp_rw [hrow]
  simp only [Finset.sum_ite_eq', Finset.mem_univ, ↓reduceIte]

/-- Under one global owner map, an owner's share is two or zero according to coordinate zero. -/
theorem threeCoordinateOwnerStitchShare (owner : Fin 3 → Fin 2) (o : Fin 2) :
    ownerQuadraticShare owner threeCoordinateOwnerStitchMatrix
        threeCoordinateOwnerStitchVector o =
      if owner 0 = o then 2 else 0 := by
  classical
  simp only [ownerQuadraticShare]
  have hrow (i : Fin 3) :
      quadraticCoordinateRow threeCoordinateOwnerStitchMatrix
          threeCoordinateOwnerStitchVector i =
        if i = 0 then 2 else 0 := by
    by_cases hi : i = 0
    · norm_num [quadraticCoordinateRow, threeCoordinateOwnerStitchMatrix,
        threeCoordinateOwnerStitchMatrixLeft, threeCoordinateOwnerStitchMatrixRight,
        threeCoordinateOwnerStitchVector, hi]
    · simp [quadraticCoordinateRow, threeCoordinateOwnerStitchMatrix,
        threeCoordinateOwnerStitchMatrixLeft, threeCoordinateOwnerStitchMatrixRight,
        threeCoordinateOwnerStitchVector, hi]
  simp_rw [hrow]
  simp only [Finset.sum_ite_eq', Finset.mem_filter, Finset.mem_univ, true_and]

/--
The two local unit shares cannot be retained by a single global coordinate
owner map: at least one of the two global owner shares is strictly below one.
-/
theorem threeCoordinateTwoOwnerStitchingObstruction (owner : Fin 3 → Fin 2) :
    ownerQuadraticShare owner threeCoordinateOwnerStitchMatrix
        threeCoordinateOwnerStitchVector 0 < 1 ∨
      ownerQuadraticShare owner threeCoordinateOwnerStitchMatrix
        threeCoordinateOwnerStitchVector 1 < 1 := by
  rw [threeCoordinateOwnerStitchShare, threeCoordinateOwnerStitchShare]
  have howner : owner 0 = 0 ∨ owner 0 = 1 := by omega
  rcases howner with h | h
  · right
    simp [h]
  · left
    simp [h]

/-- The finite Fejér adjacent-weight ratio at the positive integer index `m`. -/
def fejerRatio (m : ℕ) : ℚ :=
  (((m : ℚ) - 1) / m) ^ 2

/-- The exact exceptional ratio at `m = 3`. -/
theorem fejerRatio_three : fejerRatio 3 = 4 / 9 := by
  norm_num [fejerRatio, pow_two]

/-- Every finite Fejér ratio from `m = 4` onward is at least `9/16`. -/
theorem fejerRatio_ge_nineSixteenths (m : ℕ) (hm : 4 ≤ m) :
    (9 : ℚ) / 16 ≤ fejerRatio m := by
  have hmQ : (4 : ℚ) ≤ m := by exact_mod_cast hm
  have hmpos : (0 : ℚ) < m := by positivity
  have hden : (0 : ℚ) < (m : ℚ) ^ 2 := pow_pos hmpos 2
  have hleft : (0 : ℚ) ≤ (m : ℚ) - 4 := by linarith
  have hright : (0 : ℚ) ≤ 7 * (m : ℚ) - 4 := by linarith
  have hproduct : (0 : ℚ) ≤ ((m : ℚ) - 4) * (7 * m - 4) :=
    mul_nonneg hleft hright
  rw [fejerRatio, div_pow]
  apply (le_div_iff₀ hden).2
  nlinarith

end Erdos1191
