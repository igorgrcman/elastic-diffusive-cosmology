
"""edc_hidrogen_atom_check.py (strict)

Hydrogen atom identity check: a0 = r_e / alpha^2

Epistemic status (strict):
  - BASELINE: r_e and alpha are baseline constants here (not derived)
  - DERIVED: a0 computed from the identity (definition-level consequence)

This is NOT an independent prediction unless r_e and/or alpha are derived from EDC without CODATA injection.
"""

def run():
    print("=" * 60)
    print("EDC HYDROGEN ATOM CHECK — STRICT (Identity/Bridge)")
    print("Based on Book v17.49 Section 4.2")
    print("=" * 60)
    print()

    # Baseline inputs
    r_e = 2.8179403227e-15      # m (classical electron radius)
    alpha = 7.2973525693e-3     # fine-structure constant

    print("[BASELINE INPUTS]")
    print(f"  r_e   = {r_e:.13e} m")
    print(f"  alpha = {alpha:.13e}")
    print()

    # Identity
    a0 = r_e / (alpha ** 2)

    # Benchmark
    a0_ref = 5.29177210903e-11  # m

    rel_err = abs(a0 - a0_ref) / a0_ref

    print("[DERIVED RESULT]")
    print(f"  a0 (r_e/alpha^2) = {a0:.13e} m")
    print()
    print("[BENCHMARK]")
    print(f"  a0 (benchmark)   = {a0_ref:.13e} m")
    print(f"  relative dev     = {rel_err:.3e}  ({rel_err*1e6:.2f} ppm)")
    print()

    if rel_err < 1e-6:
        print("PASS: Identity holds to numerical rounding.")
        print("NOTE: Expected when inputs are baseline constants.")
    else:
        print("WARN: Deviation larger than expected — check input values/rounding.")
    print()

    print("=" * 60)
    print("CONCLUSION (strict):")
    print("• With baseline inputs, this is an identity check, not an independent prediction.")
    print("• For an EDC prediction claim, derive r_e and/or alpha from EDC without CODATA injection.")
    print("=" * 60)


if __name__ == "__main__":
    run()
