# C132--C134 final verification

Date: 2026-08-31 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Primary open claim: `C058`

## Claim boundaries

- C132 is an exact finite no-go for the displayed affine reuse of the local
  C130/C131 owner banks.  It does not refute a fresh joint epoch-8/16 master.
- C133 is the finite `L=0,m=1,n=4` adjacent-epoch Abel identity: fourteen
  unique rows, including four net shared `A16` rows and both upper terminals.
- C134 gives an exact signed representation of the 63-source residual and an
  exact positive-Gram-only separator.  Its negative Gram bank is not positive
  capacity and therefore does not solve C058.

## Exact Python replay

C132:

```text
VERIFY_OK EXACT_FINITE_COMPOSITE32_NAIVE_LOCAL_BANK_PASTE_NO_GO_C058_OPEN
span=7084 differences=496 residual_sources=63 owner_rows=692
owner_failures=152 mutations_rejected=5 C058_open

7 focused tests: PASS
INDEPENDENT_EXACT_ORACLE_OK span=7084 differences=496
residual_sources=63 residual_mass=4767/1024 owner_rows=692
owner_failures=152 strongest_margin=-175791028451541/10006250000000000
C058_open
```

C133:

```text
VERIFY_OK C133 rows=14 raw=18 random=512 rank15_owner=epoch8
C103_specialization_only C058_open
9 focused tests: PASS
8/8 mutations rejected
```

C134:

```text
C134_RESIDUAL63_EXACT_OK sources=63 mass=4767/1024
primitive_rank=63 signed_gram_rank=78 positive_only_separator=-1/16
ranks15_18=retained C103_rows=retained C058_open

5 focused tests: PASS
INDEPENDENT_C134_RESIDUAL63_OK sources=63 mass=4767/1024
primitive_rank=63 signed_gram_rank=78 positive_only_separator=-1/16
boundary_rank15=-1/64 ranks15_18=retained
C103_initial_final_terminal=retained C058_open
```

The C132 and C134 independent oracles import neither their main verifier nor
other canonical Python modules.

## Lean 4 replay

The pinned project reports Lean `4.33.0`.  The new theorem is

```text
Erdos1191.adjacentEpochTwoEdgeFourScaleLedger
```

Direct compilation of `Erdos1191/AdjacentEpochLedger.lean` succeeded.  After
rebuilding the root import, `lake build` completed successfully with 1,069
jobs.  `AxiomAudit.lean` then compiled and reported only

```text
[propext, Classical.choice, Quot.sound]
```

for the new theorem.  There is no `sorry`, `admit`, or custom axiom in the
statement or proof.

An initial direct `AxiomAudit.lean` invocation saw an old root `.olean` and
reported the new constant as unknown.  Rebuilding the root import resolved
the stale dependency.  This was a build-cache/dependency issue, not a failed
mathematical proof.

## Rocq/Coq reachability refresh

`rocq_health` returned:

```text
ok=true
server_version=0.3.1
switch=coq-mcp
coqc=/Users/USER/.local/bin/coqc-coq-mcp
version=9.1.1 (OCaml 4.14.2)
pet=0.2.5, pytanque_importable=true, running=true
warnings=[]
```

An import-free minimal theorem compiled and `rocq_verify` accepted it with
`verification_method=module_m` and `assumptions=[]`.  The existing independent
`rocq_kernel/PrefixScaleFiniteAudit.v` then passed a full MCP compilation, and
`rocq_assumptions` returned `assumptions=[]` for `prefixScaleCurl`.

One preliminary probe using the obsolete/minimal-install-incompatible import
`From Stdlib Require Import Arith` failed because this Rocq switch exposes the
small Corelib layout rather than that logical path.  The corrected probe and
the project audit both passed.  This is an import-selection failure, not an
unreachable MCP server or a failed kernel.

## Registry and literature audit

The CSV and JSON claim registries parse and match field-for-field:

```text
REGISTRY_PARITY_OK 134 unique 134
global_status=UNRESOLVED_AT_HARD_LIMIT
last_claims=C132,C133,C134
```

The current Martikainen v1 numbering is recorded as Theorems 1.3, 1.8, and
1.11 respectively for critical bi-parameter packing, Zygmund packing, and the
sharp `alpha+beta` range.  The literature delta records only candidate
downstream tools and their missing hypotheses; no paper was found that closes
C058.

## Current finite checkpoint

The exact residual is algebraically expressible, and the exact fourteen-row
ledger is frozen.  The next unfinished computation is a fresh joint 32-mark
cellwise epoch-8/16 program on one common physical phase.  It must retain all
ranks 15--31, all 63 cross-half signed sources, a genuinely positive-capacity
Gram, and every C133 initial/shared/final/upper-terminal row.  No result from a
relaxed, incomplete, or `optimal_inaccurate` solver run may be promoted to a
mathematical claim without independent PSD, owner, finiteness, and exact
replay checks.

## SHA-256

```text
C132 MD        f9a69d6b3e20ab8ed69b0b11974c2de40d6714659e055d6cdba3ce9d38cc2d0c
C132 verifier  6bc5387868c37452a49f43d9ee88b5cb970726cd0cc22b44aa9ca5fcf1e0ab01
C132 JSON      8508e9fa89535b1d22558b895c1fffd01a19ff2f304ed6e9a4f9b51c55eccc7a
C132 oracle    6cfd0ebbbdb1be941ab1c4b7d83cf69febc0d2b69224f512f6e9ab8ece21eccb
C132 tests     02467a213232f5fe7f075d642dc01b838ec1e1ef862c380b45c43b3c0ac75d62

C133 Lean      3817e8c110a067dcf94d165e1637e90013afdbeaf2395c687fbdc9900cd3e7dc
C133 MD        db6fca19751b2d3873c9725df22a6d89163725dc99226f38e48cf7013f63122a
C133 verifier  2eb24b4aefa16d9434ea1e8cf5ab1b945809034b0c6aed4119a77d2c06e6818c
C133 tests     b14c0b53b093ba05736b3923d75581106c741fe0cd2495be4d6da57604071386

C134 MD        79dcb07f773414db4654d88cd6d32276ac1da2b2efd2b5fec3f4732b19550efd
C134 verifier  0ed45cb651f07ca264f4237c8d4f817e4d42ac54792bf3d5901852d660dc4a0a
C134 JSON      2ef818b00aac98f56eeb1582e37aeca8906e381c702c1990f0ccef8d70a97ae0
C134 payload   9657b7bfea05bd32063f1cc16391fe60823573c7f694f46fdb65f2dda9f45d30
C134 oracle    b93582f5bef1eac0397071e93a336d8058d18768104cf0889556eafdc90aaa20
C134 tests     9863a2215460b5ed2632810cb824ab73707b4911120c32db9c70f7dcaa8ce7d6
```

## Full route-probe regression

After the focused C132--C134 replays, the complete canonical route-probe
suite was rerun from the repository root with bytecode writes disabled:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s route_probes -p '*_test.py' -v
Ran 189 tests in 584.972s
OK
```

This establishes compatibility with the existing finite harness at this
checkpoint.  It does not prove C058 or the infinite Erdős #1191 statement.
The discovery-time tree already contained the ten C135 focused tests, so the
189-test census includes them; C135 also has a separate canonical verification
record in `evidence/C135_FINAL_VERIFICATION_2026-08-31.md`.
