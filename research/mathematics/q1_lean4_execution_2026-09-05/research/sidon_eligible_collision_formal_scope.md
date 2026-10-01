# Actual eligible collision: two newest endpoints on opposite sides

The separate new module `lean/Q1/SidonEligibleCollision.lean` contains two
theorems. Both passed an actual targeted build, explicit per-declaration axiom
audit, and imported-environment checker replay. The previously verified
`Q1.SidonTripleCollision` source and evidence were preserved byte for byte.

## Exact formal claim

Use the unchanged `Erdos1191Q1.Sidon A` predicate and the already defined
`SidonTripleCollision.SignedBefore`. Suppose `m,n∈A`, `m<n`, and both nonzero
signed source labels have their actual endpoints strictly below **m**:

\[
 u=a-b,\quad v=c-d,\quad a,b,c,d<m,\quad u-v=n-m.
\]

The module extracts these actual endpoint witnesses and derives

\[
 U=\{a,d,m\},\quad V=\{b,c,n\},\quad
 |U|=|V|=3,\quad \sum U=\sum V,\quad U\ne V,\quad U\perp V.
\]

Here braces are multisets and the disjointness is of their supports. The exact
counts are

| Endpoint | Count in U | Count in V | Count in U+V |
|---|---:|---:|---:|
| m | 1 | 0 | 1 |
| n | 0 | 1 | 1 |

All four other endpoint slots are strictly below `m`. Thus `n` and `m` are the
unique largest and second-largest endpoint occurrences of this collision and
lie on opposite sides. These are derived counts, not an assumed orientation.
Old endpoint repetitions remain allowed. Signed equations use `ℤ` and actual
endpoint values use `ℕ`.

The cutoff is an endpoint value, not a formal rank clock. In a strictly
increasing enumerated history, the mathematical condition that both source
labels predate the lower output endpoint gives these premises. The Lean module
does not construct that enumeration or the source/output rank functions. It
also does not formalize the complete matching-orbit partition, its automorphism
weights, the eligible physical kernel, an eligible budget inequality, or Q1.

The two full declaration names are:

1. `Erdos1191Q1.SidonEligibleCollision.eligible_endpoints_collision` — the
   endpoint-level equal-sum/disjointness and exact two-endpoint counts.
2. `Erdos1191Q1.SidonEligibleCollision.eligible_sources_yield_collision` — the
   complete certificate from actual `SignedBefore A m` source witnesses,
   retaining their membership, equations, distinct source endpoints, and four
   strict old-endpoint inequalities.

Both declarations depend only on `propext`, `Classical.choice`, and `Quot.sound`.
Their conclusions are proved from the actual Sidon and old-source hypotheses;
no scalar target inequality, collision disjointness, or endpoint-count
conclusion is assumed. The complete source scan found no prohibited escape
tokens, and the final LSP check reported no diagnostics.

## Observed verification and byte preservation

Each execution saves exact argv, cwd, UTC interval, elapsed time, observed exit
code, full separate stdout/stderr files, embedded outputs, and their hashes.

| Check | Interval on 2026-09-05, UTC | Result |
|---|---|---|
| `lake build Q1.SidonEligibleCollision` | 12:47:38.806062–12:47:43.720880 | exit 0 |
| Explicit two-name `#print axioms` driver | 12:47:43.736264–12:47:47.094908 | exit 0; exact coverage |
| `lake env leanchecker Q1.SidonEligibleCollision` | 12:48:02.782620–12:48:11.089305 | exit 0; empty stdout/stderr |

The build/audit source snapshot contains 21 files, including the preservation
manifest. The checker binds 29 source/artifact/evidence files. All before/after
hashes agree. Separately, `sidon_eligible_collision_prior_files.json` binds 184
previously fixed files: the original 153-file manifest plus the completed
SidonTripleCollision source, evidence, and scope. All 184 files were unchanged
before and after every instrumented command.

The runtime is the same pinned Lean 4.33.0 commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`, with Lake
`5.0.0-src+d8b1897`. Runtime executable paths and hashes are recorded. The
checker replays this module in its imported environment using Lean's kernel;
it does not freshly replay all imported dependencies and is not an independent
external checker. A separately labeled post-replay executable-resolution probe
confirms the checker path and bytes without another checker execution.

At 12:48:30.726097 UTC the saved readback checked all source/artifact bytes,
complete saved outputs, runtime executable bytes, and all 184 preserved files.
It ran no additional build, audit, or checker. None of the unchanged aggregate,
existing audit suite, prior algebra modules, prior verified triple module,
configuration, or research status files was edited.

All evidence below has prefix `lean/evidence/sidon_eligible_collision_`:

| Suffix | SHA-256 |
|---|---|
| `verify.py` | `9c0401d172c1c0015102fe5956bf3910ba30c135293cb3997a8c3be1494cdda4` |
| `checker_verify.py` | `1c6a81fc3215942c5c15f3e451f53acf5c969b87dcf3aed202ae245ef2126eb2` |
| `prior_files.json` | `4e15827f9e591672b1a04787f27c7f20ea1f2cf3a12e47e3f89150522866bcb1` |
| `result.json` | `357590b17d9f50825998e9f5de4b51a37d1c7652662157d04767c198bd566358` |
| `build.run.json` | `63446ca95b85a17e0b6105ed058ee83f94a9e2a723c0f9a11d44cd5e5aa2b68d` |
| `axioms.run.json` | `de553f89fc20b7a4aa0e403ea16acfb919e0e9ea8ad91d92a9492affc36a4ba2` |
| `checker.run.json` | `768f8f5de5c14d89d3f189f45f410f5fc602acb416895637997b5a406fdb126d` |
| `runtime.json` | `5e27d263f8005559c00bfa3641d2774f3d2db5f66050e87f9a64f276eca4d6d8` |
| `checker_resolution.run.json` | `b2e4ff4c6d8a032bff191ffa477bab32337f4b366b2c95dfdb100d5cfa1ef642` |
| `readback.json` | `32ca100d4708c84d85b52a7eacc2e38542f7167cc519821a8e11353170f39f43` |

Frozen source SHA-256:
`1489bf5bea109380df3d7c8369f2a04f6450083f9ee693a9556be5a6571d5105`.
The two new declarations are local actual-combinatorial support. Neither their
successful verification nor the earlier sixteen-declaration module proves the
remaining global estimate or resolves Q1.
