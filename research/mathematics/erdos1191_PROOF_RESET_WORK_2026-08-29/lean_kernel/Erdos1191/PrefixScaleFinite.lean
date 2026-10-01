/-
Copyright (c) 2026 Research Contributor. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: OpenAI Codex
-/
import Mathlib.Algebra.BigOperators.Module

/-!
# Exact finite prefix-scale transport identities

These are algebraic finite-horizon identities. They make no analytic, asymptotic,
or Erdős Problem #1191 claim.
-/

open scoped BigOperators

namespace Erdos1191

/-- The discrete prefix/scale curl identity, equation (1.2) of the route note. -/
theorem prefixScaleCurl {G : Type*} [AddCommGroup G] (C : ℕ → ℕ → G) (j r : ℕ) :
    (C (j + 1) r - C j r) - (C (j + 1) (r + 1) - C j (r + 1)) =
      (C (j + 1) r - C (j + 1) (r + 1)) - (C j r - C j (r + 1)) := by
  abel

/-- The prefix increment from prefix `e` to prefix `e + 1`. -/
def prefixIncrement {G : Type*} [AddCommGroup G] (C : ℕ → ℕ → G)
    (e r : ℕ) : G :=
  C (e + 1) r - C e r

/-- The retained scale band from scale `r` to scale `r + 1`. -/
def scaleBand {G : Type*} [AddCommGroup G] (C : ℕ → ℕ → G)
    (e r : ℕ) : G :=
  C e r - C e (r + 1)

/--
Exact Abel summation on `n` consecutive scales starting at `L`, including the
terminal term. The statement remains valid for the zero scale horizon.
-/
theorem finiteScaleAbel_terminal {R : Type*} [CommRing R] (c delta : ℕ → R)
    (L n : ℕ) :
    (∑ k ∈ Finset.range n, c (L + k) * delta (L + k)) =
      (∑ k ∈ Finset.range n,
        (∑ t ∈ Finset.range (k + 1), c (L + t)) *
          (delta (L + k) - delta (L + k + 1))) +
        (∑ t ∈ Finset.range n, c (L + t)) * delta (L + n) := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.sum_range_succ, Finset.sum_range_succ, ih]
      rw [Finset.sum_range_succ]
      simp only [Nat.add_assoc]
      simp only [add_mul, mul_sub]
      abel

/--
Finite epoch reindexing for a weighted discrete divergence. The first and last
fluxes and every interior change of coefficient are explicit.
-/
theorem finiteEpochFlux_range {R : Type*} [CommRing R] (a flux : ℕ → R) (m : ℕ) :
    (∑ e ∈ Finset.range (m + 1), a e * (flux (e + 1) - flux e)) =
      a m * flux (m + 1) - a 0 * flux 0 +
        ∑ e ∈ Finset.range m, (a e - a (e + 1)) * flux (e + 1) := by
  induction m with
  | zero => simp [mul_sub]
  | succ m ih =>
      rw [Finset.sum_range_succ]
      rw [ih]
      rw [Finset.sum_range_succ]
      simp only [mul_sub, sub_mul]
      abel

/-- The inclusive scale-prefix coefficient through offset `k`. -/
def scalePrefix {R : Type*} [AddCommMonoid R] (c : ℕ → ℕ → R)
    (L e k : ℕ) : R :=
  ∑ t ∈ Finset.range (k + 1), c e (L + t)

/-- Two-dimensional reindexing of a finite epoch divergence, one scale at a time. -/
theorem finiteGridDivergence_range {R : Type*} [CommRing R]
    (a flux : ℕ → ℕ → R) (m n : ℕ) :
    (∑ e ∈ Finset.range (m + 1), ∑ k ∈ Finset.range n,
      a e k * (flux (e + 1) k - flux e k)) =
      ∑ k ∈ Finset.range n, (
        a m k * flux (m + 1) k - a 0 k * flux 0 k +
          ∑ e ∈ Finset.range m, (a e k - a (e + 1) k) * flux (e + 1) k) := by
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro k hk
  exact finiteEpochFlux_range (fun e ↦ a e k) (fun e ↦ flux e k) m

private theorem mul_sum_range {R : Type*} [CommRing R]
    (a : R) (f : ℕ → R) (n : ℕ) :
    a * (∑ k ∈ Finset.range n, f k) = ∑ k ∈ Finset.range n, a * f k := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.sum_range_succ, Finset.sum_range_succ, mul_add, ih]

/--
Exact two-dimensional finite epoch/scale Abel transport. Epochs are the `m + 1`
edges numbered `0, ..., m`; consequently `band 0` and `band (m + 1)` are the
initial and final prefix boundaries. All scale and epoch terminal terms are
displayed, and the statement includes the zero-scale horizon `n = 0`.
-/
theorem finiteEpochScaleAbel_transport {R : Type*} [CommRing R]
    (w : ℕ → R) (c delta band : ℕ → ℕ → R) (L m n : ℕ)
    (curl : ∀ e ∈ Finset.range (m + 1), ∀ k ∈ Finset.range n,
      delta e (L + k) - delta e (L + k + 1) =
        band (e + 1) (L + k) - band e (L + k)) :
    (∑ e ∈ Finset.range (m + 1), w e *
      ∑ k ∈ Finset.range n, c e (L + k) * delta e (L + k)) =
      (∑ k ∈ Finset.range n, (
        w m * scalePrefix c L m k * band (m + 1) (L + k) -
          w 0 * scalePrefix c L 0 k * band 0 (L + k) +
          ∑ e ∈ Finset.range m,
            (w e * scalePrefix c L e k - w (e + 1) * scalePrefix c L (e + 1) k) *
              band (e + 1) (L + k))) +
        ∑ e ∈ Finset.range (m + 1),
          w e * (∑ t ∈ Finset.range n, c e (L + t)) * delta e (L + n) := by
  calc
    _ = ∑ e ∈ Finset.range (m + 1), w e *
        ((∑ k ∈ Finset.range n, scalePrefix c L e k *
          (delta e (L + k) - delta e (L + k + 1))) +
          (∑ t ∈ Finset.range n, c e (L + t)) * delta e (L + n)) := by
      apply Finset.sum_congr rfl
      intro e he
      rw [finiteScaleAbel_terminal (c e) (delta e) L n]
      rfl
    _ = (∑ e ∈ Finset.range (m + 1), ∑ k ∈ Finset.range n,
        (w e * scalePrefix c L e k) *
          (delta e (L + k) - delta e (L + k + 1))) +
        ∑ e ∈ Finset.range (m + 1),
          w e * (∑ t ∈ Finset.range n, c e (L + t)) * delta e (L + n) := by
      simp only [mul_add, Finset.sum_add_distrib, mul_assoc]
      congr 1
      apply Finset.sum_congr rfl
      intro e he
      rw [mul_sum_range]
    _ = (∑ e ∈ Finset.range (m + 1), ∑ k ∈ Finset.range n,
        (w e * scalePrefix c L e k) *
          (band (e + 1) (L + k) - band e (L + k))) +
        ∑ e ∈ Finset.range (m + 1),
          w e * (∑ t ∈ Finset.range n, c e (L + t)) * delta e (L + n) := by
      congr 1
      apply Finset.sum_congr rfl
      intro e he
      apply Finset.sum_congr rfl
      intro k hk
      rw [curl e he k hk]
    _ = _ := by
      rw [finiteGridDivergence_range
        (fun e k ↦ w e * scalePrefix c L e k)
        (fun e k ↦ band e (L + k)) m n]

/--
The transport identity specialized to one prefix/scale potential `C`. This is
equation (2.3), with natural-number indexing shifted so that `scaleBand C 0`
is the initial prefix boundary and `scaleBand C (m + 1)` is the final one.
-/
theorem finiteEpochScaleAbel_transport_fromPotential {R : Type*} [CommRing R]
    (w : ℕ → R) (c C : ℕ → ℕ → R) (L m n : ℕ) :
    (∑ e ∈ Finset.range (m + 1), w e *
      ∑ k ∈ Finset.range n, c e (L + k) * prefixIncrement C e (L + k)) =
      (∑ k ∈ Finset.range n, (
        w m * scalePrefix c L m k * scaleBand C (m + 1) (L + k) -
          w 0 * scalePrefix c L 0 k * scaleBand C 0 (L + k) +
          ∑ e ∈ Finset.range m,
            (w e * scalePrefix c L e k - w (e + 1) * scalePrefix c L (e + 1) k) *
              scaleBand C (e + 1) (L + k))) +
        ∑ e ∈ Finset.range (m + 1),
          w e * (∑ t ∈ Finset.range n, c e (L + t)) *
            prefixIncrement C e (L + n) := by
  apply finiteEpochScaleAbel_transport w c (prefixIncrement C) (scaleBand C) L m n
  intro e he k hk
  simpa [prefixIncrement, scaleBand] using prefixScaleCurl C e (L + k)

end Erdos1191
