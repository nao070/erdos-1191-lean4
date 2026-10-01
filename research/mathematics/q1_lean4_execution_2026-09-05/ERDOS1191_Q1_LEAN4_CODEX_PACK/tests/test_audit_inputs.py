"""Behavior tests for the small report auditor; these do not validate Q1."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[1]

class AuditTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "scripts" / "audit_inputs.py"
        self.assertTrue(path.exists(), "The report audit implementation must exist")
        spec = importlib.util.spec_from_file_location("audit_inputs", path)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        self.data = json.loads((ROOT / "inputs" / "c143_full_pricing_replay.full.json").read_text())

    def test_valid_uploaded_report(self):
        result = self.mod.audit_report(self.data)
        self.assertEqual(result["status"], "REPORT_ARITHMETIC_VERIFIED")
        self.assertFalse(result["full_pricing_replayed"])
        self.assertFalse(result["Q1_proved"])

    def test_reject_wrong_check_count(self):
        d = copy.deepcopy(self.data)
        d["full_root_endpoint_checks"] = 10
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

    def test_reject_reversed_interval(self):
        d = copy.deepcopy(self.data)
        d["aggregate_lower"], d["aggregate_upper"] = d["aggregate_upper"], d["aggregate_lower"]
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

    def test_reject_failed_exit(self):
        d = copy.deepcopy(self.data)
        d["exit_code"] = 1
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

    def test_reject_false_completion_claim(self):
        d = copy.deepcopy(self.data)
        d["scope"]["Q1_resolved"] = True
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

    def test_reject_margin_sign_change(self):
        d = copy.deepcopy(self.data)
        d["min_pointwise_child_margin"] = "-1/10"
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

    def test_reject_false_interval_bound(self):
        d = copy.deepcopy(self.data)
        d["aggregate_upper"] = "1/2"
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

    def test_reject_missing_field(self):
        d = copy.deepcopy(self.data)
        del d["children_checked"]
        with self.assertRaises(ValueError):
            self.mod.audit_report(d)

if __name__ == "__main__":
    unittest.main()
