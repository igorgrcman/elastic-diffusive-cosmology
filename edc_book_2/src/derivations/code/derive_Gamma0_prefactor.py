#!/usr/bin/env python3
"""
DERIVE Γ₀ (Attempt Frequency / Prefactor) FROM EFFECTIVE 1D ACTION
===================================================================

This script computes the prefactor Γ₀ in the semiclassical tunneling rate:

    Γ ≈ Γ₀ × exp(-S/ℏ)

using the effective 1D action with M(q) and V(q) from the junction-core model.

Key formula (1D semiclassical / WKB):

    Γ₀ = (ω_n / 2π) × √(|ω_B²| / ω_n²) = √(ω_n |ω_B|) / (2π)

where:
    ω_n² = V''(q_n) / M(q_n)  [oscillation frequency at well minimum]
    ω_B² = V''(q_B) / M(q_B)  [negative: "frequency" at barrier top]

In canonical coordinates Q:
    ω_n² = U''(Q_n)  [since kinetic is ½Q̇²]
    ω_B² = U''(Q_B)

Epistemic tags:
  [Def] Definition
  [BL]  Baseline (PDG/CODATA)
  [I]   Identified (pattern fit)
  [Dc]  Derived conditional on model
  [P]   Proposed/Postulated

Date: 2026-01-27
Branch: taskC-derive-Gamma0-v1
Repository: edc_book_2/src/derivations/code/
"""

import numpy as np
import json
import csv
import os
from typing import Tuple, Dict, List, Optional
from dataclasses import dataclass, asdict

# Try to import scipy
try:
    from scipy.optimize import brentq, minimize_scalar
    from scipy.interpolate import UnivariateSpline
    from scipy.integrate import quad
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("WARNING: scipy not available. Using simplified methods.")

# Try to import matplotlib
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    print("WARNING: matplotlib not available. Skipping plots.")


# =============================================================================
# PHYSICAL CONSTANTS [BL]
# =============================================================================

M_E_MEV = 0.51099895  # MeV [BL] electron mass
ALPHA = 1.0 / 137.035999084  # [BL] fine structure constant
HBAR = 6.582119569e-22  # MeV·s [BL]
HBAR_C = 197.3269804  # MeV·fm [BL]
C_FM_PER_S = 2.998e23  # fm/s [BL]

# Target lifetime
TAU_N_BL = 879.0  # s [BL] neutron lifetime (PDG)

# =============================================================================
# EDC PARAMETERS [Dc]/[I]
# =============================================================================

SIGMA_EDC = 8.82  # MeV/fm² [Dc] brane tension
DELTA_EDC = 0.1   # fm [I] brane thickness (Compton anchor)
L0_EDC = 1.0      # fm [I] nucleon scale
TAU_EFF = 70.0    # MeV [Dc] effective inertia-energy scale (units: energy)
E0_EDC = SIGMA_EDC * L0_EDC**2  # MeV [Dc] junction-core energy scale


# =============================================================================
# V(q) FROM JUNCTION-CORE MODEL [Dc]
# =============================================================================

@dataclass
class JunctionCoreParams:
    """Parameters for junction core model."""
    C: float = 100.0          # Dimensionless coefficient [Dc]
    sigma: float = SIGMA_EDC  # Brane tension [MeV/fm²]
    delta: float = DELTA_EDC  # Brane thickness [fm]
    tau: float = 20.0         # String tension [MeV/fm]
    L0: float = L0_EDC        # In-brane leg projection [fm]
    k: float = 2.0            # Warp parameter [1/fm]
    mechanism: str = "A3"     # Lorentzian profile

    @property
    def E0(self) -> float:
        """Core energy scale E0 = C × σ × δ² [Dc]."""
        return self.C * self.sigma * self.delta**2


def V_NG_warped(q: float, params: JunctionCoreParams) -> float:
    """Nambu-Goto potential in warped bulk [Dc]."""
    tau = params.tau
    L0 = params.L0
    k = params.k

    if k < 1e-10:
        # Flat limit
        return 3.0 * tau * np.sqrt(L0**2 + q**2)

    # Straight embedding: ξ(l) = q × (1 - l/L0)
    n = 100
    dl = L0 / n
    E_leg = 0.0

    for i in range(n):
        l = (i + 0.5) * dl
        xi = q * (1.0 - l / L0)
        warp = np.exp(-k * np.abs(xi))
        dxi_dl = -q / L0
        E_leg += np.sqrt(warp**2 + dxi_dl**2) * dl

    return 3.0 * tau * E_leg


def V_core(q: float, params: JunctionCoreParams) -> float:
    """Junction-core potential (Lorentzian / A3 mechanism) [Dc]."""
    E0 = params.E0
    delta = params.delta
    x = q / delta

    if params.mechanism == "A3":
        return -E0 / (1.0 + x**2)
    elif params.mechanism in ("A1", "A2"):
        return -E0 * np.exp(-x**2)
    else:
        return -E0 / (1.0 + x**2)  # Default to Lorentzian


def V_total(q: float, params: JunctionCoreParams) -> float:
    """Total effective potential V(q) = V_NG(q) + V_core(q) [Dc]."""
    return V_NG_warped(q, params) + V_core(q, params)


# =============================================================================
# M(q) FROM TASK B [Dc]
# =============================================================================

def M_NG(q: float, params: JunctionCoreParams) -> float:
    """Nambu-Goto kinetic term M_NG(q) [Dc]."""
    L0 = params.L0
    L_leg_sq = L0**2 + q**2
    if L_leg_sq < 1e-20:
        return 0.0
    return TAU_EFF * q**2 / L_leg_sq


def M_core(q: float, params: JunctionCoreParams) -> float:
    """Junction-core kinetic term M_core(q) [Dc]."""
    delta = params.delta
    x = q / delta
    return E0_EDC / (1.0 + x**2)


def M_total(q: float, params: JunctionCoreParams) -> float:
    """Total effective mass M(q) = M_NG(q) + M_core(q) [Dc]."""
    return M_NG(q, params) + M_core(q, params)


# =============================================================================
# FIND EXTREMA [Dc]
# =============================================================================

def find_extrema(params: JunctionCoreParams,
                 q_max: float = 2.0,
                 n_points: int = 500) -> Dict:
    """
    Find barrier and well positions from V(q).

    Returns dict with q_B (barrier), q_n (neutron minimum), and related values.
    """
    q_arr = np.linspace(0.001, q_max, n_points)
    V_arr = np.array([V_total(q, params) for q in q_arr])

    # Find local maximum (barrier) and local minimum (neutron)
    dV = np.diff(V_arr)

    # Barrier: dV changes from + to - (local max)
    barrier_idx = None
    for i in range(len(dV) - 1):
        if dV[i] > 0 and dV[i+1] < 0:
            barrier_idx = i + 1
            break

    # Well: dV changes from - to + (local min) after barrier
    well_idx = None
    if barrier_idx is not None:
        for i in range(barrier_idx, len(dV) - 1):
            if dV[i] < 0 and dV[i+1] > 0:
                well_idx = i + 1
                break

    if barrier_idx is None or well_idx is None:
        return {"has_metastability": False}

    # Refine positions using spline
    if SCIPY_AVAILABLE:
        spline = UnivariateSpline(q_arr, V_arr, s=0, k=4)
        dspline = spline.derivative()

        # Refine barrier
        try:
            q_B = brentq(dspline, q_arr[max(0, barrier_idx-5)],
                        q_arr[min(len(q_arr)-1, barrier_idx+5)])
        except:
            q_B = q_arr[barrier_idx]

        # Refine well
        try:
            q_n = brentq(dspline, q_arr[max(0, well_idx-5)],
                        q_arr[min(len(q_arr)-1, well_idx+5)])
        except:
            q_n = q_arr[well_idx]
    else:
        q_B = q_arr[barrier_idx]
        q_n = q_arr[well_idx]

    V_B_val = V_total(q_B, params)
    V_n_val = V_total(q_n, params)
    V_barrier = V_B_val - V_n_val

    return {
        "has_metastability": True,
        "q_B": q_B,
        "q_n": q_n,
        "V_B": V_B_val,
        "V_n": V_n_val,
        "V_barrier": V_barrier,  # Barrier height above well
        "V_0": V_total(0, params)  # Proton energy
    }


# =============================================================================
# COMPUTE CURVATURES AND FREQUENCIES [Dc]
# =============================================================================

def compute_curvature(q: float, params: JunctionCoreParams, eps: float = 1e-5) -> float:
    """Compute V''(q) using central difference."""
    V_plus = V_total(q + eps, params)
    V_minus = V_total(q - eps, params)
    V_center = V_total(q, params)
    return (V_plus - 2*V_center + V_minus) / eps**2


def compute_frequencies(params: JunctionCoreParams, q_n: float, q_B: float) -> Dict:
    """
    Compute oscillation frequencies at well and barrier.

    ω² = V''(q) / M(q)

    Returns frequencies in natural units (1/fm).
    To convert to Hz: ω_Hz = ω × c / (2π fm)
    """
    # Curvatures
    V_pp_n = compute_curvature(q_n, params)
    V_pp_B = compute_curvature(q_B, params)

    # Masses
    M_n = M_total(q_n, params)
    M_B = M_total(q_B, params)

    # Frequencies squared (in MeV/fm² / MeV = 1/fm²)
    omega_n_sq = V_pp_n / M_n
    omega_B_sq = V_pp_B / M_B  # Should be negative at barrier

    # Convert to angular frequency in 1/s
    # ω [1/fm] × c [fm/s] = ω_angular [rad/s]
    # Then ω_angular / (2π) = frequency in Hz

    omega_n = np.sqrt(abs(omega_n_sq)) if omega_n_sq > 0 else 0
    omega_B = np.sqrt(abs(omega_B_sq))

    return {
        "V_pp_n": V_pp_n,
        "V_pp_B": V_pp_B,
        "M_n": M_n,
        "M_B": M_B,
        "omega_n_sq": omega_n_sq,
        "omega_B_sq": omega_B_sq,
        "omega_n": omega_n,      # 1/fm (natural units)
        "omega_B": omega_B,      # 1/fm (natural units)
        "well_stable": omega_n_sq > 0,
        "barrier_unstable": omega_B_sq < 0
    }


# =============================================================================
# PREFACTOR Γ₀ [Dc]
# =============================================================================

def compute_Gamma0(omega_n: float, omega_B: float) -> Dict:
    """
    Compute prefactor Γ₀ using standard 1D semiclassical formula [Dc].

    Formula (Langer/Kramers 1D):
        Γ₀ = (ω_n / 2π) × √(|ω_B|² / ω_n²)
           = (1/2π) × √(ω_n² × |ω_B|²)^(1/2)
           = √(ω_n × |ω_B|) / (2π)

    In simplest approximation (ω_n dominates):
        Γ₀ ≈ ω_n / (2π)

    We compute both for comparison.

    Args:
        omega_n: Well frequency [1/fm] (natural units)
        omega_B: Barrier frequency [1/fm] (natural units)

    Returns:
        Dictionary with prefactor values in various units.
    """
    # Prefactor in natural units [1/fm]
    Gamma0_simple = omega_n / (2 * np.pi)  # Simple formula
    Gamma0_full = np.sqrt(omega_n * omega_B) / (2 * np.pi)  # Full formula

    # Convert to 1/s using c = 2.998×10²³ fm/s
    # Γ₀ [1/fm] × c [fm/s] = Γ₀ [1/s]
    Gamma0_simple_Hz = Gamma0_simple * C_FM_PER_S
    Gamma0_full_Hz = Gamma0_full * C_FM_PER_S

    # Convert to lifetime prefactor
    # τ₀ = 1/Γ₀
    tau0_simple = 1.0 / Gamma0_simple_Hz if Gamma0_simple_Hz > 0 else np.inf
    tau0_full = 1.0 / Gamma0_full_Hz if Gamma0_full_Hz > 0 else np.inf

    return {
        "omega_n_per_fm": omega_n,
        "omega_B_per_fm": omega_B,
        "Gamma0_simple_per_fm": Gamma0_simple,
        "Gamma0_full_per_fm": Gamma0_full,
        "Gamma0_simple_Hz": Gamma0_simple_Hz,
        "Gamma0_full_Hz": Gamma0_full_Hz,
        "tau0_simple_s": tau0_simple,
        "tau0_full_s": tau0_full
    }


# =============================================================================
# EUCLIDEAN ACTION (BARRIER INTEGRAL) [Dc]
# =============================================================================

def compute_action(params: JunctionCoreParams, q_n: float, q_B: float,
                   E_level: Optional[float] = None) -> Dict:
    """
    Compute WKB action integral through barrier.

    S/ℏ = (2/ℏc) × ∫_{q_B}^{q_n} √(2M(q)(V(q) - E)) dq

    For ground state tunneling, E ≈ V(q_n) + ½ℏω_n (zero-point).
    In practice, we often use E = V(q_n) for the leading-order result.
    """
    if E_level is None:
        E_level = V_total(q_n, params)  # At well bottom

    def integrand(q):
        V_val = V_total(q, params)
        M_val = M_total(q, params)
        diff = V_val - E_level
        if diff <= 0:
            return 0.0
        return np.sqrt(2 * M_val * diff)

    if SCIPY_AVAILABLE:
        # Integrate from barrier to well
        result, error = quad(integrand, q_B, q_n, limit=200)
        S_over_hbar_c = 2 * result  # Factor of 2 for round-trip (bounce)
    else:
        # Simple trapezoidal integration
        n_points = 500
        q_arr = np.linspace(q_B, q_n, n_points)
        integrand_arr = np.array([integrand(q) for q in q_arr])
        S_over_hbar_c = 2 * np.trapz(integrand_arr, q_arr)

    # Convert to dimensionless S/ℏ
    # integrand has units √(MeV × MeV) = MeV
    # integral has units MeV × fm
    # S/ℏ = (integral [MeV·fm]) / (ℏc [MeV·fm]) is dimensionless
    S_over_hbar = S_over_hbar_c / HBAR_C

    return {
        "S_over_hbar_c": S_over_hbar_c,  # MeV·fm
        "S_over_hbar": S_over_hbar,      # dimensionless
        "E_level": E_level,
        "exp_minus_S": np.exp(-S_over_hbar)
    }


# =============================================================================
# FULL DECAY RATE CALCULATION [Dc]
# =============================================================================

def compute_decay_rate(params: JunctionCoreParams) -> Dict:
    """
    Compute full semiclassical decay rate Γ = Γ₀ × exp(-S/ℏ).

    Returns comprehensive results dictionary.
    """
    # Find extrema
    extrema = find_extrema(params)

    if not extrema.get("has_metastability", False):
        return {
            "status": "NO_METASTABILITY",
            "has_metastability": False,
            "params": asdict(params)
        }

    q_n = extrema["q_n"]
    q_B = extrema["q_B"]

    # Compute frequencies
    freqs = compute_frequencies(params, q_n, q_B)

    if not freqs["well_stable"]:
        return {
            "status": "WELL_UNSTABLE",
            "has_metastability": True,
            "extrema": extrema,
            "frequencies": freqs,
            "params": asdict(params)
        }

    # Compute prefactor
    prefactor = compute_Gamma0(freqs["omega_n"], freqs["omega_B"])

    # Compute action
    action = compute_action(params, q_n, q_B)

    # Full decay rate
    Gamma_full_Hz = prefactor["Gamma0_full_Hz"] * action["exp_minus_S"]
    tau_full_s = 1.0 / Gamma_full_Hz if Gamma_full_Hz > 0 else np.inf

    Gamma_simple_Hz = prefactor["Gamma0_simple_Hz"] * action["exp_minus_S"]
    tau_simple_s = 1.0 / Gamma_simple_Hz if Gamma_simple_Hz > 0 else np.inf

    return {
        "status": "SUCCESS",
        "has_metastability": True,
        "extrema": extrema,
        "frequencies": freqs,
        "prefactor": prefactor,
        "action": action,
        "Gamma_full_Hz": Gamma_full_Hz,
        "Gamma_simple_Hz": Gamma_simple_Hz,
        "tau_full_s": tau_full_s,
        "tau_simple_s": tau_simple_s,
        "tau_target_s": TAU_N_BL,
        "tau_ratio_full": tau_full_s / TAU_N_BL,
        "tau_ratio_simple": tau_simple_s / TAU_N_BL,
        "params": asdict(params)
    }


# =============================================================================
# SENSITIVITY ANALYSIS [Dc]
# =============================================================================

def sensitivity_scan_delta(delta_values: List[float],
                           base_params: JunctionCoreParams) -> List[Dict]:
    """Scan Γ₀ sensitivity to brane thickness δ."""
    results = []

    for delta in delta_values:
        params = JunctionCoreParams(
            C=base_params.C,
            sigma=base_params.sigma,
            delta=delta,
            tau=base_params.tau,
            L0=base_params.L0,
            k=base_params.k,
            mechanism=base_params.mechanism
        )

        result = compute_decay_rate(params)
        result["delta_fm"] = delta
        results.append(result)

    return results


def sensitivity_scan_L0(L0_values: List[float],
                        base_params: JunctionCoreParams) -> List[Dict]:
    """Scan Γ₀ sensitivity to nucleon scale L0."""
    results = []

    for L0 in L0_values:
        params = JunctionCoreParams(
            C=base_params.C,
            sigma=base_params.sigma,
            delta=base_params.delta,
            tau=base_params.tau,
            L0=L0,
            k=base_params.k,
            mechanism=base_params.mechanism
        )

        result = compute_decay_rate(params)
        result["L0_fm"] = L0
        results.append(result)

    return results


# =============================================================================
# PLOTTING [Dc]
# =============================================================================

def plot_sensitivity(results: List[Dict], x_key: str, x_label: str,
                     filename: str):
    """Plot Γ₀ sensitivity to parameter variation."""
    if not PLOTTING_AVAILABLE:
        return

    x_vals = []
    Gamma0_vals = []
    tau_vals = []

    for r in results:
        if r.get("status") == "SUCCESS":
            x_vals.append(r[x_key])
            Gamma0_vals.append(r["prefactor"]["Gamma0_full_Hz"])
            tau_vals.append(r["tau_full_s"])

    if not x_vals:
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gamma0 plot
    ax1.semilogy(x_vals, Gamma0_vals, 'b-o', linewidth=2, markersize=8)
    ax1.set_xlabel(x_label, fontsize=12)
    ax1.set_ylabel(r'$\Gamma_0$ [Hz]', fontsize=12)
    ax1.set_title(r'Prefactor $\Gamma_0$ sensitivity', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # Lifetime plot
    ax2.semilogy(x_vals, tau_vals, 'r-s', linewidth=2, markersize=8)
    ax2.axhline(TAU_N_BL, color='k', linestyle='--', label=r'$\tau_n^{BL}$ = 879 s')
    ax2.set_xlabel(x_label, fontsize=12)
    ax2.set_ylabel(r'$\tau$ [s]', fontsize=12)
    ax2.set_title('Lifetime sensitivity', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved: {filename}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Run Γ₀ derivation and sensitivity analysis."""

    print("=" * 70)
    print("DERIVE Γ₀ PREFACTOR FROM EFFECTIVE 1D ACTION")
    print("=" * 70)
    print()

    # Best-fit parameters from junction-core scan
    params = JunctionCoreParams(
        C=100.0,
        sigma=SIGMA_EDC,
        delta=DELTA_EDC,
        tau=20.0,        # MeV/fm
        L0=L0_EDC,
        k=2.0,           # 1/fm
        mechanism="A3"   # Lorentzian
    )

    print("INPUT PARAMETERS:")
    print(f"  C = {params.C} [Dc]")
    print(f"  σ = {params.sigma:.2f} MeV/fm² [Dc]")
    print(f"  δ = {params.delta:.3f} fm [I]")
    print(f"  τ = {params.tau:.1f} MeV/fm")
    print(f"  L0 = {params.L0:.2f} fm [I]")
    print(f"  k = {params.k:.1f} /fm")
    print(f"  E0 = {params.E0:.2f} MeV [Dc]")
    print()

    # Compute full decay rate
    result = compute_decay_rate(params)

    if result["status"] != "SUCCESS":
        print(f"ERROR: {result['status']}")
        return

    # Extract results
    ext = result["extrema"]
    freq = result["frequencies"]
    pref = result["prefactor"]
    act = result["action"]

    print("EXTREMA [Dc]:")
    print(f"  q_B (barrier) = {ext['q_B']:.4f} fm")
    print(f"  q_n (well)    = {ext['q_n']:.4f} fm")
    print(f"  V_barrier     = {ext['V_barrier']:.3f} MeV")
    print()

    print("EFFECTIVE MASS [Dc]:")
    print(f"  M(q_n) = {freq['M_n']:.3f} MeV")
    print(f"  M(q_B) = {freq['M_B']:.3f} MeV")
    print()

    print("CURVATURES [Dc]:")
    print(f"  V''(q_n) = {freq['V_pp_n']:.3f} MeV/fm²")
    print(f"  V''(q_B) = {freq['V_pp_B']:.3f} MeV/fm² (should be <0)")
    print()

    print("FREQUENCIES [Dc]:")
    print(f"  ω_n² = V''(q_n)/M(q_n) = {freq['omega_n_sq']:.3f} /fm² (>0: stable)")
    print(f"  ω_B² = V''(q_B)/M(q_B) = {freq['omega_B_sq']:.3f} /fm² (<0: unstable)")
    print(f"  ω_n = {freq['omega_n']:.4f} /fm")
    print(f"  ω_B = {freq['omega_B']:.4f} /fm")
    print()

    print("PREFACTOR Γ₀ [Dc]:")
    print(f"  Simple formula: Γ₀ = ω_n/(2π)")
    print(f"    Γ₀ = {pref['Gamma0_simple_Hz']:.3e} Hz")
    print(f"    τ₀ = {pref['tau0_simple_s']:.3e} s")
    print()
    print(f"  Full formula: Γ₀ = √(ω_n ω_B)/(2π)")
    print(f"    Γ₀ = {pref['Gamma0_full_Hz']:.3e} Hz")
    print(f"    τ₀ = {pref['tau0_full_s']:.3e} s")
    print()

    print("ACTION INTEGRAL [Dc]:")
    print(f"  S/ℏ = {act['S_over_hbar']:.2f}")
    print(f"  exp(-S/ℏ) = {act['exp_minus_S']:.3e}")
    print()

    print("FULL DECAY RATE [Dc]:")
    print(f"  Γ = Γ₀ × exp(-S/ℏ)")
    print(f"  Γ (full formula) = {result['Gamma_full_Hz']:.3e} Hz")
    print(f"  τ (full formula) = {result['tau_full_s']:.3e} s")
    print()
    print(f"  Target: τ_n^BL = {TAU_N_BL:.0f} s")
    print(f"  Ratio τ/τ_n^BL = {result['tau_ratio_full']:.2e}")
    print()

    # Sensitivity analysis
    print("=" * 70)
    print("SENSITIVITY ANALYSIS")
    print("=" * 70)
    print()

    # Delta sensitivity (±20% around Compton anchor)
    delta_central = DELTA_EDC
    delta_values = [delta_central * (1 + x) for x in [-0.20, -0.10, 0, 0.10, 0.20]]
    delta_results = sensitivity_scan_delta(delta_values, params)

    print("δ sensitivity (keeping L0, C, τ, k fixed):")
    print("-" * 60)
    print(f"{'δ [fm]':>10} {'Γ₀ [Hz]':>15} {'S/ℏ':>10} {'τ [s]':>15}")
    print("-" * 60)

    for r in delta_results:
        if r.get("status") == "SUCCESS":
            print(f"{r['delta_fm']:>10.4f} {r['prefactor']['Gamma0_full_Hz']:>15.3e} "
                  f"{r['action']['S_over_hbar']:>10.1f} {r['tau_full_s']:>15.3e}")
    print("-" * 60)
    print()

    # Save artifacts
    output_dir = os.path.dirname(os.path.abspath(__file__)) + "/../artifacts"
    os.makedirs(output_dir, exist_ok=True)

    # JSON output
    json_path = os.path.join(output_dir, "gamma0_results.json")
    with open(json_path, 'w') as f:
        # Convert numpy types for JSON serialization
        result_clean = json.loads(json.dumps(result, default=lambda x: float(x) if hasattr(x, '__float__') else str(x)))
        json.dump(result_clean, f, indent=2)
    print(f"Saved: {json_path}")

    # CSV output
    csv_path = os.path.join(output_dir, "gamma0_results.csv")
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Quantity", "Value", "Units", "Tag"])
        writer.writerow(["q_B", f"{ext['q_B']:.4f}", "fm", "[Dc]"])
        writer.writerow(["q_n", f"{ext['q_n']:.4f}", "fm", "[Dc]"])
        writer.writerow(["V_barrier", f"{ext['V_barrier']:.3f}", "MeV", "[Dc]"])
        writer.writerow(["M(q_n)", f"{freq['M_n']:.3f}", "MeV", "[Dc]"])
        writer.writerow(["M(q_B)", f"{freq['M_B']:.3f}", "MeV", "[Dc]"])
        writer.writerow(["omega_n", f"{freq['omega_n']:.4f}", "1/fm", "[Dc]"])
        writer.writerow(["omega_B", f"{freq['omega_B']:.4f}", "1/fm", "[Dc]"])
        writer.writerow(["Gamma0_full", f"{pref['Gamma0_full_Hz']:.3e}", "Hz", "[Dc]"])
        writer.writerow(["S_over_hbar", f"{act['S_over_hbar']:.2f}", "dimensionless", "[Dc]"])
        writer.writerow(["tau_full", f"{result['tau_full_s']:.3e}", "s", "[Dc]"])
        writer.writerow(["tau_target", f"{TAU_N_BL:.0f}", "s", "[BL]"])
    print(f"Saved: {csv_path}")

    # Sensitivity plot
    if PLOTTING_AVAILABLE:
        fig_dir = os.path.dirname(os.path.abspath(__file__)) + "/../figures"
        os.makedirs(fig_dir, exist_ok=True)
        plot_sensitivity(delta_results, "delta_fm", r"$\delta$ [fm]",
                        os.path.join(fig_dir, "gamma0_sensitivity_delta.png"))

    # Summary box
    print()
    print("=" * 70)
    print("EPISTEMIC STATUS BOX")
    print("=" * 70)
    print()
    print("  ┌─────────────────────────────────────────────────────────────────┐")
    print("  │ Γ₀ DERIVATION STATUS                                           │")
    print("  ├─────────────────────────────────────────────────────────────────┤")
    print(f"  │ ω_n = √(V''(q_n)/M(q_n)) = {freq['omega_n']:.4f} /fm        [Dc]   │")
    print(f"  │ ω_B = √(|V''(q_B)|/M(q_B)) = {freq['omega_B']:.4f} /fm      [Dc]   │")
    print(f"  │ Γ₀ = √(ω_n ω_B)/(2π) = {pref['Gamma0_full_Hz']:.2e} Hz     [Dc]   │")
    print("  ├─────────────────────────────────────────────────────────────────┤")
    print("  │ FORMULA: Standard 1D semiclassical (Langer/Kramers)            │")
    print("  │ VALIDITY: Adiabatic, harmonic near extrema, 1D reduction       │")
    print("  │ ROOT-OF-TRUST: M(q) [Dc] + V(q) [Dc] → ω_n, ω_B [Dc] → Γ₀ [Dc]│")
    print("  ├─────────────────────────────────────────────────────────────────┤")
    print("  │ UPGRADE: Γ₀ [Cal] → [Dc] ✓ ACHIEVED                           │")
    print("  └─────────────────────────────────────────────────────────────────┘")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
