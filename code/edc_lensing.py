import numpy as np
import matplotlib.pyplot as plt

def generate_background_stars(width, height, num_stars=2000):
    """Generira pozadinu sa zvijezdama i pravilnom mrežom (za lakše uočavanje distorzije)."""
    img = np.zeros((height, width, 3)) # Crna pozadina
    
    # 1. Nasumične zvijezde
    for _ in range(num_stars):
        y = np.random.randint(0, height)
        x = np.random.randint(0, width)
        brightness = np.random.rand()
        img[y, x] = [brightness, brightness, brightness]
        
    # 2. Pravilna mreža (Grid) - da se jasno vidi zakrivljenje
    # Obojit ćemo je u plavo (Plenum Grid)
    spacing = 50
    img[::spacing, :, 2] = 0.3 # Plave linije
    img[:, ::spacing, 2] = 0.3
    
    return img

def apply_edc_lensing(img, lens_x, lens_y, einstein_radius):
    """
    Simulira prolazak svjetlosti kroz gušći Plenum oko mase.
    Koristi formulu leće: beta = theta - alpha(theta)
    """
    height, width, _ = img.shape
    y_grid, x_grid = np.meshgrid(np.arange(height), np.arange(width), indexing='ij')
    
    # Vektori od centra leće do svakog piksela
    dy = y_grid - lens_y
    dx = x_grid - lens_x
    
    # Udaljenost svakog piksela od centra (r)
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 0.0001 # Izbjegavanje dijeljenja s nulom
    
    # --- EDC FIZIKA: INDEKS LOMA ---
    # Kut skretanja alpha ovisi o gradijentu tlaka (gustoće) Plenuma.
    # U weak-field limitu: alpha = 4GM / (c^2 * r)
    # Ovdje to modeliramo kao pomak piksela proporcionalan Einsteinovom radijusu.
    
    # Iznos pomaka (koliko Plenum "vuče" sliku prema centru)
    # Formula leće: pomak = R_E^2 / r
    distortion_magnitude = (einstein_radius**2) / r
    
    # Izračunaj 'izvornu' poziciju piksela (gdje bi svjetlost bila da nema mase)
    # Ovo je 'backward ray tracing'
    src_x = x_grid - dx * (distortion_magnitude / r)
    src_y = y_grid - dy * (distortion_magnitude / r)
    
    # Mapiranje (interpolacija)
    # Za jednostavnost, koristimo nearest-neighbor (zaokruživanje)
    src_x = np.clip(np.round(src_x).astype(int), 0, width - 1)
    src_y = np.clip(np.round(src_y).astype(int), 0, height - 1)
    
    return img[src_y, src_x]

# --- PARAMETRI SIMULACIJE ---
W, H = 800, 800
EINSTEIN_RADIUS = 120 # Snaga gravitacije (Masa objekta)

print("Generiram pozadinu svemira...")
background = generate_background_stars(W, H)

print("Simuliram EDC refrakciju (Gravitacijska leća)...")
# Centar leće
cx, cy = W // 2, H // 2
lensed_image = apply_edc_lensing(background, cx, cy, EINSTEIN_RADIUS)

# --- DODAVANJE CRNE RUPE / MASE U SREDINU ---
# U centru je "Event Horizon" ili objekt koji blokira svjetlost
y, x = np.ogrid[:H, :W]
mask = (x - cx)**2 + (y - cy)**2 <= (EINSTEIN_RADIUS * 0.8)**2
lensed_image[mask] = 0 # Crna rupa

# --- VIZUALIZACIJA ---
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig.patch.set_facecolor('black')

# Lijevo: Originalni svemir (Bez mase)
axes[0].imshow(background)
axes[0].set_title("1. Empty Space (Uniform Plenum)", color='white')
axes[0].axis('off')

# Desno: EDC Leća
axes[1].imshow(lensed_image)
axes[1].set_title(f"2. EDC Lensing (Plenum Refraction n(r))", color='cyan')
axes[1].axis('off')

# Tekst objašnjenja
axes[1].text(0.5, -0.1, "Light follows density gradient of the vacuum.", 
             transform=axes[1].transAxes, color='gray', ha='center')

print("Prikazujem rezultat.")
plt.show()
