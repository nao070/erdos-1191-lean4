# Erdős Problem #1191 Research Log

Started: 2026-08-26 (workspace local time)

## Mission
Resolve Q1 and Q2 for infinite Sidon sets with publication-grade rigor. No unresolved theorem-strength lemma may be promoted to a theorem.

## Wave 1 plan
1. Verify the current literature frontier from primary sources.
2. Launch independent literature, cold-proof, computational, and adversarial tracks.
3. Build a literature ledger and approach registry.
4. Test candidate mechanisms computationally.
5. Maintain exact quantifier conversions and audit all candidate claims.

## Status
Research in progress. No candidate resolution exists yet.

## Progress 2026-08-27
- `notes/counting_conversion.md`: L = sqrt(2/S) conversion proved (Q1 ⟺ S = ∞).
- `notes/forbidden_recurrence.md`: incremental forbidden-position recurrence
  proved (Lemma 1, Lemma 2, Theorem, Corollaries 1–3).
- Computational verification of the recurrence is **complete**
  (`computation/forbidden_recurrence.py`, all 5 contracts PASS; see
  `counterexamples.md` entry E2). The exact bitset engine
  `BitsetEngineR` (`computation/greedy_growth.py`) is validated against the
  naive oracle to 400 marks term-by-term and fuzzed on 2,000 random
  ≥ 2-mark seeds; constructor invariants are exact.
- Baseline harness `computation/check_sidon.py` re-run: PASS (60/60).
- Measured generator constants in `computation/README.md`.
- Next: use the validated engine for the density/measurement wave
  (Mian–Chowla growth rate, F(x) along greedy and non-greedy branches);
  literature ledger verification of the O'Bryant July-2026 bound remains open.

## Progress 2026-08-27 (continued, Wave 2)

### Finite-field implementation and verification
- Implemented GF(p^k) with explicit-modulus arithmetic (`computation/crossblock.py`).
- Verified field axioms for p ∈ {2,3,5,7,11}, k ∈ {2,3,4}: primitive elements found,
  discrete log tables complete, multiplication commutative, dlog homomorphism holds.
- Implemented Bose–Chowla and Singer constructions from first principles:
  - Bose–Chowla(q) for q ∈ {2,3,5,7,11,13}: produces q marks, verified Sidon.
  - Singer(p) for p ∈ {2,3,5,7,11}: produces p+1 marks, verified Sidon.
- All constructions pass dual Sidon characterization (diff and sum).

### Cross-block compatibility experiments
- Implemented collision taxonomy (VV/VW/WW) per `notes/obryant_splice.md`.
- Built conflict graph constructor and max-independent-set solver.
- **KEY FINDING**: Systematic scaling study reveals fundamental obstruction:

| \|V\| | max(V) | \|D(V)\| | F(V) density near max | Compatibility ratio |
|-------|--------|----------|----------------------|-------------------|
| 10    | 97     | 45       | 0.610                | 0–43%             |
| 20    | 565    | 190      | 0.900                | 0–14%             |
| 30    | 1,395  | 435      | 0.990                | 0%                |
| 50    | 5,123  | 1,225    | **1.000**            | **0%**            |
| 75    | 14,047 | 2,775    | **1.000**            | **0%**            |
| 100   | 28,566 | 4,950    | **1.000**            | **0%**            |

**Mathematical mechanism**: F(V) = V + D(V) becomes dense near max(V) as V grows.
For \|V\| ≥ 50, F(V) covers 100% of integers in [max(V), max(V)+100], so **no
integers are available** for extending V while maintaining the Sidon property.

**Conclusion**: Dense block gluing (Approach C) **cannot yield asymptotic
progress** on #1191. The forbidden set grows too fast relative to available
positions. This is a fundamental obstruction, not a technical limitation.

**Implication**: Approach C is **BLOCKED**. Must pivot to a fundamentally different
mechanism (probabilistic methods, entropy-based approaches, or methods that don't
rely on dense block gluing).

- Data: `computation/out/crossblock_scaling.json`.
- See `counterexamples.md` entry E3 for full documentation.

## Wave 2 Progress (2026-08-28)

### Literature Verification
- O'Bryant 2026 papers (Parts I & II) verified against arXiv primary sources
- Finite-field constructions (Bose–Chowla, Singer) verified to produce Sidon sets
- GF(p^k) arithmetic validated for p ∈ {2,3,5,7,11}, k ∈ {2,3,4}

### Key Finding: Fundamental Obstruction to Dense Block Gluing

**Hypothesis tested**: Can we build an infinite Sidon set by gluing dense finite blocks at W₁ ≈ V₂ (dense placement)?

**Experiment**: `computation/crossblock.py` systematic scaling study (data: `computation/out/crossblock_scaling.json`)

**Result**: F(V) = V + D(V) becomes dense near max(V) as V grows:

| |V| | max(V) | |D(V)| | F(V) density | Compatibility ratio |
|-----|--------|----------|--------------|-------------------|
| 10  | 97     | 45       | 0.610        | 0–43%             |
| 20  | 565    | 190      | 0.900        | 0–14%             |
| 30  | 1,395  | 435      | 0.990        | 0%                |
| 50  | 5,123  | 1,225    | **1.000**    | **0%**            |
| 75  | 14,047 | 2,775    | **1.000**    | **0%**            |
| 100 | 28,566 | 4,950    | **1.000**    | **0%**            |

**Mathematical mechanism**: For |V| ≥ 50, F(V) covers 100% of integers in [max(V), max(V)+100], meaning **no integers are available** for extending V while maintaining the Sidon property.

**Conclusion**: The dense block gluing strategy **cannot overcome** the natural growth of the forbidden set. This is not a technical limitation—it is a fundamental mathematical obstruction.

**Implication**: Approach C (dense algebraic/recursive construction with compatible extensions) is **BLOCKED**. Need to pivot to a fundamentally different mechanism (probabilistic methods, entropy-based approaches, or methods that don't rely on dense block gluing).

**Next**: Update approach_registry.md to mark Approach C as BLOCKED; document in counterexamples.md; consider whether the obstruction can be reformulated as a theorem.


## Handoff continuation — endpoint variance and literature refresh (2026-08-28)

### Artifact audit

- Mounted and inspected both supplied ZIPs.
- Verified by SHA-256 that all 28 files in `erdos1191_endpoint_variance_artifacts_2026-08-28.zip` duplicate files already present under the first ZIP's `core_workspace/endpoint_variance/` tree.
- Removed bytecode/test caches from the new handoff.
- Identified a self-referential entry in the original endpoint `SHA256SUMS`; all other payload entries pass when checked from the correct parent directory.
- Generated a new package-level self-excluding manifest and cross-platform verifier.

### Exact rerun

- `pytest -q`: 15 passed.
- endpoint certificate: 10,890 checks.
- diameter certificate: 15,345 checks.
- mandatory-level certificate: 16,380 checks.
- total: 42,615 exact checks.

### Mathematical audit

- Preserved the endpoint-imbalance reconstruction, Eulerian zero-mode characterization, homometric separation, and sharp unrestricted mandatory-level bound.
- Added the important scope correction that the equality family `A={0,1,...,m-1}` is non-Sidon for `m>=3`; Sidon-class sharpness remains open.
- Recorded the explicit two-moment dependence `Var E_N=S_m/N-T_m^2/N^2` for all `N` above a fixed prefix diameter, warning that such averaging alone may not be genuinely multiscale.
- Promoted the anti-Eulerian multiscale budget to the highest-priority route.

### Literature/tool refresh

- Checked the public #1191 record and current primary arXiv/journal pages for O'Bryant I/II, Táfula, Cilleruelo, Ding, and Ortega–Prendiville.
- Used Exa, SciSpace, Firecrawl ordinary/research search, and normal site-restricted searches.
- Consensus search was attempted but unavailable because the monthly quota was exhausted.
- No verified complete solution was located in the searched public sources; this is not treated as proof of absence.

### Corrected project discipline

- Rewrote the canonical approach registry to distinguish tested naive dense-translate gluing from all compatible algebraic constructions.
- Marked older crossblock/profile experiments as reported but not currently reproducible because their code/raw files were absent from the uploaded continuation.
- Created explicit proof obligations, literature ledger, counterexample ledger, source protocol, and next-lemma agenda.

### Current bottleneck

No summable or telescoping Sidon upper budget has yet been proved for the large endpoint variances forced by critical prefix growth. The next session should derive and falsify exact quartic/martingale/cycle-packing candidates rather than return to one-scale mean optimization.

## Continuation verification — 2026-08-28 14:58:42 JST

### Environment

- Working package root: `/Users/USER/Documents/ChatGPT/mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28`
- Python: `Python 3.13.13` at `/Users/USER/miniforge3/bin/python`
- OS: macOS 26.6.2 (Build 25G83), Darwin 25.6.0, arm64

### Package integrity

- Command: `python integrity/verify_package.py`
- Exit code: `0`
- Output: `PACKAGE VERIFICATION PASSED: 52 files`
- Manifest note: `integrity/PACKAGE_SHA256SUMS.txt` intentionally excludes itself.

### Exact finite verification

Run from `core_workspace/endpoint_variance/`.

- Initial command: `python -m pytest -q`
- Initial exit code: `1`
- Initial discrepancy: `/Users/USER/miniforge3/bin/python: No module named pytest`
- Classification: execution-environment dependency missing; this was not a test assertion failure.
- Recovery: created the package-external temporary virtual environment `/tmp/erdos1191-pytest.gu2FvF/venv` and installed `pytest==9.1.1` there.
- Recovery command: `/tmp/erdos1191-pytest.gu2FvF/venv/bin/python -m pytest -q`
- Recovery output: `15 passed in 0.02s`; exit code `0`.

- Command: `python certificate.py`
- Exit code: `0`
- Output: `total_checks=10890`; certificate SHA-256 field `e7716bd611165d5e22566a4355e595d440ef56c120e30e1804498784966f8c23`; homometric variances `79/28` and `55/28`; zero-mode variance `0/1`.

- Command: `python diameter_certificate.py`
- Exit code: `0`
- Output: `exact_checks=15345`; certificate SHA-256 field `82c8b646b9e620e9982b12194272376875d8bbcf040fb46aad31d36b84f517e9`.

- Command: `python required_levels_certificate.py`
- Exit code: `0`
- Output: `exact_checks=16380`; certificate SHA-256 field `81e7f7a6a07673bf2f4ccdf3e995c6b5e8a2aa310a8560006a5c355891195752`.

### Verification outcome

- All 15 supplied tests passed after isolating the missing test dependency.
- All three deterministic certificates matched the handoff baselines, totaling 42,615 exact checks.
- No mathematical or artifact discrepancy remains after the environment-only recovery.

## Anti-Eulerian continuation — Wave 0--2 (2026-08-28)

### Wave 0: independent mathematical audit

- Re-derived the bad-offset arc with the half-open block convention in both
  wrap and nonwrap cases.
- Independently verified
  `C_N(r+1)-C_N(r)=outdeg(r)-indeg(r)`, cyclic reconstruction, and
  `Var(E_N)=Var(C_N)`.
- Recomputed the unnormalised Fourier formula and confirmed the factor
  `1/N^2`.
- Confirmed that zero variance means componentwise balance and edgewise cycle
  decomposition; connectivity or a single Euler tour is unnecessary.
- Recomputed the diameter gap formula, the cubic imbalance sum, both
  polynomial sums in the mandatory-level theorem, and the homometric values
  `79/28` and `55/28`.
- Corrected the prose to say “smallest nontrivial zero mode with a nonempty
  short-edge graph,” to treat mandatory levels as an indexed multiset, and to
  separate unrestricted sharpness from Sidon sharpness.
- No mathematical error was found in the endpoint theorem.  The novelty audit
  remains preliminary.

### Literature continuation

- Retried Consensus; the request failed because all 30 monthly searches were
  used, with reset reported for 2026-09-01.  No evidence was returned.
- Reviewed 30 SciSpace abstracts over three targeted searches.
- Ran four Firecrawl research-index searches (`k=12` each), known-paper and
  related-paper inspection, exact ordinary searches, and public
  specialist-site searches.  Empty/incomplete search feedback was submitted
  where the feedback window remained open.
- Reviewed 102 Exa results over ten workstreams and fetched selected primary
  pages.
- Rechecked the official #1191 page and official O’Bryant v3 HTML.  The public
  page still displayed Open and zero claimed proofs; O’Bryant section 3.1
  explicitly discusses multiple `N`, reverse martingales, entropy, and Cauchy
  stability.
- Added arXiv:2608.13739 and arXiv:2606.17487 as adjacent recent work, and
  Bekir--Golomb 2007 as classical homometric-ruler context.  None supplies the
  missing critical-prefix budget.
- Every query group, rejection, primary-text status, and access failure is in
  `literature_ledger.md` and
  `../research_sources/SEARCH_TOOL_LOG_2026-08-28.md`.  No absence theorem or
  publication novelty claim is made.

### Wave 1: Target A exact functional

- Added `endpoint_variance/multiscale_variance.py` and test-first exhaustive
  oracles.
- Proved the exact cyclic-arc intersection formula and the resistance
  polarization

  `K_N=1/2[Phi(a-d)+Phi(b-c)-Phi(a-c)-Phi(b-d)]`.

- Proved the ordered expansion

  `N Var(C_N)=sum_(p,q) K_N(p,q)`

  and retained both exact boundary indicators in its cross-prefix form.
- For `m_j=2^j`, `N_j=D_(m_j)+1`, and `w_j=m_j^-3`, proved under the critical
  envelope

  `F_J >= (1+o(1)) log(J)/(360 C log(2))`.

- Proved absolute summability of the diagonal and of each fixed interaction;
  the unresolved mass is the signed aggregate of `O(m^4)` off-diagonal
  interactions born at a scale.
- Derived the fixed-containing-modulus prefix identity
  `C_m-2C_(m-1)+C_(m-2)=(m-1)1_(a_(m-1),a_m]`.  It reconstructs the known gap
  profile and does not supply a Sidon upper budget.
- Independently audited the new note.  One typesetting defect (a missing `+`
  between diagonal and off-diagonal sums) and four scope/definition
  clarifications were repaired before release.

### Wave 1 falsification results

- `{0,3,7,12}` at `N=6` is a Sidon three-edge Eulerian zero mode.
- For pairs `(0,3)` and `(1,7)` in `{0,1,3,7}`, covariance changes from
  `-1/4` at `N=8` to `7/8` at `N=16`.
- For `A_G={0,1,G+1,G+3}` and `N=G+4`,
  `Var=(19G+27)/(G+4)^2 -> 0`.
- An explicit iterative sparse Sidon construction has diameter-regime
  variance of order `m^4` at doubling stages.  This refutes only the specific
  unconditional critical-weight raw-variance budget; a density-compatible
  budget remains open.
- The homometric pair has common diagonal sum `65/2` but ordered off-diagonal
  sums `7` and `-5`.

### Wave 2: certified computation

#### Golomb variance search

- Exhaustive parameters: `2<=m<=7`, `m-1<=D<=25`, and
  `N=D+1,D+2,D+3`.
- Completeness: 245,505 normalized internal-mark candidates, 9,013 oriented
  Golomb rulers, 27,039 exact `Fraction` variances, 135 `(m,D)` cases.
- Independent oracle: recursive positive-gap compositions plus direct
  translated half-open block counts; 294 comparisons, zero mismatches.
- Least-diameter minima for `m=2,...,7`:
  `1/4, 3/4, 12/7, 26/9, 404/81, 1161/169`.
- Deterministic JSON SHA-256:
  `58bab957e48be7dc97206ecf45243f907064240e22785604a09512355f8f2f6e`.
- Internal canonical payload SHA-256:
  `7bde9b209c687cdbc99d933af856041feac5fd52707be25f169e5c72bbbf4cc3`.
- Singer/Bose--Chowla stress cases are explicitly `not_run`; the package has
  no validated constructor and no claim is inferred from that omission.

#### Multiscale finite certificate

- 49,192 literal cyclic-arc overlap checks.
- 49,192 resistance-polarization checks.
- 1,152 ordered pair--pair cases, evaluating 37,472 kernel terms.
- 4 exact three-cycle checks, 3 sign-flip checks, and 594 dominant-gap checks
  for `3<=G<=200`.
- Total: 100,137 exact finite checks, zero mismatches.
- Final portable canonical payload SHA-256:
  `79579be82b7d831b5bc1f57b22e1c903d3bec3a01d744e55b2e677a1e8fc821b`.
- Final JSON SHA-256:
  `9611b447cd511033ded4b23e8a8d64270235a7e4ba40b251130de59851a8ae84`.
- Two final generations were byte-identical.
- A package-level cross-environment check exposed that recording the absolute
  Python executable path made otherwise identical system/venv generations
  differ.  The path was removed from the canonical payload while Python
  version, implementation, OS, release, and machine remain recorded.  Final
  system-Python and venv-Python 3.13.13 generations are byte-identical.

### Final regression and discrepancies

Run from `core_workspace/endpoint_variance/`.

- During concurrent test-first development, one intermediate full pytest run
  saw the certificate worker's intentional minimal RED stub and reported two
  `KeyError` failures (`evidence_scope` and `canonical_payload_sha256`).  This
  was a visible in-progress state, not a mathematical regression.  The final
  implementation supplies both fields.
- Final command:
  `/tmp/erdos1191-pytest.gu2FvF/venv/bin/python -m pytest -q`.
- Final output: `33 passed, 42 subtests passed in 6.17s`.
- The three original certificates were rerun unchanged: 10,890; 15,345; and
  16,380 exact checks.
- The full Golomb certificate and multiscale certificate were each regenerated
  to `/tmp` and compared byte for byte with their packaged JSON; both matched.
- Initial Ruff run found three import-order/style-only findings.  They were
  patched without changing logic; final Ruff output was `All checks passed!`.

### Global outcome

The exact kernel and critical lower accumulation are new rigorous partial
results, and several tempting upper-budget mechanisms are now refuted.  No
density-compatible signed upper budget has been proved, and neither Q1 nor Q2
is resolved.  Global status: `UNRESOLVED_AT_HARD_LIMIT`.

## Anti-Eulerian continuation — Wave 3 (2026-08-28)

### Positive gap identity and Sidon block theorem

- Re-expressed the diameter-regime variance as the exact positive sum
  `N^-2 sum_(k<l) h_k h_l (l-k)^2(m-k-l)^2`.
- Partitioned the internal gaps into eight rank blocks and used the distinct
  differences inside consecutive Sidon subrulers to prove, for `m=8q>=16`,
  `V_m >= 9Dq^5(q-1)/(16N^2) >= 9m^6/(16,777,216N)`.
- Under `N_m<=2Cm^2 log m`, derived
  `G_J=sum_j V_(m_j)/m_j^4 >= [9/(33,554,432 C log 2)] sum_j 1/j`.
- Exchanged the positive finite sums exactly to obtain the birth kernel
  `Lambda_J(k,l)>=0` and the unconditional upper
  `G_J <= (4/3) sum_s H_s/N_s <= (4/3)log N_J`.
- Proved the three-rank lifted obstruction `V_m/m^4>=1/2304`, including dense
  `O(m^2)`-diameter bases.  It excludes pointwise `o(1)` conclusions based
  only on an isolated ruler; it does not exclude every compatible
  bounded-depth inequality.

### q-cover martingale audit

- Proved exactly
  `q^2 Var_(qN) C = Var_N R + I_(N,q)`, where `I_(N,q)` is an explicit sum of
  fibre squares.
- Recovered a genuine martingale and square-function identity for a frozen
  edge multiset.
- Found the minimal complete-load obstruction `{0,1,4}`: coarse variance
  `1/4`, fine variance `0`.  The general family is `{0,1,qN}`.
- Proved the two-way inequality
  `V(old)/2 <= q^2 V(fine) + V(birth residual)`, but a nested-star Sidon family
  shows no uniform Bessel bound for every newborn subfamily from length
  distinctness alone.  No lower bound is claimed for the complete newborn
  load.

### Critical-shell falsification

- H1--H4 were refuted by `(0,1,4,6)` and H5 by `(0,4,6,7)`.
- Complete certified scans covered 9,870 four-mark and 22,706,280 eight-mark
  candidates.  Six retained 16/32-mark seeded witnesses were also audited.
- H6 net-shell nonnegativity survived only as a finite pattern.  It is not
  promoted to a theorem and would not supply the desired upper budget.
- Certificate internal hash:
  `b3382d17c93b0048aa581ce009876570f57da2bd4adeaed1a33d163f970b0c2a`.

### Source-audited literature synthesis

- Persisted a 306-record corpus across arXiv, Crossref, OpenAlex, and Semantic
  Scholar citation chasing; 16 papers were selected, with 12 deep-tier audits.
- Exa, Firecrawl, and SciSpace were used as discovery/retrieval aids.
  Consensus was attempted but its 30/30 monthly quota was exhausted.
- No source in the audited corpus proves the required `o(log J)` budget or
  rules out every such route.  This is a qualified null finding, not an
  absence theorem.
- Quantitative checks show why current near-extremal Fourier estimates become
  trivial at `sqrt(n/log n)` and why the entropy large sieve lacks its required
  fixed modular-deficit premise for arbitrary Sidon prefixes.
- Report lint: 17 anchors used and defined; zero unknown, undefined, or unused
  anchors.  Report path is recorded in `research_state.json`.

### Exact verification

- Pre-gap-dynamics baseline `python3 -m unittest discover -v`: 42 tests
  passed.  The final package-level pytest count is recorded in the dated
  Wave 3 integrity report.
- `python3 -m unittest -v critical_shell_test.py`: 10 tests passed.
- `sidon_block_variance_certificate_2026_08_28.py`: 3,200 arbitrary-set gap
  identity checks, 9,013 exhaustive Golomb identity checks, 5,000 random
  16-mark theorem checks, four structured lifts, and one exact dyadic
  birth-expansion comparison; the v2 certificate also adds 11,213 exact
  gap-measure-dynamics checks.  All passed.  Internal payload hash:
  `be3827bc71c35daef84a4510e41e859bcc3b52810acd517b1c86df0bfde52aa7`.
- `critical_shell_certificate_2026_08_28.py` regenerated the packaged finite
  search certificate successfully.
- The system Python did not contain `pytest`; `unittest` exercised the same
  test classes without an external dependency.  This was an environment fact,
  not a failed assertion.

### Current bottleneck

The best remaining target is compatible-prefix gap-measure rigidity: under the
critical envelope, prove
`sum_(j<=J) Var_(nu_j)(u(1-u))=o(log J)` using genuine compatibility along one
infinite Sidon sequence.  A bounded-depth relation remains eligible if its
verified local charges telescope across unboundedly many scales.  Isolated
single-prefix pointwise estimates, scalar martingales, and naive birth-edge
orthogonality are rigorously insufficient.  Q1 and Q2 remain unresolved.

### Wave 3 adversarial follow-up

- The fixed-modulus monotonicity proposed after H6 was disproved.  The globally
  minimal Sidon example for doubled-prefix comparisons is `N=40`,
  `(0,20) subset (0,20,21,39)`, with variance `1/4 -> 99/400`.  The analytic
  minimality proof covers every doubled-prefix size; general non-doubling
  extensions can fail earlier.
- `prefix_monotonicity_certificate_2026_08_28.py` independently checked 780
  `r=1` configurations, 91,390 `r=2` configurations (73,434 Sidon), 3,262,623
  `r=3` configurations (427,488 Sidon), and 61 members of the infinite
  counterfamily.  Its internal payload hash is
  `8e066c5dc3a0c1eeb7086079073303b948f06a9c3e34505cf9e6ef1ba3a8f5e8`.
- A separate exact no-go theorem shows that fully orthogonal per-edge
  Hilbert coordinates have trace-synthesis product at least `P^3/(9N)` for
  `P` distinct differences.  Under the critical envelope this is already
  harmonic and cannot yield `o(log J)`.
- Added exact code and tests for the prefix counterfamily, weighted coordinate
  trace, q-cover vector increment, and discounted trace.

### Wave 3 gap-measure dynamics and optimized two-step lower bound

- Defined the normalized diameter-gap measure
  `nu_m=N_m^-1 sum_(k<m) h_k delta_(k/m)` and verified exactly that
  `Var(C_(N_m))/m^4=Var_(nu_m)(u(1-u))`.
- For `z=(u(1-u),u)` and
  `M_m=N_m Cov_(nu_m)(z)`, proved the exact dyadic mixture identity
  `M_(2m)=B M_m B^T+Q_m`, with
  `B=((1/4,1/4),(0,1/2))` and an explicit positive-semidefinite innovation
  `Q_m`.  This is a genuine cross-prefix positive potential; it does not close
  on the scalar first coordinate.
- Selected the largest `3m/4` distinct adjacent gaps and combined their exact
  rank-variance lower bound with two-step aging.  For every dyadic `M>=16`,
  obtained
  `Var(C_(N_M))/M^4 >= (9M^2-256)/(1,048,576N_M)`.
- Under `N_M<=2CM^2 log M`, the pointwise coefficient is
  `(9-256/M^2)/(2,097,152 C log M)`, and the dyadic sum has leading lower
  coefficient `9/(2,097,152 C log 2)` times `log J`.  This improves the
  direct eight-block constant by a factor of sixteen while using only
  distinct adjacent gaps.
- With the `m^-4` weight, the absolute future tail of one fixed ordered
  interaction is at most `4/(15m_s^4)`.  Since `O(m_s^4)` interactions are
  born at shell `s`, the crude absolute loss is `O(1)` per shell.  This is
  still `O(J)`, so the missing `o(log J)` signed/structural upper budget has
  not been proved.
- Exact Fraction tests checked the matrix update on 240 random increasing
  sets, the two-step theorem on structured 16/32/64-mark Erdős--Turán rulers,
  and scalar aging counterexamples in both directions.  An independent
  adversarial algebra audit confirmed every displayed constant and retained
  the caveat that finite scalar counterexamples do not settle compatibility
  inside one infinite critical sequence.

### Adjoint innovation reduction and abstract PSD no-go

- Normalized the covariance recursion as
  `R_(j+1)=rho_j B R_j B^T+Qhat_j` and solved the finite-horizon adjoint
  recursion `H_j=E+rho_j B^T H_(j+1)B`.
- Proved the exact telescope
  `sum_(j<=J) G_j=<H_1,R_1>+sum_(j<=J)<H_(j+1),Qhat_j>`.
  The universal Lyapunov majorant is
  `H=((16/15,8/105),(8/105,4/35))`, with determinant `256/2205`.
- Constructed an abstract critical orbit
  `N_j=L4^j j`, `R_j=diag(1/72,1/6)` whose innovations are strictly PSD but
  `G_j=1/72` at every scale.  The covariance is realizable as
  `Cov(u(1-u),u)` for a compactly supported probability measure, but the
  innovations are not claimed to come from compatible integer gap profiles.
- Consequently recursion, PSD, and critical growth alone cannot imply even a
  sublinear energy sum.  The exact remaining lemma is an arithmetic upper
  budget for the actual newborn-shell covariance plus rank-one mean
  innovation.  Uniformly controlled PSD-linear, trace, determinant, and
  eigenbasis potentials cannot supply it; formal forward telescopes with
  exploding coefficients exist but have an unusable terminal cost.
- Added exact code, four unit tests, and a deterministic certificate with 512
  positive-definite innovation checks and 128 adjoint-horizon checks.

### Fixed-depth Erdős--Turán closure

- Proved the band-packing inequalities
  `C(s-r+1,2)<=a_s-a_r` and
  `D-(a_s-a_r)+1>=(r+1)(m-s)`, hence
  `h_k<=N-k(m-k)`.
- Proved disjoint internal block-spectrum packing
  `R_(r)>=sum_(i<=r) C(q_i,2)` and its logarithmic Carleson corollary.  The
  resulting bound is only `O(J)` on dyadic blocks.
- For every fixed depth `L`, used arbitrarily large finite Erdős--Turán rulers
  whose last `L+1` dyadic prefixes share a `C=1` critical envelope.  Their gap
  measures tend to Lebesgue measure, giving exact limits
  `Var_nu f -> 1/180`, `Q_00/N -> 1/360`, and signed same-modulus birth shell
  `->19/3840`; the born diagonal is `O(M^-2)`.
- This refutes all uniform fixed-window `o(1/j)` lemmas based only on local
  Sidon/critical compatibility.  It does not refute global extendability or
  unbounded-history amortization.  Added exact code, three unit tests, and a
  deterministic seven-scale certificate through 1,024 marks.

## Anti-Eulerian continuation — Wave 4 (2026-08-28)

### Growing-depth local-history no-go

- Strengthened the fixed-depth Erdős--Turán family to a window whose depth
  tends to infinity.  For terminal `M=2^J`, `J>=8`, the last
  `L_J+1=floor(log_2 J)-1` dyadic prefixes share the same `C=1` critical
  envelope.
- Proved the exact gap-CDF bound `d_K<=4/n` uniformly on the window.  For
  `f(u)=u(1-u)`, the summed gap variance is
  `(log J)/(180 log 2)+O(1)`.
- Computed the uniform adjacent limits `Q_00/N->1/360`, same-final-modulus
  birth shell `->19/3840`, and limiting full innovation matrix
  `((1/360,-1/192),(-1/192,7/96))`, determinant `97/552960`.
- Scope was kept explicit: every terminal `J` uses a new finite ruler and
  prime.  This is not an infinite globally critical sequence.  Qualitative
  infinite completion of a finite Sidon set has no critical-growth guarantee.
- A separate adversarial audit independently confirmed the critical-window
  arithmetic, index ranges, uniform error, matrix entries, determinant, and
  birth-shell constant.  It recommended only the cosmetic explicit use of
  Bertrand's postulate and `n_min=Theta(2^J/J)`, which were adopted.
- The deterministic certificate checked the sufficient depth condition
  1,368,943 times over `8<=J<=100000`, plus exact structured rulers through
  65,536 marks.  Its internal payload hash is
  `4f324bccae4684a7dbadd97c7e50e3dad99a0b8b252c9464388b955c151b5704`.

### Cross-block packing and global profile resets

- Proved the constant-one weighted cross-band inequality for any disjoint
  family of ordered rank rectangles.  On the complete dyadic rank tree it
  gives `sum_v m_v^2/D_v<=1+log binom(M,2)`.
- For `M=qm`, combined all cross spectra with one block lag.  If
  `epsilon_M=max_r|N_r/N_M-r/M|`, then
  `(q-d)m^2<=N_M(2/q-2/M+4epsilon_M)+1`.
- Used all inter-block differences plus only the old prefix bound
  `N_m<=K m^2 log m` to prove
  `epsilon_M>=1/q-Km^2 log(m)/(binom(q,2)m^2+1)`.  Along one hypothetical
  global critical sequence, choosing dyadic `q` near `4K log M` forces
  `epsilon_M>1/[4(1+4K log M)]` at every large dyadic `M`.
- Audited the grid indexing through both one-sided limits.  The exact relation
  is `epsilon_M<=d_K<=epsilon_M+1/M`: on
  `[(r-1)/M,r/M)` the CDF equals `N_r/N_M`.
- The exact cross-block certificate exhaustively audited 548 normalized
  four-mark Sidon rulers in diameters 6 through 18, with 1,688 same-lag band
  checks, 552 dyadic-tree checks, and four structured Erdős--Turán rulers.
  Internal payload hash:
  `b1837cac55e843db09fd82fd7c687183971c0cd988cb1e6a12eb8dd3918fe2d6`.

### Failure of a direct innovation charge

- In the growing Erdős--Turán window, the total occupancy ratio of all
  old--new cross spectra to their exact containing bands is below `1/2`, while
  the corresponding innovation sum is `L_J/360+o(1)`.
- This refutes every fixed affine direct charge of `sum Q_00/N` to those local
  occupancy ratios, including a pointwise vanishing analogue at the back of
  the growing window.
- The nested non-Sidon profile `a_k=k^2` has limiting density `2u`, quadratic
  diameter, and positive limiting innovation
  `((19/3840,-1/80),(-1/80,5/96))`.  Its determinant is `187/1843200`.
  The equality `5^2-1^2=7^2-5^2` records why Sidon arithmetic is still the
  essential missing input.
- The Sidon family `(0,H,H+1,2H+3)` has
  `epsilon=d_K=1/4` but gap variance
  `(5H+9)/(256(H+2)^2)->0`.  The homometric rulers `(0,1,3,7)` and
  `(0,1,5,7)` have the same discrepancy, old prefix, and diameter ratio but
  different exact innovation matrices.  Thus the scalar reset size alone
  cannot control `G` or `Q`.

### Certified finite nested-prefix search

- Searched one `C=1` compatible ruler through dyadic sizes 4, 8, 16, and 32,
  enforcing the envelope at every prefix from 2 through 32 with rigorous
  rational logarithm intervals.
- Best minimum-gap witness has
  `min G_m=103963/23658496>0.0043943`; best minimum-innovation witness has
  `min Q_00/N=743151/192790528>0.0038547`.
- Both 32-mark witnesses have 496 distinct positive differences from 496
  pairs and pass 31 of 31 prefix-envelope rows.
- Completeness is claimed only at four marks: 12,341 normalized candidates,
  1,672 compatible Golomb rulers, and exact maximum `G_4=3/448`.  The later
  extensions use deterministic beam search and are not optimality claims.
- These witnesses refute four-transition monotone-decay statements but imply
  nothing about infinite extension or the asymptotic `o(log J)` budget.
- Certificate internal hash:
  `36437444becc16c7520d0abe4c825dae13e9f7a01dbdaf9e30aa50ffe6fda81b`.
- An independent Decimal/Fraction oracle recomputed all 31 caps, all 496
  differences, every displayed `G` and `Q` value, both difference-list hashes,
  and the complete four-mark optimum.  No mismatch was found.
- The full certificate generator produced byte-identical JSON under Python
  3.13.13 and 3.14.6.  This verifies those two environments only.

### Focused primary-literature delta

- Re-read O'Bryant `2606.28651v3`, especially Lemma 9.  Its explicit
  two-block gluing deletes at most `g*binom(|V|,2)` new marks and becomes
  efficient only through cubic construction-scale jumps; it does not preserve
  an all-prefix critical envelope.
- Checked Ma--Yi `2608.13739v1`: its sharp almost-covering threshold concerns
  disjoint internal difference spectra of separate finite rulers and omits all
  cross-block mark differences.
- Kept Alexeev--Mixon `2510.19804v2` directions separate: finite cyclic
  non-extension, qualitative completion of every finite Sidon set to an
  infinite PDS, and failure for arbitrary already-infinite Sidon sets are
  distinct claims.  None is quantitative enough for #1191.
- Audited current finite smoothing, PDF/PSDS, entropy, consecutive-sum,
  near-extremal rigidity, and infinite-basis papers.  No source in the focused
  accessible corpus proves the required innovation budget.
- Access limits: parts of Semantic Scholar and the arXiv export API returned
  HTTP 429; a publisher page later returned 403; newest OpenAlex counts showed
  indexing lag.  The result is a qualified null, not an absence theorem.
- Full source statements and links are in
  `research_sources/LITERATURE_DELTA_GLOBAL_HISTORY_2026-08-28.md`.

### Wave 4 current bottleneck

The strongest surviving target is a flat-profile versus profile-reset
amortization across different epochs of one globally critical Sidon history.
Small same-lag oscillation must overflow cross-difference bands; large
oscillation creates a reset.  The missing theorem is that such resets cannot
renew independently forever, with a cross-epoch charge totaling `o(log J)`
and controlling the adjoint-weighted actual innovations.  Q1 and Q2 remain
unresolved.

## Anti-Eulerian continuation — Wave 5 (2026-08-28)

### Exact cross-epoch structure

- Proved the arbitrary-epoch chord identity
  `e_M(r)-(r/m)e_M(m)=(N_m/N_M)e_m(r)` for `r<=m`, preserving the rank
  location and sign of old non-affine curvature after chord subtraction.
- Derived the arbitrary-`q` covariance update with
  `B_q=((q^-2,(q-1)q^-2),(0,q^-1))` and an exact PSD shell/mixture
  innovation.
- Strengthened the global block-packing reset to a signed statement:
  `q-1>=4K log m` implies `e_M(m)<=-1/(2q)`.
- Proved that one dyadic endpoint-flat run lasts only `O(log log m)`
  generations and obtained an exact conditional amortization by the upward
  variation of `log(N_(2^j)/4^j)`.

### Profile-only reset amortization no-go

- Constructed one infinite positive-integer sawtooth gap profile satisfying
  dyadic `C=1`, the all-prefix bound `N_n<12n^2 log n`, scalar difference
  capacity, and the exact PSD covariance recursion.
- Its reset count and endpoint-reset magnitude are `o(J)`, while every step
  has `Q_00/N>=1/2048`; hence its innovation sum is linear.
- The example is explicitly non-Sidon: at four marks the gaps
  `(1,3,14,14)` repeat difference 14.  It refutes profile/reset/PSD-only
  arguments but leaves full contiguous-sum uniqueness as the exact missing
  arithmetic input.
- A separate read-only adversarial audit rederived the chord, reset, flat-run,
  sawtooth, envelope, and exact innovation formulas and found no material
  mathematical error.  Two presentation gaps were tightened in the proof.

### Certified 64-mark nested extension

- Authenticated the Wave 4 parent certificate, then extended all four retained
  32-mark roots to 64 marks with deterministic beam search under one `C=1`
  envelope at every prefix.
- Six retained 64-mark witnesses each have 2,016 distinct positive
  differences and pass all 63 prefix-envelope checks.
- The best innovation witness keeps
  `min Q_00/N=100987452359053759/26579439869661020160>0.0037994` over five
  dyadic transitions and latest signed reset persistence above `0.6587`.
- The best persistence witness exceeds `0.7113`, with final innovation above
  `0.0025070`.
- The extension is heuristic; no optimum, 128-mark extension, infinite
  extension, or asymptotic conclusion is claimed.  Certificate internal hash:
  `a26c13574002eb442731bcbec465a5fa7553a25728e2225ddba942e6df4d3ceb`.

### Focused primary-literature delta

- Riblet--Schehr compactness gives a valid conditional diagonalization from
  uniformly bounded finite all-prefix towers at every depth to one infinite
  tower; it neither constructs those towers nor controls innovations.
- Kraft/antichain and infinite `K_(s,t)`-free graph theorems provide exact
  Carleson or block-amortization analogues but no Sidon-to-charge map.
- No checked primary source supplied the all-prefix critical tower or the
  required adjoint innovation budget.  This is a qualified null with access
  limits, recorded in
  `research_sources/LITERATURE_DELTA_CROSS_EPOCH_2026-08-28.md`.

### Wave 5 current bottleneck

The strongest surviving target is an arithmetic reset-renewal exclusion.
Repeated nearly uniform newborn shells must be charged across several
reset-to-flat cycles using uniqueness of **all** cross-epoch contiguous gap
sums.  The required charge must control the two exact terms of `Q_(m,M)` by
`o(log J)`.  Q1 and Q2 remain unresolved.

## Anti-Eulerian continuation — Wave 6 (2026-08-28)

### Exact arithmetic band ledger

- Partitioned all relevant differences by dyadic birth epoch, category, and
  rank lag.  For any integer interval, the demand of every selected family
  whose hull is contained in it is at most its inclusive integer capacity;
  hence the universal Hall pressure is at most one.
- Proved exact common-band inequalities for newborn shells and old--new
  anti-diagonals across every available epoch in one prefix.
- With `H_m=D_m^-+D_m^+`, `M_m=max(mu_m^-,mu_m^+)`, and
  `tau_(m,k)=H_m+kM_m`, proved
  `sum_m R_m(T)(R_m(T)+1)/2<=floor(T)` and integrated it to
  `sum_(tau<=X) k/tau<=1+log X`.  At exponent `1+epsilon`, the total is at
  most `(1+epsilon)/epsilon`.
- The epsilon-zero endpoint remains logarithmic.  This is exact global
  history, including the monotone limit along one infinite ruler, but it is
  not the required `o(log J)` upper budget.

### Exact finite obstructions and witnesses

- The sixteen-mark C=1 ruler
  `(0,1,18,34,79,127,171,218,319,415,509,613,710,808,903,1002)` has 120
  distinct differences, all 15 prefix caps, three nearly uniform newborn
  shells, three signed resets at most `-1/4`, and normalized innovations above
  `1/600`.  Three reset cycles do not force collision.
- A separate deterministic but non-exhaustive beam reached 128 marks.  The
  exact post-search audit found final mark 136,282, all 8,128 differences
  distinct, and all 127 prefix C=1 rows passing.  The certificate internal
  hash is
  `16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a`.
- The 22 retained arithmetic-mining transition rows exhibited the empirical
  candidate `16n Lambda_NN^2<=1`, but an independent targeted probe refuted it.
  One 64-mark C=1 Golomb ruler violates the candidate at three consecutive
  transitions, with `Lambda=9/14,17/28,45/118` and scaled values
  `2592/49,4624/49,259200/3481`.  All 2,016 differences and all 63 prefix rows
  pass exact audits.  The two discovery beams expanded 528,317 and 39,716
  states and were not exhaustive.  Certificate internal hash:
  `f77dea81744dd894a194436fffbbdc28ff0d0a0265df38be8baa0bff95844d49`.

### Forbidden-shadow route closed

- For every normalized Golomb ruler `B` and `L>=3`, proved that
  `A_L(B)={0,1,Lb_1,...}` is Golomb with exact difference decomposition
  `{1} dotcup L Delta(B) dotcup {Lb_j-1}`.
- Its one-point forbidden shadow occupies at most four residue classes modulo
  `L`, and every interval of `H` consecutive integers contains at most
  `4 ceil(H/L)` shadow points.
- Growing compatible finite windows retain innovation `1/360+o(1)` per
  transition while their total actual extension-band shadow density is
  `o(1)`.  This rules out a universal local-shadow-density charge.  The ruler
  family changes with terminal scale and is not one infinite counterexample.

### Wave 6 literature boundary

- Firecrawl, Exa, SciSpace, ordinary search, and primary arXiv pages were used
  to check disjoint difference packings, `A+A-A` shadows, and
  Singer/finite-field nesting.  Ma--Yi's finite packing theorem omits the
  mixed differences created by a union; the other checked adjacent results do
  not supply a compatible ordered-prefix integer tower.
- Consensus returned no evidence because its monthly quota was exhausted at
  30/30, with reset reported for 2026-09-01.
- No checked source in this bounded delta supplied a compatible critical
  all-prefix tower or the missing endpoint band-renewal theorem.  This is a
  qualified null, not an absence, novelty, or priority claim.

### Verification and release closure

- Shared pytest from `core_workspace/endpoint_variance`:
  `/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python -m pytest -q -p no:cacheprovider`
  passed 133 tests and 42 subtests with zero failures.
- Ruff 0.12.12 passed all 24 selected Wave 4--6 continuation sources.  A
  package-wide run also exposed four pre-existing legacy style findings, so no
  package-wide lint claim is made.
- The first complete release command
  `ERDOS1191_PYTHON=/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python ./integrity/run_all_checks.sh`
  passed package verification, the full test suite, all 42,615 original exact
  checks, and byte-for-byte regeneration of every dated continuation
  certificate, including both Wave 6 beams.
- The provisional package check initially stopped only because `.pytest_cache`,
  `.ruff_cache`, and `__pycache__` existed.  They were moved, recoverably, to
  `/tmp/erdos1191-wave6-cache-quarantine.B3CUSb`; no research artifact was
  removed or modified by that cleanup.
- After this entry and `integrity/WAVE6_TEST_VERIFICATION_2026-08-28.json` are
  sealed, the release procedure performs a second complete immutable rerun,
  then verifies a relocated staging copy and an independently extracted final
  ZIP.  Those post-seal commands do not edit the canonical research state.

### Wave 6 current bottleneck

The single surviving target is a global band-renewal self-improvement for one
infinite compatible critical Sidon sequence.  Old-history difference capacity
must prevent the active `R_m(T)` cutoffs from renewing through unboundedly many
fresh numerical bands and force
`sum_(j<=J) <H,Q_j/N_(2m_j)> = o(log J)`.  The exact endpoint ledger gives only
`O(log)`.  Q1 and Q2 remain unresolved, and no prize claim is ready.

## Anti-Eulerian continuation — Wave 7 complete birth renewal (2026-08-28)

### Complete birth spectrum and summable potential

- Extended the Wave 6 half-rhombus to every old--new lag `1<=k<2m` and added
  every newborn-internal lag family.  These families partition all pairs in a
  dyadic terminal prefix.
- Combined the exact thresholds with the universal rank floor
  `a_(i+ell)-a_i>=ell(ell+1)/2` to prove the wedge capacity ledger and
  `sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)` over one infinite Golomb history.
- The independent hostile audit verified the indices, band endpoints,
  covariance normalization, finite and asymptotic quantifiers.  It set
  `R(T)=0` on `0<=T<1` and narrowed the no-go prose to the proved affine
  class; no material theorem error was found.

### Exact affine bridge obstruction

- On the 512-mark `p=1423` E–T ruler, exact rational arithmetic gives
  `Q_(256),00/N_512>W_2(256)` with positive comparison cross-product
  `86781803501905775924014152122871`.
- Growing recent E–T windows have accumulated fixed-adjoint innovation
  `R/360+o(R)` while total complete-birth `W_2=o(1)`.  Hence no fixed-
  constant affine domination by this potential alone holds uniformly on
  finite critical windows.
- Defined the extension survival height `surv_C(P)`.  The finitely branching
  König argument proves that infinite height is equivalent to one infinite
  eventual-`C`-critical Golomb extension of the same prefix.  Changing E–T
  terminal roots do not certify this label.

### Exact renewal probes

- Refuted RH with the intervals `[21,22]` and `[382,383]`, and refuted HT at
  threshold 3 with exact margin `-1/6`.
- Proved EST for every normalized Golomb ruler through eight marks.  The
  cap-free forced-region replay covers 4,934 parents, 3,341,161 rulers, and
  37,423,576 nodes; the minimum possible `tau_(4,1)` in that region is 11.
- EST survives the authenticated 64/128-mark fixtures and 23 valid one-gap-
  swap variants, but those larger samples are not exhaustive.
- Proved the cheap-child-half lemma and isolated its overlap failure.  At
  `T=1198199/32` on the 128-mark witness, tax 120 produces only 57 genuinely
  new adjacent differences, leaving exact unpaid debt 63.

### Quantitative gluing limitation

- Specializing O'Bryant Lemma 9 to Sidon rulers, proved that using only its
  worst deletion guarantee to certify one survivor forces the first new
  prefix to jump by `Omega(n^4)`.  It cannot maintain any fixed critical
  envelope indefinitely; for `C=1`, all `n>=8` are obstructed.
- Constructed a sparse separated family showing the quadratic worst deletion
  count is sharp under Sidonness plus separation alone.  Structured low-
  conflict candidate blocks and new gluing schemes remain eligible.

### Wave 7 literature and plugin audit

- Scripted discovery retained 316 deduplicated records from 14 successful
  OpenAlex, Crossref, and arXiv rounds.  Selected mathematical statements were
  checked against primary text; lexical false positives were discarded.
- No checked source supplied both a compatible all-prefix critical tower and
  the cross-epoch innovation budget.  This is a qualified null only.
- Consensus was blocked at 30/30 monthly searches with reset 2026-09-01.
  SciSpace returned mostly adjacent work and one malformed duplicate;
  Firecrawl's final targeted search returned generic listings and was marked
  bad.
- Separately, Exa ran seven searches requesting 70 candidate results, and the
  Firecrawl research index ran three `k=12` searches (36 candidate records),
  with three records inspected and three question views.  These are discovery
  volumes, separate from the 316-record deduplicated scripted state. Discovery
  metadata was not used as theorem authority.

### Wave 7 current bottleneck

Prove an infinite-survival-conditioned debt-repayment theorem in one fixed
critical Golomb history.  Repeated old-cheap orientations must pay overlap
debt through unused non-adjacent differences or equivalent capacity, and the
resulting charge must dominate the actual covariance innovations strongly
enough to give `sum_(j<=J) <H,Q_(m_j)/N_(2m_j)> = o(log J)`.  Q2 remains the
secondary arbitrary-depth finite-feasibility plus König route.  Status:
`UNRESOLVED_AT_HARD_LIMIT`; no prize claim.

## Anti-Eulerian continuation — Wave 8 positive birth budget (2026-08-28)

### Actual-adjacent renewal

- Added the actual newborn internal-adjacent family to the Wave 6
  cross-antidiagonal integer ledger.  The selected endpoint pairs are globally
  disjoint, so cumulative active demand at every real threshold `T` is at most
  `floor(T)`.
- Proved `min(B_m^-,B_m^+)<=tau_(m,1)`.  Therefore the current newborn family
  is paid or all older adjacent ancestry is cleared.
- The correct history transition leaves at most one outstanding internal
  family.  A new-pay-only event retains, rather than erases, an older debt.
- Exact exclusive eight-mark witnesses and a 16-mark later-repayment witness
  were recorded.  On the authenticated 128-mark fixture both actual sides are
  paid at every audited epoch.

### Actual `Q_m` atom decomposition

- Derived exact pair formulas for the newborn covariance, rank-one mixture,
  and their signed sum on the common `2m` grid.
- Derived the rank-one Abel boundary fan.  Its second coordinate has no
  cancellation, so it cannot be discarded or absorbed into shell covariance.
- Converted the shell covariance to exact squared contiguous-difference atoms.
  Proved the complete sign classification: negative atoms are precisely the
  proper left-prefix and right-suffix fans; strict bulk atoms and the full
  span are positive.
- Proved automatic within-shell boundary-debt repayment.  Under the critical
  cap, the two negative adjacent endpoint atoms have globally finite dyadic
  sum; the artificial `h_0` boundary row also sums to at most `92/315`.
- The power-gap eight-mark witness proves positive non-adjacent bulk atoms are
  necessary.  The family `(0,D,3D,3D+1)` proves the rank-one term is not
  universally controlled by newborn covariance.

### Exact cross-epoch pair telescope

- Regrouped every positive birth pair with all later negative old-pair terms.
  Each net constant-`H` coefficient retains at least one half of its birth
  charge; under future modulus ratios at most `r`, it retains at least
  `1/(1+r)`.
- Globally,
  `B_H/2 <= sum_m <H,Q_m/N_(2m)> <= B_H`.
- Exact finite-horizon adjoints turn the same signed expression into the
  positive future `E`-energy tail.  Thus old-pair cancellation cannot supply
  the missing unbounded or little-o gain.
- The primary theorem target is now the positive birth budget
  `B_H(J)=o(log J)` on one infinite eventually critical Golomb branch.

### Survival/debt and density falsification

- Exact finite extension searches refuted certified rank-lag, global raw
  non-adjacent, and latest-shell repayment counts, including after actual
  renewal leaves a single outstanding family.
- Exhausted all 1,672 four-mark all-prefix-`C=1` rulers: among 3,344 activation
  events, 601 refute the literal local `U_global/T>=I_m` inequality.  The
  minimum witness is `(0,1,4,6)`.
- Found a genuine `C=1` old-clear/new-unpaid latest-shell counterexample
  `(0,4,5,7,78,86,166,199)`.  Its global reservoir still has positive margin.
- The global `m>=4` version had no failure in the retained eight- and
  sixteen-mark samples, but remains finite evidence only.
- Independently reconstructed the reported 682-mark modified-greedy fixture.
  All 232,221 differences and all 510 activations through `m=256` were checked;
  the global and exploratory square margins were positive.  The working
  envelope holds only through index 680 and fails at 681, so no infinite
  construction is inferred.

### Hegyvári bridge audit

- Read the 1986 primary article and rederived its finite parabola ruler, affine
  variants, and exact finite upper-counting inequality.
- Proved that separated splicing of finite rulers is possible exactly when
  their internal positive-difference spectra are disjoint, with an explicit
  safe shift.
- Every finite old ruler can be spliced to a sufficiently gap-translated
  Hegyvári block, but the unconditional endpoint bound becomes cubic at the
  critical scale and violates intermediate prefix caps.
- Every full affine block has a rigid universal-difference skeleton.  A finite
  menu can therefore be blocked by embedding its universal spans in an old
  Golomb ruler.  Deterministic small searches confirmed both incompatible and
  compatible two-block cases without making an asymptotic claim.

### Wave 8 literature and plugin audit

- Used the `scholar-deep-research` workflow with 22 OpenAlex/Crossref/arXiv
  rounds and retained 550 deduplicated records.  Exa, Firecrawl, SciSpace, and
  Consensus were also exercised; Consensus remained quota-blocked, and all
  source/tool limitations were logged.
- Primary screening found no theorem satisfying the survival, orientation,
  repayment, actual-covariance, and sublogarithmic requirements together.
- Ruzsa's small maximal Sidon sets show that raw unused-difference capacity is
  not a legal-extension certificate.  Greedy prescribed-prefix continuation
  gives only `M+O(n^3)`.  Infinite survival may be a one-ray tree with
  branching number one.  Existing hypergraph and Carleson theorems require
  precisely the regularity or testing estimate still missing here.
- This is a qualified search boundary, not a novelty or nonexistence proof.

### Wave 8 verification boundary

- The shared endpoint-variance suite after all additions reports
  `210 passed, 42 subtests passed`.
- New Wave 8 focused suites cover actual renewal, atom decomposition, combined
  certificates, survival probes, density candidates, Hegyvári splicing, and
  pair telescoping with exact integer or `Fraction` arithmetic.
- Three dated Wave 8 JSON certificates regenerate byte-for-byte.  The 682-mark
  fixture is reconstructed deterministically inside the test suite and is not
  stored as an unverified external payload.
- Ruff check and format verification pass the selected Wave 8 Python sources.
- All finite calculations remain falsification/certificate evidence.  The
  infinite theorem and the prize claim remain open.

## Anti-Eulerian continuation — Wave 9 rank variance and primitive spectrum (2026-08-29)

### Exact scalar reduction and the new contradiction boundary

- Rewrote the positive pair-birth budget in terms of the normalized adjacent-
  gap measure `nu_n=N_n^(-1) sum_(i<n) h_i delta_(i/n)` and its positional
  variance `V_n=Var_(nu_n)(u)`.
- The shell secant constants give the exact global comparison
  `(4/49) sum_(k=1)^(J+1)V_(2^k) <= B_H(J) <=
  (36/35) sum_(k=1)^(J+1)V_(2^k)`.  Thus P15 is equivalent up to explicit
  constants to `sum_(k<=J)V_(2^k)=o(log J)`.
- Distinct genuine adjacent gaps imply `V_n>=n^2/(512N_n)` for `n>=8`.
  Under `N_n<=2Cn^2 log n`, the same sum is at least
  `(6272 C log 2)^(-1)log J+O_C(1)`.  This lower barrier is rigorous but does
  not give the missing upper bound.
- Short-rank atoms and atoms with a small endpoint gap have cumulative cost
  `O(log log J)`.  The remaining long-rank, two-large-endpoint core has exact
  four-parameter rank/end-gap/magnitude capacity bounds.  Scaled
  Erdős--Turán windows show that local numerical density alone cannot make
  this core vanish.

### Weighted primitive cross-ratio state

- For every genuine non-adjacent pair, introduced
  `C_ij=log((M+h_i)(M+h_j)/(M(M+h_i+h_j)))`, which exactly majorizes
  `h_i h_j/(M+h_i+h_j)^2`.
- Derived the complete Abel coefficient spectrum, including every boundary;
  after multiplying by `n^2`, the positive and negative masses both equal
  `2(n-2)^2`.
- With `h_n^circ=min(h_2,...,h_(n-2))`,
  `delta_n^circ=gcd(h_2,...,h_(n-2))`, and `q=h_n^circ/delta_n^circ`, proved
  the shifted-factorial spectrum bound.  It dominates the gcd-only bound and
  is scale invariant.  The strict-interior gcd stabilizes on a fixed branch,
  but the resulting critical estimate still does not sum to P15.
- Derived exact retained and unretained dyadic recursions.  A scalar
  reweighting that cancels the retained state would require weights growing
  by more than four per epoch.  A scaled Erdős--Turán family also gives the
  local obstruction `X_(L/2)>=1/4096`.

### Complete finite falsification probe

- Exhausted all 1,672 normalized four-mark all-prefix-`C=1` Golomb rulers and
  all 1,468 normalized eight-mark Golomb rulers with terminal mark at most 40;
  1,146 of the latter satisfy every `C=1` prefix cap.
- The pointwise candidate `Delta B_(2m)<=Delta B_m` fails in 128 cases.  The
  minimum-diameter witness is `(0,4,12,13,19,30,33,35)` with exact margin
  `446533/341397504`.
- The literal harmonic schedule fails for all 1,146 bounded `C=1` rulers.
  Static one-atom and occupancy-at-most-rank-lower cell injections already
  fail at `(0,1,4,6)`.
- On the 512-mark modified-greedy and Erdős--Turán fixtures, the latest
  macroscopic long-rank core shares are respectively about `0.642208` and
  `0.665560`; the required static overlap constants are `553/4` and `647/2`.
  These are finite obstructions only and do not infer infinite survival.
- The deterministic certificate internal hash is
  `62ae7c48c70604e9f1ee3dcf2d3273a326825d75d42a59be7f517f6e16f992f8`;
  its JSON byte hash is
  `de8d8cebb3d75d132c9c693d2a42ff52019219bc02bc775a71c51e952c444c86`.

### Wave 9 primary literature and plugin audit

- The scripted state now contains 750 deduplicated records from 31 query
  rounds.  Exa reviewed 30 result slots and was strongest for Ma--Yi and
  O'Bryant.  Firecrawl's three fresh paper searches returned empty, while its
  known-record inspection successfully resolved the current Ma--Yi and
  O'Bryant arXiv versions.  SciSpace was mostly adjacent.  Consensus was
  quota-blocked at 30 monthly searches and reported a 2026-09-01 reset.
- Primary pages were checked rather than treating discovery summaries as
  authority: Ma--Yi Theorem 4.1, Shearer's official EJC article, and
  O'Bryant arXiv:2606.28651v3.
- The extracted W9-RLP inequality is hereditary over every finite epoch subset
  on one nested branch.  If `1<=q_m<=m`, `M_E=sum_(m in E)m q_m`, then
  `M_E(M_E+1)/2 <= sum_(m in E)N_(2m)q_m(q_m+1)/2`.
  It is only linear and supplies neither the product weight nor the kernel
  needed for P15.  The mechanical saturation gate remains false, so the
  literature conclusion is a qualified null.

### Wave 9 verification boundary

- The combined Wave 9 focused suite passed 21 tests.  The full shared suite
  passed `231 tests and 42 subtests` in the pre-release run.
- The shifted cross-ratio bound passed 1,302 exhaustive small Golomb fixtures;
  exact shell maps passed through `n=100`, and 700 recursion fixtures passed.
- Ruff 0.16.5 check and format verification passed for the six selected Wave 9
  source/test files.  The first complete release runner passed the 243-file
  self-excluding manifest, `231 tests and 42 subtests`, all legacy exact checks,
  byte-identical replay of every dated certificate through Wave 9, and the
  closing manifest verification.
- P15, Question 1, and Question 2 remain unresolved.  The single next theorem
  is a survival-conditioned laminar weighted incomplete-difference-triangle
  non-saturation inequality combining W9-RLP, the exact tiles, and primitive
  Abel signs on one fixed infinite critical branch.

## Anti-Eulerian continuation — Wave 10 laminar log-product and frontier phase (2026-08-29)

### Analytic advances

- Proved the arbitrary-weight hereditary incomplete-DTS inequality
  `sum r beta_r <= sum lambda*d <= sum N_(2m)Gamma_m`.  Its unit
  lag-rectangle specialization is W9-RLP.
- Proved hereditary factorial/product packing for selected dyadic birth
  differences and the exact weighted rearrangement inequality after clearing
  rational denominators.
- Proved the cut-kernel theorem
  `sum_(i<j,i<=t<=j) h_i h_j/D_(i,j) <= (log2+1/e)a_g`.
  Therefore every fixed old gap position has a future dyadic load bounded by
  `(4/3)(log2+1/e)4^(-K)`.  This localizes any obstruction to the moving
  frontier but does not give a global little-o.
- Classified the complete dyadic cross-ratio Abel shell.  The negative
  non-full bulk has right endpoints `[m-1,2m-2]`, disjoint across dyadic
  epochs, so one global weighted log-product inequality applies to every
  finite epoch set.
- Proved the uniform global spectrum law
  `F_E=(7/4)sum_(m in E)log m+O(|E|)`.  The exposed signs plus global
  distinct-positive-integer information still leave a leading
  `(1/4)sum log m` deficit and secondary `log log` slack.  For consecutive
  dyadic epochs the displayed certificate has leading term
  `(log2/8)J^2`; this is a proof-method obstruction, not the actual shell
  asymptotic.

### Exact finite LP and adversarial audit

- Exhausted W9-RLP over every epoch subset and every legal cutoff through 128
  marks by exact DP: 9,845,549 selection vectors and zero violations.
- Solved every support-conditioned tile block by an exact greedy primal and
  threshold dual.  On the 512-mark scaled E--T fixture there are 129,795
  genuine nonadjacent atoms, 204 support variables, 62 tile keys, zero
  capacity violations, and LP/actual fixed-`H` ratio about `363.799`.
- Proved the zero-column theorem: after prefix moduli are fixed, every
  existing W9-RLP row contains no tile occupancy variable, so simple row
  concatenation cannot change the LP optimum.
- The dilation family `(0,s,4s,6s)`, `s=1,...,4`, has increasing raw RLP
  slack and increasing retained objective.  Raw slack alone is not a damping
  term.
- An independent adversarial audit checked shell coefficients for all even
  counts 8 through 200, the multiset and mass formulas, HLP/rearrangement
  directions, the `7/4` Stirling main term, the global threshold proof, the
  `1/4` deficit, and the `(log2/8)J^2` coefficient.  Verdict: accepted with
  scope limited to the plain distinct-integer Abel-spectrum method.

### Wave 10 primary literature and plugin audit

- Exa: 10 searches and 100 reviewed result slots; selected primary pages
  fetched and official metadata used.
- Firecrawl: five searches and 75 result slots, plus 15 returned related-paper
  slots; known records inspected/read by canonical IDs.
- SciSpace: three searches and 30 result slots, discovery only.
- Consensus: two attempts both quota-blocked; reset reported as 2026-09-01.
- The closest positive results are full bi-/tri-tree tensor-product
  box-to-embedding theorems (arXiv:1906.11150 Theorem 2.3 and
  arXiv:2001.02373 Theorem 1.3).  The P15 positive-measure encoding and a
  vanishing box estimate remain unproved.
- The pruned-bi-tree counterexample and `T^4` proof-method obstruction rule out
  naive pruning/direct extension, with their exact scopes preserved.  Ding's
  2026 rank-weighted theorem is too weak at P15 density and controls the wrong
  moment.
- Targeted interfaces converged; overall saturation remains false.  This is a
  qualified null, not an absence or novelty theorem.

### Wave 10 verification boundary and next theorem

- The focused Wave 10 suite passes 30 tests; Ruff check and format are clean
  when run from `core_workspace/endpoint_variance`.
- The Wave 10 finite LP certificate regenerates byte-identically.  Its internal
  SHA-256 is
  `3434372738c33fa59a2b3ea8085e4dc06878f9d260c22fb853b09b1cb3092095`.
- The first complete Wave 10 release runner passed the 260-file self-excluding
  manifest, 261 tests plus 42 subtests, all legacy exact checks, byte-identical
  replay of every dated certificate through Wave 10, and the closing manifest
  verification.
- No finite fixture or DP state is promoted to `surv_C=infinity`.
- The exact obligation remains P15.  One sufficient next route combines the
  actual bulk premium with exact positive-boundary slack so the Abel repayment
  leaves `o(log J)`; a stronger lower-shell-only payment needs a global floor-
  allocation lemma.  A separate sufficient route is a full bi-/tri-tree tensor
  encoding with summably vanishing one-box constants.  The routes are not
  proved equivalent or necessary, but each must couple endpoint-product/Abel
  variables and rank-lag/survival data with nonzero coefficients.
- P15, Question 1, Question 2, and the prize claim remain unresolved.  Status:
  `UNRESOLVED_AT_HARD_LIMIT`.

## Anti-Eulerian continuation — Wave 11 triangular repayment (2026-08-29)

### Universal triangular floor

- `[RIGOROUS — SELF-CONTAINED]` Every interval difference made from `ell`
  adjacent gaps obeys `D_(p,q)>=binom(ell+1,2)`, because the adjacent gaps are
  pairwise distinct positive integers.
- Applying the exact Abel weights gives
  `K_m^low=(1/2)log m+O(1)`, `K_m^int=(3/2)log m+O(1)`, and
  `K_m^len=2log m+O(1)`.  Hence the Wave 10 leading-quarter deficit is fully
  repaid: `K_E^len-F_E=(1/4)sum log m+O(|E|)`.
- A separate `K^mix` certificate uses the length floor only on the lower shell
  and global rearrangement only on `q>=m`.  It has the same main term and is
  kept disjoint from `K^len`.

### Exact positive decomposition and surviving order

- `[RIGOROUS — SELF-CONTAINED]` With
  `G_m^len=A_m-K_m^len>=0`, the local identity is
  `T_m-K_m^len=Y_m+G_m^len+S_m`, and all three channels on the right are
  nonnegative.  The cumulative form is
  `sum Y=(T-K^len)-(G^len+S)`.
- The complete dyadic bulk bands tile one consecutive triangle.  Actual
  numerical holes, coefficient/rank permutation, containment ranks, and
  boundary slack have exact nonnegative decompositions.
- `[CONDITIONAL]` On one fixed eventual-`C` branch, the direct envelope is now
  `O_C(J log J)` instead of the Wave 10 displayed `O_C(J^2)`.  This remains
  much larger than the required `o(log J)`.

### Exact tail and finite falsification

- `[RIGOROUS — SELF-CONTAINED]` The lower residual is exactly a positive
  future cross-ratio tail.  A fixed pair has dyadic overlap
  `Theta(log(j/i))`, refuting uniform same-pair charging to its single birth
  atom.
- `[COMPUTATIONAL — CERTIFIED FINITE]` The Wave 11 certificate verifies all
  formal-log identities and finite-horizon telescopes, authenticates the
  64/128/512 fixtures and the 682-mark reconstruction through 512, and
  exhausts all 1,146 eight-mark all-prefix-`C=1` rulers.
- Bulk-only, boundary-only, all-hole-only, lower-hole-quarter, and literal
  zero-residual candidates fail in all 1,146 cases.  They share the
  minimum-terminal/lexicographic witness `(0,1,4,9,15,22,32,34)`; these are
  bounded-scope no-gos only.
- A normalized harmonic candidate has no failure in that finite scope, with
  minimum numerical margin about `0.210336`, but it has no infinite proof.
  Changing Erdős--Turán rulers retain a positive residual ratio through
  `m=1024`; no changing family is promoted to `surv_C=infinity`.

### Wave 11 primary-source and plugin audit

- The scholar spine logged 26 successful requests and 351 deduplicated
  papers.  Exa used 18 searches/180 result slots; Firecrawl used 8 searches,
  3 related calls, 4 inspections and 6 reads; SciSpace used 4 searches/40
  slots; Consensus was quota-blocked at 30/30 until 2026-09-01.
- Beck--Bogart--Pham provides the exact gap-vector/consecutive-sum language.
  Beker and RSSS give finite energy/sumset results but not nested survival;
  RSSS Example 2 blocks adjacent-gap-only energy stability.  O'Bryant gives
  Abel and separated-extension templates in the wrong state.
- The shifted-factorial improvement within each length class is only
  `O(m^(-1/2))` per shell and therefore `O(1)` over dyadic epochs.  The 2025
  Carter--Hunter--O'Bryant theorem gives
  `log diam>=2log m-O(m^(-1/2))`; this order is its subleading correction, and
  the total-diameter scalar has no cross-length/survival state.  One-tree
  Carleson results clarify the vanishing/Dini endpoint but do not supply a
  product-tree encoding.
- Overall saturation is false.  The logged conclusion is a qualified targeted
  null, not an absence or novelty claim.

### Verification boundary and next theorem

- The focused Wave 11 suite independently passed 7 tests in 47.85 seconds.
  Source, test, analytic memo, computation memo, and certificate hashes agree
  with the sealed records; the certificate internal digest is
  `1e9eb7627991687a22b1abf0cb36c52a876846d203374d830f545ddfb44d220b`.
- The exact next obligation is P17: on one fixed infinite eventually critical
  branch prove
  `G_J^len+S_J>=T_J-K_J^len-epsilon_J` with
  `epsilon_J=o(log J)`, equivalently `sum Y_m=o(log J)`.
- P15, P17, Question 1, Question 2, and the prize claim remain unresolved.
  Status: `UNRESOLVED_AT_HARD_LIMIT`.

### Wave 11 integrated release closure

- The final canonical tree contains 276 inventory files and a 275-entry
  self-excluding SHA-256 manifest.
- The complete package runner passes 268 pytest tests and 42 pytest subtests,
  every dated certificate through Wave 11 regenerates byte-identically, and
  the closing manifest verification passes.
- The final ZIP passes `unzip -t`; an independent extraction passes the
  package manifest and the complete runner with the same 268/42 counts.
- These are reproducibility results only.  They do not promote the finite
  searches, changing families, or literature audit to an infinite theorem.

## Progress 2026-08-29 (Wave 12: cut renewal and integer packing)

### Exact mathematical advance

- `[RIGOROUS — SELF-CONTAINED]` Defined the Wave 11 cut tail `R_m` and four
  explicit nonnegative sectors `Z_m^ob`, `Z_m^nb`, `Z_m^of`, and `Z_m^mf`.
  Coefficientwise comparison proves
  `Y_m=R_m-R_(2m)+Z_m` and hence the dyadic telescope
  `sum Y_m=R_4-R_(2^(J+1))+sum Z_m`.
- Each fixed pair has a uniformly summable total `Z` coefficient: the old
  future coefficient is at most `i/(4m)`, the middle-future sector crosses
  only boundedly many dyadic cuts, and each birth sector occurs once.  This
  repairs the Wave 11 same-pair `Theta(log(j/i))` obstruction.
- The remaining problem is across **different** integer pairs.  The sufficient
  P18 target is `sum_(m in E_J)Z_m=o_C(log J)` on one fixed infinite
  eventually-critical integer Golomb branch.

### Two exact boundary theorems

- `[RIGOROUS — SELF-CONTAINED]` The floor combining all numerical ranks,
  triangular length floors, and the complete interval-containment partial
  order improves `K^len` by less than `5` per epoch.  This closes that whole
  independent-ordering strategy for secondary repayment, without excluding
  crossing additive relations or survival coupling.
- `[RIGOROUS — SELF-CONTAINED]` The real ruler
  `a_n=n^2+sqrt(2)n` has all positive differences distinct and quadratic
  growth, yet `Y_m -> (3/2)(log 2-1/2)>0`.  It is not an integer
  counterexample to #1191.  It proves that any successful P18 proof must use
  integer unit spacing or a genuinely equivalent arithmetic property.

### Exact finite verification

- `wave12_cut_renewal_probe.py` implements independent rational-coefficient
  and formal-log oracles, four-sector sign checks, a containment-poset witness,
  theorem-level gain caps, and a labelled floating real-model calibration.
- Seven focused tests pass.  The deterministic certificate covers all 1,146
  bounded eight-mark all-prefix-`C=1` rulers, the authenticated 64-mark
  fixture, an independent 128-mark ruler, and 32,130 containment atoms.
- Internal payload digest:
  `fe0fd30cccaf2717d4c7dd2306772bc7dbcaea9bacf2b641d8e685d4999894a4`.
  Final certificate SHA-256:
  `e5645101d5150910de428b7184d504b1a9b90ac411c1b007be743e43e65aecc9`.
  These checks certify finite algebra only.

### Four-connector primary-source delta

- Exa, Firecrawl's paper index and publisher scraper, SciSpace, Consensus,
  and the arXiv MCP were used.  Consensus remained quota-blocked and supplied
  no evidence.
- Martikainen `arXiv:2608.22628` proves a critical two-depth Journé packing
  theorem and a Zygmund-boundary analogue.  It is a sharp Route B geometric
  template, but contains no Sidon ray, `C_(i,j)` encoding, or arithmetic box
  decay.
- Chen--Fang, DOI `10.1016/j.jcta.2026.106239`, shadows the counting function
  of any supplied Sidon set by a perfect difference set.  Its construction
  deletes input elements and inserts new ones, so it is not prescribed-prefix
  survival; it also preserves rather than improves the input density exponent.
- No checked source proves P18.  This is a qualified null, not an absence or
  novelty claim.

### Current claim boundary

- P15, P17, P18, Questions 1 and 2, and the prize claim remain unresolved.
  Status: `UNRESOLVED_AT_HARD_LIMIT`.

### Wave 12 integrated release closure

- The final canonical tree contains 295 inventory files and a 294-entry
  self-excluding SHA-256 manifest.
- The complete package runner passes 275 pytest tests and 54 pytest subtests,
  every dated certificate through Wave 12 regenerates byte-identically, and
  the closing manifest verification passes.
- The Wave 12 ZIP passes `unzip -t`; an independent extraction passes the
  package manifest and the complete runner with the same 275/54 counts.
- These are reproducibility results only.  They do not promote finite rulers,
  a real noninteger adversary, or the qualified literature audit to a solution.

## Progress 2026-08-29 (Waves 13--15: harmonic barrier and rank promotion)

### Wave 13 integer obstruction and frontier spectrum

- `[RIGOROUS — SELF-CONTAINED]` For
  `H_m=a_(2m-1)-a_(m-2)` and
  `E_m=m(m-2)(m^2+8m+6)/48`, the integer new-birth subtriangle satisfies
  `Y_m,Z_m>=Z_m^nb>=E_m/(8m^2H_m)>=m^2/(384H_m)`.
- A hypothetical eventual-`C` branch would therefore have harmonic lower
  bounds for both dyadic sums.  The universal-over-all-`C` P17 and P18
  assertions are consequently each logically equivalent to Question 1,
  not easier regularity lemmas.
- The exact finite spectrum
  `Z=mathfrak P+mathfrak U-mathfrak B-mathfrak F-mathfrak e` reduces the
  within-epoch frontier to `X=mathfrak U-mathfrak B` up to a dyadically
  summable one-sided error.  The same branch hypothesis forces
  `sum X>=(1536C log2)^(-1)log J-O_(C,a)(1)`.
- The lattice-cell identity and fixed-rank central-path theorem were proved,
  while literal occupancy-one, central-hole, and unweighted adjacent-rank
  charges were rejected by exact finite witnesses.

### Wave 14 cap-dependent future-rank promotion

- `[RIGOROUS — SELF-CONTAINED]` Spatial bins in
  `N=floor(d/log(d)^2)` future marks prove
  `rho_infinity(d)-rho_L(d)>=d/(64C log d)` under explicit floor-safe
  eventual-cap conditions.
- For macroscopic Wave 13 suffix atoms this gives a harmonic log-rank
  promotion.  The `u`-weighted resource is at least
  `1/(1024C log m)` with the displayed safe constants.
- The same suffix atom reappears in the next Wave 11 lower shell with
  `v_(m,p)=(4m-2p+1)/(16m^2)`.  Its four-channel rank/hole split proves the
  legal disjoint floor `A_J>=K_J^star+Phi_(J-1)`.
- The sharper asymptotic rebate is
  `Phi_m>=(3/2048-o_C(1))/(C log m)`.  This is a lower bound on a legal
  negative-floor component, not an upper bound for `Y`, `Z`, or `X`.
- The exact still-unallocated macroscopic coefficient is
  `u-v=(4m-2p-3)/(8m^2)`, with total mass tending to `3/8`.

### Wave 15 adjacent-epoch allocation

- `[RIGOROUS — SELF-CONTAINED]` In the immediately following block,
  `K_p=rho_(4m-1)(d_(m,p))-rho_(2m)(d_(m,p))
  >=d_(m,p)/(128C log(8m))` eventually.
- Every counted new difference is a literal Gothic `mathfrak B_(2m)` atom.
  The total load created by all nested suffix thresholds on one numerical
  difference is below `3/(4m^2)`.
- Thus the marginal promotion
  `Delta_m=sum u_(m,p)log(1+K_p/r_p)` satisfies
  `1/(512C log(8m))<=Delta_m<=mathfrak B_(2m)+O(m^-2)`.
- This allocation spends the selected bulk atoms' full values; it is not a
  disjoint premium over the existing rank/length floors.  A dyadic shift
  leaves a terminal `Theta(J)` suffix fan, and later-birth allocations face
  a `4^k` coefficient mismatch.
- Finite Hall-64 and Erdős--Turán-128 checks validate the marginal mechanism
  and give explicit failures of the invalid raw-`u log d` equal-share charge.

### Certified scope and current boundary

- The Wave 13 and Wave 14 deterministic certificates replay the exact finite
  algebra and coefficient identities.  The Wave 15 certificate records the
  local layer-cake allocation and raw-charge counterchecks.
- All certificate scope flags remain negative for an infinite critical
  branch, a global signed allocation, either Erdős question, and prize
  readiness.
- The exact next theorem is a disjoint floor-plus-promotion inequality with a
  terminal potential, or an all-epoch bounded-overlap birth-time allocation
  for the residual `u-v` channel.
- P15, P17, P18, P19, Questions 1 and 2, and the prize claim remain
  unresolved.  Status: `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-29 (Wave 16: constant-fraction promotion and terminal repair)

### Multiscale future-rank filling

- Reused the Wave 14 half-open-bin count on the disjoint blocks
  `[2^tL,2^(t+1)L)` for
  `0<=t<=floor((log_2L)/2)`.
- Under `d>=L^2/8` and the explicit eventual-cap side condition
  `sqrt(L)>=128C log(4L^(3/2))`, every block creates more than
  `d/(64C log L)` distinct differences below `d`.
- Global Golomb uniqueness makes the witness sets disjoint across blocks and
  from the old prefix, proving
  `rho_infinity(d)-rho_L(d)>d/(128C log2)`.
- For the macroscopic suffix fan this gives the constant promotion
  `kappa_C=log(1+1/(128C log2))`, hence
  `Phi_m>=kappa_C/6` and residual `u-v` resource at least `kappa_C/3`
  eventually.  The eventual-hole logarithm is uniformly `O_C(1)`.
- The deterministic certificate checks exact finite block counts,
  cross-block/old-prefix disjointness, and rank increments on Hall-64 and
  Erdős--Turán-128.  Its large numerical constant-chain row is conditional
  and explicitly does not infer a branch.

### Exact terminal potential

- Expanded the next renewal cut exactly:
  `R_(2m)=c_m log A-sum_p v_(m,p)log d_(m,p)-mathfrak e_m`.
- Verified the checksum
  `U_m+V_m=F_m+c_m=(m-1)^2/m^2` and defined
  `mathcal T_m=mathfrak F_m+mathfrak e_m+R_(2m)-mathfrak U_m>=0`.
- Obtained the exact identity
  `Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`.
- Rowwise prefix/descendant mass equality plus the interior triangular floor
  reduces the true terminal upper to
  `(3/4)log log(4m)+O_C(1)`.  The earlier isolated
  `mathfrak U_(2^J)=Theta(J)` estimate is therefore historical, not the
  current signed boundary.

### Fejer taper and the Wave 16 boundary at that time

- For `omega_(k,J)=((J+1-k)/(J+1))^2`, proved exactly that
  `sum omega/k=log J+O(1)` and all intermediate renewal coefficients have
  the favorable nonpositive sign.
- The terminal fan becomes `O_C(1/J)`.  Since `Delta_m<log13`, the
  adjacent-epoch allocation incurs only `O(1)` total weight mismatch.
- The issue remaining at the end of Wave 16 was disjoint capacity: the same next-bulk
  `beta log D` values cannot pay both `Delta_m` and the existing
  rank/length floor without a new residual-capacity or majorization theorem.
- Exact rational certificate rows cover dyadic epochs through 2048 and
  Fejer horizons through 256.  Questions 1 and 2 and the prize claim remain
  unresolved.

### Perfect-difference literature boundary

- Chen--Fang Theorem 1.1 replaces any supplied infinite Sidon set `B` by a
  perfect difference set whose counting function shadows `B(x/2)` up to an
  arbitrary divergent error.  Hence ruling out a critical perfect difference
  set would already settle Question 1; it is not a smaller preliminary lemma.
- Cilleruelo--Nathanson construct perfect difference sets with
  `limsup A(x)/sqrt(x)>=1/sqrt(2)`.  Thus full difference coverage does not
  imply a full `o(sqrt(x/log x))` law, while leaving the liminf-zero question
  open.
- O'Bryant v3 supplies a finite universal normalized-liminf constant, not
  zero.  Whole-set perfect-difference completion deletes and inserts marks,
  so it does not preserve the fixed-prefix atoms needed by the then-current
  P21.  Wave 17 subsequently closes that local gate.
- The exact theorem statements, primary links, sum-versus-difference warning,
  and no-prize/no-novelty claim boundaries are recorded in
  `research_sources/WAVE16_PERFECT_DIFFERENCE_COMPLETION_BOUNDARY_2026-08-29.md`.

## Progress 2026-08-29 (Wave 17: disjoint local capacity and excess boundary)

### Same-atom residual above the triangular floor

- Every Wave 15 selected new difference is a literal target-Gothic interior
  atom.  After the Wave 11 triangular charge, that atom retains
  `beta_x log(x/L_s)`.
- Counting all near differences of gap length at most ten in a consecutive
  integer Golomb interval proves `x/L_s>=3/2` for `x>=2147`.
- Combining the smallest target coefficient `1/(16m^2)` with the Wave 15
  layer-load cap `<3/(4m^2)` gives
  `mathfrak B_(2m)>=K_(2m)^int+[log(3/2)/12]Delta_m`
  `-2146log(3/2)/(16m^2)`.
- The error is dyadically summable and the proof uses only residual value
  above the already-spent triangular floor.

### Exact local sorted-rank surplus

- The exact interior weight multiset gives
  `F_n^(loc,int)=[2log((n-1)!)+log(b!)+log(c!)]/(4n^2)`, with
  `b=3(n-1)(n-2)/2` and `c=(n-1)(3n-4)/2`.
- An independent constant audit verified
  `|F_n^(loc,int)-K_n^int-delta_0|<=18(1+log n)/n` for `n>=16`, where
  `delta_0=3/2+(3/4)log3-2log2=0.937664855381...`.
- Therefore the surplus is above `81/128` for `n>=2^20` and above `3/4`
  for `n>=2^22`.  It pays `3Delta_m/8` eventually, or alternatively the
  full residual `u-v` promotion truncated at height two.
- These are alternate uses of one aggregate floor, not two additive
  premiums.  This closes the local P21 coefficient-capacity gate for the
  triangular floor.

### Exact remaining boundary

- With `Theta_m^[2]=sum_p r_(m,p)min(P_(m,p),2)`, the local surplus gives
  `mathfrak B_(2m)>=K_(2m)^int+Theta_m^[2]` eventually.  Wave 16 implies
  `Theta_m^[2]>=(1/3)min(kappa_C,2)` on a hypothetical eventual-`C` branch.
- The unpaid term is
  `Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+`.  Its current envelope is only
  `O_C(log log m)` per epoch; the Fejer taper alone does not make its dyadic
  sum `o(log J)`.
- P22 now asks for a bounded-reuse signed insertion of this excess using
  actual local slack and the exact endpoint/descendant renewal ledger.
  A lower bound on the already nonnegative bulk is not a signed upper.

### Certified finite scope

- The Wave 17 generator checks the ten-layer polynomial threshold, cutoff,
  exact coefficient/load ratios, and literal atom ownership on Hall-64 and
  Erdős--Turán-128 prefixes.
- The focused suite passes six tests and 37 subtests; Ruff check and format
  verification pass, and the JSON regenerates byte-identically.
- The internal deterministic certificate hash is
  `33fdade0fd2e3ad5bb0048495eeec03ee2947044ddc788dc4bf919da99e04034`.
- Finite fixtures do not construct an infinite critical branch.  P19, P22,
  Questions 1 and 2, and the prize claim remain open.

## Progress 2026-08-29 (Wave 18: descendant jumps and birth locality)

### Exact signed insertion

- Computed the exact target-interior row capacities `w_(n,p)` and proved
  `w_(n,p)>=r_(n,p)` in every boundary case.
- Used only slack above the exact Wave 17 sorted-rank floor to prove
  `Theta_n^(exc,h)<=H_n^loc+J_n^(h)`, with every selected `(p,q)` atom used
  once.  The remainder `J` is supported only on descendant jumps above
  `exp(h)/3`.
- Raised the cap to `h=5/2`.  Since `D_n>15/16` eventually, the target
  epoch pays the preceding source cap and the full Wave 16 identity becomes
  `Z_n-R_(2n)=mathfrak P_n-K_n^int-mathcal T_n`
  `-Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)+J_n^(5/2)-(U_n+Q_n)`,
  with `mathcal T_n,U_n,Q_n>=0`.
- Verified the source/target index shift and the exact Fejer reindexing loss,
  which is bounded by `15/16`.

### All-source rank-layer load

- Layer-caked each logarithmic rank excess into unit rank intervals assigned
  to actual future numerical differences.
- Proved a fixed future difference receives less than
  `log2/(2exp(h)m^2)` from source epoch `m`, and hence less than
  `[8C log2/(3exp(h))]log(4x)/x` over all post-cap dyadic sources,
  eventually.
- This closes scalar rank-layer source multiplicity, but not authenticated
  reuse of unused signed carrier capacity at the later birth epoch.

### Adversarial boundaries

- An exact abstract rank model attains leading excess
  `(3/8)log log m`, so rank monotonicity and the scalar cap alone cannot
  improve the current envelope.
- Prime Erdős--Turán finite rulers give
  `limsup H_n^loc<=(3/4)(1+log(16/3))`, showing one-epoch Golomb constraints
  do not force divergent unused slack.  The rows are different finite rulers,
  not one compatible tower.
- A distant scaled-block construction keeps the local terms fixed and makes
  the terminal potential tend to zero while creating arbitrarily large
  excess.  Its infinite extension is supercritical, so it refutes only
  terminal-identity-only estimates which omit the eventual cap.

### Current boundary

- Monotonicity in the descendant endpoint collapses the two-dimensional
  remainder to
  `J_n^(h)<=sum_p r_(n,p)[log(d_(n,p)/D_(p,n))-(h-log3)]_+`.
  At `h=5/2` this threshold is only `0.0150933...` above `log4`.
- A monotone alternating scalar quadratic-envelope model gives a positive
  midpoint jump every other scale and a `Theta(J)` Fejer sum.  Positive-part
  telescoping cannot finish P23.
- Appending a cap-sized terminal to a prime Erdős--Turán core gives an actual
  finite Golomb prefix with
  `J_n^(h)>=(3/8-o(1))log log n+O_(C,h)(1)`.  It is terminal-cap-compatible
  but not one fixed-onset eventual-`C` branch, so it sharpens the local no-go
  without refuting P23.
- P23 is the birth-time Carleson/renewal estimate
  `sum_(k<=J)omega_(k,J)J_(2^k)^(5/2)=o_C(log J)`, or an exact signed
  cancellation of that functional.
- It must control source-to-birth delay, unused nonterminal carrier capacity,
  terminal births, and the renewing band.  P19/P23, Questions 1 and 2, and
  the prize claim remain open.

## Progress 2026-08-29 (Wave 19: cross-ratio absorption and sparse spikes)

### Exact cross-ratio and endpoint advances

- Proved the rectangle telescope
  `log[a_q d_(n,p)/(a_(2n-1)D_(p,q))]=sum_(i<p)sum_(j>q)C_(i,j)`.
- Audited the four boundary cases and proved the complete cross term is at
  most `(1/2)Y_n`.  The half constant is coefficientwise asymptotically
  sharp.
- Proved `lambda_(n,q)<(3/4)c_(n,q)`, with its exact maximum at `q=n`.
  This pays the endpoint overshoot with three quarters of the existing
  prefix deficit and leaves a favorable negative quarter.
- Regenerated the exact Wave 19 coefficient certificate byte-for-byte.
  The focused suite passed `11` tests and `2,692` subtests.

### Signed frontier reduction

- Derived
  `Z_n<=(1/2)Y_n+G_n+epsilon_n`
  `-(U_n^cap+Q_n+mathfrak e_n)` without double-spending the full-span term.
- Combined the Fejer renewal and Wave 13 harmonic lower bound.  The exact
  sufficient constant is
  `limsup(sum omega G)/log J<1/(3072C log2)`; P24 uses the cleaner little-oh
  target.
- Reindexed the preceding cap to the current total promotion at cost at
  most `15/16`, isolating the current-scale positive part `(Ghat_n)_+` as the
  smallest recommended target.
- Audited the tempting raw terminal shift.  Its `v log d` mismatch is
  `(log2/6)J+O_C(log J)`, not `O(1)`; the macroscopic half alone gives
  `(log2/8)J+O_C(log J)`.  This closes that shortcut.

### Certified sparse-spike/cooldown boundary

- Built and exactly replayed one nested `C=32` Golomb chain through 512
  marks.  The final prefix has `130,816` distinct positive differences.
- For the fixed 255- and 511-mark cores, the cap-maximum next terminals are
  exactly `23,258,158` and `104,661,718`.
- The selected optimized rows have
  `J_128=0.3091860771777816204...` and
  `J_256=0.005709533721666033398...`.
- The deterministic cooldown tested 774,102 candidates and is exact along
  its chosen branch, but alternative branches were not globally searched.
  No infinite extension or P23/P24 counterexample is claimed.
- The isolated sparse suite passed `13` tests and `23` subtests, and the
  dated JSON regenerated byte-identically.

### Wave 19 literature state

- Completed all seven phases of the structured literature workflow: 345
  deduplicated records, 10 manual Sidon/Golomb selections, six full reads,
  one explicit paywall exception, and three shallow records.
- The closest finite energy theorem is Carter--Hunter--O'Bryant; the closest
  qualitative birth construction is Cilleruelo--Nathanson.  Neither gives
  the fixed-branch quantitative theorem needed for P24.
- Consensus supplied no evidence because its quota was exhausted.  SciSpace
  supplied adjacent results only.  The report records a scoped null, not a
  theorem of nonexistence or a novelty claim.
- Corrected the relevant Martikainen v1 theorem numbers to 1.3 and 1.11.

### Current boundary

P23 is not refuted, but its literal positive form is no longer recommended.
P24 remains a valid sufficient reduction, but bare current-scale `Ghat` is
locally obstructed by dilation.  P25 removes that obstruction and P26 gives
the exact rank-free remainder.  The later P27 audit shows that the unchanged
P26/P27 upper bound is saturated by an untouched inner-new-birth sector, so
P28 below is now the highest-value direction.  The
alternative construction route
is a genuine infinite spike/cooldown induction with a uniform all-prefix cap;
finite depth alone cannot establish it.  P19/P24/P25/P26, Questions 1 and 2,
publication novelty, and every prize claim remain open.

### Certified rank-slack and P25

- Sorted all `c_n=(n-1)(3n-4)/2` Gothic interior values as
  `x_(n,1)<...<x_(n,c_n)` while carrying their actual `beta` coefficients
  `gamma_(n,j)`.
- Proved the exact decomposition
  `H_n^loc=Srank_n+Pair_n`, where
  `Srank_n=sum gamma_j log(x_j/j)>=0` and
  `Pair_n=sum gamma_j log j-F_n^(loc,int)>=0`.
- Audited the Wave 18 excess proof at atom level.  Since
  `alpha_(n,p)<=1` and `log_+(D/c_n)<=log(D/j)` at sorted rank `j`,
  `Theta_n^(exc,5/2)<=Srank_n+J_n^(5/2)`.  Hence
  `Q_n^cert=Srank_n+J_n^(5/2)-Theta_n^(exc,5/2)>=0` and
  `Q_n=Q_n^cert+Pair_n` exactly.
- Retaining this singly owned slack, the cap surplus, and the singleton gives
  `Z_n<=(1/2)Y_n+R_n^cert`, with
  `R_n^cert=mathfrak U_n-F_n^(loc,int)-Srank_n-J_n^(5/2)`
  `-(1/4)Dpre_n-mathfrak e_n+epsilon_n`.
- Independently checked the equivalent form
  `R_n^cert=Z_n+(3/4)Dpre_n-J_n^(5/2)+Pair_n` and the exact coefficient
  checksum proving invariance under integer dilation of the whole ruler.
  Unlike `Ghat`, `R_n^cert` is prefix-local and has no current/previous-cap
  reindexing cost.
- Established a rigorous local no-go for bare `Ghat`: Bertrand primes and a
  scaled Erdős--Turán core plus separated terminal give, for every `n>=4`, a
  one-scale `C=32` Golomb prefix with
  `Ghat_n>=(7/32)log floor(log(2n))-C_0`, even after allowing the maximum
  current promotion permitted by elementary ranks.  Independent dyadic
  copies have Fejer sum `Omega(J log J)`.
- Scope boundary: those copies are not one compatible eventual-`C` branch.
  They refute local/independent-scale proofs for `Ghat`, not P24, P25, or an
  Erdős statement.
- The new open target is
  `sum omega (R_(2^k)^cert)_+=o_(C,a)(log J)`; a stronger uniform finite
  block form is `sum_(k=L)^(2L)(R_(2^k)^cert)_+=o_C(1)`.

### Direct sharp collapse and P26

- Renamed the Wave 19 endpoint component
  `E_n^(end,5/2)` to keep it distinct from
  `Theta_n^(exc,5/2)`.
- Combined the already proved inequalities
  `J_n^(5/2)<=E_n^(end,5/2)+(1/2)Y_n` and
  `(mathfrak P_n-mathfrak F_n)+E_n^(end,5/2)`
  `<=-(1/4)Dpre_n+epsilon_n` directly inside the exact Wave 13 spectrum.
  This gives, without any rank promotion or lower-floor insertion,
  `Z_n<=(1/2)Y_n+R_n^sharp`.
- Defined
  `R_n^sharp=mathfrak U_n-mathfrak B_n-J_n^(5/2)`
  `-(1/4)Dpre_n-mathfrak e_n+epsilon_n` and checked exactly that
  `R_n^sharp=Z_n+(3/4)Dpre_n-J_n^(5/2)`.
- Audited the sign: the negative `-J` comes from the upper bound
  `J<=E^(end)+Y/2`; no negative quantity is inferred from a lower bound.
  The actual `mathfrak B_n` is used once, and no Wave 16 terminal potential
  or Wave 17 floor is mixed into this proof.
- Proved the universal coefficient-permutation estimate
  `0<=Pair_n<=(3/(4n^2))log binom((n-1)(3n-4)/2,n-1)`
  `<=3log(3en/2)/(4n)`.
- Consequently
  `R_n^cert=R_n^sharp+Pair_n` and the dyadic `Pair` tail from exponent
  `k_0` is at most
  `(3/4)2^(1-k0)[log(3e/2)+(k0+1)log2]`.  From `n>=4` it is at most
  `(3/8)log(12e)`.
- Therefore P25 and P26 have equivalent weighted positive-part targets up
  to `O(1)`, and equivalent exponent-block targets up to
  `O(L2^(-L))=o(1)`.
- The then-smallest proposed target was
  `sum omega (R_(2^k)^sharp)_+=o_(C,a)(log J)`.  The reduction, Pair bound,
  and dilation invariance are rigorous; the positive-part estimate,
  P19/P24/P25/P26, both Erdős questions, novelty, and all prize claims remain
  open.

### Nonnegative profile remainder, P27 saturation, and P28

- Strengthened Wave 19's rectangle comparison from `S_n<=Y_n/2` to
  `S_n<=Z_n^fin`, coefficientwise.  For `x=n-i>=2` and `y=j-n>=1`, the
  finite-sector coefficient is `y(2x+y)/(4n^2)`; for `x=1` it is
  `(y+1)^2/(4n^2)`.  The `x=2,y=1`, `x=1,y=1`, and `x=1,y>=2` corners were
  checked separately with the exact `alpha` bounds.
- Put `t_(n,p)=5/2-log(c_n/L_(n,p))>0` and
  `E_n^row=sum alpha beta [log(A/a_q)-t_(n,p)]_+`.  For
  `Delta_n=J_n^(5/2)-E_n^row`, monotonicity and the one-Lipschitz property
  of positive part give `0<=Delta_n<=S_n`.
- Obtained the exact nonnegative profile decomposition
  `R_n^prof=Z_n+E_n^row-J_n^(5/2)=Z_n-Delta_n`
  `=(Z_n^fin-S_n)+Z_n^fut+(S_n-Delta_n)>=0` and
  `R_n^sharp=R_n^prof+(3Dpre_n/4-E_n^row)>=R_n^prof`.
- Isolated the disjoint inner-new-birth sector
  `W_n=sum_(j=n+2)^(2n-1)sum_(i=n)^(j-2)`
  `((j-i)^2/(4n^2))C_(i,j)`.  Since `S_n` has support only `i<=n-1`,
  `W_n<=Z_n^fin-S_n<=R_n^prof`.
- Repeated the Wave 13 layered distinct-gap proof on the `n` gaps
  `{h_n,...,h_(2n-1)}`.  With `H_n'=a_(2n-1)-a_(n-1)`, it gives
  `W_n>=E_n'/(8n^2H_n')`, where
  `E_n'=n(n-2)(n^2+4n-14)/48`.  For dyadic `n>=16` on a hypothetical
  eventual-`C` branch,
  `R_n^sharp>=R_n^prof>=W_n>1/(1536C log(4n))`.
- Therefore the tapered liminf on any extant eventual-`C` branch is at least
  `1/(1536C log2)`, twice the strict P26-sharp allowance.  This closes
  unchanged P26/P27 as a standalone intermediate upper lemma; it neither
  proves nor refutes branch nonexistence unconditionally.
- Registered P28 as the next open direction: keep the negative renewal cuts
  and construct a singly owned cross-scale carrier that relocates a positive
  part of `W_n` out of the residual while leaving a strictly larger retained
  harmonic signal.  A same-scale or block bound on unchanged `R_n^prof` is
  no longer an admissible target.
- P19/P24/P25 and the exact P26/P27 reductions remain historical inputs.
  P28, both Erdős questions, publication novelty, and every prize claim
  remain open.

## Progress 2026-08-29 (Wave 19: P28 full rows and adaptive cap)

### Full-row ownership audit

- Extended the Gothic descendant rows through `2<=p<=2n-2`.
- Proved that allocating the complete terminal coefficient `u_p` fails from
  `n=6` onward, with first dyadic failure `n=8`, worst atom `C_(1,n+1)`, and
  asymptotic worst ratio `9/8`.
- Recorded the independent ownership failure `u_p=v_p+bar r_p`: full-`u`
  allocation while retaining the next negative cut double-spends `v_p`.
- Restricted the legal transport demand to `bar r_p`.  The natural row
  quotient fits every beta row and satisfies `Sbar_n<=Y_n/2`
  coefficientwise.  The terminal atom `C_(1,2n-1)` makes the half constant
  asymptotically sharp.
- On the inner `W_n` sector the natural transport covers less than half, so
  the old strict-threshold saturation remains.

### Adaptive row cap and actual-rank correction

- Defined `h_(n,p)=max(3/2,log(c_n/L_(n,p)))`, giving nonnegative row
  threshold on the entire full-row range.
- Corrected the cap statement: the actual capped promotion is bounded by,
  and need not equal, `Cdet_n=sum_p bar r_p h_(n,p)`.
- Proved
  `Cdet_n<0.8336738101+0.3009853/n` and combined it with the Wave 17 lower
  bound to obtain `D_N>Cdet_(N/2)>=Theta_(N/2)^cap` for every `N>=2048`.
- Audited the actual-rank atom identity.  The valid inequality is
  `Theta^exc<=Srank+S_t+E_t^rank`; the endpoint-free candidate omits a
  positive term and is invalid without the stronger unproved rank condition
  `j<=exp(h)L a_q/A`.
- For the natural transport, proved both `S_t<=Y/2` and
  `E_t^rank<=3Dpre/4` coefficientwise.

### Arbitrary transport cannot remove the inner residual

- Allowed every feasible transport `0<=t_(p,q)<=beta_(p,q)` with exact row
  sums `bar r_p`, including a transport chosen after seeing all cross-ratio
  energies.
- Proved the universal dyadic floor
  `E_n^res(t)>=n^2/(2^25 H_n')` for `n>=64` by a transport-independent row
  bound, good-partner selection, distinct integer gaps, and exact
  symmetrization.
- Derived the eventual-`C` floor `>1/(2^27 C log(4n))` and Fejer liminf
  `>=1/(2^27 C log2)` on every extant branch.
- Proved that the corner `C_(2n-4,2n-1)` has exact transport coverage ratio
  `1/3` for every feasible transport.
- This closes transport optimization as a standalone P28 repair.  It does
  not close cancellation by the intact signed whole-cut/terminal-potential
  ledger.

### Current exact next theorem

- Constructed and certified the mixed transport `t=(8t0+tR)/9`, where `tR`
  is the rowwise right-greedy fill.  Prefix dominance preserves
  `S_t<=Y/2`, and exact endpoint-column formulas prove
  `E_t^rank<=2Dpre/3` for every `n>=4`.
- This replaces the natural whole-cut functional by
  `Gmix=R+Pcoef logA-Kint-T-ThetaFull-Dpre/3`
  `=Gold-Dpre/12`.
- Preserve `v` inside the negative renewal cut and preserve the full
  cap/rank/Pair balancing bracket.  Prove the signed Fejer bound for
  `Gmix` below `1/(3072C log2)`, or the corresponding clean `o(log J)`
  tapered positive-part estimate.
- Hostile finite check: the exact `n=4` Golomb ruler
  `(0,101,204,309,416,525,636,749)` satisfies
  `W_4-S_t|W_4>Dpre_4/12`, so the endpoint gain is not a direct unsigned
  payment of the inner residual.
- Do not reuse `D-cap`, `Q`, `Pair`, `Dpre`, `Y`, or `W` after they have
  already been spent in deriving that functional.
- Status remains `UNRESOLVED_AT_HARD_LIMIT`; P28, both questions, novelty,
  and every prize claim remain open.
