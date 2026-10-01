# Actual birth geometry and the centered born-dead spectrum

Status: an exact finite obstruction to automatic terminal-to-historical **gap** transfer is proved below. The asymptotic question whether actual capped Sidon prefixes force a centered born-dead eigenvalue of order `p²/log p` remains open. This is supporting research, not a proof or disproof of Erdős #1191 Q1, and these new statements are not Lean verified.

## 1. Literal actual-history matrices

Let `P={a_1<...<a_p}` be Sidon with repeated summands included in the Sidon condition. Set `F=ΔP`, `q=binom(p,2)`, and let `τ(a_j−a_i)=j` for `i<j`. Actual positive-difference injectivity makes this a function. The diagonal of each matrix below is zero. For distinct `d,e∈F`, define

```
A_de = 1[|e−d|∈F],
B_de = A_de 1[τ(|e−d|)≤max(τ(d),τ(e))],
Rret_de = A_de−B_de.
```

Thus `B` retains relations whose output label is already dead (born) when both input labels become available. A retired relation has output born strictly after both inputs. For a symmetric matrix `W` write `T_A(W)=tr(AW)/2`, and similarly for `B` and `Rret`.

For `d<e`, write `t=e−d`. The involution `(d,e)↦(t,e)` pairs a retired edge with a born-dead edge. Indeed, retirement gives `τ(t)>max(τ(d),τ(e))`, whereas the paired edge has output `d` and an input `t`, so it is born-dead. An edge with `d=t` cannot be retired. Consequently `|E(B)|≥|E(A)|/2`. This controls unit weights, not centered quadratic forms: the paired weights are `W_de` and `W_te`, which can differ or have opposite signs for a PSD residual.

The upper-endpoint cliques are genuine born-dead cliques. Their degree/eigenvalue scale is only `O(p)`, so these cliques alone do not give the desired cap-sensitive `Ω(p²/log p)` eigenvalue or beat a future block's diagonal cost of order `p`.

## 2. Historical cost and the distinction between two improvements

For fixed entrywise-nonnegative `W` on terminal `F`, restrict it to `F_n=Δ{a_1,...,a_n}` without recentering. Put

```
K_n(t)=Σ_{d<e in F_n, e−d=t} W_de,
C_hist(W)=Σ_{t≥1} max_n 1[t∉F_n] K_n(t).
```

Since every summand is nonnegative, `K_n(t)` increases until the output label is born. Hence the literal historical identity is

```
C_hist(W) = (M(W)−S(W))/2 − T_B(W),
M(W)=1ᵀW1,    S(W)=tr W.
```

This includes output labels outside terminal `F`, which never die. The terminal cost is `C_term(W)=(M−S)/2−T_A(W)`; therefore `C_hist−C_term=T_Rret(W)`.

Let `R⪰0`, `R1=0`, `W=J+λR`, and choose `λ>0` such that `W` is entrywise nonnegative. Let a compatible future block have `m` points in an interval of length `L`, and let `H=diam P`, `D=L+H−m>0`. The raw interval demand is

```
δ(W)=(m² M(W)/D−m S(W))/2.
```

Use “improvement” for the reduction of a cost, or of cost minus demand, relative to `J`. Since `M(W)=q²`, the four exact quantities are

```
C_term(J)−C_term(W) = λ(S(R)+tr(AR))/2,
C_hist(J)−C_hist(W) = λ(S(R)+tr(BR))/2,
δ(J)−δ(W)         = λ m S(R)/2,
[C_hist(J)−δ(J)]−[C_hist(W)−δ(W)]
                     = λ[tr(BR)−(m−1)S(R)]/2.
```

In particular, a spectral upper bound `B|1⊥<(m−1)I` prohibits historical **cost-minus-demand gap improvement** for every nonzero centered PSD residual. It does not prohibit a reduction in historical cost alone.

## 3. Exact p=16 capped-prefix obstruction

Take the following 32 positive points:

```
1, 3, 4, 12, 25, 29, 44, 71, 89, 123, 167, 197, 204, 259, 273, 279,
362, 410, 420, 483, 519, 700, 705, 800, 854, 887, 971, 1032,
1259, 1297, 1421, 1518.
```

The exact checker verifies all unordered sums, including repeats, are distinct; it independently verifies positive-difference injectivity. The last 16 points are reproduced by starting after the first 16 and repeatedly adjoining the smallest larger integer whose new positive differences avoid all previous differences. The initial 16 points and integer witness are fixed input data; their discovery is not claimed to be an exhaustive search.

For every `2≤n≤32`, the checker verifies `a_n≤2n²` with integers. Thus this finite history satisfies `a_n≤2n² log(2n)` with fixed `C=2`, `n_0=2`. This is not an infinite capped history and is not an asymptotic counterexample.

For the first 16 points, `q=120`, `H=278`, `|E(A)|=3669`, and `|E(B)|=3149`. Let `E` be the `120×119` matrix with columns `e_i−e_120`. The exact checker constructs

```
Dcert=Eᵀ(15I−B)E.
```

All 119 leading principal minors are positive. They are computed by fraction-free Bareiss elimination, checking that every division has zero remainder. Sylvester's criterion gives `Dcert≻0`; as `E` spans `1⊥`, this proves the strict uniform bound

```
xᵀBx < 15 ||x||²    for every nonzero x with Σx=0.
```

The log records all minors and the certificate matrix's canonical JSON SHA-256. This is an exact positivity certificate, not a floating-point eigensolver acceptance.

The checker and log also give an explicit integer vector `z` in increasing-label order, with

```
Σz=0,  ||z||²=918,
zᵀAz=13894 > 13770=15||z||²,
zᵀBz=12568 < 13770.
```

Thus `λmax(A|1⊥)≥6947/459>15`, whereas `λmax(B|1⊥)<15`. The correction `W=J+zzᵀ/25` is PSD and strictly entrywise positive, has `M=14400` and `S=3918/25`, and is admissible in the same actual Sidon history.

The future 16 points have `L=1157`, so `D=1419`. The interval demand and actual expenditure are positive and satisfy the exact inequality:

```
δ(J) = 160320/473,
δ(W) = 534288/11825 > 0,
Ψ_future(W) = 25268/25 ≥ δ(W).
```

The gains are:

| Quantity reduced relative to J | Exact reduction |
|---|---:|
| Terminal cost alone | `7406/25` |
| Historical cost alone | `6743/25` |
| Raw future demand | `7344/25` |
| Terminal cost-minus-demand gap | `62/25` |
| Historical cost-minus-demand gap | `−601/25` |

The residual improves the terminal gap but worsens the historical gap. Moreover, the spectral certificate shows that **reoptimizing over every nonzero centered PSD residual cannot improve this historical gap at m=16**: decompose the residual into rank-one centered vectors and apply the strict quadratic bound to each. This stronger finite obstruction is not confined to the displayed witness or to Fourier carriers.

The same example can be scaled into the normalized cone used by the Fourier construction. Set `R'=zzᵀ/8` and `W'=J+R'/8=J+zzᵀ/64`. Then `tr R'=459/4≤120`, the scalar feature has magnitude at most `5/√8<2`, and every entry lies in `[11/16,89/64]⊂[1/2,3/2]`. Linear rescaling of the exact identities gives terminal gap improvement `31/32`, historical gap improvement `−601/64`, and corrected positive demand `424173/1892`. This is a normalized centered-PSD obstruction; it is not a claim that the displayed feature is a birth-centered Fourier feature.

The result does not refute a sufficiently small universal asymptotic lower constant, does not refute `Ω(p²/log p)` as `p→∞`, and does not contradict the terminal Fourier theorem in [centered_spectral_gain.md](centered_spectral_gain.md). It disproves an unqualified finite transfer above the actual future diagonal threshold.

## 4. Causal energy identity, with every signed term retained

Fix any complex terminal label coefficients `z_d`; they need not be centered for the following identity. Write `G_n=F_n\F_(n−1)` and

```
f_n=1_Pn*z_Fn,
h_n=δ_(a_n)*z_F(n−1),
g_n=1_Pn*z_Gn,
I_n=||g_n||²+2 Re⟨f_(n−1)+h_n,g_n⟩,
Ret_n=Re⟨f_(n−1),h_n⟩.
```

The literal decomposition `f_n=f_(n−1)+h_n+g_n` yields

```
||f_n||²−||f_(n−1)||² = S(F_(n−1))+2 Ret_n+I_n.
```

The difference uniqueness of the actual points implies `Σ Ret_n=T_Rret(Re zz*)`; terminal convolution gives `||f_p||²=p S(F)+2T_A(Re zz*)`. Also

```
Σ_n S(F_(n−1))−pS(F)=−Σ_n n S(G_n).
```

Combining these identities gives

```
2 T_B(Re zz*) = Σ_n [I_n−n S(G_n)].
```

This is an exact reformulation of the difficulty, not a positivity assertion. The `I_n` contain signed cross terms, and the new-label diagonal subtraction is mandatory. The exact witness above verifies every intermediate energy identity and the final identity; already at ranks 11 and 12 it has `I_n−nS(G_n)=−86,−122`. Retired quadratic contributions are negative at ranks 14 and 15 (`−24,−86`). PSD of the residual alone does not assign the desired sign to these pieces.

## 5. Exact self-energy for a new birth class

The actual Sidon condition simplifies `||g_n||²` further. Write `w_i=z_(a_n−a_i)` for `i<n`. In the convolution `g_n`, the terms indexed by `(k,i)` land at `a_n+(a_k−a_i)`, where `k≤n`. For `k=i`, all terms land at `a_n` and sum to `Σ_i w_i`. For `k≠i`, all locations are distinct: equality of positive or negative differences follows from actual difference injectivity, and the two signs cannot collide. Each fixed `i` occurs at `n−1` such nonzero locations. Therefore, exactly,

```
||g_n||² = (n−1) S(G_n) + |Σ_(d∈G_n) z_d|².
```

For coefficients centered in each birth class, the last square vanishes and

```
I_n−n S(G_n)
  = −S(G_n)+2 Re⟨1_Pn*z_F(n−1), 1_Pn*z_Gn⟩.
```

Thus the positive self-energy of a new birth class cannot be counted as a new large source after paying its required diagonal. The desired centered born-dead gain must come from the new/old cross term. This identity is valid for arbitrary complex coefficients and all ranks, rather than only for the example above.

The candidate `z_(a_j−a_i)=exp(iθ(a_j−a_i))−exp(iθa_j)conj(P̂_(j−1)(θ))/(j−1)` is indeed centered in every birth class. At matching frequency, each cohort Fourier sum is the nonnegative point variance, and this gives a strong terminal convolution estimate. It does not determine the integral sign of the new/old cross term at other frequencies. In particular, the nonnegative matching-frequency contribution is not a license to discard signed contributions elsewhere.

There is also an all-rank obstruction to removing the difficult cross terms by making the residual block diagonal across birth classes. Suppose `R⪰0`, each class block is centered, and `R_de=0` for labels from different classes. Each `G_j` is a clique in both `A` and `B`, since

```
(a_j−a_i)−(a_j−a_k)=a_k−a_i
```

is an older difference. Within a centered block the sum of all matrix entries vanishes, so its off-diagonal sum is minus its trace. Consequently, exactly,

```
tr(AR)=tr(BR)=−S(R).
```

Both terminal and historical cost-alone improvements are then zero, and their cost-minus-demand improvements equal `−λm S(R)/2`. Thus a block-diagonal PSD repair destroys every improvement for every rank and every nonzero such residual. This is a proved obstruction for that repair, not a proof that all birth-centered residuals fail: the successful terminal carrier retains inter-class correlations.

## 6. Reproduction and scope

Run from any directory:

```
/opt/homebrew/opt/python@3.14/bin/python3.14 /Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/research/evidence/born_dead_spectral_exact_checks.py
```

The stdlib-only checker uses exact integers and `fractions.Fraction`; no numerical eigensolver is imported. Source, complete JSON log, and invocation metadata are respectively [the checker](evidence/born_dead_spectral_exact_checks.py), [the exact log](evidence/born_dead_spectral_exact_checks.log), and [the run record](evidence/born_dead_spectral_exact_checks.run.json). The recorded run exited 0 with `EXACT_PSD_CERTIFICATE_PASS_Q1_UNRESOLVED`.

- Checker SHA-256: `4646ba4d7e5ba22079f142a6e3f9274b554d205c26081749cf61c84020e96678`.
- Log SHA-256: `240b9ed2368de74b6ffa8e2326fc9b2674ba14ad055f91f2bf0646bcabc9936d`.
- Certificate matrix SHA-256: `91b9271abf2d13a01f22525f01fba192a4134804a47b20eaa262dd17224c8cb9`.

The remaining research obligation is an all-rank, actual-geometry spectral estimate or an asymptotic actual Sidon family showing it fails. Neither the edge-count injection nor this finite certificate settles that obligation.
