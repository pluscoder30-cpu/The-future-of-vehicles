# PHI PLANT DRONE — MECHANICAL DESIGN

## Frame Design and Structural Specifications

---

## FRAME OVERVIEW

The PHI Plant Drone frame is 3D printed from PLA filament. Larger than the healing drone to accommodate water tank and seed dispenser. Uses phi-harmonic proportions for stability under payload.

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         500mm
  ←───────────────────────→
  ┌────────────────────────┐  ─┬─
  │                        │   │
  │    ╔══╗          ╔══╗  │   │
  │    ║M1║          ║M2║  │   │
  │    ╚══╝          ╚══╝  │   │
  │                        │   │
  │   ┌────────────────┐   │   │
  │   │                │   │   │
  │   │    CENTER      │   │   │ 309mm
  │   │    BODY        │   │   │ (500/phi)
  │   │                │   │   │
  │   │   ┌────────┐   │   │   │
  │   │   │ SEEDS  │   │   │   │
  │   │   │ WATER  │   │   │   │
  │   │   └────────┘   │   │   │
  │   │                │   │   │
  │   └────────────────┘   │   │
  │                        │   │
  │    ╔══╗          ╔══╗  │   │
  │    ║M3║          ║M4║  │   │
  │    ╚══╝          ╚══╝  │   │
  │                        │   │
  └────────────────────────┘  ─┴─

  Arm Length: 180mm (center to motor)
  Arm Width: 30mm
  Arm Thickness: 10mm
  Center Body: 200mm x 200mm x 60mm
```

---

## PHI-HARMONIC DIMENSIONS

```
GOLDEN RATIO RELATIONSHIPS:
═══════════════════════════════════════════════════════════════

  Overall Width: 500mm
  Overall Height: 309mm (= 500/phi)
  Body Width: 200mm
  Body Height: 124mm (= 200/phi)
  Arm Length: 180mm
  Arm Width: 111mm (= 180/phi)
  Motor Mount: 70mm
  Motor Holes: 43mm (= 70/phi)

  All dimensions maintain phi-harmonic relationships:
  ┌──────────────────────────────────────────┐
  │  500mm / 309mm = 1.618 = phi            │
  │  200mm / 124mm = 1.613 ≈ phi            │
  │  180mm / 111mm = 1.622 ≈ phi            │
  │  70mm / 43mm   = 1.628 ≈ phi            │
  └──────────────────────────────────────────┘
```

---

## ARM DESIGN

```
ARM CROSS-SECTION:
═══════════════════════════════════════════════════════════════

  Motor Mount     Arm Shaft     Body
  ┌──────┐      ┌──────────┐  ┌────┐
  │ ╔══╗ │      │          │  │    │
  │ ║M ║ │──────│  180mm   │──│    │
  │ ╚══╝ │      │          │  │    │
  └──────┘      └──────────┘  └────┘
   70mm           30mm wide    Center

  Material: PLA (3D printed)
  Infill: 50% gyroid (heavier payload)
  Walls: 4 perimeters
  Thickness: 10mm
```

---

## CENTER BODY

```
CENTER BODY LAYOUT:
═══════════════════════════════════════════════════════════════

  Top View (lid removed):
  ┌────────────────────────────────────┐
  │                                    │
  │  ┌──────────┐  ┌──────────┐       │
  │  │          │  │          │       │
  │  │   SEED   │  │  WATER   │       │
  │  │ DISPENSER│  │  TANK    │       │
  │  │          │  │  500ml   │       │
  │  │ 100x80mm │  │ 100x80mm│       │
  │  │          │  │          │       │
  │  └──────────┘  └──────────┘       │
  │                                    │
  │  ┌──────────┐  ┌──────────┐       │
  │  │          │  │          │       │
  │  │  FPB-5   │  │ AVIONICS │       │
  │  │ BATTERY  │  │ Arduino  │       │
  │  │ 120x70mm │  │ 80x60mm  │       │
  │  │          │  │          │       │
  │  └──────────┘  └──────────┘       │
  │                                    │
  │  ┌──────────────────────────┐     │
  │  │    FREQUENCY GENERATOR   │     │
  │  └──────────────────────────┘     │
  │                                    │
  └────────────────────────────────────┘

  Wall thickness: 3mm
  Internal height: 55mm
  External height: 60mm
```

---

## SEED DISPENSER MECHANISM

```
SEED DISPENSER:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │                                    │
  │  HOPPER (3D printed)              │
  │  ┌──────────────────┐             │
  │  │ Seeds go here    │             │
  │  │ ┌──────────────┐ │             │
  │  │ │  ▼ ▼ ▼ ▼ ▼  │ │             │
  │  │ │  Seeds flow  │ │             │
  │  │ └──────┬───────┘ │             │
  │  │        │         │             │
  │  └────────┤─────────┘             │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │   GATE    │ ← Servo opens/closes
  │     │  (servo)  │                 │
  │     └─────┬─────┘                 │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │ AGITATOR  │ ← Vibration motor
  │     │ (vibrate) │   shakes seeds
  │     └─────┬─────┘                 │
  │           │                       │
  │           ▼                       │
  │     ┌───────────┐                 │
  │     │ SEED TRAY │                 │
  │     │ (aluminum)│                 │
  │     └─────┬─────┘                 │
  │           │                       │
  │           ▼                       │
  │     Seeds drop to ground          │
  │                                    │
  └────────────────────────────────────┘

  Capacity: 200g seeds (~5000 small seeds)
  Drop rate: 10 seeds/second (adjustable)
  Servo angle: 0° (closed) to 90° (open)
```

---

## WATER SYSTEM

```
WATER SYSTEM:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │                                    │
  │  WATER TANK (500ml)               │
  │  ┌──────────────────┐             │
  │  │  ~~~~~~~~~~~~~~  │             │
  │  │  ~~~ WATER ~~~  │             │
  │  │  ~~~~~~~~~~~~~~  │             │
  │  └────────┬─────────┘             │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │   PUMP    │ ← 12V, 3L/min  │
  │     │  (12V)    │                 │
  │     └─────┬─────┘                 │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │ CHECK     │ ← Prevents drip│
  │     │ VALVE     │                 │
  │     └─────┬─────┘                 │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │  NOZZLE   │ ← Adjustable   │
  │     │ (spray)   │   spray pattern│
  │     └───────────┘                 │
  │                                    │
  └────────────────────────────────────┘

  Spray pattern: 30° cone
  Spray distance: 0.5-1.5m
  Flow rate: 100ml/min (adjustable)
  Coverage: 1m diameter circle
```

---

## PROP GUARDS

Each motor gets a prop guard ring (phi-harmonic sizing):

- Ring diameter: 450mm (prop: 400mm)
- Ring width: 15mm
- Ring thickness: 5mm
- Clearance: 25mm
- Weight: 20g per guard (80g total)

---

## MATERIAL SPECIFICATIONS

| Component | Material | Weight |
|-----------|----------|--------|
| Frame arms | PLA 3D printed | 120g |
| Center body | PLA 3D printed | 160g |
| Motor mounts | PLA 3D printed | 55g |
| Prop guards | PLA 3D printed | 80g |
| Lid | PLA 3D printed | 30g |
| Hardware | Steel bolts/nuts | 45g |
| Dampeners | Rubber | 12g |
| **Total Frame** | | **502g** |

---

## ASSEMBLY SEQUENCE

1. Print all frame parts (16-20 hours print time)
2. Clean and sand all parts
3. Install motor mounts on arms
4. Attach arms to center body
5. Install prop guards
6. Install seed dispenser
7. Install water system
8. Mount battery straps
9. Install sensor mounts
10. Attach GPS mast
11. Final inspection and torque check
