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
