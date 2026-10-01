from __future__ import annotations

from fractions import Fraction
import unittest

from innovation_budget import (
    ABSTRACT_COVARIANCE,
    E_MATRIX,
    LYAPUNOV_MATRIX,
    abstract_raw_innovation,
    adjoint_transport,
    audit_abstract_orbit,
    determinant,
    matrix_subtract,
    three_point_covariance,
    verify_infinite_horizon_lyapunov_matrix,
)
from gap_measure_dynamics import is_positive_semidefinite


class InnovationBudgetTests(unittest.TestCase):
    def test_exact_lyapunov_solution(self) -> None:
        self.assertTrue(verify_infinite_horizon_lyapunov_matrix())
        self.assertEqual(
            matrix_subtract(LYAPUNOV_MATRIX, adjoint_transport(LYAPUNOV_MATRIX)),
            E_MATRIX,
        )
        self.assertEqual(determinant(LYAPUNOV_MATRIX), Fraction(256, 2205))

    def test_abstract_covariance_is_function_realizable(self) -> None:
        self.assertEqual(three_point_covariance(), ABSTRACT_COVARIANCE)

    def test_abstract_innovations_are_positive_definite(self) -> None:
        for index in range(1, 257):
            innovation = abstract_raw_innovation(index)
            self.assertTrue(is_positive_semidefinite(innovation))
            self.assertGreater(determinant(innovation), 0)

    def test_adjoint_identity_on_abstract_orbit(self) -> None:
        for horizon in (1, 2, 3, 8, 32, 128):
            audit = audit_abstract_orbit(horizon)
            self.assertEqual(audit.functional_sum, Fraction(horizon, 72))
            self.assertEqual(
                audit.functional_sum,
                audit.boundary_term + audit.innovation_sum,
            )


if __name__ == "__main__":
    unittest.main()
