# PHI HEALING DRONE — MECHANICAL DESIGN

## Frame Design and Structural Specifications

---

## FRAME OVERVIEW

The PHI Healing Drone frame is 3D printed from PLA filament. The design uses phi-harmonic proportions for structural efficiency and flight stability. All dimensions follow the golden ratio (phi = 1.618033988749894).

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         400mm
  ←─────────────────────→
  ┌──────────────────────┐  ─┬─
  │                      │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M1║        ║M2║  │   │
  │    ╚══╝        ╚══╝  │   │
  │                      │   │
  │   ┌──────────────┐   │   │
  │   │              │   │   │
  │   │   CENTER     │   │   │ 247mm
  │   │   BODY       │   │   │ (400/phi)
  │   │              │   │   │
  │   │   ┌──────┐   │   │   │
  │   │   │BATT  │   │   │   │
  │   │   └──────┘   │   │   │
  │   │              │   │   │
  │   └──────────────┘   │   │
  │                      │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M3║        ║M4║  │   │
  │    ╚══╝        ╚══╝  │   │
  │                      │   │
  └──────────────────────┘  ─┴─

  Arm Length: 150mm (center to motor)
  Arm Width: 25mm
  Arm Thickness: 8mm
  Center Body: 160mm x 160mm x 40mm
```

---

## PHI-HARMONIC DIMENSIONS

```
GOLDEN RATIO RELATIONSHIPS:
═══════════════════════════════════════════════════════════════

  Overall Width: 400mm
  Overall Height: 247mm (= 400/phi)
  Body Width: 160mm
  Body Height: 99mm (= 160/phi)
  Arm Length: 150mm
  Arm Width: 93mm (= 150/phi)
  Motor Mount: 60mm
  Motor Hole Pattern: 37mm (= 60/phi)

  All dimensions maintain phi-harmonic relationships:
  ┌──────────────────────────────────────────┐
  │  400mm / 247mm = 1.619 ≈ phi            │
  │  160mm / 99mm  = 1.616 ≈ phi            │
  │  150mm / 93mm  = 1.613 ≈ phi            │
  │  60mm / 37mm   = 1.622 ≈ phi            │
  └──────────────────────────────────────────┘
```

---

## ARM DESIGN

```
ARM CROSS-SECTION:
═══════════════════════════════════════════════════════════════

  Top View:
  ┌────────────────────────────────────────┐
  │                                        │
  │  Motor Mount     Arm Shaft    Body     │
  │  ┌──────┐      ┌──────────┐  ┌────┐  │
  │  │ ╔══╗ │      │          │  │    │  │
  │  │ ║M ║ │──────│  150mm   │──│    │  │
  │  │ ╚══╝ │      │          │  │    │  │
  │  └──────┘      └──────────┘  └────┘  │
  │   60mm           25mm wide    Center  │
  │                                        │
  └────────────────────────────────────────┘

  Side View:
  ┌────────────────────────────────────────┐
  │                                        │
  │  ┌──────┐─────────────────────┐       │
  │  │      │                     │       │
  │  │ 8mm  │      8mm thick      │       │
  │  │      │                     │       │
  │  └──────┘─────────────────────┘       │
  │                                        │
  └────────────────────────────────────────┘

  Material: PLA (3D printed)
  Infill: 40% gyroid
  Walls: 4 perimeters
  Top/Bottom: 5 layers
```

---

## MOTOR MOUNT

```
MOTOR MOUNT DETAIL:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────┐
  │                      │
  │      ┌──────┐       │
  │      │  ●   │       │  ● = Motor shaft hole (M5)
  │      │ / \  │       │
  │      │●   ● │       │  ● = Motor mount holes (M3)
  │      │ \ /  │       │      16mm pattern (M2)
  │      │  ●   │       │
  │      └──────┘       │
  │                      │
  │   Motor mount: 60mm │
  │   Hole pattern: 16mm│
  │   Shaft hole: 5mm   │
  │   Thickness: 10mm   │
  │                      │
  └──────────────────────┘

  Motor bolt pattern:
  ┌─────────────────────┐
  │                     │
  │    ●     ●         │
  │     \   /          │
  │      \ /           │
  │       ●            │  16mm between holes
  │      / \           │
  │     /   \          │
  │    ●     ●         │
  │                     │
  └─────────────────────┘

  Use M3 bolts (10mm) with lock washers
  Apply thread locker to prevent vibration loosening
```

---

## CENTER BODY

```
CENTER BODY LAYOUT:
═══════════════════════════════════════════════════════════════

  Top View (lid removed):
  ┌──────────────────────────────────────┐
  │                                      │
  │  ┌──────────┐  ┌──────────┐         │
  │  │          │  │          │         │
  │  │ MEDICAL  │  │FREQUENCY │         │
  │  │ PAYLOAD  │  │GENERATOR │         │
  │  │          │  │          │         │
  │  │ 100x80mm │  │ 80x60mm  │         │
  │  │          │  │          │         │
  │  └──────────┘  └──────────┘         │
  │                                      │
  │  ┌──────────┐  ┌──────────┐         │
  │  │          │  │          │         │
  │  │  FPB-5   │  │ AVIONICS │         │
  │  │ BATTERY  │  │          │         │
  │  │          │  │ Arduino  │         │
  │  │ 120x70mm │  │ Mega     │         │
  │  │          │  │ 80x60mm  │         │
  │  └──────────┘  └──────────┘         │
  │                                      │
  └──────────────────────────────────────┘

  Side View:
  ┌──────────────────────────────────────┐
  │  ┌──────────────────────────────┐   │
  │  │          LID                 │   │
  │  │    (removable, 4 screws)     │   │
  │  ├──────────────────────────────┤   │
  │  │                              │   │
  │  │    INTERNAL COMPARTMENTS     │   │  40mm
  │  │                              │   │
  │  │                              │   │
  │  ├──────────────────────────────┤   │
  │  │          BOTTOM              │   │
  │  └──────────────────────────────┘   │
  └──────────────────────────────────────┘

  Wall thickness: 3mm
  Internal height: 35mm
  External height: 40mm
  Lid: 4x M3 screws
```

---

## BATTERY COMPARTMENT

```
BATTERY MOUNTING:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────┐
  │                                  │
  │  ┌──────────────────────────┐   │
  │  │        FPB-5             │   │
  │  │   12V · 50Ah · 600Wh    │   │
  │  │                          │   │
  │  │   120mm × 70mm × 30mm   │   │
  │  │                          │   │
  │  └──────────────────────────┘   │
  │                                  │
  │  ┌────┐                  ┌────┐ │
  │  │STRAP│                  │STRAP│ │
  │  └────┘                  └────┘ │
  │                                  │
  └──────────────────────────────────┘

  Battery secured with:
  - 2x velcro straps
  - Foam padding (5mm)
  - Anti-vibration mount

  Weight: 850g (battery alone)
  CG adjustment: slide forward/back
```

---

## SENSOR MOUNTING

```
SENSOR LOCATIONS:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────┐
  │                                      │
  │  ┌────┐  MPU6050 (gyro/accel)       │
  │  │IMU │  Center of mass, rigid mount│
  │  └────┘                              │
  │                                      │
  │  ┌────┐  BMP280 (barometer)         │
  │  │BARO│  Bottom, vented to atmosphere│
  │  └────┘                              │
  │                                      │
  │  ┌────┐  NEO-6M (GPS)              │
  │  │ GPS│  Top, clear sky view        │
  │  └────┘  On mast (50mm above body)  │
  │                                      │
  │  ┌────┐  MAX30102 (pulse oximeter)  │
  │  │SpO2│  Bottom, patient contact    │
  │  └────┘                              │
  │                                      │
  │  ┌────┐  DS18B20 (temperature x2)  │
  │  │TEMP│  Patient contact points     │
  │  └────┘                              │
  │                                      │
  │  ┌────┐  AD8232 (ECG)              │
  │  │ ECG│  Patient contact pads       │
  │  └────┘                              │
  │                                      │
  └──────────────────────────────────────┘
```

---

## PROPELLER GUARDS

```
PROP GUARD DESIGN:
═══════════════════════════════════════════════════════════════

  Each motor gets a prop guard ring:

  ┌─────────────────────┐
  │    ┌───────────┐    │
  │   ╱             ╲   │
  │  │    ╔═══╗     │  │
  │  │    ║ M ║     │  │  Guard ring
  │  │    ╚═══╝     │  │  diameter: 350mm
  │   ╲             ╱   │  (prop: 300mm)
  │    └───────────┘    │  clearance: 25mm
  │                     │
  └─────────────────────┘

  Ring thickness: 5mm
  Ring width: 15mm
  Material: PLA (same as frame)
  Weight: 15g per guard
  Total: 60g (4 guards)

  SAFETY: Prop guards protect patient from
  accidental contact with spinning propellers.
```

---

## MATERIAL SPECIFICATIONS

| Component | Material | Dimensions | Weight |
|-----------|----------|------------|--------|
| Frame arms | PLA 3D printed | 4x 150x25x8mm | 85g |
| Center body | PLA 3D printed | 160x160x40mm | 120g |
| Motor mounts | PLA 3D printed | 4x 60x60x10mm | 45g |
| Prop guards | PLA 3D printed | 4x 350mm rings | 60g |
| Lid | PLA 3D printed | 160x160x3mm | 25g |
| Hardware | Steel bolts/nuts | M3 assorted | 35g |
| Dampeners | Rubber | 8x 8mm | 10g |
| **Total Frame** | | | **380g** |

---

## ASSEMBLY SEQUENCE

1. Print all frame parts (12-16 hours print time)
2. Clean and sand all parts
3. Test fit all components
4. Install motor mounts on arms
5. Attach arms to center body
6. Install prop guards
7. Install rubber dampeners
8. Mount battery straps
9. Install sensor mounts
10. Attach GPS mast
11. Final inspection and torque check
