/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Erdos1191.PrefixScaleFinite
import Mathlib.Tactic.Ring

/-!
# Exact adjacent epoch-8/epoch-16 ledger

This expands the `m = 1`, `n = 4`, `L = 0` case of the finite C103 transport.
The shared prefix has one net coefficient, and both upper scale-terminal rows
remain explicit.  The statement is finite algebra only: it makes no positivity,
phase-selection, arbitrary-history, C058, or Erdős Problem #1191 claim.
-/

open scoped BigOperators

namespace Erdos1191

/--
The two adjacent edges `A8 → A16` and `A16 → A32` have twelve prefix-band rows
and two upper terminals.  The old final and new initial occurrences at `A16`
are collected into the single coefficient `w8 * S8 - w16 * S16`.
-/
theorem adjacentEpochTwoEdgeFourScaleLedger {R : Type*} [CommRing R]
    (w8 w16 : R) (c8 c16 C8 C16 C32 : ℕ → R) :
    w8 * (∑ s ∈ Finset.range 4, c8 s * (C16 s - C8 s)) +
        w16 * (∑ s ∈ Finset.range 4, c16 s * (C32 s - C16 s)) =
      (∑ s ∈ Finset.range 4,
        (-w8 * (∑ u ∈ Finset.range (s + 1), c8 u)) * (C8 s - C8 (s + 1))) +
      (∑ s ∈ Finset.range 4,
        (w8 * (∑ u ∈ Finset.range (s + 1), c8 u) -
          w16 * (∑ u ∈ Finset.range (s + 1), c16 u)) *
            (C16 s - C16 (s + 1))) +
      (∑ s ∈ Finset.range 4,
        (w16 * (∑ u ∈ Finset.range (s + 1), c16 u)) *
          (C32 s - C32 (s + 1))) +
      w8 * (∑ u ∈ Finset.range 4, c8 u) * (C16 4 - C8 4) +
      w16 * (∑ u ∈ Finset.range 4, c16 u) * (C32 4 - C16 4) := by
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, Nat.zero_add]
  ring

end Erdos1191
