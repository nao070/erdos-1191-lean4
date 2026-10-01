# Failure Modes and Stop Rules

## Failure mode 1 — Residual renaming

Symptom: a quantity is decomposed, renamed, or moved between channels, and the report calls the new notation a smaller bottleneck although no bound improves.

Control: every cycle must state the old bound, new bound, and changed proof obligation. If only notation changed, grade `G0` and do not create a new Wave.

## Failure mode 2 — Vacuity/target equivalence

Symptom: a universal theorem is quantified over counterexample branches; if the target conjecture is true there are no such branches, so the theorem is vacuous. Combined with a conditional lower bound, it is equivalent to the target.

Control: mandatory quantifier-and-reduction audit before “next lemma” language.

## Failure mode 3 — Lower-bound comparison masquerading as repayment

Symptom: resource `Phi>=c/log m` and debt `Y>=c'/log m` are both lower bounds, then the proof informally treats one as paying the other.

Control: require an atomwise injection, dual certificate, or signed inequality with explicit ownership. Lower bound vs lower bound is not payment.

## Failure mode 4 — Floor double counting

Symptom: a new allocation uses atoms already consumed by `K^len`, `K^mix`, a rearrangement floor, or another certificate.

Control: every atom gets a unique owner ID. The sum of owned coefficients must be checked against the literal coefficient exactly.

## Failure mode 5 — Borrowing beyond the horizon

Symptom: a finite proof through terminal scale `M` uses capacity born at `2M` or later without an exact terminal potential.

Control: all finite-horizon inequalities must close with an explicit boundary term. Future capacity is illegal unless the identity transports it back with a proved sign.

## Failure mode 6 — Finite-to-infinite leap

Symptom: many finite compatible rulers, a large beam search, or no finite counterexample is used to infer an infinite branch or an asymptotic theorem.

Control: require compactness/Kőnig-tree compatibility with uniform bounds, or an explicit infinite construction. Record prefix compatibility, not just isolated fixtures.

## Failure mode 7 — Self-oracle verification

Symptom: the same Python formulas produce both certificate and expected values.

Control: one literal slow oracle, one optimized implementation, hand-derived microcases, randomized mutation tests, and exact rational checks.

## Failure mode 8 — Release engineering dominates research

Symptom: each exploratory edit replays all historical certificates and doubles acceptance time.

Control: FAST/FOCUSED/FORMAL/RELEASE tiers. Full historical replay only at a genuine theorem milestone.

## Failure mode 9 — Stale entrypoint drift

Symptom: top-level prompt describes Wave 12 while canonical appendices contain Wave 13–15 corrections.

Control: one generated `CURRENT_STATE.json` and one `UPDATED_START_HERE.md`; CI checks that all entrypoints name the same current claim graph.

## Failure mode 10 — Source false positives

Symptom: “Sidon set” results from harmonic analysis, compact groups, spectral theory, or unrelated finite-design problems are treated as additive-integer density literature.

Control: query with `B_2`, additive number theory, Golomb ruler, counting function, difference uniqueness, `sqrt(n/log n)`, or the exact formula. Verify theorem text.

## Failure mode 11 — Novelty from search absence

Symptom: no hit in a finite search is reported as “no prior theorem exists.”

Control: label `LITERATURE_QUALIFIED_NULL`, list inaccessible databases, and request expert/citation-chain review.

## Failure mode 12 — Progress-pressure bias

Symptom: each agent cycle must emit a positive result, so a reformulation is promoted to “progress.”

Control: allow legitimate outputs `NO_G2_PROGRESS`, `ROUTE_CLOSED_BY_COUNTEREXAMPLE`, and `STOPPED_FOR_EXTERNAL_REVIEW`.

# Stop rules

1. **No new Wave for G0.**
2. **Two-cycle rule:** after two consecutive cycles on one route without a proved order improvement, strict logical weakening, or proof-obligation closure, stop that route.
3. **Infrastructure budget:** during exploration, no more than roughly one quarter of compute/time should be spent on full historical verification. Release verification is exempt at a genuine milestone.
4. **Target-equivalence rule:** if a proposed lemma is equivalent to Q1/Q2, label it target-equivalent and do not describe it as a near-complete step.
5. **Manifest rule:** never fix a red manifest by simply hashing the current tree before claim reconciliation.
6. **Wave 15 rule:** no use as a theorem dependency until checker/test/certificate or Lean proof exists.
7. **Public-post rule:** no no-go theorem is posted until its exact quantifiers, proof, and novelty have independent review.
8. **Resolution rule:** no solved/prize-ready language without the full gate in the master prompt.
