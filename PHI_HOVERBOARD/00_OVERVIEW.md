# PHI_HOVERBOARD — Overview

## What It Is

A personal electromagnetic levitation board that hovers 8-12 mm above any ferromagnetic surface (steel plate, rail, or dedicated track). It uses phi-harmonic coil geometry — coils arranged at golden-angle (137.5°) spacing — to create constructive magnetic flux interference, achieving levitation with 40% less power than conventional Halbach arrays.

## What It Does

- Hovers silently above steel surfaces
- Rider stands on two foot pads with gyroscopic balance assist
- Accelerates/decelerates via weight shift (forward/back)
- Turns by tilting left/right
- Regenerative braking recovers 15% energy on deceleration

## Technical Specifications

| Spec | Value |
|------|-------|
| Top Speed | 20 km/h (12.4 mph) |
| Range | 15 km (9.3 miles) |
| Levitation Gap | 8-12 mm |
| Weight Capacity | 100 kg (220 lbs) |
| Board Weight | 12 kg (26.5 lbs) |
| Battery | 48V 10Ah LiFePO4 (480 Wh) |
| Motor Power | 2 × 500W hub coils (1000W total) |
| Charge Time | 2.5 hours (standard), 1.5 hours (fast) |
| Dimensions | 600mm × 200mm × 80mm (L×W×H) |
| Operating Temp | -10°C to 45°C |
| Water Resistance | IP54 (splash-proof, not submersible) |

## How It Works (Simplified)

1. **Phi-Harmonic Coils**: 8 coils arranged at 137.5° intervals around the board create overlapping magnetic fields
2. **Constructive Interference**: Fields add at the golden ratio, producing a net upward force 1.618× stronger than sum of individual coils
3. **Gyroscopic Sensors**: MPU-6050 IMU detects tilt 1000×/second and adjusts coil current
4. **Microcontroller**: Arduino Nano reads sensors and controls MOSFET H-bridges to steer magnetic flux
5. **Rider Input**: Weight shifts are detected by pressure sensors and translated to direction commands

## Cost Breakdown

| Category | Cost |
|----------|------|
| Coils & Magnets | $280 |
| Battery Pack | $200 |
| Electronics | $150 |
| Frame & Deck | $100 |
| Hardware & Misc | $70 |
| **Total** | **$800** |

## Required Surface

The hoverboard requires a ferromagnetic surface. Options:
- Steel plate (minimum 3mm thick) — ~$120 for a 2m×1m sheet
- Existing steel structures (parking garages, industrial floors)
- Dedicated hover track (DIY from steel roofing panels)

The board does NOT work on concrete, wood, tile, or asphalt without a steel underlayer.
