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

## Progress 2026-08-29 (proof reset continuation: Route C signed correlation)

This continuation is not a new numbered Wave.  It audits the post-reset
cross-kernel route and supersedes the historical instruction to prove bare
`Gmix` small.

### Exact positive-part completion

- For finitely supported real kernels, symmetric `H`, and a finite Sidon set,
  rederived
  `E_H(A)=|A|C_H(0)+2 sum_(d in Delta(A)) C_H(d)`.
- Proved the always-legal coefficientwise completion
  `E_H(A)<=|A|C_H(0)+2P_H`
  `=m^T Hm+(|A|-1)C_H(0)+2N_H`.
- Recorded its exact slack as the sum of positive correlations at omitted
  differences and negative correlations at represented differences.  The
  statement is the exact independent-coordinate positive-part completion;
  it does not retain even the cardinality of the Sidon difference set, and
  no global optimality is claimed.

### Two scoped G2 closures

- If `H` is PSD and annihilates the kernel-mass vector, total correlation is
  zero.  Nonnegative correlation at every nonzero shift then forces the
  entire effective kernel and energy to vanish.  Without that sign gate,
  `2N_H=C_H(0)+2P_H>=C_H(0)`, so a zero-mass scale contrast with nonzero
  effective energy has a mandatory negative-correlation cost.
- For any finite family of distinct point-mass kernels,
  `C_H(0)=tr(H)`.  The positive-part completion is at least the same-diagonal
  baseline, so off-diagonal coupling cannot improve this precise bound.
- The minimal two-channel fixture
  `K_1=delta_0`, `K_2=delta_1`,
  `H=[[1,-1/2],[-1/2,1]]`, `A={0,2}` has actual energy `4`, illicit PSD-only
  value `3`, and repaired positive-part value `4`.

### Exact computation and audit trail

- Added a wider-kernel exact rational certificate covering the energy and
  mass identities, Gram factorization, zero-mass theorem, point-mass class,
  mutation rejection, and deterministic replay.  Canonical payload SHA-256:
  `c9b77974643244edc713bb0d8674a5f3e951ea727eb06b0f46d4ba83696a6747`.
- Added the two-kernel rational-grid certificate: 91 reduced unit-diagonal
  positive-definite cases through denominator 12, including 45 negative
  cross coefficients and zero legal strict gains.  Canonical payload
  SHA-256:
  `4c071ae8c5ec6408da75b71ea0e54c1c2fe7c3402c3241df00594af7c665363c`.
- The two focused suites currently total 13 passing tests.  These tests check
  exact finite implementations; the universal claims rest on the displayed
  proofs, not grid exhaustion.

### Surviving obligation

- The current Route C target is no longer a zero-mass PSD contrast or a
  translated-delta coupling.  It must use nonzero-mass overlapping kernels
  with a certified joint boundary benefit, prove that the actual compatible
  difference set pays selected negative shifts, or add a genuinely
  geometry-sensitive conditional/filtration deficit.
- P28, both Erdős questions, publication novelty, and every prize claim remain
  open.  Global status stays `UNRESOLVED_AT_HARD_LIMIT`.

### Overlapping nonzero-mass kernels: exact positive feasibility

- For two nonnegative probability kernels and
  `H_b=[[1,b],[b,1]]`, put
  `A_d=R_11(d)+R_22(d)` and `B_d=R_12(d)+R_21(d)`.  Proved that a negative
  coefficient passes the all-shift sign gate exactly when
  `b>=-rho`, where `rho=min_(B_d>0) A_d/B_d>0`; the no-positive-`B_d` case is
  handled separately without an invented ratio.
- Proved the endpoint identity
  `sum_(d>=1)(A_d-B_d)=-||K_1-K_2||_2^2/2`.  Hence `rho<=1`, equality forces
  identical kernels, and distinct feasible kernels have `rho<1`.
- Under the sign gate, every feasible `b<0` gives the exact strict pure-energy
  gain
  `U_b(k)-U_0(k)=b(2+(k-1)B_0)<0`.
- The minimal half-grid witness
  `K_1=delta_0`, `K_2=(delta_0+delta_1)/2`, `b=-1/2` has ratio `4/7` at
  `k=2`.  A full-support denominator-four witness has ratio `29/176`.
- The rational family
  `K_1=(1/2-t,1/2+t)`, `K_2=(1/2,1/2)`, `b=-1+2t^2` drives the pure-energy
  ratio to zero, but total correlation mass, `C_b(0)`, and the small Gram
  eigenvalue collapse simultaneously.  This proves that unit diagonal is not
  a meaningful normalization.
- Added an exact `Fraction` certificate with endpoint, enumeration, family,
  mutation, and byte-replay coverage.  Its canonical payload SHA-256 is
  `f3950cbcb199e2c31123fc7c7b5e650c937bd971afc0e156bbd77f5bc7ae7963`.
  The overlapping suite has 10 tests; all three Route-C suites total 23
  passing tests.
- Independent theorem audit passed after adding the `rho=1`, `b=-1`,
  multi-kernel/multi-cardinality, and three-point family checks.
- This is G2 positive feasibility for a finite pure upper-energy objective,
  not a useful Sidon inequality.  No Hou--Zhao boundary-cover lower functional
  is fixed.  The precise next optimization must preserve a nondegenerate
  joint boundary-cover or lower-energy normalization while retaining a strict
  gain.

## Progress 2026-08-29 (Route C boundary-normalized cross coupling)

This continuation is not a new numbered Wave.

### Exact cross-matrix smoothing extension

- Extracted the lower boundary norm and fixed-kernel QP from Hou--Zhao v2,
  Sections 2 and 3.1, and generalized them to a symmetric positive-definite
  coupling matrix `H`.
- With `q_(j,r)=gamma_r w_j^r`, defined
  `beta=gamma^T H^-1 gamma`, `s=1^T H1`,
  `a_H=m sum h_rs<p^r,p^s>`,
  `Phi_H=sum q_j^T H^-1 q_j`, and
  `b_H=beta+2(Phi_H/m-L beta)`.
- Proved the exact master inequality
  `k^2<=(beta N+b_H T-beta)(s+a_H(k-1)/T)` under the joint cover,
  positive-definite metric, every-shift combined-correlation gate,
  `N>=2LT`, and `b_H>0`.
- Proved the block-lift gate: every lifted correlation is `1/h` times a
  convex combination of two adjacent discrete combined correlations.
- Proved `delta=beta s>=1`, with equality exactly at
  `gamma=H1/s` when the vector is an admissible nonnegative mixing weight.
- Corrected the general asymptotic calculation.  The secondary coefficient is
  `delta^(1/4)sqrt(a_H b_H)`, not `sqrt(delta a_H b_H)`.  Both expressions
  agree at `delta=1`, which is the only leading-constant-one comparison.

### Coupled boundary QP and exact witness

- Derived the strict convex QP
  `min q^T(I tensor H^-1)q` subject to `Aq>=c`, its exact dual, and the KKT
  system.  Coordinates with zero mixing weight must be deleted or fixed to
  zero.
- Certified the normalized `m=3,L=2` witness
  `p^1=(1/4,1/2,1/4)`, `p^2=(3/8,1/4,3/8)`,
  `H_12=-1/5`, `gamma=(1/2,1/2)`.  Its correlations are
  `(19/32,27/80,53/320)` and all KKT equalities hold exactly.
- Obtained
  `a_H b_H=20620579147935/22461389262592=0.9180455806...`.
  For the same kernels with `H_12=0`, the exact product is
  `840600527/912906560=0.9207958008...`.  The signed coupling therefore
  improves the coefficient by the exact square-root factor
  `0.9985054901...`, about `0.15%`.

### Bounded-search boundary and next action

- Exhausted the stated finite grid of denominator-eight symmetric kernels at
  `m=3,5`, boundary depths `L=1,2`, all 21 reduced negative rationals of
  denominator at most eight, and diagonal weights `1/8,...,7/8`, with exact
  every-shift and rational KKT checks.
- The best diagonal/direct-sum grid candidate has product
  `20720894357613941/23062969911203072=0.8984486576...` and is about
  `1.085%` better at coefficient level than the cross hit.  Therefore the
  same-kernel gain is real but not a global grid improvement; the finite grid
  is not a global no-go.
- The next finite experiment is a signed first variation of a strong
  diagonal certificate, starting with the exact Hou--Zhao eight-kernel data,
  or a broader exact cross search.  The actual #1191 obligation still needs
  one compatible infinite history and an order-changing deficit.
- P28, Questions 1 and 2, publication novelty, and every prize claim remain
  open.  Global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-29 (competitive Hou--Zhao cross perturbation)

This continuation is not a new numbered Wave and concerns the finite
`F(N)` secondary coefficient only.

### Official-source replay

- Checked the official repository at commit
  `ef044564300e546f8832b31f5fba133fd192cc3a`.
- Verified that `sidon_certificate_8kernel.py` has SHA-256
  `957a5afadd849ac4f97c2b71252abb5c796c2db3c91a608ab35097e3c49292a8`,
  matching Hou--Zhao v2 Section 4.
- The untouched verifier reproduces all 129 covering inequalities, the exact
  least positive slack, and coefficient `0.9434925907135450...`.
- The raw upstream verifier is not vendored because no explicit repository
  license was found.  The local perturbation certificate stores exact
  aggregates and supports a hash-pinned optional replay against a user-fetched
  official file.

### Exact two-cycle perturbation

- Set `H=diag(lambda)+epsilon J`, `epsilon=1/6250`, where the nonzero symmetric
  upper entries of `J` are
  `J_12=-1,J_14=2,J_17=-1,J_28=1,J_45=-1,J_48=-1,J_57=1`.
- Proved `J1=0`; hence `H1=lambda`, `s=beta=1`, and the exact published cover
  and boundary vectors remain valid without QP reoptimization.
- Proved positive definiteness by strict diagonal dominance.  The smallest
  affected-row margin is `6303669/100000000`; the smallest unchanged
  diagonal is `lambda_3=135342/100000000`.
- Checked every discrete combined correlation exactly.  The minimum is the
  positive shift-31 fraction
  `1819897465312660450421661319/6250000000000000000000000000000`;
  the block-lift identity covers every integer shift.
- Exact boundary evaluation gives coefficient
  `0.9434922260277724855...`, strictly below the official certificate by
  about `3.64686e-7`.

### Scope and next mechanism

- Exhausted all 210 alternating four-cycles in both orientations and
  sums/differences among the best 80 downhill cycles, with gcd reduction.
  The displayed matrix is the best two-cycle combination in that finite
  search, not a global matrix optimum.
- Derived a separate envelope/first-variation formula that includes exact
  boundary-QP reoptimization, changing normalized tail weights, the PD tangent
  cone, and active correlation gates.  Freezing the old boundary vectors is a
  feasible-certificate corollary, not that full derivative.
- At that checkpoint, the next task was to solve the reoptimized boundary QP
  along this direction and use the
  first-variation criterion to search broader rational cross matrices.  Even
  a better finite coefficient has no direct #1191 consequence without an
  order-changing theorem on one compatible infinite history.
- Questions 1 and 2, P28, publication novelty, and every prize claim remain
  open.  Global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-29 (live status and plugin literature delta)

- Firecrawl forced a live rendering of the otherwise direct-403 official
  #1191 page and confirmed the displayed `OPEN` status, `$1000` annotation,
  zero claimed proofs, and 2026-04-06 page edit date.
- Exa reviewed 55 raw results across five distinct status/infinite/finite
  queries.  Full fetches confirmed the official page, O'Bryant v3, and
  Hou--Zhao v2; no newly surfaced result closed the signed-payment,
  compatible-history, and order-change chain.
- A SciSpace ten-result query produced only adjacent or semantically confused
  Sidon literature after filtering.  Consensus could not run because its
  connected monthly quota was exhausted.
- These discovery checks are recorded only as a dated coverage delta.  They
  do not prove novelty or absence, and the global status remains
  `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-29 (two-scale bridge and coefficient-only closure)

- Proved the exact common-grid correlation and asymmetric left/right boundary
  master for widths `T` and `2T` on the same finite Sidon prefix.
- Derived the exact old--old/old--new/new--new energy for two nested prefixes.
  One combined sign gate is insufficient, and unit outer-prefix coverage by
  a constant simplex tail removes channel 1 from the constant leading bulk.
- Proved that every uniform finite remainder `O(N^(1/2-delta))`, `delta>0`,
  has only `O(1)` normalized dyadic Fejer sum.  In particular, no bounded
  improvement of the finite `N^(1/4)` coefficient can alter the certified
  `Omega(log J)` compatible-branch obstruction.
- Recorded the exact rank-one covariance subtraction, Sherman--Morrison
  boundary price, net gain, and a fully quantified sufficient finite-horizon
  bridge obligation with a nonanticipating rule and explicit constants.
- Independent audit found no remaining mathematical, quantifier, scope, or
  formatting defect after repairs.  Memo SHA-256:
  `5c01bcfadac11eb9279b995f93e04079e1097d6358ab274a6598d30b9dcb7f53`.
- The history obligation is open.  Q1, Q2, P28, novelty, publication, and
  prize claims remain unresolved.

## Progress 2026-08-29 (exact Hou--Zhao boundary-QP reoptimization)

This continuation is not a new numbered Wave and concerns only the finite
`F(N)` secondary coefficient.

- Kept the hash-pinned Hou--Zhao eight kernels, mixing weights, and the
  row-sum-zero two-cycle direction fixed, set `epsilon=1/462`, and solved the
  generalized boundary QP exactly.
- The rational KKT solution has 126 active cover rows; rows 1 and 15 have
  strict slack.  Every active dual coordinate and every primal coordinate is
  positive, all cover slacks are nonnegative, and stationarity,
  complementarity, and primal--dual equality hold exactly.
- Strict diagonal dominance proves `H>0`.  All 32 discrete correlations are
  strictly positive; the minimum occurs at shift 31 and the block-lift formula
  covers every integer shift.
- The exact coefficient is `0.9434876661938243084...`, giving the clean finite
  certificate
  `F(N)<=sqrt(N)+0.94348767 N^(1/4)+O(1)`.
- The exact `epsilon=1/500` solution remains a regression, and direct rational
  comparison proves the primary `1/462` product is smaller.  The canonical
  payload SHA-256 is
  `b0095488470697d0c0e38be1e18a427fc6a6e490f2ed8f04bd02a1cb20f25b52`;
  the JSON file SHA-256 is
  `1c36b59550225e030dcdbf11f82904bdc4a7104e41ae3d790202e4834ee235e3`.
- Source-backed regeneration is byte-identical to the stored JSON.  The
  offline suite passes 15 tests, and the hardened validator rejects 40
  semantic, deletion, addition, provenance, KKT, and overclaim mutations.
- Exact determinant/correlation analysis separately gives the
  PD-and-correlation feasible rational interval along this direction.  For the
  fixed published boundary vector, a Sturm count gives exactly one stationary
  point in the real PD interval and proves it is the constrained fixed-`q`
  minimum.  This is not a statement about the reoptimized value function.
- Independent mathematical and artifact audits passed.  The optimum is only
  over boundary variables for fixed outer data.  No global optimum,
  current-best, novelty, compatible-history, Q1/Q2, publication, or prize
  claim is made; the global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-29 (centered multiband critical-history carrier)

This continuation is not a new numbered Wave.  It attacks C058 inside the
uniform-box covariance family and preserves the global unresolved status.

### Exact diagonal/off-diagonal separation

- For `K_T=T^-1 1_[0,T-1]` and `L_T=K_T-K_(2T)`, the parallelogram identity
  gives `||f*K_T||_2^2=||f*K_(2T)||_2^2+||f*L_T||_2^2`.
- Hence `sum_(r>=0)||1_A*L_(2^r)||_2^2=|A|` for every finite set.  This
  positive total is the zero-lag diagonal Parseval mass.
- With `O_T=||1_A*L_T||_2^2-|A|/(2T)`, the exact finite telescope is

  `sum_(r=0)^R O_(2^r)=|A|/M-||1_A*K_M||_2^2`

  `=-2 sum_(d in Delta(A),d<M)(M-d)/M^2<=0`, where `M=2^(R+1)`.
  The infinite centered sum is zero.  A fixed-prefix weighting therefore
  cannot supply the required positive off-diagonal resource.

### Nonanticipating first-use carrier

- On a hypothetical eventually `C`-critical chain with `k_j=2^j`, set after
  a finite onset

  `T_j=2^(s_j)=k_j*2^ceil(log_2(8C log(2k_j)))`.

  This depends only on `C,j`, and `s_(j+1)-s_j` is one or two.
- The last `k_j/2` spatially ordered adjacent gaps all contain a new mark and
  have total at most `N_j-1`.  The critical cap forces at least `k_j/4` of
  them below `T_j/2`.  Their exact low-pass correlations give

  `C_(j,s_j)-C_(j-1,s_j)>1/(64C(j+1)log 2)`,

  where `C_(j,r)=||1_(A_j)*K_(2^r)||_2^2-k_j/2^r` and `0<=C_(j,r)<1`.
- Retain every band on the one- or two-band path
  `X_j=C_(j,s_j)-C_(j,s_(j+1))`.  Exact reindexing with the Fejer weights
  pays all Abel and terminal costs by less than one and gives

  `sum_j w_j X_j>=(log J)/(64C log 2)-O_C(1)`.

### Legal three-channel realization and remaining gap

- With `D=diag(1/4,1/2,1/4)`, the three-vertex path Laplacian, and
  `theta=3/25`, the matrix `H=D-theta L_path` is positive definite.  Its row
  sums equal `gamma=(1/4,1/2,1/4)`, so `s=beta=1` and the constant
  full-support cover has no inverse-metric contrast price.
- The exact cover length is `B_j=N_j+2^(s_(j+1))-1`.  Sidon difference
  counting makes `B_j/N_j-1=O_C(j/2^j)`, hence the boundary normalization
  error is summable.
- The centered normalized gain has coefficient
  `3/(1600C log 2)`, strictly above `1/(1536C log 2)`; the exact rational
  coefficient margin before the common `1/(C log 2)` factor is `11/38400`.
- Two independent mathematical audits agreed on the identities, constants,
  indexing caveat, and claim boundary.  The centered covariance carrier,
  nonanticipating schedule, internal first ownership, Abel boundary, and
  terminal payment are proved.
- A follow-up adversarial audit checked the explicit harmonic estimate,
  boundary series, and `K_(C,j_0)` term-by-term; it passed after enforcing the
  required domain `j_0>=1` in the memo.
- The retained-box payload is
  `aa1353fbeafdd5993708cecf3a4571c21c354b6bdc389608c08f4650fb34a09e`
  with 16 tests and 11 rejected mutations.  The multiband payload is
  `d58abe257554db107e526279e65405797687c0281abe77b4fe82d8d5ff69dc41`
  with 13 tests and nine rejected mutations.  Both generators replay their
  JSON byte-for-byte; the full Route-C focus now passes 93 tests.
- A targeted Firecrawl/Exa/Consensus/SciSpace refresh resurfaced the closest
  finite smoothing/Fourier/profile precedents but no checked common signed
  capacity theorem.  This is recorded as a qualified retrieval null, not a
  novelty or absence claim.
- C058 remains open only at the cross-family layer: no common inequality yet
  places this negative covariance gain and the Wave-19 positive harmonic
  atoms in one disjoint capacity ledger with opposite signs.  Q1, Q2,
  publication novelty, and every prize claim remain unresolved.

## Progress 2026-08-29 (cross-ratio box-dipole/Gothic bridge)

This is an unnumbered proof-reset continuation of C058.

### Definition and indexing audit

- Wave epoch `n` uses the `2n`-mark prefix and new gaps
  `h_n,...,h_(2n-1)`, with the global convention
  `h_r=a_r-a_(r-1)`.  The matching centered carrier cardinality is `k_j=2n`.
- The centered-carrier memo had a prose-only off-by-one expression using
  `a_(i+1)-a_i`; it was corrected.  The generator already used the correct
  boundary gap, and its JSON remains byte-identical with payload
  `d58abe257554db107e526279e65405797687c0281abe77b4fe82d8d5ff69dc41`.

### Exact continuum bridge

- For `R_T(d)=(T-d)_+/T^2`, `M=D_(i+1,j-1)`, `u=h_i`, `v=h_j`, and oriented
  edge dipoles, the exact tent

  `psi_T=R_T(M)+R_T(M+u+v)-R_T(M+u)-R_T(M+v)`

  is nonnegative, supported on `M<T<M+u+v`, and satisfies

  `psi_T=-<e_i*K_T,e_j*K_T>`.
- Direct integration gives, with no extra factor,

  `C_(i,j)=integral_0^infinity psi_T dT`.
- Therefore `W_n=integral Q_n(T)dT`.  The exact interval mixed-difference
  table proves

  `0<=Q_n(T)<=Delta_n,T^suf/(2n^2)<=Delta_tilde_n,T/(2n^2)`.

### Finite-horizon/Gothic ownership

- With `H=D_(n,2n-1)` and
  `F_H(d)=log(H/d)+d/H-1`, the coefficient moments satisfy
  `sum lambda=sum lambda D=0`, hence

  `W_n=sum lambda F_H(D)=-sum lambda log D`.
- The positive full-span coefficient has zero potential.  Every other
  positive coefficient is strict interior and exactly equals the Wave-11
  `beta_n(p,q)` coefficient.  All non-full `q=2n-1` coefficients are
  nonpositive.  Thus positive terminal capacity is not needed.
- Those `beta` atoms are already owned by `mathfrak B_n`.  This theorem is a
  basis change/capacity map, not a new reserve; adding it on top of the
  Gothic payment would be duplicate ownership.

### Scale and fixed-prefix no-go boundaries

- The Golomb ruler `{0,1,5,7}` has a positive tent supported between dyadic
  widths, and `{0,1,T,T+2}` makes the dyadic sampled-to-integral ratio
  unbounded.  Every fixed finite set of log phases similarly misses a
  sufficiently narrow large-scale tent.
- Continuum phase is exact:

  `integral_0^1 sum_r 2^(r+theta)psi_(2^(r+theta))dtheta=C_(i,j)/log 2`.
- For dyadic `k`, a prime `k<p<2k`, and
  `a_m=2pm+(m^2 mod p)`, the resulting finite set is Sidon with `N_k<4k^2`.
  It has `liminf W_(k/2)>=1/162`, while the canonical critical-width
  fixed-prefix centered increment and normalized three-channel gain tend to
  zero.  This refutes ordinary fixed-prefix domination, not a telescope on
  one fixed infinite branch; the finite family changes with `k`.

### Certificate and literature boundary

- `cross_ratio_box_dipole_certificate.py` passed 13 tests, exact finite-horizon
  audits at `n=4,5,8,16,32,64`, semantic and byte replay, and 12 mutation
  rejections.  Payload SHA-256:
  `1cf424a41ee728ab6ee39af3e4941ae94e0b4b9d94606f4a6ee65d45b49e7a09`.
- A targeted Firecrawl/Exa/Consensus/SciSpace refresh found primary
  precedents for Fourier logarithmic energy, triangular box covariance,
  cone-overlap logarithms, and log-correlated scale decompositions.  Bacry--
  Muzy's terminal plateau is especially close to the `F_H` correction.  No
  checked source supplied the Sidon finite-horizon signed ownership theorem.
  This is a qualified retrieval null and the elementary identity is not
  claimed novel.
- C058 is now open at the legal phase-integrated signed rewrite of the
  already-owned Gothic bulk, including the rank-dipole PSD/diagonal price and
  compatible-history terminal terms.  Q1, Q2, publication novelty, and every
  prize claim remain unresolved; status stays `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-29 (continuum-phase prefix/scale transport gate)

This is an unnumbered proof-reset continuation of C058.

### Exact transport identity

- For one fixed log phase and nested prefixes, defined the low-pass state
  `C_(j,r)`, retained-band edge `O_(j,r)`, and prefix first-use edge
  `Delta_(j,r)`.  Direct cancellation gives the exact grid curl

  `Delta_(j,r)-Delta_(j,r+1)=O_(j,r)-O_(j-1,r)`.
- Two finite summations by parts, with no discarded boundary, give interior
  retained-band coefficient

  `b_(j,r)=w_j s_(j,r)-w_(j+1)s_(j+1,r)`.

  The initial epoch, final epoch, and scale-terminal contributions are
  explicit in the identity.

### Naive universal-capacity gate

- For
  `c_(j,r)=2^(r+theta)/(2n_j^2) 1_(r<=R_j)`, the cumulative capacity is
  `s_(j,r)=2^(min(r,R_j)+theta)/n_j^2`.
- When `n_(j+1)=2n_j` and the epoch weights are positive, the retained-band
  coefficients are nonnegative at every scale exactly when

  `w_(j+1)2^max(0,R_(j+1)-R_j)<=4w_j`.
- The exact Fejer-weight fixture with cutoffs `2 -> 5` has
  `b=100/121-162/121=-62/121`.  Therefore the full pointwise envelope cannot
  be transposed through adjacent epochs and then treated as having only
  nonnegative coefficients.  The band values themselves need not be
  nonnegative; the gate concerns coefficients in the retained-band/PSD
  realization.
- This result does not rule out pair-dependent fractional allocation, longer
  epoch transport, randomized/adaptive phase, or payment within a larger
  signed master.

### Certified evidence and next obligation

- `phase_transport_gate_certificate.py` passed 9 tests, semantic/byte replay,
  five mutation rejections, and a separate independent finite-grid gate audit.
  Payload SHA-256:
  `d3d30f25f66c3a7f55f1881a9d7ea631b9eae2cfc2a33bf51d38a2a61226989e`.
- The separate ET certificate passed 12 tests, semantic/byte replay, and 16
  mutation rejections.  Payload SHA-256:
  `f522626a23f323e8f3304b37a83abf10bcc1ce85f90a038cd032c3f0017f54ba`.
- C066 is `HUMAN_PROOF_AUDITED`.  C058 remains `OPEN`: the next finite problem
  is a strict-interior `lambda=beta` pair-owned allocation LP, or an exact
  signed payment for every negative transport coefficient and all terminal
  rows.  No Q1, Q2, publication, novelty, or prize conclusion follows.

## Progress 2026-08-30 (pair-owned allocation and exact dipole PSD price)

This is an unnumbered proof-reset continuation of C058.  It replaces the
aggregate scalar allocation target by an owner-resolved statement and then
computes the exact cost of the stronger coefficient-PSD realization.
The two source memos both use `P_n(T)` for different quantities.  In this
summary `P_n^pot(T)` denotes the C067 positive potential and `P_n^PSD(T)`
denotes the C069 diagonal price.

### Pair-owned phase allocation

- C067 is `HUMAN_PROOF_AUDITED`.  Writing
  `Q_n=P_n^pot-N_n`, the proportional rule

  `x_(gamma,r)=u_(gamma,r) Q_n(T_r)/P_n^pot(T_r)`

  (and zero when `P_n^pot(T_r)=0`) meets the scale demand and every
  strict-interior pair capacity.  On the canonical dyadic spatial-prefix
  chain, each positive `lambda=beta` pair is born wholly inside its current
  dyadic block, so its formal negative pre-birth band is exactly zero and its
  birth band has the positive coefficient.  The scale-terminal row and
  signless-completion diagonal price remain explicit.  This is a rewrite of
  the existing Gothic ownership, not an additional copy of it and not yet a
  common PSD master.
- C068 is `CONDITIONAL_NO_GO`.  Only on the displayed nested prefixes at
  `n_-=4`, `n_+=8`, with fixed `w_-/w_+=100/81`, the exact fixture closes
  every phasewise scalar fractional allocation satisfying equations
  (4.3)--(4.5): the stated universal envelope, aggregate demand, finite
  horizon, and adjacent nonnegative coefficient gate.  Its strict rational
  contradiction gap is `461/227700`.  This does not rule out the C067
  owner-resolved allocation, signed or cross-phase payment, longer transport,
  different weights, or a larger master.

### Active coefficient-PSD price

- C069 is `HUMAN_PROOF_AUDITED`.  On the exactly active Wave edge graph,

  `min sum_i g_i(T)d_i`, subject to `diag(d)+B_T` PSD,

  equals

  `P_n^PSD(T)=sum_((i,j) in E_n(T)) alpha_(i,j)sqrt(g_i(T)g_j(T))`.

  An explicit weighted edge-Laplacian supplies the primal certificate and a
  rank-one scaled-elliptope matrix supplies the dual certificate.  The exact
  tent table gives `P_n^PSD(T)>=2Q_n(T)` and hence `Pi_n>=2W_n`.  Active
  localization is necessary for integrability.  This is the price of the
  stronger coefficient-PSD lift; positivity only after contraction with the
  actual ordered dipole Gram matrix is weaker and remains open.
- C070 is `CONDITIONAL_NO_GO`.  For the exact eight-mark Golomb prefix
  `(0,101,204,309,416,525,636,749)` at `n=4`, the active graph is bipartite
  and

  `G_4<2W_4<=Pi_4`.

  Thus the isolated positive same-epoch finite-horizon Gothic sector does not
  universally pay the coefficient-PSD price.  The actual Gram restriction,
  nonpositive Gothic boundary rows, signed cancellation, cross-epoch or
  cross-phase payment, and a larger master are not closed.

### Certificates, literature boundary, and remaining target

- `pair_owned_allocation_certificate.py` passes 10 tests and rejects seven
  mutations.  Canonical payload SHA-256:
  `25a84d6a534cb0be83d851b312579c3253268064b24b209e93a8bddee327d618`.
- `dipole_psd_price_certificate.py` passes 10 tests and rejects eight
  mutations.  Canonical payload SHA-256:
  `76fcc06eb5d1edcda2c1fd51c93122bdb558eb545bd90006627d42dcea107327`.
- Adding these 20 tests to the previous 127 gives 147 passing Route-C tests.
  Both new generators replay their JSON byte-for-byte.
- The targeted primary-source delta is
  `research_sources/signed_offdiag_2026-08-29/PSD_DIAGONAL_PRICE_LITERATURE_DELTA.md`.
  Lee--Seung's diagonal majorant/edge-square proof, Boman--Chen--Parekh--
  Toledo's factor-width-two classification, Laurent--Poljak's elliptope,
  Bacry--Muzy's cone-overlap logarithm, and Frerick--Müller--Thomaser's
  logarithmic-energy formula are known ingredients.  We did not locate the
  complete weighted statement in this application; this is a qualified
  synthesis boundary, not a novelty claim.  Consensus was unavailable after
  its monthly quota was exhausted.
- C058 remains `OPEN`.  The next exact target is either an actual
  ordered-box-dipole Gram-restricted inequality, or a signed cross-epoch,
  cross-phase, or larger-master construction that pays the C069 diagonal
  price and every C066/scale terminal row from singly owned capacity while
  inserting C067 by rewrite rather than duplication.
- P28, Question 1, Question 2, publication novelty, and every prize claim
  remain unresolved.  Global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-30 (unnumbered Route C ordered-root and ramp continuation)

This continuation is not a new numbered Wave.  It attacks the actual-Gram
branch left open after C070 and keeps C058, Q1, and Q2 open.

### C071--C073: exact actual-Gram theorem and its insertion gates

- Proved from `Tf_i=1_(V_i)-1_(U_i)` that every ordered box-dipole Gram has
  the labeled root decomposition

  `G=diag(rho)+sum_(i<j)psi_(i,j)(e_i-e_j)(e_i-e_j)^t`, `rho_i>=0`.

- The indefinite Wave matrix `B_ij=-alpha_(i,j)/2` lies in the actual
  ordered-root dual and satisfies
  `<B,G>=Q_n(T)=sum alpha_(i,j)||T^-1 1_(U_i intersect V_j)||_2^2`.
  This closes fixed-scale actual-Gram positivity without the C069
  coefficient-PSD price.
- For `eta_i=(i-c)/(2n)`, proved the exact ramp surplus

  `eta^tG eta-Q_n(T)`
  `=sum_i rho_i eta_i^2+(4n^2)^-1 sum_i psi_(i,i+1)>=0`,

  together with the optimal-shift Schur formula.
- Certified the scope gates: ungated ramp energy diverges like
  `(n^2-1)/(8n^2T)` at zero; signed band differences can leave the SDDM cone;
  and zero Wave-root slack forces constant PSD Schur cross rows.  Hence the
  active gate and every terminal row remain owned obligations.

### C074--C075: marginal transport hierarchy and payment failure

- The disjoint left/right strip geometry gives a sharp fractional
  vertex-cover/transport LP with
  `Q_n(T)<=V_n(T)<=P_n^PSD(T)/2`.
- On `(0,101,204,309,416,525,636,749)`, integrated
  `V_4=32755417/340707840` exceeds the positive Gothic upper bound by
  `898545848033/103063780892160`.  This closes only marginal-only payment;
  exact intersection cells and signed rows remain live.

### C076--C077: isolated negative-potential reserve failure

- On `(0,2,5,16,22,23,31,35)`, `N_4(2)=0` while `Q_4(2)=1/64`; exact
  phasewise and continuum audits also separate the reserve from the pair,
  marginal, coefficient-PSD, and finite-terminal full prices.
- On `A_L=(0,2,5,16,L+16,L+17,L+25,3L+25)`, the isolated reserve tends to
  `(9/64)(log(9/2)-1)` while the integrated pair, marginal, and PSD prices
  diverge logarithmically.  Thus no positive universal fraction of those
  prices is available from this scalar reserve.  The original signed
  negative rows were not discarded or ruled out.

### C078: fixed three-channel active-ramp insertion no-go

- The rank-weighted ramp is outside the formal span of the fixed three
  full-prefix channels.  A zero-mass fourth channel can preserve leading
  cover normalization, but its legal PSD extension has the exact Schur price
  `d>b^tH_3^-1b` and an active low-pass terminal.
- On the same `A_L` family and `9<T<L`,

  `Q_4(T)=9/(64T)-45/(64T^2)`,
  `min_c eta^tG eta=27/(128T)-9/(16T^2)`.

  The ramp log coefficient `27/128` exceeds the complete positive same-epoch
  Gothic coefficient `18/128` by `9/128`; an exact bound is already positive
  at `L=2^18`.
- This is only the scoped linear cellwise insertion/positive-Gothic payment
  no-go.  The indefinite labeled-cell matrix `B` itself has zero surplus in
  the actual ordered-root dual.  A direct membership-sensitive signed rewrite,
  disjoint reserve, cross-epoch/cross-phase payment, and a larger master remain
  open.

### Replay and state

- The marginal, ordered-Gram, negative-reserve, and ramp/common-master suites
  contribute 12, 15, 13, and 12 tests.  Before the C079 continuation, the
  17-suite Route-C run passed **199 tests**, and all four generators pass
  `--verify --self-check` with
  byte-exact JSON replay.
- Their payload hashes are
  `3d500b1dad4ee2501b1c0babc586c18d376782ef718c2120d6f646b7fede3739`,
  `4af9e73fbfe449c05ee685399aa78bccc2979b65840e7a81d69721f9562bea5e`,
  `b102f5345497519321b04695c4f8cde068b08367530cfef215a16dc4f86927f0`,
  and
  `cfc033c1299174bf7219a46378821444b8402cac9d7f966bab80b7f01220677b`.
- The next target is a direct labeled-cell signed use of `B`, or a
  signed/cross-epoch/cross-phase/disjoint-reserve/larger
  membership-sensitive master that pays every diagonal, Schur, active-gate,
  and terminal row exactly once while rewriting the Gothic `beta` rows.
- C058, P28, Q1, Q2, complete proof, publication novelty, and every prize
  claim remain `OPEN`; global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-30 (unnumbered direct-`B` interval/Haar continuation)

This is not a new numbered Wave.  It follows the live direct labeled-cell
branch left after C078.

### C079: physical-point interval theorem and exact Gothic ownership

- Defined `M=D^tBD` on the `n+1` current physical endpoints.  For every binary
  consecutive interval state of length `m`, proved
  `u^tMu=m^2/(4n^2)` exactly for a strictly internal interval with `m>=2`,
  and zero otherwise.
- Integrated the actual box membership states to obtain the sharp theorem
  `Q_n(T)<=||sum q_k||_2^2/(4n^2)`.
- Proved `M1=0`, `diag M=0`, and the exact row identity
  `2M_(p-n,q-n+1)=lambda_(p,q)`.  Direct physical-pair rows therefore rewrite
  the existing Gothic ledger; they are not new capacity.
- Consecutive direct-pair supports are disjoint, but the corresponding
  positive count baselines count their shared endpoint diagonal twice unless
  it receives one explicit owner.

### C080: terminal-free signed Haar-Abel bridge

- Proved the exact signs in

  `sum_(r=L)^U T_rQ_r`
  `=sum 2T_r(Q_r-Q_(r+1))-T_LQ_L+T_(U+1)Q_(U+1)`.

- Chose active endpoints with `T_L<=m_*` and `T_(U+1)>=H`, making both
  boundary rows exactly zero.
- Proved `G_T-G_(2T)` is the Gram matrix of gap dipoles convolved with the
  Haar row `K_T-K_(2T)`.  Log-phase integration gives an exact terminal-free
  signed direct-`B` representation of `W_n/log 2`.

### C081--C082: signed cell and zero-slack repair obstructions

- Exact band fixtures give both signs:
  `<B,G_3-G_6>=-1/324` and
  `<B,G_200-G_400>=63/256000`.
- On the maximal actual cell `[636,709)`, the current-block state
  `v=(-1,-1,1,1,0)` satisfies `1^tv=0` and `v^tMv=1/8`.  Hence
  `kappa J-mu M` is negative on this cell for every `kappa` and `mu>0`.
- Singleton zero slack forces every scalar interval-cover row to vanish.
  Root-restricted Schur nonnegativity on every `(t e_i,y)` likewise forces
  the external cross block to vanish.  Both results are scoped zero-price
  no-gos; positive membership correction and constrained signed states remain
  open.

### C083: count-baseline payment obstruction

- On `A_L` and `9<T<L`, the sharp count baseline is
  `11/(64T)-9/(16T^2)`, while the Wave density is
  `9/(64T)-45/(64T^2)`.
- The integrated baseline has log coefficient `11/64`; the complete positive
  same-epoch Gothic sector has `9/64`.  The finite exact witness `L=2^24`
  has gap greater than `1/32`.
- This closes only the sharp count baseline as a free repair or a payment from
  that positive sector.  Cheaper state-dependent and signed multi-epoch
  repairs remain open.

### Exact next target and replay

- Solve the finite multi-epoch actual-Haar-cell SDP.  Deduplicate all physical
  endpoints, impose every atomic-cell inequality with a positive membership
  correction, rewrite `2M=lambda`, give the shared endpoint diagonal one
  owner, and retain all birth, past-scale, active-gate, and final rows.
- Require an exact rational primal matrix, exact rational dual cell weights,
  and zero duality gap.
- `direct_ordered_b_interval_haar_certificate.py` passes 16 tests, rejects 16
  semantic/hash mutations, and reproduces the literal canonical JSON bytes.
  Payload SHA-256:
  `8f067c8e409b93058520b6e669de7eb4370e81c19b1c5abd988e1c0e68fc6ac2`.
- The full 18-suite Route-C run passes **215 tests**.
- C058, P28, Q1, Q2, complete proof, publication novelty, and every prize
  claim remain `OPEN`; global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-30 (unnumbered fixed-fixture membership-SDDM continuation)

This continuation executes the finite actual-cell target left by C083.  It is
not a new numbered Wave and does not promote a fixed fixture to a uniform
history theorem.

### C084: exact one-epoch coefficient-trace optima

- Enumerated all 16 actual half-open Haar cells, including both zero exterior
  cells, for `n=4`, `T=200`, `mu=1` and block points
  `(309,416,525,636,749)`.
- Restricted the correction to the nonnegative graph-root sum
  `C=sum w_(i,j)(e_i-e_j)(e_i-e_j)^t` plus the aggregate channel `kappa J`.
- LP A, minimizing `trace(C)` with `kappa` unpriced, has exact optimum `1/16`:
  `w_(1,3)=1/32`, `kappa=3/32`; the single dual multiplier
  `y_[749,816)=1/2` gives the same value.
- LP B, minimizing `trace(C+kappa J)`, has exact optimum `1/10`:
  `w_(0,2)=w_(2,4)=1/40`, `kappa=0`; dual multipliers `2/5` on
  `[525,616)` and `[836,925)` give the same value.

### C085: exact two-active-epoch/common-scale coefficient optimum

- Used the finite Golomb fixture `a_k=k(k+100)`, `0<=k<=15`; exact
  enumeration verifies all 120 positive differences are distinct.
- Embedded the consecutive `n=4` and `n=8` blocks, sharing only `a_7=749`,
  at common `T=200`.  Their union has 40 complete actual cells.  Both epochs
  have positive pointwise cells and positive integrated signed Haar-band
  demand (`63/256000` and `169/5120000`).
- The exact coefficient-total-trace optimum is `53/448`, with root weights
  `45/1792`, `11/448`, `3/1792`, and `1/128`, and both aggregate
  coefficients zero.  Four exact dual cells attain `53/448`; all 78 edge
  capacities and both aggregate capacities pass.
- The shared global correction diagonal is `C_(4,4)=47/1792` and is recorded
  once in `trace(C)`.  This is single accounting, not a paid Gothic, birth,
  cross-epoch, or external-reserve budget owner.

### Scope, replay, and next target

- C084--C085 are `COMPUTATIONAL_FINITE` optima only inside the stated
  root-SDDM-plus-`J` coefficient classes at fixed fixtures, `mu=1`, and
  `T=200`.  Dividing coefficient trace by `2T` does not give the physical
  integrated Haar-energy cost of a root shift; that cost depends on physical
  displacement.  No arbitrary-PSD, indefinite, signed, uniform-scale, or
  common-history optimum is claimed.
- `direct_b_membership_sddm_lp_certificate.py` passes 12 focused tests,
  rejects 12 semantic/hash mutations, and reproduces the literal raw JSON
  bytes.  Payload SHA-256:
  `d2620c68c366f765a1f5c502be65dfaf258558af93b9df5f4a50464d8fd52f23`.
  An independent exact audit checked complete cell enumeration, primal and
  dual feasibility, zero gaps, Golomb validity, integrated activity, and
  shared-point accounting.
- Next, lift the fixed corrections uniformly across epochs, scales, phases,
  and one compatible finite history.  Compute displacement-dependent
  physical root energy, rewrite `2M=lambda` without duplicate Gothic
  capacity, assign every shared endpoint a singly paid budget owner, and
  retain all birth, past-scale, active-gate, terminal, and final rows.
- C058, P28, Q1, Q2, complete proof, publication novelty, and every prize
  claim remain `OPEN`; global status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-30 (unnumbered physical Haar-energy continuation)

This continuation replaces the C084--C085 coefficient objective by exact
physical translation energy.  It is not a new numbered Wave.

### C086: exact physical root cost

- For `g_T=1_[0,T)-1_[T,2T)`, direct overlap gives the normalized root cost
  `chi_T(d)=3d/T` on `0<=d<=T`, `4-d/T` on `T<=d<=2T`, and `2` for
  `d>=2T`.
- The breakpoint values agree and `chi_T(T)=3`; coefficient trace `2` is not
  a physical-energy substitute.  The derivation holds for every `T>0` and
  `d>=0` and is `HUMAN_PROOF_AUDITED`.

### C087: exact finite physical optima and strict joint savings

- At `T=200`, the separate `n=4,n=8` physical optima are `29/200` and
  `139/3200`; the joint optimum is `3809/22400`, giving strict saving
  `103/5600`.
- For `a_k=k(k+1000)`, `0<=k<=31`, common `T=2000`, exact separate
  `n=4,n=8,n=16` optima are `299/2000`, `1489/32000`, and `1477/128000`.
  The joint optimum is `163481/896000`, and the saving is `11251/448000`.
- Complete cell-length-weighted primal/dual certificates have zero gaps and
  strictly positive dual contributions from every epoch.  These results are
  `COMPUTATIONAL_FINITE`; no legal external budget owner is supplied.

### C088: literal fixed sparse reuse and changing-family obstruction

- Reusing the displayed `T=2000` three-epoch sparse weights unchanged at
  `T=2500` fails on `[6036,6516)`: correction `1/8`, demand `9/32`, slack
  `-5/32`.
- For fixed integer `C`, the family `a_k=k(k+C)` has
  `a_3-a_0=3C+9=a_(C+5)-a_(C+4)`.  Raising `C` for deeper finite fixtures
  changes all earlier marks and the scale.
- This is a `CONDITIONAL_NO_GO` only for literal scale-independent reuse and
  that changing quadratic family.  Scale-dependent weights and a genuine
  cross-scale recurrence on one fixed compatible history remain open.

### Replay and surviving theorem contract

- `direct_b_physical_energy_lp_certificate.py` passes 16 focused tests,
  rejects 16 mutations, and reproduces the literal raw JSON bytes.  Payload:
  `3f406a1a6c7dfa19bf5172eadba5c5227ba175f4caf7811df6e53e5c75d3f630`.
  Independent audit checked the tent, physical primal/dual values, canonical
  cell-length dual, both savings, mixed-scale countercell, and collision.
- At the C098 checkpoint, the Route-C count was **25 suites / 291 tests PASS**.
- The OPEN target is a finite-horizon scale-adaptive actual-cell cover and,
  on every capped compatible finite tower,

  `G_off-P-terminals >= epsilon_C log((J+1)/(j0+1))-K_C`.

  The canonical cell-length dual gives `P>=weighted W`; feasibility or joint
  saving alone is insufficient.  Only cover excess with an explicit one-for-
  one `2M=lambda` cancellation may be charged.  Continuum phase, exact mixed-
  scale energy, singly owned resources, and every birth/past-scale/active-
  gate/terminal/final row must remain in the same ledger.
- C058, P28, Q1, Q2, complete proof, publication novelty, and every prize
  claim remain `OPEN`; status is `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-30 (unnumbered C089--C096 physical-cover narrowing)

This continuation does not create a new numbered Wave.  It keeps C058 as the
sole primary research bottleneck while separating four finite mechanisms.

### C089--C090: universal actual-Haar star and mandatory gate

- Proved an explicit endpoint-to-interior star cover for every ordered actual
  Haar state and every `n>=3`.  The internal-block state
  `1_[1,n-1]` is a sharp dual witness, so total root mass
  `(n-1)^2/(4n^2)` is optimal among universal nonnegative-root covers.
- Its physical price is the exact sum of C086 `chi_T` costs.  At every
  sufficiently low scale it equals `(n-1)^2/(2n^2)>0`, so an ungated dyadic
  sum diverges.
- An independent audit exhausted 4,774,245 representations for
  `17<=n<=100`, one million random states through `n=10^6`, and 1,000 random
  physical geometries without a counterexample.
- The audit found a mutable cached-dictionary validator flaw.  A regression
  test first reproduced certificate poisoning; the cache now stores immutable
  canonical JSON and returns a fresh object.  The former attack is rejected.

### C091--C092: exact unequal-scale energy and cell-dual floor

- Derived the oriented overlap formula `A_(T,S)(d)` and the exact quadratic
  energy `2T alpha^2+2S beta^2+2 alpha beta A_(T,S)(d)`.
- For any finite mixed-scale family, common-cell integration gives
  `E-D=sum |c| slack_c>=0`, with equality exactly at zero slack on every
  positive cell.  Coefficient PSD is neither required nor sufficient.
- The `T=2,S=4,d=-1` fixture exhibits a positive-definite price `7/4<2`
  block that violates two cells by `-1/8`; repair gives price `9/4`.
  Independent integration checked 7,744 oriented rows and all 729 adversarial
  block triples.

### C093--C094: membership threshold at a shared endpoint

- On `0^*,(-1,-1),+1^m,0^*`, predecessor-root transfer has slack
  `(4-m^2)/(8n^2)`.  Thus `m=2` is exactly tight and `m=3` is the first
  failure.
- The fixed `a_k=k(k+100)` two-epoch tower realizes the tight row at `T=200`;
  the one-sided correction covers all 40 cells and costs `81/400`.
- At `T=250`, `[1100,1114)` realizes `m=3`, leaving `-5/128`; the standard
  successor root still leaves `-1/128`.  This closes only the named fixed
  recurrence.

### C095--C096: exact full-phase parametric LP and positive surplus

- On the same fixed history and `128<=T<=256`, exact endpoint events
  `T=d,d/2` give 23 breakpoints and 22 event chambers.  Exact primal/dual
  reconstruction yields 30 optimality chambers and 18 primal vertices.
- The C087 primal transports through actual `T=216,220`, but fails at
  `T=221` by `-5/32` on `[636,637)`.
- On `(381/2,216)`, exact optimal cover excess is
  `-479/1792+4169/(64T)`.  Canonical cell-length nonnegativity on the other
  chambers gives full log-phase lower bound `56389/13934592>0`.
  Hence zero same-scale phase-excess is false for this fixture/class.

### Literature and next falsifiable object

- Primary publisher records confirm that exact uni-parametric LP solution by
  parameter intervals/rational functions is established methodology.  The
  specific physical event list and exact chamber certificates are local to
  this project.  A targeted unequal-scale Haar search found no matching paper;
  that is an unsaturated retrieval result, not novelty evidence.
- The next C058 object must optimize and transport cross-scale **surplus**,
  not merely cover the demand.  It must keep oriented mixed-scale energy,
  membership length, explicit `2M=lambda` cancellation, and every singly
  owned birth/boundary/terminal/final row in one finite-horizon ledger.
- C058 remains the sole primary bottleneck, not a last-lemma claim.  Q1, Q2,
  complete proof, novelty, publication, and prize eligibility remain open;
  global status stays `UNRESOLVED_AT_HARD_LIMIT`.

### C097--C098: exact cross-scale surplus sharing, but no cross-root payment

- The fixed 14-channel `n=4,T=200` plus `n=8,S=800` common-cell LP has exact
  optimum `1555757/6144000`, demand `173/1024`, and positive surplus
  `517757/6144000`.
- Its optimum is nevertheless lower than the separate-optimum sum by
  `10643/1228800`, certifying strict finite surplus sharing under the one
  combined sum-cover inequality.
- An exact optimal dual strictly excludes all 45 cross-scale roots (minimum
  margin `799/4000`) and the exactly priced `J4,J8,J_all` columns.  The saving
  is within-scale surplus sharing, not a cross-root mechanism.
- The combined constraint can use a large-scale same-root correction to fill
  a small-scale cell deficit, so it is weaker than separately owned epoch
  rows.  The next C058 probe must impose epochwise or signed ownership before
  testing phase transport and the full boundary/terminal ledger.

## Progress 2026-08-30 (registered C099--C110 signed-owner continuation)

### Fixed epoch-owner faces: C099--C102

- C099 imposes the two epoch demands separately on the fixed C097 14-channel
  fixture.  Its maximal cell-independent nonnegative owner LP has exact
  optimum `134081/512000=29/200+59841/512000`; the C097 pooled-row saving
  disappears and no cross root is used.
- C100 replaces those owner copies by the canonical conservative signed
  coordinate-row split.  Nine owner entries are negative and the shares sum
  pointwise to the physical square, but the optimum remains
  `134081/512000`; the minimum cross-root dual margin is `237/500`.
- C101 expands to 26 deduplicated channels and four owner ledgers.  The full
  1300-variable and no-cross 624-variable optima are both
  `156321/512000`; demand is `4663/25600` and surplus is `63061/512000`.
- C102's strict dual margins force all 676 cross columns to zero on that
  exposed optimal face.  Owner `(4,800)` is inactive, so this is only a
  fixed-cone no-go.

### Formal finite transport: C103

Lean 4 formally verifies the frozen generic algebra in
`PrefixScaleFinite.lean`: `prefixScaleCurl`, `finiteScaleAbel_terminal`,
`finiteEpochFlux_range`, `finiteGridDivergence_range`,
`finiteEpochScaleAbel_transport`, and
`finiteEpochScaleAbel_transport_fromPotential`.  The statements include
initial/final epoch boundaries, interior epoch differences, scale
differences, the upper scale terminal, and the zero-horizon case.  The clean
Lean 4.33.0 build completed 1010 jobs; local Rocq 9.1.1 independently compiled
only the curl audit.  This closes the finite algebra statement, not the C058
sign, ownership, capacity, price, or global-history application.

### Canonical coordinate-owner cone: C104--C106

- In the fixed 52-coordinate graph cone, C104 gives a feasible 20-root price
  `99062067/179732480`, proves cross-epoch roots necessary relative to the
  no-cross lower bound, and separately proves the full graph-cone floor
  `55874798199/102400000000>2D` by `14494798199/102400000000`.
- C105 enlarges to zero-row-sum PSD and supplies an exact 52-by-13 Gram witness
  with `P=19511959/50000000<2D` by `5544953/400000000`.
- C106 optimizes the complete finite C067 positive-pair allocation and proves
  negative `Phi` for every feasible correction in that fixed PSD convention.
  The complete signed four-corner replacement changes the ownership/terminal
  convention and is outside that conditional no-go.

### Aggregate whole-stencil reopening: C107--C109

For the fixed tower `a_k=k(k+100)`, epochs `n=4,8`, widths
`100,200,400,800`, and terminal `1600`, all 24 primitive four-corner stencils
have zero lower and upper sampled boundary.  Their aggregate demand is
`D_4=9/128`, `D_8=1349/10240`, hence `D=2069/10240`.

C107 records an exact epoch-block zero-row-sum PSD witness with 19 and 31
positive LDL pivots, zero epoch cross block, and 532 nonzero cross-width
upper-triangle entries.  All 608 aggregate owner-cell rows hold; minimum
positive slack is `41304919/12500000000000`, and

`P=3900000000091/10000000000000`,

`Phi=141015624909/10000000000000>0`.

The exact Fejer threshold is
`w_8/w_4>581005931206/1286084055751`.  Ratio `9/16` works for all `m>=4`, with
recorded margin `2278661602463/800000000000000`; `m=3` gives `4/9` and fails.

C108 audits the smaller no-cross-width PSD cone.  Its 380-row dual and four
12-by-12 projected slacks with 48 positive pivots prove

`P>=843669938599/2048000000000`,

which exceeds `2D` by `16069938599/2048000000000`.  Thus cross-width coupling
is necessary only inside this fixed aggregate model.

C109 supplies the ownership RED gate.  On owner `(4,200)` and cell
`[709,725)`, primitive `(5,7)` contributes `1/3200`, primitive `(4,7)`
contributes `-9/25600`, and the aggregate is `-1/25600`.  The fixed old matrix
share `-49528467/1690000000000` covers the aggregate with slack
`8243579/845000000000`, but the positive primitive residual is
`-577653467/1690000000000`.  Five exact tight rows also kill the canonical
uniform left-edge variables `tau_10,tau_11,tau_12,tau_14,tau_15`, while
source `j=13` has zero sampled capacity.  This refutes only primitivewise
inference and that fixed-old-`X` orientation, not aggregate legality or all
joint reoptimizations.

### One adjacent phase point: C110

At `t=4835/48`, widths `t,2t,4t,8t`, terminal `16t`, the exact 52-by-11 Gram
witness satisfies all 616 aggregate rows.  There are 259 zero and 357 positive
slacks, with minimum positive slack `40498647/1934000000000000`, and

`D=6221/30944`,

`P=951134501701/3000000000000`,

`2D-P=246690436855133/2901000000000000>0`.

This is a single rational midpoint, not an adjacent chamber or continuum
phase theorem.

### Updated next target

Keep the C107 cross-width structure and search for an exact witness template
on every cell of a complete rational phase chamber.  In the same model, prove
that aggregate one-for-one Gothic ownership is legal or replace it by a
genuinely reoptimized primitive/source flow, close `m=3,2,1`, and carry every
birth, shared endpoint, initial, past-scale, active-gate, final, and terminal
row through one compatible finite history.  Only then test the correctly
normalized phase integral and a horizon-uniform positive master inequality.

C058 remains the sole primary bottleneck as a priority statement.  Q1, Q2,
complete proof, novelty, publication, and prize eligibility remain open;
global status stays `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-30 (registered C111--C114)

The aggregate ownership question was separated correctly from primitive
ownership and formalized in Lean, then independently audited by the repaired
Rocq MCP.  The fixed quadratic 16-mark phase was closed exactly over 108
chambers and 109 endpoints, with a positive uniform margin for every Fejér
ratio in `[9/16,1]`.  A finite cutoff calculation showed that the final three
Fejér blocks can stay on the complete baseline at `o(1)` cost, conditional on
the core.

Adversarial testing then found and exactly certified a powers-of-two Golomb
fixture where every feasible correction in the same epoch-block PSD cone has
negative margin.  Because the fixture is not eventual fixed-`C` critical,
this is not a C058 counterexample; it rules out a geometry-free theorem and
forces a history-sensitive phase-margin/span-potential dichotomy.  Numerical
tests on several critical-near histories and larger near-arithmetic dyadic
sizes remained positive, but those runs are exploratory only.

Full details and the next target are in
`CONTINUATION_2026-08-30_C058_FULL_PHASE_AND_HISTORY_DICHOTOMY.md`.

### Signed span reset/payment lemma (C115--C116)

The normalized Wave-shell span has a signed increment whose Fejér-harmonic
finite sum is uniformly bounded by exact Abel summation.  This turns the
informal lacunarity-payment idea into a specific local target.  Positive
variation alone can still be harmonic-sized under all scalar span bounds.
Separately, the critical schedule forces a positive density of 16-mark
windows inside `8T_n`; their degenerate shape and owner localization remain
unresolved.

## Final verification refresh 2026-08-31

- The complete current Route-C discovery set contains 32 suites; a fresh
  cache-suppressed run passed all 352 tests in 261.598 seconds.
- The CSV and JSON registries agree field-for-field, contain exactly the
  sequential IDs C001--C116, and retain global status
  `UNRESOLVED_AT_HARD_LIMIT`.
- Lean MCP clean-built 1,054 jobs and the following direct Lake build
  completed 1,047 jobs.  Diagnostics were empty, theorem verification
  reported only standard Lean/mathlib axioms, and the source scan found no
  `sorry`, `admit`, or project axiom.
- The pinned Rocq MCP exposed 13 tools; health, a minimal closed proof, both
  canonical full compiles, and all five named assumption checks succeeded
  with empty assumptions.
- The old Wave 19 manifest remains intentionally unsealed.  The current
  exact census is recorded in `INTEGRITY_STATUS.md`; it is not a release or
  prize-proof claim.

## Progress 2026-08-31 (registered C117--C119)

The generic owner-fiber identity was stress-tested at its missing global
selection step.  Two rank-one zero-row-sum PSD blocks can each pay a different
local owner through one shared coordinate, yet every single global coordinate
owner map gives shares `(2,0)` or `(0,2)`.  Lean verifies symmetry, row sums,
the exact square energies, PSD, local/global values, and the obstruction.
Rocq independently checks the fixed finite obstruction with empty assumptions.
This closes only automatic owner stitching, not joint Gram optimization.

An exact adversarial 16-mark Golomb fixture then passed the finite `C=2`
dyadic envelope at `m=4,8,16` while having
`eta_2=log(1659/1768)<0`.  Over the complete phase
`1649/8<=t<=1649/4`, 87 rational chambers and 174 nonnegative dual vectors
give 348 exact endpoint PD checks and the rigorous bound

`integral Phi(t) dt/t < -1/40`.

The same rational atanh replay now encloses the normalized dual upper by
`-81/2000 < U < -1/25`; this strengthens the finite calibration without
changing the cone or the `k=2` scope.

The canonical certificate is solver-free at replay time, stores 53,592
integer weights, rejects 12 mutations, and passes all seven focused tests.
It refutes the finite error-free bare-eta bridge only in the stated independent
epoch-block cone; it does not reach sufficiently large rank or an eventual
critical infinite history.

The obstruction suggests a bounded concentration storage column

`V_k=1-H_k^2/(2^k sum_i h_(k,i)^2)`.

Cauchy gives `0<=V_k<1`, and exact Abel gives the horizon-uniform bound
`|sum_(k=k0)^K p_k Delta V_k|<=p_k0` for every finite decreasing
nonnegative `p`; for the Fejer-harmonic weights the range is
`0<=k0<=K<=J`.  Its exact
increment is about `0.372590` on the new negative fixture and `0.000996` on
the positive quadratic fixture.  This is admissible global storage, not yet a
local margin theorem.  The next exact computation is a primal/dual phase bank
for this and ordered dyadic concentration coordinates, followed by a larger-
rank held-out test and an explicit global owner ledger.

An exact reverse-concentration Golomb fixture with `H2=430`, `H3=656`,
`eta` ratio `82/215`, and
`Delta V=-443620417/1928247678` has been added to the next bank.  A trial
`epsilon=A=1/1000`, `B=1/3` survives the exact necessary-side C118 bound and
the existing exact C112 witness, but this is finite coefficient calibration,
not a local theorem.  Same-multiset permutations can reverse a bounded
order-sensitive profile increment while leaving `V` fixed, so both symmetric
and ordered storage coordinates must be tested phasewise.

C058 remains the sole primary bottleneck.  The global status remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.

### Verification and literature delta after C119 strengthening

The current 33-suite Route-C tree passed all 359 tests in 302.947 seconds.
The strengthened C118 verifier now replays both the raw integral bound and the
normalized `U<-1/25` bound; its seven focused tests and 12 semantic mutations
also pass.  Fresh Lean build/axiom audit completed 1,067 jobs with only
standard dependencies, and a fresh temporary Rocq compile/check closed all 14
audited theorem families.  Registry CSV/JSON remain identical through C119,
and first-party JSON/control/artifact scans pass with the Lean `.lake` cache
explicitly excluded from release claims.  Exact commands and hashes are in
`evidence/C119_VERIFICATION_2026-08-31.md`.

A connector-cross-checked primary-source delta found matrix Carleson stopping
times, chordal PSD completion/decomposition, and dyadic-tree Bellman formulas.
They assume positive testing data or consistent overlap data and therefore do
not solve the signed owner-selection/storage inequality.  The scoped null and
Consensus quota limitation are recorded in
`research_sources/c058_storage_2026-08-31/SCOPED_SEARCH.md`; no novelty claim
is made.

## Progress 2026-08-31 (registered C120)

The first reverse-concentration held-out row now has a solver-free exact
certificate.  On the fixed 16-mark Golomb fixture with `H2=430`, `H3=656`,
`exp(eta2)=82/215`, and
`Delta V=-443620417/1928247678`, the complete phase
`553/8<=t<=553/4` has 161 exact chambers.  The canonical payload stores 2,285
rational epoch-block Gram columns and replays 99,176 generic owner rows at
both endpoints plus 194,528 collapsed-endpoint owner rows.

For `rho=9/16` and the C119 trial
`epsilon=A=1/1000`, `B=1/3`, `e2=0`, exact rational atanh integration gives

`719/10000 < overline Phi_2 < 9/125`,

while the prototype right side lies in `(13/500,27/1000)` and the exact gap
is greater than `457/10000`.  The same fixture therefore does not refute the
complete phase-integrated target.

This conclusion cannot be localized chamberwise.  An independent eight-piece
dual on chamber 0 gives normalized upper `<2601/100000`, below the prototype
by more than `207/1000000`, with 32 exact endpoint LDL checks.  Full-phase
redistribution is therefore essential, and no pointwise/per-chamber statement
is recorded.

The artifact is
`route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE.md` and its canonical
JSON/verifier/test bundle, payload SHA-256
`388daa5b719a6f817f3d2de2f5227340b2ec355ca53e93ba2753edc3d270b10d`.
The focused seven-test suite and thirteen semantic mutations pass.  This is
finite coefficient calibration only: it proves neither scalar-`V`
sufficiency nor a global owner/C103 ledger.  The next decisive experiment is
the matching exact primal lower certificate for C118, followed by ordered
permutations and larger rank.  C058 remains the sole primary bottleneck and
the global status remains exactly `UNRESOLVED_AT_HARD_LIMIT`.

### Unregistered C118 exact-primal diagnostic after C120

The immediate C118 follow-up produced exact feasible rational factors on all
87 chambers: 1,573 columns, 53,592 open owner rows, and 104,784 endpoint owner
rows replay exactly.  The normalized witness is enclosed by

`-47703/1000000 < L_primal <= U_primal < -47702/1000000`,

while the prototype right side is in
`(-41045/1000000,-41044/1000000)` and the existing exact dual upper is about
`-0.04014304`.  The constructed lower witness misses the target by about
`0.00665787`, but this is not a no-go: the residual primal--dual gap is about
`0.00755914` and still contains the target.

The largest localized gaps are chambers 49, 73, 74, 64, and 70.  Chamber 1
could not be rationalized from the direct-integral solve at owner floors
`10^-5` or `10^-6`, so its earlier exact max-min factor was retained.  The
manifest and verifier remain disposable under `/tmp` with payload SHA-256
`50704f33c7b4dfc71e29c9e5608fc9c8b6934c54608d13dce976cd695ea8c17d`.
This diagnostic is not registered as C121 because it proves neither side of
the prototype comparison.  The next finite task is to close this exact window
by improved primals or a tighter dual before promoting the scalar storage
candidate.

### Verification after C120 and the C118 diagnostic

The current 34-suite Route-C tree passed all 366 tests in 342.109 seconds.
The C120 CLI independently replayed 161 chambers, 2,285 Gram columns, 198,352
generic owner endpoint checks, 32 chamber-0 LDL checks, and all thirteen
mutations.  Registry CSV/JSON parity is exact through C120; all 113 first-party
JSON files parse and the control scan is clean.

Fresh Lean build/axiom audit completed 1,067 jobs with only standard
dependencies.  A fresh temporary Rocq 9.1.1 compile/check closed all fourteen
audited theorem families.  Cache and generated-object scans are clean outside
the intentionally retained Lean `.lake` cache.  Exact commands, hashes, and
scope are in `evidence/C120_VERIFICATION_2026-08-31.md`.


## Progress 2026-08-31 (registered C121)

The unresolved C118 interval recorded immediately after C120 has now been
closed on the no-go side for the frozen prototype and a bounded coefficient
box.  This supersedes the earlier diagnostic's statement that the prototype
still lay in the available upper window; it does not erase the diagnostic or
turn it into a strong-duality computation.

The five largest dual-gap chambers `49,64,70,73,74` were subdivided into four
equal pieces in reciprocal coordinate `u=1/t`.  Together with the 82
unchanged chambers this gives 102 phase pieces, 204 rational epoch duals,
62,832 nonnegative weights, and 408 exact endpoint positive-definiteness
checks.  The accepted exact replay proves

`normalized dual upper < -83/2000`.

The C119 prototype right side is strictly larger, with gap greater than
`1/2000`.  More generally, `eta_2<0`,
`Delta V=3440812085/9234857208>0`, `epsilon,A>=0`, and `e_2=0` imply the
necessary condition

`B > 287434930599/860203021250 > 1/3`.

Thus every `0<=B<=1/3` fails on this fixed row in the current cone.  Lean 4
checks the frozen rational implication and Rocq 9.1.1 supplies a smaller
independent empty-assumption audit.  Neither assistant formalizes the SDP
certificate or C058.

The canonical certificate has payload SHA-256
`ee4074acc3e57c5f7fe991a74b7f33ad2424631ec75b814ab0c70c80cde11cff`.
Five focused tests pass and all 18 mutations are rejected.  The full
cache-suppressed Route-C tree passed 371 tests across 35 suite files in
357.481 seconds.  Registry parity is exact through C121 and all 114
first-party JSON artifacts parse.

The next C058 experiment is an exact outer coefficient bank using both signs
of `Delta V`, same-multiset ordered histories, and bounded ordered profile
coordinates, followed by 32 marks or a scalable critical-compatible family
and one global C103 owner/boundary ledger.  C058 remains the sole primary
bottleneck and the global status remains `UNRESOLVED_AT_HARD_LIMIT`.


## Progress 2026-08-31 (registered C122--C124)

The first exact outer coefficient bank has now been built.  C122 promotes the
C120 negative-`Delta V` full-phase dual and combines it with C121.  The two
exact necessary scalar bounds leave a nonempty interval, so they do not
refute common scalar storage.

C123 promotes the best same-multiset ordered permutation to a canonical exact
certificate.  Its 140 complete-phase chambers contain 280 epoch duals and
86,240 nonnegative rational weights; all 560 endpoint slack matrices pass
fraction-free Bareiss/Sylvester positivity.  The normalized upper is below
`301218263143/8263918620000`.  Together with a clean exact C121 fence this
leaves

`1341/4000 < B < 4753/10000`,

of exact width `2801/20000`.  Four focused tests pass and ten mutations are
rejected.  This is strict coefficient narrowing, not a contradiction.

The comparison exposed a load-bearing convention: the model uses
`T=(a_15-a_8)/8`, so a permutation can change the complete phase.  C120 uses
`[553/8,553/4]`, while C123 uses `[297/4,297/2]`.  A nonanticipating phase-base
rule must be frozen, or representative independence proved, before theorem
use.

C124 proves a minimal chronological dyadic-suffix storage column.  For every
positive dyadic shell it lies in `[0,1)`, is scale invariant and endpoint
nonanticipating, and its finite decreasing-weight Abel increments are bounded
by the first weight.  Its exact increments on C118, C120, and C123 are
`601940/4033029`, `-13171/58179`, and `51059/581790`.  In particular it
distinguishes the same-multiset C120/C123 rows in sign, unlike the scalar C119
coordinate.

Registry parity is exact through C124 and all 118 first-party JSON artifacts
parse.  The next experiment exactifies two further ordered rows and solves the
resulting rational `(B,C)` outer LP.  C058 remains the sole primary bottleneck
and the status remains `UNRESOLVED_AT_HARD_LIMIT`.


## Progress 2026-08-31 (registered C125)

Two further same-multiset rows were exactified for the C124 chronological
suffix column.  Index 12 contributes 149 chambers, 298 duals, 91,784 weights,
and 596 endpoint PD checks with normalized upper below
`42845139/1000000000`.  Index 3 contributes 155 chambers, 310 duals, 95,480
weights, and 620 endpoint checks with upper below
`6627733/100000000`.  Independent discovery replays and the promoted
canonical C120-model replay both succeed.

The resulting five-row two-column audit does not separate

`epsilon=A=1/1000`, `B=1/2`, `C=1/10`, `e_2=0`.

Exact rational log enclosures put every stored normalized dual upper more than
`1/10000` above the corresponding candidate target.  This proves only that
the present necessary-side dual bank is feasible; no primal phase witness or
local lower bound has been constructed.

The focused C125 family passes four tests and rejects twelve mutations.
Registry parity is exact through C125 and all 121 first-party JSON artifacts
parse.  The next diagnostic places C120 and C123 on the common
permutation-invariant completed-shell phase `T=H_3/8`.  C058 remains open and
the status remains `UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-31 (registered C126)

The C120/C123 same-multiset pair was replayed on the common completed-shell
phase `T=H_3/8=82`, `[82,164]`, with `rho=9/16`.  The C120 source contains
147 chambers, 294 epoch duals, 90,552 rational weights, and 588 exact endpoint
positive-definiteness checks, with normalized upper below `89/1000`.  The C123
source contains 135 chambers, 270 duals, 83,160 weights, and 540 endpoint
checks, with upper below `87/2000`.  Integer Bareiss/Sylvester reconstruction
and an independent Fraction-LDL replay both succeed.

With `epsilon=A=e_2=0` and one common scalar `B`, C121 and the common-phase
C123 row leave

`1341/4000 < B < 1133/2000`,

an outward-rounded positive width `37/160`.  Noncontradiction is checked
independently of that rounding: the exact rational witness `B=1/2` lies above
the exact C121 lower and below both exact common-phase upper bounds.  Thus
eliminating the row-dependent phase base does not create a scalar
contradiction.  The completed-shell rule has
not been proved admissible in a global C103 ledger, and no exact primal for a
surviving coefficient vector has yet been constructed.

The focused C126 family passes five tests and rejects twelve mutations.  Registry
parity is exact through C126.  C058 remains the sole primary bottleneck and
the status remains `UNRESOLVED_AT_HARD_LIMIT`.


## Progress 2026-08-31 (registered C127)

The fixed C125 vector

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`

was audited against the C120 and C123 stored dual objectives on the C126
common phase `[82,164]`.  Exact rational log enclosures and the complete C126
dependency replay prove

- C120: `normalized_dual_lower - target_upper > 21/500`;
- C123: `normalized_dual_lower - target_upper > 7/1000`.

Thus these two stored necessary-side dual certificates do not separate the
candidate after the adaptive phase discrepancy is removed.  This is not a
primal witness and does not prove feasibility of the local master inequality.
The C127 family passes five focused tests and rejects thirteen mutations.

The next finite gate is now exact complete-phase primal construction for this
candidate, with the tightest failing chamber or epoch used to choose any
minimal ordered quarter-mass extension.  C058 remains the sole primary
bottleneck and the status remains `UNRESOLVED_AT_HARD_LIMIT`.


## Progress 2026-08-31 (registered C128)

The fixed C125/C127 vector

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`

was next tested against a strictly stronger chamberwise requirement on the
common phase `[82,164]`, `rho=9/16`, in the frozen independent epoch-block,
zero-row-sum PSD cone.  The stored exact C123 local duals separate precisely
chambers `0,1,...,21`; the first is `[82,493/6]`.  On chamber 0 the target is
`>9/250`, the normalized local-dual upper is `<39/2000`, and their deficit is
`>33/2000`.  A pointwise lower bound throughout a chamber would imply the
same lower bound for its positive `dt/t` average.  These exact separations
therefore refute the uniform per-chamber and all-phase pointwise lower at the
fixed target in this frozen cone.

The C120 stored-local-dual separation count is zero.  This means only that
this particular one-sided test does not reject the C120 candidate; it is not
a C120 primal-feasibility certificate.  C128 likewise does not make the
physical phase impossible and neither proves nor refutes complete-phase
integrated primal feasibility.  The separate floating integrated-primal
screen remains heuristic and is not promoted to a canonical proof claim.

Phase redistribution is thus load-bearing for any surviving use of this
candidate.  The next primary finite gate is an
exact phase-integrated rational primal bank that uses later chamber surplus
to pay the early C123 deficits,
while retaining the full boundary, terminal, and owner ledger.  C058 remains
the sole primary bottleneck; Q1, Q2, arbitrary rank, and the global C103
ledger remain open, and the status remains `UNRESOLVED_AT_HARD_LIMIT`.

C128 final SHA-256 values are: verifier
`d6cc32966f58bc6381d8673901f5438e2c2570d20bcd07f8662192a5c3f3dea2`;
certificate JSON
`6bf92fd94021878dbac450668fb5ccf8d6391e67d628c1bd1dd6a22f68c794e5`;
compact payload
`0e7a8418b47d516297ef327c46efb014c8cac9d0636d8517219e45dd0cfc47ad`;
test
`52c1bd72aa89ad9d85785ddf0cb5e0f88a34b2285159d6447aeeae89c9ccfd07`;
and explanatory MD
`f87c3685b3929a20b8815c5f455d5820446dfcd033cb09d349d93d0da5e588b0`.


## Progress 2026-08-31 (registered C129)

C129 exactified rational primal Gram factors for selected C123 chambers on the
same fixed candidate and common phase.  The selected bank always contains the
exact deficit block `0,...,21`.  In the frozen C128 numerical surplus order,
adding the top six chambers `120,122,126,132,133,134` leaves an exact negative
raw aggregate margin.  Adding chamber `88` gives a 29-chamber sparse-seven
bank with 58 factors, raw margin `>1/15000`, and normalized margin
`>99/1000000`.  The 32-chamber robust-ten bank has 64 factors and proves raw
margin `>143/400000` and normalized margin `>103/200000`.

The robust bank exactly replays 12,140 generic owner rows, 24,280 generic
endpoint inequalities, and 23,745 collapsed-endpoint owner rows.  Every
factor is a positively scaled integer Gram matrix with exact zero-row-sum
embedding and rank witnessed modulo two pinned primes.  Independent rational
recomputation found minimum strict owner margin
`333523392719/67812500000000000>0` and no load-bearing defect.  The top-six to
sparse-seven sign change is minimal only inside the frozen numerical ordering,
not over all possible chamber selections.

C129 is not a complete-phase primal witness: it covers only 32 of 135
chambers.  The remaining 103 chambers require 206 epoch factors and cannot be
filled by zero extension, since chamber 22 already has exact positive demand
`1/32`.  The C130 acceptance target is therefore all 135 records and 270
factors, owner census totals 51,355 generic rows, 102,710 endpoint
inequalities, and 100,183 collapsed-endpoint rows, together with a strictly
positive exact full aggregate raw margin.  Even that finite completion would
leave the separate C103 nonanticipating phase/owner/Abel ledger obligation.
C058 remains the sole primary bottleneck and the global status remains
`UNRESOLVED_AT_HARD_LIMIT`.

C129 final SHA-256 values are: verifier
`b211bae87c7a29bd9a4ec32fbe53f104b6366f922c743f6273aa61e7d800ddb6`;
certificate JSON
`bdd23df5520408b09d6a9a3f8126a2ecd6b5ee68c18d3b5f5e7eb9e3c3375cf9`;
compact payload
`b1c484ec31d809d3abdca7331e4f9410feb39f007800405745ab3f22ea81241d`;
factor bank
`9f4bf884515930a03502f785e0d6381d81fdd11be7cb01648370f19ce2b58e15`;
test
`f994f505f8c1b5c6555a9e1165116911e386b8d73cff3ddea0339d8d6f1ac874`;
and explanatory MD
`94315bdedb97e41b4fe62a1b6cbd37399e2bae4b7c2b2c809c7047d8c9f47cc1`.


## Progress 2026-08-31 (registered C130)

C130 completes the exact finite C123 common-phase primal bank.  For the fixed
candidate

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`,

all 135 chambers on `[82,164]` now have both epoch factors: 270 rational Gram
factors with common denominator `100000000`.  Exact ranks range from 9 to 25
and sum to 4288.  The verifier replays 51,355 generic owner rows, 102,710
generic endpoint inequalities, and 100,183 collapsed-endpoint rows.  It also
checks 31,805 generic and interior structural-zero rows, 62,713 collapsed
structural-zero rows, 10,395 state evaluations, 20,790 separate epoch owner
recoveries, endpoint objective counts 540 separate / 270 weighted, and
interior objective counts 270 separate / 135 weighted.  The exact minimum
active owner slack is
`1137298595103/235750000000000000>0`.

The complete rational log enclosure gives raw margin `>1/400`, normalized
margin `>91/25000`, and width `<1/10^26`.  Thirty-seven chamber pieces are
negative, exactly `0--26,31--35,59,60,77--79`; the remaining 98 are positive.
The positive result therefore depends on complete phase redistribution and is
not a pointwise or every-chamber positivity claim.

Temporary floating solver data were used only for discovery and stripped from
the canonical payload.  The accepted certificate contains exact fields only.
Nine focused tests pass, 28 mutations are rejected, and an independent
canonical audit reports no P1/P2 defect.

This closes only the fixed C123 common-phase primal in the frozen independent
aggregate cone.  It proves neither a C120 primal nor every-row feasibility,
the C103 phase/Abel boundary-terminal/global-owner ledger, representative
independence, a local master, arbitrary rank, C058, Q1, Q2, novelty,
publication acceptance, or prize eligibility.  The next executable finite
priority is to exactify the complete C120 common phase, creating a two-row
finite primal bank, and then attack the cross-row/global C103 ledger.  No
two-row sufficiency claim is made.  C058 remains the sole primary bottleneck
and the global status remains exactly `UNRESOLVED_AT_HARD_LIMIT`.

C130 final SHA-256 values are: verifier
`84c540a1c259a265064eb8fb7287c8b4d696ec64719b9d9a50738efa5fb7415b`;
certificate JSON
`16dec361580b0f070c660a12f8f3f60a57baff0bbf10ae9e5c2f8e4ae13fb37d`;
compact payload
`99b4af93ff095b9a8e03208e66860e2b3c15e6789ab54e7aa1943312207b2a14`;
factor bank
`7d16af8eeba989c068e3d08ffaeff394cbf181a95cefa380834471f024d15173`;
test
`0ae8a46e75e390814a69bd300b834fb498fce266030d8dce5afb498bdfd6bffa`;
and explanatory MD
`8db181e5e64f0e13c10e141cf66f7f55139d615c043b0961a04d70ff2e753a7e`.

## Progress 2026-08-31 (registered C131)

C131 completes the exact finite C120 common-phase primal bank for the same
fixed candidate used by C127--C130,

`epsilon=A=1/1000`, `B=1/2`, `C_rt=1/10`, `e_2=0`.

All 147 chambers on `[82,164]` have both epoch factors, for 294 exact rational
Gram factors in the frozen independent epoch-4/epoch-8 zero-row-sum PSD
aggregate cone.  Exact ranks sum to 3205.  The first 115 chamber records reuse
the pinned provenance construction with scale `1/D^2`; the final 32 records
use the reduced scale `1/(D^2 midpoint)`.  This split is recorded for replay
and does not enlarge the mathematical scope of the claim.

The exact census is 53,312 generic active rows, 37,240 generic zero rows,
106,624 generic endpoint inequalities, 104,080 collapsed active rows, 73,440
collapsed zero rows, 53,312 midpoint active rows, and 37,240 midpoint zero
rows.  The minimum active slack is

`305733/87500000000000>0`.

Complete rational log integration gives raw margin `>21/1000`, normalized
margin `>3/100` and `<31/1000`, and every relevant enclosure width is
`<1/10^26`.  All 147 integrated chamber pieces are positive.  This last fact
is a statement about the certified chamber integrals, not an all-phase
pointwise theorem.

C131 and C130 therefore supply an exact two-row finite primal bank for the
fixed C120/C123 rows on the common phase.  This is not a two-row sufficiency
theorem and proves neither every-row validity nor representative independence.
The completed-shell phase has not been proved globally admissible, and the
cross-row/global C103 phase/owner/Abel boundary-terminal ledger has not been
constructed.  Arbitrary rank, C058, Q1, Q2, novelty, publication acceptance,
and prize eligibility remain open.  C058 remains the sole primary bottleneck
and the global status remains exactly `UNRESOLVED_AT_HARD_LIMIT`.

C131 final SHA-256 values are: verifier
`5f7f1a1928e413ec8808279c57da99a401a01bb3a52a1fe8bca764bacf2c3a4a`;
certificate JSON
`6b28874a6c0ffe3d36a5ada27a3b466e0dbcd19447a2da0fb501b0ccc7df5afc`;
compact payload
`5012236aa28d76867d94926a26d00ffacf602952e93358818594907f7ea7d477`;
factor bank
`bb8629e4248bc6467fe6617f319e74f42457350dd797e821e320a7dc8b0477e8`;
test
`7a8d60b8fd8d500f75a56d26243dae946029ed6b644097d49e5d5f872a4c6f83`;
and explanatory MD
`bdfbb75b19ef0ddb59b13b42cb51a22368418d0566bb75ff8d4e67a0dd24a214`.
The final family passes `8` focused tests and rejects `4` mutations.

## Progress 2026-08-31 (registered C132--C134)

C132 supplies an explicit 32-mark Golomb stress fixture of span 7084.  All
496 positive differences are distinct, and exact log enclosures give a finite
onset-4 `C=2` prefix cap through 32 marks.  The naive affine paste of the old
local C130/C131 owner banks nevertheless fails: 152 of 692 natural epoch-16
owner rows are negative.  Exact phase alignment in that affine family also
forces a repeated difference `427q` for every positive integer dilation `q`.
Only this paste family is closed.

C133 freezes the exact adjacent epoch-8/16 bookkeeping contract.  The two
four-scale edges have fourteen unique Abel rows after the four shared `A16`
occurrences are netted.  Both upper terminals and the live rank-15 past owner
remain.  Lean builds the commutative-ring identity, and an independent
Fraction verifier passes 512 deterministic fixtures, nine focused tests, and
eight mutation checks.

C134 reconstructs the entire omitted residual from 63 cross-half sources.
The primitive rank is 63, the 126 signed Gram generators have rank 78, and
the exact representation is `R16=X_plus-X_minus`.  The positive-only cone is
strictly separated by `q^T R16 q=-1/16`; hence signed expressibility is not
positive capacity.  The owner lift, ranks 15--18, and all nonzero finite C103
initial/final/upper-terminal slots are retained and independently replayed.

The Lean toolchain completed 1,069 jobs, and the new axiom audit reports only
`propext`, `Classical.choice`, and `Quot.sound`.  Rocq MCP is now reachable on
9.1.1: its minimal sandbox verification has empty assumptions, and the
existing independent `prefixScaleCurl` file again compiles with
`assumptions=[]`.  One obsolete `Stdlib` import probe failed under the minimal
Corelib layout before the corrected probes passed; this is recorded as an
import-selection error rather than a mathematical or server failure.

The next active computation is a fresh joint 32-mark cellwise epoch-8/16
positive-capacity LP/SDP on one common physical phase.  It must carry all 63
signed sources and the exact fourteen-row C133 ledger.  A relaxed solver
status, `optimal_inaccurate`, or a signed difference of PSD banks cannot be
promoted without independent PSD, owner, finiteness, phase, and exact replay.
C058 remains the sole primary bottleneck and the state remains exactly
`UNRESOLVED_AT_HARD_LIMIT`.

The same-day primary-source refresh found no theorem closing C058.  The most
concrete downstream candidate is a rank-uniform product-BMO testing lemma;
fixed-complexity Haar-shift and critical rectangle packing results remain
conditional on missing representation and testing hypotheses.  Martikainen
v1 is recorded with Theorems 1.3, 1.8, and 1.11 in their current roles.

## Progress 2026-08-31 (registered C135)

The next unused canonical ID was independently resolved as C135 after both
claim registries were found synchronized and sequential through C134. C135
records only the frozen D1 O0N1 complete-phase no-go.

The O0N1 16-mark row has 120 distinct positive differences,
`Delta V=-443620417/1928247678`, and `Delta Vrt=5034/96965`. On common phase
`[82,164]`, `rho=9/16`, coefficients
`(epsilon,A,B,C_rt,e_2)=(1/1000,1/1000,1/2,1/10,0)`, and the current
independent epoch-4/epoch-8 zero-row-sum PSD aggregate cone, the exact
refinement splits 60 of 134 parent chambers into four and retains 74 whole.
The resulting 314 pieces contain 628 epoch duals and 193,424 nonnegative
rational weights. All 1,256 endpoint Bareiss-PD checks pass; 480 refined epoch
duals strictly improve their parent objectives.

Exact 30-term rational atanh integration over the complete phase gives

`U^+<36849435771/10^12<18634061003/(5*10^11)<T^-`

and margin `>83737247/(2*10^11)>1/2500`. No chamberwise sign criterion is
used. The source SHA-256 is
`2949602baa0cb68aa3131bcb003fa2ac35156743bb2202e9a02f906ccf960c6b`;
the parent SHA-256 is
`93efb6b9846800f4025d72bd79536cc052f46f750e706b2966efa90928002912`.
The independent oracle and 10 focused tests pass, including exact semantic
partition/dual mutations and a controlled endpoint-PD failure.

By weak duality, O0N1 refutes the universal finite hypothesis that every
Golomb member of the specified frozen `4x8` cyclic same-multiset rotation bank
satisfies this candidate lower bound. It does not refute global representative
independence, Route C, or C130/C131. The earlier one-stored-dual-per-parent-
chamber `NO_SEPARATION` was a false negative for that stored classifier and
never established primal feasibility; no all-unsplit-dual optimality claim is
made.

Cross-row compatibility, global C103 ownership, nonanticipating phase
admissibility, arbitrary history/rank, C058, Q1, Q2, novelty, publication, and
prize eligibility remain open. The global status stays exactly
`UNRESOLVED_AT_HARD_LIMIT`.

## Progress 2026-08-31 (registered C136)

C136 tests the C133/C134 joint fixture without pasting C130/C131. At the exact
midpoint `t=17745/32`, a fresh 100-channel graph-Laplacian capacity with 57
positive rational roots satisfies all 1,192 direct epoch-8/epoch-16 owner-cell
constraints. The exact matrix is PSD, has zero row sums and rank 51; its
margin is

`2D-P=270571186627/9402974208>0`.

All 596 epoch-16 rows use full `M16`, so the 63 cross-half residual sources
are retained rather than replaced by two quarter-scaled `M8` blocks. The
stored 57 coefficients are uniquely reconstructed from 57 exact tight rows.
The canonical verifier, eight focused tests, ten rehashed mutation gates, and
an independent stdlib-only oracle all pass.

This does not complete the finite joint gate. The separately instantiated
one-sided box carrier has all fourteen C133 rows but is not the direct-demand
potential: on an exact cell its total is zero while weighted direct demand is
`225/32768`. Its nonzero terminals diagnose only that wrong carrier. A later
same-atom audit shows that the correct direct-`M` scale-4 states vanish on
this fixture. The next computation must therefore use the exact C133 weights
and reoptimize the graph price, while retaining the formal terminals and
one-time owners. C058 and the global problem remain open.

## Progress 2026-08-31 (registered C137 and same-atom correction)

C137 upgrades the carrier mismatch to an exact local no-go. Two adjacent
cells have the same full 100-channel state, zero supported-root features, and
zero direct demands, but different C133 box-carrier totals. A second
same-state pair changes both terminal rows. This rules out every pointwise
memoryless recovery of that carrier from the current graph, while leaving
same-atom and nonlocal mechanisms open. Eight tests, eight mutations, and an
independent stdlib oracle pass.

The direct matrices themselves supply the correct next potential. With
`C8=B`, `C16=B+U8`, and `C32=B+U8+U16`, the C133 prefix increments are exactly
the direct quadratics. This removes the artificial box-carrier link and makes
the ledger total the weighted direct demand. Exact terminal enumeration gives
zero at scale 4. The current C136 graph nevertheless fails the weighted price
test by `379481718413/9402974208`, so a new weighted optimization is required.

## Progress 2026-08-31 (registered C138 weighted same-atom witness)

C138 closes the corrected fixed-midpoint weighted gate. The cumulative
potential is reconstructed from the direct matrices as `C8=B`,
`C16=B+U8`, and `C32=B+U8+U16`; neither prefix value nor its increments are
optimization variables. Exact replay checks 2,020 increment equalities and
the C133 fourteen-row identity on 202 cells. All fourteen formal keys remain,
but only five integrated rows are nonzero; both upper terminals are retained
and evaluate to zero.

At `t=17745/32`, the new 57-root rational graph witness has exact rank 51 and
satisfies all 1,192 weighted epoch-8/epoch-16 owner rows. Its pre8/rank-7
share is also nonnegative on all 149 cells, with census `145 zero / 4
positive` and integral `6489/256`. The single unweighted physical price and
weighted demand give

`D=1305537/16384`,
`P=2367807877181/16716398592`,
`2D-P=296239592131/16716398592>0`.

The canonical verifier rejects 14 contract mutations, six focused tests pass,
and a stdlib-only oracle reconstructs the fixture, matrices, owner rows,
price, and ledger independently. Lean 4 separately checks the frozen
cumulative ledger algebra, with a 1,070-job build and only standard axioms.

This is not a full-history test: all integrated A8 rows and both terminals
vanish. It also gives no phase interval or arbitrary-rank theorem. The next
step is an exact phase-chamber continuation of the same witness, followed by
a complete factor-two phase bank and one nonanticipating global C103 owner
ledger. C058 and the main problem remain open.

## Progress 2026-09-01 (registered C139 fixed-Y chamber)

C139 keeps the exact C138 graph Y frozen and crosses all 150 global event
lines over the ambient critical band. The maximal connected closed feasible
chamber containing 17745/32 is [4425/8,555]. Its generic census is 149 cells
and 1,192 weighted owner rows, with 884 tight and 308 strict; pre8 ownership
is nonnegative and integrates to 6489/256. Both collapsed endpoints replay
exactly, and the decreasing margin is still
292559857297/16716398592 at t=555.

The immediately adjacent chambers fail by exact slacks -549/131072 and
-15/8192, proving maximality only for this fixed Y. The same-atom ledger has
two finer internal crossings, but all three affine row tables agree and all
fourteen formal rows sum to D(t). Both terminal rows remain identically zero.
The canonical replay, stdlib-only oracle, and 13 focused tests pass, including
11 adversarial mutation rejections.

The next computation is therefore a complete factor-two phase bank, not an
unjustified extension of this Y. Nonanticipating selection, nonzero history
and terminal stress, arbitrary rank, the global C103 ledger, C058, and the
main problem remain open.
