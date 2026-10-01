from __future__ import annotations

from fractions import Fraction
import unittest

import wave5_cross_epoch as cross_epoch


class CrossEpochTests(unittest.TestCase):
    def test_q_step_transport_has_the_hand_derived_coefficients(self) -> None:
        # Catches using the adjacent B matrix without taking the full q-step
        # transport, or dropping the u contribution to f(u/q).
        self.assertEqual(
            cross_epoch.q_step_transport_matrix(4),
            (
                (Fraction(1, 16), Fraction(3, 16)),
                (Fraction(0), Fraction(1, 4)),
            ),
        )

    def test_uniform_newborn_half_has_the_exact_variance_floor(self) -> None:
        # The analytic formula is the shell term used in the infinite
        # counterprofile, not a floating-point estimate from a finite run.
        self.assertEqual(
            cross_epoch.uniform_upper_half_f_variance(2), Fraction(1, 1024)
        )
        self.assertEqual(
            cross_epoch.uniform_upper_half_f_variance(4), Fraction(49, 16384)
        )
        self.assertGreater(
            cross_epoch.uniform_upper_half_f_variance(17), Fraction(1, 1024)
        )

    def test_old_profile_curvature_persists_after_subtracting_the_chord(self) -> None:
        # For this hand fixture N_4=7 and N_8=76.  At r=2,
        # e_8(2)=-4/19, e_8(4)=-31/76, and the residual is -1/152.
        points = (0, 2, 5, 6, 28, 36, 43, 75)
        row = cross_epoch.profile_persistence_row(
            points, old_count=4, final_count=8, rank=2
        )
        self.assertEqual(row.old_mass, Fraction(7, 76))
        self.assertEqual(row.old_error, Fraction(-1, 14))
        self.assertEqual(row.final_error, Fraction(-4, 19))
        self.assertEqual(row.chord_error, Fraction(-31, 152))
        self.assertEqual(row.residual, Fraction(-1, 152))
        self.assertEqual(row.transported_old_error, Fraction(-1, 152))

    def test_sawtooth_multiplier_has_flat_descents_and_large_resets(self) -> None:
        # Catches resetting every step, failing to halve, or using a
        # non-dyadic reset height.
        self.assertEqual(
            cross_epoch.sawtooth_multipliers(15),
            (1, 2, 1, 4, 2, 1, 4, 2, 1, 8, 4, 2, 1, 8, 4),
        )

    def test_integer_gap_counterprofile_has_exact_moduli_and_a_collision(self) -> None:
        # Catches confusing the diameter D with the modulus N=D+1, or
        # accidentally presenting the counterprofile as a Golomb ruler.
        profile = cross_epoch.build_sawtooth_gap_profile(4)
        self.assertEqual(
            profile.points,
            (0, 3, 17, 31, 39, 47, 55, 63, 183, 303, 423, 543, 663, 783, 903, 1023),
        )
        self.assertEqual(profile.dyadic_moduli, (4, 32, 64, 1024))
        # Numerically smallest repeated value in this 16-mark prefix.  The
        # temporally earliest violation already occurred at four marks (14).
        self.assertEqual(profile.smallest_repeated_difference, 8)

    def test_balanced_flat_shell_halves_the_entire_old_profile_error(self) -> None:
        # Level 2 is a reset.  The balanced flat extension to level 3 has
        # zero error on its newborn half and exactly halves every old error.
        profile = cross_epoch.build_sawtooth_gap_profile(3)
        level_two = cross_epoch.grid_profile_errors(profile.points, 4)
        level_three = cross_epoch.grid_profile_errors(profile.points, 8)
        self.assertEqual(
            level_two,
            (
                Fraction(0),
                Fraction(-7, 32),
                Fraction(-3, 8),
                Fraction(-3, 16),
                Fraction(0),
            ),
        )
        self.assertEqual(
            level_three[:5],
            tuple(error / 2 for error in level_two),
        )
        self.assertEqual(level_three[4:], (Fraction(0),) * 5)

    def test_counterprofile_has_a_uniform_exact_innovation_floor(self) -> None:
        # Catches normalizing Q_00 by the old modulus or misweighting the
        # exactly uniform newborn shell.  The first value is hand checked.
        profile = cross_epoch.build_sawtooth_gap_profile(10)
        self.assertEqual(
            profile.transitions[0].innovation_q00_per_new_modulus,
            Fraction(399, 262144),
        )
        self.assertTrue(
            all(
                row.innovation_q00_per_new_modulus >= Fraction(1, 2048)
                for row in profile.transitions
            )
        )
        self.assertTrue(all(row.scalar_sidon_lower_bound for row in profile.levels))
        self.assertTrue(all(row.critical_c1_dyadic_bound for row in profile.levels))


if __name__ == "__main__":
    unittest.main()
