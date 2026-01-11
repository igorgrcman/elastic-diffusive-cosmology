import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, t

# --- CONSTANTS ---
G, c, M_SUN = 6.67430e-11, 299792458.0, 1.98847e30
A_MERCURY, E_MERCURY = 5.7909227e10, 0.205630
T_DAYS = 87.9691
ORBITS_PER_CENTURY = (365.25 * 100.0) / T_DAYS

def run_simulation(dphi_target, n_orbits, mode):
    # 1. FIX: Calculate effective step size
    steps_per_orbit = int(round((2.0 * math.pi) / dphi_target))
    dphi_eff = (2.0 * math.pi) / steps_per_orbit
    
    L = math.sqrt(G * M_SUN * A_MERCURY * (1.0 - E_MERCURY**2))
    r_peri = A_MERCURY * (1.0 - E_MERCURY)
    u0 = 1.0 / r_peri
    gm_l2 = (G * M_SUN) / (L**2)
    k = (3.0 * G * M_SUN / c**2) if mode == "bridge" else 0.0

    u_dd0 = gm_l2 + k*(u0**2) - u0
    u_curr = u0
    u_prev = u0 + 0.5 * (dphi_eff**2) * u_dd0 

    peri_angles, h_list = [], []
    N_total = steps_per_orbit * n_orbits
    discard = int(N_total * 0.1)

    for i in range(1, N_total):
        u_dd = gm_l2 + k*(u_curr**2) - u_curr
        u_next = 2.0 * u_curr - u_prev + (dphi_eff**2) * u_dd
        
        # 3. FIX: Collect Hamiltonian only AFTER discard to avoid transients
        if i > discard and i % 100 == 0:
            u_prime = (u_next - u_prev) / (2.0 * dphi_eff)
            h_phi = 0.5 * u_prime**2 + 0.5 * u_curr**2 - gm_l2 * u_curr - (k/3.0) * u_curr**3
            h_list.append(h_phi)

        # Peak detection
        if i > discard and u_curr > u_prev and u_curr >= u_next:
            y1, y2, y3 = u_prev, u_curr, u_next
            x2 = i * dphi_eff
            denom = (y1 - 2.0 * y2 + y3)
            if abs(denom) > 1e-25:
                phi_peak = x2 + (0.5 * (y1 - y3) / denom) * dphi_eff
                peri_angles.append(phi_peak)
        u_prev, u_curr = u_curr, u_next
    
    # Regression on deltas
    n_list = np.arange(len(peri_angles))
    deltas = np.array(peri_angles) - 2.0 * math.pi * n_list
    slope, intercept, r, p, std_err = linregress(n_list, deltas)
    
    # 4. FIX: Use t-distribution for 95% CI
    df = len(peri_angles) - 2
    t_crit = t.ppf(0.975, df)
    ci95_slope = t_crit * std_err
    
    h0 = h_list[0]
    h_rel_drift = max(abs((h - h0) / h0) for h in h_list)
    
    # 2. FIX: Return dphi_eff and number of detected perihelia
    return slope, ci95_slope, h_rel_drift, len(peri_angles), dphi_eff

# --- EXECUTE LADDER ---
steps_to_test = [2e-4, 1e-4, 7.5e-5, 5e-5, 3.3e-5]
n_orbits = 300
results = []

print(f"{'dphi_eff':>10} | {'Peri':>4} | {'Newton (as/cy)':>15} | {'Anomaly (as/cy)':>18} | {'H-Drift':>9}")
print("-" * 75)

for d_target in steps_to_test:
    sl_n, ci_n, h_n, l_n, d_eff = run_simulation(d_target, n_orbits, "newton")
    sl_b, ci_b, h_b, l_b, _ = run_simulation(d_target, n_orbits, "bridge")
    
    to_as_cy = (180/math.pi * 3600) * ORBITS_PER_CENTURY
    adv_n = sl_n * to_as_cy
    anomaly = (sl_b - sl_n) * to_as_cy
    
    # Propagated CI95
    err_total = math.sqrt(ci_n**2 + ci_b**2) * to_as_cy
    
    results.append([d_eff, adv_n, anomaly, err_total, h_b, l_b])
    print(f"{d_eff:10.1e} | {l_b:4} | {adv_n:15.6f} | {anomaly:10.6f} +/- {err_total:7.1e} | {h_b:9.2e}")
