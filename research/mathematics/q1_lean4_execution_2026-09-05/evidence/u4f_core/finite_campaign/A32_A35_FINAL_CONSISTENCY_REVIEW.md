# A32-A35 final independent consistency review

Date: 2026-09-09. Status: PASS; no substantive correction requested.

This bounded readback compares only the four new saved mathematical
sections with the existing independent reviews, plus the updated frontier
and continuation-09 formal scope. It performs no new history generation,
finite experiment, original recordbank enumeration, global audit or Lean
rebuild. The companion JSON manifest contains all evidence bindings.

## Fixed final source

WORKING_PROOF.md whole SHA-256: ba1228dedc4a8ec495cfcea6047ccbb4a9b9f2226cb3b82ff5cc93d5af357a21.

| Section | Exact section SHA-256 |
|:---|:---|
|A32|2626ccd429dc227d0483ac5564795f4464547dbfefc83259f8fcfa6e87fb067a|
|A33|870cd46b884aad8d649d570e06e72b2b2f1c3f12a8d817ebbb9890745c51dab8|
|A34|ea002cb45c275ed43eb40f6cd278d86eb8d880ec3a8597d703ebfcb4a90c5f7a|
|A35|586f69cbb33eda0599e77a20176c7cd4a93f89d628e0db8b4a95eb9f289c6c00|

Section hashes include each heading and all bytes through the next
level-two heading boundary. The source was rechecked before this note
was saved; only files in the owned finite_campaign directory were written.

## Mathematical consistency

- A32 retains the source bank on b-1 points while enlarging only the
  forbidden bank to b past points. The eight exact chains, four increments,
  genuine coefficients and the two R=0 counterexamples match the evidence.
  No general deficit monotonicity is inferred.
- A33 pays far components, including the common price tail beyond T.
  The finite Abel terminal term, constant 1/(sqrt(24) log 2) for p=2,
  near-rank range and remaining original large-gap near norm match the
  independent hand proof. The reduction is not the full frozen theorem.
- A34 uses sequential ranks for same-birth deletions. Both horizon
  indices remain intact. The individual full-price condition and the
  simultaneous J_b condition retain T>=J_b before using the cap at J_b.
  The near-class conclusion and absence of a cross-cut budget are correct.
- A35 preserves -binom(T-b,2) alpha_(M+1), and the stronger denominator
  8(b+2)^2(b+1)^2. Its saved terminal-strip constant is valid: for
  B=max(3,ceil(delta T)), the decreasing integral gives
  sum_(b=B)^infinity 1/b^2 <= 1/(B-1). Since B-1>=B/2 and B>=delta T,
  T/[sqrt(8)(B-1)] <= 1/[sqrt(2) delta]. The nonempty-range condition
  handles arbitrary delta>0. The exact ceiling support, omitted empty b2
  core and O(log log T) upper majorant have the proper logical scope.

The frontier correctly leaves the common actual mixed-pair/cut measure,
short-horizon strip, uniform CoreUniform and original Q1 unresolved.

## Lean-09 readback only

LEAN_VERIFICATION_09.json SHA-256: 3dc23654cb533a0b2ee16e5cb0e83a4174a9f4b40227ff69776451f9f44ea675.

All eight listed file hashes match the current local files. The stored
compile81542 and audit74200 outcomes are both exit 0. The verification
lists 27 supporting declarations, with exactly one new declaration:
Erdos1191Q1.U4FProfile.priced_component_far_bound. Its displayed type
and source prove a generic finite denominator comparison from positive
D,L, nonnegative E,kappa,w, Q<=E*w and D*L<=A. This supports the
far-denominator step only. Its audit lists propext, Classical.choice
and Quot.sound; no custom axiom appears in that displayed audit.

The full actual Sidon/component instantiation, A33 Abel/integral and
uniform subclass theorem, A34 penalty/cap results, A35 finite-profile
theorem, frozen K and literal Q1 are not certified by this lemma.
The saved formal-scope paragraph states these limits correctly. No new
build or global declaration audit was run, and no process remains active.
