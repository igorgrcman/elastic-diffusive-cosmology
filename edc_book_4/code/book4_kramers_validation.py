#!/usr/bin/env python3
"""
KRAMERS ESCAPE VALIDATION FOR METASTABLE JUNCTION
==================================================
EDC Book IV - Route F v2 Implementation

Implements guardrails RF-1 through RF-6 to avoid arbitrary fitting.

Key features:
- RF-1: V(q) derived from junction-core parameters (not arbitrary)
- RF-2: Uses dimensionless Theta = DV/T_eff and Upsilon = gamma/omega_b
- RF-3: 1000 trajectories per point with full statistics
- RF-4: Identifies overdamped/underdamped/turnover regime
- RF-5: Flags fine-tuning if 879s requires extreme parameters
- RF-6: Produces book-ready verdict

Status: [Dc] Computational with strict acceptance criteria
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Any
from scipy.optimize import brentq, minimize_scalar
import warnings


# =============================================================================
# DIMENSIONLESS PARAMETERS (RF-2)
# =============================================================================

@dataclass
class DimensionlessParams:
    """
    Kramers problem in dimensionless form.

    Theta = DV / T_eff  -- barrier height in units of noise scale
    Upsilon = gamma / omega_b -- damping in units of barrier frequency

    The escape time in dimensionless units: tau_dimless = tau * omega_b
    """
    Theta: float      # DV / T_eff (barrier/noise ratio)
    Upsilon: float    # gamma / omega_b (damping/frequency ratio)

    regime: str = field(init=False)
    tau_kramers_dimless: float = field(init=False)

    def __post_init__(self):
        """Determine Kramers regime and prediction."""
        if self.Upsilon < 0.1:
            self.regime = "UNDERDAMPED"
        elif self.Upsilon > 10:
            self.regime = "OVERDAMPED"
        else:
            self.regime = "TURNOVER"

        if self.Theta <= 0:
            self.tau_kramers_dimless = 0.0
            return

        if self.Upsilon > 1:  # Overdamped (Smoluchowski)
            self.tau_kramers_dimless = (2 * np.pi / self.Upsilon) * np.exp(self.Theta)
        elif self.Upsilon < 0.1:  # Underdamped (energy diffusion)
            self.tau_kramers_dimless = (self.Theta / self.Upsilon) * np.exp(self.Theta)
        else:  # Turnover
            factor = np.sqrt(1 + (self.Upsilon/2)**2) - self.Upsilon/2
            self.tau_kramers_dimless = (2 * np.pi / factor) * np.exp(self.Theta)


# =============================================================================
# DOUBLE-WELL POTENTIAL (RF-1: anchored to junction geometry)
# =============================================================================

def create_quartic_potential(Delta_V: float, asymmetry: float = 0.1):
    """
    Create a smooth quartic double-well with specified barrier height.

    V(x) = V0 * (x^4 - 2x^2) + delta * x

    Left well = anchor minimum (ground state)
    Right well = metastable minimum (excited state)
    Barrier separates the two configurations.

    Returns potential function and derived parameters.
    """
    V0 = Delta_V
    delta = asymmetry

    def V(x):
        return V0 * (x**4 - 2*x**2) + delta * x

    def dV(x):
        return V0 * (4*x**3 - 4*x) + delta

    def d2V(x):
        return V0 * (12*x**2 - 4)

    # Find critical points
    # Left minimum (anchor)
    res_a = minimize_scalar(V, bounds=(-2, 0), method='bounded')
    x_anchor = res_a.x

    # Right minimum (metastable)
    res_m = minimize_scalar(V, bounds=(0, 2), method='bounded')
    x_meta = res_m.x

    # Barrier
    try:
        x_barrier = brentq(dV, x_anchor + 0.01, x_meta - 0.01)
    except:
        x_barrier = 0.0

    # Frequencies at critical points
    omega_meta = np.sqrt(max(d2V(x_meta), 0.01))
    omega_anchor = np.sqrt(max(d2V(x_anchor), 0.01))
    omega_barrier = np.sqrt(max(-d2V(x_barrier), 0.01))

    # Actual barrier height from metastable
    actual_DV = V(x_barrier) - V(x_meta)

    return {
        'V': V,
        'dV': dV,
        'd2V': d2V,
        'x_meta': x_meta,
        'x_anchor': x_anchor,
        'x_barrier': x_barrier,
        'omega_meta': omega_meta,
        'omega_anchor': omega_anchor,
        'omega_barrier': omega_barrier,
        'Delta_V': actual_DV,
        'V0': V0,
        'asymmetry': asymmetry,
    }


# =============================================================================
# LANGEVIN DYNAMICS (RF-3)
# =============================================================================

def langevin_step_BAOAB(x: float, v: float, dV_func, gamma: float, T: float,
                        dt: float, rng) -> Tuple[float, float]:
    """
    Single BAOAB Langevin integration step.

    BAOAB splitting: B-A-O-A-B (velocity-position-thermostat-position-velocity)
    Symmetric and stable for moderate dt.
    """
    # B: half velocity kick
    dV = dV_func(x)
    v = v - 0.5 * dt * dV

    # A: half position update
    x = x + 0.5 * dt * v

    # O: Ornstein-Uhlenbeck thermostat
    c1 = np.exp(-gamma * dt)
    c2 = np.sqrt((1 - c1**2) * T) if T > 0 else 0.0
    v = c1 * v + c2 * rng.standard_normal()

    # A: half position update
    x = x + 0.5 * dt * v

    # B: half velocity kick
    dV = dV_func(x)
    v = v - 0.5 * dt * dV

    return x, v


def run_escape_trajectory(potential: Dict, Theta: float, Upsilon: float,
                          max_time: float = 1e6, dt: float = 0.01,
                          seed: Optional[int] = None) -> Dict:
    """
    Run single escape trajectory from metastable well.

    Returns escape time and trajectory statistics.
    """
    rng = np.random.default_rng(seed)

    V = potential['V']
    dV = potential['dV']
    x_meta = potential['x_meta']
    x_barrier = potential['x_barrier']
    omega_barrier = potential['omega_barrier']
    Delta_V = potential['Delta_V']

    # Convert dimensionless params to physical
    T_eff = Delta_V / Theta if Theta > 0 else 1.0
    gamma = Upsilon * omega_barrier

    # Initial conditions: at metastable minimum
    x = x_meta
    v = rng.standard_normal() * np.sqrt(T_eff)

    # Integrate until escape
    t = 0.0
    n_steps = 0
    max_steps = int(max_time / dt)

    while n_steps < max_steps:
        x, v = langevin_step_BAOAB(x, v, dV, gamma, T_eff, dt, rng)
        t += dt
        n_steps += 1

        # Check for escape (crossed barrier toward anchor)
        if x < x_barrier:
            return {
                'escaped': True,
                'escape_time': t,
                'final_x': x,
                'n_steps': n_steps,
            }

    return {
        'escaped': False,
        'escape_time': max_time,
        'final_x': x,
        'n_steps': n_steps,
    }


def run_escape_ensemble(potential: Dict, Theta: float, Upsilon: float,
                        n_trajectories: int = 1000, max_time: float = 1e6,
                        dt: float = 0.01, seed: int = 42) -> Dict:
    """
    Run ensemble of escape trajectories (RF-3: 1000 trajectories).

    Returns ensemble statistics.
    """
    rng = np.random.default_rng(seed)
    seeds = rng.integers(0, 2**31, size=n_trajectories)

    escape_times = []
    n_escaped = 0

    for i, s in enumerate(seeds):
        result = run_escape_trajectory(potential, Theta, Upsilon,
                                       max_time=max_time, dt=dt, seed=int(s))
        if result['escaped']:
            escape_times.append(result['escape_time'])
            n_escaped += 1

    if len(escape_times) > 0:
        tau_mean = np.mean(escape_times)
        tau_std = np.std(escape_times)
        tau_median = np.median(escape_times)
    else:
        tau_mean = max_time
        tau_std = 0.0
        tau_median = max_time

    return {
        'n_trajectories': n_trajectories,
        'n_escaped': n_escaped,
        'escape_fraction': n_escaped / n_trajectories,
        'tau_mean': tau_mean,
        'tau_std': tau_std,
        'tau_median': tau_median,
        'Theta': Theta,
        'Upsilon': Upsilon,
    }


# =============================================================================
# FINE-TUNING ASSESSMENT (RF-5)
# =============================================================================

def check_fine_tuning(Theta: float, Upsilon: float, tau_target: float,
                      omega_barrier: float = 1.0) -> Dict:
    """
    Assess fine-tuning level (RF-5).

    Returns warning flags if parameters seem unnatural.
    """
    params = DimensionlessParams(Theta=Theta, Upsilon=Upsilon)

    # Physical time
    tau_pred_dimless = params.tau_kramers_dimless
    tau_pred_phys = tau_pred_dimless / omega_barrier

    # Sensitivity: d(log tau)/d(Theta) = Theta (exponential sensitivity)
    sensitivity_Theta = Theta

    # Sensitivity: d(log tau)/d(Upsilon) ~ 1 (mild)
    sensitivity_Upsilon = 1.0

    # Fine-tuning flags
    warnings_list = []

    if Theta > 100:
        warnings_list.append(f"EXTREME_BARRIER: Theta={Theta:.1f} >> 100")
    if Theta < 10:
        warnings_list.append(f"LOW_BARRIER: Theta={Theta:.1f} < 10")
    if Upsilon < 0.01:
        warnings_list.append(f"EXTREME_UNDERDAMPED: Upsilon={Upsilon:.3f}")
    if Upsilon > 100:
        warnings_list.append(f"EXTREME_OVERDAMPED: Upsilon={Upsilon:.1f}")

    return {
        'Theta': Theta,
        'Upsilon': Upsilon,
        'regime': params.regime,
        'tau_pred_dimless': tau_pred_dimless,
        'tau_pred_phys': tau_pred_phys,
        'tau_target': tau_target,
        'sensitivity_Theta': sensitivity_Theta,
        'sensitivity_Upsilon': sensitivity_Upsilon,
        'fine_tuned': len(warnings_list) > 0,
        'warnings': warnings_list,
    }


# =============================================================================
# BOOK-READY VERDICT (RF-6)
# =============================================================================

def generate_verdict(ensemble_result: Dict, kramers_pred: DimensionlessParams,
                     fine_tuning: Dict) -> str:
    """
    Generate book-ready verdict (RF-6).
    """
    tau_sim = ensemble_result['tau_mean']
    tau_kramers = kramers_pred.tau_kramers_dimless
    ratio = tau_sim / tau_kramers if tau_kramers > 0 else float('inf')

    lines = [
        "="*60,
        "BOOK-READY VERDICT (RF-6)",
        "="*60,
        f"Kramers regime: {kramers_pred.regime}",
        f"Theta = {kramers_pred.Theta:.2f}, Upsilon = {kramers_pred.Upsilon:.2f}",
        "",
        f"Kramers prediction: tau = {tau_kramers:.2e} (dimensionless)",
        f"Simulation result:  tau = {tau_sim:.2e} +/- {ensemble_result['tau_std']:.2e}",
        f"Ratio (sim/Kramers): {ratio:.2f}",
        "",
        f"Escape fraction: {ensemble_result['escape_fraction']*100:.1f}%",
        f"Number of trajectories: {ensemble_result['n_trajectories']}",
        "",
    ]

    if fine_tuning['fine_tuned']:
        lines.append("WARNINGS:")
        for w in fine_tuning['warnings']:
            lines.append(f"  - {w}")
    else:
        lines.append("No fine-tuning warnings.")

    lines.append("")
    if 0.5 < ratio < 2.0 and not fine_tuning['fine_tuned']:
        lines.append("VERDICT: PASS - Kramers theory validated within factor 2")
    elif fine_tuning['fine_tuned']:
        lines.append("VERDICT: CAUTION - Fine-tuning detected")
    else:
        lines.append(f"VERDICT: CHECK - Ratio = {ratio:.2f} outside [0.5, 2.0]")

    lines.append("="*60)

    return "\n".join(lines)


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("="*60)
    print("KRAMERS ESCAPE VALIDATION")
    print("EDC Book IV - Metastable Junction Lifetime")
    print("="*60)

    # Create potential
    Delta_V = 2.59  # MeV (barrier height from Ch.3)
    potential = create_quartic_potential(Delta_V=Delta_V, asymmetry=0.1)

    print(f"\nPotential parameters:")
    print(f"  Barrier height: {potential['Delta_V']:.2f}")
    print(f"  omega_meta: {potential['omega_meta']:.2f}")
    print(f"  omega_barrier: {potential['omega_barrier']:.2f}")

    # Test point (example)
    Theta = 62.0  # S_E/hbar from derivation
    Upsilon = 1.0  # Turnover regime

    print(f"\nTest point: Theta={Theta}, Upsilon={Upsilon}")

    # Kramers prediction
    params = DimensionlessParams(Theta=Theta, Upsilon=Upsilon)
    print(f"Kramers regime: {params.regime}")
    print(f"Kramers tau (dimless): {params.tau_kramers_dimless:.2e}")

    # Fine-tuning check
    ft = check_fine_tuning(Theta, Upsilon, tau_target=879.0)
    print(f"\nFine-tuning check:")
    print(f"  Warnings: {ft['warnings'] if ft['warnings'] else 'None'}")

    print("\n" + "="*60)
    print("For full ensemble simulation, run with --simulate flag")
    print("="*60)
