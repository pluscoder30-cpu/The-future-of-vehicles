# PHI GOLD SYNTHESIZER — MECHANICAL DESIGN

## Structural Engineering

---

## CHASSIS GEOMETRY

```
PHI-HARMONIC CHASSIS RATIOS:
═══════════════════════════════════════════════════════════════

  Overall Length:    500mm (base)
  Overall Width:     400mm (500/φ⁰·⁵)
  Overall Height:    600mm (500×φ⁰·²)
  Chamber Diameter:  140mm (500/φ²)
  Chamber Height:    180mm (500/φ²·⁵)

  ┌─────────────────────────────────────────────┐
  │                                             │
  │  ┌─────────────────────────────────────┐   │
  │  │                                     │   │
  │  │  TOP: HOPPER (500ml)               │   │
  │  │  ┌─────────────────────────────┐   │   │
  │  │  │  ╱╲╱╲╱╲ Feedstock Input ╱╲  │   │   │
  │  │  └─────────────────────────────┘   │   │
  │  │                                     │   │
  │  │  MIDDLE: TRANSMUTATION CHAMBER     │   │
  │  │  ┌─────────────────────────────┐   │   │
  │  │  │  ╔═════════════════════╗    │   │   │
  │  │  │  ║  1,200°C INTERNAL   ║    │   │   │
  │  │  │  ║  2.5L VOLUME        ║    │   │   │
  │  │  │  ║  3× RESONANCE COILS ║    │   │   │
  │  │  │  ╚═════════════════════╝    │   │   │
  │  │  └─────────────────────────────┘   │   │
  │  │                                     │   │
  │  │  BOTTOM: GOLD OUTPUT               │   │
  │  │  ┌─────────────────────────────┐   │   │
  │  │  │  ═══ GOLD COLLECTION ═══   │   │   │
  │  │  └─────────────────────────────┘   │   │
  │  │                                     │   │
  │  │  FPB-5 BATTERY (side compartment)  │   │
  │  │  ┌──────────┐                      │   │
  │  │  │  FPB-5   │                      │   │
  │  │  │  48V     │                      │   │
  │  │  │  50Ah    │                      │   │
  │  │  └──────────┘                      │   │
  │  │                                     │   │
  │  └─────────────────────────────────────┘   │
  │                                             │
  │  ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●    │
  │  Width: 400mm                              │
  │                                             │
  └─────────────────────────────────────────────┘
```

---

## TRANSMUTATION CHAMBER

| Parameter | Value |
|-----------|-------|
| Internal Volume | 2.5 liters |
| Inner Diameter | 140mm |
| Height | 180mm |
| Wall Thickness | 6mm Inconel 625 |
| Liner Thickness | 3mm Zirconia ceramic |
| Max Operating Temp | 1,200°C |
| Max Pressure | 2 atm |
| Seal Type | Graphite gasket, compression |
| Weight (empty) | 4.2 kg |

---

## COIL GEOMETRY

| Parameter | Coil 1 | Coil 2 | Coil 3 |
|-----------|--------|--------|--------|
| Frequency | 432 Hz | 699 Hz | 1131 Hz |
| Inductance | 432μH | 699μH | 1131μH |
| Wire Gauge | 12 AWG | 14 AWG | 16 AWG |
| Turns | 120 | 93 | 75 |
| Inner Diameter | 150mm | 150mm | 150mm |
| Height | 45mm | 35mm | 28mm |
| Resistance | 0.8Ω | 1.2Ω | 1.8Ω |
| Max Current | 15A | 12A | 10A |
| Core Material | Zirconia | Zirconia | Zirconia |

```
COIL SPACING (phi-harmonic):
═══════════════════════════════════════════════════════════════

  The three coils are arranged concentrically with
  phi-ratio spacing between them:

  ┌─────────────────────────────────────────┐
  │                                         │
  │           ╭─────────────╮               │
  │         ╭─│─────────────│─╮             │
  │       ╭─│─│─────────────│─│─╮           │
  │       │ │ │             │ │ │           │
  │       │ │ │  COIL 3     │ │ │           │
  │       │ │ │  (1131Hz)   │ │ │           │
  │       │ │ ╰─────────────╯ │ │           │
  │       │ │    COIL 2       │ │           │
  │       │ │    (699Hz)      │ │           │
  │       │ ╰─────────────────╯ │           │
  │       │      COIL 1          │           │
  │       │      (432Hz)         │           │
  │       ╰──────────────────────╯           │
  │                                         │
  │   Spacing: 15mm between coils           │
  │   (φ × 9.27mm ≈ 15mm)                  │
  │                                         │
  └─────────────────────────────────────────┘
```

---

## FEEDSTOCK HOPPER

| Parameter | Value |
|-----------|-------|
| Volume | 500 ml |
| Material | 304 Stainless Steel |
| Opening Diameter | 80mm |
| Wall Thickness | 1.5mm |
| Lid Type | Hinged, gasket-sealed |
| Vibration | 12V vibratory motor, 50Hz |
| Stirrer | Magnetic, 12V DC |
| Max Particle Size | 150μm (100 mesh) |
| Mounting | Top of chassis, removable |

---

## GOLD COLLECTION SYSTEM

| Parameter | Value |
|-----------|-------|
| Collection Tray | 304 SS, 150×100×25mm |
| Separator Mesh | 200 mesh (75μm) |
| Output Funnel | 304 SS, 60° cone |
| Output Valve | 12V solenoid, normally closed |
| Catch Basin | 304 SS, 200ml |
| Discharge Chute | 304 SS, 20mm OD |
| Drain Rate | 50ml/min |

---

## WEIGHT DISTRIBUTION

| Component | Weight | Position |
|-----------|--------|----------|
| FPB-5 Battery | 8.5 kg | Side compartment |
| Transmutation Chamber | 4.2 kg | Center |
| Resonance Coils | 2.8 kg | Around chamber |
| Feedstock System | 1.5 kg | Top |
| Gold Collection | 0.8 kg | Bottom |
| Cooling System | 1.2 kg | Rear |
| Control Electronics | 0.9 kg | Front |
| Chassis & Panels | 4.5 kg | Distributed |
| Wiring & Misc | 0.6 kg | Distributed |
| **Total** | **25 kg** | |

---

## PHI-HARMONIC STRUCTURAL TUNING

```
FRAME RESONANCE:
═══════════════════════════════════════════════════════════════

  Natural frequency: 432 Hz (tuned)
  Damping ratio: φ⁻¹ = 0.618
  Cross-member spacing: 61.8mm (φ × 38.2)

  ┌─────────────────────────────────────────┐
  │  0mm   61.8mm  123.6mm 185.4mm 247.2mm │
  │  ┃      ┃        ┃       ┃       ┃     │
  │  ┃─φ────┃──φ─────┃──φ────┃──φ────┃     │
  │  ┃      ┃        ┃       ┃       ┃     │
  └─────────────────────────────────────────┘

  Result: Frame absorbs transmutation vibrations
  Continuous operation: zero structural fatigue
```

---

## THERMAL MANAGEMENT

| Component | Max Temp | Cooling Method |
|-----------|----------|----------------|
| Chamber exterior | 300°C | Heat exchanger + fan |
| Chamber liner | 1,200°C | Self-insulating zirconia |
| Resonance coils | 85°C | Forced air |
| Control electronics | 45°C | Passive + fan |
| Battery compartment | 35°C | Passive |
| Outer surface | <50°C | Insulation blanket |
