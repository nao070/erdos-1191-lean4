# Mathematical and Artifact Audit Notes — 2026-08-28

## 1. Research status

No complete solution of Erdős Problem #1191 is claimed. The endpoint-imbalance theorem is a new project-internal finite result and a potentially meaningful advance beyond statistics determined only by the difference spectrum. The asymptotic coupling needed for Question 1 remains absent.

## 2. Independent rerun completed

The supplied endpoint code was rerun in the mounted workspace:

- `pytest -q`: 15 passed;
- `certificate.py`: 10,890 checks;
- `diameter_certificate.py`: 15,345 checks;
- `required_levels_certificate.py`: 16,380 checks;
- total: 42,615 exact machine checks.

The rerun output is preserved under `integrity/REVERIFICATION_2026-08-28.log`.

## 3. Exact duplicate audit

The second uploaded ZIP contained 28 files. Every one of those files had a SHA-256 match in the first ZIP under `core_workspace/endpoint_variance/`, including its six `__pycache__` entries. No unique mathematical, source, certificate, or log content was found in the second ZIP.

Therefore the new handoff does not nest or duplicate the second ZIP.

## 4. Original endpoint checksum defect

The original file `core_workspace/endpoint_variance/SHA256SUMS` includes a checksum line for `endpoint_variance/SHA256SUMS` itself. A static file cannot in general contain its own final cryptographic hash, so the manifest check reports exactly one failure: its self-entry.

This does not indicate corruption of the theorem note, code, tests, or certificates. Every other listed endpoint file checked successfully when the command was run from the correct parent directory. The top-level continuation manifest also checked successfully.

The original defective manifest is retained as:

`integrity/ORIGINAL_ENDPOINT_SHA256SUMS_WITH_SELF_ENTRY.txt`

The new package manifest excludes itself by construction.

## 5. First failed checksum run was a working-directory error

An initial check was run inside `core_workspace/endpoint_variance/` even though the manifest paths begin with `endpoint_variance/`. That produced 23 “file not found” failures. Re-running from `core_workspace/` fixed all path failures and exposed only the self-hash defect described above.

Both logs are preserved to make the distinction auditable.

## 6. Sharpness nuance: unrestricted finite sets versus Sidon sets

The mandatory-level theorem states

\[
\operatorname{Var}E_N\ge
\frac{m(m^2-1)(m^2+11)}{180N},
\]

with equality for `A={0,1,...,m-1}` and `N=m`.

For `m>=3`, this consecutive set is not Sidon: many positive differences repeat. Thus the theorem is sharp over arbitrary ordered finite sets, but the supplied equality example does not prove sharpness within the Sidon/Golomb class.

This creates a legitimate finite optimization problem: minimize the exact gap-moment variance over Golomb rulers. A Sidon-specific strengthening may exist. It would still require a cross-scale upper budget to resolve #1191.

## 7. Explicit dependence on N above the diameter

For a fixed `m`-point prefix of diameter `D` and every `N>D`, define

\[
T_m=\sum_{k=1}^{m-1}g_k k(m-k),
\qquad
S_m=\sum_{k=1}^{m-1}g_k k^2(m-k)^2.
\]

Then the exact formula is simply

\[
\operatorname{Var}E_N=\frac{S_m}{N}-\frac{T_m^2}{N^2}.
\]

Therefore averaging only over moduli larger than the same prefix diameter may collapse to the same two gap moments. A genuinely new multiscale method likely must vary prefixes, include moduli below the diameter, retain length slices, or use covariance/telescoping structure.

## 8. Endpoint theorem versus difference spectrum

The homometric pair proves an exact separation: equal positive-difference spectra do not determine offset variance. This means the new quantity is not subject to the previously identified barrier for separable nonnegative mixtures of fully averaged quadratic means.

However, after expanding the variance, the new information is quartic. Any proposed Sidon upper budget must control pair-pair interactions, not only individual difference multiplicities.

## 9. Zero modes are structural, not numerical accidents

`{0,1,N}` produces a two-edge directed cycle modulo `N`, hence exact zero variance. More generally, every Eulerian short-pair residue graph is a zero mode. A valid lower theorem must be cross-scale or density-sensitive; a pointwise positivity theorem is false.

Near-zero variance should be interpreted as a near-balanced flow problem. The relevant norm is `H^{-1}`, which emphasizes low-frequency placement and is stronger than merely knowing the multiset of imbalance values.

## 10. Dense block gluing language corrected

The original approach registry and counterexample ledger sometimes called the tested dense-translate obstruction “fundamental” and concluded that the entire algebraic/recursive route could not yield asymptotic progress. The available evidence is finite and the referenced source/raw files were not included in the uploaded ZIP.

The canonical registry now uses the narrower conclusion:

- naive near-adjacent translated dense-block gluing is blocked in the tested model;
- algebraically coordinated blocks, global redesign, finite-field towers, and nonlocal alteration remain logically open;
- older numerical details are reported but not independently reproducible from this handoff.

The original ledgers are archived unchanged for traceability.

## 11. Legacy reproducibility gap

The current ZIP refers to older code and raw data that are absent. Those claims must remain marked as reported computational evidence until the complete old workspace is recovered. See `MISSING_REFERENCED_ARTIFACTS.md`.

## 12. Literature-tool audit limitations

- The public #1191 tracker and current arXiv records were accessible.
- Exa found the central current sources, but some metadata parsing was imperfect; primary arXiv/journal pages were used as authority.
- SciSpace found Cilleruelo and older material but did not surface the newest O’Bryant papers in the targeted result set, consistent with indexing lag.
- Consensus could not search because the monthly quota was exhausted.
- Firecrawl paper search found O’Bryant I/II, Cilleruelo, Táfula, and related papers; ordinary Firecrawl search was partial and one exact query returned no results.
- Site-restricted public searches of zbMATH, MathSciNet, Project Euclid, EuDML, MathOverflow, and Math-Net.Ru were incomplete or noisy. No negative search result is treated as proof of absence.
