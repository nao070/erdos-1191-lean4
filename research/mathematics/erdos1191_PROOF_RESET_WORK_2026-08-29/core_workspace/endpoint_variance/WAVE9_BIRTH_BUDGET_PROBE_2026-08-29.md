# Wave 9: exact positive-birth-budget probe

**Date:** 2026-08-29  
**Status:** exact finite computation and local-candidate falsification;
`P15` and Erdős Problem #1191 remain open

## 1. Question audited

At a dyadic birth boundary `m -> 2m`, write

\[
 \Delta\mathcal B_H(m)=
 \frac1{N_{2m}^2}
 \sum_{\substack{0\le i<j<2m\\j\ge m}}
 h_i h_j\Phi^{(2m)}_{ij}.
\tag{1}
\]

The Wave 8 reduction says that the remaining theorem is

\[
 \sum_{m\le 2^J}\Delta\mathcal B_H(m)=o(\log J)
\tag{2}
\]

on one fixed infinite eventually critical Golomb ruler.  This probe computes
every term in (1) with `Fraction`, partitions it simultaneously by rank lag
and numerical magnitude, and tests strong local surrogates for (2).  It does
not replace the infinite quantifier by a finite fixture.

For a genuine atom `i>=1`, put

\[
 D_{i,j}=a_j-a_{i-1},\qquad \ell_{i,j}=j-i+1.
\tag{3}
\]

The artificial boundary row `i=0` is retained separately, with span
`a_j+1`.  The dyadic cell of a genuine atom records

\[
 2^r\le \ell_{i,j}<2^{r+1},\qquad
 2^s\le D_{i,j}<2^{s+1}.
\tag{4}
\]

For within-epoch plots, the absolute magnitude is also replaced by its exact
normalized depth `q`, defined by

\[
 N_{2m}/2^{q+1}<D_{i,j}\le N_{2m}/2^q.
\tag{5}
\]

No floating-point comparison decides a result below.

## 2. Exact atom and cell bounds

The kernel closed form is

\[
 \Phi_{ij}^{(L)}=
 \frac{(j-i)^2}{105L^4}
 \left(112(L-i-j)^2+16L(L-i-j)+12L^2\right).
\tag{6}
\]

It is independently sampled against the matrix definition of `Phi` at every
epoch.  Combining

\[
 h_i h_j\le D_{i,j}^2/4,
 \qquad
 \Phi_{ij}^{(L)}\le\frac43\left(\frac{j-i}{L}\right)^2
\]

gives the exact normalized atom envelope

\[
 \boxed{
 3\frac{h_i h_j\Phi_{ij}^{(L)}}{N_L^2}
 \le
 \left(\frac{\ell_{i,j}}L\right)^2
 \left(\frac{D_{i,j}}{N_L}\right)^2.}
\tag{7}
\]

The same inequality holds for the boundary row with its stated boundary
span and kernel rank gap.  For genuine atoms, global Golomb uniqueness gives
the additional exact capacity theorem

\[
 \#\{D_{i,j}:2^s\le D_{i,j}<2^{s+1}\}\le2^s.
\tag{8}
\]

Every fixture passes (7), the independent covariance-innovation oracle, the
full dyadic pair partition, global distinctness, and (8).  Equation (8) is
the strongest static magnitude capacity available here, but it has no
vanishing factor across epochs.

## 3. Exact per-epoch increments

The certificate contains every exact row, including all six authenticated
64-mark Wave 6 rulers.  Representative rows are reproduced here.  Fractions
are ordered by `m=1,2,4,...`.

### Perfect four-mark ruler `(0,1,4,6)`

```text
m=1: 1/35
m=2: 83/5488
sum: 1199/27440
```

At `m=2`, the exact signed charge is `137/10976` and the old-pair
subtraction is `29/10976`.

### Wave 6 Hall counterexample, 64 marks

```text
m=1:  1/35
m=2:  2363/411600
m=4:  4143469/644595840
m=8:  4840921/605972480
m=16: 729622523713/83658339287040
m=32: 44188002488909/4892741812224000
```

Its cumulative budget is approximately `0.066481924756`.

### Hash-authenticated Wave 6 ruler, 128 marks

```text
m=1:  1/35
m=2:  83/5488
m=4:  1531987/180741120
m=8:  1293204191/140223713280
m=16: 102925959061/11539235635200
m=32: 12188418867227/2613919473500160
m=64: 15676794152687357/2337031303389511680
```

Its cumulative budget is approximately `0.081684447133`.

### Wave 7 Erdős--Turán window, `p=1423`, 512 marks

```text
m=1:   2847/70972160
m=2:   46609085/8183650048
m=4:   8385525931/893492956160
m=8:   92534809309/8251188090880
m=16:  6905805184979/570178512977920
m=32:  14655439596291/1166667195330560
m=64:  244726502755472191/19228735054586839040
m=128: 16001973796927276379/1240461677715878051840
m=256: 1028804272398780529263/79561917838433441546240
```

The last increment is approximately `0.012930863161` and the cumulative
budget is approximately `0.089566792794`.  This is the established
changing-terminal finite window, not one all-prefix critical branch.

### Reconstructed 682-mark modified-greedy fixture

Only complete dyadic births through its 512-mark prefix are included.

```text
m=1:   1/35
m=2:   157/10752
m=4:   2509/288000
m=8:   121232873/13655900160
m=16:  10285553683/1140094894080
m=32:  36937545992941/4195538436096000
m=64:  200245019422729/21894579062046720
m=128: 29892287692515473251/3194226984708546232320
m=256: 981895646008764061653/106680470919327745310720
```

The 682-point hash is

```text
523c509485873262cf5c51c4ee974a8a9cd5b89b46cec24f9ed59c1f05d57a60
```

The last increment is approximately `0.009204080536`.  The exact cumulative
budget through 512 marks is

```text
3220063759918830329777034930560390879618811298896359
-------------------------------------------------------
30293165857460142164923175208177977807010955001856000
```

or approximately `0.106296706494`.  The audited 512-mark prefix obeys every
`C=1` cap.  The full working envelope is already known to fail at point 681,
and no infinite extension is inferred.

## 4. Complete small searches and minimal counterexamples

### 4.1 All four-mark all-prefix-`C=1` rulers

The search exhausts all `1,672` rulers.

| quantity | exact minimum | exact maximum |
|---|---|---|
| `Delta B(1)` | `16/875` at `(0,4,5,7)` | `1/35` at `(0,1,18,43)` |
| `Delta B(2)` | `169/46464` at `(0,1,3,43)` | `83/5488` at `(0,1,4,6)` |
| cumulative | `10723/462000` at `(0,4,5,43)` | `1199/27440` at `(0,1,4,6)` |

All `1,672` have `Delta B(2)<Delta B(1)`.  Nevertheless the simplest
two-parameter injections already fail:

- `CELL_ONE`: “at most one genuine atom per dyadic rank/magnitude cell”
  fails for `1,525` rulers;
- `CELL_RANK`: “cell occupancy is at most the lower rank-band endpoint”
  fails for `216` rulers.

The minimum-diameter counterexample to both is the perfect ruler

```text
(0,1,4,6).
```

Its cell `rank lag in [2,4)`, `magnitude in [4,8)` contains the three spans
`4,5,6`; hence its occupancy is `3`, not `1` or `2`.  Its exact cell charge
is `17/5488`.

### 4.2 Eight marks with terminal point at most 40

The bounded DFS visits `889,645` nodes and finds all `1,468` Golomb rulers;
`1,146` obey every `C=1` prefix cap.

The literal epoch monotonicity

\[
 \Delta\mathcal B_H(4)\le\Delta\mathcal B_H(2)
\tag{9}
\]

fails for `128` of the `1,146` rulers.  The minimum-diameter witness is

```text
(0,4,12,13,19,30,33,35),
```

with

```text
Delta B(2) = 2791/329280,
Delta B(4) = 340841/34836480,
positive margin = 446533/341397504.
```

The stronger literal harmonic schedule

\[
 2\Delta\mathcal B_H(4)\le\Delta\mathcal B_H(2)
\tag{10}
\]

fails for **all 1,146**.  Its minimum-diameter witness is

```text
(0,1,4,9,15,22,32,34),
```

with exact positive margin `1287/548800`.  This rejects the pointwise
schedule, not a possible eventual logarithmic Cesàro theorem on one infinite
branch.

## 5. Macroscopic rank/magnitude mass does not disappear in the fixtures

Define the macroscopic long-rank quadrant at epoch `m` by

```text
genuine atom,
D > N_(2m)/2,
dyadic rank-lag band lower endpoint >= m/2.
```

At the latest audited epochs, its share of the *entire* raw increment is:

| fixture | latest `m` | exact share | decimal |
|---|---:|---:|---:|
| authenticated 128 | 64 | `142426866367481261/219475118137622998` | `0.648943113` |
| Erdős--Turán 512 | 256 | `2738923201748154301783/4115217089595122117052` | `0.665559834` |
| modified greedy 512 prefix | 256 | `13242199924089976348090/20619808566184045294713` | `0.642207704` |

Thus the long finite fixtures do not exhibit a shift of the birth budget into
only low-rank or small-normalized-magnitude tails.  More than `3/5` remains
in one macroscopic quadrant at the two 512-mark terminal epochs.

Static cell overlap is also large.  If `R` is the lower rank-band endpoint,
the maximum exact ratio `cell occupancy/R` is

```text
modified greedy 512 prefix: 553/4
Erdős--Turán 512 window:     647/2
```

Consequently, the desired bounded-overlap theorem cannot mean bounded raw
occupancy in a static dyadic `(rank,magnitude)` cell.  A valid P15 mechanism
must attach a history-sensitive weight or stopping-time label which makes
repeated macroscopic cells pay for later arithmetic scarcity.

These are finite counterexamples to local surrogates.  They do not show that
the same macroscopic mass persists on an infinite eventually critical ray.

## 6. What the computation suggests next

The surviving target should distinguish at least three parameters:

1. absolute numerical magnitude of the unique difference;
2. rank lag at its unique birth epoch;
3. later **age or survival depth** before the enclosing modulus moves beyond
   that absolute magnitude band.

Global difference uniqueness proves the absolute magnitude capacity (8),
but normalization by the growing `N_(2m)` continually opens new cells.  The
missing gain must therefore come from a cross-epoch rule which charges a
macroscopic atom when its absolute band first becomes available, or from an
equivalent survival-conditioned depletion statement.  Static occupancy,
pointwise epoch monotonicity, and pointwise harmonic decay are now closed.

## 7. Reproducibility and scope

Owned artifacts are:

- `wave9_birth_budget_probe.py`;
- `test_wave9_birth_budget_probe.py`;
- `wave9_birth_budget_certificate_2026-08-29.json`;
- this note.

Run from the package root:

```bash
PYTHONPATH=core_workspace/endpoint_variance \
python core_workspace/endpoint_variance/wave9_birth_budget_probe.py

uv run --no-project --with pytest pytest -q -p no:cacheprovider \
  core_workspace/endpoint_variance/test_wave9_birth_budget_probe.py

uvx ruff check \
  core_workspace/endpoint_variance/wave9_birth_budget_probe.py \
  core_workspace/endpoint_variance/test_wave9_birth_budget_probe.py
```

Observed focused result: `6 passed`; Ruff reports `All checks passed!`.

```text
source SHA-256:
9158bf740248f97177f5214c044e478576a43ef0f7e1b6c999591d9b9e090b94

test SHA-256:
20d88779208dacf8b62fac0fdb8b13b1f66c540c9750c55ecc5df7b5ccdbb510

certificate internal SHA-256:
62ae7c48c70604e9f1ee3dcf2d3273a326825d75d42a59be7f517f6e16f992f8

certificate file SHA-256:
de8d8cebb3d75d132c9c693d2a42ff52019219bc02bc775a71c51e952c444c86
```

The certificate authenticates the Wave 6 source certificate, all fixture
point lists, exact per-epoch rows, normalized bands, global cells, exhaustive
counts, and scope flags.  It explicitly records:

```text
finite_computation_only = true
infinite_survival_inferred = false
p15_proved = false
erdos_1191_resolved = false
```
