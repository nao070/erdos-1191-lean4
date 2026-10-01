# Prefix-chosen scalar gains without a sign assumption on the Born term

2026-09-05. `/root`, GPT-6 Astra Ultra. Status: a uniform scalar carrier
lemma and a sharper remaining sign condition. The single physical-margin
problem and original Q1 remain unresolved. This note is not Lean verified.

Use one actual Sidon prefix `P_N`, `q=binom(N,2)`, `H=a_N-a_1`, and
the actual birth-linear vector `z`, with each class centered and
`|z_d|<=1`. Set

```
B = sum_({d,e} born) (z_d+z_e),
X = sum_({d,e} mixed-born) z_d z_e,
S = sum_d z_d^2.
```

Fix a known bound `m<=R N` for future-block size, where `R>0` is fixed.
Let `D_* = q^2+R N q`, assuming `N>=2`. Define from this prefix alone

```
s = 1 if B>=0, and -1 otherwise,
t = |B|/D_*,
u_d = 1+s t z_d.                                         (1)
```

There are at most `binom(q,2)` Born pairs, so `|B|<=q(q-1)<=q^2`.
Hence `0<=t<=1`, `u>=0`, and all literal prefix masses stay equal to
their uniform masses. On the full bank its trace is `q+t^2 S`.
The choice in (1) uses no future endpoints, actual future span, or
future moment. It is the same choice for every such block size.

For any compatible actual future block with positive interval
denominator, compare the exact fixed-matrix historical capacity minus
its mass-only raw demand with the uniform carrier. The existing
pair identity gives exactly

```
I_hist(u) = s t B + t^2 (X-mS/2).                         (2)
```

This identity is valid for either sign because the entire scalar
matrix `u u^T` is nonnegative. It does not apply the high-to-low
monotone injection to the minus sign.

As a sum over a subset of unordered label pairs,
`|X|<=(sum_d |z_d|)^2/2<=q^2/2`, while `S<=q`. Therefore

```
X-mS/2 >= -(q^2+R N q)/2 = -D_*/2.
```

Substitution into (2) proves the uniform actual comparison

```
I_hist(u) >= B^2/(2D_*),
I_hist(u)/q^2 >= (B/q^2)^2/[2(1+R N/q)].                 (3)
```

When `B=0` this reduces to the uniform carrier and zero gain. For
every nonzero B it is a strictly positive raw comparison. This is
not automatically a positive-part gain if the baseline raw demand
is negative. The positivity assertion here is restricted to the
actual next block `m=N` at the established extended good epochs,
using `R>=1` (for example `R=1`), where `D<=33H_N` and
`H_N<=C N^2 log(2N)`. Since the trace is at
most `2q`, its mass-only raw demand satisfies

```
delta_u >= (Nq/2)[(N-1)/(66C log(2N))-2] > 0
```

eventually, and `delta_J>=delta_u`. This is not a positivity
assertion for every arbitrary `m<=RN` in the general lemma.

Consequently, if at a collection of those epochs

```
|B| >= kappa q^2/sqrt(log(2N))                            (4)
```

with fixed `kappa>0`, then (3) gives an individually normalized
gain of order `1/log(2N)`, using choices determined by the old
prefix. In particular the terminal-cap example that makes every
bounded monotone-plus parameter lose does not rule out all scalar
choices: its negative B is handled by the minus choice (1).
The example retains its original scope, and no global cap conclusion
is inferred from it.

For a complementary condition, consider the two-channel carrier
`W=J+zz^T/8` and its actual future-moment demand. On extended good
epochs assume the proved uniform lower bound
`LB>=c q^2/log(2N)`, with fixed `c>0`, and `m=N`. The exact
historical comparison is

```
I_hist(W) = (2X+LB-mS)/16.                               (5)
```

For this same actual next block at sufficiently large extended good
epochs, the mass-only demand of W is at least
`(Nq/2)[(N-1)/(66C log(2N))-9/8]>0`. Its moment demand is no smaller.
Thus both demands used in (5) are positive on this stated range.

If `X>=-c q^2/[4log(2N)]`, then (5) is at least
`c q^2/[32log(2N)]-Nq/16`, which is eventually positive and has
normalized order `1/log(2N)`. This choice also uses no sign of B.

Thus one useful remaining prefix condition is the following dichotomy:
at enough extended good epochs to preserve reciprocal-log divergence,
either (4) holds, or

```
X >= -c q^2/[4log(2N)].                                  (6)
```

A sufficiently frequent failure of both conditions would require a
small linear Born statistic and a negative quadratic total on the
same actual, gap-constrained birth vector. The direct fiber work can
therefore focus on that joint regime rather than demand an unnecessary
nonnegative sign for B. This dichotomy has not been proved for actual
capped histories; (3) alone supplies no frequency estimate for (4).

Even if the dichotomy were proved, the individual historical comparisons
would still have to be coupled to one physical source, with its full
baseline margin and overlap/span costs. No separate budget per sign,
prefix, or future block is introduced by (1)--(6). The note supplies
neither that final coupling nor an original Q1 proof.
