# Restricting output to actual used differences retains a signed retirement term

2026-09-05. Author: `/root`, GPT-6 Astra Ultra.

Status: exact finite accounting and an actual five-point example that
refutes an unconditional nonpositive-retirement claim. This is not a
counterexample to original Q1, a fixed-onset capped infinite history,
or a refutation of an asymptotic estimate with a finite error.
No Lean verification is claimed.

## 1. Two distinct capacities

Fix a signed old source Fhat_N and a nonnegative matrix W on it.
As in `signed_bank_born_positivity.md`, its literal historical
capacity through a terminal horizon counts source pairs whose
output appears later than the sources, together with pairs whose
output has not yet appeared. Born pairs contribute neither.

One may instead restrict every physical output to the differences
that have actually appeared by a specified final rank M. This is
legitimate for a payment involving only those actual differences.
For a fixed old matrix, the maximum at an output whose birth is r
then sums exactly the source pairs available strictly before r.
Its residual capacity is a **retirement** sum, not the negative
of the full Born sum plus a diagonal correction. The latter formula
also uses the never-used output pairs, which have now been removed.

Thus the full signed Born positivity theorem alone does not give
a favorable sign for this more selective residual capacity. The
following actual example shows that the stronger unconditional
claim would be false.

## 2. An actual five-point Sidon counterexample to the stage sign

Take P_5={0,1,10,13,17}. Its ten positive differences are

```
1,3,4,7,9,10,12,13,16,17,
```

all distinct. The positive-difference uniqueness condition is
equivalent to Sidon uniqueness including repeated two-sums; the
new exact check also tests those repeated sums directly.

The old positive bank and the new output labels are

```
F_4={1,3,9,10,12,13},
G_5={4,7,16,17}.
```

On the signed source Fhat_4 use the permanent raw feature g(d)=d.
The full retirement at stage five is

```
R_5(g)=sum_({d,e} subset Fhat_4, |d-e| in G_5) d e.
```

Every pair in this sum has later source birth exactly four and
output birth five. The complete list is:

| Output | Signed unordered source pairs | Raw linear total |
|---|---|---:|
| 4 | {9,13}, {-13,-9}, {-3,1}, {-1,3} | 228 |
| 7 | {3,10}, {-10,-3} | 60 |
| 16 | {-3,13}, {-13,3} | -78 |
| 17 | none | 0 |

The totals are 2*9*13-2*1*3, 2*3*10, and -2*3*13.
Consequently

```
R_5(g)=210>0.                                      (1)
```

Every earlier retirement stage in this five-point history is zero,
so the total retirement through rank five is also positive. A
positive common source-stage or retirement-stage price merely
multiplies (1). With old normalization H_4=13 and Q_4=12,
the normalized residual is 210/(13^2*12^2)=35/4056>0.

The same example applies to the odd minimum kernel

```
K_min(d,e)=sign(d)sign(e)min(|d|,|e|).
```

Its three nonzero output totals are 16, 6, and -6, respectively.
Thus R_5(K_min)=16>0. For comparison, the odd sign outer product
has totals 0, 2, and -2, and hence zero retirement on this example.
These are direct evaluations of the same eight pairs. The minimum
kernel calculation is analytic here, not an extra program run.

## 3. The one fixed execution and its precise scope

`research/evidence/signed_retirement_fixed.py` was executed once
on four explicitly fixed histories of ranks 3, 4, 6, and 32.
It validates repeated-sum Sidon uniqueness, enumerates all signed
used pairs, separates full Born source stages from full retirement
output stages, and verifies the complete convolution identity

```
E_(P_N)(g)=N sum_(d in Fhat_N)d^2+2 Born_N(g)+2 Retired_N(g).
```

The rank-six fixture contains the five-point prefix in section 2;
its output reports the positive stage-five value 210. The rank-32
fixture has a positive stage-sixteen value 927108. Other reported
stages and final totals may be negative. There was no parameter
sweep or attempt to infer a universal sign from the other examples.

The `.run.json` stores the actual invocation, UTC start and end,
observed return code zero, before/after source hashes, the performed
unchanged-source gate, and complete stdout/stderr with their hashes.
The `.txt` and `.stderr.txt` retain the actual bytes. This is a new
check of a new stage-sign hypothesis, not a repetition of a passed
earlier experiment or the C143 pricing replay.

## 4. What remains possible

The counterexample rules out claiming R_n<=0 at every actual
birth stage, even for the raw signed linear feature with its proven
Born positivity. It also rules out claiming that an arbitrary
positive price repairs that unconditional statement.

It does not rule out a bound on the total positive retirement
with a finite initial/repeated-endpoint error, an all-rank estimate
under one fixed eventual critical cap, or cancellation forced by
the entire future of such a history. Those stronger hypotheses
and quantifiers are absent from this five-point example.

The actual-used output restriction therefore remains a possible
route, but its signed retirement capacity must be estimated as
it stands. Neither the previously proved Born sign nor omission
of the never-used output terms pays it automatically. Original Q1
and the requested final Lean theorem remain unresolved.
