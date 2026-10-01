from __future__ import annotations

import copy
from fractions import Fraction as F
import json
import unittest

import gram_marginal_transport_certificate as cert


class GramMarginalTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_certificate_validates(self) -> None:
        cert.validate_certificate(self.value)

    def test_02_committed_certificate_replays_byte_exactly(self) -> None:
        loaded = json.loads(cert.DEFAULT_CERTIFICATE.read_text(encoding="utf-8"))
        cert.validate_certificate(loaded)
        self.assertEqual(cert.rendered_bytes(loaded), cert.rendered_bytes(self.value))

    def test_03_strip_overlap_exhaustion(self) -> None:
        audit = cert.local_strip_audit()
        self.assertEqual(audit["rows_checked"], 2700)
        self.assertTrue(audit["same_sign_and_reverse_order_disjoint"])
        self.assertTrue(audit["overlap_equals_tent_numerator"])

    def test_04_fixture_is_golomb(self) -> None:
        self.assertEqual(len(cert.positive_differences(cert.GOL0MB)), 28)

    def test_05_wave_edges_are_exact(self) -> None:
        rows = cert.wave_edges(cert.GOL0MB)
        self.assertEqual([(r["left"], r["right"]) for r in rows], [(4, 6), (4, 7), (5, 7)])
        self.assertEqual([r["alpha"] for r in rows], ["1/16", "9/64", "1/16"])

    def test_06_each_stage_has_primal_dual_equality(self) -> None:
        stages = cert.marginal_price_fixture()["stages"]
        self.assertEqual(len(stages), 5)
        self.assertTrue(all(row["strong_duality_verified"] for row in stages))
        self.assertEqual(
            [row["price_coefficient_over_T_squared"] for row in stages],
            ["107/16", "27/2", "987/64", "987/64", "963/64"],
        )

    def test_07_integrated_price_is_exact(self) -> None:
        value = cert.marginal_price_fixture()["integrated_marginal_price"]
        self.assertEqual(F(value), F(32755417, 340707840))

    def test_08_gothic_separation_is_exact(self) -> None:
        row = self.value["gothic_separation"]
        self.assertEqual(F(row["positive_gothic_upper"]), F(81908500355, 936943462656))
        self.assertEqual(F(row["price_minus_gothic_upper"]), F(898545848033, 103063780892160))
        self.assertTrue(row["strict_separation_verified"])

    def test_09_payload_hash_is_canonical(self) -> None:
        self.assertEqual(self.value["integrity"]["payload_sha256"], cert.payload_hash(self.value))

    def test_10_scope_overclaim_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["status"] = "PRIZE_READY"
        cert.rehash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(changed)

    def test_11_stage_mutation_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["marginal_price"]["stages"][2]["price_coefficient_over_T_squared"] = "1/1"
        cert.rehash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(changed)

    def test_12_self_check_rejects_all_mutations(self) -> None:
        self.assertEqual(cert.self_check(self.value), 8)


if __name__ == "__main__":
    unittest.main()
