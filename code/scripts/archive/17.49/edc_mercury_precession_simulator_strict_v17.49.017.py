
"""edc_mercury_precession_simulator.py — STRICT (v17.49.017)

Mercury perihelion precession — numerical extraction with drift-cancelled anomaly.

Why v17.49.016 showed ~1600 arcsec/century:
  - The perihelion angle is estimated from a discrete φ-grid.
  - Even in Newtonian gravity the "next perihelion" will not land exactly at 2π on a coarse grid,
    producing a large *numerical drift* (~few arcsec per orbit) that inflates the per-century number.

The physically meaningful quantity is the *anomalous precession* (relativistic minus Newtonian),
which cancels the integration/detection drift to first order.

Epistemic status (strict):
  - IDENTIFIED: River-flow profile v(r)^2 = 2GM/r (bridge mapping).
  - BASELINE: Weak-field Schwarzschild-equivalent orbit equation:
        u'' + u = mu/h^2 + 3 mu u^2 / c^2
    and its Newtonian limit (without the 3 mu u^2 / c^2 term).
  - DERIVED: Numerical integration + perihelion detection + anomaly extraction (Δ = rel - newt).

Run:
  python edc_mercury_precession_simulator.py
  python edc_mercury_precession_simulator.py --step 5e-5
  python edc_mercury_precession_simulator.py --step 2e-5
  python edc_mercury_precession_simulator.py --plot

"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Tuple, Optional

import numpy as np


# -----------------------------
# Baseline parameters (inputs)
# -----------------------------
BASELINE_G = 6.67430e-11           # m^3 kg^-1 s^-2 (CODATA)
BASELINE_C = 299792458.0           # m/s (exact SI)
BASELINE_M_SUN = 1.98847e30        # kg (commonly used value)
# Mercury orbit (verification-level constants)
BASELINE_A = 5.7909227e10          # m (semi-major axis)
BASELINE_E = 0.205630              # eccentricity
BASELINE_PERIOD_DAYS = 87.9691     # days (sidereal period approx)


@dataclass(frozen=True)
class SimulationConfig:
    step_dphi: float = 5.0e-5              # rad (smaller default to reduce drift)
    phi_max_factor: float = 1.20           # integrate up to 1.2 * 2π to capture the next perihelion
    relativistic: bool = True              # include GR correction term
    plot: bool = False


def _rk4_step(u: float, up: float, dphi: float, mu: float, h2: float, c: float, relativistic: bool) -> Tuple[float, float]:
    """One RK4 step for u'' = f(u) - u.

    Orbit equation (baseline GR weak-field):
        u'' + u = mu/h^2 + 3 mu u^2 / c^2     (relativistic)
        u'' + u = mu/h^2                      (Newtonian)

    where:
        u = 1/r,  mu = GM,  h = specific angular momentum.
    """

    def acc(u_val: float) -> float:
        rhs = mu / h2
        if relativistic:
            rhs += 3.0 * mu * (u_val ** 2) / (c ** 2)
        return rhs - u_val

    k1_u = up
    k1_up = acc(u)

    k2_u = up + 0.5 * dphi * k1_up
    k2_up = acc(u + 0.5 * dphi * k1_u)

    k3_u = up + 0.5 * dphi * k2_up
    k3_up = acc(u + 0.5 * dphi * k2_u)

    k4_u = up + dphi * k3_up
    k4_up = acc(u + dphi * k3_u)

    u_next = u + (dphi / 6.0) * (k1_u + 2.0 * k2_u + 2.0 * k3_u + k4_u)
    up_next = up + (dphi / 6.0) * (k1_up + 2.0 * k2_up + 2.0 * k3_up + k4_up)

    return u_next, up_next


def _detect_second_perihelion(phi: np.ndarray, up: np.ndarray) -> Optional[float]:
    """Detect the next perihelion angle after φ=0 using u'(φ) sign changes.

    Perihelion: u'(φ)=0 and sign changes from + to - (maximum u).
    Starting at perihelion: u'(0)=0.
    We look for: aphelion (- -> +), then perihelion (+ -> -).

    Returns:
        φ_peri2 in radians, or None if not found.
    """
    n = len(phi)
    if n < 20:
        return None

    found_aphelion = False

    for i in range(3, n - 2):
        s_prev = np.sign(up[i - 1])
        s_curr = np.sign(up[i])

        if s_prev == 0:
            s_prev = np.sign(up[i - 2])
        if s_curr == 0:
            s_curr = np.sign(up[i + 1])

        if not found_aphelion:
            if s_prev < 0 and s_curr > 0:
                found_aphelion = True
            continue

        if s_prev > 0 and s_curr < 0:
            # Linear interpolation for u'=0
            phi0, phi1 = phi[i - 1], phi[i]
            up0, up1 = up[i - 1], up[i]
            if up1 == up0:
                return float(phi0)
            frac = -up0 / (up1 - up0)
            return float(phi0 + frac * (phi1 - phi0))

    return None


def simulate_once(cfg: SimulationConfig) -> Tuple[float, float, float]:
    """Return (advance_per_orbit_rad, arcsec_per_century_raw, phi_peri2)."""
    G = BASELINE_G
    c = BASELINE_C
    M = BASELINE_M_SUN

    a = BASELINE_A
    e = BASELINE_E

    mu = G * M
    p = a * (1.0 - e ** 2)     # semi-latus rectum
    h2 = mu * p                # Newtonian specific angular momentum squared

    # Start at perihelion
    r_p = a * (1.0 - e)
    u0 = 1.0 / r_p
    up0 = 0.0

    phi_max = cfg.phi_max_factor * (2.0 * math.pi)
    n_steps = int(phi_max / cfg.step_dphi) + 1

    phi = np.linspace(0.0, phi_max, n_steps, dtype=float)
    u = np.empty_like(phi)
    up = np.empty_like(phi)

    u[0] = u0
    up[0] = up0

    for i in range(1, n_steps):
        u[i], up[i] = _rk4_step(u[i - 1], up[i - 1], cfg.step_dphi, mu, h2, c, cfg.relativistic)

    phi_peri2 = _detect_second_perihelion(phi, up)
    if phi_peri2 is None:
        raise RuntimeError("Failed to detect the next perihelion. Try smaller --step or larger --phi-max-factor.")

    advance = phi_peri2 - 2.0 * math.pi

    # Orbits per century
    orbits_per_century = (100.0 * 365.25) / BASELINE_PERIOD_DAYS
    arcsec_per_century = advance * (180.0 / math.pi) * 3600.0 * orbits_per_century

    return float(advance), float(arcsec_per_century), float(phi_peri2)


def gr_closed_form_arcsec_per_century() -> float:
    """Baseline GR closed-form anomaly (weak-field): Δφ = 6πGM/(a(1-e^2)c^2) per orbit."""
    G = BASELINE_G
    c = BASELINE_C
    M = BASELINE_M_SUN
    a = BASELINE_A
    e = BASELINE_E
    mu = G * M

    advance_per_orbit = 6.0 * math.pi * mu / (a * (1.0 - e ** 2) * c ** 2)

    orbits_per_century = (100.0 * 365.25) / BASELINE_PERIOD_DAYS
    arcsec_per_century = advance_per_orbit * (180.0 / math.pi) * 3600.0 * orbits_per_century
    return float(arcsec_per_century)


def main():
    parser = argparse.ArgumentParser(description="Mercury perihelion precession (strict numerical extraction).")
    parser.add_argument("--plot", action="store_true", help="Plot u(φ) and mark the detected perihelion.")
    parser.add_argument("--step", type=float, default=5.0e-5, help="Step size in φ (radians). Default: 5e-5.")
    parser.add_argument("--phi-max-factor", type=float, default=1.20, help="Max φ as factor of 2π. Default: 1.20.")
    args = parser.parse_args()

    cfg_rel = SimulationConfig(step_dphi=args.step, phi_max_factor=args.phi_max_factor, relativistic=True, plot=args.plot)
    cfg_newt = SimulationConfig(step_dphi=args.step, phi_max_factor=args.phi_max_factor, relativistic=False, plot=False)

    print("=" * 60)
    print("EDC MERCURY PRECESSION SIMULATOR — STRICT (v17.49.017)")
    print("=" * 60)
    print("[BASELINE INPUTS]")
    print(f"  G          = {BASELINE_G:.6e} m^3 kg^-1 s^-2")
    print(f"  c          = {BASELINE_C:.1f} m/s (exact)")
    print(f"  M_sun      = {BASELINE_M_SUN:.6e} kg")
    print(f"  a (Mercury)= {BASELINE_A:.6e} m")
    print(f"  e (Mercury)= {BASELINE_E:.6f}")
    print(f"  step_dphi  = {args.step:.1e} rad")
    print()
    print("[CLAIM MANAGEMENT]")
    print("  Status: DERIVED (conditional on bridge mapping and Schwarzschild-equivalent orbit equation)")
    print()

    gr_ref = gr_closed_form_arcsec_per_century()
    print("[BASELINE] GR closed-form anomaly (weak-field):")
    print(f"  {gr_ref:.2f} arcsec/century")
    print()

    adv_rel, arcsec_rel, phi2_rel = simulate_once(cfg_rel)
    adv_newt, arcsec_newt, phi2_newt = simulate_once(cfg_newt)

    print("[DERIVED] Raw perihelion shifts (contain numerical drift):")
    print(f"  relativistic: φ₂={phi2_rel:.9f} rad, advance={adv_rel:.3e} rad, raw={arcsec_rel:.2f} arcsec/century")
    print(f"  Newtonian:    φ₂={phi2_newt:.9f} rad, advance={adv_newt:.3e} rad, raw={arcsec_newt:.2f} arcsec/century")
    print()

    anomaly = arcsec_rel - arcsec_newt
    rel_err = abs(anomaly - gr_ref) / gr_ref if gr_ref != 0 else float("nan")

    print("[DERIVED] Anomalous precession (drift-cancelled):")
    print(f"  anomaly = (relativistic - Newtonian) = {anomaly:.2f} arcsec/century")
    print(f"  deviation vs GR closed-form: {rel_err*100.0:.4f}%")
    print()

    print("=" * 60)
    print("CONCLUSION (strict):")
    print("• Raw shifts include numerical drift from perihelion detection on a discrete φ grid.")
    print("• The anomalous precession (rel - newt) cancels drift and should match ~43 arcsec/century.")
    print("• This is expected if the bridge reproduces Schwarzschild in the weak-field regime.")
    print("=" * 60)

    if args.plot:
        import matplotlib.pyplot as plt
        # quick plot for the relativistic run
        G = BASELINE_G
        c = BASELINE_C
        M = BASELINE_M_SUN
        a = BASELINE_A
        e = BASELINE_E
        mu = G * M
        p = a * (1.0 - e ** 2)
        h2 = mu * p
        r_p = a * (1.0 - e)
        u0 = 1.0 / r_p
        up0 = 0.0
        phi_max = cfg_rel.phi_max_factor * (2.0 * math.pi)
        n_steps = int(phi_max / cfg_rel.step_dphi) + 1
        phi = np.linspace(0.0, phi_max, n_steps, dtype=float)
        u = np.empty_like(phi)
        up = np.empty_like(phi)
        u[0] = u0
        up[0] = up0
        for i in range(1, n_steps):
            u[i], up[i] = _rk4_step(u[i - 1], up[i - 1], cfg_rel.step_dphi, mu, h2, c, True)
        phi2 = _detect_second_perihelion(phi, up)

        plt.figure()
        plt.plot(phi, u, label="u(φ)=1/r (relativistic)")
        if phi2 is not None:
            plt.axvline(phi2, linestyle="--", label="detected perihelion")
        plt.xlabel("φ [rad]")
        plt.ylabel("u = 1/r [1/m]")
        plt.title("Mercury u(φ) — perihelion detection (strict demo)")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()
