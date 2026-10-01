# C135 final verification — 2026-08-31

## Outcome

The canonical C135 verifier, focused mutation suite, and independent replay
all pass.  The accepted result is only the frozen O0N1 complete-phase dual
separator in the stated 52-coordinate independent epoch-4/epoch-8 cone.
It refutes the corresponding universal finite D1 rotation hypothesis by weak
duality.  It does not refute Route C, establish physical primal
infeasibility, or resolve C058.

## Fresh canonical replay

From `route_probes/`:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_certificate.py
EXACT_C135_OK ... pieces=314 epoch_duals=628 endpoint_PD_checks=1256 margin_gt_1_over_2500=True mutations_rejected=8 C058_OPEN

PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_test.py
Ran 10 tests in 54.601s
OK

PYTHONDONTWRITEBYTECODE=1 python3 -B ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_independent_oracle.py
INDEPENDENT_EXACT_REPLAY_OK_KILL
```

The independent replay reconstructed 120 distinct positive differences,
314 refined pieces, 628 epoch duals, 193,424 rational weights, and 1,256
endpoint Bareiss positive-definiteness checks.  It reproduced the exact
normalized, target, and separator hashes and certified the clean margin
greater than `1/2500`.

## Registry state

After registration, the CSV and JSON claim registries match field-for-field:

```text
REGISTRY_PARITY_OK 135 unique 135 last C135
global_status=UNRESOLVED_AT_HARD_LIMIT
```

## SHA-256

```text
explanatory MD       ee0b4158fb83da58e8e10feee263d280e8ac45ed59a42b948352ef6bc48272fc
verifier             0222b9a40a02e85529a739a9861a1ef0f7caf21081a4946546b3dc84f209b057
certificate JSON     662b5e9a20f5531c71fb8e4edbc1cc0ab31c0cdee23c7adf3b3e048d29a15218
certificate payload  e53d4850d09d38b68d51c2ad35337ca48f455006ccfda851ef451e45880cd9e3
refined source       2949602baa0cb68aa3131bcb003fa2ac35156743bb2202e9a02f906ccf960c6b
parent source        93efb6b9846800f4025d72bd79536cc052f46f750e706b2966efa90928002912
independent oracle   bf37a13abfb4e3b862b872a7bd37bce23bad965b88eabe71310d0cd5b4b54910
focused tests        288501a0bf8fc8a9a867f89e687b963e6a214c47d0cedc14791f3bcce5c02394
```

## Adversarial gate and full regression

The pre-promotion critic independently reconstructed the O0N1 fixture,
target, exact partition, parent classification, endpoint PD checks, and
complete-phase separator before returning a conditional scope pass. The ten
focused tests reject 35 explicit rehashed or semantic mutations: forbidden
claim upgrades, fixture/type drift, partition corruption, exact dual/scalar
corruption, provenance drift, and a controlled doubled-weight mutation whose
two endpoint slacks are both non-PD. The verifier's built-in self-audit
separately rejects eight scope/claim mutations.

The repository-wide Route-C command

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s route_probes -p '*_test.py' -v
```

completed with `Ran 199 tests in 635.584s — OK`.

The source artifacts remain byte-preserved. The canonical verifier and
independent oracle have no `/private/tmp` dependency; the oracle does not
import the C135 verifier and uses no removable `assert` gate. C135 was the
next unused ID at its pre-write audit and was registered sequentially after
C134. A separate concurrent promotion subsequently appended C136; the live
registries are now field-identical and sequential through C136, with C135
unchanged. C058 remains `OPEN`, and `FINAL_STATUS.txt` remains
`UNRESOLVED_AT_HARD_LIMIT`.
