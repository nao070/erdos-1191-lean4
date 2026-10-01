# Proof Obligations — Erdős Problem #1191

> **RESET SUPERSESSION — 2026-08-29.** This is the historical Wave 0--19
> obligation ledger, not the current work order. Use
> `../UPDATED_START_HERE.md`, `../QUANTIFIER_AND_REDUCTION_AUDIT.md`, and
> `../ROUTE_PORTFOLIO.md` for the reconciled quantifiers and current program.
> P17/P18 and the saturated P26/P27/bare-`Gmix` upper targets must not be
> revived as smaller intermediate lemmas.

**Updated:** 2026-08-30 unnumbered proof-reset continuation, after Wave 19  
**Current global status:** `UNRESOLVED_AT_HARD_LIMIT`

## P0. Independent proof audit of endpoint reconstruction

- Reprove `C_N(r+1)-C_N(r)=delta_N(r)` with the exact half-open block convention.
- Check the cyclic bad-offset arc `(a,b]` for wrap and nonwrap cases.
- Verify `sum_r delta_N(r)=0` and the reconstruction constant.
- Verify the variance equality under `E_N=|P_N|-C_N`.
- Verify the unnormalized Fourier transform gives the factor `1/N^2`.
- Verify the cycle decomposition equivalence for a directed multigraph.
- Status: **COMPLETE for the finite identity.**  A separate proof audit checked
  the half-open convention, wrap cases, sign, reconstruction, cycle
  decomposition, and the unnormalised-Fourier factor `1/N^2`.  “Eulerian” now
  explicitly means componentwise balanced; it does not require connectivity.

## P1. Diameter-regime algebra and scope

- Reprove the gap-moment formula.
- Reprove `delta_N(a_i)=m+1-2i` when `diam(A)<N`.
- Recompute `sum_i(m+1-2i)^2=m(m^2-1)/3`.
- Recompute the mandatory-level centred sum.
- State correctly that sharpness is over arbitrary finite sets; the equality family is non-Sidon for `m>=3`.
- Status: **COMPLETE for the stated unrestricted theorem.**  The mandatory
  entries are an indexed multiset (symmetric values may coincide), and equality
  requires every extra entry to equal `(m^2-1)/6`.  Sidon-class sharpness
  remains open.

## P2. Novelty audit

- Search for the endpoint-reconstruction identity under circular discrepancy, graph divergence, discrete potential theory, inverse Laplacians, electrical networks, arc coverage processes, and interval stabbing.
- Search for the homometric separation phenomenon in Golomb-ruler and phase-retrieval literature.
- Search for all-offset block-energy variance in prior Sidon proofs.
- Status: expanded public search negative but **not conclusive**.  Firecrawl,
  Exa, SciSpace, specialist-site indexes, exact-formula queries, and primary
  arXiv pages were checked.  Bekir--Golomb supplies classical homometric-ruler
  context, while the cycle-resistance identity is standard discrete potential
  theory; no source found the complete Sidon multiscale formulation.  Direct
  MathSciNet/zbMATH coverage and expert review remain obligations.
  Wave 6 added a bounded primary-source check of disjoint difference packings,
  one-point extension shadows, and Singer/finite-field nesting.  It found no
  checked compatible critical all-prefix integer tower or endpoint
  band-renewal theorem.  Consensus was unavailable after its 30/30 monthly
  quota; this remains a qualified null, not an absence or novelty theorem.

## P3. Exact multiscale functional

Produce an explicit functional `F(A)` involving endpoint variance across prefixes/moduli/offsets with:

1. an exact finite expansion;
2. transparent boundary terms;
3. nonnegative or controllable interaction kernel;
4. a stated scale schedule and weights.

Status: **COMPLETE for the exact finite expansion; open for the needed bound.**
With `m_j=2^j`, `N_j=D_{m_j}+1`, and `w_j=m_j^-3`, the exact ordered pair-pair
kernel and both prefix-birth and short-pair indicators are now written in
`endpoint_variance/MULTISCALE_ARC_KERNEL_AND_OBSTRUCTIONS_2026-08-28.md`.
Wave 3 adds the sign-free gap expansion
`V_m=N_m^-2 sum_{k<l}h_kh_l(l-k)^2(m-k-l)^2` and its exact birth-kernel
exchange for `G_J=sum_j V_{m_j}/m_j^4`; see
`endpoint_variance/SIDON_BLOCK_VARIANCE_AND_POSITIVE_MULTISCALE_2026-08-28.md`.
The normalized gap measures also satisfy the exact vector recursion
`M_(2m)=B M_m B^T+Q_m`, `Q_m>=0`, for
`M_m=N_m Cov_(nu_m)(u(1-u),u)`; see
`endpoint_variance/GAP_MEASURE_DYNAMICS_AND_TWO_STEP_LOWER_BOUND_2026-08-28.md`.
Its full iteration transports every PSD innovation by an explicit power of
`B`.  Among all `r>=2` co-Lipschitz scalar aging consequences, `r=2` gives the
largest asymptotic lower coefficient, so deeper scalar aging is saturated.
The finite-horizon adjoint recursion gives the exact companion identity
`sum G_j=<H_1,R_1>+sum <H_(j+1),Q_j/N_(j+1)>`; see
`endpoint_variance/ADJOINT_LYAPUNOV_INNOVATION_BUDGET_AND_PSD_NO_GO_2026-08-28.md`.

## P4. Universal Sidon upper budget

Prove a nontrivial upper bound for the functional from P3 using global uniqueness of positive differences. The bound must control repeated counting of the same pair, difference, or endpoint quadruple across scales.

A trivial `O(m^4)` pointwise range bound is insufficient.

Status: **central missing theorem.**  Diagonal absolute summability is proved,
but the signed off-diagonal budget is not.  Complementary cycles, a genuine
three-edge Sidon cycle, covariance sign reversal under modulus doubling, and
homometric off-diagonal signs refute positivity and monotonicity shortcuts.
An unconditional `o(log J)` budget is also refuted by an explicit sparse
infinite Sidon construction; the critical envelope must be used essentially.
For the new positive functional, the unconditional shell grouping gives only
`G_J <= (4/3) log N_J = O(J)`.  The exact required replacement is
`G_J=o(log J)` under the critical envelope.  A three-rank lifted Sidon family
with `V_m/m^4>=1/2304` shows that no uniform pointwise `o(1)` estimate follows
from an isolated Sidon ruler plus `N=O(m^2)`.  It does not exclude a
bounded-depth estimate with genuine compatible-prefix hypotheses.
However, the later Erdős--Turán fixed-depth theorem shows that any *uniform
finite-window* estimate based only on those local prefixes, Sidon uniqueness,
and a common critical envelope is also false: its innovation tends to `1/360`
and its signed birth shell to `19/3840`.  A surviving bounded-depth formula
must use an additional global embeddability hypothesis or participate in an
unbounded-history amortization.
At the `m^-4` weight, each fixed ordered interaction has absolute future tail
at most `4/(15m_s^4)`, so the crude total loss is `O(1)` per birth shell.  The
open task is to extract enough signed/structural cancellation to make the
sum `o(log J)`; the matrix innovation identity alone does not supply this.
Indeed an explicit abstract critical orbit with arbitrary PSD innovations has
`G_j=1/72` at every scale.  Its innovations are not claimed to arise from a
Golomb ruler, so it rules out only PSD-recursion-only arguments and sharpens
the target to the arithmetic structure of actual birth shells.

The reset Route-C audit adds a complementary exact closure.  For any finite
joint kernel, replacing represented Sidon differences by all positive shifts
has the legal bound

`E_H<=|A|C_H(0)+2 sum_(d>=1) C_H(d)_+`

`=m^T H m+(|A|-1)C_H(0)+2 sum_(d>=1)(-C_H(d))_+`.

Hence negative common-shift correlation has an exact mandatory cost.  If the
channels are probability kernels, `H` is PSD, and `H 1=0`, pointwise
nonnegative off-shift correlation forces the joint energy to vanish.
Distinct point-mass channels likewise cannot beat their same-diagonal
positive-part bound.  See
`../route_probes/ROUTE_C_POSITIVE_PART_ZERO_MASS_NO_GO.md`.  This closes
those method classes only.

The follow-up overlapping-kernel theorem gives a positive finite feasibility
result.  For `H_b=[[1,b],[b,1]]`, the exact shift gate is
`b>=-min_(B_d>0) A_d/B_d`; every feasible `b<0` strictly improves the pure
upper-energy expression over `b=0`.  The minimal half-grid witness has ratio
`4/7`.  But a rational family makes that ratio tend to zero while total
correlation mass, `C_b(0)`, and a Gram eigenvalue all collapse.  Thus unit
diagonal is not a meaningful normalization.  See
`../route_probes/ROUTE_C_OVERLAPPING_KERNEL_FEASIBILITY.md`.

The boundary-cover normalization has subsequently been derived exactly.  For
`H` positive definite, the generalized master inequality is

`k^2<=(beta N+b_H T-beta)(s+a_H(k-1)/T)`,

where `beta=gamma^T H^-1 gamma`, `s=1^T H1`, and the boundary QP uses
`I tensor H^-1`.  Its leading factor `delta=beta s` is at least one; equality
holds exactly at `gamma=H1/s` when this vector is nonnegative.  The corrected
secondary coefficient is `delta^(1/4)sqrt(a_H b_H)`.  An exact `delta=1`
two-kernel KKT certificate strictly improves the same fixed kernels with
`H_12=0` by a coefficient factor `0.9985054901...`.  However, a different
diagonal candidate wins the same bounded grid by about `1.085%` at coefficient
level, and the cross hit does not improve the published Hou--Zhao constant.
See `../route_probes/ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md`.

A separate row-sum-zero perturbation of the official eight-kernel certificate
does improve that finite constant.  With the exact integer two-cycle matrix
and `epsilon=1/6250`, the old cover remains unchanged, strict diagonal
dominance proves `H>0`, every combined shift is positive, and the certified
coefficient becomes `0.9434922260277725...`, versus the published
`0.9434925907135450...`.  See
`../route_probes/ROUTE_C_HOU_ZHAO_CROSS_PERTURBATION.md`.  This closes the
finite feasibility question “can controlled cross terms improve a competitive
diagonal certificate?” in the affirmative.  It does not change the
`N^(1/4)` order or supply a compatible infinite history.

The boundary QP for that pinned direction has now also been reoptimized
exactly.  With the same hash-pinned kernels, mixing weights, and integer
direction but `epsilon=1/462`, a 126-active-row rational KKT certificate gives

`F(N)<=sqrt(N)+0.94348767 N^(1/4)+O(1)`.

The exact coefficient is `0.9434876661938243...`; positive definiteness and
every discrete/lifted correlation gate remain strict.  This is global only in
the boundary variable for the fixed outer data.  It proves no optimum over
epsilon, directions, kernels, or mixing weights and supplies no current-best,
novelty, compatible-history, Q1/Q2, or prize conclusion.  See
`../route_probes/ROUTE_C_HOU_ZHAO_TWO_CYCLE_EPSILON_EXPLORATION.md`.

Accordingly, the sharpened P4 input is now a **published-competitive,
fixed-outer-data boundary-optimized** cross construction **together with** an order-changing
compatible-history theorem, actual difference-set payment, or a
geometry-sensitive compatible-history term.  Even the competitive finite
coefficient gain alone does not change the `O(log J)` obstruction.

This last limitation is now a theorem for the named coefficient-only method
class.  For dyadic `2^j`-mark prefixes, span counting gives
`N_j>=1+binom(2^j,2)`.  Therefore any uniform finite remainder
`O(N^(1/2-delta))`, `delta>0`, becomes `O(2^(-2delta j))` after leading
normalization and has uniformly bounded Fejer sum.  It cannot pay the
certified `Omega(log J)` new-birth floor.

The precise surviving Route-C carrier is instead the retained square
`V_j=||1_A*K_T-1_A*K_(2T)||_2^2`.  With
`H_theta=D-theta(1,-1)(1,-1)^T`, its exact boundary-adjusted gain is
`G_j=theta B_D V_j-kappa Q_j U_D+kappa theta Q_j V_j`.  A sufficient next
obligation must fix one nonanticipating rule `Pi` and explicit
`eta_C>0,K_C<infinity`, retain all terminal/boundary costs, and prove
`sum omega G_j(Pi)/N_j>=eta_C log J-K_C` on every stated finite compatible
critical-cap chain.  This is open; see
`../route_probes/ROUTE_C_TWO_SCALE_BRIDGE_AND_COEFFICIENT_NO_GO.md`.

Wave 6 now supplies an exact global arithmetic ledger.  Multi-epoch
newborn-shell and old--new anti-diagonal families obey inclusive integer
capacity.  For `tau_(m,k)=D_m^-+D_m^++k max(mu_m^-,mu_m^+)`, layer-cake
integration gives `sum_(tau<=X) k/tau<=1+log X` and the uniform
`(1+epsilon)/epsilon` bound at exponent `1+epsilon`.  These theorems extend
to all epochs of one infinite sequence by monotone convergence, but the
endpoint remains `O(log X)`, exactly the wrong order for P4.  The missing step
is therefore an old-history no-renewal improvement, not another local capacity
estimate.

## P5. Critical-envelope lower budget

Under `a_m<=C m^2 log m` for all sufficiently large `m`, prove a lower bound for the same P3 functional that exceeds P4 by an unbounded factor.

Requirements:

- constants uniform in depth;
- no independent choice of offsets that destroys cross-scale consistency;
- boundary/truncation errors lower order;
- conclusion divergent, not a better fixed constant.

Status: the lower accumulation for the explicit functional is **complete**:
under the critical envelope,
`F_J >= (1+o(1)) log(J)/(360 C log 2)`.  The precise remaining obligation is a
density-compatible signed upper budget `F_J=o(log J)`; no such estimate is
proved.
Wave 3 strengthens this: for `m=8q>=16`,
`V_m>=9m^6/(16,777,216N_m)`, hence under the same critical envelope
`G_J>=9(33,554,432 C log 2)^-1 sum_j 1/j=Omega_C(log J)`.
The optimized two-step distinct-gap theorem strengthens the pointwise bound to
`V_M/M^4 >= (9M^2-256)/(1,048,576N_M)`.  Under
`N_M<=2CM^2 log M`, its dyadic sum has leading coefficient
`9/(2,097,152 C log 2)` in front of `log J`, sixteen times the direct
eight-block coefficient.

## P6. Anti-Eulerian stability

Quantify the implication of small `H^{-1}` imbalance:

- approximate flow decomposition into directed cycles;
- edge deletion or transport distance to Eulerianity;
- control of cycle lengths and modulus divisibility;
- behavior under changing or nested moduli.

Status: exact zero characterization known and audited; stability open.  The
Sidon example `{0,3,7,12}` at `N=6` gives a genuine three-edge zero cycle, so
distinct edge lengths alone do not yield anti-Eulerianity.  No claim that
small variance puts “most edges” in cycles is allowed without a normalized
stability theorem.

## P7. Sidon-specific gap optimization

For positive gap vectors with distinct contiguous sums, bound the exact diameter-regime variance from below. Determine whether the general mandatory-level order/constant can be improved under the Golomb condition.

Status: **exact finite computation complete in the certified range; asymptotic
problem open.**  All normalized rulers with `2<=m<=7`, `m-1<=D<=25` were
enumerated at `N=D+1,D+2,D+3`: 245,505 candidates, 9,013 oriented rulers, and
27,039 exact variances.  A separate composition/direct-block oracle made 294
checks with zero mismatches.  The strict finite gap above the unrestricted
bound for `3<=m<=7` does not imply a uniform asymptotic factor.

## P8. Martingale/entropy bridge

Construct nested partitions and prove an identity or inequality linking endpoint variance to martingale square functions or entropy increments. Establish a total budget controlled by unique differences.

Status: a fixed-containing-modulus second-difference identity is complete:
`C_m-2C_{m-1}+C_{m-2}=(m-1)1_(a_{m-1},a_m]`.  It reconstructs the known gap
profile and supplies no Sidon-specific total budget, so a useful martingale
bridge with shorter/nested moduli remains open.
Wave 3 also proves the exact cover identity
`q^2 V_{qN}=V_N(R_N)+I_{N,q}` with a nonnegative fibre innovation.  It gives a
true martingale for a frozen edge multiset, but not for complete prefix loads.
The Sidon family `{0,1,qN}` has positive coarse variance and zero fine
variance; newborn residual arcs can have quadratic covariance.  Any surviving
filtration must account for births in extra coordinates and prove a summable
global trace bound.
The fully diagonal version is now **REFUTED**: for `P=binom(m,2)` distinct
edge differences and arbitrary positive coordinate weights,
`(sum 1/w_p)(sum w_p d_p(N-d_p)/N^2) >= P^3/(9N)`.  Under the critical
envelope this already costs `Omega(1/log m)` per dyadic scale.  Any remaining
filtration must retain structured off-diagonal covariance blocks.

## P8a. Long-range gap-measure rigidity

Let
`nu_j=N_j^-1 sum_{k<m_j} h_k delta_{k/m_j}`.  Prove under the critical
envelope a restriction across an unbounded number of nested prefixes strong
enough to force
`sum_{j<=J} Var_{nu_j}(u(1-u))=o(log J)`.

Obligations:

- use genuine compatible-prefix information, not only an isolated ruler;
  fixed-depth local compatibility alone is insufficient; a bounded-depth
  inequality remains eligible only if its hypotheses are verified along one
  global critical sequence and its charges telescope or amortize;
- survive the three-rank lifted constant-shell family;
- quantify exactly where distinct contiguous gap sums enter;
- state a summable charge or injection with multiplicities audited.

Status: **open supporting route; superseded as highest priority by P13.**  The exact positive update
`M_(2m)=B M_m B^T+Q_m` supplies a two-coordinate state and PSD innovations,
and the optimized two-step theorem supplies the stronger lower constant.
Scalar aging can move in either direction, and no upper budget for the
accumulated innovations is known.  The fixed-interaction absolute charge is
`O(1)` per shell, not yet `o(1/j)` on average.
Equivalently, by the exact adjoint identity, prove
`sum_(j<=J)<H_(j+1),Q_j/N_(j+1)>=o(log J)` for the actual innovation formula.
Generic uniformly controlled fixed/scale-dependent PSD-linear potentials,
trace, determinant, and eigenbasis arguments are exhausted unless they
incorporate integer birth-shell or distinct-contiguous-sum information.
Formal forward telescopes with exploding coefficients exist but have an
unusable terminal cost.

Wave 4 closes a larger local class.  For terminal mark count `M=2^J`, the
last `floor(log_2 J)-1` prefixes of a finite Erdős--Turán ruler share the same
`C=1` critical envelope while their total gap variance is
`(log J)/(180 log 2)+O(1)` and their adjacent innovations approach `1/360`.
Thus even a window whose depth tends to infinity like `log J` cannot prove the
budget from its local data alone.  The family depends on `J`, so a theorem
using one infinite globally critical history remains eligible.

An exact cross-block theorem now gives a genuine such-history restriction:
if `M=qm`, the old prefix satisfies `N_m<=K m^2 log m`, and
`epsilon_M=max_r|N_r/N_M-r/M|`, then
`epsilon_M>=1/q-Km^2 log(m)/(binom(q,2)m^2+1)`.  Hence a hypothetical global
critical sequence has `epsilon_M=Omega(1/log M)` at every large dyadic `M`.
This is a discrepancy lower bound and has not been converted into an upper
bound for `Var_nu(f)` or the adjoint innovation sum.

## P8c. Global arithmetic band-renewal self-improvement

For one infinite normalized Golomb ruler satisfying
`N_n<=C n^2 log(2n)` eventually, use all cross-epoch contiguous-sum
uniqueness to prove that the Wave 6 cutoffs `R_m(T)` cannot renew through
unboundedly many fresh numerical bands without paying an old-history capacity
charge.  The required consequence is

`sum_(j<=J) <H,Q_j/N_(2m_j)> = o(log J)`.

Obligations:

- start from the exact multi-epoch integer ledger and its endpoint
  `sum_(tau<=X) k/tau<=1+log X`; a second `O(log)` bound is insufficient;
- make the charge depend on the one globally compatible sequence, since every
  terminal-scale-dependent recent window can evade it;
- use the exact chord inheritance and signed reset from Wave 5, but retain
  full Sidon arithmetic rather than only profiles, reset counts, or PSD data;
- do not assume Hall-pressure decay beyond the universal `Lambda<=1`: one
  exactly audited 64-mark C=1 ruler violates the proposed
  `1/(4 sqrt(n))` law at three consecutive transitions;
- survive the exactly audited 128-mark finite witness; finite extendibility is
  not a contradiction;
- survive the sixteen-mark ruler with three strongly negative, nearly uniform
  reset cycles and positive innovation;
- do not charge innovation by universal local one-point forbidden-shadow
  density: a residue lift confines that shadow to four residue classes and
  yields growing compatible finite windows with total shadow density `o(1)`
  and divergent innovation;
- distinguish the exact finite and infinite endpoint statements from any
  optimality, exhaustive-search, or asymptotic construction claim.

Wave 6 proves the exact `O(log)` capacity endpoint and closes the obvious
decay, short-cycle, and local-shadow strengthenings.  It does not prove the
old-history self-improvement.

Status: **open Wave 6 precursor; superseded as highest priority by P13.**

## P8b. Net-shell H6 and fixed-modulus monotonicity

The finite candidate H6 says each net birth shell in the tested decomposition
is nonnegative.  It survived the stated certified ranges but remains
unproved.  The proposed sufficient statement
`Var_N C(A_{2r}) >= Var_N C(A_r)` at one containing modulus is **REFUTED**.
The globally minimal Sidon counterexample for doubled-prefix comparisons is
`N=40, A_4=(0,20,21,39)`, with `1/4 -> 99/400`; an infinite counterfamily
exists for every `N>=40`.

Status: fixed-modulus route **REFUTED**; H6 itself remains only a finite
observation and is not a priority because it would not prove the needed upper
budget even if true.

## P9. Finite Fourier-uniformity applicability

Before using Ortega–Prendiville or Ding:

- state the exact finite theorem and error term;
- prove the prefix/window is within the required extremal deficit;
- track modulus dependence;
- show enough windows/scales qualify;
- avoid circular density assumptions.

Status: conditional route only.

## P10. Q2 compatible construction

To resolve Question 2, prove existence of arbitrary-depth normalized rulers with a fixed envelope `b_k<=Ck^2(log(2k))^d` for every prefix coordinate.

Obligations:

- complete cross-scale collision classification;
- uniform constants independent of depth;
- compactness argument stated precisely;
- no reliance on independently dense finite blocks;
- if probabilistic, positive probability with all prefix constraints simultaneously.

Status: open.

## P11. Legacy computation recovery

Obtain and hash the missing older `computation/` source, raw output, manifests, and finite-profile solvers before treating their numerical claims as reproducible.

Status: artifacts missing.

## P12. Solution gate

Before any `RESOLVED_*` status:

- self-contained theorem and proof;
- hostile line-by-line review;
- exact current literature search using the final theorem statement;
- no finite computation in an infinite inference;
- uniform constants and quantifiers checked;
- all external dependencies named and verified;
- reproducible files and manifests generated.

Status: not reached.  The strongest surviving step is still conditional, so
the only permitted global label is `UNRESOLVED_AT_HARD_LIMIT`.

## P13. Infinite-survival-conditioned debt repayment and innovation budget

Let `P` be a finite Golomb prefix and `surv_C(P)` the height of its extension
tree under the eventual cap `N_r<=floor(2Cr^2 log r)`.  Finite branching and
König's lemma prove that `surv_C(P)=infinity` exactly when `P` lies on one
infinite eventual-`C`-critical Golomb ruler.

For every dyadic epoch in such an infinite branch, use the complete Wave 7
birth families.  The proved wedge ledger gives
`sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)`, but changing E–T windows refute every
fixed-constant affine domination of adjoint innovation by this potential
alone.

Required new theorem:

- condition the charge on `surv_C(A_(2m))=infinity`, not finite-window
  compatibility;
- orient each active epoch by the cheap-child-half lemma;
- separate genuinely new adjacent differences from nested old-half overlap
  and already counted boundary atoms;
- prove that accumulated old-cheap overlap debt is repaid by unused non-
  adjacent differences below the threshold or by equal integer-capacity
  slack;
- link this repayment quantitatively to both the newborn-shell covariance and
  rank-one mixture terms of the actual `Q_m`;
- deduce `sum_(j<=J) <H,Q_(m_j)/N_(2m_j)> = o(log J)`.

Mandatory adversarial checks:

- RH and HT are false and may not be used;
- EST is a theorem only through eight marks and finite evidence thereafter;
- on the 128-mark fixture at `T=1198199/32`, adjacent matching leaves debt 63;
- the 512-mark and growing E–T windows defeat `W_2`-only affine bounds;
- O'Bryant Lemma 9's scalar worst guarantee forces an `Omega(n^4)` first-new-
  prefix jump and cannot be the black-box proof;
- no finite survival computation may be promoted to infinite survival.

Wave 8 resolves the adjacent-overlap part more sharply than this formulation.
The actual-newborn/old-clear dichotomy leaves at most one internal-adjacent
family outstanding on a fixed history, and the negative adjacent `kappa`
atoms have a finite total under the critical cap.  Exact atom expansion shows
that the remaining shell debt is the proper non-adjacent boundary fan, while
the rank-one term is an independent Abel fan.  Raw certified/global/latest
non-adjacent cardinality variants are refuted by exact finite `C=1` witnesses.

Most importantly, the exact pair telescope proves that all future negative
old-pair terms can reduce the positive birth budget by at most a factor two.
Thus cancellation-based debt repayment cannot supply an unbounded gain, and
the surviving obligation is P15.

Status: **adjacent debt resolved; raw local repayment and cancellation routes
refuted; superseded as highest priority by P15.**

## P14. Q2 finite feasibility plus König

For fixed `C,d`, prove that for every `M` there exists a normalized
`M`-mark Golomb ruler with `a_k<=Ck^2(log(2k))^d` for every `k<=M`.
The finitely branching prefix tree then has an infinite branch.  Witnesses at
different depths need not be chosen compatibly in advance, but they must use
the same coordinate caps.  O'Bryant's worst-guarantee separated gluing is
insufficient; all mixed old--new and new--new collisions require a uniform
construction or whole-prefix existence proof.

Status: secondary open route.

## P15. Positive birth-budget Carleson theorem on one infinite branch

For dyadic `m`, let

`B_H(J)=sum_(m<=2^J) N_(2m)^(-2)
sum_(0<=i<j<2m, j>=m) h_i h_j Phi_(ij)`,

where `Phi_(ij)=<H,K_(ij)^(2m)>`.  Each endpoint pair occurs at exactly one
birth epoch.  Wave 8 proves the exact global comparison

`B_H(J)/2 <= sum_(j<=J)<H,Q_(2^j)/N_(2^(j+1))> <= B_H(J)`.

Required theorem:

- assume one infinite Golomb ruler satisfies
  `N_n<=C n^2 log(2n)` eventually;
- prove `B_H(J)=o(log J)`;
- use all-contiguous-sum uniqueness with the exact product/kernel weights,
  not only the count of unused integer differences;
- give a bounded-overlap charge across both magnitude scale and rank-lag
  scale on the same infinite branch;
- explicitly include the rank-one births and the non-adjacent shell bulk;
- allow only a finite initial error, not an unproved local factor-one bound.

Mandatory adversarial checks:

- `(0,1,4,6)` refutes the literal local global-density inequality;
- `(0,4,5,7,78,86,166,199)` refutes latest-shell density at an
  old-clear/new-unpaid `C=1` event;
- scaled `(0,8,24,56,58,314,318,319)` refutes any version dropping the
  critical hypothesis;
- the unscaled power-gap ruler requires a positive non-adjacent bulk atom to
  repay its shell boundary fan;
- `(0,D,3D,3D+1)` refutes constant comparison of the rank-one term with
  newborn covariance;
- the 682-mark reconstructed fixture is finite positive evidence only;
- infinite survival may be a single ray, so no branching entropy or Kraft
  slack may be assumed.

Equivalent exact-positive form: after finite-horizon adjointing, each born
pair contributes its positive future `E`-energy tail.  A proof may control
that tail instead of `B_H`, but it must obtain the same sublogarithmic result.

### Wave 9 exact reformulation

Define

`nu_n=N_n^(-1) sum_(i<n) h_i delta_(i/n)` and
`V_n=Var_(nu_n)(u)`.  Wave 9 proves

`(4/49) sum_(k=1)^(J+1) V_(2^k)
 <= B_H(J) <=
 (36/35) sum_(k=1)^(J+1) V_(2^k)`.

Thus P15 is quantitatively equivalent to
`sum_(k<=J) Var_(nu_(2^k))(u)=o(log J)`.  This scalar form includes the shell
and rank-one births together.  It does not prove the required upper.  In fact,
distinct genuine adjacent gaps give `V_n>=n^2/(512N_n)` for `n>=8`, so the
critical cap forces
`B_H(J)>=(6272 C log 2)^(-1) log J+O_C(1)`.  The contradiction can therefore
come only from uniqueness of non-adjacent contiguous sums on the same infinite
branch.

Wave 9 also proves the lossless core reduction

`B_m<=B_m^core(theta,eta)+(18/35)theta^2+(36/35)eta`.

With `theta_j^2=eta_j=1/(j log j)`, all non-core terms total
`O(log log J)`.  The surviving core has long rank distance and two large
endpoint gaps.  Its four-parameter `(R,X,Y,Z)` tiles obey exact endpoint-band,
difference-capacity, and interval-overlap bounds, but scaled Erdős--Turán
windows show that local numerical sparsity cannot make the core vanish.

The valid hereditary rank-lag constraint

`M_E(M_E+1)/2 <= sum_(m in E) N_(2m)q_m(q_m+1)/2`,
`M_E=sum_(m in E)m q_m`,

controls linear difference lengths only.  A weighted cross-ratio potential
majorizes the genuine non-adjacent product and has an exact birth recursion,
but its dyadic birth sum is again comparable to a positive sum of state
potentials.  Its primitive Abel bound uses
`delta_n^circ=gcd(h_2,...,h_(n-2))` and is only `O(log log n)` under the
critical cap.

Additional mandatory adversarial checks:

- pointwise `Delta B_(2m)<=Delta B_m` fails in 128 of the 1,146 exhausted
  eight-mark all-prefix-`C=1` rulers with terminal at most 40;
- the literal harmonic schedule fails in all 1,146;
- static one-atom and occupancy-at-most-rank-band cells fail at `(0,1,4,6)`;
- the macroscopic long-rank/large-magnitude quadrant exceeds `3/5` of the
  terminal birth increment on both 512-mark finite calibrators;
- a changing scaled Erdős--Turán family has birth charge at least `1/2352`
  and retained cross-ratio potential at least `1/4096` while numerical
  difference density tends to zero;
- no changing finite family may be promoted to `surv_C=infinity`.

Wave 10 outcome: arbitrary-weight laminar packing, hereditary log-product
packing, and a fixed-location kernel tail are now proved.  The exact global
Abel bulk floor has leading coefficient `7/4`, so plain distinct-integer
rearrangement leaves a leading quarter deficit.  Existing W9-RLP rows have
zero tile-variable coefficients after the moduli are fixed, so simple LP
concatenation also fails.  P16 records the refined missing coupling.

Wave 11 superseding outcome: the triangular interval floor pays that entire
leading quarter and gives the exact three-channel identity.  P15 remains
open, and its current exact Route A mechanism is P17.

Status: **central theorem still open; exact next mechanism refined by P17.**

## P16. Survival-conditioned Abel repayment or tensor-box theorem

Let `E_J={4,8,...,2^J}`.  For each dyadic `m`, let `I_m` be the negative
non-full Abel bulk and let `beta_(m,p,q)` be its exact coefficient.  Define

`F_E=sum_r beta_r^down log r`

from the global coefficient rearrangement and let

`P_J=sum_(m in E_J)sum_((p,q) in I_m) beta_(m,p,q)log D_(p,q)-F_(E_J)`

be the actual interval-consistency premium over the rank-only floor.  Let
`Q_J` be the exact positive-fan log mass,
`T_J=sum_(m in E_J)theta_m log a_(2m-1)`, and
`S_J=2T_J-Q_J>=0`.  The proved Wave 10 law is

`F_E=(7/4)sum_(m in E)log m+O(|E|)`.

### Route A obligation — historical Wave 10 formulation

This paragraph is preserved to show the exact Wave 10 state.  Wave 11 has
already discharged its leading-quarter/fan-allocation subproblem by the
termwise `K^len` floor.  The current obligation is P17 below; do not read the
remaining “must” statements here as additional current requirements.

The exact Abel identity is

`sum_(m in E_J)Y_m=U_(E_J)-P_J-S_J`,

where `U_E=sum_(m in E)theta_m log a_(2m-1)-F_E`.  On one fixed infinite
eventual-`C`-critical Golomb branch, it is sufficient to prove that there is
`epsilon_J>=0`, `epsilon_J=o(log J)`, such that

`P_J+S_J >= U_(E_J)-epsilon_J`.

Equivalently, prove
`0<=U_(E_J)-P_J-S_J<=epsilon_J`.  The stronger bulk-only inequality
`P_J>=U_(E_J)-epsilon_J` also suffices, but is not known to be necessary.
If the premium is assigned to the lower-shell fan `q=m-1`, the proof must
first define and justify a global allocation because `F_E` is sorted across
all coefficient classes and epochs and has no canonical fanwise split.  The
argument must cancel both the leading quarter and secondary accumulated
slack, and must use more than global integer distinctness.

### Route B obligation

Split the tile objective into

- endpoint-limited weight `R^2XY`, to be encoded on a full tri-tree;
- difference-limited weight `R^2Z^2`, to be encoded on a full bi-tree.

Construct a positive measure and test function for which the exact P15 core
is dominated by the Hardy embedding energy, keep sparsity in the arbitrary
measure rather than pruning the tensor weight, and prove from contiguous-sum
uniqueness plus `surv_C=infinity` that the one-box constants vanish with
enough summability to give `o(log J)`.

Mandatory checks:

- W9-RLP has zero columns in the current fixed-modulus tile LP; a valid new
  row must contain endpoint-product or Abel variables with nonzero
  coefficients;
- the global `7/4` spectrum law already includes simultaneous sorting over
  arbitrary finite dyadic epoch sets;
- the fixed-position kernel tail is `O(4^(-K))`, but moving-frontier mass may
  remain `O(1)` per epoch;
- the pruned-bi-tree counterexample forbids arbitrary zeroing of tensor
  weights; it does not say every sparse measure fails;
- the `T^4` literature gives an obstruction to straightforward proof
  extension, not an impossibility theorem for every four-parameter embedding;
- the 512-mark E--T fixture and 9,845,549-selection DP are finite only;
- any theorem must distinguish one `surv_C=infinity` ray from a changing
  sequence of locally critical finite rulers.

Wave 11 outcome: the interval-length floor
`K_m^len=2log m+O(1)` completes P16's missing-leading-quarter subproblem and
removes the need to allocate the old globally sorted floor fanwise.  The
secondary `o(log J)` repayment is not proved and is isolated as P17.  Route B
remains open.

Status: **partly complete; its remaining Route A mechanism is sharpened by
P17 after Wave 11.**

## P17. Secondary triangular-floor survival repayment

For each dyadic epoch let

`K_m^len=sum_((p,q) in I_m) beta_(m,p,q) log binom(q-p+2,2)`

and let `G_m^len=A_m-K_m^len>=0`.  Wave 11 proves, without a survival
hypothesis,

`K_m^len=2 log m+O(1)`

and the exact local identity

`T_m-K_m^len=Y_m+G_m^len+S_m`,

where `Y_m,G_m^len,S_m` are all nonnegative.  Thus the leading-quarter
allocation issue in P16 is complete: the lower shell contributes
`(1/2)log m+O(1)` and the interior contributes `(3/2)log m+O(1)`.

Required theorem: for every fixed `C>0` and every fixed infinite normalized
Golomb ruler satisfying `N_n<=C n^2 log(2n)` eventually:

`G_J^len+S_J >= T_J-K_J^len-epsilon_J`,

for some `epsilon_J>=0` with `epsilon_J=o(log J)`.  Equivalently,

`0<=sum_(m in E_J)Y_m<=epsilon_J=o(log J)`.

This was the exact Wave 11 Route A target.  The direct critical-cap estimate
is only `T_J-K_J^len=O_C(J log J)`.  Wave 13 below shows that its
universal-over-all-`C` form is already Question-1-equivalent; any proof must
therefore use information not contained in the per-length triangular floor
alone.

Mandatory gates:

- use one fixed `surv_C=infinity` branch; changing finite Erdős--Turán rulers
  are not admissible evidence for the infinite quantifier;
- do not charge each future occurrence of `(i,j)` uniformly to its birth:
  its dyadic overlap coefficient is `Theta(log(j/i))`;
- do not use another within-length sorting or a stronger global diameter
  theorem as the main payment: the former adds only `O(m^(-1/2))` per shell,
  while the latter has only an `O(m^(-1/2))` subleading correction to
  `2log m` and contains no cross-length/survival state;
- preserve the exact nonnegative channels `Y`, `G^len`, and `S`; do not
  cancel signed surrogates across incompatible allocations;
- test any finite shadow on all 1,146 bounded all-prefix-`C=1` rulers, the
  authenticated Wave 6--10 fixtures, and changing Erdős--Turán windows, but
  never promote those tests to infinite survival.

A separate Route B remains admissible: encode the exact positive core as a
positive measure on full bi-/tri-trees and prove a summably vanishing product-
box profile.  One-tree qualitative vanishing is insufficient, and no
equivalence with the displayed Route A inequality has been proved.

Wave 12 rewrites this obligation by the exact positive cut renewal in P18.
That rewrite removes the logarithmic same-pair overlap in the raw future
tails, but it does not prove the required sum over different integer pairs.

Wave 13 proves an unavoidable integer new-birth floor.  With
`H_m=a_(2m-1)-a_(m-2)` and

`E_m=m(m-2)(m^2+8m+6)/48>=m^4/48`,

one has

`Y_m>=Z_m^nb>=E_m/(8m^2 H_m)>=m^2/(384H_m)`.

On any hypothetical eventual-`C` branch this gives
`Y_m>=1/(1536C log(4m))` eventually and hence

`liminf_(J->infinity) sum_(m in E_J)Y_m/log J
 >=1/(1536C log 2)`.

Therefore the universal-over-all-`C` P17 assertion is logically equivalent
to Question 1: Question 1 makes its branch class empty, while P17 plus an
assumed counterexample branch contradicts this harmonic lower bound.  This is
a reduction, not a proof of P17 or Question 1.

Status: **open; reclassified after Wave 13 as a Question-1-equivalent
contradiction statement, with the exact signed form recorded in P19.**

## P18. Integer cut-renewal packing on one surviving branch

Retain the Wave 11 positive cross ratios `C_(i,j)` and define

`R_m=sum_(i=1)^(m-2)((m-i)/(2m))^2 sum_(j=m)^infinity C_(i,j)`.

Wave 12 proves the coefficientwise identity

`Y_m=R_m-R_(2m)+Z_m`,

where `Z_m=Z_m^ob+Z_m^nb+Z_m^of+Z_m^mf>=0` and

```text
Z_m^ob = sum_(m<=j<2m, i<=m-2)
           ((j-i)^2-(m-i)^2)/(4m^2) C_(i,j),
Z_m^nb = sum_(m<=j<2m, m-1<=i<=j-2)
           (j-i)^2/(4m^2) C_(i,j),
Z_m^of = sum_(j>=2m, i<=m-2)
           i(4m-3i)/(16m^2) C_(i,j),
Z_m^mf = sum_(j>=2m, m-1<=i<=2m-2)
           (2m-i)^2/(16m^2) C_(i,j).
```

Therefore, for `E_J={4,8,...,2^J}`,

`sum_(m in E_J)Y_m=R_4-R_(2^(J+1))+sum_(m in E_J)Z_m`.

Historical Wave 12 sufficient theorem: for every fixed `C>0` and every fixed infinite
normalized **integer** Golomb ruler satisfying
`a_n<=C n^2 log(2n)` eventually, prove

`sum_(m in E_J)Z_m=o_C(log J)`.

Wave 13 shows that this requested little-oh cannot coexist with an actual
branch in its hypothesis.  For every finite integer Golomb prefix containing
`a_(2m-1)`, let `H_m=a_(2m-1)-a_(m-2)`.  Distinctness of the `m+1` suffix
gaps and the product floor `C_(i,j)>=h_i h_j/D_(i,j)^2` give

`Z_m>=Z_m^nb>=E_m/(8m^2H_m)>=m^2/(384H_m)`.

Thus an eventual-`C` cap forces

`liminf_(J->infinity) sum_(m in E_J)Z_m/log J
 >=1/(1536C log 2)`.

Consequently the universal-over-all-`C` P18 assertion is equivalent to
Question 1, just as P17 is.  It is not a smaller packing property expected to
hold on a surviving critical branch.  It remains a valid contradiction
target, but calling it an intermediate lemma obscures its full logical cost.

Mandatory gates:

- use one fixed `surv_C=infinity` branch, not a terminal-scale-dependent
  family;
- exploit integer unit spacing, additive interval-sum relations, or an
  explicitly equivalent arithmetic input across different pairs;
- do not stop at fixed-pair coefficient summability: this is now uniform, but
  the number and mass of different pairs remain uncontrolled;
- do not use only numerical ranks, triangular length floors, and the complete
  interval-containment order.  Their jointly optimized floor gains less than
  `5` per epoch beyond `K^len`;
- reject any proposed argument that also proves the same statement for real
  Golomb rulers: `a_n=n^2+sqrt(2)n` has quadratic growth, all differences
  distinct, and `Y_m -> (3/2)(log 2-1/2)>0`;
- preserve all four nonnegative `Z` sectors and the terminal term in the
  telescope.  The displayed `Z` estimate is sufficient, not claimed
  equivalent to P17;
- test every finite shadow on the 1,146 bounded all-prefix-`C=1` rulers and
  authenticated 64/128-mark fixtures without promoting finite survival to an
  infinite theorem.

Route B remains separate: a full bi-/tri-tree positive-measure encoding with
a summably vanishing arithmetic box profile would also suffice.  Martikainen's
critical two-depth Journé packing is a geometric template only; no checked
source supplies the Sidon encoding or box decay.

Status: **open but reclassified: universal P18 is Question-1-equivalent, not
a subordinate different-pair packing lemma.**

## P19. Signed terminal repayment and suffix-frontier contradiction

Wave 12's exact telescope gives the cancellation-faithful form

`sum_(m in E_J)Z_m-R_(2^(J+1))=o_C(log J)`.

The fixed constant `R_4` is absorbed in the little-oh term.  This is exactly
P17, not the stronger separate decay demanded by P18.  The Wave 13 harmonic
lower bounds for both `Y` and `Z` show that even this signed assertion cannot
coexist with an actual eventual-critical integer branch; proving it
universally is another form of proving Question 1.

Wave 13 also expands each `Z_m` into the exact finite frontier spectrum

`Z_m=mathfrak P_m+mathfrak U_m-mathfrak B_m-mathfrak F_m-mathfrak e_m`.

The prefix/full-span channel has the one-sided summable removal

`0<=Z_m<=X_m+epsilon_m`,
`X_m=mathfrak U_m-mathfrak B_m`,
`epsilon_m=((4m-3)/(16m^2))log a_(2m-1)`.

Under an eventual critical cap, the dyadic sum of `epsilon_m` is finite, but
the integer new-birth theorem forces

`sum_(m in E_J)X_m
 >=(1536C log2)^(-1)log J-O_(C,a)(1)`.

Hence the terminal suffix fan beats its interior descendants harmonically on
every hypothetical critical branch.  A useful new lemma must give a genuinely
cross-epoch arithmetic upper that contradicts this frontier lower, or retain
the exact terminal-tail cancellation; a within-epoch positive packing cannot
make the frontier sparse.

The exact integer-cell identity

`C_(i,j)=sum_(x=0)^(h_i-1) sum_(y=0)^(h_j-1)
 log((M+x+y+1)^2/((M+x+y)(M+x+y+2)))`,

with `M=D_(i+1,j-1)`, exposes the lattice but does not itself control cell
multiplicity.  Golomb uniqueness controls the four corner differences, not
the internal levels `M+x+y`.  The combined rank/length/containment floor also
remains capped at constant gain per epoch.

Primary artifacts:

- `endpoint_variance/WAVE13_P18_HARMONIC_OBSTRUCTION_2026-08-29.md`;
- `endpoint_variance/WAVE13_FRONTIER_SPECTRUM_AND_SIGNED_REPAYMENT_2026-08-29.md`;
- `endpoint_variance/wave13_p18_harmonic_obstruction_certificate_2026-08-29.json`.

Status: **central Route A statement open; exactly Question-1-equivalent.
P15, P17, P18, P19, Questions 1 and 2, and the prize claim remain
unresolved.**

## P20. Future-rank promotion and disjoint birth-time allocation

Wave 14 proves a new theorem on every fixed infinite eventual-`C` branch.
For an old prefix difference `d in Delta_L`, put

`N=floor(d/log(d)^2)`.

Once the explicit side conditions in
`WAVE14_FUTURE_RANK_PROMOTION_2026-08-29.md` hold, spatial bins of width `d`
in the next `N` marks give

`rho_infinity(d)-rho_L(d) >= d/(64C log d)`.

For the macroscopic Wave 13 suffix `d_(m,p)=D_(p,2m-1)`, `2<=p<=m`, this
implies

`log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p)))
 >=1/(512C log m)`

eventually.  The sharper pre-simplification is

`log(1+1/(64C log d_(m,p)))`.

The same suffix atom reappears in the epoch-`2m` Wave 11 lower shell with
coefficient

`v_(m,p)=(4m-2p+1)/(16m^2)`.

Writing `L_(m,p)=binom(2m-p+1,2)`, the exact nonnegative split

`log d=log L+log(rho_(2m)/L)+log(rho_infinity/rho_(2m))
       +log(d/rho_infinity)`

proves the disjoint floor improvement

`A_J >= K_J^star+Phi_(J-1)`,  
`K_J^star=max(K_J^len,K_J^mix)`,

where

`Phi_m=sum_p v_(m,p)log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p)))`.

Its macroscopic coefficient mass tends to `3/16`, and the sharp Wave 14
bound gives

`Phi_m >= (3/2048-o_C(1))/(C log m)`.

This is a genuine harmonic rebate.  It is not an upper bound for `Y_m`,
`Z_m`, or `X_m`, and comparing its lower bound with the separate Wave 13
lower bound is invalid.

Wave 15 localizes another promotion component.  Let

`K_p=rho_(4m-1)(d_(m,p))-rho_(2m)(d_(m,p))`

and

`Delta_m=sum_(p=2)^m u_(m,p)log(1+K_p/rho_(2m)(d_(m,p)))`.

Then, eventually,

`Delta_m>=1/(512C log(8m))`.

Every new difference counted by `K_p` is a literal atom of the next Gothic
bulk `mathfrak B_(2m)`.  The complete nested load on one new numerical
difference is less than `3/(4m^2)`, so

`Delta_m <= mathfrak B_(2m)
 +3(ceil(e^12)-1)/(4m^2)`.

The error is dyadically summable.  This is a gross adjacent-epoch allocation
of the marginal rank increment, not a disjoint premium over `K^len`,
`K^mix`, or the global rearrangement floor.

Required theorem: prove either

1. a disjoint strengthening
   `mathfrak B_(2m)>=existing_floor+c Delta_m-summable_error` with enough
   uniform `c>0`, together with an exact terminal potential; or
2. a global birth-time allocation for the residual suffix coefficient
   `u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2)` whose total reuse is bounded across all
   dyadic epochs and whose horizon boundary is `o(log J)`.

Mandatory gates:

- do not add `Phi_m` to the Wave 10 global floor without checking rank
  overlap; only the explicit next lower-shell insertion is currently legal;
- do not add the Wave 15 `Delta_m` allocation to an existing floor: its proof
  spends the full values `beta(x)log x` of the selected bulk atoms;
- do not replace the marginal term by `u_(m,p)log d_(m,p)`.  The finite Hall
  64 and Erdős--Turán 128 audits give explicit failures, and `x<=d` has the
  wrong logarithmic direction;
- historically, shifting `mathfrak B_(2m)` backward while omitting the exact
  renewal tail exposed an unmatched `mathfrak U_M=Theta(J)` fan.  Wave 16
  absorbs this into `mathcal T_m>=0`; it must not be reused as the current
  obstruction;
- a fixed numerical difference born `k` dyadic epochs later can carry a
  source-to-birth coefficient ratio of order `4^k`; adjacent-epoch bounded
  reuse does not establish all-epoch bounded reuse;
- all finite fixtures remain falsification and algebra checks only.

Status: **partly complete; historically superseded by P22 and now by P23 as
the current target.**
Future promotion, the legal next-shell rebate, adjacent-epoch nested reuse,
terminal repair, and Wave 17's local triangular-floor disjoint allocation are
proved.  The uncapped signed excess allocation needed for P19 remains open.

## P21. Constant-fraction promotion with disjoint bulk capacity

Wave 16 strengthens the conditional future-rank theorem.  On one fixed
eventual-`C` branch, every old difference `d>=L^2/8` satisfies, for all
sufficiently large `L`,

`rho_infinity(d)-rho_L(d)>d/(128C log 2)`.

For `d_(m,p)=D_(p,2m-1)`, `2<=p<=m`, put

`kappa_C=log(1+1/(128C log 2))`.

Then the promotion logarithm is at least `kappa_C` uniformly, the legal
next-shell resource obeys `Phi_m>=kappa_C/6`, and the residual `u-v`
resource obeys `Theta_m>=kappa_C/3` eventually.  The eventual-hole factor
`log(d/rho_infinity(d))` is uniformly `O_C(1)`.

Wave 16 also proves the exact terminal potential

`Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`, `mathcal T_m>=0`,

and hence

`Z_m-R_(2m)<=(3/4)log log(4m)+O_C(1)`.

Thus the isolated `mathfrak U_(2^J)=Theta(J)` fan is not an independent
terminal obstruction.  A Fejer taper preserves the harmonic signal and
makes the raw terminal and one-step weight mismatch negligible.

Wave 17 proves the requested local statement for the triangular interior
floor in two ways.  First,

`mathfrak B_(2m)>=K_(2m)^int+[log(3/2)/12]Delta_m`
`-2146log(3/2)/(16m^2)`.

The proof spends only the same-atom residual above the triangular floor.
Second, the exact sorted-rank floor on the same interior atom set is

`F_n^(loc,int)=[2log((n-1)!)+log(b!)+log(c!)]/(4n^2)`,

where `b=3(n-1)(n-2)/2` and `c=(n-1)(3n-4)/2`.  Its surplus
`D_n=F_n^(loc,int)-K_n^int` satisfies

`|D_n-[3/2+(3/4)log3-2log2]|<=18(1+log n)/n` for `n>=16`.

Thus `D_n>81/128` for `n>=2^20` and `D_n>3/4` for
`n>=2^22`.  In particular,

`mathfrak B_(2m)>=K_(2m)^int+(3/8)Delta_m`

for `2m>=2^20`, and the full residual `u-v` promotion truncated at height
two is paid for `2m>=2^22`.  This closes the local coefficient-capacity
overlap without counting one atom twice.

Mandatory gates:

- retain `R_(2m)`, `mathfrak F_m`, and `mathfrak e_m` when auditing the
  terminal suffix; together they form the nonnegative potential;
- do not cite the historical raw `Theta(J)` suffix fan as the current
  terminal boundary;
- distinguish the proved branch-conditional multiscale theorem from the
  finite Hall/ET certificate;
- do not infer a contradiction merely because `Phi_m` or `Theta_m` now has
  constant size; it remains a lower bound on a positive resource;
- preserve the exact floor allocation and prove that any promotion charge
  uses residual, not already-spent, bulk capacity;
- do not spend the sorted-rank surplus once for `Delta_m` and again for the
  capped `u-v` promotion; these are alternate uses of one aggregate capacity;
- do not promote the local lower bound to a signed global upper.

Status: **COMPLETE for the local triangular-floor capacity gate.**  The
same-atom residual, stronger sorted-rank floor, explicit errors, and finite
thresholds are proved.  Historically, at the end of Wave 17, P19 still
remained open because the promotion above the fixed truncation and the
endpoint/descendant renewal residual were not yet paid.  Wave 18 now inserts
that promotion sign-faithfully modulo the single positive descendant-jump
functional `J_n^(5/2)`.  Thus the current obstruction is P23: prove its
tapered `o(log J)` bound on one fixed compatible eventual-`C` branch, or
cancel it before taking `log_+` against the retained signed ledger.

## P22. Signed repayment of uncapped promotion excess

For the residual coefficient

`r_(m,p)=u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2)`

and promotion logarithm

`P_(m,p)=log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p)))`,

Wave 17 splits

`Theta_m^[2]=sum_p r_(m,p)min(P_(m,p),2)`

from

`Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+`.

The local sorted-rank surplus pays `Theta_m^[2]` eventually, and Wave 16
forces `Theta_m^[2]>=(1/3)min(kappa_C,2)` on an eventual-`C` branch.  The
uncapped excess has only the present envelope `O_C(log log m)` per epoch.
Consequently a Fejer taper does not by itself make its dyadic accumulation
`o(log J)`.

Required theorem: put

`H_n^loc=mathfrak B_n-F_n^(loc,int)>=0`.

Prove a bounded-reuse signed allocation controlling

`sum_k omega_(k,J)Theta_(m_k)^exc`

by the unused `H_(m_(k+1))^loc`, the unused portion of `D_(m_(k+1))`, and
the exact renewal terms, with total loss `o(log J)`.  The result must be
inserted into

`Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`, `mathcal T_m>=0`,

with every endpoint/descendant term retained.  An equivalent direct signed
terminal inequality is acceptable.

Mandatory gates:

- authenticate each promotion carrier and its source-to-target coefficient;
- bound total reuse across all dyadic sources, not only adjacent epochs;
- keep the fixed truncation and excess as an exact identity;
- do not count `D_n` both in `Theta^[2]` and in an additional floor;
- do not infer a signed upper from the nonnegativity of `H_n^loc`;
- finite Hall/ET rows are falsification and ownership checks only.

Wave 18 completes two sub-obligations.  For a general cap `h`, exact local
row capacities prove

`Theta_n^(exc,h)<=H_n^loc+J_n^(h)`.

At `h=5/2`, the Wave 17 surplus pays the previous source cap and yields the
exact sign-faithful insertion

`Z_n-R_(2n)=mathfrak P_n-K_n^int-mathcal T_n`
`-Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)+J_n^(5/2)-(U_n+Q_n)`,

where `mathcal T_n,U_n,Q_n>=0`.  A separate rank-layer allocation bounds
reuse from all dyadic sources for every future numerical difference.  Thus
local capacity, sign, and all-source rank-slot reuse are no longer open.

Status: **PARTLY COMPLETE; superseded by P23 as the current Route A
obligation.**  The positive descendant-jump functional still lacks the
required tapered little-oh bound.

## P23. Birth-time Carleson repayment of descendant jumps

For the exact Wave 18 residual

`J_n^(h)=sum_p [r_(n,p)/w_(n,p)] sum_q beta_(n,p,q)`
` log_+(d_(n,p)c_n/(exp(h)L_(n,p)D_(p,q)))`,

prove at `h=5/2`, on one fixed infinite normalized integer Golomb ruler
satisfying the eventual-`C` envelope,

`sum_(k<=J)omega_(k,J)J_(2^k)^(5/2)=o_C(log J)`,

or prove an exact signed cancellation of the same term against
`mathfrak P_n-K_n^int-mathcal T_n`.

The current all-source rank-layer theorem gives a fixed future difference
`x` total load

`Lambda^(exc,h)(x)<[8C log2/(3exp(h))]log(4x)/x`

eventually.  What it does not give is a bound on the dyadic birth scale
`b(x)` in terms of `x`, unused local slack at that birth, or a terminal
carrier when the birth index is `2n-1`.

Wave 18 also gives the exact one-dimensional reduction

`J_n^(h)<=sum_p r_(n,p)[log(d_(n,p)/D_(p,n))-(h-log3)]_+`.

At `h=5/2` its threshold is only `0.0150933...` above `log4`.  A monotone
alternating scalar quadratic-envelope model has a `Theta(J)` tapered sum, and
a terminal-cap-compatible family of actual finite Golomb prefixes attains
`J_n^(h)>=(3/8-o(1))log log n+O_(C,h)(1)`.  The latter family is not one
fixed-onset eventual-`C` branch.  These results do not refute P23, but prove
that its input must be compatible-tower structure or signed cancellation
before the positive part, not a stronger one-epoch estimate.

Mandatory gates:

- keep source scale and birth scale distinct and control their Fejer weight
  mismatch, including carriers born after the horizon;
- use only slack above the already-spent local sorted-rank floor;
- retain terminal births in the exact renewal identity;
- handle the renewing band `n/2<p<=n`, whose residual mass is
  `5/32-1/(4n)`;
- do not infer the theorem from one-epoch Golomb distinctness or quadratic
  diameter: finite Erdős--Turán rulers keep `H_n^loc` uniformly bounded;
- do not use the terminal identity without the eventual cap: a distant-block
  construction makes the excess arbitrarily large while its local terms stay
  fixed;
- treat every finite certificate as an algebra/constant audit, not an
  infinite-branch proof.

Wave 19 proves that the whole `J` term need not be controlled positively.
Its cross-ratio part is absorbed by half of `Y`, while its endpoint part is
paid by three quarters of the existing prefix/full-span deficit.  The
certified 512-mark spike/cooldown witness also shows that large finite
midpoint jumps survive two additional compatible dyadic stages.  This does
not refute P23 on an infinite branch, but makes the literal positive P23
statement an overstrong and no-longer-recommended target.

Status: **OPEN BUT RECLASSIFIED; superseded by the sign-faithful P24
target.**  P19, Questions 1 and 2, and any prize claim remain open.

## P24. Cross-ratio-absorbed signed frontier bound

For `n>=4`, Wave 19 proves the exact rectangle identity

`log[a_q d_(n,p)/(a_(2n-1)D_(p,q))]`
`=sum_(i<p)sum_(j>q)C_(i,j)`

and the coefficientwise half-absorption

`S_n<=(1/2)Y_n`.

It also proves, with

`Dpre_n=sum_(q=n)^(2n-2)((2q-1)/(4n^2))`
` log(a_(2n-1)/a_q)`,

that the endpoint weights satisfy

`lambda_(n,q)<(3/4)(2q-1)/(4n^2)`

and hence

`(mathfrak P_n-mathfrak F_n)+E_n^(5/2)`
`<=-(1/4)Dpre_n+epsilon_n`,

where `sum_k epsilon_(2^k)<infinity` on one fixed eventual-`C` branch.
Using the uncontracted Wave 13 spectrum exactly once gives

`Z_n<=(1/2)Y_n+G_n+epsilon_n`
`-(U_n^cap+Q_n+mathfrak e_n)`,

where

`G_n=mathfrak U_n-K_n^int-Theta_(n/2)^[5/2]`
`-Theta_n^(exc,5/2)-(1/4)Dpre_n`.

After a fixed onset `k_0`, the weighted renewal identity therefore gives

`(1/2)sum_(k=k0)^J omega_(k,J)Y_(2^k)`
`<=O_(C,a,k0)(1)+sum_(k=k0)^J omega_(k,J)G_(2^k)`.

The Wave 13 integer lower bound makes the left side at least

`[1/(3072C log2)]log J+O_(C,k0)(1)`.

Thus the exact directly sufficient theorem is

`limsup_(J->infinity)[sum omega G]/log J<1/(3072C log2)`.

The cleaner P24 target is

`sum_(k=k0)^J omega_(k,J)G_(2^k)=o_(C,a)(log J)`

for every `C` and every fixed compatible infinite eventual-`C` integer
Golomb branch.

An exact cap reindexing reduces this to the current-scale expression

`Ghat_n=mathfrak U_n-K_n^int-Theta_n^[5/2]`
`-Theta_n^(exc,5/2)-(1/4)Dpre_n`

with cost at most `15/16`.  In particular,

`sum omega (Ghat_(2^k))_+=o_(C,a)(log J)`

is a sufficient next lemma.  Stronger sufficient forms are
`(Ghat_(2^k))_+=o_(C,a)(1/k)` or
`sum_(k=L)^(2L)(Ghat_(2^k))_+=o_(C,a)(1)`.

Mandatory gates:

- use the uncontracted prefix/full-span spectrum or the contracted terminal
  potential, never both copies of `mathfrak F_n`;
- keep `K_n^int` distinct from the next-shell `K^low+Phi` resource;
- include the exceptional full-suffix residual
  `bar r_(n,2n-2)=3/(8n^2)` whenever `u=v+bar r` is used outside `p<=n`;
- do not use a one-step Fejer shift of the raw `v log d` fan: its exact
  mismatch is `(log2/6)J+O_C(log J)`, with `(log2/8)J+O_C(log J)` already
  present on `p<=n`;
- treat the 512-mark `C=32` spike/cooldown witness as a finite obstruction,
  not an infinite branch or a counterexample to P23/P24;
- quantify over every fixed compatible infinite eventual-`C` branch.

Status: **OPEN, BUT SUPERSEDED BY P25 AS THE RECOMMENDED ROUTE A TARGET.**
The two coefficientwise absorptions and cap reindexing are rigorous.  The
bare positive part of `Ghat` is now known to have a sharp local dilation
obstruction; P19/P24, Questions 1 and 2, and any prize claim remain open.

## P25. Certified rank-slack, dilation-invariant signed remainder

Let the `c_n=(n-1)(3n-4)/2` Gothic interior atoms be sorted as

`x_(n,1)<...<x_(n,c_n)`,

and carry the actual coefficient of `x_(n,j)=D_(p_j,q_j)` as
`gamma_(n,j)=beta_(n,p_j,q_j)`.  Define

`Srank_n=sum_j gamma_(n,j)log(x_(n,j)/j)`,

`Pair_n=sum_j gamma_(n,j)log j-F_n^(loc,int)`.

Integer distinctness and the rearrangement definition of the Wave 17 floor
give the exact nonnegative split

`H_n^loc=Srank_n+Pair_n`,  `Srank_n,Pair_n>=0`.

The actual Wave 18 excess proof spends only

`sum_(2<=p<=n)sum_q alpha_(n,p)beta_(n,p,q)`
` log_+(D_(p,q)/c_n)`.

If this atom has sorted rank `j`, then `j<=c_n`, `D_(p,q)>=j`, and
`alpha_(n,p)<=1`.  Therefore the spent term is at most `Srank_n`, and

`Theta_n^(exc,5/2)<=Srank_n+J_n^(5/2)`.

Thus the following is a certified, singly owned part of the Wave 18
remainder:

`Q_n^cert=Srank_n+J_n^(5/2)-Theta_n^(exc,5/2)>=0`,

with the exact audit `Q_n=Q_n^cert+Pair_n`.  Retaining `Q_n^cert`, the cap
surplus, and `mathfrak e_n` in Wave 19 gives the prefix-local remainder

`R_n^cert=mathfrak U_n-F_n^(loc,int)-Srank_n-J_n^(5/2)`
`-(1/4)Dpre_n-mathfrak e_n+epsilon_n`

and the per-epoch inequality

`Z_n<=(1/2)Y_n+R_n^cert`.

There is no current/previous-cap reindexing loss: the preceding cap cancels
exactly between `G_n` and `U_n^cap`.  The weighted renewal identity yields

`(1/2)sum omega Y<=O_(a,k0)(1)+sum omega R^cert`.

The exact alternative form is

`R_n^cert=Z_n+(3/4)Dpre_n-J_n^(5/2)+Pair_n`.

It is invariant under multiplying the whole infinite ruler by any positive
integer.  Indeed `Srank_n` gains `B_n^coef log L`, while `mathfrak U_n`,
`mathfrak e_n`, and `epsilon_n` gain their corresponding masses, and

`U_n^coef-B_n^coef-1/(4n^2)+(4n-3)/(16n^2)=0`.

The recommended sufficient theorem is

`sum_(k=k0)^J omega_(k,J)(R_(2^k)^cert)_+=o_(C,a)(log J)`.

A stronger finite-window version is

`sum_(k=L)^(2L)(R_(2^k)^cert)_+=o_C(1)`

uniformly over compatible finite Golomb towers satisfying the cap throughout
the required window.  Unlike a statement quantified only over hypothetical
infinite critical branches, this finite form is non-vacuous and directly
falsifiable.

Mandatory gates:

- `Srank_n` is spent exactly once in `Q_n^cert`; `Pair_n` is not part of that
  payment and appears with a positive sign in `R_n^cert`;
- use the carried coefficients in value-rank order, not a newly optimized
  coefficient permutation;
- do not add the whole `H_n^loc` after retaining `Q_n^cert`;
- keep the height `h=5/2` and the Wave 18 macro source range `2<=p<=n` in
  the excess proof;
- treat the dilation invariance as removal of a local obstruction, not as a
  bound on `R_n^cert`;
- quantify any infinite conclusion over one fixed compatible eventual-`C`
  branch, or use the stronger uniform finite-window formulation.

Status: **RIGOROUS, SUPERSEDED BY P26, AND SUBJECT TO THE SAME P27
SATURATION.**  The
rank-slack extraction, exact algebra, and dilation audit are rigorous.  P25
and P26 differ only by the nonnegative dyadically summable `Pair_n` term.
Thus the later inner-new-birth floor applies a fortiori to `R_n^cert`; its
unchanged weighted/block positive-part upper target is not an easier
standalone lemma either.  Questions 1 and 2, publication novelty, and every
prize claim remain open.

## P26. Direct rank-free sharp remainder

To avoid collision with the Wave 18 promotion excess, write
`E_n^(end,5/2)` for the **endpoint component** called `E_n^(5/2)` in Wave
19 Sections 3 and 5.  The exact Wave 19 inequalities are

`J_n^(5/2)<=E_n^(end,5/2)+S_n`
`<=E_n^(end,5/2)+(1/2)Y_n`

and

`(mathfrak P_n-mathfrak F_n)+E_n^(end,5/2)`
`<=-(1/4)Dpre_n+epsilon_n`.

Adding the untouched terms of the Wave 13 spectrum therefore proves, with
no rank promotion or floor insertion,

`Z_n<=(1/2)Y_n+R_n^sharp`,

where

`R_n^sharp=mathfrak U_n-mathfrak B_n-J_n^(5/2)`
`-(1/4)Dpre_n-mathfrak e_n+epsilon_n`.

This sign is legitimate: the two displayed Wave 19 bounds give

`mathfrak P_n-mathfrak F_n`
`<=-(1/4)Dpre_n+epsilon_n+(1/2)Y_n-J_n^(5/2)`.

No negative term was inferred from a lower bound.  Since exactly

`mathfrak P_n-mathfrak F_n=-Dpre_n+epsilon_n`,

one also has the identity

`R_n^sharp=Z_n+(3/4)Dpre_n-J_n^(5/2)`.

The weighted renewal argument now yields directly

`(1/2)sum_(k=k0)^J omega_(k,J)Y_(2^k)`
`<=O_(a,k0)(1)+sum_(k=k0)^J omega_(k,J)R_(2^k)^sharp`.

This originally suggested the standalone target

`sum_(k=k0)^J omega_(k,J)(R_(2^k)^sharp)_+`
`=o_(C,a)(log J)`.

The exact weaker signed threshold remains

`limsup [sum omega R^sharp]/log J<1/(3072C log2)`.

The relation to P25 is exact:

`R_n^cert=R_n^sharp+Pair_n`.

The coefficient multiset in the Gothic interior has `a=n-1` high weights
`1/n^2`, `a` low weights `1/(4n^2)`, and
`(n-1)(3n-8)/2` middle weights `1/(2n^2)`.  Put
`c=(n-1)(3n-4)/2` and `b=c-a=3(n-1)(n-2)/2`.  Rearrangement gives the sharp
permutation bound

`0<=Pair_n<=(3/(4n^2))log binom(c,n-1)`

`<=[3(n-1)/(4n^2)]log(e(3n-4)/2)`

`<=(3/(4n))log(3en/2)`.

For dyadic `n=2^k`, consequently

`sum_(k=k0)^infinity Pair_(2^k)`
`<=(3/4)2^(1-k0)[log(3e/2)+(k0+1)log2]`.

In particular the tail from `n>=4` is at most `(3/8)log(12e)`.  Also

`(R_n^sharp)_+<=(R_n^cert)_+`
`<=(R_n^sharp)_++Pair_n`.

Hence the P25 and P26 weighted `o(log J)` targets are equivalent up to an
absolute `O(1)`, and their block forms differ by
`O(L2^(-L))=o(1)`.

The quantity `R_n^sharp` is prefix-local and exactly invariant under integer
dilation of the whole ruler.  This follows either from its identity with
`Z,Dpre,J`, or from

`U_n^coef-B_n^coef-1/(4n^2)+(4n-3)/(16n^2)=0`.

Mandatory gates:

- `E_n^(end,5/2)` is the Wave 19 endpoint component, not
  `Theta_n^(exc,5/2)`;
- `mathfrak B_n` is the actual negative Gothic bulk, not a lower floor;
- do not mix `R_n^sharp` with the distinct Wave 16 terminal potential
  `mathcal T_n`;
- the binomial bound is sharp over abstract coefficient permutations, not a
  claim that a Golomb ruler realizes the maximizing permutation;
- summability of `Pair_n` makes P25 and P26 asymptotically equivalent but
  proves neither positive-part theorem;
- the finite Erdős--Turán dilation family still uses different rulers at
  different scales and is not a P26 counterexample.

Status: **RIGOROUS REDUCTION, BUT CLOSED AS AN EASIER STANDALONE UPPER
TARGET BY THE P27 SATURATION AUDIT BELOW.**  The direct signed collapse,
binomial `Pair_n` bound, equivalence with P25, and dilation audit remain
rigorous.  The `o(log J)` and strict P26-sharp conclusions are not available
on an extant eventual-`C` branch: the untouched inner-new-birth sector alone
has at least the forbidden harmonic mass.  This is not an unconditional
refutation, because the existence of such a branch is precisely the
hypothesis to be contradicted.

## P27. Nonnegative profile remainder and inner-new-birth saturation

Put `A=a_(2n-1)`, `u_(n,q)=log(A/a_q)`,
`v_(n,p,q)=log X_(n,p,q)`, and

`t_(n,p)=5/2-log(c_n/L_(n,p))>0`.

Define the row-exact endpoint term and absorbed descendant increment by

`E_n^row=sum_(p=2)^n sum_(q=n)^(2n-2)`
` alpha_(n,p)beta_(n,p,q)[u_(n,q)-t_(n,p)]_+`,

`Delta_n=J_n^(5/2)-E_n^row`
`=sum alpha beta { [u+v-t]_+-[u-t]_+ }`.

Since the positive-part map is increasing and one-Lipschitz,

`0<=Delta_n<=S_n`.

Let `Z_n^fin=Z_n^ob+Z_n^nb` and
`Z_n^fut=Z_n^of+Z_n^mf`.  The strengthened coefficient audit gives
`S_n<=Z_n^fin`: for `x=n-i>=2`, `y=j-n>=1`, the finite-sector coefficient is
`y(2x+y)/(4n^2)` and dominates `K_(n,i,j)`; for `x=1` it is
`(y+1)^2/(4n^2)`, including the two Wave 19 corner cases.  Consequently

`R_n^prof:=Z_n+E_n^row-J_n^(5/2)=Z_n-Delta_n`

`=(Z_n^fin-S_n)+Z_n^fut+(S_n-Delta_n)>=0`,

and

`Z_n<=S_n+R_n^prof<=(1/2)Y_n+R_n^prof`.

Moreover

`R_n^sharp=R_n^prof+(3/4)Dpre_n-E_n^row>=R_n^prof`.

Here `E_n^row<=E_n^(end,5/2)<=3Dpre_n/4`, since
`t_(n,p)>=5/2-log3` in every row.

Thus the positive part in P26 is redundant.  More importantly, this does
not make the desired upper bound easier.  Define the untouched inner-birth
sector

`W_n=sum_(j=n+2)^(2n-1) sum_(i=n)^(j-2)`
` ((j-i)^2/(4n^2))C_(i,j)`.

The rectangle `S_n` has `i<=n-1`, so `W_n<=Z_n^fin-S_n<=R_n^prof`.
If `H_n'=a_(2n-1)-a_(n-1)`, the Wave 13 layered distinct-gap argument on
the `n` gaps `{h_n,...,h_(2n-1)}` gives exactly

`W_n>=E_n'/(8n^2 H_n')`,

`E_n'=sum_(r=2)^(n/2)(2r-1)(n+1-2r)(n+2-2r)/2`
`=n(n-2)(n^2+4n-14)/48`.

For dyadic `n>=16`, `E_n'>=n^4/48`, hence

`R_n^sharp>=R_n^prof>=W_n>=n^2/(384a_(2n-1))`.

On any hypothetical fixed eventual-`C` branch this implies

`R_n^sharp>1/(1536C log(4n))`

eventually and therefore

`liminf_(J->infinity) [sum_(k=k0)^J omega_(k,J)R_(2^k)^sharp]/log J`
`>=1/(1536C log2)`.

This is twice the strict P26-sharp threshold `1/(3072C log2)`.  Therefore
P26/P27 `o(log J)` or the strict sharp bound cannot hold on any *extant*
eventual-`C` branch.  The statement is conditional and does not construct
or rule out such a branch by itself.  It shows that P26/P27 is not a
standalone intermediate packing lemma weaker than Question 1.  The uniform
block `o_C(1)` formulation has the same saturation whenever the quantified
compatible cap-respecting finite towers are nonempty.

The dyadic right-endpoint bands of `W_(2^k)` are disjoint and every
coefficient is positive.  Hence ordinary Fejer tapering supplies no
one-step cancellation of this channel; a new negative-cut carrier with
explicit ownership is necessary.

Status: **SATURATED / CLOSED AS A STANDALONE INTERMEDIATE UPPER TARGET.**
Pointwise nonnegativity and the inner-sector floor are rigorous.  No claim
is made that P27, Question 1, or Question 2 has been proved or refuted
unconditionally.

## P28. Relocate the untouched inner-new-birth sector with exact ownership

The next open direction must change the ledger, not attempt to prove P26 or
P27 unchanged.  Starting from the exact tapered cut-renewal identity, find
a sign-faithful cross-scale carrier for a positive part of `W_n` so that an
inequality of the form

`Z_n<=(1/2)Y_n+R_n^prof-eta W_n+V_n-V_(2n)+Err_n`

holds with some fixed `eta>0`, with the Fejer reindexing of `V_n-V_(2n)`
nonpositive or `O(1)` and `sum_k omega_(k,J)Err_(2^k)=o(log J)`.  The same
inner-birth atom may occur only once: it must be moved to the retained side
or paid by a negative renewal cut, never counted both as signal and as a
residual rebate.  Any viable version must also retain the exact support
distinction `i>=n` for `W_n` versus `i<=n-1` for the descendant rectangle.

An acceptable P28 lemma must leave a positive harmonic signal after the
transfer and give a residual coefficient strictly below that signal.  A
mere restatement `R_n^prof=o(1/k)` or a same-scale cap/rank estimate is ruled
out by P27.  Whether such a carrier exists is open.

Status: **OPEN — CURRENT HIGHEST-VALUE ROUTE A DIRECTION.**  P19/P24/P25 and
the reductions P26/P27 remain part of the history, but none proves either
Erdos question, publication novelty, or a prize claim.

### P28 exact boundary after the full-row and arbitrary-transport audits

The first two literal full-row allocations are now completely separated.

- Allocating the whole terminal coefficient `u_p` to its descendant row
  fails coefficientwise from `n=6` onward (first dyadic failure `n=8`), with
  worst atom `C_(1,n+1)` and limiting ratio `9/8`.  Independently, it is
  inadmissible because `u_p=v_p+bar r_p`: retaining the next negative cut
  while spending all of `u_p` spends `v_p` twice.
- The cut-valid demand `bar r_p=u_p-v_p` fits every row.  Its natural
  transport `t0=(bar r_p/w_p)beta_(p,q)` satisfies
  `S_(t0)<=Y_n/2` coefficientwise, with asymptotically sharp atom
  `C_(1,2n-1)`.  On the inner `W_n` sector it leaves strictly more than
  `W_n/2`, so the old strict threshold remains saturated.

The adaptive height

`h_(n,p)=max(3/2,log(c_n/L_(n,p)))`

has nonnegative row threshold on the entire range.  The actual cap obeys

`Theta_n^cap<=C_n^det=sum_p bar r_p h_(n,p)`

(generally not equality), and the deterministic profile satisfies

`C_n^det<0.8336738101+0.3009853/n`.

The Wave 17 surplus therefore pays the preceding cap exactly at the correct
index:

`D_N>C_(N/2)^det>=Theta_(N/2)^cap` for every `N>=2048`.

Actual Gothic ranks do not delete the endpoint.  For every feasible transport
`t`, with actual rank `j_(p,q)` and
`sigma_(p,q)=h_(n,p)-log(j_(p,q)/L_(n,p))>=0`, the valid bound is

`Theta_n^exc<=Srank_n+S_(t)+E_(t)^rank`,

`E_(t)^rank=sum t_(p,q)[log(A/a_q)-sigma_(p,q)]_+`.

The endpoint-free shortcut `Theta^exc<=Srank+S_(t)` is not justified: it
would require `j_(p,q)<=exp(h_p)L_p a_q/A`, not merely
`j_(p,q)<=exp(h_p)L_p`.

Transport optimization alone is also insufficient.  For every feasible
transport and every dyadic `n>=64`, the exact inner residual obeys

`E_n^res(t)>=n^2/(2^25 H_n')`.

On a hypothetical eventual-`C` branch this is
`>1/(2^27 C log(4n))`, with Fejer liminf at least
`1/(2^27 C log2)`.  The corner `C_(2n-4,2n-1)` has exact coverage ratio
`1/3` for every feasible transport.  These are residual floors, not a
contradiction and not a proof of P28.

The highest-value remaining lemma is now a **signed whole-cut theorem**.
For whichever verified feasible transport is used, form the complete
cap/rank/Pair ledger first and retain the Wave 12 cuts or the equivalent
Wave 16 terminal potential without extracting `v` again.  The target must
control the resulting signed `G` functional in Fejer mean below
`1/(3072C log2)` (or by a clean `o(log J)` positive-part estimate).  A
transport-only improvement, a same-scale `W` domination, or reuse of the
already dropped nonnegative bracket is not an admissible completion.

Status: **OPEN.**  P28, Question 1, Question 2, and every prize claim remain
unresolved.

### P28 mixed right-greedy strengthening and exact remaining obligation

The explicit transport

`t=(8t0+tR)/9`,

where `tR` is the rowwise right-greedy fill, is feasible for every `n>=4`.
Every right-fill row prefix is at most the corresponding natural prefix, so

`S_t<=S_(t0)<=Y_n/2`.

An exact all-column count additionally gives

`mu_q(t)<=2c_(n,q)/3`, hence `E_t^rank<=2Dpre_n/3`.

In the complete ownership ledger this improves the natural functional by
exactly `Dpre_n/12`:

`Gmix_n=R_n+Pcoef_n log A-K_n^int-T_n-Theta_n^full-Dpre_n/3`

`=Gold_n-Dpre_n/12`.

> **Reset supersession note (2026-08-29):** The following statement is the
> historical pre-reset target.  The later exact identity in
> `endpoint_variance/WAVE19_P28_GMIX_SELF_CANCELLATION_NO_GO_2026-08-29.md`
> proves that bare `Gmix` grows linearly in the horizon, so it is closed as an
> upper target.  The current honestly owned residual is `X_n+P_n` in
> `ROUTE_PORTFOLIO.md`, and any repair needs a genuinely new singly owned
> negative carrier or a different Route-C/D mechanism.

The historical pre-reset P28 obligation was

`limsup_(J->infinity) [sum_(k=k0)^J omega_(k,J)Gmix_(2^k)]/log J`
`<1/(3072C log2)`,

or a stronger legally owned estimate such as
`sum omega (Gmix_(2^k))_+=o(log J)`.

The hostile algebraic rewrite

`Gmix_n=Y_n+B_n-K_n^int-Theta_n^full+(2/3)Dpre_n`

does not grant those positive terms again: `D-ThetaPrev`, `Qad`, and `Pair`
were already inside the favorable bracket dropped in deriving `Gmix`.

Nor can the endpoint gain be used by the unsigned shortcut
`W_n-S_t<=Dpre_n/12`.  The Golomb ruler
`(0,101,204,309,416,525,636,749)` at `n=4` violates it by an exact rational
logarithmic separation.  This finite witness does not refute a whole-cut
corrected signed inequality.

Historical status: **SUPERSEDED / BARE-`Gmix` TARGET CLOSED BY THE RESET
NO-GO.**  P28 as a design program, the `X+P` payment problem, Questions 1 and
2, and every prize claim remain open.

## RC1. Couple the proved centered multiband carrier to the harmonic floor

The uniform-box covariance family now supplies a proved internal carrier on
every hypothetical eventually `C`-critical dyadic chain.  After a finite
onset, the nonanticipating width schedule

`T_j=2^j 2^ceil(log_2(8C(j+1)log 2))`

moves by one or two bands.  The complete path carrier `X_j` has exact
single-scale ownership and satisfies

`sum_j w_j X_j >= (log J)/(64C log 2)-O_C(1)`.

The fixed three-channel path coupling with `theta=3/25` has a summable
boundary normalization error, so its centered normalized gain has coefficient
`3/(1600C log 2)>1/(1536C log 2)`.

The cross-ratio/box-dipole continuation now proves the missing *scale-density
map*.  With `R_T(d)=(T-d)_+/T^2` and oriented gap dipoles,

`C_(i,j)=integral_0^infinity psi_T dT`,
`psi_T=-<e_i*K_T,e_j*K_T> >= 0`.

Writing `W_n=integral Q_n(T)dT`, its exact mixed-difference expansion gives

`0<=Q_n(T)<=Delta_n,T^suf/(2n^2)<=Delta_tilde_n,T/(2n^2)`.

For `H=D_(n,2n-1)` and
`F_H(d)=log(H/d)+d/H-1`, the coefficient moments vanish and

`W_n=sum lambda_(p,q)F_H(D_(p,q))=-sum lambda_(p,q)log D_(p,q)`.

Apart from the full-span coefficient, whose `F_H(H)` is zero, every positive
`lambda` is exactly the already-owned Wave-11 strict-interior
`beta_n(p,q)` coefficient.  Every other `q=2n-1` coefficient is nonpositive,
so no positive next-shell/terminal capacity is needed.  This is C063; it is
not permission to count the same Gothic atom again.

No fixed finite log-phase grid integrates all tents atomwise, while the exact
continuum identity is

`integral_0^1 sum_r 2^(r+theta)psi_(2^(r+theta))dtheta=C_(i,j)/log 2`.

Moreover the explicit finite ET family in C065 proves that ordinary
fixed-prefix domination by the canonical critical one/two-band increment is
false.  These results narrow, but do not finish, the obligation.  It is now
to derive both sectors from one independently valid finite-horizon inequality
by *rewriting*, rather than adding to, the Gothic ownership ledger.

C066 exposes the exact prefix/scale transport governing the most direct
attempt.  For a fixed log phase, nested prefixes, and finite scale horizon,

`Delta_(j,r)-Delta_(j,r+1)=O_(j,r)-O_(j-1,r)`.

If `s_(j,r)=sum_(t<=r)c_(j,t)`, two finite Abel summations give the interior
retained-band coefficient

`b_(j,r)=w_j s_(j,r)-w_(j+1)s_(j+1,r)`,

with the initial epoch, final epoch, and scale-terminal rows kept explicitly.
For the universally saturated pointwise-capacity profile and
`n_(j+1)=2n_j`, every `b_(j,r)` is nonnegative exactly when

`w_(j+1) 2^max(0,R_(j+1)-R_j)<=4w_j`.

The certified cutoff jump `R_j=2` to `R_(j+1)=5` violates this gate and has
`b=-62/121`.  Thus the full capacity envelope cannot simply be transposed
through adjacent epochs and treated as a nonnegative retained-band mixture.
This does not rule out pair-dependent fractional allocation, longer
transport, phase randomization, or a larger signed master.

C067 now solves the local positive-potential pair allocation exactly.  If

`P_n(T)=sum_(gamma in Gamma_n) beta_gamma R_T(d_gamma)`

and `u_(gamma,r)=T_r beta_gamma R_(T_r)(d_gamma)`, then

`x_(gamma,r)=u_(gamma,r)Q_n(T_r)/P_n(T_r)`

(with all variables zero when `P_n(T_r)=0`) satisfies the demand and every
pair capacity.  The continuum-phase integral preserves each owner, and the
unused positive budget is exactly the nonpositive finite-potential sector.
For the canonical dyadic spatial-prefix chain, the physical pair
`(a_(p-1),a_q)` of every strict-interior positive owner lies wholly in the
new block `n,...,2n-2` and therefore has a unique birth epoch.  Its pre-birth
state is zero, so the formal preceding negative Abel coefficient multiplies
zero; the birth coefficient is positive.  All scale-terminal rows remain
explicit.  This is a human-proof-audited owner lift, not a reuse of the
already-owned Gothic `beta` rows and not yet a common PSD master.

C068 closes the coefficientwise scalar fallback only under its stated
constraints.  On the exact nested Golomb prefixes

`A^-=(0,1,3,7,12,20,30,44)`

and

`A^+=(0,1,3,7,12,20,30,44,1044,1094,2095,2155,2225,2305,2395,2495)`,

with `n_-=4`, `n_+=8`, and `w_-/w_+=100/81`, no phasewise nonnegative scalar
family can simultaneously satisfy the universal envelope (4.3), aggregate
demand (4.4), and coefficientwise adjacent gate (4.5) of
`ROUTE_C_PAIR_OWNED_ALLOCATION_LP_PROBE.md`.  The exact first-use supremum is
`18/385`; seven positive Wave atoms give the strict rational contradiction.
This conditional no-go does not apply to owner-resolved coefficients,
signed payment, longer transport, other weight systems, or a relaxation
justified inside a larger master.

C069 identifies the exact price of the stronger coefficient-PSD lift.  For
the scale-active rank-dipole graph, put `(B_T)_(i,j)=-alpha_(i,j)/2` on active
edges and `g_i(T)=||e_i*K_T||_2^2`.  Then

`P_n(T)=min{sum_i g_i(T)d_i: diag(d)+B_T is PSD}`

has the exact primal-dual value

`P_n(T)=sum_((i,j) in E_n(T)) alpha_(i,j)sqrt(g_i(T)g_j(T))`.

The tent table gives `P_n(T)>=2Q_n(T)`, hence the integrated price
`Pi_n>=2W_n`.  Exact localization to the active graph is essential for
integrability.  This price belongs only to a coefficient-PSD completion;
positivity after contraction with the actual ordered box-dipole Gram matrix
is a weaker problem and remains available.

C070 proves that the positive same-epoch finite-horizon sector alone cannot
pay that coefficient-PSD price universally.  For the exact eight-mark Golomb
prefix `(0,101,204,309,416,525,636,749)` at `n=4`, the complete active graph
is bipartite and the certified strict inequality is

`G_4<2W_4<=Pi_4`,

where `G_4=sum beta_gamma F_440(d_gamma)` is the entire positive
strict-interior same-epoch capacity.  This is a conditional no-go only for
that isolated payment source and coefficient-PSD lift.  It leaves the actual
Gram restriction, nonpositive Gothic boundary rows, signed cancellation,
cross-epoch or cross-phase payment, and a larger channel master open.

C071 replaces that stronger coefficient-PSD requirement by the exact geometry
of the actual ordered box-dipole Gram matrix.  With full gap intervals
`V_i=[a_(i-1),a_i)` and `U_i=V_i+T`, one has

`T f_i=1_(V_i)-1_(U_i)`

and the two interval families are separately disjoint.  Hence the pointwise
rank vector is only `0`, `+e_i`, `-e_i`, or `e_j-e_i` with `i<j`, and

`G_T=diag(rho)+sum_(i<j) psi_(i,j)(e_i-e_j)(e_i-e_j)^t`, `rho_i>=0`.

For the indefinite Wave matrix `B_ii=0`,
`B_ij=-alpha_(i,j)/2` on nonadjacent Wave edges, this gives the exact
labeled-cell identity

`<B,G_T>=Q_n(T)=sum_(j>=i+2) alpha_(i,j)||T^-1 1_(U_i intersect V_j)||_2^2`.

Thus fixed-scale positivity is proved in the actual ordered-root dual without
paying C069's coefficient-PSD diagonal price.

C072 proves an exact rank-ramp domination in the same cone.  For
`eta_i=(i-c)/(2n)`,

`eta^tG_T eta-Q_n(T)`
`=sum_i rho_i eta_i^2+(1/(4n^2))sum_i psi_(i,i+1)(T)>=0`,

and the optimal shift and energy are

`c_*=(r^tG_T 1)/(1^tG_T 1)`,

`min_c eta^tG_T eta`
`=(r^tG_T r-(r^tG_T 1)^2/(1^tG_T 1))/(4n^2)`.

C073 records three exact scope gates.  The ungated ramp has small-scale
energy `(n^2-1)/(8n^2T)` and therefore diverges at zero; a signed band
difference can leave the SDDM/root cone; and the zero slack on every
nonadjacent Wave root forces every PSD Schur cross-block row to be constant.
Consequently an active gate, its finite boundary/terminal rows, and either
actual labeled-cell structure or a larger signed master are mandatory.

C074 retains only the disjoint left/right strip marginals and proves the
sharp fractional vertex-cover/transport hierarchy

`Q_n(T)<=V_n(T)<=P_n^PSD(T)/2`.

C075 shows that even this cheaper marginal-only price is not paid by the
positive same-epoch sector.  On the C070 eight-mark fixture,

`V_4=32755417/340707840`,

while `G_4<81908500355/936943462656`, with exact positive separation
`898545848033/103063780892160`.  The exact intersection cells, signed rows,
and cross-epoch/cross-phase mechanisms are not covered by this no-go.

C076 tests the unused negative-potential magnitude
`U_n=G_n-W_n=int N_n(T)dT` as an isolated nonnegative reserve.  The Golomb
fixture `(0,2,5,16,22,23,31,35)` has `N_4(2)=0` while `Q_4(2)>0`, and an exact
one-phase and continuum-phase audit shows that this reserve does not fully pay
the pair, marginal, coefficient-PSD, or finite-terminal prices.  This does
not discard the negative rows with their signed kernels.

C077 strengthens only the constant-fraction version.  For

`A_L=(0,2,5,16,L+16,L+17,L+25,3L+25)`, `L>=26`,

the isolated reserve converges to
`(9/64)(log(9/2)-1)`, whereas the integrated pair, marginal, and
coefficient-PSD prices diverge logarithmically.  No positive universal
fraction of those three prices comes from this isolated reserve.

C078 closes the tempting insertion of the optimal active ramp into the fixed
three full-prefix channel carrier when its baseline is paid only by the
positive same-epoch Gothic `lambda=beta` sector.  The rank-weighted ramp is
not in that formal three-channel span; a zero-mass fourth channel preserves
the old cover normalization but has the Schur price
`d>b^tH_3^-1b`; and active gating leaves a nonzero terminal.  On the same
affine Golomb family and `9<T<L`,

`Q_4(T)=9/(64T)-45/(64T^2)`,

`min_c eta^tG_T eta=27/(128T)-9/(16T^2)`.

The ramp baseline therefore has logarithmic coefficient `27/128`, whereas
the complete positive same-epoch Gothic sector has `18/128`; their gap is
`(9/128)log L+O(1)`, already positive by an exact bound at `L=2^18`.
This is a scoped no-go for that insertion and payment source only.  The
indefinite matrix `B` itself has zero surplus in the actual ordered-root dual,
so a direct labeled-cell signed rewrite remains open, as do disjoint external
reserve, cross-epoch or cross-phase payment, and a larger
membership-sensitive master.

C079 carries that indefinite matrix into physical point coordinates.  If
`D u=(u_i-u_(i+1))` and `M=D^tBD`, then every binary consecutive interval
state `u_[p,q]` of length `m` satisfies

`u^tMu=m^2/(4n^2)`

exactly for a strictly internal interval with `m>=2`, and is zero otherwise.
Consequently

`0<=Q_n(T)<=||sum_(k=0)^n delta_(b_k)*K_T||_2^2/(4n^2)`,

and the constant is sharp.  Moreover `M1=0`, `diag M=0`, and the literal
physical-pair identity is

`2M_(p-n,q-n+1)=lambda_(p,q)`.

Thus the direct `M` ledger is exactly the same Gothic mixed-difference ledger,
not new capacity.  Consecutive dyadic direct-pair supports are disjoint, but
their positive count baselines share one endpoint diagonal which still needs
one explicit owner.

C080 supplies the exact terminal-free signed Haar bridge.  For
`T_r=2^(r+theta)`,

`sum_(r=L)^U T_rQ_r`
`=sum_(r=L)^U 2T_r(Q_r-Q_(r+1))-T_LQ_L+T_(U+1)Q_(U+1)`.

Choosing `T_L<=m_*` and `T_(U+1)>=H` makes both endpoint rows exactly zero,
and

`G_T-G_(2T)=Gram((delta_(b_i)-delta_(b_(i+1)))*(K_T-K_(2T)))`.

After log-phase integration this is an exact common-coordinate representation
of `W_n/log 2` by signed direct-`B` Haar rows, with no hidden terminal.

C081 proves that those rows cannot be declared nonnegative or covered for
free by the aggregate full-prefix Haar square.  Exact contractions of both
signs occur:

`<B,G_3-G_6>=-1/324`,
`<B,G_200-G_400>=63/256000`.

On the actual half-open cell `[636,709)`, the current-block Haar state
`v=(-1,-1,1,1,0)` has `1^tv=0` but `v^tMv=1/8`; hence
`v^t(kappa J-mu M)v=-mu/8` for every `kappa` and `mu>0`.

C082 closes two zero-slack repairs only.  Singleton interval states have
`e_k^tMe_k=0`, so any scalar cover `(c^tu)^2<=C u^tMu` on all interval states
forces `c=0`.  Likewise root-restricted Schur nonnegativity on every
`(t e_i,y)` with positive-definite external block forces `X^te_i=0` for all
`i`, hence `X=0`.  Positive membership slack or genuinely constrained signed
actual states remain available.

C083 shows that the sharp C079 count baseline is neither free nor paid solely
by the positive same-epoch Gothic sector.  On `A_L` and `9<T<L`,

`B_count(T)=11/(64T)-9/(16T^2)`,

whereas the Wave density has leading coefficient `9/64`.  After integration,
the count baseline has log coefficient `11/64`, versus `9/64` for the
complete positive Gothic sector.  At `L=2^24` the exact gap is greater than
`1/32`.  This leaves a cheaper state-dependent PSD correction, signed
cross-epoch/cross-phase repair, and a larger master open.

C084 solves the exact one-epoch coefficient-trace LP on the complete 16-cell
`n=4`, `T=200`, `mu=1` fixture.  Within the nonnegative root-SDDM-plus-`J`
class, LP A has optimum `trace(C)=1/16` with `kappa` unpriced, while LP B has
optimum `trace(C+kappa J)=1/10`.  Both values have exact rational primal and
dual witnesses, and both zero exterior cells are retained.

C085 solves one substantive two-active-epoch/common-scale coefficient LP.
For the 16-mark Golomb fixture `a_k=k(k+100)`, the `n=4` and `n=8` blocks
share `a_7=749`; at `T=200` their 40-cell union has optimum `53/448`, zero
aggregate coefficients, and positive signed integrated Haar demand in both
epochs.  The shared correction entry is `C_(4,4)=47/1792`, recorded once in
the single global matrix `C`.

C086 supplies the missing physical objective for every `T>0` and `d>=0`.
For `g_T=1_[0,T)-1_[T,2T)`, one root has exact normalized energy

`chi_T(d)=3d/T` for `0<=d<=T`,
`chi_T(d)=4-d/T` for `T<=d<=2T`, and
`chi_T(d)=2` for `d>=2T`.

In particular `chi_T(T)=3`, not the coefficient-trace price `2`.  This
three-piece tent theorem is `HUMAN_PROOF_AUDITED`.

C087 solves the resulting physical root-SDDM-plus-`J` LP on two fixed common-
scale systems.  At `T=200`, the separate `n=4,n=8` optima are `29/200` and
`139/3200`, the joint optimum is `3809/22400`, and the strict saving is
`103/5600`.  At `T=2000`, the separate `n=4,n=8,n=16` optima are `299/2000`,
`1489/32000`, and `1477/128000`, the joint optimum is `163481/896000`, and
the saving is `11251/448000`.  Exact cell duals give zero gaps and strictly
positive contributions from every epoch.  These optima remain
`COMPUTATIONAL_FINITE` and supply no external budget owner.

C088 closes only literal scale-independent reuse of the displayed three-
epoch sparse weights and the changing quadratic finite family as a compatible
history.  At `T=2500`, cell `[6036,6516)` has correction `1/8`, demand `9/32`,
and slack `-5/32`.  For fixed integer `C`,
`a_3-a_0=3C+9=a_(C+5)-a_(C+4)` in `a_k=k(k+C)`; increasing `C` changes all
earlier marks.  Scale-dependent weights and a genuine recurrence on one
fixed history remain open.

Thus the local physical root cost is now exact and strict joint savings exist
on the stated fixtures.  The next theorem must organize them scale-adaptively
inside a legal finite-horizon common-history ledger across epochs, scales,
and phases.  On every capped compatible finite tower it must prove

`G_off-P-terminals >= epsilon_C log((J+1)/(j0+1))-K_C`.

The canonical cell-length dual gives `P>=weighted W`; feasibility and joint
saving alone are insufficient.  Only cover excess with an explicit one-for-
one `2M=lambda` cancellation may be charged.  The ledger must retain the exact
signed `M_s` rows, continuum phase, exact mixed-scale energy, and pay the
physical correction once from an owned resource.  It must have:

1. the centered covariance path entering with the favorable negative sign;
2. the Wave-19 harmonic atoms entering with the opposite sign;
3. the proved `lambda=beta` capacity map and C067 proportional pair allocation
   inserted by rewriting the existing Gothic rows, never by adding a second
   copy of their capacity;
4. no diagonal Parseval mass counted as off-diagonal gain;
5. no atom, renewal cut, boundary slack, or terminal term owned twice; and
6. an explicit finite terminal remainder bounded uniformly in the horizon;
7. either a direct labeled-cell signed argument using the indefinite `B`, or
   the exact required diagonal/Schur price paid explicitly from a singly
   owned signed, cross-epoch, cross-phase, disjoint, or larger-master reserve;
8. one compatible spatial-prefix history, not the changing finite family of
   the C065 no-go; and
9. every C066 prefix/scale initial, final, and terminal boundary row retained,
   with no negative band silently discarded;
10. if the ramp route is used, its active-gate first/last rows and low-pass
    terminal are singly owned, and its baseline is not charged only to the
    positive same-epoch Gothic sector;
11. a scale-adaptive physical membership correction on every actual Haar
    cell, not merely an aggregate `J` cover, coefficient optimum, or literal
    reuse of one fixed sparse correction;
12. one explicit paid owner for each shared endpoint diagonal, beyond merely
    recording it once in a global matrix; and
13. every birth, past-scale, active-gate, and final row retained in the same
    finite multi-epoch block.

Subtracting separately valid smoothing masters is inadmissible because each
has its own leading positive slack.  Likewise the full uncentered covariance
is inadmissible as the desired carrier because its harmonic contribution is
diagonal rather than `O(1)`.

The direct-`B` bundle passes 16 tests, rejects 16 mutations, and replays the
literal canonical JSON bytes; payload
`8f067c8e409b93058520b6e669de7eb4370e81c19b1c5abd988e1c0e68fc6ac2`.

The C084--C085 membership-SDDM bundle passes 12 focused tests, rejects 12
semantic/hash mutations, and replays the literal raw JSON bytes; payload
`d2620c68c366f765a1f5c502be65dfaf258558af93b9df5f4a50464d8fd52f23`.
Its independent exact audit checked the complete cell partitions, all primal
slacks and dual capacities, both zero gaps, Golomb validity, and shared-point
accounting.

The C086--C088 physical-energy bundle passes 16 focused tests, rejects 16
mutations, and replays the literal raw JSON bytes; payload
`3f406a1a6c7dfa19bf5172eadba5c5227ba175f4caf7811df6e53e5c75d3f630`.
Its independent audit checked the tent normalization and breakpoints, every
physical primal/dual objective and saving, cell-length dual, `T=2500`
countercell, and quadratic-family collision.  At the C098 checkpoint, the
Route-C bundle count was **291 tests PASS across 25 suites**.

Status: **OPEN — CENTERED INTERNAL CARRIER, SCALE/GOTHIC CAPACITY MAP,
EXACT PHASE TRANSPORT, LOCAL PAIR ALLOCATION, FIXED-SCALE ORDERED-ROOT
POSITIVITY, PHYSICAL-PAIR GOTHIC REWRITE, AND TERMINAL-FREE SIGNED HAAR BRIDGE
PROVED; FIXED-FIXTURE ONE- AND TWO-EPOCH COEFFICIENT-TRACE MEMBERSHIP REPAIRS
CERTIFIED; EXACT PHYSICAL ROOT COST AND FIXED-FIXTURE TWO-/THREE-EPOCH JOINT
SAVINGS CERTIFIED; SCALE-ADAPTIVE COMMON-HISTORY PHYSICAL-ENERGY PAYMENT,
SHARED-ENDPOINT BUDGET OWNERSHIP, AND ALL BIRTH/PAST-SCALE/FINAL ROWS MISSING.**
This is not Q1, Q2, publication, or prize evidence.

Primary P28 artifacts are
`endpoint_variance/WAVE19_P28_FULL_ROW_OWNERSHIP_AUDIT_2026-08-29.md`,
`endpoint_variance/WAVE19_P28_ADAPTIVE_ROW_CAP_CANDIDATE_2026-08-29.md`,
`endpoint_variance/WAVE19_P28_ARBITRARY_TRANSPORT_RESIDUAL_FLOOR_2026-08-29.md`,
and
`endpoint_variance/WAVE19_P28_MIXED_RIGHT_GREEDY_ENDPOINT_GAIN_2026-08-29.md`.

### Unnumbered C089--C096 narrowing of C058

C089 supplies a coefficient-mass-optimal universal endpoint star on every
ordered actual-Haar state, but C090 proves that its ungated low-scale physical
price is a positive constant and therefore diverges.  C091 gives the exact
orientation-sensitive unequal-scale Haar correlation.  C092 then proves the
finite mixed-scale cell-length identity

`physical cover price - integrated demand = sum_c |c| * cell slack >= 0`.

Thus a cross-scale block may reduce the sum of separate cover surpluses, but
it cannot price a cellwise-feasible cover below the integrated signed demand.
C093 makes shared-endpoint transfer membership-sensitive: the predecessor
root has slack `(4-m^2)/(8n^2)`, so `m=2` is tight and `m=3` is the first
failure.  C094 realizes the failure on the fixed two-epoch Golomb tower.

C095 certifies the complete open-chamber physical LP over `128<T<256` on that
fixed history: 22 event chambers, 30 exact optimality chambers, and 18 primal
vertices.  The C087 primal transports through `T=216,220` but fails at
`T=221`.  C096 proves that the optimal same-scale cover excess over the full
log phase is not zero on this fixture; it is at least
`56389/13934592` after the stated normalization.

Consequently C058 is the sole **primary research bottleneck**, not a claim
that only one lemma remains.  Its next admissible object must optimize
cross-scale **surplus** with membership-aware weights and simultaneously
exhibit the one-for-one `2M=lambda` cancellation and every owned boundary,
birth, past-scale, active-gate, terminal, and final row.  The fixed-fixture
results do not prove that such a master exists or fails.

### Unnumbered C097--C098 cross-scale surplus checkpoint

C097 solves one exact 14-channel finite LP on the fixed `n=4,T=200` and
`n=8,S=800` history.  Under a single common-cell inequality for the sum of
the two demands, the joint optimum is `1555757/6144000`: it lies strictly
above integrated demand `173/1024`, but below the sum of the two separate
optima by `10643/1228800`.  This proves finite surplus sharing only.

C098 prevents a stronger reading on this fixture.  An exact optimal dual has
strictly positive reduced-cost margin on all 45 cross-scale roots (minimum
`799/4000`) and on `J4`, `J8`, and `J_all`; complementary slackness therefore
forces all of them to vanish at every optimum exposed by that dual.  The
saving comes from same-scale surplus sharing across the weaker combined
constraint, not from a cross-scale root payment.

The next C058 probe must strengthen the model to separate epochwise or
signed-owned rows and then test whether a genuine cross-root/current-to-past
payment survives with the full boundary/terminal ledger.  C058 remains open.

### Registered C099--C110 obligation boundary

The preceding probe request has been executed.  Its exact finite conclusions
are now C099--C110, and they alter the next experiment without closing C058.

- C099--C100 show that the fixed 14-channel separately owned nonnegative model
  and its canonical conservative signed coordinate-row split both have optimum
  `134081/512000` and no active cross root.  C100's minimum cross-root margin
  is `237/500`; no other signed ownership law is quantified.
- C101--C102 show that the fixed 26-channel four-owner graph LP has equal full
  and no-cross optimum `156321/512000`, with all 676 cross columns excluded on
  that exposed face.  The `(4,800)` owner is inactive, and PSD, indefinite,
  other-phase, and other-history masters are outside the claim.
- C103 formally closes the generic finite prefix/scale curl and complete 2D
  Abel transport identities.  Lean's six registered theorems retain the
  initial and final epoch boundaries, interior epoch differences, scale
  differences, upper terminal, and zero horizon; Rocq independently checks
  only the curl lemma.  The Route-C sign, capacity, ownership, and analytic
  application remain obligations.
- C104--C106 close only the fixed canonical 52-coordinate graph/PSD basis and
  frozen C067 positive-pair terminal convention.  The graph cone costs more
  than `2D`; the larger PSD cone has a feasible `P<2D` witness, but the exact
  C106 dual and pair allocation force negative `Phi` throughout that fixed
  convention.  A complete signed-stencil replacement is a different basis.

For that replacement, C107 verifies one exact aggregate finite block.  On the
fixed `n=4,8`, widths `100,200,400,800`, terminal `1600` fixture,
`D=2069/10240`; an epoch-block zero-row-sum PSD matrix satisfies all 608 rows
and gives

`P=3900000000091/10000000000000`,

`Phi=141015624909/10000000000000>0`.

Its cross-epoch block is zero.  C108 proves within the four independent-width
subcone that
`P>=843669938599/2048000000000>2D` by
`16069938599/2048000000000`, so cross-width coupling must be retained in this
fixed aggregate PSD model.  The C107 Fejer gate works for `m>=4` and fails at
`m=3`.

C109 prevents upgrading aggregate rows to primitive ownership without a new
proof.  At owner `(4,200)`, cell `[709,725)`, the aggregate demand is
`-1/25600`, yet primitive `(5,7)` has positive demand `1/3200` and fixed-old-
`X` residual `-577653467/1690000000000`.  The associated left-edge cascade
closes only that old matrix and uniform orientation; it does not close direct
aggregate ownership or joint reoptimization.  C110 supplies one additional
phase point `t=4835/48`, with all 616 rows feasible and
`2D-P=246690436855133/2901000000000000>0`; it supplies no interval.

The remaining load-bearing obligations are therefore:

1. prove that the one-for-one aggregate four-corner Gothic replacement is a
   legal singly owned term in the finite master, or construct a genuinely
   reoptimized primitive/source allocation that survives C109;
2. build exact chamber-compatible witnesses over a complete phase interval,
   integrate them with the correct `log 2` normalization, and keep the C103
   terminal terms rather than inferring an interval from the two sample points;
3. close the failing Fejer rows `m=3,2,1` without duplicating Gothic capacity;
4. retain every birth, shared endpoint, initial, past-scale, active-gate,
   final, and scale-terminal row on one compatible finite history; and
5. prove a horizon-uniform positive master inequality before any asymptotic
   passage.

Status: **OPEN.**  C058 remains the sole primary research bottleneck in the
priority sense.  Neither Erdős question, a complete proof, novelty,
publication, nor prize eligibility follows; the global state is
`UNRESOLVED_AT_HARD_LIMIT`.

### Registered C111--C114 obligation boundary

Three former sub-obligations are now narrowed: aggregate net-row change of
basis is a formal finite identity; the complete fixed `n=4,8` quadratic phase
has positive exact margin; and the last three Fejér masters may be omitted at
`o(1)` cost after a legal core is supplied.  None gives an arbitrary-history
core.  The exact C114 lacunary dual shows why: Golomb distinctness alone does
not force positive epoch-block margin.

The remaining primary obligation is to prove, under the eventual critical
cap and at arbitrary adjacent dyadic size, a phase-integrated positive margin
or a signed span/gap-potential increment whose Fejér-weighted C103 Abel sum is
lower order.  A proof must also assign every shared endpoint, cutoff-final,
birth, and scale-terminal row once.  See
`CONTINUATION_2026-08-30_C058_FULL_PHASE_AND_HISTORY_DICHOTOMY.md`.

### Registered C115--C116 exact next inequality

Writing `H_k=N_(2^(k+1))-N_(2^k)`, C115 proves the signed Fejér sum of
`log(H_(k+1)/(4H_k))/(k+1)` is uniformly `O_C(1)`.  C116 supplies a linear
number of controlled 16-mark windows in each large shell.  It remains to
derive the legal phase-integrated PSD margin lower bound by that signed
increment, extend or localize it at arbitrary dyadic size, and insert it with
all C103 boundary and one-time owner rows.  This is the exact current C058
obligation.

### Registered C117--C119 sharpened obligation

Two shortcuts are now unavailable.  C117 shows that local PSD owner maps do
not automatically stitch across a shared coordinate.  C118 shows that the
signed total-span increment `eta_k` alone cannot support an error-free uniform
finite bridge in the current independent epoch-block cone even when
`eta_k<0` on a finite `k=2`, `C=2`-envelope fixture; its exact normalized
full-phase dual upper is below `-1/25`.

The first admissible enriched target is

`Phi_bar_k >= (epsilon_C - A_C eta_k - sum_r B_(C,r) Delta V_(k,r))/(k+1) - e_k`,

where every `V_(k,r)` is bounded and nonanticipating.  C119 proves that
`V_k=1-H_k^2/(2^k sum_i h_(k,i)^2)` has uniformly bounded Fejér-weighted
signed increments; ordered dyadic interval-mass coordinates have the same
bounded-telescope property.  What remains open is the local analytic lower
bound, not the global summability of these storage columns.

Before promotion, the enriched target must have exact phasewise primal
witnesses as well as dual stress tests, survive held-out and larger-rank
critical-compatible histories (including reverse-concentration and
same-multiset permutation rows), and assign every shared coordinate, birth,
cutoff-final, and scale-terminal row once.  C058 remains open and the global
status stays `UNRESOLVED_AT_HARD_LIMIT`.

### Registered C120 phase-integration correction

The reverse-concentration row now passes the enriched target for the complete
factor-two phase at `rho=9/16`: exact chamberwise primals give normalized lower
`>719/10000`, while the C119 prototype RHS is `<27/1000`.  However, an exact
dual on chamber 0 puts its normalized supremum below `2601/100000`, strictly
below the same RHS.  Therefore the remaining C058 obligation must be stated
after complete phase integration; a pointwise or per-chamber lower bound is
too strong even on this finite row.

The first exact C118 primal bank now gives normalized lower near `-0.04770218`,
while the prototype is near `-0.04104430` and the existing dual upper is near
`-0.04014304`.  Hence the target remains inside an unresolved exact
primal--dual window of about `0.00755914`; the constructed lower witness is not
a counterexample.  The next finite gate is to close that window, beginning
with the largest gap chambers 49, 73, 74, 64, 70 and the chamber-1
rationalization boundary.

It must then be followed by same-multiset ordered permutations, a larger-rank
or scalable critical-compatible family, and a single global owner ledger
containing every C103 initial, final, interior, birth, cutoff, shared-endpoint,
and scale-terminal row.  C120 is one held-out calibration and does not prove
that the scalar `V` separates arbitrary histories.  C058 and the global status
are unchanged.


### Registered C121 coefficient-box closure and remaining obligation

The old C118 fixed-primal/pointwise-dual interval is now superseded by an exact
reciprocal-subdivision upper certificate.  On the frozen positive-`Delta V`
C118 row in the current cone, the complete-phase normalized optimum is below
`-83/2000`.  Since `eta_2<0`, `Delta V>0`, `epsilon,A>=0`, and
`e_2=0`, any compatible scalar coefficient must satisfy

`B > 287434930599/860203021250 > 1/3`.

Thus the C119 prototype and every `0<=B<=1/3` fail on this row.  The
negative-`Delta V` C120 full-phase upper audit yields only the much weaker
restriction `B<0.9904` approximately, so the two known rows do not yet
contradict every scalar `B`.

The exact remaining finite obligation is to construct a multi-fixture outer
coefficient bank with complete-phase upper rows of both `Delta V` signs,
bounded ordered profile coordinates, same-multiset order permutations, and
held-out larger-rank or scalable critical-compatible histories.  Any surviving
candidate must then acquire exact primals and one global owner ledger
containing every C103 initial, final, interior, birth, cutoff,
shared-endpoint, and scale-terminal row.  C121 does not close C058, Q1, Q2,
novelty, publication, or prize eligibility.


### Registered C122--C124 two-column finite obligation

The scalar bank is now exact but noncontradictory.  C121 and C123 give the
clean necessary interval

`1341/4000 < B < 4753/10000`.

Let `C` denote the coefficient of the bounded chronological suffix potential
from C124.  With `d_+=3440812085/9234857208`,
`d_-=443620417/1928247678`,
`w_+=601940/4033029`, `w_-=13171/58179`,
`w_p=51059/581790`,
`lambda_+=log(1768/1659)`, and `lambda_-=log(215/82)`, the registered finite
dual fences imply the necessary half-planes

`d_+ B + w_+ C + 3 e_2 > epsilon + A lambda_+ + 249/2000`,

`d_- B + w_- C - 3 e_2 < 57/250 - epsilon - A lambda_-`,

and

`d_- B - w_p C - 3 e_2 < 219/2000 - epsilon - A lambda_-`.

These are finite cone-specific necessary conditions.  Their infeasibility has
not been proved, and positive `e_2` relaxes them.  Before solving the expanded
outer LP, the adaptive rule `T=(a_15-a_8)/8` must be frozen as the intended
nonanticipating C103/C116 phase selection, or representative independence of
the full factor-two average must be proved.

The next exact rows are ordered permutations chosen to expose opposite or
near-zero `Delta V_rt`.  A surviving coefficient vector still needs exact
primal witnesses, 32-mark or scalable critical-compatible stress, and one
global owner ledger containing every C103 initial, final, interior, birth,
cutoff, shared-endpoint, and scale-terminal row.  This is the current finite
front of C058; it does not close C058, Q1, or Q2.


### Registered C125 surviving rational vector and next obligation

The five-row necessary-side system now has the explicit rational survivor

`epsilon=A=1/1000`, `B=1/2`, `C=1/10`, `e_2=0`.

For each fixed row, exact rational logarithm enclosures and the fully replayed
dual give certified upper-minus-target gap greater than `1/10000`.  This does
not prove feasibility of the local PSD master: an upper certificate above the
target cannot replace a primal witness.

The next obligation is therefore not another fit to the same adaptive data.
First audit the C120/C123 same-multiset pair on one common completed-shell
factor-two phase.  If the rational vector survives, either construct exact
phasewise primals with uniform integrated slack or extend by the four ordered
quarter-mass coordinates and solve the new rational outer system on held-out
rows.  Only a surviving constructive mechanism should proceed to 32 marks or
a scalable critical-compatible family and one C103-complete global owner
ledger.  C058 remains open.


### Registered C126 common-phase noncontradiction and next obligation

On the fixed C120/C123 pair, the completed-shell choice `T=H_3/8=82` gives one
common phase `[82,164]`.  Every stored chamber dual and both endpoint slack
matrices replay exactly.  Under `epsilon=A=e_2=0`, outward-rounded C121 and
common-phase scalar fences leave

`1341/4000 < B < 1133/2000`,

whose exact width is `37/160`.  Because clean-window nonemptiness alone would
not prove exact noncontradiction, the certificate separately checks the exact
rational witness `B=1/2` against the exact C121 lower and both exact
common-phase uppers.  Therefore phase-base mismatch is not the missing scalar
contradiction.

The remaining obligation is constructive and global.  First test the
surviving rational coefficient vector against these common-phase rows and
construct exact phasewise primals with integrated slack on every retained
training row.  If that fails, add only the smallest chronological quarter-mass
coordinates needed to separate the failing row and re-solve the exact outer
system.  A surviving mechanism must then pass 32-mark or scalable
critical-compatible stress and be embedded in one C103-complete owner and
boundary ledger.  Global admissibility of `T=H_3/8`, arbitrary rank, C058,
Q1, and Q2 remain open.


### Registered C127 candidate nonseparation and primal obligation

On the common phase `[82,164]`, the fixed C125 candidate has exact certified
stored-dual margins greater than `21/500` on C120 and `7/1000` on C123.  The
comparison uses `normalized_dual_lower - target_upper`, so neither stored
certificate separates the candidate.  It does not establish that the primal
PSD target is attainable.

The first remaining obligation is therefore to solve the complete-phase
primal side for this exact candidate on every retained row.  A success must be
promoted to rational Gram factors with endpoint and integral slack; a failure
must identify a precise chamber/epoch obstruction before adding the minimum
chronological quarter-mass coordinates.  Only then should the route proceed
to 32 marks/scalable histories and a single nonanticipating C103 owner and
boundary ledger.  C058, Q1, and Q2 remain open.


### Registered C128 pointwise no-go and phase-integrated primal obligation

For the fixed C125/C127 candidate
`(epsilon,A,B,C_rt,e_2)=(1/1000,1/1000,1/2,1/10,0)` on the common phase
`[82,164]`, the exact C123 stored local dual separates precisely chambers
`0,1,...,21` in the frozen independent epoch-block cone.  Chamber 0 is
`[82,493/6]`, where the target is `>9/250`, the normalized local-dual upper is
`<39/2000`, and the certified deficit is `>33/2000`.  Because a pointwise
lower throughout a chamber would imply the corresponding positive `dt/t`
average lower, the fixed target cannot hold uniformly chamber by chamber or
at every phase in this cone.

The C120 stored-local-dual separation count of zero is not a C120 primal
witness.  C128 does not make the physical phase impossible and supplies no
integrated primal feasibility or infeasibility certificate.  In particular,
the separate floating integrated screen is heuristic only and is excluded
from the proof claim.

The first remaining finite obligation is therefore **not** another pointwise
or per-chamber construction.  It is to build an exact phase-integrated
rational primal bank whose later-chamber surplus pays the early C123 deficits,
with exact integrated log sums and every boundary, terminal, and owner row.
A surviving bank must then pass scalable critical-compatible stress and be
embedded in one nonanticipating C103 ledger.  C058 remains the sole primary
bottleneck; Q1, Q2, arbitrary rank, and the global ledger remain open, and the
project status remains `UNRESOLVED_AT_HARD_LIMIT`.


### Registered C129 selected-bank success and complete-phase obligation

For the fixed C123 candidate and common phase, C129 gives exact rational
primal factors for nested selected chamber banks.  The initial deficit block
is `0,...,21`.  Its union with the frozen top-six surplus selection still has
raw margin `<0`; the 29-chamber sparse-seven bank has 58 factors and margins
raw `>1/15000`, normalized `>99/1000000`; the 32-chamber robust-ten bank has
64 factors and margins raw `>143/400000`, normalized `>103/200000`.

The robust-bank owner census is 12,140 generic rows, 24,280 generic endpoint
inequalities, and 23,745 collapsed-endpoint rows.  Independent exact audit
recomputed minimum owner slack
`333523392719/67812500000000000>0` and found no load-bearing defect.  This
closes only the selected integrated sub-bank, not the full phase and not a
universal minimality statement about the number of surplus chambers.

The immediate C130 obligation is exact and finite:

1. store all 135 C123 chamber records and both epoch factors for each, for 270
   factors total;
2. supply the missing 103 chambers / 206 factors rather than zero-extending
   them—chamber 22 already has positive demand `1/32`;
3. reproduce exact owner census totals 51,355 generic rows, 102,710 endpoint
   inequalities, and 100,183 collapsed-endpoint rows; and
4. prove the complete exact aggregate raw margin is strictly positive.

After this finite gate, the separate C103 obligation remains: one
nonanticipating phase rule and one global owner/boundary/Abel ledger must
support the same mechanism.  C129 proves no complete-phase witness, arbitrary
rank theorem, global ledger, C058, Q1, or Q2.  The project status remains
`UNRESOLVED_AT_HARD_LIMIT`.


### Registered C130 complete-C123 success and two-row/global obligation

For the fixed C123 row, fixed candidate, common phase `[82,164]`, and frozen
independent epoch-block aggregate cone, C130 supplies all 135 chamber records
and 270 exact rational Gram factors.  The denominator is `100000000`; ranks
range from 9 to 25 and sum to 4288.  The exact replay closes owner totals
51,355 generic rows, 102,710 generic endpoint inequalities, and 100,183
collapsed endpoint rows.  Structural-zero totals are 31,805 generic and
interior rows and 62,713 collapsed rows; owner recovery totals are 10,395
state evaluations and 20,790 separate epoch checks.  The endpoint objective
totals are 540 separate / 270 weighted, and the interior totals are 270
separate / 135 weighted.  Minimum active owner slack is

`1137298595103/235750000000000000>0`.

The complete exact integral has raw margin `>1/400`, normalized margin
`>91/25000`, and enclosure width `<1/10^26`.  Its 37 negative pieces are
exactly `0--26,31--35,59,60,77--79`; 98 pieces are positive.  Thus the
obligation is closed only after complete phase integration, not pointwise.
Temporary floats were stripped from the accepted payload.  The exact-only
canonical artifact passes nine focused tests and 28 mutation rejections; an
independent audit found no P1/P2 defect.

The immediate remaining finite obligation is now:

1. exactify the complete C120 common phase for the same fixed candidate;
2. retain exact per-epoch owner recovery, endpoint/interior objectives,
   structural-zero rows, and complete rational log integration;
3. combine the resulting C120 and C123 witnesses only as a **two-row finite
   bank**, without inferring sufficiency for every row; and
4. construct the cross-row/global C103 nonanticipating phase/owner/Abel ledger,
   including every boundary, terminal, cutoff, shared-endpoint, and one-time
   owner row.

C130 does not prove a C120 witness, every-row validity, representative
independence, a local master inequality, arbitrary rank, C058, Q1, Q2,
novelty, publication acceptance, prize eligibility, or Erdős Problem #1191.
C058 remains the sole primary bottleneck and the project status remains
exactly `UNRESOLVED_AT_HARD_LIMIT`.

### Registered C131 complete-C120 success and cross-row/global obligation

For the fixed C120 row, fixed candidate, common phase `[82,164]`, and frozen
independent epoch-block aggregate cone, C131 supplies all 147 chamber records
and 294 exact rational Gram factors.  Exact ranks sum to 3205.  The first 115
records retain the pinned provenance at scale `1/D^2`; the final 32 use the
reduced scale `1/(D^2 midpoint)`.

The exact census is 53,312 generic active rows, 37,240 generic zero rows,
106,624 generic endpoint inequalities, 104,080 collapsed active rows, 73,440
collapsed zero rows, 53,312 midpoint active rows, and 37,240 midpoint zero
rows.  Minimum active slack is

`305733/87500000000000>0`.

The complete exact integral has raw margin `>21/1000`, normalized margin in
`(3/100,31/1000)`, and every relevant rational enclosure has width
`<1/10^26`.  All 147 integrated chamber pieces are positive.  This closes the
fixed C120 complete-phase primal only; it is not an all-phase pointwise or
every-row assertion.

C130 and C131 now form a two-row finite primal bank.  The immediate remaining
obligation is:

1. audit cross-row compatibility without treating C120/C123 as representative
   of every admissible row;
2. prove the completed-shell phase rule is nonanticipating and globally
   admissible in the intended finite-horizon construction;
3. construct one C103 phase/owner/Abel ledger containing every boundary,
   terminal, cutoff, shared-endpoint, birth, and scale-terminal row exactly
   once; and
4. stress the resulting mechanism at 32 marks or on a scalable
   critical-compatible family before any arbitrary-rank promotion.

C131 does not prove two-row sufficiency, representative independence, a local
master inequality, arbitrary rank, C058, Q1, Q2, novelty, publication
acceptance, prize eligibility, or Erdős Problem #1191.  C058 remains the sole
primary bottleneck and the project status remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.

### Registered C132--C134 joint epoch-8/16 obligation

The admissible finite target is no longer an unspecified cross-row stitch.
It is the following explicit gate on the C132 32-mark fixture:

1. use the natural physical state ranks `15..31` and keep every one of the 63
   C134 cross-half sources;
2. use one common physical phase and prove that its selection is
   nonanticipating for the finite history under test;
3. introduce a genuinely positive-capacity Gram variable; the exact signed
   representation `X_plus-X_minus` is demand data, not capacity;
4. enforce all fourteen C133 rows: four initial `A8`, four net shared `A16`,
   four final `A32`, and two upper scale terminals;
5. owner-partition every coordinate row exactly once, with rank 15 owned by
   epoch 8 and ranks 16--31 by epoch 16 in the natural test;
6. retain birth, prebirth-zero, cutoff, shared-endpoint, final, diagonal, and
   scale-terminal contributions rather than absorbing them into an unnamed
   remainder;
7. cover the whole declared phase partition and every declared cell; and
8. independently replay PSD, owner equalities, objective/margin, finiteness,
   source hashes, and any rational certificate.

C132 already closes the naive affine local-bank paste and its exactly aligned
affine subfamily.  C134 closes positive-Gram-only representation of the
residual but does not close a joint positive-capacity master.  These are
genuinely exhausted strict subroutes, not evidence against fractional or
cross-block ownership, a fresh joint program, another ruler, or arbitrary
rank.

Only after the finite gate passes may the proof seek a rank-uniform
product-BMO testing or fixed-complexity transport theorem and then use the
C116 controlled windows.  Until that promotion is proved, C058, Q1, Q2, and
the main Erdős problem remain open.  The project status remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.

### Registered C135 frozen-rotation no-go and surviving obligation

C135 adds one exact finite veto, not a new global theorem. For the fixed O0N1
row, common phase `[82,164]`, `rho=9/16`, fixed candidate coefficients, and
the current independent epoch-4/epoch-8 aggregate cone, its 314-piece exact
complete-phase dual has `U^+<T^-`. The exact bank contains 628 epoch duals,
193,424 nonnegative rational weights, and 1,256 endpoint Bareiss-PD checks.
Classification occurs only after complete-phase summation; there is no
chamberwise sign acceptance gate.

Therefore the universal assertion that every Golomb member of the specified
frozen `4x8` cyclic same-multiset rotation bank satisfies the frozen candidate
lower bound is false, with O0N1 as a weak-duality counterexample. This does
not refute global representative independence, and C130's O0N0 certificate
remains valid in its own scope.

The earlier one-stored-dual-per-parent-chamber `NO_SEPARATION` bank has also
been replayed exactly. It was a false negative as an infeasibility classifier,
not primal feasibility; C135 makes no optimality claim about all unsplit
duals. The surviving obligations are still cross-row compatibility, a
globally admissible nonanticipating phase rule, one complete C103 owner/Abel
ledger, and the arbitrary-history/rank bridge. C058 remains OPEN and the
global status remains `UNRESOLVED_AT_HARD_LIMIT`.

### Registered C136 direct-owner feasibility and surviving charge obligation

C136 closes one narrower question: at the displayed 32-mark fixture and the
single phase `17745/32`, the fresh positive graph-root cone can satisfy every
direct full-`M8`/full-`M16` owner-cell inequality with `P<2D`. This is exact
finite feasibility, not a solver-status claim.

The remaining finite obligation is stronger and must not be replaced by free
prefix/scale variables. A valid successor must:

1. define each prefix/scale potential from the same physical capacity atoms;
2. make all fourteen C133 rows literal differences of that potential;
3. retain the multiplier-16 terminal rows formally and evaluate their actual
   same-atom values; on the current fixture those aggregate values are zero;
4. retain full `M16`, all 63 cross-half sources, rank 15, and one-time owner
   partitions;
5. prove the resulting charge equality or inequality on every declared cell;
6. avoid post-hoc fixture-fitted scalar normalizations; and
7. pass independent exact replay before any phase-interval or arbitrary-rank
   promotion.

The one-sided box carrier audited in C136 cannot simply be identified with
the direct-demand potential. Full fourteen-row feasibility and infeasibility
are both still unknown. C058 remains OPEN.

### Registered C137 no-go and corrected C138 target

C137 exhausts every pointwise memoryless map from the current C136 graph state
to the one-sided box carrier. It does not exhaust the direct-`M` cumulative
potential. The next accepted finite formulation must use

`C8_s=B_s`, `C16_s=B_s+U8_s`, `C32_s=B_s+U8_s+U16_s`,

so that the two prefix increments and the C133 weighted direct demands agree
by definition rather than by fitted coefficients. The baseline `B_s` must be
the retained pre-8 history (for a finite fixture it may be instantiated by the
epoch-4 direct potential), not an unexplained global zero.

The current C136 witness is insufficient because it proves an unweighted
margin only. The required solver gate uses `w8=1,w16=9/16`, exact owner
shares, and the same physical price. It must certify a positive weighted
`2D-P` or return an exact dual no-go. C058 remains OPEN regardless of the
finite outcome.

### Registered C138 fixed-phase weighted same-atom success

C138 satisfies the corrected finite formulation at exactly one phase. It
uses the direct atoms themselves:

`C8=B`, `C16=B+U8`, `C32=B+U8+U16`,

so the two prefix increments and the C133 weighted direct demands agree
without fitted prefix variables. The finite `4+4+4+2` identity is also
checked in Lean. Both terminal keys remain explicit and their direct-M values
are verified to be zero on the fixture.

The exact 57-root witness satisfies all 1,192 weighted owner rows and the
separate pre8 nonnegative-owner gate. With weights only on the demand RHS,
the full single physical price satisfies

`2D-P=296239592131/16716398592>0`.

This closes neither the general terminal obligation nor C058. Acceptance of
the next stage requires:

1. extend the witness over a proved rational phase interval, checking every
   collapsed endpoint and every internal ledger chamber;
2. cover a complete factor-two phase domain or give a legal nonanticipating
   phase-selection theorem;
3. stress nonzero initial, cutoff, and terminal history rows rather than rely
   on this five-nonzero-row degeneracy;
4. promote the owner/master construction uniformly to arbitrary adjacent
   dyadic ranks; and
5. embed it in one C103-complete global owner/boundary/Abel ledger before any
   asymptotic conclusion.

C058, Q1, Q2, publication, and prize readiness remain OPEN.

### Registered C139 fixed-Y maximal connected chamber

C139 upgrades the C138 midpoint only inside one frozen graph. For the explicit
C132 fixture and the exact C138 graph Y, every weighted owner row and pre8
share is nonnegative on the maximal connected closed chamber [4425/8,555].
The margin is affine and remains positive at both endpoints. The immediately
adjacent chambers have exact negative owner slacks, so no connected extension
of this same Y through either boundary is possible.

This closes the fixed-Y local chamber computation, not phase coverage. The
remaining obligation is to construct a complete factor-two phase bank, prove
that its chamber/witness choice is nonanticipating, stress nonzero initial,
cutoff, and terminal histories, promote uniformly to arbitrary adjacent
dyadic ranks, and embed the result in one C103-complete global owner ledger.
C058, Q1, Q2, publication, and prize readiness remain OPEN.
