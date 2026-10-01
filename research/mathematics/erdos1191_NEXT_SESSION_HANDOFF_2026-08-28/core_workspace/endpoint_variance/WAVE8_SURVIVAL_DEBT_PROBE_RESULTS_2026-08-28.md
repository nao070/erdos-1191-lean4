# Wave 8 finite survival and non-adjacent debt probe

**Date:** 2026-08-28  
**Status:** three direct debt-repayment candidates are refuted, including one
after the actual-adjacent renewal reduces the history to a single outstanding
family.  A normalized reservoir/innovation comparison survives bounded
critical samples but is false without a critical-envelope hypothesis.  No
infinite extension or resolution of Erdős Problem #1191 is claimed.

## 1. Exact objects tested

At a threshold `T`, let `S(T)` be the endpoint-pair set in the active Wave 6
cross-antidiagonal families and let

\[
 P(T)=\sum_{m:\tau_{m,1}\le T}(m-1).
\]

For an active epoch and a cheap side `s` with mean `mu_s` and discrepancy
`D_s`, define

\[
 L_{m,s}(T)=\min\left\{m-1,
 \left\lfloor\frac{T-2D_s}{\mu_s}\right\rfloor\right\}.
\]

Every actual difference inside that half having rank lag at most `L_(m,s)`
is at most `T`.  The verifier enumerates every allowed old/new orientation,
forms the exact endpoint-pair union, removes `S(T)` and the selected adjacent
pairs, and calls the remaining non-adjacent set the **certified reservoir**.
Because every input is independently checked to be Golomb, counting endpoint
pairs is exactly the same as counting numerical differences.

It also computes two larger actual reservoirs:

1. all unused non-adjacent pairs in the history through the latest active
   shell whose difference is at most `floor(T)`;
2. the same set restricted to pairs whose right endpoint is born in the
   latest active shell.

The exact fixed-adjoint charge is

\[
 I_m=\left\langle H,Q_m/N_{2m}\right\rangle,
 \qquad
 H=\begin{pmatrix}16/15&8/105\\8/105&4/35\end{pmatrix}.
\]

All comparisons use `Fraction`; no floating-point value decides a result.

## 2. Candidates and verdicts

The following candidates were tested at every eligible activation threshold.

| label | proposed inequality | verdict |
|---|---|---|
| CRD | one coherent cheap-side choice has `U_cert >= P-new_adjacent` | **false** |
| CRT | `U_cert >= P` | **false** |
| GND | all historical actual non-adjacent differences repay the adjacent debt | **false** |
| LND | latest-shell actual non-adjacent differences repay that debt | **false** |
| CDQ | `U_cert/T >= I_m` | **false** |
| GDQ | `U_global/T >= I_m` | survives the bounded scopes, but is **false without a critical cap** |

The smallest displayed CRD witness is

```text
P = (0,4,10,13,15,27,34,35)
T = 25/2
tax = 4, adjacent debt = 3, certified non-adjacent reservoir = 0
```

It obeys every `C=1` prefix cap and has exact finite survival counts

```text
depth 0:      1
depth 1:    286
depth 2: 61,427
```

Thus `surv_1(P)>=2` does not repair CRD.  It says nothing about
`surv_1(P)=infinity`.

For GND, a bounded witness is

```text
P = (0,3,7,13,21,22,33,38)
T = 51/4
adjacent debt = 3
global non-adjacent reservoir = 2
latest-shell reservoir = 2
depth-two critical extensions = 61,448
```

Again, finite survival through two levels does not remove the counterexample.

## 3. Comparison with the actual-adjacent renewal theorem

The parallel actual-adjacent theorem proves that at a first-cross activation
the newborn internal adjacent family is paid, or all ancestry is cleared.
Consequently at most one internal family is outstanding.  Replacing the Wave
7 certified-set debt by this sharper actual debt still does not make raw
non-adjacent cardinality sufficient.

The exact counterexample is

```text
P = (0,2,5,6,14,25,32,42)
m = 4
tau_(4,1) = 43/4
newborn actual adjacent threshold = 11 > 43/4
outstanding demand = 3
global non-adjacent reservoir = 2
latest-shell non-adjacent reservoir = 1
```

This ruler obeys every `C=1` prefix cap.  Its finite critical-extension tree
has `(1,280,59,361)` nodes at depths `(0,1,2)`.  Therefore even

> actual single-family debt + finite survival depth two

does not imply non-adjacent repayment.

This is an immediate-repayment counterexample at the birth threshold.  It
does not contradict later ancestry clearance in the actual-adjacent theorem,
nor does it rule out a separately proved delayed non-adjacent charge.

## 4. Complete finite scopes

### Four marks

- 1,672 normalized `C=1` Golomb rulers;
- all 3,344 activation events with both dyadic epochs active;
- 74,506 exact one-step critical children;
- no root dies at depth one.

CRD fails at 1,534 events, GND at 306, and GDQ at 601.  These early failures
include boundary debt and show why at least one genuine renewal epoch is
needed before interpreting the density statistic.

### Eight marks, terminal mark at most 40

- 1,468 rulers;
- 889,645 DFS nodes;
- all 6,506 events with epochs `(1,2,4)` active;
- 1,146 of the rulers obey every `C=1` prefix cap;
- those roots have 320,051 exact one-step critical children and none dies.

Failure counts are:

```text
CRD: 901          CRT: 6,506
GND:  12          LND:    81
CDQ: 1,705        GDQ:     0
```

### Actual single-family renewal, terminal mark at most 45

The larger exhaustive scope contains 26,458 rulers and 2,742,059 DFS nodes.
At the `m=4` first-cross event:

```text
old-clear only:  1,250
new-pay only:      268
both sides paid: 24,940
```

Among the 1,250 genuinely outstanding single-family events, the global raw
debt inequality fails 6 times and the latest-shell version fails 16 times.
The normalized density comparisons do not fail in this bounded scope.  Their
minimum exact ratios are

\[
 \min \frac{U_{global}/T}{I_4}
 =\frac{186624000}{10274249}>18,
\]

and

\[
 \min \frac{U_{latest}/T}{I_4}
 =\frac{3250176}{354757}>9.
\]

These are finite minima, not universal constants.

### Authenticated 64/128 and gap-swap scope

The verifier re-authenticates the Wave 6 certificate, the Hall witness, six
64-mark rulers, the 128-mark ruler, and all 23 legal single adjacent-gap
swaps: 31 rulers and 1,924 threshold events.  GND, LND, and GDQ have no
negative event there.  Every one of the 156 actual renewal events pays both
actual sides, so the single-debt comparison is vacuous on these fixtures.

The new-preferred orientation is suboptimal at 221 authenticated events and
can lose 552 certified pairs.  The deterministic incremental greedy choice
matches the exact optimum at all 1,924 events.  This is only a finite
algorithmic observation; it is not a proof that greedy is universally exact.

## 5. Unrestricted density no-go

GDQ cannot hold for arbitrary Golomb rulers.  Start from

```text
B = (0,8,24,56,58,314,318,319)
```

and multiply every mark by 100.  At the `m=4` renewal event, the exact values
are

```text
T = 42449/2
U_global = 5
I_4 = 16828076637395 / 7660787849434944
```

and

\[
 \frac{U_{global}}T-I_4
 =-\frac{637727146686430915}
 {325192783420663937856}<0.
\]

The latest-shell density also fails.  This scaled ruler violates the `C=1`
prefix cap, so it refutes only an unconditional bridge.  It does not refute
a theorem which genuinely uses a critical envelope or
`surv_C(P)=infinity`.

## 6. What remains plausible

Raw non-adjacent cardinality cannot pay even the one outstanding actual
family.  A density-to-innovation bridge is also impossible without a growth
hypothesis.  The remaining admissible statement is therefore narrower:

> On one infinite eventually `C`-critical branch, prove that old-clear-only
> epochs cannot exhibit the scaling pathology above, and control their exact
> adjoint innovations by a summable or sub-logarithmic function of unused
> non-adjacent density and survival-sensitive capacity.

Finite survival depth one or two is demonstrably insufficient.  Any next
proof must exploit the full infinite branch, or derive a quantitative
consequence of arbitrarily deep critical extension which strengthens with
depth.

## 7. Reproducibility

Owned artifacts are:

- `wave8_survival_debt_probe.py`;
- `test_wave8_survival_debt_probe.py`;
- `wave8_survival_debt_certificate_2026-08-28.json`;
- this note.

Generate and test with

```text
PYTHONPATH=core_workspace/endpoint_variance \
python core_workspace/endpoint_variance/wave8_survival_debt_probe.py

PYTHONPATH=core_workspace/endpoint_variance \
pytest -q -p no:cacheprovider \
  core_workspace/endpoint_variance/test_wave8_survival_debt_probe.py
```

The certificate authenticates every stated finite scope and explicitly sets
`erdos_1191_resolved=false` and `infinite_extension_claimed=false`.
