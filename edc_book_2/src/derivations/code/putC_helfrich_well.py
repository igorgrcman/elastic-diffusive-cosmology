#!/usr/bin/env python3
"""
PUT C HELFRICH: Compute V_bend(q) from Helfrich bending term
=============================================================

This script computes the bending energy contribution to V(q) when the
Y-junction node displaces into the bulk, creating a dimple in the brane.

Levels of approximation:
  Level 1: Scaling / analytic toy model [Dc]
  Level 2: Variational ansatz with explicit profile [Dc]
  Level 3: Numerical shape minimization [Dc/P] (optional)

Key parameter closure:
  κ = C_κ × σ × δ²  [Dc] (dimensional analysis)

Epistemic Status:
  - Helfrich functional: [Def]
  - Monge gauge approximation: [Dc]
  - Parameter closure κ ~ σδ²: [Dc]
  - Profile ansatz: [I]
  - Numerical results: [Cal]

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
    from scipy.optimize import minimize, brentq
    from scipy.integrate import quad, dblquad
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

M_E_MEV = 0.51099895  # Electron mass [MeV] [BL]
ALPHA = 1.0 / 137.035999084  # Fine structure constant [BL]

# Δm_np options
DELTA_M_NP_PDG = 1.29333236  # MeV [BL] (Option B)
DELTA_M_NP_BOOK = (5.0/2.0 + 4.0*ALPHA) * M_E_MEV  # MeV [Dc] (Option A)

# Calibrated barrier height
V_B_CAL = 2.6  # MeV [Cal]

# Z3 conjecture predictions
V_B_CONJ_B = 2.0 * DELTA_M_NP_PDG  # MeV [Dc]
V_B_CONJ_A = 2.0 * DELTA_M_NP_BOOK  # MeV [Dc]


# =============================================================================
# BRANE PARAMETERS [Dc] — from existing repo
# =============================================================================

# Brane tension (from book: E_σ = m_e c²/α hypothesis)
SIGMA_DEFAULT = 8.82  # MeV/fm² [Dc]

# Brane thickness (characteristic scale)
DELTA_DEFAULT = 0.1  # fm [P] (order of magnitude)

# String tension for legs (use same order as sigma for consistency)
TAU_DEFAULT = 5.0  # MeV/fm [I]

# In-brane leg projection
L0_DEFAULT = 1.0  # fm [I] (nucleon scale)


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class HelfrichParameters:
    """Parameters for Helfrich model."""
    name: str
    sigma: float     # Brane tension [MeV/fm²]
    delta: float     # Brane thickness [fm]
    C_kappa: float   # Dimensionless coefficient for κ
    c0: float        # Spontaneous curvature [1/fm]
    a: float         # Dimple characteristic radius [fm]
    tau: float       # String tension [MeV/fm]
    L0: float        # In-brane leg projection [fm]

    @property
    def kappa(self) -> float:
        """Bending rigidity κ = C_κ × σ × δ² [MeV]"""
        return self.C_kappa * self.sigma * self.delta**2

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d['kappa'] = self.kappa
        return d


@dataclass
class HelfrichResult:
    """Results from Helfrich computation."""
    variant: str
    level: str  # "L1", "L2", "L3"
    params: Dict[str, Any]

    # Potential curves
    q_values: List[float]
    V_bend_values: List[float]
    V_NG_values: List[float]
    V_total_values: List[float]

    # Critical points
    q_0: Optional[float]  # Proton (ground state)
    q_n: Optional[float]  # Neutron (metastable min)
    q_B: Optional[float]  # Barrier (saddle)

    # Energies
    V_at_q0: Optional[float]
    V_at_qn: Optional[float]
    V_at_qB: Optional[float]
    V_B: Optional[float]

    # Comparisons
    V_B_vs_cal_pct: Optional[float]
    V_B_vs_conj_A_pct: Optional[float]
    V_B_vs_conj_B_pct: Optional[float]

    # Status
    has_metastability: bool
    notes: str


# =============================================================================
# LEVEL 1: SCALING / ANALYTIC TOY MODEL [Dc]
# =============================================================================

def level1_V_bend(q: float, params: HelfrichParameters) -> float:
    """
    Level 1: Scaling estimate for bending energy.

    Model [Dc]:
      Dimple of depth q and radius a.
      Mean curvature H ~ q/a² in the dimple region.

      E_bend ≈ (κ/2) × (2H - c0)² × πa²
             = (κ/2) × (2q/a² - c0)² × πa²

    For c0 = 0:
      E_bend = (κ/2) × (4q²/a⁴) × πa² = 2πκq²/a²

    For c0 ≠ 0:
      E_bend = (κ/2) × (4q²/a⁴ - 4c0·q/a² + c0²) × πa²
             = 2πκq²/a² - 2πκc0·q + (πκc0²a²/2)
             = A·q² - B·q + C

    where A = 2πκ/a², B = 2πκc0, C = πκc0²a²/2
    """
    kappa = params.kappa
    a = params.a
    c0 = params.c0

    # Coefficients
    A = 2 * np.pi * kappa / a**2
    B = 2 * np.pi * kappa * c0
    C = 0.5 * np.pi * kappa * c0**2 * a**2

    E_bend = A * q**2 - B * q + C

    return E_bend


def level1_V_bend_derivative(q: float, params: HelfrichParameters) -> float:
    """First derivative of V_bend for Level 1."""
    kappa = params.kappa
    a = params.a
    c0 = params.c0

    A = 2 * np.pi * kappa / a**2
    B = 2 * np.pi * kappa * c0

    return 2 * A * q - B


def level1_minimum_q(params: HelfrichParameters) -> Optional[float]:
    """
    Find minimum of V_bend alone (Level 1).

    For c0 ≠ 0:
      dE_bend/dq = 4πκq/a² - 2πκc0 = 0
      → q_min = c0·a²/2

    This is positive only if c0 > 0.
    """
    c0 = params.c0
    a = params.a

    if c0 > 0:
        return c0 * a**2 / 2
    return None


# =============================================================================
# LEVEL 2: VARIATIONAL ANSATZ [Dc]
# =============================================================================

def profile_polynomial(r: np.ndarray, q: float, a: float) -> np.ndarray:
    """
    Polynomial profile ansatz: w(r) = q × (1 - (r/a)²)² for r < a, 0 otherwise.

    Properties [Dc]:
      - w(0) = q (node depth)
      - w(a) = 0 (smooth transition)
      - w'(a) = 0 (smooth derivative)
      - w''(0) = -4q/a² (curvature at center)
    """
    w = np.where(r < a, q * (1 - (r/a)**2)**2, 0.0)
    return w


def profile_gaussian(r: np.ndarray, q: float, a: float) -> np.ndarray:
    """
    Gaussian profile ansatz: w(r) = q × exp(-r²/a²)

    Properties [Dc]:
      - w(0) = q
      - w(r→∞) → 0
      - ∇²w(0) = -4q/a² (curvature at center)
    """
    return q * np.exp(-(r/a)**2)


def profile_bessel_like(r: np.ndarray, q: float, a: float) -> np.ndarray:
    """
    Bessel-like profile (capped at r=a): w(r) = q × cos²(πr/2a) for r < a

    Properties [Dc]:
      - w(0) = q
      - w(a) = 0
      - Smooth cosine transition
    """
    w = np.where(r < a, q * np.cos(np.pi * r / (2*a))**2, 0.0)
    return w


def compute_laplacian_axisym(r: np.ndarray, w: np.ndarray) -> np.ndarray:
    """
    Compute ∇²w = w'' + w'/r in axisymmetric coordinates.

    Uses finite differences.
    """
    dr = r[1] - r[0] if len(r) > 1 else 1e-6
    n = len(r)

    laplacian = np.zeros(n)

    for i in range(1, n-1):
        w_pp = (w[i+1] - 2*w[i] + w[i-1]) / dr**2
        w_p = (w[i+1] - w[i-1]) / (2*dr)
        if r[i] > 1e-10:
            laplacian[i] = w_pp + w_p / r[i]
        else:
            # At r=0, use L'Hopital: lim(w'/r) = w''
            laplacian[i] = 2 * w_pp

    # Boundary handling
    if n > 2:
        # At r=0: w'/r → w''(0) by L'Hopital, so ∇²w(0) = 2w''(0)
        w_pp_0 = (w[2] - 2*w[1] + w[0]) / dr**2 if n > 2 else 0
        laplacian[0] = 2 * w_pp_0

        # At r=R: extrapolate
        laplacian[-1] = laplacian[-2]

    return laplacian


def level2_E_bend_for_profile(q: float, params: HelfrichParameters,
                              profile_func, n_points: int = 200) -> float:
    """
    Compute E_bend for a given profile ansatz.

    E_bend = (κ/2) ∫ 2πr dr (∇²w - c0)²
    """
    kappa = params.kappa
    a = params.a
    c0 = params.c0

    # Integration domain: r ∈ [0, 3a] to capture decay
    R_max = 3 * a
    r = np.linspace(0, R_max, n_points)
    dr = r[1] - r[0]

    # Compute profile
    w = profile_func(r, q, a)

    # Compute Laplacian
    lap_w = compute_laplacian_axisym(r, w)

    # Integrand: (κ/2) × (∇²w - c0)² × 2πr
    integrand = (kappa / 2) * (lap_w - c0)**2 * 2 * np.pi * r

    # Integrate (trapezoidal)
    E_bend = np.trapz(integrand, r)

    return E_bend


def level2_V_bend(q: float, params: HelfrichParameters,
                  profile: str = "polynomial") -> float:
    """
    Level 2: Variational bending energy with explicit profile.

    Profiles available:
      "polynomial" — (1-(r/a)²)² [Dc]
      "gaussian" — exp(-r²/a²) [Dc]
      "bessel" — cos²(πr/2a) [Dc]
    """
    profile_funcs = {
        "polynomial": profile_polynomial,
        "gaussian": profile_gaussian,
        "bessel": profile_bessel_like
    }

    if profile not in profile_funcs:
        profile = "polynomial"

    return level2_E_bend_for_profile(q, params, profile_funcs[profile])


def level2_V_bend_best(q: float, params: HelfrichParameters) -> Tuple[float, str]:
    """
    Compute V_bend using the profile that gives lowest energy (variational).
    Returns (E_bend, profile_name).
    """
    results = {}
    for profile in ["polynomial", "gaussian", "bessel"]:
        results[profile] = level2_V_bend(q, params, profile)

    best_profile = min(results, key=results.get)
    return results[best_profile], best_profile


# =============================================================================
# NAMBU-GOTO LEG CONTRIBUTION (from Put C baseline)
# =============================================================================

def V_NG(q: float, params: HelfrichParameters) -> float:
    """
    Nambu-Goto leg contribution to V(q).

    V_NG(q) = 3 × τ × L_leg(q) = 3τ√(L0² + q²)  [Dc]

    (Three identical legs by Z₃ symmetry)
    """
    L_leg = np.sqrt(params.L0**2 + q**2)
    return 3 * params.tau * L_leg


def V_NG_derivative(q: float, params: HelfrichParameters) -> float:
    """Derivative of V_NG."""
    L_leg = np.sqrt(params.L0**2 + q**2)
    return 3 * params.tau * q / L_leg


# =============================================================================
# TOTAL POTENTIAL AND EXTREMUM FINDING
# =============================================================================

def V_total(q: float, params: HelfrichParameters, level: str = "L2",
            profile: str = "polynomial") -> float:
    """
    Total potential: V_total(q) = V_NG(q) + V_bend(q)
    """
    V_ng = V_NG(q, params)

    if level == "L1":
        V_bend = level1_V_bend(q, params)
    else:  # L2
        V_bend = level2_V_bend(q, params, profile)

    return V_ng + V_bend


def dV_total(q: float, params: HelfrichParameters, level: str = "L2",
             profile: str = "polynomial", eps: float = 1e-6) -> float:
    """Numerical derivative of V_total."""
    if q < eps:
        return (V_total(eps, params, level, profile) -
                V_total(0, params, level, profile)) / eps
    return (V_total(q + eps, params, level, profile) -
            V_total(q - eps, params, level, profile)) / (2 * eps)


def d2V_total(q: float, params: HelfrichParameters, level: str = "L2",
              profile: str = "polynomial", eps: float = 1e-5) -> float:
    """Second derivative of V_total."""
    return (V_total(q + eps, params, level, profile) -
            2*V_total(q, params, level, profile) +
            V_total(q - eps, params, level, profile)) / eps**2


def find_extrema(params: HelfrichParameters, level: str = "L2",
                 profile: str = "polynomial", q_max: float = 2.0) -> Tuple[Optional[float], Optional[float]]:
    """
    Find stationary points of V_total.

    Returns (q_n, q_B):
      q_n: metastable minimum (if exists)
      q_B: barrier maximum (if exists, with q_B < q_n)
    """
    if not SCIPY_AVAILABLE:
        # Simple scan
        n = 100
        dq = q_max / n
        q_n, q_B = None, None

        prev_dV = dV_total(dq, params, level, profile)
        for i in range(2, n):
            q = i * dq
            curr_dV = dV_total(q, params, level, profile)

            if prev_dV > 0 and curr_dV < 0:
                q_B = q - 0.5 * dq
            elif prev_dV < 0 and curr_dV > 0:
                q_n = q - 0.5 * dq

            prev_dV = curr_dV

        return q_n, q_B

    # Scipy-based
    def dV_func(q):
        if q < 1e-10:
            q = 1e-10
        return dV_total(q, params, level, profile)

    n = 60
    q_grid = np.linspace(0.01, q_max, n)
    dV_grid = [dV_func(q) for q in q_grid]

    q_n, q_B = None, None

    for i in range(len(q_grid) - 1):
        if dV_grid[i] * dV_grid[i+1] < 0:
            try:
                q_root = brentq(dV_func, q_grid[i], q_grid[i+1])
                d2V = d2V_total(q_root, params, level, profile)

                if d2V > 0:
                    if q_n is None or q_root > q_n:
                        q_n = q_root
                else:
                    if q_B is None:
                        q_B = q_root
            except:
                pass

    # Ensure q_B < q_n for proper metastability
    if q_n is not None and q_B is not None and q_B > q_n:
        q_n, q_B = None, None

    return q_n, q_B


# =============================================================================
# MAIN COMPUTATION FUNCTION
# =============================================================================

def compute_helfrich_variant(params: HelfrichParameters, level: str = "L2",
                             profile: str = "polynomial",
                             q_max: float = 2.0, n_points: int = 200) -> HelfrichResult:
    """
    Compute V_total(q) for a given Helfrich parameter set.
    """
    q_values = np.linspace(0, q_max, n_points)

    # Compute potential components
    V_bend_values = []
    V_NG_values = []
    V_total_values = []

    for q in q_values:
        v_ng = V_NG(q, params)
        if level == "L1":
            v_bend = level1_V_bend(q, params)
        else:
            v_bend = level2_V_bend(q, params, profile)
        V_NG_values.append(v_ng)
        V_bend_values.append(v_bend)
        V_total_values.append(v_ng + v_bend)

    # Ground state at q=0
    q_0 = 0.0
    V_at_q0 = V_total_values[0]

    # Find extrema
    q_n, q_B = find_extrema(params, level, profile, q_max)

    has_metastability = (q_n is not None and q_B is not None and
                         q_B < q_n and q_B > 0)

    # Compute derived quantities
    V_at_qn = None
    V_at_qB = None
    V_B = None
    V_B_vs_cal_pct = None
    V_B_vs_conj_A_pct = None
    V_B_vs_conj_B_pct = None

    if q_n is not None:
        V_at_qn = V_total(q_n, params, level, profile)

    if q_B is not None:
        V_at_qB = V_total(q_B, params, level, profile)

    if has_metastability:
        V_B = V_at_qB - V_at_qn
        if V_B > 0:
            V_B_vs_cal_pct = (V_B - V_B_CAL) / V_B_CAL * 100
            V_B_vs_conj_A_pct = (V_B - V_B_CONJ_A) / V_B_CONJ_A * 100
            V_B_vs_conj_B_pct = (V_B - V_B_CONJ_B) / V_B_CONJ_B * 100

    # Generate notes
    if has_metastability:
        notes = (f"Helfrich {level} ({profile}): Metastability FOUND. "
                 f"q_B={q_B:.4f}, q_n={q_n:.4f}, V_B={V_B:.4f} MeV. "
                 f"κ={params.kappa:.4f} MeV, c0={params.c0:.4f} /fm.")
    else:
        if q_n is None and q_B is None:
            notes = (f"Helfrich {level} ({profile}): No metastability. "
                     f"V_total(q) monotonically increasing. "
                     f"κ={params.kappa:.4f} MeV, c0={params.c0:.4f} /fm.")
        elif q_B is not None and q_n is None:
            notes = (f"Helfrich {level} ({profile}): Found barrier at q_B={q_B:.4f} "
                     f"but no subsequent minimum.")
        else:
            notes = (f"Helfrich {level} ({profile}): Unusual landscape. "
                     f"q_n={q_n}, q_B={q_B}.")

    return HelfrichResult(
        variant=f"helfrich_{level}_{profile}",
        level=level,
        params=params.to_dict(),
        q_values=list(q_values),
        V_bend_values=V_bend_values,
        V_NG_values=V_NG_values,
        V_total_values=V_total_values,
        q_0=q_0,
        q_n=q_n,
        q_B=q_B,
        V_at_q0=V_at_q0,
        V_at_qn=V_at_qn,
        V_at_qB=V_at_qB,
        V_B=V_B,
        V_B_vs_cal_pct=V_B_vs_cal_pct,
        V_B_vs_conj_A_pct=V_B_vs_conj_A_pct,
        V_B_vs_conj_B_pct=V_B_vs_conj_B_pct,
        has_metastability=has_metastability,
        notes=notes
    )


# =============================================================================
# PARAMETER SCANS
# =============================================================================

def scan_c0_values(params_base: HelfrichParameters, level: str = "L2",
                   profile: str = "polynomial") -> List[HelfrichResult]:
    """
    Scan over spontaneous curvature c0 values.

    c0 > 0 is needed for the bending term to provide a "well" (local minimum).
    """
    results = []

    # c0 values in units of 1/δ
    c0_factors = [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0]

    for c0_factor in c0_factors:
        c0 = c0_factor / params_base.delta

        params = HelfrichParameters(
            name=f"c0_scan_{c0_factor}",
            sigma=params_base.sigma,
            delta=params_base.delta,
            C_kappa=params_base.C_kappa,
            c0=c0,
            a=params_base.a,
            tau=params_base.tau,
            L0=params_base.L0
        )

        result = compute_helfrich_variant(params, level, profile)
        results.append(result)

    return results


def scan_C_kappa_values(params_base: HelfrichParameters, level: str = "L2",
                        profile: str = "polynomial") -> List[HelfrichResult]:
    """
    Scan over dimensionless bending rigidity coefficient C_κ.
    """
    results = []

    C_kappa_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]

    for C_kappa in C_kappa_values:
        params = HelfrichParameters(
            name=f"Ckappa_scan_{C_kappa}",
            sigma=params_base.sigma,
            delta=params_base.delta,
            C_kappa=C_kappa,
            c0=params_base.c0,
            a=params_base.a,
            tau=params_base.tau,
            L0=params_base.L0
        )

        result = compute_helfrich_variant(params, level, profile)
        results.append(result)

    return results


def comprehensive_scan() -> List[HelfrichResult]:
    """
    Comprehensive parameter scan over (C_κ, c0, τ, a) space.
    """
    results = []

    # Base values
    sigma = SIGMA_DEFAULT
    delta = DELTA_DEFAULT
    L0 = L0_DEFAULT

    # Scan ranges
    C_kappa_values = [0.5, 1.0, 2.0, 5.0]
    c0_factors = [0.0, 1.0, 2.0, 5.0, 10.0]  # in units of 1/δ
    tau_values = [1.0, 2.0, 5.0, 10.0]
    a_factors = [0.5, 1.0, 2.0]  # in units of δ

    for C_kappa in C_kappa_values:
        for c0_factor in c0_factors:
            for tau in tau_values:
                for a_factor in a_factors:
                    c0 = c0_factor / delta
                    a = a_factor * delta

                    params = HelfrichParameters(
                        name=f"scan_Ck{C_kappa}_c0f{c0_factor}_tau{tau}_af{a_factor}",
                        sigma=sigma,
                        delta=delta,
                        C_kappa=C_kappa,
                        c0=c0,
                        a=a,
                        tau=tau,
                        L0=L0
                    )

                    result = compute_helfrich_variant(params, "L2", "polynomial",
                                                      q_max=3.0, n_points=100)
                    results.append(result)

    return results


# =============================================================================
# OUTPUT FUNCTIONS
# =============================================================================

def save_results_json(results: List[HelfrichResult], filepath: str):
    """Save results to JSON."""
    data = []
    for r in results:
        d = {
            'variant': r.variant,
            'level': r.level,
            'params': r.params,
            'q_0': r.q_0,
            'q_n': r.q_n,
            'q_B': r.q_B,
            'V_at_q0': r.V_at_q0,
            'V_at_qn': r.V_at_qn,
            'V_at_qB': r.V_at_qB,
            'V_B': r.V_B,
            'V_B_vs_cal_pct': r.V_B_vs_cal_pct,
            'V_B_vs_conj_A_pct': r.V_B_vs_conj_A_pct,
            'V_B_vs_conj_B_pct': r.V_B_vs_conj_B_pct,
            'has_metastability': r.has_metastability,
            'notes': r.notes
        }
        data.append(d)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Results saved to {filepath}")


def save_results_csv(results: List[HelfrichResult], filepath: str):
    """Save summary to CSV."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'variant', 'level', 'kappa', 'c0', 'a', 'tau',
            'q_B', 'q_n', 'V_B', 'V_B_vs_cal_pct', 'has_metastability'
        ])

        for r in results:
            writer.writerow([
                r.variant,
                r.level,
                f"{r.params.get('kappa', 0):.6f}",
                f"{r.params.get('c0', 0):.4f}",
                f"{r.params.get('a', 0):.4f}",
                f"{r.params.get('tau', 0):.2f}",
                f"{r.q_B:.6f}" if r.q_B else '',
                f"{r.q_n:.6f}" if r.q_n else '',
                f"{r.V_B:.6f}" if r.V_B else '',
                f"{r.V_B_vs_cal_pct:.2f}" if r.V_B_vs_cal_pct else '',
                r.has_metastability
            ])

    print(f"Results saved to {filepath}")


def plot_V_bend(result: HelfrichResult, filepath: str):
    """Plot V_bend(q) alone."""
    if not PLOTTING_AVAILABLE:
        return

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(result.q_values, result.V_bend_values, 'b-', linewidth=2,
            label=f'V_bend(q) [{result.level}]')

    ax.set_xlabel('q [fm]', fontsize=12)
    ax.set_ylabel('V_bend(q) [MeV]', fontsize=12)
    ax.set_title(f'Helfrich Bending Energy — {result.variant}', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Parameter info
    p = result.params
    info = f"κ={p['kappa']:.4f} MeV, c₀={p['c0']:.2f}/fm, a={p['a']:.2f} fm"
    ax.text(0.02, 0.98, info, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(facecolor='wheat', alpha=0.5))

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {filepath}")


def plot_V_total(result: HelfrichResult, filepath: str):
    """Plot V_total(q) with components and extrema marked."""
    if not PLOTTING_AVAILABLE:
        return

    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot components
    ax.plot(result.q_values, result.V_NG_values, 'g--', linewidth=1.5,
            alpha=0.7, label='V_NG(q)')
    ax.plot(result.q_values, result.V_bend_values, 'b--', linewidth=1.5,
            alpha=0.7, label='V_bend(q)')
    ax.plot(result.q_values, result.V_total_values, 'r-', linewidth=2.5,
            label='V_total(q)')

    # Mark extrema
    if result.q_0 is not None:
        ax.axvline(result.q_0, color='green', linestyle=':', alpha=0.5)
        ax.plot(result.q_0, result.V_at_q0, 'go', markersize=10,
                label=f'q₀={result.q_0:.2f} (proton)')

    if result.q_B is not None:
        ax.axvline(result.q_B, color='orange', linestyle=':', alpha=0.5)
        ax.plot(result.q_B, result.V_at_qB, 's', color='orange', markersize=10,
                label=f'q_B={result.q_B:.3f} (barrier)')

    if result.q_n is not None:
        ax.axvline(result.q_n, color='red', linestyle=':', alpha=0.5)
        ax.plot(result.q_n, result.V_at_qn, 'r^', markersize=10,
                label=f'q_n={result.q_n:.3f} (neutron)')

    ax.set_xlabel('q [fm]', fontsize=12)
    ax.set_ylabel('V(q) [MeV]', fontsize=12)
    ax.set_title(f'Total Potential — {result.variant}', fontsize=14)
    ax.legend(loc='best', fontsize=9)
    ax.grid(True, alpha=0.3)

    # Parameter info
    p = result.params
    info = f"κ={p['kappa']:.4f} MeV, c₀={p['c0']:.2f}/fm, a={p['a']:.2f} fm, τ={p['tau']:.1f} MeV/fm"
    ax.text(0.02, 0.98, info, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(facecolor='wheat', alpha=0.5))

    if result.V_B is not None:
        vb_info = f"V_B = {result.V_B:.3f} MeV"
        ax.text(0.98, 0.98, vb_info, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(facecolor='lightgreen', alpha=0.7))

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {filepath}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("="*70)
    print("PUT C HELFRICH: Bending Term Analysis")
    print("="*70)
    print()

    # Reference values
    print("REFERENCE VALUES:")
    print(f"  σ (brane tension) [Dc]:  {SIGMA_DEFAULT:.2f} MeV/fm²")
    print(f"  δ (brane thickness) [P]: {DELTA_DEFAULT:.2f} fm")
    print(f"  Δm_np (PDG) [BL]:        {DELTA_M_NP_PDG:.6f} MeV")
    print(f"  Δm_np (Book) [Dc]:       {DELTA_M_NP_BOOK:.6f} MeV")
    print(f"  V_B_cal [Cal]:           {V_B_CAL:.3f} MeV")
    print(f"  2×Δm_np (conj A) [Dc]:   {V_B_CONJ_A:.4f} MeV")
    print(f"  2×Δm_np (conj B) [Dc]:   {V_B_CONJ_B:.4f} MeV")
    print()

    all_results = []

    # --- BASELINE: c0 = 0 (best-case closure) ---
    print("="*70)
    print("CASE 1: c0 = 0 (No spontaneous curvature)")
    print("="*70)

    params_c0_zero = HelfrichParameters(
        name="baseline_c0_zero",
        sigma=SIGMA_DEFAULT,
        delta=DELTA_DEFAULT,
        C_kappa=1.0,  # [Dc] O(1) coefficient
        c0=0.0,       # No spontaneous curvature
        a=DELTA_DEFAULT,  # a ~ δ [I]
        tau=TAU_DEFAULT,
        L0=L0_DEFAULT
    )

    print(f"\nParameters:")
    print(f"  κ = C_κ × σ × δ² = 1.0 × {SIGMA_DEFAULT} × {DELTA_DEFAULT}² = {params_c0_zero.kappa:.6f} MeV")
    print(f"  c0 = 0 (no spontaneous curvature)")
    print(f"  a = δ = {DELTA_DEFAULT} fm")
    print(f"  τ = {TAU_DEFAULT} MeV/fm")

    # Level 1
    result_L1_c0_zero = compute_helfrich_variant(params_c0_zero, "L1")
    all_results.append(result_L1_c0_zero)
    print(f"\nLevel 1 (scaling): {result_L1_c0_zero.notes}")

    # Level 2
    result_L2_c0_zero = compute_helfrich_variant(params_c0_zero, "L2", "polynomial")
    all_results.append(result_L2_c0_zero)
    print(f"Level 2 (polynomial): {result_L2_c0_zero.notes}")

    # --- CASE 2: c0 ≠ 0 (spontaneous curvature scan) ---
    print("\n" + "="*70)
    print("CASE 2: c0 ≠ 0 (Spontaneous curvature scan)")
    print("="*70)

    c0_scan_results = scan_c0_values(params_c0_zero, "L2", "polynomial")
    all_results.extend(c0_scan_results)

    print("\nc0 scan results:")
    for r in c0_scan_results:
        c0_val = r.params['c0']
        c0_factor = c0_val * DELTA_DEFAULT
        status = "METASTABLE" if r.has_metastability else "no metastability"
        vb_str = f"V_B={r.V_B:.3f}" if r.V_B else "—"
        print(f"  c0 = {c0_factor:.1f}/δ = {c0_val:.1f}/fm: {status}, {vb_str}")

    # --- COMPREHENSIVE SCAN ---
    print("\n" + "="*70)
    print("COMPREHENSIVE PARAMETER SCAN")
    print("="*70)

    scan_results = comprehensive_scan()
    all_results.extend(scan_results)

    metastable_results = [r for r in scan_results if r.has_metastability]
    print(f"\nScanned {len(scan_results)} parameter combinations")
    print(f"Found {len(metastable_results)} metastable configurations")

    # --- BEST MATCHES ---
    if metastable_results:
        print("\n" + "="*70)
        print("BEST MATCHES")
        print("="*70)

        # Best match to V_B_cal
        best_cal = min(metastable_results,
                       key=lambda r: abs(r.V_B - V_B_CAL) if r.V_B else float('inf'))
        print(f"\nBest match to V_B_cal = {V_B_CAL} MeV:")
        print(f"  κ = {best_cal.params['kappa']:.4f} MeV")
        print(f"  c0 = {best_cal.params['c0']:.2f} /fm")
        print(f"  a = {best_cal.params['a']:.2f} fm")
        print(f"  τ = {best_cal.params['tau']:.1f} MeV/fm")
        print(f"  V_B = {best_cal.V_B:.4f} MeV (error: {best_cal.V_B_vs_cal_pct:.1f}%)")

        # Best match to 2×Δm_np
        best_conj = min(metastable_results,
                        key=lambda r: abs(r.V_B - V_B_CONJ_B) if r.V_B else float('inf'))
        print(f"\nBest match to 2×Δm_np = {V_B_CONJ_B:.4f} MeV:")
        print(f"  κ = {best_conj.params['kappa']:.4f} MeV")
        print(f"  c0 = {best_conj.params['c0']:.2f} /fm")
        print(f"  V_B = {best_conj.V_B:.4f} MeV (error: {best_conj.V_B_vs_conj_B_pct:.1f}%)")

        # Plot best result
        plot_V_total(best_cal, "derivations/figures/helfrich_Vtotal_best_cal.png")
        plot_V_bend(best_cal, "derivations/figures/helfrich_Vbend_best_cal.png")
    else:
        print("\nNo metastable configurations found.")
        print("Helfrich term alone (with tested parameters) does NOT produce metastability.")

    # --- ANALYSIS: Why c0 = 0 fails ---
    print("\n" + "="*70)
    print("ANALYSIS: Why c0 = 0 fails")
    print("="*70)
    print("""
With c0 = 0:
  V_bend(q) = (κ/2) ∫ (∇²w)² dA ~ κ q²/a²  [always positive]
  V_NG(q) = 3τ√(L0² + q²)  [always increasing]

Both terms are POSITIVE and INCREASING with q.
→ V_total(q) = V_NG(q) + V_bend(q) is monotonically increasing.
→ NO metastability possible with c0 = 0.

For metastability, need c0 > 0:
  V_bend(q) ~ κ(q²/a² - 2c0·q + c0²a²/2)
            = κ[(q - c0·a²)²/a² + (c0²a²/2 - c0²a²)]

The linear term -2κc0·q provides NEGATIVE contribution that can
compete with the positive NG stretching cost, potentially creating
a local minimum.

Key finding: Helfrich with c0=0 is a NO-GO. Need c0 ≠ 0 or alternative mechanism.
""")

    # --- SAVE OUTPUTS ---
    print("\n" + "="*70)
    print("SAVING OUTPUTS")
    print("="*70)

    save_results_json(all_results, "derivations/artifacts/helfrich_results.json")
    save_results_csv(all_results, "derivations/artifacts/helfrich_results.csv")

    # Plots for baseline cases
    plot_V_total(result_L1_c0_zero, "derivations/figures/helfrich_Vtotal_L1_c0zero.png")
    plot_V_total(result_L2_c0_zero, "derivations/figures/helfrich_Vtotal_L2_c0zero.png")

    # Plot for representative c0 ≠ 0 case (if metastable)
    for r in c0_scan_results:
        if r.has_metastability:
            plot_V_total(r, f"derivations/figures/helfrich_Vtotal_c0_{r.params['c0']:.1f}.png")
            break

    # --- SUMMARY ---
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    n_meta = len([r for r in all_results if r.has_metastability])

    print(f"""
Results:
  Total configurations tested: {len(all_results)}
  Metastable configurations:   {n_meta}

Case 1 (c0 = 0, best-case closure):
  Status: NO METASTABILITY
  Reason: V_bend ~ +q² adds to NG stretching cost; no mechanism for well.
  Conclusion: c0 = 0 is a NO-GO for Helfrich-only metastability.

Case 2 (c0 ≠ 0, spontaneous curvature):
  Status: {'METASTABILITY POSSIBLE' if n_meta > 0 else 'NO METASTABILITY'}
  Mechanism: Linear term -2κc0·q competes with stretching cost.
  Requirement: c0 must be [P] (not derived from geometry alone).

CRITICAL CONCLUSION:
  Helfrich term with κ = σδ² [Dc] does NOT produce metastability
  without additional assumption (c0 ≠ 0).

  If c0 ≠ 0 is acceptable as [P], metastability can emerge.
  If c0 must be derived, Helfrich-only route is insufficient.

OPEN for [Der] closure:
  1) Derive c0 from brane geometry (mean curvature of background?)
  2) Or: proceed to junction core model (alternative mechanism)
""")

    print("="*70)
    print("HELFRICH EXECUTION COMPLETE")
    print("="*70)


if __name__ == "__main__":
    main()
