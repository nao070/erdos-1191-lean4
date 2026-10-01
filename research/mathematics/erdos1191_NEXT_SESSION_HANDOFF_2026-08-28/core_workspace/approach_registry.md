# Approach Registry — Erdős Problem #1191

**Updated:** 2026-08-29 continuation, Wave 0--19  
**Allowed statuses:** ACTIVE, CONDITIONAL, SATURATED, BLOCKED, REFUTED, COMPLETE

## A0. Independent endpoint-theorem audit

- **Status:** ACTIVE
- **Evidence:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Mechanism:** rederive the endpoint-imbalance reconstruction, Fourier normalization, diameter formula, mandatory-level bound, equality conditions, and homometric separation; conduct a systematic novelty search.
- **Current support:** the proof was independently rederived and passed the
  half-open, Fourier, Eulerian, diameter, mandatory-level, and homometric
  audit.  The shared suite has been extended beyond the 15-test baseline; the
  three original certificates still total 42,615 checks.
- **Open issue:** the exact theorem audit is complete; a publication-level
  prior-art/expert novelty audit is not.
- **Next falsifiable test:** locate the complete statement under interval-load
  covariance, cycle Green functions, or circular discrepancy terminology.

## A1. Anti-Eulerian multiscale variance budget — parent program for Q1

- **Status:** ACTIVE — current primary implementation is A28/P28; A23--A27
  are rigorous upstream reductions or saturation boundaries
- **Evidence:** `[CONDITIONAL]`
- **Mechanism:** couple `Var E_N=||delta_N||_{H^{-1}}^2` across prefixes/moduli so that critical growth forces a divergent lower bound while global Sidon difference uniqueness gives a finite or slower upper budget.
- **Why new:** endpoint variance is quartic and separates homometric rulers, so it escapes the certified barrier for difference-spectrum-only mixtures of means.
- **Current result:** the exact cyclic-arc kernel, its resistance
  representation, all prefix/short-pair boundary indicators, and the critical
  dyadic functional are proved.  The critical lower sum is
  `(1+o(1)) log J/(360 C log 2)`.  Wave 3 additionally gives the positive
  gap-pair identity and the stronger functional
  `G_J=sum_j Var(C_{N_j})/m_j^4=Omega_C(log J)`.  Its current sharpest
  project-internal lower step is
  `Var(C_(N_M))/M^4 >= (9M^2-256)/(1,048,576N_M)`, obtained by an exact
  two-step gap-measure update.  The update closes positively on the matrix
  `M_m=N_m Cov_(nu_m)(u(1-u),u)` rather than on a scalar.
- **Gap:** no critical-density upper budget `G_J=o(log J)` has been proved.
  The unconditional positive expansion gives only `G_J<=(4/3)log N_J=O(J)`.
- **Next falsifiable test:** exploit compatibility over unboundedly many
  prefixes to control the covariance innovations or improve the birth-shell
  moment estimate from `O(1)` absolute cost per shell to `o(1/j)` on average.
  The rank-lift obstruction excludes isolated-prefix pointwise estimates.  A
  stronger Erdős--Turán family excludes every uniform fixed-depth theorem
  based only on the visible finite window and its critical compatibility.
  Wave 4 strengthens this to the last `floor(log_2 J)-1` dyadic prefixes,
  whose total gap variance is `(log J)/(180 log 2)+O(1)`.  A bounded-depth
  formula remains eligible only if it uses a genuinely global extension or
  embeddability hypothesis whose charges amortize over unbounded history.

## A2. Nested-modulus anti-cycle packing

- **Status:** ACTIVE
- **Evidence:** `[HEURISTIC]`
- **Mechanism:** zero or low variance corresponds to Eulerian or nearly Eulerian short-pair residue graphs; distinct Sidon edge lengths in each directed cycle must sum to multiples of the modulus.
- **Current obstruction:** `{0,3,7,12}` at `N=6` is a Sidon three-cycle zero
  mode, and an individual covariance changes sign from `N=8` to `N=16` in
  `{0,1,3,7}`.
- **Gap:** exact cycles can occur, and no normalized near-Eulerian stability or
  packing theorem is known.
- **Next falsifiable test:** construct critical-envelope rulers that remain
  near Eulerian at several incommensurable moduli, or prove that this is
  impossible with quantitative `H^-1` loss.

## A3. Martingale / reverse-martingale / entropy formulation

- **Status:** ACTIVE
- **Evidence:** `[HEURISTIC]`
- **Mechanism:** retain the offset variable in nested interval partitions and identify a telescoping energy or entropy increment controlled by unique differences.
- **Current result:** at one fixed containing modulus,
  `C_m-2C_{m-1}+C_{m-2}` is exactly the centered indicator of the new adjacent
  gap after centering.  Wave 3 proves the exact q-cover projection
  `q^2 V_{qN}=V_N(R_N)+I_{N,q}`, with `I>=0`, and a genuine frozen-edge
  martingale square function.  Independently, the diameter-gap measure gives
  the exact finite-dimensional recursion
  `M_(2m)=B M_m B^T+Q_m`, `Q_m>=0`.  This is the first positive canonical
  complete-prefix update, but no global upper bound on its innovations is
  known.
- **Obstruction:** canonical complete loads are not martingales: in
  `{0,1,4}`, the modulus-2 variance `1/4` becomes zero at modulus 4 because a
  newborn residual arc exactly complements the old arc.  Newborn residuals
  can also be quadratically correlated, so distinct differences alone give no
  uniform Bessel bound for every newborn subfamily.  No lower bound is claimed
  for the complete newborn load.
- **Further no-go:** assigning every distinct edge its own orthogonal Hilbert
  coordinate cannot help.  For every positive diagonal weighting,
  `U_w T_w >= binom(m,2)^3/(9N)`, hence its normalized critical cost is at
  least `1/(576 C log m)` per scale.  The vector q-cover trace also spends
  positive energy on exact scalar zero modes.
- **Next falsifiable test:** a vector-valued filtration must charge birth
  coordinates in structured covariance blocks, not diagonal coordinates;
  audit the block synthesis cost before pursuing entropy inequalities.

## A4. Sidon-specific optimization of the diameter-regime variance

- **Status:** ACTIVE
- **Evidence:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Mechanism:** minimize the exact gap-moment variance over Golomb gap vectors, where all contiguous sums are distinct.
- **Reason:** the current equality family is consecutive and non-Sidon for `m>=3`, so Sidon-specific strengthening is not ruled out.
- **Current result:** Wave 3 proves uniformly, for every Sidon ruler with
  `m=8q>=16` and `N=D+1`,
  `Var C_N >= 9Dq^5(q-1)/(16N^2) >= 9m^6/(16,777,216N)`.
  A later optimized argument needs only distinct adjacent gaps and gives, for
  dyadic `M>=16`,
  `Var C_(N_M)/M^4 >= (9M^2-256)/(1,048,576N_M)`, improving the critical
  asymptotic constant by a factor of sixteen.
  Exhaustive exact minima for `2<=m<=7`,
  `m-1<=D<=25`, and `N=D+1,D+2,D+3`; 245,505 candidates and an independent
  294-check oracle.  At the least feasible diameter the ratio to the general
  mandatory bound is strictly above one for `3<=m<=7`.
- **Gap:** the single-prefix lower bound is now asymptotically strong enough;
  the missing step is exclusively a cross-prefix upper/amortization theorem.
- **Next falsifiable test:** stop extending isolated finite minima unless they
  test a proposed long-range compatibility inequality.

## A5. Finite Fourier-uniformity dichotomy

- **Status:** CONDITIONAL
- **Evidence:** `[RIGOROUS — MODULO NAMED THEOREM]`
- **Mechanism:** either many finite windows are near extremal and obey Fourier/residue equidistribution, or their deficits force a global density drop.
- **Gap:** #1191-critical prefixes are logarithmically below finite extremality; applicability is not automatic.
- **Next falsifiable test:** quantify the exact near-extremality threshold needed by Ortega–Prendiville/Ding and test whether a critical prefix supplies enough qualifying windows.

## A6. Length-sliced H^{-1} almost orthogonality

- **Status:** ACTIVE
- **Evidence:** `[HEURISTIC]`
- **Mechanism:** decompose endpoint imbalance by dyadic difference lengths or pair birth times and control cross-slice cancellation.
- **Gap:** no proven positivity/almost-orthogonality under Sidon uniqueness.
  The exact kernel shows that nesting is positive, disjointness negative, and
  crossings can have either sign; cyclic topology alone is insufficient.
- **Next falsifiable test:** exhaustive search for extreme negative `H^-1`
  covariance between two birth/length slices subject to a critical envelope.

## A7. Global arithmetic band-renewal self-improvement

- **Status:** SATURATED — superseded as primary by A8; exact ledger retained
- **Evidence:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Mechanism:** use all newborn-shell and old--new anti-diagonal differences
  from every available dyadic epoch.  Their exact inclusive integer-capacity
  ledgers must be strengthened by an old-history charge whenever the active
  mean-gap cutoff renews into a fresh numerical band.
- **Current theorem:** with
  `tau_(m,k)=D_m^-+D_m^++k max(mu_m^-,mu_m^+)`, the cumulative selected demand
  below `T` is at most `floor(T)`.  Layer-cake integration gives
  `sum_(tau<=X) k/tau<=1+log X` and
  `sum k/tau^(1+epsilon)<=(1+epsilon)/epsilon`.  These statements are exact
  for every finite epoch family and extend to one infinite ruler by monotone
  convergence.
- **Hard limit:** exponent one gives only `O(log X)`, not the required
  `o(log J)`.  Changing mean gaps can renew which numerical band lies below
  the useful cutoff.
- **Closed strengthening 1:** the universal birth-lag Hall pressure is at most
  one, but no tested decay may be promoted.  One exactly audited 64-mark C=1
  Golomb ruler violates `Lambda_NN<=1/(4 sqrt(n))` at three consecutive
  transitions.
- **Closed strengthening 2:** a sixteen-mark ruler survives three strongly
  negative nearly uniform resets with positive innovation; three-cycle
  collision is false.
- **Closed strengthening 3:** a residue lift confines the one-point forbidden
  shadow to four residue classes and gives growing finite compatible windows
  with shadow-density sum `o(1)` but divergent innovation.  Local shadow
  density cannot be the universal charge.
- **Next falsifiable test:** propose an explicit old-history potential on the
  threshold bands, prove it is not reset by translation to a fresh mean-gap
  scale, and test it on the 64- and 128-mark certificates before seeking the
  infinite theorem.

## B1. Fully translation-averaged one-scale mean energy

- **Status:** SATURATED — for Q1
- **Evidence:** `[RIGOROUS — MODULO NAMED THEOREM]`
- **Mechanism:** O’Bryant’s block energy plus weighted Cauchy inequality.
- **Conclusion:** yields a positive universal constant and can optimize that architecture, but does not supply the unbounded gain required for Q1.
- **Allowed future use:** as a component of a genuinely multiscale/stability argument, not as another isolated weight optimization.

## B2. Separable nonnegative mixtures of global mean kernels

- **Status:** BLOCKED
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`
- **Mechanism:** scale mixtures depending only on difference multiplicities.
- **Reason:** they retain no endpoint-incidence information; the homometric separation shows endpoint variance contains strictly more data.
- **Allowed future use:** only if covariance, signs, offsets, or cross-scale consistency are retained.

## C1. Naive near-adjacent translated dense-block gluing

- **Status:** BLOCKED — in the tested model
- **Evidence:** `[COMPUTATIONAL — EXPERIMENTAL]`
- **Mechanism:** append a dense finite Sidon block by a generic nearby translation.
- **Reported obstruction:** the forbidden shadow `F(V)=V+D(V)` became nearly/full dense near `max(V)` in the tested finite regimes.
- **Correction:** this does not prove that all algebraic/recursive
  constructions are impossible.  Wave 6 gives an exact counterfamily to any
  universal local-density premise: the Golomb residue lift has forbidden
  shadow in at most four classes modulo an arbitrarily large `L`.  The older
  source code and raw scaling JSON were also not included in the handoff.
- **Next action:** do not spend primary effort here unless the missing artifacts are recovered or a theorem with explicit hypotheses is formulated.

## C2. Algebraically coordinated compatible construction — Q2

- **Status:** ACTIVE — secondary
- **Evidence:** `[CONDITIONAL]`
- **Mechanism:** finite-field/function-field towers, compatible discrete logarithms, mixed-radix signatures, global hypergraph alteration, or whole-prefix existence under `b_k<=Ck^2(log k)^d`.
- **Gap:** complete classification of cross-scale difference collisions and a uniform depth-independent envelope.
- **Next falsifiable test:** derive the exact coordinate recurrence and reject any scheme with polynomial exponent above 2.

## C3. Ruzsa/Cilleruelo exponent barrier audit

- **Status:** ACTIVE — secondary
- **Evidence:** `[RIGOROUS — MODULO NAMED THEOREM]`
- **Mechanism:** rederive parameter inequalities and deletion losses determining the exponent `sqrt(2)-1`.
- **Gap:** no modification currently reaches the `1/2` density exponent up to logarithms.
- **Next falsifiable test:** identify whether any proposed coding improvement changes the governing exponent inequality rather than only constants.

## D1. Finite profile / SAT / exhaustive computation

- **Status:** ACTIVE — falsification tool
- **Evidence:** `[COMPUTATIONAL — EXPERIMENTAL]`
- **Mechanism:** exact small-ruler optimization, counterexample minimization, candidate functional testing.
- **Rule:** finite UNSAT or verified ranges remain finite statements; no asymptotic conclusion without a uniform theorem.
- **Current available code:** endpoint-variance, exact cyclic-kernel, and
  Golomb-variance verifiers, the positive gap/birth kernel, the q-cover
  identity, and critical-shell falsifiers with deterministic dated artifacts.
  H1--H5 are exactly refuted; H6 survived only the explicitly certified finite
  ranges and is not promoted to a theorem.  Its proposed fixed-modulus
  monotonicity proof is refuted by the globally minimal doubled-prefix Sidon
  example at `N=40`.  Wave 5 extends authenticated Wave 4 roots to six
  64-mark nested `C=1` witnesses, each passing all 63 prefix envelopes and all
  2,016 difference checks.  The best retained five-transition innovation
  minimum exceeds `0.0037994`, with latest signed profile persistence above
  `0.6587`.  Only the four-mark root layer is complete; every later extension
  is deterministic beam evidence and is not an optimality or infinite-
  extension claim.  Wave 6 separately extends one retained 64-mark fixture to
  128 marks: all 8,128 differences and all 127 C=1 prefix rows pass exact
  audits, but the beam was heuristic.  Another finite branch reaches 64 marks
  with three consecutive exact Hall-decay violations.  Neither is an infinite
  construction or an asymptotic result.  Older profile solvers are not in this
  package.

## E1. Endpoint-theorem novelty and terminology search

- **Status:** ACTIVE
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`
- **Mechanism:** search circular discrepancy, graph divergence, inverse cycle Laplacian, negative Sobolev norms, electrical networks, interval coverage, homometric/Golomb literature, and additive-combinatorial block energies.
- **Gap:** preliminary searches found no exact match, but terminology may differ.
- **Wave 6 delta:** bounded primary checks of disjoint difference packings,
  `A+A-A` shadows, and Singer/finite-field nesting found no compatible
  critical all-prefix tower or endpoint band-renewal theorem.  Consensus was
  quota-blocked.  This is a qualified null only.
- **Next action:** check zbMATH/MathSciNet reviews and forward citations with the exact formula.

## Registry rule

A route is not marked COMPLETE until it proves or disproves Q1 or Q2 with all quantifiers and dependencies audited. A route whose central lemma is merely equivalent to the original question remains BLOCKED unless it introduces an independently verifiable mechanism.

## A8. Complete-birth wedge potential plus infinite-survival debt repayment

- **Status:** SATURATED — partly resolved and superseded by A9
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`
- **Proved mechanism:** full old--new and newborn-internal birth families
  partition every pair. Rank-lag capacity gives
  `sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)` over one infinite Golomb ruler.
- **Closed direct bridge:** exact 512-mark and growing E–T windows refute
  every fixed-constant affine domination of adjoint innovation by this
  potential alone.
- **Admissible global label:** `surv_C(P)`, the height of the critical Golomb
  extension tree. König gives infinite height iff the same prefix lies on one
  infinite critical branch.
- **Finite theorem:** EST holds universally through eight marks and survives
  the authenticated larger sample. RH and HT are refuted.
- **Exact debt:** the 128-mark fixture has EST tax 120, only 57 genuinely new
  adjacent charges, and unpaid overlap debt 63.
- **Next falsifiable test:** find a non-adjacent repayment injection on the
  infinite-survival subtree and prove it quantitatively pays the two exact
  pieces of `Q_m`; first test it against the 128-mark debt row and the growing
  E–T windows.

**Wave 8 disposition.**  Actual-adjacent renewal leaves at most one unpaid
internal family, and the adjacent endpoint part of the exact shell debt has a
finite critical-history sum.  The remaining shell debt is a proper
non-adjacent boundary fan, with a separate rank-one Abel fan.  Exact local
cardinality repayment statements are false.  Finally, the pair telescope
shows that all negative old-pair terms save at most a factor two.  These facts
replace the general debt-repayment target by A9.

## A9. Positive birth-budget Carleson theorem

- **Status:** SATURATED — historical Wave 8 foundation, superseded as the
  primary target by A12/P17
- **Evidence:** `[CONDITIONAL]`
- **Mechanism:** group every pair at its unique dyadic birth and retain the
  exact weight `h_i h_j Phi_(ij)/N_(2m)^2`.  Prove that the cumulative positive
  budget `B_H(J)` is `o(log J)` on one infinite eventually critical Golomb
  branch.
- **Exact reduction:**
  `B_H(J)/2 <= sum_(j<=J)<H,Q_j/N_(2m_j)> <= B_H(J)`.
  The signed old-pair tail is therefore irrelevant beyond a constant factor.
- **Positive atom envelope:** every genuine non-adjacent square atom is a
  globally unique Golomb difference; the artificial boundary row sums to at
  most `92/315`.  The remaining loss is the positive square moment, not
  duplicate numerical labels.
- **Closed local variants:** universal `U_global/T` fails at four marks;
  latest-shell density fails at a `C=1` old-clear event; raw non-adjacent
  counts do not repay the single outstanding adjacent family; scaling refutes
  any theorem which omits the critical hypothesis.
- **Next falsifiable theorem:** a two-parameter magnitude/rank-lag Carleson
  injection with bounded overlap across birth epochs, proved from uniqueness
  of all contiguous sums and conditioned on one fixed infinite branch.
- **Guardrail:** no finite critical fixture, even the 682-mark audit, proves
  infinite survival or the vanishing average.

## C4. O'Bryant separated-block gluing

- **Status:** ACTIVE — black-box worst-guarantee iteration blocked; structured
  version retained
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`
- **Obstruction:** guaranteeing one survivor solely from Lemma 9's deletion
  allowance `binom(n,2)` requires a candidate window `Omega(n^4)` and violates
  every fixed all-prefix critical envelope eventually; for `C=1`, all
  `n>=8` fail.
- **Sharp scope:** the quadratic deletion allowance is necessary for some
  sparse separated candidate blocks under only Sidonness and separation.
- **Still eligible:** choose blocks with a sparse actual conflict graph,
  exploit maximum independent sets, avoid large separation by mixed-
  difference signatures, or prove whole-prefix feasibility directly.

## C5. Uniform finite feasibility tree — Q2

- **Status:** ACTIVE — secondary
- **Evidence:** `[RIGOROUS — MODULO NAMED THEOREM]`
- **Mechanism:** prove a nonempty finite level for every depth under the same
  coordinate caps; finite branching plus König supplies an infinite ruler.
- **Boundary:** independently chosen finite witnesses are sufficient only
  when every level uses identical coordinate caps. Existing 128-mark and
  reconstructed 682-mark evidence are finite nodes, not arbitrary-depth
  feasibility; the latter working envelope fails at index 681.
- **Next falsifiable test:** formulate a structured mixed-difference
  construction with a depth-independent cap and audit all collision types.

## C6. Adaptive Hegyvári/parabola-block gluing

- **Status:** ACTIVE — unconditional version quantitatively blocked; adaptive
  version open
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`
- **Mechanism:** use affine, rotated, and uniformly gap-translated finite
  parabola blocks whose internal spectrum avoids the old ruler, then control
  every mixed difference and intermediate prefix.
- **Exact criterion:** a sufficiently separated splice of normalized rulers
  `A` and `B` exists iff `Delta(A) intersect Delta(B)` is empty.
- **Unconditional guarantee:** choosing `u>=max(0,M-p)` avoids an arbitrary
  old diameter `M`, but the safe endpoint is `M+2p(M+p)+1`; this is cubic at
  the critical scale and the first new prefix is already too large.
- **Rigid-menu obstruction:** every full `(p,u)` affine block contains
  `2p+u` and `p(2p+u)`.  Any finite menu can be blocked by an old Golomb ruler
  containing those spans.
- **Still eligible:** an adaptive, survival-conditioned choice with a proved
  small intersection/deletion theorem and a depth-independent intermediate-
  prefix bound.

## E2. Wave 7 primary-source and plugin audit

- **Status:** ACTIVE — qualified literature boundary
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`
- **Closest ingredients:** O'Bryant gluing/deletion, Riblet--Schehr
  compactness, Ma--Yi internal-spectrum packing, Hall/Alexeev--Mixon
  qualitative completion, Fang--Sándor disjoint-spectrum lacunarity, and
  Kraft/graph amortization analogues.
- **Gap:** none supplies the mixed-spectrum infinite-survival innovation
  budget or Q2 all-prefix critical tower.
- **Tool limits:** Consensus quota 30/30; SciSpace adjacent/malformed
  duplicate metadata; Firecrawl generic final listings. No null result is a
  novelty or absence theorem.

## E3. Wave 8 positive-budget and extension literature audit

- **Status:** ACTIVE — qualified literature boundary
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`
- **Closest ingredients:** Ruzsa maximality, Cilleruelo greedy continuation,
  Hegyvári consecutive sums, Bennett--Bohman random greedy, conflict-free
  hypergraph matchings, Lyons branching flows, tree Carleson embedding, and
  Ortega--Prendiville Fejér identities.
- **Gap:** none supplies the positive birth-budget `o(log J)` theorem, its
  exact weighted contiguous-sum injection, or a compatible critical tower.
- **Structural warnings:** unused difference capacity need not yield a legal
  child; infinite survival may be a one-ray tree; known hypergraph and
  Carleson theorems assume the regularity/testing estimate still missing.
- **Tool limits:** Consensus quota 30/30; SciSpace adjacent-only in the
  decisive queries; some Firecrawl bodies interleaved/truncated; the scripted
  saturation gate remains false.  No null result is a novelty claim.

## A10. Scalar rank variance, core tiles, and primitive cross ratios

- **Status:** ACTIVE — foundation refined by A11 after Wave 10
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`
- **Scalar equivalence:**
  `(4/49) sum V_(2^k)<=B_H<=(36/35) sum V_(2^k)`.  This removes the matrix
  bookkeeping while retaining all shell and rank-one births.
- **Forced barrier:** distinct genuine adjacent gaps imply
  `V_n>=n^2/(512N_n)`, hence the critical cap gives an explicit
  `Omega_C(log J)` lower budget.
- **Core reduction:** with `theta_j^2=eta_j=1/(j log j)`, short-rank or
  small-endpoint atoms cost only `O(log log J)`.  The remaining atom has long
  rank distance, two large endpoint gaps, and a globally unique interval
  difference.
- **Tile ledger:** `(R,X,Y,Z)` cells satisfy
  `q<=min(A_XA_Y,Z,2R^2N/Z)` and the exact product/kernel envelope.  Local
  summation still loses the full logarithm.
- **Primitive cross ratio:** `h_i h_j/D_ij^2<=C_ij`, with an exact Abel
  formula and a scale-invariant factorial upper using
  `delta_n^circ=gcd(h_2,...,h_(n-2))`.  The retained state obeys an exact
  dyadic recursion, but the birth sum remains comparable to a positive state
  sum.
- **Next falsifiable theorem:** survival-conditioned non-saturation of the
  core on one fixed ray, formulated as a laminar weighted incomplete-DTS LP
  or an equivalent primitive cross-ratio Carleson estimate.

## E4. Wave 9 primary-source and plugin audit

- **Status:** ACTIVE — qualified literature boundary
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`
- **Closest new source:** Ma--Yi Theorem 4.1 gives a rank-lag/small-difference
  packing inequality; Shearer's DTS LP gives the adjacent linear-programming
  architecture.  Their project transplant is the hereditary `(W9-RLP)`
  inequality for arbitrary epoch subsets.
- **Exact gap:** all checked interfaces are linear in difference lengths.
  None controls the product/kernel core, varying laminar scopes, or supplies
  the required sublogarithmic overlap on one infinite branch.
- **Tool boundary:** independent Exa passes converged on Ma--Yi and O'Bryant;
  Firecrawl known-ID reads succeeded although the main-agent semantic searches
  were empty; Consensus was quota-blocked; SciSpace results were adjacent.
  Overall saturation remains false, so the null is explicitly qualified.

## A11. Survival-conditioned Abel repayment / tensor-box encoding

- **Status:** ACTIVE — partly resolved and refined by A12 after Wave 11
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`
- **New exact inputs:** arbitrary-weight hereditary incomplete-DTS inequality;
  hereditary factorial and weighted log-product packing; fixed-gap future
  kernel tail `O(4^(-K))`; exact dyadic Abel sign support; global spectrum law
  `F_E=(7/4)sum_(m in E)log m+O(|E|)`.
- **Localized deficit:** the plain global distinct-integer certificate leaves
  a leading `(1/4)sum log m` deficit plus secondary `log log` slack.  The
  missing leading quarter comes from the lower-shell fan `q=m-1`.
- **Finite LP obstruction:** after all prefix moduli are fixed, existing
  W9-RLP rows have zero coefficients on current tile occupancy variables.
  Adding them leaves the exact primal and dual unchanged.  A valid new row
  must contain endpoint-product or primitive Abel variables with nonzero
  coefficients.
- **Route A:** with actual bulk mass `A_J`, exact positive-fan mass `Q_J`,
  `T_J=sum theta_m log a_(2m-1)`, set `P_J=A_J-F_E`,
  `S_J=2T_J-Q_J>=0`, and `U_E=T_J-F_E`.  Use the exact identity
  `sum Y_m=U_E-P_J-S_J` and prove
  `P_J+S_J>=U_E-epsilon_J` for some nonnegative
  `epsilon_J=o(log J)`.  A lower-shell-only premium is a stronger sufficient
  candidate and requires its own global floor allocation lemma.
- **Route B:** split weights into `R^2XY` and `R^2Z^2`, encode them on full
  tri-/bi-trees with tensor weights and arbitrary positive measures, and prove
  a summably vanishing box constant.  This is a separate sufficient program,
  not a proved equivalent or necessary reformulation of Route A.
- **Guardrails:** fixed-position decay does not control a moving frontier;
  arbitrary pruning destroys the product-weight hypothesis; four-tree papers
  obstruct straightforward methods but do not prove a general impossibility;
  finite E--T windows and finite survival depth are not an infinite branch.
- **Next falsifiable test:** state a concrete lower-shell premium inequality,
  verify it on every authenticated finite branch and scaled E--T family, and
  prove that its only extra hypothesis is exactly `surv_C=infinity` or a
  monotone finite-depth approximation suitable for König compactness.

## E5. Wave 10 product-tree and weighted-Sidon literature audit

- **Status:** ACTIVE — qualified literature boundary
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`
- **Closest positive results:** product-weight box-to-embedding theorems on the
  full bi-tree (arXiv:1906.11150, Theorem 2.3) and full tri-tree
  (arXiv:2001.02373, Theorem 1.3; DOI `10.4171/RMI/1378`).
- **Negative interfaces:** arXiv:1903.02478 gives an existential pruned-tree
  box/Carleson separation; arXiv:2108.04789 disproves the proposed
  small-energy majorization used by straightforward `T^4` extensions.  These
  are method obstructions with exact scope, not universal impossibility
  theorems.
- **2026 Sidon check:** Ding's rank-weighted theorem is valid, but its error is
  not small at P15 density and it does not control endpoint-gap products.
- **Tool boundary:** Exa 10 searches/100 result slots; Firecrawl five searches/
  75 slots plus 15 related results; SciSpace 30 slots; Consensus quota blocked
  until 2026-09-01.  Targeted interfaces converged, overall saturation is
  false, and the null is qualified only.

## A12. Triangular interval floor and secondary survival repayment

- **Status:** FOUNDATION — refined by A13 after Wave 12
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` for the interval floor and exact
  decompositions.
- **Universal input:** every interval of `ell` adjacent gaps satisfies
  `D_(p,q)>=binom(ell+1,2)`.  With the exact Abel coefficients this gives
  `K_m^len=2 log m+O(1)`, split as `(1/2)log m+O(1)` on the lower shell and
  `(3/2)log m+O(1)` on the interior.  It repays the entire leading quarter
  missing from the Wave 10 global floor.
- **Exact state:** with `G_m^len=A_m-K_m^len>=0` and the exact boundary slack
  `S_m>=0`,
  `T_m-K_m^len=Y_m+G_m^len+S_m`.  Hence over consecutive dyadic epochs,
  `sum Y=(T-K^len)-(G^len+S)` with all three right-hand channels
  nonnegative.  A separate disjoint mixed certificate uses the length floor
  only on `q=m-1` and globally rearranges only `q>=m`; it must not be added to
  `K^len`.
- **[CONDITIONAL] Improvement:** on one fixed infinite eventually
  `C`-critical branch the
  direct envelope improves from Wave 10's displayed `O_C(J^2)` to
  `O_C(J log J)`.  This is not `o(log J)` and therefore does not close P15.
- **Exact secondary state:** the lower residual is a positive future
  cross-ratio tail.  Its dyadic same-pair overlap is
  `Theta(log(j/i))`, so a uniform charge of every occurrence to the pair's
  single birth atom is impossible.
- **Open next theorem:** prove on one fixed
  `surv_C=infinity` branch
  `G_J^len+S_J >= T_J-K_J^len-epsilon_J` with
  `epsilon_J=o(log J)`, using cross-length allocation or a genuinely
  survival-conditioned state.  The theorem must survive E54--E57.

## E6. Wave 11 consecutive-sum, survival, and one-box literature audit

- **Status:** ACTIVE — qualified literature boundary
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`
- **Checked interfaces:** Beck--Bogart--Pham supplies the positive gap-vector /
  consecutive-sum formulation; Beker and RSSS supply finite energy and
  sumset results; Fabian--Rue--Spiegel and O'Bryant supply strong-infinite or
  separated-extension templates; Carter--Hunter--O'Bryant supplies the 2025
  finite-diameter improvement; Cohen--Colonna--Singman,
  Ottazzi--Santagati, and El-Fallah et al. supply one-tree vanishing,
  boundedness, and sharp Dini one-box endpoints.
- **Quantitative boundary:** shifted-factorial sorting within a fixed length
  class improves the triangular floor by only `O(m^(-1/2))` per shell.  The
  2025 diameter theorem has `log diam>=2log m-O(m^(-1/2))`; only its
  subleading correction has that order, and the total-diameter scalar has no
  cross-length/survival state.  Neither route can pay the secondary
  `O(log log m)` profile.
- **Tool boundary:** 26 successful scripted scholarly requests, 351
  deduplicated papers, Exa 18/180, Firecrawl 8 searches plus 3 related calls,
  SciSpace 4/40, and one Consensus attempt blocked at quota 30/30.  Overall
  saturation is false.  The null is qualified and is not an absence or
  novelty theorem.

## A13. Positive cut renewal and integer different-pair packing

- **Status:** FOUNDATION — P18 reclassified by Wave 13
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` for the renewal identity and
  fixed-pair coefficient budget; global P18 packing remains open.
- **Exact renewal:** with the Wave 11 future cut tail `R_m`, four explicit
  nonnegative sectors satisfy
  `Y_m=R_m-R_(2m)+Z_m`.  Hence
  `sum Y_m=R_4-R_(2^(J+1))+sum Z_m` over consecutive dyadic epochs.
- **Overlap repair:** each fixed pair has uniformly bounded total `Z`
  coefficient.  Old-future weights are at most `i/(4m)` and sum
  geometrically; the middle-future sector occurs at boundedly many cuts; the
  birth sectors occur once.
- **Wave 12 proposed theorem:** on one fixed infinite eventually-`C` integer
  Golomb branch, prove `sum_(m in E_J)Z_m=o_C(log J)`.  Wave 13 proves that
  this separate decay cannot coexist with an actual branch in the hypothesis;
  its universal-over-all-`C` form is equivalent to Question 1 and is not a
  smaller packing lemma.
- **Required new input:** packing across different integer interval sums,
  crossing additive relations, or a product-tree encoding that retains this
  arithmetic.  Pairwise coefficient summability alone is insufficient.
- **Mandatory real-model gate:** `a_n=n^2+sqrt(2)n` has unique positive real
  differences and quadratic growth but nondecaying `Y_m`.  An argument that
  never uses integer unit spacing cannot close P18.

## N8. Combined rank-length-containment floor

- **Status:** REJECTED AS A COMPLETE P17 MECHANISM
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`.
- **Theorem:** among all numerical-rank assignments that are linear
  extensions of the complete interval-containment poset, even the optimal
  combined floor with `D>=binom(ell+1,2)` gains less than `5` per epoch over
  `K^len`.
- **Refutes:** paying the secondary accumulated slack using only global rank,
  interval length, and containment monotonicity, even when optimized jointly.
- **Does not refute:** crossing-interval additive identities, numerical unit
  spacing between interval sums, or survival-conditioned coupling.

## N9. Abstract real-Golomb relaxation

- **Status:** REJECTED
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`.
- **Countermodel:** `a_n=n^2+sqrt(2)n` is a quadratic real Golomb ruler and
  `Y_m -> (3/2)(log 2-1/2)>0`.
- **Refutes:** deriving P17 from difference uniqueness, order, quadratic
  growth, and cross-ratio algebra in a form valid over arbitrary real marks.
- **Does not refute:** the original integer problem.

## E7. Wave 12 renewal and critical-product literature audit

- **Status:** ACTIVE — qualified literature boundary
- **Evidence:** `[LITERATURE STATUS — PUBLIC RECORD ONLY]`.
- **Closest geometry:** Martikainen's `arXiv:2608.22628` combines two
  individually nonsummable depth weights at the critical exponent under
  pairwise incomparability and a Zygmund boundary relation.  It is a sharp
  Route B template, not an arithmetic encoding.
- **Closest completion result:** Chen--Fang DOI
  `10.1016/j.jcta.2026.106239` constructs a density-shadowing perfect
  difference set from any Sidon set, but deletes input elements and inserts
  new ones.  It neither preserves a prescribed prefix nor improves the input
  exponent.
- **Tool boundary:** Exa 6/62, Firecrawl paper index 6/72 plus one publisher
  scrape, SciSpace 5/50, arXiv MCP primary sections, and two Consensus quota
  failures.  Overall saturation is false; the null is qualified only.

## A14. Harmonic new-birth barrier and signed frontier repayment

- **Status:** ACTIVE — exact Route A boundary after Wave 13
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` for the finite theorem,
  conditional only when an eventual-critical branch is invoked.
- **Universal integer floor:** with
  `H_m=a_(2m-1)-a_(m-2)` and
  `E_m=m(m-2)(m^2+8m+6)/48>=m^4/48`,
  `Y_m,Z_m>=Z_m^nb>=E_m/(8m^2H_m)>=m^2/(384H_m)`.
- **Harmonic consequence:** an eventual
  `a_n<=C n^2 log(2n)` cap would force both dyadic sums to have
  `liminf/log J >=1/(1536C log2)`.  Hence the forms of P17 and P18 quantified
  over all `C>0` are each logically equivalent to Question 1.  This is a
  reduction, not a solution or a construction of a critical branch.
- **Exact signed target:** retain the terminal channel:
  `sum_(m in E_J)Z_m-R_(2^(J+1))=o_C(log J)`.  This is exactly P17 after
  absorbing `R_4`; proving it universally is itself Question-1-equivalent.
- **Frontier spectrum:** the exact interval-log expansion is
  `Z_m=mathfrak P_m+mathfrak U_m-mathfrak B_m-mathfrak F_m-mathfrak e_m`.
  With `X_m=mathfrak U_m-mathfrak B_m`,
  `0<=Z_m<=X_m+epsilon_m` and
  `epsilon_m=((4m-3)/(16m^2))log a_(2m-1)` has finite dyadic sum under the
  cap.  Nevertheless
  `sum X_m >=(1536C log2)^(-1)log J-O_(C,a)(1)`.
- **Interpretation:** the terminal suffix fan necessarily beats its interior
  descendants harmonically on every hypothetical critical branch.  A new
  Route A lemma must be genuinely cross-epoch and arithmetic, or explicitly
  preserve terminal-tail cancellation; within-epoch positive sparsification
  cannot close the argument.
- **Artifacts:**
  `endpoint_variance/WAVE13_P18_HARMONIC_OBSTRUCTION_2026-08-29.md` and
  `endpoint_variance/WAVE13_FRONTIER_SPECTRUM_AND_SIGNED_REPAYMENT_2026-08-29.md`.

## N10. Separate positive decay of Y or Z on a surviving critical branch

- **Status:** RECLASSIFIED — QUESTION-1-EQUIVALENT, NOT AN INTERMEDIATE LEMMA
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`.
- **Obstruction:** the integer new-birth subtriangle alone contributes at
  least `m^2/(384H_m)`, hence at least
  `1/(1536C log(4m))` per sufficiently large dyadic epoch under a critical
  cap.
- **Refutes:** treating either `sum Y=o(log J)` or `sum Z=o(log J)` as a
  compatible regularity property of a hypothetical surviving branch.
- **Does not refute:** the universal assertions themselves; if Question 1 is
  true their hypothesis class is empty.  It proves the exact all-`C`
  equivalence and leaves Question 1 unresolved.

## N11. Bare integer-cell occupancy and central-rank pointwise charges

- **Status:** REJECTED IN THEIR LITERAL FORMS
- **Evidence:** `[RIGOROUS IDENTITY + CERTIFIED FINITE DIAGNOSTICS]`.
- **Exact carriers:**
  `C_(i,j)=sum_(s<h_i,t<h_j) kappa_(M+s+t)` with
  `kappa_n=log((n+1)^2/(n(n+2)))>0`; for fixed rank distance, the two central
  differences form disjoint paths whose vertices have degree at most two.
- **Lattice obstruction:** Golomb uniqueness controls the four corner
  differences, not all internal levels `M+s+t`.  The literal occupancy bound
  `M_n<=1` already fails in the complete eight-mark scope, and raw maxima are
  large on the authenticated 64/128-mark fixtures.
- **Central-rank obstruction:** complete finite witnesses have consecutive
  integer and adjacent-rank central values; the pointwise candidate
  `C_(i,j)<=|log(B/C)|` is false, with ratios above `17` in the bounded
  all-prefix scope and above `226` on the Hall fixture.
- **Scope:** the path theorem is reusable, while the rank-envelope table is
  only a finite diagnostic and not an asymptotic impossibility theorem.  A
  viable charge must retain outer/inner curvature or a survival-conditioned
  multiplicity estimate.
- **Artifact:**
  `endpoint_variance/WAVE13_LATTICE_CELL_AND_CENTRAL_RANK_NO_GO_2026-08-29.md`.

## A15. Cap-dependent future-rank promotion and legal next-shell rebate

- **Status:** ACTIVE — RIGOROUS HARMONIC RESOURCE, GLOBAL SIGNED UPPER OPEN
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]`, with an independent coefficient
  audit and deterministic finite certificate.
- **Promotion theorem:** for an old difference `d in Delta_L`, spatial bins
  in `N=floor(d/log^2 d)` future marks give, under the explicit eventual-cap
  side conditions,
  `rho_infinity(d)-rho_L(d)>=d/(64C log d)`.
- **Macroscopic consequence:** for `d_(m,p)=D_(p,2m-1)`, `2<=p<=m`,
  `log(rho_infinity/rho_(2m))>=1/(512C log m)` eventually.
- **Legal coefficient:** the same atom reappears in the next lower shell with
  `v_(m,p)=(4m-2p+1)/(16m^2)`.  The exact rank/hole split proves
  `A_J>=K_J^star+Phi_(J-1)` without overlap with the interior part of
  `K^mix`.
- **Scale:** the macroscopic `v`-mass tends to `3/16`, and the sharper
  promotion formula yields
  `Phi_m>=(3/2048-o_C(1))/(C log m)`.
- **Boundary:** this does not imply `Phi>=Y`, `Phi>=Z`, or an upper bound for
  `X`; those are separate positive quantities.  The remaining suffix
  coefficient `u-v` has macroscopic mass tending to `3/8`.
- **Artifacts:**
  `endpoint_variance/WAVE14_FUTURE_RANK_PROMOTION_2026-08-29.md`,
  `endpoint_variance/WAVE14_PROMOTION_REBATE_AND_ALLOCATION_BOUNDARY_2026-08-29.md`,
  and `endpoint_variance/wave14_future_rank_promotion_certificate_2026-08-29.json`.

## A16. Adjacent-epoch nested promotion allocation

- **Status:** FOUNDATION — LOCAL REUSE SOLVED; DISJOINTNESS CLOSED BY WAVE 17
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` plus finite Hall-64 and
  Erdős--Turán-128 calibration.
- **Local count:** in the immediately following block,
  `K_p=rho_(4m-1)(d_(m,p))-rho_(2m)(d_(m,p))
  >=d_(m,p)/(128C log(8m))` eventually.
- **Literal carrier:** every new difference at most `d_(m,p)` is an atom of
  `mathfrak B_(2m)` with coefficient at least `1/(16m^2)`.
- **Nested load theorem:** for
  `Delta_m=sum_(p=2)^m u_(m,p)log(1+K_p/r_p)`, the total reuse load on one
  new numerical difference is below `3/(4m^2)`.  Hence
  `1/(512C log(8m))<=Delta_m<=mathfrak B_(2m)+O(m^-2)`.
- **Boundary:** this original proof spends the whole selected
  `beta(x)log x` value.  Wave 17 supplies a separate same-atom residual and a
  stronger local rearrangement floor, closing this local overlap for the
  triangular floor.  Sending uncapped loads to much later births can still
  incur a `4^k` coefficient mismatch.
- **Next theorem:** P22, the signed repayment of promotion above the fixed
  cap with the full endpoint/descendant renewal retained.
- **Artifact:**
  `endpoint_variance/WAVE15_LOCAL_PROMOTION_ALLOCATION_AND_HORIZON_OBSTRUCTION_2026-08-29.md`.

## A17. Multiscale constant-fraction future-rank filling

- **Status:** ACTIVE — RIGOROUS CONDITIONAL THEOREM, SIGNED USE OPEN
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` plus a deterministic finite
  block-disjointness certificate.
- **Mechanism:** use the mutually disjoint blocks
  `M_t=2^tL`, `0<=t<=floor((log_2L)/2)`.  Under
  `d>=L^2/8` and `sqrt(L)>=128C log(4L^(3/2))`, each block produces more
  than `d/(64C log L)` new differences below `d`.  Golomb uniqueness makes
  all witnesses across blocks distinct.
- **Theorem:**
  `rho_infinity(d)-rho_L(d)>d/(128C log2)`.
- **Suffix consequence:** with
  `kappa_C=log(1+1/(128C log2))`, every macroscopic suffix promotion is at
  least `kappa_C`; consequently `Phi_m>=kappa_C/6` and the residual `u-v`
  resource is at least `kappa_C/3` eventually.
- **Hole consequence:** `log(d/rho_infinity(d))=O_C(1)` on these suffixes.
- **Boundary:** this is a positive rank resource.  It cannot be subtracted
  from `X_m` without a disjoint negative carrier.  Finite fixture rows do
  not satisfy the asymptotic side condition and do not construct a branch.
- **Artifacts:**
  `endpoint_variance/WAVE16_MULTISCALE_FUTURE_RANK_FILLING_2026-08-29.md`
  and
  `endpoint_variance/wave16_multiscale_future_rank_certificate_2026-08-29.json`.

## A18. Terminal renewal potential and Fejer taper

- **Status:** FOUNDATION — TERMINAL HORIZON REPAIRED; LOCAL OVERLAP CLOSED BY WAVE 17
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` plus exact rational
  coefficient and taper certificates.
- **Exact identity:**
  `Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`, with
  `mathcal T_m>=0`.
- **True terminal size:** rowwise prefix/descendant mass equality and the
  interior triangular floor give
  `Z_m-R_(2m)<=(3/4)log log(4m)+O_C(1)`.
- **Taper:** `omega_(k,J)=((J+1-k)/(J+1))^2` preserves
  `sum omega/k=log J+O(1)`, gives favorable renewal signs, makes the raw
  terminal fan `O_C(1/J)`, and makes the one-step `Delta` reindexing loss
  `O(1)` because `Delta_m<log13`.
- **Boundary:** the taper does not manufacture new negative capacity.  Wave
  17 supplies the missing local disjoint premium, but the part of the
  residual promotion above the fixed cap still lacks a signed insertion.
- **Artifacts:**
  `endpoint_variance/WAVE16_TERMINAL_POTENTIAL_2026-08-29.md` and
  `endpoint_variance/wave16_terminal_potential_certificate_2026-08-29.json`.

## A19. Same-atom residual capacity above the triangular floor

- **Status:** COMPLETE — LOCAL P21 INEQUALITY
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` plus exact finite ownership and
  coefficient/load checks.
- **Mechanism:** ten layers of near differences in a consecutive integer
  Golomb interval imply `x/L_s>=3/2` for every selected value `x>=2147`.
  The target Gothic atom retains `beta_x log(x/L_s)` after the triangular
  floor.
- **Theorem:** with `c_0=log(3/2)/12` and
  `E_m=2146log(3/2)/(16m^2)`,
  `mathfrak B_(2m)>=K_(2m)^int+c_0Delta_m-E_m`.
- **Why disjoint:** the proof uses only the literal residual of each selected
  atom above its already-spent triangular amount; the error discards at most
  the 2146 small positive integer values.
- **Boundary:** a positive local lower bound is not a signed terminal upper.
- **Artifacts:**
  `endpoint_variance/WAVE17_DISJOINT_RESIDUAL_CAPACITY_AND_EXCESS_BOUNDARY_2026-08-29.md`
  and
  `endpoint_variance/wave17_residual_capacity_certificate_2026-08-29.json`.

## A20. Local sorted-rank surplus and capped promotion

- **Status:** COMPLETE — LOCAL CAPACITY AND FIXED CAP
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` with an independently audited
  constant-tracked asymptotic estimate.
- **Exact floor:** for `a=n-1`, `b=3(n-1)(n-2)/2`, and
  `c=(n-1)(3n-4)/2`,
  `F_n^(loc,int)=[2log(a!)+log(b!)+log(c!)]/(4n^2)` and
  `mathfrak B_n>=F_n^(loc,int)`.
- **Surplus:** for `D_n=F_n^(loc,int)-K_n^int`,
  `|D_n-[3/2+(3/4)log3-2log2]|<=18(1+log n)/n` for `n>=16`.
  Hence `D_n>81/128` for `n>=2^20` and `D_n>3/4` for
  `n>=2^22`.
- **Consequences:** the same single floor gives
  `mathfrak B_(2m)>=K_(2m)^int+(3/8)Delta_m` eventually, or alternatively
  pays the entire residual `u-v` promotion truncated at logarithmic height
  two.
- **Boundary:** those two uses are alternatives, not additive claims.  The
  excess `Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+` can be
  `O_C(log log m)` per epoch and is not paid by the local theorem.
- **Wave 18 disposition:** the excess is inserted into the signed identity up
  to one explicit descendant-jump functional; see A21--A22 and P23.
- **Artifact:**
  `CONTINUATION_2026-08-29_WAVE17_DISJOINT_CAPACITY_AND_EXCESS.md`.

## A21. Exact descendant-jump insertion

- **Status:** COMPLETE — P22 SIGN AND LOCAL-CARRIER SUBPROBLEM
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` with exact coefficient checks.
- **Mechanism:** the target-interior row capacities satisfy
  `w_(n,p)>=r_(n,p)`.  The unused sorted-rank slack pays
  `Theta_n^(exc,h)` except for the explicit positive functional `J_n^(h)`.
- **Signed theorem:** at `h=5/2`, the target surplus pays the previous source
  cap and
  `Z_n-R_(2n)=mathfrak P_n-K_n^int-mathcal T_n`
  `-Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)+J_n^(5/2)-(U_n+Q_n)`,
  where `mathcal T_n,U_n,Q_n>=0`.
- **Interpretation:** because `c_n/L_(n,p)<3`, `J_n^(h)` sees only large
  descendant-to-terminal jumps.  No atom is used twice.
- **Boundary:** the theorem does not bound the tapered sum of `J`.
- **Artifact:**
  `endpoint_variance/WAVE18_EXCESS_DESCENDANT_JUMP_AND_BIRTH_LOCALITY_2026-08-29.md`.

## A22. All-source rank-layer allocation and birth locality

- **Status:** ACTIVE — REUSE BOUND COMPLETE, BIRTH-TIME CARRIER P23 OPEN
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` plus exact finite constant
  checks.
- **Mechanism:** layer-cake the logarithmic rank excess and assign each unit
  interval to the future numerical difference occupying that rank slot.
- **Theorem:** a fixed future difference receives total post-cap dyadic load
  `<[8C log2/(3exp(h))]log(4x)/x` eventually.
- **Midpoint reduction:**
  `J_n^(h)<=sum_p r_(n,p)[log(d_(n,p)/D_(p,n))-(h-log3)]_+`.
  Scalar alternating jumps and terminal-cap-compatible finite Golomb rows
  show that positive-part telescoping or a stronger one-epoch estimate cannot
  make its tapered sum little-oh.
- **Remaining debt:** current hypotheses do not bound the dyadic birth scale
  in terms of `x`, guarantee unused slack above the local rank floor, or put
  terminal births inside the interior carrier.
- **No-go boundary:** prime Erdős--Turán rulers keep one-epoch `H_n^loc`
  bounded, and an unconditional distant-block extension defeats any
  terminal-identity-only upper without the critical cap.
- **Next theorem:** P23, a birth-time Carleson/renewal estimate for the
  tapered `J_n^(5/2)` sum or an equivalent signed cancellation.
- **Artifact:**
  `CONTINUATION_2026-08-29_WAVE18_DESCENDANT_JUMP_AND_BIRTH_LOCALITY.md`.

## N12. Raw suffix repayment from local promotion witnesses

- **Status:** REJECTED IN THE LITERAL RAW-LOG FORM
- **Reason:** a witness difference satisfies `x<=d_(m,p)`, hence
  `log x<=log d_(m,p)`.  The valid layer-cake proof pays only the marginal
  log-rank increment `log(1+K_p/r_p)`, not `log d_(m,p)`.
- **Finite counterchecks:** equal-share raw allocation leaves an unpaid
  `2.65023` on Hall 64 at `m=16` and `1.60917` on Erdős--Turán 128 at
  `m=32`.
- **Does not refute:** a disjoint aggregate allocation using coefficient
  rearrangement, a terminal potential, or all-epoch arithmetic structure.

## N13. Positive-density difference coverage as a shortcut

- **Status:** REJECTED AS A SHORTCUT; EXACT LOGICAL REDUCTION RECORDED
- **Primary boundary:** Chen--Fang construct, from any infinite Sidon set
  `B`, a perfect difference set whose counting function shadows `B(x/2)` up
  to any prescribed divergent error.  Thus any hypothetical critical
  counterexample can be replaced by a critical perfect-difference
  counterexample.
- **Consequence:** proving the Question-1 liminf-zero statement even only for
  perfect difference sets, or excluding a critical Sidon set with positive
  difference density, would already settle Question 1.  This is not an
  easier preliminary lemma.
- **False stronger claim:** a universal `rho_A(x)=o(x)` is refuted by perfect
  difference sets, which have `rho_A(x)=floor(x)`.  Cilleruelo--Nathanson also
  show that full coverage does not force a full `o(sqrt(x/log x))` law.
- **P22 boundary:** whole-set completion deletes and inserts marks; it does
  not preserve a prescribed prefix, suffix ranks, or signed birth-time
  ownership for the uncapped promotion excess on the existing ray.
- **Artifact:**
  `research_sources/WAVE16_PERFECT_DIFFERENCE_COMPLETION_BOUNDARY_2026-08-29.md`.

## A23. Cross-ratio half absorption and endpoint-deficit cancellation

- **Status:** COMPLETE — SIGN-FAITHFUL P23 REDUCTION
- **Evidence:** `[RIGOROUS — SELF-CONTAINED]` plus exact rational coefficient
  enumeration and four deterministic Golomb fixture checks.
- **Rectangle theorem:** the exact terminal/descendant ratio is a positive
  cross-ratio rectangle, and its Wave 18 coefficient is at most one half of
  the corresponding Wave 12 `Y_n` coefficient.  Hence `S_n<=(1/2)Y_n`.
- **Endpoint theorem:** the remaining endpoint coefficient satisfies
  `lambda_(n,q)<(3/4)c_(n,q)`; the constant is the sharp uniform supremum.
  Therefore the endpoint overshoot consumes at most `3/4` of the existing
  prefix/full-span deficit, leaving `-(1/4)Dpre_n`.
- **Signed result:**
  `Z_n<=(1/2)Y_n+G_n+epsilon_n`
  `-(U_n^cap+Q_n+mathfrak e_n)`, with all discarded terms nonnegative and
  `sum epsilon_(2^k)<infinity` under a fixed eventual cap.
- **Boundary:** this uses the uncontracted Wave 13 spectrum.  Expanding the
  Wave 16 terminal potential at the same time would double-spend
  `mathfrak F_n`.
- **Artifact:**
  `endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`.

## A24. Current-scale signed frontier P24

- **Status:** OPEN, HISTORICAL UPSTREAM TARGET — SUPERSEDED BY A25/P25
- **Evidence:** `[CONDITIONAL]` as the remaining theorem; its reduction and
  cap reindexing are rigorous.
- **Target:** for every fixed compatible infinite eventual-`C` branch,
  `sum omega G=o_(C,a)(log J)`.  The exact weaker sufficient threshold is
  `limsup(sum omega G)/log J<1/(3072C log2)`.
- **Current-scale form:** replacing the preceding cap by the current total
  promotion gives `sum omega G<=sum omega Ghat+15/16`.  A sufficient next
  lemma is `sum omega (Ghat)_+=o_(C,a)(log J)`.
- **Exact obstruction:** shifting the raw `v log d` fan across one Fejer
  step incurs `(log2/6)J+O_C(log J)`; the macroscopic half alone contributes
  `(log2/8)J+O_C(log J)`.  This is a leading channel, not a bounded horizon
  error.  `K^low+Phi` also has different ownership from `K_n^int`.
- **New boundary:** a prime Erdős--Turán dilation family makes `Ghat_n`
  grow like `Omega(log log n)` while satisfying a fixed `C=32` cap on the
  relevant one-scale window.  Independent dyadic copies have Fejer sum
  `Omega(J log J)`.  They are not one compatible infinite branch, but they
  prove that same-scale Golomb, rank, and cap facts cannot establish P24's
  current-scale positive-part estimate.
- **Next mechanism:** retain the authenticated rank slack inside `Q_n` and
  pass to the dilation-invariant A25/P25 remainder.
- **Artifact:**
  `CONTINUATION_2026-08-29_WAVE19_CROSS_RATIO_AND_SPARSE_SPIKE.md`.

## A25. Certified rank-slack and the dilation-invariant P25 remainder

- **Status:** COMPLETE REDUCTION — EQUIVALENT TO A26 UP TO SUMMABLE PAIR
- **Evidence:** `[RIGOROUS — SELF-CONTAINED REDUCTION]`; the remaining
  positive-part theorem is conditional and open.
- **Sorted atoms:** order all Gothic interior values as
  `x_(n,1)<...<x_(n,c_n)` and carry their actual coefficients `gamma_(n,j)`.
  Then
  `Srank_n=sum gamma_j log(x_j/j)>=0` and
  `Pair_n=sum gamma_j log j-F_n^(loc,int)>=0`, with
  `H_n^loc=Srank_n+Pair_n` exactly.
- **Certified ownership:** the Wave 18 excess proof uses at most
  `Srank_n`, so
  `Q_n^cert=Srank_n+J_n^(5/2)-Theta_n^(exc,5/2)>=0` and
  `Q_n=Q_n^cert+Pair_n`.  `Srank_n` is not available for a second floor.
- **Signed result:** retaining `Q_n^cert`, the cap surplus, and the singleton
  gives
  `Z_n<=(1/2)Y_n+R_n^cert`, where
  `R_n^cert=mathfrak U_n-F_n^(loc,int)-Srank_n-J_n^(5/2)`
  `-(1/4)Dpre_n-mathfrak e_n+epsilon_n`.
- **Exact audit:**
  `R_n^cert=Z_n+(3/4)Dpre_n-J_n^(5/2)+Pair_n`.
  It is prefix-local and exactly invariant under integer dilation of the
  whole ruler; the previous/current capped promotion cancels before the
  final expression is formed.
- **Target:**
  `sum omega (R_(2^k)^cert)_+=o_(C,a)(log J)`.  A stronger non-vacuous
  finite formulation asks
  `sum_(k=L)^(2L)(R_(2^k)^cert)_+=o_C(1)` uniformly over compatible finite
  cap-respecting towers.
- **Nonclaim:** neither dilation invariance nor the certified extraction
  proves the target.  P19/P24/P25, both Erdős questions, novelty, and every
  prize claim remain open.
- **Artifact:**
  `endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`.

## A26. Direct rank-free sharp remainder P26

- **Status:** SATURATED AS A STANDALONE UPPER TARGET — RETAINED EXACT
  REDUCTION
- **Evidence:** `[RIGOROUS — SELF-CONTAINED REDUCTION]`; the remaining
  positive-part theorem is open.
- **Unambiguous endpoint notation:** let `E_n^(end,5/2)` denote the Wave 19
  endpoint component, not the Wave 18 promotion excess.  Wave 19 proves
  `J_n^(5/2)<=E_n^(end,5/2)+(1/2)Y_n` and
  `(mathfrak P_n-mathfrak F_n)+E_n^(end,5/2)`
  `<=-(1/4)Dpre_n+epsilon_n`.
- **Direct signed result:** adding the untouched terms of the exact Wave 13
  spectrum gives
  `Z_n<=(1/2)Y_n+R_n^sharp`, where
  `R_n^sharp=mathfrak U_n-mathfrak B_n-J_n^(5/2)`
  `-(1/4)Dpre_n-mathfrak e_n+epsilon_n`.
- **Exact identity:**
  `R_n^sharp=Z_n+(3/4)Dpre_n-J_n^(5/2)`.  It is prefix-local, contains no
  rank at infinity, needs no cap reindexing, and is exactly invariant under
  integer dilation.
- **P25 equivalence:**
  `R_n^cert=R_n^sharp+Pair_n`, with
  `0<=Pair_n<=(3/(4n^2))log binom((n-1)(3n-4)/2,n-1)`.
  Hence `sum_k Pair_(2^k)<infinity`; the P25 and P26 weighted targets differ
  by `O(1)`, and their exponent-block targets differ by `O(L2^(-L))`.
- **Historical target:**
  `sum omega (R_(2^k)^sharp)_+=o_(C,a)(log J)`, or the stronger compatible
  finite-window form
  `sum_(k=L)^(2L)(R_(2^k)^sharp)_+=o_C(1)`.
- **Ownership:** `mathfrak B_n` is the actual negative bulk and is used once.
  No `K_n^int`, `F_n^(loc,int)`, `Srank_n`, promotion excess, or Wave 16
  terminal potential is inserted into this direct proof.
- **Disposition:** the A27 inner-new-birth floor shows that on any extant
  eventual-`C` branch this remainder already has harmonic mass twice the
  strict P26-sharp allowance.  Thus P26 is not an easier standalone packing
  lemma.  This conditional conflict is not an unconditional proof or
  refutation of an Erdős question.
- **Artifact:**
  `endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`.

## A27. Nonnegative profile remainder and saturation boundary

- **Status:** COMPLETE NO-GO FOR UNCHANGED P26/P27 UPPER TARGET
- **Evidence:** `[RIGOROUS — SELF-CONTAINED CONDITIONAL SATURATION]`.
- **Row-exact absorption:** with
  `t_(n,p)=5/2-log(c_n/L_(n,p))`, put
  `E_n^row=sum alpha beta [log(A/a_q)-t_(n,p)]_+` and
  `Delta_n=J_n^(5/2)-E_n^row`.  The positive-part contraction gives
  `0<=Delta_n<=S_n`.
- **Coefficient strengthening:** if
  `Z_n^fin=Z_n^ob+Z_n^nb`, the Wave 19 rectangle coefficients obey
  `S_n<=Z_n^fin` exactly, including `x=2,y=1` and `x=1` corners.
- **Profile remainder:**
  `R_n^prof=Z_n+E_n^row-J_n^(5/2)=Z_n-Delta_n`
  `=(Z_n^fin-S_n)+Z_n^fut+(S_n-Delta_n)>=0`, and
  `R_n^sharp=R_n^prof+(3Dpre_n/4-E_n^row)>=R_n^prof`.
  The last sign follows from
  `E_n^row<=E_n^(end,5/2)<=3Dpre_n/4`.
- **Untouched sector:**
  `W_n=sum_(j=n+2)^(2n-1)sum_(i=n)^(j-2)`
  `((j-i)^2/(4n^2))C_(i,j)` lies inside `Z_n^fin-S_n`, because the
  descendant rectangle has only `i<=n-1`.
- **Exact floor:** for `H_n'=a_(2n-1)-a_(n-1)`,
  `W_n>=E_n'/(8n^2H_n')`, where
  `E_n'=n(n-2)(n^2+4n-14)/48`.  For dyadic `n>=16` and an eventual-`C`
  cap,
  `R_n^sharp>=R_n^prof>=W_n>1/(1536C log(4n))`.
- **Consequence:** on any extant eventual-`C` branch the Fejer liminf is at
  least `1/(1536C log2)`, twice P26-sharp's allowed constant.  This closes
  unchanged P26/P27 as an easier intermediate upper theorem; it does not
  prove that an eventual-critical branch exists or does not exist.
- **Artifact:**
  `endpoint_variance/WAVE19_NONNEGATIVE_SHARP_REMAINDER_DECOMPOSITION_2026-08-29.md`.

## A28. Inner-new-birth relocation with negative renewal ownership

- **Status:** ACTIVE — CURRENT HIGHEST-VALUE ROUTE A
- **Evidence:** `[OPEN SIGNED DIRECTION AFTER RIGOROUS LOCAL CAP/TRANSPORT AUDITS]`.
- **Required mechanism:** retain the exact Wave 12 negative cut terms and
  construct a cross-scale carrier that removes a positive amount of `W_n`
  from `R_n^prof` without also spending that atom as retained birth signal.
  A model target is
  `Z_n<=Y_n/2+R_n^prof-eta W_n+V_n-V_(2n)+Err_n`, with fixed `eta>0`,
  favorable or bounded Fejer reindexing of `V`, and tapered `Err=o(log J)`.
- **Ownership gate:** support `i>=n` in `W_n` and support `i<=n-1` in the
  descendant rectangle must remain disjoint.  No full-span coefficient,
  rank slack, or renewal cut may be used twice.
- **Success criterion:** after relocation, the retained dyadic birth signal
  must still have a positive harmonic constant strictly larger than the
  new residual constant.  Merely asking for pointwise or block smallness of
  `R_n^prof` is ruled out by A27.
- **Nonclaim:** no such carrier is currently proved.  A28 does not answer
  Question 1 or 2 and supports no novelty or prize claim.

### A28.1 Full-row ownership boundary

- The naive full-`u` allocation is closed: it first exceeds the finite
  coefficient at `n=6`, tends to a worst ratio `9/8`, and double-spends the
  cut coefficient because `u=v+bar r`.
- The legal demand is `bar r`.  Its natural transport fits every beta row and
  proves `Sbar<=Y/2`, but leaves more than half of the saturated inner
  `W_n` channel.
- **Disposition:** use only `bar r`; keep `v` inside the whole negative cut.

### A28.2 Adaptive-cap and actual-rank boundary

- With `h_p=max(3/2,log(c_n/L_p))`, the actual cap is bounded by the
  deterministic profile `Cdet=sum bar r_p h_p`; it is not generally equal
  to that profile.
- The exact bound
  `Cdet_n<0.8336738101+0.3009853/n` and the Wave 17 surplus estimate give
  `D_N>Cdet_(N/2)>=Theta_(N/2)^cap` for `N>=2048`.
- Actual ranks leave the endpoint term:
  `Theta^exc<=Srank+S_t+E_t^rank`.  The candidate bound without
  `E_t^rank` is invalid at the atomic level.
- **Disposition:** the cap is no longer the barrier; the positive
  cross/endpoint terms must remain in the signed ledger.

### A28.3 Arbitrary-transport residual floor

- Every feasible transport, even one chosen after inspecting the energies,
  leaves
  `E_n^res(t)>=n^2/(2^25 H_n')` for dyadic `n>=64`.
- On an eventual-`C` branch the corresponding Fejer liminf is at least
  `1/(2^27 C log2)`.  The last-two-row corner has exact coverage ratio
  `1/3` for every feasible transport.
- **Disposition:** optimizing the transport alone cannot complete A28.
  The primary remaining route is cancellation/domination by the intact
  signed whole-cut or terminal-potential ledger.

### A28.4 Current falsifiable target

The verified mixed transport `t=(8t0+tR)/9` preserves `S_t<=Y/2` and
improves the endpoint to `E_t^rank<=2Dpre/3`.  Retain the exact
cap/rank/Pair bracket and prove the Fejer bound for

`Gmix=R+Pcoef log A-Kint-T-ThetaFull-Dpre/3`

strictly below
`1/(3072C log2)`, or prove the clean tapered positive-part estimate
`sum omega (Gmix_(2^k))_+=o(log J)`.  Any proposed shortcut must be rejected if
it extracts a raw `v` fan while keeping the negative cut, reuses the dropped
`D-cap+Q+Pair` bracket, or tries to solve the problem by transport coverage
alone.

The mixed gain is exactly `Dpre/12`, but the unsigned implication
`W-S_t<=Dpre/12` is false on the certified eight-mark `n=4` Golomb ruler.
The surviving route must therefore use the signed whole-cut terms in
`Gmix`; the endpoint saving is not a standalone payment theorem.
- **Artifacts:**
  `endpoint_variance/WAVE19_P28_ADAPTIVE_ROW_CAP_CANDIDATE_2026-08-29.md`,
  `endpoint_variance/WAVE19_P28_ARBITRARY_TRANSPORT_RESIDUAL_FLOOR_2026-08-29.md`,
  and
  `endpoint_variance/WAVE19_P28_MIXED_RIGHT_GREEDY_ENDPOINT_GAIN_2026-08-29.md`.

## N14. Literal positive P23 after sparse spike/cooldown

- **Status:** NOT REFUTED, BUT NO LONGER RECOMMENDED
- **Finite evidence:** one exact `C=32` Golomb chain reaches 512 marks and
  contains a certified stage with `J_128=0.3091860771...`; both 256- and
  512-stage maximum legal terminals are exact for their fixed cores.
- **Scope:** the first-legal cooldown branch is not globally exhaustive and
  no infinite compatible tower is constructed.  Therefore this is neither
  a P23 counterexample nor a solution of Question 1 or 2.
- **Disposition:** use the finite chain to falsify local and one-epoch
  arguments; attack P24's signed `Ghat` target instead of `J` in isolation.
- **Artifacts:**
  `endpoint_variance/WAVE19_SPARSE_SPIKE_COOLDOWN_BOUNDARY_2026-08-29.md`
  and `endpoint_variance/wave19_sparse_spike_certificate_2026-08-29.json`.

## E8. Wave 19 fixed-branch literature audit

- **Status:** COMPLETE SCOPED SEARCH; NO MATCHING THEOREM FOUND
- **Evidence:** 345 deduplicated records, 10 manually selected Sidon/Golomb
  sources, six full reads, one explicit paywall exception, and three shallow
  records.  Connector limitations are recorded.
- **Closest interfaces:** Carter--Hunter--O'Bryant for finite energy and
  Cilleruelo--Nathanson for qualitative birth/completion.
- **Boundary:** neither supplies a quantitative first-birth delay, terminal
  ownership, or fixed compatible critical branch.  The null is not a proof
  of theorem nonexistence and not a novelty claim.
- **Artifacts:** `../research_sources/wave19_literature_state/`.
