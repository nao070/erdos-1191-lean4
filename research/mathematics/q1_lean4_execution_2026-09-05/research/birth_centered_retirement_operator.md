# Birth-centered retirement: matching blocks and a dense actual-family obstruction

Date: 2026-09-05. Author: `/root/lean_target`, GPT-6 Astra Ultra.

**Proved:** there is an explicit infinite family of finite positive integer Sidon sets `P`, with `N=|P|→∞` and `diam P≤41N²`, for which the actual birth-class projection satisfies

```
λmax(C Rret C) ≥ N²/2^37.
```

Thus a bound `||C Rret C||=O(N^(3/2) (log N)^k)` for all finite Sidon sets, for any fixed `k`, is false even at this terminal density. This is an analytic construction, not a numerical eigenvalue extrapolation. The family does **not** satisfy one fixed-onset critical cap at every initial rank. It does not disprove Q1, a bound restricted to such all-prefix histories, or a favorable correction bound for the particular Fourier carrier constructed in the parent note. Nothing in this note is asserted to be Lean verified.

## 1. Literal operators and an equal-three-sum matching decomposition

Let `P={a_1<...<a_N}` be Sidon, with repeated summands included. For the unique positive difference `d=a_j−a_i`, write `τ(d)=j` and `G_j={a_j−a_i:i<j}`. On `F=ΔP`, define the symmetric zero-diagonal retirement matrix by

```
Rret_de = 1[|d−e|∈F and τ(|d−e|)>max(τ(d),τ(e))],
C = direct_sum_(j=2..N) (I_(j−1)−J_(j−1)/(j−1)).
```

`C` is the orthogonal projection onto vectors with zero sum on every actual endpoint-birth class. These are actual integer differences; no birth marks are assigned independently.

For `j,l<n`, let the `(j−1)×(l−1)` matrix `M_(j,l;n)` have entry 1 at `(i,k)` exactly when some `r<n` satisfies

```
(a_l−a_k)−(a_j−a_i)=a_n−a_r>0.
```

Equivalently,

```
a_i+a_r=a_j+a_k+a_n−a_l.                 (1)
```

The difference uniqueness gives at most one `r` for a fixed entry. More strongly:

- Fix `i`. In (1), `a_r−a_k=a_j+a_n−a_l−a_i>0`, since `n>l` and `j>i`. Positive-difference injectivity gives at most one pair `(k,r)`. Every row of `M_(j,l;n)` has at most one 1.
- Fix `k`. Equation (1) prescribes the sum `a_i+a_r`. Sum uniqueness, including repeats, gives at most two ordered pairs `(i,r)`. Every column has at most two 1s.

Consequently `||M_(j,l;n)||≤sqrt(2)` by the row/column Schur bound. Its positive-orientation entries are disjoint as `n` varies, because the output difference has unique endpoints. The literal off-diagonal block of `Rret` is

```
(Rret)_(G_j,G_l)
 = Σ_(n>max(j,l)) [M_(j,l;n)+M_(l,j;n)^T].       (2)
```

For `j=l` this block vanishes: the difference between two labels in `G_j` is already born before `j`.

This is a genuine matching decomposition with bounded norms for its individual pieces. Summing it only gives an order `N²` upper bound. There is no automatic square-root saving when adding the different future endpoint matchings. The construction below proves that such a saving cannot hold in general, even after applying `C` on both sides.

For reference the elementary all-rank upper bound is `||C Rret C||≤||Rret||≤N(N−1)`: each possible positive output difference contributes at most two neighbors to a row, and there are `binom(N,2)` such differences. The obstruction below has the same order, with a deliberately conservative constant.

## 2. A three-cluster lemma retaining the exact retired outputs

Let `P=L∪U∪V` be an actual Sidon set, with every point of `L` less than every point of `U`, and every point of `U` less than every point of `V`. Write

```
ℓ=|L|,  u=|U|,  v=|V|,
h_src=diam L+diam U,
D=diam L+diam U+diam V,
μ=(Σ_(x∈L) x)/ℓ,
V_L=Σ_(x∈L)(x−μ)².
```

Assume the literal separation inequalities

```
min U−max L > h_src,
min V−max U > h_src.                         (3)
```

Define a coefficient vector on the entire `ΔP` by

```
z_(b−x)=x−μ  for b∈U, x∈L,
z_d=0       for every other label.
```

This is well-defined by actual Sidon difference uniqueness. Every birth class with upper endpoint in `U` sums to `Σ_(x∈L)(x−μ)=0`; earlier and later classes have only zero coefficients. Therefore `Cz=z`, and

```
S=||z||²=u V_L,
Σ_d z_d=0,
Σ_d d z_d=−u V_L=−S.                         (4)
```

All differences between two supported labels have magnitude at most `h_src`. By (3) none of these output labels joins two different point clusters. An output in `ΔL` is already born; one in `ΔV` is always born after both supported input labels; an output in `ΔU` may or may not be retired. Hence on the support of `z` the actual retirement matrix is **exactly**

```
Rret = A_V + R_U,
(A_V)_de=1[|d−e|∈ΔV],
(R_U)_de=1[the output is in ΔU and is actually retired].
```

No edge from the last term is discarded on sign grounds. Its maximum degree is at most `2|ΔU|=u(u−1)`, so

```
zᵀR_U z ≥ −u(u−1)S.                         (5)
```

The actual convolution `f=1_V*z` has the exact energy expansion

```
||f||²=vS+zᵀA_V z.                           (6)
```

Its coefficients sum to zero. By (4), its first moment is `−vS`. Its support lies in an integer interval of width `D`; if `c` is the midpoint of that interval, Cauchy gives

```
(vS)² ≤ ||f||² Σ_(k=0..D)(k−D/2)²
       = ||f||² D(D+1)(D+2)/12.
```

Thus, whenever `V_L>0`, combining all terms proves the finite inequality

```
       zᵀRret z       12v²u V_L
       ───────── ≥ ─────────────── − v − u(u−1).       (7)
          S         D(D+1)(D+2)
```

This retains the actual source incidence, birth order, the entire possible `ΔU` correction, and every diagonal term. The large positive contribution comes from differences inside a later real point cluster, not from arbitrarily deleting edges of an old adjacency matrix.

## 3. An explicit integer Sidon family, with a proof of Sidonicity

Let `r` be any odd prime and, for `0≤i<r`, set

```
b_i=2ri+ρ_i,   ρ_i=i² mod r ∈{0,...,r−1}.             (8)
```

This is the elementary quadratic-residue integer construction often called the Erdős–Turán construction. Its properties needed here are proved directly, so no external asymptotic distribution theorem is used.

If `b_i+b_j=b_k+b_l`, then

```
2r(i+j−k−l)=ρ_k+ρ_l−ρ_i−ρ_j.
```

The right side has absolute value less than `2r`, hence `i+j=k+l` and the residue sums agree. Modulo the odd prime `r`, the sum and sum of squares therefore determine the product, so `ij≡kl (mod r)`. The unordered roots of the corresponding quadratic over the field are equal. All four indices lie in `[0,r−1]`, giving `{i,j}={k,l}` as multisets. This includes repeated summands. Thus (8), and every subset of it, is Sidon.

We also have

```
b_(i+1)−b_i ≥ r+1,
diam{b_i,...,b_(i+t−1)} < 2rt.                        (9)
```

In particular the order of the points is exactly the index order, without any sorting ambiguity.

Assume now `r≥2^34`, and put

```
ℓ=floor(r/8),       u=floor(r/2^18),       v=ℓ,
L={b_i:0≤i<ℓ},
U={b_i:3ℓ≤i<3ℓ+u},
V={b_i:6ℓ≤i<7ℓ}.
```

Translate all selected points by 1 to make them positive; this changes no difference, variance, or operator. The index ranges are disjoint and lie below `r`, and `u≤ℓ`. From (9), `h_src<2r(ℓ+u)`. On the other hand,

```
min U−max L ≥ 4rℓ+r+1 > h_src,
min V−max U ≥ 6rℓ−2ru+r+1 > h_src.
```

Therefore (3) holds literally.

## 4. Quantitative Ω(N²) lower bound

For `ℓ` points with consecutive gaps at least `r`, the pairwise-difference formula for variance gives

```
V_L=(1/ℓ)Σ_(i<j)(b_j−b_i)²
    ≥r² ℓ(ℓ²−1)/12
    ≥r² ℓ³/24.                                      (10)
```

Our parameter range has `ℓ≥r/9`, `u≥r/2^19`, and `u≤r/2^18`. Also, by (9),

```
D<2r(2ℓ+u)≤(1/2+2^-17)r²,
D+2≤(2/3)r².
```

Substitution into the positive term of (7) yields, with all constants explicit,

```
  12v²u V_L        12(r²/81)u(r^5/(24·729))
 ──────────── ≥ ────────────────────────────
 D(D+1)(D+2)            (2r²/3)^3
              = ur/34992 ≥ ur/2^16.                  (11)
```

Thus (7), `v=ℓ≤r/8`, and `u(u−1)≤u²≤ur/2^18` give

```
zᵀRret z/S ≥ 3ur/2^18−r/8
             ≥ ur/2^17−r/8
             ≥ r²/2^36−r/8
             ≥ r²/2^37,                             (12)
```

where the last inequality uses `r≥2^34`. Because `Cz=z`, this is a Rayleigh lower bound for `C Rret C`.

Finally let `N=|P|=2ℓ+u`. Then `N≤r`, `N≥2r/9`, and `diam P<2r²≤(81/2)N²<41N²`. Equations (11)–(12) prove

```
λmax(C Rret C) ≥ r²/2^37 ≥ N²/2^37,
diam P ≤ 41N².                                     (13)
```

There are arbitrarily large odd primes, so this gives an infinite family. For any fixed exponent `k`, the ratio of (13) to `N^(3/2)(log N)^k` tends to infinity along this family. The proposed general operator upper bound is therefore false. The constants and prime threshold are chosen for a short proof rather than optimized.

One can divide `z` by `diam L` to put every coefficient in `[-1,1]`. This preserves the Rayleigh quotient and the birth-class centering. For the normalized vector `w`, the residual `wwᵀ` has trace at most `uℓ≤|ΔP|`, and `W=J+wwᵀ/8` has entries in `[7/8,9/8]`, mass `|ΔP|²`, and trace at most `9|ΔP|/8`. Every literal prefix restriction remains centered. The obstruction therefore lies within the bounded normalized PSD cone already under consideration; it is not merely an example with unbounded feature coordinates. It need not coincide with the particular phase chosen by the birth-centered Fourier theorem.

## 5. What this does and does not close

The bounded matching factorization in (2) is correct, but contributions from the future endpoint matchings can add coherently after birth-class centering. In this family, actual `ΔV` outputs supply precisely such coherent positive retirement energy. A general all-Sidon cancellation estimate cannot remove it.

The family meets a strong **terminal** density bound and hence the critical cap at its terminal rank. It does not meet a single fixed-onset cap at all smaller ranks: its first cluster starts with the index-spaced construction (8), so at any fixed initial rank beyond 1 the point size grows with the prime. Neither translation by 1 nor the birth-class projection changes this fact. No infinite fixed-onset capped Sidon history is constructed.

The exact historical gap equals the terminal gap minus the signed retirement correction. A large positive retirement direction therefore rules out the proposed universal small-operator route. It does not, by itself, show that the born-dead matrix has small centered positive spectrum, that all admissible carriers fail, or that the parent birth-centered Fourier carrier must choose this direction. These are separate questions.

The original Q1 and the all-prefix transport problem remain unresolved.

## 6. Exact verification and reproduction scope

The analytic proof in Sections 2–4 applies to every prime above its stated threshold. It does not rely on computing such a prime or its difference matrix. The dedicated [exact checker](evidence/birth_retirement_operator_exact_checks.py) instead does two bounded, reproducible checks:

1. It verifies every rational constant and threshold inequality used in (10)–(13).
2. On two fixed small instances of the same elementary construction, with primes `101` and `1031`, it verifies actual sum/difference uniqueness, birth-class centering, every supported retired edge, the exact `ΔV + ΔU` decomposition, the retained `ΔU` bound, convolution energy, and the first-moment inequality. On the first fixture it also verifies the complete matching factorization (2), with every edge accounted for exactly once, row degree at most 1, and column degree at most 2.

These small fixtures check identities; their Rayleigh quotients are not used to infer the large-prime theorem. No numerical eigensolver or floating-point arithmetic occurs in the checker. All 26 and 260 positive points of the respective fixtures are included in the [complete exact log](evidence/birth_retirement_operator_exact_checks.log). The [run record](evidence/birth_retirement_operator_exact_checks.run.json) identifies the interpreter, command, UTC times, before/after source hashes, log hash, and exit code 0.

```
/opt/homebrew/opt/python@3.14/bin/python3.14 /Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/research/evidence/birth_retirement_operator_exact_checks.py
```

- Checker SHA-256: `d22f86067be98bf9b4d9fdf8bf408e12bc75da81ae6036f7c1c1cfae36b54f0b`.
- Log SHA-256: `71bb170238f7ec92cc5a86c17c51be27e519f3fcb92dc81a78ab4d444a9a5d98`.
- Status: `EXACT_FACTOR_AND_MOMENT_CHECKS_PASS_ASYMPTOTIC_PROOF_IN_NOTE`.
