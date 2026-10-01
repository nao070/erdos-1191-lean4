# C131 final verification record — 2026-08-31

Global status: `UNRESOLVED_AT_HARD_LIMIT`

## Registered finite claim

C131 completes the exact finite C120 common-phase primal bank for the frozen
C125 coefficient candidate, phase interval `[82,164]`, and `rho=9/16` in the
independent epoch-block aggregate cone.  The accepted certificate contains
all 147 exact phase chambers and 294 rational Gram factors.  It reuses the
hash-pinned old C120 factors for new chambers 0--114 and embeds exact reduced
integer factors for chambers 115--146.

Every one of the 147 integrated piece margins is strictly positive.  The
exact clean fences are

```text
raw margin > 21/1000
3/100 < normalized margin < 31/1000
minimum active owner slack = 305733/87500000000000
raw enclosure width < 1/10^26
```

This is a fixed finite witness.  It does not prove a nonanticipating C103
phase rule, the global Abel boundary/terminal ledger, representative
independence, a local or global master inequality, arbitrary rank, C058,
Q1/Q2, novelty, publication acceptance, or prize eligibility.

## Exact artifacts

| artifact | SHA-256 |
|---|---|
| `route_probes/ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_certificate.py` | `5f7f1a1928e413ec8808279c57da99a401a01bb3a52a1fe8bca764bacf2c3a4a` |
| `route_probes/ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_certificate.json` | `6b28874a6c0ffe3d36a5ada27a3b466e0dbcd19447a2da0fb501b0ccc7df5afc` |
| `route_probes/ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_test.py` | `7a8d60b8fd8d500f75a56d26243dae946029ed6b644097d49e5d5f872a4c6f83` |
| `route_probes/ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL.md` | `bdfbb75b19ef0ddb59b13b42cb51a22368418d0566bb75ff8d4e67a0dd24a214` |
| certificate payload | `5012236aa28d76867d94926a26d00ffacf602952e93358818594907f7ea7d477` |
| accepted tail factor bank | `bb8629e4248bc6467fe6617f319e74f42457350dd797e821e320a7dc8b0477e8` |
| temporary tail discovery bank | `c39708a826344077fad6e4910982a45e0e0b1319cbf5ced901f085407baed909` |

The focused command returned:

```text
Ran 8 tests in 57.246s
OK
```

The standalone self-check returned:

```text
VERIFY_OK row=C120 common_phase=[82,164] rho=9/16 chambers=147 factors=294 raw_margin>21/1000 3/100<normalized_margin<31/1000 mutations_rejected=4 C058_open
```

## Independent audits and verifier hardening

An independent exact implementation, not importing the C129 or discovery
generator replay, returned `INDEPENDENT_EXACT_AUDIT_OK`.  It reproduced the
115+32 chamber split, join `553/4`, exact factor-bank hash, rank and owner
censuses, clean margins, and the rejection of removing the tail midpoint
scale.  A wrong `DeltaVrt` sign was also checked independently and was shown
to make the target easier by the exact amount `13171/872685`; the canonical
negative sign is therefore pinned and load-bearing.

Code review found one verifier API defect before finalization: a long-lived
process could reuse the arithmetic replay cache after a pinned dependency was
removed.  A regression test was first observed failing against the old code.
The verifier now checks C126, C129, prefix verifier, prefix certificate, and
model provenance before every cache lookup.  The new test and all eight C131
tests pass after the fix; independent re-review found no remaining P1/P2
issue.  The mathematical payload and factor bank were unchanged by this
hardening.

## Full Route-C regression and registry gate

The cache-suppressed command

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s route_probes -p '*test*.py' -v
```

found 44 suite files and returned:

```text
Ran 426 tests in 650.696s
OK
```

There were no failures, errors, or skips.  The synchronized CSV and JSON
registries contain exactly 131 claims with eight identical fields per row,
sequential IDs `C001`--`C131`, no gaps or duplicates, and `C058` still labeled
`OPEN`.  The five current status/obligation/approach/continuation/log documents
each contain one C131 section and no stale pre-hardening C131 hash or
placeholder.  `FINAL_STATUS.txt` remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.

All 129 first-party JSON files parse after excluding the intentionally retained
Lean `.lake` dependency/build cache.  Python bytecode created by verification
subprocesses was moved recoverably outside the canonical tree to
`/tmp/erdos1191-pycache-c131.5eGAqX`.  The resulting first-party tree contains
no `__pycache__`, `.pyc`, `.pyo`, or Rocq `.vo/.vok/.vos/.glob` artifact.

## Exact remaining bottleneck

C130 and C131 now form a fixed two-row finite primal bank.  The immediate
C058 obligation is still to construct one globally admissible nonanticipating
completed-shell phase rule and place both rows inside a single exact C103
owner/Abel boundary-terminal ledger, then survive representative-independence,
scalable-history, and arbitrary-rank gates.  More fixed 16-mark point checks
alone cannot close this obligation.
