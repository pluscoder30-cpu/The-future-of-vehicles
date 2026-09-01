# PHI Medical Stretcher Drone — MECHANICAL DIAGRAM
## Buildable Documentation | Physical Layout & Assembly

---

## EXPLODED VIEW (Top-Down)

```
                    PHI MEDICAL STRETCHER DRONE
                   EXPLODED VIEW (TOP-DOWN)

                    ┌─────────────────────────────────────────┐
                    │              ROTOR SHROUDS               │
                    │         8x enclosed carbon fiber        │
                    │         (folded for transport)          │
                    │              2.2m diagonal              │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         TOP FRAME                        │
                    │    Carbon fiber octocopter frame        │
                    │    2.2m diagonal                        │
                    │    25kg crash-rated                     │
                    │              50mm tall                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         PROPULSION LAYER                 │
                    │    ┌─────────────────────────────┐      │
                    │    │   8x T-Motor U15L Motors    │      │
                    │    │   15kW each, 120KV          │      │
                    │    │   28-inch folding props     │      │
                    │    └─────────────────────────────┘      │
                    │              100mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         AVIONICS BAY                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   Pixhawk 6X Flight Ctrl    │      │
                    │    │   Cube Orange+ Backup       │      │
                    │    │   LiDAR + Cameras + GPS     │      │
                    │    └─────────────────────────────┘      │
                    │              150mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         PATIENT PLATFORM                 │
                    │    ┌─────────────────────────────┐      │
                    │    │   STRETCHER PLATFORM         │      │
                    │    │   ┌─────────────────────┐   │      │
                    │    │   │ MEDICAL MONITOR     │   │      │
                    │    │   │ ECG SpO2 BP Temp    │   │      │
                    │    │   └─────────────────────┘   │      │
                    │    │   ┌─────────────────────┐   │      │
                    │    │   │ PATIENT HARNESS     │   │      │
                    │    │   │ 5-point trauma      │   │      │
                    │    │   └─────────────────────┘   │      │
                    │    │   ┌─────────────────────┐   │      │
                    │    │   │ LIFE SUPPORT        │   │      │
                    │    │   │ O2 IV AED Meds      │   │      │
                    │    │   └─────────────────────┘   │      │
                    │    │   ┌─────────────────────┐   │      │
                    │    │   │ PHI-HARMONIC (x8)   │   │      │
                    │    │   │ 16.18Hz healing     │   │      │
                    │    │   └─────────────────────┘   │      │
                    │    └─────────────────────────────┘      │
                    │              300mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         POWER SYSTEM                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   FPB-20 Battery            │      │
                    │    │   20kWh, 51.2V, 40kg        │      │
                    │    │   4C discharge (80kW)       │      │
                    │    └─────────────────────────────┘      │
                    │              200mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         LANDING GEAR                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   Hydraulic struts (4x)      │      │
                    │    │   Quick-release latches       │      │
                    │    └─────────────────────────────┘      │
                    │              400mm (extended)            │
                    └─────────────────────────────────────────┘

    TOTAL LENGTH: 2200mm (diagonal)
    TOTAL HEIGHT: 800mm (without gear)
    WITH GEAR: 1200mm
```

---

## TOP VIEW WITH DIMENSIONS

```
                    TOP VIEW (Plan Form)

                    ┌─────────────────────────────────────────────┐
                    │                                             │
                    │              2200mm (diagonal)               │
                    │◄───────────────────────────────────────────►│
                    │                                             │
                    │         ┌───┐                   ┌───┐      │
                    │         │M1 │                   │M2 │      │
                    │         └───┘                   └───┘      │
                    │           │                       │         │
                    │           │     ┌─────────┐     │         │
                    │           │     │ FLIGHT  │     │         │
                    │           │     │   CTRL  │     │         │
                    │           │     └─────────┘     │         │
                    │    ┌───┐  │  ┌───────────────┐  │  ┌───┐  │
                    │    │M8 │──┼──│   PATIENT     │──┼──│M3 │  │
                    │    └───┘  │  │   PLATFORM    │  │  └───┘  │
                    │           │  │   ┌───────┐   │  │         │
                    │           │  │   │Stretcher│  │         │
                    │           │  │   └───────┘   │  │         │
                    │    ┌───┐  │  └───────────────┘  │  ┌───┐  │
                    │    │M7 │──┼──────────────────────┼──│M4 │  │
                    │    └───┘  │                      │  └───┘  │
                    │           │     ┌─────────┐     │         │
                    │           │     │  POWER  │     │         │
                    │           │     │ SYSTEM  │     │         │
                    │           │     └─────────┘     │         │
                    │         ┌───┐                   ┌───┐      │
                    │         │M6 │                   │M5 │      │
                    │         └───┘                   └───┘      │
                    │                                             │
                    └─────────────────────────────────────────────┘

                    2200mm width
                    ◄───────────────────────────────────────────►

    MOTOR POSITIONS (8x octocopter):
    - M1, M2: Front (left/right)
    - M3, M4: Right (front/rear)
    - M5, M6: Rear (right/left)
    - M7, M8: Left (rear/front)
    - Spacing: 45° intervals on 2.2m diagonal circle
```

---

## SIDE CROSS-SECTION

```
    SIDE VIEW (Cross-Section)

    ◄──────────── 2200mm (diagonal) ────────────►

    ▲
    │   ┌─────────────────────────────────────────────┐
    │   │ ┌───┐ ┌─────────────────────┐ ┌───┐       │
    │   │ │M1 │ │    ROTOR SHROUD     │ │M2 │       │ Enclosed rotors
    │   │ └───┘ │    (carbon fiber)   │ └───┘       │ (IEC compliant)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         TOP FRAME                       │ │ Carbon composite
    │   │ │    ┌─────────────────────────────┐      │ │ 25kg frame
    │   │ │    │   Flight Controller         │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         PATIENT PLATFORM                 │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Medical Monitor Array     │      │ │ ECG SpO2 BP
    │   │ │    └─────────────────────────────┘      │ │ Temp Resp EtCO2
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Patient Harness           │      │ │ 5-point MIL-STD
    │   │ │    └─────────────────────────────┘      │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Life Support Module       │      │ │ O2 IV AED
    │   │ │    └─────────────────────────────┘      │ │ Medications
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   PHI-Harmonic Emitters (x8)│      │ │ 16.18Hz healing
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         POWER SYSTEM                     │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   FPB-20 Battery Pack       │      │ │ 20kWh 51.2V
    │   │ │    │   40kg, 4C discharge        │      │ │ 80kW max
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌───┐ ┌─────────────────────┐ ┌───┐       │
    │   │ │M8 │ │    ROTOR SHROUD     │ │M7 │       │ Enclosed rotors
    │   │ └───┘ │    (carbon fiber)   │ └───┘       │ (lower set)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         WINCH SYSTEM                     │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Hydraulic Patient Winch    │      │ │ 150kg capacity
    │   │ │    │   10m cable, dual redundant  │      │ │ 10m cable
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         LANDING GEAR                     │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Hydraulic struts (4x)      │      │ │ 400mm travel
    │   │ │    │   Quick-release for pickup   │      │ │ Quick-release
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   └─────────────────────────────────────────────┘
    ▼
         TOTAL HEIGHT: 800mm (frame only)
         WITH GEAR: 1200mm
```

---

## PATIENT PLATFORM LAYOUT

```
    PATIENT PLATFORM (Top View)

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   ◄──────── 1800mm (length) ────────────►   │
    │                                             │
    │   ┌─────────────────────────────────────┐   │ ▲
    │   │                                     │   │ │
    │   │         STRETCHER PLATFORM          │   │ │
    │   │         1800mm x 600mm              │   │ 600mm
    │   │                                     │   │ │
    │   │    ┌─────────────────────────────┐  │   │ │
    │   │    │   PATIENT AREA              │  │   │ │
    │   │    │   1600mm x 500mm            │  │   │ │
    │   │    │                             │  │   │ ▼
    │   │    │   ┌─────┐   ┌─────┐        │  │
    │   │    │   │HEAD │   │FEET │        │  │
    │   │    │   └─────┘   └─────┘        │  │
    │   │    │                             │  │
    │   │    │   5-point harness (x2)     │  │
    │   │    │   Quick-release buckles     │  │
    │   │    └─────────────────────────────┘  │
    │   │                                     │
    │   │    ┌─────────────────────────────┐  │
    │   │    │   MEDICAL MONITOR ARRAY     │  │
    │   │    │   ECG SpO2 BP Temp Resp     │  │
    │   │    │   EtCO2, 5-lead ECG         │  │
    │   │    └─────────────────────────────┘  │
    │   │                                     │
    │   │    ┌─────────────────────────────┐  │
    │   │    │   LIFE SUPPORT MODULE       │  │
    │   │    │   O2 Tank, IV Pump, AED     │  │
    │   │    │   Medication Dispenser      │  │
    │   │    └─────────────────────────────┘  │
    │   │                                     │
    │   │    ┌─────────────────────────────┐  │
    │   │    │   PHI-HARMONIC EMITTERS     │  │
    │   │    │   8x coil emitters          │  │
    │   │    │   16.18Hz primary           │  │
    │   │    │   360° coverage             │  │
    │   │    └─────────────────────────────┘  │
    │   │                                     │
    │   └─────────────────────────────────────┘
    │                                             │
    │   MOTOR ARM ATTACHMENT POINTS:              │
    │   ┌───┐                           ┌───┐    │
    │   │M1 │───── carbon arm ─────────│M2 │    │
    │   └───┘                           └───┘    │
    │     │                                     │
    │   carbon arm                     carbon arm│
    │     │                                     │
    │   ┌───┐                           ┌───┐    │
    │   │M8 │                           │M3 │    │
    │   └───┘                           └───┘    │
    │                                             │
    └─────────────────────────────────────────────┘
```

---

## ROTOR SHROUD DETAIL

```
    ROTOR SHROUD (Side View, per rotor)

    ◄──────────── 300mm (shroud diameter) ────────────►

    ▲
    │   ┌─────────────────────────────────────────────┐
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Top cover
    │   │░░░░░░░░░░░ Carbon fiber ░░░░░░░░░░░░░░░░░░░│ (2mm)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         PROPELLER                       │ │
    │   │ │    28-inch folding carbon fiber         │ │
    │   │ │    Spinning plane (clearance)           │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         MOTOR MOUNT                     │ │
    │   │ │    T-Motor U15L, 15kW                   │ │
    │   │ │    120KV, 88mm diameter                 │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         SHROUD WALL                     │ │
    │   │ │    Carbon fiber, 3mm thick              │ │
    │   │ │    HEPA-filtered air intake             │ │
    │   │ │    Emergency jettison bolts             │ │
    │   │ └─────────────────────────────────────────┘ │
    │   └─────────────────────────────────────────────┘
    ▼

    SHROUD SPECIFICATIONS:
    - Material: Carbon fiber composite
    - Wall thickness: 3mm
    - Diameter: 300mm
    - Air intake: HEPA-filtered (medical grade)
    - Jettison: 4x explosive bolts (emergency only)
    - IEC 60601-1 compliant (medical electrical equipment)
```

---

## WINCH SYSTEM

```
    HYDRAULIC PATIENT WINCH

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   WINCH MECHANISM                           │
    │   ┌─────────────────────────────────────┐   │
    │   │   Hydraulic motor: 5kW             │   │
    │   │   Cable: 150kg rated, 10m length   │   │
    │   │   Speed: 0.5 m/s (loaded)          │   │
    │   │   Dual redundant (2x motors)       │   │
    │   │   Brake: Electromagnetic fail-safe │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   PATIENT HARNESS                           │
    │   ┌─────────────────────────────────────┐   │
    │   │   Type: 5-point trauma-rated       │   │
    │   │   Standard: MIL-STD-1671           │   │
    │   │   Quick-release: Single-pull        │   │
    │   │   Padding: Medical-grade foam       │   │
    │   │   Load rating: 200kg                │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   EXTRACTION METHOD                         │
    │   ┌─────────────────────────────────────┐   │
    │   │   1. Winch lowers to patient        │   │
    │   │   2. Harness secured by paramedic   │   │
    │   │   3. Winch retracts (0.5 m/s)      │   │
    │   │   4. Patient secured on platform    │   │
    │   │   5. Medical monitoring begins      │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   LOAD MONITORING                           │
    │   ┌─────────────────────────────────────┐   │
    │   │   Load cell: 0-200kg, 0.1kg res    │   │
    │   │   Real-time weight distribution     │   │
    │   │   Center of gravity tracking        │   │
    │   │   Alert if >150kg or asymmetric     │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    └─────────────────────────────────────────────┘
```

---

## ASSEMBLY STACK ORDER

```
    ASSEMBLY SEQUENCE (Bottom to Top)

    STEP 1: Landing Gear
    ┌─────────────────────────────────────────┐
    │ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐│
    │ │Strut 1│ │Strut 2│ │Strut 3│ │Strut 4││  Hydraulic struts
    │ └───────┘ └───────┘ └───────┘ └───────┘│  Quick-release
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 2: Power System
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   FPB-20 Battery Pack              │ │  20kWh, 51.2V
    │ │   BMS + Charge Controllers         │ │  40kg, 4C discharge
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 3: Winch System
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Hydraulic Winch (dual redundant)  │ │  150kg, 10m cable
    │ │   Patient Harness                   │ │  MIL-STD quick-release
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 4: Patient Platform
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Stretcher Platform               │ │  1800mm x 600mm
    │ │   Medical Monitor Array            │ │  ECG SpO2 BP Temp
    │ │   Life Support Module              │ │  O2 IV AED
    │ │   PHI-Harmonic Emitters (x8)       │ │  16.18Hz healing
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 5: Avionics Bay
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Pixhawk 6X Flight Controller     │ │  Primary
    │ │   Cube Orange+ Backup              │ │  Redundant
    │ │   LiDAR + 4x Cameras + 2x GPS     │ │  Navigation
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 6: Top Frame
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Carbon Fiber Frame               │ │  2.2m diagonal
    │ │   8x Motor Mounts                  │ │  25kg, crash-rated
    │ │   Rotor Shrouds (8x)              │ │  HEPA-filtered
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
```

---

## DIMENSIONS SUMMARY

| Dimension | Value | Notes |
|-----------|-------|-------|
| Frame Diagonal | 2200mm | Octocopter |
| Frame Height | 50mm | Top frame only |
| Total Height | 800mm | Without gear |
| Total Height (gear) | 1200mm | Extended |
| Rotor Shroud | 300mm dia | Each, 8x |
| Propeller | 28-inch | Folding carbon |
| Patient Platform | 1800 x 600mm | Stretcher |
| Battery Pack | 20kWh | 51.2V, 40kg |
| Winch Cable | 10m | 150kg rated |
| Weight (empty) | 85kg | Without payload |
| Max Payload | 150kg | Patient + equipment |
| Crash Energy | 25kg-rated | Honeycomb crumple zones |

---

## MATERIALS SPECIFICATION

| Component | Material | Grade | Notes |
|-----------|----------|-------|-------|
| Frame | Carbon Composite | Aerospace | 2.2m diagonal |
| Rotor Shrouds | Carbon Fiber | Aerospace | HEPA-filtered |
| Crumple Zones | Honeycomb Aluminum | Aerospace | Crash absorption |
| Landing Gear | Aluminum Alloy | Aircraft | Hydraulic |
| Patient Platform | Aluminum | Medical | 6061-T6 |
| Stretcher Frame | Carbon Fiber | Medical | MIL-STD rated |
| Fasteners | Titanium | Aerospace | MIL-STD |

---

**Document**: 03_MECHANICAL.md
**Vehicle**: PHI MEDICAL STRETCHER DRONE
**Status**: BUILDABLE ✓
