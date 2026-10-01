# Erdős Problem #1191 — Route C proof-reset checkpoint

Date: 2026-08-30 continuation (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Scope: exact finite signed-correlation, ordered-root, and direct-Haar
theorems, scoped payment no-gos, current primary-source audit, and the finite
multi-epoch actual-cell SDP target.  This is not a new numbered Wave.

## What is now proved

1. For every finite Sidon set and finite joint-kernel system, the exact
   independent-coordinate positive-part completion is

   `E_H<=|A|C_H(0)+2P_H`

   `=m^T Hm+(|A|-1)C_H(0)+2N_H`,

   with an exact slack formula.  This relaxation is not globally strongest;
   it does not retain even `|Delta(A)|=binom(|A|,2)`.
2. If `H` is PSD, annihilates the probability-kernel mass vector, and has
   nonzero effective energy `C_H(0)>0`, then some nonzero combined correlation
   is negative.  In fact `2N_H=C_H(0)+2P_H>=C_H(0)`.
3. Distinct translated point-mass channels cannot improve their same-diagonal
   independent-coordinate positive-part bound.
4. Overlap can escape that obstruction.  For two probability kernels and
   `H_b=[[1,b],[b,1]]`, a negative coefficient passes the shift gate exactly
   when `b>=-rho`, with `rho=min_(B_d>0) A_d/B_d`.  Every feasible `b<0`
   gives

   `U_b(k)-U_0(k)=b(2+(k-1)B_0)<0`.
5. Probability mass gives the endpoint identity
   `sum_(d>=1)(A_d-B_d)=-||K_1-K_2||_2^2/2`; hence `rho<=1`, equality forces
   identical kernels, and distinct kernels have `rho<1`.
6. The uniform law on any `m`-point Sidon set satisfies
   `H(X+X')=2log_2(m)-(m-1)/m`, so a separate uniform-prefix entropy value
   contains no spacing geometry.

All theorem-level items above passed independent adversarial proof review.
No finite-to-infinite inference is included.

## Exact fixtures and the normalization warning

- Minimal overlap grid:
  `K_1=delta_0`, `K_2=(delta_0+delta_1)/2`, `b=-1/2`, with
  `U_b(2)/U_0(2)=4/7`.
- First full-support denominator-four grid: ratio `29/176`.
- Degenerating rational family:
  `K_1=(1/2-t,1/2+t)`, `K_2=(1/2,1/2)`, `b=-1+2t^2`.
  Its pure-energy ratio tends to zero, but total correlation mass,
  `C_H(0)`, and the small Gram eigenvalue all vanish like `t^2`.

Therefore unit diagonal does not normalize the problem.  The pure-energy
gain is real but is not yet a useful joint Sidon inequality.

## Boundary-cover-normalized extension

The lower-side normalization from Hou--Zhao Lemma 2.1 and Proposition 3.1
has now been generalized to a positive-definite cross matrix.  Put

`beta=gamma^T H^-1 gamma`, `s=1^T H1`,

`a_H=m sum_(r,s) h_rs <p^r,p^s>`,

`Phi_H=sum_(j<Lm) q_j^T H^-1 q_j`, and

`b_H=beta+2(Phi_H/m-L beta)`.

Under the joint cover, the every-shift combined-correlation gate, `b_H>0`,
and the source-style separation `N>=2LT`, the exact master inequality is

`k^2<=(beta N+b_H T-beta)(s+a_H(k-1)/T)`.

Cauchy--Schwarz gives `delta=beta s>=1`, with equality exactly when
`gamma=H1/s` and that vector is a nonnegative admissible mixing weight.  The
correct general secondary coefficient is

`delta^(1/4)sqrt(a_H b_H)`,

not `sqrt(delta a_H b_H)`.  At the only leading-constant-one normalization
`delta=1`, it reduces to `sqrt(a_H b_H)`.

The coupled boundary problem is the strict convex program

`Phi_H=min q^T(I_(Lm) tensor H^-1)q` subject to `Aq>=c`,

with dual `c^T y-y^T A(I tensor H)A^T y/4` and exact KKT certificate.  Zero
mixing coordinates must be deleted or fixed to zero; treating them as free is
not the same problem.

An exact normalized witness uses `m=3`, `L=2`,

`p^1=(1/4,1/2,1/4)`, `p^2=(3/8,1/4,3/8)`,

`H=[[1,-1/5],[-1/5,1]]`, and `gamma=(1/2,1/2)`.  It has

`a_H b_H=20620579147935/22461389262592=0.9180455806...`.

For the same kernels with `H_12=0`, the exact product is

`840600527/912906560=0.9207958008...`.

Thus the coefficient improves by the exact square-root ratio
`0.9985054901...`, about `0.15%`.  This does not establish a global cross
advantage: in the stated denominator-eight, `m in {3,5}`, `L in {1,2}`
grid, a different diagonal/direct-sum candidate has product
`20720894357613941/23062969911203072=0.8984486576...`, and is better by
about `1.085%` at coefficient level.  The grid result is finite and is not a
global no-go.

## Exact perturbation of the published eight-kernel certificate

The official Hou--Zhao v2 certificate was fetched from commit
`ef044564300e546f8832b31f5fba133fd192cc3a`.  Its verifier SHA-256 is
`957a5afadd849ac4f97c2b71252abb5c796c2db3c91a608ab35097e3c49292a8`,
exactly the hash printed in the paper, and the untouched verifier reproduces
all 129 covers and the published coefficient `0.9434925907135450...`.

Let `D=diag(lambda)` be its diagonal coupling and let `J` have the symmetric
nonzero upper entries

`J_12=-1, J_14=2, J_17=-1, J_28=1, J_45=-1, J_48=-1, J_57=1`.

Every row sum of `J` is zero.  At `epsilon=1/6250`, put `H=D+epsilon J`.
Then `H1=lambda`, `s=beta=1`, so the published mixing vector, cover, and
boundary weights remain valid without reoptimization.  Exact strict diagonal
dominance proves `H` positive definite; its smallest affected-row margin is
`6303669/100000000`.  Every discrete combined correlation is positive, with
minimum at shift 31,

`1819897465312660450421661319/6250000000000000000000000000000`.

Exact recomputation gives the finite coefficient

`sqrt(a_H b_H)=0.9434922260277724855...`,

strictly below the published one by about `3.64686e-7`.  The search exhausted
210 alternating four-cycles in both orientations and sums/differences among
the best 80 downhill cycles; the chosen two-cycle combination was best only
in that bounded search.  This is not a global optimum, a novelty theorem, or
an order-changing result for #1191.

## Exact boundary-QP reoptimization on the pinned direction

The boundary vectors are no longer frozen.  Keeping the same hash-pinned
eight kernels, mixing vector, and integer direction `J`, set
`epsilon=1/462` and solve the generalized boundary QP exactly.  The unique
fixed-outer-data optimum has 126 active cover rows; rows 1 and 15 are inactive
with strict slack.  Exact rational KKT replay verifies positive active dual
coordinates, nonnegative cover slack, stationarity, complementarity,
primal--dual equality, and strict positivity of every primal coordinate.

Strict diagonal dominance still proves `H>0`, every one of the 32 discrete
correlations is strictly positive, and the smallest correlation is the
shift-31 fraction

`140676565613953482417771177563/481250000000000000000000000000000`.

The resulting exact coefficient is

`sqrt(a_H b_H^*)=0.9434876661938243084...<94348767/100000000`,

so the project-internal master lemma certifies

`F(N)<=sqrt(N)+0.94348767 N^(1/4)+O(1)`.

This optimum is only over the boundary variable for the fixed kernels,
mixing weights, direction, and epsilon.  It is not an optimum over epsilon,
directions, kernels, or mixing weights, and it carries no current-best,
novelty, Q1/Q2, compatible-history, publication, or prize claim.

Along the same direction, exact determinant and correlation calculations give
the PD-and-correlation feasible rational interval
`{e in Q:-rho<e<rho}` with `rho=0.0474555448542...`.  For the separately fixed
published boundary vector, Sturm's theorem proves exactly one stationary point
in the real PD interval, bracketed by
`80060813/500000000000 < e_* < 160121627/1000000000000`; it is the constrained
fixed-`q` minimum.  This statement does not concern the reoptimized value
function.

## Exact two-scale bridge boundary

Two widths are not themselves an obstacle.  On the common `h` grid, widths
`T=mh` and `2T` have the exact lifted correlation

`C_h(qh+t)=((h-t)C(q)+tC(q+1))/h^2`,

so the discrete nonnegative-shift gate and the cross-matrix boundary master
remain legal on the **same** finite prefix.  If the kernels lack a common
symmetry center, the left and right boundary quadratic programs must be kept
separate rather than silently doubled.

Different nested prefixes do not factor this way.  Their exact energy splits
into old--old, old--new, and new--new coefficient functions.  One combined
correlation gate controls only the old--old sector, while a constant simplex
tail covers a new mark with weight only `gamma_2`; unit new-mark cover forces
the old channel out of the constant leading bulk.

There is also an exact method closure.  For `2^j`-mark prefixes,
`N_j>=1+binom(2^j,2)`.  Hence every uniform finite remainder
`O(N^(1/2-delta))`, `delta>0`, contributes a geometrically summable `O(1)`
after division by `sqrt(N_j)` and the bounded Fejer weights.  In particular,
even deleting the whole `N^(1/4)` term cannot change the existing
`Omega(log J)` compatible-branch floor.

The smallest retained-covariance candidate uses
`H_theta=diag(lambda,1-lambda)-theta(1,-1)(1,-1)^T`.  It preserves
`s=beta=1` and gives the exact product

`(B_D+kappa Q)(U_D-theta V)`,

where `V` is the same-prefix two-width square and `Q` is its boundary price.
The exact box replay then shows why the raw positive gain is insufficient:
the dyadic total of `V` is diagonal Parseval mass, while the centered
off-diagonal part sums to zero on every fixed prefix.

The centered compatible-history subproblem is now solved by retaining every
band on the short path between successive nonanticipating widths.  Let
`k_j=2^j` and, after a finite `C`-dependent onset, set

`T_j=2^(s_j)=k_j*2^ceil(log_2(8C log(2k_j)))`.

Then `s_(j+1)-s_j` is one or two.  At least `k_j/4` newly owned adjacent gaps
are at most `T_j/2`, and the centered first-use low-pass increment is at least

`1/(64 C (j+1) log 2)`.

Writing `C_(j,r)=||1_(A_j)*K_(2^r)||_2^2-k_j/2^r` and retaining the complete
path

`X_j=C_(j,s_j)-C_(j,s_(j+1))`,

exact endpoint matching and Fejer summation give

`sum w_j X_j >= (log J)/(64 C log 2)-O_C(1)`.

The fixed three-channel realization uses
`D=diag(1/4,1/2,1/4)`, the three-vertex path Laplacian, and `theta=3/25`.
It is positive definite, has `s=beta=1`, and the constant full-support cover
has no inverse-metric contrast penalty.  Since its boundary ratio differs
from one by a summable `O_C(j/2^j)`, the normalized centered gain has leading
coefficient

`3/(1600 C log 2)>1/(1536 C log 2)`.

The memo also records a fully explicit finite-horizon constant
`K_(C,j_0)` for the safe choice `eta_C=3/(3200 C log 2)`; no hidden
`O_C(1)` is needed in the stated component theorem.

This closes the nonanticipating centered carrier, internal scale ownership,
Abel boundary, and terminal payment.  The companion box-dipole continuation
also closes the continuous scale-density map and identifies every positive
finite-horizon coefficient with an already-owned strict-interior Gothic
`beta_n(p,q)` atom.  Continuum phase averaging is exact; fixed finite phases
and ordinary fixed-prefix domination are closed by explicit counterexamples.
It does **not** close C058: the missing statement is now a legal
phase-integrated *rewrite* of the existing Gothic ledger, including the
rank-dipole PSD/diagonal price and compatible-history terminal terms.
The audited derivations are
`route_probes/ROUTE_C_RETAINED_COVARIANCE_BOX_PROBE.md` and
`route_probes/ROUTE_C_CENTERED_MULTIBAND_HISTORY_CARRIER.md`, followed by
`route_probes/ROUTE_C_CROSS_RATIO_BOX_DIPOLE_BRIDGE.md`.

The next algebraic layer is also exact.  On a finite nested prefix/scale grid,
the prefix and scale differences obey a zero-curl identity.  Two finite Abel
summations yield interior retained-band coefficient

`b_(j,r)=w_j s_(j,r)-w_(j+1)s_(j+1,r)`,

with all initial, final, and scale-terminal rows displayed.  For the
universally saturated pointwise-capacity profile at consecutive dyadic
epochs, all these coefficients are nonnegative iff

`w_(j+1)2^max(0,R_(j+1)-R_j)<=4w_j`.

A certified cutoff jump `2 -> 5` has `b=-62/121`.  This closes only the
shortcut that transposes the full envelope through adjacent epochs and
silently assumes nonnegative coefficients.  Pair-dependent allocation,
longer transport, and a larger signed master remain open.  The audited
derivation is `route_probes/ROUTE_C_PHASE_TRANSPORT_GATE.md`.

## Pair-owned allocation and exact coefficient-PSD price

C067's source memo and C069's source memo both use `P_n(T)` for different
quantities.  In this summary `P_n^pot(T)` means the positive finite-horizon
potential, while `P_n^PSD(T)` means the least coefficient-PSD diagonal price.

C067 now solves the positive strict-interior allocation at owner resolution.
For the scale weights `u_(gamma,r)`, the exact proportional rule

`x_(gamma,r)=u_(gamma,r)Q_n(T_r)/P_n^pot(T_r)`

(with zero variables when `P_n^pot(T_r)=0`) meets every pair capacity and the
aggregate Wave demand.  On the canonical dyadic spatial-prefix chain, each
physical strict-interior positive `lambda=beta` pair is born wholly inside
its current dyadic block.  Its formal negative pre-birth band is therefore
zero, the birth coefficient is positive, and the scale-terminal row stays
explicit.  This owner lift is a rewrite of the already-owned Gothic `beta`
sector, not a second reserve.

C068 closes only the scalar fractional fallback of the stated envelope
class.  On the certified nested Golomb prefixes with `n=4 -> 8` and weight
ratio `100/81`, the first-use supremum is `18/385` and seven exact positive
Wave atoms give contradiction gap `461/227700`.  Owner-resolved coordinates,
signed or cross-phase payment, longer transport, and a larger master remain
available.

C069 gives the exact least diagonal cost of the stronger active
coefficient-PSD completion:

`P_n^PSD(T)=sum_((i,j) in E_n(T)) alpha_(i,j)sqrt(g_i(T)g_j(T))`.

The primal is the explicit weighted edge-Laplacian completion and the dual
optimizer is rank one in the diagonally scaled elliptope.  The tent table
gives `P_n^PSD(T)>=2Q_n(T)` and, after integration, `Pi_n>=2W_n`.  Exact active
localization is mandatory for integrability.  This does not price an argument
that uses positivity only on the actual ordered box-dipole Gram matrix.

C070 shows that the isolated positive same-epoch Gothic sector cannot pay
that stronger price universally.  For
`(0,101,204,309,416,525,636,749)` at `n=4`, the active graph is bipartite and
the exact certificate has

`G_4<2W_4<=Pi_4`.

The remaining target at the C070 checkpoint was therefore an actual
Gram-restricted inequality or a signed cross-epoch, cross-phase, or larger
master.  The next continuation resolves the fixed-scale Gram restriction but
not its legal signed insertion.  C067 must still enter by rewriting, never
duplicating, the Gothic `beta` ownership.
The audited derivations are
`route_probes/ROUTE_C_PAIR_OWNED_ALLOCATION_LP_PROBE.md` and
`route_probes/ROUTE_C_DIPOLE_PSD_PRICE_PROBE.md`.

## Actual ordered-root continuation and scoped ramp closures

C071 proves the exact full-gap root decomposition

`G_T=diag(rho)+sum_(i<j)psi_(i,j)(e_i-e_j)(e_i-e_j)^t`, `rho_i>=0`.

The indefinite Wave matrix `B_ij=-alpha_(i,j)/2` belongs to this labeled
ordered-root dual and satisfies `<B,G_T>=Q_n(T)` as a literal cellwise
sum of squares.  C072 proves

`eta^tG_T eta-Q_n(T)`
`=sum_i rho_i eta_i^2+(4n^2)^-1 sum_i psi_(i,i+1)>=0`

with the exact optimal-shift Schur formula.  C073 proves the insertion gates:
the ungated ramp diverges at zero, signed bands may leave the root cone, and
zero nonadjacent-root slack blocks nonconstant PSD Schur cross-coupling.

C074 keeps only disjoint strip marginals and obtains
`Q_n(T)<=V_n(T)<=P_n^PSD(T)/2`.  C075 shows on the C070 fixture that
`V_4=32755417/340707840` exceeds the full positive same-epoch Gothic sector
by the exact positive margin `898545848033/103063780892160`.  Exact labeled
intersections and signed rows remain outside this marginal-only no-go.

C076--C077 close only the unused negative-potential magnitude as an isolated
nonnegative payment source.  On `(0,2,5,16,22,23,31,35)` it vanishes at an
active scale and fails exact phase, integrated-price, and terminal full
payment.  On
`A_L=(0,2,5,16,L+16,L+17,L+25,3L+25)` it stays bounded while the pair,
marginal, and coefficient-PSD prices diverge logarithmically, so it pays no
positive universal fraction of those three prices.  The original negative
rows with their signed kernels remain live.

C078 closes a linear cellwise insertion of the active ramp into the fixed
three full-prefix channel carrier with baseline payment only from the
positive same-epoch Gothic sector.  The ramp is not in that formal channel
span; a zero-mass fourth channel retains a positive Schur/energy price and a
nonzero gate terminal.  On `A_L`, the optimal ramp baseline has logarithmic
coefficient `27/128`, whereas the complete positive sector has `18/128`, so
the gap is `(9/128)log L+O(1)` and is exactly positive already at `L=2^18`.
The indefinite labeled-cell `B` itself has zero surplus in the actual root
dual, so a direct membership-sensitive signed rewrite is not ruled out.

These are C071--C078, not a new numbered Wave.  The source memos are
`route_probes/ROUTE_C_ORDERED_GRAM_RAMP_MASTER.md`,
`route_probes/ROUTE_C_GRAM_MARGINAL_TRANSPORT_PRICE_PROBE.md`,
`route_probes/ROUTE_C_NEGATIVE_POTENTIAL_RESERVE_NO_GO.md`, and
`route_probes/ROUTE_C_RAMP_COMMON_MASTER_NO_GO.md`.

## Direct ordered-`B` interval/Haar bridge and remaining cell SDP

C079 sets `M=D^tBD` on the physical point coordinates.  Every binary
consecutive interval state of length `m` has exact value `m^2/(4n^2)` for a
strictly internal interval with `m>=2`, and zero otherwise.  Thus

`Q_n(T)<=||sum q_k||_2^2/(4n^2)`

sharply.  The identities `M1=0`, `diag M=0`, and
`2M_(p-n,q-n+1)=lambda_(p,q)` prove that direct `M` rows and finite-horizon
Gothic rows are the same physical pairs.  This is a rewrite, not a second
capacity.  Consecutive direct-pair supports are disjoint, but their positive
count baselines share one endpoint diagonal.

C080 proves the exact signed Abel identity, including lower negative and
upper positive endpoint rows.  Active endpoints can be chosen so both vanish.
Together with the exact Haar Gram identity for `G_T-G_(2T)`, this yields a
terminal-free signed direct-`B` representation of `W_n/log 2`.

C081 fixes both signed-band signs with `-1/324` and `+63/256000`.  On the
actual half-open cell `[636,709)`, `1^tv=0` and `v^tMv=1/8`, so
`kappa J-mu M` is negative for every finite `kappa` and `mu>0`.  C082 shows
that singleton zero slack also kills every nonzero scalar interval cover and
every nontrivial root-restricted Schur cross block at zero price.

C083 closes payment of the sharp count baseline by the positive same-epoch
Gothic sector.  On `A_L`, the baseline has log coefficient `11/64` versus
`9/64` for that sector, and at `L=2^24` the exact gap exceeds `1/32`.

C084 solves the exact complete-cell `n=4`, `T=200`, `mu=1`
root-SDDM-plus-`J` coefficient LPs, with optima `1/16` and `1/10`.  C085
solves one substantive two-active-epoch `n=4/n=8`, common-`T=200` fixture,
with exact optimum `53/448`; its shared global correction diagonal
`47/1792` is counted once.

These are C079--C085, not a new numbered Wave.  C084--C085 are
`COMPUTATIONAL_FINITE` coefficient-trace results: `trace(C)/(2T)` is not the
physical root-shift energy, and one global accounting entry is not a paid
budget owner.

C086 proves the exact physical root cost `chi_T(d)=3d/T,4-d/T,2` on the
three ranges `[0,T]`, `[T,2T]`, and `[2T,infinity)`.  C087 gives strict exact
joint physical savings `103/5600` and `11251/448000` on the stated two- and
three-epoch fixtures.  C088 shows the fixed sparse correction has slack
`-5/32` on one nearby-scale cell and the fixed quadratic family has the
collision `a_3-a_0=a_(C+5)-a_(C+4)`.  It closes only literal fixed reuse and
that changing family.

The OPEN target is a scale-adaptive finite-horizon actual-cell cover and the
single-ledger net inequality
`G_off-P-terminals >= epsilon_C log((J+1)/(j0+1))-K_C` on every capped
compatible finite tower.  Since the cell-length dual gives
`P>=weighted W`, feasibility/joint saving alone is insufficient; only cover
excess with explicit one-for-one `2M=lambda` cancellation may be charged.

## Reproducible evidence

From `route_probes/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_cross_kernel_positive_part_certificate.py \
  signed_offdiag_two_kernel_test.py \
  test_overlapping_kernel_probe.py \
  test_boundary_normalized_cross_kernel_probe.py \
  test_hou_zhao_cross_perturbation_certificate.py \
  test_hou_zhao_reoptimized_boundary_certificate.py \
  test_retained_covariance_box_probe.py \
  test_centered_multiband_history_certificate.py \
  test_cross_ratio_box_dipole_certificate.py \
  test_et_fixed_prefix_no_go_certificate.py \
  test_phase_transport_gate_certificate.py \
  test_pair_owned_allocation_certificate.py \
  test_dipole_psd_price_certificate.py \
  test_gram_marginal_transport_certificate.py \
  test_ordered_gram_ramp_master_certificate.py \
  test_negative_potential_reserve_certificate.py \
  test_ramp_common_master_no_go_certificate.py \
  test_direct_ordered_b_interval_haar_certificate.py \
  test_direct_b_membership_sddm_lp_certificate.py \
  test_direct_b_physical_energy_lp_certificate.py
```

The first three suites total 23 tests, the boundary-normalized suite adds 11,
the fixed-boundary Hou--Zhao suite adds 15, and the reoptimized-boundary suite
adds 15.  The exact box suite adds 16, the centered multiband suite adds 13,
the cross-ratio box-dipole suite adds 13, the ET no-go suite adds 12, and the
phase-transport suite adds 9.  The pair-owned allocation and active dipole
PSD-price suites add 10 tests each.  The marginal, ordered-Gram,
negative-reserve, and ramp/common-master suites add 12, 15, 13, and 12 tests.
The direct ordered-`B` interval/Haar, membership-SDDM, and physical-energy
suites add 16, 12, and 16 tests.  The full 20-suite replay therefore has
**243 passing Route-C tests** at this
checkpoint.  Canonical payload
SHA-256 values are:

- positive-part/zero-mass:
  `c9b77974643244edc713bb0d8674a5f3e951ea727eb06b0f46d4ba83696a6747`;
- two-point-mass obstruction:
  `4c071ae8c5ec6408da75b71ea0e54c1c2fe7c3402c3241df00594af7c665363c`;
- overlapping-kernel feasibility:
  `f3950cbcb199e2c31123fc7c7b5e650c937bd971afc0e156bbd77f5bc7ae7963`;
- boundary-normalized cross kernel:
  `4ef2140b8e741975ab3ad142c4027de0b1df132871d46405732d953fc141b908`.
- Hou--Zhao cross perturbation:
  `3efa7efa0342c8312e9f30eab6122f5d83b1e074266825ba7ae52b9cd5399ea0`.
- Hou--Zhao reoptimized boundary:
  `b0095488470697d0c0e38be1e18a427fc6a6e490f2ed8f04bd02a1cb20f25b52`.
- retained covariance boxes:
  `aa1353fbeafdd5993708cecf3a4571c21c354b6bdc389608c08f4650fb34a09e`;
- centered multiband history carrier:
  `d58abe257554db107e526279e65405797687c0281abe77b4fe82d8d5ff69dc41`;
- cross-ratio box-dipole/Gothic bridge:
  `1cf424a41ee728ab6ee39af3e4941ae94e0b4b9d94606f4a6ee65d45b49e7a09`;
- ET fixed-prefix no-go:
  `f522626a23f323e8f3304b37a83abf10bcc1ce85f90a038cd032c3f0017f54ba`;
- continuum-phase transport gate:
  `d3d30f25f66c3a7f55f1881a9d7ea631b9eae2cfc2a33bf51d38a2a61226989e`.
- pair-owned allocation and birth transport:
  `25a84d6a534cb0be83d851b312579c3253268064b24b209e93a8bddee327d618`;
- active dipole coefficient-PSD price:
  `76fcc06eb5d1edcda2c1fd51c93122bdb558eb545bd90006627d42dcea107327`;
- ordered-strip marginal transport:
  `3d500b1dad4ee2501b1c0babc586c18d376782ef718c2120d6f646b7fede3739`;
- actual ordered-root/ramp master:
  `4af9e73fbfe449c05ee685399aa78bccc2979b65840e7a81d69721f9562bea5e`;
- isolated negative-potential reserve no-go:
  `b102f5345497519321b04695c4f8cde068b08367530cfef215a16dc4f86927f0`;
- fixed-carrier ramp-payment no-go:
  `cfc033c1299174bf7219a46378821444b8402cac9d7f966bab80b7f01220677b`;
- direct ordered-`B` interval/Haar bridge:
  `8f067c8e409b93058520b6e669de7eb4370e81c19b1c5abd988e1c0e68fc6ac2`;
- fixed-fixture membership-SDDM coefficient LP:
  `d2620c68c366f765a1f5c502be65dfaf258558af93b9df5f4a50464d8fd52f23`;
- physical Haar-energy LP:
  `3f406a1a6c7dfa19bf5172eadba5c5227ba175f4caf7811df6e53e5c75d3f630`.

Each committed JSON certificate has semantic/hash verification and
byte-exact deterministic rendering tests.

## Primary-source boundary

The current audit is in `research_sources/signed_offdiag_2026-08-29/`.
The later centered-multiband four-plugin delta is recorded there as
`TARGETED_MULTIBAND_PLUGIN_DELTA.md`; the narrower primary-source continuation
is `CROSS_RATIO_BOX_DIPOLE_PLUGIN_DELTA.md`; and the weighted completion
continuation is `PSD_DIAGONAL_PRICE_LITERATURE_DELTA.md`.
The ordered-root/SDDM and ramp ingredient search is
`ORDERED_GRAM_ROOT_CONE_LITERATURE_DELTA.md`.
Hou--Zhao proves finite cooperative boundary cover with diagonal direct-sum
energy and leaves “controlled cross-kernel terms” to future work.  O'Bryant
gives a positive universal upper bound for the normalized liminf, not a
positive or equal liminf value.  Goh's exact uniform-prefix entropy is
geometry-blind; its conditional theorem requires the conditional law already
to be Sidon in the entropic sense.  Táfula supplies a common nonnegative
Fourier parameter, not a signed compatible-history deficit.  Niu
arXiv:2604.25214v3 is withdrawn and excluded from theorem evidence.

For the weighted diagonal price, Lee--Seung supplies the known diagonal
majorant/edge-square mechanism, Boman--Chen--Parekh--Toledo the
factor-width-two architecture, Laurent--Poljak the elliptope, and
Bacry--Muzy plus Frerick--Müller--Thomaser the closest logarithmic
box/dipole-energy precedents.  We did not locate the complete weighted
statement in this application.  This is not a novelty claim.  The Consensus
query could not run because its monthly quota was exhausted; Exa, Firecrawl,
and SciSpace discovery was filtered against the linked primary records.

For the ordered-root continuation, Schoenberg's negative-type/root-distance
framework and modern SDDM/Laplacian decomposition and Schur-complement sources
are adjacent ingredients.  No checked source states the complete
application-specific interval-cell factorization, Wave dual contraction,
active ramp insertion, or Gothic ownership theorem.  This is only an
ingredient search with a dated qualified null; no novelty claim follows.

C079--C088 remain inside that same ingredient boundary.  No checked source
states the application-specific `M=D^tBD`, `2M=lambda`, terminal-free signed
Haar-Abel bridge, actual membership-cell correction, physical-energy payment,
and multi-epoch ownership theorem together.  No novelty inference is made.

No checked source combines signed coupling, legal every-shift payment, one
compatible infinite history, and an order-changing deficit.  This is a dated
qualified null, not an absence or novelty theorem.

## Exact next target

Do not run another unnormalized kernel-ratio search.  The boundary functional,
dual, and a strict same-kernel normalized gain are now fixed.  The next
falsifiable task is:

1. prove a finite-horizon scale-adaptive actual-cell cover on every capped
   compatible finite tower, retaining continuum phase and exact mixed-scale
   energy;
2. prove the same ledger satisfies
   `G_off-P-terminals >= epsilon_C log((J+1)/(j0+1))-K_C`; since the
   cell-length dual gives `P>=weighted W`, charge only cover excess backed by
   explicit one-for-one `2M=lambda` cancellation, with every root, shared
   endpoint, birth, past-scale, C066/active-gate, terminal, and final row
   singly owned;
3. in parallel, seek an actual difference-set payment or compatible-history
   inverse theorem that changes the asymptotic order;
4. only secondarily, broaden the exact cross-matrix/kernel search while
   retaining `delta=1`, every-shift legality, rational primal/dual
   certificates, and comparison against a genuinely competitive diagonal
   optimum rather than merely its own `H_12=0` comparator;
5. do not infer an infinite theorem from the finite bridge or LP, replace a
   negative Haar row by its positive part, or rerun the aggregate-`J`,
   zero-slack, and positive-Gothic count-baseline shortcuts closed by
   C081--C083; do not treat C084--C085 coefficient trace as physical energy,
   C087 feasibility/joint saving as payment, or the C088 sparse weights as a
   scale-independent recurrence.

P28, Question 1, Question 2, publication novelty, and every prize claim remain
open.

## Unnumbered C089--C096 checkpoint

The physical-cover branch is now narrower.  A universal actual-Haar star is
available and coefficient-mass optimal, but its ungated low-scale physical
price diverges.  The exact unequal-width Haar correlation is oriented, and
the common-cell length dual proves that no finite mixed-scale cellwise cover
can cost less than its integrated demand.  Shared-endpoint predecessor
transfer is tight at membership length two and fails at length three.

On the fixed 16-mark `a_k=k(k+100)` history, exact parametric analysis over
`128<=T<=256` yields 22 event chambers and 30 optimality chambers.  The C087
primal survives through the actual values `T=216,220`, fails at `T=221`, and
the optimal same-scale phase excess has rational lower bound
`56389/13934592>0`.  This closes only zero same-scale surplus on that finite
fixture/class.

The next falsifiable C058 target is therefore a cross-scale **surplus** LP or
signed master on a capped compatible finite tower.  It must retain the exact
mixed-scale objective, make membership length visible at every shared
endpoint, and place the matching `2M=lambda` cancellation plus all
birth/past-scale/active-gate/terminal/final rows in one singly owned ledger.
C058 remains the sole primary research bottleneck, but it is not the last
unproved lemma and no global claim is promoted.

## Unnumbered C097--C098 checkpoint

On the fixed 14-channel `T=200,S=800` instance, the exact common-cell
sum-cover optimum is `1555757/6144000`.  It has positive surplus
`517757/6144000`, yet saves `10643/1228800` relative to the separate optima.
This is the first certified finite cross-scale surplus-sharing effect in the
current route.

The same exact dual has positive reduced-cost margin on all 45 cross-scale
roots (minimum `799/4000`) and on `J4,J8,J_all`.  Hence none of those columns
causes the saving; it is realized by within-scale roots under the weaker
combined inequality.  The next C058 run must impose separate epochwise or
signed-owned inequalities and search for an active cross/current-to-past
payment while retaining exact physical costs, one-for-one cancellation, and
every singly owned boundary and terminal row.

## Superseding signed-owner and whole-stencil checkpoint

The epochwise follow-up has now been executed.  Its scope must be read in the
following order.

1. The fixed 14-channel nonnegative epoch-owner model and its canonical signed
   coordinate-row variant both return the separate optimum and exclude every
   cross root.
2. The fixed 26-channel, four-owner model again has full optimum equal to its
   no-cross optimum; all 676 cross dual margins are strict.  One owner is
   inactive, so this is not a universal four-owner theorem.
3. On the fixed 52-coordinate model, graph-root cross-epoch coupling is
   necessary in the graph cone, and a rational zero-row-sum PSD witness has
   `P<2D`.  Under the frozen positive-pair C067 terminal allocation, however,
   an exact projected PSD dual proves `P>2G_off^max` for the entire fixed cone.
   This closes that convention only.

The complete signed four-corner stencil is a different convention.  Keeping
each primitive

`alpha_ij [R(M)+R(D)-R(M+u)-R(M+v)]`

whole makes its `T=100` lower endpoint and `T=1600` terminal vanish on the
displayed fixture.  Summing all 24 primitives gives

`D_4=9/128`, `D_8=1349/10240`, and `D=2069/10240`.

The corresponding exact epoch-block cross-width PSD witness has zero epoch
cross block, 608 feasible aggregate owner rows, minimum positive slack
`41304919/12500000000000`, and

`P=3900000000091/10000000000000`,

`Phi=141015624909/10000000000000>0`.

This is the first exact positive aggregate whole-stencil fixture in the
current route.  It does not create directed current-to-past flow: all saving
occurs inside the two epoch blocks through cross-width terms.  An exact
380-row, 48-pivot dual for the four independent width blocks proves

`P>=843669938599/2048000000000`

and exceeds `2D` by `16069938599/2048000000000`.  Thus cross-width coupling is
essential in this fixed smaller cone.

The Fejér ratio gate is exact.  If `r=w_8/w_4`, the weighted fixture is
positive exactly for

`r>581005931206/1286084055751`.

The worst guaranteed value `r=9/16` works for every `m>=4`; `m=3` gives
`r=4/9` and negative `Phi`.  The final `m=3,2,1` boundary remains open.

### Primitive and phase RED gates

The aggregate PSD inequalities must not be renamed primitivewise cover.  The
smallest exact countercell currently recorded is owner `n4,T200`, cell
`[709,725)`: primitive `(5,7)` contributes `1/3200`, primitive `(4,7)`
contributes `-9/25600`, and their aggregate row is `-1/25600`.  The old PSD
owner share is `-49528467/1690000000000`; it covers the aggregate with slack
`8243579/845000000000` but misses the positive primitive by
`577653467/1690000000000`.  The fixed-old-`X` left-edge cascade supplies an
additional exact obstruction to that particular directed orientation.  It
does not prove a joint reoptimized primitive-flow SDP no-go.

At the adjacent rational phase midpoint `t=4835/48`, a separate 52-coordinate
Gram factor satisfies all 616 aggregate owner-cell rows and gives

`P=951134501701/3000000000000`,

`2D-P=246690436855133/2901000000000000>0`.

This verifies one neighboring point, not an open phase chamber.  Continuum
phase, primitive ownership, the complete birth/final/terminal ledger, a
compatible infinite history, and the small-`m` closure are still missing.
The newest results are registered as C107--C110 with exactly the fixed-scope
boundaries stated above.  C058 remains
the sole primary bottleneck and the problem remains unresolved.

### Superseding C111--C114 checkpoint

The complete fixed-history phase is now exact: 108 chambers and 109 endpoints
cover every `t in [100,200]`, every Fejér ratio in `[9/16,1]`, with
`t Phi>=255996752651/2560000000000`.  Finite aggregate change of basis is
formally legal, so primitivewise positivity is no longer the relevant gate.
The final three Fejér blocks are asymptotically excisable at `o(1)` cost after
a legal core exists.  Conversely, an exact powers-of-two Golomb dual gives
strictly negative margin in the same epoch-block PSD cone; because that ruler
is not eventual fixed-`C` critical, it rules out only geometry-free
generalization.

The full proof boundary and next history-potential inequality are recorded in
`core_workspace/CONTINUATION_2026-08-30_C058_FULL_PHASE_AND_HISTORY_DICHOTOMY.md`.
C058 and every global claim remain unresolved.
