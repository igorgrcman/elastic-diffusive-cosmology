"""EDC lensing visualization (strict epistemic labels).

This script produces a simple gravitational lensing visualization.

Modes
-----
- demo: purely illustrative deformation using a dimensionless strength parameter.
- physical: baseline GR weak-field point-mass thin-lens mapping.

Epistemic rule:
- 'physical' mode uses BASELINE constants (CODATA/IAU-style values).
- Any extra 'visual_scale' applied in physical mode is explicitly labeled as illustrative.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt

# Allow running directly from the scripts directory without installing the package.
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from edc.constants.registry import get_constant
from edc.physics.lensing import (
    DistanceUnit,
    distance_to_meters,
    k_px2_from_physical,
    pixel_scale_arcsec,
)


@dataclass(frozen=True)
class LensingConfig:
    width: int = 800
    height: int = 800
    seed: int = 42
    stars: int = 50
    fov_deg: float = 2.0


def _rand_stars(cfg: LensingConfig) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(cfg.seed)
    xs = rng.uniform(0, cfg.width, size=cfg.stars)
    ys = rng.uniform(0, cfg.height, size=cfg.stars)
    return xs, ys


def _apply_point_lens_shift(
    x: np.ndarray,
    y: np.ndarray,
    *,
    cx: float,
    cy: float,
    k_px2: float,
    min_r_px: float = 6.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Apply the point-lens pixel shift model: |Δ| = k/r.

    Vector form: Δ⃗ = k * r⃗ / r^2.
    """
    dx = x - cx
    dy = y - cy
    r2 = dx * dx + dy * dy
    r2 = np.maximum(r2, float(min_r_px) ** 2)
    x2 = x + k_px2 * dx / r2
    y2 = y + k_px2 * dy / r2
    return x2, y2


def _draw_deformed_grid(ax: plt.Axes, cfg: LensingConfig, *, k_px2: float) -> None:
    cx, cy = cfg.width / 2.0, cfg.height / 2.0
    grid_step = 25

    xs = np.arange(0, cfg.width + 1, grid_step)
    ys = np.arange(0, cfg.height + 1, grid_step)

    # Vertical lines
    for x0 in xs:
        x = np.full_like(ys, fill_value=float(x0), dtype=float)
        y = ys.astype(float)
        x2, y2 = _apply_point_lens_shift(x, y, cx=cx, cy=cy, k_px2=k_px2)
        ax.plot(x2, y2, linewidth=0.6)

    # Horizontal lines
    for y0 in ys:
        x = xs.astype(float)
        y = np.full_like(xs, fill_value=float(y0), dtype=float)
        x2, y2 = _apply_point_lens_shift(x, y, cx=cx, cy=cy, k_px2=k_px2)
        ax.plot(x2, y2, linewidth=0.6)


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="EDC lensing demo (strict epistemic labels)")

    p.add_argument("--mode", choices=["demo", "physical"], default="demo")

    # Common rendering options
    p.add_argument("--width", type=int, default=800)
    p.add_argument("--height", type=int, default=800)
    p.add_argument("--stars", type=int, default=50)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--fov", type=float, default=2.0, help="Field of view (degrees) across the image width")
    p.add_argument("--out", type=str, default="artifacts/edc_lensing_output.png")

    # Demo mode
    p.add_argument("--strength", type=float, default=60.0, help="Demo strength (dimensionless) - only used in demo mode")

    # Physical mode
    p.add_argument("--mass", type=float, default=None, help="Lens mass in kg (physical mode)")
    p.add_argument("--mass_solar", type=float, default=None, help="Lens mass in solar masses (physical mode)")
    p.add_argument("--Dl", type=float, default=1.0, help="Observer->lens distance")
    p.add_argument("--Ds", type=float, default=2.0, help="Observer->source distance")
    p.add_argument("--units", type=str, default="Mpc", help="Distance units: m, km, AU, pc, kpc, Mpc, Gpc")

    # Strictness/visibility knobs
    p.add_argument(
        "--visual_scale",
        type=float,
        default=1.0,
        help="Multiply pixel shifts for visibility. If not 1, output is explicitly labeled as illustrative scaling.",
    )

    return p.parse_args()


def main() -> int:
    args = _parse_args()

    cfg = LensingConfig(
        width=args.width,
        height=args.height,
        stars=args.stars,
        seed=args.seed,
        fov_deg=args.fov,
    )

    # Baseline constants (allowed injection)
    G = get_constant("G", allow={"BASELINE"}).value
    c = get_constant("c", allow={"BASELINE"}).value
    M_sun = get_constant("M_sun", allow={"BASELINE"}).value

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.mode == "demo":
        status = "ILLUSTRATIVE"
        k_px2 = float(args.strength) ** 2
        k_label = f"k={k_px2:.3g} px^2 (demo strength={args.strength})"
    else:
        status = "BASELINE"
        units: DistanceUnit = args.units  # type: ignore[assignment]
        Dl_m = distance_to_meters(float(args.Dl), units)
        Ds_m = distance_to_meters(float(args.Ds), units)

        if args.mass_solar is not None:
            M = float(args.mass_solar) * M_sun
        elif args.mass is not None:
            M = float(args.mass)
        else:
            M = M_sun

        k_px2 = k_px2_from_physical(M, Dl_m, Ds_m, fov_deg=cfg.fov_deg, width_px=cfg.width, G=G, c=c)
        k_label = f"k={k_px2:.3g} px^2 (thin-lens point-mass, GR weak-field)"

        # If physical is too small to see, the user can optionally scale the displacement.
        if float(args.visual_scale) != 1.0:
            status = "BASELINE + ILLUSTRATIVE (display scaling)"
            k_px2 = k_px2 * float(args.visual_scale)

    # Generate stars and apply mapping
    xs, ys = _rand_stars(cfg)
    cx, cy = cfg.width / 2.0, cfg.height / 2.0
    xs2, ys2 = _apply_point_lens_shift(xs, ys, cx=cx, cy=cy, k_px2=k_px2)

    # Plot
    fig = plt.figure(figsize=(6.5, 6.8), dpi=160)
    fig.patch.set_facecolor("black")
    ax = fig.add_subplot(111)
    ax.set_facecolor("black")

    _draw_deformed_grid(ax, cfg, k_px2=k_px2)
    ax.scatter(xs2, ys2, s=12, color="white")

    ax.set_xlim(0, cfg.width)
    ax.set_ylim(cfg.height, 0)
    ax.set_aspect("equal")
    ax.axis("off")

    # A small central mask for aesthetics
    ax.add_artist(plt.Circle((cx, cy), radius=10, color="black"))

    # Text overlays
    px_scale = pixel_scale_arcsec(cfg.fov_deg, cfg.width)
    title = "Lensing demo (strict epistemic labels)"
    ax.set_title(title, color="white", pad=8)

    ax.text(
        0.02,
        0.96,
        f"[STATUS: {status}]\nFOV={cfg.fov_deg}°  scale={px_scale:.3g} arcsec/px\n{k_label}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        color="white",
    )

    if args.mode == "physical":
        ax.text(
            0.02,
            0.08,
            "Tip: Solar-mass lenses at Mpc distances produce micro-arcsecond deflections.\n"
            "Try a galaxy lens (mass_solar ~ 1e11–1e12) or use --visual_scale for visibility.",
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=7,
            color="white",
            alpha=0.8,
        )

    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)

    # Console summary
    print("====================================================")
    print("EDC LENSING — STRICT VISUALIZATION")
    print("====================================================")
    print(f"[STATUS: {status}]")
    print(f"image size: {cfg.width}×{cfg.height} px, seed={cfg.seed}, stars={cfg.stars}")
    print(f"pixel scale: {px_scale:.6g} arcsec/px")
    print(f"{k_label}")
    print(f"saved: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
