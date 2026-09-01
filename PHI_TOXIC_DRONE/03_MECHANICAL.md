# PHI TOXIC DRONE — MECHANICAL DESIGN

## Frame Design

---

## FRAME OVERVIEW

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         500mm
  ←───────────────────────→
  ┌────────────────────────┐
  │    ╔══╗          ╔══╗  │
  │    ║M1║          ║M2║  │
  │    ╚══╝          ╚══╝  │
  │   ┌────────────────┐   │
  │   │    CENTER      │   │  309mm (500/phi)
  │   │    BODY        │   │
  │   │  ┌────┐┌────┐  │   │
  │   │  │TANK││SENS│  │   │
  │   │  │1.5L││    │  │   │
  │   │  └────┘└────┘  │   │
  │   └────────────────┘   │
  │    ╔══╗          ╔══╗  │
  │    ║M3║          ║M4║  │
  │    ╚══╝          ╚══╝  │
  └────────────────────────┘

  Arm: 200mm, Body: 200x200x75mm
  Reinforced for hazmat operations
```

---

## CHEMICAL SENSOR ARRAY

```
SENSOR LAYOUT:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  SENSOR ARRAY (bottom of drone)    │
  │                                    │
  │  ┌──────┐  ┌──────┐  ┌──────┐   │
  │  │MQ-135│  │ MQ-7 │  │ MQ-2 │   │
  │  │ VOC  │  │  CO  │  │ SMOKE│   │
  │  └──────┘  └──────┘  └──────┘   │
  │                                    │
  │  ┌──────┐  ┌──────┐              │
  │  │  pH  │  │TEMP  │              │
  │  │SENSOR│  │SENSOR│              │
  │  └──────┘  └──────┘              │
  │                                    │
  │  Sensor spacing: φ-angles         │
  │  Coverage: 360° detection         │
  └────────────────────────────────────┘

  All sensors extend 3cm below frame
  for direct air/chemical contact
```

---

## NEUTRALIZER SYSTEM

```
NEUTRALIZER TANK:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  NEUTRALIZER SYSTEM                │
  │                                    │
  │  ┌──────────┐                     │
  │  │ TANK 1.5L│                     │
  │  │ H: 162mm │ (= 100×φ)          │
  │  │ D: 100mm │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │ PUMP 24V │ 5L/min             │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │ NOZZLE   │ Adjustable spray   │
  │  └──────────┘                     │
  │                                    │
  │  Neutralizer: baking soda solution│
  │  (for acid spills)                │
  │  Or: activated carbon slurry      │
  │  (for organic spills)             │
  └────────────────────────────────────┘
```

---

## MATERIALS

| Component | Material | Weight |
|-----------|----------|--------|
| Frame (reinforced) | PLA 3D printed | 600g |
| Motors (4x) | Brushless | 480g |
| ESCs (4x) | | 120g |
| Props (4x) | 500mm | 100g |
| Battery (FPB-10) | 2× FPB-5 | 1700g |
| Neutralizer (full) | Chemical | 1500g |
| Sensors | Chemical array | 100g |
| Avionics | | 80g |
| Frequency gen | | 50g |
| Wiring | | 100g |
| Hazmat labels | | 20g |
| **Total** | | **4,850g** |

**Max takeoff weight: 5.5 kg**
