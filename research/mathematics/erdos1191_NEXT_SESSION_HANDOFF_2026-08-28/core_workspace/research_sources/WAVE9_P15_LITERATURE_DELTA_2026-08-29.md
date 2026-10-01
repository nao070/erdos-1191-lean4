# Wave 9 P15 literature delta — 2026-08-29

## Qualified conclusion

The primary literature checked through 2026-08-29 does not prove the P15 birth
budget or provide a black-box theorem that can be substituted for it. The best
exact interface is rank-lag difference packing from Ma--Yi and Shearer's
difference-triangle LP. Wave 9 imports that interface to one nested branch via
the hereditary inequality below, but the conversion to the exact
`h_i h_j Phi_ij/N_(2m)^2` weights remains open.

Full provenance, queries, saturation limits, and source-by-source exclusions are
in:

- `research_sources/wave9_literature_state/QUERY_LOG.md`
- `research_sources/wave9_literature_state/PRIMARY_SOURCE_AUDIT.md`
- `research_sources/wave9_literature_state/research_state.json`

## Exact primary interfaces

### Ma--Yi small-rank-difference bound

For families of fixed-`t` Golomb rulers with pairwise-disjoint complete positive
difference sets in `[1,U]`, define

\[
A_t^{\rm S}=
\max_{1\le q\le t-1}\frac{q}{q+1}
\left(t-\frac{q+1}{2}\right)^2.
\]

Then

\[
\limsup_{U\to\infty}\frac{P_t(U)}U
\le\min\left\{1,\frac{\binom t2}{A_t^{\rm S}}\right\}.
\]

The proof selects all differences of rank lag at most `q`, uses distinctness for
a quadratic lower bound on their sum, and counts each adjacent gap at most `s`
times at lag `s`. Primary source:
[Ma--Yi, Theorem 4.1](https://arxiv.org/html/2608.13739#S4).

### Shearer LP inequalities

For an `(I,J)` difference triangle set, every set of `n` selected differences
has sum at least `n(n+1)/2`. If those differences have average `r` and maximum
`M`, then `M>=r+(n-1)/2`. Shearer's closed forms include

\[
M(I,5)\ge\frac{91I+6}{6},\qquad
M(I,6)\ge\frac{179I+9}{8}.
\]

Primary source: [official EJC paper](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v6i1r31),
DOI `10.37236/1463`.

## Wave 9 hereditary rank-lag packing lemma

This is derived for the project; it is not stated in the cited papers. For any
finite set `E` of dyadic epochs and choices `1<=q_m<=m`, select

\[
D_{m,s,j}=a_j-a_{j-s},
\qquad 1\le s\le q_m,\quad m\le j<2m.
\]

These are birth pairs, so all selected values are globally distinct. With
`M_E=sum_(m in E) m q_m`, expansion into adjacent gaps gives

\[
\boxed{
\frac{M_E(M_E+1)}2
\le
\sum_{m\in E}N_{2m}\frac{q_m(q_m+1)}2.
}
\tag{W9-RLP}
\]

The inequality is valid for an arbitrary epoch subset and uses only one nested
Golomb branch. It is therefore a legitimate rank-lag/magnitude constraint for a
future P15 LP or Carleson argument. In canonical gap indices,
`D_(m,s,j)=sum_(r=j-s+1)^j h_r`; the `s=1` lane records a newborn gap only
linearly and does not control its quadratic rank-one atom.

## Why this does not yet prove P15

1. `(W9-RLP)` controls linear difference lengths, not the nonlinear gap products
   `h_i h_j` or the kernel `Phi_ij`.
2. Under `N_(2m)<=O(m^2 log m)`, the right side retains the entire logarithmic
   slack; no source removes it by two-parameter bounded overlap.
3. The rank-one objective remains uncontrolled: the lag-one packing constraint
   sees each newborn gap linearly, not its quadratic birth atom. The concurrent
   internal Wave 9 analysis separately sums the artificial `h_0` row; that step
   is not supplied by Ma--Yi or Shearer.
4. Ma--Yi and Shearer use fixed-size complete rulers with a common scope, while
   P15 has varying, laminar, incomplete birth triangles.
5. Local-density results of Riblet and Cilleruelo require finite near-extremality.
   P15 permits `N_(2m) asymp m^2 log m`, where `2m/sqrt(N_(2m))` can be only
   `asymp1/sqrt(log m)`.
6. Random-block extension theorems construct special nested Sidon sets below the
   critical all-prefix exponent and do not control the P15 weights.

## Current sources that do not alter open status

- [O'Bryant, arXiv:2606.28651v3](https://arxiv.org/html/2606.28651v3): exact
  critical liminf obstruction and one-spatial-scale occupancy energy; the
  multi-scale/martingale/entropy ideas are explicitly nonrigorous suggestions.
- [Croot et al., arXiv:2606.17487v2](https://arxiv.org/abs/2606.17487): large
  sieve for algebraically structured sets of squares, not arbitrary prefixes.
- [Nathanson, arXiv:2608.07416v2](https://arxiv.org/abs/2608.07416): finite
  globally Delta-separated pair sums, not weighted contiguous-sum births.
- [Kohayakawa--Lee--Moreira--Rodl](https://doi.org/10.1137/17M1114934): genuine
  iterative extension in a random ambient set, but at subcritical exponents and
  without the P15 energy.
- Riblet's union-of-interval bounds and Cilleruelo's near-extremal gap theorem:
  quantitatively nonuniform over the P15-allowed logarithmic span.

## Next proof target suggested by the literature

The concurrent internal Carleson analysis has already reduced the unresolved mass
to survival-conditioned long-rank, two-large-endpoint core tiles. Formulate a
finite laminar weighted incomplete-DTS LP for that core. Include `(W9-RLP)` for
every epoch subset and lag cutoff, use the exact P15 atom weights as the objective,
and search for stable exact dual certificates. The missing analytic lemma is a
survival-conditioned cross-epoch non-saturation estimate with sublogarithmic total
overlap. Any proposed dual must be tested against every mandatory P15 finite
counterexample before being promoted to an infinite theorem.

**Canonical status:** P15 remains the highest-priority open theorem.
