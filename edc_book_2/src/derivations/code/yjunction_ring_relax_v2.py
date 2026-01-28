#!/usr/bin/env python3
"""
Y-Junction + Ring Coupled Oscillator Model: STRICT Relaxation Study (v2)

STRICT CRITERION (b): Simultaneous settling of node AND ring

Three metrics must ALL satisfy thresholds continuously for T_hold:
  1. q(t) = ||r_0(t) - r_0,eq||  →  q_RMS < ε_q = η_q * L0
  2. D(t) = ring distortion      →  D_RMS < ε_D = η_D
  3. V_ring(t)                   →  V_ring_RMS - V_ring_min < ε_V = η_V * (V0 - Vmin)

This prevents "false settling" where q looks quiet but energy circulates in ring.

Author: EDC Research
Date: 2026-01-27
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh
import json
import csv
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import List, Tuple, Dict, Optional
import warnings

# =============================================================================
# MODEL DEFINITION [Def]
# =============================================================================

@dataclass
class ModelParams:
    """Parameters for the Y-junction + ring model."""
    L0: float = 1.0
    L_ring: float = 1.732  # sqrt(3) for equilateral
    m0: float = 1.0
    m_out: float = 1.0
    k_leg: float = 1.0
    k_ring: float = 1.0
    gamma_0: float = 0.0
    gamma_out: float = 0.0


@dataclass
class StrictCriterion:
    """Threshold parameters for strict (b) criterion."""
    eta_q: float = 1e-3      # q threshold relative to L0
    eta_D: float = 1e-3      # distortion threshold (dimensionless)
    eta_V: float = 1e-3      # V_ring threshold relative to (V0 - Vmin)
    T_hold_periods: int = 10 # Number of slowest-mode periods to hold
    window_periods: int = 2  # RMS window in slowest-mode periods


def compute_equilibrium_positions(params: ModelParams) -> np.ndarray:
    """Equilibrium: central node at origin, outer nodes at 120° intervals."""
    r0 = np.array([0.0, 0.0])
    angles = np.array([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3])
    r1 = params.L0 * np.array([np.cos(angles[0]), np.sin(angles[0])])
    r2 = params.L0 * np.array([np.cos(angles[1]), np.sin(angles[1])])
    r3 = params.L0 * np.array([np.cos(angles[2]), np.sin(angles[2])])
    return np.array([r0, r1, r2, r3])


def compute_potential_energy(positions: np.ndarray, params: ModelParams) -> Tuple[float, float, float]:
    """V = V_legs + V_ring. Returns (V_total, V_legs, V_ring)."""
    r0, r1, r2, r3 = positions

    V_legs = 0.0
    for ri in [r1, r2, r3]:
        d = np.linalg.norm(ri - r0)
        V_legs += 0.5 * params.k_leg * (d - params.L0)**2

    V_ring = 0.0
    for ri, rj in [(r1, r2), (r2, r3), (r3, r1)]:
        d = np.linalg.norm(rj - ri)
        V_ring += 0.5 * params.k_ring * (d - params.L_ring)**2

    return V_legs + V_ring, V_legs, V_ring


def compute_kinetic_energy(velocities: np.ndarray, params: ModelParams) -> float:
    v0, v1, v2, v3 = velocities
    T = 0.5 * params.m0 * np.dot(v0, v0)
    for vi in [v1, v2, v3]:
        T += 0.5 * params.m_out * np.dot(vi, vi)
    return T


def compute_forces(positions: np.ndarray, params: ModelParams) -> np.ndarray:
    """F_i = -dV/dr_i"""
    r0, r1, r2, r3 = positions
    forces = np.zeros((4, 2))

    # Leg forces
    for i, ri in enumerate([r1, r2, r3], start=1):
        d_vec = ri - r0
        d = np.linalg.norm(d_vec)
        if d > 1e-10:
            unit = d_vec / d
            F_mag = -params.k_leg * (d - params.L0)
            forces[i] += F_mag * unit
            forces[0] -= F_mag * unit

    # Ring forces
    for i, j in [(1, 2), (2, 3), (3, 1)]:
        ri, rj = positions[i], positions[j]
        d_vec = rj - ri
        d = np.linalg.norm(d_vec)
        if d > 1e-10:
            unit = d_vec / d
            F_mag = -params.k_ring * (d - params.L_ring)
            forces[j] += F_mag * unit
            forces[i] -= F_mag * unit

    return forces


def compute_damping_forces(velocities: np.ndarray, params: ModelParams) -> np.ndarray:
    """F_damp = -gamma * v"""
    forces = np.zeros((4, 2))
    forces[0] = -params.gamma_0 * velocities[0]
    for i in [1, 2, 3]:
        forces[i] = -params.gamma_out * velocities[i]
    return forces


# =============================================================================
# THREE METRICS FOR STRICT CRITERION (b)
# =============================================================================

def compute_q_metric(positions: np.ndarray, eq_pos: np.ndarray) -> float:
    """Metric 1: q = ||r_0 - r_0,eq||"""
    return np.linalg.norm(positions[0] - eq_pos[0])


def compute_distortion_D(positions: np.ndarray) -> float:
    """
    Metric 2: Ring distortion (departure from equilateral).
    D = sqrt( sum_i (s_i - s_bar)^2 / s_bar^2 ) / sqrt(3)
    """
    r1, r2, r3 = positions[1], positions[2], positions[3]
    s12 = np.linalg.norm(r2 - r1)
    s23 = np.linalg.norm(r3 - r2)
    s31 = np.linalg.norm(r1 - r3)
    s_bar = (s12 + s23 + s31) / 3.0

    if s_bar < 1e-10:
        return 0.0

    D = np.sqrt(((s12 - s_bar)**2 + (s23 - s_bar)**2 + (s31 - s_bar)**2) / s_bar**2)
    return D


def compute_V_ring_metric(positions: np.ndarray, params: ModelParams) -> float:
    """Metric 3: V_ring (ring spring potential energy)."""
    _, _, V_ring = compute_potential_energy(positions, params)
    return V_ring


def compute_all_metrics(y: np.ndarray, params: ModelParams, eq_pos: np.ndarray) -> Dict:
    """Compute all three metrics plus auxiliary quantities."""
    positions = y[:8].reshape(4, 2)
    velocities = y[8:].reshape(4, 2)

    V_total, V_legs, V_ring = compute_potential_energy(positions, params)
    T = compute_kinetic_energy(velocities, params)

    q = compute_q_metric(positions, eq_pos)
    D = compute_distortion_D(positions)

    return {
        'q': q,
        'D': D,
        'V_ring': V_ring,
        'V_total': V_total,
        'V_legs': V_legs,
        'T': T,
        'E_total': T + V_total
    }


# =============================================================================
# NORMAL MODE ANALYSIS
# =============================================================================

def compute_hessian(params: ModelParams, eq_pos: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """Hessian d^2V/dr_i dr_j at equilibrium via finite differences."""
    n = 8
    H = np.zeros((n, n))

    def V_func(pos_flat):
        pos = pos_flat.reshape(4, 2)
        V, _, _ = compute_potential_energy(pos, params)
        return V

    pos0 = eq_pos.flatten()

    for i in range(n):
        for j in range(i, n):
            pos_pp = pos0.copy(); pos_pp[i] += eps; pos_pp[j] += eps
            pos_pm = pos0.copy(); pos_pm[i] += eps; pos_pm[j] -= eps
            pos_mp = pos0.copy(); pos_mp[i] -= eps; pos_mp[j] += eps
            pos_mm = pos0.copy(); pos_mm[i] -= eps; pos_mm[j] -= eps

            H[i, j] = (V_func(pos_pp) - V_func(pos_pm) - V_func(pos_mp) + V_func(pos_mm)) / (4 * eps**2)
            H[j, i] = H[i, j]

    return H


def compute_normal_modes(params: ModelParams) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Compute normal mode frequencies.
    Returns: (frequencies, eigenvectors, omega_min)
    where omega_min is the smallest nonzero frequency (slowest physical mode).
    """
    eq_pos = compute_equilibrium_positions(params)
    H = compute_hessian(params, eq_pos)

    masses = np.array([params.m0, params.m0, params.m_out, params.m_out,
                       params.m_out, params.m_out, params.m_out, params.m_out])
    M_inv_sqrt = np.diag(1.0 / np.sqrt(masses))
    H_tilde = M_inv_sqrt @ H @ M_inv_sqrt

    eigenvalues, eigenvectors = eigh(H_tilde)

    frequencies = np.zeros(8)
    for i, ev in enumerate(eigenvalues):
        if ev > 1e-10:
            frequencies[i] = np.sqrt(ev)

    # Slowest physical mode (exclude zero modes: translation, rotation)
    # Threshold: anything below 0.01 is considered a zero mode (CM motion)
    physical_freqs = frequencies[frequencies > 0.1]
    omega_min = np.min(physical_freqs) if len(physical_freqs) > 0 else 1.0

    return frequencies, eigenvectors, omega_min


# =============================================================================
# INITIAL CONDITIONS
# =============================================================================

def create_initial_conditions(
    params: ModelParams,
    ic_type: str = "symmetric_push",
    amplitude: float = 0.3
) -> np.ndarray:
    """
    IC-1 "symmetric_push": Central node pushed along +y
    IC-2 "doublet": r1 pushed radially outward
    IC-3 "ring_mode": Outer nodes displaced tangentially (circulation)
    """
    eq_pos = compute_equilibrium_positions(params)
    positions = eq_pos.copy()
    velocities = np.zeros((4, 2))

    if ic_type == "symmetric_push":
        positions[0, 1] += amplitude

    elif ic_type == "doublet":
        r0, r1 = positions[0], positions[1]
        direction = r1 - r0
        direction = direction / np.linalg.norm(direction)
        positions[1] += amplitude * direction

    elif ic_type == "ring_mode":
        for i in [1, 2, 3]:
            r0, ri = positions[0], positions[i]
            radial = ri - r0
            radial = radial / np.linalg.norm(radial)
            tangent = np.array([-radial[1], radial[0]])
            positions[i] += amplitude * tangent

    else:
        raise ValueError(f"Unknown IC type: {ic_type}")

    y0 = np.zeros(16)
    y0[:8] = positions.flatten()
    y0[8:] = velocities.flatten()
    return y0


# =============================================================================
# SIMULATION
# =============================================================================

def equations_of_motion(t, y, params: ModelParams):
    """dy/dt for the system."""
    positions = y[:8].reshape(4, 2)
    velocities = y[8:].reshape(4, 2)

    forces = compute_forces(positions, params)
    if params.gamma_0 > 0 or params.gamma_out > 0:
        forces += compute_damping_forces(velocities, params)

    masses = np.array([params.m0, params.m0, params.m_out, params.m_out,
                       params.m_out, params.m_out, params.m_out, params.m_out])
    accelerations = forces.flatten() / masses

    dydt = np.zeros(16)
    dydt[:8] = velocities.flatten()
    dydt[8:] = accelerations
    return dydt


@dataclass
class StrictRelaxationResult:
    """Results with strict three-metric criterion."""
    params_dict: dict
    ic_type: str
    gamma: float

    # Normal modes
    frequencies: List[float] = field(default_factory=list)
    omega_min: float = 0.0
    T_slowest: float = 0.0  # Period of slowest mode

    # Initial/equilibrium values
    E_initial: float = 0.0
    V_ring_min: float = 0.0

    # Thresholds (computed)
    eps_q: float = 0.0
    eps_D: float = 0.0
    eps_V: float = 0.0

    # Relaxation times (None if not achieved)
    t_relax_q: Optional[float] = None      # Time when q criterion first met
    t_relax_D: Optional[float] = None      # Time when D criterion first met
    t_relax_V: Optional[float] = None      # Time when V_ring criterion first met
    t_relax_strict: Optional[float] = None # Time when ALL THREE met for T_hold

    # Flags for "cheating" detection
    q_passed_alone: bool = False           # q passed but D or V didn't
    D_passed_alone: bool = False
    V_passed_alone: bool = False

    # Time series (sampled)
    t_series: List[float] = field(default_factory=list)
    q_series: List[float] = field(default_factory=list)
    D_series: List[float] = field(default_factory=list)
    V_ring_series: List[float] = field(default_factory=list)
    E_series: List[float] = field(default_factory=list)

    # Status
    status: str = "UNKNOWN"  # RELAXED_STRICT, RELAXED_PARTIAL, NO_RELAX, CONSERVATIVE


def compute_running_rms(series: np.ndarray, window_size: int) -> np.ndarray:
    """Compute running RMS with given window size."""
    if window_size < 1:
        window_size = 1
    n = len(series)
    rms = np.zeros(n)
    for i in range(n):
        start = max(0, i - window_size + 1)
        rms[i] = np.sqrt(np.mean(series[start:i+1]**2))
    return rms


def run_strict_simulation(
    params: ModelParams,
    criterion: StrictCriterion,
    ic_type: str = "symmetric_push",
    amplitude: float = 0.3,
    t_max: float = 1000.0,
    dt_sample: float = 0.1
) -> StrictRelaxationResult:
    """
    Run simulation with strict three-metric criterion.
    """
    # Setup
    eq_pos = compute_equilibrium_positions(params)
    frequencies, _, omega_min = compute_normal_modes(params)
    T_slowest = 2 * np.pi / omega_min if omega_min > 0 else 10.0

    # Compute equilibrium V_ring
    _, _, V_ring_eq = compute_potential_energy(eq_pos, params)

    # Initial conditions
    y0 = create_initial_conditions(params, ic_type, amplitude)
    initial_metrics = compute_all_metrics(y0, params, eq_pos)
    E_initial = initial_metrics['E_total']
    V_ring_initial = initial_metrics['V_ring']

    # Compute thresholds
    eps_q = criterion.eta_q * params.L0
    eps_D = criterion.eta_D
    eps_V = criterion.eta_V * max(V_ring_initial - V_ring_eq, 1e-10)

    # Time parameters
    window_time = criterion.window_periods * T_slowest
    T_hold = criterion.T_hold_periods * T_slowest
    window_samples = max(int(window_time / dt_sample), 1)
    hold_samples = max(int(T_hold / dt_sample), 1)

    # Run simulation
    t_span = (0.0, t_max)
    t_eval = np.arange(0, t_max, dt_sample)

    sol = solve_ivp(
        lambda t, y: equations_of_motion(t, y, params),
        t_span,
        y0,
        method='RK45',
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10
    )

    # Extract time series
    t_series = sol.t
    n_points = len(t_series)

    q_series = np.zeros(n_points)
    D_series = np.zeros(n_points)
    V_ring_series = np.zeros(n_points)
    E_series = np.zeros(n_points)

    for i, yi in enumerate(sol.y.T):
        metrics = compute_all_metrics(yi, params, eq_pos)
        q_series[i] = metrics['q']
        D_series[i] = metrics['D']
        V_ring_series[i] = metrics['V_ring']
        E_series[i] = metrics['E_total']

    # Compute running RMS
    q_rms = compute_running_rms(q_series, window_samples)
    D_rms = compute_running_rms(D_series, window_samples)
    V_ring_rms = compute_running_rms(V_ring_series - V_ring_eq, window_samples)

    # Check criteria
    q_pass = q_rms < eps_q
    D_pass = D_rms < eps_D
    V_pass = V_ring_rms < eps_V
    all_pass = q_pass & D_pass & V_pass

    # Find first time each criterion is met
    t_relax_q = t_series[np.argmax(q_pass)] if np.any(q_pass) else None
    t_relax_D = t_series[np.argmax(D_pass)] if np.any(D_pass) else None
    t_relax_V = t_series[np.argmax(V_pass)] if np.any(V_pass) else None

    # Find strict relaxation: all three for T_hold consecutive samples
    t_relax_strict = None
    consecutive = 0
    for i in range(n_points):
        if all_pass[i]:
            consecutive += 1
            if consecutive >= hold_samples:
                t_relax_strict = t_series[i - hold_samples + 1]
                break
        else:
            consecutive = 0

    # Detect "cheating" (partial passing)
    q_passed_alone = np.any(q_pass & ~D_pass) or np.any(q_pass & ~V_pass)
    D_passed_alone = np.any(D_pass & ~q_pass) or np.any(D_pass & ~V_pass)
    V_passed_alone = np.any(V_pass & ~q_pass) or np.any(V_pass & ~D_pass)

    # Determine status
    gamma = params.gamma_0 + params.gamma_out
    if gamma == 0:
        status = "CONSERVATIVE"
    elif t_relax_strict is not None:
        status = "RELAXED_STRICT"
    elif t_relax_q is not None or t_relax_D is not None or t_relax_V is not None:
        status = "RELAXED_PARTIAL"
    else:
        status = "NO_RELAX"

    return StrictRelaxationResult(
        params_dict=asdict(params),
        ic_type=ic_type,
        gamma=gamma,
        frequencies=frequencies.tolist(),
        omega_min=omega_min,
        T_slowest=T_slowest,
        E_initial=E_initial,
        V_ring_min=V_ring_eq,
        eps_q=eps_q,
        eps_D=eps_D,
        eps_V=eps_V,
        t_relax_q=t_relax_q,
        t_relax_D=t_relax_D,
        t_relax_V=t_relax_V,
        t_relax_strict=t_relax_strict,
        q_passed_alone=q_passed_alone,
        D_passed_alone=D_passed_alone,
        V_passed_alone=V_passed_alone,
        t_series=t_series.tolist(),
        q_series=q_series.tolist(),
        D_series=D_series.tolist(),
        V_ring_series=V_ring_series.tolist(),
        E_series=E_series.tolist(),
        status=status
    )


# =============================================================================
# PARAMETER SCAN
# =============================================================================

def run_parameter_scan(
    criterion: StrictCriterion,
    k_ratios: List[float] = [0.1, 0.3, 1.0, 3.0, 10.0],
    m_ratios: List[float] = [0.3, 1.0, 3.0],
    gammas: List[float] = [0.0, 0.001, 0.01, 0.1],
    ic_types: List[str] = ["symmetric_push", "doublet", "ring_mode"],
    t_max: float = 1000.0
) -> List[StrictRelaxationResult]:
    """Run parameter scan with strict criterion."""
    results = []
    total = len(k_ratios) * len(m_ratios) * len(gammas) * len(ic_types)
    count = 0

    for k_ratio in k_ratios:
        for m_ratio in m_ratios:
            for gamma in gammas:
                for ic_type in ic_types:
                    count += 1
                    print(f"[{count}/{total}] k_ring/k_leg={k_ratio}, m0/m_out={m_ratio}, "
                          f"gamma={gamma}, IC={ic_type}")

                    params = ModelParams(
                        k_ring=k_ratio,
                        k_leg=1.0,
                        m0=m_ratio,
                        m_out=1.0,
                        gamma_0=gamma,
                        gamma_out=gamma
                    )

                    try:
                        result = run_strict_simulation(
                            params, criterion, ic_type,
                            amplitude=0.3, t_max=t_max
                        )
                        results.append(result)
                    except Exception as e:
                        print(f"  ERROR: {e}")

    return results


# =============================================================================
# REPORTING
# =============================================================================

def generate_summary_table(results: List[StrictRelaxationResult]) -> str:
    """Generate summary table."""
    lines = []
    lines.append("=" * 120)
    lines.append("Y-JUNCTION + RING: STRICT RELAXATION SUMMARY (v2)")
    lines.append("=" * 120)
    lines.append("")

    # Statistics
    total = len(results)
    conservative = sum(1 for r in results if r.status == "CONSERVATIVE")
    strict = sum(1 for r in results if r.status == "RELAXED_STRICT")
    partial = sum(1 for r in results if r.status == "RELAXED_PARTIAL")
    no_relax = sum(1 for r in results if r.status == "NO_RELAX")

    lines.append(f"Total runs: {total}")
    lines.append(f"  CONSERVATIVE (gamma=0):  {conservative}")
    lines.append(f"  RELAXED_STRICT:          {strict}")
    lines.append(f"  RELAXED_PARTIAL:         {partial}")
    lines.append(f"  NO_RELAX:                {no_relax}")
    lines.append("")

    # Cheating detection
    cheating_q = sum(1 for r in results if r.q_passed_alone)
    cheating_D = sum(1 for r in results if r.D_passed_alone)
    cheating_V = sum(1 for r in results if r.V_passed_alone)

    lines.append("'Cheating' cases (one metric passes, others don't):")
    lines.append(f"  q passed alone: {cheating_q}")
    lines.append(f"  D passed alone: {cheating_D}")
    lines.append(f"  V_ring passed alone: {cheating_V}")
    lines.append("")

    # Normal mode frequencies
    lines.append("Normal mode frequencies (sample, k_ring/k_leg=1, m0/m_out=1):")
    for r in results:
        if r.params_dict['k_ring'] == 1.0 and r.params_dict['m0'] == 1.0 and r.gamma == 0:
            freqs = sorted([f for f in r.frequencies if f > 1e-6])
            lines.append(f"  omega = {freqs}")
            lines.append(f"  omega_min = {r.omega_min:.4f}, T_slowest = {r.T_slowest:.2f}")
            break
    lines.append("")

    # Detailed table header
    lines.append("-" * 120)
    lines.append(f"{'k_r/k_l':>8} {'m0/m_o':>7} {'gamma':>8} {'IC':>15} {'status':>15} "
                 f"{'t_strict':>10} {'t_q':>8} {'t_D':>8} {'t_V':>8} {'cheat':>8}")
    lines.append("-" * 120)

    for r in results:
        k_ratio = r.params_dict['k_ring'] / r.params_dict['k_leg']
        m_ratio = r.params_dict['m0'] / r.params_dict['m_out']

        t_strict = f"{r.t_relax_strict:.1f}" if r.t_relax_strict else "N/A"
        t_q = f"{r.t_relax_q:.1f}" if r.t_relax_q else "N/A"
        t_D = f"{r.t_relax_D:.1f}" if r.t_relax_D else "N/A"
        t_V = f"{r.t_relax_V:.1f}" if r.t_relax_V else "N/A"

        cheat = ""
        if r.q_passed_alone:
            cheat += "q"
        if r.D_passed_alone:
            cheat += "D"
        if r.V_passed_alone:
            cheat += "V"
        if not cheat:
            cheat = "-"

        lines.append(f"{k_ratio:>8.2f} {m_ratio:>7.2f} {r.gamma:>8.4f} {r.ic_type:>15} "
                     f"{r.status:>15} {t_strict:>10} {t_q:>8} {t_D:>8} {t_V:>8} {cheat:>8}")

    lines.append("-" * 120)

    return "\n".join(lines)


def save_results(results: List[StrictRelaxationResult], output_dir: Path):
    """Save results to files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # JSON (full results, but trim time series)
    json_results = []
    for r in results:
        d = asdict(r)
        # Keep only first/last 10 points of time series to reduce file size
        for key in ['t_series', 'q_series', 'D_series', 'V_ring_series', 'E_series']:
            if len(d[key]) > 20:
                d[key] = d[key][:10] + d[key][-10:]
        # Convert numpy bools to Python bools
        for key in ['q_passed_alone', 'D_passed_alone', 'V_passed_alone']:
            d[key] = bool(d[key])
        json_results.append(d)

    with open(output_dir / "strict_relax_results.json", 'w') as f:
        json.dump(json_results, f, indent=2)

    # CSV summary
    with open(output_dir / "strict_relax_summary.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k_ring/k_leg', 'm0/m_out', 'gamma', 'ic_type',
                         'status', 't_relax_strict', 't_relax_q', 't_relax_D', 't_relax_V',
                         'omega_min', 'T_slowest', 'cheat_q', 'cheat_D', 'cheat_V'])

        for r in results:
            k_ratio = r.params_dict['k_ring'] / r.params_dict['k_leg']
            m_ratio = r.params_dict['m0'] / r.params_dict['m_out']
            writer.writerow([
                f"{k_ratio:.2f}", f"{m_ratio:.2f}", f"{r.gamma:.4f}", r.ic_type,
                r.status,
                f"{r.t_relax_strict:.1f}" if r.t_relax_strict else "N/A",
                f"{r.t_relax_q:.1f}" if r.t_relax_q else "N/A",
                f"{r.t_relax_D:.1f}" if r.t_relax_D else "N/A",
                f"{r.t_relax_V:.1f}" if r.t_relax_V else "N/A",
                f"{r.omega_min:.4f}", f"{r.T_slowest:.2f}",
                r.q_passed_alone, r.D_passed_alone, r.V_passed_alone
            ])

    # Summary report
    summary = generate_summary_table(results)
    with open(output_dir / "strict_relax_report.txt", 'w') as f:
        f.write(summary)

    print(f"\nResults saved to {output_dir}")


# =============================================================================
# PLOTTING
# =============================================================================

def plot_results(results: List[StrictRelaxationResult], output_dir: Path):
    """Generate diagnostic plots."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available, skipping plots")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. t_relax_strict vs gamma (for runs that achieved strict relaxation)
    fig, ax = plt.subplots(figsize=(10, 6))

    for ic_type in ["symmetric_push", "doublet", "ring_mode"]:
        gammas = []
        t_relax = []
        for r in results:
            if r.ic_type == ic_type and r.t_relax_strict is not None and r.gamma > 0:
                gammas.append(r.gamma)
                t_relax.append(r.t_relax_strict)

        if gammas:
            ax.scatter(gammas, t_relax, label=ic_type, s=50, alpha=0.7)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Damping coefficient γ')
    ax.set_ylabel('Strict relaxation time t_relax')
    ax.set_title('Strict Relaxation Time vs Damping')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "strict_trelax_vs_gamma.png", dpi=150)
    plt.close()

    # 2. Sample time series for different statuses
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Find representative runs
    rep_runs = {}
    for status in ["CONSERVATIVE", "RELAXED_STRICT", "RELAXED_PARTIAL", "NO_RELAX"]:
        for r in results:
            if r.status == status:
                rep_runs[status] = r
                break

    for ax, (status, r) in zip(axes.flat, rep_runs.items()):
        if r is None:
            continue

        t = np.array(r.t_series)
        ax.plot(t, r.q_series, 'b-', label='q', alpha=0.7)
        ax.plot(t, r.D_series, 'r-', label='D', alpha=0.7)
        ax.plot(t, np.array(r.V_ring_series) - r.V_ring_min, 'g-', label='V_ring - V_min', alpha=0.7)

        # Thresholds
        ax.axhline(r.eps_q, color='b', linestyle='--', alpha=0.3)
        ax.axhline(r.eps_D, color='r', linestyle='--', alpha=0.3)
        ax.axhline(r.eps_V, color='g', linestyle='--', alpha=0.3)

        ax.set_xlabel('Time')
        ax.set_ylabel('Metric value')
        ax.set_title(f"{status}\nIC={r.ic_type}, γ={r.gamma}")
        ax.legend(loc='upper right')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "strict_sample_timeseries.png", dpi=150)
    plt.close()

    # 3. Cheating detection histogram
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = ['q alone', 'D alone', 'V alone', 'None (clean)']
    counts = [
        sum(1 for r in results if r.q_passed_alone and not r.D_passed_alone and not r.V_passed_alone),
        sum(1 for r in results if r.D_passed_alone and not r.q_passed_alone and not r.V_passed_alone),
        sum(1 for r in results if r.V_passed_alone and not r.q_passed_alone and not r.D_passed_alone),
        sum(1 for r in results if not r.q_passed_alone and not r.D_passed_alone and not r.V_passed_alone)
    ]

    bars = ax.bar(categories, counts, color=['blue', 'red', 'green', 'gray'])
    ax.set_ylabel('Number of runs')
    ax.set_title('"Cheating" Detection: Partial Criterion Satisfaction')

    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(output_dir / "strict_cheating_histogram.png", dpi=150)
    plt.close()

    print(f"Plots saved to {output_dir}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Y-JUNCTION + RING: STRICT RELAXATION STUDY (v2)")
    print("=" * 70)
    print()

    # Define strict criterion
    criterion = StrictCriterion(
        eta_q=1e-3,
        eta_D=1e-3,
        eta_V=1e-3,
        T_hold_periods=10,
        window_periods=2
    )

    print(f"Strict criterion thresholds:")
    print(f"  η_q = {criterion.eta_q} (q < η_q * L0)")
    print(f"  η_D = {criterion.eta_D} (distortion)")
    print(f"  η_V = {criterion.eta_V} (V_ring - V_min < η_V * ΔV)")
    print(f"  T_hold = {criterion.T_hold_periods} periods of slowest mode")
    print()

    # Run parameter scan
    results = run_parameter_scan(
        criterion,
        k_ratios=[0.1, 0.3, 1.0, 3.0, 10.0],
        m_ratios=[0.3, 1.0, 3.0],
        gammas=[0.0, 0.001, 0.01, 0.1],
        ic_types=["symmetric_push", "doublet", "ring_mode"],
        t_max=1000.0
    )

    # Output
    output_dir = Path(__file__).parent.parent / "artifacts"
    save_results(results, output_dir)

    # Print summary
    print()
    print(generate_summary_table(results))

    # Plots
    fig_dir = Path(__file__).parent.parent / "figures"
    plot_results(results, fig_dir)
