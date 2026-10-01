# A42 independent review: source-pair recovery improves the rank tail

Date: 2026-09-09. Status: PASS for the full unchanged original core,
with no missing orientation factor. This is a hand proof, without
new finite calculations, source scans or Lean builds.

## One physical record per ordered source pair

Fix a cut b and component k, and let D be the actual positive
difference set of the first n=b-1 points. The oriented original
source pair is d>e in D. Sidon positive-difference uniqueness
recovers the ordered endpoints of d and of e. It also recovers
the ordered output endpoints (i,r) from the positive label t=d-e,
when that output exists at all.

Thus the map from original records at this cut/component to (d,e)
is injective. The ordering d>e already fixes the source orientation;
the actual positive output has i<r and a unique endpoint pair.
Neither a different matching description nor source-birth order
creates another copy of the same original physical record. Each
record covers a given cut once and enters a given component once.

Consequently, with H=H_b,

    Q_bk <= sum_{d>e in D} d e
          =[(sum_{d in D}d)^2-sum_{d in D}d^2]/2
          <= n^4 H^2/32.                         (1)

The equality is the exact off-diagonal product identity. The last
step uses the actual old-gap bound sum_D d<=n^2 H/4. Allowing
source pairs with shared endpoints or without an output only
enlarges the upper sum; it does not introduce multiplicity in
the injection for the original strict subset. Equation (1) is
independent of the future bank size.

## Finite genuine rank tail

Fix p>1/2 once and R_b=ceil(b(log b)^p)+1 for b>=3. Then
R_b>=b+2 and R_b-1>=b(log b)^p. For the original far component
part with k>=R_b, H_k>=H_b and (1) give, when M>=R_b,

    P_rankfar_b <= n^4/32 sum_{k=R_b}^M kappa_k
                 =n^4/32 (alpha_{R_b}-alpha_{M+1})
                 <=1/[32(log b)^(4p)].           (2)

The last bound uses alpha_R=1/[R^2(R-1)^2]<=1/(R-1)^4 and n<=b.
If M<R_b the far sum is empty and (2) holds with zero on the left.
The terminal alpha_{M+1} is retained in the exact telescope.
For k>T the actual output set remains fixed at T, while the
original genuine coefficients continue through M. This argument
does not terminate or refit those coefficients.

Since 2p>1, the same decreasing integral from2 yields

    sum_{b=3}^{T-1}sqrt(P_rankfar_b)/b
      <=(log 2)^(1-2p)/[sqrt(32)(2p-1)].          (3)

The b2 core is empty. The result needs no cap or existence of an
infinite admissible history; the infinite integral is only a
numerical upper bound on finite actual sums.

For the fixed p=5/8, the absolute norm constant is
1/[sqrt(2)(log 2)^(1/4)], and the remaining original components
satisfy

    k<ceil(b(log b)^(5/8))+1.

This is a smaller growing rank strip than A40's p=3/4 choice.
It still leaves a nontrivial near-component estimate unresolved.

## Comparison with the A40 linear-future-size estimate

Write m=min(k,T)-b. The existing actual output bound and variance
inequality give

    Q_bk<=n^2 m^2 H^2/8.

Since Q_bk>=0, taking the geometric mean with (1) gives

    Q_bk<=sqrt([n^2 m^2 H^2/8][n^4 H^2/32])
          =n^3 m H^2/16.                         (4)

This numerically dominates A40's n^3 m H^2/4 bound. A40 remains
valid and retains useful actual mixed-label recovery structure;
its older coefficient must not be presented as the strongest
known numerical bound after (1)-(4).

The source-pair cap and the output cap discard different physical
correlations. Their combined numerical bound still does not pay
the full remaining square-root harmonic norm. The fixed original
cap, all strict gates, all cuts and both horizons remain unchanged.
This is a valid sufficient component decomposition, not a proof
of CoreUniform, Q1, or a bounded maximal prefix length.

The source and review dependencies are bound in
A41_A42_review_manifest.json. The full source/output injection,
weighted bound and norm calculation are hand mathematics here.
