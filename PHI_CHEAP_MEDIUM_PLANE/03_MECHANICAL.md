# PHI_CHEAP_MEDIUM_PLANE — Mechanical Design

## 1. FUSELAGE STRUCTURE

### 1.1 Frame Type
- **Construction**: Semi-monocoque aluminum tube frame
- **Primary material**: 6061-T6 aluminum alloy
- **Fasteners**: AD41623 pop rivets + AN bolts
- **Skin**: 0.032"–0.063" aluminum sheet

### 1.2 Fuselage Dimensions
```
                    ┌─────────────────────────────────────┐
                    │         TOP VIEW                     │
                    │                                      │
    ┌──────────────────────────────────────────────────────┐
    │  ◄──── 8000mm (26.25 ft) ────►                      │
    │                                                      │
    │  ┌──┐  ┌──────────────────────────────────┐  ┌──┐   │
    │  │  │  │                                  │  │  │   │
    │  │N │  │         CABIN                    │  │T │   │
    │  │O │  │      1400mm W × 1800mm L         │  │A │   │
    │  │S │  │                                  │  │I │   │
    │  │E │  │    ┌────┐          ┌────┐        │  │L │   │
    │  │  │  │    │SEAT│          │SEAT│        │  │  │   │
    │  │  │  │    │ 1  │          │ 2  │        │  │  │   │
    │  │  │  │    └────┘          └────┘        │  │  │   │
    │  │  │  │                                  │  │  │   │
    │  │  │  │    ┌────┐          ┌────┐        │  │  │   │
    │  │  │  │    │SEAT│          │SEAT│        │  │  │   │
    │  │  │  │    │ 3  │          │ 4  │        │  │  │   │
    │  │  │  │    └────┘          └────┘        │  │  │   │
    │  │  │  │                                  │  │  │   │
    │  │  │  └──────────────────────────────────┘  │  │   │
    │  └──┘                                        └──┘   │
    └──────────────────────────────────────────────────────┘
```

### 1.3 Cross-Section
```
    ┌─────────────────────────────────────┐
    │         SIDE VIEW                    │
    │                                      │
    │   ◄── 8000mm ──►                    │
    │                                      │
    │  ┌─┐                              ┌─┐│
    │  │ │    ┌──────────────────────┐   │ ││
    │  │N│    │     CABIN            │   │T││
    │  │O│    │  1200mm H × 1400mm W │   │A││
    │  │S│    │                      │   │I││
    │  │E│    │   CEILING: 1100mm    │   │L││
    │  │ │    │   FLOOR: 100mm       │   │ ││
    │  └─┘    └──────────────────────┘   └─┘│
    │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
    │           LANDING GEAR                 │
    └─────────────────────────────────────┘

    Height at tail: 2800mm from ground
    Height at nose: 2400mm from ground
    Cabin height: 1200mm (seated)
```

### 1.4 Station Lines
| Station | Location | Frame Type |
|---|---|---|
| Station 0 | Nose tip | — |
| Station 1 | Firewall | 0.090" Al plate, 500×600mm |
| Station 2 | Forward bulkhead | 0.063" Al ring |
| Station 3 | Forward seat rail | 1×1×1/8" sq tube |
| Station 4 | Center bulkhead | 0.063" Al ring |
| Station 5 | Aft seat rail | 1×1×1/8" sq tube |
| Station 6 | Aft bulkhead | 0.063" Al ring |
| Station 7 | Tail cone start | 1×1×1/8" sq tube taper |
| Station 8 | Tail wheel | — |

---

## 2. WING DESIGN

### 2.1 Wing Profile
- **Airfoil**: NACA 2412
- **Aspect Ratio**: 14000/1400 = 10:1
- **Wing Area**: 14 m² (150.7 ft²)
- **Wing Loading**: 800 kg / 14 m² = 57.1 kg/m² (11.7 lb/ft²)

### 2.2 Wing Structure
```
    ┌───────────────────────────────────────────────────┐
    │            WING CROSS-SECTION (NACA 2412)          │
    │                                                    │
    │    ◄──── 1400mm chord ────►                        │
    │                                                    │
    │         ┌─────────────────────────┐                │
    │    ┌────┤                         ├────┐          │
    │   ╱     │    LEADING EDGE         │     ╲         │
    │  ╱      │                         │      ╲        │
    │ ╱       │    ┌───┐     ┌───┐     │       ╲       │
    │╱        │    │SPAR│     │SPAR│     │        ╲      │
    │         │    │ 1  │     │ 2  │     │         │     │
    │╲        │    └───┘     └───┘     │        ╱      │
    │ ╲       │                         │       ╱       │
    │  ╲      │    TRAILING EDGE        │      ╱        │
    │   ╲────┤                         ├────╱          │
    │         └─────────────────────────┘                │
    │                                                    │
    │    Spar 1: 1.5"×1"×1/8" Al channel (main)         │
    │    Spar 2: 1"×1"×1/8" Al sq tube (rear)           │
    │    Ribs: 0.040" Al, NACA 2412 profile             │
    │    Skin: 0.032" Al sheet                           │
    │    Leading edge: 0.040" Al sheet, rolled           │
    │    Trailing edge: 0.032" Al sheet                  │
    └───────────────────────────────────────────────────┘
```

### 2.3 Wing Dimensions
| Parameter | Value |
|---|---|
| Span | 14000 mm (45.93 ft) |
| Chord (root) | 1400 mm |
| Chord (tip) | 1050 mm |
| Taper ratio | 0.75 |
| Washout | 3° (root to tip) |
| Dihedral | 2° |
| Incidence | 3° |
| Sweep (quarter-chord) | 0° (straight) |
| Number of ribs | 28 (14 per side) |
| Rib spacing | 500 mm |
| Spar stations | 25% and 75% chord |

### 2.4 Wing Attachment
```
    ┌─────────────────────────────────────┐
    │         WING ROOT FITTING            │
    │                                      │
    │  ┌────────────────────────────────┐  │
    │  │      WING ROOT                  │  │
    │  │   ┌──────────────────────┐     │  │
    │  │   │   MAIN SPAR          │     │  │
    │  │   │   1.5"×1"×1/8"      │     │  │
    │  │   │                      │     │  │
    │  │   │   ┌──┐    ┌──┐     │     │  │
    │  │   │   │B1│    │B2│     │     │  │
    │  │   │   └──┘    └──┘     │     │  │
    │  │   │                      │     │  │
    │  │   └──────────────────────┘     │  │
    │  └────────────────────────────────┘  │
    │                                      │
    │  B1: AN6 bolt, 1/4"-20 × 3"         │
    │  B2: AN6 bolt, 1/4"-20 × 3"         │
    │  Bushings: AN960-616 washer          │
    │  Nut: AN365-616A castle nut          │
    │  Cotter pin: AN380-2-2A              │
    └─────────────────────────────────────┘

    Bolt pattern: 2 bolts per side
    Bolt material: Cadmium-plated steel
    Torque: 25-30 ft-lb
    Safety wire: yes, 0.032" stainless
```

### 2.5 Flaps
- **Type**: Plain flap (hinged trailing edge)
- **Span**: 50% of wing span (3500mm each side)
- **Chord**: 30% of local chord
- **Deflection**: 0°–45°
- **Actuation**: Manual cable
- **Position**: Inboard section, from root to 50% span

### 2.6 Ailerons
- **Type**: Plain aileron
- **Span**: 50% of wing span (3500mm each side)
- **Chord**: 25% of local chord
- **Deflection**: ±25°
- **Actuation**: Control stick via cable
- **Position**: Outboard section, from 50% to tip

---

## 3. EMPENNAGE (TAIL)

### 3.1 Horizontal Stabilizer
```
    ┌───────────────────────────────────────────────────┐
    │            HORIZONTAL STABILIZER                    │
    │                                                    │
    │    ◄──── 3000mm span ────►                        │
    │                                                    │
    │   ┌──────────────────────────────────────────┐     │
    │   │  ╱╲                                      │     │
    │   │ ╱  ╲    NACA 0009                        │     │
    │   │╱    ╲   (symmetric)                     │     │
    │   │      ╲                                   │     │
    │   │       ╲                                  │     │
    │   │        ╲   TRAILING EDGE                 │     │
    │   │         ╲                                │     │
    │   │          ╲─── ELEVATOR                   │     │
    │   │                                           │     │
    │   └──────────────────────────────────────────┘     │
    │                                                    │
    │   Airfoil: NACA 0009 (symmetric)                  │
    │   Span: 3000 mm                                   │
    │   Chord: 800 mm                                   │
    │   Elevator chord: 250 mm (30%)                    │
    │   Elevator deflection: ±25°                       │
    │   Spar: 1"×1"×1/8" Al sq tube                     │
    │   Skin: 0.032" Al sheet                           │
    │   Ribs: 0.032" Al, NACA 0009                     │
    └───────────────────────────────────────────────────┘
```

### 3.2 Vertical Stabilizer
```
    ┌───────────────────────────────────────────────────┐
    │            VERTICAL STABILIZER                      │
    │                                                    │
    │   ◄── 1500mm height ──►                          │
    │                                                    │
    │   ┌────────────────────┐                          │
    │   │  ╱╲                │                          │
    │   │ ╱  ╲   NACA 0009  │                          │
    │   │╱    ╲             │                          │
    │   │      ╲            │                          │
    │   │       ╲           │                          │
    │   │        ╲  RUDDER  │                          │
    │   │         ╲         │                          │
    │   │          ╲        │                          │
    │   │           ╲       │                          │
    │   └────────────────────┘                          │
    │                                                    │
    │   Airfoil: NACA 0009 (symmetric)                  │
    │   Height: 1500 mm                                │
    │   Chord: 1000 mm                                 │
    │   Rudder chord: 350 mm (35%)                     │
    │   Rudder deflection: ±30°                        │
    │   Spar: 1"×1"×1/8" Al sq tube                    │
    │   Skin: 0.032" Al sheet                          │
    └───────────────────────────────────────────────────┘
```

---

## 4. LANDING GEAR

### 4.1 Configuration
- **Type**: Tricycle (nose wheel + 2 main gear)
- **Main gear track**: 2400 mm
- **Main gear position**: 2000mm aft of CG
- **Nose gear position**: 1500mm forward of CG
- **CG range**: 25%–33% MAC (350mm–462mm from leading edge)

### 4.2 Main Gear Detail
```
    ┌───────────────────────────────────────────────────┐
    │            MAIN GEAR DETAIL                        │
    │                                                    │
    │                    ┌─────────┐                     │
    │                    │  GEAR   │                     │
    │                    │  LEG    │                     │
    │                    │         │                     │
    │                    │  4130   │                     │
    │                    │  Chrome │                     │
    │                    │  Moly   │                     │
    │                    │         │                     │
    │                    │  1" OD  │                     │
    │                    │  × 0.095│                     │
    │                    │  wall   │                     │
    │                    │         │                     │
    │                    │  Length: │                     │
    │                    │  800mm  │                     │
    │                    └────┬────┘                     │
    │                         │                          │
    │                    ┌────┴────┐                     │
    │                    │ BUNGEE  │                     │
    │                    │ SHOCK   │                     │
    │                    └────┬────┘                     │
    │                         │                          │
    │                    ┌────┴────┐                     │
    │                    │  WHEEL  │                     │
    │                    │  6.00×6 │                     │
    │                    └─────────┘                     │
    │                                                    │
    │   Shock absorption: 4× bungee cord, 3/4" dia      │
    │   Total stroke: 150mm                              │
    │   Wheel bearing: sealed, automotive               │
    │   Tire pressure: 30 PSI                           │
    │   Brakes: hydraulic disc, dual-caliper            │
    └───────────────────────────────────────────────────┘
```

### 4.3 Nose Gear Detail
```
    ┌───────────────────────────────────────────────────┐
    │            NOSE GEAR DETAIL                        │
    │                                                    │
    │                    ┌─────────┐                     │
    │                    │  STRUT  │                     │
    │                    │         │                     │
    │                    │  4130   │                     │
    │                    │  Chrome │                     │
    │                    │  Moly   │                     │
    │                    │         │                     │
    │                    │  0.75"  │                     │
    │                    │  OD     │                     │
    │                    │         │                     │
    │                    │  Oleo   │                     │
    │                    │  type   │                     │
    │                    │         │                     │
    │                    │  Stroke:│                     │
    │                    │  100mm  │                     │
    │                    └────┬────┘                     │
    │                         │                          │
    │                    ┌────┴────┐                     │
    │                    │  FORK   │                     │
    │                    └────┬────┘                     │
    │                         │                          │
    │                    ┌────┴────┐                     │
    │                    │  WHEEL  │                     │
    │                    │  5.00×5 │                     │
    │                    └─────────┘                     │
    │                                                    │
    │   Shock absorption: internal oleo spring           │
    │   Steering: connected to rudder pedals             │
    │   Tire pressure: 25 PSI                           │
    └───────────────────────────────────────────────────┘
```

---

## 5. CG CALCULATIONS

### 5.1 Weight Distribution
| Component | Weight (kg) | Location (mm from nose) | Moment (kg·mm) |
|---|---|---|---|
| Fuselage frame | 120 | 4000 | 480,000 |
| Wings (pair) | 100 | 3800 | 380,000 |
| Empennage | 25 | 7200 | 180,000 |
| Landing gear | 60 | 3500 | 210,000 |
| Motor-Left | 15 | 800 | 12,000 |
| Motor-Right | 15 | 800 | 12,000 |
| Propellers (pair) | 5 | 750 | 3,750 |
| ESCs (pair) | 4 | 1200 | 4,800 |
| Batteries (group A) | 80 | 3000 | 240,000 |
| Batteries (group B) | 80 | 3200 | 256,000 |
| Avionics | 10 | 1000 | 10,000 |
| Instruments | 5 | 900 | 4,500 |
| Controls | 8 | 3500 | 28,000 |
| Seats (4) | 30 | 3800 | 114,000 |
| Safety equip | 30 | 3000 | 90,000 |
| Miscellaneous | 20 | 4000 | 80,000 |
| **Empty weight** | **602** | **3420** | **2,103,050** |
| Pilot | 80 | 3000 | 240,000 |
| Passengers (3) | 240 | 3600 | 864,000 |
| **Full weight** | **922** | **3420** | **3,207,050** |

### 5.2 CG Position
- **Empty CG**: 2,103,050 / 602 = 3494 mm from nose
- **Full CG**: 3,207,050 / 922 = 3478 mm from nose
- **CG range**: 3400–3600 mm from nose
- **MAC**: 1400 mm chord
- **CG as % MAC**: (3494 - 3400) / 1400 = 6.7% (empty) — TOO FAR FORWARD

> **Note**: CG calculation requires iteration. Batteries should be positioned aft to achieve 25–33% MAC target. Adjust battery locations to 3800–4200mm from nose.

---

## 6. FLIGHT CONTROLS

### 6.1 Control Routing
```
    ┌───────────────────────────────────────────────────┐
    │            CONTROL ROUTING                         │
    │                                                    │
    │   STICK ──[PUSH-PULL]──┬── AILERON               │
    │                        │   (cable to wing)         │
    │                        │                          │
    │                        └── ELEVATOR              │
    │                            (cable to tail)        │
    │                                                    │
    │   PEDALS ──[PUSH-PULL]──┬── RUDDER              │
    │                         │   (cable to tail)       │
    │                         │                          │
    │                         └── NOSE GEAR            │
    │                             (cable to strut)      │
    │                                                    │
    │   THROTTLE ──[ELECTRIC]──┬── ESC-L              │
    │                          │   (signal wire)        │
    │                          │                         │
    │                          └── ESC-R              │
    │                              (signal wire)        │
    │                                                    │
    │   FLAP HANDLE ──[CABLE]── FLAPS                  │
    │                         (cable to wing)           │
    │                                                    │
    │   TRIM SWITCH ──[ELECTRIC]── TRIM MOTOR          │
    │                              (linear actuator)     │
    └───────────────────────────────────────────────────┘
```

### 6.2 Control Travel Limits
| Control | Neutral | Full Left/Down | Full Right/Up |
|---|---|---|---|
| Aileron | 0° | -25° | +25° |
| Elevator | 0° | -25° | +25° |
| Rudder | 0° | -30° | +30° |
| Flaps | 0° (up) | — | 45° (down) |
| Trim | 0° | -10° | +10° |

---

## 7. MATERIAL SPECIFICATIONS

### 7.1 Aluminum
| Alloy | Temper | Use | Tensile Strength |
|---|---|---|---|
| 6061 | T6 | Frame, structure | 310 MPa |
| 2024 | T3 | Wing skin (alternate) | 485 MPa |
| 5052 | H32 | Fairings, non-structural | 330 MPa |

### 7.2 Steel
| Alloy | Use | Tensile Strength |
|---|---|---|
| 4130 | Landing gear, fittings | 560 MPa |
| 4340 | High-stress fittings | 745 MPa |
| 304 | Hardware, nuts/bolts | 505 MPa |

### 7.3 Fasteners
| Type | Size | Use |
|---|---|---|
| AN6 | 1/4"-20 | Wing root bolts |
| AN8 | 5/16"-18 | Landing gear bolts |
| AN3 | 3/16"-24 | General structure |
| AD41623 | 1/8" pop rivet | Skin attachment |
| AD41624 | 5/32" pop rivet | High-load skin |
| AN365 | Castle nut | Critical bolts |
| AN960 | Washer | Under all bolts |

---

## 8. WEIGHT AND BALANCE SUMMARY

| Item | Weight (kg) |
|---|---|
| Empty weight | 800 |
| Max fuel/battery | 80 |
| Pilot | 80 |
| Passengers (3-5) | 240-400 |
| Cargo | 0-160 |
| **MTOW** | **1,360** |

> **Note**: At 800 kg empty, this aircraft exceeds Part 103 ultralight limits (317 kg). Classification as Experimental Amateur-Built (FAR Part 21.191) is required. See 09_REGULATORY.md.
