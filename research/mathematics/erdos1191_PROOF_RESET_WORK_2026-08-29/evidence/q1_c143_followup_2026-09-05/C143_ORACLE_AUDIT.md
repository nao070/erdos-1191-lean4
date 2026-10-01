# C143 V2 primary-data and independent exact oracle audit

Date: 2026-09-05 JST. Source and bank in Downloads were not changed.

The supplied pilot bank is a complete finite fixture, not a partial parent run. A new independent exact replay checks its entire primal certificate, stored price and margin affines, exact phase partition and integral. The complete full-pricing replay also PASSED with process exit 0 in 213.412660 seconds, checking all 90,600,510 graph-root/phase pairs using exact integer arithmetic. Its durable result and scope are in `c143_full_pricing_replay.full.json`; stdout/progress is in `c143_full_pricing_replay.full.log`.

## Primary files and provenance

Source: `/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2`.
Bank: `runs/pilot_s32_n16_r1/C143_BANK.json`, 144,369,995 bytes.

- Bank SHA256: `d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`.
- Supplied independent oracle SHA256: `3df90c1818a6839a0ebcdebe204a1cfb7b5e38db4405a67fd29d2341b95a8d29`.
- All 79 files in `C143_PACKAGE_SHA256SUMS.json` match their hashes.
- All 28 files in the run's `SOURCE_SHA256.json` match current source files; its canonical hash matches `RUN_CONFIG.json` and the bank's saved run config.
- The bank's canonical payload hash and frozen target identity/history hash are independently verified.
- `checkpoint/results.jsonl` contains exactly 1,890 unique certified children: 743 `CERTIFIED_SUBINTERVAL` and 1,147 `CERTIFIED_FULL`. Each serialized certificate equals the corresponding bank child exactly. There are no failure rows in this supplied V2 result log.
- `checkpoint_endpoints/results.jsonl` contains exactly 961 unique `FULLROOT_ENDPOINT_CERTIFIED` rows; every serialized certificate equals the corresponding bank endpoint exactly.
- Both checkpoint states are exactly `{"pending":[]}`.

The full geometric partition has 960 parents, 1,890 basis children, 961 collapsed endpoints, 196 channels and 19,110 canonical graph roots. Every canonical parent breakpoint, every child interval tiling, every endpoint identity, and the one-to-one integral-record map are independently checked. Two discovery samples (`g000074/pC` and `g000817/pC`) equal their child left endpoint; this is harmless because samples lie in their closed child domain and certification checks the entire interval independently.

## What the lost terminal output does and does not establish

The run directory contains the bank, `RUN_CONFIG.json`, `SOURCE_SHA256.json`, and the two state/result pairs. It contains no `ORACLE_full-pricing.log`, `SUMMARY.json`, or `PILOT_CANONICAL_PASS.txt`.

The supplied `c143/runner.py` writes `ORACLE_full-pricing.log` and `SUMMARY.json` after its oracle subprocess returns, and writes the canonical pilot marker after that successful return. Therefore this folder alone does not preserve proof of a successful completed oracle subprocess. This does not contradict the user's report of running an oracle separately or losing output; the correct finding is that the final verdict is not recoverable from these run files.

A separate read-only primary trace, `/Users/USER/Desktop/c143_sample.txt`, records Python PID 53447 launched 2026-09-04 12:59:32.183+0900 and sampled at 15:55:14.421+0900. The shell history records V2 pilot execution and subsequent oracle/parent sampling commands (inspected by the main agent). The requested `c143_oracle_sample.txt` and `c143_parent_after_oracle.txt` are absent from Desktop. Process activity is not an oracle PASS certificate.

## Gaps in the supplied independent oracle

The original `oracle/c143_independent_oracle.py` correctly reconstructs geometry, primal feasibility, primal-dual objective equality, dual signs, exact full-root reduced costs in full mode, collapsed endpoint margins, and the arithmetic of integral bounds. However its `verify()` does not connect each child's stored `margin_affine` to `2*D - computed primal objective`; it also lacks exact canonical parent-breakpoint comparison, child tiling/domain coverage, and basis-list uniqueness/domain/length validation. A rehashed malformed certificate can therefore evade some intended structural checks even though the supplied bank may be correct.

The new independent replay closes those checks on the actual bank and does not use the generator's discovery solver, floating-point filters, or serialized ambiguity classifications. It verifies computed objective affines equal both stored objective affines; twice the independently computed signed demand minus price is explicitly checked as `margin = 2*D - price`. Dynamic-boundary continuity is checked within a geometry parent. Continuity across different geometry parents is not assumed: vanishing cells can remove owner gates at a collapsed endpoint, and that endpoint is separately certified.

## Exact arithmetic and its acceleration

Let `q` denote one integer Haar state. For owner epoch `e`, put `d_a = q_a - q_{a+1}` on its direct indices. The original dense point-matrix quadratic form equals

`sum_{a<c, c-a>1} -2*(c-a)^2*d_a*d_c / (8*e^2)`.

Multiplication by `m/128` and the epoch weight gives the owner demand. This sparse integer formula avoids dense Fraction matrix multiplication without changing the quadratic form.

For each serialized graph root `(i,j)` of nonnegative weight `x_ij`, the energy is `x_ij*(q_i-q_j)^2`. Its owner contribution is `x_ij*(q_i-q_j)*(1_G(i)*q_i-1_G(j)*q_j)`. The replay scales all `x_ij` to one positive denominator, accumulates exact owner shares with Python integers, and compares every share against the exact positive-part demand. Cell widths are affine rational functions of phase, so this reconstructs the objective and signed demand affines exactly.

For all-root dual pricing, let `S[g,i] = q_i` and `P[g,i] = 1_G(i)*q_i` for each selected dual gate. If `T = P^T diag(y) S`, the dual coefficient for `(i,j)` is

`T[i,i] + T[j,j] - T[i,j] - T[j,i]`.

The objective uses the same identity with `P=S` and cell width weights. Rational weights are scaled to one denominator. Arbitrarily large signed integer numerators are decomposed into signed base-2^20 digits. Each digit matrix product uses NumPy int64 only after proving the absolute partial-sum bound

`number_of_rows * (2^20-1) * max_abs(P) * max_abs(S) < 2^62`.

Reconstruction uses Python arbitrary-precision integers. There is no floating-point pricing or unproved int64 overflow assumption. All 19,110 reduced-cost affines are checked at both endpoints of every child; affine nonnegativity then holds throughout each child. Collapsed endpoints use their own independently reconstructed geometries. The total full-root target is 90,600,510 checks: 72,235,800 child endpoint/root checks plus 18,364,710 collapsed-endpoint/root checks.

The signed integral is recomputed from every reconstructed margin as `beta*(1/L-1/R) + alpha*log(R/L)`. Logarithms use the rational atanh partial sum and its rational geometric tail. The aggregate must equal both bank rational endpoints exactly and have strictly positive lower bound.

## Reproduction and validation

Replay script SHA256: `97ae7610717ad75bfdb9e850f1a15e1cbbeb50451030c9887dbc18deb8db3959`. The run used `/Users/USER/miniforge3/bin/python` (Python 3.13.13, NumPy 2.4.6). Do not run with Python optimization flags that disable assertions.

Run from any directory (the script's source bank path is explicit):

```sh
/Users/USER/miniforge3/bin/python -B /Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.py --mode full --output /Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.full.json > /Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.full.log 2>&1
```

The primal-only command substitutes `--mode primal` and `.primal.json/.primal.log`. It completed with process exit 0 in 105.900286 seconds, checking all 1,890 child and 961 endpoint certificates. Its minimum pointwise child margin is exactly `18976473121/3065610240 > 0`.

`c143_full_pricing_replay.equivalence.py` completed with process exit 0 in 8.868914 seconds. It verified 242 signed 140-bit matrix-product entries against direct Python summation, 56 owner demands against the supplied dense Fraction oracle, all 293 Haar cell states in parent 0 against the supplied state function, one complete original Fraction primal/dual basis replay, and 38,220 all-root objective values and original integer pricing checks. This is an implementation cross-check; its finite sample is not represented as the full bank replay.

All 11 adversarial rejection checks passed with process exit 0 in 42.933479 seconds. Results are in `c143_full_pricing_replay.adversarial.json`. These test malformed support, selected-gate/dual lengths and uniqueness, false objective/dual affines, missing interval coverage, false geometric and endpoint phases, duplicated integral records, and an unsafe int64 bound.

## Precise mathematical scope

Success proves a positive exact factor-two margin and a rigorous positive phase-integral enclosure for this one frozen `n16-contract-s32-r1` history, using the supplied graph-root cone and the old/new epoch weights in this bank. It checks every phase in that fixture's band, including all collapsed endpoints. The main agent's `C143_WEIGHT_EXTENSION.json` uses the same bank SHA256 and derives a fixed-witness extension to every `rho` in `[97/100,1]`, including the convention `rho=m^2/(m+1)^2` for every integer `m>=66`. Its explicit dependency, independent verification of the original bank's primal owner gates, is now closed by the whole-bank replay above. This dependency closure does not claim dual optimality of the old basis at `rho<1`. The extension's separate signed-demand/autocorrelation argument and rational bounds remain recorded in that companion artifact; both results retain fixed-history scope.

It does not establish uniformity over all admissible histories or all ranks, a history-independent positive margin, one compatible nonanticipating infinite ledger, or Erdős 1191 Q1/Q2. All original unresolved scope flags remain false. No source file or bank in Downloads was changed and no canonical pilot marker was manufactured there.
