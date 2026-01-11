#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EDC Mercury Precession — Bridge Validation (v17.49 baseline)

Epistemic status:
- BASELINE: Newtonian limit + Schwarzschild 1PN correction term (benchmark orbit equation).
- IDENTIFIED: Interpretation via plenum "river" bridge (Painlevé–Gullstrand ↔ Schwarzschild mapping).
- DERIVED (numerical): anomalous perihelion advance computed via difference-of-runs (Bridge − Newton).

NOT YET:
- A fully native EDC prediction where the river profile v(r) is derived from 5D membrane dynamics
  without importing the Newtonian weak-field baseline.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# Constants + Mercury parameters (SI)
# ---------------------------------------------------------------------------
G = 6.67430e-11
c = 299_792_458.0
M_sun = 1.98847e30

a = 5.7909227e10     # m
e = 0.205630         # -
T_days = 87.9691     # days

@dataclass(frozen=True)
class RunResult:
    mode: str
    dphi: float
    n_orbits: int
    perihelion_angles: List[float]
    avg_dphi_per_orbit: float
    advance_per_orbit_rad: float
    advance_arcsec_per_century: float

def orbit_rhs(u: float, L: float, mode: str) -> float:
    """
    u'' + u = f(u)
    Newton: f(u) = GM/L^2
    Bridge (Schwarzschild 1PN): f(u) = GM/L^2 + 3GM/c^2 * u^2
    """
    base = G * M_sun / (L * L)
    if mode == "newton":
        return base
    if mode == "bridge":
        return base + 3.0 * G * M_sun * u * u / (c * c)
    raise ValueError(f"Unknown mode: {mode}")

def integrate_orbit(dphi: float, n_orbits: int, mode: str) -> Tuple[np.ndarray, np.ndarray]:
    # Newtonian baseline angular momentum (good enough for 1PN delta)
    L = math.sqrt(G * M_sun * a * (1.0 - e * e))

    r_peri = a * (1.0 - e)
    u0 = 1.0 / r_peri

    u_prev = u0
    u_curr = u0

    steps_per_orbit = max(1, int((2.0 * math.pi) / dphi))
    N = steps_per_orbit * n_orbits

    phis = np.linspace(0.0, N * dphi, N + 1, dtype=float)
    us = np.empty(N + 1, dtype=float)
    us[0] = u0

    for i in range(1, N + 1):
        u_dd = orbit_rhs(u_curr, L, mode) - u_curr
        u_next = 2.0 * u_curr - u_prev + (dphi * dphi) * u_dd
        u_prev, u_curr = u_curr, u_next
        us[i] = u_curr

    return phis, us

def detect_perihelia(phis: np.ndarray, us: np.ndarray, discard_fraction: float = 0.5) -> List[float]:
    start = int(len(us) * discard_fraction)
    angles: List[float] = []

    for i in range(start + 1, len(us) - 1):
        if us[i] > us[i - 1] and us[i] > us[i + 1]:
            # Quadratic interpolation peak (x in {-1,0,1})
            y1, y2, y3 = float(us[i - 1]), float(us[i]), float(us[i + 1])
            denom = (y1 - 2.0 * y2 + y3)
            if abs(denom) < 1e-30:
                x_peak = 0.0
            else:
                x_peak = 0.5 * (y1 - y3) / denom
                x_peak = max(-1.0, min(1.0, x_peak))

            phi_peak = float(phis[i]) + x_peak * (float(phis[i + 1]) - float(phis[i]))
            angles.append(phi_peak)

    return angles

def summarize_run(mode: str, dphi: float, n_orbits: int) -> RunResult:
    phis, us = integrate_orbit(dphi, n_orbits, mode)
    peri = detect_perihelia(phis, us)

    if len(peri) < 4:
        raise RuntimeError(f"Not enough perihelia detected ({len(peri)}). Increase n_orbits or reduce dphi.")

    deltas = [peri[i + 1] - peri[i] for i in range(len(peri) - 1)]
    avg = float(sum(deltas) / len(deltas))

    advance = avg - 2.0 * math.pi  # rad/orbit
    arcsec_per_orbit = advance * (180.0 / math.pi) * 3600.0
    orbits_per_century = (365.25 * 100.0) / T_days
    arcsec_per_century = arcsec_per_orbit * orbits_per_century

    return RunResult(mode, dphi, n_orbits, peri, avg, advance, arcsec_per_century)

def print_result(rr: RunResult) -> None:
    print(f"[MODE: {rr.mode.upper()}] dphi={rr.dphi:g} rad, n_orbits={rr.n_orbits}")
    print(f"  perihelia detected: {len(rr.perihelion_angles)}")
    print(f"  avg Δφ per orbit:  {rr.avg_dphi_per_orbit:.12f} rad")
    print(f"  advance/orbit:     {rr.advance_per_orbit_rad:.12e} rad")
    print(f"  advance:           {rr.advance_arcsec_per_century:.6f} arcsec/century")

def main() -> int:
    ap = argparse.ArgumentParser(description="Mercury perihelion precession (Newton vs Bridge) with difference-of-runs.")
    ap.add_argument("--dphi", type=float, default=1e-4, help="step in φ [rad] (default 1e-4)")
    ap.add_argument("--n-orbits", type=int, default=100, help="number of orbits (default 100)")
    ap.add_argument("--plot", action="store_true", help="generate plot")
    ap.add_argument("--out", type=str, default="", help="output PNG path (optional)")
    ap.add_argument("--no-show", action="store_true", help="do not show plot window")
    args = ap.parse_args()

    rr_newton = summarize_run("newton", args.dphi, args.n_orbits)
    rr_bridge = summarize_run("bridge", args.dphi, args.n_orbits)
    anomaly = rr_bridge.advance_arcsec_per_century - rr_newton.advance_arcsec_per_century

    print("=" * 60)
    print("MERCURY PERIHELION PRECESSION — DIFFERENCE-OF-RUNS")
    print("=" * 60)
    print_result(rr_newton)
    print_result(rr_bridge)
    print("-" * 60)
    print(f"[ANOMALY: BRIDGE − NEWTON] {anomaly:.6f} arcsec/century")
    print("=" * 60)

    if args.plot:
        try:
            import matplotlib
            if args.no_show or args.out:
                matplotlib.use("Agg", force=True)
            import matplotlib.pyplot as plt

            phN, uN = integrate_orbit(args.dphi, 2, "newton")
            phB, uB = integrate_orbit(args.dphi, 2, "bridge")

            plt.figure()
            plt.plot(phN, uN, label="Newton")
            plt.plot(phB, uB, label="Bridge (Schwarzschild 1PN)")
            plt.xlabel("φ [rad]")
            plt.ylabel("u(φ)=1/r [1/m]")
            plt.legend()
            plt.title("Mercury orbit u(φ), first 2 orbits")

            if args.out:
                plt.savefig(args.out, dpi=200, bbox_inches="tight")
                print(f"[saved] {args.out}")

            if not args.no_show and not args.out:
                plt.show()
            else:
                plt.close()

        except ImportError:
            print("Plot requested but matplotlib not installed. pip install matplotlib")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
