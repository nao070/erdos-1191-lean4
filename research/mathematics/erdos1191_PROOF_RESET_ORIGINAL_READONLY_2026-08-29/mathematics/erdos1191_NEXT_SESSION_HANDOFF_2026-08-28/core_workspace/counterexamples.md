# Counterexamples, Zero Modes, and Computational Evidence

Every entry distinguishes exact present artifacts from older reported experiments whose source/raw files are missing.

## E1. Baseline Sidon-check harness — legacy reported result

- **Status:** `[COMPUTATIONAL — EXPERIMENTAL]`
- **Legacy paths:** `computation/check_sidon.py`, `computation/out/check_sidon.json`.
- **Reported outcome:** 60/60 battery, 600/600 fuzz agreement, 600/600 transport checks.
- **Use:** prior calibration only.
- **Caution:** the code and raw output are not in this handoff; do not call this independently rerun.

## E2. Forbidden-position recurrence — legacy reported result

- **Status:** `[COMPUTATIONAL — EXPERIMENTAL]`
- **Legacy paths:** `computation/forbidden_recurrence.py`, `computation/greedy_growth.py`, `computation/out/forbidden_recurrence.json`.
- **Reported outcome:** exhaustive and fuzz tests passed in the older workspace.
- **Use:** historical context for greedy-extension work.
- **Caution:** source/raw files absent.

## E3. Naive dense translated-block gluing obstruction

- **Status:** `[COMPUTATIONAL — EXPERIMENTAL]`
- **Legacy paths:** `computation/crossblock.py`, `computation/out/crossblock_scaling.json`.
- **Tested hypothesis:** append a dense finite Sidon block near the old maximum using a generic translation.
- **Reported trend:** the forbidden shadow `F(V)=V+D(V)` became nearly/full dense in a fixed short interval above `max(V)` as the tested old ruler size increased; the reported compatibility ratio reached zero in the tested regimes.
- **Valid conclusion:** the tested near-adjacent generic translated-block mechanism is strongly disfavored and should not be the primary route.
- **Invalid stronger conclusion:** this does not prove that every algebraically coordinated block, global redesign, finite-field tower, or probabilistic whole-prefix construction is impossible.
- **Reproducibility:** pending recovery of the missing code and raw JSON.

## E4. Exact Eulerian zero mode

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Family:** `A={0,1,N}` at modulus `N`.
- **Short edges:** `0->1` of length `1` and `1->0` of length `N-1`.
- **Result:** `delta_N=0` and `Var E_N=0`.
- **Verified instance in certificate:** `N=37`.
- **Reproduction:** `cd endpoint_variance && python certificate.py`.
- **Refutes:** any unconditional claim that every nontrivial Sidon set has positive offset-energy variance at every modulus.

## E5. Homometric Sidon rulers separated by endpoint variance

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Rulers:**

  `A={0,1,4,10,12,17}`  
  `A'={0,1,8,11,13,17}`

- **Common positive-difference spectrum:** `{1,2,...,13,16,17}`.
- **Modulus:** `N=14`.
- **Exact variances:** `79/28` and `55/28`, difference `6/7`.
- **Reproduction:** `cd endpoint_variance && python certificate.py`.
- **Refutes:** any claim that all-offset energy variance is determined solely by the difference multiplicities `r_A(d)`.

## E6. Mandatory-level equality family is not Sidon

- **Status:** `[RIGOROUS — SELF-CONTAINED]`
- **Family:** `A={0,1,...,m-1}`, `N=m`.
- **Role:** equality in the general mandatory-level variance lower bound.
- **Observation:** for `m>=3`, differences repeat, so the family is not Sidon/Golomb.
- **Refutes:** calling the current constant “sharp for Sidon sets” without a separate Golomb-ruler optimization.

## E7. Working-directory checksum false alarm

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Event:** the original endpoint manifest was first checked from inside `endpoint_variance/`, although its paths start with `endpoint_variance/`.
- **Outcome:** 23 file-not-found failures.
- **Correction:** run from `core_workspace/`; all payload files pass except the manifest’s self-entry.
- **Logs:** `integrity/REVERIFICATION_2026-08-28.log`, `integrity/ORIGINAL_ENDPOINT_MANIFEST_CHECK_2026-08-28.log`.

## E8. Self-referential SHA-256 manifest

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Original file:** archived as `integrity/ORIGINAL_ENDPOINT_SHA256SUMS_WITH_SELF_ENTRY.txt`.
- **Defect:** includes a checksum of itself, producing one deterministic mismatch.
- **Impact:** packaging integrity issue only; theorem payload files passed.
- **Correction:** package-level manifest excludes itself.

## E9. Two-moment collapse for N above a fixed diameter

- **Status:** `[RIGOROUS — SELF-CONTAINED]`
- **Setup:** fixed prefix of diameter `D`, all `N>D`.
- **Identity:** `Var E_N=S_m/N-T_m^2/N^2`, where `S_m,T_m` depend only on the prefix gap moments.
- **Warning:** averaging over many moduli all larger than the same fixed diameter may add no new structural information beyond two moments.
- **Use:** reject unproductive “multiscale” variants that merely rescale one prefix’s same two quantities.

## E10. Genuine three-edge Sidon Eulerian zero mode

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Set and modulus:** `A={0,3,7,12}`, `N=6`.
- **Sidon check:** its positive differences are `{3,4,5,7,9,12}`.
- **Short-edge residue cycle:** `0->3->1->0`, with distinct lengths `3,4,5`.
- **Result:** every residue is covered exactly twice, so `delta_N=0` and
  `Var E_N=0`.
- **Refutes:** the claim that distinct Sidon edge lengths forbid nontrivial
  Eulerian zero modes, or that only complementary two-cycles matter.
- **Reproduction:** run `test_three_cycle_sidon_zero_mode` in
  `endpoint_variance/test_multiscale_variance.py`.

## E11. Cyclic covariance has no order-only or nested-modulus sign rule

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Set:** `A={0,1,3,7}`; pairs `p=(0,3)`, `q=(1,7)`.
- **Exact result:** `K_8(p,q)=-1/4`, while `K_16(p,q)=7/8`.
- **Additional sign audit:** nested arcs are positive and disjoint arcs are
  negative, but a partial crossing can have either sign.
- **Refutes:** positivity of all cross terms, covariance-sign preservation
  under `N|N'`, and classification from cyclic crossing type alone.

## E12. A dominant Golomb gap can suppress variance

- **Status:** `[RIGOROUS — SELF-CONTAINED]`
- **Family:** `A_G={0,1,G+1,G+3}` for `G>=3`, at `N=G+4`.
- **Sidon check:** the six differences are
  `{1,2,G,G+1,G+2,G+3}` and are distinct.
- **Exact result:**
  `Var E_N=(19G+27)/(G+4)^2 -> 0`.
- **Refutes:** a claim that one long internal gap, even at the maximal split
  level, forces large endpoint variance.

## E13. Unconditional critical-weight raw-variance budget is false

- **Status:** `[RIGOROUS — SELF-CONTAINED]` for the construction and
  `[REFUTED]` for the proposed budget.
- **Construction:** from a normalized `h`-mark Sidon ruler `A` of diameter `D`
  with `h>=2`, choose
  `M>D`, put `P_h={2^i-1:0<=i<h}`, `G=M(2^(h-1)-1)`, and
  `A^+=A union (D+2G+1+M P_h)`.
- **Collision audit:** old, new-internal, and cross differences occupy
  separated ranges; equality of two cross differences forces
  `M(P_i-P_j)=a-a'`, hence both sides vanish because `|a-a'|<=D<M`.
  Also `P_h` is Sidon: equality of two differences of powers of two first
  matches their 2-adic valuations and then their larger exponents.
- **Result:** iteration gives an infinite sparse Sidon sequence with
  `Var E_{D_m+1} >= (m/2-1)^4/25` at every doubling stage.
- **Refutes:** an unconditional
  `sum_{j<=J} m_j^-3 Var E_{D_{m_j}+1}=o(log J)` bound for all infinite Sidon
  sequences.
- **Surviving scope:** an upper budget must use the critical-density envelope
  essentially.

## E14. Homometric rulers force signed endpoint-sensitive off-diagonal terms

- **Status:** `[PROJECT-INTERNAL EXACT FINITE THEOREM]`
- **Data:** the E5 pair has the common diagonal kernel sum `65/2` at `N=14`.
- **Exact ordered off-diagonal sums:** `7` for the first ruler and `-5` for
  the second.
- **Refutes:** nonnegativity of the distinct-pair contribution and any exact
  reduction of the quartic budget to a nonnegative function of difference
  lengths alone.

## E15. Certified small Golomb-ruler variance minima

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`
- **Complete range:** `2<=m<=7`, `m-1<=D<=25`, at
  `N=D+1,D+2,D+3`.
- **Counts:** 245,505 normalized candidates, 9,013 oriented Golomb rulers,
  27,039 exact variance evaluations, and 135 `(m,D)` cases.
- **Independent oracle:** recursive positive-gap compositions plus direct
  half-open block counting; 294 comparisons and zero mismatches.
- **Least-diameter minima:** `1/4, 3/4, 12/7, 26/9, 404/81, 1161/169` for
  `m=2,...,7`.
- **Valid conclusion:** the unrestricted consecutive-set equality mechanism
  is absent in these finite least-diameter cases for `m>=3`.
- **Invalid conclusion:** no uniform Sidon asymptotic improvement follows from
  this finite range.
- **Artifact:**
  `endpoint_variance/golomb_variance_certificate_2026-08-28.json`.

## E16. A critical one-shell constant survives the positive kernel

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Construction:** start with any `m`-mark Sidon ruler `B`, `4|m`, diameter
  `R`, put `G=R+1`, and shift the first quarter by `0`, the second quarter by
  `G`, and the remaining half by `2G`.
- **Sidon audit:** differences with rank increments `0,1,2` lie in three
  disjoint integer intervals; equality inside one interval reduces to equality
  of differences of `B`.
- **Exact consequence:** the two rank-boundary gaps give
  `Var C_(D+1)/m^4 >= 1/2304`.
- **Dense instance:** an Erdős--Turán base has diameter `O(m^2)`, so the lift
  remains critical at its top scale.
- **Refutes:** a uniform pointwise `V_m/m^4=o(1)` conclusion based only on an
  isolated Sidon ruler and `N=O(m^2)`.
- **Does not refute:** bounded-depth estimates that assume actual compatibility
  with neighboring prefixes or one global critical sequence.
- **Artifact:**
  `endpoint_variance/SIDON_BLOCK_VARIANCE_AND_POSITIVE_MULTISCALE_2026-08-28.md`.

## E17. A newborn edge can erase all old scalar variance

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Minimal instance:** `A={0,1,4}`, coarse modulus `N=2`, fine modulus `4`.
- **Exact values:** `C_2=(0,1)` and `Var C_2=1/4`, while the newborn length-3
  arc complements the old length-1 arc and `C_4` is constant, so
  `Var C_4=0`.
- **General family:** `A={0,1,qN}` has
  `Var C_N=(N-1)/N^2` and `Var C_(qN)=0`.
- **Refutes:** scalar martingale normalization of canonical complete loads and
  every inequality `q^2 V_(qN)>=cV_N` with fixed `c>0`.
- **Artifact:**
  `endpoint_variance/Q_COVER_MARTINGALE_AND_BIRTH_OBSTRUCTION_2026-08-28.md`.

## E18. Newborn residual arcs are not uniformly almost orthogonal

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Construction:** use a dense Erdős--Turán ruler and retain a linear-sized
  star of newborn pairs sharing one endpoint at modulus `N=p^2`.
- **Mechanism:** the folded residual arcs are nested, with cross covariance
  bounded below by a positive constant for two linear-sized index blocks.
- **Consequence:** for the explicitly selected star subfamily
  `B_N^star`, `Var B_N^star >> p^2`, whereas the sum of its individual arc
  variances is `O(p)`.
- **Refutes:** any uniform Bessel/almost-orthogonality constant for every
  newborn subfamily derived only from uniqueness of difference lengths.
- **Caution:** this does not assert a lower bound for the complete newborn
  load, whose additional centered arcs may cancel.

## E19. Critical-shell shortcuts H1--H5 fail on four marks

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]` with exact hand-checkable
  witnesses.
- **H1--H4 witness:** `A=(0,1,4,6)`, compatible with `C=1/2`; its second
  birth shell has positive off-diagonal part `1/112` and net
  `39/1568 > 25/1568` diagonal.
- **H5 witness:** `A=(0,4,6,7)`, compatible with `C=1`; normalized level
  energy rises from `1/50` to `87/4096`.
- **Certified scope:** 9,870 four-mark candidates and 22,706,280 eight-mark
  candidates, plus seeded 16/32-mark witnesses; 8,451 independent-oracle
  checks, zero mismatches.
- **Survivor:** H6 net-shell nonnegativity had no failure in the stated finite
  ranges.  This is not an asymptotic theorem and points in the wrong direction
  for the needed upper budget.
- **Artifacts:** `endpoint_variance/critical_shell_results_2026-08-28.md` and
  `endpoint_variance/critical_shell_certificate_2026-08-28.json`.

## E20. Fixed-modulus left-prefix variance monotonicity is false

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Smallest Sidon instance:** `N=40`, prefix `(0,20)`, full ruler
  `(0,20,21,39)`.
- **Exact values:** `1/4 -> 99/400`, a decrease of `1/400`.
- **Infinite family:** `(0,ceil(N/2),ceil(N/2)+1,N-1)` is Sidon for every
  `N>=40`; the prefix variance tends to `1/4`, while the full variance is
  `(10N-4)/N^2 -> 0`.
- **Minimality:** a sharp four-mark lower bound and the general mandatory-level
  bound plus Popoviciu prove that no doubled-prefix size `A_r subset A_2r` can
  fail below `N=40`.  General non-doubling extensions can fail earlier.
- **Certified audit:** 780 two-gap, 91,390 four-gap, and 3,262,623 six-gap
  configurations, plus 61 family instances; exact formula and literal oracle
  agree in every audited four-mark case.
- **Refutes:** the proposed route from fixed-modulus prefix monotonicity to H6,
  and every positive multiplicative monotonicity constant.

## E21. Orthogonal edge coordinates have an unavoidable harmonic trace cost

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Statement:** for `P` distinct Sidon differences below `N` and every
  positive diagonal coordinate weighting,
  `U_w T_w >= P^3/(9N)`.
- **Critical consequence:** with `P=binom(m,2)` and
  `N<=Cm^2 log m`, the normalized cost is at least
  `1/(576 C log m)` per scale, totaling `Omega_C(log J)`.
- **Zero-mode audit:** the three-cycle scalar variance is zero but its vector
  square-function increment is `2`; diagonalization retains ghost energy.
- **Refutes:** all per-edge orthogonal Hilbert factorizations followed by a
  diagonal trace/Cauchy reconstruction, regardless of weight optimization.
- **Surviving scope:** structured off-diagonal block coordinates are not
  excluded.

## E22. One-step scalar gap-measure aging has no two-sided factor

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Decrease fixture:** for `A=(0,1,4,6)`,
  `Var_nu f=3/448` and `Var_nu f(U/2)=297/50176`, with ratio `99/112<1`.
- **Increase fixture:** for `A=(0,1,3,7)`,
  `Var_nu f=87/16384` and `Var_nu f(U/2)=1615/262144`, with ratio
  `1615/1392>1`.
- **No positive lower factor:** append gaps `H,H+c` to an `(r-2)`-mark
  Golomb base, with `H,c` larger than its diameter.  Letting `H` grow gives
  limiting ratio `9/(16(r-3)^2)`, then letting `r` grow gives zero.
- **No finite upper factor:** the Golomb gap family `(H,1,H+2)` has original
  variance `O(1/H)` while its aged variance tends to `1/256`.
- **No fixed diameter-power monotonicity:** for
  `(0,D-3) subset (0,D-3,D-2,D)`, every fixed scalar power has ratio tending
  to `5/8`.
- **Refutes:** replacement of the exact covariance-matrix recursion by a
  universal one-step scalar comparison.
- **Does not refute:** the rigorous two-step scalar lower theorem, nor a
  compatibility-dependent scalar estimate inside one fixed critical
  infinite sequence.
- **Artifact:**
  `endpoint_variance/GAP_MEASURE_DYNAMICS_AND_TWO_STEP_LOWER_BOUND_2026-08-28.md`.

## E23. Every purely local fixed-depth critical window can retain constant innovation

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Construction:** for dyadic `M`, choose a prime `M<=p<2M` and use the
  `M`-mark Erdős--Turán ruler `b_i=2pi+(i^2 mod p)`.
- **Fixed-window compatibility:** for every fixed `L`, the prefixes
  `M,M/2,...,M/2^L` satisfy the same `C=1` critical envelope once `M` is
  sufficiently large.
- **Exact limits:** the full normalized variance tends to `1/180`, the newest
  matrix innovation `Q_00/N_M` tends to `1/360`, and the same-modulus signed
  birth shell tends to `19/3840`.
- **Off-diagonal audit:** the born diagonal is `O(M^-2)`, so the born ordered
  off-diagonal sum has the same positive `19/3840` limit.
- **Refutes:** every uniform `o(1/j)` lemma based only on a fixed number of
  visible Sidon prefixes and their local critical compatibility.
- **Does not refute:** a condition asserting extendability into one infinite
  globally critical Sidon sequence, or an unbounded-history amortized budget.
- **Artifact:**
  `endpoint_variance/FIXED_DEPTH_ERDOS_TURAN_NO_GO_AND_INTERVAL_PACKING_2026-08-28.md`.

## E24. Logarithmically growing local critical windows retain main-order energy

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Construction:** for `M=2^J`, choose `M<=p<2M` prime and use
  `b_i=2pi+(i^2 mod p)`.  Retain the last
  `floor(log_2 J)-1` dyadic prefixes.
- **Common envelope:** every retained prefix satisfies
  `N_n<=2n^2 log n` for `J>=8`.
- **Uniform limits:** gap discrepancy is at most `4/n`, gap variance tends to
  `1/180`, adjacent `Q_00/N` tends to `1/360`, and the same-final-modulus
  birth shell tends to `19/3840`.
- **Accumulation:** the retained gap variances sum to
  `(log J)/(180 log 2)+O(1)`; the window depth tends to infinity.
- **Refutes:** every uniform upper-budget theorem based only on the last
  `floor(log_2 J)-1` prefixes, local Sidon uniqueness, and their common
  critical envelope.
- **Does not refute:** a theorem using embeddability into one infinite
  globally critical sequence or history older than this `Theta(log J)`
  scale-index window.
- **Artifact:**
  `endpoint_variance/GROWING_DEPTH_ERDOS_TURAN_NO_GO_2026-08-28.md`.

## E25. Cross-band occupancy cannot directly pay covariance innovation

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Data:** in the E24 window, the `n^2` old--new differences of a transition
  lie in a band of length `W_n>=2pn`.
- **Exact consequence:** over all retained transitions,
  `sum n^2/W_n<1/2`, whereas
  `sum Q_00/N=L_J/360+o(1)` tends to infinity.
- **Refutes:** for fixed `A,B`, every direct inequality
  `sum Q_00/N <= A+B sum(|old-new spectrum|/|containing band|)`, as well as a
  pointwise vanishing version at the back of the growing window.
- **Does not refute:** a charge comparing cross differences between multiple
  separated epochs of one global history.
- **Artifact:**
  `endpoint_variance/CROSS_BLOCK_DIAMETER_PROFILE_PACKING_2026-08-28.md`.

## E26. Quadratic diameter and profile moments alone allow positive innovation

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Profile:** `a_k=k^2`; its limiting gap density is `2u` and
  `N_m/N_(2m)->1/4`.
- **Limit:** with `z=(u(1-u),u)`, the innovation tends to
  `((19/3840,-1/80),(-1/80,5/96))`, whose determinant is
  `187/1843200>0`.
- **Refutes:** any covariance-moment-only argument that omits integer Sidon
  uniqueness.
- **Scope:** the squares are not Sidon:
  `5^2-1^2=7^2-5^2=24`.  This is a control obstruction, not a #1191
  counterexample.

## E27. Four compatible critical transitions need not show decay

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Scope:** two 32-mark Golomb rulers satisfy the same `C=1` envelope at all
  31 prefixes from 2 through 32 marks, and each has all 496 positive
  differences distinct.
- **Gap witness:**
  `min_(m=4,8,16,32) G_m=103963/23658496>0.0043943`.
- **Innovation witness:**
  `min_(m=4,8,16,32) Q_(m/2,00)/N_m`
  `=743151/192790528>0.0038547`.
- **Completeness boundary:** the 4-mark root search is complete over 12,341
  normalized candidates; the 8/16/32 extensions are deterministic beam
  witnesses and are not claimed optimal.
- **Refutes:** dyadic monotone decay and any four-transition lemma forcing a
  smaller universal threshold under only Golomb uniqueness plus the common
  envelope.
- **Does not refute:** any asymptotic budget or infinite-history theorem.
- **Artifacts:** `endpoint_variance/wave4_nested_results_2026-08-28.md` and
  its dated JSON certificate.

## E28. Scalar diameter-profile discrepancy does not control variance or innovation

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Vanishing-variance family:** for `H>=2`,
  `A_H=(0,H,H+1,2H+3)` is Sidon and has
  `epsilon_4=d_K(nu_4,lambda)=1/4`, but
  `Var_nu f=(5H+9)/(256(H+2)^2)->0`.
- **Different-innovation pair:** `(0,1,3,7)` and `(0,1,5,7)` are homometric
  Sidon rulers with the same two-mark old prefix, final modulus 8, diameter
  ratio `1/4`, and discrepancy `1/4`.  Their normalized innovations are
  `((51/16384,37/4096),(37/4096,67/1024))` and
  `((67/16384,37/4096),(37/4096,51/1024))`, respectively.
- **Refutes:** any universal variance lower bound from a positive scalar
  discrepancy and any claim that scalar reset size plus the diameter ratio
  determines `Q`.
- **Surviving scope:** a global theorem may track reset location, sign,
  persistence, and cross-epoch Sidon differences.
- **Artifact:**
  `endpoint_variance/CROSS_BLOCK_DIAMETER_PROFILE_PACKING_2026-08-28.md`.

## E29. Sparse profile resets do not amortize innovations without Sidon arithmetic

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Construction:** at dyadic size `n_j=2^j`, set
  `N_j=4^j k_j`, where `k_j` halves until one and then resets to the largest
  power of two at most `j`; fill every newborn half with equal positive
  integer gaps.
- **Bounds:** the dyadic `C=1` envelope, the all-prefix bound
  `N_n<12n^2 log n`, scalar Sidon capacity, and the exact covariance recursion
  all hold.  Endpoint reset count and total reset magnitude are `o(J)`.
- **Innovation:** every transition has the exact lower bound
  `Q_00/N>=1/2048`, so the innovation sum is `Omega(J)`.
- **Why it is not a #1191 counterexample:** the four-mark gaps are
  `(1,3,14,14)`, and positive difference 14 occurs twice.  Later uniform
  shells have many repeated contiguous sums.
- **Refutes:** every reset-amortization theorem using only profiles, scalar
  diameter capacity, reset count/magnitude, critical growth, or abstract PSD
  dynamics.
- **Surviving scope:** a theorem using uniqueness of all cross-epoch
  contiguous sums in one genuine Sidon sequence.
- **Artifact:**
  `endpoint_variance/CROSS_EPOCH_RESET_AMORTIZATION_2026-08-28.md`.

## E30. Five-transition finite Sidon witnesses retain innovation and reset persistence

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Data:** authenticated 32-mark Wave 4 roots extend to six 64-mark Golomb
  rulers under the same `C=1` envelope at every prefix.  Each has 2,016
  distinct positive differences and 63 verified prefix rows.
- **Innovation witness:**
  `min_(m=4,8,16,32,64) Q_(m/2,00)/N_m`
  `=100987452359053759/26579439869661020160>0.0037994`, with latest signed
  reset persistence above `0.6587`.
- **Persistence witness:** latest signed persistence exceeds `0.7113`, while
  its final innovation exceeds `0.0025070`.
- **Completeness boundary:** the 32-to-64 extension uses deterministic beam
  search.  No 64-mark optimum, 128-mark extension, infinite extension, or
  asymptotic lower bound is claimed.
- **Refutes:** any five-transition theorem forcing innovation below the
  displayed threshold or near-total reset decorrelation under only the finite
  Golomb and common-envelope hypotheses.
- **Does not refute:** an unbounded-history arithmetic amortization.
- **Artifacts:** `endpoint_variance/wave5_nested_results_2026-08-28.md` and
  its dated JSON certificate.
- **Historical scope correction:** Wave 6 later produced one separate
  128-mark finite continuation; this does not alter what the Wave 5
  certificate itself proves.

## E31. The exact multi-epoch band ledger is logarithmic at the endpoint

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Theorem:** for
  `tau_(m,k)=D_m^-+D_m^++k max(mu_m^-,mu_m^+)`, distinct cross-boundary
  anti-diagonal differences give
  `sum_(tau<=X) k/tau<=1+log X`; at exponent `1+epsilon` the total is at most
  `(1+epsilon)/epsilon`.
- **Hard limit:** epsilon zero is exactly logarithmic.  The lower innovation
  ledger is also logarithmic, so capacity plus layer-cake integration alone
  does not yield the required `o(log J)` contradiction.
- **Surviving scope:** an old-history theorem may prevent the useful cutoff
  from renewing into fresh numerical bands.
- **Artifact:**
  `endpoint_variance/wave6_collision_reset_renewal_2026-08-28.md`.

## E32. Three strongly negative reset cycles need not collide

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Ruler:**
  `(0,1,18,34,79,127,171,218,319,415,509,613,710,808,903,1002)`.
- **Audit:** all 120 positive differences are distinct and all 15 nontrivial
  prefixes satisfy C=1.  Its three newborn shells have normalized
  discrepancies `1/66,1/184,3/784`, all signed resets are at most `-1/4`,
  and every normalized innovation is greater than `1/600`.
- **Refutes:** collision after only three reset-to-nearly-uniform cycles.
- **Does not refute:** an unbounded-history collision or amortization theorem.

## E33. Empirical adjacent-epoch Hall decay fails three times in one ruler

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Candidate refuted:** `Lambda_NN(n,2n)<=1/(4 sqrt(n))`, equivalently
  `16n Lambda_NN^2<=1`.
- **Exact transitions:** the E32 prefix extends to one 64-mark C=1 Golomb
  ruler with
  `Lambda=9/14,17/28,45/118` at `n=8,16,32`, hence scaled values
  `2592/49,4624/49,259200/3481`.
- **Audit:** all 2,016 differences and all 63 prefix envelopes pass; the
  sorted-difference SHA-256 is
  `fd3e33ac286ab6748fdf133a6562ec4f6573723cbac4047ef26b432fee27a836`.
- **Boundary:** the integer endpoint scan is complete for these fixed marks,
  but the two discovery beams were not exhaustive.  No asymptotic Hall lower
  bound or infinite extension is claimed.
- **Artifacts:** `endpoint_variance/wave6_hall_candidate_probe_results_2026-08-28.md`
  and its dated JSON certificate.

## E34. Local one-point forbidden-shadow density is not universal

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Construction:** for a normalized Golomb ruler `B` and `L>=3`,
  `A_L(B)={0,1,Lb_1,...}` is Golomb and
  `Delta^+(A_L(B))={1} dotcup L Delta^+(B) dotcup {Lb_j-1}`.
- **Shadow bound:** `A_L(B)+Delta^+(A_L(B))` occupies at most the four residue
  classes `-1,0,1,2 (mod L)`, so any interval of `H` consecutive integers
  contains at most `4 ceil(H/L)` shadow points.
- **Growing-window no-go:** compatible finite windows can have total actual
  extension-band shadow density `o(1)` while normalized innovation tends to
  `1/360` per transition and its sum diverges.
- **Refutes:** every universal fixed-constant charge of innovation by local
  one-point shadow density.
- **Boundary:** the finite ruler family changes with terminal scale; it is not
  one infinite counterexample to #1191.
- **Artifact:**
  `endpoint_variance/FORBIDDEN_SHADOW_RESIDUE_NO_GO_2026-08-28.md`.

## E35. A finite critical witness extends to 128 marks

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Audit:** 128 increasing marks, final mark 136,282, all 8,128 positive
  differences distinct, and every prefix from 2 through 128 satisfies
  `N_n<=floor(2n^2 log n)`.
- **Dynamics:** its minimum recorded normalized innovation is the exact
  positive fraction
  `2044607601929603/815542875732049920`; the new 64-to-128 signed persistence
  is `245589681743053/402372206022787`.
- **Refutes:** any six-transition finite lemma forcing collision, zero
  innovation, or loss of the common C=1 envelope.
- **Boundary:** the seeded beam was non-exhaustive.  This is not an optimum,
  an infinite extension, or an asymptotic construction.
- **Artifacts:** `endpoint_variance/wave6_arithmetic_mining_results_2026-08-28.md`
  and its dated JSON certificate.

## E36. Complete-birth `W_2` cannot affinely dominate recent innovation

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Exact step:** the 512-mark `p=1423` E–T ruler has
  `Q_(256),00/N_512>W_2(256)`; comparison cross-product
  `86781803501905775924014152122871` is positive.
- **Growing window:** over `R=floor((1/2)log_2 log M)` recent transitions,
  adjoint innovation is at least `R/360+o(R)` while total `W_2=o(1)`.
- **Refutes:** every fixed-nonnegative-constant affine domination of the
  displayed innovation sum by `W_2` alone on all finite critical windows.
- **Does not refute:** a term conditioned on infinite survival of the same
  prefix; the terminal ruler and prime change with `M`.
- **Artifact:**
  `endpoint_variance/WAVE7_GLOBAL_BAND_RENEWAL_POTENTIAL_2026-08-28.md`.

## E37. Local renewal holes RH are false

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Witnesses:** values 21 and 22 from epochs 8 and 4 fill `[21,22]`, giving
  RH margin `-1`; a second failure uses 382 and 383 from epochs 8 and 16.
- **Refutes:** demanding one unused integer hole for each additional epoch in
  a local occupied interval.
- **Artifact:** `endpoint_variance/wave7_band_renewal_probe_results_2026-08-28.md`.

## E38. Direct harmonic epoch tax HT is false

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Witness:** at threshold 3, activations 1 and 3 give
  `H_2=3/2`, reciprocal sum `4/3`, proposed tax `1/3`, and margin `-1/6`.
- **Refutes:** paying renewal count directly from the harmonic slack.

## E39. Adjacent cheap halves do not repay the EST tax

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Threshold:** `T=1198199/32`, with seven active epochs.
- **Ledger:** EST tax 120; largest distinct cheap-adjacent union 63; nested
  overlap 57; boundary overlap 6; genuinely new charge 57; unpaid debt 63.
- **Refutes:** proving EST or the innovation budget by matching cheap adjacent
  halves alone.
- **Does not refute:** repayment by unused non-adjacent differences or global
  extension-capacity slack. EST itself remains proved through eight marks
  and is only tested thereafter on the stated finite 64/128-mark fixtures and
  23 accepted one-gap-swap variants.

## E40. Worst-guarantee O'Bryant gluing misses the critical first prefix

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Ledger:** one scalar-guaranteed survivor after an `n`-mark old ruler needs
  at least `binom(n,2)+1` candidate marks, a window `Omega(n^4)`, and a first
  new modulus of the same order.
- **Consequence:** every fixed critical envelope eventually fails; for the
  package `C=1` envelope, all `n>=8` fail analytically.
- **Sharp scope:** sparse separated candidates can force all `binom(n,2)`
  deletions.
- **Does not refute:** structured candidates with fewer actual conflicts or a
  gluing theorem that controls mixed differences without the large gap.
- **Artifact:** `endpoint_variance/WAVE7_GLUE_DELETE_NO_GO_2026-08-28.md`.

## E41. Local global-density payment is false inside the `C=1` class

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Witness:** `(0,1,4,6)` at `m=2`, with `T=3`, `U_global=0`, and exact
  innovation `137/10976`.
- **Scope:** all 1,672 four-mark all-prefix-`C=1` Golomb rulers and 3,344
  activation events were exhausted; 601 events violate
  `U_global(T)/T>=I_m`.
- **Finite survival:** the witness has level counts `(1,67,4879)` through
  depth two.  This is not infinite survival.
- **Refutes:** the literal per-epoch factor-one bridge, including its
  uncorrected square-reservoir version.
- **Does not refute:** an eventual cumulative theorem with a finite initial
  error on one infinite branch.
- **Artifact:** `endpoint_variance/WAVE8_DENSITY_CANDIDATE_2026-08-28.md`.

## E42. Latest-shell density misses an old atom

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Witness:** `(0,4,5,7,78,86,166,199)` at `m=4`.
- **Values:** `T=72`, `delta_4=80`, old ancestry cleared, current family
  unpaid, `U_latest=0`, and `I_4=5539453/1075200000`.
- **Finite survival:** level counts `(1,121,16030)` through depth two.
- **Refutes:** paying a genuine outstanding family or its innovation solely
  from unused differences born in the latest shell.
- **Boundary:** the global reservoir has one atom and a positive local margin;
  no infinite conclusion follows.

## E43. Adjacent assets and the full span do not repay the shell fan

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Witness:** `(0,8,24,56,58,314,318,319)`, whose gaps are distinct powers
  of two and hence give 28 distinct consecutive sums.
- **Exact deficit:** deleting the sole positive non-adjacent bulk interval
  leaves boundary debt `1869979/6720` larger than the full-span corner plus
  every positive adjacent atom.
- **Repair:** restoring the non-adjacent bulk atom leaves surplus
  `41407/2240` and exact shell energy `41407/1178240`.
- **Refutes:** any boundary-fan proof using only adjacent renewal and the
  shell diameter.

## E44. Newborn covariance cannot uniformly dominate the rank-one term

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Family:** `(0,D,3D,3D+1)` for every integer `D>=2`.
- **Exact asymptotic:**
  `D^(-1)<H,R_2>/<H,S_2> -> 46/45`.
- **Refutes:** every unconditional constant comparison of rank-one mixture
  energy with newborn-shell covariance.
- **Does not refute:** a global critical-history budget which pays the two
  terms by different atoms.

## E45. Old-pair cancellation cannot provide a little-o gain

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Theorem:** after a pair is born, its positive term minus all later old-pair
  subtractions retains between one half and one times its raw constant-`H`
  birth charge.  If every future modulus ratio is at most `r`, the lower
  factor is `1/(1+r)`.
- **Global consequence:**
  `B_H(J)/2 <= sum_(j<=J)<H,Q_j/N_(2m_j)> <= B_H(J)`.
- **Refutes:** using the negative part of the signed `Q_m` identity as an
  unbounded cancellation mechanism.  Exact finite-horizon adjoints instead
  recover a positive future `E`-energy tail.
- **Artifact:** `endpoint_variance/WAVE8_PAIR_TELESCOPE_2026-08-28.md`.

## E46. A fixed finite Hegyvári-block menu can be blocked

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Rigid differences:** every affine/rotated full `(p,u)` block contains
  `2p+u` and `p(2p+u)`.
- **Embedding lemma:** any finite list of prescribed positive distances can
  be embedded in a finite Golomb ruler.  Hence an old ruler can contain the
  universal span of every block in a finite menu, making every separated
  splice impossible.
- **Explicit case:** for `p=5`, `u=0,1,2,3`, the Golomb ruler
  `(0,50,106,161,323,383,767,832)` contains all four universal spans.
- **Refutes:** iterating a fixed finite list of affine Hegyvári blocks by
  translation alone.
- **Does not refute:** an adaptive survival-conditioned family with a proved
  depth-independent spectrum-intersection bound.

## E47. Pointwise and literal harmonic birth decay fail

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Scope:** all 1,468 normalized eight-mark Golomb rulers with terminal at
  most 40; 1,146 obey every all-prefix-`C=1` cap.
- **Monotonicity:** 128 rulers have `Delta B_4>Delta B_2`.  The minimum-
  diameter witness is `(0,4,12,13,19,30,33,35)` with exact margin
  `446533/341397504`.
- **Harmonic schedule:** every one of the 1,146 rulers violates the literal
  inequality `2 Delta B_4<=Delta B_2`.
- **Does not refute:** eventual Cesaro decay conditioned on one infinite
  critical branch.
- **Artifact:** `endpoint_variance/WAVE9_BIRTH_BUDGET_PROBE_2026-08-29.md`.

## E48. Static rank/magnitude cells have large overlap

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Minimum witness:** `(0,1,4,6)` has three genuine atoms in the cell with
  rank band `[2,4)` and absolute magnitude band `[4,8)`.  It refutes both
  one-atom-per-cell and occupancy-at-most-rank-band-lower.
- **Long calibration:** the required overlap ratio reaches `553/4` on the
  modified-greedy all-prefix-`C=1` 512 prefix and `647/2` on the 512-mark
  Erdős--Turán ruler.
- **Surviving fact:** a genuine absolute magnitude band `[M,2M)` contains at
  most `M` atoms because its interval differences are distinct integers.
  That fact has no history-vanishing factor.
- **Artifact:** the Wave 9 birth-budget probe and certificate.

## E49. Macroscopic core mass need not decay on long finite rulers

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Core quadrant:** genuine births with span greater than `N/2` and dyadic
  rank-lag band lower at least `m/2`.
- **Modified-greedy 512:** terminal share
  `13242199924089976348090/20619808566184045294713>3/5`; every prefix cap is
  `C=1` through the audited 512 marks.
- **Erdős--Turán 512:** terminal share
  `2738923201748154301783/4115217089595122117052>3/5`.
- **Does not refute:** a survival-conditioned average theorem; neither fixture
  is certified as one infinite critical branch.

## E50. Local numerical sparsity does not control birth or retained cross ratio

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Family:** scaled Erdős--Turán rulers with `L` marks and
  `s_L=ceil(log L)` have a fixed recent-prefix critical constant while
  `|Delta|/N_L->0`.
- **Positive costs:** terminal `B_(L/2)>=1/2352` and retained genuine
  cross-ratio potential `X_(L/2)>=1/4096`.
- **Refutes:** every local bound forcing either cost to zero solely from
  numerical difference occupancy, even after the exact `(D/N)^2` factor is
  retained.
- **Boundary:** the ruler and dilation change with `L`.  The family is not a
  compatible infinite branch.
- **Artifacts:**
  `endpoint_variance/WAVE9_BIRTH_BUDGET_CARLESON_ANALYSIS_2026-08-29.md`
  and `endpoint_variance/WAVE9_WEIGHTED_CROSS_RATIO_2026-08-29.md`.

## E51. Raw W9-RLP slack does not damp the retained objective

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Family:** `A_s=(0,s,4s,6s)` for `s=1,2,3,4`; every member is Golomb and
  satisfies all available `C=1` prefix caps.
- **RLP behavior:** the minimum all-subset/all-cutoff W9-RLP slack is exactly
  `s`.
- **Objective behavior:** the retained scalar charge
  `s^2/(2(6s+1)^2)` and fixed-`H` charge
  `2s^2/(35(6s+1)^2)` both increase strictly with `s`.
- **Refutes:** using unnormalized raw RLP slack as a free-standing damping
  penalty for the primitive or rank-variance objective.
- **Does not refute:** a normalized deficit coupled in the same inequality to
  endpoint products and infinite survival.
- **Artifact:** `endpoint_variance/WAVE10_LAMINAR_LP_PROBE_2026-08-29.md`.

## E52. Existing W9-RLP rows are zero columns in the fixed-modulus tile LP

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Observation:** after a finite ruler and all `N_(2m)` are fixed, each
  W9-RLP row contains only constants `m,q_m,N_(2m)` and no occupancy variable
  `x_(m,t)`.
- **Consequence:** adjoining every epoch-subset/cutoff RLP row leaves the
  current tile feasible set, primal optimum, and dual optimum unchanged.
- **Finite audit:** 9,845,549 cutoff vectors through 128 marks, zero
  violations; exact primal equals exact threshold dual in every tested tile
  block.
- **Refutes:** the literal strategy “put the existing W9-RLP and tile rows in
  one LP” without deriving a new mixed row.
- **Does not refute:** weighted RLP inequalities whose coefficients themselves
  depend on endpoint products, Abel atoms, or a survival-conditioned state.

## E53. Plain global Abel-spectrum rearrangement misses a leading quarter

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Theorem:** after all negative non-full Abel bulk coefficients over an
  arbitrary finite dyadic epoch set are globally sorted,
  `F_E=(7/4)sum_(m in E)log m+O(|E|)`.
- **Critical consequence:** the corresponding displayed upper certificate
  retains `(1/4)sum log m` plus secondary `log log` slack.  For consecutive
  dyadic epochs through `2^J` its leading term is `(log 2/8)J^2`.
- **Refutes:** closing P15 using only the exposed Abel signs, the coefficient
  multiset, and global distinct-positive-integer rearrangement, even when all
  epochs are sorted simultaneously.
- **Does not refute:** extra interval-sum algebra, numerical-hole exclusion,
  lower-shell/future coupling, or a tensor-tree embedding conditioned on one
  infinite critical branch.
- **Artifacts:**
  `endpoint_variance/WAVE10_LAMINAR_WEIGHTED_TRIANGLE_ANALYSIS_2026-08-29.md`
  and `endpoint_variance/WAVE10_HEREDITARY_LOG_PRODUCT_PACKING_2026-08-29.md`.

## E54. Same-pair future-tail charging has logarithmic dyadic overlap

- **Status:** `[REFUTED]` for the stated uniform birth-charge mechanism.
- **Exact identity:** the Wave 11 lower residual at epoch `m` is
  `sum_(i<m-1)((m-i)/(2m))^2 sum_(j>=m) C_(ij)` on an infinite ruler.
- **Obstruction:** after summing dyadic `m`, the coefficient with which a
  fixed pair `(i,j)` reappears is `Theta(log(j/i))` when `j/i` is large.
- **Refutes:** a term-by-term estimate assigning every future-tail occurrence
  to the pair's unique birth atom with a universal overlap constant.
- **Does not refute:** a collective cross-length telescope or a
  survival-conditioned inequality allowing logarithmic weights to be repaid
  by other positive channels.
- **Artifact:**
  `endpoint_variance/WAVE11_SURVIVAL_ABEL_REPAYMENT_ANALYSIS_2026-08-29.md`.

## E55. The triangular floor does not force local residual decay

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]` for the explicit audited
  window.  On changing scaled Erdős--Turán rulers for
  `m=16,...,1024`, `Y_m/(T_m-K_m^mix)` stays between about `0.12118` and
  `0.12689`; the new length floor can remain sharp up to constant-order
  residual at an epoch.
- **Asymptotic scope:** `[RIGOROUS — MODULO NAMED THEOREM]`.  Combining the
  Wave 9 positive lower bound for the changing Erdős--Turán family with the
  Wave 11 interval comparison refutes deducing pointwise `Y_m=o(1)` solely
  from the triangular interval bound and changing finite critical windows.
- **Does not refute:** decay after averaging on one fixed infinite
  eventually-critical branch.  The rulers change with `m`.
- **Artifact:** `endpoint_variance/wave11_abel_repayment_certificate_2026-08-29.json`.

## E56. Within-length shifted-factorial refinements are summably too small

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Theorem:** for one length class, the improvement beyond
  `D>=binom(ell+1,2)` obtained by sorting its `O(m)` distinct values is only
  `O(m^(-1/2))` per shell.  The short-length part follows from
  `(1/m)sum log(1+m/ell^2)` and the long-length part from `sum ell^(-2)`.
- **Consequence:** over dyadic epochs this gain is `O(1)` and cannot cancel
  the secondary `O(log log m)` profile.  The best checked 2025 finite-diameter
  theorem has `log diam>=2log m-O(m^(-1/2))`; only its subleading correction
  has that order, and it supplies no interval-length/survival coupling.
- **Refutes:** closing P17 by another independent sorting inside fixed length
  classes or by a global diameter improvement alone.
- **Does not refute:** cross-length allocation, exact future-tail telescoping,
  or survival-conditioned product-box control.
- **Artifact:**
  `research_sources/WAVE11_SURVIVAL_ABEL_LITERATURE_DELTA_2026-08-29.md`.

## E57. Literal Abel-repayment candidates fail in the complete bounded C=1 scope

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]`.
- **Exact scope:** all 1,146 normalized eight-mark Golomb rulers with terminal
  mark at most 40 satisfying every `C=1` prefix cap; signs are checked after
  clearing rational exponents and comparing integers.
- **Result:** bulk-only `P>=U`, boundary-only `S>=U`, all-hole-only
  `H^num>=U` (the raw probe calls this `H>=U`),
  lower-hole-quarter, and literal zero-residual `P+S>=U` fail in all 1,146
  cases.  The minimum-terminal then lexicographic witness is
  `(0,1,4,9,15,22,32,34)`.
- **Survivor:** the tested normalized-harmonic inequality has zero bounded
  failures and minimum numerical margin about `0.210336`; this is not an
  infinite theorem and by itself does not yield `o(log J)`.
- **Refutes:** those five literal finite-shadow inequalities without a new
  survival or cross-length hypothesis.
- **Does not refute:** P17 on one fixed infinite eventually-critical branch.
- **Artifact:**
  `endpoint_variance/wave11_abel_repayment_certificate_2026-08-29.json`.

## E58. Full rank-length-containment floors gain only a constant per epoch

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Setup:** combine the global numerical rank of every Wave 11 bulk
  difference, the triangular length floor
  `D>=binom(ell+1,2)`, and the complete partial order induced by proper
  interval containment.  Minimize the resulting weighted log floor over all
  linear extensions.
- **Theorem:**
  `0<=K_J^inc-K_J^len<5|E_J|`.  The witness orders right-endpoint bands by
  epoch and atoms within a band by nondecreasing length; the exact cumulative
  atom count is `2m^2-5m+2<2m^2`.
- **Refutes:** closing the secondary P17 repayment using only these three
  independent order/floor inputs, even after optimizing their joint rank
  assignment.
- **Does not refute:** crossing-interval additive relations, integer
  unit-spacing packing between different sums, or survival-conditioned
  coupling.
- **Artifact:**
  `endpoint_variance/WAVE12_SIGNED_OFFDIAGONAL_SURVIVAL_ANALYSIS_2026-08-29.md`.

## E59. A quadratic real Golomb ruler has nondecaying Wave 11 birth energy

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Model:** `a_n=n^2+sqrt(2)n`, for `n>=0`.
- **Uniqueness:** equality of two positive differences separately equates
  their rational and irrational parts, forcing equal index gap and index sum,
  hence the same pair.
- **Exact asymptotic:** with `r=j-i` and `s=i+j-1+sqrt(2)`,
  `C_(i,j)=log((1-s^(-2))/(1-r^(-2)))`, and dominated Riemann convergence
  gives
  `Y_m -> (3/2)(log 2-1/2)=0.28972077083991793...`.
- **Refutes:** every proposed P17 argument that uses only abstract difference
  uniqueness, order, quadratic growth, and the cross-ratio formula and hence
  remains valid over the reals.
- **Does not refute:** Erdős #1191.  The marks are not integers.  The example
  instead proves that integer unit spacing or an equivalent arithmetic input
  is essential.
- **Finite calibration:** the Wave 12 certificate records
  `Y_1024=0.2893858160837208`; this floating value is not used for any exact
  sign or identity decision.
- **Artifacts:**
  `endpoint_variance/WAVE12_SIGNED_OFFDIAGONAL_SURVIVAL_ANALYSIS_2026-08-29.md`
  and `endpoint_variance/wave12_cut_renewal_certificate_2026-08-29.json`.

## E60. Integer new-birth mass rules out little-oh on an existing critical branch

- **Status:** `[RIGOROUS — SELF-CONTAINED]`.
- **Finite theorem:** for every dyadic `m>=4`, set
  `H_m=a_(2m-1)-a_(m-2)` and
  `E_m=m(m-2)(m^2+8m+6)/48>=m^4/48`.  Then
  `Y_m,Z_m>=Z_m^nb>=E_m/(8m^2H_m)>=m^2/(384H_m)`.
- **Mechanism:** the suffix contains exactly `m+1` distinct positive integer
  gaps.  Layering their distance from each fixed gap and using
  `C_(i,j)>=h_i h_j/D_(i,j)^2` gives the displayed constant.
- **Conditional consequence:** any fixed infinite branch with
  `a_n<=C n^2 log(2n)` eventually would satisfy
  `Y_m,Z_m>1/(1536C log(4m))` eventually and therefore
  `liminf sum Y/log J, liminf sum Z/log J >=1/(1536C log2)`.
- **Refutes:** interpreting P17 or P18 little-oh as an ordinary decay property
  compatible with an existing critical branch.  The terminal tail cannot be
  discarded from the faithful signed identity
  `sum Z-R_(2^(J+1))=o(log J)`.
- **Logical boundary:** this does not construct a critical branch and does not
  unconditionally disprove the universal P17/P18 assertions.  Quantified over
  every `C>0`, each assertion is equivalent to Question 1 and is vacuous if
  Question 1 is true.  Question 1 remains unresolved.
- **Frontier consequence:** the exact spectrum
  `Z=mathfrak P+mathfrak U-mathfrak B-mathfrak F-mathfrak e` gives
  `0<=Z<=X+epsilon`, while the theorem forces
  `sum X >=(1536C log2)^(-1)log J-O_(C,a)(1)`.  Thus a purely within-epoch
  positive frontier sparsification cannot be the missing upper bound.
- **Artifacts:**
  `endpoint_variance/WAVE13_P18_HARMONIC_OBSTRUCTION_2026-08-29.md`,
  `endpoint_variance/WAVE13_FRONTIER_SPECTRUM_AND_SIGNED_REPAYMENT_2026-08-29.md`,
  and
  `endpoint_variance/wave13_p18_harmonic_obstruction_certificate_2026-08-29.json`.

## E61. Literal lattice-occupancy and central-rank charges fail

- **Status:** `[RIGOROUS IDENTITY + CERTIFIED FINITE COUNTEREXAMPLES]`.
- **Exact lattice identity:** with `M=D_(i+1,j-1)`,
  `C_(i,j)=sum_(s<h_i,t<h_j)kappa_(M+s+t)` and
  `kappa_n=log((n+1)^2/(n(n+2)))>0`.
- **Occupancy counterexample:** the induced literal bound `M_n<=1` already
  fails on the eight-mark ruler `(0,3,14,22,23,27,29,39)`, where the maximum
  weighted occupancy is `63/16`.  The authenticated Hall-64 and
  Erdős--Turán-128 fixtures have maxima `6679145/4096` and `77742955/8192`.
- **Central path theorem:** for each fixed rank distance, central differences
  form a disjoint path and every difference vertex has degree at most two.
  This bounded incidence is valid but insufficient by itself.
- **Central-hole witness:** `(0,1,4,9,15,22,32,34)` has a Wave 12 birth cell
  with central values `32,33`, so no unused integer or difference rank lies
  strictly between them.
- **Pointwise-rank witness:** on `(0,1,7,10,22,24,35,40)`, the cell `(4,6)`
  has consecutive central ranks but
  `C_(4,6)/|log(14/13)|=17.4338...`; the Hall-64 fixture reaches
  `226.4785...`.  Hence `C_(i,j)<=|log(B/C)|` is false.
- **Refutes:** bare cell-occupancy-one, central-hole, and unweighted
  adjacent-rank pointwise payments.
- **Does not refute:** a charge retaining outer/inner curvature or a
  survival-conditioned aggregate multiplicity theorem.  The actual-rank
  envelope table is a finite diagnostic, not an asymptotic no-go.
- **Artifact:**
  `endpoint_variance/WAVE13_LATTICE_CELL_AND_CENTRAL_RANK_NO_GO_2026-08-29.md`.
