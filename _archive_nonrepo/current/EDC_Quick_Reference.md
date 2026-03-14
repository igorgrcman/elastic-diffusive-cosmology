# EDC Quick Reference Card

## 🔢 FORMULE — Brzi Pregled

```
┌─────────────────────────────────────────────────────────────────┐
│  ℏ = σ · rₑ³ / c                          [Status: I]          │
│                                                                 │
│  α = mₑc² / (σ · rₑ²)                     [Status: I]          │
│                                                                 │
│  G = c⁴ Rξ¹² / (128π² σ rₑ¹³)            [Status: I]          │
│                                                                 │
│  v(r) = √(2GM/r)                          [Status: D]          │
└─────────────────────────────────────────────────────────────────┘
```

## 📊 PARAMETRI

```
σ  = 1.41×10¹⁸ J/m²     (napetost membrane)
rₑ = 2.82×10⁻¹⁵ m       (klasični radijus elektrona)
Rξ = 2.16×10⁻¹⁸ m       (kompaktna dimenzija)
c  = 2.998×10⁸ m/s      (brzina svjetlosti)
```

## ⚠️ UPOZORENJA

```
❌ NE KORISTI: ℏ = σ·Rξ³/c     (off by 10¹⁰!)
❌ NE KORISTI: G = c²/(4πσ)    (off by 10⁸!)
❌ NE KORISTI: F_bulk u m/s²   (krive dimenzije!)

✅ KORISTI: ℏ = σ·rₑ³/c
✅ KORISTI: G = c⁴Rξ¹²/(128π²σrₑ¹³)
✅ KORISTI: F_bulk u m³/s⁴
```

## 🎯 HIJERARHIJA

```
(Rξ/rₑ)¹² = 4.1×10⁻³⁸

→ Geometrijski razlog zašto je gravitacija 10³⁸× slabija od EM!
```

## 📋 EPISTEMIC STATUS

```
D = Derived (matematički dokazano)
I = Identified (numerički match, nije jedinstveno)
P = Proposed (spekulacija)
Cal = Calibrated (kalibrirano iz opservacija)
BL = Baseline (CODATA vrijednost)
```

## ✅ ŠTO JE DOKAZANO (D)

- v(r) = √(2GM/r) iz Euler-Laplace
- Superpozicija M = ΣMᵢ iz linearnosti
- ν_bulk ≤ 2.6×10¹¹ m²/s iz Merkura

## ⚠️ ŠTO JE IDENTIFICIRANO (I)

- ℏ, α, G formule — rade numerički
- Potencije 12, 13 — pronađene fitanjem

## ❓ ŠTO JE SPEKULACIJA (P)

- 12 = 4×3 interpretacija
- 13 = 12+1 interpretacija
- 128π² = (4π)²×8 interpretacija
