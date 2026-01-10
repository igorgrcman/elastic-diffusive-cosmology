#!/usr/bin/env python3
"""
EDC / GR Lensing Demonstration (Strict Epistemic Labelling)

This script generates a simple background (grid + point-like stars) and applies a
thin-lens-style deflection field to produce a lensing-like distortion.

Epistemic status rules (EDC Rigor Standard):
- DEMO mode: uses an arbitrary "strength" parameter -> PROPOSED (illustrative).
- PHYSICAL mode: uses the weak-field GR point-mass deflection with user-supplied
  M, D_l, D_s and FOV -> BASELINE (because it injects external astronomical inputs).

IMPORTANT:
This is a visualization tool. It does not by itself establish that EDC derives
the lensing law from first principles unless the mapping parameters are derived
within the theory rather than injected.

Output: saves a PNG to ./artifacts (created if missing).
"""

from __future__ import annotations

import argparse
import math
import os
from dataclasses import dataclass
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Baseline constants (only used in PHYSICAL mode)
# -----------------------------
C_LIGHT = 299_792_458.0  # m/s (exact)
G_NEWTON = 6.67430e-11   # m^3 kg^-1 s^-2 (CODATA-like nominal)


@dataclass(frozen=True)
class LensConfig:
    width: int = 800
    height: int = 800
    grid_step: int = 20
    n_stars: int = 50
    star_radius_px: int = 5
    bh_radius_px: int = 20
    seed: int = 42


def make_background(cfg: LensConfig) -> np.ndarray:
    """
    Create a simple test image (grid + stars).
    Returns an RGB image in [0, 1].
    """
    w, h = cfg.width, cfg.height
    img = np.zeros((h, w, 3), dtype=float)

    # Blue grid
    img[::cfg.grid_step, :, 2] = 0.8
    img[:, ::cfg.grid_step, 2] = 0.8

    # Stars: white disks
    rng = np.random.default_rng(cfg.seed)
    yy, xx = np.ogrid[:h, :w]
    for _ in range(cfg.n_stars):
        y_c = int(rng.integers(100, h - 100))
        x_c = int(rng.integers(100, w - 100))
        star_mask = (xx - x_c) ** 2 + (yy - y_c) ** 2 <= (cfg.star_radius_px ** 2)
        img[star_mask] = 1.0

    return img


def compute_strength_demo(strength: float) -> Tuple[float, str]:
    """
    DEMO mode: user supplies a dimensionless strength, we convert to k (px^2).
    Shift magnitude is: |Δ| = k / r  (pixels), so k has units of px^2.
    """
    # PROPOSED: purely illustrative mapping between a slider and pixel strength.
    k = float(strength) ** 2
    return k, "[STATUS: PROPOSED] DEMO strength parameter (illustrative)"


def compute_strength_physical(
    mass_kg: float,
    d_l_m: float,
    d_s_m: float,
    fov_deg: float,
    width_px: int,
) -> Tuple[float, str]:
    """
    PHYSICAL mode: derive k (px^2) from the weak-field GR point-mass deflection.

    Thin lens relation in angle:
        beta = theta - (D_ls/D_s) * alpha_hat
    with alpha_hat = 4GM/(c^2 b) and b = theta * D_l.

    Converting to pixels with angle_per_pixel = fov / width:
        shift_pixels ≈ (D_ls/D_s) * alpha_hat / angle_per_pixel
                    = k / r_pixels

    This yields:
        k = (D_ls/D_s) * 4GM / (c^2 * D_l * angle_per_pixel^2)

    NOTE: This uses baseline constants + external astrophysical inputs -> BASELINE.
    """
    if d_s_m <= d_l_m:
        raise ValueError("Need D_s > D_l (source must be behind the lens).")

    d_ls = d_s_m - d_l_m
    angle_per_pixel = math.radians(fov_deg) / float(width_px)
    k = (d_ls / d_s_m) * (4.0 * G_NEWTON * mass_kg) / (C_LIGHT ** 2 * d_l_m * angle_per_pixel ** 2)

    return float(k), "[STATUS: BASELINE] GR weak-field point-mass thin-lens mapping"


def apply_lens(img: np.ndarray, k_px2: float, cfg: LensConfig) -> np.ndarray:
    """
    Apply a radial deflection:
        Δ = (k / r) * r_hat

    Implementation:
        src = x - Δx, y - Δy
    """
    h, w = cfg.height, cfg.width
    y, x = np.ogrid[:h, :w]
    cx, cy = w // 2, h // 2
    dx = x - cx
    dy = y - cy
    r = np.sqrt(dx ** 2 + dy ** 2).astype(float)
    r[r == 0] = 1.0

    # Deflection magnitude in pixels
    displacement = k_px2 / r  # |Δ| = k/r

    # Unit direction vectors
    ux = dx / r
    uy = dy / r

    # Source coordinates (backward mapping)
    src_x = np.clip(x - ux * displacement, 0, w - 1).astype(int)
    src_y = np.clip(y - uy * displacement, 0, h - 1).astype(int)

    lensed = img[src_y, src_x].copy()

    # Central occluder (a visual "lens core")
    mask = r < float(cfg.bh_radius_px)
    lensed[mask] = 0.0

    return lensed


def sanity_check(k_px2: float, cfg: LensConfig) -> None:
    """
    Small internal check: report characteristic scales and shifts.

    For a point-mass thin lens (baseline GR), the mapping behaves like:
        |Δθ| ≈ θ_E^2 / |θ|

    In this pixelized toy renderer we use:
        |Δpx| ≈ k_px2 / r_px
    where k_px2 ≈ (θ_E in pixels)^2.
    """
    arcsec_per_px = (cfg.fov_deg * 3600.0) / float(cfg.img_size)
    theta_E_px = math.sqrt(max(k_px2, 0.0))
    theta_E_arcsec = theta_E_px * arcsec_per_px

    print(f"deflection strength k: {k_px2:.6e} px^2  (|Δ| ≈ k/r)")
    print(f"pixel scale: {arcsec_per_px:.6e} arcsec/px  (FOV={cfg.fov_deg} deg, N={cfg.img_size}px)")
    print(f"Einstein scale (approx): θ_E ≈ {theta_E_px:.6e} px  ≈ {theta_E_arcsec:.6e} arcsec")

    if theta_E_px < 1e-3:
        print("WARNING: θ_E << 1 px → lensing is visually negligible at this FOV/pixel scale.")

    for r in (50, 100, 200):
        shift_px = k_px2 / r
        shift_arcsec = shift_px * arcsec_per_px
        print(f"  expected |Δ| at r={r:>3d}px: {shift_px:.3e} px  ({shift_arcsec:.3e} arcsec)")



def main() -> int:
    parser = argparse.ArgumentParser(description="EDC/GR lensing demonstration with strict epistemic labelling.")
    parser.add_argument("--mode", choices=["demo", "physical"], default="demo", help="demo=illustrative, physical=GR thin-lens mapping.")
    parser.add_argument("--strength", type=float, default=80.0, help="DEMO mode strength (dimensionless; k = strength^2).")
    parser.add_argument("--mass", type=float, default=1.98847e30, help="PHYSICAL mode: lens mass in kg (default ~Sun).")
    parser.add_argument("--Dl", type=float, default=1.0, help="PHYSICAL mode: D_l in arbitrary units; use --units to set scale.")
    parser.add_argument("--Ds", type=float, default=2.0, help="PHYSICAL mode: D_s in arbitrary units; must be > D_l.")
    parser.add_argument("--units", choices=["m", "pc", "kpc", "Mpc"], default="Mpc", help="Units for D_l and D_s in PHYSICAL mode.")
    parser.add_argument("--fov", type=float, default=2.0, help="PHYSICAL mode: horizontal field of view in degrees.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for star field.")
    parser.add_argument("--out", type=str, default="artifacts/edc_lensing_output.png", help="Output PNG path.")
    parser.add_argument("--no-show", action="store_true", help="Do not open an interactive window.")
    args = parser.parse_args()

    cfg = LensConfig(seed=args.seed)

    # Build background
    img = make_background(cfg)

    # Choose k and status line
    if args.mode == "demo":
        k, status_line = compute_strength_demo(args.strength)
    else:
        # Convert units to meters
        unit_scale = {
            "m": 1.0,
            "pc": 3.085677581e16,
            "kpc": 3.085677581e19,
            "Mpc": 3.085677581e22,
        }[args.units]
        d_l = float(args.Dl) * unit_scale
        d_s = float(args.Ds) * unit_scale
        k, status_line = compute_strength_physical(args.mass, d_l, d_s, args.fov, cfg.width)

    print("====================================================")
    print("EDC LENSING — STRICT VISUALIZATION")
    print("====================================================")
    print(status_line)
    print(f"image size: {cfg.width}×{cfg.height} px, seed={cfg.seed}, stars={cfg.n_stars}")
    print(f"deflection strength k: {k:.6g} px^2  (|Δ| = k/r)")
    sanity_check(k, cfg)

    # Lens
    lensed = apply_lens(img, k, cfg)

    # Save
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    plt.figure(figsize=(8, 8))
    plt.imshow(lensed)
    plt.axis("off")
    plt.title("Lensing demo (strict epistemic labels)", fontsize=14)
    plt.savefig(args.out, bbox_inches="tight", pad_inches=0)
    print(f"saved: {args.out}")

    if not args.no_show:
        plt.show()
    else:
        plt.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
