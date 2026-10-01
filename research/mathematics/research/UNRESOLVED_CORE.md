# Erdős Problem #1191 Q1 — Unresolved Core

Checkpoint date: 2026-09-09 (Asia/Tokyo)  
Status: **Q1 unresolved; research objective ACTIVE; no new route is started here.**

## 1. Dependency graph to the original Q1

```text
Original Q1
  For every positive infinite Sidon A,
  liminf C_A(x) sqrt(log x / x) = 0
  [OPEN; frozen in Lean as Erdos1191Q1.Q1]
                         ↑
  CONTRADICTION TO EVERY FIXED-CAP ACTUAL HISTORY
  For each fixed C and onset m0, arbitrarily long compatible Sidon
  prefixes cannot satisfy a_m <= C m^2 log(2m) at every m >= m0.
  [mathematically reviewed finite-tree equivalence; not Lean-verified]
                         ↑
  UNPROVED GLOBAL CLOSURE / CORE
  On each arbitrary fixed-cap actual history, compare the divergent
  local demand with one same-source all-rank capacity/correlation ledger,
  uniformly in history and horizon, with no duplicated physical charge
  and with all boundary/cutoff/terminal/overlap/slack terms retained.
                         ↑
        ┌────────────────┼──────────────────┐
        │                │                  │
  local demand      finite one-copy    correlated Fourier
  divergence        envelope/ledger    commutator profile P_b
  [reviewed math]    [Lean verified]    [reviewed math]
        │                │                  │
        └────────────────┼──────────────────┘
                         ↑
  Sidon positive-difference uniqueness, shadow moments, local interval
  demand, finite disjoint-block accounting, direct-moment algebra
  [Lean-verified supporting results]
                         ↑
  C143/C139/C140 and exact finite scripts
  [finite computational evidence only; no global quantifier]
```

The arrows at the global-closure level are not present theorems. In particular,
the bottom two levels do not imply the top two merely by summing finite local
inequalities.

## 2. Direct unresolved implications, in dependency order

### U0. Exact target and negation bridge

**Status: Lean-verified.** The original real-cutoff target, integer squared
condition, and exact eventual-lower-bound negation are fixed. This is not an
open implication; it anchors what any endgame must prove.

### U1. Negation to a single fixed-cap actual history, and finite-tree reduction

**Status: mathematically proved/reviewed, not Lean-verified.** A counterexample
to Q1 can be expressed as an increasing infinite Sidon history obeying one
eventual cap `a_m <= C m^2 log(2m)`; König's lemma turns absence of such a history
into a finite obstruction for every fixed `C,m0`. Exact constants/onset and all
intermediate ranks must be retained.

Missing formal implication: connect this reviewed finite-tree bridge to the
literal `Erdos1191Q1.Q1` theorem in Lean.

### U2. Fixed cap to sufficiently many productive epochs

**Status: mathematically proved/reviewed, not Lean-verified.** Saved good-epoch
arguments give logarithmically frequent dyadic epochs and a divergent
reciprocal-index sum. At those epochs, saved carrier/moment arguments give
positive local demand lower bounds of the required nonsummable scale.

This does **not** yet permit addition of the local gains: the same physical
labels and source pairs can participate at several cuts.

### U3. Finite one-copy physical-label accounting

**Status: Lean-verified for its explicit finite hypotheses.** The chain through
`shared_interval_demand_budget`, `growing_prefix_interval_envelope`, and
`actual_blocks_envelope_accounting` bundles contributions with the same numeric
label before taking a maximum and partitions selected/other/unused/slack terms.
For a chosen finite history and disjoint actual blocks, it prevents the basic
duplicate-label charge.

What U3 does not prove:

- a history-uniform bound on the physical envelope;
- a cap-sensitive positive or negative margin;
- infinite-horizon summability;
- that the locally selected improving rows can all be realized against one
  globally useful ledger;
- a contradiction to the cap.

### U4. Global same-source capacity/correlation theorem

**Status: UNPROVED — principal high-level gap.** A sufficient theorem must work
for every one actual fixed-cap history, uniformly over all ranks/horizons, and
must give an inequality strong enough to contradict U2. It must retain exactly
one charge for each physical resource and all initial, birth, owner, cutoff,
terminal, old/cross/unused, overlap, and slack terms.

The C143 follow-up expresses one sufficient Route-C form as a legal certificate
with

\[
0\le R_J=B_J-\sum_k\omega_{k,J}\Phi_k,\qquad B_J=O_C(1),
\]

and simultaneously

\[
\sum_k\omega_{k,J}\Phi_k\ge\varepsilon_C\log J-O_C(1),
\qquad \varepsilon_C>0.
\]

Neither the same-source identity/bound nor the arbitrary-history lower bound is
currently proved in a form that closes Q1.

### U4-F. Latest reviewed Fourier specialization

**Status: reviewed mathematics, closing bound unproved.** The output-rank
commutator reduces the uncontrolled part of one route to an actual correlated
profile

\[
N_T(P)=\sum_{b=2}^{T-1}\frac{\sqrt{P_b(T)}}{b},
\]

where one physical source pair may cover several cuts `b`. The tempting raw
`O(T^3H_T^2)` estimate is analytically false on an explicit finite actual Sidon
family. A sufficient uniform upper bound on `N_T(P)`, or an equivalent exact
cross-scale commutator estimate, remains unproved.

### U4-F-core. Six-endpoint localization

**Status: PROVISIONAL / not independently reviewed / not Lean-verified.** The
latest note claims omitted classes contribute only a uniform finite error and
reduces `N_T(P)` to a six-distinct, logarithmically localized core. It explicitly
does not bound that core. Until its cited incidence estimates are independently
audited, it cannot be used as a proved implication.

Conditional missing statement, only if that audit passes:

\[
\sup_T\sum_b\frac{\sqrt{P_b^{\mathrm{core}}(T)}}{b}<\infty
\]

or another cap-sensitive estimate strong enough to close U4.

### U4-E. Physical-envelope specialization

**Status: exact finite dual reviewed; asymptotic implication unproved.** The
one-copy allocation dual and its explicit actual-block feasible witness are
known. The missing implication is that a fixed-onset cap uniformly excludes
every such witness strongly enough that total demanded improvement exceeds the
baseline margin. Positive finite improvement, by itself, is insufficient.

### U4-R and U4-G. Other reviewed branches

**Status: open alternatives, not cumulative prerequisites.** The latest state
also records:

- a full adaptive integer-modulus comparison beyond fixed/coprime families;
- a genuinely joint capacity inequality for the coherent `Gamma` and `Psi`
  sources, because their residuals remain additive and the full defect cannot
  be paid twice.

These are route-specific alternatives to U4-F/U4-E. Their existence means the
current state must not pretend that one single named covariance lemma is already
the uniquely established bottleneck.

### U5. Global contradiction to Q1

**Status: UNPROVED.** Even a bounded component of U4 must be inserted into one
exact global identity and shown to contradict the divergent lower bound under
the same cap and history. Boundary limits and the passage from every finite
horizon to absence of an infinite capped history must be justified.

### U6. Final formal bridge and release

**Status: UNPROVED / NOT BUILT.** Needed after the mathematical closure:

- formalize any non-Lean U1–U5 dependencies actually used;
- in the current triple-fiber branch, identify `orderedCard/6` with the
  inverse-automorphism-weighted multiset fiber before using later orbit/energy
  statements;
- prove literal `Erdos1191Q1.Q1` or `¬ Erdos1191Q1.Q1`;
- run a clean pinned build, final theorem type check, complete dependency/axiom
  audit, and the required checker review.

## 3. Bottleneck verdict on the proposed wording

The sentence

> 局所的な需要・改善を、全履歴で共有される一つの実際の差ラベル予算へ、重複計上なしで累積移送できるか

is **YES as a high-level description, but NO as a literal claim that the finite
transport/bookkeeping itself is still wholly missing or that this is one unique
route-specific lemma**.

Corrections required by the sources:

1. One budget is not shared between different histories. For each arbitrary
   actual fixed-cap history there is one ledger; the bound and constants must be
   uniform over all histories.
2. The finite one-copy label envelope and accounting are already Lean-verified.
3. The unresolved content is the cap-sensitive, all-rank, same-source **uniform
   separation/correlation estimate** needed to beat that ledger.
4. The latest concrete reviewed Fourier version is the overlapping `P_b`
   profile; the proposed six-endpoint reduction is still provisional.

Therefore the safest shortest logical gap to record is:

> **Prove, for every one fixed-cap actual Sidon history, a history-uniform
> all-rank same-source capacity/correlated-profile bound strong enough to
> contradict the already reviewed divergent local demand, without duplicating
> any physical pair/label or dropping any boundary/slack term.**

## 4. Exact next action after this checkpoint

Remain in recovery mode. The first action on a later research resume is to
independently audit `q1_lean4_execution_2026-09-05/research/future_covariance_rank_localization.md`
against `causal_fourier_rank_commutator.md`, `signed_retirement_fibers.md`, and
the cited incidence bounds. Only after that audit should the exact core-profile
statement be promoted or rejected. No new proof search is part of this
checkpoint.

## 5. Evidence anchors

- `research/PROBLEM_CONTRACT.md`
- `research/STATE.md`
- `research/LEAN_CLAIM_LEDGER.md`
- `q1_lean4_execution_2026-09-05/evidence/goal12_pause_checkpoint.json`
- `q1_lean4_execution_2026-09-05/evidence/goal11_reviewed_research.json`
- `q1_lean4_execution_2026-09-05/research/growing_label_budget.md`
- `q1_lean4_execution_2026-09-05/research/physical_envelope_allocation_dual.md`
- `q1_lean4_execution_2026-09-05/research/causal_fourier_rank_commutator.md`
- `q1_lean4_execution_2026-09-05/research/future_covariance_rank_localization.md`
- `erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/C143_TO_Q1_REPORT.md`
