import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Data.EReal.Basic
import Mathlib.Order.LiminfLimsup
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Data.Finset.Card

/-!
# Frozen statement of Erdős Problem 1191, Q1

This module states the challenge; it does not assert a resolution.
Natural numbers in the set are required to be positive. The count includes both endpoints.
The liminf is taken in the extended reals, to give the ordinary mathematical liminf even
when a real-valued function has infinite lower limit. In particular, divergence to positive
infinity must not become zero through a conditionally complete real supremum convention.
-/

namespace Erdos1191Q1

/-- Membership in the positive integers, with no removal or alteration of the input set. -/
def Positive (A : Set ℕ) : Prop := ∀ a ∈ A, 1 ≤ a

/-- Unique unordered two-summand sums, allowing repeated summands. -/
def Sidon (A : Set ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A, ∀ d ∈ A,
    a + b = c + d → (a = c ∧ b = d) ∨ (a = d ∧ b = c)

/-- The finite set of elements of `A` between 1 and an integer cutoff, inclusive. -/
noncomputable def countingSet (A : Set ℕ) (N : ℕ) : Finset ℕ := by
  classical
  exact (Finset.Icc 1 N).filter (· ∈ A)

/-- Integer counting function. -/
noncomputable def count (A : Set ℕ) (N : ℕ) : ℕ := (countingSet A N).card

/-- Real counting function, defined by the nonnegative natural floor. -/
noncomputable def realCount (A : Set ℕ) (x : ℝ) : ℕ := count A ⌊x⌋₊

/-- The original real-valued normalization, using the natural logarithm. -/
noncomputable def normalized (A : Set ℕ) (x : ℝ) : ℝ :=
  realCount A x * Real.sqrt (Real.log x / x)

/-- Original real-cutoff lower-limit conclusion for one input set. -/
def Original (A : Set ℕ) : Prop :=
  Filter.liminf (fun x : ℝ ↦ (normalized A x : EReal)) Filter.atTop = 0

/-- Integer squared epsilon formulation for one input set. -/
def IntegerSquared (A : Set ℕ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∀ M : ℕ, ∃ N : ℕ,
    max M 2 ≤ N ∧ (count A N : ℝ) ^ 2 * Real.log N < ε * N

/-- Frozen affirmative challenge. There is no declaration here claiming this proposition. -/
def Q1 : Prop := ∀ A : Set ℕ, Positive A → A.Infinite → Sidon A → Original A

/-- Integer form of the same universal challenge, pending the equivalence bridge. -/
def Q1Integer : Prop :=
  ∀ A : Set ℕ, Positive A → A.Infinite → Sidon A → IntegerSquared A

end Erdos1191Q1
