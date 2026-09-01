# PHI FOOD DRONE — OVERVIEW

## PHI-Food-Drone: Portable Phi-Harmonic Food Growing Drone v1.0

**Project Codename:** PHI_FOOD_DRONE
**Version:** 1.0
**Status:** Design Complete — Build Ready
**Total BOM Cost:** $347.89
**Build Time:** 35-55 hours (1-2 builders, 2-3 weeks)
**Skill Level:** Intermediate Maker / Basic Electronics
**Target Cost:** Under $350

---

## WHAT IS THE PHI FOOD DRONE?

The PHI Food Drone is a portable food-growing drone that grows herbs and vegetables in small spaces using phi-harmonic nutrient synthesis frequencies. It can plant seeds, deliver nutrients, monitor plant health, and apply growth-optimizing frequencies to accelerate food production.

The drone measures 450mm × 450mm × 230mm, weighs 2.1 kg, and carries a payload of up to 800g (seeds, nutrients, water). It is powered by a single FPB-5 field plasma battery providing 3.5 hours of continuous operation.

This is NOT a replacement for traditional farming — it is a tool for growing fresh food in urban environments, balconies, rooftops, and small garden plots.

---

## KEY SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Vehicle Type | Quadcopter Food Drone |
| Dimensions | 450mm × 450mm × 230mm |
| Weight | 2.1 kg (with battery) |
| Max Payload | 800g (seeds/nutrients/water) |
| Max Speed | 35 km/h |
| Cruise Speed | 20 km/h |
| Hover Time | 3.5 hours |
| Range | 12 km |
| Battery | FPB-5 Field Plasma Battery (12V, 50Ah) |
| Total Cost | $347.89 |
| Propellers | 4× phi-harmonic balanced (350mm) |
| Motors | 4× brushless (900KV) |
| Seed Bays | 3 types (herbs, vegetables, flowers) |
| Nutrient System | Liquid feed, 300ml tank |
| Frequency Range | 417-639Hz phi-harmonic (528·Φ⁻² to 528·Φ) |
| Sensors | Soil moisture, pH, light, temperature |
| Communication | WiFi + 433MHz telemetry |

---

## ARCHITECTURE DIAGRAM

```
┌──────────────────────────────────────────────────────────────────┐
│                    PHI FOOD DRONE — TOP VIEW                     │
│                                                                  │
│     ┌──────┐                                    ┌──────┐        │
│     │MOTOR │                                    │MOTOR │        │
│     │  1   │                                    │  2   │        │
│     └──┬───┘                                    └──┬───┘        │
│        │    ┌──────────────────────────────┐        │            │
│   ┌────┼────┼──────────────────────────────┼────┼────┐          │
│   │    │    │                              │    │    │          │
│   │    │    │         CENTER BODY          │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────┐┌──────┐┌──────┐  │    │    │          │
│   │    │    │  │HERB  ││VEG   ││FLOWER│  │    │    │          │
│   │    │    │  │SEEDS ││SEEDS ││SEEDS │  │    │    │          │
│   │    │    │  └──────┘└──────┘└──────┘  │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  NUTRIENT TANK       │    │    │    │          │
│   │    │    │  │  300ml liquid feed   │    │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  FREQUENCY GENERATOR │    │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  FPB-5 BATTERY       │    │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    └──────────────────────────────┘    │    │          │
│   └────┼───────────────────────────────────────┼────┘          │
│   ┌────┴───┐                              ┌────┴───┐           │
│   │MOTOR 3 │                              │MOTOR 4 │           │
│   └────────┘                              └────────┘           │
│                                                                  │
│   Cost: $348   Weight: 2.1 kg   Payload: 800g                 │
│   Flight Time: 3.5 hours   Range: 12 km                        │
└──────────────────────────────────────────────────────────────────┘
```

---

## PHI-HARMONIC DESIGN PRINCIPLES

- **Body dimensions:** 450mm / 278mm = 1.618 = phi
- **Seed bay ratios:** Herb/Veg = φ, Veg/Flower = φ
- **Frequency sequence:** 417Hz (528·Φ⁻²), 528Hz, 639Hz (phi-ladder)
- **Nutrient tank:** Height/Diameter = φ
- **Motor spacing:** Diagonal/Arm = φ
- **Sensor placement:** At φ-angles from center

---

## COST BREAKDOWN

| Category | Cost | % |
|----------|------|---|
| Frame (3D printed) | $30.00 | 8.6% |
| Motors and propellers | $82.00 | 23.6% |
| FPB-5 Battery | $85.00 | 24.5% |
| Seed System | $22.00 | 6.3% |
| Nutrient System | $20.00 | 5.8% |
| Frequency Generator | $15.00 | 4.3% |
| Avionics | $48.89 | 14.1% |
| pH Sensor | $15.00 | 4.3% |
| Miscellaneous | $30.00 | 8.6% |
| **SUBTOTAL** | **$347.89** | **100%** |

---

## SAFETY RATING

**Urban Farming Tool — Outdoor Use Only**

- Not for commercial food production
- Use only edible-grade nutrients
- Check local drone regulations
- Do not fly over people
- Keep away from electrical lines

---

## PROJECT FILES

| File | Description |
|------|-------------|
| 00_OVERVIEW.md | This file |
| 01_PARTS_LIST.md | Complete parts list |
| 02_WIRING.md | Electrical wiring diagrams |
| 03_MECHANICAL.md | Frame design |
| 04_CIRCUIT.md | Circuit schematics |
| 05_ASSEMBLY.md | Assembly instructions |
| 06_SAFETY.md | Safety guidelines |
| 07_PERFORMANCE.md | Performance data |
| 08_PHI_PHYSICS.md | Phi-harmonic food growth theory |
| 09_GROWING_PROTOCOLS.md | Food growing guidelines |
| 10_COMPLETE_BOM.md | Full bill of materials |
| 11_PHI_HARMONIC_SPECS.md | Phi tuning parameters |
| 12_POWER_SYSTEM.md | Battery and power distribution |
| 13_CONTROL_SYSTEM.md | Avionics and autonomy |
| README.md | Quick start guide |
| MANUAL.md | Kid-friendly operations manual |

---

## DISCLAIMER

The PHI Food Drone is an experimental urban farming tool. It is NOT a substitute for proper soil preparation, watering, and fertilization. Growth frequency effects are based on preliminary studies. Build and operate at your own risk.
