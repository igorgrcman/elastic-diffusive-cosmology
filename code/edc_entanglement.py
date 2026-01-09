import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# --- EDC FIZIKA: ENTANGLEMENT KAO GEOMETRIJA ---
# 1. 'Surface View': Dva fotona se udaljavaju. Izgledaju nepovezano.
# 2. 'Bulk View': Oni su krajevi jedne te iste potkove (Flux Tube) u 5D.
# 3. Signal putuje kroz 'potkovu' (Bulk) puno brže nego kroz površinu.

def generate_bulk_connection(p1, p2, depth):
    """Generira luk (most) koji spaja dvije čestice kroz 5. dimenziju (z < 0)"""
    # Parametarska krivulja (polukrug u dubinu)
    t = np.linspace(0, np.pi, 50)
    
    # Središnja točka
    center_x = (p1[0] + p2[0]) / 2
    radius = abs(p2[0] - p1[0]) / 2
    
    # Koordinate luka
    x = center_x + radius * np.cos(t) # Putuje od p2 do p1
    y = np.zeros_like(x)              # Ostaje na y=0 liniji
    z = -depth * np.sin(t)            # Ide u dubinu (Bulk)
    
    return x, y, z

# --- VIZUALIZACIJA ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(14, 6))

# LIJEVO: 2D Ljudski pogled (Membrana)
ax2d = fig.add_subplot(1, 2, 1)
ax2d.set_title("HUMAN VIEW (3D Membrane)\n'Spooky Action at a Distance'", color='cyan')
ax2d.set_xlim(-6, 6)
ax2d.set_ylim(-3, 3)
ax2d.set_aspect('equal')
ax2d.axis('off')

# Grid membrane (da se vidi da je prostor ravan)
for i in range(-6, 7):
    ax2d.axvline(i, color='gray', alpha=0.2, lw=0.5)
    ax2d.axhline(i/2, color='gray', alpha=0.2, lw=0.5)

# DESNO: 5D Božji pogled (EDC Bulk Reality)
ax3d = fig.add_subplot(1, 2, 2, projection='3d')
ax3d.set_title("EDC VIEW (5D Bulk Geometry)\n'Connected via Flux Shortcut'", color='magenta')
ax3d.set_xlim(-6, 6)
ax3d.set_ylim(-3, 3)
ax3d.set_zlim(-5, 1)
ax3d.axis('off')
ax3d.view_init(elev=20, azim=-90) # Gledamo 'ispod' stola

# --- OBJEKTI ---
# Čestice (A i B)
p_left, = ax2d.plot([], [], 'o', color='cyan', markersize=12, label='Particle A')
p_right, = ax2d.plot([], [], 'o', color='cyan', markersize=12, label='Particle B')
signal_surf, = ax2d.plot([], [], '.', color='red', markersize=8) # Signal po površini

p3d_left, = ax3d.plot([], [], [], 'o', color='cyan', markersize=12)
p3d_right, = ax3d.plot([], [], [], 'o', color='cyan', markersize=12)
bulk_line, = ax3d.plot([], [], [], '-', color='magenta', alpha=0.6, lw=2) # 5D Veza
signal_bulk, = ax3d.plot([], [], [], '*', color='yellow', markersize=15) # Signal kroz Bulk

# Membrana u 3D pogledu (prozirna površina)
xx, yy = np.meshgrid(np.linspace(-6, 6, 10), np.linspace(-3, 3, 5))
ax3d.plot_surface(xx, yy, np.zeros_like(xx), color='blue', alpha=0.1)

# Tekstovi
dist_text = ax2d.text(0, -2, "", color='white', ha='center')
status_text = ax2d.text(0, 2, "", color='yellow', ha='center', fontsize=12)

# Globalno stanje
state = {
    'separation': 1.0,
    'pulse_pos': 0.0, # 0 do 1 (put od A do B)
    'triggered': False
}

def update(frame):
    # 1. ŠIRENJE: Čestice se udaljavaju
    if state['separation'] < 4.0:
        state['separation'] += 0.05
        status_text.set_text("System State: Separating Particles...")
    elif not state['triggered']:
        state['triggered'] = True
        state['pulse_pos'] = 0
        status_text.set_text("EVENT: Spin Change at A!")
    
    # Pozicije čestica
    sep = state['separation']
    xA, xB = -sep, sep
    
    # Ažuriraj 2D prikaz
    p_left.set_data([xA], [0])
    p_right.set_data([xB], [0])
    
    # Crtanje "Svjetlosnog signala" (sporo) po površini
    if state['triggered']:
        # Signal ide brzinom svjetlosti (c) po površini
        # Recimo da mu treba 100 frameova da pređe put
        surf_progress = min((frame - 80) * 0.02, 1.0)
        if surf_progress > 0 and surf_progress < 1:
            sig_x = xA + (xB - xA) * surf_progress
            signal_surf.set_data([sig_x], [0])
            dist_text.set_text(f"Surface Signal (c): {int(surf_progress*100)}% to target")
        elif surf_progress >= 1:
             dist_text.set_text("Surface Signal: ARRIVED (Too Late)")
    
    # Ažuriraj 3D prikaz (Bulk Connection)
    p3d_left.set_data([xA], [0])
    p3d_left.set_3d_properties([0])
    
    p3d_right.set_data([xB], [0])
    p3d_right.set_3d_properties([0])
    
    # Crtaj Bulk "Flux Tube" (Most)
    # Dubina mosta ovisi o udaljenosti (geodezik)
    bx, by, bz = generate_bulk_connection([-sep, 0], [sep, 0], depth=sep*0.8)
    bulk_line.set_data(bx, by)
    bulk_line.set_3d_properties(bz)
    
    # SIGNAL KROZ BULK (Brz!)
    if state['triggered']:
        # Signal kroz Bulk putuje trenutno ili puno brže (Tachyon/Sound)
        # Ovdje ga animiramo brzo da se vidi putanja
        bulk_progress = min((frame - 80) * 0.1, 1.0) # 5x brži od površine
        
        if bulk_progress > 0 and bulk_progress < 1:
            # Nađi koordinate na luku
            idx = int(bulk_progress * (len(bx)-1))
            signal_bulk.set_data([bx[idx]], [by[idx]])
            signal_bulk.set_3d_properties([bz[idx]])
            status_text.set_text("BULK TRANSFER: INSTANTANEOUS!")
        elif bulk_progress >= 1:
            signal_bulk.set_data([xB], [0])
            signal_bulk.set_3d_properties([0])
            status_text.set_text("Correlation Established via 5D!")

    return p_left, p_right

ani = FuncAnimation(fig, update, frames=200, interval=30, blit=False)
print("Prikazujem EDC Entanglement mehanizam...")
plt.show()
