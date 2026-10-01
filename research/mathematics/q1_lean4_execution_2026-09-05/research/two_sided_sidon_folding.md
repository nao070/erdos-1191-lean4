# Folding a two-sided Sidon history into the positive integers

Date: 2026-09-05. Author: `/root`, GPT-6 Astra Ultra.
Status: supporting exact reduction; original Q1 remains unresolved.
This note does not assert a Lean verification.

## 1. A residue-separated folding map

Let `A` be a Sidon subset of the integers, with uniqueness of unordered
two-sums including repeated summands. Define

\[
 f(a)=\begin{cases}4a+1,&a\ge0,\\-4a+2,&a<0.
       \end{cases}
\tag{1}
\]

Every value is a positive integer. The map is injective: on each sign
class it is injective, and its two sign classes have residues `1` and
`2` modulo `4`.

The image `B=f(A)` is Sidon. To prove this, suppose
`f(a)+f(b)=f(c)+f(d)` with `a,b,c,d` in `A`. The residues of a
nonnegative/nonnegative pair, negative/negative pair, and mixed pair are
respectively `2`, `0`, and `3` modulo `4`. Thus both sides have the same
pair type.

If all four entries are nonnegative, cancellation gives `a+b=c+d`.
If all are negative, it gives the same equality after changing signs.
Sidonness of `A` recovers the unordered pair in both cases, including
the repeated-summand cases.

In the mixed case, reorder within each pair so that `a,c>=0` and
`b,d<0`. Cancellation gives `a-b=c-d`, hence `a+d=c+b`. The latter
is an equality of sums of elements of `A`. Its two possible Sidon
matchings are `a=c,d=b` or `a=b,d=c`; the second is excluded by the
opposite signs. Thus the original mixed pairs agree as well.

No equation involving two positive original elements and two negative
original elements has been silently turned into a Sidon equation: the
residue separation is what excludes that problematic pair-type comparison.

## 2. Counts and diameter caps

For every real `X>=0`, (1) gives the exact inclusion and count inequality

\[
 f(A\cap[-X,X])\subseteq B\cap[1,4X+2],\qquad
 |A\cap[-X,X]|\le C_B(4X+2).
\tag{2}
\]

In particular an infinite integer Sidon set folds to an infinite positive
integer Sidon set.

Suppose there is a nested sequence of finite integer Sidon sets
`P_n`, of cardinality `n`, all containing a common anchor point, and
with diameters `H_n`. Translate the common anchor to zero once. Then
every point of `P_n` has absolute value at most `H_n`. For the increasing
enumeration `b_1<b_2<...` of the folded union, (2) gives

\[
 \boxed{\quad b_n\le4H_n+2.\quad}                  \tag{3}
\]

Thus one fixed bound `H_n<=C n^2 log(2n)` for all sufficiently large
`n` implies `b_n<=(4C+1)n^2 log(2n)` for all sufficiently large `n`.
The harmless constant is fixed, not chosen anew at each rank. Therefore
such a two-sided nested diameter-capped history would give a true
counterexample to original Q1 after applying its established integer
formulation bridge.

The new point in a nested two-sided history may be added on the left or
the right. Infinitely many left additions cause no obstruction to (1)--(3).
No infinite translation of the entire union is being used.

The same map also shows that the zero-liminf question for positive integer
Sidon sets is equivalent to the analogous question for radial counts
`|A cap [-X,X]|` of integer Sidon sets. For the nontrivial implication,
apply Q1 to `B`, choose its arbitrarily large small-density cutoffs `x`,
and put `X=(x-2)/4` in (2). The normalization ratio
`sqrt((log X)/X)/sqrt((log x)/x)` tends to `2`, so small normalized
counts remain small. This is an equivalence of formulations, not a proof
that either formulation holds.

## 3. Why the full difference-batch identity is much stronger than a density profile

In any actual `n`-point Sidon history, the newly born full label set
is `G_n={a_n-a_i:i<n}` and has cardinality `n-1`. Its positive
differences are exactly `Delta P_(n-1)`:

\[
 \Delta G_n=F_{n-1},\qquad
 F_n=F_{n-1}\ \dot\cup\ G_n.
\tag{4}
\]

This uses all labels, without imposing a physical-width cutoff. In the
truncated banks studied earlier, only the inclusion for within-batch
differences remains; (4) is stronger.

Conversely, consider abstract finite positive-label sets satisfying
`F_1=empty`, `|G_n|=n-1`, `Delta G_n=F_(n-1)`, and
`F_n=F_(n-1) disjoint-union G_n`. Induction gives
`|F_n|=binom(n,2)`. The difference map on unordered pairs of `G_n`
then has image of size `binom(n-1,2)`, the size of its domain, so it
is injective. Hence `G_n` is Sidon. Further,

\[
 Q_n=\{0\}\cup G_n
\]

is an actual `n`-point Sidon set with `Delta Q_n=F_n`: the differences
from zero are `G_n`, the internal differences are `F_(n-1)`, and they
are disjoint. These statements follow from the displayed recurrence
alone and need no geometric reconstruction theorem.

To obtain one **nested** endpoint history from all these individually
realized `Q_n`, an additional reconstruction argument is needed. The
old `Q_(n-1)` and the embedded subset `G_n` have the same full distance
set, but equal distance sets must not be confused with an already chosen
congruence. A primary-source verification of collision-free turnpike
uniqueness is being carried out separately in
`recursive_difference_tower.md`.

If congruences matching consecutive rulers exist after finitely many
initial stages, apply an isometry to each new ruler so its embedded old
subset is the already fixed old ruler. This constructs nested actual
integer Sidon sets. They have diameters `max F_n`; (3) then turns an
eventual quadratic-log bound on those maxima into a genuine Q1
counterexample. This final conditional sentence does not assume that
such a bounded recurrence has been constructed.

Neither the abstract birth profiles previously analyzed nor their
coherent physical birth ranks establish (4). The missing condition is
an exact identity of full difference sets, not just their cardinalities,
leading Schur counts, or limiting Fourier transforms. Original Q1 is
unresolved.
