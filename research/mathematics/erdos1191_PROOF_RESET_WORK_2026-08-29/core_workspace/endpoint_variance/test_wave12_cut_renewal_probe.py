from __future__ import annotations

import json
import tempfile
import unittest
from hashlib import sha256
from itertools import pairwise
from pathlib import Path

from complete_birth_ledger import erdos_turan_ruler
from wave12_cut_renewal_probe import (
    DEFAULT_WAVE11_CERTIFICATE,
    algebraic_renewal_coefficients,
    build_certificate,
    containment_floor_audit,
    cumulative_bulk_count,
    quadratic_birth_value,
    quadratic_limit,
    renewal_audit,
    renewal_coefficients,
    renewal_sector_coefficients,
)


class Wave12CutRenewalTests(unittest.TestCase):
    def test_pair_coefficient_oracles_agree(self) -> None:
        for m, horizon in ((4, 7), (4, 31), (8, 31), (8, 63), (16, 63)):
            with self.subTest(m=m, horizon=horizon):
                self.assertEqual(
                    renewal_coefficients(m, horizon),
                    algebraic_renewal_coefficients(m, horizon),
                )

    def test_all_four_sectors_are_coefficientwise_nonnegative(self) -> None:
        for m, horizon in ((4, 31), (8, 63), (16, 127)):
            with self.subTest(m=m, horizon=horizon):
                sectors = renewal_sector_coefficients(m, horizon)
                self.assertEqual(len(sectors), 4)
                self.assertTrue(
                    all(
                        coefficient >= 0
                        for mapping in sectors.values()
                        for coefficient in mapping.values()
                    )
                )

    def test_exact_form_identity_on_integer_golomb_ruler(self) -> None:
        points = erdos_turan_ruler(64, 131)
        for m in (4, 8, 16, 32):
            with self.subTest(m=m):
                audit = renewal_audit(points, m)
                self.assertTrue(audit.pair_coefficient_identity)
                self.assertTrue(audit.sector_coefficients_nonnegative)
                self.assertTrue(audit.exact_form_identity)
                self.assertTrue(audit.primitive_cross_ratios_positive)

    def test_containment_witness_is_a_full_linear_extension(self) -> None:
        audit = containment_floor_audit(16, exhaustive_order_check=True)
        self.assertEqual(audit.atom_count, cumulative_bulk_count(16))
        self.assertTrue(audit.count_formula_verified)
        self.assertTrue(audit.witness_is_full_containment_linear_extension)
        self.assertTrue(audit.all_epoch_ranks_below_two_m_squared)
        self.assertTrue(audit.witness_gain_below_five_per_epoch)

    def test_containment_floor_gain_is_bounded_per_epoch(self) -> None:
        audit = containment_floor_audit(128)
        self.assertTrue(audit.witness_gain_below_five_per_epoch)
        self.assertLess(
            audit.witness_gain_float_projection,
            5 * audit.epoch_count,
        )
        self.assertLess(audit.cap_gain_float_projection, 5 * audit.epoch_count)
        self.assertTrue(
            all(value < 5 for value in audit.per_epoch_gain_float_projections.values())
        )
        self.assertTrue(
            all(
                value < 5
                for value in audit.per_epoch_cap_gain_float_projections.values()
            )
        )

    def test_quadratic_real_model_converges_to_positive_limit(self) -> None:
        expected = quadratic_limit()
        values = [quadratic_birth_value(m) for m in (32, 64, 128, 256, 512)]
        self.assertGreater(expected, 0)
        self.assertTrue(all(left < right for left, right in pairwise(values)))
        self.assertLess(abs(values[-1] - expected), 0.001)

    def test_certificate_is_deterministic_and_self_hashed(self) -> None:
        first = build_certificate(DEFAULT_WAVE11_CERTIFICATE)
        second = build_certificate(DEFAULT_WAVE11_CERTIFICATE)
        self.assertEqual(first, second)
        internal_hash = first.pop("certificate_sha256")
        canonical = json.dumps(first, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())
        self.assertFalse(first["claim_boundary"]["p17_proved"])

        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            output.write_text(
                json.dumps(second, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            reloaded = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(reloaded, second)


if __name__ == "__main__":
    unittest.main()
