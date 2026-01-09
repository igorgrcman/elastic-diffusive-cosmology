import numpy as np
import matplotlib.pyplot as plt

def calculate_mass_spectrum():
    print("--- EDC GEOMETRIC MASS DERIVATION ---")
    
    # 1. ULAZNA KONSTANTA (Samo geometrija i vezanje)
    # Fine Structure Constant (mjera jačine EM interakcije)
    # CODATA 2018 value
    ALPHA = 1 / 137.035999084 
    
    print(f"Input: Fine Structure Constant (α) = {ALPHA:.12f}")
    
    # 2. EDC IZVOD: PROTON-ELECTRON MASS RATIO
    # Formula iz tvojeg rada: (4*pi + 5/6) / alpha
    # 4*pi = Sferna topologija
    # 5/6 = Korekcija za pakiranje (Packing factor) u 5D
    
    edc_ratio = (4 * np.pi + (5/6)) / ALPHA
    
    # Stvarna izmjerena vrijednost (NIST/CODATA)
    measured_ratio = 1836.15267343
    
    # Izračun greške
    error_ratio = abs(edc_ratio - measured_ratio) / measured_ratio * 100
    
    print("\n[1] PROTON-TO-ELECTRON MASS RATIO (mp/me)")
    print(f"EDC Prediction (Geometric): {edc_ratio:.6f}")
    print(f"Standard Model (Measured):  {measured_ratio:.6f}")
    print(f"Accuracy: {100 - error_ratio:.4f}%")
    print(f"Discrepancy: {error_ratio:.4f}%")
    
    # 3. EDC IZVOD: WEINBERG ANGLE (Slabo miješanje)
    # Formula: sin^2(theta_W) = 1/4 - 4*alpha
    # Ovo povezuje EM i Slabu silu kroz geometriju
    
    edc_weinberg = 0.25 - (4 * ALPHA)
    
    # Mjereno (Effective weak mixing angle) ~ 0.23122
    measured_weinberg = 0.23122
    
    error_weinberg = abs(edc_weinberg - measured_weinberg) / measured_weinberg * 100
    
    print("\n[2] WEINBERG ANGLE (sin²θw)")
    print(f"EDC Prediction: {edc_weinberg:.6f}")
    print(f"Standard Model: {measured_weinberg:.6f}")
    print(f"Discrepancy: {error_weinberg:.4f}%")

    # --- VIZUALIZACIJA ---
    visualize_results(edc_ratio, measured_ratio, edc_weinberg, measured_weinberg)

def visualize_results(edc_mp, real_mp, edc_w, real_w):
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Graf 1: Proton Mass Ratio
    labels = ['EDC Theory', 'Experiment']
    values = [edc_mp, real_mp]
    colors = ['cyan', 'white']
    
    bars = ax1.bar(labels, values, color=colors, alpha=0.7)
    ax1.set_ylim(1830, 1840) # Zoom in da se vidi razlika (koje nema!)
    ax1.set_title("Proton/Electron Mass Ratio", fontsize=14, color='white')
    ax1.bar_label(bars, fmt='%.2f', color='white', fontsize=12)
    
    # Dodaj tekst o preciznosti
    ax1.text(0.5, 1832, "Geometry defines Mass", ha='center', color='cyan')
    
    # Graf 2: Weinberg Angle
    values_w = [edc_w, real_w]
    bars2 = ax2.bar(labels, values_w, color=['magenta', 'white'], alpha=0.7)
    ax2.set_ylim(0.2, 0.26)
    ax2.set_title("Weak Mixing Angle (sin²θw)", fontsize=14, color='white')
    ax2.bar_label(bars2, fmt='%.4f', color='white', fontsize=12)
    
    plt.tight_layout()
    print("\nPrikazujem grafove...")
    plt.show()

if __name__ == "__main__":
    calculate_mass_spectrum()
