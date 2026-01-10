"""edc_double_slit.py

EDC Double Slit (Pilot-Wave Intuition Demo)

Epistemic status: DEMONSTRATION / PROPOSED visualization.
This script is a classical-wave interference simulation used to build intuition for the
EDC "plenum pilot-wave" narrative. It is not a quantum-mechanical prediction and is not
calibrated to SI units by default (dimensionless grid units are used).

The detector sampling uses the (time-averaged) wave intensity as a probability distribution
to generate an accumulation pattern.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ----------------------------
# Model (dimensionless units)
# ----------------------------
RESOLUTION = 200  # grid points per axis
X_MIN, X_MAX = -15.0, 15.0
Y_MIN, Y_MAX = 0.0, 30.0

WAVELENGTH = 1.5        # grid units
SLIT_SEPARATION = 6.0   # grid units (center-to-center)
EPS = 1e-6              # avoids singular amplitude at r=0

# Reproducibility: set to an integer for deterministic sampling; keep None for stochastic runs.
RNG_SEED: int | None = None


def interference_intensity_2d(x: np.ndarray, y: np.ndarray, k: float, slit_sep: float, eps: float = EPS) -> np.ndarray:
    """Time-averaged interference intensity for two coherent point sources in 2D.

    Amplitude model: A(r) ~ 1/sqrt(r) (2D cylindrical spreading). The time-averaged intensity is:
        I = a1^2 + a2^2 + 2 a1 a2 cos(Δφ),  with Δφ = k (r1 - r2)

    Parameters are dimensionless unless you explicitly map grid units to SI units.
    """
    r1 = np.sqrt((x - slit_sep / 2.0) ** 2 + y ** 2)
    r2 = np.sqrt((x + slit_sep / 2.0) ** 2 + y ** 2)

    a1 = 1.0 / np.sqrt(r1 + eps)
    a2 = 1.0 / np.sqrt(r2 + eps)

    phase_diff = k * (r1 - r2)
    intensity = a1**2 + a2**2 + 2.0 * a1 * a2 * np.cos(phase_diff)
    return intensity


def _safe_normalize(p: np.ndarray) -> np.ndarray:
    total = float(np.sum(p))
    if not np.isfinite(total) or total <= 0.0:
        return np.ones_like(p) / p.size
    return p / total


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)

    k = 2.0 * np.pi / WAVELENGTH

    x = np.linspace(X_MIN, X_MAX, RESOLUTION)
    y = np.linspace(Y_MIN, Y_MAX, RESOLUTION)
    X, Y = np.meshgrid(x, y)

    print("Computing plenum interference field (double slit)...")
    intensity_field = interference_intensity_2d(X, Y, k, SLIT_SEPARATION)

    detector_prob = _safe_normalize(intensity_field[-1, :])

    # ----------------------------
    # Visualization
    # ----------------------------
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(10, 8))

    # Top: wave / intensity field ("plenum")
    ax_wave = fig.add_axes([0.1, 0.34, 0.8, 0.58])  # [left, bottom, width, height]
    ax_wave.set_title("EDC Pilot Wave Dynamics (Double Slit)", color="white", fontsize=14)
    ax_wave.set_ylabel("Distance from slits", color="white")
    ax_wave.axis("off")

    im = ax_wave.imshow(
        intensity_field,
        extent=[X_MIN, X_MAX, Y_MIN, Y_MAX],
        origin="lower",
        cmap="ocean",
        aspect="auto",
        vmin=0.0,
        vmax=np.percentile(intensity_field, 95),
    )

    # Slit wall at y=0 (purely illustrative)
    wall_y = 0.0
    ax_wave.plot([X_MIN, -SLIT_SEPARATION / 2.0 - 0.5], [wall_y, wall_y], color="gray", linewidth=5)
    ax_wave.plot(
        [-SLIT_SEPARATION / 2.0 + 0.5, SLIT_SEPARATION / 2.0 - 0.5],
        [wall_y, wall_y],
        color="gray",
        linewidth=5,
    )
    ax_wave.plot([SLIT_SEPARATION / 2.0 + 0.5, X_MAX], [wall_y, wall_y], color="gray", linewidth=5)
    ax_wave.text(0.5, 0.03, "Slits (Flux Entry)", transform=ax_wave.transAxes, color="white", ha="center", va="bottom", fontsize=10)

    # Bottom: detector histogram
    ax_det = fig.add_axes([0.1, 0.06, 0.8, 0.20])
    ax_det.set_xlabel("Detector screen position", color="white", labelpad=6)
    ax_det.set_yticks([])
    ax_det.set_xlim(X_MIN, X_MAX)
    ax_det.set_title("Particle Accumulation (Detector Screen)", color="cyan", fontsize=10, pad=10)

    particles_x: list[float] = []
    hist_bins = np.linspace(X_MIN, X_MAX, 100)
    bin_width = float(hist_bins[1] - hist_bins[0])
    counts, _ = np.histogram([], bins=hist_bins)
    bars = ax_det.bar(hist_bins[:-1], counts, width=bin_width, color="cyan", alpha=0.7)

    info_text = ax_wave.text(0.02, 0.95, "", transform=ax_wave.transAxes, color="white", fontsize=9)

    def update(_frame: int):
        impact_x = float(rng.choice(x, p=detector_prob))
        particles_x.append(impact_x)

        counts, _ = np.histogram(particles_x, bins=hist_bins)
        for bar, height in zip(bars, counts):
            bar.set_height(int(height))

        ymax = int(np.max(counts)) if len(particles_x) > 0 else 1
        ax_det.set_ylim(0, max(ymax + 1, 1))

        info_text.set_text(
            f"Particles Detected: {len(particles_x)}\n"
            "Interpretation: Wave guides flux (demo)"
        )
        return bars

    print("Starting simulation... watch the accumulation build up.")
    ani = FuncAnimation(fig, update, frames=200, interval=20, blit=False)
    plt.show()


if __name__ == "__main__":
    main()
