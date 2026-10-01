# Independent review of the eligible separation deficit

2026-09-05, 12:53:57 UTC. Reviewer: `/root/moment_evidence_audit`, inherited
GPT-6 Astra Ultra. This is an analytical and semantic review; no finite checker,
Lean build, axiom audit, or kernel replay was executed for this review.

Reviewed the entire `signed_eligible_separation_deficit.md`, SHA-256
`151b97dc7775a04f42f1b3d74dee9c112dde7fa06078346ef7d0519fa4463765`.
Read the prerequisite definitions and equations in §§1–4 of
`signed_output_energy_closure.md`, SHA-256
`8a1ac50d3e8744757e93a287d8943cea5aebc4dd542cc0f0b2608134122c9b12`.
The later sections of that source are outside this review.

**Verdict:** all seven displayed conclusions, the actual rank count, and the
single-budget interpretation are valid at their stated scope. No material
correction is required. The finite, cap-free geometric estimate does not supply
the missing asymptotic distribution of eligible energy or a Q1 contradiction.

## Algebra and normalization

The condition `n>ell>max(u,v,x,y)` makes `t,p,q,A,B` positive. Equal three-sums
give `A+B=t+p+q`. The four formal eligible source products are `-g1,-g2` and
their signed reflections, and division by the positive integer
`aut(U)aut(V)` is the same exact multiset normalization as in the input.
Thus the carrier and energy quantities compared here both carry precisely one
factor `1/aut`; no extra factor two or eight is introduced during summation.

For each `gi` the two factors sum to `t`, so its positive part is at most
`t²/4`. Hence `P≤t²/2`. Substitution into the exact defect gives

\[
G_\lambda\ge
\frac{8(1+\lambda)(pq+AB+t(p+q))+8(1+3\lambda)t^2}{\mathrm{aut}},
\]

which implies (1) for `lambda≥0`. The physical-source interpretation retains
the specified `0≤lambda≤1`; the wider algebraic range is not imported into that
interpretation.

For (2), whichever of `p,q,A,B` equals `M` has a partner at least `L`, so
`pq+AB≥LM`. Both `s+t≥M` and `s+t≥t+2L` hold, including when the maximum lies
in `{p,q}`. Averaging those inequalities yields the displayed bound on
`t(s+t)`. Subtracting `D*H*/2` leaves `L(M+t)/2≥0`. This checks the signs and
constants of (2)–(3).

The three-slot variance identity is
`[h²+z²+(h-z)²]/3`, with `0≤z≤h`; its maximum is `2h²/3`. Repeated slots cause
no issue. Applying the bound separately to both triples and multiplying by the
exact factor `12/aut` gives `DeltaY≤16(H*)²/aut`. Also `DeltaY>0` follows, for
example, from the positive `18t²/aut` term in its exact distance formula.
All divisions by `H*`, `aut`, and `DeltaY` used in (4) therefore have positive
denominators. Combining the lower defect bound with this upper energy bound
gives the stated coefficient `D*/(4H*)` in the valid direction.

## Actual rank count and fixed cap

The latest of the four old source endpoints is `a_b`, so `D*=a_r-a_b` exactly.
The intermediate output endpoint `ell` lies strictly between them, giving
`h=r-b≥2`. The interval `[a_b,a_r]` contains exactly the `h+1` consecutive
history points of ranks `b,...,r`. Their `h(h+1)/2` positive differences are
distinct positive integers, by actual Sidon two-sum uniqueness, and all are at
most `D*`. Thus `D*≥h(h+1)/2`; this is an actual endpoint count, not an
independent-label model.

Since `H*≤H_r`, the factor `D*/(4H*)` is at least
`h(h+1)/(8H_r)`, verifying (5). One fixed eventual cap
`H_r≤C r² log(2r)` then gives (6) at all ranks beyond the same fixed onset.
The logarithm is positive there, and the cap constant is positive (as required
by any such cap on nonzero widths). For `h≥epsilon r`, dropping the additional
positive `h/r²` yields the displayed `epsilon²` estimate. Nothing here permits
a rank-dependent choice of `C` or of the onset.

## Single physical budget and formal alignment

At an eligible collision, both actual sources precede the lower output
endpoint. Every payment from a strictly future block has this property. Each
eligible collision has at most one eligible output, whose four formal records
share the actual newest output rank. Multiplying (4) by a finite nonnegative
output price and summing produces the coefficient `(1+lambda)/32` of the
subtracted energy in (7). Active collisions lacking an eligible output and
the nonnegative Born-only remainder add nonnegative energy to the first term;
they require no subtraction and do not pay another copy of the budget.

For `omega=u`, the left side is exactly the already defined output-clock
eligible carrier budget. Pairwise disjoint physical output differences allow
each physical source pair to be charged at most once. The source matrix remains
the complete PSD source; this estimate does not assert that deleting its
ineligible entries preserves PSD. No historical boundary or ineligible
capacity is added as a second payment resource.

The two recent Lean modules align with the local eligibility used here:

- `Q1/SidonTripleCollision.lean`, SHA-256
  `d4f042ca3fe5a729ec6785988d5b2c819257bfaadf372c730353276000cf532e`,
  derives equal-sum distinct triple multisets and support disjointness from
  actual Sidon old-source witnesses.
- `Q1/SidonEligibleCollision.lean`, SHA-256
  `1489bf5bea109380df3d7c8369f2a04f6450083f9ee693a9556be5a6571d5105`,
  uses cutoff `m` below `n`, retains all four source endpoint inequalities
  `<m`, and proves exact opposite-side counts of `m` and `n`.

With `m=ell`, these are precisely the endpoint facts needed at the start of
the analytical note. Their cutoff is an actual value. Formal history/rank
enumeration, matching-orbit counting, carrier and energy expansions, and the
inequalities reviewed above remain outside those Lean modules. Their previous
successful execution records were not rerun or re-audited for this review.

## Optional local strengthening

One can retain the nonnegative difference already computed after (2). Without
any new assumption it gives

\[
 pq+AB+ts+t^2\ge\tfrac12(t+2L)(t+M),
\]

and therefore

\[
 G_\lambda\ge\frac{4(1+\lambda)(t+2L)H^*}{\mathrm{aut}}
 \ge(1+\lambda)\frac{t+2L}{4H^*}\,\Delta Y.
\]

Thus `(D*+L)/H*` may replace `D*/H*` in the subtraction in (7). This is a valid
local refinement; it does not improve the guaranteed rank-only factor when no
additional lower bound on `L` is available. The original source was left
unchanged.

The explicit unresolved scope is correct: even a positive fraction of energy
at fractional rank gaps would leave the factor `1/log(2r)`. Divergence of the
weighted energy alone does not establish divergence of the weighted defect,
and no demand-versus-budget contradiction has been proved here.
