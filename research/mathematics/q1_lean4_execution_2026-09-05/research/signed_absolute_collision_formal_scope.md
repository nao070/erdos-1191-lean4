# Formal scope of the absolute signed-collision algebra

2026-09-05. Author: /root/moment_evidence_audit, GPT-6 Astra Ultra.

**Result.** The new module `lean/Q1/SignedAbsoluteCollision.lean`
proves the requested six-product absolute-value inequality. Its targeted
build, explicit five-declaration axiom audit, and targeted imported-
environment Leanchecker replay all returned exit 0. All five declarations
use only `propext`, `Classical.choice`, and `Quot.sound`.

The source is frozen at SHA-256
`dcba412797c23aecd2709f81be9b2f7781b867abecb9c3e0403697408e7214be`.
It imports the unchanged `Q1.SignedCollision` module. The new argument
is proved from elementary real hypotheses; the desired absolute-value
inequality is not assumed. No actual Sidon orbit partition, clock
assignment, output-clock PSD source, physical-envelope bound, or original
Q1 conclusion is formalized by this module.

## Mathematical statements and the combinatorial boundary

Let a,b,p,q,r be nonnegative real numbers satisfying
`p+q+r=a+b=S>0`. The definition `crossSum` is exactly the sum
of the six ordered unequal-slot terms

~~~
F=|(a-p)(b-q)|+|(a-p)(b-r)|+|(a-q)(b-p)|
  +|(a-q)(b-r)|+|(a-r)(b-p)|+|(a-r)(b-q)|.
~~~

Repeated coordinate values are retained in all six slots; the definition
does not deduplicate equal products. The module proves

~~~
F<=S^2+(p^2+q^2+r^2)-2ab<=4(p^2+q^2+r^2),
2F/A<=2[4(p^2+q^2+r^2)/A]       when A>0.
~~~

The proof first bounds one product after multiplying by S. If both
factors are nonnegative, the exact polynomial identity

~~~
S(a-p)(b-q)+aq(a-p)+bp(b-q)=abr
~~~

gives its upper bound. If the product is nonpositive its absolute value
is its negative. Both factors cannot be negative, since that would
contradict `p+q+r=a+b` and `r>=0`. The single-product theorem itself
does not require S>0. The sum theorem applies it to all six orders,
uses the exact raw-product sum, and cancels S using the explicit positive
hypothesis. The four-squares bound follows from the nonnegativity of
`(p-q)^2`, `(p-r)^2`, `(q-r)^2` and `ab>=0`. The final theorem
divides only by an explicitly positive A.

In the analytical collision argument one would set
`a=n-x`, `b=n-y`, and the three coordinates to `n-u_i`, obtaining
S from the equal triple sums. The formal module does not construct these
endpoints, prove their unique births, count their matching orbits, or
identify A with `aut(U)aut(V)`. In particular, calling `2F/A` the
actual absolute retirement still requires that separate combinatorial
identification. The newly established analytical bound for absolute
Born contributions by three times Born is also outside this module.

## Complete new declaration inventory

All five names have the prefix `Erdos1191Q1.SignedAbsoluteCollision.`.

| Name | Kind and proved scope |
|---|---|
| `crossSum` | Noncomputable definition of the six absolute cross products |
| `cross_abs_mul_le` | Theorem deriving the multiplied single-product bound by sign cases |
| `crossSum_le_reduced` | Theorem summing all six bounds, retaining the negative term `-2ab` |
| `crossSum_le_four_squares` | Theorem proving the four-square upper bound |
| `absolute_retired_le_twice_born` | Theorem giving the normalized inequality for a positive divisor |

There is one definition and four theorems. The Lean LSP diagnostic pass
on the final source returned success with no warnings or errors. The
linear-causal agent separately read the source and supported the theorem
semantics and the external combinatorial boundary; its independently
owned review is `research/signed_absolute_collision_review.md`.

## Actual targeted verification

All commands ran in the existing pinned Lean project directory
`q1_lean4_execution_2026-09-05/lean`. On 2026-09-05 UTC:

| Action | Arguments after Lake | Start to finish | Exit |
|---|---|---|---:|
| Targeted build | `build Q1.SignedAbsoluteCollision` | 11:11:48.752702 to 11:11:54.772529 | 0 |
| Explicit axiom audit | `env lean evidence/signed_absolute_collision_axioms.lean` | 11:11:54.775858 to 11:11:56.853395 | 0 |
| Kernel replay | `env leanchecker Q1.SignedAbsoluteCollision` | 11:12:04.097974 to 11:12:11.103627 | 0 |

The build printed `Built Q1.SignedAbsoluteCollision` and successful
completion. Each of the five explicit `#print axioms` commands returned
exactly the three allowed axioms. The kernel replay had empty stdout and
stderr; its actual process return code, rather than its lack of output,
records success.

The axiom driver inventory exactly matches every new source declaration,
with one parsed result per declaration. The token scan found no `sorry`,
`admit`, `axiom`, `native_decide`, or `unsafe`. The proof assurance
comes from successful Lean compilation and explicit axiom output, not
from the source scan alone.

Every build/audit command recorded its exact arguments, working directory,
complete separate stdout/stderr and hashes, start/end times, elapsed time,
observed exit code, and input hashes before/after. The frozen eighteen-file
input snapshot covers the fourteen earlier Lean source/configuration
files, both new algebra modules, and this module's axiom driver and
verification runner. Every unchanged-input gate passed. The result also
hashes the compiled artifacts. A subsequent read-only audit matched all
saved output bytes and every current input/artifact hash to the records.
It did not rerun a successful compiler check.

The replay separately bound its source files, compiled artifacts, prior
result/runtime records, runner and checker executable before and after.
A post-replay `lake env which leanchecker` probe confirmed the recorded
executable resolution and hash. That probe was not another replay.
Leanchecker used a new process in its existing imported environment. It
did not freshly recheck every dependency and is Lean's own kernel,
not an independent external checker.

## Evidence paths and hashes

All following evidence files are under `lean/evidence/` and have the
unique `signed_absolute_collision_` prefix:

- `verify.py` and `checker_verify.py`: instrumented runners.
- `build.run.json`, `build.stdout.txt`, `build.stderr.txt`.
- `axioms.lean`, `axioms.run.json`, `axioms.stdout.txt`, `axioms.stderr.txt`.
- `checker.run.json`, `checker.stdout.txt`, `checker.stderr.txt`.
- `result.json`: exact declaration/axiom inventory and source/artifact hashes.
- `runtime.json`: actual Lean/Lake versions, resolved executable hashes,
  Python executable/version/hash, and the captured runtime probes.
- `checker_resolution.run.json`: the post-replay resolution observation.

For example, the full build-record name is
`lean/evidence/signed_absolute_collision_build.run.json`.

| Artifact | SHA-256 |
|---|---|
| Result | `d8b2c290fd37ad22f8bd3d75814cbf08e0d19856996d2d3b40d79be96b441110` |
| Build record | `887fae151cf213e3b1464a351026aeb8b3751213ae374466a00f833495501d71` |
| Axiom record | `4f3c9a34715c234b2a18649bc8fe5fa62d6a7e8c16d50111f15c2076e67a7246` |
| Checker record | `d1f7d19752c8ff20a74dd220209f25d5aaab3290eac5a69344560663f61a3ad1` |
| Verification runner | `ee2b1a94bdd1180181253a2d747f3be57d70560a1631b4be6becc60d8eef4fec` |
| Checker runner | `a83be887f39e76ab6875934ac2fc47e45712b0a1f995a1295abbcccd81724169` |

Runtime capture reports Lean 4.33.0, commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`, and Lake
`5.0.0-src+d8b1897`. No pinned version or configuration changed.

The existing aggregate `Q1.lean`, `Q1/AxiomAudit.lean`, previous
source modules and evidence, and status files were not edited. The
earlier 98-declaration scope was not rerun. This new module was built
as an explicit target and is absent from the unchanged aggregate
imports. These five new algebra declarations do not prove original Q1.
