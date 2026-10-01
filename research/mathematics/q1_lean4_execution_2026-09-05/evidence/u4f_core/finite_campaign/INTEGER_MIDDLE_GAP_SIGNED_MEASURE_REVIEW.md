# A26: exact integer-middle-gap flux and actual reuse of one Sidon pair

2026-09-09. This bounded check uses the eight A24 variant records and
only their seven middle endpoint pairs in the existing certified
C=1,m0=2,M=T=96 record bank. The component is fixed at k=48, with

    lambda_48=kappa_48/H_48^2=1/1148518878296832.

All identities below are exact integer/rational identities. No history
was generated, no full-horizon profile was recomputed, and no new Lean
verification was performed.

## The signed measure of the eight-record boundary

At the original b24->25 transition, l=6, all-large-old-gap selection,
define

    mu(B)=sum_(birth records with middle gap B) Hquad
           -sum_(retirement records with middle gap B) Hquad.

This keeps the unequal physical Hquad factors. The result is

| B | Unique middle ranks (q,s) | Birth Hquad sum | Retirement Hquad sum | mu(B) |
|---:|---|---:|---:|---:|
| 14 | (6,7) | 0 | 184 | -184 |
| 48 | (6,9) | 713 | 184 | 529 |
| 70 | (6,10) | 0 | 350 | -350 |
| 105 | (6,12) | 0 | 349 | -349 |
| 214 | (6,15) | 0 | 350 | -350 |
| 332 | (6,18) | 713 | 0 | 713 |
| 422 | (6,20) | 713 | 0 | 713 |

The total signed width is722, despite the record-count change being-2.
The exact first moment is

    sum_B B*mu(B)=424373.

For finite signed integer-supported measures, linearity and the exact
identity B=sum_(s=1)^B 1 give

    sum_B B*mu(B)=sum_(s>=1) sum_(B>=s) mu(B).       (1)

Nonnegativity of mu is neither true nor required. The sum is evaluated
at its seven constant-threshold intervals, not by scanning every integer:

| Integer threshold s | Length | sum_(B>=s) mu(B) | Interval contribution |
|---|---:|---:|---:|
| 1..14 | 14 | 722 | 10108 |
| 15..48 | 34 | 906 | 30804 |
| 49..70 | 22 | 377 | 8294 |
| 71..105 | 35 | 727 | 25445 |
| 106..214 | 109 | 1076 | 117284 |
| 215..332 | 118 | 1426 | 168268 |
| 333..422 | 90 | 713 | 64170 |
| 423 onward | — | 0 | 0 |

The seven interval contributions sum to424373, proving (1) in this
specific example. Its priced value is exactly

    424373/1148518878296832.

All the threshold tails happen to be positive here. This is a property
of these eight records, not a sign theorem for arbitrary actual flux.
Thresholds in (1) reuse the same physical records; they are not separate
budgets.

## Trace of the same seven actual middle pairs

For each selected B, its actual endpoint pair was independently
recovered from the certified prefix through48 and is unique. Then the
saved original M96 bank was filtered once by r<=48 and that middle pair.
Only the type-2 minus and type-3 plus records contribute BH; the type-1
minus record is not counted again. Each retained row keeps its actual
birth c, output(i,r), full original record, BH=B*Hquad and its one
coverage interval c+1,...,i-1. All183 retained records passed an
independent strict-gate recheck, with UNKNOWN=0. The optional large-gap
subclassification also has no unresolved comparisons.

| B | All BH records | Type2 / Type3 | Maximum uses at one cut | Large-gap records | Large-gap maximum |
|---:|---:|---:|---:|---:|---:|
| 14 | 40 | 18 / 22 | 16 | 13 | 7 |
| 48 | 45 | 21 / 24 | 22 | 21 | 11 |
| 70 | 25 | 13 / 12 | 13 | 10 | 6 |
| 105 | 18 | 7 / 11 | 12 | 9 | 7 |
| 214 | 27 | 16 / 11 | 17 | 7 | 5 |
| 332 | 14 | 7 / 7 | 9 | 6 | 6 |
| 422 | 14 | 8 / 6 | 10 | 2 | 2 |

There are183 traced physical BH records in total, of which68 have all
three old gaps large. These are records belonging to seven prescribed
middle pairs, not the full component's record count. Every pair has
q=6, so its BH diagonal selector q<=l<s also holds at l=6.

The exact JSON stores every birth/output multiplicity, cut profile and
record interval. For each group it checks the two equivalent forms

    sum_h BH_h * sum_(b=c_h+1)^(i_h-1) 1/b
      =sum_b (1/b) sum_(h:c_h<b<i_h) BH_h.           (2)

Each physical record occurs once on the left with its full actual
coverage. The right side charges the same interval, without inventing
independent budgets for its cuts. The JSON also records the unweighted
harmonic coverage and the Hquad-weighted coverage separately.

Summed over these seven pairs only, the unpriced BH harmonic coverage is

    all original BH:
      2016761693430816171237131/428163098127382800;
    all-large-old-gap BH:
      75498616224418301123647/61565935678447200.

Multiplication by the one lambda_48 gives respectively

    2016761693430816171237131/491753401189358103275845691289600;
    75498616224418301123647/70709639386705086745546439270400.

These are linear harmonic-coverage masses of the selected component
subprofile. They are not N, a square-root norm, or the full M96 horizon.

## Exact rejection of one-use charging for a unique Sidon middle gap

The proposed shortcut "unique B implies at most one BH use at a fixed
cut/component" is false. A small counterexample even fixes the latest
birth c and the matching type in addition to B, b and k.

In the same certified variant, B=48 has the unique middle pair
(q,s)=(6,9), with point values(19,67). At b=11,k=48 there are these two
all-large-gap, strict-core type-3 records:

| Old quadruple | Actual old values | Hquad | Output ranks | Output values | Numeric output | Coverage | BH |
|---|---|---:|---|---|---:|---|---:|
| (2,6,9,10) | (2,19,67,89) | 87 | (17,18) | (312,351) | 39 | 11..16 | 4176 |
| (1,6,9,10) | (1,19,67,89) | 88 | (19,20) | (401,441) | 40 | 11..18 | 4224 |

Their original record rows are, in the saved11-column convention,

    [87,48,2,10,6,9,10,9,17,18,39],
    [88,48,1,10,6,9,10,9,19,20,40].

Both cover b=11 and have r<=48, and both use the same genuine component
price. They have distinct outer endpoint p and actual output; middle
pair uniqueness cannot identify or discard either record. Their
original four-old-endpoint sets and output endpoints are separately
six-distinct. The old gaps are(17,48,22) and(18,48,22), respectively,
and both satisfy the original strict tests and the large-gap selector.

The same B=48 pair has22 simultaneous original BH uses at b=25,k=48,
with BH coefficient414480. The all-large-gap subset has11 uses there,
with coefficient204720. These are direct actual counterexamples to
one-use charging, without any abstract multiplicity relaxation.

What Sidon uniqueness does fix is the middle endpoint pair, and after
also fixing the outer endpoints and matching it fixes at most one
actual output. It does not fix those outer endpoints or prevent reuse
across output times and overlapping cut intervals. No stronger global
occupancy bound is inferred from the finite counts here.

## Evidence and mathematical scope

`integer_middle_gap_signed_measure_existing.py` performs only the
specified eight-row moment calculation and seven-pair trace. It binds
the original input, record bank, independent checker, certificate and
A24 source hashes. `integer_middle_gap_signed_measure_existing_exact.json`
stores the exact signed measure, threshold intervals, all traced rows,
their genuine harmonic contributions, multiplicities and witnesses.
The companion manifest records hashes and this scope.

The first-moment identity is valid but does not itself provide an upper
bound. The one-use shortcut is rigorously rejected on an actual fixed
C=1,m0=2 history, including its large-gap remainder. The next estimate
must retain repeated uses of the same middle pair, unequal Hquad, and
overlapping coverage across records and components. Uniform U4-F and
the original Q1 remain unresolved.
