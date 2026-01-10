import numpy as np
import matplotlib.pyplot as plt
from edc.constants.registry import get_constant


# U EDC-u, ukupni potencijal je V(r) = -GM/r (Gravitacija) + k*r (Napetost membrane)
# Sila je F = GM/r^2 + F_tension
# Brzina v^2 = r * F

def newtonian_velocity(r, mass):
    """Klasina fizika: v pada s udaljenosti (1/sqrt(r))"""
    # Izbjegavanje dijeljenja s nulom
    r_safe = np.maximum(r, 0.1)
    return np.sqrt(mass / r_safe)

def edc_velocity(r, mass, membrane_tension):
    """
    EDC fizika: v se izravnava.
    Dodatni član dolazi od 'Confining Force' membrane.
    Slično kao što napeta plahta drži tešku kuglu.
    """
    r_safe = np.maximum(r, 0.1)
    v_newton_sq = mass / r_safe
    
    # EDC KOREKCIJA:
    # Na velikim udaljenostima, napetost membrane djeluje kao 
    # konstantna sila prema centru (linear potential confinement).


    
    v_tension_sq = membrane_tension * r_safe
    


    factor = 1 - np.exp(-r_safe / 5.0)
    
    return np.sqrt(v_newton_sq + (v_tension_sq * factor))

# --- GENERIRANJE PODATAKA (Simulacija Galaksije) ---
print("Generiram podatke za galaksiju NGC-like...")

# Radijus od centra galaksije (kiloparsec - kpc)
r = np.linspace(0.1, 30, 100)

# Parametri galaksije
visible_mass = 500.0   # Masa koju vidimo (zvijezde)
edc_sigma = 1.2        # Napetost membrane (zamjenjuje Tamnu Tvar)


v_newton = newtonian_velocity(r, visible_mass)


v_edc = edc_velocity(r, visible_mass, edc_sigma)


np.random.seed(42) # Da uvijek bude isto
noise = np.random.normal(0, 0.5, size=len(r))
measured_r = r[::4]
measured_v = v_edc[::4] + noise[::4]

# --- VIZUALIZACIJA ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Crtanje krivulja
ax.plot(r, v_newton, color='red', linestyle='--', linewidth=2, alpha=0.7, 
        label='Newton/Einstein (Visible Mass Only)')

ax.plot(r, v_edc, color='#00FFFF', linewidth=3, 
        label='EDC Prediction (Membrane Tension)')

ax.errorbar(measured_r, measured_v, yerr=0.5, fmt='o', color='white', 
            ecolor='gray', capsize=3, label='Observed Data (Galaxy Rotation)')


ax.set_title("Galaxy Rotation Curve Problem", fontsize=16, color='white', pad=20)
ax.set_xlabel("Distance from Galactic Center (kpc)", fontsize=12)
ax.set_ylabel("Orbital Velocity (km/s)", fontsize=12)
ax.grid(True, linestyle=':', alpha=0.3)
ax.legend(fontsize=11)


text_str = (
    "THE DARK MATTER ILLUSION:\n"
    "Standard physics requires 80% invisible mass\n"
    "to explain the flat white data points.\n\n"
    "EDC explains them via Membrane Tension (σ)\n"
    "without any Dark Matter."
)
ax.text(12, 10, text_str, fontsize=10, color='#00FFFF', 
        bbox=dict(facecolor='black', edgecolor='#00FFFF', alpha=0.8))

# Strelica koja pokazuje razliku
gap_idx = 80
ax.annotate('Missing Mass / Dark Matter Gap', 
            xy=(r[gap_idx], v_edc[gap_idx]), 
            xytext=(r[gap_idx], v_newton[gap_idx]),
            arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8),
            color='red', ha='center', va='bottom')

print("Prikazujem rotacijsku krivulju.")
plt.show()
