# PHI FOOD DRONE — MECHANICAL DESIGN

## Frame Design and Structural Specifications

---

## FRAME OVERVIEW

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         450mm
  ←───────────────────────→
  ┌────────────────────────┐  ─┬─
  │    ╔══╗          ╔══╗  │   │
  │    ║M1║          ║M2║  │   │
  │    ╚══╝          ╚══╝  │   │
  │   ┌────────────────┐   │   │
  │   │    CENTER      │   │   │ 278mm
  │   │    BODY        │   │   │ (450/phi)
  │   │                │   │   │
  │   │ ┌───┐┌───┐┌───┐│   │   │
  │   │ │HERB││VEG ││FLW││   │   │
  │   │ └───┘└───┘└───┘│   │   │
  │   │                │   │   │
  │   └────────────────┘   │   │
  │    ╔══╗          ╔══╗  │   │
  │    ║M3║          ║M4║  │   │
  │    ╚══╝          ╚══╝  │   │
  └────────────────────────┘  ─┴─

  Arm Length: 165mm
  Arm Width: 28mm
  Body: 180mm x 180mm x 55mm
```

---

## PHI-HARMONIC DIMENSIONS

| Component | Dimension | Phi Relationship |
|-----------|-----------|-----------------|
| Overall width | 450mm | Base |
| Overall height | 278mm | 450/φ |
| Body width | 180mm | 450/φ^1.3 |
| Body height | 111mm | 180/φ |
| Arm length | 165mm | 450/φ^1.6 |
| Herb bay | 130mm | Base |
| Veg bay | 80mm | 130/φ |
| Flower bay | 50mm | 80/φ |

---

## SEED BAY LAYOUT

```
SEED DISPENSER:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  3-CHANNEL SEED DISPENSER          │
  │                                    │
  │  ┌──────────┐ ┌──────┐ ┌──────┐  │
  │  │ HERB     │ │ VEG  │ │ FLWR │  │
  │  │ 130mm    │ │ 80mm │ │ 50mm │  │
  │  │ ┌──────┐ │ │┌────┐│ │┌────┐│  │
  │  │ │Seeds │ │ ││Seeds││ ││Seeds││  │
  │  │ │      │ │ ││    ││ ││    ││  │
  │  │ └──┬───┘ │ │└─┬──┘│ │└─┬──┘│  │
  │  │    │gate │ │  │gate│ │  │gate│  │
  │  │    │servo│ │  │svr │ │  │svr │  │
  │  │    ▼    │ │  ▼  │ │  ▼  │  │
  │  │  SEED   │ │ SEED│ │ SEED│  │
  │  │  TRAY   │ │TRAY │ │TRAY │  │
  │  └──────────┘ └──────┘ └──────┘  │
  │                                    │
  │  Bay ratio: 130/80 = 1.625 ≈ φ   │
  │  Bay ratio: 80/50 = 1.600 ≈ φ    │
  └────────────────────────────────────┘
```

---

## NUTRIENT TANK

```
NUTRIENT TANK:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  NUTRIENT SYSTEM                   │
  │                                    │
  │  ┌──────────┐                     │
  │  │ TANK     │                     │
  │  │ 300ml    │                     │
  │  │ φ height │                     │
  │  │  = 100mm │                     │
  │  │ diameter │                     │
  │  │  = 62mm  │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │  PUMP    │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │  NOZZLE  │                     │
  │  └──────────┘                     │
  │                                    │
  │  Tank H/D = 100/62 = 1.613 ≈ φ   │
  └────────────────────────────────────┘
```

---

## MATERIAL SPECIFICATIONS

| Component | Material | Weight |
|-----------|----------|--------|
| Frame | PLA 3D printed | 380g |
| Motors (4x) | Brushless | 240g |
| ESCs (4x) | | 80g |
| Propellers (4x) | | 50g |
| Battery (FPB-5) | | 850g |
| Arduino + sensors | | 70g |
| Seed system | | 95g |
| Nutrient system | | 85g |
| Frequency gen | | 50g |
| Wiring | | 70g |
| **Total** | | **1,970g** |

**Target: Under 2,100g (4.6 lbs) with full payload**
