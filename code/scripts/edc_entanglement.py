"""EDC Entanglement Visualization (Conceptual Demo)

Epistemic status: DEMONSTRATION (not derived; not a physical simulator)

This animation is an intuition aid. It visualizes two particles separating on a
3D "membrane" while remaining connected by a hypothetical higher-dimensional
bulk curve.

Important notes:
- Distances and time are in arbitrary units.
- "Surface" and "bulk" transfer speeds are dimensionless visualization parameters.
- No claim is made about faster-than-light signalling or physical mechanism here.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def generate_bulk_connection(p1: tuple[float, float], p2: tuple[float, float], depth: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return a 3D arc connecting two 2D points via a negative-z bulk curve.

    The arc is purely illustrative: a semicircle dipping into z < 0.
    """
    t = np.linspace(0.0, np.pi, 80)

    center_x = (p1[0] + p2[0]) / 2.0
    radius = abs(p2[0] - p1[0]) / 2.0

    x = center_x + radius * np.cos(t)      # from p2 to p1
    y = np.zeros_like(x)                   # keep y=0 for clarity
    z = -abs(depth) * np.sin(t)            # dip into the bulk (z < 0)

    return x, y, z


def main() -> None:
    # --- Visualization parameters (dimensionless) ---
    separation_start = 1.0
    separation_max = 4.0
    separation_step = 0.05

    event_frame = 80
    surface_speed = 0.02   # progress per frame (0..1)
    bulk_speed = 0.10      # progress per frame (0..1)

    plt.style.use("dark_background")
    fig = plt.figure(figsize=(14, 6))

    # LEFT: 2D "membrane" view
    ax2d = fig.add_subplot(1, 2, 1)
    ax2d.set_title("MEMBRANE VIEW (3D Projection)\n'Apparent Nonlocal Correlation'", color="cyan")
    ax2d.set_xlim(-6, 6)
    ax2d.set_ylim(-3, 3)
    ax2d.set_aspect("equal")
    ax2d.axis("off")

    # Light grid to emphasize flatness
    for i in range(-6, 7):
        ax2d.axvline(i, color="gray", alpha=0.2, lw=0.5)
        ax2d.axhline(i / 2, color="gray", alpha=0.2, lw=0.5)

    # RIGHT: 3D "bulk" geometry view
    ax3d = fig.add_subplot(1, 2, 2, projection="3d")
    ax3d.set_title("EDC BULK VIEW (Illustrative)\n'Connected via Bulk Shortcut'", color="magenta")
    ax3d.set_xlim(-6, 6)
    ax3d.set_ylim(-3, 3)
    ax3d.set_zlim(-5, 1)
    ax3d.axis("off")
    ax3d.view_init(elev=20, azim=-90)  # look "under the table"

    # Objects: particles in 2D
    particle_a_2d, = ax2d.plot([], [], "o", color="cyan", markersize=12)
    particle_b_2d, = ax2d.plot([], [], "o", color="cyan", markersize=12)
    surface_signal, = ax2d.plot([], [], ".", color="red", markersize=8)

    # Objects: particles and bulk connection in 3D
    particle_a_3d, = ax3d.plot([], [], [], "o", color="cyan", markersize=12)
    particle_b_3d, = ax3d.plot([], [], [], "o", color="cyan", markersize=12)
    bulk_line, = ax3d.plot([], [], [], "-", color="magenta", alpha=0.6, lw=2)
    bulk_signal, = ax3d.plot([], [], [], "*", color="yellow", markersize=15)

    # Membrane plane in 3D view
    xx, yy = np.meshgrid(np.linspace(-6, 6, 10), np.linspace(-3, 3, 5))
    ax3d.plot_surface(xx, yy, np.zeros_like(xx), color="blue", alpha=0.1)

    # Text overlays (2D panel)
    dist_text = ax2d.text(0, -2, "", color="white", ha="center")
    status_text = ax2d.text(0, 2, "", color="yellow", ha="center", fontsize=12)

    state = {
        "separation": separation_start,
        "triggered": False,
    }

    def update(frame: int):
        # Phase 1: separate particles
        if state["separation"] < separation_max:
            state["separation"] += separation_step
            status_text.set_text("System state: separating particles…")
        elif not state["triggered"]:
            state["triggered"] = True
            status_text.set_text("Event at A: measurement/setting changed (demo)")

        sep = float(state["separation"])
        x_a, x_b = -sep, sep

        # Update 2D particles
        particle_a_2d.set_data([x_a], [0.0])
        particle_b_2d.set_data([x_b], [0.0])

        # Update 3D particles
        particle_a_3d.set_data([x_a], [0.0])
        particle_a_3d.set_3d_properties([0.0])
        particle_b_3d.set_data([x_b], [0.0])
        particle_b_3d.set_3d_properties([0.0])

        # Bulk connection geometry
        bx, by, bz = generate_bulk_connection((x_a, 0.0), (x_b, 0.0), depth=sep * 0.8)
        bulk_line.set_data(bx, by)
        bulk_line.set_3d_properties(bz)

        # Phase 2: show "surface" vs "bulk" transfer (conceptual)
        if state["triggered"]:
            # Surface progress
            surf_progress = np.clip((frame - event_frame) * surface_speed, 0.0, 1.0)
            if 0.0 < surf_progress < 1.0:
                sig_x = x_a + (x_b - x_a) * surf_progress
                surface_signal.set_data([sig_x], [0.0])
                dist_text.set_text(f"Surface transfer: {int(surf_progress * 100)}% (demo)")
            elif surf_progress >= 1.0:
                dist_text.set_text("Surface transfer: arrived (demo)")

            # Bulk progress
            bulk_progress = np.clip((frame - event_frame) * bulk_speed, 0.0, 1.0)
            if 0.0 < bulk_progress < 1.0:
                idx = int(bulk_progress * (len(bx) - 1))
                bulk_signal.set_data([bx[idx]], [by[idx]])
                bulk_signal.set_3d_properties([bz[idx]])
                status_text.set_text("Bulk shortcut transfer: in progress (demo)")
            elif bulk_progress >= 1.0:
                bulk_signal.set_data([x_b], [0.0])
                bulk_signal.set_3d_properties([0.0])
                status_text.set_text("Correlation shown via bulk shortcut (demo)")

        return (
            particle_a_2d,
            particle_b_2d,
            surface_signal,
            particle_a_3d,
            particle_b_3d,
            bulk_line,
            bulk_signal,
            dist_text,
            status_text,
        )

    FuncAnimation(fig, update, frames=200, interval=30, blit=False)
    print("Showing EDC entanglement visualization (conceptual demo)…")
    plt.show()


if __name__ == "__main__":
    main()
