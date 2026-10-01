# Proof Obligations — Erdős Problem #1191

**Updated:** 2026-08-29 continuation, Wave 0--13  
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
