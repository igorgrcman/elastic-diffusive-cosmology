import numpy as np
import matplotlib.pyplot as plt

# Podaci (v17.49.5 + ujednačeni nazivi)
dphi_eff = np.array([1.9999953e-4, 9.9999766e-5, 4.9999883e-5])
newton  = np.array([-0.897536, -0.233044,  0.000207])
anomaly = np.array([42.982419, 42.990724, 42.922350])
anom_ci95 = np.array([2.5e-4, 1.6e-3, 9.8e-4]) 

fig, ax1 = plt.subplots(figsize=(10, 6))

# Invertiramo X-os: profinjenje (manji dphi) ide udesno
ax1.set_xscale("log")
ax1.set_xlim(2.5e-4, 4e-5) # coarse (lijevo) -> fine (desno)

# Newtonov drift (LHS)
line1, = ax1.plot(dphi_eff, newton, marker="o", color="tab:red", label="Newtonian drift (arcsec/century)")
ax1.set_xlabel(r"Effective step size $d\phi_{\mathrm{eff}}$ (rad) $\rightarrow$ Refinement direction")
ax1.set_ylabel("Newtonian drift (arcsec/century)", color="tab:red")
ax1.tick_params(axis='y', labelcolor="tab:red")
ax1.grid(True, which="both", ls="--", alpha=0.3)

# Anomalija (RHS)
ax2 = ax1.twinx()
line2 = ax2.errorbar(dphi_eff, anomaly, yerr=anom_ci95, fmt="o", color="tab:blue",
                     capsize=4, markersize=8, label="Anomaly ± 95% CI (arcsec/century)")
ax2.set_ylabel("Anomalous precession (arcsec/century)", color="tab:blue")
ax2.tick_params(axis='y', labelcolor="tab:blue")

# GR Benchmark linija
line3 = ax2.axhline(y=42.98, color="black", linestyle=":", alpha=0.6, label="GR Benchmark (42.98)")

# Stability Text Box
textstr = "EDC Stability Check:\nBridge H-drift ~ 10⁻¹⁰\nAcross all runs"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

# Kombinirana legenda
lines = [line1, line2, line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=3)

plt.title("EDC Mercury Precession: Numerical Refinement & Stability Analysis")
plt.tight_layout()
plt.savefig("edc_validation_final.png", dpi=300, bbox_inches='tight')
