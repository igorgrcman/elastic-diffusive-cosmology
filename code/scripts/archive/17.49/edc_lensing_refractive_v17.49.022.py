"""edc_lensing_final_v17.49.022.py — STRICT EDC

Gravitacijska leća kao refrakcija u Plenumu (River Model).
Cilj: Vizualizacija distorzije izvedene direktno iz mase M.
"""

import numpy as np
import matplotlib.pyplot as plt

def run_lensing_v22():
    print("=" * 60)
    print("EDC LENSING SIMULATOR — FINAL RIGOR (v17.49.022)")
    print("=" * 60)

    # 1. PARAMETRI (Svemirski razmjeri)
    G = 6.67430e-11
    c = 299792458.0
    M_lens = 2e42  # Teška galaksija za jak efekt
    
    r_s = 2 * G * M_lens / c**2
    print(f"[DERIVED] Schwarzschild radius: {r_s:.2f} m")

    # 2. GENERIRANJE GUSTE POZADINE (Da se izbjegne crni ekran)
    W, H = 800, 800
    img = np.zeros((H, W, 3))
    
    # Grid (Mreža) - ključno za vidljivost distorzije
    img[::30, :, 2] = 0.4  # Plave horizontalne linije
    img[:, ::30, 2] = 0.4  # Plave vertikalne linije
    
    # Nasumične "velike" zvijezde
    for _ in range(300):
        y_pos, x_pos = np.random.randint(20, H-20), np.random.randint(20, W-20)
        img[y_pos-2:y_pos+2, x_pos-2:x_pos+2] = 1.0  # Bijeli kvadratići

    # 3. EDC REFRAKCIJSKA MATEMATIKA
    y, x = np.ogrid[:H, :W]
    cx, cy = W // 2, H // 2
    dx = x - cx
    dy = y - cy
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 1e-9

    # Skaliranje za vizualni prikaz (EDC bridge)
    # n(r) gradijent uzrokuje otklon proporcionalan r_s / r
    scale_factor = 2000.0 
    displacement = (scale_factor * r_s) / r

    # Backward ray tracing
    src_x = x - dx * (displacement / r)
    src_y = y - dy * (displacement / r)

    # Interpolacija (Mapiranje piksela)
    src_x = np.clip(src_x, 0, W - 1).astype(int)
    src_y = np.clip(src_y, 0, H - 1).astype(int)
    
    lensed_img = img[src_y, src_x]
    
    # 4. EVENT HORIZONT (Masa u centru koja blokira svjetlost)
    mask = r < 15
    lensed_img[mask] = [0, 0, 0]

    # 5. PRIKAZ
    plt.figure(figsize=(10, 10), facecolor='black')
    plt.imshow(lensed_img)
    plt.title("EDC Gravitational Lensing (Strict Refractive Model v0.22)", color='white')
    plt.axis('off')
    print("[STATUS] Rendering complete. Showing plot...")
    plt.show()

if __name__ == "__main__":
    run_lensing_v22()
