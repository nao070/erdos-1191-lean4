from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import random

from endpoint_variance import (
    crossing_loads,
    endpoint_imbalance,
    forward_difference,
    homometric_distance_spectrum,
    offset_energies,
    poincare_lower_bound,
    short_pair_edges,
    variance,
    variance_from_imbalance,
)


def frac(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    checks = {
        "exhaustive_sets": 0,
        "arc_identities": 0,
        "difference_identities": 0,
        "variance_reconstructions": 0,
        "poincare_bounds": 0,
        "random_cases": 0,
    }

    for universe_size in range(1, 8):
        universe = range(universe_size)
        for size in range(universe_size + 1):
            for subset in combinations(universe, size):
                for modulus in range(2, 9):
                    edges = short_pair_edges(subset, modulus)
                    loads = crossing_loads(subset, modulus)
                    energies = offset_energies(subset, modulus)
                    delta = endpoint_imbalance(subset, modulus)
                    assert sum(loads) == sum(edge.distance for edge in edges)
                    assert sum(energies) == sum(modulus - edge.distance for edge in edges)
                    assert all(loads[r] + energies[r] == len(edges) for r in range(modulus))
                    checks["arc_identities"] += 1
                    assert forward_difference(loads) == delta
                    checks["difference_identities"] += 1
                    direct = variance(loads)
                    assert direct == variance(energies)
                    assert direct == variance_from_imbalance(delta)
                    checks["variance_reconstructions"] += 1
                    assert direct >= poincare_lower_bound(delta)
                    checks["poincare_bounds"] += 1
                    checks["exhaustive_sets"] += 1

    rng = random.Random(1191)
    for _ in range(2000):
        modulus = rng.randint(2, 40)
        size = rng.randint(0, 9)
        points = sorted(rng.sample(range(0, 100), size))
        loads = crossing_loads(points, modulus)
        delta = endpoint_imbalance(points, modulus)
        assert forward_difference(loads) == delta
        assert variance(loads) == variance_from_imbalance(delta)
        assert variance(loads) >= poincare_lower_bound(delta)
        checks["random_cases"] += 1

    left = [0, 1, 4, 10, 12, 17]
    right = [0, 1, 8, 11, 13, 17]
    left_v = variance(crossing_loads(left, 14))
    right_v = variance(crossing_loads(right, 14))
    assert homometric_distance_spectrum(left, right)
    assert left_v == Fraction(79, 28)
    assert right_v == Fraction(55, 28)

    zero_mode_n = 37
    zero_mode = [0, 1, zero_mode_n]
    assert variance(crossing_loads(zero_mode, zero_mode_n)) == 0
    assert endpoint_imbalance(zero_mode, zero_mode_n) == [0] * zero_mode_n

    payload = {
        "theorem": "endpoint-imbalance reconstruction of offset-energy variance",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "homometric_pair": {
            "left": left,
            "right": right,
            "modulus": 14,
            "left_variance": frac(left_v),
            "right_variance": frac(right_v),
            "difference": frac(left_v - right_v),
        },
        "zero_mode": {
            "family_instance": zero_mode,
            "modulus": zero_mode_n,
            "variance": "0/1",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["sha256"] = hashlib.sha256(canonical).hexdigest()
    Path("certificate.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
