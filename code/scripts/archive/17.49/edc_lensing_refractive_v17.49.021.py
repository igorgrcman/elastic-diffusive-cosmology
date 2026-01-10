import numpy as np
import matplotlib.pyplot as plt

def run_strict_lensing():
    # 1. OSNOVNI PARAMETRI (Fizičke konstante)
    G = 6.67430e-11
    c = 299792458.0
    M_lens = 1e42  # Masa galaktičkog reda za vidljiv efekt
    
    # 2. EDC FIZIKA: Schwarzschildov radijus i snaga distorzije
    r_s = 2 * G * M_lens / c**2
    k = 150.0  # Skaliranje za vizuelni prikaz na ekranu
    distortion_power = k * np.sqrt(r_s)

    # 3. GENERISANJE POZADINE (Zvezde i mreža)
    W, H = 800, 800
    img = np.zeros((H, W, 3))
    
    # Dodavanje guste mreže (Grid) - ključno za uočavanje distorzije
    img[::40, :, 2] = 0.5  # Plave horizontalne linije
    img[:, ::40, 2] = 0.5  # Plave vertikalne linije
    
    # Dodavanje većih zvezda (ne samo 1 piksel)
    for _ in range(200):
        y_pos, x_pos = np.random.randint(50, H-50), np.random.randint(50, W-50)
        img[y_pos-2:y_pos+2, x_pos-2:x_pos+2] = 1.0 # Bele zvezde 4x4 piksela

    # 4. PRIMENA LENSINGA (Refrakcija Plenuma)
    y, x = np.ogrid[:H, :W]
    cx, cy = W // 2, H // 2
    dx = x - cx
    dy = y - cy
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 1e-9

    # Skretanje svetlosti prema EDC modelu refrakcije
    displacement = (distortion_power**2) / r
    src_x = x - dx * (displacement / r)
    src_y = y - dy * (displacement / r)

    # Mapiranje koordinata (Interpolacija)
    src_x = np.clip(src_x, 0, W - 1).astype(int)
    src_y = np.clip(src_y, 0, H - 1).astype(int)
    
    lensed_img = img[src_y, src_x]
    
    # Dodavanje Event Horizonta (Masa u centru koja blokira svetlost)
    mask = r < (distortion_power * 0.5)
    lensed_img[mask] = 0

    # 5. PRIKAZ
    plt.figure(figsize=(10, 10))
    plt.imshow(lensed_img)
    plt.title("EDC Gravitational Lensing (Strict Refraction Model)")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    run_strict_lensing()
