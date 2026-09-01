# PHI FTL CAR — MECHANICAL DESIGN

## Structural Engineering

---

## FRAME GEOMETRY

```
PHI-HARMONIC FRAME RATIOS:
══════════════════════════════════════════════════════════════

  Overall Length:    4800mm (base)
  Overall Width:     1850mm (4800/φ²)
  Overall Height:    1450mm (4800/φ²·⁴)
  Wheelbase:         2968mm (4800/φ⁰·⁵)
  Front Track:       1580mm
  Rear Track:        1560mm

  ┌─────────────────────────────────────────────┐
  │                                             │
  │  ┌─────────────────────────────────────┐   │
  │  │                                     │   │
  │  │  FRONT    CABIN (4)    REAR        │   │
  │  │  ┌───┐  ┌──────────┐  ┌─────┐    │   │
  │  │  │HUD│  │ PASSENGERS│  │TRUNK│    │   │
  │  │  └───┘  └──────────┘  └─────┘    │   │
  │  │                                     │   │
  │  └─────────────────────────────────────┘   │
  │                                             │
  │  ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●    │
  │  Wheelbase: 2968mm                        │
  │                                             │
  └─────────────────────────────────────────────┘
```

---

## SUSPENSION SYSTEM

| Parameter | Front | Rear |
|-----------|-------|------|
| Type | MacPherson strut | Multi-link |
| Spring Rate | 28 N/mm | 32 N/mm |
| Damping | Adjustable | Adjustable |
| Travel | 150mm | 140mm |
| Anti-roll bar | 28mm | 22mm |
| Phi-ratio spacing | φ mm between mounts | φ mm between mounts |

---

## STEERING

| Parameter | Value |
|-----------|-------|
| Type | Electric power rack-and-pinion |
| Lock-to-lock | 2.8 turns |
| Turning circle | 11.2m |
| Ratio | 14:1 |
| Column | Tilt/telescope |

---

## WHEEL SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Size | 19×8.5" |
| Bolt pattern | 5×114.3mm |
| Offset | 38mm |
| Tire | 245/40R19 |
| Load rating | 800 kg per tire |
| Phi-ratio | Tire height/width = 0.40 ≈ 1/φ² |

---

## TRUNK DIMENSIONS

| Parameter | Value |
|-----------|-------|
| Length | 1100mm |
| Width | 1200mm |
| Height | 500mm |
| Volume | 660 liters |
| With seats folded | 1,320 liters |
| Floor height | 650mm |

---

## WEIGHT DISTRIBUTION

| Component | Weight | Position |
|-----------|--------|----------|
| Unibody frame | 380 kg | Center |
| FPB-80 Battery | 252 kg | Low center |
| Cabin/Interior | 280 kg | Center |
| Drivetrain | 220 kg | Front |
| Warp coils | 80 kg | Distributed |
| Suspension | 160 kg | Distributed |
| Wheels/tires | 180 kg | Distributed |
| Electrical | 120 kg | Distributed |
| Body panels | 140 kg | Distributed |
| **Total** | **1,850 kg** | |

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
  10c travel: zero structural fatigue
```
