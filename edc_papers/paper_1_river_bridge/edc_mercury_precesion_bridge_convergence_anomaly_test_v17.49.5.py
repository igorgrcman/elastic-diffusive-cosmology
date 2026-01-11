import math
import numpy as np
from scipy.stats import linregress

# --- CONSTANTS ---
G, c, M_SUN = 6.67430e-11, 299792458.0, 1.98847e30
A_MERCURY, E_MERCURY = 5.7909227e10, 0.205630
T_DAYS = 87.9691
ORBITS_PER_CENTURY = (365.25 * 100.0) / T_DAYS

def run_simulation(dphi_target, n_orbits, mode):
    # 3. PATCH: dphi_eff (Usklađivanje s mrežom)
    steps_per_orbit = int(round((2.0 * math.pi) / dphi_target))
    dphi = (2.0 * math.pi) / steps_per_orbit
    
    L = math.sqrt(G * M_SUN * A_MERCURY * (1.0 - E_MERCURY**2))
    r_peri = A_MERCURY * (1.0 - E_MERCURY)
    u0 = 1.0 / r_peri
    gm_l2 = (G * M_SUN) / (L**2)
    k = (3.0 * G * M_SUN / c**2) if mode == "bridge" else 0.0

    # 1. PATCH: Konzistentna inicijalizacija
    u_dd0 = gm_l2 + k*(u0**2) - u0
    u_curr = u0
    u_prev = u0 + 0.5 * (dphi**2) * u_dd0 

    peri_angles, h_list = [], []
    N = steps_per_orbit * n_orbits
    discard = int(N * 0.05)

    for i in range(1, N):
        u_dd = gm_l2 + k*(u_curr**2) - u_curr
        u_next = 2.0 * u_curr - u_prev + (dphi**2) * u_dd
        
        # 4. PATCH: H-Drift od početne vrijednosti
        if i % 100 == 0:
            u_prime = (u_next - u_prev) / (2.0 * dphi)
            h_phi = 0.5 * u_prime**2 + 0.5 * u_curr**2 - gm_l2 * u_curr - (k/3.0) * u_curr**3
            h_list.append(h_phi)

        # Peak detection
        if i > discard and u_curr > u_prev and u_curr >= u_next:
            y1, y2, y3 = u_prev, u_curr, u_next
            x2 = i * dphi
            denom = (y1 - 2.0 * y2 + y3)
            if abs(denom) > 1e-25:
                phi_peak = x2 + (0.5 * (y1 - y3) / denom) * dphi
                peri_angles.append(phi_peak)

        u_prev, u_curr = u_curr, u_next
    
    # 1. PATCH: Regresija na delta (izbjegavanje 2*pi*n dominacije)
    n_list = np.arange(len(peri_angles))
    deltas = np.array(peri_angles) - 2.0 * math.pi * n_list
    delta_slope, intercept, r_val, p_val, std_err = linregress(n_list, deltas)
    
    h0 = h_list[0]
    h_rel_drift = max(abs((h - h0) / h0) for h in h_list)
    
    return delta_slope, std_err, h_rel_drift, len(peri_angles)

def analyze():
    steps = [2e-4, 1e-4, 5e-5]
    to_as_cy = (180/math.pi * 3600) * ORBITS_PER_CENTURY
    
    print(f"{'dphi':>8} | {'Newton (as/cy)':>15} | {'Anomaly (as/cy)':>22} | {'H-Drift (B)':>9}")
    print("-" * 85)
    
    for d in steps:
        sl_n, err_n, h_n, l_n = run_simulation(d, 200, "newton")
        sl_b, err_b, h_b, l_b = run_simulation(d, 200, "bridge")
        
        # 2. PATCH: Propagacija pogreške (Anomaly ± error)
        adv_n = sl_n * to_as_cy
        adv_b = sl_b * to_as_cy
        anomaly = adv_b - adv_n
        
        # Error bars (95% CI approx: 2*sigma)
        err_total = math.sqrt(err_n**2 + err_b**2) * to_as_cy * 2.0
        
        print(f"{d:8.1e} | {adv_n:15.6f} | {anomaly:10.6f} ± {err_total:.1e} | {h_b:9.2e}")

if __name__ == "__main__":
    analyze()
