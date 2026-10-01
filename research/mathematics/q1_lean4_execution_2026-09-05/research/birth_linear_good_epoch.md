# A coherent birth-linear carrier at a good dyadic epoch

Date: 2026-09-05. Author: `/root/lean_target`, GPT-6 Astra Ultra.

Status: a proved finite mathematical supporting theorem. Under the two stated diameter conditions, the carrier below gives a normalized terminal row improvement of order `1/log N` under the critical cap. Its coefficients before normalization are unchanged under extension of the actual Sidon history. No claim about the frequency of good epochs, no repeated spending of a historical physical budget, and no Q1 proof is made here. This note introduces no Lean declaration or numerical experiment.

## 1. Exact hypotheses and notation

Let `p≥2` be even, `N=2p`, and let

```
P_N={a_1<a_2<...<a_N}
```

be an actual integer Sidon set, with repeated summands included in its Sidon property. Write `P_n={a_1,...,a_n}`, `H_n=a_n−a_1`, `H=H_N`, and assume

```
H_p ≥ 2H_(p/2),             H ≤ 8H_p.                (1)
```

In particular `H` is a positive integer. Let `F=ΔP_N` and `q=|F|=N(N−1)/2`. For the unique positive label `d=a_j−a_i`, `i<j`, set

```
bar_a_(j−1)=(1/(j−1))Σ_(k<j) a_k,
g_d=bar_a_(j−1)−a_i,
z_d=g_d/H,
V_j=Σ_(i<j)(a_i−bar_a_(j−1))²,
S=Σ_(d∈F) z_d²,
μ_1=Σ_(d∈F) d z_d.                                  (2)
```

The sign in (2) is intentional. The symbol `μ_1` always denotes the first label moment; `bar_a_n` denotes a prefix mean.

Actual positive-difference injectivity makes these literal functions on physical labels. The unnormalized coefficient `g_d` depends only on the points present when `d` is born. Extending the history does not change it. At different terminal ranks, the vectors `z` differ on their common bank only by the scalar normalization `1/H`.

For every actual birth class `G_j={a_j−a_i:i<j}`, and hence every prefix restriction, we have

```
Σ_(d∈G_j)z_d=0,
Σ_(d∈ΔP_n)z_d=0,
|z_d|≤1,
S=(1/H²)Σ_(j=2..N)V_j≤q.                             (3)
```

The coordinate bound follows because each prefix mean and every old point lie in `[a_1,a_N]`. A stronger upper bound is unnecessary below.

## 2. The two diameter conditions force S≥q/8192

For every `j=3p/2+1,...,2p`, the old prefix `P_(j−1)` contains both index sets

```
I={1,...,p/2},              K={p+1,...,3p/2}.
```

Each set has exactly `p/2` members. The first condition in (1) implies, for `i∈I`,

```
a_i≤a_1+H_(p/2)≤a_1+H_p/2.
```

For `k∈K` we have `a_k≥a_p=a_1+H_p`. Thus every such cross gap is at least `H_p/2`. These inequalities use coordinates relative to `a_1`; an assertion `a_i≤a_p/2` without that translation would be incorrect in general.

The elementary pairwise formula for variance is

```
V_j=(1/(j−1))Σ_(i<k<j)(a_k−a_i)².
```

Keeping only the `(p/2)²` cross pairs and using `j−1≤2p` gives

```
V_j ≥ (1/(2p))·(p²/4)·(H_p²/4)=pH_p²/32.
```

There are exactly `p/2` selected stages. All other `V_j` are nonnegative, so

```
Σ_(j=2..N)V_j ≥ p²H_p²/64
                ≥ p²H²/4096
                ≥ qH²/8192.                         (4)
```

The last two inequalities use `H≤8H_p` and `q=p(2p−1)≤2p²`, respectively. Put

```
η=1/8192=2^-13.
```

Equations (3)–(4) prove

```
ηq≤S≤q.                                             (5)
```

For each class, the first moment has a particularly useful exact identity:

```
Σ_(i<j)(a_j−a_i)(bar_a_(j−1)−a_i)=V_j.
```

Indeed, the coefficient sum multiplying `a_j` is zero, and subtracting the remaining product yields exactly the variance. Consequently

```
μ_1=(1/H)Σ_j V_j = H S ≥ ηqH.                        (6)
```

## 3. A direct integer first-moment proof of the energy lower bound

Extend `z` by zero off `F`, and define the actual convolution

```
f(x)=Σ_(a∈P_N) z_(x−a),              E=Σ_(x∈Z)f(x)².
```

Because `F⊆{1,...,H}`, its support is contained in the **2H integer positions**

```
a_1+1,...,a_1+2H.
```

By (3) and (6), the two exact moment identities are

```
Σ_x f(x)=0,
Σ_x x f(x)=Nμ_1=NHS.                                (7)
```

Use the midpoint `c=a_1+H+1/2`. The zero total allows `x` in the second identity to be replaced by `x−c`. Cauchy and the exact centered square sum give

```
(NHS)²
 ≤ E Σ_(k=1..2H)(k−H−1/2)²
 = E·H(4H²−1)/6.
```

Therefore, already without the good-epoch assumptions,

```
E ≥ 6N²H S²/(4H²−1) ≥ (3/2)N²S²/H.                 (8)
```

Under (1), (5) yields the main energy estimate

```
                  E ≥ (3/2)η² N²q²/H.               (9)
```

The support length, mean subtraction, and exact diagonal cost are retained. This short first-moment proof gives stronger constants than the Fourier estimates below.

## 4. Verification of the proposed Taylor–Parseval argument

Define

```
Z(ξ)=Σ_(d∈F)z_d exp(i dξ),
P̂_N(ξ)=Σ_(a∈P_N)exp(i aξ).
```

The coefficients are real. Equations (3) and (6) imply `Z(0)=0` and `Z'(0)=iμ_1`. The elementary exponential remainder bound gives, for every real `ξ`,

```
|Z(ξ)−iμ_1ξ| ≤ (ξ²/2)Σ_d |z_d|d² ≤ qH²ξ²/2.        (10)
```

For `η/(2H)≤ξ≤η/H`, the last expression is at most `μ_1ξ/2`. Thus

```
|Z(ξ)|≥μ_1ξ/2≥η²q/4.                               (11)
```

The same magnitude bound holds on the reflected negative interval. Rephase the point exponential sum at `(a_1+a_N)/2`. For `|ξ|≤1/H`, every relative phase has magnitude at most `1/2`, so

```
|P̂_N(ξ)|≥N cos(1/2)≥7N/8≥N/2.                     (12)
```

The two intervals in (11) have total length `η/H` and lie inside `[-π,π]` because `H≥1` and `η≤1`. Parseval therefore gives the requested independent chain

```
E=(1/(2π))∫_(-π)^π |P̂_N(ξ)|² |Z(ξ)|² dξ
 ≥ η^5 N²q²/(128πH)=N²q²/(2^72πH).                  (13)
```

No contribution of a signed energy increment is inferred from this nonnegative total-energy integral.

## 5. The linear sign permits a stronger Fourier window

There is a useful exact refinement of (10), specific to the coefficients in (2). For a fixed class with `n=j−1`, pair covariance gives

```
Z_j(ξ)
 = (1/(nH))Σ_(i<k<j)(a_k−a_i)
       [exp(iξ(a_j−a_i))−exp(iξ(a_j−a_k))]
 = (iξ/(nH))Σ_(i<k<j)(a_k−a_i)²
       ∫_0^1 exp(iξ[a_j−a_k+t(a_k−a_i)])dt.           (14)
```

All weights after `iξ` are nonnegative, and every phase location in square brackets lies in `[0,H]`. For `1/(2H)≤ξ≤1/H`, taking imaginary parts and using `cos x≥1−x²/2≥1/2` for `0≤x≤1` yields

```
Im Z_j(ξ) ≥ ξ V_j/(2H),
|Z(ξ)|≥Im Z(ξ)≥ξμ_1/2≥μ_1/(4H)=S/4≥ηq/4.          (15)
```

There is no cancellation between the class contributions in this imaginary part. Together with the reflected interval and (12), whose total length is now `1/H`, this gives

```
E ≥ η²N²q²/(128πH)=N²q²/(2^33πH).                   (16)
```

Equivalently, for `ξ≠0` and with continuous extension `μ_1` at zero, `Z(ξ)/(iξ)` is the Fourier transform of a positive finite measure supported in `[0,H]`, with total mass `μ_1`. Formula (14) supplies that measure explicitly as a sum of positive interval measures. This observation strengthens the proposed Fourier proof; the direct integer estimate (9) is stronger still.

## 6. Normalized nonnegative PSD carrier and the exact row comparison

Set

```
R=zzᵀ,                  W=J+R/8.
```

Then `R` is centered in every birth class, is PSD of rank one, and has trace `S≤q`. The matrix `W` is PSD, every entry lies in `[7/8,9/8]`, and

```
M(W)=1ᵀW1=q²,
tr W=q+S/8≤9q/8.                                   (17)
```

All prefix restrictions retain their zero sums and hence their exact squared masses. The two nonnegative rank-one decomposition is

```
W=(1/2)[(1+z/√8)(1+z/√8)ᵀ+(1−z/√8)(1−z/√8)ᵀ].     (18)
```

Both scalar vectors are positive. On every prefix they have the same mass and trace as the corresponding restriction of `W`, because the restricted coefficient sum is zero.

Let `A_de=1[d≠e, |d−e|∈F]` be the actual old-label adjacency matrix. Sidon difference injectivity gives the exact convolution expansion

```
E=NS+zᵀAz.                                         (19)
```

For any compatible actual future block of `m≥1` points and positive interval denominator `D_B=L+H−m`, use the raw demand

```
δ(X)=(m²M(X)/D_B−m tr X)/2
```

and terminal available capacity

```
C_term(X)=(M(X)−tr X)/2−tr(AX)/2.
```

Define the improvement as the reduction of capacity minus raw demand relative to `J`. Direct substitution of (17) and (19) gives, retaining all diagonal terms,

```
I_m=[C_term(J)−δ(J)]−[C_term(W)−δ(W)]
   =[E−(N+m−1)S]/16.                               (20)
```

The interval denominator cancels in this comparison because both masses equal `q²`. It is not silently set to a favorable value. If positive-part demands are used, one additionally applies the relevant positivity statement for that actual future block; (20) itself is the raw-demand identity.

Suppose now `H≤K N² log(2N)` with fixed `K>0`, and `1≤m≤R_0N` with fixed `R_0>0`. Combining (5), (9), and (20) proves the uniform bound

```
       I_m       3                         R_0+1
       ─── ≥ ───────────────────── − ─────────────────.      (21)
        q²    2^31 K log(2N)              8(N−1)
```

In particular it is positive whenever

```
(N−1)/log(2N) > 2^28 K(R_0+1)/3,                    (22)
```

and hence eventually, uniformly for all such `m`. This is the desired `Ω(1/log N)` normalized row scale on good epochs.

If a scalar nonnegative carrier is wanted, choose the better of the two vectors in (18) at this terminal prefix. Their raw demands and traces coincide for every future block, and their difference in capacity depends only on the old history. Thus the same sign gives at least the matrix improvement (21) for every `m` and every positive interval denominator at this fixed old prefix. This is not an assertion that one sign is simultaneously optimal at all earlier prefixes.

## 7. Transport boundary

The carrier eliminates phase selection and preserves its unnormalized coefficients under extension. These are compatibility properties of the construction. The bounds above concern total convolution energy and an individual terminal row.

They do not bound the signed retirement correction in the historical envelope, show that good epochs have a divergent harmonic sum, or authorize summing separate row gains against the same physical source budget. The positive measure in (14) is a Fourier representation of the coefficient vector, not a proof that every historical energy increment is nonnegative.

The remaining transport and epoch-occurrence arguments are separate obligations. Q1 remains unresolved.

Independent mathematical review: `/root/global_route` read the complete note and separately rederived the variance lower bound, both exact moments, the integer support and square sum, both Fourier chains, the final constants and positivity threshold, and the simultaneous scalar-sign selection. No mathematical correction was requested. This is a semantic review, not Lean or numerical verification.
