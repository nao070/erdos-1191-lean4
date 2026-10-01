# A56 independent review: full-price short lower-output delay

Date: 2026-09-09. Status: PASS independent hand proof. No new finite task or Lean run; no shared source edits or redelegation.

## Exact claim

Fix q>1 once and R_c=floor(c/(log c)^q). Retain the original strict-core physical records with i-c<=R_c, allowing any original upper output r<=T. Price each selected record by the original full de*u_r^[M], T<=M, and retain all original covered cuts c+1,...,i-1. This changes neither the frozen core nor any original component coefficient, cap parameter, endpoint or terminal alpha.

## Actual count at fixed upper output

The four distinct old endpoints imply that exactly one source label ends at birth c. For each fixed output pair(i,r), the two possibilities (fresh larger or fresh smaller source) and the other old endpoint give at most2(c-1) records, by actual Sidon difference recovery exactly as in A55. At fixed r there are at most R_c allowable lower output indices i. Thus at most2(c-1)R_c selected records have this c,r. Each has de<=H_c^2.

The full birth price therefore satisfies

    E_c <= 2(c-1)R_c H_c^2 sum_{r=c+2}^T u_r^[M]
         <= 2(c-1)R_c sum_{r=c+2}^T alpha_r H_c^2/H_r^2
         <= 2(c-1)R_c sum_{r=c+2}^T alpha_r.

Here u_r^[M]<=alpha_r/H_r^2 follows from genuine finite pricing and monotone H_k, with alpha_(M+1) subtracted before an upper bound is taken. All actual ranks used satisfy r<=T<=M. There is no assumed history extension; only the explicit positive scalar alpha series will be extended to an infinite summation for an upper bound.

## Exact scalar tail

For integer n>=1,

    (1/n^3-1/(n+1)^3)/3 - alpha_(n+2)
     = (12n^3+25n^2+16n+4)
       /[3 n^3 (n+1)^3 (n+2)^2] >0.

Summing n=c,...,T-2 gives sum_{r=c+2}^T alpha_r <= [c^(-3)-(T-1)^(-3)]/3 <=1/(3c^3); if T<c+2 the original sum is empty. This yields

    E_c <= 2(c-1)R_c/(3c^3)
         <= 2R_c/(3c^2)
         <= 2/[3c(log c)^q].

The scalar tail bound does not replace any record u_r by a reset or reindexed genuine price.

## Exact physical coverage and convergent norm

All original strict records have c>=4. In the dyadic birth group 2^ell<=c<2^(ell+1), ell>=2,

    E_ell <= (2/3)(ell log2)^(-q).

For each selected record,

    sum_{b=c+1}^{i-1}1/b <= (i-c-1)/c
                         <= R_c/c <= (ell log2)^(-q).

Because R_c<c for c>=4, all covered cuts obey2^ell<b<2^(ell+2), independently of how large r is. The harmonic support weight is at most2log2. The exact coverage identity gives

    I_ell <= (2/3)(ell log2)^(-2q),
    N_ell <= 2 sqrt(log2/3)/(ell log2)^q.

Summing birth groups by pointwise square-root subadditivity proves

    N_selected <= 2 sqrt(log2/3)/(log2)^q
                  * sum_{ell>=2}ell^(-q) < infinity, q>1.

For q=5/4, the series is at most integral_1^infinity x^(-5/4)dx=4, so

    N_selected <= 8/[sqrt3 (log2)^(3/4)].

The bound is uniform for all original finite M,T and requires no cap. It selects a full-record class through i-c, while A55 selects through r-c and A43 selects cut-dependent components through k-b. No general comparison or unproved disjointness of these classes is used. If multiple paid classes overlap, an ordered partition or positive majorization avoids double-counting as an identity; the sum of their norm bounds is still a valid upper bound on their union.

## Verification and unresolved boundary

Independent hand review checked fresh-source orientation multiplicity, finite alpha indices, the explicit positive polynomial, integer support endpoints, q>1 and the q5/4 constant. No additional record, history, source/bin or profile evaluation was performed for A56. Root-reported generic Lean work is not represented here as full verification of A56. The complete count/price/coverage/uniform norm remains a hand proof. CoreUniform, the remaining frozen norm, Q1 and final clean Lean closure are unproved. On the remaining class after this payment one may impose i-c>floor(c/log^(5/4)c); the next estimate must still retain common source/output correlations and full original price.

## Source binding

This proof reuses the exact source uniqueness and full-price conventions reviewed in A55 and the earlier source-pair and birth-group notes. SHA-256 of reused pre-existing sources:

- `A42_SOURCE_PAIR_RANK_TAIL_REVIEW.md`: `1f8f530e53de783939ef396490e1fc13168c5babd344e2602bd4add395c9e350`
- `A43_SHORT_RANK_COMPONENT_REVIEW.md`: `29fcc131c926e1c7c2d24e4d11171213e603d8ef19bd5dec4300529324b3f02f`
- `A53_BIRTH_RELATIVE_COMPONENT_TAIL_REVIEW.md`: `befdce4b639afa97044cb66628797a00e60387dd2df53169585453a2f57db208`
- `A50_A54_final_review_manifest.json`: `41b65b36e33bf4ceb922da65676a95780be468fe10ee082257a8b5dee336e4b7`
- `A53_EXISTING_RESTART_WITNESS_EXACT.json`: `4922d09cc1962ef0d7a466baa3713210e24d863b4c6bff7c8a02d38eb749caa2`
- `A54_EXISTING_WITNESS_FLAG_EXACT.json`: `89dcbd66964618bac33a48adc3e4cf694e2b8f9c7e3b0f6011060f9404e71d9b`
- `C1_m02_dense_variant1_M96.json`: `d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e`
- `C1_m02_dense_variant1_M96_independent_check.json`: `970215ab400c0427c10f30ad44e2bd9db4b8f2cf91ded2a85205b1c160ac4083`
- `reference_evaluator.py`: `3c8339dca1d7e75a0e7e2ff4088c0deea13a39274ad53430df83362d65fd5756`
- `independent_checker.py`: `24673840329f7407395428f6cfda5706813c4f0e4b386723540aa62645c7a198`
