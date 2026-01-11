import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# --- CONSTANTS ---
G, c, M_SUN = 6.67430e-11, 299792458.0, 1.98847e30
A_MERCURY, E_MERCURY = 5.7909227e10, 0.205630
T_DAYS = 87.9691
ORBITS_PER_CENTURY = (365.25 * 100.0) / T_DAYS

def run_simulation(dphi_target, n_orbits, mode):
    steps_per_orbit = int(round((2.0 * math.pi) / dphi_target))
    dphi = (2.0 * math.pi) / steps_per_orbit
    
    L = math.sqrt(G * M_SUN * A_MERCURY * (1.0 - E_MERCURY**2))
    r_peri = A_MERCURY * (1.0 - E_MERCURY)
    u0 = 1.0 / r_peri
    gm_l2 = (G * M_SUN) / (L**2)
    k = (3.0 * G * M_SUN / c**2) if mode == "bridge" else 0.0

    # Taylor initialization
    u_dd0 = gm_l2 + k*(u0**2) - u0
    u_curr = u0
    u_prev = u0 + 0.5 * (dphi**2) * u_dd0 

    peri_angles, h_list = [], []
    N = steps_per_orbit * n_orbits
    discard = int(N * 0.1) # Increased discard for safety

    for i in range(1, N):
        u_dd = gm_l2 + k*(u_curr**2) - u_curr
        u_next = 2.0 * u_curr - u_prev + (dphi**2) * u_dd
        
        if i % 200 == 0:
            u_prime = (u_next - u_prev) / (2.0 * dphi)
            h_phi = 0.5 * u_prime**2 + 0.5 * u_curr**2 - gm_l2 * u_curr - (k/3.0) * u_curr**3
            h_list.append(h_phi)

        if i > discard and u_curr > u_prev and u_curr >= u_next:
            y1, y2, y3 = u_prev, u_curr, u_next
            x2 = i * dphi
            denom = (y1 - 2.0 * y2 + y3)
            if abs(denom) > 1e-25:
                phi_peak = x2 + (0.5 * (y1 - y3) / denom) * dphi
                peri_angles.append(phi_peak)
        u_prev, u_curr = u_curr, u_next
    
    n_list = np.arange(len(peri_angles))
    deltas = np.array(peri_angles) - 2.0 * math.pi * n_list
    slope, intercept, r, p, std_err = linregress(n_list, deltas)
    
    h0 = h_list[0]
    h_rel_drift = max(abs((h - h0) / h0) for h in h_list)
    return slope, std_err, h_rel_drift

# --- EXECUTE LADDER ---
steps_to_test = [2e-4, 1e-4, 7.5e-5, 5e-5, 3.3e-5]
n_orbits = 300 # More orbits for better statistics
results = []

print(f"{'dphi':>10} | {'Newton (as/cy)':>15} | {'Anomaly (as/cy)':>18} | {'H-Drift':>9}")
for d in steps_to_test:
    sl_n, err_n, h_n = run_simulation(d, n_orbits, "newton")
    sl_b, err_b, h_b = run_simulation(d, n_orbits, "bridge")
    
    to_as_cy = (180/math.pi * 3600) * ORBITS_PER_CENTURY
    adv_n = sl_n * to_as_cy
    anomaly = (sl_b - sl_n) * to_as_cy
    err_stat = math.sqrt(err_n**2 + err_b**2) * to_as_cy * 1.97 # 95% CI
    
    results.append([d, adv_n, anomaly, err_stat, h_b])
    print(f"{d:10.1e} | {adv_n:15.6f} | {anomaly:10.6f} +/- {err_stat:7.1e} | {h_b:9.2e}")

# --- PLOTTING ---
res = np.array(results)
d_eff, n_drift, anom, ci, h_drift = res[:,0], res[:,1], res[:,2], res[:,3], res[:,4]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xscale("log")
ax1.set_xlim(2.5e-4, 2.5e-5) # Fine to the right

ax1.plot(d_eff, n_drift, 'o--', color='tab:red', label="Newtonian Drift (LHS)")
ax1.set_xlabel(r"Step Size $d\phi_{\mathrm{eff}}$ (rad) $\rightarrow$ Refinement")
ax1.set_ylabel("Newtonian Drift (as/cy)", color='tab:red')

ax2 = ax1.twinx()
ax2.errorbar(d_eff, anom, yerr=ci, fmt='o-', color='tab:blue', capsize=4, label="Anomaly ± 95% CI (RHS)")
ax2.axhline(y=42.98, color='black', ls=':', alpha=0.6, label="GR Benchmark")
ax2.set_ylabel("Anomalous Precession (as/cy)", color='tab:blue')

# Stability Box
ax1.text(0.05, 0.95, f"Bridge H-drift range:\n{min(h_drift):.1e} to {max(h_drift):.1e}", 
         transform=ax1.transAxes, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax1.legend(loc='lower left', bbox_to_anchor=(0.1, -0.25), ncol=3)
plt.tight_layout()
plt.savefig("edc_validation_v17.50.png", dpi=300)
plt.show()
