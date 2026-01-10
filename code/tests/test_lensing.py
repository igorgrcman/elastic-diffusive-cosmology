import math
import pathlib
import sys
import unittest

# Allow running tests without installing the package.
CODE_DIR = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = CODE_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from edc.constants.registry import get_constant
from edc.physics.lensing import (
    distance_to_meters,
    gr_hat_deflection_arcsec,
    k_px2_from_physical,
    pixel_scale_rad,
)


class TestGRPointMassLensing(unittest.TestCase):
    def test_solar_limb_deflection_arcsec(self) -> None:
        """Baseline GR benchmark: ~1.75 arcsec deflection at the solar limb."""
        G = get_constant("G", allow={"BASELINE"}).value
        c = get_constant("c", allow={"BASELINE"}).value
        M_sun = get_constant("M_sun", allow={"BASELINE"}).value
        R_sun = get_constant("R_sun", allow={"BASELINE"}).value

        alpha_arcsec = gr_hat_deflection_arcsec(M_sun, R_sun, G=G, c=c)
        # Reference value computed from the same formula with standard constants:
        # ~1.7512 arcsec. Use a small tolerance to allow for constant rounding.
        self.assertAlmostEqual(alpha_arcsec, 1.7512, delta=0.002)

    def test_distance_units(self) -> None:
        """1 Mpc equals 1e6 parsecs."""
        pc_m = distance_to_meters(1.0, "pc")
        self.assertAlmostEqual(distance_to_meters(1.0, "Mpc"), 1.0e6 * pc_m, delta=1e-3 * pc_m)

    def test_k_linear_in_mass(self) -> None:
        """Pixel-space k should scale linearly with lens mass."""
        G = get_constant("G", allow={"BASELINE"}).value
        c = get_constant("c", allow={"BASELINE"}).value
        M_sun = get_constant("M_sun", allow={"BASELINE"}).value

        Dl = distance_to_meters(1.0, "Mpc")
        Ds = distance_to_meters(2.0, "Mpc")

        k1 = k_px2_from_physical(M_sun, Dl, Ds, fov_deg=2.0, width_px=800, G=G, c=c)
        k2 = k_px2_from_physical(2.0 * M_sun, Dl, Ds, fov_deg=2.0, width_px=800, G=G, c=c)

        self.assertAlmostEqual(k2 / k1, 2.0, delta=1e-12)

    def test_k_matches_closed_form(self) -> None:
        """k formula matches the derived mapping used by the visualization."""
        G = get_constant("G", allow={"BASELINE"}).value
        c = get_constant("c", allow={"BASELINE"}).value
        M = get_constant("M_sun", allow={"BASELINE"}).value

        Dl = distance_to_meters(1.0, "Mpc")
        Ds = distance_to_meters(2.0, "Mpc")
        Dls = Ds - Dl

        theta_per_px = pixel_scale_rad(fov_deg=2.0, width_px=800)
        expected_k = (4.0 * G * M / (c * c)) * (Dls / (Dl * Ds)) / (theta_per_px * theta_per_px)

        got_k = k_px2_from_physical(M, Dl, Ds, fov_deg=2.0, width_px=800, G=G, c=c)
        self.assertAlmostEqual(got_k, expected_k, delta=abs(expected_k) * 1e-12 + 1e-30)


if __name__ == "__main__":
    unittest.main()
