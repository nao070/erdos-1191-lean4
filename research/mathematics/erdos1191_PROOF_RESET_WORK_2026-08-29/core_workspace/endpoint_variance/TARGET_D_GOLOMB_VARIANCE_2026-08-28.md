# Target D: exact Golomb-ruler variance minima (2026-08-28)

**Evidence label:** [PROJECT-INTERNAL EXACT FINITE THEOREM]

This dated extension addresses only the finite optimization requested in
Target D.  It does not prove a uniform Sidon-specific asymptotic lower bound,
does not supply a cross-prefix upper budget, and does not resolve Erdős
Problem #1191.

## Exact search contract

For each `2 <= m <= 7` and `m-1 <= D <= 25`, the primary engine enumerates
every choice of `m-2` internal marks from `{1,...,D-1}`.  Thus the exact
completeness denominator is

```text
binomial(D-1, m-2).
```

It retains a candidate exactly when all positive differences are distinct,
equivalently when all nonempty contiguous sums of its positive gap vector are
distinct.  Both orientations are enumerated.  Reflection classes are formed
only after the exhaustive filter, so symmetry reduction cannot hide a ruler.

For every retained ruler the verifier computes the `Fraction`-valued
diameter-regime variance at

```text
N = D+1, D+2, D+3.
```

The dated JSON contains every case count, the exact minimum at each modulus,
all oriented minimizers, their gap vectors, and their reflection-class
representatives.

## Completeness and independent audit

The full run scanned 245,505 normalized internal-mark candidates over 135
`(m,D)` pairs.  It retained 9,013 oriented Golomb rulers and evaluated 27,039
exact variances.

An independent oracle covers `2 <= m <= 5`, `m-1 <= D <= 12`, at all three
modulus offsets.  It does not use the primary subset enumerator or gap-moment
formula: it recursively enumerates positive gap compositions, checks
contiguous sums directly, and recomputes variance from translated half-open
block membership at every offset.  Its 294 enumeration/minimum/minimizer
comparisons have mismatch count zero.

The oracle test was also mutation-checked: deliberately dropping candidates
whose last internal mark is `D-1` produced 19 failing subcases before the
correct primary range was restored.

## First feasible diameter at each mark count

The table reports `N=D+1`.  `classes` is the number of reflection classes
among the minimizers.  The last column compares the finite minimum with the
general mandatory-level lower bound.

| m | least feasible D | oriented rulers | minimum variance | oriented minimizers | classes | ratio to mandatory bound |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | `1/4` | 1 | 1 | `1` |
| 3 | 3 | 2 | `3/4` | 2 | 1 | `9/8` |
| 4 | 6 | 2 | `12/7` | 2 | 1 | `4/3` |
| 5 | 11 | 4 | `26/9` | 2 | 1 | `13/9` |
| 6 | 17 | 8 | `404/81` | 4 | 2 | `1616/987` |
| 7 | 25 | 10 | `1161/169` | 2 | 1 | `1161/728` |

The oriented minimizers in these least-diameter cases are:

- `m=2`: `(0,1)`;
- `m=3`: `(0,1,3)` and its reflection;
- `m=4`: `(0,1,4,6)` and its reflection;
- `m=5`: `(0,2,7,8,11)` and its reflection;
- `m=6`: `(0,1,8,11,13,17)`, `(0,1,8,12,14,17)`, and their reflections;
- `m=7`: `(0,1,11,16,19,23,25)` and its reflection.

The strict ratios above one for `3 <= m <= 7` are exact finite evidence that
the unrestricted consecutive-set equality mechanism is unavailable at these
least feasible Golomb diameters.  They are not evidence for a uniform ratio
as `m` tends to infinity.

## Mandatory stress instances

The certificate also records:

- the exact zero mode `{0,1,N}`;
- a separated union of two modular cycles with zero variance;
- the certified homometric six-mark pair, including variances `79/28` and
  `55/28` at modulus 14;
- a ten-mark greedy Mian-Chowla prefix;
- twelve deterministic random six-mark rulers (seed `1191`);
- the dominant-central-gap ruler `(0,1,50,54,60)`;
- the seven-mark ruler `(0,1,4,10,18,23,25)`, checked coordinate by coordinate
  against `b_k <= 2 k^2 log(2k)`;
- an explicit `not_run` record for Singer/Bose-Chowla rulers, because the
  canonical handoff contains no validated construction code and the protocol
  makes that stress case conditional on reliable code.

## Reproduction and hashes

Run:

```bash
python -m unittest discover -v
uvx --from pytest pytest -q
python golomb_variance_certificate_2026_08_28.py
```

The default `python -m pytest -q` command could not run in the active
Miniforge interpreter because `pytest` was not installed there.  The isolated
`uvx` run reported `31 passed, 42 subtests passed` after the concurrently
developed multiscale suite was also present.

The certificate was regenerated to a temporary path and compared byte for
byte with the checked output.  Both files had SHA-256

```text
58bab957e48be7dc97206ecf45243f907064240e22785604a09512355f8f2f6e
```

The canonical-payload hash recorded inside the JSON, and independently
recomputed after removing only the hash field, is

```text
7bde9b209c687cdbc99d933af856041feac5fd52707be25f169e5c72bbbf4cc3
```

The machine-readable artifact is
`golomb_variance_certificate_2026-08-28.json`; its generator is
`golomb_variance_certificate_2026_08_28.py`.
