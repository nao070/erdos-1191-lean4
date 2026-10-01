# Route C / C127: common-phase ordered candidate audit

## Exact finite statement

C127 places the fixed C125 rational vector

\[
(\epsilon,A,B,C_{\rm rt},e_2)
=\left(\frac1{1000},\frac1{1000},\frac12,\frac1{10},0\right)
\]

against the two stored C126 dual upper certificates on the same completed-shell
phase

\[
T=H_3/8=82,\qquad [T,2T]=[82,164],\qquad \rho=9/16.
\]

For a row with ordered-suffix increment \(\Delta V_{\rm rt}\), the target is

\[
R=\frac{\epsilon-A\eta-B\Delta V-C_{\rm rt}\Delta V_{\rm rt}}3-e_2,
\qquad \eta=\log(82/215),
\qquad \Delta V=-\frac{443620417}{1928247678}.
\]

The verifier encloses \(\log(215/82)\) by the pinned 30-term rational atanh
series from C125.  To avoid any floating-point inference, it subtracts the
target upper endpoint from the normalized dual-objective lower endpoint.

The exact comparisons are

- C120, \(\Delta V_{\rm rt}=-13171/58179\): certified margin
  `normalized_lower - target_upper > 21/500`;
- C123, \(\Delta V_{\rm rt}=51059/581790\): certified margin
  `normalized_lower - target_upper > 7/1000`.

Numerically, only for orientation, the respective target/margin pairs are
approximately `(0.04654489427, 0.04238873076)` and
`(0.03607324642, 0.007343051989)`.  Both exact margins are greater than
`1/10000`.

## Replay and provenance

C127 pins and checks before use:

- C126 verifier SHA-256
  `830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981`;
- C126 compact certificate SHA-256
  `b1a37954b11a807161d85d916a875058d9a4dab51a5dc208468429fe937074cf`;
- C126 compact payload SHA-256
  `03a8df34c95e20b3e24d7d1a91d4de169136a699239c3b5f777a60916a1f1f86`;
- C125 verifier SHA-256
  `1d9f4d8ea7756eb89fa9e8cc5d44e15a6480057df82392afadd30cbcbcb48fe2`.

The delegated C126 replay reconstructs 147 C120 chambers and 135 C123
chambers, totaling 564 epoch duals, 173,712 rational weights, and 1,128 exact
endpoint positive-definiteness checks.

## Exact scope

The positive gaps prove only that these two necessary-side dual upper checks
do not separate the fixed C125 candidate on this fixed common phase.  A dual
upper objective above the target does not supply a primal witness.

C127 does **not** prove any of the following:

- a primal phase witness for either row;
- the local master inequality;
- admissibility of the completed-shell phase rule in the global C103/C058
  construction;
- phase-representative independence;
- ordered-vector storage at arbitrary rank;
- a global owner ledger;
- C058, Q1, Q2, publication novelty, or a prize claim.

The research status therefore remains `UNRESOLVED_AT_HARD_LIMIT`.
