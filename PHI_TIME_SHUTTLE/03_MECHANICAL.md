# PHI TIME SHUTTLE — MECHANICAL DESIGN

## Frame, Structure, and Mechanical Systems

---

## HULL STRUCTURE

### Overall Dimensions

| Parameter | Value |
|-----------|-------|
| Overall Length | 3,800mm (12.5 ft) |
| Overall Width | 2,600mm (8.5 ft) |
| Overall Height | 2,000mm (6.6 ft) |
| Cabin Length | 2,200mm |
| Cabin Width | 1,800mm |
| Cabin Height | 1,400mm |
| CG Position | 2,348mm from nose (61.8% — φ-point) |
| Wetted Area | 28 m² |

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
│         │    ┌────────────────────┐     │             │
│         │    │                    │     │             │
│         │    │   TEMPORAL COIL    │     │             │
│         │    │      ARRAY         │     │             │
│         │    │   (8 coils in      │     │             │
│         │    │    bi-toroidal     │     │             │
│         │    │    config)         │     │             │
│         │    └────────────────────┘     │             │
│          \                              /              │
│           \    BATTERY BAY            /               │
│            \   (4× FPB-100)         /                │
│             \                      /                 │
│              └──────────────────────┘                 │
│                                                      │
│  Width:  2,600mm                                     │
│  Height: 2,000mm                                     │
│                                                      │
│  Hull Material: CFRP [0/±45/90]₅ quasi-isotropic     │
│  Hull Thickness: 4mm skin, 18mm frame                 │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Material Stack-Up

| Layer | Material | Thickness | Purpose |
|-------|----------|-----------|---------|
| 1 | Ceramic TPS coating | 2mm | Thermal protection |
| 2 | CFRP outer skin | 4mm | Structural shell |
| 3 | CFRP frame | 18mm | Primary structure |
| 4 | Lead lining | 2.5mm | X-ray shielding |
| 5 | Tungsten foil | 1.5mm | Gamma shielding |
| 6 | Polyethylene | 25mm | Neutron shielding |
| 7 | CFRP inner skin | 4mm | Cabin wall |
| **Total** | | **~57mm** | |

---

## TEMPORAL FRAME

### Design

The temporal frame supports the 8 phi-harmonic coils in a bi-toroidal arrangement. Made from Invar 36 (CTE = 1.2 × 10⁻⁶/°C) for thermal stability.

```
TEMPORAL FRAME — TOP VIEW

              C01    C02
             / | \  / | \
           C08  | C03  |  C03
           /    |/   \|    \
         C07 ---+-- TC --+--- C03
           \    |\   /|    /
           C06  | C04  |  C04
             \ | /  \ | /
              C05    C04

  TC = Temporal Center (fold node location)

  All coils mounted on kinematic mounts (3-point contact)
  Alignment accuracy: ±0.008mm
  Thermal isolation: >12 K/W per mount
  Vibration damping ratio: >0.12
```

### Coil Mounting Detail

```
KINEMATIC MOUNT (per coil):

  ┌─────────────────────────┐
  │    COIL (22 kg)          │
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
| Diameter | 15mm OD × 1.5mm wall |
| Length | 618mm (φ × 382mm) |
| Quantity | 10 |
| Max load per strut | 50 kN |
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
│  │   Width: 1,800mm  Height: 1,400mm             │  │
│  │   Headroom: 650mm above seat                   │  │
│  │   Window: Polycarbonate 5mm, UV-coated         │  │
│  │                                                │  │
│  └────────────────────────────────────────────────┘  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Seat Specifications

| Parameter | Value |
|-----------|-------|
| Type | Carbon fiber bucket with memory foam |
| Mounting | 4× M6 titanium bolts to floor |
| Adjustment | Forward/aft: 200mm rail travel |
| Recline | 5-position, 10°-30° |
| Restraint | 4-point harness (FIA-rated) |
| Weight | 6 kg each |

---

## TEMPORAL COIL ARRAY MOUNTING

### Bi-Toroidal Configuration

```
SIDE VIEW — COIL POSITIONS

          C01    C02
         / | \  / | \
       C08  | C03  |  C03
       /    |/   \|    \
     C07 ---+-- TC --+--- C03
       \    |\   /|    /
       C06  | C04  |  C04
         \ | /  \ | /
          C05    C04

  Coil positions (relative to TC center):
  C01: (0, +450, +200) mm
  C02: (+450, 0, +200) mm
  C03: (0, -450, +200) mm
  C04: (-450, 0, +200) mm
  C05: (0, +450, -200) mm
  C06: (+450, 0, -200) mm
  C07: (0, -450, -200) mm
  C08: (-450, 0, -200) mm

  Torus major radius: 450mm
  Torus minor radius: 200mm
  Coil spacing: φ-harmonic multiples
```

### Individual Coil Specifications

| Parameter | Value |
|-----------|-------|
| Inner diameter | 600mm |
| Outer diameter | 900mm |
| Length | 400mm |
| Turns | 1,618 (≈ 1000 × φ) |
| Wire | YBCO superconductor, 2mm dia |
| Mass | 22 kg |
| Operating temp | 77K (liquid nitrogen) |
| Max current | 6,000 A |
| Inductance | 3.6 mH |

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
              │  SHOCK      │ ← Coil spring, 300 lb/in
              │  ABSORBER   │   Travel: 100mm
              └──────┬──────┘   Damping: hydraulic
                     │
              ┌──────┴──────┐
              │   STRUT     │ ← Ti-6Al-4V, 25mm OD
              └──────┬──────┘
                     │
              ┌──────┴──────┐
              │   WHEEL     │ ← 10" aluminum hub
              │  (10×4.00)  │   4-ply pneumatic tire
              └─────────────┘   No brakes (fold-teleport)


  3× landing gear assemblies:
  - Nose gear: centered, steerable ±15°
  - Main gear: 1,400mm track width
  - All gear: 500mm ground clearance
  - Spring rate: 300 lb/in (absorbs 5g impact)
```

---

## STRUCTURAL ANALYSIS

### Load Cases

| Load Case | Safety Factor | Max Stress | Limit |
|-----------|---------------|------------|-------|
| 3g maneuver | 2.5 | 180 MPa | 450 MPa |
| 5g landing | 2.0 | 300 MPa | 600 MPa |
| Temporal fold (1.2g) | 3.8 | 160 MPa | 600 MPa |
| Temporal fold radiation | N/A | 0.0755 mSv | 1 mSv |
| Thermal cycling (-40→+60°C) | N/A | 3.6mm growth | Accommodated |
| Impact (15J at hull) | N/A | No penetration | Pass |

All safety factors > 1.5. Design meets experimental aircraft standards.

### Mass Budget

| Component | Mass (kg) | % |
|-----------|-----------|---|
| Hull skin (CFRP) | 220 | 21.0% |
| Hull frame (CFRP) | 110 | 10.5% |
| Space frame (Al 7075) | 100 | 9.5% |
| Temporal frame (Invar) | 55 | 5.2% |
| Structural struts (Ti) | 38 | 3.6% |
| Temporal coils (8×) | 176 | 16.8% |
| Hull coating (ceramic) | 30 | 2.9% |
| Fasteners, brackets | 41 | 3.9% |
| **Structural subtotal** | **770** | **73.3%** |
| Batteries (4×85 kg) | 340 | 32.4% |
| Electronics, wiring | 55 | 5.2% |
| Life support | 40 | 3.8% |
| Seats, interior | 50 | 4.8% |
| Temporal cocoon | 30 | 2.9% |
| Communication | 18 | 1.7% |
| **Non-structural subtotal** | **280** | **26.7%** |
| **TOTAL DRY MASS** | **1,050** | **100%** |
| Pilot (80 kg) | 80 | — |
| Passenger (80 kg) | 80 | — |
| Payload (200 kg) | 200 | — |
| **MAX GROSS MASS** | **1,410** | — |

---

## THERMAL PROTECTION

### Heat Shield Locations

| Location | Material | Thickness | Max Temp |
|----------|----------|-----------|----------|
| Hull exterior | Ceramic TPS tiles | 2mm | 1,200°C |
| Coil bay | MLI (10-layer) | 5mm | Cryogenic |
| Battery bay | Phase-change pad | 10mm | 55°C |
| Electronics bay | Ceramic fiber | 6mm | 200°C |
| Temporal cocoon | Lead + CFRP | 6mm | 100°C |

### Cryogenic System

| Component | Specification |
|-----------|--------------|
| Coolant | Liquid nitrogen (LN2) |
| Operating temp | 77K (-196°C) |
| Dewar capacity | 50L |
| Consumption rate | 2L/hour (standby), 10L/hour (fold) |
| Insulation | MLI blanket (10 layers) |
| Delivery | Insulated hose, solenoid valve control |
| Boil-off | Vented to atmosphere |

---

## WELDING SPECIFICATIONS (Space Frame)

| Parameter | Value |
|-----------|-------|
| Process | TIG (GTAW) |
| Filler | ER5356 (aluminum, for 7075) |
| Gas | 100% Argon, 25 CFH |
| Tungsten | 2% lanthanated, 3/32" |
| Amperage | 90-140A (28mm tube) |
| Joint type | Tube-to-tube, full penetration |
| Weld size | 4mm fillet minimum |
| Quality | Visual 100%, dye penetrant 10% |

---

## STRUCTURAL LIFE

| Component | Design Life | Inspection Interval |
|-----------|-------------|---------------------|
| Hull skin | 5,000 folds | Every 500 folds |
| Hull frame | 5,000 folds | Every 500 folds |
| Space frame | 5,000 folds | Every 1,000 folds |
| Temporal frame | 2,500 folds | Every 250 folds |
| Structural struts | 2,500 folds | Every 250 folds |
| Temporal coils | 500 folds | Every 50 folds |
| Batteries | 10,000 cycles | Every 1,000 cycles |
