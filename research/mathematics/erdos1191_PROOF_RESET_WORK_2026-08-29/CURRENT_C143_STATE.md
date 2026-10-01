# Current state: C143 V2, verified 2026-09-05

Read [the restored C143-to-Q1 report](evidence/q1_c143_followup_2026-09-05/C143_TO_Q1_REPORT.md)
before using older registry/entrypoint descriptions as the current checkpoint.

Primary data:
`/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/runs/pilot_s32_n16_r1/C143_BANK.json`

SHA-256: `d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`.
Size: 144,369,995 bytes.

- The full 960-parent, 1,890-child, 961-endpoint pilot is complete.
- A new strengthened independent full-pricing replay passed 90,600,510
  exact root-at-phase checks, exit 0.
- Every phase has positive local margin; the signed phase integral lies
  strictly between 0.04694333 and 0.04694335.
- The same witnesses work for later weights in `[97/100,1]` on this fixed
  64-mark history. Both terminal and lower-cutoff corrections have been
  reconstructed with their actual signs.
- Fixed-size, one-use positive-window pasting is rigorously insufficient:
  its total dyadic contribution is bounded while the full required signal
  grows logarithmically. A whole-tower theorem needs long-range/signed
  transport, uniform rank/history bounds, and one exact global owner ledger.
- Horizon-dependent finite certificates can be used; nonanticipation is a
  hypothesis of particular causal methods, not a universal prerequisite.

The Downloads packages and historical claim registry are preserved. The
new evidence, proof reviews, executable audits and full output are under
`evidence/q1_c143_followup_2026-09-05/`.

**Global status: `UNRESOLVED_AT_HARD_LIMIT`. Q1 is not solved.**
