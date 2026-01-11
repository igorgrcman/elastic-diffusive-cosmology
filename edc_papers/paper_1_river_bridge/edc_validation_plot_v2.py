import numpy as np
import matplotlib.pyplot as plt

# Data from Table 1 (v17.49.5 results)
# Sorted from largest to smallest step for consistent plotting
dphi_eff = np.array([1.9999953e-4, 9.9999766e-5, 4.9999883e-5])
newton  = np.array([-0.897536, -0.233044,  0.000207])
anomaly = np.array([42.982419, 42.990724, 42.922350])
anom_ci95 = np.array([2.5e-4, 1.6e-3, 9.8e-4]) 

# Sort indices to ensure lines plot correctly
idx = dphi_eff.argsort()
dphi_eff, newton, anomaly, anom_ci95 = dphi_eff[idx], newton[idx], anomaly[idx], anom_ci95[idx]

fig, ax1 = plt.subplots(figsize=(10, 6))

# Newton Drift (LHS)
ax1.set_xscale("log")
line1, = ax1.plot(dphi_eff, newton, marker="o", color="tab:red", linestyle="--", alpha=0.7, label="Newtonian Drift (LHS)")
ax1.set_xlabel(r"Effective Step Size $d\phi_{\mathrm{eff}}$ (rad)")
ax1.set_ylabel("Newtonian Drift [arcsec/century]", color="tab:red")
ax1.tick_params(axis='y', labelcolor="tab:red")
ax1.grid(True, which="both", ls="--", alpha=0.4)

# Anomaly (RHS)
ax2 = ax1.twinx()
line2 = ax2.errorbar(dphi_eff, anomaly, yerr=anom_ci95, fmt="o", color="tab:blue",
                     capsize=4, markersize=8, label="Bridge-Newton Anomaly $\pm$ 95% CI (RHS)")
ax2.set_ylabel("Anomalous Precession [arcsec/century]", color="tab:blue")
ax2.tick_params(axis='y', labelcolor="tab:blue")

# GR Benchmark line
line3 = ax2.axhline(y=42.98, color="black", linestyle=":", alpha=0.6, label="GR Benchmark (42.98 as/cy)")

# Legend adjustment: Moving it to avoid covering the 5e-5 point
lines = [line1, line2, line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.15), 
           ncol=3, frameon=True, shadow=True)

plt.title("EDC Mercury Precession: Convergence and Systematic Analysis")
plt.tight_layout()

plt.savefig("edc_mercury_validation_v2.png", dpi=300, bbox_inches='tight')
print("Plot saved as edc_mercury_validation_v2.png")
