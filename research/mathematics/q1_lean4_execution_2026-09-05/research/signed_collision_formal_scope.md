# Formal scope of the signed-collision algebra module

2026-09-05. Author: /root/moment_evidence_audit, GPT-6 Astra Ultra.

**Result.** The new module `lean/Q1/SignedCollision.lean` builds with
Lean 4.33.0. Its sixteen explicitly audited declarations use only
`propext`, `Classical.choice`, and `Quot.sound`. A separate, targeted
Leanchecker process also returned exit 0 in the imported environment.
These checks formalize the algebraic engine of the signed multiset
argument. They do not formalize its Sidon matching partition or prove Q1.

The mathematical source is `research/signed_multiset_born_retirement.md`,
whose reviewed SHA-256 is
`324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487`.
The Lean source SHA-256 is
`771477f28220c6d7480abc77cd4ba49f1981c09e6f46f3b14093b028ccbc1bda`.

## Exact mathematical coverage

The module works over real numbers. From `X<=c`, `Y<=c`, and
`X+Y=-c`, it proves `X^2+Y^2+c^2<=6c^2`. Its proof uses
`(c-X)(c-Y)>=0` and the squared centering identity; nonnegativity
of c need not be added as a separate hypothesis.

The definitions are precisely

~~~
born(U,c,A)=(4U+12c^2)/A,
retired(U,V,c,A)=(2U+6V-12c^2)/A.
~~~

Here U,V denote numerical variance values. They are not Lean multisets
or point triples. The module proves the exact total and gap identities,
Born nonnegativity, and `retired<=2born` from `U>=0`, `V<=6c^2`,
and `A>0`. A corollary substitutes the centered coordinate variance
for V. The divisor is an arbitrary positive real; identifying it with
`aut(U)aut(V)` remains part of the unformalized combinatorial argument.
The two ring identities hold even when the divisor is zero under Lean's
total division convention. The inequalities used for collisions explicitly
require a positive divisor.

Finite-stage aggregation is also proved, with its precise assumptions
visible in the theorem statement. The partition theorem assumes
`totalB=sum B_i+remainder`, `totalR=sum R_i`, a nonnegative remainder,
and each local inequality `R_i<=2B_i`. It does not construct the actual
Sidon collision partition. Finite nonnegative weighting preserves the
comparison without any monotonicity hypothesis. Interpreting the weights
as Born source-clock and retired output-clock prices is external to this
real-valued algebra.

Given the explicit identity `E=D+2B+2R` and `R<=2B`, the module proves
`E<=D+6B` and `(E-D)/6<=B`. It proves
`j(Z+v)-(j-1)Z=Z+jv`, and a finite weighted energy-gap inequality
assuming the exact energy identity at every index. It does not derive
the actual signed convolution identity from a Sidon history.

Finally, for real `j>=2`, `H>0`,
`Z<=(j-1)(j-2)H^2` and `v<=2(j-1)H^2`, it proves

~~~
(Z+jv)/[(j(j-1))^2 H^2] <= 2/j^2+1/[j(j-1)].
~~~

The rational simplification is a separate theorem with explicit nonzero
denominators. No infinite-series or zeta-value theorem is added here.
The good-epoch analysis, asymptotic divergence, physical envelope, and
original Q1 remain outside this formalization.

## Complete declaration inventory

Every name below has the prefix `Erdos1191Q1.SignedCollision.`.
There are two noncomputable real-valued definitions and fourteen theorems.

| Name | Kind and scope |
|---|---|
| `centered_variance_le` | Theorem: maximal centered coordinate bounds the three-coordinate variance |
| `born` | Definition: algebraic Born formula |
| `retired` | Definition: algebraic retirement formula |
| `born_nonneg` | Theorem: nonnegative variance and positive divisor |
| `born_add_retired` | Theorem: exact total identity |
| `twice_born_sub_retired` | Theorem: exact comparison gap |
| `retired_le_twice_born` | Theorem: comparison from variance bounds and positive divisor |
| `retired_le_twice_born_of_centered` | Theorem: centered-coordinate specialization |
| `retired_le_twice_born_of_partition` | Theorem: explicitly assumed finite partition and Born remainder |
| `weighted_retired_le_twice_born` | Theorem: finite nonnegative weighting |
| `energy_le_diagonal_add_six_born` | Theorem: upper energy bound from an assumed identity |
| `energy_gap_div_six_le_born` | Theorem: one-sixth Born lower bound |
| `signed_diagonal_increment` | Theorem: exact signed-diagonal polynomial identity |
| `weighted_energy_gap_div_six_le_born` | Theorem: finite weighted energy-gap consequence |
| `canonical_diagonal_ratio` | Theorem: exact rational simplification with nonzero denominators |
| `normalized_signed_diagonal_le` | Theorem: pointwise normalized diagonal upper bound |

## Observed verification and bindings

Lean LSP diagnostic feedback on the final source returned success with
no warnings or errors. The independent linear-causal agent read the
entire source and found no semantic mismatch or scope overclaim; that
read was a mathematical review, not a separate Lean execution.

The instrumented runner is
`lean/evidence/signed_collision_verify.py`, SHA-256
`d1728a8ba5dd6df162b8f606f134832cec6a86df2f3284f429d1575b4cfb0565`.
It ran only the new module target and its explicit declaration driver,
with the existing pinned configuration:

| Action | Exact arguments after the Lake executable | Observed UTC interval | Exit |
|---|---|---|---:|
| Targeted module build | `build Q1.SignedCollision` | 10:46:59.984014 to 10:47:02.965059 | 0 |
| Explicit axiom audit | `env lean evidence/signed_collision_axioms.lean` | 10:47:02.968042 to 10:47:04.997105 | 0 |

The date for both intervals is 2026-09-05. The build printed
`Built Q1.SignedCollision` and successful completion. The audit driver
contains an explicit `#print axioms` command for each of the sixteen
names above. The runner checks that this list exactly matches the source
declaration inventory and that each declaration occurs once in the axiom
output. All sixteen outputs contain exactly the three allowed axioms.
The source token scan found no `sorry`, `admit`, `axiom`,
`native_decide`, or `unsafe`. Successful kernel-checked compilation and
the explicit axiom outputs, rather than the token scan alone, establish
the formal result.

Each command preserved separate complete stdout and stderr, their hashes,
timestamps, the observed return code, and source hashes before and after.
The frozen seventeen-file input snapshot includes the fourteen existing
Lean source/configuration files, the new module, the explicit axiom
driver, and this verification runner. Every unchanged-input gate passed.
Five resulting compiled artifact files were also hashed. A subsequent
read-only check matched all current source/artifact hashes and the saved
stdout/stderr bytes to these records. It did not rerun a successful build.

Key files under `lean/evidence/` are:

- `signed_collision_build.run.json`, `.stdout.txt`, `.stderr.txt`.
- `signed_collision_axioms.lean`, `.run.json`, `.stdout.txt`, `.stderr.txt`.
- `signed_collision_result.json`, containing all declaration names, per-name
  axiom sets, the final source snapshot, and compiled artifact hashes.
- `signed_collision_runtime.json` and the separately captured
  `signed_collision_lean_version`, `signed_collision_lake_version`,
  `signed_collision_resolved_lean`, and `signed_collision_resolved_lake`
  command records and output files.

Result SHA-256:
`a66123d33af1f99877a727fe4f1382f46179c401216356935fcf60ff0aedf031`.
Build record SHA-256:
`3e54201c897878d42fd800a27907cab03ac979b8d871bbb706254969abadeaac`.
Axiom record SHA-256:
`5d9fc9532ee9d1f3561d70351c6995118f8f1f256ed63e37e87fcff353998bed`.

The recorded runtime reports Lean 4.33.0, commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`, and Lake
`5.0.0-src+d8b1897`. Resolved Lean/Lake executable hashes and the
Python executable/version/hash are captured in the runtime record.
No pinned version or dependency configuration was changed.

## Targeted Leanchecker replay

At the parent's subsequent request, the separate runner
`lean/evidence/signed_collision_checker_verify.py` executed

~~~
lake env leanchecker Q1.SignedCollision
~~~

once in a new process, from 2026-09-05 10:49:39.280542 UTC to
10:49:46.279760 UTC. The observed return code was 0; both saved
output streams are empty. Their emptiness is not being used as an exit
status substitute. The record contains the actual process return code.
Source files, compiled artifacts, the prior result/runtime records,
the checker runner, and the checker executable were bound by unchanged
hashes before and after. A post-replay `lake env which leanchecker`
probe confirmed that resolution matched the recorded executable and hash.
That probe was not a second checker run.

The replay record is `lean/evidence/signed_collision_checker.run.json`,
SHA-256
`2d1b859b87572341b8b329355fc7025a4891d0371b6767227f5f94230a0b27e3`.
Its stdout/stderr files, checker runner, and
`signed_collision_checker_resolution.run.json` are saved alongside it.

This is Lean's own kernel replay of the new module in its imported
environment. It is not `--fresh` replay of all imported declarations,
and it is not an independent external checker. The earlier fresh-replay
records retain their previous scopes.

Only the new module, uniquely prefixed evidence files, and this scope
note were authored for this task. `Q1.lean`, `Q1/AxiomAudit.lean`, the
pinned versions, status files, and existing evidence were not edited.
The new module is intentionally absent from the unchanged aggregate
imports and was built by its explicit target. The unrelated existing
82-declaration audit was not rerun. Original Q1 remains unresolved.
