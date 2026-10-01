# Independent audit of the three-clock core localization

2026-09-05. Reviewer: `/root/causal_telescoping`, GPT-6 Astra Ultra.
Ownership: this review only. The parent's source was not edited.

**Result: PASS.** The complete argument in `clock_core_localization.md`,
including the all-output star bound, the constants 3 and 6 in the
old-clock tails, the Born repeated/automatic deletion in (7), and
the final simultaneous core identities, is supported by independent
derivation. Two minor domain clarifications were reported to the
parent and incorporated before the final source hash below. No tests,
finite search, or Lean execution were performed.

Current reviewed source SHA256:

```
38fe3a9b361f60bd3312c07bf87781b04690c2078de69617e58e505e86b768a8
```

The supporting `near_retirement_incidence.md` was read in full,
and the repeated-configuration argument of
`birth_linear_total_causal_sign.md` was rechecked. The remaining
signed cores and one physical margin are unbounded by this audit;
original Q1 remains unresolved.

## 1. The star bound does extend to every output birth

The source's mixed-pair orientation is unique: the new source is
`d in G_b` and the old source is `e in F_(b-1)`, independently of
their numeric order. In the case `d>e`, the equation

```
a_j-a_i=a_r-a_b+e
```

has a nonzero right side. If it were zero for `r<b`, then
`e=a_b-a_r` would be in `G_b`, contrary to its old birth. For
`r>=b` it would force a nonpositive `e`. Actual uniqueness of
nonzero signed differences thus permits at most one ordered pair
`(i,j)`, whether the right side is positive or negative.

In the case `d<e`, repeated-summand Sidon uniqueness permits at
most one unordered pair solving
`a_i+a_j=a_b+a_r-e`, hence at most two ordered assignments.
The endpoint restrictions `i<b,j<r` only lower these counts.
The numeric cases are disjoint. This proves (2) with coefficient
three, including `r=b` and the full Born side `r<b`.

The absolute coefficient estimate (1) follows from
`|g_d|,|g_e|<=H_b`. For retired pairs `r>b`, monotonicity makes
`w_r<=w_b`. No artificial choices of output rank are summed:
each source pair has one numeric output and at most one actual
output birth.

## 2. The clock and numeric-label tails retain their constants

The interval centered at the integer `b` contains at most
`2floor[b/(log b)^gamma]+1` possible output ranks. Also

```
3q_(b-1)/q_b^2
 = 6(b-2)/[b^2(b-1)] <= 6/b^2.
```

This proves (3) with the two constants 12 and 6. Its convergence
requires exactly the stated `gamma>1`. The estimate is at source
price, so it controls both chronological sides.

For `k_b=floor[b/(log b)^a]`, there are at most
`(b-1)q_(k_b)` pairs with old source birth at most `k_b`.
Since `q_(k_b)<=b^2/[2(log b)^(2a)]`, their priced contribution
at `b` is at most

```
2/[(b-1)(log b)^(2a)] <= 3/[b(log b)^(2a)].
```

This proves (4). The parent added `F_0=F_1=empty` and
`q_0=q_1=0`, covering cutoffs below two, which are possible for
large fixed `a` and small `b`.

For an old output, every new source and target in `F_(k_b)`
allows at most two old partners, `e=d-t` and `e=d+t`. This
doubles the preceding count and proves (5) with constant six.
Since `k_b<b`, these records really are Born. The convergence
threshold in both statements is `2a>1`.

For the numeric cutoff in (6), the analogous count is
`2(b-1)floor[b^2/(log b)^beta]`. Its price is at most

```
8/[(b-1)(log b)^beta] <= 12/[b(log b)^beta],
```

which proves the displayed constant and convergence for `beta>1`.
Neither target counting argument creates a further rank multiplicity.

Finally, `0<=w_b-w_r<=w_b` is used only on the retired subset.
The parent made that restriction explicit after review. For Born
records the weight order is reversed, so an unrestricted extension
to their clock-price difference would not follow.

## 3. The automatic Born count is safe, and can be strengthened

Consider a used pair and its output, with their unique physical
difference endpoints. If its two equal triple multisets coincide,
the corresponding three oriented nonzero edges form a balanced
three-edge graph. There are no loops. Such a graph must be a
directed three-cycle on three distinct point vertices: a two-cycle
would leave a loop for its third edge.

Write the actual points as `a_h<a_i<a_j`. Their three positive
lengths are

```
p=a_i-a_h,    q=a_j-a_i,    p+q=a_j-a_h.
```

The two possible used source-pair choices from this triangle are
`{p,p+q}` and `{q,p+q}`. The second has equal source births `j`
and is excluded from the mixed causal sum `B_T`. The first shares
lower endpoint `h`; it is mixed and has

```
b=j,     c=i,     r=j=b.
```

Conversely each such triple supplies just this one automatic mixed
record, and the record recovers its three points. Difference
uniqueness rules out equal short lengths in this triangle.
Consequently an `M`-point prefix contains exactly
`binom(M,3)` automatic mixed records, and at most
`2binom(M,3)` automatic used records even if same-birth pairs
are allowed. Both counts are below the source's loose `M^3`
allowance. Thus the automatic constant in (7) is safe.

There are two useful strengthenings, neither needed by the source:

* Every automatic mixed record has `r=b`, so it already belongs to
  the near-clock deletion (3).
* At a fixed source birth `b` there are `q_(b-1)` such records.
  Their absolute source-price sum over all ranks is therefore at most
  `sum_b q_(b-1)/q_b^2=4zeta(2)-6`.

The latter is an absolute bound; it does not rely on cancellation of
the automatic coefficients or their separate centered formula.

## 4. Nontrivial repeated endpoints and the dyadic bound

If two different equal-sum triple multisets shared any point,
canceling one occurrence would give a two-sum equality, and Sidon
uniqueness including repeats would force the triples to agree.
Hence the supports of different members of one sum fiber are
disjoint, including when one member has repeated slots.

In an `M`-point prefix there are at most `M^2` repeated triples,
represented by `{a,a,b}`. Each has at most `M` different equal-sum
partners, by this disjointness. Every unordered collision has at
most six matchings of its three slots. The resulting three signed
differences sum to zero; when nonzero, the largest length is the
sum of the other two and yields at most two used source pairs.
Repeated slots or equal short lengths can reduce the number, and
do not increase it. Thus `12M^3` safely bounds these records.

A source pair and its actual output endpoints fix its unordered
triple collision, so records from outside this enumeration are not
being discarded. Counting some collisions or slot descriptions more
than once only enlarges the upper bound. Automatic collisions were
handled separately in §3.

For a Born record with `N<=b<2N`, the output birth obeys `r<=b`.
All its source and output endpoints therefore lie in `P_(2N)`.
The combined bound `13(2N)^3` in source (7) is valid. Each record
costs at most `1/q_b^2<=1/q_N^2`. Since `q_N>=N^2/4`,

```
13(2N)^3/q_N^2 <= 1664/N,
sum_(N=2^j,j>=1) 1664/N = 1664.
```

This gives even an explicit absolute constant for (7), without
using a cap. A unique source birth assigns each original record
to exactly one source dyad.

For retirements, the imported order of operations is correct:
the far-rank part is first removed at `w_r` by its separate tail.
In the remaining source dyad, all endpoints lie before
`ceil[2N(log(2N))^alpha]`; the repeated-endpoint bound is then
`O_alpha((log(2N))^(3alpha)/N)` and is dyadically summable.
This does not transfer the far-rank tail to `w_b`.

## 5. The simultaneous cores and their scope

For Born records, failure of a displayed core condition is covered
by, respectively, the old-source tail (4), old-output tail (5),
the two-sided close-clock tail (3), the short numeric-output tail
(6), or the non-six-endpoint deletion (7). The strict boundaries
are correct: the excluded equalities belong to the non-strict
tail cutoffs. Overlaps between omitted sets are harmless under
their absolute bounds. This proves (8).

For retired records, the prior core already removes close-clock,
far-clock, short-output, and repeated-endpoint pieces. Adding the
old-source cutoff uses (4) at the smaller price `w_r`. This proves
(9). Substitution in the exact causal identity gives (10), with a
uniform bounded error; the unchanged diagonal term is retained.

The final physical upper bound uses `t=|d-e|<H_b`, since both
source labels are in the old source bank range. Thus the fixed-onset
cap at **source rank `b`** gives `t<=Cb^2 log(2b)`, even when
the actual output birth is later. In the Born core all clocks
are between `b/(log b)^a` and `b`; in the retired core they are
between `b/(log b)^a` and `b(log b)^alpha`. Their ratios are
therefore bounded by the stated fixed logarithmic powers.

The localization is correct. It proves neither a sign for either
core nor that a divergent Born contribution pays the single
physical margin. Those missing estimates, and Q1, remain open.
