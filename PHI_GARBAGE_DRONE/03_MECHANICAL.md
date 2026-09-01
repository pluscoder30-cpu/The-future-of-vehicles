# PHI GARBAGE DRONE — MECHANICAL DESIGN

## Frame Design

---

## FRAME OVERVIEW

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         450mm
  ←───────────────────────→
  ┌────────────────────────┐
  │    ╔══╗          ╔══╗  │
  │    ║M1║          ║M2║  │
  │    ╚══╝          ╚══╝  │
  │   ┌────────────────┐   │
  │   │    CENTER      │   │  278mm (450/phi)
  │   │    BODY        │   │
  │   │  ┌────┐┌────┐  │   │
  │   │  │ARM ││BINS│  │   │
  │   │  └────┘└────┘  │   │
  │   └────────────────┘   │
  │    ╔══╗          ╔══╗  │
  │    ║M3║          ║M4║  │
  │    ╚══╝          ╚══╝  │
  └────────────────────────┘

  Arm: 165mm, Body: 180x180x65mm
```

---

## ROBOTIC ARM

```
2-DOF ROBOTIC ARM:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  ARM LAYOUT:                       │
  │                                    │
  │  Base servo (rotation)            │
  │       │                           │
  │       ▼                           │
  │  ┌─────────┐                     │
  │  │ Shoulder │ ← Servo 2          │
  │  │  servo   │                     │
  │  └────┬────┘                     │
  │       │                           │
  │       ▼                           │
  │  ┌─────────┐                     │
  │  │  Arm     │ 150mm length       │
  │  │  link    │                     │
  │  └────┬────┘                     │
  │       │                           │
  │       ▼                           │
  │  ┌─────────┐                     │
  │  │ Gripper  │ ← Servo 3         │
  │  │ (2-finger)│                    │
  │  └─────────┘                     │
  │                                    │
  │  Reach: 200mm from center         │
  │  Grip force: 500g                 │
  │  Rotation: 360°                   │
  └────────────────────────────────────┘
```

---

## SORTING SYSTEM

```
3-BIN SORTING SYSTEM:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  SORTING BINS:                     │
  │                                    │
  │  ┌──────┐ ┌──────┐ ┌──────┐     │
  │  │PLASTIC│ │METAL │ │PAPER │     │
  │  │  🔵   │ │  ⚪  │ │  🟤  │     │
  │  │ 100mm │ │ 62mm │ │ 38mm │     │
  │  └──────┘ └──────┘ └──────┘     │
  │                                    │
  │  Bin sizes in phi ratio:           │
  │  100/62 = 1.613 ≈ φ              │
  │  62/38 = 1.632 ≈ φ               │
  │                                    │
  │  Sorting mechanism:                │
  │  1. Arm picks up trash             │
  │  2. Metal detector identifies      │
  │  3. IR sensor identifies type      │
  │  4. Camera confirms                │
  │  5. Arm deposits in correct bin    │
  └────────────────────────────────────┘
```
