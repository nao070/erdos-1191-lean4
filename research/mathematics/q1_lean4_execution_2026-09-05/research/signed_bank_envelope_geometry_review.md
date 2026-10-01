# Independent review of signed-bank envelope geometry

2026-09-05. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: equations (1)–(7), parity cancellation, and the stated finite demand dominance are correct. One sentence in the initial source incorrectly described every opposite-sign coefficient product as negative under the assumption of oddness alone. The parent replaced it by the exact product `-h(x)h(y)`; the formulas were already correct. This review binds the corrected source. No further mathematical correction was identified.

The full target was read and the kernels, supports, traces, and comparison independently rederived. No finite experiment, previous checker, or Lean command was run. Positive-bank causal Abel identities are not imported into the signed bank by this audit.

## Correlation conventions and the parity involution

For positive output u, a signed source pair consists of an index d with `d,d+u in Fhat`. The positive and negative same-sign parts each contribute D to the unit kernel and `D_h` to the odd-feature kernel. For an opposite-sign pair `{-x,y}`, one has `x+y=u` and product `-h(x)h(y)`. Choosing x in the ordered sum determines this physical pair uniquely. Unequal x and y give the two different pairs `{-x,y}` and `{-y,x}`; equal summands give one pair. This proves (1), including the factors two and the convention at `u/2`.

Oddness does not require h to be nonnegative on positive labels, so the signed product need not be negative. The corrected wording preserves the exact minus sign in front of `S_h` without making that extra assumption.

The map `d -> -d-u` preserves the correlation index set and negates the linear summand. Its possible fixed point has two opposite labels and a zero linear sum. This proves (2) pointwise. The same output and the same multiset of source birth ranks are preserved, as is the output birth; any literal Born or retirement mask is therefore preserved. Complete signed prefixes have zero feature sum as well. Consequently the mixed shadow inner product has zero diagonal and zero off-diagonal terms, and `<f_0,f_phi>=0` for the actual future block.

The scalar kernel differs from the pure moment kernel at the same `s=t^2` only by the canceled linear term. More generally, in the specified scalar–moment demand, replacing t by zero at fixed s preserves the physical kernel and removes the nonpositive demand term `-c*t^2`. This proves the stated optimality of t=0 for that demand, without claiming optimality among all possible scalar lower bounds.

## The sign endpoint is pointwise the positive unit kernel

For `phi=sign` one has `D_h=D` and `S_h=S`. Adding the unit kernel to the feature kernel leaves `4D`. Since `Q=2q`, its normalized kernel is exactly `D/q^2`. Both banks use the same positive-output old exclusion `u notin F` and the same actual-span mask. Equality therefore holds at each output and each prefix, and survives a maximum over any common row family. For a historical Born mask, the two same-sign copies have identical birth data, while all opposite-sign entries of the full W vanish. This gives the asserted masked identity as well.

The full W has entries two inside its two sign blocks and zero across them. Its energy is `2||f_+||^2+2||f_-||^2`. The autocorrelation kernels of F and -F agree, including the diagonal q, so the two norms agree. Thus `E_W=4||f_+||^2`, `tr W=4q`, and the matrix mass is `Q^2=4q^2`. Applying the original positive-bank Cauchy denominator and then dividing the full pair demand by `Q^2` gives exactly (4), including the diagonal `-m/(2q)`.

## Both interval conventions in the finite dominance theorem

Let the actual future block have minimum b and maximum `b+L-1`. Its signed shadow is enclosed by

```
[b-H,b+L-1+H], of inclusive length T=L+2H.
```

All m future points lie in this interval and are holes: the source bank omits zero and compatibility excludes their nonzero signed differences. The signed mass denominator is therefore `T-m`. The positive-bank interval instead has length `L+H-1` and contains exactly `m-1` such holes, giving

```
D_pos=L+H-m=T-H-m.
```

These denominators differ by H; neither is silently replaced by the other. Since the actual block has `L>=m` and `H>=1`, both are positive. Also `T>=3`, so the full signed moment denominator `T(T^2-1)` is nonzero.

The sign feature has first moment `mu=2*sum_(d in F)d=Q*A` and square sum Q. Substitution into the full signed moment demand gives exactly (5): its moment term is `6m^2*A^2/[T(T^2-1)]` and its trace term is again `-m/(2q)`.

Translate the old points so the first is zero and the last is H. Their sum of positive differences is `sum_i(2i-N-1)*a_i`. The sum of its positive coefficients is `floor(N^2/4)`, proving the displayed upper bound by replacing the corresponding coordinates by H and the negative-coefficient coordinates by zero. This bound needs no relaxation of the actual Sidon history.

For `N>=8`,

```
A/H <= floor(N^2/4)/q <= N/[2(N-1)] <= 4/7,
12*A^2 <= (192/49)*H^2 < 4H^2.
```

The remaining algebra in (6) is correct:

```
T^2-1-4H(T-H)=L^2-1>=0,
12A^2/[T(T^2-1)] <= H/[T(T-H)]
 <= H/[(T-m)(T-H-m)]
 = 1/D_pos-1/(T-m).
```

All factors are positive, and reducing each factor of the product denominator makes the second fraction larger. Multiplying by `m^2/2`, adding the common signed mass term, and retaining the equal diagonal terms proves `delta_sign<=delta_pos`. If positive parts are used, their ordering also follows from monotonicity of `max(x,0)`; positivity is unnecessary for this dominance statement.

The theorem compares the specified full-interval signed first-moment lower bound with the existing positive unit demand. It supplies no analogous dominance for an optimized hole-aware moment denominator, another feature, or further shadow information.

## The linear-feature sign window and the scope boundary

For `phi(d)=d/H`, every correlation index satisfies `-H<=d<=H-u`. The quadratic `d(d+u)` has minimum `-u^2/4` and maximum `H(H-u)` on this interval for `0<u<=2H`. Dividing by `H^2`, summing the actual pairs, and applying the same nonnegative masks proves (7). In particular the residual is nonpositive on `H<=u<=2H`; both kernels vanish beyond `2H`.

This pointwise window does not locate the row that wins the shared physical maximum, whose H varies by row. No such selection or asymptotic cost estimate is inferred. The final paragraph's separate odd-monotone Born-positivity result is motivation and is not needed for (1)–(7); this review verifies the finite geometry and demand comparison, not that separate theorem. No signed-bank analogue of the positive-bank raw causal energy increments or Abel divergence is assumed here. Original Q1 remains unresolved.

Reviewed corrected source SHA-256: `0318606f4346c0ebaa8551756a8215c6802f1aa6dc25384f4bc3924e7f882b0b`.
