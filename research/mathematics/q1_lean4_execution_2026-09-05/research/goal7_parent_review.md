# Parent audit of the new mean and actual-shadow identities

2026-09-05. Reviewer: `/root`, GPT-6 Astra Ultra.

The complete `completed_fiber_mean_route.md` and
`physical_allocation_shadow_slack.md` were independently read and their
mathematical identities rederived. They pass within their stated scope.
No original-Q1 conclusion, new Lean declaration, or blanket verification
of the research notes is implied. The new fixed mean-identity run is
read back separately; no passed run is repeated by this review.

## Full fiber mean with its positive mass retained

For the mean note, the original full Mean is Base-rho^T Q^T e.
The vector rho has zero mass and zero x moment, while e has mass 3
and value 1/R on its support. Therefore the symmetric min-kernel
formula gives exactly

```
rho^T(Q+Q^T)e=-(3-1/R)rho.b-rho^T K e.
```

The constant part of the min kernel vanishes against rho, and
`integral T_rho=rho.t=-rho.b`. Substituting these two facts proves
equation (6), with precisely `f=T_e-3+1/R`. For its self term,
`e.t=e.mu=-e.b`; expanding min through absolute distance gives
`e^T Qe=(sum e_i e_j |t_i-t_j|)/4-(3-1/R)e.b/2`, as in (7).
No zero-mass formula is applied to e.

Sorting all actual fiber endpoints gives Qe=(k-1)d_k/R and the
closed A_end formula (9). Its second mean really is the mean of
earlier fiber endpoints, not a replacement for the ambient mean.
On the kth endpoint interval the tail values are exactly
`f=-(k-1)/R` and `T_xi=rk/R-C_r(k)`, proving (10)--(11).
Expanding the square in (12) yields the original Gram plus the
mixed integral and the term W2*J. Subtracting that last term proves
(13) without dropping a signed boundary.

The bracket in (9) has absolute value at most
`(1/2+1+2)R(R-1)`, and the sum of k-1 is at most 9R^2/2.
Thus |A_end|<=63R^2/4. Also W2<=2(R-1)^2 and J<=18, giving
the safe |Endpoint|<=52R^2. These are quadratic fiber bounds;
their sum does not give the sought cubic bound. In the alternative
column formula, Q^T e=(C-C_out)/R on each fiber endpoint. Summing
that identity and completing the one global square gives (17),
with every outside-fiber term O_s retained. It cannot be added a
second time to the other square completion.

## Actual allocation and its surviving slack

For the shadow note, both masks are one on the actual Delta B.
The signed square expansion is `Ez=mS+2q^2 rho^B`; the ordinary
one is `E0=mq+2q^2 sum_(DeltaB)a`. They prove respectively
`rho^B-d=(Ez-LB)/(2q^2)>=0` and the exact centered unit square e.
Thus every moment-deficit positive part at the actual allocation is
zero, not merely bounded by a portion of e. Summing the local
identity and retaining the physical maximum-minus-selected-row
terms proves (5)--(8). In particular the minimum physical margin
is at least sum e; the raw-demand restriction is essential outside
the established positive-demand epochs.

The centered full-interval coordinate has square norm V_J and
inner product m*mu with f_z. Its projection formula proves (9).
The m-1 actual holes besides the least B point lie inside J.
For m>=3 at least one lies away from the interval center, so mu!=0
forces a strict signed slack. With every h_k>0, equality in the
compact minimum would force all lambda_k=0 and then require
L_B(0)=0; this verifies the stated conditional finite strictness.
It yields no horizon-uniform quantitative gap.

The unique leftmost shadow representation has value one. Cauchy
on the other D-1 values gives precisely (10); D=1 forces mq=1
and is separated. Substituting Nq>=2D and the fixed-cap upper
bound for D gives (11). For the holes, the variance identity and
their distinct positive differences give
`W_Q>=q_r(q_r+1)(2q_r+1)/(6r)`. Using q_r>=r^2/4 then gives
W_Q>=r^5/192. Together with r>=N/2 and V_J<=T^3/12 this proves
the constant 1024 in (13). Both displayed lower scales are
summable; neither bounds the true total slack above nor provides
the required divergent gap.

## Signed-source result and precise review boundaries

The complete `signed_bank_born_positivity.md` was also read. The
parent had independently derived its signed Schur partition before
delegating the full proof, then checked the final all-clock cases,
odd monotone extension, full historical capacity identity, signed
support and good-epoch normalization. The later wording refinement
correctly distinguishes unique-maximum Born pairs from same-birth
pairs in a tied lower-clock retired group. The separate independent
review is `signed_bank_born_positivity_review.md`.

For each actual positive triple x+y=z the signed groups have raw
products 2yz, 2xz and -2xy. All Born groups share the latest clock;
their sums in each unique-maximum case are respectively 2x^2,
2y^2 and 2z^2. Tied maxima and doubled labels have the stated
nonnegative full sums. The odd monotone generalization follows
from differences of ordered feature values. Same-birth sources
must remain included. No old positive-bank causal Abel formula is
therefore imported. In the future demand the interval has length
L+2H and all m block points are holes. The resulting gain constant
`6lambda eta^2/(34^3 C log(2N))-lambda/(2N)` is correct relative
to the signed unit source; it is not a shared-source contradiction.

The current source and review hashes are bound in
`evidence/goal7_reviewed_research.json`. The finite exact run has
only its stated one-fiber scope. The physical-margin estimate and
original Q1 remain unresolved.
