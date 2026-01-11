import numpy as np
import matplotlib.pyplot as plt

# Metrološki podaci iz v17.51 loga
dphi_eff = np.array([1.9999953e-4, 9.9999766e-5, 7.4999813e-5, 4.9999883e-5, 3.3333317e-5])
newton  = np.array([-0.897390, -0.230477, -0.149687, 0.000228, 0.014073])
anomaly = np.array([42.981552, 42.985448, 43.001897, 42.922965, 42.932474])
ci95 = np.array([1.2e-4, 9.9e-4, 1.2e-3, 5.7e-4, 1.0e-2])

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xscale("log")
ax1.set_xlim(2.5e-4, 2.5e-5) # Fine to the right

# Newton
line1, = ax1.plot(dphi_eff, newton, 'o--', color='tab:red', label="Newtonian drift (arcsec/century)")
ax1.set_xlabel(r"Effective step size $d\phi_{\mathrm{eff}}$ (rad) $\rightarrow$ Refinement")
ax1.set_ylabel("Newtonian drift (arcsec/century)", color='tab:red')

# Anomaly
ax2 = ax1.twinx()
line2 = ax2.errorbar(dphi_eff, anomaly, yerr=ci95, fmt='o-', color='tab:blue', capsize=4, label="Anomaly ± 95% CI (arcsec/century)")
ax2.axhline(y=42.98, color='black', ls=':', alpha=0.6, label="GR Benchmark (42.98)")
ax2.set_ylabel("Anomalous precession (arcsec/century)", color='tab:blue')

# Stability Box
ax1.text(0.05, 0.95, "Bridge H-drift range:\n5.1e-10 to 1.7e-09\nStability: Verified", 
         transform=ax1.transAxes, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower left', bbox_to_anchor=(0.1, -0.2), ncol=2)

plt.tight_layout()
plt.savefig("convergence_plot.pdf")
print("Grafikon convergence_plot.pdf generiran.")
