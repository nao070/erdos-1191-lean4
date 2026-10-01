# Wave 11 saturation and qualification

## Scripted corpus

- 26 successful scholarly requests: Crossref 8, arXiv 11, OpenAlex 7.
- 449 returned slots; 351 papers after cross-source deduplication.
- 14 structured evidence records: 13 full and 1 shallow.
- Four malformed arXiv field-query failures were logged; one further request
  was refused by the local phase-1 round cap and did not reach the provider.

Final four-axis saturation result:

| Source | Last query | New % | Authors % | Venues % | Citations | Result |
|---|---|---:|---:|---:|---:|---|
| Crossref | 2025 finite-Sidon diameter | 40.0 | 2.2 | 1.9 | 16 | saturated |
| arXiv | Riblet exact author/title | 50.0 | 0.1 | 2.1 | 0 | not saturated |
| OpenAlex | interval-product/Golomb gaps | 100.0 | 12.6 | 20.0 | 29 | not saturated |

Therefore **overall saturation is false**.

## Provider coverage

- Exa: 18 searches / 180 slots.
- Firecrawl: 8 searches / 120 slots; 3 related calls / 45 slots; 4 inspect;
  6 read.
- SciSpace: 4 searches / 40 slots.
- Consensus: 1 blocked call; account quota 30/30, reset 2026-09-01.

## Qualified targeted conclusion

The exact product/geometric-mean branch reached the same boundary through the
scholarly APIs, Exa, Firecrawl, and SciSpace:

- the Golomb gap-vector formulation is available;
- global diameter and rank-selected first moments are available;
- adjacent-difference sumset products are available;
- enumeration and graceful-permutation results are available;
- no checked theorem has both the actual interval-log product and one fixed
  nested critical branch in its hypotheses and conclusion.

This is **targeted convergence of the logged interface**, not a claim that the
literature contains no such theorem.  The state remains at discovery phase 1
because the overall source-level gate is unsatisfied; manual theorem-text
verification, rather than the polluted automated ranking, determines every
load-bearing disposition in the memo.

