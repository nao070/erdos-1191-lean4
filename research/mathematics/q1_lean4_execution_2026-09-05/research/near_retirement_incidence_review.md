# Independent review of near-retirement incidence

Date: 2026-09-05 08:21:59 UTC. Reviewer: `/root/linear_causal_sign`,
GPT-6 Astra Ultra.

**Result:** the complete mathematical assertions and scope boundaries in
`near_retirement_incidence.md` are supported. No material correction is
requested. The source was not edited. Its observed SHA-256 was

```
b832e9b8f5abbb374ed10f08170ded8b7db825830c6a7ecb1ad8451b0a31d155
```

The complete source and `late_retirement_tail.md` were read, together
with the relevant original Abel/moment proofs in
`causal_birth_energy_telescoping.md` and the compact-exponent hypothesis
in `fixed_width_bank_density.md`. This is an independent analytic
audit. No passed evidence was rerun, no numerical experiment was used,
and no Lean conclusion is asserted. Original Q1 remains unresolved.

## 1. Actual endpoint intersection and repeated configurations

For fixed source clock `b`, output clock `r>b`, and old source
`e in F_(b-1)`, write `d=a_b-a_i` and `t=a_r-a_j`.
If `d>e`, the equality is
`a_j-a_i=a_r-a_b+e>0`. Actual positive-difference injectivity gives
at most one ordered endpoint pair `(i,j)`, hence at most one `d`.
If `d<e`, it is `a_i+a_j=a_b+a_r-e`. Repeated-summand Sidonness
gives at most one unordered pair and at most two ordered assignments.
When `i=j` it gives only one. Restricting to `i<b,j<r` can only reduce
these numbers. Thus the maximum-three degree and
`I_(b,r)<=3q_(b-1)` are correct, including repeated endpoints.

Distinct equal-sum triple multisets cannot share a point: cancellation
would give a forbidden repeated-summand two-sum collision. Writing a
repeated triple as `{a,a,b}` gives at most `L^2` choices and at most
`L` partners for each. Six slot matchings with at most two used source
pairs each give `12L^3`, allowing overcounting. Coincident triples
produce only the automatic three-cycle configurations; their used pairs
are born, so they cannot retire.

For `N<=b<2N` and `r<b(log b)^alpha`, every relevant endpoint is in
the stated `P_(L_N)`. Hence `12L_N^3/q_N^2` is valid and its dyadic
sum is finite. This is one prefix-wide bound, not a new allowance for
every source/output clock pair.

## 2. The physical output cutoff and both clocks

Same-birth sources have output in the earlier bank and cannot retire.
Every retired pair has one source in `G_b`, one in `F_(b-1)`, and one
actual output birth. Since both coefficients are bounded by `H_b`,

```
w_r |g_d g_e| <= w_b |g_d g_e| <= 1/q_b^2.
```

The ultra-near count uses at most `floor(b/(log b)^gamma)` output
ranks and
`3q_(b-1)/q_b^2=6(b-2)/(b^2(b-1))`. Its constant and the threshold
`gamma>1` are correct.

For fixed physical `t`, each new source `d` has at most two old partners
`d-t,d+t`. Thus at most `2(b-1)D_b` source pairs have `t<=D_b`, over
all future output clocks together. The constants 8 and 12 follow from
`8/((b-1)(log b)^beta)` and `b/(b-1)<=3/2` for `b>=3`. Integer floors
match the strict complementary core cutoffs.

These two bounds and the repeated-endpoint bound use the stronger
source price `w_b`. They also control `w_b-w_r` on these same sets.
The older late-rank tail instead uses decay at `r`, so its conclusion
cannot be transferred to `w_b`. The source preserves this distinction.
The four core conditions exhaust the complement of the excluded sets;
their possible overlaps are harmless under the absolute bounds.

## 3. Star packing, Cauchy, and target multiplicity

The preceding points generating `m_(b,r)` occupy at most `H_b` integer
positions and have diameter at most `H_b-1`. Their positive differences
are distinct. Thus `binom(m_(b,r),2)<=H_b-1` and the stated square-root
bound hold. New-source degree is at most `2m_(b,r)` and old-source
degree at most three. Cauchy on the edge set actually proves

```
sum_edges |g_d g_e| <= sqrt(6m_(b,r) v_b S_(b-1)),
```

which is stronger than the source's absolute value of the signed sum.
Restricting to core edges preserves the degree bounds.

Disjoint output birth classes give exactly the new part of the same
physical bank in `[1,H_b]`. Subtracting its `q_b` old labels is correct.
The dyadic-rectangle description retains cross-batch point pairs as
well as internal ones. Finally the multiplicity per physical target
over a source dyad is exactly bounded by
`2 sum_(b=N..2N-1)(b-1)=3N(N-1)`; it cannot be dropped.

Two optional refinements are `m_(b,r)<=r-1` and, after the output
cutoff, `binom(m^*_(b,r),2)<=W_b-1` for `W_b=H_b-D_b>=1`.
They are used in the separate follow-on, rather than changes required
to repair the original proof.

## 4. Abel comparison and every nongood source dyad

The core count inequality is appropriately one-sided: the signed sum
is bounded above by absolute products, each costing at most `1/q_N^2`
when its source clock is at least `N`. Including future outputs beyond
the terminal rank enlarges that nonnegative bound.

For `N<=n<2N`, permanent coefficients give `S_n>=S_N`, and the
actual moment bound gives `E_n>=(3/2)N^2S_N^2/H_(2N)^3`.
Also `q_(2N)>4q_N`, `H_(2N)>=H_N`, so the block loses at least
`15w_N/16` of its weight. This proves exactly the `45/32` factor and
the displayed denominator in `Lambda_N`, without assuming a good
epoch or monotonicity of `E_n`.

The blocks are disjoint parts of the Abel interior at dyadic terminal
horizons. Therefore the pointwise sufficient incidence bound, if
proved, yields the claimed subcritical retirement estimate. One may
explicitly write `0<=kappa<1/2`; any feasible instance of the stated
target already forces nonnegativity once `S_N>0`.

The alternative global target keeps every source dyad on its left
and uses productive dyads only for the energy lower bound on the
right. This is the correct direction. Productive divergence does not
prove that upper bound or permit deletion of nongood source terms.
The fixed-width density theorem also really requires exponents in
a fixed compact subset of `(1/2,1)`, as the source states.

Finally the physical margin and source-clock commutator remain separate
obligations. Even proving subcritical retirement would not remove
them. The source's claims pass this audit; the logarithmic saving is
still unproved. `near_retirement_packing_limits.md` records the bounded
follow-on and quantifies this remaining scale gap.
