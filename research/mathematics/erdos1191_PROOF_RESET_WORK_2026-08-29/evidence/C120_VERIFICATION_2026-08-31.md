# C120 verification checkpoint

Date: 2026-08-31 (Asia/Tokyo)

Status: exact finite calibration only.  C058 and both questions in Erdős
Problem #1191 remain unresolved; the global status is
`UNRESOLVED_AT_HARD_LIMIT`.

## Canonical C120 certificate

The canonical bundle is:

- `route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE.md`;
- `route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py`;
- `route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.json`;
- `route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate_test.py`.

The stdlib-only exact replay returned:

```text
VERIFY_OK chambers_replayed=161 gram_columns=2285 owner_endpoint_checks=198352 local_endpoint_ldl_checks=32 full_phase_prototype_survives_exactly chamber0_pointwise_prototype_fails_exactly mutations_rejected=13
```

It verifies 99,176 generic owner rows at both endpoints, 194,528 collapsed
endpoint owner rows, all rational zero-row-sum epoch-block Gram factors, and
the rational atanh log enclosures.  The exact conclusions are

```text
719/10000 < full-phase normalized witness < 9/125
13/500 < prototype RHS < 27/1000
full-phase normalized witness - prototype RHS > 457/10000
chamber-0 normalized upper < 2601/100000
prototype RHS - chamber-0 upper > 207/1000000
```

Thus only the complete phase-integrated comparison survives.  The independent
chamber-0 dual rules out a pointwise or per-chamber reading.

Payload SHA-256:

```text
388daa5b719a6f817f3d2de2f5227340b2ec355ca53e93ba2753edc3d270b10d
```

Current file SHA-256 values after the prose-only eta/boundary clarification:

```text
042703e5faa21650b3aba8de1504fe1f29817b87df551dbf2332155e8aab5c44  ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE.md
6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9  ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py
6d0382b1267aac07e1ba5533a6a8d292dc29ba937911cae2bef9628052c21e74  ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.json
62d79af37857dbcc6b426c8aeb9128200615b5be1a906d3314793e8b97b3b00f  ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate_test.py
```

## Full Route-C regression

The cache-suppressed command

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s route_probes -p '*test*.py' -v
```

found 34 suite files and returned:

```text
Ran 366 tests in 342.109s
OK
```

There were no failures, errors, or skips.  The seven new C120 tests are
included in, not added to, the 366-test total.

## Formal toolchains

Lean remains pinned to 4.33.0 and mathlib commit
`db584cd6d46c92f209a44c0f1c829460d327499d`.  A fresh final
`lake build` completed 1,067 jobs, and
`lake env lean Erdos1191/AxiomAudit.lean` exited zero.  Its theorem output
contains only `propext`, `Classical.choice`, and `Quot.sound`; the project
source scan contains no `sorry`, `admit`, custom `axiom`, or `native_decide`.

The Rocq MCP health/minimal probes and the selective assumptions audit are
recorded in `evidence/formal_toolchain_refresh_2026-08-31.txt`.  A fresh final
temporary-directory Rocq 9.1.1 replay compiled
`OwnershipFiniteAudit.v`, printed `Closed under the global context` for all
14 audited theorem families, and passed `rocq check -silent`.  The canonical
Rocq tree contains no generated object or auxiliary file and no `Admitted`,
`Axiom`, `Parameter`, `Conjecture`, or `Abort` declaration.

## Registry and artifact gates

The CSV and JSON registries are byte-semantically equal through 120 sequential
claims, `C001`--`C120`.  `C058` remains `OPEN` and the global status remains
exactly `UNRESOLVED_AT_HARD_LIMIT`.  All 113 first-party JSON files parse.
The selected text/control scan is clean.  Python cache files created by test
subprocesses were moved recoverably outside the canonical worktree to:

```text
/tmp/erdos1191-pycache-c120.vX2840
/tmp/erdos1191-pycache-post-c118.VnIPCX
```

The final generated-artifact scan excludes the intentionally retained Lean
`.lake` build/dependency cache and finds no `__pycache__`, `.pyc`, `.pyo`,
Rocq `.vo/.vok/.vos/.glob/.aux`, or lock artifact elsewhere in the canonical
tree.  The preserved old release manifest remains intentionally unsealed and
was not regenerated.

## Unregistered C118 primal diagnostic

A disposable follow-up exact bank under `/tmp` gives 87 feasible rational
C118 factors, 1,573 columns, 53,592 open owner rows, and 104,784 endpoint
owner rows.  Its normalized witness lies in
`(-47703/1000000,-47702/1000000)`, below the prototype interval
`(-41045/1000000,-41044/1000000)`.  The existing exact dual upper is about
`-0.04014304`, so the target remains inside a residual primal--dual window of
about `0.00755914`.  This is not a no-go and is not registered as C121.

Disposable manifest payload SHA-256:

```text
50704f33c7b4dfc71e29c9e5608fc9c8b6934c54608d13dce976cd695ea8c17d
```

The next finite task is to close that exact window, beginning with chambers
49, 73, 74, 64, 70 and the chamber-1 rationalization boundary.  Formalization
remains subordinate to this C058 phase-integrated search.
