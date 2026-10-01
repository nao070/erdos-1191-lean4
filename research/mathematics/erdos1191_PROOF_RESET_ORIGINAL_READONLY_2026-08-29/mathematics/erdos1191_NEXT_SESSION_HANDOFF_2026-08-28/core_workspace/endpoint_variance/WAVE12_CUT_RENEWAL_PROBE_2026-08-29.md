# Wave 12 cut-renewal probe and certificate

Date: 2026-08-29  
Scope: **exact finite verification and labelled real-model calibration only**

## 1. What is certified

`wave12_cut_renewal_probe.py` implements two independent exact checks of

\[
Y_m=R_m-R_{2m}+Z_m.
\]

The first oracle stores the coefficient of every abstract `C_(i,j)` as a
`Fraction`.  The second substitutes an integer Golomb ruler and stores each
quantity as a canonical `ExactLogForm`.  The four explicit sectors of `Z_m`
are separately checked coefficientwise nonnegative.

The same program constructs the epoch/length ordering that is a linear
extension of the complete interval-containment poset.  It checks the exact
atom count

\[
B(m)=2m^2-5m+2
\]

and records both the actual witness gain and the looser theorem-level rank
cap `rank<2m^2`.

## 2. Exact finite coverage

The generated certificate
`wave12_cut_renewal_certificate_2026-08-29.json` records:

- five abstract coefficient-oracle rows, all exact;
- all 1,146 eight-mark all-prefix-`C=1` rulers, with zero failures;
- four renewal epochs on the 64-mark Wave 6 Hall counterexample fixture;
- five renewal epochs on an independently generated 128-mark Erdős--Turán
  ruler;
- 32,130 containment atoms through epoch 128;
- six per-epoch witness gains and six theorem-level cap gains, every one
  below the proved constant `5`.

The real Golomb model `a_n=n^2+sqrt(2)n` is evaluated only as a labelled
floating calibration.  At epoch 1024,

\[
Y_{1024}=0.2893858160837208,
\]

while the proved limit is

\[
\frac32(\log2-1/2)=0.28972077083991793\ldots.
\]

No floating comparison is used in an exact identity or sign decision.

## 3. Reproduction

From `core_workspace/endpoint_variance/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_wave12_cut_renewal_probe.py

PYTHONDONTWRITEBYTECODE=1 python3 \
  wave12_cut_renewal_probe.py \
  --output wave12_cut_renewal_certificate_2026-08-29.json
```

Observed focused result:

```text
Ran 7 tests in 12.709s
OK
```

The certificate's internal payload digest is

```text
fe0fd30cccaf2717d4c7dd2306772bc7dbcaea9bacf2b641d8e685d4999894a4
```

The final pretty-printed certificate file SHA-256 is

```text
e5645101d5150910de428b7184d504b1a9b90ac411c1b007be743e43e65aecc9
```

They differ because the internal digest is computed before inserting its own
field.

## 4. Claim boundary

The certificate proves the finite algebraic identity, the nonnegative
coefficient sectors, and the stated containment witness.  It does not prove
`surv_C=infinity`, the integer renewal packing lemma, P17, P15, either
question in Erdős #1191, or a prize claim.
