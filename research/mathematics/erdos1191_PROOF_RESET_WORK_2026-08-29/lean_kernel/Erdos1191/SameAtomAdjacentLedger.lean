/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Erdos1191.AdjacentEpochLedger

/-!
# Same-atom adjacent-epoch ledger

This specializes the frozen fourteen-row adjacent epoch ledger to cumulative
potentials built from one baseline and the same two direct increment atoms.
Both upper terminal rows remain explicit.  The statements are finite algebra
only: they make no positivity, phase-selection, owner-capacity, arbitrary-history,
C058, or Erdős Problem #1191 claim.
-/

open scoped BigOperators

namespace Erdos1191

/-- The epoch-8 cumulative potential is the baseline potential. -/
def sameAtomC8 {R : Type*} (B : ℕ → R) : ℕ → R :=
  B

/-- The epoch-16 cumulative potential adds the epoch-8 direct atom. -/
def sameAtomC16 {R : Type*} [Add R] (B U8 : ℕ → R) : ℕ → R :=
  fun s ↦ B s + U8 s

/-- The epoch-32 cumulative potential adds both direct atoms to the baseline. -/
def sameAtomC32 {R : Type*} [Add R] (B U8 U16 : ℕ → R) : ℕ → R :=
  fun s ↦ B s + U8 s + U16 s

/-- The first prefix increment of the cumulative same-atom potential is exactly `U8`. -/
theorem sameAtomC16_sub_C8 {R : Type*} [CommRing R] (B U8 : ℕ → R) (s : ℕ) :
    sameAtomC16 B U8 s - sameAtomC8 B s = U8 s := by
  simp [sameAtomC8, sameAtomC16]

/-- The second prefix increment of the cumulative same-atom potential is exactly `U16`. -/
theorem sameAtomC32_sub_C16 {R : Type*} [CommRing R] (B U8 U16 : ℕ → R) (s : ℕ) :
    sameAtomC32 B U8 U16 s - sameAtomC16 B U8 s = U16 s := by
  simp [sameAtomC16, sameAtomC32]

/--
The four-scale weighted direct sum for the same two increment atoms expands
into four initial rows, four net shared rows, four final rows, and the two
upper terminal rows.  No terminal is discarded in this identity.
-/
theorem sameAtomAdjacentEpochFourScaleLedger {R : Type*} [CommRing R]
    (w8 w16 : R) (c B U8 U16 : ℕ → R) :
    w8 * (∑ s ∈ Finset.range 4, c s * U8 s) +
        w16 * (∑ s ∈ Finset.range 4, c s * U16 s) =
      (∑ s ∈ Finset.range 4,
        (-w8 * (∑ u ∈ Finset.range (s + 1), c u)) *
          (sameAtomC8 B s - sameAtomC8 B (s + 1))) +
      (∑ s ∈ Finset.range 4,
        (w8 * (∑ u ∈ Finset.range (s + 1), c u) -
          w16 * (∑ u ∈ Finset.range (s + 1), c u)) *
            (sameAtomC16 B U8 s - sameAtomC16 B U8 (s + 1))) +
      (∑ s ∈ Finset.range 4,
        (w16 * (∑ u ∈ Finset.range (s + 1), c u)) *
          (sameAtomC32 B U8 U16 s - sameAtomC32 B U8 U16 (s + 1))) +
      w8 * (∑ u ∈ Finset.range 4, c u) * U8 4 +
      w16 * (∑ u ∈ Finset.range 4, c u) * U16 4 := by
  simpa [sameAtomC8, sameAtomC16, sameAtomC32] using
    adjacentEpochTwoEdgeFourScaleLedger w8 w16 c c
      (sameAtomC8 B) (sameAtomC16 B U8) (sameAtomC32 B U8 U16)

/-- Both upper terminal contributions vanish when both direct terminal atoms vanish. -/
theorem sameAtomUpperTerminals_eq_zero {R : Type*} [CommRing R]
    (w8 w16 : R) (c U8 U16 : ℕ → R) (h8 : U8 4 = 0) (h16 : U16 4 = 0) :
    w8 * (∑ u ∈ Finset.range 4, c u) * U8 4 +
      w16 * (∑ u ∈ Finset.range 4, c u) * U16 4 = 0 := by
  simp [h8, h16]

end Erdos1191
