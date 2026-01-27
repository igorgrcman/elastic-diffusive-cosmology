#!/usr/bin/env python3
"""
JUNCTION CORE WELL: Geometry-only finite-thickness regularization
==================================================================

This script tests whether a localized junction-core action term S_core
can produce metastability in V_total(q) = V_NG(q) + V_core(q), using
only existing EDC scales (σ, δ, τ) without introducing bulk fields.

Core idea:
  S_core = -∫ dt E0 × f(q/δ)
  where E0 is built from σ, δ (dimensional closure) and f decays for q >> δ.

Candidate mechanisms:
  A1) Overlap/regularization: E0 = C × σ × δ², f(x) = exp(-x²)
  A2) Junction rim (line): E0 = C × σ × δ², f(x) = exp(-x²) [same form]
  A3) Curvature core: V_core = -E0/(1 + (q/δ)²)  [Lorentzian]

Epistemic tags:
  [Def] Definition
  [BL]  Baseline (PDG/CODATA)
  [I]   Identified (pattern fit)
  [Dc]  Derived conditional on model
  [P]   Proposed/Postulated
  [Cal] Calibrated/Scanned

Date: 2026-01-27
Repository: edc_book_2/src/derivations/code/
"""

import numpy as np
import json
import csv
import os
from dataclasses import dataclass, asdict
from typing import Tuple, Optional, Dict, Any, List

# Try to import scipy
try:
    from scipy.optimize import brentq
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
# PHYSICAL CONSTANTS [BL] — from PDG/CODATA
# =============================================================================

M_E_MEV = 0.51099895  # MeV [BL] electron mass
ALPHA = 1.0 / 137.035999084  # [BL] fine structure constant

# Neutron-proton mass difference
DELTA_M_NP_PDG = 1.29333236  # MeV [BL] PDG 2022 (Option B)
DELTA_M_NP_BOOK = (5.0/2.0 + 4.0*ALPHA) * M_E_MEV  # MeV [Dc] (Option A)

# Target barrier heights
V_B_CAL = 2.6  # MeV [Cal] from WKB fit to τ_n
V_B_TARGET_B = 2.0 * DELTA_M_NP_PDG  # MeV [Dc] = 2.587 MeV
V_B_TARGET_A = 2.0 * DELTA_M_NP_BOOK  # MeV [Dc] = 2.585 MeV

# =============================================================================
# EDC PARAMETERS [Dc]/[I]
# =============================================================================

SIGMA_EDC = 8.82  # MeV/fm² [Dc] brane tension (from E_σ = m_e c²/α)
DELTA_EDC = 0.1   # fm [I] brane thickness
L0_EDC = 1.0      # fm [I] nucleon scale


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class JunctionCoreParams:
    """Parameters for junction core model."""
    mechanism: str      # A1, A2, A3
    C: float           # Dimensionless coefficient [P] or [Dc]
    sigma: float       # Brane tension [MeV/fm²]
    delta: float       # Brane thickness [fm]
    tau: float         # String tension [MeV/fm]
    L0: float          # In-brane leg projection [fm]
    k: float           # Warp parameter [1/fm] (0 for flat)

    @property
    def E0(self) -> float:
        """Core energy scale E0 = C × σ × δ² [Dc]."""
        return self.C * self.sigma * self.delta**2


@dataclass
class CoreResult:
    """Results from junction core computation."""
    mechanism: str
    C: float
    E0: float              # Core energy scale [MeV]
    has_metastability: bool
    q_n: Optional[float]   # Neutron position [fm]
    q_B: Optional[float]   # Barrier position [fm]
    V_B: Optional[float]   # Barrier height [MeV]
    Delta_m: Optional[float]  # V(q_n) - V(0) [MeV]

    # Comparison ratios
    V_B_over_2Dm_B: Optional[float]  # V_B / (2 × Δm_np_PDG)
    V_B_over_2Dm_A: Optional[float]  # V_B / (2 × Δm_np_Book)
    V_B_vs_cal_pct: Optional[float]  # (V_B - V_B_cal)/V_B_cal × 100

    params: Dict[str, Any]
    notes: str


# =============================================================================
# NAMBU-GOTO BASELINE (from putC_compute_MV.py)
# =============================================================================

def V_NG_flat(q: float, tau: float, L0: float) -> float:
    """
    Nambu-Goto potential in flat bulk [Dc].

    V_NG(q) = 3 × τ × √(L0² + q²)

    Three legs by Z₃ symmetry.
    """
    return 3.0 * tau * np.sqrt(L0**2 + q**2)


def V_NG_warped(q: float, tau: float, L0: float, k: float) -> float:
    """
    Nambu-Goto potential in warped bulk [Dc].

    Uses straight embedding approximation for leg energy.
    For k > 0, warping reduces effective tension at large ξ.
    """
    if k < 1e-10:
        return V_NG_flat(q, tau, L0)

    # Straight embedding: ξ(l) = q × (1 - l/L0)
    # Integrate numerically
    n = 50
    dl = L0 / n
    E_leg = 0.0

    for i in range(n):
        l = (i + 0.5) * dl
        xi = q * (1.0 - l / L0)
        warp = np.exp(-k * np.abs(xi))
        dxi_dl = -q / L0
        E_leg += np.sqrt(warp**2 + dxi_dl**2) * dl

    return 3.0 * tau * E_leg


# =============================================================================
# JUNCTION CORE MECHANISMS
# =============================================================================

def V_core_A1(q: float, params: JunctionCoreParams) -> float:
    """
    Mechanism A1: Overlap/regularization energy [Dc/P].

    Physical picture:
      When q ≈ 0, the three junction legs overlap near the brane surface.
      This creates a localized "core" energy that depends on q/δ.
      As q increases beyond δ, the overlap decreases exponentially.

    Model [Dc]:
      V_core(q) = -E0 × exp(-(q/δ)²)
      E0 = C × σ × δ²

    The minus sign creates attraction toward q = 0 (proton state).

    Parameter C:
      [Dc] if C ~ O(1) from geometric argument
      [P]  if C is scanned over range
    """
    E0 = params.E0
    x = q / params.delta
    return -E0 * np.exp(-x**2)


def V_core_A2(q: float, params: JunctionCoreParams) -> float:
    """
    Mechanism A2: Junction rim (line energy) [Dc/P].

    Physical picture:
      The junction can be viewed as having a circular "rim" of radius ~ δ
      where the three legs meet. This rim has a line tension τ_line ~ σ × δ.
      The rim energy scales as τ_line × perimeter ~ σ × δ × δ = σ × δ².

    Model [Dc]:
      V_core(q) = -E0 × exp(-(q/δ)²)
      E0 = C × σ × δ²

    Same functional form as A1 but different physical interpretation.
    The line interpretation suggests C ~ 2π (circumference factor).

    Tag: [Dc] if C = 2π from geometry; [P] if scanned.
    """
    # Same mathematical form as A1, different physical interpretation
    E0 = params.E0
    x = q / params.delta
    return -E0 * np.exp(-x**2)


def V_core_A3(q: float, params: JunctionCoreParams) -> float:
    """
    Mechanism A3: Curvature-concentrated core (Lorentzian) [Dc/P].

    Physical picture:
      The junction has concentrated curvature at q = 0.
      The curvature energy behaves as 1/(1 + (q/δ)²).
      This gives a "softer" decay than Gaussian.

    Model [Dc]:
      V_core(q) = -E0 / (1 + (q/δ)²)
      E0 = C × σ × δ²

    The Lorentzian has longer tails than Gaussian, which may affect
    the barrier structure differently.

    Tag: [Dc] if C ~ O(1); [P] if scanned.
    """
    E0 = params.E0
    x = q / params.delta
    return -E0 / (1.0 + x**2)


def V_core(q: float, params: JunctionCoreParams) -> float:
    """Dispatch to appropriate mechanism."""
    if params.mechanism == "A1":
        return V_core_A1(q, params)
    elif params.mechanism == "A2":
        return V_core_A2(q, params)
    elif params.mechanism == "A3":
        return V_core_A3(q, params)
    else:
        raise ValueError(f"Unknown mechanism: {params.mechanism}")


# =============================================================================
# TOTAL POTENTIAL
# =============================================================================

def V_total(q: float, params: JunctionCoreParams) -> float:
    """
    Total potential [Dc]:

    V_total(q) = V_NG(q) + V_core(q)

    No brane tension contribution here (absorbed into E0 interpretation).
    """
    V_ng = V_NG_warped(q, params.tau, params.L0, params.k)
    V_c = V_core(q, params)
    return V_ng + V_c


def dV_total(q: float, params: JunctionCoreParams, eps: float = 1e-7) -> float:
    """First derivative by central difference."""
    if q < eps:
        return (V_total(eps, params) - V_total(0, params)) / eps
    return (V_total(q + eps, params) - V_total(q - eps, params)) / (2 * eps)


def d2V_total(q: float, params: JunctionCoreParams, eps: float = 1e-6) -> float:
    """Second derivative by central difference."""
    return (V_total(q + eps, params) - 2*V_total(q, params) + V_total(q - eps, params)) / eps**2


# =============================================================================
# EXTREMUM FINDING
# =============================================================================

def find_extrema(params: JunctionCoreParams, q_max: float = 2.0) -> Tuple[Optional[float], Optional[float]]:
    """
    Find stationary points of V_total(q).

    Returns (q_n, q_B) where:
      q_n = metastable minimum (neutron)
      q_B = barrier saddle point (between q=0 and q_n)

    Metastability requires: 0 < q_B < q_n with V(q_B) > V(q_n).
    """
    # Scan for sign changes in dV
    n = 100
    q_grid = np.linspace(0.01, q_max, n)
    dV_grid = [dV_total(q, params) for q in q_grid]

    q_n = None
    q_B = None

    for i in range(len(q_grid) - 1):
        if dV_grid[i] * dV_grid[i+1] < 0:
            # Sign change — refine with bisection
            q_low, q_high = q_grid[i], q_grid[i+1]

            if SCIPY_AVAILABLE:
                try:
                    q_root = brentq(lambda q: dV_total(q, params), q_low, q_high)
                except:
                    q_root = 0.5 * (q_low + q_high)
            else:
                # Simple bisection
                for _ in range(20):
                    q_mid = 0.5 * (q_low + q_high)
                    if dV_total(q_mid, params) * dV_total(q_low, params) < 0:
                        q_high = q_mid
                    else:
                        q_low = q_mid
                q_root = 0.5 * (q_low + q_high)

            # Check curvature
            d2V = d2V_total(q_root, params)

            if d2V > 0:
                # Local minimum — candidate for neutron
                if q_n is None or q_root > q_n:
                    q_n = q_root
            else:
                # Local maximum — candidate for barrier
                if q_B is None:
                    q_B = q_root

    # Validate: need q_B < q_n for proper metastability
    if q_n is not None and q_B is not None:
        if q_B >= q_n:
            # Invalid structure — swap or reject
            q_n, q_B = None, None

    return q_n, q_B


# =============================================================================
# COMPUTATION
# =============================================================================

def compute_junction_core(params: JunctionCoreParams, q_max: float = 2.0) -> CoreResult:
    """
    Compute V_total and find metastability for given parameters.
    """
    q_n, q_B = find_extrema(params, q_max)

    has_metastability = (q_n is not None and q_B is not None and 0 < q_B < q_n)

    V_B = None
    Delta_m = None
    V_B_over_2Dm_B = None
    V_B_over_2Dm_A = None
    V_B_vs_cal_pct = None

    V_at_0 = V_total(0, params)

    if has_metastability:
        V_at_qn = V_total(q_n, params)
        V_at_qB = V_total(q_B, params)

        V_B = V_at_qB - V_at_qn
        Delta_m = V_at_qn - V_at_0

        if V_B > 0:
            V_B_over_2Dm_B = V_B / V_B_TARGET_B
            V_B_over_2Dm_A = V_B / V_B_TARGET_A
            V_B_vs_cal_pct = (V_B - V_B_CAL) / V_B_CAL * 100

    # Notes
    if has_metastability:
        notes = (f"Metastability FOUND. q_B = {q_B:.4f} fm, q_n = {q_n:.4f} fm, "
                 f"V_B = {V_B:.4f} MeV, ratio = {V_B_over_2Dm_B:.3f}")
    else:
        if q_n is None and q_B is None:
            notes = "No extrema found. V(q) likely monotonic."
        elif q_n is not None and q_B is None:
            notes = f"Found minimum at q_n = {q_n:.4f} fm but no barrier."
        else:
            notes = f"Unusual structure: q_B = {q_B}, q_n = {q_n}"

    params_dict = {
        'mechanism': params.mechanism,
        'C': params.C,
        'E0': params.E0,
        'sigma': params.sigma,
        'delta': params.delta,
        'tau': params.tau,
        'L0': params.L0,
        'k': params.k
    }

    return CoreResult(
        mechanism=params.mechanism,
        C=params.C,
        E0=params.E0,
        has_metastability=has_metastability,
        q_n=q_n,
        q_B=q_B,
        V_B=V_B,
        Delta_m=Delta_m,
        V_B_over_2Dm_B=V_B_over_2Dm_B,
        V_B_over_2Dm_A=V_B_over_2Dm_A,
        V_B_vs_cal_pct=V_B_vs_cal_pct,
        params=params_dict,
        notes=notes
    )


# =============================================================================
# PARAMETER SCANS
# =============================================================================

def closure_scan() -> List[CoreResult]:
    """
    Scan C ~ O(1) for closure attempt.

    If metastability exists for C in [0.5, 2], this is a strong [Dc] result.
    If C >> 1 or narrow tuning required, result is [P/Cal].
    """
    results = []

    # Closure attempt: C ~ O(1)
    C_closure = [0.5, 1.0, 2.0, np.pi, 2*np.pi]  # O(1) values with geometric motivation

    # Also scan tau to find viable regime
    tau_values = [1.0, 2.0, 5.0, 10.0]

    print("\n" + "="*70)
    print("CLOSURE ATTEMPT: C ~ O(1)")
    print("="*70)

    for mechanism in ["A1", "A2", "A3"]:
        print(f"\nMechanism {mechanism}:")

        for C in C_closure:
            for tau in tau_values:
                params = JunctionCoreParams(
                    mechanism=mechanism,
                    C=C,
                    sigma=SIGMA_EDC,
                    delta=DELTA_EDC,
                    tau=tau,
                    L0=L0_EDC,
                    k=0.0  # Flat bulk first
                )

                result = compute_junction_core(params)
                results.append(result)

                if result.has_metastability:
                    print(f"  C={C:.2f}, τ={tau:.1f}: METASTABLE, "
                          f"V_B={result.V_B:.3f} MeV, ratio={result.V_B_over_2Dm_B:.3f}")

    return results


def extended_scan() -> List[CoreResult]:
    """
    Extended scan over C in [0.1, 100] to map parameter space.

    This is explicitly [P] — scanning beyond O(1) closure.
    """
    results = []

    # Extended range
    C_extended = np.logspace(-1, 2, 20)  # 0.1 to 100
    tau_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
    k_values = [0.0, 1.0, 2.0]  # Include warping

    print("\n" + "="*70)
    print("EXTENDED SCAN: C in [0.1, 100]  [P]")
    print("="*70)

    for mechanism in ["A1", "A2", "A3"]:
        print(f"\nMechanism {mechanism}:")
        count = 0

        for C in C_extended:
            for tau in tau_values:
                for k in k_values:
                    params = JunctionCoreParams(
                        mechanism=mechanism,
                        C=C,
                        sigma=SIGMA_EDC,
                        delta=DELTA_EDC,
                        tau=tau,
                        L0=L0_EDC,
                        k=k
                    )

                    result = compute_junction_core(params)
                    results.append(result)

                    if result.has_metastability:
                        count += 1

        print(f"  Total metastable: {count}")

    return results


def targeted_scan() -> List[CoreResult]:
    """
    Targeted scan to find parameters matching V_B ≈ 2.6 MeV or 2×Δm_np.
    """
    results = []

    # Fine scan around promising regions
    C_fine = np.linspace(5, 50, 20)
    tau_fine = np.linspace(0.5, 5.0, 10)

    print("\n" + "="*70)
    print("TARGETED SCAN: Matching V_B targets [Cal]")
    print("="*70)

    best_match_cal = None
    best_error_cal = float('inf')
    best_match_conj = None
    best_error_conj = float('inf')

    for mechanism in ["A1", "A2", "A3"]:
        for C in C_fine:
            for tau in tau_fine:
                for k in [0.0, 1.0]:
                    params = JunctionCoreParams(
                        mechanism=mechanism,
                        C=C,
                        sigma=SIGMA_EDC,
                        delta=DELTA_EDC,
                        tau=tau,
                        L0=L0_EDC,
                        k=k
                    )

                    result = compute_junction_core(params)
                    results.append(result)

                    if result.has_metastability and result.V_B is not None:
                        error_cal = abs(result.V_B - V_B_CAL)
                        error_conj = abs(result.V_B - V_B_TARGET_B)

                        if error_cal < best_error_cal:
                            best_error_cal = error_cal
                            best_match_cal = result

                        if error_conj < best_error_conj:
                            best_error_conj = error_conj
                            best_match_conj = result

    if best_match_cal:
        print(f"\nBest match to V_B_cal = {V_B_CAL} MeV:")
        print(f"  Mechanism: {best_match_cal.mechanism}")
        print(f"  C = {best_match_cal.C:.2f}")
        print(f"  τ = {best_match_cal.params['tau']:.2f} MeV/fm")
        print(f"  V_B = {best_match_cal.V_B:.4f} MeV")
        print(f"  Error: {best_match_cal.V_B_vs_cal_pct:.1f}%")

    if best_match_conj:
        print(f"\nBest match to 2×Δm_np = {V_B_TARGET_B:.4f} MeV:")
        print(f"  Mechanism: {best_match_conj.mechanism}")
        print(f"  C = {best_match_conj.C:.2f}")
        print(f"  τ = {best_match_conj.params['tau']:.2f} MeV/fm")
        print(f"  V_B = {best_match_conj.V_B:.4f} MeV")
        print(f"  Ratio: {best_match_conj.V_B_over_2Dm_B:.4f}")

    return results


# =============================================================================
# OUTPUT FUNCTIONS
# =============================================================================

def save_results_json(results: List[CoreResult], filepath: str):
    """Save results to JSON."""
    data = []
    for r in results:
        d = {
            'mechanism': r.mechanism,
            'C': r.C,
            'E0': r.E0,
            'has_metastability': r.has_metastability,
            'q_n': r.q_n,
            'q_B': r.q_B,
            'V_B': r.V_B,
            'Delta_m': r.Delta_m,
            'V_B_over_2Dm_B': r.V_B_over_2Dm_B,
            'V_B_over_2Dm_A': r.V_B_over_2Dm_A,
            'V_B_vs_cal_pct': r.V_B_vs_cal_pct,
            'params': r.params,
            'notes': r.notes
        }
        data.append(d)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {filepath}")


def save_results_csv(results: List[CoreResult], filepath: str):
    """Save summary to CSV."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'mechanism', 'C', 'E0', 'tau', 'k',
            'q_n', 'q_B', 'V_B', 'Delta_m',
            'V_B_over_2Dm_B', 'V_B_vs_cal_pct', 'has_metastability'
        ])

        for r in results:
            writer.writerow([
                r.mechanism,
                f"{r.C:.4f}",
                f"{r.E0:.4f}",
                f"{r.params['tau']:.2f}",
                f"{r.params['k']:.2f}",
                f"{r.q_n:.4f}" if r.q_n else '',
                f"{r.q_B:.4f}" if r.q_B else '',
                f"{r.V_B:.4f}" if r.V_B else '',
                f"{r.Delta_m:.4f}" if r.Delta_m else '',
                f"{r.V_B_over_2Dm_B:.4f}" if r.V_B_over_2Dm_B else '',
                f"{r.V_B_vs_cal_pct:.2f}" if r.V_B_vs_cal_pct else '',
                r.has_metastability
            ])

    print(f"Saved: {filepath}")


def plot_potential(params: JunctionCoreParams, filepath: str, title: str = None):
    """Plot V_total(q) with components."""
    if not PLOTTING_AVAILABLE:
        print(f"Plotting unavailable. Skipping {filepath}")
        return

    q_values = np.linspace(0, 2.0, 200)
    V_ng_values = [V_NG_warped(q, params.tau, params.L0, params.k) for q in q_values]
    V_core_values = [V_core(q, params) for q in q_values]
    V_total_values = [V_total(q, params) for q in q_values]

    fig, ax = plt.subplots(figsize=(10, 7))

    # Offset V_NG for visibility
    V_ng_offset = V_ng_values[0]
    V_ng_shifted = [v - V_ng_offset for v in V_ng_values]

    ax.plot(q_values, V_ng_shifted, 'b--', linewidth=1.5, alpha=0.7, label='V_NG (shifted)')
    ax.plot(q_values, V_core_values, 'g--', linewidth=1.5, alpha=0.7, label='V_core')
    ax.plot(q_values, [v - V_ng_offset + V_core_values[0] for v in V_total_values],
            'r-', linewidth=2.5, label='V_total')

    # Find and mark extrema
    q_n, q_B = find_extrema(params)
    if q_n is not None:
        V_qn = V_total(q_n, params) - V_ng_offset + V_core_values[0]
        ax.plot(q_n, V_qn, 'o', color='orange', markersize=12, label=f'q_n = {q_n:.3f} fm')
        ax.axvline(q_n, color='orange', linestyle=':', alpha=0.5)

    if q_B is not None:
        V_qB = V_total(q_B, params) - V_ng_offset + V_core_values[0]
        ax.plot(q_B, V_qB, 's', color='red', markersize=12, label=f'q_B = {q_B:.3f} fm')
        ax.axvline(q_B, color='red', linestyle=':', alpha=0.5)

    ax.set_xlabel('q [fm]', fontsize=14)
    ax.set_ylabel('V(q) [MeV] (shifted)', fontsize=14)

    if title:
        ax.set_title(title, fontsize=14)
    else:
        ax.set_title(f'Junction Core Well — Mechanism {params.mechanism}', fontsize=14)

    ax.legend(loc='best', fontsize=11)
    ax.grid(True, alpha=0.3)

    # Parameter box
    param_str = (f"C = {params.C:.2f}, τ = {params.tau:.2f} MeV/fm\n"
                 f"E0 = {params.E0:.4f} MeV, δ = {params.delta:.2f} fm\n"
                 f"σ = {params.sigma:.2f} MeV/fm², k = {params.k:.1f} 1/fm")
    ax.text(0.98, 0.98, param_str, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    # V_B annotation
    if q_n is not None and q_B is not None:
        V_B = V_total(q_B, params) - V_total(q_n, params)
        ratio = V_B / V_B_TARGET_B
        vb_str = f"V_B = {V_B:.3f} MeV\nV_B/(2Δm) = {ratio:.3f}"
        ax.text(0.02, 0.98, vb_str, transform=ax.transAxes, fontsize=11,
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filepath}")


def plot_comparison(results: List[CoreResult], filepath: str):
    """Plot V_B vs C for all mechanisms."""
    if not PLOTTING_AVAILABLE:
        print(f"Plotting unavailable. Skipping {filepath}")
        return

    fig, ax = plt.subplots(figsize=(10, 7))

    colors = {'A1': 'blue', 'A2': 'green', 'A3': 'red'}

    for mech in ['A1', 'A2', 'A3']:
        mech_results = [r for r in results if r.mechanism == mech and r.has_metastability]
        if mech_results:
            C_vals = [r.C for r in mech_results]
            V_B_vals = [r.V_B for r in mech_results]
            ax.scatter(C_vals, V_B_vals, c=colors[mech], label=f'Mechanism {mech}',
                      alpha=0.6, s=30)

    # Target lines
    ax.axhline(V_B_CAL, color='black', linestyle='--', linewidth=2, label=f'V_B_cal = {V_B_CAL} MeV')
    ax.axhline(V_B_TARGET_B, color='purple', linestyle=':', linewidth=2,
               label=f'2×Δm_np = {V_B_TARGET_B:.3f} MeV')

    ax.set_xlabel('C (dimensionless coefficient)', fontsize=14)
    ax.set_ylabel('V_B [MeV]', fontsize=14)
    ax.set_title('Junction Core Well: V_B vs C', fontsize=14)
    ax.set_xscale('log')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)

    # Mark O(1) region
    ax.axvspan(0.5, 2.0, alpha=0.1, color='green', label='O(1) region')

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filepath}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("="*70)
    print("JUNCTION CORE WELL: Geometry-only metastability")
    print("="*70)
    print()

    # Reference values
    print("REFERENCE VALUES [BL]/[Dc]:")
    print(f"  Δm_np (PDG) [BL]:     {DELTA_M_NP_PDG:.6f} MeV")
    print(f"  Δm_np (Book) [Dc]:    {DELTA_M_NP_BOOK:.6f} MeV")
    print(f"  V_B_cal [Cal]:        {V_B_CAL:.3f} MeV")
    print(f"  2×Δm_np (PDG) [Dc]:   {V_B_TARGET_B:.4f} MeV")
    print(f"  2×Δm_np (Book) [Dc]:  {V_B_TARGET_A:.4f} MeV")
    print()

    print("EDC PARAMETERS [Dc]/[I]:")
    print(f"  σ = {SIGMA_EDC:.2f} MeV/fm² (brane tension)")
    print(f"  δ = {DELTA_EDC:.2f} fm (brane thickness)")
    print(f"  E0(C=1) = σ×δ² = {SIGMA_EDC * DELTA_EDC**2:.4f} MeV")
    print()

    all_results = []

    # --- Closure attempt ---
    closure_results = closure_scan()
    all_results.extend(closure_results)

    # --- Extended scan ---
    extended_results = extended_scan()
    all_results.extend(extended_results)

    # --- Targeted scan ---
    targeted_results = targeted_scan()
    all_results.extend(targeted_results)

    # --- Analysis ---
    print("\n" + "="*70)
    print("ANALYSIS")
    print("="*70)

    metastable_results = [r for r in all_results if r.has_metastability]

    print(f"\nTotal configurations tested: {len(all_results)}")
    print(f"Metastable configurations: {len(metastable_results)}")

    # Closure check: metastability for C ~ O(1)?
    closure_meta = [r for r in metastable_results if 0.5 <= r.C <= 2*np.pi]
    print(f"\nClosure check (C in [0.5, 2π]):")
    print(f"  Metastable in O(1) range: {len(closure_meta)}")

    if closure_meta:
        # Best in O(1) range
        best_closure = min(closure_meta, key=lambda r: abs(r.V_B - V_B_TARGET_B) if r.V_B else float('inf'))
        print(f"\n  Best O(1) match to 2×Δm_np:")
        print(f"    Mechanism: {best_closure.mechanism}")
        print(f"    C = {best_closure.C:.2f}")
        print(f"    τ = {best_closure.params['tau']:.2f} MeV/fm")
        print(f"    V_B = {best_closure.V_B:.4f} MeV")
        print(f"    Ratio V_B/(2Δm_np) = {best_closure.V_B_over_2Dm_B:.4f}")
        print(f"    Status: [Dc] — geometry-only with C ~ O(1)")
    else:
        print("  NO metastability found for C ~ O(1)!")
        print("  This indicates C >> 1 may be required [P/Cal]")

    # Overall best match
    if metastable_results:
        best_overall = min(metastable_results,
                          key=lambda r: abs(r.V_B - V_B_TARGET_B) if r.V_B else float('inf'))
        print(f"\nOverall best match to 2×Δm_np:")
        print(f"  Mechanism: {best_overall.mechanism}")
        print(f"  C = {best_overall.C:.2f}")
        print(f"  τ = {best_overall.params['tau']:.2f} MeV/fm")
        print(f"  k = {best_overall.params['k']:.2f} 1/fm")
        print(f"  V_B = {best_overall.V_B:.4f} MeV")
        print(f"  Ratio = {best_overall.V_B_over_2Dm_B:.4f}")

        if best_overall.C > 10:
            print(f"  Status: [P/Cal] — requires C >> 1")
        else:
            print(f"  Status: [Dc] — C ~ O(1)")

        # Generate plot for best match
        params_best = JunctionCoreParams(
            mechanism=best_overall.mechanism,
            C=best_overall.C,
            sigma=best_overall.params['sigma'],
            delta=best_overall.params['delta'],
            tau=best_overall.params['tau'],
            L0=best_overall.params['L0'],
            k=best_overall.params['k']
        )
        plot_potential(params_best,
                      "derivations/figures/junction_core_Vtotal_best.png",
                      f"Best Match: {best_overall.mechanism}, C={best_overall.C:.1f}")

    # --- Save outputs ---
    print("\n" + "="*70)
    print("SAVING OUTPUTS")
    print("="*70)

    save_results_json(all_results, "derivations/artifacts/junction_core_results.json")
    save_results_csv(all_results, "derivations/artifacts/junction_core_results.csv")

    # Comparison plot
    plot_comparison(all_results, "derivations/figures/junction_core_V_B_vs_C.png")

    # Individual mechanism plots for C ~ O(1)
    for mech in ['A1', 'A2', 'A3']:
        # Find best O(1) example for this mechanism
        mech_closure = [r for r in closure_meta if r.mechanism == mech] if closure_meta else []
        if mech_closure:
            best_mech = mech_closure[0]
            params_mech = JunctionCoreParams(
                mechanism=mech,
                C=best_mech.C,
                sigma=SIGMA_EDC,
                delta=DELTA_EDC,
                tau=best_mech.params['tau'],
                L0=L0_EDC,
                k=best_mech.params['k']
            )
            plot_potential(params_mech,
                          f"derivations/figures/junction_core_Vtotal_{mech}_closure.png",
                          f"Mechanism {mech}: C={best_mech.C:.2f}, τ={best_mech.params['tau']:.1f}")

    # --- Summary ---
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    print(f"""
Junction Core Well Analysis Complete
=====================================

Tested configurations: {len(all_results)}
Metastable found: {len(metastable_results)}
Metastable with C ~ O(1): {len(closure_meta)}

Core energy scale:
  E0 = C × σ × δ² = C × {SIGMA_EDC:.2f} × {DELTA_EDC}² = C × {SIGMA_EDC * DELTA_EDC**2:.4f} MeV

Mechanisms tested:
  A1: Overlap/regularization — V_core = -E0 exp(-(q/δ)²)
  A2: Junction rim (line) — same form, different interpretation
  A3: Curvature core (Lorentzian) — V_core = -E0/(1+(q/δ)²)

Key findings:""")

    if closure_meta:
        print(f"""
  [SUCCESS] Metastability EXISTS for C ~ O(1)!
  Best closure result:
    - Mechanism: {best_closure.mechanism}
    - C = {best_closure.C:.2f}
    - V_B = {best_closure.V_B:.4f} MeV
    - Ratio V_B/(2Δm_np) = {best_closure.V_B_over_2Dm_B:.4f}

  Status: [Dc] — geometry-only junction core can produce metastability
  with dimensionless coefficient C ~ O(1), built from existing scales (σ, δ).
""")
    else:
        print("""
  [PARTIAL] No metastability for C ~ O(1).
  Metastability requires C >> 1, making this [P/Cal] rather than [Dc].

  Consider:
    1. Different profile functions
    2. Including brane tension contribution
    3. Warped metric effects
""")

    print(f"""
Decision outcome:
  - If C ~ O(1) works: strong [Dc] result, path to [Der] via geometric derivation
  - If C >> 1 needed: [P/Cal] leaning, similar to phenomenological node well
  - If no metastability: no-go for geometry-only, need bulk field coupling

Next steps:
  1. If [Dc]: derive C from junction geometry (angles, curvature at vertex)
  2. If [P/Cal]: document as improvement over arbitrary V_node_0 fitting
  3. If no-go: proceed to bulk field coupling as last mechanism
""")

    print("="*70)
    print("JUNCTION CORE WELL EXECUTION COMPLETE")
    print("="*70)


if __name__ == "__main__":
    main()
