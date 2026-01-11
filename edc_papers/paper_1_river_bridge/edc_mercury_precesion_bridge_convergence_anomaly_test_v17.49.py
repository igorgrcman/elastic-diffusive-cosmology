#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EDC Mercury Precession - Convergence & Stability Tracker (v17.49.3)
Method: Difference-of-runs with Verlet Symplectic Integration
"""

import math
import numpy as np
import time

# --- CONSTANTS ---
G = 6.67430e-11
c = 299792458.0
M_SUN = 1.98847e30
A_MERCURY = 5.7909227e10
E_MERCURY = 0.205630
T_DAYS = 87.9691
ORBITS_PER_CENTURY = (365.25 * 100.0) / T_DAYS

def run_simulation(dphi, n_orbits, mode):
    # Initial conditions
    L = math.sqrt(G * M_SUN * A_MERCURY * (1.0 - E_MERCURY**2))
    r_peri = A_MERCURY * (1.0 - E_MERCURY)
    u0 = 1.0 / r_peri
    
    # Pre-calculate constants for speed
    gm_l2 = (G * M_SUN) / (L**2)
    edc_coeff = (3.0 * G * M_SUN / c**2) if mode == "bridge" else 0.0
    
    # Arrays
    steps_per_orbit = int((2.0 * math.pi) / dphi)
    N = steps_per_orbit * n_orbits
    
    # Verlet integration (u_next = 2*u - u_prev + dphi^2 * u_dd)
    u_prev = u0
    u_curr = u0
    
    peri_angles = []
    energy_drift = []
    
    # We skip first 5% to avoid startup transients
    discard = int(N * 0.05)

    for i in range(1, N):
        # Binet RHS: u'' = f(u) - u
        u_dd = gm_l2 + edc_coeff * (u_curr**2) - u_curr
        u_next = 2.0 * u_curr - u_prev + (dphi**2) * u_dd
        
        # Peak detection (u_max = perihelion)
        if i > discard:
            if u_curr > u_prev and u_curr >= u_next:
                # Quadratic interpolation
                y1, y2, y3 = u_prev, u_curr, u_next
                x2 = i * dphi
                denom = (y1 - 2.0 * y2 + y3)
                if abs(denom) > 1e-25:
                    dx = 0.5 * (y1 - y3) / denom
                    phi_peak = x2 + dx * dphi
                    peri_angles.append(phi_peak)

        u_prev, u_curr = u_curr, u_next
        
    return peri_angles

def analyze_convergence():
    steps_to_test = [2e-4, 1e-4, 5e-5]
    n_orbits = 200 # Povećano za bolju statistiku
    
    print(f"{'dphi':>10} | {'Perihelia':>10} | {'Newton (as/cy)':>15} | {'Bridge-Newton (as/cy)':>20}")
    print("-" * 65)
    
    for dphi in steps_to_test:
        # Newton Run
        p_newt = run_simulation(dphi, n_orbits, "newton")
        adv_newt = (np.mean(np.diff(p_newt)) - 2.0*math.pi) * (180/math.pi*3600) * ORBITS_PER_CENTURY
        
        # Bridge Run
        p_bridge = run_simulation(dphi, n_orbits, "bridge")
        adv_bridge = (np.mean(np.diff(p_bridge)) - 2.0*math.pi) * (180/math.pi*3600) * ORBITS_PER_CENTURY
        
        anomaly = adv_bridge - adv_newt
        
        print(f"{dphi:10.1e} | {len(p_bridge):10} | {adv_newt:15.6f} | {anomaly:20.6f}")

if __name__ == "__main__":
    print("======================================================")
    print("EDC BRIDGE VALIDATION: CONVERGENCE & ANOMALY TEST")
    print("======================================================")
    start_time = time.time()
    analyze_convergence()
    print("-" * 65)
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")
