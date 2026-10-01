# Next Lemma Targets: Anti-Eulerian Multiscale Rigidity

## Continuation disposition — 2026-08-29

### Wave 18 correction and exact next theorem

- Exact target-interior row capacities satisfy `w_(n,p)>=r_(n,p)` and the
  unused sorted-rank slack gives
  `Theta_n^(exc,h)<=H_n^loc+J_n^(h)` with no atom reuse.
- At `h=5/2`, `D_n>15/16` eventually pays the source-`n/2` capped term.
  Substitution into the Wave 16 identity gives
  `Z_n-R_(2n)=mathfrak P_n-K_n^int-mathcal T_n`
  `-Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)+J_n^(5/2)-(U_n+Q_n)`,
  with all three remainders `mathcal T_n,U_n,Q_n` nonnegative.
- An exact rank-layer allocation proves all-source reuse is summable for each
  fixed future difference.  On an eventual-`C` branch its post-cap load is
  `<[8C log2/(3exp(h))]log(4x)/x` eventually.
- Finite Erdős--Turán rulers show one-epoch local slack need not diverge; a
  distant-block construction shows the terminal identity alone is
  insufficient without the critical cap.
- The exact q-collapse is
  `J_n^(h)<=sum_p r_(n,p)[log(d_(n,p)/D_(p,n))-(h-log3)]_+`.
  Scalar alternating jumps and terminal-cap-compatible finite Golomb
  prefixes show that neither positive-part telescoping nor a one-epoch
  strengthening can prove the required little-oh.

**Current highest-value lemma (P23).** Prove, on one fixed infinite
eventual-`C` integer Golomb branch,

`sum_(k<=J) omega_(k,J)J_(2^k)^(5/2)=o_C(log J)`,

or an exact signed cancellation of this functional against
`mathfrak P_n-K_n^int-mathcal T_n`.  A valid proof must control birth delay,
authenticate unused capacity at every nonterminal birth carrier, retain the
terminal births in the renewal ledger, and handle the renewing band
`n/2<p<=n`.  Pointwise rank stabilization, tapering alone, or reuse bounds
without a birth-time moment do not prove P23.

### Wave 17 correction and exact next theorem

- A same-atom residual above the Wave 11 triangular floor proves
  `mathfrak B_(2m)>=K_(2m)^int+[log(3/2)/12]Delta_m`
  `-2146log(3/2)/(16m^2)`.
- The exact sorted-rank floor on the same target-interior atoms leaves a
  surplus `D_n` satisfying
  `|D_n-[3/2+(3/4)log3-2log2]|<=18(1+log n)/n` for `n>=16`.
- Hence `D_n>81/128` from `n=2^20` and `D_n>3/4` from
  `n=2^22`.  One single stronger floor pays `3Delta_m/8` eventually, or
  alternatively the residual `u-v` promotion truncated at height two.
- This closes P21's local triangular-floor capacity gate.  The two uses are
  alternatives, not additive charges.

**Historical Wave 17 highest-value lemma (P22).**  Put

`Theta_m^exc=sum_p (u_(m,p)-v_(m,p))(P_(m,p)-2)_+`,

where `P_(m,p)=log(rho_infinity(d_(m,p))/rho_(2m)(d_(m,p)))`.
Prove a bounded-reuse signed allocation of

`sum_k omega_(k,J)Theta_(m_k)^exc`

to actual local slack, unused local rank surplus, and exact renewal terms,
with cumulative loss `o(log J)`.  Insert the result into

`Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`,
`mathcal T_m>=0`, retaining every endpoint and descendant term.

The proof must authenticate every carrier across all source epochs, must not
spend `D_n` twice, and must not infer a signed upper from a positive bulk
lower bound.  Finite Hall/ET rows do not construct an eventual-critical
branch. Wave 18 proves the exact signed insertion and all-source rank-layer
reuse portions, leaving only the P23 birth-time/descendant-jump estimate above.

### Historical Wave 16 correction and P21 target

- Disjoint future blocks strengthen the Wave 14 promotion to
  `rho_infinity(d)-rho_L(d)>d/(128C log2)` for every macroscopic old
  `d>=L^2/8` once the explicit eventual-cap side condition holds.
- With `kappa_C=log(1+1/(128C log2))`, the legal next-shell rebate is at
  least `kappa_C/6` and the residual `u-v` promotion at least `kappa_C/3`
  per sufficiently large epoch.
- Exact renewal expansion gives
  `Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`,
  `mathcal T_m>=0`.  The true terminal upper is `O_C(log J)` at
  `m=2^J`, not the historical isolated-fan `Theta(J)` estimate.
- Fejer weights preserve `sum omega/k=log J+O(1)`, make the raw terminal
  fan negligible, give favorable renewal signs, and reduce one-step
  allocation mismatch to `O(1)`.

**Historical Wave 16 highest-value lemma (P21).**  Prove a genuinely disjoint capacity
inequality such as

`mathfrak B_(2m)>=chosen_existing_floor+c Delta_m-epsilon_m`

with a quantitatively sufficient fixed `c>0` and total weighted error
`o(log J)`, or an equivalent bounded-reuse allocation for the constant-size
residual `u-v` channel.  The terminal horizon is repaired; the exact
bottleneck is now double use of the same `beta log D` bulk capacity.

Wave 17 proves this local inequality for the triangular floor, including
explicit constants, summable error, and a stronger sorted-rank version.
The proof still must retain the renewal tail and must not infer a
contradiction merely by comparing lower bounds on positive resources.

### Historical Waves 13--15 correction and target

- Wave 13 proves the integer harmonic barrier
  `Y_m,Z_m>=m^2/(384H_m)` and the exact frontier
  `X_m=mathfrak U_m-mathfrak B_m` up to a summable one-sided boundary.
  Under a hypothetical eventual-`C` branch, `sum X_m` has a positive
  `Omega_C(log J)` lower bound.
- Wave 14 proves cap-dependent future-rank promotion
  `rho_infinity(d)-rho_L(d)>=d/(64C log d)` and a legal next-lower-shell
  rebate `A_J>=K_J^star+Phi_(J-1)`.
- Wave 15 proves that the immediately realized marginal promotion
  `Delta_m` has total nested load below `3/(4m^2)` per new numerical
  difference and fits into the full next Gothic bulk up to `O(m^-2)`.
- The Wave 15 allocation is not disjoint from the old rank/length floors.
  Its isolated terminal-fan estimate is corrected by Wave 16; the
  all-epoch late-birth `4^k` coefficient mismatch remains.

**Historical Wave 15 highest-value lemma (P20).**  Prove either

`mathfrak B_(2m)>=existing_floor+c Delta_m-summable_error`

with an exact terminal potential, or prove
an all-epoch bounded-overlap birth-time allocation for

`u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2)`.

The proof must retain the terminal channel and must not double-spend the
selected bulk values already used by a floor.  Charging raw
`u_(m,p)log d_(m,p)` to the local witnesses is explicitly rejected.  The
all-`C` P17/P18 statements are Question-1-equivalent contradiction targets,
not subordinate decay lemmas.

Wave 16 supplies the terminal potential/taper part, Wave 17 supplies the
local disjoint-capacity part, and Wave 18 inserts the excess up to the single
descendant-jump functional.  The surviving problem is P23's birth-time
estimate.  The Wave 12 subsection below is historical and supplies the
cut-renewal foundation for this target.

### Wave 12 correction and exact next theorem

- For the Wave 11 future cut tail `R_m`, four explicit nonnegative sectors
  satisfy `Y_m=R_m-R_(2m)+Z_m` coefficientwise.
- Over `E_J={4,8,...,2^J}`, this gives
  `sum Y_m=R_4-R_(2^(J+1))+sum Z_m`.
- Every fixed pair now has uniformly summable total `Z` coefficient.  The
  remaining burden is packing the mass of different integer interval pairs.
- The jointly optimal floor from numerical rank, triangular length, and the
  complete containment poset gains less than `5` per epoch beyond `K^len`.
- The real quadratic Golomb ruler `a_n=n^2+sqrt(2)n` has nondecaying `Y_m`.
  Therefore the missing proof must use integer unit spacing or an equivalent
  arithmetic fact.

**Historical Wave 12 highest-value lemma (P18).**  On one fixed infinite normalized
integer Golomb ruler with `a_n<=C n^2 log(2n)` eventually, prove

`sum_(m in E_J)Z_m=o_C(log J)`.

This is sufficient for P17; it is not asserted equivalent because the
terminal positive `R` tail remains.  Seek a bounded-overlap injection across
different integer pairs, crossing interval-sum arithmetic, or a full
product-tree encoding that retains exactly that arithmetic.  Do not return to
abstract real-Golomb uniqueness, fixed-pair summability, or another
rank/length/containment floor.

The Wave 11 subsection below is preserved as the derivation of P17.  Its
  “single highest-value” label is historical and is superseded by P23 above.

### Wave 11 correction and exact next theorem

- Every length-`ell` interval difference satisfies
  `D_(p,q)>=binom(ell+1,2)`.  With the exact Abel coefficients this gives the
  local floor `K_m^len=2log m+O(1)`, split into lower-shell
  `(1/2)log m+O(1)` and interior `(3/2)log m+O(1)` contributions.
- This unconditionally repays the complete leading
  `(1/4)sum log m` missing from the Wave 10 `7/4` global spectrum floor.
- Define `G_m^len=A_m-K_m^len>=0`.  The exact three-channel identity is
  `T_m-K_m^len=Y_m+G_m^len+S_m`, with all terms on the right nonnegative.
- The direct eventual-critical envelope is now `O_C(J log J)`, not the old
  displayed `O_C(J^2)`, but it is still not `o(log J)`.
- The lower residual is an exact positive future cross-ratio tail.  A fixed
  pair has dyadic multiplicity `Theta(log(j/i))`, so no uniform same-atom
  birth charge can close the sum.
- Another within-length shifted-factorial sort improves the floor by only
  `O(m^(-1/2))` per shell and hence `O(1)` over dyadic epochs.

**Historical Wave 11 highest-value lemma (P17).**  On one fixed infinite normalized Golomb
ruler with `N_n<=C n^2 log(2n)` eventually, prove that some
`epsilon_J>=0`, `epsilon_J=o(log J)`, satisfies

`G_J^len+S_J >= T_J-K_J^len-epsilon_J`.

Equivalently, prove

`0<=sum_(m in E_J)Y_m<=epsilon_J=o(log J)`.

The proof must use cross-length allocation, the exact future-tail telescope,
or a genuinely survival-conditioned state.  It must distinguish a single
`surv_C=infinity` ray from changing finite Erdős--Turán windows.  Do not spend
another wave on an independent diameter bound, fixed-length product sort, or
uniform same-pair birth charging unless it introduces a new coupling that
escapes E54--E56.

The separate Route B remains a full bi-/tri-tree positive-measure encoding
with a summably vanishing product-box profile.  It is not proved equivalent to
P17.  The Q2 secondary route remains uniform arbitrary-depth finite
feasibility under one coordinate cap followed by König compactness.  Status:
`UNRESOLVED_AT_HARD_LIMIT`; no prize claim is ready.

The remaining dated sections below are historical dispositions retained for
audit continuity.  Their phrases “exact next theorem” and “next target” name
the target at that earlier wave; the sole current highest-priority lemma is
P23 at the top of this file.

### Wave 10 correction and exact next theorem

- Arbitrary weighted birth intervals satisfy the hereditary laminar inequality
  `sum r beta_r <= sum lambda*d <= sum N_(2m)Gamma_m`; W9-RLP is its unit
  lag-rectangle case.  The corresponding selected-difference product is at
  least `M!`.
- At every fixed old gap position, the endpoint-product/inverse-difference
  future load has tail at most
  `(4/3)(log 2+1/e)4^(-K)`.  Therefore any persistent mass must migrate to the
  advancing frontier.
- The exact negative Abel bulk uses right-end bands `[m-1,2m-2]`, disjoint
  across dyadic `m`.  Its simultaneous global rearrangement floor is
  `F_E=(7/4)sum_(m in E)log m+O(|E|)`.
- The plain certificate still misses the positive boundary by a leading
  `(1/4)sum log m` plus secondary `log log` slack.  This is a rigorous limit
  of the exposed signs plus global distinct-positive-integer information, not
  a statement about the actual shell sum.
- In the fixed-modulus tile LP, every existing W9-RLP row has zero coefficient
  on every occupancy variable.  The literal concatenated LP therefore has the
  same primal and dual optimum.  A new mixed row is mandatory.
- The exact finite audit checks 9,845,549 subset/cutoff selections through 128
  marks with zero violations, exact primal=dual, and a 512-mark LP/actual
  fixed-`H` ratio about `363.799`.  These are finite no-go calibrations only.

**Sufficient candidate Route A:** let `A_J` be actual bulk log mass, `Q_J`
the exact positive-fan mass, `T_J=sum theta_m log a_(2m-1)`, and set
`P_J=A_J-F_E`, `S_J=2T_J-Q_J>=0`, `U_E=T_J-F_E`.  The exact identity is

`sum_(m in E_J)Y_m=U_E-P_J-S_J`.

On one fixed infinite normalized Golomb ruler with
`N_n<=C n^2 log(2n)` eventually, prove that there is `epsilon_J>=0`,
`epsilon_J=o(log J)`, with

`P_J+S_J >= U_(E_J)-epsilon_J`.

The stronger bulk-only or lower-shell-only repayment would also suffice, but
is not known to be necessary.  A lower-shell allocation needs an additional
global accounting lemma because `F_E` is sorted across all coefficient classes
and epochs.  The proof must use `surv_C=infinity`; another independent
factorial or magnitude-band capacity is exhausted by the `7/4` theorem.

**Separate sufficient candidate Route B:** split the tile objective into endpoint-limited
`R^2XY` and difference-limited `R^2Z^2`, encode them on full tri-/bi-trees
with tensor weights and arbitrary positive measures, dominate the exact core
by the Hardy embedding energy, and prove a summably vanishing one-box constant
from contiguous-sum uniqueness and survival.  Route B is not currently proved
equivalent to Route A or necessary for every solution of P15.

Mandatory falsification gates:

1. the new inequality must have nonzero coefficients on both the endpoint/
   Abel state and the rank-lag/survival state;
2. it must distinguish one infinite ray from changing scaled Erdős--Turán
   windows and bounded extension trees;
3. fixed-position decay alone is insufficient because the frontier moves;
4. arbitrary pruning is invalid under the product-weight embedding theorem;
5. the known `T^4` result blocks a proof mechanism, not every possible
   four-parameter theorem;
6. any claimed premium must be tested against `(0,s,4s,6s)` and every
   authenticated Wave 6--10 fixture.

The secondary Q2 route remains uniform arbitrary-depth finite feasibility
under one fixed coordinate cap followed by König compactness.  Status:
`UNRESOLVED_AT_HARD_LIMIT`; no prize claim is ready.

### Wave 9 scalar correction and exact next theorem

- The full positive birth budget is quantitatively equivalent to a scalar
  dyadic rank-variance sum:
  `(4/49)sum V_(2^k)<=B_H<=(36/35)sum V_(2^k)`.
- Distinct genuine adjacent gaps force `V_n>=n^2/(512N_n)`.  Under a
  hypothetical `C`-critical branch this already gives
  `B_H(J)>=(6272C log2)^(-1)log J+O_C(1)`.  The missing upper must use every
  non-adjacent contiguous sum on the same branch.
- Short-rank or small-endpoint atoms have cumulative cost `O(log log J)` after
  the canonical Wave 9 cutoffs.  The only surviving mass is a long-rank,
  two-large-endpoint core with exact `(R,X,Y,Z)` tile bounds.
- Local numerical sparsity is insufficient: changing scaled Erdős--Turán
  windows have birth charge at least `1/2352` and retained cross-ratio
  potential at least `1/4096` while numerical difference density vanishes.
- Complete bounded searches refute pointwise birth monotonicity, a literal
  harmonic schedule, one-atom static cells, and occupancy bounded by rank-band
  lower endpoints.  Long finite 512-mark fixtures retain more than `3/5` of
  their terminal charge in the macroscopic core quadrant.
- A genuine weighted cross-ratio potential majorizes every non-adjacent
  endpoint product.  Its Abel coefficients and primitive factorial upper are
  exact, and its dyadic recursion is exact, but its birth sum remains
  comparable to a positive state sum.
- Ma--Yi/Shearer yield the valid hereditary rank-lag inequality `(W9-RLP)` on
  arbitrary epoch subsets.  It is linear in difference lengths and does not
  control the exact product/kernel objective.

**Single exact next theorem:** on one fixed infinite normalized Golomb ruler
with `N_n<=C n^2 log(2n)` eventually, prove survival-conditioned
cross-epoch non-saturation of the long-rank/two-large-endpoint core:

`sum_(j<=J) B_(2^j)^core=o(log J)`.

Equivalent targets are the scalar dyadic rank-variance statement or the
retained primitive cross-ratio state sum.  The concrete Wave 10 architecture
is a laminar weighted incomplete-difference-triangle LP containing `(W9-RLP)`
for every epoch subset, the exact tile constraints, and the primitive Abel
coefficients.  A successful dual must be uniform on the `surv_C=infinity`
subtree and must be proved analytically; finite LP certificates are discovery
only.

The secondary Q2 route remains uniform arbitrary-depth finite feasibility
under one fixed coordinate cap followed by König compactness.  Status:
`UNRESOLVED_AT_HARD_LIMIT`; no prize claim is ready.

### Wave 8 correction and exact next theorem

- The actual-adjacent ledger and old-clear/new-pay dichotomy leave at most one
  outstanding internal-adjacent family on a fixed history.  The two negative
  adjacent shell atoms have a finite dyadic sum under the critical cap.
- The actual innovation has an exact common-grid pair decomposition.  Its
  shell square expansion has negative coefficients only on the proper left-
  prefix and right-suffix fans; strict bulk intervals and the full span are
  positive.  The rank-one component has a separate Abel boundary fan.
- A positive envelope charges all genuine atoms to globally unique non-
  adjacent Golomb differences.  The artificial boundary row has total cost
  at most `92/315`.
- The exact pair telescope proves that every pair retains at least half its
  raw birth charge after all future negative old-pair terms.  Consequently
  `B_H(J)/2 <= sum_(j<=J)<H,Q_j/N_(2m_j)> <= B_H(J)`.
- Literal local `U_global/T` is false in the complete four-mark `C=1` scope;
  latest-shell density, raw adjacent-debt repayment, unconditional scaling,
  constant rank-one-to-shell comparison, and adjacent-only shell-fan
  repayment also have exact counterexamples.
- The 682-mark modified-greedy fixture passes all 510 tested activations
  through `m=256`, but its working envelope already fails at index 681 and no
  infinite branch is inferred.
- Hegyvári finite parabola blocks have an exact spectrum-disjoint splicing
  criterion.  Unconditional gap translation makes the critical-scale endpoint
  cubic, and a fixed finite menu can be blocked by universal internal spans.
- The targeted Wave 8 literature state contains 550 deduplicated records.
  No checked theorem supplies the positive birth budget or a compatible
  critical tower; this is a qualified null only.

**Single exact next theorem:** for one infinite normalized Golomb ruler with
`N_n<=C n^2 log(2n)` eventually, prove

`B_H(J)=o(log J)`,

where

`B_H(J)=sum_(m<=2^J) N_(2m)^(-2)
sum_(0<=i<j<2m,j>=m) h_i h_j Phi_(ij)`.

The proof must use uniqueness of all contiguous sums and give a bounded-
overlap charge simultaneously in numerical magnitude and rank lag across
dyadic births on the same infinite ray.  A finite initial error is harmless;
a repeated local factor-one inequality is neither necessary nor true.  Exact
finite-horizon adjoints may be used equivalently, but their signed terms
telescope to positive future `E`-energy rather than cancellation.

The secondary Q2 target remains uniform finite feasibility under one fixed
coordinate cap, followed by König compactness.  Status:
`UNRESOLVED_AT_HARD_LIMIT`.

### Wave 7 correction and exact next theorem

- The complete birth spectrum now partitions every pair in a dyadic prefix:
  full old--new lags `1<=k<2m` plus newborn-internal lags.  If a family has
  demand `q_F`, rank lag `ell_F`, and exact upper threshold `gamma_F`, then
  the wedge ledger proves
  `sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)` over all epochs of one infinite
  Golomb ruler.
- This summable potential does not pay covariance innovation locally.  The
  exact `p=1423`, 512-mark step has `Q_00/N>W_2`, and growing recent E–T
  windows have adjoint innovation `R/360+o(R)` but total `W_2=o(1)`.  This
  refutes fixed-constant affine domination by `W_2` alone, not a hypothesis
  that detects extension through one fixed infinite branch.
- Define `surv_C(P)` as the height of the finitely branching tree of future
  Golomb extensions of `P` under the eventual `C`-critical cap.  König's lemma
  gives `surv_C(P)=infinity` iff `P` lies on one infinite such ruler.  This is
  the exact admissible nonlocal label; it is not itself an innovation bound.
- Local renewal holes RH are refuted by the exact intervals `[21,22]` and
  `[382,383]`.  Direct harmonic tax HT is refuted with margin `-1/6` at
  threshold 3.
- The epoch-size threshold tax EST is proved for every normalized Golomb
  ruler through eight marks, with no diameter assumption.  Its forced-region
  enumeration covers 4,934 parents, 3,341,161 rulers, and 37,423,576 search
  nodes.  EST survives the authenticated 64/128-mark fixtures and 23 valid
  adjacent-gap swaps, but those larger scopes are not exhaustive.
- The cheap-child-half lemma cannot prove EST by adjacent matching.  On the
  128-mark witness at `T=1198199/32`, tax 120 yields only 57 genuinely new
  adjacent differences, leaving exact debt 63.
- Naive iteration of O'Bryant Lemma 9 from its scalar worst deletion guarantee
  requires a first-new-prefix jump `Omega(n^4)` and violates every fixed
  critical envelope eventually; for `C=1`, every `n>=8` is obstructed.  This
  does not rule out structured low-conflict blocks or a new gluing theorem.
- The Wave 7 primary-source audit retained 316 deduplicated records.  No
  checked source supplied the all-prefix critical tower or the needed
  innovation budget.  Consensus was quota-blocked; SciSpace and Firecrawl had
  the recorded relevance/metadata failures.  This is a qualified null only.

**Single exact next theorem:** in one infinite normalized Golomb ruler under
`N_n<=C n^2 log(2n)` eventually, condition every relevant family on
`surv_C(A_(2m))=infinity` and prove that repeated old-cheap orientations repay
their overlap debt through unused non-adjacent differences or equivalent
integer slack.  The resulting charge must quantitatively dominate the actual
newborn-shell and mixture contributions to `Q_m` and imply

`sum_(j<=J) <H,Q_(m_j)/N_(2m_j)> = o(log J)`.

The secondary Q2 target is uniform finite feasibility at every depth under
one coordinate cap; finite branching and König then supply an infinite ruler.
Neither target is proved.  Status: `UNRESOLVED_AT_HARD_LIMIT`.

### Wave 6 correction and exact next theorem

- The exact birth-lag Hall theorem is only `Lambda<=1`: every selected family
  demand whose integer hull lies in an inclusive interval is bounded by that
  interval's integer capacity.  The complete endpoint scan proves this finite
  statement without sampling.
- The empirical strengthening `Lambda_NN(n,2n)<=1/(4 sqrt(n))` is refuted.
  One exactly audited C=1 Golomb ruler reaches 64 marks and violates it at
  three consecutive transitions:
  `Lambda=9/14,17/28,45/118`, with scaled values
  `2592/49,4624/49,259200/3481`.  All 2,016 differences and all 63 prefix
  envelopes pass; the two extension beams are deterministic but not
  exhaustive.
- A separate exact finite audit reaches 128 marks (final mark 136,282), with
  all 8,128 differences distinct and all 127 nontrivial prefix envelopes at
  C=1.  Its discovery was heuristic.  It proves neither optimality nor an
  infinite extension.
- Theorems A--C give exact multi-epoch newborn-shell and old--new
  anti-diagonal integer-capacity ledgers.  With
  `tau_(m,k)=D_m^-+D_m^++k max(mu_m^-,mu_m^+)`, Theorem D gives
  `sum_(tau<=X) k/tau<=1+log X` and, for every epsilon>0,
  `sum k/tau^(1+epsilon)<=(1+epsilon)/epsilon`.  The endpoint epsilon=0 is
  still logarithmic and therefore does not close Q1.
- The sixteen-mark C=1 ruler survives three strongly negative resets with
  almost uniform newborn shells and normalized innovations above `1/600`.
  Three-cycle collision is not a valid theorem.
- The residue lift `A_L(B)={0,1,Lb_1,...}` is Golomb and confines the
  one-point forbidden shadow to at most four classes modulo L.  Growing
  compatible finite windows have total extension-band shadow density `o(1)`
  while their innovation sum diverges.  Universal local-shadow charging is
  refuted.
- The bounded Wave 6 literature audit found no checked compatible critical
  all-prefix tower or endpoint band-renewal theorem.  This is a qualified
  null, not an absence or novelty claim.

**Single exact next theorem:** for one infinite normalized Golomb ruler under
`N_n<=C n^2 log(2n)`, prove that old-history capacity prevents the Wave 6
cutoffs `R_m(T)` from renewing through unboundedly many fresh numerical bands
and consequently

`sum_(j<=J) <H,Q_j/N_(2m_j)> = o(log J)`.

This must use global compatibility and cross-epoch contiguous-sum uniqueness;
the exact `O(log)` endpoint ledger, Hall capacity alone, finite extension,
profile/reset/PSD data, and local forbidden-shadow density are insufficient.

### Wave 5 correction and exact next target

- Cross-epoch chord inheritance is exact:
  `e_M(r)-(r/m)e_M(m)=(N_m/N_M)e_m(r)`.  Deep block packing also fixes the
  reset's rank and sign: `e_M(m)<=-1/(2q)` once `q-1>=4K log m`.
- One endpoint-flat dyadic run has length only `O(log log m)`, and the number
  of nearly flat steps admits an exact conditional charge to the upward
  variation of `log(N_(2^j)/4^j)`.
- Critical growth does not control that variation.  An infinite nested
  non-Sidon integer gap profile satisfies a fixed all-prefix
  `O(n^2 log n)` envelope and scalar capacity, has sparse resets, yet keeps
  `Q_00/N>=1/2048` on every transition.  The repeated difference 14 at four
  marks is the precise reason it is not a #1191 counterexample.
- Authenticated 32-mark roots extend heuristically to 64 marks under the same
  `C=1` envelope at all 63 prefixes.  The best retained witness keeps
  innovation above `0.0037994` for five transitions and latest signed reset
  persistence above `0.6587`.  This is finite calibration only.
- Therefore the new target is an **arithmetic reset-renewal exclusion**:
  prove that replacing repeated equal newborn gaps by one globally Sidon gap
  sequence forces enough additional span or overlapping-band occupation
  across several reset-to-flat cycles to pay the actual adjoint innovations
  by `o(log J)`.

### Wave 4 correction and sharpened target

- The fixed-depth obstruction is now a growing-depth theorem.  For terminal
  `M=2^J`, the last `floor(log_2 J)-1` dyadic prefixes of one finite
  Erdős--Turán ruler share the same `C=1` critical envelope, while their gap
  variances sum to `(log J)/(180 log 2)+O(1)` and adjacent innovations tend
  uniformly to `1/360`.  Thus recent history of `Theta(log J)` scale indices,
  equivalently `Theta(log log M)` dyadic generations, is still insufficient.
- A genuine global-history packing law is now proved.  If `M=qm`, the old
  prefix obeys `N_m<=K m^2 log m`, and
  `epsilon_M=max_r|N_r/N_M-r/M|`, then
  `epsilon_M>=1/q-Km^2 log(m)/(binom(q,2)m^2+1)`.  Hence every hypothetical
  global critical sequence has `epsilon_M=Omega(1/log M)` at all large
  dyadic `M`: its diameter profile must repeatedly reset.
- The direct bridge from this packing law to innovation is false.  Over the
  growing Erdős--Turán window, total old--new band occupancy is below `1/2`
  while the innovation sum is `L/360+o(1)`.  Any new charge must compare
  different profile epochs, not pay `Q_00/N` from each local containing band.
- Certified nested 32-mark witnesses satisfy the same `C=1` envelope at every
  prefix and keep both `G_m` and `Q_00/N` bounded away from zero over four
  transitions.  They are finite beam witnesses, not infinite constructions.

- The exact diameter-regime gap kernel is now nonnegative term by term:
  `V_m=N_m^-2 sum_(k<l) h_kh_l(l-k)^2(m-k-l)^2`.
- For every Sidon prefix with `m=8q>=16`,
  `V_m>=9m^6/(16,777,216N_m)`.  Thus the critical lower accumulation is
  strengthened to `G_J=sum_j V_(m_j)/m_j^4=Omega_C(log J)`.
- The exact positive birth expansion has the unconditional upper
  `G_J<=(4/3)log N_J=O(J)`.  The precise desired theorem is
  `G_J=o(log J)` under the critical envelope.
- The gap measures obey the exact matrix recursion
  `M_(2m)=B M_m B^T+Q_m`, `Q_m>=0`, for
  `M_m=N_m Cov_(nu_m)(u(1-u),u)` and
  `B=((1/4,1/4),(0,1/2))`.  Combining two steps with the largest `3m/4`
  distinct adjacent gaps proves the sharper pointwise lower bound
  `Var(C_(N_M))/M^4 >= (9M^2-256)/(1,048,576N_M)` for `M>=16` dyadic.
  Under the critical envelope its asymptotic coefficient is
  `9/(2,097,152 C log M)`, sixteen times the direct eight-block constant.
- The upper problem now has the exact adjoint identity
  `sum_(j<=J) G_j=<H_1,R_1>+sum_(j<=J)<H_(j+1),Q_j/N_(j+1)>`.
  Here `H_j` is explicitly defined backwards and uniformly dominated by
  `H=((16/15,8/105),(8/105,4/35))`.  An abstract critical PSD orbit with
  `G_j=1/72` rules out every proof that uses only the recursion, PSD, and
  critical growth.  It is not a compatible Golomb counterexample.  The exact
  target is therefore an arithmetic upper bound for the actual birth-shell
  innovations `Q_j`.
- A three-rank lift gives one critical shell with
  `V_m/m^4>=1/2304`; no uniform pointwise `o(1)` estimate based only on one
  isolated Sidon ruler and its quadratic diameter can prove the desired upper
  bound.  This rank-lift family alone does not exclude compatible bounded-depth
  hypotheses; the separate Erdős--Turán family below does.
- A separate Erdős--Turán argument treats every fixed depth `L`: arbitrarily
  large finite Sidon windows have their last `L+1` prefixes in one `C=1`
  critical envelope, yet `Q_00/N -> 1/360` and the signed birth shell tends to
  `19/3840`.  Thus local finite-window compatibility alone cannot give
  `o(1/j)`.  Only a hypothesis using embeddability in one global critical
  sequence or an unbounded-history amortization remains eligible.
- The exact q-cover identity gives a frozen-edge martingale, but complete loads
  are destroyed by newborn-edge cancellation.  `{0,1,4}` is the minimal
  example, and nested newborn arcs refute a uniform Bessel bound.
- Shell hypotheses H1--H5 are refuted exactly.  H6 survived certified finite
  searches only and must not be stated as a theorem.
- The natural H6 proof by fixed-modulus prefix monotonicity is also refuted:
  the globally minimal Sidon example for doubled-prefix comparisons at `N=40` has
  `Var(0,20)=1/4 > 99/400=Var(0,20,21,39)`.
- Fully orthogonal per-edge martingale coordinates are blocked by the exact
  trace lower bound `U_wT_w>=P^3/(9N)`, which already accumulates harmonically
  at critical density.

**Highest-value consequence now:** for the actual gap-measure innovations

\[
Q_j=G_j^{\rm diam}\operatorname{Cov}_{\sigma_j}z
+\frac{N_jG_j^{\rm diam}}{N_{j+1}}d_jd_j^{\mathsf T},
\]

deduce the adjoint-weighted arithmetic budget

\[
\sum_{j\le J}\langle H_{j+1},Q_j/N_{j+1}\rangle=o(\log J).
\]

Equivalently, find a long-range invariant of the normalized gap measures

\[
\nu_j=N_j^{-1}\sum_{k<m_j}h_k\delta_{k/m_j}
\]

that uses distinct contiguous gap sums across an unbounded number of nested
prefixes and forces

\[
\sum_{j\le J}\operatorname{Var}_{\nu_j}(u(1-u))=o(\log J).
\]

Equivalently, it is enough to prove this upper budget for the same
`m^-4`-weighted endpoint variance already forced by the two-step theorem.
The exact covariance-matrix innovations are now the canonical state variables.
A successful proof must obtain this consequence from the Wave 6 global
band-renewal self-improvement, converting the endpoint `O(log)` ledger into a
sublogarithmic old-history charge.

Any candidate must first pass the three-rank lift, the birth-complement family,
the fixed-modulus counterfamily, the orthogonal-coordinate trace no-go, the
exact H1--H5 witnesses, the growing-depth Erdős--Turán limit, the direct
cross-band-charge no-go, the non-Sidon square profile, the infinite non-Sidon
sawtooth renewal profile, the sixteen-mark three-cycle ruler, the 64-mark
three-transition Hall counterexample, the 128-mark finite witness, and the
growing residue-lift shadow no-go.

**Next exact formulation:** prove the global band-renewal self-improvement.
Begin with Theorems C--D, not with a new local shell statistic.  Quantify the
old-history capacity paid whenever the active threshold family moves to a
fresh mean-gap band, and show that one infinite compatible Sidon sequence
cannot repeat this renewal often enough to saturate the endpoint
`1+log X` ledger.  Convert that global charge into an `o(log J)` bound for the
two exact terms of the actual innovation `Q_(m,M)`.

- **Target A, exact layer:** complete.  The cyclic-arc covariance kernel,
  cycle-resistance formula, exact pair--pair expansion, and all
  prefix/short-pair boundary indicators are in
  `core_workspace/endpoint_variance/MULTISCALE_ARC_KERNEL_AND_OBSTRUCTIONS_2026-08-28.md`.
- **Target A, theorem-strength layer:** open.  The older `m^-3` functional has
  forced lower bound `(1+o(1)) log J/(360 C log 2)`.  The stronger current
  `m^-4` functional has the two-step lower coefficient
  `(9+o(1))/(2,097,152 C log 2)` in front of `log J`.  The missing statement
  is the density-compatible signed/structural upper budget `G_J=o(log J)`.
- **Target B:** complementary two-cycles and a genuine three-edge Sidon cycle
  show that exact zero modes persist.  Covariance sign can reverse when the
  modulus doubles.  Quantitative anti-Eulerian stability remains open.
- **Target C, fixed containing modulus:** the exact prefix second difference
  is one centered adjacent-gap indicator.  This reconstructs the known gap
  profile and is saturated unless changing/shorter moduli introduce new
  structure.
- **Target D, certified finite layer:** complete for `2<=m<=7`,
  `m-1<=D<=25`, at `N=D+1,D+2,D+3`, with an independent oracle.  No uniform
  asymptotic strengthening follows from this range.
- **Ruled out:** diagonal-only positivity, termwise sign preservation under
  doubled moduli, prefix monotonicity, a dominant-gap lower principle, and the
  specific unconditional critical-weight raw-variance budget.

The next session should not rederive the kernel, matrix update, growing-depth
no-go, or cross-block band formulas.  It should construct and falsify explicit
cross-epoch reset potentials, beginning with the exact same-lag oscillation in
equation (8) of
`core_workspace/endpoint_variance/CROSS_BLOCK_DIAMETER_PROFILE_PACKING_2026-08-28.md`.

**Status:** research agenda, not proved  
**Primary question:** Erdős #1191 Question 1  
**Starting contradiction hypothesis:** for some fixed `C>0`,

\[
a_m\le C m^2\log m
\]

for all sufficiently large `m`.

## 1. Exact finite signal already available

For the `m`-point prefix `A_m={a_1<...<a_m}`, put `D_m=a_m-a_1` and initially choose `N_m=D_m+1`. Every pair is then short. The boundary-load variance satisfies

\[
V_m:=\operatorname{Var} E_{N_m}(A_m)
\ge
\frac{m(m^2-1)(m^2+11)}{180N_m}.
\]

Under the critical envelope this is

\[
V_m\gg_C \frac{m^3}{\log m}.
\]

The missing ingredient is **not** another lower bound at one scale. It is a Sidon upper budget for a coupled functional involving many prefixes, moduli, offsets, or length slices.

## 2. Target A: exact quartic expansion with summable interaction multiplicity

For selected pairs `(m_j,N_j)` and weights `w_j>=0`, expand

\[
\mathcal V=\sum_j w_j\operatorname{Var}E_{N_j}(A_{m_j})
\]

into pair-pair interactions. Starting from

\[
C_N(r)=\sum_{p\in P_N(A)}1_{B_p}(r),
\]

one has

\[
N\operatorname{Var}C_N
=\sum_{p,q}\left(|B_p\cap B_q|-\frac{|B_p||B_q|}{N}\right).
\]

Derive the exact cyclic-arc intersection kernel with all wrap cases. Then seek a scale schedule and weights for which:

1. the critical-envelope lower bound makes `mathcal V` diverge faster than the proposed upper budget;
2. each ordered pair of global differences, or each endpoint quadruple, enters the upper side with uniformly summable total weight;
3. negative covariance terms are controlled without discarding the endpoint-sensitive gain.

### Falsification tests

- `{0,1,N}` at its zero modulus;
- two-edge and longer directed cycles;
- unions of edge-disjoint residue cycles;
- homometric rulers with different endpoint variance;
- prefixes with one dominant gap;
- moduli sharing many divisors versus pairwise coprime moduli.

### Success threshold

A fixed-factor improvement is insufficient. The final ratio between the density-forced lower bound and the Sidon upper budget must tend to infinity.

## 3. Target B: nested-modulus anti-cycle theorem

For a modulus `N`, zero variance is equivalent to an Eulerian directed short-pair residue graph. Each directed cycle in a Sidon set uses distinct positive edge lengths below `N`, and its oriented length sum is a nonzero multiple of `N`.

Candidate theorem shape:

> Under a uniform critical-density lower bound, there is a positive-density or weighted-divergent set of scales at which the short-pair residue graph is quantitatively far from every Eulerian flow.

Possible quantitative distances:

- `||delta_N||_{H^{-1}}^2` itself;
- minimum number or total weight of edges to delete to make `G_N` Eulerian;
- minimum `l1` transport needed to balance endpoint charges;
- cycle-space projection defect;
- discrepancy over cyclic intervals.

### Necessary cautions

- `||delta_N||_2` alone can miss low-frequency placement effects seen by `H^{-1}`.
- Divisibility of cycle length sums can be satisfied at many related moduli; nested moduli may be worse than incommensurable ones.
- A theorem about exact Eulerianity is probably too brittle; near-Eulerian stability is required.
- The two-cycle zero mode must be explicitly excluded by density, length diversity, or cross-scale hypotheses.

## 4. Target C: martingale-difference identity retaining all offsets

Let `f=1_A` on a localized interval and consider nested translated interval partitions. Seek a martingale or reverse-martingale sequence `M_j` for which an increment norm controls endpoint variance:

\[
\|M_{j+1}-M_j\|_2^2
\quad\text{or}\quad
H(M_j)-H(M_{j+1}).
\]

A valid identity should:

- keep the offset variable coupled across levels;
- telescope or satisfy square-function orthogonality;
- translate the total energy/entropy budget into a count controlled by unique differences;
- avoid choosing an unrelated minimizing offset at every scale.

The classical mean energy has already been optimized to a constant-level theorem. The new ingredient must use variance, covariance, or stability across levels.

## 5. Target D: optimize the diameter-regime gap formula over Golomb rulers

For `D<N`, let `g_k=a_{k+1}-a_k` and `x_k=k(m-k)`. Then

\[
V_N(g)=\frac1N\sum_{k=1}^{m-1}g_kx_k^2
-\left(\frac1N\sum_{k=1}^{m-1}g_kx_k\right)^2.
\]

The Sidon/Golomb condition is exactly that all contiguous sums

\[
g_i+g_{i+1}+\cdots+g_{j-1}
\]

are distinct.

Determine or bound

\[
V_m^{\mathrm{Sidon}}(D,N)
=
\min V_N(g)
\]

over positive integer gap vectors of length `m-1` with total `D` and distinct contiguous sums.

### Why this is worth doing

The current mandatory-level inequality is sharp over arbitrary finite sets, but its equality family is consecutive and therefore non-Sidon for `m>=3`. A Sidon-specific strengthening may expose structural concentration or a stable profile that can be coupled across prefixes.

### Exact-computation program

- enumerate normalized Golomb rulers for the smallest feasible `m,D`;
- compute exact rational variances;
- identify minimizers and symmetry classes;
- compare `N=D+1`, `N=D+t`, and optimized `N`;
- test rulers with a dominant central gap;
- formulate the weakest pattern surviving exhaustive search;
- produce certificates or independent exhaustive engines for any claimed finite minimum.

### Limitation

Even `V_N\gg m^4` at each prefix would not settle #1191 without a cross-prefix upper budget. Treat this target as structure discovery, not the endpoint.

## 6. Target E: length-sliced almost orthogonality

Write

\[
\delta_N=\sum_s\delta_{N,s},
\]

where slice `s` contains pair differences in a dyadic band or pairs born in a specified prefix range. Expand

\[
\|\delta_N\|_{H^{-1}}^2
=
\sum_s\|\delta_{N,s}\|_{H^{-1}}^2
+2\sum_{s<t}\langle\delta_{N,s},\delta_{N,t}\rangle_{H^{-1}}.
\]

Try to prove that persistent cancellation of diagonal energies by cross terms is incompatible with:

- uniqueness of positive differences;
- the critical growth schedule;
- many incommensurable moduli;
- endpoint rank structure in complete prefixes.

A Littlewood–Paley, large-sieve, or incidence formulation is useful only if all normalizations and boundary terms are explicit.

## 7. Target F: finite Fourier uniformity dichotomy

For a window `I` of length `X`, a Sidon subset can contain at most about `sqrt(X)` points. Use a dichotomy:

1. many windows/prefixes are near this finite extremal size, so Fourier-uniformity and residue equidistribution theorems may apply; or
2. enough windows have a quantitative deficit, which may force a global drop below the critical infinite envelope.

Required before invoking an external uniformity theorem:

- exact near-extremality threshold;
- uniform dependence of the Fourier error on the deficit;
- compatibility with moving windows and growing moduli;
- proof that the number of applicable windows is sufficient;
- no circular use of the desired density conclusion.

## 8. Candidate exact identities to derive immediately

### 8.1 Cyclic arc covariance

For short pairs `p=(a,b)` and `q=(c,d)`, derive a closed expression for

\[
K_N(p,q)=|B_{a,b}\cap B_{c,d}|-\frac{(b-a)(d-c)}N.
\]

Classify by the cyclic order of the four endpoints and relate the sign to crossing/nesting of arcs.

### 8.2 Fourier pair expansion

From

\[
\widehat\delta_N(k)
=\sum_{a<b,\,b-a<N}
\left(e^{-2\pi i ka/N}-e^{-2\pi i kb/N}\right),
\]

expand `|delta_hat|^2`, sum over frequencies with the inverse-cycle-Laplacian kernel, and identify which endpoint coincidences or difference equalities simplify under the Sidon property.

### 8.3 Prefix update

When `a_{m+1}` is added, derive an exact formula for the change in the diameter-regime quantities

\[
T_m=\sum_{k=1}^{m-1}g_k k(m-k),
\qquad
S_m=\sum_{k=1}^{m-1}g_k k^2(m-k)^2,
\]

and hence for `V_m`. Seek a compensated increment with a sign or telescoping property.

### 8.4 Average over moduli above the diameter

For fixed prefix and every `N>D`,

\[
V_N=\frac{S_m}{N}-\frac{T_m^2}{N^2}.
\]

This dependence is explicit. Determine whether weighted averaging over `N>D` adds any information or merely rescales the same two gap moments. Do not spend time on this route if it collapses to a two-moment statistic.

## 9. Historical pre-Wave 12 umbrella lemma

The concrete current highest-value lemma is P23 in the Wave 18 disposition
at the top of this file.  The formulation below is retained only as the older
program-level umbrella and must not supersede P23.

The preferred theorem has the following logical form:

> **Anti-Eulerian multiscale budget.** There exist an explicit scale/prefix selection rule and nonnegative weights such that every infinite Sidon sequence obeys a universal upper bound for the corresponding weighted endpoint-variance functional, while every sequence satisfying `a_m<=C m^2 log m` eventually forces a lower bound exceeding that upper bound by an unbounded factor.

The theorem must specify the functional, weights, boundaries, and constants. It must be strictly easier to establish than #1191 itself because its upper bound should exploit an exact interaction-counting or telescoping mechanism not present in the original formulation.
