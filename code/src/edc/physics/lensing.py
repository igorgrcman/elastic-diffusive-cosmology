"""GR weak-field point-mass lensing helpers.

Implements thin-lens point-mass deflection and the pixel-scale mapping used by
EDC demo scripts.

The physical model is baseline GR (weak-field Schwarzschild):
  \hat{\alpha}(b) = 4GM/(c^2 b)
  \alpha(\theta) = (D_ls/D_s) \hat{\alpha}(D_l \theta)
"""

from __future__ import annotations

import math
from typing import Literal


DistanceUnit = Literal["m", "km", "AU", "pc", "kpc", "Mpc", "Gpc"]


_UNIT_TO_METERS: dict[str, float] = {
    "m": 1.0,
    "km": 1e3,
    "AU": 149_597_870_700.0,  # IAU 2012 (exact)
    "pc": 3.085677581491367e16,
    "kpc": 3.085677581491367e19,
    "Mpc": 3.085677581491367e22,
    "Gpc": 3.085677581491367e25,
}


def distance_to_meters(value: float, units: DistanceUnit) -> float:
    """Convert a distance to meters."""
    if units not in _UNIT_TO_METERS:
        raise ValueError(f"Unsupported distance unit: {units!r}")
    return float(value) * _UNIT_TO_METERS[units]


def pixel_scale_rad(fov_deg: float, width_px: int) -> float:
    """Angular scale per pixel in radians/px, assuming a square FOV across width_px."""
    if width_px <= 0:
        raise ValueError("width_px must be positive")
    return math.radians(float(fov_deg)) / float(width_px)


def pixel_scale_arcsec(fov_deg: float, width_px: int) -> float:
    """Angular scale per pixel in arcseconds/px."""
    return pixel_scale_rad(fov_deg, width_px) * (180.0 / math.pi) * 3600.0


def gr_hat_deflection_rad(M_kg: float, b_m: float, *, G: float, c: float) -> float:
    """Weak-field point-mass bending angle (hat) in radians."""
    if b_m <= 0:
        raise ValueError("b_m must be positive")
    return 4.0 * G * float(M_kg) / (float(c) ** 2 * float(b_m))


def gr_hat_deflection_arcsec(M_kg: float, b_m: float, *, G: float, c: float) -> float:
    """Weak-field point-mass bending angle (hat) in arcseconds."""
    return gr_hat_deflection_rad(M_kg, b_m, G=G, c=c) * (180.0 / math.pi) * 3600.0


def thin_lens_deflection_rad(
    M_kg: float,
    Dl_m: float,
    Ds_m: float,
    theta_rad: float,
    *,
    G: float,
    c: float,
) -> float:
    """Observed deflection angle alpha(theta) for a point lens in thin-lens geometry.

    alpha(theta) = (D_ls/D_s) * 4GM/(c^2 * D_l * theta)

    Returns |alpha| in radians (direction is radial toward the lens).
    """
    if Dl_m <= 0 or Ds_m <= 0:
        raise ValueError("Distances must be positive")
    if Ds_m <= Dl_m:
        raise ValueError("Require Ds > Dl for lensing geometry")
    if theta_rad <= 0:
        raise ValueError("theta_rad must be positive")

    Dls = Ds_m - Dl_m
    return (4.0 * G * float(M_kg) / (float(c) ** 2)) * (Dls / (Dl_m * Ds_m)) * (1.0 / float(theta_rad))


def k_px2_from_physical(
    M_kg: float,
    Dl_m: float,
    Ds_m: float,
    *,
    fov_deg: float,
    width_px: int,
    G: float,
    c: float,
) -> float:
    """Compute the pixel-space strength parameter k (px^2) used by the demo.

    With a square field of view, each pixel corresponds to an angle theta_px.
    For a point mass in thin-lens geometry, the pixel shift magnitude becomes:
        |Δ| ≈ k / r_px

    where:
        k = [4GM/c^2 * (D_ls/(D_l D_s))] / theta_px^2
    """
    theta_px = pixel_scale_rad(fov_deg, width_px)
    Dls = Ds_m - Dl_m
    return (4.0 * G * float(M_kg) / (float(c) ** 2)) * (Dls / (Dl_m * Ds_m)) / (theta_px ** 2)
