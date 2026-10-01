# Independent semantic review of the absolute collision module

Date: 2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Verdict:** PASS for the five declarations in
`lean/Q1/SignedAbsoluteCollision.lean`: one definition and four theorems.
The absolute comparison is actually derived from six real cross products;
it is not assumed through a partition, an energy bound, or a hypothesis
equivalent to the conclusion. No source correction is requested.

This review binds to the complete 4,512-byte source with SHA256

```
dcba412797c23aecd2709f81be9b2f7781b867abecb9c3e0403697408e7214be
```

The frozen file was read completely in tool chunk `97a361`. Current
source and evidence bindings were inspected at actual UTC time
`2026-09-05T11:13:14.373417+00:00` in chunk `8e3ddd`, and the
checker's separately named source-and-artifact gate was inspected at
`2026-09-05T11:13:53.225805+00:00` in chunk `2210b7`.

The reviewer ran no Lean build, axiom audit, checker, or mathematical
test. Execution facts below are read from the author's completed,
source-bound records and checked against their current saved bytes.
Only this review file was written. Lean, status files, and run records
were preserved.

## 1. Definition and exact hypotheses

The definition `crossSum a b p q r` contains exactly

```
|(a-p)(b-q)| + |(a-p)(b-r)| + |(a-q)(b-p)|
 + |(a-q)(b-r)| + |(a-r)(b-p)| + |(a-r)(b-q)|.
```

These are the six ordered unequal SLOT pairs, with no omission or
extra diagonal. Numeric values p,q,r may coincide. Such coincidences
do not collapse occurrences in the explicit expression, which is the
correct algebraic convention for repeated endpoint slots.

The elementary lemma assumes a,b,p,q,r are nonnegative reals and
p+q+r=a+b. The next two theorems additionally require a+b>0; the final
division theorem also requires divisor>0. These are direct numeric
hypotheses, not positivity of a target sum or an assumed retirement
estimate. They include the actual newest-endpoint substitutions used
in the analytical note, where all five distances are strictly positive.

## 2. The product estimate is proved by signs and a polynomial identity

`cross_abs_mul_le` establishes

```
(a+b)|(a-p)(b-q)| <= -(a+b)(a-p)(b-q)+2ab r.
```

Its proved identity is

```
(a+b)(a-p)(b-q)+a q(a-p)+b p(b-q)=ab r.
```

This follows after substituting r=a+b-p-q. When both factors a-p
and b-q are nonnegative, the last two terms on the left are
nonnegative, so the desired absolute estimate follows. When the factors
have opposite signs, the absolute value is the negation of their product
and the remaining term 2ab r is nonnegative. Both factors cannot be
strictly negative: that would give p+q>a+b while r>=0 and the sum
hypothesis give p+q<=a+b.

All four cases occur explicitly in the proof. Zero values need no
division or implicit strict positivity. The impossible case is discharged
from the stated hypotheses, not from a new assumption about Sidon sets.

## 3. Six-term summation and division retain the correct factors

`crossSum_le_reduced` invokes the preceding lemma in all six orders.
Each missing coordinate appears twice, so the added terms sum to
4ab(p+q+r). It proves the signed-product identity

```
sum_(i!=j)(a-delta_i)(b-delta_j)
 =6ab-(a+b)^2-(p^2+q^2+r^2),
```

then cancels the positive factor a+b. The conclusion is precisely

```
crossSum <= (a+b)^2+(p^2+q^2+r^2)-2ab.
```

Thus the negative twice-product term of the stronger analytical estimate
is retained. It is not replaced by a free sign conjecture.

`crossSum_le_four_squares` proves
(p+q+r)^2<=3(p^2+q^2+r^2) from the three nonnegative squares
(p-q)^2, (p-r)^2, (q-r)^2. With ab>=0 and the reduced estimate it
then obtains crossSum<=4(p^2+q^2+r^2).

Finally, `absolute_retired_le_twice_born` multiplies by 2 and divides
by the explicitly positive divisor to give

```
2 crossSum/divisor <= 2[4(p^2+q^2+r^2)/divisor].
```

The factor 2 on the absolute-retirement expression and the factor 4
in the Born expression match equations (1)--(3) of
`signed_output_clock_source.md`. No target-comparison hypothesis is
present in this theorem or its supporting lemmas.

## 4. Observed saved verification evidence

The following completed commands all used cwd
`/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/lean`.
Their recorded executable launcher was `/Users/USER/.elan/bin/lake`.

| Saved operation | Actual recorded UTC interval | Recorded return code |
|---|---|---:|
| `lake build Q1.SignedAbsoluteCollision` | 11:11:48.752702 to 11:11:54.772529 | 0 |
| `lake env lean evidence/signed_absolute_collision_axioms.lean` | 11:11:54.775858 to 11:11:56.853395 | 0 |
| `lake env leanchecker Q1.SignedAbsoluteCollision` | 11:12:04.097974 to 11:12:11.103627 | 0 |

All intervals above are on 2026-09-05. The build stdout records the
successful module build. The explicit axiom driver names exactly the
definition and four theorems reviewed here. Every one of its five output
entries lists only `propext`, `Classical.choice`, and `Quot.sound`.
The checker stdout and stderr are empty; its return code is zero.
All three saved stderr files are empty.

The build and axiom records have equal before/after hashes for all 18
listed inputs. The checker record has equal before/after hashes for its
26 listed source, artifact, runner, and result inputs, and separately
records an unchanged checker executable hash. The reviewer independently
compared current listed input and compiled-artifact bytes with these
recorded snapshots and found no mismatches. Each separate stdout/stderr
file matches both its recorded hash and the complete text in its record.

The precise record bindings are:

```
lean/evidence/signed_absolute_collision_build.run.json
887fae151cf213e3b1464a351026aeb8b3751213ae374466a00f833495501d71

lean/evidence/signed_absolute_collision_axioms.run.json
4f3c9a34715c234b2a18649bc8fe5fa62d6a7e8c16d50111f15c2076e67a7246

lean/evidence/signed_absolute_collision_checker.run.json
d1f7d19752c8ff20a74dd220209f25d5aaab3290eac5a69344560663f61a3ad1

lean/evidence/signed_absolute_collision_result.json
d8b2c290fd37ad22f8bd3d75814cbf08e0d19856996d2d3b40d79be96b441110

lean/evidence/signed_absolute_collision_runtime.json
18fbb244cb8f8f52a3ab4f54650b6f4eb90ae6905f4e98bbadef813e7a385ea8
```

The saved runtime is Lean 4.33.0, commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`. The checker operation
replays this module in its imported environment using Lean's own kernel.
It is not a new replay of every imported dependency or an independent
external proof checker. The five-name audit is also not an audit rerun
of all pre-existing project declarations.

## 5. Exact formalization boundary

To interpret the final inequality as an actual collision bound, one must
still supply the analytical substitutions

```
p=n-u_1, q=n-u_2, r=n-u_3,
a=n-x, b=n-y,
divisor=aut(U)aut(V),
actual Rabs=2 crossSum/divisor,
actual B=4(p^2+q^2+r^2)/divisor.
```

The Lean module proves the real inequality for any permitted inputs.
It does not formalize the multiset orbit count, the doubled-pattern
factor cancellation, the injective identification with actual physical
source pairs, the exhaustion of all stage records, or the nonnegative
Born-only remainder. Those are the separate reviewed analytical results.
Consequently the actual Sidon stage statement Rabs_j<=2B_j is not
yet a Lean theorem furnished by this module, even though the essential
six-product inequality no longer has to be assumed.

The module also does not formalize absolute Born<=3Born, the output-clock
Gram source, its PSD or nonnegative entries, historical capacity,
future-block allocation, or a baseline-margin estimate. No new original-Q1
conclusion follows. The module's introductory scope comment accurately
states this boundary; no semantic overclaim was found.
