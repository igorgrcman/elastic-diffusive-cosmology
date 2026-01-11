import math
import numpy as np
from scipy.stats import linregress

# --- CONSTANTS ---
G, c, M_SUN = 6.67430e-11, 299792458.0, 1.98847e30
A_MERCURY, E_MERCURY = 5.7909227e10, 0.205630
T_DAYS = 87.9691
ORBITS_PER_CENTURY = (365.25 * 100.0) / T_DAYS

def run_simulation(dphi, n_orbits, mode):
    L = math.sqrt(G * M_SUN * A_MERCURY * (1.0 - E_MERCURY**2))
    r_peri = A_MERCURY * (1.0 - E_MERCURY)
    u0 = 1.0 / r_peri
    gm_l2 = (G * M_SUN) / (L**2)
    k = (3.0 * G * M_SUN / c**2) if mode == "bridge" else 0.0

    # 1. PATCH: Konzistentna Verlet inicijalizacija (u'(0)=0)
    u_dd0 = gm_l2 + k*(u0**2) - u0
    u_curr = u0
    u_prev = u0 + 0.5 * (dphi**2) * u_dd0 # Taylor 2nd order

    peri_angles, h_list = [], []
    steps_per_orbit = int((2.0 * math.pi) / dphi)
    N = steps_per_orbit * n_orbits
    discard = int(N * 0.05)

    for i in range(1, N):
        u_dd = gm_l2 + k*(u_curr**2) - u_curr
        u_next = 2.0 * u_curr - u_prev + (dphi**2) * u_dd
        
        # 2. PATCH: Hamiltonian Drift monitoring
        if i % 100 == 0:
            u_prime = (u_next - u_prev) / (2.0 * dphi)
            h_phi = 0.5 * u_prime**2 + 0.5 * u_curr**2 - gm_l2 * u_curr - (k/3.0) * u_curr**3
            h_list.append(h_phi)

        # Peak detection with Quadratic Interpolation
        if i > discard and u_curr > u_prev and u_curr >= u_next:
            y1, y2, y3 = u_prev, u_curr, u_next
            x2 = i * dphi
            denom = (y1 - 2.0 * y2 + y3)
            if abs(denom) > 1e-25:
                phi_peak = x2 + (0.5 * (y1 - y3) / denom) * dphi
                peri_angles.append(phi_peak)

        u_prev, u_curr = u_curr, u_next
    
    # 3. PATCH: Linear Regression za precesiju
    n_list = np.arange(len(peri_angles))
    slope, intercept, r_val, p_val, std_err = linregress(n_list, peri_angles)
    
    # Invarijantna devijacija (H_max - H_min) / H_avg
    h_drift = (max(h_list) - min(h_list)) / abs(np.mean(h_list))
    
    return slope, std_err, h_drift, len(peri_angles)

def analyze():
    steps = [2e-4, 1e-4, 5e-5]
    print(f"{'dphi':>8} | {'Peri':>4} | {'Newton (as/cy)':>14} | {'Anomaly (as/cy)':>16} | {'H-Drift':>9}")
    print("-" * 75)
    for d in steps:
        s_n, err_n, h_n, l_n = run_simulation(d, 200, "newton")
        s_b, err_b, h_b, l_b = run_simulation(d, 200, "bridge")
        
        # Prebacivanje slope (rad/orbit) u as/cy
        to_as_cy = (180/math.pi * 3600) * ORBITS_PER_CENTURY
        adv_n = (s_n - 2.0*math.pi) * to_as_cy
        adv_b = (s_b - 2.0*math.pi) * to_as_cy
        anomaly = adv_b - adv_n
        
        print(f"{d:8.1e} | {l_n:4} | {adv_n:14.6f} | {anomaly:16.6f} | {h_n:9.2e}")

analyze()
