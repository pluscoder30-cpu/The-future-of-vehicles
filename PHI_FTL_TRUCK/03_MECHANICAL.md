# PHI FTL TRUCK — MECHANICAL DESIGN

## Structural Engineering

---

## FRAME GEOMETRY

```
PHI-HARMONIC FRAME RATIOS:
══════════════════════════════════════════════════════════════

  Overall Length:    6200mm (base)
  Overall Width:     2400mm (6200/φ²)
  Overall Height:    2800mm (6200/φ)
  Wheelbase:         3832mm (6200/φ⁰·⁶)
  Front Overhang:    1200mm
  Rear Overhang:     1168mm

  ┌─────────────────────────────────────────────────┐
  │                                                 │
  │  ┌──────┐                    ┌──────────────┐   │
  │  │ CAB  │                    │  CARGO BED   │   │
  │  │2400mm│                    │   4200mm     │   │
  │  │      │                    │              │   │
  │  └──────┘                    └──────────────┘   │
  │                                                 │
  │  ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●    │
  │  Wheelbase: 3832mm                             │
  │                                                 │
  └─────────────────────────────────────────────────┘
```

---

## SUSPENSION SYSTEM

| Parameter | Front | Rear |
|-----------|-------|------|
| Type | Double wishbone | Multi-leaf |
| Spring Rate | 35 N/mm | 85 N/mm |
| Damping | Adjustable | Adjustable |
| Travel | 200mm | 180mm |
| Anti-roll bar | 32mm | 28mm |
| Phi-ratio spacing | φ mm between mounts | φ mm between mounts |

---

## STEERING

| Parameter | Value |
|-----------|-------|
| Type | Power rack-and-pinion |
| Lock-to-lock | 3.2 turns |
| Turning circle | 14.5m |
| Ratio | 16:1 |
| Column | Tilt/telescope |

---

## WHEEL SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Size | 22.5×9.0" |
| Bolt pattern | 10×225mm |
| Offset | 120mm |
| Tire | 295/75R22.5 |
| Load rating | 3550 kg per tire |
| Phi-ratio | Tire height/width = 0.75 ≈ 1/φ |

---

## CARGO BED DIMENSIONS

| Parameter | Value |
|-----------|-------|
| Length | 4200mm |
| Width | 2300mm |
| Height | 1200mm |
| Volume | 11.6 m³ |
| Floor thickness | 4mm steel |
| Wall thickness | 3mm aluminum |
| Tailgate | Hydraulic assist |
| Load capacity | 8000 kg |

---

## WEIGHT DISTRIBUTION

| Component | Weight | Position |
|-----------|--------|----------|
| Frame | 680 kg | Center |
| FPB-80 Battery | 280 kg | Low center |
| Cab | 420 kg | Front |
| Cargo bed | 320 kg | Rear |
| Drivetrain | 380 kg | Front |
| Warp coils | 120 kg | Distributed |
| Suspension | 240 kg | Distributed |
| Wheels/tires | 360 kg | Distributed |
| Electrical | 180 kg | Distributed |
| Interior | 220 kg | Front |
| **Total** | **3,200 kg** | |

---

## PHI-HARMONIC STRUCTURAL TUNING

```
FRAME RESONANCE:
══════════════════════════════════════════════════════════════

  Natural frequency: 432 Hz (tuned)
  Damping ratio: φ⁻¹ = 0.618
  Cross-member spacing: 618mm (φ × 1000)

  ┌─────────────────────────────────────────┐
  │  0mm    618mm   1236mm  1854mm  2472mm  │
  │  ┃       ┃       ┃       ┃       ┃     │
  │  ┃──φ────┃──φ────┃──φ────┃──φ────┃     │
  │  ┃       ┃       ┃       ┃       ┃     │
  └─────────────────────────────────────────┘

  Result: Frame absorbs warp field vibrations
  12c travel: zero structural fatigue
```
