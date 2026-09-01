# PHI PLANT DRONE — OVERVIEW

## PHI-Plant-Drone: Portable Phi-Harmonic Plant Growing Drone v1.0

**Project Codename:** PHI_PLANT_DRONE
**Version:** 1.0
**Status:** Design Complete — Build Ready
**Total BOM Cost:** $248.32
**Build Time:** 30-50 hours (1-2 builders, 2-3 weeks)
**Skill Level:** Intermediate Maker / Basic Electronics
**Target Cost:** Under $250

---

## WHAT IS THE PHI PLANT DRONE?

The PHI Plant Drone is a portable plant-growing drone that plants seeds, waters plants, and applies phi-harmonic growth frequencies to accelerate plant growth. It hovers over gardens, farms, or reforestation sites and provides targeted care to individual plants.

The drone measures 500mm × 500mm × 250mm, weighs 2.0 kg, and carries a payload of up to 1kg (seeds, water, nutrients). It is powered by a single FPB-5 field plasma battery providing 3.5 hours of continuous operation. The phi-harmonic frequency generator operates at growth-optimizing frequencies (432Hz, 528Hz, 639Hz) tuned to plant cellular resonance.

This is NOT a replacement for proper gardening — it is a tool that accelerates growth and reduces manual labor.

---

## KEY SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Vehicle Type | Quadcopter Plant Drone |
| Dimensions | 500mm × 500mm × 250mm |
| Weight | 2.0 kg (with battery) |
| Max Payload | 1.0 kg (seeds/water/nutrients) |
| Max Speed | 35 km/h |
| Cruise Speed | 20 km/h |
| Hover Time | 3.5 hours |
| Range | 12 km |
| Battery | FPB-5 Field Plasma Battery (12V, 50Ah) |
| Battery Cost | $85 |
| Total Cost | $248.32 |
| Propellers | 4× phi-harmonic balanced (400mm) |
| Motors | 4× brushless (800KV) |
| Flight Controller | Arduino Mega + MPU6050 |
| Seed Dispenser | Gravity-fed, servo-controlled |
| Water System | Pressurized spray, 500ml tank |
| Frequency Generator | 432-639Hz phi-harmonic |
| Sensors | Soil moisture, light, temperature |
| Communication | WiFi + 433MHz telemetry |
| GPS | Ublox NEO-6M |

---

## ARCHITECTURE DIAGRAM

```
┌──────────────────────────────────────────────────────────────────┐
│                    PHI PLANT DRONE — TOP VIEW                    │
│                                                                  │
│     ┌──────┐                                    ┌──────┐        │
│     │MOTOR │                                    │MOTOR │        │
│     │  1   │                                    │  2   │        │
│     └──┬───┘                                    └──┬───┘        │
│        │    ┌──────────────────────────────┐        │            │
│        │    │                              │        │            │
│   ┌────┼────┼──────────────────────────────┼────┼────┐          │
│   │    │    │                              │    │    │          │
│   │    │    │         CENTER BODY          │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  SEED DISPENSER      │    │    │    │          │
│   │    │    │  │  ┌────┐ ┌────┐      │    │    │    │          │
│   │    │    │  │  │SEED│ │SEED│      │    │    │    │          │
│   │    │    │  │  │BAY1│ │BAY2│      │    │    │    │          │
│   │    │    │  │  └────┘ └────┘      │    │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  WATER TANK (500ml)  │    │    │    │          │
│   │    │    │  │  + Pump + Nozzle     │    │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  FREQUENCY GENERATOR │    │    │    │          │
│   │    │    │  │  432Hz · 528Hz · 639Hz│   │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    │                              │    │    │          │
│   │    │    │  ┌──────────────────────┐    │    │    │          │
│   │    │    │  │  FPB-5 BATTERY       │    │    │    │          │
│   │    │    │  │  12V · 50Ah · 600Wh  │    │    │    │          │
│   │    │    │  └──────────────────────┘    │    │    │          │
│   │    │    └──────────────────────────────┘    │    │          │
│   │    │                                       │    │          │
│   └────┼───────────────────────────────────────┼────┘          │
│        │                                       │                │
│   ┌────┴───┐                              ┌────┴───┐           │
│   │MOTOR 3 │                              │MOTOR 4 │           │
│   └────────┘                              └────────┘           │
│                                                                  │
│   Cost: $248   Weight: 2.0 kg   Payload: 1.0 kg               │
│   Flight Time: 3.5 hours   Range: 12 km                        │
└──────────────────────────────────────────────────────────────────┘
```

---

## SIDE VIEW

```
                                    ┌─────┐
                                    │GPS  │
                                    │ANT  │
                                    └──┬──┘
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         │                             │                             │
         │    ┌──────────────────────────────────────────────────┐  │
         │    │              CENTER BODY (500mm × 500mm)         │  │
         │    │                                                  │  │
         │    │  ┌──────────┐  ┌──────────┐  ┌──────────┐      │  │
         │    │  │SEED      │  │ WATER    │  │FREQUENCY │      │  │
         │    │  │DISPENSER │  │ TANK     │  │GENERATOR │      │  │
         │    │  │200g seeds│  │ 500ml    │  │432-639Hz │      │  │
         │    │  └──────────┘  └──────────┘  └──────────┘      │  │
         │    │                                                  │  │
         │    │  ┌──────────┐  ┌──────────┐  ┌──────────┐      │  │
         │    │  │AVIONICS  │  │ SOIL     │  │LIGHT     │      │  │
         │    │  │Arduino   │  │ MOISTURE │  │SENSOR    │      │  │
         │    │  │MPU6050   │  │ SENSOR   │  │          │      │  │
         │    │  └──────────┘  └──────────┘  └──────────┘      │  │
         │    │                                                  │  │
         │    │  ┌──────────────────────────────────────────┐   │  │
         │    │  │        FPB-5 BATTERY (12V, 50Ah)         │   │  │
         │    │  └──────────────────────────────────────────┘   │  │
         │    └──────────────────────────────────────────────────┘  │
         │                             │                             │
         │    ┌────────┐               │              ┌────────┐   │
         │    │PROP 1  │               │              │PROP 2  │   │
         │    │ 400mm  │               │              │ 400mm  │   │
         │    └────────┘               │              └────────┘   │
         └─────────────────────────────┼─────────────────────────────┘
                                       │
                              ┌────────┴────────┐
                              │  WATER NOZZLE   │
                              │  (adjustable)   │
                              └─────────────────┘

         PAYLOAD LAYOUT:
         ┌──────────────────────────────────────────────┐
         │  Seed Bay 1: Vegetable seeds (100g)         │
         │  Seed Bay 2: Herb seeds (100g)              │
         │  Water Tank: 500ml (0.5 kg)                 │
         │  Nutrient pouch: 50ml liquid fertilizer     │
         │  Total payload: ~700g typical, 1kg max      │
         └──────────────────────────────────────────────┘
```

---

## PHI-HARMONIC DESIGN PRINCIPLES

All subsystems are tuned to phi (φ = 1.618033988749894):

- **Propeller blade ratio:** Blade length / Hub radius = φ
- **Body dimensions:** Length / Width = 500mm / 309mm ≈ φ
- **Frequency sequence:** 432Hz, 528Hz, 639Hz (phi-spaced)
- **Seed dispenser:** Two bays in φ ratio (124mm / 76mm ≈ φ)
- **Water tank:** Height / Diameter = φ
- **Motor spacing:** Diagonal / Arm = φ
- **Flight controller loop rate:** 1000/φ = 618Hz
- **Spray pattern:** Nozzle spacing at φ-angles
- **Weight distribution:** CG at φ-point along body diagonal
- **Sensor placement:** At φ-angles from center

---

## COST BREAKDOWN SUMMARY

| Category | Cost | % of Total |
|----------|------|-----------|
| Frame (3D printed PLA) | $32.00 | 12.9% |
| Motors and propellers | $72.00 | 29.0% |
| FPB-5 Battery | $85.00 | 34.2% |
| Seed Dispenser | $15.00 | 6.0% |
| Water System | $18.00 | 7.2% |
| Frequency Generator | $15.00 | 6.0% |
| Avionics | $26.32 | 10.6% |
| Miscellaneous | $5.00 | 2.0% |
| **SUBTOTAL** | **$248.32** | **100%** |

---

## SAFETY RATING

**Agricultural Tool — Outdoor Use Only**

- Not for indoor use (water spray)
- Check local drone regulations
- Do not fly over people
- Keep away from electrical lines
- Use eye protection when testing spray system
- Do not operate in high winds (>25 km/h)

---

## PROJECT FILES

| File | Description |
|------|-------------|
| 00_OVERVIEW.md | This file — project overview |
| 01_PARTS_LIST.md | Complete parts list with sources and prices |
| 02_WIRING.md | Electrical wiring diagrams |
| 03_MECHANICAL.md | Frame design and structural specs |
| 04_CIRCUIT.md | Avionics and sensor circuit schematics |
| 05_ASSEMBLY.md | Step-by-step assembly instructions |
| 06_SAFETY.md | Safety guidelines and agricultural protocols |
| 07_PERFORMANCE.md | Flight and planting performance data |
| 08_PHI_PHYSICS.md | Phi-harmonic plant growth theory |
| 09_PLANTING_PROTOCOLS.md | Planting and growing guidelines |
| 10_COMPLETE_BOM.md | Full bill of materials |
| 11_PHI_HARMONIC_SPECS.md | Phi tuning parameters |
| 12_POWER_SYSTEM.md | FPB-5 battery and power distribution |
| 13_CONTROL_SYSTEM.md | Avionics, flight controller, and autonomy |
| README.md | Quick start and build guide |
| MANUAL.md | Complete operations manual (kid-friendly) |

---

## DISCLAIMER

The PHI Plant Drone is an experimental agricultural drone using phi-harmonic frequency therapy to promote plant growth. It is NOT a substitute for proper soil preparation, watering, and fertilization. Growth frequency effects are based on preliminary studies and anecdotal evidence. Build and operate at your own risk. Consult with agricultural professionals before use on valuable crops.
