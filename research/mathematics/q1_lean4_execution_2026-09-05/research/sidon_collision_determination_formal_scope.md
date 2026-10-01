# Actual Sidon collision determination and finite cardinality

The new module `lean/Q1/SidonCollisionDetermination.lean` proves that actual
Sidon endpoint records are determined by their three designated near
coordinates. It then proves a finite cardinality bound by an actual injection
into a threefold Cartesian product. All seven new declarations passed the
targeted build, explicit axiom audit, and imported-environment checker replay.

This is a combinatorial count for a literal finite set. No uniqueness or
cardinality conclusion is assumed. The proved upper bound is `|K|³`; the
sharper analytical `2 binom(|K|,3)` count and the complete matching-orbit
formalization remain outside this module.

## Exact endpoint determination

The actual endpoint set is `A : Set ℕ` with the unchanged
`Erdos1191Q1.Sidon A` predicate. Given actual members `n,ell,v,y∈A` with
`ell<n` and `v<n`, the module proves

\[
 n+y-\ell-v\ne0\quad\text{in }\mathbb Z.
\]

Indeed, equality to zero would give the actual natural two-sum equality
`n+y=ell+v`. Sidonicity forces `n=ell` or `n=v`, both impossible. This proof
does not require an unproved far-gap assumption, nor does it require more
pairwise-distinctness premises than those already stated.

For two actual endpoint equations

\[
 \ell+u+v=n+x+y,\qquad \ell+u'+v=n+x'+y,
\]

with `u,x,u',x'∈A`, the same nonzero gap is `u-x=u'-x'`. The already verified
actual Sidon signed-difference uniqueness then proves `u=u'` and `x=x'`.
All subtraction in this argument is integer subtraction. The conclusion is
valid for positive or negative far gaps and is not a hypothesis.

## Literal finite record set and repetitions

Fix newest value `n` and a finite candidate set `K : Finset ℕ`. A record has
type `((ℕ×ℕ)×ℕ)×(ℕ×ℕ)` and is written

\[
 T=(((\ell,v),y),(u,x)),\qquad
 U=\{u,v,\ell\},\quad V=\{x,y,n\}.
\]

The finite set `collisions A K n` consists **exactly** of records satisfying

- `ell,v,y∈K`;
- all six endpoint slots belong to the actual set `A`;
- `u,v,x,y<ell<n`;
- `ell+u+v=n+x+y`.

The definition filters the finite product `K³ × (range n)²`.
`mem_collisions_iff` proves that its range restrictions on `u,x` add no hidden
condition: they follow from `u,x<ell<n` and disappear from the exact membership
characterization. The construction is finite even when `A` is infinite.

No inequality `u<v` or `x<y` is imposed. Thus the designation “near” means
that `ell,v,y` are the chosen coordinates in `K`; the definition is deliberately
large enough to contain every low-defect record with its analytically chosen
closer endpoints. Geometric clustering and the existence of those closer
choices are not assumed inside the cardinality proof and are not proved by
this module.

Repeated old slots within a triple are permitted, including `u=v` or `x=y`.
Under actual Sidonicity the module proves
`Disjoint (triple u v ell) (triple x y n)` by applying the actual eligible
endpoint certificate to

\[
 (u-x)-(y-v)=n-\ell.
\]

Therefore distinct collision sides cannot share an endpoint, but the proof
does not replace either multiset by an ordinary set or discard within-side
multiplicities. In particular, the tuple model is not restricted to the
six-distinct class merely to obtain its count.

## The proved cardinality implication

Projection to the first component is the concrete map

\[
 (((\ell,v),y),(u,x))\longmapsto((\ell,v),y)\in K^3.
\]

On two actual records with the same image, equality of the three coordinates
and the endpoint-determination theorem force equality of the far pair. This
proves injectivity on the finite collision set. The finite-set injection
theorem and the Cartesian-product cardinality formula yield

\[
 \#\operatorname{collisions}(A,K,n)\le(\#K)^3.
\]

This counts the literal tuples. An unordered multiset collision with a chosen
near endpoint on each side supplies such a record; choosing the closer
endpoints in the analytical low-defect regime gives the intended application.
A separate quotient-of-multisets cardinality theorem and the sharper count
using an unordered three-element near set with two assignments have not been
formalized here. Neither an automorphism divisor nor a signed source-record
multiplicity is inserted into this tuple cardinality.

The local Sidon interval count and the low-defect clustering theorem remain
analytical. Combining their already proved analytical bounds with `|K|³`
would keep the same logarithmic summability threshold with a weaker constant;
that combined summability theorem is not claimed as Lean-verified. Growth
conditions, full collision partition, Gram kernels, energy estimates, and Q1
are likewise outside this module.

## Exact seven-declaration audit

All names have prefix `Erdos1191Q1.SidonCollisionDetermination.`.

| Name | Kind | Actual audited axioms |
|---|---|---|
| `far_gap_ne_zero` | theorem | `propext`, `Quot.sound` |
| `far_pair_unique` | theorem | `propext`, `Quot.sound` |
| `collisions` | definition | `propext`, `Classical.choice`, `Quot.sound` |
| `mem_collisions_iff` | theorem | `propext`, `Classical.choice`, `Quot.sound` |
| `collision_multisets_disjoint` | theorem | `propext`, `Classical.choice`, `Quot.sound` |
| `near_projection_injective` | theorem | `propext`, `Classical.choice`, `Quot.sound` |
| `collisions_card_le_cube` | theorem | `propext`, `Classical.choice`, `Quot.sound` |

The audit driver names each declaration exactly once, and its complete output
contains exactly those seven names. The source scan found no prohibited proof
escape tokens. The fixed source had no LSP diagnostics before the substantive
executions. No custom axiom, placeholder proof, native decision procedure, or
unsafe proof shortcut was introduced.

## Actual verification and preservation

Each instrumented execution saves exact argv, cwd, UTC interval, elapsed time,
observed return code, full separate stdout/stderr, embedded complete outputs,
their hashes, and source hashes before and after.

| Execution | Interval on 2026-09-05, UTC | Result |
|---|---|---|
| `lake build Q1.SidonCollisionDetermination` | 13:36:01.510911–13:36:10.180191 | exit 0 |
| Explicit seven-name axiom audit | 13:36:10.204168–13:36:13.439739 | exit 0; exact coverage |
| `lake env leanchecker Q1.SidonCollisionDetermination` | 13:37:10.455564–13:37:24.436422 | exit 0; empty stdout/stderr |

The build/audit snapshot contains 23 source, configuration, driver, runner,
and preservation-manifest files. The checker binds 31 source, artifact, and
evidence files. All before/after hashes agree. Each command additionally
checks all 281 files of `evidence/goal9_reviewed_research.json` before and
after execution. The new preservation manifest records the original snapshot
path and its hash; no previous snapshot was rewritten.

Runtime probes record pinned Lean 4.33.0, commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`, Lake
`5.0.0-src+d8b1897`, Python 3.14.6, and resolved executable paths and hashes.
The checker replays the new module in the existing imported environment with
Lean's kernel. It is not fresh replay of all imported dependencies or an
independent external checker. A separately labeled post-replay path-resolution
probe confirms the checker executable without another checker replay.

The final byte readback passed at **13:37:57.654716 UTC**, checking every saved
output, bound source/artifact, runtime executable, and all 281 preserved files.
There was no failed substantive execution or failed readback in this task.
The parent was told when preservation gates began and when this final
observation completed, so governance updates could resume afterward. No
successful prior suite was rerun.

Frozen source SHA-256:
`7b21c6150011439e3f01c7c4ba172002094d21a9298eba7f33ce649f5ea9db64`.

Evidence paths have prefix `lean/evidence/sidon_collision_determination_`:

| Suffix | SHA-256 |
|---|---|
| `verify.py` | `5d23d333c30ee2cafe77f0dcc08a650db0881ee1ac4620fcc0a7b6d47fd14e96` |
| `checker_verify.py` | `9f4c015a53b495410ad891cecfce3c55f76be83fe02d55b794c1621205b7e9d6` |
| `prior_files.json` | `09fa3f5fe6adac144da41ec61daf66e329c559e3bfc8b374b0969958fb248162` |
| `result.json` | `a2065d5987dde9d5deb305ff96bd4e10b2c18deda8a45ca28b824d0016307455` |
| `build.run.json` | `2bc1526b729814d2766e91bb44ed3c6635f3d299b7ce11d91ea4941a50de2fdb` |
| `axioms.run.json` | `d948c4bb646d03c2ae6a670ef2d419f5d3509b43359e64ab099f0323125af2cc` |
| `checker.run.json` | `3a41dce57b8bb99c0a8a8e622747692d81a7da8772dfc6e7a4085390712b4c3a` |
| `runtime.json` | `02196c9db0d464a5d8e39fcd137354755b579264d8fbe4ec4b2d6cc167d2e54c` |
| `checker_resolution.run.json` | `80bf311931e9833b200f7a14e8a899adb72a1d3d0229a9b1ac23412aa60b3af9` |
| `readback.json` | `733fddaf7acf74b1b3f3f5e8d0438a1357b955c150790d13d18d52dc51223631` |

The final readback record contains the complete hash inventory, including the
post-replay resolution record and the readback runner. The aggregate,
configuration, prior verified sources and evidence, and research status were
not edited by this task. The current goal and original Q1 remain unresolved.
