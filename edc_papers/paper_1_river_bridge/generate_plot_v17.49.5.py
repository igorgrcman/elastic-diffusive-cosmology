import numpy as np
import matplotlib.pyplot as plt

# Podaci iz v17.49.5 tablice
dphi_eff = np.array([1.9999953e-4, 9.9999766e-5, 4.9999883e-5])
newton  = np.array([-0.897536, -0.233044,  0.000207])
anomaly = np.array([42.982419, 42.990724, 42.922350])
anom_ci95 = np.array([2.5e-4, 1.6e-3, 9.8e-4])

plt.figure(figsize=(8, 5))
fig, ax1 = plt.subplots()

# Newton drift (Lijeva os)
ax1.set_xscale("log")
ax1.plot(dphi_eff, newton, 'o-', color='tab:red', label="Newtonov drift (as/cy)")
ax1.set_xlabel(r"Veličina koraka $d\phi_{\mathrm{eff}}$ (rad)")
ax1.set_ylabel("Newtonov numerički drift", color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.grid(True, which="both", ls="-", alpha=0.2)

# Anomalija (Desna os)
ax2 = ax1.twinx()
ax2.errorbar(dphi_eff, anomaly, yerr=anom_ci95, fmt='o-', color='tab:blue', capsize=5, label="EDC Anomalija ± 95% CI")
ax2.set_ylabel("Anomalna precesija (as/cy)", color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title("Konvergencija Newtonovog drifta i stabilnost EDC anomalije")
fig.tight_layout()
plt.savefig("convergence_plot.pdf") # Sprema kao vektorski PDF
print("Grafikon spremljen kao convergence_plot.pdf")
