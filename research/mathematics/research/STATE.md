# Erdős Problem #1191 Q1 — Pre-flight State

Checkpoint date: 2026-09-09 (Asia/Tokyo)  
Original Q1: **UNRESOLVED**  
Research goal status: **ACTIVE**

`ACTIVE` here is the requested research-objective state. The last historical
goal-service observation in `q1_lean4_execution_2026-09-05/evidence/goal12_pause_checkpoint.json`
was `paused`, with cause unknown; it was not a mathematical `blocked` finding.
No new mathematical exploration was started during this checkpoint.

## 1. Git state

Repository root: `/Users/USER/Documents/ChatGPT/mathematics`

| Field | Recorded value |
|---|---|
| branch | `master` |
| commit SHA | **NONE** — unborn branch; `git rev-parse HEAD` fails |
| `git status` header | `## No commits yet on master` |
| tracked/index files | 0 |
| staged files | 0 |
| tracked dirty files | 0 |
| workspace dirty reason | untracked content only |
| untracked files after this four-file checkpoint | `2373` |
| SHA-256 of sorted newline-delimited untracked path list | `56554abdd97d746ff442bef98bf519e808058577b2c6f4f13eeab2f807e6a97b` |

Because the repository has no first commit, every substantive artifact is
untracked. The exact full list is reproducible with
`git ls-files --others --exclude-standard`; the hash above fixes that list
without embedding thousands of paths. Top-level counts are recorded below.

```text
    1 .DS_Store
    4 .scholar_cache
    1 ERDOS1191_Q1_UNRESOLVED_CHECKPOINT_2026-09-05.zip
    1 erdos1191_C058_C116_UNSEALED_HANDOFF_2026-08-31.verification.txt
    1 erdos1191_C058_C116_UNSEALED_HANDOFF_2026-08-31.zip
    1 erdos1191_C058_C116_UNSEALED_HANDOFF_2026-08-31.zip.sha256
    1 erdos1191_CONTINUED_ANTI_EULERIAN_2026-08-28.zip
  380 erdos1191_NEXT_SESSION_HANDOFF_2026-08-28
  393 erdos1191_PROOF_RESET_ORIGINAL_READONLY_2026-08-29
  864 erdos1191_PROOF_RESET_WORK_2026-08-29
    1 erdos1191_WAVE10_LAMINAR_LOG_PRODUCT_HANDOFF_2026-08-29.zip
    1 erdos1191_WAVE11_TRIANGULAR_ABEL_REPAYMENT_HANDOFF_2026-08-29.zip
    1 erdos1191_WAVE12_CUT_RENEWAL_HANDOFF_2026-08-29.zip
    1 erdos1191_WAVE18_DESCENDANT_JUMP_HANDOFF_2026-08-29.zip
    1 erdos1191_WAVE3_GAP_INNOVATION_HANDOFF_2026-08-28.zip
    1 erdos1191_WAVE5_ARITHMETIC_RESET_RENEWAL_HANDOFF_2026-08-28.zip
    1 erdos1191_WAVE6_ARITHMETIC_BAND_RENEWAL_HANDOFF_2026-08-28.zip
    1 erdos1191_WAVE7_COMPLETE_BIRTH_RENEWAL_HANDOFF_2026-08-28.zip
    1 erdos1191_WAVE8_POSITIVE_BIRTH_BUDGET_HANDOFF_2026-08-29.zip
    1 erdos1191_WAVE9_RANK_VARIANCE_CORE_HANDOFF_2026-08-29.zip
  711 q1_lean4_execution_2026-09-05
    4 research
    1 アーカイブ.zip
```

This is not a clean or version-addressable research repository. A filename or
timestamp is therefore not a substitute for a Git revision or content hash.

## 2. Source precedence and recovery checkpoint

Current state precedence:

1. `q1_lean4_execution_2026-09-05/evidence/goal12_pause_checkpoint.json`
2. `q1_lean4_execution_2026-09-05/RESEARCH_STATUS.md`
3. `q1_lean4_execution_2026-09-05/OUTCOME.json`
4. `q1_lean4_execution_2026-09-05/evidence/goal11_reviewed_research.json`
5. current Lean sources and their source-bound evidence under
   `q1_lean4_execution_2026-09-05/lean/`
6. C143 V2 follow-up evidence under
   `erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/`

The root archive `ERDOS1191_Q1_UNRESOLVED_CHECKPOINT_2026-09-05.zip` is intact:
59 members, SHA-256
`0c7fd25b15e0ed2d58335aaf44f86384904e8a1bcffa19e42935997650af5d42`,
and `unzip -t` passes. It is nevertheless an early 2026-09-05 snapshot and omits
the later difference-budget, MomentDemand, collision, and triple-fiber work.
It is not the current recovery checkpoint. Older C139-era ledgers, the 2026-08-29
reset, and the 2026-08-31 unsealed handoff are historical/superseded.

The live authoritative C143 bank was rehashed during this audit:

- path: `/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/runs/pilot_s32_n16_r1/C143_BANK.json`
- bytes: `144369995`
- SHA-256: `d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`

## 3. Original Q1 and completion condition

The frozen statement and exact negation are in `research/PROBLEM_CONTRACT.md`.
In brief, Q1 asserts for every positive infinite Sidon set \(A\) that

\[
\liminf_{x\to\infty}|A\cap[1,x]|\sqrt{\log x/x}=0.
\]

Completion requires either a proof of this literal universal statement or one
actual infinite Sidon counterexample satisfying the exact eventual positive
lower bound, followed by a final Lean theorem, clean pinned build, and complete
semantic/dependency/axiom audit. None exists.

## 4. Evidence classification

### A. Lean-verified supporting results

Current rerun on 2026-09-09:

- `lake build` completed and proceeded through the `&&` verification chain;
- `lake env lean Q1/AxiomAudit.lean` completed successfully;
- `lake env leanchecker Q1.PhysicalLabelEnvelope` returned exit code 0.

The pinned environment is Lean `4.33.0` and mathlib commit
`db584cd6d46c92f209a44c0f1c829460d327499d`. The source scan of the eight
modules behind the historical 54-name scope found no `sorry`, `admit`,
`sorryAx`, target custom axiom, `native_decide`, `Lean.ofReduceBool`, or kernel
skip. The 54-name sources match the saved source hashes; see
`research/LEAN_CLAIM_LEDGER.md`.

Actually verified supporting content includes:

- the original/real/integer formulations and exact negation bridges;
- nonvacuity via the powers-of-three Sidon example;
- direct moment and prescribed two-/three-jump algebra;
- Sidon sum uniqueness versus positive-difference uniqueness;
- finite weighted actual-difference budgets and interval shadow inequalities;
- a finite growing-prefix physical envelope with one copy per numeric physical
  label and an exact used/other/unused/slack partition;
- MomentDemand's finite centered first-moment demand and shared envelope;
- later signed/triple/ranked collision and ordered triple-fiber support modules.

Count warning: 54 is a historical explicit axiom-audit selection through
`PhysicalLabelEnvelope`, not the number of all declarations in those modules
and not the latest total. The current base verification record has 82 selected
declarations after MomentDemand. Seven later, separate scopes add
`16+5+16+2+4+7+6`, giving 138 distinct supporting declarations across eight
saved scopes. There is no single combined-138 fresh replay, no independent
external checker result, and no final Q1 theorem.

### B. Mathematically proved/reviewed in the project, not Lean-verified

The following are recorded as hand proofs with internal independent review;
this is not a claim of external peer review or Lean verification:

- the capped infinite-history / finite-tree reformulation of the negation;
- the all-rank Haar-state classification, correction integral, and cutoff terms
  surrounding the C143 lift;
- the fixed-size positive-window `O(1)` versus full `Omega(log J)` obstruction;
- fixed-cap good-epoch frequency and divergent sums of individual local demand
  lower bounds;
- exact finite physical-envelope allocation duality and its actual-history
  feasible witness;
- exact output-rank commutator identities reducing one reviewed Fourier route to
  the correlated profile `sum_b sqrt(P_b(T))/b`;
- analytic no-go results and explicit finite Sidon counterfamilies listed below.

These items remain supporting mathematics because the uniform all-history
closure implication is absent.

### C. Finite computational or numerical evidence only

| Evidence | What is established | Hard scope limit |
|---|---|---|
| C143 V2 full-pricing replay | 90,600,510 exact root/phase checks; 960 parents, 1,890 children, 961 endpoints; positive margin/integral for `n16-contract-s32-r1` | one frozen 64-mark history; not arbitrary rank/history and not Lean/Q1 |
| C143 weight extension | fixed witnesses remain feasible for `97/100 <= rho <= 1` | same fixture; no enlarged history quantifier |
| saved exact rational scripts | selected Haar, matrix-transport, completed-fiber, retirement, and causal-sign identities/examples | only named finite examples; several are sanity or counterexample checks |
| spectral/bounded searches | exact finite PSD obstructions or no witness in the searched domain | “no witness” is not a theorem outside the bounded search |
| C139/C140 | historical exact finite chambers/fixtures | superseded as current computational checkpoint; never global Q1 evidence |

No finite result in this repository establishes Q1 or its negation.

### D. Provisional / unverified

- `research/future_covariance_rank_localization.md` (inside the execution
  workspace) claims a finite-error localization of the covariance profile to a
  six-distinct core. Its source hash is recorded, but parent independent review
  was not completed, no Lean execution covers it, and the remaining core profile
  is not bounded. Status: **PROVISIONAL**.
- any interpretation of 138 as one combined release audit is unverified and
  rejected by the saved scope metadata.
- the exact original Q1 theorem, a counterexample, and a complete release are
  absent, not merely pending a build.

### E. Rejected / failed approaches

| Rejected claim or route | Evidence-bounded reason | Does not imply |
|---|---|---|
| fixed-size positive-window pasting | captures `O(1)` mass versus `Omega(log J)` full signal and cannot reproduce long-range matrix entries | Q1 is false or every multiscale method fails |
| corrected direct form is PSD on arbitrary vectors | explicit Lean witness gives `-1/18` | actual Haar-state corrected form fails |
| per-relation summable charge gives a finite global budget | number of born relations makes total charge diverge; actual Sidon counterexamples isolate the inference | a fixed-cap theorem is impossible |
| raw pair budget plus coarse demand closes the route | exact bookkeeping leaves the same-order birth cost | signed/geometric refinements cannot work |
| raw causal `O(T^3 H_T^2)` bound | explicit finite actual Sidon family has larger order | an infinite fixed-cap counterexample exists |
| independent-label entropy transfers to actual labels | required correlation transfer is missing | Q1 is false |
| fixed/finitely many coprime moduli close residue route | dilation/lattice loss remains; full adaptive interval is uncovered | all adaptive modulus arguments fail |
| adding a new PSD source removes the old residual | old and new residuals remain additive/nonnegative | the source construction is useless |
| source-clock/output-clock price transfer | an actual six-point collision violates the naive transfer | all clock transport is impossible |

## 5. Current maximum bottleneck

The proposed wording is directionally correct but not literally the remaining
finite bookkeeping problem.

> For each arbitrary fixed-onset, fixed-cap actual Sidon history, prove a
> uniform all-rank same-source capacity/correlation estimate that compares the
> non-summable local demands with one physical difference-label ledger, while
> charging every physical label/pair only once and retaining every boundary,
> cutoff, terminal, overlap, old/cross/unused, and slack term.

The finite one-copy envelope and its accounting are already Lean-verified.
What is missing is a cap-sensitive uniform strict gap or correlated upper bound.
Also, “全履歴で共有される一つの予算” must not mean sharing a single budget
between different histories: one ledger is built for each actual history, and
the theorem/constants must be uniform over all such histories.

This is the high-level principal obstruction supported by the sources, but it
is not the only route-specific open task. The latest reviewed state also lists
the full adaptive-modulus comparison, the joint `Gamma/Psi` capacity inequality,
and the correlated `P_b` covariance profile. Thus it is inaccurate to mark the
quoted sentence as one already isolated, singular lemma. The shortest reviewed
Fourier formulation is a sufficient uniform bound on the actual overlapping
`sum_b sqrt(P_b(T))/b` profile (or an equivalent commutator estimate). The
six-endpoint-core refinement remains provisional.

## 6. Next exact action

Do not start a new proof search. On formal resumption, first independently audit
`q1_lean4_execution_2026-09-05/research/future_covariance_rank_localization.md`
against its cited actual-pair incidence and raw-product bounds. If and only if
that audit passes, freeze the exact six-endpoint core inequality still missing.
Separately, the next formal bridge is to prove that `orderedCard/6` is the
inverse-automorphism-weighted multiset triple-fiber mass before using the later
orbit/energy/source chain.
