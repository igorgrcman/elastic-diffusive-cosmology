import numpy as np

# --- EDC CONSTANTS ---
G = 6.67430e-11
M_SUN = 1.98847e30
c = 299792458.0
A_MERCURY = 5.790923e10
E_MERCURY = 0.205630

def get_perihelion_phi(dphi, use_edc=True):
    r_0 = A_MERCURY * (1.0 - E_MERCURY)
    u = 1.0 / r_0
    L = np.sqrt(G * M_SUN * A_MERCURY * (1.0 - E_MERCURY**2))
    
    def f(u_val):
        newton = (G * M_SUN) / (L**2)
        # Ključni EDC doprinos izveden iz PG toka
        edc = (3.0 * G * M_SUN / c**2) * (u_val**2) if use_edc else 0.0
        return newton + edc - u_val

    # RK4
    phi = 0.0
    curr_u, curr_du = u, 0.0
    
    # Spremanje zadnja 3 koraka za preciznu detekciju vrha (parabola fit)
    u_history = []
    phi_history = []
    
    steps = int((2.0 * np.pi + 0.05) / dphi)
    for i in range(steps):
        # RK4 koraci...
        k1_u = curr_du
        k1_du = f(curr_u)
        k2_u = curr_du + 0.5 * dphi * k1_du
        k2_du = f(curr_u + 0.5 * dphi * k1_u)
        k3_u = curr_du + 0.5 * dphi * k2_du
        k3_du = f(curr_u + 0.5 * dphi * k2_u)
        k4_u = curr_du + dphi * k3_du
        k4_du = f(curr_u + dphi * k3_u)
        
        curr_u += (dphi / 6.0) * (k1_u + 2*k2_u + 2*k3_u + k4_u)
        curr_du += (dphi / 6.0) * (k1_du + 2*k2_du + 2*k3_du + k4_du)
        current_phi = i * dphi
        
        # Tražimo perihel nakon što prođemo polovicu puta
        if current_phi > np.pi:
            u_history.append(curr_u)
            phi_history.append(current_phi)
            if len(u_history) > 3:
                u_history.pop(0)
                phi_history.pop(0)
                # Ako smo prošli vrh (du postaje negativan)
                if u_history[1] > u_history[2] and u_history[1] > u_history[0]:
                    # Kvadratna interpolacija za ekstrem (vrh parabole)
                    y1, y2, y3 = u_history
                    x1, x2, x3 = phi_history
                    denom = (x1-x2)*(x1-x3)*(x2-x3)
                    A = (x3*(y2-y1) + x2*(y1-y3) + x1*(y3-y2)) / denom
                    B = (x3**2*(y1-y2) + x2**2*(y3-y1) + x1**2*(y2-y3)) / denom
                    return -B / (2*A)
    return 0.0

# Izvršavanje
dphi = 5e-6 # Finiji korak za bolju rezoluciju
p_edc = get_perihelion_phi(dphi, True)
p_newt = get_perihelion_phi(dphi, False)

anomaly = (p_edc - p_newt) * (180/np.pi * 3600) * 415.2
print(f"EDC NATIVE RESULT: {anomaly:.4f} arcsec/century")
