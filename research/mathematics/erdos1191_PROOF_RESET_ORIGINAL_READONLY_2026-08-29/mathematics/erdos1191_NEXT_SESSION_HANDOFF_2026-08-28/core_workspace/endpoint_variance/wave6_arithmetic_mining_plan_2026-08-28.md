# Wave 6 Arithmetic Mining Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an exact birth-lag interval/Hall-pressure oracle, mine all authenticated Wave 5 witnesses and the non-Sidon sawtooth, and certify one heuristic 128-mark extension.

**Architecture:** A pure exact-analysis module partitions all rank pairs by dyadic birth epoch, `ON`/`NN` category, and rank lag; a separate generator authenticates inputs, optionally runs the targeted extension, and serializes exact audits.  Tests use hand-derived fixtures and the committed certificate, while the results note separates the exact Hall theorem from heuristic discovery.

**Tech Stack:** Python 3.13.13, standard-library `dataclasses`, `fractions`, `hashlib`, and `json`; existing read-only Wave 4/5 exact audit modules.

**Spec:** `wave6_arithmetic_mining_design_2026-08-28.md`

## Global Constraints

- Create only files beginning with `wave6_arithmetic_mining_` in `core_workspace/endpoint_variance`.
- Do not modify Wave 5 or other agents' files.
- Serialize exact integers and rational strings only; no float-derived certificate fields.
- Authenticate Wave 5 hash `a26c13574002eb442731bcbec465a5fa7553a25728e2225ddba942e6df4d3ceb`.
- Record runtime/source provenance and limit canonical byte claims to the recorded runtime.
- State that every conclusion is finite unless separately proved as an exact finite theorem.
- Work in the shared checkout without creating commits.

---

### Task 1: Exact birth-lag pair partition

**Files:**
- Create: `wave6_arithmetic_mining_test.py`
- Create: `wave6_arithmetic_mining_search.py`

**Interfaces:**
- Consumes: a strictly increasing integer `tuple[int, ...]` of power-of-two length.
- Produces: `LagFamilyAudit` and `birth_lag_families(points) -> tuple[LagFamilyAudit, ...]`.

- [ ] **Step 1: Write the failing four-mark partition test**

```python
def test_four_mark_birth_lag_partition_is_exact(self) -> None:
    families = mining.birth_lag_families((0, 1, 4, 6))
    keyed = {(f.epoch, f.category, f.lag): f for f in families}
    self.assertEqual(sum(f.demand for f in families), 6)
    self.assertEqual(keyed[(4, "ON", 2)].pairs, ((0, 2), (1, 3)))
    self.assertEqual(keyed[(4, "ON", 2)].differences, (4, 5))
    self.assertEqual((keyed[(4, "ON", 2)].lower,
                      keyed[(4, "ON", 2)].upper,
                      keyed[(4, "ON", 2)].width), (4, 5, 2))
```

- [ ] **Step 2: Run the test and verify RED**

Run: `python3 -m unittest -v wave6_arithmetic_mining_test.Wave6ArithmeticMiningTests.test_four_mark_birth_lag_partition_is_exact`

Expected: import failure because `wave6_arithmetic_mining_search` does not yet exist.

- [ ] **Step 3: Implement validation, epoch assignment, and exact rows**

```python
@dataclass(frozen=True)
class LagFamilyAudit:
    epoch: int
    category: str
    lag: int
    pairs: tuple[tuple[int, int], ...]
    differences: tuple[int, ...]
    demand: int
    distinct_count: int
    collision_deficit: int
    lower: int
    upper: int
    width: int

def birth_lag_families(points: Sequence[int]) -> tuple[LagFamilyAudit, ...]:
    marks = _validated_power_two_points(points)
    grouped: dict[tuple[int, str, int], list[tuple[int, int, int]]] = {}
    for right in range(1, len(marks)):
        epoch = 1 << right.bit_length()
        boundary = epoch // 2
        for left in range(right):
            category = "ON" if left < boundary else "NN"
            grouped.setdefault((epoch, category, right - left), []).append(
                (left, right, marks[right] - marks[left])
            )
    rows = []
    for (epoch, category, lag), entries in sorted(grouped.items()):
        pairs = tuple((left, right) for left, right, _ in entries)
        differences = tuple(difference for _, _, difference in entries)
        rows.append(LagFamilyAudit(
            epoch, category, lag, pairs, differences, len(entries),
            len(set(differences)), len(entries) - len(set(differences)),
            min(differences), max(differences),
            max(differences) - min(differences) + 1,
        ))
    assert sum(row.demand for row in rows) == len(marks) * (len(marks) - 1) // 2
    return tuple(rows)
```

- [ ] **Step 4: Run the focused test and full new test file**

Run: `python3 -m unittest -v wave6_arithmetic_mining_test.py`

Expected: PASS.

- [ ] **Step 5: Review checkpoint**

Confirm that the families cover exactly `binom(M,2)` distinct rank pairs and that no Wave 5 file changed.

---

### Task 2: Exact interval Hall-pressure oracle

**Files:**
- Modify: `wave6_arithmetic_mining_test.py`
- Modify: `wave6_arithmetic_mining_search.py`

**Interfaces:**
- Consumes: `tuple[LagFamilyAudit, ...]` plus optional categories, epochs, minimum demand, and minimum epoch count.
- Produces: `HallPressureAudit | None` via `hall_pressure(...)`.

- [ ] **Step 1: Add failing Golomb and sawtooth tests**

```python
def test_golomb_hall_pressure_is_at_most_one(self) -> None:
    audit = mining.hall_pressure(mining.birth_lag_families((0, 1, 4, 6)),
                                 min_family_demand=1,
                                 min_epoch_count=1)
    self.assertIsNotNone(audit)
    self.assertLessEqual(audit.ratio, Fraction(1))

def test_sawtooth_two_epoch_nn_pressure_is_exactly_46(self) -> None:
    points = build_sawtooth_gap_profile(6).points
    audit = mining.hall_pressure(mining.birth_lag_families(points),
                                 categories=("NN",),
                                 epochs=(32, 64),
                                 min_family_demand=2,
                                 min_epoch_count=2)
    self.assertEqual((audit.lower, audit.upper, audit.demand,
                      audit.width, audit.ratio),
                     (64, 64, 46, 1, Fraction(46)))
    self.assertEqual(tuple((f.epoch, f.lag, f.demand) for f in audit.families),
                     ((32, 1, 15), (64, 1, 31)))
```

- [ ] **Step 2: Run both tests and verify RED**

Expected: attribute/import failure for `hall_pressure`.

- [ ] **Step 3: Implement the exact endpoint scan**

```python
@dataclass(frozen=True)
class HallPressureAudit:
    lower: int
    upper: int
    width: int
    demand: int
    ratio: Fraction
    represented_epochs: tuple[int, ...]
    families: tuple[LagFamilyAudit, ...]

def hall_pressure(families, *, categories=("ON", "NN"), epochs=None,
                  min_family_demand=2, min_epoch_count=2):
    allowed_categories = frozenset(categories)
    allowed_epochs = None if epochs is None else frozenset(epochs)
    eligible = tuple(
        family for family in families
        if family.category in allowed_categories
        and (allowed_epochs is None or family.epoch in allowed_epochs)
        and family.demand >= min_family_demand
    )
    endpoints = sorted({f.lower for f in eligible} | {f.upper for f in eligible})
    best = None
    for lower in endpoints:
        for upper in endpoints:
            if upper < lower:
                continue
            contained = tuple(
                family for family in eligible
                if lower <= family.lower and family.upper <= upper
            )
            represented = tuple(sorted({f.epoch for f in contained}))
            if len(represented) < min_epoch_count:
                continue
            demand = sum(f.demand for f in contained)
            width = upper - lower + 1
            candidate = HallPressureAudit(
                lower, upper, width, demand, Fraction(demand, width),
                represented, contained,
            )
            if best is None or _hall_rank(candidate) > _hall_rank(best):
                best = candidate
    return best
```

- [ ] **Step 4: Verify GREEN and add theorem invariant checks**

Run: `python3 -m unittest -v wave6_arithmetic_mining_test.py`

Expected: all tests PASS; additionally assert every authenticated Golomb fixture has ratio `<=1`.

- [ ] **Step 5: Review checkpoint**

Check the maximizer against an independent brute scan over all integer intervals on the four-mark fixture.

---

### Task 3: Descriptive ON/NN transition spectra

**Files:**
- Modify: `wave6_arithmetic_mining_test.py`
- Modify: `wave6_arithmetic_mining_search.py`

**Interfaces:**
- Produces `CategorySpectrumAudit`, `TransitionPackingAudit`, and `transition_packing(points, new_count)`.

- [ ] **Step 1: Add failing hand-fixture assertions**

```python
def test_four_mark_transition_splits_on_and_nn_exactly(self) -> None:
    row = mining.transition_packing((0, 1, 4, 6), new_count=4)
    self.assertEqual(row.old_new.pair_count, 4)
    self.assertEqual(row.old_new.differences, (3, 4, 5, 6))
    self.assertEqual(row.new_new.differences, (2,))
    self.assertEqual(row.overlap_width, 0)
    self.assertEqual(row.cross_collision_values, ())
```

- [ ] **Step 2: Run the test and verify RED**

Expected: `transition_packing` missing.

- [ ] **Step 3: Implement category spectra and overlap accounting**

Compute pair/difference tuples for `left < m <= right` and
`m <= left < right < 2m`, exact hull intersection, distinct occupied values
inside it, and set intersection of actual values.

```python
def transition_packing(points: Sequence[int], *, new_count: int) -> TransitionPackingAudit:
    marks = _validated_power_two_points(tuple(points)[:new_count])
    old_count = new_count // 2
    old_new_pairs = tuple(
        (left, right) for left in range(old_count)
        for right in range(old_count, new_count)
    )
    new_new_pairs = tuple(
        (left, right) for left in range(old_count, new_count)
        for right in range(left + 1, new_count)
    )
    old_new = _category_spectrum(marks, "ON", old_new_pairs)
    new_new = _category_spectrum(marks, "NN", new_new_pairs)
    lower = max(old_new.lower, new_new.lower)
    upper = min(old_new.upper, new_new.upper)
    return _transition_from_spectra(new_count, old_new, new_new, lower, upper)
```

- [ ] **Step 4: Verify the hand fixture and sawtooth collision rows**

Run: `python3 -m unittest -v wave6_arithmetic_mining_test.py`

Expected: PASS, including a sawtooth assertion that the 32-to-64 `ON` and
`NN` spectra share actual difference 64.

- [ ] **Step 5: Review checkpoint**

Confirm pair counts are `m^2` and `binom(m,2)` at every dyadic transition.

---

### Task 4: Authenticated mining and targeted 128 extension

**Files:**
- Modify: `wave6_arithmetic_mining_test.py`
- Modify: `wave6_arithmetic_mining_search.py`
- Create: `wave6_arithmetic_mining_certificate.py`

**Interfaces:**
- Produces `WitnessArithmeticAudit` via `audit_witness(points)`.
- Produces a payload via `build_payload(wave5_certificate, beam_width=32, candidates_per_state=16, seed=601191)`.

- [ ] **Step 1: Add failing authentication and small-payload tests**

Test that a copied Wave 5 payload with a changed point fails its internal hash,
that all six authenticated witnesses are enumerated, and that exact payload
rows contain no Python floats or `_decimal` keys.

- [ ] **Step 2: Run tests and verify RED**

Expected: missing certificate module or `build_payload`.

- [ ] **Step 3: Implement exact witness audits**

```python
@dataclass(frozen=True)
class WitnessArithmeticAudit:
    points: tuple[int, ...]
    pair_count: int
    sorted_differences: tuple[int, ...]
    difference_collisions: tuple[
        tuple[int, tuple[tuple[int, int], ...]], ...
    ]
    lag_families: tuple[LagFamilyAudit, ...]
    transition_rows: tuple[TransitionPackingAudit, ...]
    adjacent_nn_pressures: tuple[HallPressureAudit, ...]
```

Require Golomb uniqueness for authenticated/extended witnesses but permit and
record collisions for the labeled sawtooth control.

- [ ] **Step 4: Implement deterministic generator and targeted extension**

Authenticate the Wave 5 internal hash, pass its leading persistence witness to
`beam_extend_nested` with sizes `(4,8,16,32,64,128)`, `C=1`, beam 32,
candidates 16, seed 601191, retain 1, then independently call the existing
nested audit and the new arithmetic audit.  Snapshot source hashes before the
search and abort if they change before serialization.

- [ ] **Step 5: Run small tests and verify GREEN**

Run: `python3 -m unittest -v wave6_arithmetic_mining_test.py`

Expected: PASS without rerunning the full canonical extension in ordinary unit
tests; the committed-artifact test covers the full result after Task 5.

---

### Task 5: Canonical certificate, results, and independent replay

**Files:**
- Create: `wave6_arithmetic_mining_certificate_2026-08-28.json`
- Create: `wave6_arithmetic_mining_results_2026-08-28.md`
- Modify: `wave6_arithmetic_mining_test.py`

**Interfaces:**
- Consumes all Task 1-4 APIs.
- Produces the final hash-bearing research artifact and human-readable finite-scope report.

- [ ] **Step 1: Generate the full certificate on the release interpreter**

Run:

```bash
/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python \
  wave6_arithmetic_mining_certificate.py \
  --wave5-certificate wave5_nested_certificate_2026-08-28.json \
  --beam-width 32 --candidates-per-state 16 --seed 601191 \
  --output wave6_arithmetic_mining_certificate_2026-08-28.json
```

Expected: one authenticated JSON containing six 64-mark audits, sawtooth64,
and one audited 128-mark heuristic witness.

- [ ] **Step 2: Add and run the committed-certificate test**

Validate the internal canonical hash, recorded runtime, complete source
manifest, Wave 5 parent hash, `6*2016 + 8128` independently unique Golomb
differences, sawtooth collisions, exact family reconstruction, and
`Lambda_NN=46`.

- [ ] **Step 3: Write the results note**

Report the exact theorem, all adjacent-epoch NN pressure rows, ON/NN range
tables, the 128 witness/search parameters, candidate reset-renewal
interpretation, reproduction command, canonical/source hashes, and explicit
finite/asymptotic limitations.

- [ ] **Step 4: Run focused and compatibility tests**

Run:

```bash
/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python -m unittest -v \
  wave6_arithmetic_mining_test.py wave5_nested_test.py test_wave5_cross_epoch.py
```

Expected: zero failures.

- [ ] **Step 5: Run an independent replay**

Use a standalone inline Python audit that does not trust stored counts: rebuild
all pair differences and birth-lag families from points, recompute every band
and Hall maximum, validate all-prefix `C=1` for the 128 witness, verify source
hashes, and assert the results note contains the final canonical hash.

- [ ] **Step 6: Final review checkpoint**

Search all Wave 6 files for `optimal`, `asymptotic`, `proof`, `best`, and
`counterexample`; retain only wording explicitly supported by the exact finite
theorem or clearly qualified heuristic evidence.
