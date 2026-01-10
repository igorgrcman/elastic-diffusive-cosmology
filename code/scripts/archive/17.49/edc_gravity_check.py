"""edc_gravity_check.py

EDC Toolkit — Gravity/Geometry Sanity Check (Symbolic)

Epistemic status:
  - DERIVED (mathematical identity): Given a metric g_{μν}, the Christoffel symbols,
    Ricci tensor/scalar, and Einstein tensor follow from differential geometry.
  - DEMONSTRATION: This script is a symbolic sanity check and does not fit or calibrate
    against experimental data. It uses no CODATA constants.

What it does:
  1) Builds a generic static, spherically symmetric metric:
        ds^2 = -A(r) dt^2 + B(r) dr^2 + r^2 dθ^2 + r^2 sin^2θ dφ^2
  2) Derives Γ^a_{bc}, R_{μν}, R, and G_{μν}.
  3) Prints the (typically diagonal) non-zero Einstein tensor components.
  4) Optional check: substitutes the Schwarzschild vacuum form A(r)=1-2M/r, B(r)=1/A(r)
     and verifies G_{μν} → 0 (vacuum) symbolically.

Conventions:
  - Metric signature: (-, +, +, +)
  - Coordinates: (t, r, θ, φ)
  - The parameter M in the Schwarzschild check is treated as a symbolic constant.
    (Interpretation in SI units would involve 2GM/(c^2 r); not used here.)
"""

from __future__ import annotations

import sympy as sp


def _build_metric():
    """Return (coords, metric, A(r), B(r))."""
    t, r, theta, phi = sp.symbols("t r theta phi", real=True)
    A = sp.Function("A")(r)
    B = sp.Function("B")(r)

    g = sp.diag(
        -A,
        B,
        r ** 2,
        r ** 2 * sp.sin(theta) ** 2,
    )
    coords = (t, r, theta, phi)
    return coords, g, A, B


def _christoffel_symbols(coords, g):
    """Compute Christoffel symbols Γ^a_{bc} for metric g."""
    n = len(coords)
    g_inv = sp.simplify(g.inv())
    Gamma = [[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for a in range(n):
        for b in range(n):
            for c in range(n):
                expr = sp.Integer(0)
                for d in range(n):
                    expr += g_inv[a, d] * (
                        sp.diff(g[d, c], coords[b])
                        + sp.diff(g[d, b], coords[c])
                        - sp.diff(g[b, c], coords[d])
                    )
                Gamma[a][b][c] = sp.simplify(sp.Rational(1, 2) * expr)

    return Gamma


def _ricci_tensor(coords, Gamma):
    """Compute Ricci tensor R_{bd} from Christoffel symbols."""
    n = len(coords)
    R = sp.Matrix.zeros(n, n)

    for b in range(n):
        for d in range(n):
            term = sp.Integer(0)
            for c in range(n):
                term += sp.diff(Gamma[c][b][d], coords[c]) - sp.diff(Gamma[c][b][c], coords[d])
                for e in range(n):
                    term += Gamma[c][b][d] * Gamma[e][c][e] - Gamma[c][b][e] * Gamma[e][c][d]
            R[b, d] = sp.simplify(term)

    return R


def _einstein_tensor(coords, g, Gamma):
    """Compute Einstein tensor G_{μν} = R_{μν} - 1/2 R g_{μν}."""
    R_mu_nu = _ricci_tensor(coords, Gamma)
    g_inv = sp.simplify(g.inv())
    R_scalar = sp.simplify((g_inv * R_mu_nu).trace())
    G = sp.simplify(R_mu_nu - sp.Rational(1, 2) * R_scalar * g)
    return G, R_mu_nu, R_scalar


def _print_nonzero_components(G, coords):
    labels = ["t", "r", "θ", "φ"]
    print("\n--- NON-ZERO EINSTEIN TENSOR COMPONENTS (symbolic) ---")
    found = False
    for i in range(G.rows):
        for j in range(G.cols):
            gij = sp.simplify(G[i, j])
            if gij != 0:
                found = True
                print(f"G_{labels[i]}{labels[j]} = {gij}")
    if not found:
        print("All components simplified to 0 (unexpected for generic A(r), B(r)).")


def _schwarzschild_vacuum_check(coords, g, G, A, B):
    """Substitute Schwarzschild vacuum form and verify G_{μν} -> 0."""
    _, r, _, _ = coords
    M = sp.Symbol("M", real=True)

    A_s = 1 - 2 * M / r
    B_s = 1 / A_s

    subs = {A: A_s, B: B_s}

    print("\n--- VACUUM CHECK: Schwarzschild form A=1-2M/r, B=1/A ---")
    labels = ["t", "r", "θ", "φ"]
    ok = True
    for i in range(4):
        for j in range(4):
            expr = sp.simplify(sp.together(G[i, j].subs(subs).doit()))
            if expr != 0:
                ok = False
                print(f"G_{labels[i]}{labels[j]} -> {expr}  (NOT zero)")
    if ok:
        print("PASS: All G_{μν} components simplify to 0 (vacuum solution).")


def verify_gravity_derivation(run_vacuum_check: bool = True):
    print("--- EDC TOOLKIT: Gravity / Geometry Sanity Check (Symbolic) ---")
    print("Building metric and computing curvature tensors...")

    coords, g, A, B = _build_metric()
    Gamma = _christoffel_symbols(coords, g)
    G, R_mu_nu, R_scalar = _einstein_tensor(coords, g, Gamma)

    _print_nonzero_components(G, coords)

    print("\n--- NOTES ---")
    print("• If you set G_{μν}=0, you obtain vacuum field equations for A(r), B(r).")    
    print("• This script performs no calibration and uses no physical constants.")

    if run_vacuum_check:
        _schwarzschild_vacuum_check(coords, g, G, A, B)


def main():
    verify_gravity_derivation(run_vacuum_check=True)


if __name__ == "__main__":
    main()
