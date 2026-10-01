# Independent review: C143 fixed-history weight extension

Reviewed 2026-09-05. Verdict: **PASS for the stated conditional fixed-history claim.** No blocking mathematical error found. This is not a new verification of the bank's primal gate feasibility or a global Q1 theorem.

## Reviewed objects and replay

- `c143_weight_extension.py` SHA-256: `c29c338154f2ef370b327349469987c3d1bc096c8b40b5fedfe9d8f2a19b1a04`.
- `C143_WEIGHT_EXTENSION.json` SHA-256: `654b29c591747cc89df1da472bc2d5dc9ead0dcc006ad5457b100fa2e45c6a7c`.
- Bank SHA-256: `d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`.

Executed the script in a separate Python process, writing only `/tmp/c143_weight_extension_review_replay.json`; it exited successfully and reproduced the reviewed JSON byte for byte. Independently inspected the V2 `c142/master.py`, `c143/exact_phase.py`, and `c143/geometry.py` definitions. Main files were not edited.

## Mathematical checks

1. **Weight monotonicity.** For each new-epoch owner gate, the RHS is `max(rho*d,0)` with signed unweighted demand `d`; its LHS and graph support do not depend on `rho`. For `0<rho<=1`, this RHS is at most `max(d,0)`. Old-epoch and preold constraints are unchanged. Therefore any verified nonnegative graph support at weight one stays feasible. Its retained-support margin is exactly `M_rho(t)=M_1(t)-2(1-rho)D_new(t)`; no dual optimality at reduced weight follows or is claimed.

2. **Pair autocorrelation normalization.** The half-open Haar autocorrelation at positive separation `d` is `2W-3d` on `d<=W`, `d-2W` on `W<=d<=2W`, and zero beyond. With `q=(8/m)h`, direct factor `m/128`, and the factor two for unordered off-diagonal pairs, the multiplier is `(m/128)*(8/m)^2*2=1/m` times `M_ij`. Since `8e^2 M` is the integer matrix used by the script, its coefficient `matrix[i][j]/(8e^2 m)` is correct. The diagonal vanishes because both the diagonal and first off-diagonal of `B` vanish. The separate half-open cell summation checks ten epoch/phase combinations exactly.

3. **Affine endpoint transfer.** Demand is affine between `d/m` and `d/(2m)` breakpoints; the script checks absence of internal pair breakpoints. On each certified child, retaining its support makes the transferred margin affine in phase. Endpoint positivity therefore gives positivity throughout that child. Collapsed geometric endpoints are treated explicitly. The reported minimum normalized margin is also valid: an affine `M(t)/t` is monotone or constant on each positive-phase child. For the whole interval `rho in [97/100,1]`, linearity in `rho` reduces the bound to its two endpoints. Independently checked that both reported original minima exceed their transferred counterparts, so the lower-endpoint minima reported in this particular hash-pinned run are valid uniformly over the entire weight interval, even without presuming `D_new>=0` everywhere.

4. **Exact numeric consequences.** The retained-support allowable loss is `18976473121/539545531140 > 3/100`. The transferred minimum margin is `6975267967/7664025600 > 0`. For `L=2075/8`, integrating the uniform margin floor against `dt/t^2` on `[L,2L]` gives exactly the claimed lower bound `6975267967/3975713280000` (approximately `0.00175446957`). This lower bound needs no logarithm approximation.

5. **Fejer index convention.** Under the project's taper `omega_(k,J)=((J+1-k)/(J+1))^2`, an adjacent pair `(k,k+1)` has ratio `omega_(k+1,J)/omega_(k,J)=m^2/(m+1)^2` when **`m=J-k`**. Thus the script's minimum is correctly `m=66`: `4225/4356 < 97/100 <= 4356/4489`. If using the alternative old-epoch coordinate `s=J+1-k`, the equivalent threshold is `s>=67`. These indices must not be interchanged.

## Dependency and scope boundary

The proof assumes the separate bank verification establishes nonnegative primal graph coefficients, every owner gate, correct child containment, complete phase coverage, and endpoint consistency. Hash pinning identifies the object; it does not prove those properties. The original integral fences in this script are comparisons against stored bank bounds, not an independent replay of that logarithmic integral; the transferred integral floor above is newly checked algebraically.

The script explicitly leaves all histories, all ranks, global owner payment, and Q1 unresolved. Extending one 64-mark history to nearby weights does not establish a uniform theorem for hypothetical infinite counterexamples, nor an admissible global charging scheme. The Fejer threshold describes this fixed-history certificate's weights only.

For any future generalization away from the pinned bank, it would be prudent to assert `0<rho<=1` and take the uniform weight-interval bound as the minimum of both weight-endpoint minima explicitly. The reviewed bank satisfies these conditions; they are not blocking findings here.
