# C137 final verification — 2026-08-31

## Outcome

C137 exactly refutes pointwise memoryless recovery of the audited one-sided
box-pair C133 ledger from the current C136 100-channel graph state.  This is
only a no-go for that carrier and graph state.  It leaves a cumulative
same-`M8/M16`-atom potential, enlarged channels, nonlocal transport, and C058
open.

## Fresh canonical replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_certificate.py --verify --self-check
MUTATION_OK rejected=8/8
C137_LOCAL_CHARGE_NO_GO_OK state=652c2c363064 lhsA=64/104961675 lhsB=176/314885025 C058_open

PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_test.py
Ran 8 tests in 7.298s
OK

PYTHONDONTWRITEBYTECODE=1 python3 -B route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_independent_oracle.py
C137_INDEPENDENT_ORACLE_OK full_state_collision terminal_collision root_zero_terminals C058_open
```

## Exact no-go witnesses

- The complete 100-channel state is identical on
  `[616,20401/32)` and `[20401/32,21009/32)`.  All 57 supported root
  features and all direct demands vanish, but the C133 totals are respectively
  `64/104961675` and `176/314885025`.
- A second identical-state cell pair changes both terminal rows.
- Separate zero-root/direct cells have a positive epoch-8 terminal and a
  positive epoch-16 terminal.

Therefore no arbitrary pointwise function of the full state can recover the
ledger total, fourteen-row vector, or terminal pair.  Scalar, diagonal,
owner-block, affine, and supported-root linear maps are strict subclasses and
also fail.

## SHA-256

```text
explanatory MD      fd8845e8bb41903b5076a23d4365a3d611995314fbae6d483b8473a8e04ec267
verifier            217fe0610cfe020f88a9373ed165425a3188d9c006de2f6329deca1391875458
certificate JSON    1e083832ad6d845773b3e37437fd017a03810916dbddd12df05dac71f78e8967
certificate payload 6999d793e3a2a8c44e30989df363b87fabc8f942ae4536b770edcc7b0eb85aca
independent oracle  11399fb4a815eff378ad0cec6dcabc52e4ad8a8efcb9f339e57fd813a0254562
focused tests       f12886118403f632d9a0442afa332ac1a0fc4d911848c2f5e659ccaf0cc3ed27
```
