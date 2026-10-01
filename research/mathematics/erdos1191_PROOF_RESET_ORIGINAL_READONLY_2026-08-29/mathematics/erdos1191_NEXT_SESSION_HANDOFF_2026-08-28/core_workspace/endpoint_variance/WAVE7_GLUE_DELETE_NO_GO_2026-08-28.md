# Wave 7: what Lemma 9 can and cannot guarantee for a critical prefix tower

Date: 2026-08-28  
Scope: a proof-method obstruction for a naive black-box iteration of
O'Bryant's Lemma 9, not an obstruction to specially designed extensions and
not a solution of Erdős Problem #1191.

Primary source:
[O'Bryant, *On the Thickness of Infinite Generalized Sidon Sets, I*,
Lemma 9 and the proof of Theorem 3, arXiv:2606.28651v3](https://arxiv.org/html/2606.28651v3#S4).

Throughout this note `\log` is the natural logarithm and `\binom{x}{2}=x(x-1)/2`.
We specialize Lemma 9 to `g=1`, so “Golomb ruler” means an integer
Sidon set.

## 1. Exact one-step ledger

Normalize the old ruler as

\[
V=\{0=a_1<a_2<\cdots<a_n\},
\qquad
N=N_n:=a_n-a_1+1=a_n+1.
\]

Thus `V\subset[0,N)`.  Let the candidate ruler `W` have `q` marks and
be contained in `[W_1,W_1+m)`.  Lemma 9 assumes

\[
W_1-N\ge \max\{N,m\}
\tag{1}
\]

and returns `W^*\subseteq W` such that

\[
|W^*|\ge q-\binom n2,
\qquad
V\cup W^*\text{ is Sidon}.
\tag{2}
\]

Put

\[
B_n:=\binom n2.
\]

If the scalar bound (2) is the **only** reason used to certify that at least
`r\ge1` new marks survive, then necessarily

\[
q\ge B_n+r.
\tag{3}
\]

There is a second completely elementary constraint.  A `q`-mark integer
Sidon ruler has `\binom q2` distinct positive differences, all lying between
`1` and its diameter.  Hence

\[
\operatorname{diam}(W)\ge\binom q2,
\qquad
m\ge\binom q2+1.
\tag{4}
\]

If `W^*\ne\varnothing`, every retained new mark is at least `W_1`.  The
first new prefix therefore satisfies, directly from (1),

\[
\boxed{
N_{n+1}\ge
N+\max\!\left\{N,\binom q2+1\right\}+1.
}
\tag{5}
\]

Combining (3)--(5) gives the exact worst-guarantee ledger

\[
\boxed{
\begin{aligned}
q&\ge B_n+r,\\
m&\ge\binom{B_n+r}{2}+1,\\
|W^*|&\ge r,\\
N_{n+1}
&\ge
N+\max\!\left\{N,\binom{B_n+r}{2}+1\right\}+1.
\end{aligned}}
\tag{6}
\]

The last line concerns the **first** retained mark of the block, irrespective
of how many more marks the block later contributes.  It is consequently
stronger for an all-prefix problem than an estimate made only after the
entire new block has been counted.

For reference, Sidon packing in the old ruler also gives

\[
N\ge B_n+1.
\tag{7}
\]

No density theorem has been used in (3)--(7); all quantities are integers
except when a logarithmic envelope is imposed below.

## 2. The black-box critical-envelope no-go

Fix `C>0` and define the common critical envelope

\[
F_C(k):=2Ck^2\log k.
\tag{8}
\]

### Theorem 1 (exact necessary inequality)

Suppose an `n`-mark old ruler is extended by one invocation of Lemma 9,
and positive retention is certified solely from its worst-case scalar
guarantee (2).  If the first new prefix is to obey
`N_{n+1}\le F_C(n+1)`, then necessarily

\[
\boxed{
N+\binom{B_n+1}{2}+2\le F_C(n+1).
}
\tag{9}
\]

In particular, using only the universal packing bound (7),

\[
\boxed{
\frac{B_n(B_n+3)}2+3\le F_C(n+1).
}
\tag{10}
\]

**Proof.**  To certify even one survivor, (3) forces `q\ge B_n+1`.
Equation (4) then forces
`m\ge\binom{B_n+1}{2}+1`.  Equation (5) gives

\[
N_{n+1}\ge N+\binom{B_n+1}{2}+2,
\]

which proves (9).  Substitute `N\ge B_n+1` to obtain (10). ∎

The left side of (10) is

\[
\frac18n^4+O(n^3),
\]

whereas the right side of (10) is

\[
2Cn^2\log n\,(1+o(1)).
\]

Their ratio is

\[
\frac{n^2}{16C\log n}(1+o(1))\longrightarrow\infty.
\tag{11}
\]

Thus, for every fixed `C`, a black-box iteration that relies only on
(2) eventually cannot certify even one further mark inside the common
critical envelope.

An entirely explicit sufficient condition for failure is

\[
n^2>256C\log(2n).
\tag{12}
\]

Indeed, for `n\ge2`,

\[
\binom{B_n+1}{2}
>\frac{B_n^2}{2}
\ge\frac{n^4}{32},
\]

while

\[
F_C(n+1)\le8Cn^2\log(2n).
\]

Condition (12) makes the former quantity larger than the latter.

### Exact `C=1` calibration

For the package's `C=1` envelope, the obstruction already holds for every
`n\ge8`.  Around the transition:

| old `n` | `B_n` | minimum candidate `q` | minimum window `m` | minimum `N_{n+1}` from (6),(7) | `F_1(n+1)` |
|---:|---:|---:|---:|---:|---:|
| 7 | 21 | 22 | 232 | 255 | `128\log 8\approx266.1685` |
| 8 | 28 | 29 | 407 | 437 | `162\log 9\approx355.9504` |

Here is a rigorous all-`n\ge8` check, not a floating-point inference.
The coarser lower bound in the proof above is

\[
\frac{B_n^2}{2}
=\frac{n^2(n-1)^2}{8}.
\]

The inequality

\[
\frac{n^2(n-1)^2}{8}
>2(n+1)^2\log(n+1)
\tag{13}
\]

is equivalent to

\[
H(n):=
\frac{n^2(n-1)^2}{(n+1)^2\log(n+1)}>16.
\]

For real `x>1`, logarithmic differentiation gives

\[
\frac{H'(x)}{H(x)}
=\frac2x+\frac2{x-1}-\frac2{x+1}
-\frac1{(x+1)\log(x+1)}>0.
\]

The last inequality follows because
`2/x>1/((x+1)\log(x+1))` and
`2/(x-1)>2/(x+1)`.  Finally,
`\log9<9/4` (for example from the positive exponential series), so

\[
H(8)>
\frac{3136}{81(9/4)}
=\frac{12544}{729}>16.
\]

Therefore (13), and hence the contradiction to the `C=1` envelope,
holds for every `n\ge8`.

### Exponent consequence

At every unbounded sequence of block-start sizes `n`, the scalar
guarantee alone requires

\[
N_{n+1}=\Omega(n^4).
\tag{14}
\]

Consequently it cannot certify an all-prefix envelope

\[
N_k=O\!\left(k^\alpha(\log k)^\beta\right)
\]

for any fixed `\alpha<4` and fixed `\beta`.  This `4` is a
constraint on this proof method, not a lower-bound exponent for actual
infinite Sidon sequences.

If one deliberately keeps only one guaranteed mark at every step, (6) gives

\[
N_{n+1}-N_n
\ge \binom{B_n+1}{2}+2
=\frac18n^4+O(n^3),
\]

and summation yields

\[
N_n\ge\frac1{40}n^5-O(n^4).
\tag{15}
\]

Equation (15) applies only to this unit-growth implementation.  It is not a
universal consequence for block iterations.

## 3. The same loss can look harmless at selected block endpoints

Let `r\ge1` be the guaranteed number of retained marks and
`s=n+r`.  If one ignores all intermediate prefixes and checks the
envelope only after assigning all `r` new marks their final indices, (6)
still imposes the necessary inequality

\[
2Cs^2\log s
\ge
N+\binom{B_n+r}{2}+2.
\tag{16}
\]

In particular,

\[
s^2\log s\ge\frac{B_n(B_n-1)}{4C}.
\tag{17}
\]

Therefore selected stage sizes must obey

\[
s\ge n^{\,2-o(1)}.
\tag{18}
\]

For example, if `s\le n^2`, taking logarithms in (17) gives
`\log s/\log n\ge2-O(\log\log n/\log n)`; if `s>n^2`, (18) is
automatic.  This is the precise sense in which endpoint-only use of the
worst guarantee forces nearly squaring stage sizes.

There is no contradiction at selected endpoints: when `r` and `q`
are both of order `n^2`, the candidate window has order `n^4` but the
new stage size also has order `n^2`, so the window is merely quadratic
in the **new** size.  The fatal all-prefix gap occurs because the first point
of that block still has index `n+1`, not index `s`.

## 4. O'Bryant's actual cubic iteration

For `g=1`, the proof of Theorem 3 takes a prime power parameter
`p_i` and sets

\[
p_{i+1}=p_i^3,
\qquad
m_i=p_i^2-1.
\]

The next candidate block has:

\[
\begin{array}{c|c}
\text{quantity}&\text{scale in }p_i\\ \hline
\text{candidate marks}&p_{i+1}=p_i^3\\
\text{candidate window}&m_{i+1}=p_i^6-1\\
\text{old cardinality}&n_i\sim p_i\\
\text{worst deletion}&\binom{n_i}{2}=O(p_i^2)\\
\text{retained new marks}&p_i^3-O(p_i^2)\\
\text{new block start}&p_i^6+p_i^3-1\\
\text{final stage size}&n_{i+1}\sim p_i^3\\
\text{final containing endpoint}&2p_i^6+O(p_i^3).
\end{array}
\]

Here `n_i\sim p_i` follows inductively: the `i`-th candidate contributes at
least `p_i-O(p_{i-1}^2)=p_i-O(p_i^{2/3})` marks, while the sum of all earlier
candidate sizes is `o(p_i)`.

Thus the loss fraction is `O(1/p_i)`, and at the selected final
endpoints the width is `\Theta(n_{i+1}^2)`.  This is exactly what is
needed for the paper's limsup construction.

At the first new prefix, however,

\[
N_{n_i+1}=\Omega(p_i^6)=\Omega(n_i^6).
\tag{19}
\]

The cubic choice is not forced by Lemma 9 merely to retain something.
For a guaranteed retained fraction at least `\theta\in(0,1)`, it is
enough at the scalar level to take

\[
q\ge\frac{B_n}{1-\theta}.
\tag{20}
\]

To make the deletion fraction tend to zero, one needs

\[
\frac{q}{n^2}\longrightarrow\infty.
\tag{21}
\]

The paper's cubic jump is a convenient algebraic choice satisfying (21);
the universal nonempty-retention threshold is only quadratic.  Either
choice is incompatible with a critical **first-new-prefix** bound when
only the worst guarantee is used.

## 5. Candidate capacity inside a critical first prefix

The preceding obstruction can be restated as a gap between the candidate
capacity of the coordinate budget and the candidate size demanded by the
deletion guarantee.

If `N_{n+1}\le F_C(n+1)`, then (5) forces

\[
\binom q2
\le F_C(n+1)-N-2.
\tag{22}
\]

When the right side is nonnegative,

\[
q\le
\left\lfloor
\frac{1+\sqrt{1+8(F_C(n+1)-N-2)}}2
\right\rfloor
=O_C(n\sqrt{\log n}).
\tag{23}
\]

But the black-box guarantee demands

\[
q\ge B_n+1=\frac12n^2+O(n).
\tag{24}
\]

The multiplicative gap between (24) and the leading capacity in (23) is
of order

\[
\frac{n}{4\sqrt{C\log n}}.
\tag{25}
\]

There is also a separate separation-slack constraint.  From (5),

\[
N_{n+1}\ge2N+1,
\]

so any separated successor inside the envelope, even one with zero
old/new internal-spectrum collisions, must have

\[
2N+1\le F_C(n+1).
\tag{26}
\]

Thus a special-block construction must solve both problems: it must beat the
quadratic deletion charge and keep enough factor-two slack in the old width.

More generally, a hypothetical replacement for Lemma 9 with a uniform loss
`L(n)` could certify one new point only by taking `q\ge L(n)+1`.
Equation (23) shows that the same separated-block architecture would require

\[
L(n)=O_C(n\sqrt{\log n})
\tag{27}
\]

at block starts.  O'Bryant's `L(n)=B_n=\Theta(n^2)` is larger by the
factor displayed in (25).

## 6. Why the quadratic deletion cannot be uniformly wished away

The count `B_n` is worst-case sharp if the only hypotheses are that
`V,W` are Sidon and sufficiently separated.  Here is a self-contained
construction.

List the positive differences of `V` as

\[
d_1,\ldots,d_{B_n}
\]

and put `D=\max d_i`.  Choose an integer radix `R>4D+4`, set
`x_i=R^i`, and define

\[
W_0=\{x_i,x_i+d_i:1\le i\le B_n\}.
\tag{28}
\]

The within-pair differences are the distinct `d_i`.  Every cross-pair
difference with `j>i` has the form

\[
R^j-R^i+\varepsilon d_j-\eta d_i,
\qquad \varepsilon,\eta\in\{0,1\}.
\tag{29}
\]

The base differences `R^j-R^i` are distinct by their exact
`R`-adic valuation and any two are separated by at least `R`.
Perturbation differences have magnitude at most `2D`.  For fixed
`(j,i)`, the four perturbations
`0,d_j,-d_i,d_j-d_i` are distinct.  Finally, every cross-pair
difference exceeds `D`.  Hence `W_0` is Sidon and

\[
\Delta^+(W_0)\cap\Delta^+(V)=\{d_1,\ldots,d_{B_n}\},
\]

with those overlaps represented by `B_n` vertex-disjoint pairs.
Any subset of `W_0` whose internal differences avoid
`\Delta^+(V)` must delete at least one endpoint from each pair, hence at
least `B_n` marks.  Translating `W_0` arbitrarily far to the right
enforces (1) without changing any difference.

This sharpness example is extremely sparse.  It proves that no smaller
uniform loss follows from Sidonness plus separation alone.  It does **not**
prove that an optimally chosen small-diameter algebraic or randomized block
must lose `B_n` marks.

## 7. Guaranteed statements versus possible improvements

### Guaranteed by the black-box lemma

1. Positive scalar-guaranteed retention requires `q\ge B_n+1`.
2. Such a candidate has window length `\Omega(n^4)`.
3. Separation places its first retained point beyond that window.
4. Hence every fixed critical envelope eventually fails at the first new
   prefix; for `C=1`, all `n\ge8` already fail.
5. If intermediate prefixes are suppressed, stage indices must jump at least
   `n^{2-o(1)}`.
6. The deletion count is uniformly sharp for some, generally sparse,
   candidate blocks.

### Not ruled out

1. A specially chosen `W` can have far fewer collisions with
   `\Delta^+(V)` than the universal bound charges.
2. The proof of Lemma 9 deletes a prescribed endpoint from each conflicting
   pair; exploiting the actual conflict graph or its maximum independent set
   may retain much more.
3. Algebraic rotations, dilations, randomized blocks, or a localized
   old-history charge could improve the actual loss.
4. A new gluing argument could avoid the large separation condition by
   controlling mixed differences directly.
5. Finite successful extensions, including the authenticated finite
   witnesses elsewhere in this package, do not contradict this theorem:
   they use actual structure, not merely the scalar lower bound (2).

## 8. Exact replay

The companion check
`wave7_glue_delete_no_go_test.py` independently evaluates the integer
ledger, the transition at `n=7,8`, the exact candidate capacities
`22,25`, the `C=1` inequality for every `8\le n\le2048`, and
the unit-growth polynomial identity.  It uses Python `Decimal.ln` at
80-digit precision; the all-`n\ge8` theorem itself remains the analytic
proof above.

Reproduction:

    /tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python -m pytest -q \
      core_workspace/endpoint_variance/wave7_glue_delete_no_go_test.py

Recorded result:

    4 passed in 0.15s

Static check:

    /tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python -m ruff check \
      core_workspace/endpoint_variance/wave7_glue_delete_no_go_test.py

Recorded result: `All checks passed!`

## 9. Logical boundary

The result proved here is:

> **Naive worst-guarantee iteration of O'Bryant's separated-block Lemma 9
> cannot certify an unbounded all-prefix critical Sidon tower.**

It is not:

- a proof that every invocation of Lemma 9 deletes `B_n` marks;
- a proof that no structured candidate block can extend a given old ruler;
- a lower bound for all infinite Sidon sequences;
- an asymptotic conclusion from the package's finite witnesses; or
- a solution of Erdős Problem #1191.
