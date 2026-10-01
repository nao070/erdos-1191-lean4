# Independent review: coherent full-defect source

2026-09-05. Independent analytical review of `research/coherent_defect_source.md`, final SHA-256 `6f25451c2cb22a9dae3f0f7347a8b83a9f16a91f2979ffdc687ccb552fbd9f97`. Final source readback: **2026-09-05T15:01:25.679291+00:00**. This revision supersedes review SHA-256 `a776bb05dfe1af69dafe920105b546c562b84895828c32d00ae983d8af478dfc`.

**Result:** all equations (1)–(15), the repaired actual pair-budget transfer, and the final residual identity are supported. The parent identified a real scope gap in the original general-allocation argument: original pair constraints need hold only where Theta's component is positive. The previous review's transfer proof imposed the stronger condition on every physical pair, so it did not justify the original claim for an arbitrary feasible allocation. The updated source repairs that gap by clipping the transferred pair portions and restricting the error charges to the positive support of the original component. Section 3 below verifies that repair explicitly. The previously used disjoint-cell allocation was already valid, since its masks are disjoint on every pair.

The coordinated clarification that the terminal coordinate is relative to `a_1` remains in force. Replacing only the new general-transfer passage by the old passage reconstructs source hash `fbfe703c8b6b181d18c99c61294d0f7810e6d6f98806f983d61445c0474cba05` exactly; all other formulas and reviewed text are unchanged. No further correction is required. The source is a replacement physical source, not a PSD remainder after debiting Theta from an old reserve. Original Q1 remains unresolved. No numerical, Lean, or previously successful verification was rerun for this review or its repair.

## 1. Monotone potential, trace, and the exact terminal comparison

For each `k>=2`, the signed bank has exactly `Q_k` labels. A constant feature of value `sqrt(V_k)/(2Q_k H_k)` gives the matrix in (1), with zero extension outside its bank. Its full matrix mass has `Q_k^2` summands, and its trace has `Q_k` summands. This yields exactly (2), including the ratio `1/Q_k` only when `V_k>0`. A zero potential produces a zero component.

The assumed upper bound on `V_k` makes every entry at most `1/4`. Direct subtraction of the rank prices gives

```
kappa_k Q_k = 4/[(k-1)(k+1)^2]
            = 1/(k-1)-1/(k+1)-2/(k+1)^2.
```

Its sum from two is `4-2zeta(2)`, verifying (3). Since the trace summands are nonnegative, the infinite trace sum is legitimate. Restricting any later component to `Fhat_N` leaves exactly `Q_N^2` entries, so its total tail is at most `Q_N^2 alpha_(N+1)/4`. This is exactly the factor in (4). In particular every finite restriction converges entrywise and is a limit of PSD, entrywise nonnegative matrices. No claim of finite total matrix mass on the whole infinite label set is needed for Gamma.

The layer identity follows by expanding `u_r` and interchanging nonnegative sums:

```
sum_(r=2..N) u_r (V_r-V_(r-1))
 = sum_(k>=2) kappa_k V_min(k,N)/H_k^2.
```

For `k<=N`, the corresponding contribution to the restricted Gamma mass is exactly one quarter of this quantity. The discrepancy consists only of the two tails displayed in the source. Call their nonnegative sums `A_N` and `B_N`. Both satisfy `0<=A_N,B_N<=R_N`, where

```
R_N = (N-1)^2/[4(N+1)^2].
```

For `B_N`, use `V_N<=Q_N^2H_N^2` and monotonicity of `H_k`. Thus `|A_N-B_N|<=R_N`, not merely `2R_N`; (5) retains the correct sharper constant. Literal historical capacity charges a subset of the unordered distinct-label entries of one fixed nonnegative matrix. It is therefore at most half its full restricted mass, giving (6). The complete future tail and never-used outputs are covered by this estimate.

## 2. Direct financing by the actual full defect

The imported actual stage theorem gives nonnegative increments of `Gcum_k(lambda)`, and the exact identity

```
Gcum_k(lambda)=(1+lambda)Y_k-8Hcum_k(lambda).
```

Since the eligible carrier is nonnegative, `V_k=Gcum_k/(1+lambda)` is a nonnegative monotone potential bounded by `Y_k`. Here `Y_k=E_k-kZ_k`, not the full energy `E_k`. Young's inequality gives `E_k<=k^2 Z_k`, so

```
Y_k <= (k^2-k)Z_k = Q_k Z_k <= Q_k^2 H_k^2.
```

This verifies the upper-bound hypothesis of Section 1 with the correct diagonal removal. The rank-one source therefore applies directly, with no cubic fiber error. Equation (7) follows by scaling (6).

The old exact eligible identity is `Elig_N(Psi_lambda)=(1+lambda)Ycal_N/8-Gcal_N/8`. Additivity of eligible pair entries and `Elig_N(Gamma_lambda)<=C_N(Gamma_lambda)` then give (8). The same defect is used once, to finance the one added component `(1+lambda)Gamma_lambda`. Historical capacity covers more pairs than eligibility, so using it for the upper estimate does not assert a PSD property of an eligibility mask.

## 3. Entrywise replacement and a single globally finite error

For the previous translate Gram, Cauchy bounds each cross-correlation by the squared norm `L_k`, proving (9). The constant matrix `B_k` is a new PSD matrix with the same diagonal as `A_k`. Entrywise domination says nothing about PSD domination: a nonzero symmetric matrix with zero diagonal cannot be PSD. Thus the previously established `gamma J-A_k` obstruction remains intact.

The full-fiber inequality from the earlier source gives

```
L_k/(Q_k^2H_k^2)
 <= Gcum_k/[4(1+lambda)Q_k^2H_k^2] + k^3/(6Q_k^2).
```

The first term is exactly the entry of the new component `C_k^V`; this establishes (10) component by component, not just after aggregation. Every error component is a constant nonnegative Gram. Its full matrix mass is `k^3/6`, before multiplying by `kappa_k`. Summation by parts yields

```
sum_(k>=2) kappa_k k^3
 = 8alpha_2 + sum_(k>=3)alpha_k(3k^2-3k+1)
 = 2zeta(2)+1/4.
```

Tonelli therefore proves (11) on the complete infinite physical label set. The unordered-pair error is at most half this mass; diagonal entries need not be assigned any physical payment.

The support restriction in the repaired transfer is essential for an arbitrary feasible allocation. Work component by component and write `A_h=A_k(h)`, `E_h=E_k(h)`, and `G_h=C_k^V(h)` on actual unordered distinct-label pairs. The componentwise comparison is `0<=A_h<=G_h+E_h`. Define

```
c_h = max(A_h-E_h,0),       e_h = E_h 1[A_h>0].
```

Then `0<=c_h<=G_h`, both `c_h` and `e_h` vanish when `A_h=0`, and `A_h<=c_h+e_h`. This holds also when `G_h=0`, since then `A_h<=E_h` forces `c_h=0`.

Let `f_(I,h)>=0` denote the original row fraction, including its physical row mask. General feasibility requires `sum_I f_(I,h)<=1` whenever `A_h>0`; no bound is needed on the zero entries of `A`. For component coefficient `kappa_k`, define the row's old, transferred, and error payments by

```
a_I = kappa_k sum_h f_(I,h) A_h,
p_I = kappa_k sum_h f_(I,h) c_h,
e_I = kappa_k sum_h f_(I,h) e_h.
```

The support conditions ensure that every nonzero contribution to `p_I` or `e_I` occurs where the original feasibility constraint applies. In particular the transferred portions form a valid physical allocation of Gamma: for `G_h>0`, their fractions of its entry are `f_(I,h)c_h/G_h`, whose sum is at most one; for `G_h=0`, assign zero. Thus no condition on the original unconstrained zero entries is silently imported.

If `delta_I<=a_I` is the original nonnegative proved demand, then

```
delta'_I = max(delta_I-e_I,0) <= p_I,
delta'_I >= delta_I-e_I.
```

Summing the restricted error uses only the original constrained support, giving `sum_I e_I<=kappa_k sum_h E_h`. Summing further over all components is at most the one global unordered error allowance `[2zeta(2)+1/4]/12`. This proves the repaired general form of (12). All physical row masks are preserved; across components their coefficients are distinct fixed summands. As an optional exact local accounting identity, one could replace `e_h` by `min(A_h,E_h)`, since `A_h=c_h+min(A_h,E_h)`; the source's stated restricted error already suffices.

These clipped portions are allocations of entries of the unchanged PSD source Gamma. No clipped matrix is claimed PSD, and no equivalence with Gamma's unmodified affine-row optimization problem follows. The retained demand is a valid lower bound on its allocated actual pair payment, rather than necessarily the standard closed-form Gamma projection demand. For disjoint-cell allocations all masks are already disjoint on every physical pair, so the earlier unrestricted error proof was sufficient for that specific construction. The general support repair does not alter the independent direct-demand proof in Section 4.

## 4. Polylogarithmic endpoint range and all horizon constants

In a cell strictly after bank `k`, constant-feature convolution has total mass `m_j` times the feature sum, exact diagonal `m_j T_k`, and supporting interval with at most `3D` sites. Ordinary mass projection therefore yields the displayed `J_j`. Empty cells contribute zero, and positive-part selection loses no validity. Actual Sidon uniqueness implies that different disjoint cells have disjoint internal differences, so all these rows together use each component pair at most once.

The counting estimate from the one fixed cap and the finite Hardy inequality concern the same actual cumulative occupancies `F_j`. For the proposed range,

```
j0 = ceil((log k)^2),     J = floor(k^2/(log k)^2),
k(k-1)/2 <= D <= Ck^2 log(2k),
```

the minimum of the square-root lower bound divided by `k` tends to infinity at least as a fixed-`C` multiple of `sqrt(log k)`. One may use the lower bound on `D`, the lower bound on `j`, and the uniform upper bound `log(4jD+4)=O_C(log k)` throughout the range. Hence subtraction of `k+1` produces a multiplicative `1-o(1)` uniformly over all retained cells.

The Hardy sum is asymptotic to the integral of `1/[j log(4Dj)]`. The ratio of its upper and lower logarithmic endpoints tends to `4/2=2`, because `log D=2log k+O_C(log log k)`. Rounding, the replacement of `j/(j+1)^2` by `1/j`, and the additive constant inside the logarithm have vanishing error. This gives (13) with coefficient `D/(4C)` and factor `log 2`.

The terminal coordinate relative to `a_1` is at most `(J+1)D=O_C(k^4/log k)`. The unconditional actual Sidon count bounds the total number of points by `O_C(k^2/sqrt(log k))`. Since `T_k/M_k=1/Q_k`, the complete diagonal loss divided by `M_k` is `O_C(1/sqrt(log k))`, uniformly whenever `V_k>0`. Combining it with (13) gives the leading coefficient `log 2/(24C)` and the eventual safe fraction `log 2/(48C)` in (14). The onset depends on the one cap and its onset, not on the size of `V_k`. No uniform fraction over arbitrary cap constants is asserted.

On a sufficiently late good dyadic window, the prior cumulative-defect estimate implies `V_N>=beta^2 N^6H_N/2`. Monotonicity and `H_k<=K H_N` then give the stated lower bound `M_k>=beta^2N^6/(8K^2H_N)` for every `N<=k<2N`. Multiplying by the window price sum and the demand fraction gives

```
[15 beta^2/(128 K^2 C log(2N))] * [log 2/(48C)]
 = 5 beta^2 log 2/[2048 K^2 C^2 log(2N)],
```

which is exactly (15). The good-window reciprocal-log sum is an imported actual-history consequence of the same fixed cap. Windows have disjoint component indices, and every fixed component uses finitely many cells. Every fixed finite collection of these rows therefore occurs by a finite actual terminal rank; taking terminal ranks to infinity includes all of them. There is no interchange that creates an extra copy of a component budget.

## 5. Remaining scope

The final residual decomposition is exact by linearity of eligible payments in the combined source. Both residual summands remain nonnegative for the stated feasible additive allocations. Divergent new paid demands do not imply that either residual is bounded or negative, and the full defect cannot be financed twice. The new construction supports a replacement source and a finite-error entrywise demand transfer; it supplies no recursive PSD remainder, uniform terminal capacity bound, or cap contradiction. All results reviewed here are analytical and remain distinct from the separately verified finite ordered-fiber Lean bridge.
