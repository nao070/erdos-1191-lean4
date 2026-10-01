# Independent review: causal Fourier coefficient route

Reviewed 2026-09-05. This is an independent analytical review, not a Lean verification or a new numerical experiment. The reviewed source is `research/causal_fourier_coefficient_route.md`, SHA-256 `344529631f892c8577f7caa45e440b422fb9de8f3a6d06c3a52031fbfb98a820`. Current source readback was checked at **2026-09-05T14:24:02.424397+00:00**.

**Result:** all six displayed identities or estimates are supported at their stated scope. No mathematical correction to the source is required. The new exact identity keeps actual causal eligibility and the output birth price. The ordinary Carleson theorem supplies the point-polynomial maximal estimate, but does not supply the missing coefficient estimate. Original Q1 remains unresolved.

## 1. Signed kernel and actual causal coefficient identity

For a positive output `t`, a same-sign positive pair has magnitudes `d+t,d`; its weight is `(1+lambda)d(d+t)`. The negative reflected pair contributes the same weight. These are exactly the factor `2(1+lambda)K_n^+(t)` in (1). For opposite signs the only orientation giving positive output is `(x,-y)`, where `x,y>0` and `x+y=t`; its weight is `(1-lambda)xy`. The coefficient of `h_n^2` has the correct multiplicity: the ordered splits `(x,y)` and `(y,x)` represent distinct signed source pairs if `x!=y`, whereas the equal split occurs once. Thus (1) has neither a missing factor nor a duplicated unordered-pair factor.

All coefficients are nonnegative for `0<=lambda<=1`. Strict positive-frequency projection and the absence of zero in the positive gap bank make the constant term zero.

For an actual output `a_r-a_i`, both source labels lie before the lower endpoint precisely when they lie in `Fhat_(i-1)`. Equivalently their maximum endpoint birth satisfies `b<i<r`. Sidon uniqueness implies that this output has no representation before rank `r`, and exactly one after that rank. Consequently its complete-history price is `u_r`, independent of which eligible source pair produces it. Equation (2) is therefore a literal sum of eligible pairs at their output prices. It does not replace an output price by a source birth price.

The polynomial coefficient also enforces the order: a summand indexed by `i>=r` cannot contribute at frequency `a_r`, because all frequencies of `C_(i-1)` are strictly positive. For `i<r`, Sidon uniqueness identifies the actual output endpoints, so the summation introduces no further representation multiplicity. Orthogonality of characters for normalized Haar measure gives the stated integral identity without changing the allocation budget. The terminal restriction concerns output ranks at most `T`; the coefficients `u_r` still depend on the complete fixed history.

The reciprocal-price definitions are used for ranks at least two. The polynomial at rank one is zero. In (6), the inherited lower-endpoint index range is `2<=i<r`, as in the definition of `Q_T`; no undefined rank-zero bank is needed.

## 2. Primary Carleson theorem and the order obstruction

The author-hosted paper states Theorem 1.1 directly on the circle for ordinary Fourier partial sums, with `r>2` and `r'=r/(r-1)<p<infinity`. Thus `r=3,p=4` is admissible. Its homogeneous variation seminorm controls the required maximal function here because the positive-frequency polynomial has zero constant coefficient, hence its cutoff-zero partial sum is zero. The theorem does not provide a general `r=2` variation estimate. [Oberlin–Seeger–Tao–Thiele–Wright, Theorem 1.1](https://webhomes.maths.ed.ac.uk/~wright/papers/osttw0710.pdf).

For the finite polynomial `F_T`, the symmetric numerical cutoff `a_n` includes exactly the positive frequencies `a_1,...,a_n`. Expanding its fourth power, the Sidon property leaves precisely the two trivial orderings of each two-sum, with the diagonal counted once. Therefore

```
||sum c_j z^(a_j)||_4^4
 = 2(sum |c_j|^2)^2 - sum |c_j|^4.
```

This proves the norm used in (3), including the unweighted value `2T^2-T`. The coefficients `a_j-a_1` are fixed across the partial sums, so the weighted application has the same legitimate partial-sum structure.

The source's positive Sidon example is exact: `{1,11,12}` has unordered two-sums `2,12,13,22,23,24`, all distinct. Its second-prefix gap polynomial is `10z^10`; the third is `z+10z^10+11z^11`. A numerical cutoff that includes frequency ten already includes frequency one, so the earlier gap polynomial cannot be that kind of truncation of the later one. This rejects the proposed direct identification, not all possible Fourier estimates.

The Laurent expansion `|F_n|^2=n+sum_d(z^d+z^(-d))` gives (4) after applying `z d/dz`: the negative frequencies acquire coefficients `-d`, while the positive ones acquire `d`. Thus `D(|F_n|^2)=h_n-conjugate(h_n)` and its strict positive projection is `h_n`. A separate scalar projection bound on each such differentiated quadratic input does not justify exchanging that projection with a pointwise maximum. No estimate for (2) follows just from (3) and (4).

## 3. Actual graph bound and harmonic summation

For fixed `t>0`, each edge has endpoints differing by `t` in the actual signed label bank. A vertex can meet only its neighbors at distance `t` on either side, hence degree at most two. Orienting each edge to give positive output selects it once. Since

```
|de|+lambda de <= (1+lambda)|de|,
|de| <= (d^2+e^2)/2,
```

the sum is at most `(1+lambda)Z_n`. There are exactly `Q_n` signed nonzero labels, all of magnitude at most `H_n`, proving both inequalities in (5). This argument includes opposite signs and the equal-magnitude opposite pair.

The price bound follows from monotonicity of the span and telescoping the nonnegative increments:

```
u_r <= H_r^(-2) sum_(k>=r) kappa_k
    = 1/(Q_r^2 H_r^2).
```

For `2<=i<r`, one has `Q_(i-1)<=Q_(r-2)` and `H_(i-1)<=H_r`. Using the loose count `r-1` gives the first inequality in (6). The remaining factor is exactly

```
(r-1)Q_(r-2)/Q_r^2
 = (r-2)(r-3)/(r^2(r-1)) <= 1/r.
```

The rank-three expression vanishes, and rank two has no eligible lower endpoint. Thus there is no exceptional positive contribution omitted at the onset. This bound requires no growth cap and gives only a harmonic upper estimate. It is compatible with divergent demands; it is neither a uniform-in-terminal-rank bound nor a proof that the capacity itself grows harmonically.

## 4. Literature scope and unresolved implication

O'Bryant's version-three primary record gives the positive upper constant `2 sqrt(g)/sqrt(log 2)` for the stated normalized liminf. The version-three text labels Section 3.1 as nonrigorous further thoughts. Neither statement supplies the zero liminf sought here. This review imports no other formula or normalization from that paper. [Primary record](https://arxiv.org/abs/2606.28651), [version-three text](https://arxiv.org/html/2606.28651v3).

A uniform-in-`T` upper bound for the actual functional (2), for every history satisfying one fixed cap, would combine with the previously established eligible-demand divergence to rule out such a capped history. The present note proves no such upper bound. Its established result is the exact causal coefficient formulation and the verified scope of the available elementary and Carleson estimates. This audit ran no numerical or Lean checks, changed no authored source, and does not change the formal status of Q1.
