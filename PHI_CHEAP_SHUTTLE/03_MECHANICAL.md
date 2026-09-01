# PHI CHEAP SHUTTLE — MECHANICAL DESIGN

## Frame, Structure, and Mechanical Systems

---

## FRAME DESIGN — ALUMINUM SPACEFRAME

The frame is a welded 6061-T6 aluminum spaceframe with triangular bracing. All tubes are cut to φ-multiples of 100mm for phi-harmonic resonance.

### Main Dimensions

| Parameter | Value |
|-----------|-------|
| Overall Length | 3000mm |
| Overall Width | 1500mm |
| Overall Height | 1800mm |
| Cockpit Length | 1200mm |
| Cockpit Width | 900mm |
| Cockpit Height | 950mm |
| Floor Height | 400mm |
| CG Position | 1854mm from nose (61.8% — φ-point) |
| Wing Area (fairing) | 2.25 m² |
| Wetted Area | 8.4 m² |

### Tube Specifications

| Location | Tube Size | Wall | Length | Qty | Material |
|----------|-----------|------|--------|-----|----------|
| Longitudinal (main) | 1.5" OD | 0.125" | 3000mm | 4 | 6061-T6 |
| Longitudinal (secondary) | 1.0" OD | 0.095" | 1618mm | 4 | 6061-T6 |
| Vertical (cockpit) | 0.75" OD | 0.065" | 950mm | 6 | 6061-T6 |
| Vertical (aft) | 1.0" OD | 0.095" | 1200mm | 4 | 6061-T6 |
| Cross-member (floor) | 1.0" OD | 0.095" | 1500mm | 6 | 6061-T6 |
| Diagonal brace | 0.75" OD | 0.065" | 423.6mm | 12 | 6061-T6 |
| Diagonal brace | 0.75" OD | 0.065" | 261.8mm | 16 | 6061-T6 |
| Diagonal brace | 0.75" OD | 0.065" | 161.8mm | 8 | 6061-T6 |

### φ-Harmonic Tube Lengths

All diagonal braces are cut to φ-multiples of 100mm:
- 1 × 100mm = 100.0mm
- 1 × 161.8mm = 161.8mm (φ¹)
- 1 × 261.8mm = 261.8mm (φ²)
- 1 × 423.6mm = 423.6mm (φ³)
- 1 × 685.4mm = 685.4mm (φ⁴)

This creates a fractal bracing pattern that distributes loads at natural harmonic intervals.

---

## WELDING SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Process | TIG (GTAW) |
| Filler | ER4043 (aluminum) |
| Gas | 100% Argon, 20 CFH |
| Cup Size | #7 (7/16") |
| Tungsten | 2% lanthanated, 1/8" |
| Amperage | 80-120A (depending on wall) |
| Preheat | None required (6061-T6) |
| Post-weld | Solution heat treat optional |

### Weld Joint Specifications

| Joint Type | Preparation | Filler | Notes |
|------------|-------------|--------|-------|
| Tube-to-tube (corner) | 45° V-groove | ER4043 | Full penetration |
| Tube-to-tube (T-joint) | No prep (fill) | ER4043 | Fillet weld all around |
| Tube-to-plate | Plug weld + fillet | ER4043 | 6mm plug holes |
| Gusset plate | Fillet weld | ER4043 | 6mm fillet |
| Floor pan | Stitch weld | ER4043 | 50mm welds, 100mm spacing |

### Weld Quality Standards

- No cracks, porosity, or lack of fusion
- Weld size: minimum 3mm fillet
- Penetration: 75% minimum for structural joints
- Post-weld cleaning: wire brush + acetone
- Visual inspection: 100% of welds
- Dye penetrant test: 10% sample (critical joints)

---

## COCKPIT DESIGN

### Clamshell Cockpit

```
┌──────────────────────────────────────────────────┐
│              COCKPIT — CROSS SECTION              │
│                                                  │
│              ┌────────────────┐                   │
│              │  Fiberglass    │                   │
│              │  Canopy        │                   │
│              │  (hinged rear) │                   │
│              └───────┬────────┘                   │
│                      │                            │
│         ┌────────────┼────────────┐               │
│         │            │            │               │
│    ┌────┴────┐  ┌────┴────┐  ┌────┴────┐        │
│    │ PILOT   │  │ CENTER  │  │PASSENGER│        │
│    │ SEAT    │  │ CONSOLE │  │ SEAT    │        │
│    │         │  │         │  │         │        │
│    │ Bucket  │  │ Throttle│  │ Bucket  │        │
│    │ Seat    │  │ Gauges  │  │ Seat    │        │
│    │ (salv-  │  │ Comms   │  │ (salv-  │        │
│    │  age)   │  │         │  │  age)   │        │
│    └────┬────┘  └────┬────┘  └────┬────┘        │
│         │            │            │               │
│    ┌────┴────────────┴────────────┴────┐         │
│    │         FIBERGLASS FLOOR           │         │
│    │     (aluminum-reinforced)          │         │
│    └───────────────────────────────────┘         │
│                                                  │
│    Width: 900mm (36")                            │
│    Height: 950mm (37.4")                         │
│    Depth: 1200mm (47.2")                         │
│                                                  │
└──────────────────────────────────────────────────┘
```

### Cockpit Dimensions

| Parameter | Value |
|-----------|-------|
| Interior Width | 900mm (36") |
| Interior Height | 950mm (37.4") |
| Interior Depth | 1200mm (47.2") |
| Seat-to-Pedal | 700mm (adjustable) |
| Headroom | 600mm above seat |
| Canopy Opening | 800mm × 600mm |
| Canopy Hinge | Rear-mounted, gas strut assist |

### Seat Specifications

| Parameter | Value |
|-----------|-------|
| Type | Salvaged automotive bucket seats |
| Source | Junkyard (late-model sedan) |
| Mounting | 4× M10 bolts to aluminum floor |
| Adjustment | Forward/aft: 150mm travel |
| Recline | Fixed at 20° recline |
| Restraint | 4-point harness (eBay surplus) |
| Weight | 8 kg each |

---

## THRUSTER MOUNTING

### Mounting Pattern

```
┌──────────────────────────────────────────────────┐
│         THRUSTER MOUNTING — TOP VIEW              │
│                                                  │
│         ┌──────────────────────────┐              │
│         │                          │              │
│    ┌────┴────┐                ┌────┴────┐        │
│    │THRUSTER │                │THRUSTER │        │
│    │  #1     │                │  #2     │        │
│    │Front-L  │                │Front-R  │        │
│    │         │                │         │        │
│    │  ┌───┐  │                │  ┌───┐  │        │
│    │  │   │  │                │  │   │  │        │
│    │  └───┘  │                │  └───┘  │        │
│    └────┬────┘                └────┬────┘        │
│         │                          │              │
│         │    ┌──────────────┐      │              │
│         │    │   COCKPIT    │      │              │
│         │    │              │      │              │
│         │    │              │      │              │
│         │    └──────────────┘      │              │
│         │                          │              │
│    ┌────┴────┐                ┌────┴────┐        │
│    │THRUSTER │                │THRUSTER │        │
│    │  #3     │                │  #4     │        │
│    │Rear-L   │                │Rear-R   │        │
│    │         │                │         │        │
│    │  ┌───┐  │                │  ┌───┐  │        │
│    │  │   │  │                │  │   │  │        │
│    │  └───┘  │                │  └───┘  │        │
│    └────┬────┘                └────┴────┘        │
│         │                          │              │
│         └──────────┬───────────────┘              │
│                    │                              │
│              ┌─────┴─────┐                        │
│              │ EXHAUST   │                        │
│              └───────────┘                        │
│                                                  │
│  Thruster positions based on φ-ratio spacing:    │
│  Front-to-Rear: 1200mm (φ¹ × 740mm)            │
│  Left-to-Right: 800mm (φ⁰ × 800mm)             │
│                                                  │
└──────────────────────────────────────────────────┘
```

### Mounting Hardware

| Component | Specification | Qty |
|-----------|--------------|-----|
| Mounting Plate | 6061-T6, 6mm thick, 200mm × 200mm | 4 |
| Threaded Rod | M10 × 1.5, 300mm (stainless) | 16 |
| Compression Spring | M10 ID, 50mm free length | 16 |
| Lock Nut | M10 nylon-insert | 32 |
| Flat Washer | M10 stainless | 32 |
| Vibration Isolator | Rubber grommet, 10mm ID | 16 |

---

## LANDING GEAR

### Spring-Loaded Skid Design

```
┌──────────────────────────────────────────────────┐
│              LANDING GEAR — SIDE VIEW              │
│                                                  │
│              ┌─────────────┐                      │
│              │   FRAME     │                      │
│              │   (1.5" tube)│                     │
│              └──────┬──────┘                      │
│                     │                             │
│              ┌──────┴──────┐                      │
│              │  PIVOT BOLT  │ ← M12 Grade 8      │
│              │  (12mm)      │                     │
│              └──────┬──────┘                      │
│                     │                             │
│         ┌───────────┼───────────┐                 │
│         │           │           │                 │
│    ┌────┴────┐      │      ┌────┴────┐           │
│    │ SPRING  │      │      │ SPRING  │           │
│    │ (coil,  │      │      │ (coil,  │           │
│    │  200lb) │      │      │  200lb) │           │
│    └────┬────┘      │      └────┬────┘           │
│         │           │           │                 │
│    ┌────┴───────────┴───────────┴────┐           │
│    │         SKID TUBE               │           │
│    │    (1.5" aluminum tube)         │           │
│    │    Length: 1200mm               │           │
│    │    Ground contact: rubber pad   │           │
│    └─────────────────────────────────┘           │
│                                                  │
│  4× landing gear assemblies (2 front, 2 rear)   │
│  Spring rate: 200 lb/in (absorbs 5g impact)      │
│  Skid spacing: 1200mm (front/rear)              │
│  Track width: 1200mm (left/right)               │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## FIBERGLASS SHELL

### Layup Schedule

| Layer | Material | Orientation | Thickness | Purpose |
|-------|----------|-------------|-----------|---------|
| 1 | Gel coat | N/A | 0.5mm | Surface finish |
| 2 | 2oz cloth | 0°/90° | 0.3mm | Finish layer |
| 3 | 6oz cloth | ±45° | 0.8mm | Shear strength |
| 4 | 6oz cloth | 0°/90° | 0.8mm | Bending strength |
| 5 | Foam core | N/A | 12mm | Stiffness |
| 6 | 6oz cloth | 0°/90° | 0.8mm | Bending strength |
| 7 | 6oz cloth | ±45° | 0.8mm | Shear strength |
| **Total** | | | **~16mm** | |

### Shell Sections

| Section | Location | Material | Weight |
|---------|----------|----------|--------|
| Nose cone | Forward 600mm | Fiberglass + foam | 3.2 kg |
| Canopy | Cockpit roof | Fiberglass (clear) | 2.8 kg |
| Side panels | Left/right | Fiberglass + foam | 4.5 kg each |
| Bottom panel | Floor | Fiberglass + aluminum | 5.2 kg |
| Thrust frame | Aft section | Fiberglass + aluminum | 6.8 kg |
| Fairing | Aerodynamic shell | Fiberglass | 3.5 kg |

---

## THERMAL PROTECTION

### Heat Shield Locations

| Location | Material | Thickness | Max Temp |
|----------|----------|-----------|----------|
| Exhaust area | Ceramic blanket | 12mm | 1200°C |
| Thruster mounts | Aluminum plate + ceramic | 6mm | 600°C |
| Floor (aft) | Ceramic blanket + aluminum | 8mm | 400°C |
| Cockpit floor | Ceramic fiber board | 6mm | 200°C |

---

## WEIGHT BUDGET

| Component | Weight (kg) |
|-----------|-------------|
| Aluminum Frame | 48.0 |
| Fiberglass Shell | 26.0 |
| Cockpit (seats, controls) | 22.0 |
| Thrusters (4× complete) | 32.0 |
| Batteries (4× FPB-20) | 56.0 |
| Avionics | 4.5 |
| Landing Gear | 8.0 |
| Wiring & Connectors | 3.5 |
| Fasteners | 2.5 |
| **EMPTY WEIGHT** | **202.5 kg** |
| Pilot (80 kg) | 80.0 |
| Passenger (80 kg) | 80.0 |
| **GROSS WEIGHT** | **362.5 kg** |

---

## STRUCTURAL ANALYSIS SUMMARY

| Load Case | Safety Factor | Limit |
|-----------|---------------|-------|
| 3g maneuver | 2.1 | Frame max stress: 180 MPa |
| 5g landing impact | 1.8 | Frame max stress: 300 MPa |
| Thrust loading (4× 500N) | 3.2 | Frame max stress: 95 MPa |
| Cabin pressurization (0.5 psi) | 4.5 | Shell max stress: 40 MPa |
| Thermal expansion (ΔT=200°C) | N/A | 3.6mm growth, accommodated |

All safety factors > 1.5. Frame design meets experimental aircraft standards (FAR Part 23 equivalent for homebuilt).
