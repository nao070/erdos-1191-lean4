# Independent review of the retirement-clock tail

2026-09-05. Reviewer: `/root/causal_telescoping`, GPT-6 Astra Ultra.
Ownership: this review and an appended reference in the causal note;
the parent's tail source was not edited.

**Result:** the complete mathematical argument and equations (1)–(4)
of `late_retirement_tail.md` pass independent derivation. The parent
corrected the minor real-coordinate/integer-bin distinction in §4,
and the resulting complete source was reread and supported. The near-birth signed retirement
term, the source-time commutator, and the single physical margin remain
uncontrolled. This is a mathematical review, not Lean or numerical
verification, and does not resolve original Q1.

Current fully reviewed source SHA256:

```
5dbcf37e0a7fd687a8371c5f71c04b11cab45992a622ebe31ebba15d469963ab
```

Earlier snapshot, before the coordinate prose clarification, SHA256:

```
3de34390d8d97dd3688d422fd97d9bd60c5a5bb5259f6eb49a5c1d60657cbeca
```

## 1. Literal source-pair counting

For two distinct labels `d=a_b-a_i` and `e=a_b-a_j` in the same
birth class, their positive difference is `|a_i-a_j|`, with both
endpoints strictly earlier than `b`. Therefore such a pair is already
used when born and cannot retire later. Every retired unordered pair
whose later source birth is `b` has exactly one endpoint in `G_b`
and one in `F_(b-1)`. Its unique orientation by these two classes gives

```
# possible pairs = |G_b| |F_(b-1)|
                 = (b-1)^2(b-2)/2 <= b^3/2.
```

There is no factor two. At `b=2`, `F_1` is empty, so no mixed pair
exists. Allowing nonretiring pairs in the displayed count only makes
it an upper bound, which is the direction required.

The physical output `|d-e|` is fixed by the pair. If it ever belongs
to the sequence's difference bank, difference uniqueness supplies
one actual birth `r`. No further sum over putative retirement ranks
is permitted or needed.

## 2. Actual retirement-time price and the exponent threshold

For a label whose birth is at most `b`, both its defining point and
its birth-prefix mean lie in `[a_1,a_b]`. Hence `|g_d g_e|<=H_b^2`.
For the actual retirement `r>b`, monotonicity gives `H_r>=H_b`, and

```
q_r=r(r-1)/2 >= r^2/4,
w_r |g_d g_e|
 <= H_b^2/(q_r^2 H_r^2)
 <= 16/r^4.
```

The stipulated tail condition `r>=b(log b)^alpha` therefore gives
`16/[b^4(log b)^(4alpha)]` per pair. Multiplication by the count
from §1 gives exactly `8/[b(log b)^(4alpha)]` for source birth `b`.
Summing over `b>=3` proves source equation (1). Its convergence uses
`4alpha>1`; no cap or onset is involved. Because `log b>1` for
`b>=3`, the cutoff is genuinely later than `b` for the stated
positive `alpha`.

For `p=4alpha>1`, the function `1/[x(log x)^p]` is positive and
decreasing for `x>=3`. Thus

```
sum_(b=3..infinity) 1/[b(log b)^p]
 <= 1/[3(log 3)^p] + integral_(3..infinity) dx/[x(log x)^p]
 = 1/[3(log 3)^p] + (log 3)^(1-p)/(p-1).
```

This verifies the explicit constant in source equation (3), including
the first discrete term and the factor eight. The estimate is uniform
in the entire sequence and terminal horizon.

## 3. The exact signed remainder and its scope

Let `R_T^far` be the signed sum over source equation (1)'s pairs with
actual `r<=T`. The absolute sum of its infinite series is bounded by
the displayed constant `C_alpha`; hence

```
R_T(w) = R_T^near + R_T^far,
|R_T^far| <= C_alpha,
2B_T(w)+2R_T^near+D_T(w) = A_T(w)-2R_T^far.
```

This proves source equation (4), with an error of absolute value at
most `2C_alpha`. The tail has an actual absolutely convergent signed
limit as the horizon increases. The statement is stronger than a
bound on each finite horizon separately.

The price is `w_r` throughout. For source-time prices `w_b`, the
decay factor `r^-4` used above is absent. Likewise, the commutator
price `w_b-w_r` includes the earlier price and is not dominated by
the late price. The source correctly excludes both from this result.
It also retains the physical-margin term in causal equation (24).
There is no sign estimate or required-scale upper bound for the
remaining `R_T^near`.

## 4. A minor coordinate clarification

For every remaining near pair,

```
0 < log_2 r - log_2 b < alpha log_2(log b).
```

This is the exact real logarithmic-coordinate statement. If “dyadic
index” instead means the integer bin `floor(log_2 n)`, then

```
floor(log_2 r)-floor(log_2 b) < alpha log_2(log b)+1.
```

Thus the initially reviewed source's sentence about the dyadic index
lag requires either the real-coordinate interpretation or this harmless
additive one. Both show an unbounded `O_alpha(log log b)` bin lag;
neither gives a bounded-lag reduction. This does not affect any of
source equations (1)–(4). The parent was notified and corrected the
source to state both coordinate conventions exactly as above. The
complete corrected source was reread before recording the current hash.

## 5. Outcome

The uniformly absolutely summable late-retirement tail is supported.
In the causal Abel identity it can be absorbed into a bounded error,
so the unbounded retirement obstruction is restricted to
`b<r<b(log b)^alpha` for any fixed `alpha>1/4`. The remaining joint
near-retirement and physical-margin inequality is still unproved.
