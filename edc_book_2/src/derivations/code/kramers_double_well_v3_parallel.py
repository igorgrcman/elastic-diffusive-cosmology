#!/usr/bin/env python3
"""
Route F v3: Kramers Escape with PARALLEL COMPUTATION

Optimized for Apple M1 Pro (multiprocessing).

Same guardrails as v2 (RF-1 through RF-6) but with:
- multiprocessing.Pool for parallel trajectory simulation
- Reduced grid for faster results
- Same scientific rigor

Author: Claude Code (Route F v3 - parallel)
Date: 2026-01-27
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Any
import json
import os
from pathlib import Path
from scipy.optimize import brentq, minimize_scalar
import multiprocessing as mp
from functools import partial
import warnings

# Number of CPU cores (M1 Pro has 8 performance + 2 efficiency)
N_CORES = min(mp.cpu_count(), 8)


# =============================================================================
# DIMENSIONLESS PARAMETERS
# =============================================================================

@dataclass
class DimensionlessParams:
    """Kramers problem in dimensionless form."""
    Theta: float      # ΔV / T_eff
    Upsilon: float    # γ / ω_b
    regime: str = field(init=False)
    tau_kramers_dimless: float = field(init=False)

    def __post_init__(self):
        if self.Upsilon < 0.1:
            self.regime = "UNDERDAMPED"
        elif self.Upsilon > 10:
            self.regime = "OVERDAMPED"
        else:
            self.regime = "TURNOVER"

        if self.Theta <= 0:
            self.tau_kramers_dimless = 0.0
            return

        if self.Upsilon > 1:
            self.tau_kramers_dimless = (2 * np.pi / self.Upsilon) * np.exp(self.Theta)
        elif self.Upsilon < 0.1:
            self.tau_kramers_dimless = (self.Theta / self.Upsilon) * np.exp(self.Theta)
        else:
            factor = np.sqrt(1 + (self.Upsilon/2)**2) - self.Upsilon/2
            self.tau_kramers_dimless = (2 * np.pi / factor) * np.exp(self.Theta)


# =============================================================================
# POTENTIAL
# =============================================================================

def create_quartic_potential(Delta_V: float = 1.0, asymmetry: float = 0.1):
    """Create quartic double-well potential."""
    V0 = Delta_V
    delta = asymmetry

    def V(x):
        return V0 * (x**4 - 2*x**2) + delta * x

    def dV(x):
        return V0 * (4*x**3 - 4*x) + delta

    def d2V(x):
        return V0 * (12*x**2 - 4)

    res_p = minimize_scalar(V, bounds=(-2, 0), method='bounded')
    x_p = res_p.x
    res_n = minimize_scalar(V, bounds=(0, 2), method='bounded')
    x_n = res_n.x

    try:
        x_b = brentq(dV, x_p + 0.01, x_n - 0.01)
    except:
        x_b = 0.0

    omega_n = np.sqrt(max(d2V(x_n), 0.01))
    omega_p = np.sqrt(max(d2V(x_p), 0.01))
    omega_b = np.sqrt(max(-d2V(x_b), 0.01))
    actual_DV = V(x_b) - V(x_n)

    return {
        'V': V, 'dV': dV, 'd2V': d2V,
        'x_n': x_n, 'x_p': x_p, 'x_b': x_b,
        'omega_n': omega_n, 'omega_p': omega_p, 'omega_b': omega_b,
        'Delta_V': actual_DV, 'V0': V0, 'delta': delta
    }


# =============================================================================
# SINGLE TRAJECTORY (for parallel execution)
# =============================================================================

def run_single_trajectory(
    args: Tuple[int, float, float, float, float, float, float, float, float]
) -> float:
    """
    Run single trajectory and return escape time.

    Args is tuple: (seed, x_n, x_b, dV_params, gamma, T_eff, omega_b, dt, t_max)
    """
    seed, x_n, x_b, V0, delta, gamma, T_eff, omega_b, dt, t_max = args

    # Recreate dV function (can't pickle lambda)
    def dV(x):
        return V0 * (4*x**3 - 4*x) + delta

    rng = np.random.default_rng(seed)

    x = x_n
    v = rng.standard_normal() * np.sqrt(T_eff)

    # BAOAB integrator coefficients
    c1 = np.exp(-gamma * dt)
    c2 = np.sqrt((1 - c1**2) * T_eff) if T_eff > 0 else 0.0

    t = 0.0

    while t < t_max:
        if x < x_b:
            return t

        # BAOAB step
        F = -dV(x)
        v = v + 0.5 * dt * F
        x = x + 0.5 * dt * v
        v = c1 * v + c2 * rng.standard_normal()
        x = x + 0.5 * dt * v
        F = -dV(x)
        v = v + 0.5 * dt * F

        t += dt

    return t_max


def run_escape_ensemble_parallel(
    potential: dict,
    Theta: float,
    Upsilon: float,
    n_trajectories: int = 1000,
    t_max_factor: float = 10.0,
    dt_factor: float = 0.01,
    base_seed: int = 42,
    n_workers: int = N_CORES
) -> Dict[str, Any]:
    """Run ensemble using parallel workers."""

    x_n = potential['x_n']
    x_b = potential['x_b']
    omega_b = potential['omega_b']
    Delta_V = potential['Delta_V']
    V0 = potential['V0']
    delta = potential['delta']

    T_eff = Delta_V / Theta if Theta > 0 else 1e-10
    gamma = Upsilon * omega_b

    dimless = DimensionlessParams(Theta=Theta, Upsilon=Upsilon)

    tau_estimate = dimless.tau_kramers_dimless / omega_b if omega_b > 0 else 1000
    t_max = min(t_max_factor * max(tau_estimate, 100), 30000)
    dt = dt_factor / omega_b if omega_b > 0 else 0.01

    # Prepare arguments for parallel execution
    args_list = [
        (base_seed + i, x_n, x_b, V0, delta, gamma, T_eff, omega_b, dt, t_max)
        for i in range(n_trajectories)
    ]

    # Run in parallel
    with mp.Pool(n_workers) as pool:
        escape_times = pool.map(run_single_trajectory, args_list)

    escape_times = np.array(escape_times)

    # Compute statistics
    escaped = escape_times[escape_times < t_max * 0.99]
    n_escaped = len(escaped)

    if n_escaped > 0:
        stats = {
            'mean': float(np.mean(escaped)),
            'std': float(np.std(escaped)),
            'median': float(np.median(escaped)),
            'p10': float(np.percentile(escaped, 10)),
            'p25': float(np.percentile(escaped, 25)),
            'p75': float(np.percentile(escaped, 75)),
            'p90': float(np.percentile(escaped, 90)),
            'p95': float(np.percentile(escaped, 95)),
            'min': float(np.min(escaped)),
            'max': float(np.max(escaped)),
        }
    else:
        stats = {k: np.inf for k in ['mean', 'std', 'median', 'p10', 'p25', 'p75', 'p90', 'p95', 'min', 'max']}

    tau_kramers = dimless.tau_kramers_dimless / omega_b if omega_b > 0 else np.inf

    return {
        'n_trajectories': n_trajectories,
        'n_escaped': n_escaped,
        'escape_fraction': n_escaped / n_trajectories,
        'tau_kramers': tau_kramers,
        'regime': dimless.regime,
        'Theta': Theta,
        'Upsilon': Upsilon,
        'T_eff': T_eff,
        'gamma': gamma,
        **stats
    }


# =============================================================================
# COMPUTE TAU MAP (PARALLEL)
# =============================================================================

def compute_tau_map_parallel(
    Theta_values: np.ndarray,
    Upsilon_values: np.ndarray,
    n_trajectories: int = 1000,
    n_workers: int = N_CORES
) -> Dict[str, Any]:
    """Compute τ(Θ, Υ) map using parallel execution."""

    potential = create_quartic_potential(Delta_V=1.0, asymmetry=0.1)

    n_Theta = len(Theta_values)
    n_Upsilon = len(Upsilon_values)

    tau_mean = np.zeros((n_Theta, n_Upsilon))
    tau_median = np.zeros((n_Theta, n_Upsilon))
    tau_p90 = np.zeros((n_Theta, n_Upsilon))
    tau_kramers = np.zeros((n_Theta, n_Upsilon))
    escape_frac = np.zeros((n_Theta, n_Upsilon))
    regimes = np.empty((n_Theta, n_Upsilon), dtype=object)

    total = n_Theta * n_Upsilon
    count = 0

    for i, Theta in enumerate(Theta_values):
        for j, Upsilon in enumerate(Upsilon_values):
            count += 1
            print(f"[{count}/{total}] Θ={Theta:.1f}, Υ={Upsilon:.2f} ... ", end='', flush=True)

            result = run_escape_ensemble_parallel(
                potential=potential,
                Theta=Theta,
                Upsilon=Upsilon,
                n_trajectories=n_trajectories,
                base_seed=42 + i * 1000 + j * 100,
                n_workers=n_workers
            )

            tau_mean[i, j] = result['mean']
            tau_median[i, j] = result['median']
            tau_p90[i, j] = result['p90']
            tau_kramers[i, j] = result['tau_kramers']
            escape_frac[i, j] = result['escape_fraction']
            regimes[i, j] = result['regime']

            print(f"τ={result['mean']:.1f}, esc={result['escape_fraction']:.0%}, {result['regime']}")

    return {
        'Theta_values': Theta_values,
        'Upsilon_values': Upsilon_values,
        'tau_mean': tau_mean,
        'tau_median': tau_median,
        'tau_p90': tau_p90,
        'tau_kramers': tau_kramers,
        'escape_fraction': escape_frac,
        'regimes': regimes,
        'potential': {
            'omega_b': potential['omega_b'],
            'omega_n': potential['omega_n'],
            'Delta_V': potential['Delta_V']
        }
    }


# =============================================================================
# FINE-TUNING CHECK
# =============================================================================

def check_fine_tuning(Theta: float, Upsilon: float) -> Dict[str, Any]:
    """Check if parameters require fine-tuning (RF-5)."""
    warnings_list = []
    level = "NATURAL"

    if Theta < 1:
        warnings_list.append(f"Θ={Theta:.2f} < 1: noise dominates")
        level = "UNPHYSICAL"
    elif Theta > 60:
        warnings_list.append(f"Θ={Theta:.2f} > 60: extreme suppression")
        level = "FINE-TUNED"
    elif Theta > 30:
        warnings_list.append(f"Θ={Theta:.2f} > 30: borderline")
        level = "BORDERLINE"

    if Upsilon < 0.01:
        warnings_list.append(f"Υ={Upsilon:.3f} < 0.01: extreme underdamping")
        level = "FINE-TUNED"
    elif Upsilon > 100:
        warnings_list.append(f"Υ={Upsilon:.1f} > 100: extreme overdamping")
        level = "FINE-TUNED"

    return {
        'Theta': Theta,
        'Upsilon': Upsilon,
        'fine_tuning_level': level,
        'warnings': warnings_list
    }


def find_879s_contour(tau_map: Dict, tau_target: float = 879.0, tolerance: float = 0.5):
    """Find where τ = 879s on the map."""
    Theta_vals = tau_map['Theta_values']
    Upsilon_vals = tau_map['Upsilon_values']
    tau_mean = tau_map['tau_mean']

    log_tau = np.log10(np.maximum(tau_mean, 1e-10))
    log_target = np.log10(tau_target)

    matches = []

    for i, Theta in enumerate(Theta_vals):
        for j, Upsilon in enumerate(Upsilon_vals):
            if abs(log_tau[i, j] - log_target) < tolerance:
                ft = check_fine_tuning(Theta, Upsilon)
                matches.append({
                    'Theta': float(Theta),
                    'Upsilon': float(Upsilon),
                    'tau_measured': float(tau_mean[i, j]),
                    'log_tau_error': float(abs(log_tau[i, j] - log_target)),
                    'fine_tuning': ft['fine_tuning_level'],
                    'regime': str(tau_map['regimes'][i, j]),
                    'warnings': ft['warnings']
                })

    matches.sort(key=lambda x: x['log_tau_error'])

    if not matches:
        verdict = "NO-GO: τ=879s not achievable in scanned range"
    else:
        best = matches[0]
        if best['fine_tuning'] == 'NATURAL':
            verdict = f"VIABLE: τ=879s at Θ={best['Theta']:.1f}, Υ={best['Upsilon']:.2f} (NATURAL)"
        elif best['fine_tuning'] == 'BORDERLINE':
            verdict = f"MARGINAL: τ=879s at Θ={best['Theta']:.1f}, Υ={best['Upsilon']:.2f} (borderline)"
        else:
            verdict = f"FINE-TUNED: τ=879s requires extreme parameters"

    return {
        'tau_target': tau_target,
        'matches': matches,
        'n_matches': len(matches),
        'verdict': verdict,
        'best_match': matches[0] if matches else None
    }


# =============================================================================
# VISUALIZATION
# =============================================================================

def plot_tau_map(tau_map: Dict, contour_879: Dict, save_path: str):
    """Plot 2D map τ(Θ, Υ) with 879s contour."""
    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm

    Theta = tau_map['Theta_values']
    Upsilon = tau_map['Upsilon_values']
    tau = tau_map['tau_mean']

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: τ map
    ax1 = axes[0]
    Th_grid, Up_grid = np.meshgrid(Theta, Upsilon, indexing='ij')

    tau_plot = np.clip(tau, 1, 1e6)
    tau_plot = np.where(np.isinf(tau_plot), 1e6, tau_plot)

    im = ax1.pcolormesh(Th_grid, Up_grid, tau_plot,
                        norm=LogNorm(vmin=1, vmax=1e6),
                        cmap='viridis', shading='auto')
    plt.colorbar(im, ax=ax1, label='τ (escape time)')

    # 879s contour
    ax1.contour(Th_grid, Up_grid, tau_plot, levels=[879], colors='red', linewidths=2)

    # Mark matches
    for m in contour_879['matches'][:5]:
        marker = 'o' if m['fine_tuning'] == 'NATURAL' else 's'
        color = 'lime' if m['fine_tuning'] == 'NATURAL' else 'orange'
        ax1.scatter(m['Theta'], m['Upsilon'], c=color, s=100, marker=marker,
                   edgecolors='black', linewidths=2, zorder=10)

    ax1.axhline(0.1, color='white', linestyle='--', alpha=0.5)
    ax1.axhline(10, color='white', linestyle='--', alpha=0.5)

    ax1.set_xlabel('Θ = ΔV / T_eff', fontsize=12)
    ax1.set_ylabel('Υ = γ / ω_b', fontsize=12)
    ax1.set_yscale('log')
    ax1.set_title('Escape Time Map τ(Θ, Υ)\nRed contour: τ = 879', fontsize=12)

    # Right: τ vs Θ for fixed Υ
    ax2 = axes[1]
    for Up_target, color in [(0.1, 'blue'), (1.0, 'green'), (10.0, 'orange')]:
        j = np.argmin(np.abs(Upsilon - Up_target))
        ax2.semilogy(Theta, tau[:, j], 'o-', color=color, label=f'Υ = {Upsilon[j]:.1f}')
        ax2.semilogy(Theta, tau_map['tau_kramers'][:, j], '--', color=color, alpha=0.5)

    ax2.axhline(879, color='red', linestyle='-', linewidth=2, label='τ = 879s')
    ax2.set_xlabel('Θ = ΔV / T_eff', fontsize=12)
    ax2.set_ylabel('τ (escape time)', fontsize=12)
    ax2.set_title('Escape Time vs Barrier Height', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"Saved: {save_path}")
    plt.close()


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run Route F v3 with parallel computation."""
    print("="*70)
    print("ROUTE F v3: PARALLEL KRAMERS ANALYSIS")
    print(f"Using {N_CORES} CPU cores")
    print("="*70)

    base_dir = Path(__file__).parent.parent
    artifacts_dir = base_dir / "artifacts"
    figures_dir = base_dir / "figures"
    artifacts_dir.mkdir(exist_ok=True)
    figures_dir.mkdir(exist_ok=True)

    # Grid (RF-2)
    Theta_values = np.array([3, 5, 6, 7, 8, 9, 10, 12, 15])
    Upsilon_values = np.array([0.1, 0.3, 1.0, 3.0, 10.0])

    n_trajectories = 1000

    print(f"\nGrid: {len(Theta_values)} × {len(Upsilon_values)} = {len(Theta_values)*len(Upsilon_values)} points")
    print(f"Trajectories: {n_trajectories}")
    print(f"Θ: {Theta_values}")
    print(f"Υ: {Upsilon_values}")

    # Compute map
    print("\n" + "="*60)
    print("Computing τ(Θ, Υ) map...")
    print("="*60 + "\n")

    tau_map = compute_tau_map_parallel(
        Theta_values=Theta_values,
        Upsilon_values=Upsilon_values,
        n_trajectories=n_trajectories,
        n_workers=N_CORES
    )

    # Find 879s
    print("\n" + "="*60)
    print("Finding τ = 879s contour...")
    print("="*60)

    contour_879 = find_879s_contour(tau_map, tau_target=879.0, tolerance=0.5)

    print(f"\nVERDICT: {contour_879['verdict']}")
    print(f"Matches: {contour_879['n_matches']}")

    if contour_879['best_match']:
        best = contour_879['best_match']
        print(f"\nBest match:")
        print(f"  Θ = {best['Theta']:.1f}")
        print(f"  Υ = {best['Upsilon']:.2f}")
        print(f"  τ = {best['tau_measured']:.1f}")
        print(f"  Regime: {best['regime']}")
        print(f"  Fine-tuning: {best['fine_tuning']}")

    # Plot
    plot_tau_map(tau_map, contour_879, str(figures_dir / "kramers_v3_tau_map.png"))

    # RF-6: Book verdict
    print("\n" + "="*70)
    print("RF-6: BOOK-READY VERDICT")
    print("="*70)

    if contour_879['best_match']:
        best = contour_879['best_match']
        Delta_m_np = 1.293  # MeV

        verdict = f"""
ROUTE F VERDICT: {contour_879['verdict'].split(':')[0]}

τ = 879s achieved at:
  Θ = ΔV/T_eff = {best['Theta']:.1f}
  Υ = γ/ω_b = {best['Upsilon']:.2f}  ({best['regime']} regime)

PHYSICAL INTERPRETATION:
  If ΔV = Δm_np c² = 1.293 MeV:
    T_eff = ΔV/Θ = {Delta_m_np/best['Theta']:.3f} MeV
          = {Delta_m_np/best['Theta']/0.511:.2f} × m_e c²

FINE-TUNING STATUS: {best['fine_tuning']}
{' '.join(best['warnings']) if best['warnings'] else 'No warnings.'}

CONSTRAINT ON M5 COUPLING:
  The effective noise scale T_eff ~ {Delta_m_np/best['Theta']:.2f} MeV
  implies specific coupling strength to M5 vacuum fluctuations.
"""
    else:
        verdict = """
ROUTE F VERDICT: NO-GO

τ = 879s NOT achievable in natural parameter range.
"""

    print(verdict)

    # Save results
    results = {
        'tau_map': {
            'Theta_values': Theta_values.tolist(),
            'Upsilon_values': Upsilon_values.tolist(),
            'tau_mean': tau_map['tau_mean'].tolist(),
            'tau_median': tau_map['tau_median'].tolist(),
            'escape_fraction': tau_map['escape_fraction'].tolist(),
            'regimes': [[str(r) for r in row] for row in tau_map['regimes']],
        },
        'contour_879': {
            'verdict': contour_879['verdict'],
            'n_matches': contour_879['n_matches'],
            'best_match': contour_879['best_match'],
            'matches': contour_879['matches']
        },
        'verdict_text': verdict
    }

    json_path = artifacts_dir / "kramers_v3_results.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {json_path}")

    print("\n" + "="*70)
    print("Route F v3 complete.")
    print("="*70)


if __name__ == "__main__":
    main()
