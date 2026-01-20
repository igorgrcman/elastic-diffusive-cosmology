import numpy as np
import matplotlib.pyplot as plt

def run_fixed_lensing():
    print("====================================================")
    print("EDC LENSING V0.23 - PROOF OF CONCEPT")
    print("====================================================")

    W, H = 800, 800
    # 1. Kreiramo sliku sa jako debelom plavom mrežom
    img = np.zeros((H, W, 3))
    img[::20, :, 2] = 0.8  # Jaka plava mreža (horizontalna)
    img[:, ::20, 2] = 0.8  # Jaka plava mreža (vertikalna)
    
    # Dodajemo velike bijele krugove (zvijezde)
    for _ in range(50):
        y_c, x_c = np.random.randint(100, 700, 2)
        yy, xx = np.ogrid[:H, :W]
        star_mask = (xx - x_c)**2 + (yy - y_c)**2 < 25
        img[star_mask] = 1.0

    # 2. EDC Matematika (Ista ona koja radi na Merkuru)
    # G, M, c su ovdje sažeti u jedan 'power' faktor radi jednostavnosti prikaza
    distortion_power = 80.0 
    
    y, x = np.ogrid[:H, :W]
    cx, cy = W // 2, H // 2
    dx, dy = x - cx, y - cy
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 1.0

    # Skretanje zraka (EDC Refrakcija)
    displacement = (distortion_power**2) / r
    src_x = np.clip(x - dx * (displacement / r), 0, W - 1).astype(int)
    src_y = np.clip(y - dy * (displacement / r), 0, H - 1).astype(int)
    
    # 3. Primjena leće
    lensed_img = img[src_y, src_x]
    
    # Crna rupa u sredini
    mask = r < 20
    lensed_img[mask] = 0

    # 4. SPREMANJE I PRIKAZ
    plt.figure(figsize=(10, 10))
    plt.imshow(lensed_img)
    plt.axis('off')
    
    # Spremamo na disk da budemo sigurni
    plt.savefig('edc_lensing_output.png', bbox_inches='tight', pad_inches=0)
    print("SLIKA JE SPREMLJENA KAO: edc_lensing_output.png")
    plt.show()

if __name__ == "__main__":
    run_fixed_lensing()
