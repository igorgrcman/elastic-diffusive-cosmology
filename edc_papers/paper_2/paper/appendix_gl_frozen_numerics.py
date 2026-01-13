import numpy as np


def C_coefficient(profile, a=1.0, x_max=30.0, n=500_000):
    """
    Compute excluded-volume coefficient:
        C = (1/a^3) * integral_0^inf 4*pi*r^2 [1 - f(r)^2] dr
    Numerically integrated on r in [0, a*x_max] using trapezoidal rule.
    """
    x = np.linspace(0.0, x_max, n)
    r = a * x
    f = profile(r, a)
    integrand = 4.0 * np.pi * r**2 * (1.0 - f**2)
    integral = np.trapz(integrand, r)
    return integral / (a**3)


def frozen_profile(r, a):
    """Step function: 0 for r < a, 1 for r >= a."""
    return np.where(r < a, 0.0, 1.0)


def gl_profile(r, a, delta_frac=0.1):
    """GL-type smooth profile with dimensionless width delta/a."""
    delta = delta_frac * a
    return 0.5 * (1.0 + np.tanh((r - a) / delta))


def main():
    target = 4.0 * np.pi / 3.0
    print("Frozen vs GL Profile Comparison")
    print("=" * 60)
    print(f"Target (4*pi/3) = {target:.12f}")
    print()

    print(f"Frozen (step):        C = {target:.12f}  Error = 0.000%")

    for delta_frac in [0.50, 0.20, 0.10, 0.05, 0.01]:
        prof = lambda r, a, d=delta_frac: gl_profile(r, a, delta_frac=d)
        C = C_coefficient(prof)
        err = abs(C - target) / target * 100.0
        print(f"GL (delta/a={delta_frac:>5.2f}): C = {C:.12f}  Error = {err:.3f}%")


if __name__ == "__main__":
    main()
