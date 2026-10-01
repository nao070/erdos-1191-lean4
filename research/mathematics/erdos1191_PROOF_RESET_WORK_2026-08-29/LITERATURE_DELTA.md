# Erdős Problem #1191 — literature delta

Search dates: 2026-08-29--2026-08-30 (Asia/Tokyo)  
Evidence label: `LITERATURE_QUALIFIED_NULL`

## Live official status

The live HTML at `https://www.erdosproblems.com/1191` was fetched on
2026-08-29 with a forced-live Firecrawl render after the generic reader
received HTTP 403.  It currently marks #1191 `OPEN`, displays `$1000`, reports zero proof
claims, and gives exactly the two questions recorded in this package.  The
page says it was last edited 2026-04-06.  This is a status check, not evidence
that every unpublished claim has been found.

## Primary sources checked

### O'Bryant, arXiv:2606.28651v3

Version 3 was submitted 2026-07-26.  Theorem 1 proves for every
`g`-Golomb ruler `A`

`liminf A(n)/sqrt(n/log n)<=2*sqrt(g)/sqrt(log 2)`.

For `g=1` this is an explicit constant improvement within the classical finite
liminf theorem; it does not make the constant zero and therefore does not
settle Q1.

The original LaTeX, Section 3.1, explicitly raises four architecture ideas:

1. average over more than one block width `N`;
2. treat block occupancies as conditional expectations and seek a reverse
   martingale;
3. replace energy by an entropy inequality;
4. exploit failure of the smooth profile which makes weighted Cauchy sharp.

Section 5 asks a finite fine-distribution question over several partial
block endpoints.  These are genuine primary-text motivations for Route C,
not proved improvements.

### Táfula, arXiv:2607.20753v1

Submitted 2026-07-22.  It proves density restrictions for zero-sum linear
forms and recovers the classical phenomenon for `(1,-1)`.  It does not prove
the zero value in Q1 and does not provide the Q2 construction.

### O'Bryant, arXiv:2607.23795v1

Submitted 2026-07-26.  It extends explicit finite liminf constants to even
`B_h` sets.  At `h=2` it specializes to the same Part-I constant and does
not improve Q1 to zero.

### Ma--Yi, arXiv:2608.13739v1

Submitted 2026-08-13.  It studies families of fixed-`t` finite Golomb rulers
whose difference sets are mutually disjoint and determines when their
union almost covers `[1,U]`.  This is a new post-v3 adjacent source found in
the delta search.  It neither constructs one compatible infinite Sidon set
nor supplies an all-scale counting lower bound, so it is not a direct Q1 or
Q2 result.  Product-scale finite difference families may be a Route-D gluing
adversary/template only after cross-stage uniqueness is proved.

### Hou--Zhao, arXiv:2607.01169v2

Originally submitted 2026-07-01; the current v2 was checked.  This is a
finite-Sidon result, not an infinite-density
theorem: it proves

`F(N)<=sqrt(N)+0.9435*N^(1/4)+O(1)`.

Its original LaTeX Section 2 is nevertheless a concrete Route-C mechanism.
Several smoothing kernels are placed in a Hilbert direct sum; the individual
kernels need not satisfy the boundary covering inequality, while their
weighted combination does.  The resulting exact master inequality is

`k^2 <= (N+bH-1)*(1+a*(k-1)/H)`.

Thus this construction is strictly stronger than taking a nonnegative average
of separately valid scalar bounds and escapes the elementary convex-ratio
no-go recorded in `route_probes/ROUTE_C_MULTI_N_CONVEXITY_NO_GO.md`.
Section 5 identifies controlled cross-kernel terms as a possible extension,
but explicitly warns that positive semidefiniteness of the coefficient matrix
alone is insufficient: the combined correlation kernel must also stay
nonnegative at every nonzero shift.  The paper only improves a finite
second-order term; it does not yield the all-scale decorrelation or entropy
loss required for Q1, and it gives no Q2 construction.

## Discovery-tool results

| database/tool | exact query or action | inspected result | disposition |
|---|---|---|---|
| official page | `GET /1191`, 2026-08-29 | live statement/status/prize/proof-claim count | direct status authority |
| arXiv MCP | `("infinite Sidon" OR "Golomb ruler") AND (liminf OR thickness OR density)`, math.NT/math.CO, 2026-07-26..2026-08-29 | one finite-packing hit, 2608.13739 | adjacent, not direct |
| arXiv MCP | four exact-title/formula variants after 2026-07-26 | zero direct infinite-density hits | qualified null |
| arXiv LaTeX | 2606.28651v3 Sections 3.1 and 5 | multi-`N`, reverse-martingale, entropy, irregularity proposals verified | primary mechanism evidence |
| arXiv LaTeX | 2607.01169v2 Sections 2 and 5 | joint multi-kernel boundary cover and direct-sum energy; cross-correlation positivity caveat | finite-only Route-C mechanism |
| OpenAlex | quota first; exact three arXiv IDs; broad dated title/abstract query | metadata for 2606.28651, 2607.20753, 2608.13739; broad query zero | metadata/citation discovery only |
| Exa | five semantic status/infinite/finite queries, 55 raw results | official #1191, O'Bryant I/II, Hou--Zhao, Táfula, and adjacent pages | useful discovery, primary pages rechecked and duplicates filtered |
| SciSpace | full natural-language exact Q1 question | mostly classical or adjacent records; no direct resolution | discovery only |
| Firecrawl | forced-live scrape of the exact official #1191 URL (`maxAge=0`) | HTTP 200; open status, `$1000`, zero proof claims, 2026-04-06 edit date | direct status rendering; not novelty evidence |
| Consensus | exact infinite-Sidon liminf query, 2020--2026 | no search executed: 30/30 monthly quota exhausted; reset 2026-09-01 | access limitation, not a null result |

OpenAlex reported a `$1.00` daily budget before the calls and `$0.001` spent
for the broad search.  Its zero broad-query result is not used as a novelty
claim.

## Centered multiband follow-up

After the project-internal box telescope isolated a centered one- or two-band
prefix-changing carrier, all four user-requested discovery plugins were used
again against the narrower common-sign/capacity question.  Exa and Firecrawl
mainly resurfaced Hou--Zhao, Carter--Hunter--O'Bryant,
Ortega--Prendiville, and adjacent finite Golomb/Fourier work.  SciSpace
returned mostly general harmonic-analysis analogies after filtering, and the
Consensus query surfaced no theorem with the required compatible-history
ownership interface.

No checked hit supplied one valid inequality coupling a centered covariance
gain to the existing critical-history harmonic floor with opposite signs and
disjoint capacity.  This is a dated targeted retrieval null only.  It is not
evidence that the internal construction is novel or that no such theorem
exists.

## Cross-ratio box-dipole follow-up

After the exact identity

`C_(i,j)=-integral <e_i*K_T,e_j*K_T>dT`

was derived, the user-requested Firecrawl, Exa, Consensus, and SciSpace tools
were queried again with the narrower logarithmic-energy, interval-overlap,
cone, wavelet, and finite-horizon terminology.  Primary-source verification
identified:

- Frerick--Müller--Thomaser, arXiv:2209.05439 / Potential Analysis 2024,
  for a Fourier integral formula for mutual logarithmic energy;
- Bacry--Muzy, arXiv:cond-mat/0207094 / CMP 2003, for an exact cone-overlap
  logarithm whose finite-scale triangular part is
  `log(T/t)-1+t/T` and whose terminal plateau restores the missing term;
- Gneiting's Euclid-hat scale mixtures for triangular interval covariance;
  and
- Junnila--Saksman--Webb and Duplantier--Rhodes--Sheffield--Vargas for
  continuous scale decompositions of log-correlated fields.

These sources contain the ingredients, not the project-specific four-point
Sidon ledger.  No checked source states the exact box-dipole cross-ratio form,
its exact continuum log-phase periodization, or the required no-double-count
finite-horizon Gothic insertion.  This is a dated targeted qualified null,
not novelty evidence.  Full details and source cautions are in
`research_sources/signed_offdiag_2026-08-29/CROSS_RATIO_BOX_DIPOLE_PLUGIN_DELTA.md`.

## Ordered-Gram root-cone and rank-ramp follow-up

After the exact ordered interval-cell factorization was derived, Exa,
Firecrawl, and SciSpace were queried for its conjunction with SDDM/grounded
Laplacians, squared-rank distances, Sidon/Wave weights, and the active ramp
comparison.  Consensus remained unavailable because its monthly quota was
exhausted.  Primary-source checking located only general ingredients:

- Schoenberg's 1938 negative-type framework for squared Euclidean distances;
- Spielman--Teng's standard SDD/graph-Laplacian architecture; and
- Durfee--Peebles--Peng--Rao's SDDM/Laplacian-minor equivalence.

No checked source states the complete application-specific ordered
interval-cell Gram decomposition, the Wave dual identity, the active
rank-ramp comparison, and the finite-horizon Gothic ownership interface
together.  This is a dated targeted qualified null and an ingredient map,
not a novelty or absence claim.  Details and primary links are in
`research_sources/signed_offdiag_2026-08-29/ORDERED_GRAM_ROOT_CONE_LITERATURE_DELTA.md`.

The subsequent direct physical-coordinate result `M=D^tBD`, its
`2M=lambda` Gothic rewrite, and the terminal-free signed Haar-Abel bridge
remain within this same qualified ingredient boundary.  No new external
source claim was introduced for C079--C083.  In particular, no checked source
combines these identities with actual Sidon membership cells, shared-endpoint
ownership, and the finite multi-epoch SDP now required.  This is not a
novelty or absence claim.

## Sources not fully closed in this session

- zbMATH Open and MathSciNet review/citation chains still need an
  institutional or interactive search.
- Google Scholar is useful only for citation chaining and was not treated as
  theorem evidence.
- EuDML, Numdam, Project Euclid, Math-Net.Ru, and MathOverflow remain subject
  to false positives or incomplete public indexing.
- Human expert/citation-chain review remains mandatory before any public
  novelty claim.

## Delta conclusion

No checked source supplies a proof or disproof of either question.  The
official problem remains open.  The search conclusion is strictly a
qualified null.  The post-v3 finite difference-packing paper 2608.13739 does
not change the claim graph.  Hou--Zhao 2607.01169v2 supplies a rigorous example
of a joint multi-kernel mechanism that is not mere convex averaging, so it
sharpens the design requirements for Route C without proving any new
implication toward Q1 or Q2.  O'Bryant's primary-text suggestions continue to
justify a genuinely different Route C, but none is yet a theorem for #1191.
The ordered-root search likewise located only known SDDM/Laplacian and
squared-distance ingredients, not the application-specific common-master
theorem; this is no novelty claim.
The direct `M=D^tBD`, `2M=lambda`, and Haar-Abel continuation does not change
that conclusion or establish priority.

## C089--C098 physical-cover continuation

The universal-star, unequal-scale Haar, shared-endpoint transfer, parametric
physical-cover, and fixed 14-channel surplus results are project-internal
finite derivations and certificates.  The chamberwise rational behavior in
C095 is consistent with established one-parameter linear-programming
methodology; the closest primary records checked here are Väliaho (1979),
DOI `10.1007/BF01930856`, and Adelgren (2026), DOI
`10.1007/s11590-025-02277-3`.  Those sources do not state the present physical
event list, certificates, or C058 ownership problem.

C097--C098 add no external theorem claim: they prove strict sharing only in a
fixed weaker sum-cover LP and then exclude all cross-scale roots and tested
aggregate columns from its optimum face.  This does not change the qualified
retrieval null and supplies no absence, priority, novelty, publication, or
prize evidence.

## Signed finite-tree transport refresh — 2026-08-30

A forced-live Firecrawl read of
[Erdős Problems #1191](https://www.erdosproblems.com/1191) still labels the
problem `OPEN`, records no proof claim, and warns that finite computation alone
cannot resolve it.  The displayed `$1000` wording is historical and does not
make this workspace prize-ready.

The frozen prefix/scale Abel formula and the new signed-owner LP triggered a
narrow four-plugin search: 24 Exa results across three distinct queries, 20
Firecrawl paper-index results, a 12-result Firecrawl related-paper expansion,
and 10 SciSpace results were reviewed.  Consensus returned no papers because
its monthly quota was exhausted.  The two closest primary texts checked in
body were:

- Lai,
  [*The Bellman functions of the Carleson Embedding Theorem and the Doob's
  martingale inequality*](https://arxiv.org/abs/1411.5408), whose telescoping
  Bellman argument is built on nonnegative Carleson increments `alpha_n`; and
- Treil,
  [*Sharp A2 estimates of Haar shifts via Bellman
  function*](https://arxiv.org/abs/1105.2252), which handles signed Haar-shift
  operators through bilinear estimates but combines the resulting quadratic
  bounds with nonnegative scale weights.

These papers supply useful Bellman/tree precedents.  Neither checked statement
provides the project-specific oriented mixed-width physical price, separate
coordinate-owner rows, one-for-one `2M=lambda` Gothic ownership, or all finite
initial/final/terminal rows in one signed source-to-sink ledger.  This is a
dated targeted qualified null, not evidence of novelty or absence.

## Adjacent Carleson primary-source mapping — 2026-08-30

Two additional primary records sharpen the boundary without supplying the
missing theorem.

- Culiuc--Treil,
  [*The Carleson Embedding Theorem with matrix weights*
  (arXiv:1508.01716v2)](https://arxiv.org/abs/1508.01716), Theorems 1.1--1.2,
  proves equivalence between a matrix-weighted martingale embedding and a
  positive-semidefinite matrix Carleson testing condition.  For the best
  constants it records `B<=A<=4e^2 d^2 B`.  This is a genuine PSD-matrix
  precedent, but its testing matrices and measure are positive semidefinite;
  it does not supply the present signed owner shares, Gothic four-corner
  cancellation, physical mixed-width price, or primitive/boundary ledger.
- Bickel--Wick,
  [*A Study of the Matrix Carleson Embedding Theorem with Applications to
  Sparse Operators* (arXiv:1503.06493)](https://arxiv.org/abs/1503.06493),
  studies dyadic matrix-weighted Carleson embedding through positive-
  semidefinite coefficient sequences, maximal functions, and matrix
  sequence-space duality.  It is another genuine cross-scale matrix
  precedent, but its testing hypothesis does not manufacture the signed
  coordinate-owner inequalities or the strictly positive four-corner
  surplus required here.
- Benito-de la Cigoña--Borges--D'Emilio--Pasquariello--Wagner,
  [*Matrix Weighted L^p Estimates in the Nonhomogeneous Setting*
  (arXiv:2506.15570v2)](https://arxiv.org/abs/2506.15570), Theorem C / Theorem
  4.3, gives a variable-weight scalar Carleson embedding for cube-localized
  weights satisfying the explicit compatibility condition (1.3)/(4.7), with
  the usual positive-coefficient Carleson application.  Its variable local
  weights are conceptually adjacent to phase- or owner-dependent weighting,
  but the required compatibility estimate is an assumption, not a
  consequence of Sidon ownership, and the theorem does not handle this
  project's signed four-corner source rows.

The internal C099--C106 results and the registered C107--C110 finite
witnesses therefore remain project-specific calculations.  None of these
primary papers converts a fixed positive `Phi`, a Fejér ratio gate, or even
a complete finite phase cover into a compatible-history C058 theorem.  No
absence, priority, novelty, publication, or prize conclusion is drawn.

## 2026-08-31 C058 bounded-storage / overlap-consistency delta

A connector-cross-checked follow-up added the bilinear matrix-Carleson failure
paper, chordal PSD completion/decomposition, and dyadic-tree Bellman formulas.
The useful boundary is now sharper: matrix Carleson theorems assume positive
testing data; chordal completion assumes consistent clique overlaps; and the
tree Bellman sources do not supply the signed physical owner rows.  Thus none
repairs the C117 owner-selection obstruction or proves the enriched C058
storage/dissipation inequality.  Search queries, exact relevance, quota
limitations, and primary links are recorded in
`research_sources/c058_storage_2026-08-31/SCOPED_SEARCH.md`.  This remains a
dated qualified null, not a novelty claim.
