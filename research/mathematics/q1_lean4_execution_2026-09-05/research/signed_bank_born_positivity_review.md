# Independent review of signed-bank full Born positivity

Date: 2026-09-05. Reviewer: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Reviewed source: `signed_bank_born_positivity.md`, authored by
`/root/causal_telescoping`. The complete note was read. The exact
support convention and good-epoch hypotheses were cross-checked against
`future_moment_demand.md` and `coherent_birth_linear_envelope.md`.
The baseline boundary was checked against
`signed_bank_envelope_geometry.md`.

**Verdict:** the finite full-Born positivity theorem, its odd-monotone
and symmetric mixed extensions, the fixed-matrix historical identity,
the signed-support future moment demand, and the stated good-epoch gain
are mathematically supported. No material correction is required. A
sentence concerning where same-birth source pairs occur was flagged to
the author for precision; the distinction is recorded below and its
resolution is recorded in the final-source follow-up. The source
was not edited by this reviewer. No experiment or Lean run was needed
or performed. The existing 82 audited Lean declarations concern the
earlier positive-bank framework; this review does not extend their
formal scope.

## 1. The pair partition is exhaustive and has the correct multiplicities

Every used pair of distinct signed labels determines one canonical
numeric relation `x+y=z`, `0<x<=y`. For same-sign sources, take the
smaller magnitude and the positive output as the summands. For
opposite-sign sources, their magnitudes are the summands. This rule is
unique; no point-endpoint pattern or six-distinct condition is imposed.

For `x<y`, the pairs with output `x` are `{y,z}` and `{-z,-y}`;
those with output `y` are `{x,z}` and `{-z,-x}`; those with output
`z` are `{-x,y}` and `{-y,x}`. These are six distinct unordered
pairs. They give the three product totals

```
2phi(y)phi(z),  2phi(x)phi(z),  -2phi(x)phi(y).
```

The pair `{x,y}` does not belong to this same Schur triple. If its
output is used, it has the separate relation `(y-x)+x=y`.

For `x=y`, the two positive-product pairs are `{x,2x}` and
`{-2x,-x}`, while `{-x,x}` is one negative-product pair. The source
labels in the latter pair are distinct, even though their magnitudes
agree. Thus its contribution is `-phi(x)^2`, without a factor two.
This verifies both the repeated-label count and all repeated point-
endpoint configurations: the partition is on actual signed labels and
does not delete any such configuration.

## 2. Source-clock prices, ties, and equal-birth pairs

Let `M=max(tau(x),tau(y),tau(z))`. A pair is Born exactly when its
output clock is no greater than its maximum source clock. Therefore
every Born pair in one numeric Schur triple has maximum source clock
**equal to M**. An arbitrary nonnegative weight `alpha_M` is common
to every retained term. No monotonicity of the sequence `alpha` is
used.

For `x<y`, a unique latest clock at `x` retires the output-`x`
group and leaves
`2phi(x)[phi(z)-phi(y)]`. A unique latest clock at `y` similarly
leaves `2phi(y)[phi(z)-phi(x)]`. A unique latest clock at `z`
leaves `2phi(z)[phi(x)+phi(y)]`. All three expressions are
nonnegative for the stated odd monotone feature. If at least two
clocks attain M, all groups are Born; their sum is

```
2phi(x)[phi(z)-phi(y)]+2phi(y)phi(z) >= 0.
```

For the linear raw feature these reduce to the source's
`2x^2`, `2y^2`, `2z^2`, and `2(x^2+xy+y^2)` respectively.

In the unique-maximum case, each Born pair contains the unique
latest label, so its two source births differ. If the lower two
clocks tie, the retired group can contain equal-birth sources. In
the tied-maximum case, equal-birth sources can also be Born. Thus
same-birth pairs must remain in the complete partition and cannot
be removed from the full Born functional. This is the precision
requested of the wording in source section 2; it changes no formula.

For `x=y`, the two possible retained totals are

```
2phi(x)phi(2x),
2phi(x)phi(2x)-phi(x)^2 >= phi(x)^2.
```

The second includes the equal-clock formal case. The actual bank
cannot have `tau(x)=tau(2x)`: the difference of these two positive
labels in one birth star would already be an old positive label x.
Likewise an actual Schur triple cannot have all three clocks equal.
Checking those formal tie cases anyway is valid and strengthens the
exhaustiveness of the finite argument.

The symmetric mixed-feature extension has the stated factor `1/2`.
For instance, a unique latest x contributes

```
phi(x)[psi(z)-psi(y)]+psi(x)[phi(z)-phi(y)] >= 0.
```

The doubled-label negative term is `-phi(x)psi(x)`, once. Its
positive terms and all tie cases are nonnegative by the same
monotonicity. The source correctly separates this bilinear sign
statement from PSD: an arbitrary symmetric mixed kernel, or an
arbitrary sequence of nonnegative source-clock weights, does not
by itself supply a PSD matrix.

## 3. The signed historical identity includes same-birth retirement

For the one fixed terminal matrix
`W=J+lambda zz^T`, `0<=lambda<=1`, every entry is nonnegative.
The feature is odd on each signed prefix, with a **fixed terminal
normalization**. Hence its prefix sums vanish, and terminal mass
and trace are `Q^2` and `Q+lambda S`.

For fixed output t, the unmasked prefix correlation increases as
sources are added. If t is used at rank r, the old-label mask makes
the correlation zero from rank r onwards. Its historical maximum
is exactly the sum of source-pair entries available strictly before
r. If t never appears by N, the maximum is its terminal sum.
Consequently

```
C_hist(W) = sum_(d<e)W_de - FullBorn(W).
```

The terminal off-diagonal residual is `-lambda S/2`; subtracting
the full Born residual proves

```
C_hist(J)-C_hist(W)
 = lambda[FullBorn(zz^T)+S/2] >= lambda S/2.
```

This maximum is the unspanned historical capacity of one fixed
matrix on literal prefix restrictions. The identity does not
automatically describe a maximum over independently normalized
terminal rows, nor a different maximum with row-dependent span masks.
Those are separate physical-envelope obligations.

The distinction from the earlier positive-bank causal identities is
essential, and the source states it correctly. For a concrete actual
example, the integer Sidon history `P_3={0,1,3}` has positive labels
`1,2,3` with births `2,3,3`. The signed sources `-1,1` both have
birth 2, while their output 2 is born at rank 3. Thus a same-birth
signed pair retires later. In particular `Delta Ghat_n` need not
lie in the older positive bank. The former positive-bank new/new
cancellation and its causal `D_n` or diagonal formula cannot be
imported unchanged. This example is a direct three-point arithmetic
check, not a program run.

The optional convolution identity
`E=NS+2FullBorn+2FullRetired` is the complete used-pair expansion.
It establishes no missing signed analogue of the old causal Abel
identity.

## 4. The future interval, its holes, and all moment constants

The block span convention is `B subset [b,b+L-1]`, with both
endpoints present. Since the signed source includes `-H` and `H`,
the uniform shadow reaches both `b-H` and `b+L-1+H`. The enclosing
integer interval therefore has exactly

```
T=L+2H
```

positions. Every point of B is a hole in both channels: a distinct
point would give a forbidden old difference, while an equal point
would require the omitted zero label. All m holes lie in the
interval, so `D=T-m`. Its positivity follows from the nonzero total
uniform mass `mQ` on the complement. This verifies both corrections
relative to the earlier one-sided source.

The exact moments are `sum f_0=mQ`, `sum f_z=0`, and
`sum_u u f_z(u)=m mu`. For `z_d=d/H`,
`mu=HS>0`. Centering the full interval at `b+(L-1)/2` gives
the coordinate square sum `T(T^2-1)/12`. Thus the lower energy
`LB=12m^2 mu^2/[T(T^2-1)]` has the correct denominator and
orientation. Using the full interval in this Cauchy estimate is
valid even though the actual support has m holes.

The pair expansion is

```
E_B(W)=m(Q+lambda S)+2sum_(t in Delta B)K_W(t).
```

Difference uniqueness in the actual block gives the coefficient
one per physical t; signed sources introduce no extra factor.
Subtracting this exact diagonal yields source equation (17).
Its positive part is also paid because the full physical kernel
is nonnegative. No separate physical capacity is allocated to the
two feature channels.

## 5. Good epochs and the normalized gain

At the actual two-lookahead good ranks, the earlier variance result
has `eta=1/(128*32^2)=2^-17`. Each positive birth-class square sum
of the label d is at least the square sum after subtracting its
class mean. Doubling over the signed bank gives

```
eta Q <= S <= Q,    Q=N(N-1).
```

The next block has m=N and actual length `L<=32H`, hence
`T<=34H`. The lower moment energy is consequently

```
LB >= 12N^2 S^2/(34^3 H).
```

Combining the exact historical capacity difference with the raw
demand change gives

```
gain = lambda[FullBorn+(LB-(m-1)S)/2].
```

The `S/2` in capacity has already reduced `mS/2` to `(m-1)S/2`.
It must not be charged again. Under the fixed eventual cap
`H<=C N^2 log(2N)`, dropping the nonnegative full Born term and
using S<=Q yields exactly

```
gain/Q^2 >= 6lambda eta^2/[34^3 C log(2N)]-lambda/(2N).
```

Here `(N-1)/Q=1/N`, so the last denominator is correct. The
source's lower bound for the mass-only raw demand of W follows
from `D<=34H` and is eventually positive. The unit raw demand
is at least that demand, and the moment demand adds a nonnegative
term. Thus the positive-part comparison is valid beyond a fixed
initial range. On the selected dyadic epochs, the reciprocal-log
gain sum diverges and the sum of `1/N` converges, using the already
proved lookahead frequency result.

## 6. What this review does and does not establish

The source proves a new full Born sign theorem for the actual signed
bank, with no endpoint error and with arbitrary nonnegative
source-stage prices in that sign functional. This removes the
earlier sign obstruction for this new carrier.

The gain is relative to the uniform **signed** source. The normalized
signed sign-feature at lambda=1 reproduces the earlier positive-bank
unit kernel exactly; hence a signed-relative gain cannot be identified
with a gain over that previous baseline. The source explicitly
retains this limitation. It also leaves the shared physical maximum,
changes of terminal normalization, actual span masks and overlap,
and the baseline global margin unpaid.

This audit supports the finite mathematical statements within those
scopes. It is not an original-Q1 proof, a claim about the older
positive-bank full-total sign, or a signed-bank Lean verification.

## 7. Final-source follow-up and exact version binding

On 2026-09-05, after the author's wording update, this reviewer read
the complete source again and computed SHA-256 from the same bytes
that were printed for that readback. The actual observation time was
`2026-09-05T09:18:54.930478+00:00` (UTC), with enclosing readback
tool chunk `88c8b2`. The observed source path was

```
/Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/research/signed_bank_born_positivity.md
```

The observed final source SHA-256 is

```
ff32b2cab2234f21cc727f4b639d57d2cfe136f456526a0adb8d754779cc19e1
```

This is a **follow-up binding** to the newly observed bytes, not a
claim that this hash had been recorded during the initial review.

The current section 2 now explicitly says that same-birth sources
occur in the retired group of a unique-maximum triple when its two
lower clocks tie, and can be Born in the tied-maximum case. This
resolves the earlier wording observation and agrees with the proof.

The current source also contains an explicit section 5 scope
paragraph warning against importing the positive-bank Abel expression
`D_n=S_(n-1)+(n-1)v_n`, giving the actual `{0,1,3}` example, and
separating the older birth-linear feature. This paragraph was not in
the first complete source readback; it has now been reviewed as part
of this follow-up. Its assertions are correct and already agree with
the independently derived scope discussion in review section 3.

Re-reading the remaining source confirms that the numbered
mathematical identities, constants, and proved conclusions retain
the content supported by the initial audit. The final version is
supported without an outstanding correction. This follow-up involved
reading and hashing only; no mathematical test, evidence rerun, Lean
execution, or edit to the source was performed.
