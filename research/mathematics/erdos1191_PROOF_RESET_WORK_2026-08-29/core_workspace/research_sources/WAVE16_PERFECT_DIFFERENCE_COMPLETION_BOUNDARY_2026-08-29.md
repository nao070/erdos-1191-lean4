# Wave 16 primary-source boundary: perfect-difference completion and critical density

Date: 2026-08-29 (Asia/Tokyo)

Status: **exact completion theorem and exact logical boundary; Question 1 remains open**

## 1. Definitions and the question tested

For a set `A` of positive integers, write

\[
 d_A(u)=\#\{(a,a')\in A^2:a-a'=u\}
\]

and

\[
 \rho_A(x)=\#\{1\leq u\leq x:d_A(u)>0\}.
\]

Thus `A` is a Sidon set, equivalently an integer Golomb ruler, when
`d_A(u)<=1` for every nonzero integer `u`.  It is a **perfect difference
set** when

\[
 d_A(u)=1\qquad(u\in\mathbb Z\setminus\{0\}).
\tag{1}
\]

In particular, a perfect difference set is Sidon and

\[
 \rho_A(x)=\lfloor x\rfloor.
\tag{2}
\]

The literature question relevant to Wave 16 is whether adding either

\[
 \rho_A(x)\geq\delta x\quad\hbox{for every sufficiently large }x
\tag{3}
\]

or the stronger perfect-difference condition (1) makes it possible to rule
out the hypothetical critical envelope

\[
 a_n\leq Cn^2\log(2n)\quad\hbox{eventually}.
\tag{4}
\]

The checked completion theorem shows that this is not a smaller known
subproblem: excluding (4) even in the perfect-difference subclass is already
equivalent to Question 1.

## 2. Chen--Fang's exact whole-set completion theorem

Yong-Gao Chen and Jin-Hui Fang,
[*Dense perfect difference sets constructed from Sidon
sets*](https://doi.org/10.1016/j.jcta.2026.106239), Journal of
Combinatorial Theory, Series A **225** (January 2027), article 106239,
Theorem 1.1, prove the following.

> For every Sidon set `B` and every positive function
> `omega(x)->infinity`, there is a perfect difference set `A` such that,
> for every `x>=1`,
> \[
> B(x/2)-\omega(x)\leq A(x)\leq B(x/2)+\omega(x).
> \tag{5}
> \]

The DOI and online article are dated 2026, while the assigned journal volume
is the January 2027 volume.  This explains the `2026/2027` bibliographic
description; it is one article, not two versions of the theorem.  The full
publisher text, including Theorem 1.1 and its proof, was checked for this
note.

The construction starts from the dilate `2B`.  It builds a sparse auxiliary
odd set `V` and deletes a sparse even subset `C` of `2B`, with output of the
form

\[
 A=V\cup\bigl((2B)\setminus C\bigr).
\tag{6}
\]

The induction makes every positive integer occur as a difference and keeps
every positive difference representation unique.  The sparse insertion and
deletion bounds give the two sides of (5).

The earlier theorem of Javier Cilleruelo and Melvyn B. Nathanson,
[*Perfect difference sets constructed from Sidon
sets*](https://arxiv.org/abs/math/0609244), Combinatorica **28** (2008),
401--414, [DOI](https://doi.org/10.1007/s00493-008-2339-4), Theorem 1,
gave the one-sided predecessor

\[
 A(x)\geq B(x/3)-\omega(x).
\tag{7}
\]

Chen--Fang improve the dilation loss from `1/3` to `1/2`, obtain a matching
upper bound, and make (5) valid for all `x>=1`.

Here and below, the 2006 arXiv manuscript numbers these results Theorems 1
and 3; the journal references number them Theorems 1.1 and 1.3.

## 3. Exact Question 1 equivalence

Question 1 asks whether every infinite Sidon set satisfies

\[
 \liminf_{x\to\infty}A(x)\sqrt{\frac{\log x}{x}}=0.
\tag{8}
\]

Suppose, toward its negation, that a Sidon set `B` satisfies

\[
 \lambda:=\liminf_{x\to\infty}
 B(x)\sqrt{\frac{\log x}{x}}>0.
\tag{9}
\]

Apply (5) with, for example, `omega(x)=log(x+2)`.  Since

\[
 \log(x+2)\sqrt{\frac{\log x}{x}}\longrightarrow0
\]

and `log x/log(x/2)->1`, the resulting perfect difference set satisfies

\[
 \liminf_{x\to\infty}
 A(x)\sqrt{\frac{\log x}{x}}
 \geq\frac{\lambda}{\sqrt2}>0.
\tag{10}
\]

Conversely, a perfect difference set satisfying (10) is itself a Sidon
counterexample to (8).  The usual monotone inversion between counting
functions and enumerations identifies (9)--(10) with an eventual bound of
the form (4), with a changed constant.  Consequently,

\[
 \boxed{
 \begin{aligned}
 &\text{Question 1 is false}\ \\
 &\iff \text{there is a perfect difference set satisfying (9)}\ \\
 &\iff \text{there is a Sidon set satisfying (3) and (9)}.
 \end{aligned}}
\tag{11}
\]

For the last implication, the perfect set supplied by Chen--Fang has
`rho_A(x)=floor(x)`, so it satisfies (3) for every fixed `delta<1` and all
sufficiently large `x`.  The reverse implication in (11) merely observes
that the set in question is already a counterexample to Question 1; its
difference density is not needed for that direction.

Thus a theorem asserting

> positive lower density of represented positive differences, together
> with unique difference representations, forbids (4)

would prove Question 1.  It is not a currently available preliminary lemma.
Likewise, proving (8) only for perfect difference sets would already suffice
for Question 1, by applying (5) to any hypothetical general counterexample.
These are reductions, not resolutions.

## 4. Why the stronger density shortcut is false

Cilleruelo--Nathanson's Theorem 3 constructs a perfect difference set `A`
such that

\[
 \limsup_{x\to\infty}\frac{A(x)}{\sqrt{x}}
 \geq\frac1{\sqrt2}.
\tag{12}
\]

Along the subsequence in (12),

\[
 \frac{A(x)}{\sqrt{x/\log x}}
 =\frac{A(x)}{\sqrt x}\sqrt{\log x}
 \longrightarrow\infty.
\tag{13}
\]

Therefore neither of the following can be inferred from full difference
coverage and unique representations:

- `A(x)=o(sqrt(x/log x))` as `x->infinity`;
- an eventual bound `A(x)=O(sqrt(x/log x))`.

This does not refute Question 1, whose conclusion is only the **liminf** zero
in (8).  It rules out replacing that liminf target by a full little-oh
statement.  It also directly disproves a universal claim
`rho_A(x)=o(x)`: a perfect set has (2).  More generally, for an integer
`q>=1`, the dilate `qA` is still Sidon and has

\[
 \rho_{qA}(x)=\lfloor x/q\rfloor,
\tag{14}
\]

so positive lower density is compatible with unique positive-difference
representation even without full coverage.

## 5. The current general thickness theorem stops at a constant

Kevin O'Bryant,
[*On the Thickness of Infinite Generalized Sidon Sets,
I*](https://arxiv.org/abs/2606.28651v3), arXiv:2606.28651v3, Theorem 1,
proves that every infinite `g`-Golomb ruler satisfies

\[
 \liminf_{x\to\infty}
 \frac{A(x)}{\sqrt{x/\log x}}
 \leq\frac{2\sqrt g}{\sqrt{\log2}}.
\tag{15}
\]

O'Bryant uses the endpoint convention
`A(x)=|A intersect [0,x)|`; the present note otherwise counts positive
elements at most `x`.  The two conventions differ by at most one and hence
give exactly the same normalized liminf and limsup statements used here.

For Sidon sets, `g=1`, so the right side is
`2/sqrt(log 2)`, approximately `2.40224`, rather than zero.  Corollary 2
gives the enumeration form

\[
 \limsup_{n\to\infty}\frac{a_n}{n^2\log n}
 \geq\frac{\log2}{2g}.
\tag{16}
\]

Equations (15)--(16) sharpen the known finite constant.  They do not prove
(8), and they do not contradict an eventual upper envelope (4) when `C` is
larger than the lower-bound constant.  The theorem assumes only bounded
difference multiplicity; it does not contain an additional positive-density
hypothesis for `A-A` that could be read as a zero conclusion.

The checked sources therefore give a precise boundary:

- full or positive-density difference coverage does not force a full
  little-oh bound, by (12)--(14);
- forcing the liminf in (8) to zero even for perfect difference sets is
  Question 1-equivalent, by (5)--(11); and
- the current general theorem (15) supplies a finite constant, not zero.

This is a statement about the cited theorems.  It is not a literature-wide
proof that no other relevant theorem exists.

## 6. Whole infinite-set replacement is not finite-prefix completion

The word “completion” must be used with care here.

| Property | Prescribed finite-prefix completion | Chen--Fang Theorem 1.1 |
|---|---|---|
| Input | A specified finite Golomb prefix `F` | A complete infinite Sidon set `B` |
| Required containment | Output contains every mark of `F` | No assertion that `B`, `2B`, or a prescribed prefix is contained in `A` |
| Modification | Old marks and old pair identities survive | Elements of `2B` may be deleted and new odd elements are inserted, as in (6) |
| Compatibility | One fixed prefix ray or extension tree is retained | Only the output's global perfectness and the counting comparison (5) are retained |
| Valid use here | Transfer finite-prefix state variables | Transfer an existential asymptotic counterexample |

In particular, Chen--Fang do **not** prove that an arbitrary finite Golomb
ruler can be retained as the initial segment of their output, nor that old
Wave 16 quantities such as `rho_L(d)`, the exact suffix thresholds, or a
birth-time allocation survive the construction.  No such finite-prefix
claim should be cited from (5).

On the other hand, this loss of prefix identity does not weaken the logical
reduction (11).  Question 1 is an asymptotic universal statement: if any
counterexample `B` exists, replacing the whole infinite set by the new
perfect set `A` is enough to produce a perfect counterexample.  Hence:

- **existence/Q1 logic:** whole-set replacement is sufficient;
- **the fixed-ray Wave 16 allocation problem:** whole-set replacement is
  insufficient.

This distinction also explains why the completion theorem does not allocate
the positive future-rank resource already proved in Wave 16.  It changes the
entire ruler instead of providing a map that preserves the current ruler's
prefix atoms and signed bookkeeping.

## 7. Representation-function warning

The classical Erdős--Turán statement in
[*On a Problem of Sidon in Additive Number Theory, and on Some Related
Problems*](https://doi.org/10.1112/jlms/s1-16.4.212), Journal of the London
Mathematical Society **16** (1941), 212--215, concerns representations of a
nonnegative integer as a **sum**.  It cannot be transferred mechanically to
differences.  In a sum `n=a+b` with nonnegative terms, both terms are at most
`n`; in a difference `n=a-b`, both endpoints can be arbitrarily larger than
`n`.  Perfect difference sets, with representation function exactly one for
every nonzero integer, are explicit obstructions to the naive difference
analogue.

## 8. Claim boundary and primary links

What is established by the checked primary sources is:

1. perfect difference sets exist and can shadow the counting function of any
   supplied infinite Sidon set at the half-scale, up to arbitrary divergent
   error, by Chen--Fang (5);
2. positive or full density of the positive difference set is compatible
   with unique representations, by (2) and (14);
3. full little-oh critical thinning is false, by Cilleruelo--Nathanson
   (12)--(13); and
4. the strongest checked general thickness bound is the finite constant in
   O'Bryant (15), not the zero required in Question 1.

The following are **not** established:

- no critical Sidon set or critical perfect difference set is constructed;
- Question 1, Question 2, the Wave 16 signed allocation target, and the prize
  problem are not resolved;
- no claim is made that the search is exhaustive;
- no absence, novelty, priority, or prize-submission claim is made; and
- Chen--Fang is not a prescribed-prefix extension theorem.

Direct primary sources:

- [Chen--Fang, publisher article and DOI](https://doi.org/10.1016/j.jcta.2026.106239)
- [Cilleruelo--Nathanson, author/arXiv text](https://arxiv.org/html/math/0609244)
- [Cilleruelo--Nathanson, journal DOI](https://doi.org/10.1007/s00493-008-2339-4)
- [O'Bryant, arXiv v3 full text](https://arxiv.org/html/2606.28651v3)
- [Erdős--Turán 1941, journal DOI](https://doi.org/10.1112/jlms/s1-16.4.212)

The productive Wave 16 interpretation is therefore narrow: perfect-
difference completion is a powerful **logical reduction of the hypothetical
counterexample class**, but it is not the missing signed/disjoint allocation
on the existing infinite ray.
