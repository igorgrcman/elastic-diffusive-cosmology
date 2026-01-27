#!/usr/bin/env python3
"""
Y-Junction + Ring Coupled Oscillator Model: Relaxation/Thermalization Study

This code models a toy mechanical analogue of the neutron Y-junction with extra
internal degrees of freedom: 3 radial "legs" connected to a central node, with
the three outer endpoints connected into a "ring" (triangle) with 3 springs.

IMPORTANT PHYSICS NOTE:
- In a purely conservative spring-mass system, the energy does not decay.
- Mode 1 (DAMPED): add minimal Rayleigh damping to define a relaxation time.
- Mode 2 (EFFECTIVE): treat ring/leg modes as bath; compute effective relaxation
  of collective coordinate q(t) by tracking energy flow + coarse-graining.

Author: EDC Research
Date: 2026-01-27
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh
import json
import csv
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Tuple, Dict, Optional
import warnings

# =============================================================================
# MODEL DEFINITION [Def]
# =============================================================================

@dataclass
class ModelParams:
    """Parameters for the Y-junction + ring model."""
    # Geometry
    L0: float = 1.0          # Rest length of legs (node to outer)
    L_ring: float = 1.732    # Rest length of ring edges (sqrt(3) for equilateral)

    # Masses
    m0: float = 1.0          # Central node mass
    m_out: float = 1.0       # Outer node mass (all equal)

    # Spring constants
    k_leg: float = 1.0       # Leg spring constant
    k_ring: float = 1.0      # Ring spring constant

    # Damping (Mode 1)
    gamma_0: float = 0.0     # Damping on central node
    gamma_out: float = 0.0   # Damping on outer nodes

    def __post_init__(self):
        # For equilateral geometry: L_ring = sqrt(3) * L0 if node at centroid
        # But we allow general L_ring for parameter scans
        pass


def compute_equilibrium_positions(params: ModelParams) -> np.ndarray:
    """
    Compute equilibrium positions for equilateral triangle configuration.

    Central node at origin, outer nodes at 120-degree intervals.
    For consistency, we set the outer nodes at distance L0 from center.

    Returns: positions array of shape (4, 2) for [r0, r1, r2, r3]
    """
    # Central node at origin
    r0 = np.array([0.0, 0.0])

    # Outer nodes at 120-degree intervals, distance L0 from center
    angles = np.array([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3])
    r1 = params.L0 * np.array([np.cos(angles[0]), np.sin(angles[0])])
    r2 = params.L0 * np.array([np.cos(angles[1]), np.sin(angles[1])])
    r3 = params.L0 * np.array([np.cos(angles[2]), np.sin(angles[2])])

    return np.array([r0, r1, r2, r3])


def compute_potential_energy(positions: np.ndarray, params: ModelParams) -> Tuple[float, float, float]:
    """
    Compute potential energy: V = V_legs + V_ring

    Returns: (V_total, V_legs, V_ring)
    """
    r0, r1, r2, r3 = positions

    # Leg contributions
    V_legs = 0.0
    for ri in [r1, r2, r3]:
        d = np.linalg.norm(ri - r0)
        V_legs += 0.5 * params.k_leg * (d - params.L0)**2

    # Ring contributions (edges: 1-2, 2-3, 3-1)
    V_ring = 0.0
    for ri, rj in [(r1, r2), (r2, r3), (r3, r1)]:
        d = np.linalg.norm(rj - ri)
        V_ring += 0.5 * params.k_ring * (d - params.L_ring)**2

    return V_legs + V_ring, V_legs, V_ring


def compute_kinetic_energy(velocities: np.ndarray, params: ModelParams) -> float:
    """Compute kinetic energy T = sum_i (1/2) m_i |v_i|^2"""
    v0, v1, v2, v3 = velocities
    T = 0.5 * params.m0 * np.dot(v0, v0)
    for vi in [v1, v2, v3]:
        T += 0.5 * params.m_out * np.dot(vi, vi)
    return T


def compute_forces(positions: np.ndarray, params: ModelParams) -> np.ndarray:
    """
    Compute forces on all nodes: F_i = -dV/dr_i

    Returns: forces array of shape (4, 2)
    """
    r0, r1, r2, r3 = positions
    forces = np.zeros((4, 2))

    # Leg forces on central node and outer nodes
    for i, ri in enumerate([r1, r2, r3], start=1):
        d_vec = ri - r0
        d = np.linalg.norm(d_vec)
        if d > 1e-10:
            unit = d_vec / d
            # Force magnitude: -k * (d - L0)
            F_mag = -params.k_leg * (d - params.L0)
            # Force on outer node i (pulls toward equilibrium)
            forces[i] += F_mag * unit
            # Force on central node (Newton's 3rd law)
            forces[0] -= F_mag * unit

    # Ring forces between outer nodes
    outer_indices = [1, 2, 3]
    edges = [(1, 2), (2, 3), (3, 1)]
    for i, j in edges:
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
    """Compute viscous damping forces: F_damp = -gamma * v"""
    v0, v1, v2, v3 = velocities
    forces = np.zeros((4, 2))
    forces[0] = -params.gamma_0 * v0
    for i in [1, 2, 3]:
        forces[i] = -params.gamma_out * velocities[i]
    return forces


# =============================================================================
# EQUATIONS OF MOTION
# =============================================================================

def equations_of_motion(t: float, y: np.ndarray, params: ModelParams) -> np.ndarray:
    """
    ODEs for the coupled oscillator system.

    State vector y = [r0_x, r0_y, r1_x, r1_y, ..., r3_y, v0_x, v0_y, ..., v3_y]
    Total: 16 components (4 nodes * 2D * 2 for position+velocity)
    """
    # Unpack state
    positions = y[:8].reshape(4, 2)
    velocities = y[8:].reshape(4, 2)

    # Compute forces
    F_spring = compute_forces(positions, params)
    F_damp = compute_damping_forces(velocities, params)
    F_total = F_spring + F_damp

    # Accelerations
    accelerations = np.zeros((4, 2))
    accelerations[0] = F_total[0] / params.m0
    for i in [1, 2, 3]:
        accelerations[i] = F_total[i] / params.m_out

    # Return derivatives: [velocities, accelerations]
    dydt = np.zeros(16)
    dydt[:8] = velocities.flatten()
    dydt[8:] = accelerations.flatten()

    return dydt


# =============================================================================
# INITIAL CONDITIONS
# =============================================================================

def create_initial_conditions(
    ic_type: str,
    params: ModelParams,
    amplitude: float = 0.3
) -> np.ndarray:
    """
    Create initial conditions for different excitation types.

    IC-1 "symmetric_push": r0 displaced along +y by amplitude
    IC-2 "doublet": r1 displaced outward (radially) by amplitude
    IC-3 "ring_mode": r1,r2,r3 displaced tangentially (circulation mode)

    Returns: state vector y0 of shape (16,)
    """
    eq_pos = compute_equilibrium_positions(params)
    positions = eq_pos.copy()
    velocities = np.zeros((4, 2))

    if ic_type == "symmetric_push":
        # Push central node upward
        positions[0, 1] += amplitude

    elif ic_type == "doublet":
        # Push r1 outward radially
        r0, r1 = positions[0], positions[1]
        direction = r1 - r0
        direction = direction / np.linalg.norm(direction)
        positions[1] += amplitude * direction

    elif ic_type == "ring_mode":
        # Tangential displacement of outer nodes (circulation)
        for i in [1, 2, 3]:
            r0, ri = positions[0], positions[i]
            radial = ri - r0
            radial = radial / np.linalg.norm(radial)
            # Tangential is perpendicular to radial
            tangent = np.array([-radial[1], radial[0]])
            positions[i] += amplitude * tangent
    else:
        raise ValueError(f"Unknown IC type: {ic_type}")

    # Pack into state vector
    y0 = np.zeros(16)
    y0[:8] = positions.flatten()
    y0[8:] = velocities.flatten()

    return y0


# =============================================================================
# OBSERVABLES AND METRICS
# =============================================================================

def compute_observables(y: np.ndarray, params: ModelParams, eq_pos: np.ndarray) -> Dict:
    """Compute all observables from state vector."""
    positions = y[:8].reshape(4, 2)
    velocities = y[8:].reshape(4, 2)

    # Energies
    V_total, V_legs, V_ring = compute_potential_energy(positions, params)
    T = compute_kinetic_energy(velocities, params)
    E_total = T + V_total

    # Collective coordinate q: distance of central node from equilibrium
    q = np.linalg.norm(positions[0] - eq_pos[0])

    # Symmetric leg extension
    q_sym = 0.0
    for i in [1, 2, 3]:
        leg_length = np.linalg.norm(positions[i] - positions[0])
        q_sym += (leg_length - params.L0)
    q_sym /= 3.0

    # Ring deviation from equilateral
    ring_deviation = 0.0
    edges = [(1, 2), (2, 3), (3, 1)]
    for i, j in edges:
        d = np.linalg.norm(positions[j] - positions[i])
        ring_deviation += (d - params.L_ring)**2
    ring_deviation = np.sqrt(ring_deviation / 3.0)

    return {
        'E_total': E_total,
        'T': T,
        'V_total': V_total,
        'V_legs': V_legs,
        'V_ring': V_ring,
        'q': q,
        'q_sym': q_sym,
        'ring_deviation': ring_deviation
    }


def compute_equilibrium_energy(params: ModelParams) -> float:
    """Compute V_min at equilibrium configuration."""
    eq_pos = compute_equilibrium_positions(params)
    V_min, _, _ = compute_potential_energy(eq_pos, params)
    return V_min


# =============================================================================
# LINEARIZED ANALYSIS (Normal Modes)
# =============================================================================

def compute_hessian(params: ModelParams, eq_pos: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Compute Hessian matrix d^2V/dr_i dr_j at equilibrium via finite differences.

    Returns: 8x8 Hessian matrix (4 nodes * 2D)
    """
    n = 8  # 4 nodes * 2 dimensions
    H = np.zeros((n, n))

    def V_func(pos_flat):
        pos = pos_flat.reshape(4, 2)
        V, _, _ = compute_potential_energy(pos, params)
        return V

    pos0 = eq_pos.flatten()

    for i in range(n):
        for j in range(i, n):
            # Mixed partial derivative via central differences
            pos_pp = pos0.copy()
            pos_pp[i] += eps
            pos_pp[j] += eps

            pos_pm = pos0.copy()
            pos_pm[i] += eps
            pos_pm[j] -= eps

            pos_mp = pos0.copy()
            pos_mp[i] -= eps
            pos_mp[j] += eps

            pos_mm = pos0.copy()
            pos_mm[i] -= eps
            pos_mm[j] -= eps

            H[i, j] = (V_func(pos_pp) - V_func(pos_pm) - V_func(pos_mp) + V_func(pos_mm)) / (4 * eps**2)
            H[j, i] = H[i, j]

    return H


def compute_normal_modes(params: ModelParams) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute normal mode frequencies and eigenvectors around equilibrium.

    Returns: (frequencies, eigenvectors)
    - frequencies: array of angular frequencies omega_k
    - eigenvectors: 8x8 matrix, columns are mode shapes
    """
    eq_pos = compute_equilibrium_positions(params)
    H = compute_hessian(params, eq_pos)

    # Mass matrix (diagonal)
    masses = np.array([params.m0, params.m0, params.m_out, params.m_out,
                       params.m_out, params.m_out, params.m_out, params.m_out])
    M = np.diag(masses)
    M_inv_sqrt = np.diag(1.0 / np.sqrt(masses))

    # Transform to mass-weighted coordinates: H_tilde = M^(-1/2) H M^(-1/2)
    H_tilde = M_inv_sqrt @ H @ M_inv_sqrt

    # Solve eigenvalue problem
    eigenvalues, eigenvectors = eigh(H_tilde)

    # Frequencies: omega^2 = eigenvalue
    # Some eigenvalues may be zero (rigid body modes) or slightly negative (numerical)
    frequencies = np.zeros(8)
    for i, ev in enumerate(eigenvalues):
        if ev > 1e-10:
            frequencies[i] = np.sqrt(ev)
        else:
            frequencies[i] = 0.0

    return frequencies, eigenvectors


# =============================================================================
# SIMULATION AND RELAXATION TIME MEASUREMENT
# =============================================================================

@dataclass
class SimulationResult:
    """Results from a single simulation run."""
    params: dict
    ic_type: str
    amplitude: float

    # Time series (sampled)
    t: List[float]
    E_total: List[float]
    V_total: List[float]
    q: List[float]
    q_sym: List[float]
    ring_deviation: List[float]

    # Derived quantities
    V_min: float
    E_initial: float
    frequencies: List[float]

    # Relaxation metrics
    t_relax_energy: Optional[float] = None  # Time when V-V_min < eps_V
    t_relax_q: Optional[float] = None       # Time when q < eps_q
    t_relax_full: Optional[float] = None    # Time when both q AND ring_dev < threshold

    # Mode 2 effective relaxation (for undamped)
    t_effective_q_rms: Optional[float] = None


def run_simulation(
    params: ModelParams,
    ic_type: str,
    amplitude: float = 0.3,
    t_max: float = 500.0,
    dt_sample: float = 0.1,
    eps_energy_frac: float = 1e-3,
    eps_q: float = 0.01,
    eps_ring: float = 0.01,
    n_persist: int = 10
) -> SimulationResult:
    """
    Run simulation and measure relaxation time.

    Relaxation criteria:
    - eps_energy_frac: fraction of initial excess energy
    - eps_q: threshold for q coordinate
    - eps_ring: threshold for ring deviation
    - n_persist: number of periods mode must stay within threshold
    """
    eq_pos = compute_equilibrium_positions(params)
    y0 = create_initial_conditions(ic_type, params, amplitude)

    # Compute V_min and initial energy
    V_min = compute_equilibrium_energy(params)
    obs0 = compute_observables(y0, params, eq_pos)
    E_initial = obs0['E_total']
    excess_energy = obs0['V_total'] - V_min
    eps_V = eps_energy_frac * max(excess_energy, 1e-10)

    # Compute normal mode frequencies
    frequencies, _ = compute_normal_modes(params)
    omega_min = min([f for f in frequencies if f > 0.01])
    T_min = 2 * np.pi / omega_min if omega_min > 0 else 10.0

    # Adjust t_max based on damping
    if params.gamma_0 > 0 or params.gamma_out > 0:
        # Estimate decay time from damping
        gamma_eff = max(params.gamma_0, params.gamma_out)
        t_decay_est = 5.0 / gamma_eff if gamma_eff > 0 else t_max
        t_max = min(t_max, max(t_decay_est * 3, 100.0))

    # Integration
    t_span = (0, t_max)
    t_eval = np.arange(0, t_max, dt_sample)

    sol = solve_ivp(
        lambda t, y: equations_of_motion(t, y, params),
        t_span,
        y0,
        method='DOP853',
        t_eval=t_eval,
        rtol=1e-10,
        atol=1e-12
    )

    # Extract observables
    t_series = sol.t.tolist()
    E_series = []
    V_series = []
    q_series = []
    q_sym_series = []
    ring_dev_series = []

    for i in range(len(sol.t)):
        obs = compute_observables(sol.y[:, i], params, eq_pos)
        E_series.append(obs['E_total'])
        V_series.append(obs['V_total'])
        q_series.append(obs['q'])
        q_sym_series.append(obs['q_sym'])
        ring_dev_series.append(obs['ring_deviation'])

    # Check energy conservation (for undamped case)
    if params.gamma_0 == 0 and params.gamma_out == 0:
        E_drift = abs(E_series[-1] - E_series[0]) / E_series[0]
        if E_drift > 1e-6:
            warnings.warn(f"Energy drift: {E_drift:.2e}")

    # Compute relaxation times
    t_relax_energy = None
    t_relax_q = None
    t_relax_full = None

    # Mode 1: with damping
    if params.gamma_0 > 0 or params.gamma_out > 0:
        # Find time when V - V_min < eps_V and stays there
        for i, (t, V, q, rd) in enumerate(zip(t_series, V_series, q_series, ring_dev_series)):
            if V - V_min < eps_V:
                # Check persistence
                persist = True
                for j in range(i, min(i + n_persist, len(t_series))):
                    if V_series[j] - V_min >= eps_V:
                        persist = False
                        break
                if persist and t_relax_energy is None:
                    t_relax_energy = t

            if q < eps_q and t_relax_q is None:
                persist = True
                for j in range(i, min(i + n_persist, len(t_series))):
                    if q_series[j] >= eps_q:
                        persist = False
                        break
                if persist:
                    t_relax_q = t

            # Full relaxation: both q AND ring deviation small
            if q < eps_q and rd < eps_ring and t_relax_full is None:
                persist = True
                for j in range(i, min(i + n_persist, len(t_series))):
                    if q_series[j] >= eps_q or ring_dev_series[j] >= eps_ring:
                        persist = False
                        break
                if persist:
                    t_relax_full = t

    # Mode 2: effective relaxation for undamped case
    t_effective_q_rms = None
    if params.gamma_0 == 0 and params.gamma_out == 0:
        # Compute running RMS of q over windows
        window_size = int(5 * T_min / dt_sample)  # 5 periods
        if window_size > 0 and len(q_series) > 2 * window_size:
            q_arr = np.array(q_series)
            for i in range(window_size, len(q_series) - window_size):
                q_window = q_arr[i - window_size:i + window_size]
                q_rms = np.sqrt(np.mean(q_window**2))
                if q_rms < eps_q and t_effective_q_rms is None:
                    t_effective_q_rms = t_series[i]
                    break

    return SimulationResult(
        params=asdict(params),
        ic_type=ic_type,
        amplitude=amplitude,
        t=t_series,
        E_total=E_series,
        V_total=V_series,
        q=q_series,
        q_sym=q_sym_series,
        ring_deviation=ring_dev_series,
        V_min=V_min,
        E_initial=E_initial,
        frequencies=frequencies.tolist(),
        t_relax_energy=t_relax_energy,
        t_relax_q=t_relax_q,
        t_relax_full=t_relax_full,
        t_effective_q_rms=t_effective_q_rms
    )


# =============================================================================
# PARAMETER SCANS
# =============================================================================

def run_parameter_scan() -> List[SimulationResult]:
    """Run parameter scan over k_ring/k_leg, mass ratios, and damping."""
    results = []

    # Dimensionless parameters
    k_ring_ratios = [0.1, 0.3, 1.0, 3.0, 10.0]
    mass_ratios = [0.3, 1.0, 3.0]  # m0/m_out
    gamma_values = [0.0, 1e-3, 1e-2, 1e-1]  # Damping coefficients
    ic_types = ["symmetric_push", "doublet", "ring_mode"]

    base_params = ModelParams(
        L0=1.0,
        L_ring=np.sqrt(3),  # Equilateral at equilibrium
        m0=1.0,
        m_out=1.0,
        k_leg=1.0,
        k_ring=1.0,
        gamma_0=0.0,
        gamma_out=0.0
    )

    total_runs = len(k_ring_ratios) * len(mass_ratios) * len(gamma_values) * len(ic_types)
    run_count = 0

    for k_ratio in k_ring_ratios:
        for m_ratio in mass_ratios:
            for gamma in gamma_values:
                for ic_type in ic_types:
                    run_count += 1
                    print(f"Run {run_count}/{total_runs}: k_ring/k_leg={k_ratio}, m0/m_out={m_ratio}, gamma={gamma}, IC={ic_type}")

                    params = ModelParams(
                        L0=1.0,
                        L_ring=np.sqrt(3),
                        m0=m_ratio,
                        m_out=1.0,
                        k_leg=1.0,
                        k_ring=k_ratio,
                        gamma_0=gamma,
                        gamma_out=gamma
                    )

                    try:
                        result = run_simulation(
                            params, ic_type,
                            amplitude=0.3,
                            t_max=500.0 if gamma > 0 else 200.0
                        )
                        results.append(result)
                    except Exception as e:
                        print(f"  Error: {e}")

    return results


# =============================================================================
# PLOTTING
# =============================================================================

def create_plots(results: List[SimulationResult], output_dir: Path):
    """Generate diagnostic plots."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('Agg')
    except ImportError:
        print("Matplotlib not available, skipping plots")
        return

    # Select representative cases for detailed plots
    # 1. Undamped symmetric push with k_ring/k_leg = 1
    # 2. Damped symmetric push with gamma = 0.01
    # 3. Comparison across k_ring ratios

    # Find representative results
    undamped_cases = [r for r in results if r.params['gamma_0'] == 0
                     and r.ic_type == 'symmetric_push'
                     and abs(r.params['k_ring'] - 1.0) < 0.1
                     and abs(r.params['m0'] - 1.0) < 0.1]

    damped_cases = [r for r in results if r.params['gamma_0'] > 0
                   and r.ic_type == 'symmetric_push'
                   and abs(r.params['k_ring'] - 1.0) < 0.1
                   and abs(r.params['m0'] - 1.0) < 0.1]

    # Plot 1: Energy vs time (undamped vs damped)
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    if undamped_cases:
        r = undamped_cases[0]
        ax = axes[0]
        ax.plot(r.t, r.E_total, 'b-', label='E_total', linewidth=0.5)
        ax.plot(r.t, r.V_total, 'r-', label='V_total', linewidth=0.5)
        ax.axhline(r.V_min, color='k', linestyle='--', label='V_min')
        ax.set_xlabel('Time')
        ax.set_ylabel('Energy')
        ax.set_title(f'Undamped (gamma=0): Energy Conservation')
        ax.legend()
        ax.set_xlim(0, min(100, max(r.t)))

    if damped_cases:
        r = damped_cases[-1]  # Highest damping
        ax = axes[1]
        ax.plot(r.t, r.E_total, 'b-', label='E_total', linewidth=0.5)
        ax.plot(r.t, r.V_total, 'r-', label='V_total', linewidth=0.5)
        ax.axhline(r.V_min, color='k', linestyle='--', label='V_min')
        ax.set_xlabel('Time')
        ax.set_ylabel('Energy')
        ax.set_title(f'Damped (gamma={r.params["gamma_0"]:.3f}): Energy Decay')
        ax.legend()

    plt.tight_layout()
    plt.savefig(output_dir / 'yjunction_energy_vs_time.png', dpi=150)
    plt.close()

    # Plot 2: q vs time
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    if undamped_cases:
        r = undamped_cases[0]
        ax = axes[0]
        ax.plot(r.t, r.q, 'b-', linewidth=0.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('q (node displacement)')
        ax.set_title('Undamped: q(t) oscillates indefinitely')
        ax.set_xlim(0, min(100, max(r.t)))

    if damped_cases:
        r = damped_cases[-1]
        ax = axes[1]
        ax.plot(r.t, r.q, 'b-', linewidth=0.5)
        if r.t_relax_q is not None:
            ax.axvline(r.t_relax_q, color='r', linestyle='--', label=f't_relax_q={r.t_relax_q:.1f}')
            ax.legend()
        ax.set_xlabel('Time')
        ax.set_ylabel('q (node displacement)')
        ax.set_title(f'Damped (gamma={r.params["gamma_0"]:.3f}): q(t) decays')

    plt.tight_layout()
    plt.savefig(output_dir / 'yjunction_q_vs_time.png', dpi=150)
    plt.close()

    # Plot 3: Mode energy partition (for undamped case)
    if undamped_cases:
        r = undamped_cases[0]
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(r.t, r.V_total, 'b-', label='V_total', linewidth=0.5, alpha=0.7)
        ax.fill_between(r.t, 0, r.q_sym, alpha=0.3, label='q_sym (leg extension)')
        ax.plot(r.t, r.ring_deviation, 'g-', label='ring_deviation', linewidth=0.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('Energy / Deviation')
        ax.set_title('Mode Energy Partition (Undamped)')
        ax.legend()
        ax.set_xlim(0, min(100, max(r.t)))
        plt.tight_layout()
        plt.savefig(output_dir / 'yjunction_mode_energy_partition.png', dpi=150)
        plt.close()

    # Plot 4: Relaxation time vs damping
    damped_symmetric = [r for r in results if r.params['gamma_0'] > 0
                        and r.ic_type == 'symmetric_push'
                        and abs(r.params['k_ring'] - 1.0) < 0.1
                        and abs(r.params['m0'] - 1.0) < 0.1]

    if len(damped_symmetric) >= 2:
        fig, ax = plt.subplots(figsize=(8, 5))
        gammas = [r.params['gamma_0'] for r in damped_symmetric]
        t_relax_full = [r.t_relax_full if r.t_relax_full else float('nan') for r in damped_symmetric]
        t_relax_q = [r.t_relax_q if r.t_relax_q else float('nan') for r in damped_symmetric]

        ax.loglog(gammas, t_relax_q, 'bo-', label='t_relax (q only)')
        ax.loglog(gammas, t_relax_full, 'rs-', label='t_relax (q + ring)')
        ax.set_xlabel('Damping coefficient gamma')
        ax.set_ylabel('Relaxation time')
        ax.set_title('Relaxation Time vs Damping')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / 'yjunction_trelax_vs_gamma.png', dpi=150)
        plt.close()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main execution: run scans, generate outputs, create plots."""
    print("="*60)
    print("Y-Junction + Ring Coupled Oscillator: Relaxation Study")
    print("="*60)

    # Setup paths
    script_dir = Path(__file__).parent
    artifacts_dir = script_dir.parent / 'artifacts'
    figures_dir = script_dir.parent / 'figures'
    artifacts_dir.mkdir(exist_ok=True)
    figures_dir.mkdir(exist_ok=True)

    # Run parameter scan
    print("\nRunning parameter scan...")
    results = run_parameter_scan()

    # Save detailed results to JSON
    print("\nSaving results...")
    json_path = artifacts_dir / 'yjunction_relax_results.json'

    # Convert results to serializable format
    results_dict = []
    for r in results:
        rd = {
            'params': r.params,
            'ic_type': r.ic_type,
            'amplitude': r.amplitude,
            'V_min': r.V_min,
            'E_initial': r.E_initial,
            'frequencies': r.frequencies,
            't_relax_energy': r.t_relax_energy,
            't_relax_q': r.t_relax_q,
            't_relax_full': r.t_relax_full,
            't_effective_q_rms': r.t_effective_q_rms,
            # Don't save full time series to keep file size manageable
            't_final': r.t[-1] if r.t else None,
            'E_final': r.E_total[-1] if r.E_total else None,
            'q_final': r.q[-1] if r.q else None,
        }
        results_dict.append(rd)

    with open(json_path, 'w') as f:
        json.dump(results_dict, f, indent=2)

    # Save summary CSV
    csv_path = artifacts_dir / 'yjunction_relax_summary.csv'
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'k_ring/k_leg', 'm0/m_out', 'gamma', 'ic_type',
            't_relax_q', 't_relax_full', 't_effective_q_rms',
            'omega_min', 'E_initial', 'status'
        ])

        for r in results:
            k_ratio = r.params['k_ring'] / r.params['k_leg']
            m_ratio = r.params['m0'] / r.params['m_out']
            gamma = r.params['gamma_0']
            omega_min = min([f for f in r.frequencies if f > 0.01]) if any(f > 0.01 for f in r.frequencies) else 0

            # Determine status
            if gamma == 0:
                status = 'CONSERVATIVE'
            elif r.t_relax_full is not None:
                status = 'RELAXED'
            else:
                status = 'NOT_RELAXED'

            writer.writerow([
                f'{k_ratio:.2f}',
                f'{m_ratio:.2f}',
                f'{gamma:.4f}',
                r.ic_type,
                f'{r.t_relax_q:.2f}' if r.t_relax_q else 'N/A',
                f'{r.t_relax_full:.2f}' if r.t_relax_full else 'N/A',
                f'{r.t_effective_q_rms:.2f}' if r.t_effective_q_rms else 'N/A',
                f'{omega_min:.3f}',
                f'{r.E_initial:.4f}',
                status
            ])

    # Generate plots
    print("\nGenerating plots...")
    create_plots(results, figures_dir)

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    # Count outcomes
    conservative = sum(1 for r in results if r.params['gamma_0'] == 0)
    relaxed = sum(1 for r in results if r.t_relax_full is not None)
    not_relaxed = sum(1 for r in results if r.params['gamma_0'] > 0 and r.t_relax_full is None)

    print(f"Total runs: {len(results)}")
    print(f"  Conservative (no damping): {conservative}")
    print(f"  Damped & relaxed: {relaxed}")
    print(f"  Damped & not relaxed (in time window): {not_relaxed}")

    # Key finding for Mode 2 (undamped)
    undamped_with_effective = [r for r in results if r.params['gamma_0'] == 0 and r.t_effective_q_rms is not None]
    print(f"\nMode 2 (effective relaxation, undamped):")
    print(f"  Runs with effective q_RMS relaxation: {len(undamped_with_effective)}")
    if undamped_with_effective:
        print(f"  -> Some runs show q coordinate settling temporarily while energy remains in internal modes")
    else:
        print(f"  -> No effective relaxation observed (q oscillates throughout)")

    # Scaling with damping
    damped_relaxed = [r for r in results if r.params['gamma_0'] > 0 and r.t_relax_full is not None]
    if damped_relaxed:
        gammas = sorted(set(r.params['gamma_0'] for r in damped_relaxed))
        print(f"\nMode 1 (damped) relaxation times:")
        for g in gammas:
            cases = [r for r in damped_relaxed if r.params['gamma_0'] == g]
            avg_t = np.mean([r.t_relax_full for r in cases])
            print(f"  gamma={g:.4f}: avg t_relax_full = {avg_t:.1f}")

    print("\n" + "="*60)
    print("Artifacts saved to:")
    print(f"  {json_path}")
    print(f"  {csv_path}")
    print(f"  {figures_dir}/yjunction_*.png")
    print("="*60)

    return results


if __name__ == '__main__':
    results = main()
