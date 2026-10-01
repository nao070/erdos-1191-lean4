# Proof Obligation DAG

## Target statements

### Q1
For every infinite additive Sidon set `A subset N`,

`liminf_{x->infinity} A(x) * sqrt(log x / x) = 0`.

### Q2
There exists an infinite additive Sidon set `A` and `c>0` such that

`liminf_{x->infinity} A(x) * (log x)^c / sqrt(x) > 0`.

Q1 and Q2 are separate. Resolving one does not automatically resolve the other.

## Foundational equivalence to formalize

### E0 — Critical-cap equivalence

For the increasing enumeration `A={a_1<a_2<...}`, Q1 is equivalent to:

> There is no finite `C` and no infinite Sidon sequence satisfying `a_n <= C n^2 log(2n)` for every sufficiently large `n`.

Status: `HUMAN_PROOF_AUDITED`, not yet Lean-certified in the supplied package.

## Existing Route A nodes

### A1 — finite Abel/coefficient identities
Status: mixed `HUMAN_PROOF_AUDITED + COMPUTATIONAL_FINITE`.

### A2 — Wave 11 triangular length floor
`K_m^len = 2 log m + O(1)` and leading-quarter repayment.
Status: `HUMAN_PROOF_AUDITED + COMPUTATIONAL_FINITE`; fragile constants and `O(1)` should be made explicit in Lean.

### A3 — positive decomposition
`T_m - K_m^len = Y_m + G_m^len + S_m` with nonnegative channels.
Status: `HUMAN_PROOF_AUDITED + COMPUTATIONAL_FINITE`.

### A4 — Wave 12 telescope
`sum_{m in E_J} Y_m = R_4 - R_{2^{J+1}} + sum_{m in E_J} Z_m`.
Status: `HUMAN_PROOF_AUDITED + COMPUTATIONAL_FINITE` through Wave 12.

### A5 — Wave 13 new-birth harmonic floor
`Z_m^nb >= E_m/(8m^2H_m) >= m^2/(384H_m)`.
Under the eventual cap, `Y_m,Z_m >= const_C/log m` on large dyadic epochs.
Status: `HUMAN_PROOF_AUDITED + focused exact tests`; needs Lean.

### A6 — P17/P18 reclassification

`universal P17 <=> Q1 <=> universal P18`.

Status: `HUMAN_PROOF_AUDITED`; this is a reduction, not a solution.

### A7 — Wave 14 rank promotion and legal rebate
A future-rank resource `Phi_m` of harmonic size can be inserted into a literal lower-shell floor without overlapping the particular floor used in that theorem.
Status: `HUMAN_PROOF_AUDITED + focused exact tests`.

### A8 — Wave 15 adjacent-epoch local allocation
Candidate statement: the marginal promotion `Delta_m` has bounded nested reuse and fits in literal next-epoch negative bulk up to a summable error.
Status: `HUMAN_PROOF_PENDING_AUDIT`. No Wave 15 checker/test/certificate was found.

### A9 — terminal horizon closure
Need an exact finite-horizon potential or ownership theorem that absorbs the terminal fan without borrowing from future epochs.
Status: `OPEN`.

### A10 — disjoint premium
Need to prove that the selected next-epoch atoms are extra to, not already consumed by, the existing global/length/rank floor.
Status: `OPEN`.

## Alternative architecture nodes

### C1 — multi-N averaging
Exploit freedom to average across block sizes, not only translations at fixed N.
Status: `OPEN`; suggested by O'Bryant's discussion.

### C2 — reverse martingale / conditional expectation
Identify a monotone or orthogonal multiscale potential behind block conditional expectations.
Status: `OPEN`; suggested by O'Bryant's discussion.

### C3 — entropy/information inequality
Replace or strengthen the optimized one-scale Cauchy energy argument by an entropy inequality that is sensitive to irregular block occupancy.
Status: `OPEN`; suggested by O'Bryant's discussion.

### C4 — inverse theorem for near extremizers
Show that a branch near the critical one-scale constant must have structure incompatible across infinitely many scales.
Status: `OPEN`.

## Q2 construction nodes

### D1 — compatible finite block family
Status: partial constructions exist; finite only.

### D2 — cross-stage Sidon preservation
Status: `OPEN` at the target density.

### D3 — all-scale counting lower bound
Status: `OPEN`; limsup spikes are insufficient.

### D4 — summable deletion/error budget
Status: `OPEN`.

## Dependency graph

- Q1 proof can arise from:
  - E0 + A9 + A10 + established A1–A8; or
  - E0 + one of C1–C4 plus a new contradiction; or
  - a completely new route.
- Universal P17/P18 are not children strictly below Q1; they are target-equivalent nodes.
- A8 alone does not imply A10 or A9.
- A7 lower bounds cannot be compared to A5 lower bounds to infer repayment.
- Q2 requires D1+D2+D3+D4; no finite certificate can replace D2–D4.

## Promotion rule

A node may be called CLOSED only when its exact quantified statement has:

1. an independent human-readable proof;
2. adversarial counterexample search;
3. executable finite checks where applicable;
4. a formal proof for kernel-critical identities;
5. a claim-registry entry with scope and dependencies.
