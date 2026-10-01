# Adversarial review: fixed-window localization obstruction

Date: 2026-09-05. Scope: sections 3--4 of `GLOBAL_OBSTRUCTION_ANALYSIS.md`, including the exact connection to the earlier positive cross-ratio floor. Verdict: **PASS with the explicit dyadic `n>=16` floor hypothesis and the original-budget scope stated below.** This review uses algebra and the source definitions, not a finite search.

## 1. The index distinction is real; the constant 384 survives

The memo's `W_n` is exactly the Wave-19 inner sector

`sum_{j=n+2}^{2n-1} sum_{i=n}^{j-2} (j-i)^2 C_ij/(4n^2)`.

It is **not** literally Wave-13 `Z_n^nb`, whose left index begins at `n-1` and whose gap set has `n+1` elements. The relevant sources are:

- `route_probes/ROUTE_C_CROSS_RATIO_BOX_DIPOLE_BRIDGE.md`, equations (1.1)--(1.2), for the exact positive primitive and `W_n` definition.
- `core_workspace/endpoint_variance/WAVE13_P18_HARMONIC_OBSTRUCTION_2026-08-29.md`, sections 1--3, for the original layered argument on `n+1` gaps.
- `core_workspace/endpoint_variance/WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`, sections 4--5, for the already written adaptation to the required `n` gaps.

The adaptation was independently checked, rather than inferred from the larger sector's lower bound. Set `G={n,...,2n-1}`, `H=sum_{i in G} h_i=a_(2n-1)-a_(n-1)`, and

`Q_i=sum_{j in G, |j-i|>=2} |j-i|^2 h_j`.

For `2<=r<=n/2`, at most `2r-1` indices are within distance less than `r` of `i`, so at least `t_r=n+1-2r` remain. Sidonicity implies that the adjacent gaps are distinct positive integers; hence their sum on this far set is at least `t_r(t_r+1)/2`. Since `d^2>=sum_{r=2}^{min(d,n/2)}(2r-1)`,

`Q_i>=E'_n=sum_{r=2}^{n/2}(2r-1)(n+1-2r)(n+2-2r)/2`

`=n(n-2)(n^2+4n-14)/48`.

The cross-ratio product bound is also exact: with `D=M+u+v`,

`C_ij=log(1+uv/(MD)) >= uv/(MD+uv) >= uv/D^2 >= h_i h_j/H^2`.

Each unordered pair occurs twice in `sum_i h_i Q_i`. Therefore

`W_n >= [sum_{i<j, j-i>=2}(j-i)^2 h_i h_j]/(4n^2 H^2)`

`>=E'_n/(8n^2 H)`.

Finally,

`E'_n-n^4/48=n(n^2-11n+14)/24>=0`

for dyadic `n>=16` (indeed for every even `n>=10`). Thus

`W_n>=n^2/(384H)>=n^2/(384a_(2n-1))`.

There is no extra factor of two to lose: the factor `1/2` from unordered pairs has already produced the denominator `8`. Under the fixed cap `a_(2n-1)<=4Cn^2 log(4n)`, the resulting `1/(1536C log(4n))` floor is valid. Applying the 384 bound at arbitrary smaller `n` would require a separate check and is not approved by this review.

## 2. Bounded-rank upper bound and its scope

For nonadjacent gap pairs, integer spacing gives `M>=1`, while `M+u<=H`. Hence

`0<=C_ij<=log((M+u)/M)<=log H`.

There are exactly `n-d` available pairs of gap-rank separation `d`, and using the looser bound `n` yields

`W_n^(<=L)<=log(H)/(4n) sum_{d=2}^L d^2`

`<=L(L+1)(2L+1) log(H)/(24n)`.

Combining with the verified lower floor gives precisely the memo's factor `64C` in the fraction bound. For fixed `C,L`, it tends to zero; the more general sufficient condition `L^3(log n)^2/n -> 0` is correct for fixed `C`.

A consecutive 16-mark window contains 15 gaps and therefore only pairs of gap-rank separation at most 14. The conclusion applies when the total coefficient allocated to each original primitive satisfies `0<=lambda_ij<=alpha_ij`. Under this original-budget condition, any family of these windows contributes at most `W_n^(<=14)`, independently of overlap or window selection. A window's intrinsic smaller-rank normalization cannot be substituted for the global `alpha_ij` without a separately proved source of capacity.

This does not obstruct signed corrections, distant roots, a genuinely different reserve, or an inequality on a restricted actual-state family.

## 3. A stronger valid consequence: fixed-window mass is summable

For fixed `C,L` and dyadic `n=2^k`, the cap gives `log H=O_C(k)` for sufficiently large `k`. Therefore

`W_(2^k)^(<=L)=O_(C,L)(k/2^k)`.

Its sum over dyadic epochs converges, and every Fejer-weighted partial sum is bounded because the weights lie in `[0,1]`. In contrast, the full sector has

`sum_{k=k0}^J omega_(k,J) W_(2^k) >= [1/(1536C log 2)] log J-O_(C,k0)(1)`.

Thus fixed positive windows using original capacities have bounded total mass and cannot supply the required logarithmically diverging signal. This is a conditional architectural obstruction on capped finite towers or a hypothetical capped infinite branch; it neither constructs that branch nor resolves Q1.

## 4. Literal matrix pasting

The `n` gap coordinates correspond to `n+1` physical points `a_(n-1),...,a_(2n-1)`. For local interior point indices `1<=i<j<=n-1`, `d=j-i>=3`, every mixed-difference term lies outside the suppressed diagonal and first off-diagonal of `B_n`. Consequently

`(D^T B_n D)_ij=[-2d^2+(d-1)^2+(d+1)^2]/(8n^2)=1/(4n^2)`.

A matrix supported within a consecutive window of `L+1` physical coordinates is zero whenever `|i-j|>L`. Every finite linear combination has the same band restriction, even with arbitrary signs. It cannot equal the displayed matrix when `n-2>max(L,2)`. This proves the stated literal-equality obstruction. It makes no claim about domination on actual Haar/box states or about compositions involving new nonlocal operators.

## 5. Requested precision changes

The author was asked to state the dyadic `n>=16` hypothesis and the `n`-gap derivation explicitly, distinguishing it from Wave-13's larger sector. A nearby section-5 wording also needs care: a lower bound tending to zero does not by itself prove that the actually realizable Sidon family has collapsed points in its closure. It proves that the stated estimates do not supply uniform separation; the parameter region they allow contains degenerate boundary points. This wording issue does not affect the two proofs reviewed above.
