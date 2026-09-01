# PHI_HUMANOID_ROBOT — Mechanical Design

## Mechanical Drawings, Dimensions & Assembly Geometry

---

## 1. Overall Dimensions

```
                    FRONT VIEW                          SIDE VIEW
                    ──────────                          ──────────

                 ← 200mm →                          ← 180mm →
                ┌──────────┐                         ┌──────────┐
                │  HEAD    │ ← 150mm                 │  HEAD    │ ← 150mm
                │  200×180 │                         │  180×150 │
                └────┬─────┘                         └────┬─────┘
                     │ Neck (80mm)                        │ Neck (80mm)
                ┌────┴─────┐                         ┌────┴─────┐
                │          │                         │          │
           ────┤  TORSO   ├────                ────┤  TORSO   ├────
          │    │  300×200  │    │               │    │  200×180  │    │
          │    │  400mm H  │    │               │    │  400mm H  │    │
          │    └────┬─────┘    │               │    └────┬─────┘    │
          │         │          │               │         │          │
     ┌────┴────┐    │    ┌────┴────┐     ┌────┴────┐    │    ┌────┴────┐
     │ LEFT    │    │    │ RIGHT   │     │ LEFT    │    │    │ RIGHT   │
     │ SHOULDER│    │    │SHOULDER │     │ SHOULDER│    │    │SHOULDER │
     │ 130mm   │    │    │ 130mm   │     │ 130mm   │    │    │ 130mm   │
     └────┬────┘    │    └────┬────┘     └────┬────┘    │    └────┬────┘
          │         │         │               │         │         │
     ┌────┴────┐    │    ┌────┴────┐     ┌────┴────┐    │    ┌────┴────┐
     │  UPPER  │    │    │  UPPER  │     │  UPPER  │    │    │  UPPER  │
     │  ARM    │    │    │  ARM    │     │  ARM    │    │    │  ARM    │
     │  250mm  │    │    │  250mm  │     │  250mm  │    │    │  250mm  │
     └────┬────┘    │    └────┬────┘     └────┬────┘    │    └────┬────┘
          │         │         │               │         │         │
     ┌────┴────┐    │    ┌────┴────┐     ┌────┴────┐    │    ┌────┴────┐
     │  LOWER  │    │    │  LOWER  │     │  LOWER  │    │    │  LOWER  │
     │  ARM    │    │    │  ARM    │     │  ARM    │    │    │  ARM    │
     │  280mm  │    │    │  280mm  │     │  280mm  │    │    │  280mm  │
     └────┬────┘    │    └────┬────┘     └────┬────┘    │    └────┬────┘
          │         │         │               │         │         │
     ┌────┴────┐    │    ┌────┴────┐     ┌────┴────┐    │    ┌────┴────┐
     │  HAND   │    │    │  HAND   │     │  HAND   │    │    │  HAND   │
     │ 120×80  │    │    │ 120×80  │     │ 120×80  │    │    │ 120×80  │
     │  120mm  │    │    │  120mm  │     │  120mm  │    │    │  120mm  │
     └─────────┘    │    └─────────┘     └─────────┘    │    └─────────┘
                    │                                    │
               ┌────┴─────┐                        ┌────┴─────┐
               │  PELVIS  │                        │  PELVIS  │
               │  200×150 │                        │  150×120 │
               └────┬─────┘                        └────┬─────┘
                    │                                    │
               ┌────┴────┐                         ┌────┴────┐
               │  UPPER  │ ← 300mm                 │  UPPER  │ ← 300mm
               │  LEG    │                         │  LEG    │
               │  (FEMUR)│                         │  (FEMUR)│
               └────┬────┘                         └────┬────┘
                    │                                    │
               ┌────┴────┐                         ┌────┴────┐
               │  LOWER  │ ← 350mm                 │  LOWER  │ ← 350mm
               │  LEG    │                         │  LEG    │
               │  (TIBIA)│                         │  (TIBIA)│
               └────┬────┘                         └────┬────┘
                    │                                    │
               ┌────┴────┐                         ┌────┴────┐
               │  FOOT   │ ← 100mm                 │  FOOT   │ ← 100mm
               │ 250×100 │                         │ 250×100 │
               └─────────┘                         └─────────┘

     ←──────── 600mm ────────→                ←──────── 400mm ────────→
      (shoulder to shoulder)                   (front to back)
```

## 2. Height Breakdown

| Segment | Height (mm) | φ Ratio | Notes |
|---------|-------------|---------|-------|
| Foot | 100 | — | 250mm L × 100mm W |
| Ankle offset | 25 | — | Joint center height |
| Lower leg | 350 | φ×216 | Knee flexion/extension range |
| Knee joint | 30 | — | Joint housing |
| Upper leg | 300 | φ×185 | Hip-to-knee |
| Hip joint | 35 | — | Joint housing |
| Pelvis | 80 | — | Width: 200mm |
| Torso | 400 | φ×247 | Waist to shoulder |
| Neck | 80 | — | Pan/tilt mechanism |
| Head | 150 | — | 200mm W × 180mm D × 150mm H |
| **Total** | **1,600** | **63.0 in** | — |

## 3. Phi-Harmonic Joint Geometry

### 3.1 Joint Angular Arrangement (137.5° Offset)

Each pair of co-located joints uses a 137.5° (φ × 90° = 145.6° rounded to 137.5°) angular offset to minimize interference and optimize torque distribution.

```
              0° (reference)
                │
                │   Joint A
                │   (mounted at 0°)
                │
                ├─── 137.5° ─── Joint B
                │                (mounted at 137.5°)
                │
                │   Cross-section view showing motor placement
                │
                │
                ▼ 270° (bottom)
```

### 3.2 Hip Joint Assembly (HAA + HFE)

```
        TOP VIEW                              SIDE VIEW
        ─────────                             ──────────

    ┌─────────────┐                      ┌─────────────┐
    │  PELVIS     │                      │  PELVIS     │
    │  PLATE      │                      │  PLATE      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  HAA MOTOR  │ ← 137.5° offset     │  HAA MOTOR  │
    │  D6374      │    from HFE          │  D6374      │
    │  14.5Nm     │                      │  14.5Nm     │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  HFE MOTOR  │ ← 0° reference       │  HFE MOTOR  │
    │  D6374      │                      │  D6374      │
    │  14.5Nm     │                      │  14.5Nm     │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  ENCODER     │                      │  ENCODER     │
    │  AS5048A     │                      │  AS5048A     │
    │  14-bit      │                      │  14-bit      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  UPPER LEG  │                      │  UPPER LEG  │
    │  (FEMUR)    │                      │  (FEMUR)    │
    │  40mm OD    │                      │  40mm OD    │
    └─────────────┘                      └─────────────┘

    Joint HAA range: ±35°                  Joint HFE range: -120° to +30°
    (abduction/adduction)                  (flexion/extension)
```

### 3.3 Knee Joint Assembly (KFE + KAA)

```
        FRONT VIEW                           SIDE VIEW
        ──────────                           ──────────

    ┌─────────────┐                      ┌─────────────┐
    │  UPPER LEG  │                      │  UPPER LEG  │
    │  (FEMUR)    │                      │  (FEMUR)    │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  KFE MOTOR  │ ← 137.5° offset     │  KFE MOTOR  │
    │  D6374      │    from KAA          │  D6374      │
    │  14.5Nm     │                      │  14.5Nm     │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  KAA MOTOR  │ ← 0° reference       │  KAA MOTOR  │
    │  D5065      │                      │  D5065      │
    │  4.8Nm      │                      │  4.8Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  LOWER LEG  │                      │  LOWER LEG  │
    │  (TIBIA)    │                      │  (TIBIA)    │
    │  35mm OD    │                      │  35mm OD    │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  ANKLE      │                      │  ANKLE      │
    │  JOINT      │                      │  JOINT      │
    └─────────────┘                      └─────────────┘

    Joint KFE range: 0° to +130°         Joint KAA range: ±15°
    (flexion/extension)                  (abduction/adduction)
```

### 3.4 Ankle Joint Assembly (AFE + TOE)

```
        FRONT VIEW                           SIDE VIEW
        ──────────                           ──────────

    ┌─────────────┐                      ┌─────────────┐
    │  LOWER LEG  │                      │  LOWER LEG  │
    │  (TIBIA)    │                      │  (TIBIA)    │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  AFE MOTOR  │ ← 137.5° offset     │  AFE MOTOR  │
    │  D5065      │    from TOE          │  D5065      │
    │  4.8Nm      │                      │  4.8Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  TOE MOTOR  │ ← 0° reference       │  TOE MOTOR  │
    │  D5065      │                      │  D5065      │
    │  4.8Nm      │                      │  4.8Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  FOOT PLATE │                      │  FOOT PLATE │
    │  250×100mm  │                      │  250×100mm  │
    │  4mm 6061   │                      │  4mm 6061   │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  RUBBER PAD │                      │  RUBBER PAD │
    │  10mm 60A   │                      │  10mm 60A   │
    └─────────────┘                      └─────────────┘

    Joint AFE range: -20° to +45°        Toe range: 0° to +60°
    (dorsiflexion/plantarflexion)        (toe-off for push-off)
```

### 3.5 Shoulder Joint Assembly (SAA + SFE + SHS)

```
        FRONT VIEW                           SIDE VIEW
        ──────────                           ──────────

    ┌─────────────┐                      ┌─────────────┐
    │  TORSO      │                      │  TORSO      │
    │  FRAME      │                      │  FRAME      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  SAA MOTOR  │ ← 137.5° offset     │  SAA MOTOR  │
    │  D5065      │    from SFE          │  D5065      │
    │  4.8Nm      │                      │  4.8Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  SFE MOTOR  │ ← 0° reference       │  SFE MOTOR  │
    │  D5065      │                      │  D5065      │
    │  4.8Nm      │                      │  4.8Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  SHS MOTOR  │ ← 275° (137.5×2)    │  SHS MOTOR  │
    │  D5065      │                      │  D5065      │
    │  4.8Nm      │                      │  4.8Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  UPPER ARM  │                      │  UPPER ARM  │
    │  (HUMERUS)  │                      │  (HUMERUS)  │
    │  30mm OD    │                      │  30mm OD    │
    └─────────────┘                      └─────────────┘

    SAA range: -90° to +180°            SFE range: -60° to +180°
    SHS range: -45° to +45°            (horizontal adduction)
```

### 3.6 Wrist Joint Assembly (WFE + WRU)

```
        FRONT VIEW                           SIDE VIEW
        ──────────                           ──────────

    ┌─────────────┐                      ┌─────────────┐
    │  LOWER ARM  │                      │  LOWER ARM  │
    │  (ULNA)     │                      │  (ULNA)     │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  WFE MOTOR  │ ← 137.5° offset     │  WFE MOTOR  │
    │  M5671      │    from WRU          │  M5671      │
    │  1.2Nm      │                      │  1.2Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  WRU MOTOR  │ ← 0° reference       │  WRU MOTOR  │
    │  M5671      │                      │  M5671      │
    │  1.2Nm      │                      │  1.2Nm      │
    └──────┬──────┘                      └──────┬──────┘
           │                                     │
    ┌──────┴──────┐                      ┌──────┴──────┐
    │  HAND       │                      │  HAND       │
    │  CHASSIS    │                      │  CHASSIS    │
    │  120×80mm   │                      │  120×80mm   │
    └─────────────┘                      └─────────────┘

    WFE range: -80° to +80°             WRU range: -70° to +70°
```

### 3.7 Hand Assembly (5-Fingered Gripper)

```
        PALM VIEW                           SIDE VIEW
        ──────────                          ──────────

    ┌─────────────────────────────┐     ┌─────────────────────────────┐
    │                             │     │                             │
    │   ┌───┐                     │     │  ┌───┐                     │
    │   │ T │ Thumb               │     │  │ T │                     │
    │   │ h │                     │     │  │ h │                     │
    │   │ u │                     │     │  │ u │                     │
    │   │ m │                     │     │  │ m │                     │
    │   │ b │                     │     │  │ b │                     │
    │   └─┬─┘                     │     │  │ b │                     │
    │     │                       │     │  └─┬─┘                     │
    │  ┌──┴──┐                    │     │    │                       │
    │  │  I  │ Index              │     │  ┌─┴─┐                     │
    │  │  n  │                    │     │  │   │                     │
    │  │  d  │                    │     │  │   │                     │
    │  │  e  │                    │     │  │   │                     │
    │  │  x  │                    │     │  └─┬─┘                     │
    │  └──┬──┘                    │     │    │                       │
    │  ┌──┴──┐                    │     │  ┌─┴─┐                     │
    │  │  M  │ Middle             │     │  │   │                     │
    │  │  i  │                    │     │  │   │                     │
    │  │  d  │                    │     │  │   │                     │
    │  │  d  │                    │     │  └─┬─┘                     │
    │  │  l  │                    │     │    │                       │
    │  │  e  │                    │     │  ┌─┴─┐                     │
    │  └──┬──┘                    │     │  │   │                     │
    │  ┌──┴──┐                    │     │  │   │                     │
    │  │  R  │ Ring               │     │  └─┬─┘                     │
    │  │  i  │                    │     │    │                       │
    │  │  n  │                    │     │  ┌─┴─┐                     │
    │  │  g  │                    │     │  │   │                     │
    │  └──┬──┘                    │     │  └─┬─┘                     │
    │  ┌──┴──┐                    │     │    │                       │
    │  │  P  │ Pinky              │     │  ┌─┴─┐                     │
    │  │  i  │                    │     │  │   │                     │
    │  │  n  │                    │     │  └───┘                     │
    │  │  k  │                    │     │                             │
    │  │  y  │                    │     │  ← 120mm                   │
    │  └──┬──┘                    │     │                             │
    │     │                       │     │  ← 80mm (palm width)        │
    │  ┌──┴──┐                    │     └─────────────────────────────┘
    │  │ PALM│                     │
    │  │     │                     │
    │  └──┬──┘                     │
    │     │                        │
    │  ┌──┴──────┐                │
    │  │  WRIST  │                │
    │  │  MOUNT  │                │
    │  └─────────┘                │
    │                             │
    │  ← 120mm                   │
    └─────────────────────────────┘

    FINGER JOINTS:
    ┌─────────────────────────────────────────────────────────────────┐
    │  Thumb:  CMC (50°) → MCP (70°) → IP (80°)                    │
    │  Index:  MCP (90°) → PIP (100°) → DIP (80°)                  │
    │  Middle: MCP (90°) → PIP (100°) → DIP (80°)                  │
    │  Ring:   MCP (90°) → PIP (100°) → DIP (80°)                  │
    │  Pinky:  MCP (90°) → PIP (100°) → DIP (80°)                  │
    │                                                                 │
    │  φ-sequence finger lengths:                                    │
    │  Index: 70mm  (φ⁰ × 70)                                       │
    │  Middle: 80mm (φ⁰·² × 70 ≈ 80)                               │
    │  Ring: 70mm (φ⁰ × 70)                                         │
    │  Pinky: 55mm (φ⁻⁰·⁵ × 70 ≈ 55)                              │
    │  Thumb: 60mm (φ⁻⁰·² × 70 ≈ 60)                              │
    └─────────────────────────────────────────────────────────────────┘
```

## 4. Joint Specifications Table

| # | Joint | Axis | Motor | Range | Speed | Torque | DOF |
|---|-------|------|-------|-------|-------|--------|-----|
| 1 | Hip AA | Z | D6374 150KV | ±35° | 180°/s | 14.5Nm | 1 |
| 2 | Hip FE | Y | D6374 150KV | -120° to +30° | 180°/s | 14.5Nm | 1 |
| 3 | Knee FE | Y | D6374 150KV | 0° to +130° | 180°/s | 14.5Nm | 1 |
| 4 | Knee AA | Z | D5065 270KV | ±15° | 200°/s | 4.8Nm | 1 |
| 5 | Ankle FE | Y | D5065 270KV | -20° to +45° | 200°/s | 4.8Nm | 1 |
| 6 | Toe Flex | Y | D5065 270KV | 0° to +60° | 200°/s | 4.8Nm | 1 |
| 7 | Shoulder AA | Z | D5065 270KV | -90° to +180° | 200°/s | 4.8Nm | 1 |
| 8 | Shoulder FE | Y | D5065 270KV | -60° to +180° | 200°/s | 4.8Nm | 1 |
| 9 | Shoulder HS | X | D5065 270KV | -45° to +45° | 200°/s | 4.8Nm | 1 |
| 10 | Elbow FE | Y | D5065 270KV | 0° to +145° | 200°/s | 4.8Nm | 1 |
| 11 | Wrist FE | Y | M5671 100KV | -80° to +80° | 300°/s | 1.2Nm | 1 |
| 12 | Wrist RU | X | M5671 100KV | -70° to +70° | 300°/s | 1.2Nm | 1 |
| 13 | Torso Yaw | Z | D6374 150KV | -45° to +45° | 150°/s | 14.5Nm | 1 |
| 14 | Torso Pitch | Y | D6374 150KV | -30° to +30° | 150°/s | 14.5Nm | 1 |
| 15 | Head Pan | Z | M5671 100KV | -90° to +90° | 300°/s | 1.2Nm | 1 |
| 16 | Head Tilt | Y | M5671 100KV | -30° to +45° | 300°/s | 1.2Nm | 1 |

## 5. Center of Mass Analysis

```
MASS DISTRIBUTION (approximate):

Component          Mass (kg)    Height (mm)    CG Height (mm)
──────────────────────────────────────────────────────────────
Head               3.5          1525-1600      1562
Torso              8.0          1045-1445      1245
Left Upper Arm     1.2          1315-1565      1440
Left Lower Arm     0.9          1065-1315      1190
Left Hand          0.4          945-1065       1005
Right Upper Arm    1.2          1315-1565      1440
Right Lower Arm    0.9          1065-1315      1190
Right Hand         0.4          945-1065       1005
Pelvis + Hip       4.5          965-1045       1005
Left Upper Leg     3.5          665-965        815
Left Lower Leg     3.0          315-665        490
Left Foot          2.5          0-100          50
Right Upper Leg    3.5          665-965        815
Right Lower Leg    3.0          315-665        490
Right Foot         2.5          0-100          50
Batteries (×4)     12.0         965-1045       1005
Electronics        1.5          1045-1445      1245
Cabling            0.5          various        1000
──────────────────────────────────────────────────────────────
TOTAL              50.0         —              —
```

**Center of Mass (standing, feet flat):**
- X (lateral): 0mm (symmetric)
- Y (anterior-posterior): ~15mm forward of ankle pivot
- Z (vertical): ~1050mm from ground

**Static Stability Margin:**
- Lateral: 50mm (foot width / 2)
- Anterior: 60mm (heel to CG projection)
- Posterior: 40mm (CG projection to toe)

## 6. Structural Analysis

### 6.1 Load Cases

| Load Case | Description | Safety Factor |
|-----------|-------------|---------------|
| LC1: Standing | Static weight on both feet | 3.0 |
| LC2: Walking | Dynamic load during single support | 2.5 |
| LC3: Running | Dynamic load at 10 km/h | 2.0 |
| LC4: Impact | 0.5m drop, feet flat | 2.0 |
| LC5: Carry | 5 kg payload in hands | 2.5 |

### 6.2 Critical Stress Points

| Location | Max Stress | Material Limit | Safety Factor |
|----------|-----------|----------------|---------------|
| Hip bearing mount | 45 MPa | 276 MPa (6061-T6) | 6.1 |
| Knee bearing mount | 38 MPa | 276 MPa | 7.3 |
| Torso-pelvis joint | 52 MPa | 276 MPa | 5.3 |
| Shoulder mount | 28 MPa | 276 MPa | 9.9 |
| Ankle pivot | 32 MPa | 276 MPa | 8.6 |

### 6.3 Deflection Limits

| Location | Max Deflection | Limit | Status |
|----------|---------------|-------|--------|
| Torso (1g load) | 0.3mm | 2mm | PASS |
| Upper leg (lateral load) | 0.5mm | 3mm | PASS |
| Lower leg (axial load) | 0.2mm | 1mm | PASS |
| Arm (5kg payload) | 1.2mm | 5mm | PASS |

## 7. Tolerance Stack-Up

| Interface | Tolerance | Notes |
|-----------|-----------|-------|
| Joint bearing bore | ±0.02mm | Press-fit, 608ZZ bearing |
| Motor mount holes | ±0.1mm | M4 bolt pattern |
| Structural tube OD | ±0.05mm | 6061-T6 seamless |
| Bearing seat concentricity | ±0.05mm | Critical for encoder accuracy |
| Foot plate flatness | ±0.1mm | FSR mounting surface |

## 8. Weight Budget

| Category | Weight (kg) | % |
|----------|-------------|---|
| Structural frame | 8.0 | 16% |
| Actuators (motors) | 12.5 | 25% |
| Actuators (controllers) | 2.0 | 4% |
| Sensors | 1.0 | 2% |
| Electronics | 1.5 | 3% |
| Batteries | 12.0 | 24% |
| Cabling/connectors | 2.5 | 5% |
| Head subsystem | 2.0 | 4% |
| Hands | 1.5 | 3% |
| Cooling | 0.5 | 1% |
| Fasteners/hardware | 2.0 | 4% |
| Joint covers/decorative | 1.5 | 3% |
| Margin (10%) | 3.0 | 6% |
| **TOTAL** | **50.0** | **100%** |

---

*Document: 03_MECHANICAL.md — PHI_HUMANOID_ROBOT Mechanical Design*
*Version: 1.0 | Date: 2026-08-27*
