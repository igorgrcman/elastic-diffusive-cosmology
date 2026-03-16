#!/usr/bin/env python3
"""Generate superheavy validation figure for PRC paper."""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

plt.rcParams.update({
    'font.size': 10,
    'font.family': 'serif',
    'axes.linewidth': 1.0,
    'xtick.major.width': 1.0,
    'ytick.major.width': 1.0,
    'lines.linewidth': 1.5,
    'mathtext.fontset': 'cm',
})

fig = plt.figure(figsize=(7.0, 3.5))
gs = GridSpec(1, 2, figure=fig, wspace=0.40)

# ================================================================
# Panel (a): Out-of-Sample Validation
# ================================================================
ax1 = fig.add_subplot(gs[0])

# OOS data: 6 measured superheavy isotopes
# Format: (label, log_t_exp, log_t_edc, log_t_gn_baseline)
oos_data = [
    (r'$^{289}$Fl', +0.32, -0.06, 7.58),
    (r'$^{290}$Fl', +1.28, +1.83, 9.54),
    (r'$^{290}$Mc', -0.19, -1.31, 6.41),
    (r'$^{293}$Lv', -1.22, -1.75, 6.21),
    (r'$^{294}$Ts', -1.59, -1.71, 6.33),
    (r'$^{294}$Og', -3.15, -3.33, 4.71),
]

labels = [d[0] for d in oos_data]
log_exp = np.array([d[1] for d in oos_data])
log_edc = np.array([d[2] for d in oos_data])
log_gn = np.array([d[3] for d in oos_data])

# Perfect agreement line and band
lim = [-5, 11]
ax1.plot(lim, lim, 'k-', lw=0.8, alpha=0.4)
ax1.fill_between(lim,
    [l - 1.5 for l in lim],
    [l + 1.5 for l in lim],
    alpha=0.08, color='gray', label=r'$\pm 1.5$ dex')

# Standard GN (open red squares)
ax1.scatter(log_exp, log_gn, c='crimson', marker='s', s=45,
    facecolors='none', linewidths=1.2, zorder=5,
    label='Standard GN')

# EDC corrected (filled blue circles)
ax1.scatter(log_exp, log_edc, c='steelblue', s=45, zorder=6,
    label='This work')

# Labels for EDC points
offsets = [(5, 5), (5, -12), (-45, 5), (5, 5), (-45, -10), (5, 5)]
for i, lab in enumerate(labels):
    ax1.annotate(lab, (log_exp[i], log_edc[i]),
        textcoords='offset points', xytext=offsets[i],
        fontsize=7, color='steelblue')

ax1.set_xlabel(r'$\log_{10}(t_{1/2}^{\,\mathrm{exp}}\!/\mathrm{s})$')
ax1.set_ylabel(r'$\log_{10}(t_{1/2}^{\,\mathrm{pred}}\!/\mathrm{s})$')
ax1.set_title('(a) Out-of-sample validation', fontsize=10)
ax1.legend(fontsize=7.5, loc='upper left', framealpha=0.9)
ax1.set_xlim(-4.5, 3)
ax1.set_ylim(-5, 11)
ax1.grid(True, alpha=0.2, linewidth=0.5)

# ================================================================
# Panel (b): Predictions for Z=119, 120
# ================================================================
ax2 = fig.add_subplot(gs[1])

# Predictions
A_pred = [298, 302, 304]
log_t_edc = [-0.19, 1.46, 2.89]
log_t_err = [1.3, 1.3, 1.3]
log_t_gn = [7.2, 8.1, 9.3]
pred_labels = [r'$^{298}$119', r'$^{302}$120',
               r'$^{304}$120' + '\n' + r'($N\!=\!184$)']

# Sobiczewski range (approximate)
ax2.axhspan(-1, 2, xmin=0, xmax=1, alpha=0.08, color='green',
    label='Sobiczewski (2007)')

# Standard GN (open red squares)
ax2.scatter(A_pred, log_t_gn, c='crimson', marker='s', s=55,
    facecolors='none', linewidths=1.2, zorder=5,
    label='Standard GN')

# EDC (filled blue circles with error bars)
ax2.errorbar(A_pred, log_t_edc, yerr=log_t_err,
    fmt='o', color='steelblue', capsize=4, capthick=1.2,
    markersize=6, zorder=6, label='This work')

# Labels
label_offsets = [(6, -3), (6, -3), (6, 3)]
for i, lab in enumerate(pred_labels):
    ax2.annotate(lab, (A_pred[i], log_t_edc[i]),
        textcoords='offset points', xytext=label_offsets[i],
        fontsize=8, color='steelblue',
        ha='left', va='center')

# Reference lines
ax2.axhline(y=0, color='gray', linestyle=':', lw=0.8, alpha=0.5)

ax2.set_xlabel('Mass number $A$')
ax2.set_ylabel(r'$\log_{10}(t_{1/2}\!/\mathrm{s})$')
ax2.set_title('(b) Predictions for $Z = 119, 120$', fontsize=10)
ax2.legend(fontsize=7.5, loc='upper left', framealpha=0.9)
ax2.set_xlim(295, 308)
ax2.set_ylim(-3, 11)
ax2.grid(True, alpha=0.2, linewidth=0.5)

plt.tight_layout()

# Save
outdir = '.'
plt.savefig(f'{outdir}/superheavy_validation.pdf',
    bbox_inches='tight', dpi=300)
plt.savefig(f'{outdir}/superheavy_validation.png',
    bbox_inches='tight', dpi=300)
print("Saved superheavy_validation.pdf and .png")
