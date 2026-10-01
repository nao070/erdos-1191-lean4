# Wave 9 primary-literature audit against P15

Cutoff: **2026-08-29**. This audit continues the Wave 8 corpus and asks only
whether a primary theorem can prove the surviving obligation

\[
B_H(J)=\sum_{m\le 2^J}\frac1{N_{2m}^2}
 \sum_{0\le i<j<2m,\ j\ge m}h_i h_j\Phi_{ij}=o(\log J)
\]

on one infinite Golomb branch with
`N_n <= C n^2 log(2n)` eventually. By the canonical Wave 8 telescope, this is
equivalent up to a factor two to the required positive contribution to the
dyadic `Q_m` sum. The literature must therefore respect birth epoch, contiguous
sum uniqueness, the exact gap-product/kernel weight, and the same nested branch.

## 1. Qualified result

**No checked primary theorem proves P15 or supplies a black-box substitution.**
The search did, however, locate the closest exact packing mechanism and yields a
new, rigorous transplant inequality for the project:

1. Ma--Yi's small-rank-difference proof and Shearer's difference-triangle LP
   control *linear sums of distinct difference values*.
2. Their argument applies to P15 birth pairs after a hereditary/incomplete-triangle
   reformulation, giving inequality `(W9-RLP)` below for arbitrary sets of dyadic
   epochs.
3. No source converts that linear rank-lag packing into the nonlinear weights
   `h_i h_j Phi_ij/N_(2m)^2`, supplies two-parameter bounded overlap, or covers
   the independent rank-one births. A concurrent self-contained Wave 9 analysis
   handles the artificial `h_0` row internally; that is project progress, not a
   theorem supplied by this literature search.
4. Local-density theorems require near-extremal finite Sidon sets; P15's coordinate
   hypothesis permits spans larger by a logarithmic factor and does not imply
   their hypotheses.
5. Random-block constructions produce a genuinely nested infinite Sidon set, but
   only in a random ambient set and at exponents below the critical all-prefix
   scale.

Accordingly the outcome is a **qualified null plus one exact structural lemma**,
not a resolution of P15.

An independent main-agent plugin pass (30 Exa slots, three empty Firecrawl
semantic searches followed by successful known-ID reads, two quota-blocked
Consensus calls, and 20 SciSpace slots) converged on the same two strongest 2026
interfaces: Ma--Yi and O'Bryant. This replication increases confidence in the
triage, but the tool limitations mean it does not upgrade the qualified null to
an exhaustive one.

## 2. Closest exact theorem: Ma--Yi rank-lag packing

For a fixed number of marks `t`, Ma and Yi consider a family of `b` Golomb rulers
whose complete positive-difference sets are pairwise disjoint and contained in
`[1,U]`. Their Theorem 1.1 proves

\[
P_t(U)=U-o(U)\quad\Longleftrightarrow\quad 3\le t\le5.
\]

For `t>=6` they obtain a positive-density leave by a Fourier obstruction. More
directly relevant to P15 is their Theorem 4.1. Selecting in each ruler every
difference of rank lag at most `q` gives

\[
m_q=\sum_{s=1}^{q}(t-s)
   =q\left(t-\frac{q+1}{2}\right)
\]

selected differences per ruler. Since all `b m_q` selected values are distinct,
their sum is at least `b m_q(b m_q+1)/2`. Each adjacent gap is counted at most
`s` times at lag `s`, so the sum is at most
`b U q(q+1)/2`. Optimizing gives

\[
A_t^{\rm S}=
\max_{1\le q\le t-1}\frac{q}{q+1}
  \left(t-\frac{q+1}{2}\right)^2,
\qquad
\limsup_{U\to\infty}\frac{P_t(U)}U
\le \min\left\{1,\frac{\binom t2}{A_t^{\rm S}}\right\}.
\]

This statement and its proof are explicit in
[Ma--Yi, Theorem 4.1](https://arxiv.org/html/2608.13739#S4). It is the closest
published mechanism found because it couples **rank lag** to the fact that
difference values occupy a finite **magnitude interval**.

### Exact mismatch with P15

Ma--Yi assume separate fixed-`t` rulers and disjoint *complete* internal spectra.
P15 instead has one ruler, increasing `t=2m`, and at epoch `m` uses the incomplete
birth triangle `j>=m`; old marks are reused at every later epoch. More importantly,
Ma--Yi sum difference lengths `a_j-a_i`. P15 sums products of two individual gaps,
multiplied by the kernel coefficient `Phi_ij` and normalized by `N_(2m)^2`.
Neither quantity uniformly dominates the other: a few large gaps can concentrate
the products while leaving the linear difference sum within the Ma--Yi bound.

## 3. New project lemma derived from the packing proof

The useful part of Ma--Yi does survive the nested geometry once the objects are
reindexed by birth epoch. The following is a derivation for this project, **not a
theorem stated in Ma--Yi**.

Let `E` be any finite set of dyadic epochs. At epoch `m in E`, choose an integer
`1<=q_m<=m` and select the birth differences

\[
D_{m,s,j}=a_j-a_{j-s},
\qquad 1\le s\le q_m,
\qquad m\le j<2m.
\]

There are exactly `m q_m` of them. Distinct endpoint pairs have distinct positive
differences in an infinite Golomb ruler, and birth epochs partition endpoint
pairs. Therefore all selected `D_(m,s,j)`, over all `m in E`, are distinct. Put

\[
M_E=\sum_{m\in E}m q_m.
\]

For fixed `m,s`, expand the selected differences into adjacent gaps. Every gap
is used at most `s` times, whence

\[
\sum_{j=m}^{2m-1}(a_j-a_{j-s})\le sN_{2m}.
\]

Summing over `s`, and comparing with the sum of the `M_E` smallest positive
integers, gives the **hereditary rank-lag packing inequality**

\[
\boxed{
\frac{M_E(M_E+1)}2
\le
\sum_{m\in E}N_{2m}\frac{q_m(q_m+1)}2.
}
\tag{W9-RLP}
\]

It is hereditary because `E` is arbitrary, not just an initial block of epochs.
It is also completely compatible with one nested branch; no independence or
branching entropy is used. In the canonical convention
`h_0=1`, `h_r=a_r-a_(r-1)` for `r>=1`, the selected interval is
`D_(m,s,j)=sum_(r=j-s+1)^j h_r`. Thus `s>=2` sees a nontrivial contiguous-sum
bulk interval, whereas `s=1` sees a newborn gap only *linearly*. It does not
control the quadratic rank-one atom built from that gap.

`(W9-RLP)` is insufficient by itself. Under
`N_(2m) <= O(m^2 log m)`, its right side retains the full logarithmic slack and
controls only linear difference values. To reach P15 one would need a weighted
upgrade that turns the layer-cake of `h_i h_j Phi_ij` into charges detectable by
`(W9-RLP)` without losing that logarithm.

As an indexing sanity check, the inequality was evaluated in 32 epoch/lag-cutoff
configurations on seven finite Golomb rulers, including `(0,1,4,6)`, the
old-clear/latest-shell witness `(0,4,5,7,78,86,166,199)`, and the scaled witness
`(0,8,24,56,58,314,318,319)`. Every distinctness, lower-sum, and upper-sum check
passed. This finite check is not the proof; the preceding global-distinctness and
gap-multiplicity argument is.

## 4. Shearer's difference-triangle LP

An `(I,J)` difference triangle set consists of `I` rulers with `J+1` marks and
globally distinct internal differences. Shearer writes each difference
`X_ijk` as a contiguous sum of top-row gaps and uses two families of valid LP
constraints:

- every set of `n` distinct positive differences has sum at least `n(n+1)/2`;
- for a set of `n` differences of average `r` and maximum `M`,
  `M >= r+(n-1)/2`.

The second family strengthens earlier LPs. His closed forms include

\[
M(I,5)\ge\frac{91I+6}{6},
\qquad
M(I,6)\ge\frac{179I+9}{8}.
\]

These statements were verified in the
[official EJC paper and PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v6i1r31).
Ma--Yi also record exactly how such asymptotic DTS bounds imply uncovered-density
bounds for fixed-mark ruler packings.

Shearer's LP is a plausible architecture for a future proof: P15 birth pairs form
a laminar family of incomplete difference triangles, and `(W9-RLP)` is one valid
constraint of that generalized LP. But the published variables are unweighted
differences and a common finite scope. The LP has no dyadic kernel, no gap-product
objective, no varying scope, and no diagonal/rank-one term. Applying it to P15
would require a new dual certificate for a **laminar weighted incomplete-DTS LP**.

## 5. O'Bryant's one-scale occupancy energy

O'Bryant proves for every infinite `g`-Golomb ruler `A` that

\[
\liminf_{n\to\infty}
\frac{|A\cap[0,n)|}{\sqrt{n/\log n}}
\le\frac{2\sqrt g}{\sqrt{\log2}}.
\]

Equivalently, for the ordered elements,

\[
\limsup_{r\to\infty}\frac{a_r}{r^2\log r}
\ge\frac{\log2}{2g}.
\]

This is an exact theorem at P15's critical scale, but it is an upper obstruction,
not construction or weighted packing. In the proof, physical intervals of length
`N` have occupancies `F_l^(t)`. Averaging the offset `t` gives one shift for which

\[
\sum_l\binom{F_l}{2}\le \frac g2(N-1),
\qquad
\sum_lF_l^2\le gN+o(N).
\]

Weighted Cauchy with
`w_l=(l log(lN))^(-1/2)` and
`sum_l w_l^2<=log 2+o(1)` then yields the liminf constant.
[O'Bryant, Theorem 1 and Section 3](https://arxiv.org/html/2606.28651v3#S3)
contain the complete argument.

This is the nearest published quadratic-energy estimate, but it is unsigned,
uses a single spatial block length at a time, and chooses a favorable physical
offset. P15 is indexed by mark births on the same branch and needs products of
specific gaps with `Phi_ij`. O'Bryant's subsequent discussion explicitly labels
multi-`N`, reverse-martingale, and entropy ideas as nonrigorous suggestions. They
cannot be promoted to a theorem. His separated gluing lemma also constructs a
large-limsup ruler through huge block jumps; as already recorded canonically, it
does not supply the all-prefix critical cap.

## 6. A genuine nested construction, but below the required scale

Kohayakawa, Lee, Moreira, and Rodl sample an ambient random set with

\[
p_m=\min\{1,\alpha m^{-1+\delta}\}.
\]

Their Theorem 2.2 constructs, almost surely, an infinite Sidon subset with
all-sufficiently-large-`n` lower bounds. The proof really is iterative: a prior
Sidon set in earlier blocks is extended by an independent set in a later block,
using deletion or an uncrowded-hypergraph theorem, followed by Borel--Cantelli.
This is therefore authentic evidence that mixed old--new conflicts can be handled
in a specially prepared nested construction.

It does not solve the prescribed P15 problem. The ambient set is random, the
blocks are chosen to enforce separation/regularity, and the guaranteed density is
at most `(n log n)^(1/3)` in the broad range, with the stronger exponent
`sqrt(2)-2+delta` only near `delta=1`. Even at `delta=1`, this is the classical
`sqrt(2)-1` exponent, below the critical `1/2` scale. The construction does not
bound P15's birth energy. See
[Theorems 2.1--2.2 and the proof overview](https://repositorio.usp.br/bitstreams/ba7fd00d-e405-4f8a-99df-a8224edecfce).

## 7. Why finite local-density theorems do not close the gap

### Riblet: unions of intervals

If an ambient set `E` of cardinality `n` is a union of `k` intervals, Riblet's
Theorem 3.1 bounds every Sidon subset by

\[
\begin{cases}
(\sqrt{\alpha^2+2}+\alpha)\sqrt n+o(\sqrt n),
 & k/\sqrt n\to\alpha>0,\\
\sqrt n+o(\sqrt n), & k=o(\sqrt n),\\
\sqrt n+k n^{1/4}+o(n^{1/4}), & k=o(n^{1/4}).
\end{cases}
\]

This controls cardinality from total ambient interval length. It has no nested
compatibility and no weights. More decisively, P15 permits
`N_(2m)` as large as `O(m^2 log m)`, for which the generic `sqrt(N_(2m))`
upper bound exceeds the actual `2m` marks by `sqrt(log m)`. The theorem is then
already satisfied with logarithmic slack. See
[Riblet, Theorem 3.1](https://arxiv.org/abs/2202.01296).

### Cilleruelo: gaps in near-extremal Sidon sets

Cilleruelo assumes a finite Sidon set in `[1,N]` has
`|A|=sqrt(N)-L` and proves quantitative equidistribution in every interval of
length `cN`; the error depends on `N`, `c`, and the positive part of `L`. In the
near-extremal regime `L=O(N^(1/4))`, this yields maximum gap
`O(N^(3/4))`. [Theorem 1.1 and Corollary 1.1](https://emis.muni.cz/journals/INTEGERS/papers/a11/a11.pdf)
were checked in the primary PDF.

P15's hypothesis does not imply near-extremality in the enclosing interval. At
the permitted logarithmic span `N asymp m^2 log m`, one has
`2m/sqrt(N) asymp 1/sqrt(log m)` and hence `L asymp sqrt(N)`. Substitution makes
the theorem's error at least the size of the desired main term. Thus it cannot
give a uniform density increment or a bounded-overlap charge for P15.

## 8. Other current candidates and exact exclusions

| Source | Verified contribution | Why it does not prove P15 |
|---|---|---|
| [Croot et al., arXiv:2606.17487v2](https://arxiv.org/abs/2606.17487) | Combinatorial large sieve using algebraic splitting modulo small primes. | Its Sidon theorem is for subsets of the squares; an arbitrary critical prefix has no fixed modular splitting deficit. |
| [Nathanson, arXiv:2608.07416v2](https://arxiv.org/abs/2608.07416) | Finite pair-sum sets with global Delta separation. | Global separation of pair sums is not a weighted theorem for contiguous differences or birth epochs. |
| [O'Bryant Part II, arXiv:2607.23795](https://arxiv.org/abs/2607.23795) | Extends the liminf obstruction to even-order `B_h` sets. | No new Sidon birth-weight control. |
| [Ruzsa, *An Infinite Sidon Sequence*](https://doi.org/10.1006/jnth.1997.2192) and [Cilleruelo, arXiv:1209.0326](https://arxiv.org/abs/1209.0326) | Explicit compatible infinite chains with exponent `sqrt(2)-1+o(1)`. | Below critical all-prefix density and construction-specific; no P15 energy. |
| [Ruzsa, *A Small Maximal Sidon Set*](https://doi.org/10.1023/A:1009757824153) | Very small finite maximal Sidon sets. | A no-go result for raw unused-difference capacity; maximality in a finite interval is not an infinite branch theorem. |
| arXiv:2604.25214 | Computational finite cyclic extension examples. | The abstract itself leaves the dilation-family proof open; wrong extension target. |
| Harmonic-analysis Sidon/Carleson literature | Powerful tree and operator embeddings. | No preservation of distinct integer contiguous sums or the P15 birth coefficients. |

## 9. Exact theorem still needed

The literature narrows the missing result to a weighted upgrade of `(W9-RLP)`.
A usable theorem must do all of the following simultaneously:

1. decompose `h_i h_j Phi_ij` by rank lag and gap-size thresholds;
2. assign each layer to distinct contiguous-difference magnitude capacity;
3. prove bounded overlap across both dyadic birth epoch and rank lag on the same
   branch;
4. lose `o(log J)`, not the full logarithm permitted by the coordinate cap;
5. either separately charge the rank-one births, for which rank-lag packing
   records the newborn gap only linearly, or explicitly invoke the project's new
   summability proof for the artificial `h_0` row; and
6. remain valid on a single surviving ray, without branching entropy.

The concurrent internal file
`core_workspace/endpoint_variance/WAVE9_BIRTH_BUDGET_CARLESON_ANALYSIS_2026-08-29.md`
already reduces the unresolved mass to survival-conditioned long-rank,
two-large-endpoint core tiles and proves a four-parameter local Carleson-box
estimate. The literature supplies no theorem that discharges that surviving
condition. A promising concrete next step is therefore to add `(W9-RLP)` for
every epoch subset and lag cutoff as valid global constraints in a finite
**laminar weighted incomplete-DTS LP** for those core tiles. Stable exact dual
multipliers may suggest the missing survival-conditioned Carleson certificate;
failure on the canonical counterexamples would identify the needed extra
constraint before another proof attempt.

## 10. Bottom line for the canonical proof state

P15 remains open. Ma--Yi/Shearer provide the best rigorous rank-lag/magnitude
packing interface, and `(W9-RLP)` imports that interface to a single nested branch
without extra assumptions. Combined with the concurrent internal reduction, the
unresolved step is not ordinary distinctness or finite density; it is
survival-conditioned, cross-epoch non-saturation of the weighted core tiles, with
sublogarithmic loss.
