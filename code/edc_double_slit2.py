import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- EDC FIZIKA: PILOT WAVE DYNAMICS ---
# 1. Plenum (Prostor) je fluid koji prenosi valove.
# 2. Čestica je 'Flux Event' koji 'surfa' na gradijentu tlaka tog vala.
# 3. Determinizam: Čestica ne bira nasumično, nego ide tamo gdje je val gura.

def calculate_wave_field(x, y, k, slit_dist):
    """
    Izračunava interferencijski uzorak valova iz dva izvora (proreza).
    """
    # Udaljenosti od lijevog i desnog proreza
    r1 = np.sqrt((x - slit_dist/2)**2 + y**2)
    r2 = np.sqrt((x + slit_dist/2)**2 + y**2)
    
    # Amplituda opada s udaljenosti (1/sqrt(r) u 2D)
    # Dodajemo malu konstantu da izbjegnemo dijeljenje s nulom
    a1 = 1 / np.sqrt(r1 + 0.5)
    a2 = 1 / np.sqrt(r2 + 0.5)
    
    # Superpozicija valova (zbrajanje faza)
    # Koristimo sin(kr) za prikaz trenutnog stanja vala
    wave = a1 * np.sin(k * r1) + a2 * np.sin(k * r2)
    
    # Vjerojatnost (Intenzitet) je kvadrat amplitude (vremenski usrednjen)
    intensity = (a1 + a2 * np.cos(k*(r1-r2)))**2 
    
    return wave, intensity

# --- POSTAVKE SIMULACIJE ---
WIDTH = 30
HEIGHT = 20
RESOLUTION = 150
WAVELENGTH = 1.2
K = 2 * np.pi / WAVELENGTH
SLIT_DIST = 4.0

# Generiranje mreže prostora
x = np.linspace(-WIDTH/2, WIDTH/2, RESOLUTION)
y = np.linspace(0, HEIGHT, RESOLUTION)
X, Y = np.meshgrid(x, y)

print("Računam EDC polje (Plenum interference)...")
wave_field, intensity_field = calculate_wave_field(X, Y, K, SLIT_DIST)

# Vjerojatnost detekcije na vrhu ekrana (zadnji red mreže)
detector_prob = intensity_field[-1, :]
detector_prob /= np.sum(detector_prob) # Normalizacija na 1

# --- VIZUALIZACIJA ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 9))

# GORNJI GRAF: Valno polje (Plenum)
ax_wave = fig.add_axes([0.1, 0.4, 0.8, 0.55])
ax_wave.set_title("EDC Pilot Wave Dynamics (Double Slit)", color='white', fontsize=16)
ax_wave.axis('off')

# Prikaz vala (koristimo 'ocean' ili 'gist_earth' za tekući izgled)
# vmin/vmax podešeni za bolji kontrast valova
im = ax_wave.imshow(wave_field, extent=[-WIDTH/2, WIDTH/2, 0, HEIGHT], 
                    origin='lower', cmap='ocean', aspect='auto', alpha=0.9)

# Crtanje proreza (barijera na dnu)
ax_wave.plot([-WIDTH/2, -SLIT_DIST/2-0.5], [0, 0], color='gray', linewidth=6)
ax_wave.plot([-SLIT_DIST/2+0.5, SLIT_DIST/2-0.5], [0, 0], color='gray', linewidth=6)
ax_wave.plot([SLIT_DIST/2+0.5, WIDTH/2], [0, 0], color='gray', linewidth=6)
ax_wave.text(0, -1.5, "Slits (Flux Entry)", color='cyan', ha='center')

# DONJI GRAF: Detektor (Histogram čestica)
ax_det = fig.add_axes([0.1, 0.05, 0.8, 0.25])
ax_det.set_title("Particle Accumulation (Detector Screen)", color='cyan', fontsize=12)
ax_det.set_xlim(-WIDTH/2, WIDTH/2)
ax_det.set_yticks([]) # Sakrij brojeve na Y osi
ax_det.spines['top'].set_visible(False)
ax_det.spines['right'].set_visible(False)
ax_det.spines['left'].set_visible(False)

# Inicijalizacija histograma
particles_x = []
bins = np.linspace(-WIDTH/2, WIDTH/2, 80)
bars = ax_det.bar(bins[:-1], np.zeros(len(bins)-1), width=np.diff(bins), 
                  color='cyan', edgecolor='black', alpha=0.8)

# Tekstualni info
info_text = ax_wave.text(0.02, 0.95, "", transform=ax_wave.transAxes, 
                         color='white', fontsize=10)

def update(frame):
    # U svakom frame-u "ispalimo" nekoliko čestica
    # One padaju po vjerojatnosti koju diktira EDC val (intensity_field)
    
    new_particles = np.random.choice(x, size=5, p=detector_prob)
    particles_x.extend(new_particles)
    
    # Ažuriraj histogram
    counts, _ = np.histogram(particles_x, bins=bins)
    max_count = 0
    for bar, count in zip(bars, counts):
        bar.set_height(count)
        if count > max_count: max_count = count
        
    # Skaliraj Y os da histogram lijepo stane
    ax_det.set_ylim(0, max_count * 1.1 if max_count > 0 else 1)
    
    info_text.set_text(f"Particles Detected: {len(particles_x)}\nInterpretation: Wave Guides Flux")
    
    return bars

print("Pokrećem simulaciju... Čestice će formirati pruge interferencije.")
ani = FuncAnimation(fig, update, frames=300, interval=20, blit=False)

plt.show()
