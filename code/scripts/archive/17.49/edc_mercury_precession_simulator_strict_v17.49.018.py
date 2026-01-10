
"""edc_mercury_precession_simulator.py — STRICT (v17.49.018)

Mercury perihelion precession — numerical extraction with drift-cancelled anomaly
+ convergence (self-test) mode.

Key rigor point:
  - Raw perihelion shift estimates include *numerical drift* from discrete φ sampling and perihelion detection.
  - The physically interpreted quantity in this verification script is the *anomalous precession*:
        anomaly = (relativistic - Newtonian)
    which cancels the drift to first order.

Epistemic status (strict):
  - IDENTIFIED: River-flow profile v(r)^2 = 2GM/r (bridge mapping).
  - BASELINE: Weak-field Schwarzschild-equivalent orbit equation:
        u'' + u = mu/h^2 + 3 mu u^2 / c^2
    and its Newtonian limit (without the 3 mu u^2 / c^2 term).
  - DERIVED: Numerical integration + perihelion detection + anomaly extraction (Δ = rel - newt).
  - DERIVED: Convergence table across step sizes (self-test), if enabled.

What this script is NOT:
  - Not a first-principles derivation of v(r) from EDC core dynamics.
  - Not an independent prediction unless the bridge identifications are derived (not assumed).

Run:
  python edc_mercury_precession_simulator.py
  python edc_mercury_precession_simulator.py --step 5e-5
  python edc_mercury_precession_simulator.py --convergence
  python edc_mercury_precession_simulator.py --convergence --tol 0.05

"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Tuple, Optional, List

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
    step_dphi: float = 5.0e-5              # rad
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


def _run_once(step: float, phi_max_factor: float) -> Tuple[float, float, float, float]:
    """Run both relativistic and Newtonian and return (raw_rel, raw_newt, anomaly, phi2_rel)."""
    cfg_rel = SimulationConfig(step_dphi=step, phi_max_factor=phi_max_factor, relativistic=True, plot=False)
    cfg_newt = SimulationConfig(step_dphi=step, phi_max_factor=phi_max_factor, relativistic=False, plot=False)

    _, raw_rel, phi2_rel = simulate_once(cfg_rel)
    _, raw_newt, _ = simulate_once(cfg_newt)
    anomaly = raw_rel - raw_newt
    return raw_rel, raw_newt, anomaly, phi2_rel


def convergence_self_test(steps: List[float], phi_max_factor: float, tol_arcsec: float) -> Tuple[bool, List[Tuple[float, float, float, float]]]:
    """Return (pass, rows) where each row is (step, raw_rel, raw_newt, anomaly)."""
    rows = []
    for st in steps:
        raw_rel, raw_newt, anomaly, _ = _run_once(st, phi_max_factor)
        rows.append((st, raw_rel, raw_newt, anomaly))
    anomalies = [r[3] for r in rows]
    spread = max(anomalies) - min(anomalies)
    passed = spread <= tol_arcsec
    return passed, rows


def main():
    parser = argparse.ArgumentParser(description="Mercury perihelion precession (strict numerical extraction).")
    parser.add_argument("--plot", action="store_true", help="Plot u(φ) and mark the detected perihelion.")
    parser.add_argument("--step", type=float, default=5.0e-5, help="Step size in φ (radians). Default: 5e-5.")
    parser.add_argument("--phi-max-factor", type=float, default=1.20, help="Max φ as factor of 2π. Default: 1.20.")
    parser.add_argument("--convergence", action="store_true", help="Run convergence self-test across step sizes.")
    parser.add_argument("--tol", type=float, default=0.05, help="Convergence tolerance in arcsec/century for anomaly spread. Default: 0.05.")
    args = parser.parse_args()

    print("=" * 60)
    print("EDC MERCURY PRECESSION SIMULATOR — STRICT (v17.49.018)")
    print("=" * 60)
    print("[BASELINE INPUTS]")
    print(f"  G          = {BASELINE_G:.6e} m^3 kg^-1 s^-2")
    print(f"  c          = {BASELINE_C:.1f} m/s (exact)")
    print(f"  M_sun      = {BASELINE_M_SUN:.6e} kg")
    print(f"  a (Mercury)= {BASELINE_A:.6e} m")
    print(f"  e (Mercury)= {BASELINE_E:.6f}")
    print()

    print("[CLAIM MANAGEMENT]")
    print("  Status: DERIVED (conditional on bridge mapping and Schwarzschild-equivalent orbit equation)")
    print("  Interpretation rule: ONLY the anomaly (relativistic - Newtonian) is treated as physical here.")
    print()

    gr_ref = gr_closed_form_arcsec_per_century()
    print("[BASELINE] GR closed-form anomaly (weak-field):")
    print(f"  {gr_ref:.2f} arcsec/century")
    print()

    # Single run with user step
    raw_rel, raw_newt, anomaly, phi2_rel = _run_once(args.step, args.phi_max_factor)

    print("[DERIVED] Raw perihelion shifts (contain numerical drift):")
    print(f"  relativistic: φ₂={phi2_rel:.9f} rad, raw={raw_rel:.2f} arcsec/century")
    print(f"  Newtonian:    raw={raw_newt:.2f} arcsec/century")
    print()

    rel_err = abs(anomaly - gr_ref) / gr_ref if gr_ref != 0 else float("nan")
    print("[DERIVED] Anomalous precession (drift-cancelled):")
    print(f"  anomaly = (relativistic - Newtonian) = {anomaly:.2f} arcsec/century")
    print(f"  deviation vs GR closed-form: {rel_err*100.0:.4f}%")
    print()

    # Convergence self-test
    if args.convergence:
        steps = [1.0e-4, 5.0e-5, 2.0e-5]
        passed, rows = convergence_self_test(steps, args.phi_max_factor, args.tol)
        print("[SELF-TEST] Convergence across step sizes (anomaly spread criterion):")
        print(f"  steps tested: {', '.join(f'{s:.0e}' for s in steps)} rad")
        print(f"  tolerance:    {args.tol:.3f} arcsec/century (max-min anomaly)")
        print()
        print("  step_dphi    raw_rel      raw_newt     anomaly")
        for st, rr, rn, an in rows:
            print(f"  {st:9.0e}  {rr:9.2f}   {rn:9.2f}   {an:7.3f}")
        anomalies = [r[3] for r in rows]
        spread = max(anomalies) - min(anomalies)
        print()
        print(f"  anomaly spread (max-min): {spread:.4f} arcsec/century")
        print("  PASS" if passed else "  FAIL (reduce step or improve perihelion estimator)")
        print()

    print("=" * 60)
    print("CONCLUSION (strict):")
    print("• Raw shifts include numerical drift from perihelion detection on a discrete φ grid.")
    print("• The anomalous precession (rel - newt) cancels drift and should match ~43 arcsec/century.")
    print("• Agreement is expected if the bridge reproduces Schwarzschild in the weak-field regime.")
    print("=" * 60)

    if args.plot:
        import matplotlib.pyplot as plt

        # Plot for the relativistic run
        step = args.step
        phi_max = args.phi_max_factor * (2.0 * math.pi)
        n_steps = int(phi_max / step) + 1
        phi = np.linspace(0.0, phi_max, n_steps, dtype=float)

        # Recompute the trajectory for plotting
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

        u = np.empty_like(phi)
        up = np.empty_like(phi)
        u[0] = u0
        up[0] = up0

        for i in range(1, n_steps):
            u[i], up[i] = _rk4_step(u[i - 1], up[i - 1], step, mu, h2, c, True)

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
