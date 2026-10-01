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

## E62. Promotion is not automatically a signed frontier repayment

- **Status:** `[RIGOROUS SIGN/ALLOCATION BOUNDARY]`.
- **Positive theorem:** under an eventual critical cap, the Wave 14 suffix
  ranks acquire a harmonic promotion.  The exact next-lower-shell copy with
  coefficient `v_(m,p)` gives a legal addition to the Wave 11 length or mixed
  floor.
- **Obstruction:** the Wave 13 positive coefficient is larger:
  `u_(m,p)-v_(m,p)=(4m-2p-3)/(8m^2)` on the macroscopic subfan, with total
  mass tending to `3/8`.  The next-shell copy is omitted from the Gothic
  same-epoch bulk `mathfrak B_m`.
- **Refutes:** subtracting the full `u`-weighted future promotion from the
  frontier merely because the ranks increase.  In
  `log d=log rho_infinity+log(d/rho_infinity)`, promotion transfers mass
  between two nonnegative positive channels; it does not by itself create a
  negative term.
- **Does not refute:** the legally proved `v`-weighted next-shell rebate or a
  future disjoint allocation of the residual `u-v` channel.
- **Artifacts:**
  `endpoint_variance/WAVE14_FUTURE_RANK_PROMOTION_2026-08-29.md` and
  `endpoint_variance/WAVE14_PROMOTION_REBATE_AND_ALLOCATION_BOUNDARY_2026-08-29.md`.

## E63. Raw-log failure and the historical isolated-fan horizon estimate

- **Status:** `[RIGOROUS BOUNDARY + CERTIFIED FINITE COUNTERCHECKS]`.
- **Valid local theorem:** the marginal rank increment
  `Delta_m=sum u_(m,p)log(1+K_p/r_p)` has bounded nested reuse and fits into
  the full literal next bulk up to a dyadically summable `O(m^-2)` error.
- **Raw-log failure:** the same atomwise proof cannot pay
  `u_(m,p)log d_(m,p)`, because witnesses have `x<=d` and hence the wrong
  direction `log x<=log d`.  Equal-share finite allocation leaves unpaid
  mass `2.65023` on Hall 64 at `m=16` and `1.60917` on Erdős--Turán 128 at
  `m=32`.
- **Floor-overlap warning:** the local theorem spends each selected
  `beta(x)log x` in full.  It is not a premium which may be added to an
  existing rank or length floor.
- **Historical horizon estimate:** isolating `mathfrak U_(2^J)` after a
  one-step shift leaves a `Theta(J)` positive fan.  Wave 16 proves that this
  is not the correct terminal signed object: `R_(2m)`, `mathfrak F_m`, and
  `mathfrak e_m` absorb it into a nonnegative potential.  The isolated-fan
  estimate must no longer be cited as an independent no-go.  The separate
  `4^k` coefficient mismatch for much later births remains valid.
- **Does not refute:** the Wave 16 terminal potential, a disjoint
  floor-plus-Delta inequality, or an all-epoch birth-time theorem using
  additional arithmetic structure.
- **Artifact:**
  `endpoint_variance/WAVE15_LOCAL_PROMOTION_ALLOCATION_AND_HORIZON_OBSTRUCTION_2026-08-29.md`.

## E64. Terminal taper alone did not solve the historical bulk-capacity overlap

- **Status:** `[RIGOROUS CLAIM BOUNDARY]`.
- **Positive correction:** exact summation by parts gives
  `Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m` with
  `mathcal T_m>=0`; the terminal upper is `O_C(log J)` at `m=2^J`.
  Fejer weights suppress the raw terminal fan and preserve the harmonic
  lower signal.
- **Historical Wave 16 obstruction:** Wave 15 pays its marginal promotion from the
  same literal `beta log D` values which support the interior rank/length
  floor.  Terminal cancellation changes neither ownership nor residual
  capacity of those atoms.  Wave 17 subsequently solves this local overlap
  for the triangular floor; E66 records why the signed global problem remains.
- **Refutes:** treating a horizon taper or the terminal identity alone as a
  proof that `Delta_m` is an additive premium over `K^len`, `K^mix`, or the
  global rearrangement floor.
- **Does not refute:** the now-proved Wave 17 residual-capacity and
  majorization theorems, or a future bounded-reuse signed carrier for the
  uncapped `u-v` promotion excess.
- **Artifacts:**
  `endpoint_variance/WAVE16_TERMINAL_POTENTIAL_2026-08-29.md` and
  `endpoint_variance/wave16_terminal_potential_certificate_2026-08-29.json`.

## E65. Difference-set sparsity is false, and the critical dense case is not easier

- **Status:** `[PRIMARY-SOURCE THEOREM BOUNDARY]`.
- **Counterexample to sparsity:** a perfect difference set is Sidon and
  represents every positive integer exactly once, so
  `rho_A(x)=floor(x)`, not `o(x)`.
- **Counterexample to full little-oh:** Cilleruelo--Nathanson construct a
  perfect difference set with
  `limsup A(x)/sqrt(x)>=1/sqrt(2)`, excluding a universal full
  `o(sqrt(x/log x))` conclusion.  This does not refute the liminf-zero
  Question 1.
- **Reduction boundary:** Chen--Fang's half-scale counting shadow converts
  any hypothetical Question-1 counterexample into a perfect-difference
  counterexample.  Therefore excluding critical positive/full difference
  coverage is Question-1-equivalent, not a shortcut.
- **Does not refute:** the fixed-ray Wave 17 disjoint-capacity theorem or a
  P22 excess allocation; Chen--Fang is whole-set replacement and does not
  preserve prefix atoms.
- **Artifact:**
  `research_sources/WAVE16_PERFECT_DIFFERENCE_COMPLETION_BOUNDARY_2026-08-29.md`.

## E66. Local disjoint capacity is not a signed global repayment

- **Status:** `[RIGOROUS CLAIM BOUNDARY]`.
- **Tempting inference:** once one proves
  `mathfrak B_(2m)>=K_(2m)^int+cDelta_m-o(1)` or finds an eventual constant
  surplus above `K_(2m)^int`, the Wave 13 harmonic lower bound is
  contradicted.
- **Why it fails:** these are lower bounds on an already nonnegative interior
  bulk.  They do not by themselves give an upper bound for `Z_m`, `X_m`, or
  the signed terminal expression.  The exact renewal identity still contains
  the prefix, endpoint, descendant, and nonnegative-potential terms.
- **Exact remaining term:** after spending the local sorted-rank surplus on
  the residual `u-v` promotion truncated at height two, the unpaid charge is
  `Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+`.  Its present general envelope is
  `O_C(log log m)` per epoch, so a Fejer taper alone does not yield the
  required `o(log J)` total.
- **Double-spend warning:** the sorted-rank surplus can pay the Wave 15
  `Delta_m` premium or the capped residual promotion, but those are alternate
  allocations of the same aggregate capacity and may not be added.
- **Does not refute:** a bounded-reuse signed allocation of
  `Theta_m^exc` using actual local slack and the full renewal ledger.
- **Artifact:**
  `endpoint_variance/WAVE17_DISJOINT_RESIDUAL_CAPACITY_AND_EXCESS_BOUNDARY_2026-08-29.md`.

## E67. Rank monotonicity and the scalar cap do not remove promotion excess

- **Status:** `[RIGOROUS ABSTRACT-MODEL NO-GO]`.
- **Model:** for `N=binom(2m,2)` and integer `K>exp(h)`, take finite ranks on
  `{K,2K,...,NK}`, limiting ranks on the positive integers, and thresholds
  `d_(m,p)=K L_(m,p)`.
- **Exact result:** finite rank is `L_(m,p)`, limiting rank is
  `K L_(m,p)`, and
  `Theta_m^(exc,h)=R_m(log K-h)`.  With `K` of order `C log m`, this is
  `(3/8)log log m+O_C(1)`.
- **Refutes:** improving the excess to a summable per-epoch term using only
  rank monotonicity, integer rank bounds, and a scalar critical envelope.
- **Does not refute:** a theorem using the compatible birth geometry of one
  infinite Golomb branch.  The model is not asserted to be such a tower.

## E68. Complete one-epoch Golomb constraints do not force growing local slack

- **Status:** `[RIGOROUS — SELF-CONTAINED FINITE-FAMILY NO-GO]`.
- **Family:** for each odd prime `p`, use the strictly increasing Golomb ruler
  `a_i=2pi+(i^2 mod p)`, `0<=i<p`, and `n=(p+1)/2`.
- **Exact bound:** its diameter is below `8n^2`, and along these different
  finite rulers
  `limsup H_n^loc<=(3/4)(1+log(16/3))=2.00548...`.
- **Refutes:** proving that `H_n^loc` must diverge from one-epoch integer
  distinctness, Golomb uniqueness, and quadratic diameter alone.
- **Does not refute:** a cross-epoch theorem on one nested infinite branch;
  the prime rows are not compatible prefixes of one ruler.

## E69. The terminal identity alone cannot bound descendant-jump excess

- **Status:** `[RIGOROUS — SELF-CONTAINED, SUPERCRITICAL SCOPE]`.
- **Construction:** fix a `(2n-1)`-mark Golomb core, make a large translation
  `X` its next terminal mark, and append a suitably scaled finite Golomb
  block.  The scale exceeds the core diameter, and `X` avoids the finitely
  many remaining cross-collision equations.
- **Exact behavior:** `H_n^loc` and `D_n` remain fixed,
  `mathcal T_n(X)->0`, while the block supplies arbitrarily many new future
  differences below every terminal suffix threshold.  Hence the uncapped
  promotion excess becomes arbitrarily large.
- **Refutes:** any unconditional estimate of the excess from local slack,
  deterministic surplus, and the terminal potential alone.
- **Does not refute:** P23, which assumes one eventual-`C` branch.  The
  superincreasing infinite extension of this construction is supercritical.
- **Artifact:**
  `endpoint_variance/WAVE18_EXCESS_DESCENDANT_JUMP_AND_BIRTH_LOCALITY_2026-08-29.md`.

## E70. Positive-part midpoint jumps do not telescope under a scalar cap

- **Status:** `[RIGOROUS ABSTRACT-MODEL NO-GO]`.
- **Model:** at `h=5/2`, let `A_k=4^k exp(s_k)`, where
  `s_(2j)=0`, `s_(2j+1)=eta`, and `h-log12<eta<log4`.
- **Exact behavior:** `A_k` is increasing and has a quadratic dyadic
  envelope, but
  `[log(A_(k+1)/A_k)-(h-log3)]_+` is a fixed positive constant every other
  epoch.  Its Fejer sum is `Theta(J)`.
- **Refutes:** completing the q-collapsed P23 functional by endpoint
  telescoping and a scalar cap after taking positive parts.
- **Does not refute:** a signed cancellation before `log_+` or a theorem
  exploiting actual compatible Golomb-tower geometry.  The model is real and
  not asserted to be a difference sequence.

## E71. Terminal-cap-compatible finite Golomb prefixes attain log-log jump loss

- **Status:** `[RIGOROUS — SELF-CONTAINED FINITE-FAMILY NO-GO]`.
- **Family:** for prime `p=2n-1`, take the Erdős--Turán core of diameter
  `H=8n^2-12n+5`, then append
  `X=floor(C(2n-1)^2 log(4n-2))`.  For large prime rows `X>2H`, so every new
  difference is larger than every core difference and the append is Golomb.
- **Exact bound:** `c_n/L_(n,p)>1/2`, every descendant is at most `H`, and
  every suffix is at least `X-H`; hence
  `J_n^(h)>=R_n log((X-H)/(2exp(h)H))`
  `=(3/8-o(1))log log n+O_(C,h)(1)`.
- **Refutes:** an improvement of the one-epoch `O_C(log log n)` bound using
  local Golomb uniqueness, local slack, the terminal identity, and a cap only
  at the terminal index.
- **Does not refute:** P23.  The varying Erdős--Turán cores need not satisfy
  one fixed-onset eventual-`C` all-prefix envelope and are not one compatible
  infinite branch.

## E72. The raw Fejer suffix shift has an exact linear base channel

- **Status:** `[RIGOROUS — SELF-CONTAINED NO-GO]`.
- **Exact split:** on the full suffix range `2<=p<=2n-2`, write
  `u_(n,p)=v_(n,p)+bar r_(n,p)`, with the exceptional last value
  `bar r_(n,2n-2)=3/(8n^2)`.  Wave 18's shorter `r` formula is used only on
  `p<=n`.
- **Mismatch:** for the Fejer taper,
  `delta_(k,J)=omega_(k,J)-omega_(k+1,J)` equals
  `(2(J-k)+1)/(J+1)^2`.  If
  `B_n^v=sum_p v_(n,p)log d_(n,p)`, the exact rank floor and eventual cap
  squeeze it to `(1/2)log n+O_C(log log n)`.
- **Exact consequence:**
  `sum_(k<J)delta_(k,J)B_(2^k)^v`
  `=(log2/6)J+O_C(log J)`.  The macroscopic range `p<=n` already gives
  `(log2/8)J+O_C(log J)`.
- **Refutes:** treating the raw `v log d` shift as an `O(1)` horizon error or
  replacing it by the bounded Wave 15 `Delta` mismatch.
- **Does not refute:** a same-weight global Abel cancellation or a direct
  positive-part theorem for Wave 19's current-scale `Ghat`.
- **Artifact:**
  `endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`.

## E73. A 512-mark compatible spike/cooldown chain survives the C=32 cap

- **Status:** `[COMPUTATIONAL — CERTIFIED FINITE]` with exact integer and
  rational replay.
- **Construction:** a certified 32-mark root plus a separated translated
  95-mark scaled Erdős--Turán block gives 127 marks.  A reserve terminal,
  deterministic first-legal cooldown, and exact cap-maximum terminal steps
  produce compatible prefixes at 128, 256, and 512 marks.
- **Exact facts:** every prefix obeys the rational `C=32` envelope; the
  512-mark prefix has all `130,816` positive differences distinct.  For the
  fixed 255- and 511-mark cores, the largest cap-legal terminals are exactly
  `23,258,158` and `104,661,718`.  The selected rows have
  `J_128=0.309186077177...` and `J_256=0.005709533721...`.
- **Search boundary:** each first-legal choice is exhaustive for its fixed
  prefix, and each terminal maximum is exact for its fixed core.  Alternative
  cooldown branches were not searched, so the 511-mark path is not globally
  optimal or exhaustive.
- **Refutes:** local, one-epoch, or two-transition arguments claiming that a
  cap-compatible terminal spike cannot be followed by another long finite
  compatible cooldown.
- **Does not refute:** P23, P24, P25, or P26 and does not answer Question 1
  or 2.  No infinite compatible branch or inductive extension theorem is
  proved.
- **Artifacts:**
  `endpoint_variance/WAVE19_SPARSE_SPIKE_COOLDOWN_BOUNDARY_2026-08-29.md`
  and `endpoint_variance/wave19_sparse_spike_certificate_2026-08-29.json`.

## E74. Prime Erdős--Turán dilation obstructs bare current-scale Ghat

- **Status:** `[RIGOROUS — SELF-CONTAINED FINITE-FAMILY NO-GO]`.
- **Construction:** for every `n>=4`, choose by Bertrand a prime
  `2n-1<P<4n-2`, put
  `b_i=2Pi+(i^2 mod P)` for `0<=i<=2n-2`, set
  `H=b_(2n-2)`, append `X=2H+1`, and multiply all `2n` marks by
  `s_n=floor(log(2n))`.  The residue argument makes the core Golomb;
  `X>2H` separates every appended difference from the old spectrum.  A
  superincreasing infinite Golomb completion exists.
- **Exact local cap:**
  `H+1>2n^2`, `X<32n^2`, and `X/b_q<4` for `n<=q<=2n-2`.  Hence
  `a_q<32q^2 log(2q)` for every `n<=q<=2n-1`.
- **Promotion-robust lower bound:** for every infinite completion,
  `Pi_(n,p)<log(64s_n)` on `2<=p<=n`.  With the exact coefficient masses,
  `U_n^coef-R_n=(6n^2-12n+9)/(16n^2)>=7/32`, and therefore

  `Ghat_n>=(7/32)log s_n-C_0`,

  where
  `C_0=1/4+(3/8)log64+(3/16)log4`.
  Thus bare `Ghat_n` can be `Omega(log log n)` even after allowing the
  largest promotion permitted by the elementary rank inequalities.
- **Independent-scale consequence:** choosing a separate construction at
  each dyadic `n=2^k`, always with the same one-scale constant `C=32`, gives
  a Fejer positive-part sum `Omega(J log J)`.
- **Refutes:** a pointwise or dyadic-block proof for bare `Ghat` using only
  same-scale Golomb distinctness, elementary rank bounds, and the scalar cap.
  It historically motivated passing through P25 to P26's rank-free,
  dilation-invariant sharp remainder; E75 records the later saturation of
  that unchanged target.
- **Does not refute:** P24, P25, or P26 on one fixed compatible eventual-`C`
  branch.  The dyadic examples are different rulers, and each displayed cap
  starts at its selected scale.  No infinite critical branch, answer to
  Question 1 or 2, novelty claim, or prize claim follows.
- **Artifact:**
  `endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`.

## E75. Untouched inner-new-birth sector saturates P26/P27

- **Status:** `[RIGOROUS — SELF-CONTAINED CONDITIONAL SATURATION NO-GO]`.
- **Sharper remainder:** write
  `t_(n,p)=5/2-log(c_n/L_(n,p))>0`,
  `E_n^row=sum alpha beta [log(A/a_q)-t_(n,p)]_+`, and
  `Delta_n=J_n^(5/2)-E_n^row`.  Then `0<=Delta_n<=S_n` and the exact
  coefficient audit `S_n<=Z_n^fin` gives

  `R_n^prof=Z_n+E_n^row-J_n^(5/2)`
  `=(Z_n^fin-S_n)+Z_n^fut+(S_n-Delta_n)>=0`.

  Also `R_n^sharp>=R_n^prof`.
- **Unabsorbed support:** define

  `W_n=sum_(j=n+2)^(2n-1)sum_(i=n)^(j-2)`
  `((j-i)^2/(4n^2))C_(i,j)`.

  The Wave 19 descendant rectangle is supported on `i<=n-1`, so
  `W_n<=Z_n^fin-S_n<=R_n^prof` with no coefficient overlap.
- **Finite floor with exact constant:** on the `n` distinct adjacent gaps
  `{h_n,...,h_(2n-1)}`, put `H_n'=a_(2n-1)-a_(n-1)`.  The layered
  product proof gives

  `W_n>=E_n'/(8n^2H_n')`,

  `E_n'=sum_(r=2)^(n/2)(2r-1)(n+1-2r)(n+2-2r)/2`
  `=n(n-2)(n^2+4n-14)/48`.

  For dyadic `n>=16`, `E_n'>=n^4/48`, hence
  `W_n>=n^2/(384a_(2n-1))`.
- **Compatible-branch consequence:** if one fixed infinite branch obeys
  `a_m<=Cm^2log(2m)` eventually, then

  `R_n^sharp>=R_n^prof>=W_n>1/(1536C log(4n))`

  at all sufficiently large dyadic `n`.  Therefore its tapered liminf is at
  least `1/(1536C log2)`, twice the strict P26-sharp allowance
  `1/(3072C log2)`.
- **One-step boundary:** for dyadic `n`, the right-endpoint bands supporting
  `W_n` are disjoint.  All coefficients are positive, so ordinary Fejer
  tapering cannot cancel this floor.  It can disappear only through a new
  explicitly owned negative-cut carrier, not by reindexing `R_n^prof`
  unchanged.
- **Refutes:** treating the unchanged P26/P27 `o(log J)`, strict-threshold,
  or block-smallness conclusion as an easier standalone packing lemma.  A
  successful continuation must relocate or absorb this inner sector while
  retaining the negative renewal cuts and exact atom ownership.
- **Does not refute unconditionally:** P26/P27 as implications from a
  hypothetical branch, Question 1, or Question 2.  If no eventual-`C`
  branch exists, the branch-quantified implications are vacuous; E75 does
  not itself establish nonexistence.  It also makes no novelty or prize
  claim.
- **Artifact:**
  `endpoint_variance/WAVE19_NONNEGATIVE_SHARP_REMAINDER_DECOMPOSITION_2026-08-29.md`.

## E76. Full-terminal row allocation fails and double-spends the cut

- **Status:** `[RIGOROUS EXACT COEFFICIENT/OWNERSHIP NO-GO]`.
- **Candidate refuted:** allocate the complete terminal coefficient `u_p`
  uniformly across its full Gothic descendant row while retaining the Wave
  16 negative renewal cut.
- **First failure:** the global coefficient maximum is always at
  `C_(1,n+1)`, with ratio

  `(36n^4-140n^3+167n^2-41n-14)`
  `/[4(n-1)(2n-3)(2n-1)^2]`.

  It exceeds one for every `n>=6`; the first dyadic failure is `n=8`, and
  the ratio tends to `9/8`.
- **Independent ownership failure:** `u_p=v_p+bar r_p`.  The `v_p` part is
  already owned by the next negative cut.  Spending all of `u_p` in the
  current descendant row while retaining that cut counts `v_p` twice even
  at epochs where the coefficient inequality happens to fit.
- **Surviving legal version:** transport only `bar r_p=u_p-v_p`.  Its
  natural allocation fits every row and obeys `Sbar<=Y/2`, but does not
  complete P28.
- **Does not refute:** a signed whole-cut theorem using the legal `bar r`
  transport, Question 1, or Question 2.
- **Artifact:**
  `endpoint_variance/WAVE19_P28_FULL_ROW_OWNERSHIP_AUDIT_2026-08-29.md`.

## E77. Adaptive height and actual ranks do not erase the endpoint

- **Status:** `[RIGOROUS ATOMIC INEQUALITY BOUNDARY]`.
- **Candidate refuted:** from
  `h_p>=log(j_(p,q)/L_p)`, conclude directly that
  `Theta^exc<=Srank+S_t`.
- **Exact split:** with
  `sigma_(p,q)=h_p-log(j_(p,q)/L_p)>=0`,

  `log(d_p/(exp(h_p)L_p))`
  `=log(D_(p,q)/j_(p,q))+log X_(p,q)+log(A/a_q)-sigma_(p,q)`.

  Therefore the valid positive-part bound retains

  `E_t^rank=sum t_(p,q)[log(A/a_q)-sigma_(p,q)]_+`.

- **Atomic witness to the missing implication:** the nonnegative logarithmic
  values `log(D/j)=0`, `log X=0`, `log(A/a_q)=1`, `sigma=0` give left side
  `1` and endpoint-free right side `0`.
- **What would be sufficient but is unproved:**
  `j_(p,q)<=exp(h_p)L_p a_q/A`.
- **Does not refute:** an actual-rank theorem which keeps and pays the
  endpoint term inside the complete signed ledger.
- **Artifact:**
  `endpoint_variance/WAVE19_P28_ADAPTIVE_ROW_CAP_CANDIDATE_2026-08-29.md`.

## E78. Arbitrary row transport cannot eliminate the inner residual

- **Status:** `[RIGOROUS UNIVERSAL TRANSPORT FLOOR]`.
- **Candidate refuted:** evade the P27 inner floor by choosing an arbitrary
  feasible, energy-aware transport `t_(p,q)` of the legal `bar r_p` demand.
- **Universal floor:** for every dyadic `n>=64`,

  `E_n^res(t)>=n^2/(2^25 H_n')`.

  This includes the rowwise left-greedy transport which maximizes the covered
  energy after seeing all cross ratios.
- **Eventual-`C` consequence:** on any extant eventual-`C` branch the floor
  is `>1/(2^27 C log(4n))`, and its Fejer liminf is at least
  `1/(2^27 C log2)`.
- **Exact corner obstruction:** `C_(2n-4,2n-1)` has full coefficient
  `9/(4n^2)` and receives exactly the total last-two-row demand
  `3/(4n^2)`, so every feasible transport covers exactly `1/3` there.
- **Does not refute:** cancellation by the intact Wave 12 cut difference or
  the equivalent complete Wave 16 terminal-potential ledger.  The floor is
  not itself a contradiction.
- **Artifact:**
  `endpoint_variance/WAVE19_P28_ARBITRARY_TRANSPORT_RESIDUAL_FLOOR_2026-08-29.md`.

## E79. The mixed endpoint gain does not directly pay the inner residual

- **Status:** `[RIGOROUS FINITE COUNTEREXAMPLE TO AN UNSIGNED SHORTCUT]`.
- **Verified mixed theorem:** with `t=(8t0+tR)/9`, the rowwise right-greedy
  prefix dominance preserves `S_t<=Y_n/2`, and exact endpoint columns give
  `E_t^rank<=2Dpre_n/3` for every `n>=4`.
- **Tempting shortcut refuted:** use the gain `Dpre_n/12` to assert
  `W_n-S_t<=Dpre_n/12` pointwise.
- **Golomb witness:** at `n=4`,
  `(0,101,204,309,416,525,636,749)` has mixed residual coefficients
  `259/5760`, `3/32`, and `5/128` on the three inner atoms.  Exact rational
  lower/upper bounds for their logarithms prove

  `W_4-S_t|W_4>Dpre_4/12`.

- **Does not refute:** the signed whole-cut target
  `Gmix=R+Pcoef logA-Kint-T-ThetaFull-Dpre/3`.  A legally retained cut or
  terminal term may still supply cancellation unavailable to the unsigned
  comparison.
- **Ownership warning:** the hostile rewrite of `Gmix` does not permit reuse
  of `D-ThetaPrev`, `Qad`, or `Pair`; those terms were already dropped with
  favorable sign.
- **Artifact:**
  `endpoint_variance/WAVE19_P28_MIXED_RIGHT_GREEDY_ENDPOINT_GAIN_2026-08-29.md`.

## 2026-08-31 C132/C134 exact strict-subroute no-go results

### Naive affine paste of the C130/C131 local banks

- **Fixture:** `C120 union (1239+5*C123)`, 32 marks, span 7084.
- **Finite validity:** all 496 positive differences are distinct; prefixes
  `4..32` satisfy the exact audited onset-4 `C=2` cap.
- **Failure:** the natural epoch-16 owner audit has 152 strict failures among
  692 rows.  The strongest margin is
  `-175791028451541/10006250000000000`.
- **Scope:** this refutes affine reuse of the named local owner factors.  It
  does not refute fresh cross-block factors, fractional ownership, or a joint
  epoch-8/16 program.
- **Artifact:**
  `route_probes/ROUTE_C_C132_COMPOSITE32_NAIVE_PASTE_NO_GO.md`.

### Exact phase alignment inside the same affine paste family

- **Forced alignment:** `T=1169+143q`.
- **Collision:** `711-284=427=143+284`, so the concatenation has two copies
  of the positive difference `427q` for every integer `q>0`.
- **Scope:** only this exact affine alignment family is exhausted; a different
  ruler or a new common physical phase is not ruled out.

### Positive-Gram-only representation of the 63-source residual

- **Target:** `R16=M16-(M8_left+M8_right)/4`.
- **Separator:** for `q=e0+e8`, `q^T R16 q=-1/16`, whereas every positive
  rank-one Gram root has value `(q dot z)^2>=0`.
- **Boundary support:** dropping rank 15 forces the `(0,8)` target entry to
  zero although it equals `-1/32`; restricting to mapped C123 ranks 19--31
  similarly misses the exact entry `15/2048`.
- **Scope:** the positive-only cone and the two named smaller supports are
  exhausted.  The exact signed representation exists, but its negative bank
  is not positive capacity.
- **Artifact:**
  `route_probes/ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP.md`.

### Frozen universal D1 same-multiset rotation transfer

- **Target:** the assertion that every Golomb member of the specified frozen
  `4x8` cyclic old/new same-multiset rotation bank satisfies the fixed
  complete-phase lower bound used by C125--C130.
- **Counterexample:** the O0N1 16-mark Golomb row on phase `[82,164]`,
  `rho=9/16`, and the fixed coefficient vector.  An exact 314-piece dual bank
  has `U^+<T^-`, with separator margin greater than `1/2500` by weak
  duality.
- **Earlier false negative:** the one-stored-dual-per-parent-chamber bank's
  `NO_SEPARATION` result was never primal feasibility; exact rational
  subdivision exposes the separator.
- **Scope:** this exhausts only the displayed O0N1 transfer under the frozen
  cone and coefficients.  It does not invalidate C130's O0N0 witness, Route
  C, every rotation, global representative independence, or C058.
- **Artifact:**
  `route_probes/ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO.md`.

### Pointwise recovery of the one-sided C133 box carrier from the C136 graph

- **Target:** any memoryless map from the current 100-channel graph state to
  the one-sided box-carrier C133 total, fourteen-row vector, or terminal pair.
- **State-collision witness:** the full state is identical on
  `[616,20401/32)` and `[20401/32,21009/32)`, with all 57 supported root
  features and all direct demands zero, but the carrier totals are
  `64/104961675` and `176/314885025`.
- **Terminal witness:** a second identical-state pair changes both terminal
  rows; separate zero-capacity cells have positive epoch-8 and epoch-16
  carrier terminals.
- **Consequence:** scalar, diagonal, owner-block, affine, linear, and arbitrary
  nonlinear pointwise maps from this state all fail.
- **Scope:** this exhausts only the one-sided all-pairs box carrier. It does
  not refute the cumulative direct-`M8/M16` potential, enlarged state,
  nonlocal transport, or C058. In fact the correct same-`M` aggregate
  terminals vanish on this fixture.
- **Artifact:**
  `route_probes/ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO.md`.
