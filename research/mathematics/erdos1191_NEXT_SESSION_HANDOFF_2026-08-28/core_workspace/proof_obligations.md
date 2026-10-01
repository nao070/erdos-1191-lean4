# Proof Obligations — Erdős Problem #1191

**Updated:** 2026-08-29 continuation, Wave 0--19  
**Current global status:** unresolved

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

The exact remaining P28 obligation is

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

Status: **OPEN — CURRENT HIGHEST-VALUE LEMMA IS SIGNED WHOLE-CUT CONTROL OF
`Gmix`, NOT A FURTHER TRANSPORT LEMMA.**

Primary P28 artifacts are
`endpoint_variance/WAVE19_P28_FULL_ROW_OWNERSHIP_AUDIT_2026-08-29.md`,
`endpoint_variance/WAVE19_P28_ADAPTIVE_ROW_CAP_CANDIDATE_2026-08-29.md`,
`endpoint_variance/WAVE19_P28_ARBITRARY_TRANSPORT_RESIDUAL_FLOOR_2026-08-29.md`,
and
`endpoint_variance/WAVE19_P28_MIXED_RIGHT_GREEDY_ENDPOINT_GAIN_2026-08-29.md`.
