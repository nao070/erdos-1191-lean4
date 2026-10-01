# Independent review of the same-stage retirement injection

2026-09-05 08:18 UTC. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: no mathematical defect identified in equations (1)–(14), the endpoint injection, the partition, or the stated uniform constants. The complete source was read and all equations were independently rederived against the raw coefficient and clock definitions in `causal_birth_energy_telescoping.md`, the endpoint definitions in `retirement_shadow_review.md`, and `late_retirement_tail.md`. No numerical experiment, finite checker, or Lean command was run. Existing source files were preserved.

## Actual endpoints, clocks, and injectivity

For a retiring pair `d<e`, the unique output `e-d=a_n-a_k` gives the unique overlap `x=a_n+d=a_k+e`. Both original labels are old. Write the unique representation of `d` as `a_i-a_h`, where `h<i<n`. Then `d'=x-a_i=a_n-a_h` is actually born at `n`, whereas `e` remains old. The case `k=i` would imply `e=d'`, contradicting the disjoint old and new banks. Thus the image has distinct sources and output `|a_k-a_i|` born strictly before `n`.

The image is a mixed-born pair at the original retirement stage. Its price is therefore the same `w_n` as the original retirement price. This does not replace either price by the earlier `w_b`.

The unordered image identifies its unique newer label and that label's birth `n`. Sidon difference uniqueness determines the overlap position for its source pair. From this position one recovers the old resource points `x-d'=a_i`, `x-e=a_k`, and the original label `d=x-a_n`. These recover the entire original record. Images at different stages cannot coincide. This proves global injectivity, including the clock information.

For the fixed raw feature, `g_(d')-g_d=m_n-m_i`. Increasing actual endpoints imply `m_n>m_i`. The image-minus-source difference is exactly `(m_n-m_i)*g_e`, still signed by `g_e`; its weighted form is (2). Neither injectivity nor monotonicity of the means licenses replacing this signed expression by a nonnegative quantity.

## The convolution partition and the automatic term

Every new-star convolution location is `a_n+a_k-a_h`, with `k<=n` and `h<n`. At `k=h` all contributions meet at `a_n` and sum to zero. All other signed differences have unique ordered endpoints. The noncentral translated positions are respectively old positive differences, old negative differences, and new positive differences, so the three classes in (3) are disjoint and exhaustive. The stated pointwise coefficients follow directly. Some coefficients can themselves be zero; no nonzero coefficient is omitted by describing these location classes.

On the positive old class, the old-star coefficient is `m_i-a_h` and the new-star coefficient is `m_n-a_h`. Hence

```
<h_n,k_n>
  = sum_(2<=i<n) sum_(h<i) [(m_i-a_h)^2
                           +(m_n-m_i)*(m_i-a_h)]
  = sum_(2<=i<n) v_i
  = S_(n-1).
```

Each cross inner product counts one overlap of an unordered mixed pair; there is no additional factor two. The factor two belongs to the expansion of a squared convolution norm, not to `x_n` or `rho_n` separately.

For completeness, every term of `f_(n-1)(a_n+d)` has an old resource `a_k` and old label `e=a_n+d-a_k>d`. It therefore represents an actual retirement of `{d,e}` at `n`. Replacing its high resource as above gives its injection image. Conversely every original retirement appears this way. Thus the positive-location part of `<f_(n-1),k_n>` minus `<f_(n-1),h_n>` is exactly `A_n^inj`.

The remaining parts of `<f_(n-1),k_n>` are the negative positions `a_n-d` and the fixed positions `2a_n-a_h`. They are exactly `U_n` and `F_n^fix`. The additional `<h_n,k_n>` contributes `S_(n-1)`. This proves (5) with every mixed-born pair accounted for once. In particular, the positive old-location injection images have both resources old, while the automatic contribution has the high resource `a_n`; these are distinct pair records. The fixed and negative locations belong to disjoint classes and supply no duplicate pair capacity.

## Uniform counts and all constants

From `S_(n-1)<=q_(n-1)*H_n^2`,

```
w_n*S_(n-1) <= q_(n-1)/q_n^2
             = 2*(n-2)/(n^2*(n-1))
             = 4/n^2-2/[n*(n-1)].
```

Summing from `n=2` gives `4*(zeta(2)-1)-2=4*zeta(2)-6<0.58`. The formula gives zero at `n=2`, consistently with the empty previous bank.

At a fixed position, `f_(n-1)` has at most `n-1` terms: each old resource point determines at most one source label. Each coefficient has absolute value at most `H_n`. The fixed expression has `n-1` distinct positions and each new coefficient is bounded by `H_n`. Hence its absolute size is at most `(n-1)^2*H_n^2`, its weighted size is at most `4/n^2`, and its full absolute sum is at most `4*(zeta(2)-1)<2.58`.

The unpaired expression has `q_(n-1)` distinct negative positions, giving instead

```
w_n*|U_n| <= (n-1)*q_(n-1)/q_n^2
           = 2*(n-2)/n^2.
```

This bound is not summable and has no sign content. The smaller count for fixed positions cannot be transferred to it. These three estimates prove (6)–(8) without any cap assumption or discarded signed diagonal.

## The far-image bound uses the original record

Same-birth source pairs have an earlier output, so every original retirement with later source birth `b` uses one label from `G_b` and one from `F_(b-1)`. There are at most `(b-1)*q_(b-1)<=b^3/2` such original pairs, and each has at most one actual retirement. No retirement is possible with `b=2`.

For its image at `r`, the unchanged `g_e` is bounded by `H_b`, the new coefficient is bounded by `H_r`, and the mean difference is between zero and `H_r`. Since `H_b<=H_r`, each of the two absolute products in (9), after multiplying by `w_r`, is at most `1/q_r^2<=16/r^4`. For `r>=b*(log b)^alpha`, counting by the original `b` gives exactly

```
8*sum_(b>=3) 1/[b*(log b)^(4alpha)] = C_alpha.
```

Convergence requires precisely the stated `alpha>1/4`. The constant bounds the far-image sum and the far signed-difference absolute sum separately. The latter uses its direct mean bound and therefore needs no factor two. There is no additional sum over possible `r`, and the statement concerns tagged injection images rather than every born pair of rank `r`. The same estimate does not apply to the earlier price `w_b` or to the lag commutator.

## Abel equations and the remaining signed functional

Summing (5) and splitting the injection difference into near and far originals gives (11). Its error is exactly the automatic sum, the signed fixed-position sum, and the far injection difference. Applying the three separate absolute estimates gives the displayed error constant.

Together with `2B_T+2R_T+D_T=A_T`, the identity `B_T-R_T=J_T+e_T` solves to

```
B_T = A_T/4+J_T/2-D_T/4+e_T/2,
R_T = A_T/4-J_T/2-D_T/4-e_T/2.
```

These signs and coefficients in (12) are correct. The retained diagonal bound is `0<=D_T<=8*zeta(2)-10`. If the unproved condition `J_T>=-(1/2-epsilon)*A_T-O(1)` held, the resulting coefficient of `A_T` in the lower bound for `B_T` would be `epsilon/2`. If `J_T` merely had a uniformly bounded negative part, the coefficient would be `1/4`. Neither condition follows from the established counting bounds.

Finally, putting `d_n=k_n-h_n` and using the independently checked automatic identity gives

```
||d_n||^2=(n-1)*v_n-S_(n-1),
x_n-rho_n=S_(n-1)+<f_(n-1),d_n>.
```

The norm is nonnegative and is bounded above by the causal diagonal charge at each stage. Expanding `||f_(n-1)+d_n||^2` proves (14), including the coefficient `3` of `S_(n-1)`. The square there uses `f_n-2h_n`, not the actual next state `f_n`; it is therefore not an energy telescoping argument. The finite weighted increment norm alone supplies no finite bound for its bilinear work against `f_(n-1)`.

The current result is an exact reduction to the joint near-injection and unpaired functional, with uniformly bounded discarded terms. Its required signed estimate and the one physical-margin obligation remain unproved. Original Q1 remains unresolved.

Reviewed target SHA-256: `517e7c38ebb8c567b5ad0aae2fe2bba801e5e302bd88f10008476821b1647c17`.

Supporting source SHA-256 values at review: `causal_birth_energy_telescoping.md` = `1194fc85cf2328e16056ad92ee065f10aa7e8a458b5844aad70fcd8b14f8cd1f`; `retirement_shadow_review.md` = `3668aa7ee835dc3df1e5877043fc98fbd229aee5bbed1267e3ad854541b515fc`; `late_retirement_tail.md` = `5dbcf37e0a7fd687a8371c5f71c04b11cab45992a622ebe31ebba15d469963ab`.
