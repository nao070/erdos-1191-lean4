# Route C: C123 exact ordered-permutation full-phase dual

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite coefficient narrowing; `C058` remains open

## 1. Frozen scope

This certificate concerns one fixed 16-mark Golomb ruler,

`(0,22,60,83,154,284,494,513,575,620,711,777,880,989,1100,1169)`,

at `k=2`, `C=2`, `rho=9/16`, in the current independent epoch-block,
zero-row-sum PSD cone and owner convention.  Its old four gaps

`(71,130,210,19)`

and new eight gaps

`(62,45,91,66,103,109,111,69)`

are permutations of the corresponding C120 multisets.  The scalar C119
concentration increment is therefore unchanged:

`Delta V=-443620417/1928247678`.

This is a finite same-multiset stress row.  It is not an arbitrary-rank
statement, a larger-cone no-go, or an eventual critical infinite history.

## 2. Complete-phase exact replay

The adaptive phase used by the frozen model is

`297/4 <= t <= 297/2`.

It splits into 140 exact event chambers.  The canonical source stores one
rational dual for each of the two epoch blocks on every chamber, giving

- 280 epoch duals;
- 86,240 nonnegative rational weights; and
- 560 endpoint positive-definiteness checks.

Every dual objective and demand coefficient is reconstructed with
`fractions.Fraction`.  Both endpoints of every slack matrix pass an exact
fraction-free Bareiss/Sylvester test.  The full `dt/t` integral uses a
rational atanh enclosure with an explicit tail.  No floating-point value is
used in the accepted comparison.

The replay proves that the normalized full-phase upper is strictly below

`301218263143/8263918620000`.

Because `eta_2<0`, `epsilon,A>=0`, `e_2=0`, and `Delta V<0`, compatibility
with this row forces the clean necessary condition

`B < 4753/10000`.

## 3. Exact scalar bank after C121

The independently replayed C121 positive-`Delta V` row gives the clean
necessary condition

`B > 1341/4000`.

Thus the two clean constraints leave the nonempty open interval

`1341/4000 < B < 4753/10000`,

whose exact width is

`2801/20000`.

Accordingly C123 narrows the scalar bank but does not refute every scalar
storage coefficient.  The C121 contradiction-scale normalized upper would
need to be about `0.025625`, while this row's certified fence is about
`0.036450`.

## 4. Load-bearing phase-base caveat

The same-multiset comparison does not keep the numerical phase interval
fixed.  The current model chooses

`T=(a_15-a_8)/8`,

so moving the first new-shell gap changes `a_8`.  C120 uses
`[553/8,553/4]`, while this permutation uses `[297/4,297/2]`.
Therefore the exact result certifies order sensitivity of the presently
specified adaptive-row computation, but it does not yet prove that an
intrinsic order effect survives every representative or every admissible
scale choice.

Before this bank can support a theorem, the nonanticipating C103/C116 phase
selection rule must be frozen, or representative independence of the
factor-two phase average must be proved.  This caveat is part of the claim,
not a later implementation detail.

## 5. Artifacts and hashes

- verifier: `ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_certificate.py`,
  SHA-256
  `b366f13c7b8af1ce68a381924b427bc53f92ece3a4d2e2f82e4fa61278157de8`;
- compact certificate:
  `ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_certificate.json`,
  SHA-256
  `91eb0e02db28909fe1cd49a31a50fe2589089b28521f11e1951b58521db42491`;
- canonical full dual source:
  `ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_source.json`,
  SHA-256
  `85951114431d84b327b976b8ccc914068181f64302b3c308470be9b419a398f5`;
- internal source payload SHA-256
  `2e27fdcb950b3bd5de025b8364edcfcafe93bef33cb8370bc70a893876b071ba`;
- regression test:
  `ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_test.py`,
  SHA-256
  `ab177bc283ad631778228fbb496c77e9a62bb7d82ab95ba6bd8ff49ab1084405`.

The focused replay passes four tests and the CLI self-check rejects ten
arithmetic, provenance, structure, and scope mutations.

## 6. Next C058 gate

The smallest admissible extension is a two-variable rational outer bank using
the bounded chronological suffix coordinate from C124.  The next two
ordered-permutation rows should be exactified before solving that bank.  A
surviving coefficient vector must still pass held-out 32-mark or scalable
critical-compatible histories and acquire one global C103 owner/boundary
ledger.  C058, Q1, Q2, novelty, publication, and prize eligibility remain
unresolved; the global status is `UNRESOLVED_AT_HARD_LIMIT`.
