"""edc_double_slit2.py

EDC Double Slit (Pilot-Wave Intuition Demo, variant 2)

Epistemic status: DEMONSTRATION / PROPOSED visualization.
This script shows:
  (1) a static pilot-wave field (visual) and
  (2) a particle-accumulation histogram (sampling) driven by the wave intensity.

Notes:
- The wave field is shown as an instantaneous phase snapshot (sin(k r)).
- The sampling distribution uses the time-averaged intensity:
    I = a1^2 + a2^2 + 2 a1 a2 cos(Δφ)
  which is the standard result for two coherent sources.

All parameters are in dimensionless grid units unless you explicitly calibrate them.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ----------------------------
# Simulation parameters (dimensionless)
# ----------------------------
WIDTH = 30.0
HEIGHT = 20.0
RESOLUTION = 150

WAVELENGTH = 1.2
K = 2.0 * np.pi / WAVELENGTH
SLIT_DIST = 4.0
EPS = 1e-6

RNG_SEED: int | None = None


def calculate_wave_and_intensity(x: np.ndarray, y: np.ndarray, k: float, slit_dist: float) -> tuple[np.ndarray, np.ndarray]:
    """Return (wave_snapshot, time_averaged_intensity) for two coherent sources."""
    r1 = np.sqrt((x - slit_dist / 2.0) ** 2 + y ** 2)
    r2 = np.sqrt((x + slit_dist / 2.0) ** 2 + y ** 2)

    a1 = 1.0 / np.sqrt(r1 + EPS)
    a2 = 1.0 / np.sqrt(r2 + EPS)

    # Visual: instantaneous phase snapshot
    wave = a1 * np.sin(k * r1) + a2 * np.sin(k * r2)

    # Sampling: time-averaged intensity (coherent superposition)
    phase_diff = k * (r1 - r2)
    intensity = a1**2 + a2**2 + 2.0 * a1 * a2 * np.cos(phase_diff)
    return wave, intensity


def _safe_normalize(p: np.ndarray) -> np.ndarray:
    total = float(np.sum(p))
    if not np.isfinite(total) or total <= 0.0:
        return np.ones_like(p) / p.size
    return p / total


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)

    x = np.linspace(-WIDTH / 2.0, WIDTH / 2.0, RESOLUTION)
    y = np.linspace(0.0, HEIGHT, RESOLUTION)
    X, Y = np.meshgrid(x, y)

    print("Computing plenum field (double slit)...")
    wave_field, intensity_field = calculate_wave_and_intensity(X, Y, K, SLIT_DIST)

    detector_prob = _safe_normalize(intensity_field[-1, :])

    # ----------------------------
    # Visualization
    # ----------------------------
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(10, 9))

    ax_wave = fig.add_axes([0.1, 0.4, 0.8, 0.55])
    ax_wave.set_title("EDC Pilot Wave Dynamics (Double Slit)", color="white", fontsize=16)
    ax_wave.axis("off")

    im = ax_wave.imshow(
        wave_field,
        extent=[-WIDTH / 2.0, WIDTH / 2.0, 0.0, HEIGHT],
        origin="lower",
        cmap="ocean",
        aspect="auto",
        vmin=-np.percentile(np.abs(wave_field), 95),
        vmax=np.percentile(np.abs(wave_field), 95),
    )

    # Slit wall at y=0
    ax_wave.plot([-WIDTH / 2.0, -SLIT_DIST / 2.0 - 0.5], [0, 0], color="gray", linewidth=6)
    ax_wave.plot([-SLIT_DIST / 2.0 + 0.5, SLIT_DIST / 2.0 - 0.5], [0, 0], color="gray", linewidth=6)
    ax_wave.plot([SLIT_DIST / 2.0 + 0.5, WIDTH / 2.0], [0, 0], color="gray", linewidth=6)
    ax_wave.text(0, -1.5, "Slits (Flux Entry)", color="cyan", ha="center")

    ax_det = fig.add_axes([0.1, 0.05, 0.8, 0.25])
    ax_det.set_title("Particle Accumulation (Detector Screen)", color="cyan", fontsize=12)
    ax_det.set_xlim(-WIDTH / 2.0, WIDTH / 2.0)
    ax_det.set_yticks([])
    ax_det.spines["top"].set_visible(False)
    ax_det.spines["right"].set_visible(False)
    ax_det.spines["left"].set_visible(False)

    particles_x: list[float] = []
    bins = np.linspace(-WIDTH / 2.0, WIDTH / 2.0, 80)
    bars = ax_det.bar(bins[:-1], np.zeros(len(bins) - 1), width=np.diff(bins), color="cyan", edgecolor="black", alpha=0.8)

    info_text = ax_wave.text(0.02, 0.95, "", transform=ax_wave.transAxes, color="white", fontsize=10)

    def update(_frame: int):
        # Spawn a small batch per frame for faster convergence.
        new_particles = rng.choice(x, size=5, p=detector_prob)
        particles_x.extend([float(v) for v in new_particles])

        counts, _ = np.histogram(particles_x, bins=bins)
        max_count = int(np.max(counts)) if len(particles_x) > 0 else 1
        for bar, count in zip(bars, counts):
            bar.set_height(int(count))

        ax_det.set_ylim(0, max_count * 1.1 if max_count > 0 else 1)
        info_text.set_text(
            f"Particles Detected: {len(particles_x)}\n"
            "Interpretation: Wave guides flux (demo)"
        )
        return bars

    print("Starting simulation... particles will form interference fringes.")
    ani = FuncAnimation(fig, update, frames=300, interval=20, blit=False)
    plt.show()


if __name__ == "__main__":
    main()
