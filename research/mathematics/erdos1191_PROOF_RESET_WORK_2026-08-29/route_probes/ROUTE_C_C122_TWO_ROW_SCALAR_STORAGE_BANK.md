# Route C: C122 exact two-row scalar storage bank

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite coefficient narrowing; `C058` remains open

## 1. Frozen scope

This bank combines only two fixed 16-mark, `k=2`, `C=2`, `rho=9/16`
complete-phase rows in the current independent epoch-block zero-row-sum PSD
cone:

- the positive-`Delta V` C118/C121 row; and
- the negative-`Delta V` C120 reverse-concentration row.

It assumes one common scalar `B`, `epsilon,A>=0`, and `e_2=0`.  It says
nothing about a larger cross-epoch cone, arbitrary rank, an eventual critical
history, or a vector-valued ordered profile.

## 2. Exact lower constraint from C121

C121 proves a complete-phase normalized dual upper below `-83/2000` on the
C118 row.  Since `eta_2<0` and

`Delta V=3440812085/9234857208>0`,

compatibility forces

`B > 287434930599/860203021250 > 1/3`.

## 3. Exact upper constraint from the C120 full-phase dual

The promoted C120 dual bank has 161 phase chambers, 322 rational epoch duals,
and 644 exact endpoint positive-definiteness checks.  Exact rational atanh
integration gives a normalized upper strictly below `19/250`.

Here

`Delta V=-443620417/1928247678`

and `eta_2<0`.  Thus the right side is at least
`B*abs(Delta V)/3`, so compatibility forces the coarse exact bound

`B < 2892371517/2918555375`.

## 4. The two-row bank does not contradict scalar storage

The resulting necessary interval is

`287434930599/860203021250 < B < 2892371517/2918555375`.

Its exact coarse width is

`13193055646707058533/20084401210083413750 > 0`.

Therefore these two rows do **not** refute every scalar `B`.  To contradict
the C121 lower barrier, a negative-`Delta V` complete-phase normalized upper
would need to be at most

`14168000419188271087/552894826111299052500`

(approximately `0.02562513`), whereas the current exact C120 upper is about
`0.075954`.

## 5. Ordered-permutation diagnostic

A disposable numerical screen kept the same old-gap and new-gap multisets as
C120 while permuting their order.  Eighty Golomb candidates were sampled at
four phase points.  The best sampled candidate had points

`(0,22,60,83,154,284,494,513,575,620,711,777,880,989,1100,1169)`,

sampled normalized dual upper about `0.035514`, and a heuristic implied
`B` upper about `0.46310`.  This is closer to the C121 lower barrier but is
not exact, not a full-phase certificate, and is not registered as a claim.

## 6. Artifacts and next gate

- exact verifier:
  `ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_certificate.py`;
- compact canonical statement:
  `ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_certificate.json`;
- promoted C120 full-phase dual source:
  `ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_source.json`;
- exact replay test:
  `ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_test.py`.

The next executable gate is to exactify the best ordered-permutation rows,
then add bounded ordered profile coordinates if the scalar interval remains
nonempty.  A surviving candidate must still pass 32-mark or scalable-family
stress and acquire one global C103 owner/boundary ledger.  C058, Q1, Q2,
novelty, and prize eligibility remain unresolved; the global status is
`UNRESOLVED_AT_HARD_LIMIT`.

## 7. C123 supersession of the sampled diagnostic

The sampled candidate in section 5 has now been promoted to the exact C123
full-phase certificate.  Its 140 chambers, 280 epoch duals, 86,240 rational
weights, and 560 endpoint positive-definiteness checks replay exactly.  It
forces the clean upper restriction `B<4753/10000`; together with the clean
C121 lower restriction it leaves

`1341/4000 < B < 4753/10000`.

Thus the scalar interval is narrower but still nonempty.  C124 now supplies
the first bounded chronological suffix coordinate for the two-variable outer
bank.  The adaptive phase-base caveat recorded in C123/C124 must be settled
before theorem use.
