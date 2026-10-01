# A79.4 independent length-bound supplement

Status: PASS — bounded hand review of the arithmetic length allowance only.

This supplement preserves `A79_PACKING_REVIEW.md` unchanged. It records the additional A79.4 proof already checked against the supplied integrated section; no finite calculation, profile enumeration, build, or repeated C18 readback was performed for this supplement.

## Claim and proof

For nonnegative interval lengths L, J and future difference t, write

`K(L,J,t) = (max((L+J)^2-t^2,0) + max((L-J)^2-t^2,0))/4`.

Then `K(L,J,t) <= (L^2+J^2)/2`. In fact, each positive part is at most its corresponding square, and `((L+J)^2+(L-J)^2)/4 = (L^2+J^2)/2`.

The three exact geometric cases in A78 give an independent case check. For the ordered four old endpoints let their adjacent gaps be A, B, C >= 0 and let H = A+B+C.

- Interlaced: L=A+B, J=B+C, t=A+C and K=BH. Thus `L^2+J^2-2K = A^2+C^2 >= 0`.
- Nested: L=H, J=B, t=abs(C-A) and K=BH+2AC. Thus `L^2+J^2-2K = (A-C)^2 >= 0`.
- Separated: L=A, J=C, t=A+2B+C and K=0, so the inequality follows from nonnegativity of the two squares.

Consequently, in a fiber containing q intervals X, summing over its unordered pairs gives

`sum_{unordered {X,Y}} K(X,Y) <= ((q-1)/2) sum_X L_X^2`.

For q>=2, each square L_X^2 occurs in exactly q-1 unordered-pair summands. The empty and singleton fibers have pair sum zero and are treated directly. The inequality is pointwise and arithmetic; it does not use or imply positive semidefiniteness of a kernel matrix.

## Source binding and scope

The integrated text inspected for this supplement was `research/u4f_core/WORKING_PROOF.md`, with the following SHA-256 values at that read:

- Whole proof: `85d5b5f2437ac03203eba0277a1ee5e5b957756085bc03f5ded11270bbb354d0`.
- A79 raw section: `2bf65d0288cdd3aa9bdd5069f6b6d81d8bd779d8cb49e0f58086efea114152ea`.
- A79 canonical section, obtained by removing trailing whitespace and appending one LF: `d4b0dd043e4d662aaa85b85b88734d7c10dfb5d1ab17cb47fa9d44227da2c0cc`.

Existing supporting artifacts, left unchanged:

- `A79_PACKING_REVIEW.md`: `9394dd50f3df73b9b7d05a143d54eefdac35338959cc0976af4f27001aa1f581`.
- `A78_KERNEL_REVIEW.md`: `f53d4b95b6982b59d601977a3d52d44a4e60ee812d2f5706af99dbed79f6427c`.
- `A78_INDEPENDENT_CHECK.json`: `b8831ee9a770c2087c32115c158384f62fb0a43fc79ac4713c9296a237e36e01`.
- `lean/Q1/U4FFiberKernel.lean`: `e3c651935b253bf0e2d57a4482cff8ae52fe7d0b1b2c144cab893bfd751a5bf3`.

The numerical comparisons in root's `A79_fiber_packing_check.py` and `A79_FIBER_PACKING_EXACT.json` remain root finite calculations. They were not rerun or independently certified by this hand supplement. The three existing Lean case lemmas supply case algebra only; this supplement makes no claim of a new Lean verification of A79.4.

The length allowance is an upper bound on the unfiltered common-fiber mass. It does not give an actual-mass lower bound, a PSD charging rule, a uniform square-root harmonic norm estimate, or a proof or refutation of the frozen proposition or Q1. Original component prices, horizons, strict gates, and their unresolved global summation remain unchanged.
