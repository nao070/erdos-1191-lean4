# Approach Registry — Erdős Problem #1191

**Updated:** 2026-08-29 continuation, Wave 0--13  
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

- **Status:** ACTIVE — current primary implementation is A14/P19
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
