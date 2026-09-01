# PHI FIRE DRONE — MECHANICAL DESIGN

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
  │   │  │TANK││CAM │  │   │
  │   │  │2L  ││    │  │   │
  │   │  └────┘└────┘  │   │
  │   └────────────────┘   │
  │    ╔══╗          ╔══╗  │
  │    ║M3║          ║M4║  │
  │    ╚══╝          ╚══╝  │
  └────────────────────────┘

  Arm: 200mm, Body: 200x200x70mm
  Reinforced for heavy payload
```

---

## RETARDANT TANK

```
RETARDANT SYSTEM:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  RETARDANT TANK (2L)              │
  │  Height: 162mm (= 100×φ)         │
  │  Diameter: 100mm                   │
  │  H/D = 1.62 ≈ φ                   │
  │                                    │
  │  ┌──────────┐                     │
  │  │ ~~~~~~~~ │                     │
  │  │ ~WATER~~ │                     │
  │  │ ~~~~~~~~ │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │  PUMP    │ 12V, 5L/min        │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │ NOZZLES  │ 2x wide spray      │
  │  └──────────┘                     │
  └────────────────────────────────────┘

  Capacity: 2 liters (2 kg)
  Spray coverage: 3m diameter
  Duration: 24 seconds at full flow
```

---

## MATERIALS

| Component | Material | Weight |
|-----------|----------|--------|
| Frame (reinforced) | PLA 3D printed | 550g |
| Motors (4x) | Brushless | 400g |
| ESCs (4x) | | 120g |
| Props (4x) | 500mm | 100g |
| Battery (FPB-10) | 2× FPB-5 | 1700g |
| Retardant (full) | Water/retardant | 2000g |
| Cameras | | 100g |
| Avionics | | 80g |
| Retardant system | | 150g |
| Frequency gen | | 50g |
| Wiring | | 100g |
| **Total** | | **5,350g** |

**Max takeoff weight: 6 kg**
