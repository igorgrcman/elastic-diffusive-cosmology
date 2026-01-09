import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- EDC FIZIKA: PILOT WAVE INTERFERENCIJA ---
# Čestica je 'Flux Event' (lokalizirana).
# Prostor je 'Plenum' (medij koji prenosi valove).
# Čestica 'jaše' na valu kojeg sama stvara ili koji prolazi kroz proreze.

def calculate_wave_field(x, y, k, slit_dist):
    """
    Računa intenzitet vala na membrani nakon prolaska kroz dva proreza.
    Princip superpozicije: Val1 + Val2
    """
    # Udaljenost od prvog proreza (Slit 1)
    r1 = np.sqrt((x - slit_dist/2)**2 + y**2)
    # Udaljenost od drugog proreza (Slit 2)
    r2 = np.sqrt((x + slit_dist/2)**2 + y**2)
    
    # Valna funkcija (sinusni valovi iz izvora)
    # A * sin(k*r - w*t) ... ovdje gledamo vremenski usrednjen intenzitet
    # Amplituda opada s udaljenosti (1/sqrt(r) za 2D valove)
    
    amp1 = 1 / np.sqrt(r1 + 0.1)
    amp2 = 1 / np.sqrt(r2 + 0.1)
    
    # Superpozicija (zbrajanje faza)
    wave_field = amp1 * np.sin(k * r1) + amp2 * np.sin(k * r2)
    
    # Intenzitet = kvadrat amplitude
    intensity = wave_field**2
    return intensity

# --- POSTAVKE SIMULACIJE ---
resolution = 200
wavelength = 1.5  # Valna duljina 'Plenum' vala
k = 2 * np.pi / wavelength
slit_separation = 6.0  # Razmak između proreza

# Mreža prostora (Ekran je na vrhu, prorezi na dnu)
x = np.linspace(-15, 15, resolution)
y = np.linspace(0, 30, resolution)
X, Y = np.meshgrid(x, y)

print("Računam EDC valno polje...")
# Izračun polja interferencije
Intensity_Field = calculate_wave_field(X, Y, k, slit_separation)

# Vjerojatnost nalaženja čestice na detektoru (gornji rub y=30)
# Uzimamo zadnji red intenziteta
detector_prob = Intensity_Field[-1, :]
detector_prob /= np.sum(detector_prob) # Normalizacija

# --- VIZUALIZACIJA ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 8))

# 1. GLAVNI EKRAN: Valno polje (Plenum)
ax_wave = fig.add_axes([0.1, 0.3, 0.8, 0.6]) # [left, bottom, width, height]
ax_wave.set_title("EDC Pilot Wave Dynamics (Double Slit)", color='white', fontsize=14)
ax_wave.set_ylabel("Distance from Slits", color='white')
ax_wave.axis('off')

# Crtanje toplinske mape vala (Plava = 'Plenum Density')
# Koristimo 'vmin' i 'vmax' da istaknemo pruge
im = ax_wave.imshow(Intensity_Field, extent=[-15, 15, 0, 30], origin='lower', 
                    cmap='ocean', aspect='auto', vmin=0, vmax=0.5)

# Crtanje proreza (Zid na dnu)
ax_wave.plot([-15, -slit_separation/2-0.5], [0, 0], color='gray', linewidth=5)
ax_wave.plot([-slit_separation/2+0.5, slit_separation/2-0.5], [0, 0], color='gray', linewidth=5)
ax_wave.plot([slit_separation/2+0.5, 15], [0, 0], color='gray', linewidth=5)
ax_wave.text(0, -2, "Slits (Flux Entry)", color='white', ha='center')

# 2. DONJI EKRAN: Detektor (Gdje čestice udaraju)
ax_det = fig.add_axes([0.1, 0.05, 0.8, 0.2])
ax_det.set_xlabel("Detector Screen Position", color='white')
ax_det.set_yticks([])
ax_det.set_xlim(-15, 15)
ax_det.set_title("Particle Impact Accumulation", color='cyan', fontsize=10)

# Inicijalizacija čestica (prazan histogram)
particles_x = []
hist_bins = np.linspace(-15, 15, 100)
n, _ = np.histogram([], bins=hist_bins)
bars = ax_det.bar(hist_bins[:-1], n, width=0.3, color='cyan', alpha=0.7)

# Tekst za EDC objašnjenje
info_text = ax_wave.text(0.02, 0.95, "", transform=ax_wave.transAxes, color='white', fontsize=9)

def update(frame):
    # Simuliramo udarac jedne po jedne čestice
    # Čestice ne padaju nasumično, nego po vjerojatnosti vala (EDC determinizam)
    
    # Odaberi poziciju na temelju distribucije intenziteta
    impact_x = np.random.choice(x, p=detector_prob)
    particles_x.append(impact_x)
    
    # Ažuriraj histogram
    n, _ = np.histogram(particles_x, bins=hist_bins)
    for bar, height in zip(bars, n):
        bar.set_height(height)
    
    ax_det.set_ylim(0, max(n) + 1 if len(particles_x) > 0 else 1)
    
    # Animiraj "putanju" čestice (samo vizualni efekt - bijela točkica leti)
    # U EDC-u čestica prati liniju toka ("surfa")
    
    info_text.set_text(f"Particles Detected: {len(particles_x)}\nInterpretation: Wave Guides Flux")
    
    return bars

print("Pokrećem simulaciju... Gledajte kako val vodi čestice.")
ani = FuncAnimation(fig, update, frames=200, interval=20, blit=False)

plt.show()
