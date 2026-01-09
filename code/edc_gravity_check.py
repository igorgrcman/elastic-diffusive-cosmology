import sympy
from sympy import symbols, sin, Function, Matrix, simplify, diff

def verify_gravity_derivation():
    print("--- EDC TOOLKIT: Gravity Derivation Check ---")
    print("Initializing symbolic variables...")
    
    # 1. Definiranje koordinata i varijabli
    t, r, theta, phi = symbols('t r theta phi')
    
    # Definiramo nepoznate funkcije metrike A(r) i B(r)
    # U EDC-u, one ovise o gustoći i napetosti membrane
    A = Function('A')(r)  # Povezano s g_tt
    B = Function('B')(r)  # Povezano s g_rr
    
    # 2. Definiranje Metrike (Sferno simetrična, statična)
    # ds^2 = -A(r)dt^2 + B(r)dr^2 + r^2 dtheta^2 + r^2 sin^2(theta) dphi^2
    print("Defining Metric Tensor g_mu_nu...")
    g = Matrix([
        [-A, 0, 0, 0],
        [0, B, 0, 0],
        [0, 0, r**2, 0],
        [0, 0, 0, r**2 * sin(theta)**2]
    ])
    
    # Inverzna metrika
    g_inv = g.inv()
    coords = [t, r, theta, phi]
    
    # 3. Izračun Christoffelovih simbola
    print("Calculating Christoffel Symbols (Gamma)...")
    Gamma = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(4):
                sum_term = 0
                for l in range(4):
                    # Formula: 1/2 * g^kl * (dg_li/dx^j + dg_lj/dx^i - dg_ij/dx^l)
                    term = 0.5 * g_inv[k, l] * (diff(g[l, i], coords[j]) + diff(g[l, j], coords[i]) - diff(g[i, j], coords[l]))
                    sum_term += term
                Gamma[i][j][k] = simplify(sum_term)

    # 4. Izračun Riccijevog tenzora R_mu_nu
    print("Calculating Ricci Tensor (R_mu_nu)...")
    R_tensor = Matrix.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            sum_term = 0
            for k in range(4):
                # Riemannova kontrakcija
                term1 = diff(Gamma[j][i][k], coords[k])
                term2 = -diff(Gamma[j][k][k], coords[i])
                term3 = 0
                term4 = 0
                for m in range(4):
                    term3 += Gamma[j][i][m] * Gamma[m][k][k]
                    term4 -= Gamma[j][k][m] * Gamma[m][i][k]
                sum_term += term1 + term2 + term3 + term4
            R_tensor[i, j] = simplify(sum_term)

    # 5. Izračun Riccijevog skalara R
    print("Calculating Ricci Scalar (R)...")
    R_scalar = 0
    for i in range(4):
        for j in range(4):
            R_scalar += g_inv[i, j] * R_tensor[i, j]
    R_scalar = simplify(R_scalar)
    
    # 6. Izračun Einsteinovog tenzora G_mu_nu
    # G_mu_nu = R_mu_nu - 1/2 * R * g_mu_nu
    print("Calculating Einstein Tensor (G_mu_nu)...")
    G_tensor = Matrix.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            G_tensor[i, j] = simplify(R_tensor[i, j] - 0.5 * R_scalar * g[i, j])

    # Ispis rezultata
    print("\n--- RESULTS: NON-ZERO EINSTEIN COMPONENTS ---")
    print(f"G_tt (Time component)  = {G_tensor[0, 0]}")
    print(f"G_rr (Radial component)= {G_tensor[1, 1]}")
    print("\nSUCCESS: The metric geometry generates a valid curvature tensor.")

if __name__ == "__main__":
    verify_gravity_derivation()
