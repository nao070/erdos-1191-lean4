# Wave 7 continuation: complete birth renewal and the infinite-survival boundary

**Date:** 2026-08-28  
**Canonical status:** `UNRESOLVED_AT_HARD_LIMIT`  
**Prize claim:** not ready

## 1. What Wave 7 changed

Wave 7 closes the bookkeeping gap left by the Wave 6 half-rhombus ledger.
At each dyadic epoch `m`, it includes every old--new rank lag
`1 <= k < 2m` and every difference internal to the newborn block.  Over a
terminal `M=2^J` prefix these birth families partition all `binom(M,2)`
endpoint pairs exactly once.

For each family `F`, let `q_F` be its demand, `ell_F` its rank lag, and
`gamma_F` its exact upper activation threshold.  Golomb uniqueness gives

\[
 \sum_F q_F 1_{\{\gamma_F\le T\}}\le\lfloor T\rfloor.
\]

The rank floor

\[
 a_{i+\ell}-a_i\ge \ell(\ell+1)/2
\]

upgrades this to the wedge ledger

\[
 \sum_{\ell_F\ge K}q_F1_{\{\gamma_F\le T\}}
 \le \max(0,\lfloor T\rfloor-K(K+1)/2+1).
\]

After summing in `K` and integrating, one obtains the first genuinely
summable all-history arithmetic potential in this project:

\[
 \boxed{\mathcal W_2=\sum_F\frac{q_F\ell_F}{\gamma_F^2}
 \le 8\sqrt2<12.}
\]

This is a rigorous theorem for every finite epoch family and, by monotone
convergence, for all epochs of one infinite Golomb ruler.  The adversarial
audit checked every index, threshold, lag, normalization, and quantifier.
It repaired the harmless convention `R(T)=0` for `0<=T<1` and narrowed the
finite-window no-go to its proved affine class.

## 2. Why the summable potential still does not close Question 1

For the 512-mark Erdős--Turán ruler with `p=1423`, all prefixes from 256
through 512 satisfy the package's `C=1` envelope.  Exact rational evaluation
gives

\[
 \frac{Q_{256,00}}{N_{512}}
 =\frac{72931155410271048281010903}
 {26431687539869343576651464704}
 >\mathcal W_2(256),
\]

with positive comparison cross-product
`86781803501905775924014152122871`.

More strongly, for terminal-dependent Erdős--Turán rulers of size
`M=2^J`, the most recent
`R=floor((1/2)log_2 log M)` transitions satisfy one common critical envelope,
while

\[
 \sum_{s<R}\frac{Q_{m_s,00}}{N_{2m_s}}
 =\frac{R}{360}+o(R)\to\infty,
 \qquad
 \sum_{s<R}\mathcal W_2(m_s)=o(1).
\]

Since `H-E` is positive semidefinite, the same obstruction applies to the
fixed adjoint charge.  Therefore no fixed nonnegative constants `C_0,C_1`
can give a uniform finite-window inequality

\[
 \sum_s\langle H,Q_{m_s}/N_{2m_s}\rangle
 \le C_0+C_1\sum_s\mathcal W_2(m_s).
\]

The terminal ruler and prime change with `M`.  This is not one infinite
critical history, and it does not refute an estimate with a hypothesis that
certifies infinite extension of the same prefix.

## 3. Exact infinite-survival label

For a positive rational `C` and a normalized finite Golomb prefix `P` of
length `n`, form the rooted tree of Golomb extensions that obey

\[
 N_r\le\lfloor2Cr^2\log r\rfloor
\]

at every new rank `r>=n`.  Let `surv_C(P)` be its maximum extension height,
possibly infinity.  The tree is finitely branching because every next mark
has an explicit coordinate cap.  König's infinity lemma therefore gives

\[
 \boxed{\operatorname{surv}_C(P)=\infty
 \iff P\text{ lies on one infinite eventual-}C\text{-critical Golomb ruler}.}
\]

For a family born at `m`, set
`lambda_C(F)=surv_C(A_(2m))`.  An E–T terminal window certifies only a finite
lower bound for this label, and changing `M` changes the root.  Thus a theorem
conditioned on `lambda_C(F)=infinity` lies outside the finite-window no-go.
The label is a quantifier device, not yet an innovation estimate.

## 4. Renewal probes: two refutations and one finite theorem

Three exact candidates were tested.

1. **RH, one local hole per renewed epoch, is refuted.**  The authenticated
   64-mark fixture has values 21 and 22 from different epochs in `[21,22]`,
   giving exact margin `-1`.  A second witness occurs at `[382,383]`.
2. **HT, a direct harmonic epoch tax, is refuted.**  At threshold 3 the first
   two unit activations give exact margin `-1/6`.
3. **EST, the epoch-size threshold tax, survives only as a finite theorem:**

   \[
   S(T)+\sum_{m:\tau_{m,1}\le T}(m-1)\le\lfloor T\rfloor.
   \]

   EST is proved for every normalized Golomb ruler through eight marks,
   without a diameter assumption.  The cap-free eight-mark proof exhausts
   the only forced failure region: 4,934 bounded parents, 3,341,161 rulers,
   and 37,423,576 search nodes; the actual minimum is
   `tau_(4,1)=11`.  EST also survives complete scoring of the authenticated
   64/128-mark fixtures and 23 valid one-gap-swap variants.  These larger
   checks are finite and non-exhaustive outside the stated mutation class.

The cheap-child-half lemma proves that at every active epoch at least one
child half contributes all its adjacent differences below the activation
threshold.  Nested old halves prevent summing those contributions directly.
On the 128-mark fixture at `T=1198199/32`, the EST tax is 120, but the largest
distinct cheap-adjacent union has size 63; after boundary overlap only 57
genuinely new adjacent differences remain.  The exact unpaid debt is 63.

Even a universal proof of EST would add only a positive endpoint charge; it
would not alone prove the required `o(log J)` innovation budget.  The charge
must be linked to reset orientation and actual matrix innovation.

## 5. O'Bryant Lemma 9: exact black-box limitation

O'Bryant's Lemma 9 is the closest checked mixed old--new gluing theorem.  For
an old `n`-mark ruler it guarantees deletion of at most `B_n=binom(n,2)`
candidate marks.  If this scalar guarantee is the only certificate of even
one survivor, the candidate needs at least `B_n+1` marks and hence window
length at least `binom(B_n+1,2)+1`.  The separated first new prefix must obey

\[
 N_{n+1}\ge N_n+\binom{B_n+1}{2}+2=\Omega(n^4).
\]

For every fixed critical constant this eventually exceeds
`2C(n+1)^2 log(n+1)`; for `C=1` the analytic obstruction holds for every
`n>=8`.  The worst deletion count is uniformly sharp for some separated,
very sparse Sidon candidate blocks.

This rules out only naive black-box iteration of the worst scalar guarantee.
It does not rule out structured blocks with a smaller actual conflict graph,
mixed-difference coding without large separation, or another gluing theorem.

## 6. Current primary-source boundary

The Wave 7 scoping review retained 316 deduplicated records from 14 successful
OpenAlex, Crossref, and arXiv query rounds and then verified selected theorem
statements against primary pages.  The closest ingredients remain:

- O'Bryant's quantitative separated-block deletion lemma;
- Riblet--Schehr compactness, yielding the conditional finite-tower-to-
  infinite-tower König route;
- Ma--Yi packing of separate internal difference spectra, which omits mixed
  differences;
- Hall/Alexeev--Mixon qualitative infinite completion, without coordinate
  control;
- Fang--Sándor lacunarity for two disjoint internal difference spectra,
  again without mixed-union uniqueness; and
- exact Kraft/graph amortizations with no proved Sidon encoding.

No checked primary source supplies either the required all-prefix critical
Sidon tower or the infinite-history innovation budget.  This is a bounded,
qualified null, not a novelty or nonexistence theorem.

Plugin limitations are part of the audit trail.  Consensus was blocked by
its 30/30 monthly quota with reset reported for 2026-09-01.  SciSpace returned
mostly adjacent results, duplicated Fang--Sándor once with malformed
metadata, and omitted the current central O'Bryant paper in the broad query.
A separate Exa pass ran seven searches and requested 70 candidate results.
Firecrawl's research index ran three `k=12` searches (36 candidate records),
with three records inspected and three question views; its final hosted web
query returned generic listing pages and was marked bad.  These Exa and
Firecrawl counts are discovery volume, not 106 distinct verified papers and
not part of the 316-record scripted deduplication.  Discovery candidates were
never used as theorem authority; official primary pages controlled every
retained claim.

## 7. Exact next theorem

The highest-value remaining target is the following **infinite-survival-
conditioned debt-repayment/innovation budget**.

> Let `A` be one infinite Golomb ruler satisfying
> `N_n<=C n^2 log(2n)` eventually.  At every dyadic epoch attach the complete
> birth families, cheap-child orientation, unpaid overlap debt, and the label
> `lambda_C(F)=infinity`.  Prove that repeated old-cheap renewals repay their
> debt through previously unused non-adjacent differences or equivalent
> integer-capacity slack, with a charge that quantitatively dominates the
> actual newborn-shell and mixture terms of `Q_m`, and deduce
> \[
> \sum_{j\le J}\langle H,Q_{m_j}/N_{2m_j}\rangle=o(\log J).
> \]

A valid proof must use one fixed infinite branch, not changing terminal
windows; distinguish adjacent overlap from genuinely unused differences;
and connect its charge to `Q`, not merely to EST or `W_2`.

The secondary Question 2 route is finite feasibility plus König: for fixed
`C,d`, prove that for every depth `M` there is a normalized length-`M` Golomb
ruler satisfying `a_k<=Ck^2(log(2k))^d` for every `k<=M`.  Finite branching
then yields one infinite tower.  O'Bryant's worst-guarantee gluing cannot
establish this, so a structured mixed-difference construction or a whole-
prefix existence proof is required.

## 8. Canonical Wave 7 files

- `endpoint_variance/WAVE7_GLOBAL_BAND_RENEWAL_POTENTIAL_2026-08-28.md`
- `endpoint_variance/WAVE7_ADVERSARIAL_AUDIT_2026-08-28.md`
- `endpoint_variance/wave7_band_renewal_probe_results_2026-08-28.md`
- `endpoint_variance/WAVE7_GLUE_DELETE_NO_GO_2026-08-28.md`
- `../research_sources/wave7_literature_state/PRIMARY_SOURCE_AUDIT.md`
- `../research_sources/wave7_literature_state/QUERY_LOG.md`

The exact verifiers are `complete_birth_ledger.py`,
`test_complete_birth_ledger.py`, `wave7_band_renewal_probe.py`,
`test_wave7_band_renewal_probe.py`, and
`wave7_glue_delete_no_go_test.py`.  Their finite output supports only the
scope stated in the proof notes.

No solution, disproof, infinite critical construction, or prize-ready claim
is asserted.  The status remains `UNRESOLVED_AT_HARD_LIMIT`.
