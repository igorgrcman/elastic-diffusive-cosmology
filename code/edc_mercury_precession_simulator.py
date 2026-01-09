import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

# --- EDC KONFIGURACIJA ---
# U EDC-u gravitacija je rezultat tlaka Plenuma i napetosti Membrane.
# G = c^2 / (4 * pi * sigma)
# Ovdje koristimo normalizirane jedinice za vizualizaciju.

GM = 4 * np.pi**2  # Gravitacijski parametar (Definiran tlakom Plenuma)

# OVO JE KLJUČNA RAZLIKA U INTERPRETACIJI:
# U GR ovo je "zakrivljenost prostora".
# U EDC ovo je "MEMBRANE STIFFNESS CORRECTION" (Korekcija krutosti membrane).
# Kada je membrana jako savijena (blizu Sunca), ona pruža dodatni nelinearni otpor.
EDC_NONLINEAR_TERM = 0.015  

# Početni uvjeti za Merkur (na membrani)
r0 = 0.39  # Perihel
x0 = r0
y0 = 0.0

# Brzina na membrani (transverzalni val)
vy0 = np.sqrt(GM / r0) * 1.25 
vx0 = 0.0

initial_state = [x0, y0, vx0, vy0]

# Vrijeme simulacije
years = 8.0         
points_per_year = 600
t = np.linspace(0, years, int(years * points_per_year))

# --- EDC JEDNADŽBE GIBANJA ---
def edc_equations_of_motion(state, t):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    
    # 1. Hidrostatski član (Newtonov limit)
    # Ovo dolazi od Young-Laplace jednadžbe: Delta P ~ Curvature
    accel_hydrostatic = -GM / r**3
    
    # 2. EDC Nelinearni član (Precesija)
    # Ovo dolazi od članova višeg reda u Akciji membrane (bending energy).
    # Membrana se "opire" jakom savijanju više nego što Newton predviđa.
    # Sila F ~ 1/r^2 + alpha/r^4
    membrane_resistance = 1 + (EDC_NONLINEAR_TERM / r**2)
    
    # Ukupno ubrzanje na membrani
    ax = x * accel_hydrostatic * membrane_resistance
    ay = y * accel_hydrostatic * membrane_resistance
    
    return [vx, vy, ax, ay]

# --- IZRAČUN ---
print("Rješavam dinamiku membrane... (EDC Action)")
solution = odeint(edc_equations_of_motion, initial_state, t)
x_pos = solution[:, 0]
y_pos = solution[:, 1]

# --- VIZUALIZACIJA ---
fig, ax = plt.subplots(figsize=(9, 9))
# Tamnoplava pozadina predstavlja Plenum (Fluid)
ax.set_facecolor('#000015') 
fig.patch.set_facecolor('#000015')

# Postavke prikaza
limit = 1.4
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_aspect('equal')
ax.axis('off')

# Grafički elementi
# Sunce (izvor deformacije membrane)
sun, = ax.plot([0], [0], 'o', color='#FFD700', markersize=18, 
               markeredgecolor='#FF4500', markeredgewidth=2, label='Sun (Mass Load)')

# Merkur (objekt koji prati geodezik na membrani)
planet, = ax.plot([], [], 'o', color='#00FFFF', markersize=7, label='Mercury')

# Trag (Geodezik)
trail, = ax.plot([], [], '-', color='white', linewidth=0.9, alpha=0.5)

# Oznake
title = ax.text(0.5, 1.02, 'EDC: Anomalous Precession via Membrane Stress', 
                transform=ax.transAxes, color='white', ha='center', fontsize=14, fontweight='bold')
mech_text = ax.text(0.5, 0.98, 'Cause: Nonlinear Elastic Response (Not Geometry)', 
                    transform=ax.transAxes, color='#AAAAAA', ha='center', fontsize=10)

def init():
    planet.set_data([], [])
    trail.set_data([], [])
    return planet, trail

def animate(i):
    step = i * 5  # Brzina
    if step >= len(x_pos):
        step = len(x_pos) - 1
        
    this_x = x_pos[step]
    this_y = y_pos[step]
    
    planet.set_data([this_x], [this_y])
    trail.set_data(x_pos[:step], y_pos[:step])
    
    return planet, trail

ani = animation.FuncAnimation(fig, animate, frames=len(t)//5, init_func=init, 
                              interval=1, blit=True)

print("Pokrećem simulaciju membrane.")
plt.show()
