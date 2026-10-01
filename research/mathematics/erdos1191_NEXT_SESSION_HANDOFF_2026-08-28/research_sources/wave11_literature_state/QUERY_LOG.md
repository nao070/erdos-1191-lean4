# Wave 11 literature query log

**Cutoff:** 2026-08-29.  All counts below are calls or returned result slots,
not claims about unique papers unless explicitly labelled as such.

## 1. Scholar script spine

All successful scholarly searches used
`/Users/USER/miniforge3/bin/python3` with the scripts in
`/Users/USER/.agents/skills/scholar-deep-research/scripts/` and persisted
to `research_state.json`.

Final successful request counts:

| Source | Requests | Ingested slots | New-at-ingest | Merged-at-ingest |
|---|---:|---:|---:|---:|
| Crossref | 8 | 185 | 157 | 28 |
| arXiv | 11 | 215 | 149 | 66 |
| OpenAlex | 7 | 49 | 48 | 1 |
| **Total** | **26** | **449** | **354** | **95** |

After DOI/title deduplication the state contains **351 papers**.  Fourteen
records have structured evidence: thirteen full-text and one abstract-only.

### Exact successful query matrix

The first five clusters were sent once to each of Crossref, arXiv, and
OpenAlex, for 15 requests:

1. `positive integer sequences all sums of consecutive terms distinct quantitative gaps holes repulsion`
2. `infinite Sidon sequence extension prescribed finite Sidon prefix compactness`
3. `dense Sidon sets nested prefixes additive energy stability distribution`
4. `weighted difference triangle inequalities Golomb ruler endpoint ranks`
5. `Carleson embedding sparse positive measures vanishing box constant tree`

Three one-source refinements brought the count to 18:

- Crossref: `one-box Dini Carleson measures locally finite trees vanishing sparse`
- arXiv: `Hegyvári all consecutive sums distinct sequence kmax strong infinite Sidon one-box Carleson`
- OpenAlex: `strong infinite Sidon quantitative separation prescribed prefix extension consecutive sums`

The scale-sensitive product branch added one request per source, bringing the
count to 21:

- Crossref: `graceful permutation Golomb ruler gap sequence product inequality consecutive sums`
- arXiv: `Golomb ruler gaps all consecutive sums distinct weighted logarithmic product geometric mean`
- OpenAlex: `distinct consecutive interval sums product lower bound Golomb ruler gap sequence`

Four exact arXiv author/title searches brought the count to 25:

- `Adrian Beker consecutive sums strictly increasing sequences`
- `Ruzsa Shakan Solymosi Szemeredi distinct consecutive differences`
- `Kevin O Bryant thickness infinite generalized Sidon sets`
- `Robin Riblet Sidon set union intervals`

The final Crossref request, number 26, was:

- `On the diameter of finite Sidon sets Carter Hunter O Bryant`

### Script failures and budget boundary

- Four field-qualified arXiv attempts of the form `ti:"..."` were passed by
  the wrapper as `all:ti:"..."` and returned HTTP 400.  They are recorded as
  four source failures but not as successful query entries.  The four plain
  author/title retries above succeeded.
- A final direct `2202.01296` arXiv attempt was refused locally by the configured
  phase-1 `max_rounds=10` cap.  No cap was raised: the Riblet record was already
  present and was deep-read directly.

## 2. User-requested discovery providers

- **Exa:** 18 searches at ten results each, **180 reviewed result slots**.
- **Firecrawl research index:** eight searches at `k=15`, **120 slots**;
  three related-paper calls at `k=15`, **45 slots**; four inspect calls and six
  in-body read calls.
- **SciSpace:** four searches at ten results each, **40 slots**.  The fourth
  prompt asked exactly: `Which primary papers prove product, logarithmic-product, or geometric-mean lower bounds for the distinct contiguous sums of a positive integer gap sequence whose partial sums form a Golomb ruler?`
- **Consensus:** one search attempt, blocked because all **30/30 monthly
  searches** were already used.  The provider reported reset on 2026-09-01.

The Exa/Firecrawl/SciSpace prompts covered the five scope axes above plus the
product/geometric-mean refinement.  Provider slots overlap substantially and
are not added to the 351-paper deduplicated scholarly corpus.

## 3. Primary-page verification outside the discovery providers

Eight web-verification calls contained ten official-source searches, six page
opens, and five in-page theorem finds.  One official arXiv PDF for graceful
permutations was also downloaded temporarily and converted to text.  These
checks corrected or fixed:

- the direction of the Ruzsa--Shakan--Solymosi--Szemerédi sumset bound;
- the arXiv-versus-journal theorem number for the locally finite tree paper;
- the 2023 corrigendum boundary for Beck--Bogart--Pham;
- the DOI and exact lower-order constant of the 2025 Sidon-diameter theorem;
- the fact that graceful permutations constrain only adjacent absolute
  differences.

## 4. Final scripted saturation snapshot

The configured thresholds were new-paper percentage `50`, new-author
percentage `25`, new-venue percentage `30`, maximum new citations `100`, at
least four evaluable axes, and at least two rounds.

| Source | Successful requests | Last new % | New authors % | New venues % | Max new citations | Axes passed | Saturated |
|---|---:|---:|---:|---:|---:|---:|---|
| Crossref | 8 | 40.0 | 2.2 | 1.9 | 16 | 4/4 | yes |
| arXiv | 11 | 50.0 | 0.1 | 2.1 | 0 | 3/4 | no |
| OpenAlex | 7 | 100.0 | 12.6 | 20.0 | 29 | 3/4 | no |

Overall saturation is therefore **false**.  The exact product/geometric-mean
branch is only *qualifiedly converged*: its checked hits reduce to structural
gap-vector formulations, global diameter bounds, adjacent-difference sumset
growth, or terminological false positives, not a P17 theorem.
