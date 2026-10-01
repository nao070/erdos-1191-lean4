# Wave 7 search and verification log

Cutoff: **2026-08-28**. Scope: global/nested integer Sidon or Golomb sequences, literal prefix compatibility, difference-spectrum and interval packing across epochs, renewal/Carleson analogues, $B_2$ density, and completion of prescribed finite Sidon sets. This log records a bounded scoping review, not a proof of novelty or nonexistence.

## Scripted discovery

The `scholar-deep-research` state contains 316 deduplicated records after the following 14 successful query rounds.

| # | Source | Exact query | Hits | New | Merged |
|---:|---|---|---:|---:|---:|
| 1 | OpenAlex | `nested Sidon sequence Golomb ruler compatible prefixes` | 0 | 0 | 0 |
| 2 | Crossref | `perfect difference set finite Sidon set extension prescribed` | 50 | 50 | 0 |
| 3 | arXiv | `"Sidon sequence"` | 21 | 21 | 0 |
| 4 | Crossref | `Golomb ruler difference packing` | 50 | 50 | 0 |
| 5 | OpenAlex | `infinite Sidon sequences` | 50 | 50 | 0 |
| 6 | arXiv | `"Golomb ruler"` | 31 | 29 | 2 |
| 7 | Crossref | `infinite Sidon sequence density` | 50 | 46 | 4 |
| 8 | OpenAlex | `perfect difference sets Sidon prescribed finite` | 45 | 44 | 1 |
| 9 | arXiv | `"B_2 sequence"` | 3 | 2 | 1 |
| 10 | OpenAlex | `B2 sequence density nested prefixes Sidon` | 0 | 0 | 0 |
| 11 | Crossref | `Sidon sequence Carleson embedding renewal` | 50 | 30 | 20 |
| 12 | arXiv | `"B_2 sequence"` | 3 | 0 | 3 |
| 13 | OpenAlex | `B2 sequence density nested prefixes Sidon` | 0 | 0 | 0 |
| 14 | Crossref | `Sidon sequence Carleson embedding renewal` | 50 | 0 | 50 |

One attempted arXiv query, `all:all:"Sidon sequence" AND (all:nested OR all:extension OR all:completion)`, returned HTTP 400 before any record was incorporated. It was logged in `search_diagnostics` and replaced by the valid phrase queries above.

The built-in saturation diagnostic reported:

| Source | Rounds | Records contributed | Last-round new | Failures | Saturated |
|---|---:|---:|---:|---:|---|
| OpenAlex | 5 | 93 | 0 | 0 | yes |
| Crossref | 5 | 177 | 0 | 0 | yes |
| arXiv | 4 | 54 | 0 | 1 | yes |

The diagnostic used thresholds of 50% for new records, 25% for new authors, 30% for new venues, 100 for the maximum citation count of a newly found record, at least two rounds, and all four evaluable axes. “Saturated” describes convergence of these recorded queries under those thresholds; it does not establish literature completeness.

The ranking pass used

\[
\mathrm{score}
=0.6\,\mathrm{relevance}
+0.15\,\frac{\log_{10}(\mathrm{citations}+1)}3
+0.15\,e^{-\Delta\mathrm{years}/5}
+0.1\,\mathrm{venue\ prior}.
\]

The generic result sets contained obvious lexical false positives, including biomedical uses of “Sidon.” Consequently the final mathematical corpus was selected manually from titles/abstracts and then checked against primary full text; the automatic top 24 is preserved only as discovery provenance and is not represented as the final evidence set.

## Host-web enrichment and citation chasing

The bounded web pass used exact-title, identifier, and theorem-level searches around the following primary records:

- arXiv:2606.28651v3 — O’Bryant, infinite $g$-Golomb upper obstruction and Lemma 9 gluing/deletion;
- arXiv:2510.19804v2 — Alexeev–Mixon, prescribed finite counterexamples and Hall completion;
- arXiv:2505.20851v2 / DOI `10.1007/s10474-026-01604-z` — Riblet–Schehr, compactness;
- arXiv:2008.04804v2 — Sudakov–Tomon–Wagner, prefix-code/Kraft antichain inequality;
- arXiv:2608.13739v1 — Ma–Yi, disjoint internal Golomb spectra;
- arXiv:2605.14229 — Gupta–O’Bryant, nested LM rulers;
- arXiv:2607.07931 — Gupta, modular-to-ordinary finite rulers;
- arXiv:2409.14409 — Xu–Xiu–Fan–Liang, disjoint-mark Golomb rulers;
- arXiv:1209.0326 / DOI `10.1016/j.aim.2014.01.011` — Cilleruelo, explicit infinite Sidon density;
- arXiv:math/0609244 / DOI `10.1007/s00493-008-2339-4` — Cilleruelo–Nathanson, perturbed perfect difference sets;
- DOI `10.1016/j.jcta.2026.106239` — Chen–Fang, improved density transfer;
- DOI `10.4171/LEM/1097` / arXiv:2309.14524 — Barré–Pichot, exact modular threshold;
- arXiv:1908.05591 — Mészáros–Rónyai–Szabó, finite Singer difference sets;
- arXiv:1910.08661v3 — Conlon–Fox–Sudakov, adjacent graph-prefix sparsity;
- arXiv:2208.11357v1 — Fang–Sándor, two sets with disjoint nonzero difference spectra.

Citation trails were followed from O’Bryant to Halberstam–Roth, Caicedo–Martos–Trujillo, Erdős/Cilleruelo, and Ruzsa; from Alexeev–Mixon to Marshall Hall, Jr., *Cyclic projective planes*, DOI `10.1215/S0012-7094-47-01482-8`; from Ma–Yi to perfect difference families, Wild/Mathon product constructions, difference triangle sets, Lorentzen–Nilsen, and Shearer; and from the perfect-difference density papers through Cilleruelo–Nathanson to Chen–Fang.

Additional exact concept searches included:

- `nested Golomb ruler sequence prefixes`
- `Sidon sequence prescribed prefix extension infinite`
- `Sidon difference spectrum packing disjoint intervals blocks`
- `Sidon sequence renewal Carleson embedding arithmetic`
- `perfect difference set containing prescribed finite Sidon set`
- exact title, arXiv-ID, DOI, author, theorem number, and displayed-formula fragments for the records above.

Theorem statements were checked in primary arXiv HTML/PDF or publisher pages. Crossref and OpenAlex were used for discovery and metadata, not as sole proof of a theorem. Chen–Fang’s theorem statement and online-publication metadata were checked against the publisher/indexed record; its January 2027 issue assignment is separated from its 2026 online publication date.

## Plugin and hosted-search delta

- Consensus was retried with `"Sidon sequence" infinite density sqrt(x/log x) multiscale year:2018-2026` and returned an exact quota failure: all 30 monthly searches had been used, with reset shown as 2026-09-01. It therefore added no evidence.
- A SciSpace natural-language query for multiscale/global infinite additive Sidon behavior at $\sqrt{x/\log x}$ returned ten mostly adjacent papers and omitted O’Bryant’s already primary-checked 2026 result.
- A targeted SciSpace query for finite $A,B$ with $(A-A)\cap(B-B)=\{0\}$ surfaced Fang–Sándor, *On disjoint sets*, and mostly irrelevant records. Two 2026 Zenodo computational/AI heuristic notes were excluded as nonauthoritative for theorem verification. SciSpace duplicated Fang–Sándor once with an unrelated malformed DOI, so only the official arXiv record was used.
- A hosted Firecrawl research search for `"Sidon" "disjoint sets" differences multiscale nested prefixes` returned generic arXiv listing pages and no theorem-level bridge. It was marked bad for missing the requested topics; search id `01a04846-5f7f-767a-a4b9-8a9d96a3ae24`, feedback id `01a04846-bfb8-77aa-9a22-2cbf8ca2a3c0`.

These failures and metadata defects are part of the evidence trail: hosted relevance search was useful for one adjacent lead but was not trusted as a bibliographic authority or theorem source.

## Reproducibility

Let:

    STATE=research_sources/wave7_literature_state/research_state.json
    SCRIPTS=/Users/USER/.agents/skills/scholar-deep-research/scripts
    PY=/Users/USER/miniforge3/bin/python

Then the final local diagnostics are:

    $PY $SCRIPTS/research_state.py --state "$STATE" status
    $PY $SCRIPTS/research_state.py --state "$STATE" saturation
    $PY $SCRIPTS/research_state.py --state "$STATE" query diagnostics
    $PY $SCRIPTS/research_state.py --state "$STATE" query queries

The ranking configuration recorded in the state was produced with:

    $PY $SCRIPTS/rank_papers.py \
      --state "$STATE" \
      --question "Which primary results through 2026-08-28 bear directly on compatible nested integer Sidon or Golomb prefix towers, cross-epoch difference-spectrum packing, quantitative completion of prescribed finite Sidon sets, and arithmetic renewal or Carleson budgets?" \
      --alpha 0.6 --beta 0.15 --gamma 0.15 --delta 0.1 --top 30

The state JSON is the machine-readable query ledger. `PRIMARY_SOURCE_AUDIT.md` is the manually verified synthesis. The latter intentionally overrides automated relevance rankings when the retrieved record is mathematically off-topic.

## Qualified search limits

- Exact-phrase nulls are terminology-sensitive.
- Older undigitized sources and sources outside the followed citation trails may be absent.
- The review did not exhaust every language, database, thesis, or conference proceeding.
- Algebraic finite constructions at unrelated group orders do not by themselves give literal nested inclusion.
- Internal-spectrum disjointness and mark-set disjointness were not treated as substitutes for uniqueness of the full mixed difference spectrum.
- No null result in the report is a novelty claim.
