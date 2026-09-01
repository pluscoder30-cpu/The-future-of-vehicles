# PHI AI FIRE DRONE — MECHANICAL DESIGN

## Frame Design (AI-Enhanced)

---

## FRAME OVERVIEW

The PHI AI Fire Drone uses a larger 500mm frame to carry retardant payload and AI processor. All dimensions follow phi-harmonic proportions.

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         500mm
  ←─────────────────────→
  ┌──────────────────────┐  ─┬─
  │                      │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M1║        ║M2║  │   │
  │    ╚══╝        ╚══╝  │   │
  │                      │   │
  │   ┌──────────────┐   │   │
  │   │   CENTER     │   │   │ 309mm
  │   │   BODY       │   │   │ (500/phi)
  │   │              │   │   │
  │   │  ┌────┐      │   │   │
  │   │  │BATT│      │   │   │
  │   │  └────┘      │   │   │
  │   │              │   │   │
  │   │  ┌────┐      │   │   │
  │   │  │ AI │      │   │   │
  │   │  └────┘      │   │   │
  │   │              │   │   │
  │   │  ┌────────┐  │   │   │
  │   │  │RETARDANT│  │   │   │
  │   │  │ TANK   │  │   │   │
  │   │  └────────┘  │   │   │
  │   └──────────────┘   │   │
  │                      │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M3║        ║M4║  │   │
  │    ╚══╝        ╚══╝  │   │
  │                      │   │
  └──────────────────────┘  ─┴─

  Arm Length: 185mm
  Arm Width: 30mm
  Arm Thickness: 10mm
  Center Body: 200mm x 200mm x 60mm
```

---

## RETARDANT TANK MOUNTING

```
RETARDANT TANK LAYOUT:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────┐
  │                                      │
  │   RETARDANT TANK (2 Liter)          │
  │   ┌──────────────────────────────┐  │
  │   │                              │  │
  │   │   ┌──────────────────────┐   │  │
  │   │   │                      │   │  │
  │   │   │   200mm x 100mm x 80mm│   │  │
  │   │   │                      │   │  │
  │   │   └──────────────────────┘   │  │
  │   │                              │  │
  │   │   Inlet: Top (fill port)     │  │
  │   │   Outlet: Bottom (to pump)   │  │
  │   │   Material: HDPE plastic     │  │
  │   │   Weight: 150g (empty)       │  │
  │   │                              │  │
  │   └──────────────────────────────┘  │
  │                                      │
  │   Mounting: Velcro straps + bracket  │
  │   CG adjustment: Slide forward/back  │
  │                                      │
  └──────────────────────────────────────┘
```

---

## MATERIAL SPECIFICATIONS

| Component | Material | Dimensions | Weight |
|-----------|----------|------------|--------|
| Frame arms | PLA 3D printed | 4x 185x30x10mm | 120g |
| Center body | PLA 3D printed | 200x200x60mm | 180g |
| Motor mounts | PLA 3D printed | 4x 70x70x12mm | 55g |
| Prop guards | PLA 3D printed | 4x 450mm rings | 80g |
| Retardant mount | PLA 3D printed | Custom bracket | 30g |
| AI processor mount | PLA 3D printed | 70x35x10mm | 10g |
| Hardware | Steel bolts/nuts | M3/M4 assorted | 50g |
| Dampeners | Rubber | 8x 10mm | 15g |
| **Total Frame** | | | **540g** |

---

## WEIGHT CHECKLIST

| Component | Target Weight |
|-----------|---------------|
| Frame (with mounts) | 540g |
| Motors (4x) | 320g |
| ESCs (4x) | 120g |
| Propellers (4x) | 80g |
| Battery (FPB-10) | 1400g |
| Arduino + sensors | 70g |
| Raspberry Pi + Camera | 15g |
| Thermal Camera | 10g |
| Retardant System (empty) | 200g |
| Retardant (2L full) | 200g |
| Frequency generator | 50g |
| Wiring and hardware | 100g |
| **Total** | **3,105g** |

**Target: Under 3,500g (7.7 lbs)**
