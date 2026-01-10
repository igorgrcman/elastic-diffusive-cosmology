"""edc_constants.py

Epistemic status:
- EDC relations computed here are PROPOSED unless a derivation is explicitly provided in the book.
- Reference numbers are BASELINE (PDG/NIST/CODATA), used only for comparison.

Sources (baseline):
- PDG 2020 Physical Constants: mp/me; sin^2 theta_hat(MZ) (MS-bar); mW; mZ; and footnote sin^2 theta_eff.
- NIST Fundamental Physical Constants: sin^2 theta_W.
"""

import numpy as np
import matplotlib.pyplot as plt
from edc.constants.registry import get_constant

def calculate_mass_spectrum():
    print("--- EDC GEOMETRIC MASS DERIVATION ---")
    
    # 1. INPUT CONSTANT (Geometry only (workbench))

    # CODATA 2018 value
    ALPHA = get_constant('alpha', allow={'BASELINE'}).value  # dimensionlessprint(f"Input: Fine Structure Constant (α) = {ALPHA:.12f}")
    
    # 2. EDC IZVOD: PROTON-ELECTRON MASS RATIO
    # Candidate relation (from manuscript): (4*pi + 5/6) / alpha
    # 4*pi = Sferna topologija
    # 5/6 = Korekcija za pakiranje (Packing factor) u 5D
    
    edc_ratio = (4 * np.pi + (5/6)) / ALPHA
    
    # Stvarna izmjerena vrijednost (NIST/CODATA)
    measured_ratio = 1836.15267343
    

    error_ratio = abs(edc_ratio - measured_ratio) / measured_ratio * 100
    
    print("\n[1] PROTON-TO-ELECTRON MASS RATIO (mp/me)")
    print(f"EDC (PROPOSED relation): {edc_ratio:.6f}")
    print(f"Baseline (PDG):  {measured_ratio:.6f}")
    print(f"Accuracy: {100 - error_ratio:.4f}%")
    print(f"Discrepancy: {error_ratio:.4f}%")
    

    # Formula: sin^2(theta_W) = 1/4 - 4*alpha
    # This connects EM i Slabu silu kroz geometriju
    
    edc_weinberg = 0.25 - (4.0 * ALPHA)  # PROPOSED relation

    # Baseline references for sin^2(theta_W) depend on definition/scheme.
    # Use multiple references so we can see where the PROPOSED relation is 'closest'.
    sin2_msbar = get_constant('sin2_thetaW_hat_mZ_MSbar', allow={'BASELINE'}).value
    sin2_eff  = get_constant('sin2_thetaW_eff', allow={'BASELINE'}).value
    mw = get_constant('mW_GeV', allow={'BASELINE'}).value
    mz = get_constant('mZ_GeV', allow={'BASELINE'}).value
    sin2_on_shell = 1.0 - (mw * mw) / (mz * mz)  # on-shell definition (mass-ratio form)
    sin2_nist = get_constant('sin2_thetaW_NIST', allow={'BASELINE'}).value

    refs = [
        ("MS-bar at MZ (PDG)", sin2_msbar),
        ("Effective (PDG footnote)", sin2_eff),
        ("On-shell (1 - mW^2/mZ^2)", sin2_on_shell),
        ("NIST sin^2(theta_W)", sin2_nist),
    ]

    def rel_err(a: float, b: float) -> float:
        return abs(a - b) / abs(b) if b != 0 else float("nan")

    print("\n[2] WEAK MIXING ANGLE sin^2(theta_W) (definition-dependent)")
    print(f"EDC (PROPOSED relation): {edc_weinberg:.6f}")
    for label, val in refs:
        print(f"Baseline {label:>28}: {val:.6f}  |  rel.err = {rel_err(edc_weinberg, val)*100:.3f}%")

    # --- VISUALIZATION ---
    visualize_results(edc_ratio, measured_ratio, edc_weinberg, refs)


def visualize_results(edc_mp, real_mp, edc_w, refs):
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Proton Mass Ratio
    labels = ['EDC (PROPOSED)', 'Baseline (PDG)']
    values = [edc_mp, real_mp]
    colors = ['cyan', 'white']
    
    bars = ax1.bar(labels, values, color=colors, alpha=0.7)
    ax1.set_ylim(1830, 1840) # Zoom in da se vidi razlika (koje nema!)
    ax1.set_title("Proton/Electron Mass Ratio", fontsize=14, color='white')
    ax1.bar_label(bars, fmt='%.2f', color='white', fontsize=12)
    
    # Dodaj tekst o preciznosti
    
    
    # Plot 2: Weinberg Angle
    labels_w = ['EDC (PROPOSED)'] + [lbl for (lbl, _) in refs]
    values_w = [edc_w] + [val for (_, val) in refs]
    x = np.arange(len(values_w))
    bars2 = ax2.bar(x, values_w, alpha=0.7)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels_w, rotation=20)
    ax2.set_ylim(0.2, 0.26)
    ax2.set_title("Weak Mixing Angle (sin²θw)", fontsize=14, color='white')
    ax2.bar_label(bars2, fmt='%.4f', color='white', fontsize=12)
    
    plt.tight_layout()
    print("\nGenerating plots...")
    plt.show()

if __name__ == "__main__":
    calculate_mass_spectrum()
