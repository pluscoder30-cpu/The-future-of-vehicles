# PHI TELEPORT SHUTTLE — MECHANICAL DESIGN

## Frame, Structure, and Mechanical Systems

---

## HULL STRUCTURE

### Overall Dimensions

| Parameter | Value |
|-----------|-------|
| Overall Length | 3,200mm (10.5 ft) |
| Overall Width | 2,100mm (6.9 ft) |
| Overall Height | 1,800mm (5.9 ft) |
| Cabin Length | 1,900mm |
| Cabin Width | 1,500mm |
| Cabin Height | 1,200mm |
| CG Position | 1,978mm from nose (61.8% — φ-point) |
| Wetted Area | 22 m² |

### Hull Cross-Section (Forward View)

```
┌──────────────────────────────────────────────────────┐
│              HULL CROSS-SECTION                       │
│                                                      │
│              ┌──────────────────────┐                 │
│             /                        \                │
│            /      PASSENGER           \               │
│           /       COMPARTMENT         \               │
│          /                              \              │
│         │    ┌────────────────┐     │                 │
│         │    │                │     │                 │
│         │    │   FOLD COIL    │     │                 │
│         │    │     ARRAY      │     │                 │
│         │    │  (12 coils in  │     │                 │
│         │    │  dodecahedral  │     │                 │
│         │    │   config)      │     │                 │
│         │    └────────────────┘     │                 │
│          \                          /                  │
│           \    BATTERY BAY        /                   │
│            \  (4× FPB-100)      /                    │
│             \                  /                     │
│              └──────────────────────┘                 │
│                                                      │
│  Width:  2,100mm                                     │
│  Height: 1,800mm                                     │
│                                                      │
│  Hull Material: CFRP [0/±45/90]₄ quasi-isotropic     │
│  Hull Thickness: 3mm skin, 15mm frame                 │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Material Stack-Up

| Layer | Material | Thickness | Purpose |
|-------|----------|-----------|---------|
| 1 | Ceramic TPS coating | 2mm | Thermal protection |
| 2 | CFRP outer skin | 3mm | Structural shell |
| 3 | CFRP frame | 15mm | Primary structure |
| 4 | Lead lining | 2mm | X-ray shielding |
| 5 | Tungsten foil | 1mm | Gamma shielding |
| 6 | Polyethylene | 20mm | Neutron shielding |
| 7 | CFRP inner skin | 3mm | Cabin wall |
| **Total** | | **~46mm** | |

---

## FOLD-NODE FRAME

### Design

The fold-node frame supports the 12 phi-harmonic coils in a dodecahedral arrangement. Made from Invar 36 (CTE = 1.2 × 10⁻⁶/°C) for thermal stability.

```
FOLD-NODE FRAME — TOP VIEW

              C01
             / | \
           C12  |  C02
           /    |    \
         C11 --+-- C03
          |\  FC  /|
          | C10 C04 |
          |/    |   \|
         C09 --+-- C05
           \    |    /
           C08  |  C06
             \ | /
              C07

  FC = Fold Center (primary fold node location)

  All coils mounted on kinematic mounts (3-point contact)
  Alignment accuracy: ±0.01mm
  Thermal isolation: >10 K/W per mount
  Vibration damping ratio: >0.10
```

### Coil Mounting Detail

```
KINEMATIC MOUNT (per coil):

  ┌─────────────────────────┐
  │    COIL (12 kg)          │
  │                          │
  │  ┌────┐  ┌────┐  ┌────┐ │
  │  │Ball│  │Ball│  │Ball│ │ ← 3-point kinematic mount
  │  │  1 │  │  2 │  │  3 │ │   (constrains 6 DOF)
  │  └──┬─┘  └──┬─┘  └──┬─┘ │
  │     │       │       │    │
  │  ┌──┴───────┴───────┴──┐ │
  │  │   INVAR 36 PLATE    │ │
  │  │   (low CTE)         │ │
  │  └──────────┬──────────┘ │
  │             │            │
  │  ┌──────────┴──────────┐ │
  │  │   STRUCTURAL STRUT  │ │ ← Ti-6Al-4V
  │  │   (to hull frame)   │ │
  │  └─────────────────────┘ │
  └─────────────────────────┘
```

### Structural Struts

| Parameter | Value |
|-----------|-------|
| Material | Ti-6Al-4V |
| Diameter | 12mm OD × 1.5mm wall |
| Length | 500mm (φ × 310mm) |
| Quantity | 8 |
| Max load per strut | 100 kN |
| Fatigue life | >10,000 cycles |
| Thermal isolation | >5 K/W |

---

## COCKPIT DESIGN

### Passenger Compartment Layout

```
┌──────────────────────────────────────────────────────┐
│              COCKPIT — SIDE VIEW                       │
│                                                      │
│  ┌────────────────────────────────────────────────┐  │
│  │                                                │  │
│  │   ┌──────┐         ┌──────┐                    │  │
│  │   │ PILOT│         │CO-   │                    │  │
│  │   │ SEAT │         │PILOT │                    │  │
│  │   │      │  CONSOLE│ SEAT │                    │  │
│  │   │ CF/  │  ┌────┐│      │                    │  │
│  │   │foam  │  │    ││ CF/  │                    │  │
│  │   └──┬───┘  │NAV ││foam  │                    │  │
│  │      │      │DISP│└──┬───┘                    │  │
│  │   ┌──┴──────┴────┴──┴──┐                      │  │
│  │   │   CFRP HONEYCOMB   │                      │  │
│  │   │      FLOOR          │                      │  │
│  │   └────────────────────┘                      │  │
│  │                                                │  │
│  │   Width: 1,500mm  Height: 1,200mm             │  │
│  │   Headroom: 550mm above seat                   │  │
│  │   Window: Polycarbonate 4mm, UV-coated         │  │
│  │                                                │  │
│  └────────────────────────────────────────────────┘  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Seat Specifications

| Parameter | Value |
|-----------|-------|
| Type | Carbon fiber bucket with memory foam |
| Mounting | 4× M5 titanium bolts to floor |
| Adjustment | Forward/aft: 180mm rail travel |
| Recline | 5-position, 10°-30° |
| Restraint | 4-point harness (FIA-rated) |
| Weight | 5 kg each |

---

## FOLD COIL ARRAY MOUNTING

### Dodecahedral Configuration

```
TOP VIEW — COIL POSITIONS

              C01
             / | \
           C12  |  C02
           /    |    \
         C11 --+-- C03
          |\  FC  /|
          | C10 C04 |
          |/    |   \|
         C09 --+-- C05
           \    |    /
           C08  |  C06
             \ | /
              C07

  Coil positions (relative to FC center):
  C01: (0, +350, +180) mm
  C02: (+303, +175, +180) mm
  C03: (+303, -175, +180) mm
  C04: (0, -350, +180) mm
  C05: (-303, -175, +180) mm
  C06: (-303, +175, +180) mm
  C07: (0, +350, -180) mm
  C08: (+303, +175, -180) mm
  C09: (+303, -175, -180) mm
  C10: (0, -350, -180) mm
  C11: (-303, -175, -180) mm
  C12: (-303, +175, -180) mm

  Dodecahedron radius: 350mm
  Coil spacing: φ-harmonic multiples
```

### Individual Coil Specifications

| Parameter | Value |
|-----------|-------|
| Inner diameter | 400mm |
| Outer diameter | 600mm |
| Length | 300mm |
| Turns | 1,618 (≈ 1000 × φ) |
| Wire | YBCO superconductor, 2mm dia |
| Mass | 12 kg |
| Operating temp | 77K (liquid nitrogen) |
| Max current | 5,000 A |
| Inductance | 2.4 mH |

---

## BATTERY BAY

### Layout

```
BATTERY BAY — TOP VIEW

  ┌────────────────────────────────────┐
  │                                    │
  │  ┌──────────┐      ┌──────────┐   │
  │  │ FPB-100  │      │ FPB-100  │   │
  │  │ Unit 1   │      │ Unit 2   │   │
  │  │ 100kWh   │      │ 100kWh   │   │
  │  └──────────┘      └──────────┘   │
  │                                    │
  │         ┌──────────────┐           │
  │         │  COPPER BUS  │           │
  │         │    BAR       │           │
  │         └──────────────┘           │
  │                                    │
  │  ┌──────────┐      ┌──────────┐   │
  │  │ FPB-100  │      │ FPB-100  │   │
  │  │ Unit 3   │      │ Unit 4   │   │
  │  │ 100kWh   │      │ 100kWh   │   │
  │  └──────────┘      └──────────┘   │
  │                                    │
  │  Cooling: Phase-change pads        │
  │  Monitoring: Voltage/current/temp  │
  │  Max temp: 55°C                    │
  └────────────────────────────────────┘
```

---

## LANDING GEAR

### Fixed Tricycle Gear

```
LANDING GEAR — SIDE VIEW

              ┌─────────────┐
              │   FRAME     │
              │  (CFRP)     │
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │  SHOCK      │ ← Coil spring, 250 lb/in
              │  ABSORBER   │   Travel: 80mm
              └──────┬──────┘   Damping: hydraulic
                     │
              ┌──────┴──────┐
              │   STRUT     │ ← Ti-6Al-4V, 20mm OD
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │   WHEEL     │ ← 8" aluminum hub
              │  (8×3.50)   │   4-ply pneumatic tire
              └─────────────┘   No brakes (teleport)


  3× landing gear assemblies:
  - Nose gear: centered, steerable ±15°
  - Main gear: 1,200mm track width
  - All gear: 450mm ground clearance
  - Spring rate: 250 lb/in (absorbs 5g impact)
```

---

## STRUCTURAL ANALYSIS

### Load Cases

| Load Case | Safety Factor | Max Stress | Limit |
|-----------|---------------|------------|-------|
| 3g maneuver | 2.5 | 160 MPa | 400 MPa |
| 5g landing | 2.0 | 280 MPa | 560 MPa |
| Fold transit (4.2g) | 2.8 | 200 MPa | 560 MPa |
| Fold radiation | N/A | 0.161 mSv | 1 mSv |
| Thermal cycling (-40→+60°C) | N/A | 3.2mm growth | Accommodated |
| Impact (10J at hull) | N/A | No penetration | Pass |

All safety factors > 1.5. Design meets experimental aircraft standards.

### Mass Budget

| Component | Mass (kg) | % |
|-----------|-----------|---|
| Hull skin (CFRP) | 180 | 21.4% |
| Hull frame (CFRP) | 95 | 11.3% |
| Space frame (Al 7075) | 85 | 10.1% |
| Fold-node frame (Invar) | 45 | 5.4% |
| Structural struts (Ti) | 30 | 3.6% |
| Fold coils (12×) | 144 | 17.1% |
| Hull coating (ceramic) | 25 | 3.0% |
| Fasteners, brackets | 36 | 4.3% |
| **Structural subtotal** | **640** | **76.2%** |
| Batteries (4×85 kg) | 340 | 40.5% |
| Electronics, wiring | 45 | 5.4% |
| Life support | 35 | 4.2% |
| Seats, interior | 40 | 4.8% |
| Fold cocoon | 25 | 3.0% |
| Communication | 15 | 1.8% |
| **Non-structural subtotal** | **200** | **23.8%** |
| **TOTAL DRY MASS** | **840** | **100%** |
| Pilot (80 kg) | 80 | — |
| Passenger (80 kg) | 80 | — |
| Payload (100 kg) | 100 | — |
| **MAX GROSS MASS** | **1,100** | — |

---

## THERMAL PROTECTION

### Heat Shield Locations

| Location | Material | Thickness | Max Temp |
|----------|----------|-----------|----------|
| Hull exterior | Ceramic TPS tiles | 2mm | 1,200°C |
| Coil bay | MLI (8-layer) | 4mm | Cryogenic |
| Battery bay | Phase-change pad | 8mm | 55°C |
| Electronics bay | Ceramic fiber | 5mm | 180°C |
| Fold cocoon | Lead + CFRP | 5mm | 90°C |

### Cryogenic System

| Component | Specification |
|-----------|--------------|
| Coolant | Liquid nitrogen (LN2) |
| Operating temp | 77K (-196°C) |
| Dewar capacity | 50L |
| Consumption rate | 1.5L/hour (standby), 8L/hour (fold) |
| Insulation | MLI blanket (8 layers) |
| Delivery | Insulated hose, solenoid valve control |
| Boil-off | Vented to atmosphere |

---

## WELDING SPECIFICATIONS (Space Frame)

| Parameter | Value |
|-----------|-------|
| Process | TIG (GTAW) |
| Filler | ER5356 (aluminum, for 7075) |
| Gas | 100% Argon, 22 CFH |
| Tungsten | 2% lanthanated, 1/8" |
| Amperage | 80-130A (25mm tube) |
| Joint type | Tube-to-tube, full penetration |
| Weld size | 3mm fillet minimum |
| Quality | Visual 100%, dye penetrant 10% |

---

## STRUCTURAL LIFE

| Component | Design Life | Inspection Interval |
|-----------|-------------|---------------------|
| Hull skin | 10,000 folds | Every 1,000 folds |
| Hull frame | 10,000 folds | Every 1,000 folds |
| Space frame | 10,000 folds | Every 2,000 folds |
| Fold-node frame | 5,000 folds | Every 500 folds |
| Structural struts | 5,000 folds | Every 500 folds |
| Fold coils | 1,000 folds | Every 100 folds |
| Batteries | 10,000 cycles | Every 1,000 cycles |
