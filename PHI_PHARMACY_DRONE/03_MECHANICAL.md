# PHI Pharmacy Drone — MECHANICAL DIAGRAM
## Buildable Documentation | Physical Layout & Assembly

---

## EXPLODED VIEW (Top-Down)

```
                    PHI PHARMACY DRONE
                   EXPLODED VIEW (TOP-DOWN)

                    ┌─────────────────────────────────────────┐
                    │              TOP SHELL                    │
                    │         Carbon fiber fairing             │
                    │         IP54 sealed                      │
                    │         800mm x 800mm                    │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         PROPULSION LAYER                 │
                    │    ┌─────────────────────────────┐      │
                    │    │   4x T-Motor F40 Pro II     │      │
                    │    │   750W, 2450KV each          │      │
                    │    │   10-inch folding props     │      │
                    │    └─────────────────────────────┘      │
                    │              100mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         AVIONICS BAY                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   Pixhawk 6C Flight Ctrl    │      │
                    │    │   Safety Processor STM32F4  │      │
                    │    │   LiDAR + Cameras + GPS     │      │
                    │    └─────────────────────────────┘      │
                    │              80mm tall                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         MEDICATION STORAGE               │
                    │    ┌─────────────────────────────┐      │
                    │    │   REFRIGERATED ZONE (2-8C)   │      │
                    │    │   14 slots, Peltier cooled   │      │
                    │    │   RFID per slot              │      │
                    │    └─────────────────────────────┘      │
                    │    ┌─────────────────────────────┐      │
                    │    │   AMBIENT ZONE (15-25C)     │      │
                    │    │   6 slots, heated            │      │
                    │    │   RFID per slot              │      │
                    │    └─────────────────────────────┘      │
                    │              200mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         DISPENSING ARM                    │
                    │    ┌─────────────────────────────┐      │
                    │    │   4-DOF Robotic Arm          │      │
                    │    │   30cm reach, 500g payload   │      │
                    │    │   Force-sensing gripper      │      │
                    │    │   Barcode verification       │      │
                    │    └─────────────────────────────┘      │
                    │              150mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         POWER SYSTEM                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   FPB-5 Battery              │      │
                    │    │   5kWh, 25.6V                │      │
                    │    └─────────────────────────────┘      │
                    │              100mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         BOTTOM SHELL                     │
                    │         Carbon fiber, IP54              │
                    │         Landing skids                   │
                    │         800mm x 800mm                    │
                    └─────────────────────────────────────────┘

    TOTAL LENGTH: 800mm
    TOTAL WIDTH: 800mm
    TOTAL HEIGHT: 400mm
```

---

## TOP VIEW WITH DIMENSIONS

```
                    TOP VIEW (Plan Form)

                    ┌─────────────────────────────────────────────┐
                    │                                             │
                    │              800mm                           │
                    │◄───────────────────────────────────────────►│
                    │                                             │
                    │    ┌───┐                         ┌───┐     │ ▲
                    │    │M1 │                         │M2 │     │ │
                    │    └───┘                         └───┘     │ │
                    │      │                           │         │ │
                    │      │     ┌───────────────┐     │         │ │
                    │      │     │   FLIGHT      │     │         │ 800mm
                    │      │     │   CONTROLLER  │     │         │ │
                    │      │     └───────────────┘     │         │ │
                    │      │                           │         │ │
                    │    ┌───┐   ┌───────────────┐   ┌───┐     │ │
                    │    │M4 │───│   MEDICATION   │───│M3 │     │ │
                    │    └───┘   │   STORAGE     │   └───┘     │ ▼
                    │            │   (20 slots)   │
                    │            └───────────────┘
                    │            ┌───────────────┐
                    │            │   DISPENSING   │
                    │            │   ARM (4-DOF)  │
                    │            └───────────────┘
                    │            ┌───────────────┐
                    │            │   POWER SYS   │
                    │            │   FPB-5       │
                    │            └───────────────┘
                    │                                             │
                    └─────────────────────────────────────────────┘

                    800mm width
                    ◄───────────────────────────────────────────►

    MOTOR POSITIONS (4x quadcopter):
    - M1: Front-Left
    - M2: Front-Right
    - M3: Rear-Right
    - M4: Rear-Left
    - Spacing: 90° intervals on 800mm circle
```

---

## SIDE CROSS-SECTION

```
    SIDE VIEW (Cross-Section)

    ◄──────────── 800mm (width) ────────────►

    ▲
    │   ┌─────────────────────────────────────────────┐
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Top Shell
    │   │░░░░░░░░░░░ Carbon fiber, IP54 ░░░░░░░░░░░░░│ (2mm)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌───┐ ┌─────────────────────┐ ┌───┐       │
    │   │ │M1 │ │    ROTOR AREA       │ │M2 │       │ Propulsion
    │   │ └───┘ │    10-inch props    │ └───┘       │ (750W each)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         AVIONICS BAY                     │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Flight Controller         │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    REFRIGERATED ZONE (2-8C)             │ │
    │   │ │    ┌───┬───┬───┬───┬───┬───┬───┐       │ │
    │   │ │    │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │       │ │ 14 slots
    │   │ │    ├───┼───┼───┼───┼───┼───┼───┤       │ │ Peltier cooled
    │   │ │    │ 8 │ 9 │10 │11 │12 │13 │14 │       │ │ RFID per slot
    │   │ │    └───┴───┴───┴───┴───┴───┴───┘       │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Peltier Modules (2x)       │      │ │ 60W total
    │   │ │    └─────────────────────────────┘      │ │
    │   │ ├─────────────────────────────────────────┤ │
    │   │ │    AMBIENT ZONE (15-25C)                │ │
    │   │ │    ┌───┬───┬───┬───┬───┐               │ │ 6 slots
    │   │ │    │15 │16 │17 │18 │19 │20              │ │ Heated
    │   │ │    └───┴───┴───┴───┴───┘               │ │ RFID per slot
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Ambient Heater (20W)       │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    DISPENSING ARM                        │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   4-DOF Robotic Arm          │      │ │ 30cm reach
    │   │ │    │   Force-sensing gripper      │      │ │ 500g payload
    │   │ │    │   Barcode scanner            │      │ │ Verification
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    POWER SYSTEM                          │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   FPB-5 Battery             │      │ │ 5kWh 25.6V
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Bottom Shell
    │   │░░░░░░░░░░░ Carbon fiber, IP54 ░░░░░░░░░░░░░│ (2mm)
    │   │░░░░░░░░░░░ Landing skids ░░░░░░░░░░░░░░░░░░│
    │   └─────────────────────────────────────────────┘
    ▼
         TOTAL HEIGHT: 400mm
```

---

## MEDICATION STORAGE LAYOUT

```
    MEDICATION STORAGE BAY (Top View, Lid Open)

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   ◄──────── 400mm (width) ────────────►     │
    │                                             │
    │   REFRIGERATED ZONE (2-8°C)                 │
    │   ┌───┬───┬───┬───┬───┬───┬───┐           │ ▲
    │   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │           │ │
    │   ├───┼───┼───┼───┼───┼───┼───┤           │ │
    │   │ 8 │ 9 │10 │11 │12 │13 │14 │           │ 300mm
    │   └───┴───┴───┴───┴───┴───┴───┘           │ │
    │   Each slot: 50mm x 50mm x 80mm            │ │
    │   RFID reader per slot                      │ │
    │   Tamper-evident lock per slot              │ ▼
    │                                             │
    │   AMBIENT ZONE (15-25°C)                    │
    │   ┌───┬───┬───┬───┬───┐                   │ ▲
    │   │15 │16 │17 │18 │19 │20                  │ │
    │   └───┴───┴───┴───┴───┘                   │ 100mm
    │   Each slot: 50mm x 50mm x 80mm            │ │
    │   RFID reader per slot                      │ │
    │   Tamper-evident lock per slot              │ ▼
    │                                             │
    │   DISPENSING AREA                           │
    │   ┌─────────────────────────────────────┐   │
    │   │   Barcode Scanner (1D/2D)           │   │
    │   │   Photo Confirmation Camera (5MP)   │   │
    │   │   Delivery chute                    │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    └─────────────────────────────────────────────┘

    SLOT SPECIFICATIONS:
    - Dimensions: 50mm x 50mm x 80mm
    - Capacity: 1 medication bottle/box per slot
    - RFID: 13.56MHz per slot (ISO 15693)
    - Lock: Electromagnetic solenoid (power-off = locked)
    - Audit: Timestamp of every open/close
    - Tamper-evident: Physical seal + electronic log
```

---

## DISPENSING ARM DETAIL

```
    4-DOF DISPENSING ARM (Side View)

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   ARM JOINTS (4x)                           │
    │   ┌─────────────────────────────────────┐   │
    │   │   Joint 1: Base Rotation            │   │
    │   │   Range: 360° continuous            │   │
    │   │   Speed: 120°/s                     │   │
    │   │                                     │   │
    │   │         ┌─────┐                     │   │
    │   │         │ J1  │                     │   │
    │   │         └──┬──┘                     │   │
    │   │            │                         │   │
    │   │   Joint 2: Shoulder                 │   │
    │   │   Range: -90° to +90°              │   │
    │   │   Speed: 90°/s                      │   │
    │   │            │                         │   │
    │   │         ┌──┴──┐                     │   │
    │   │         │ J2  │                     │   │
    │   │         └──┬──┘                     │   │
    │   │            │                         │   │
    │   │   Joint 3: Elbow                    │   │
    │   │   Range: 0° to 135°                │   │
    │   │   Speed: 90°/s                      │   │
    │   │            │                         │   │
    │   │         ┌──┴──┐                     │   │
    │   │         │ J3  │                     │   │
    │   │         └──┬──┘                     │   │
    │   │            │                         │   │
    │   │   Joint 4: Wrist                    │   │
    │   │   Range: -90° to +90°              │   │
    │   │   Speed: 180°/s                     │   │
    │   │            │                         │   │
    │   │         ┌──┴──┐                     │   │
    │   │         │ J4  │                     │   │
    │   │         └──┬──┘                     │   │
    │   │            │                         │   │
    │   │         ┌──┴──┐                     │   │
    │   │         │GRIP │                     │   │
    │   │         └─────┘                     │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   GRIPPER                                   │
    │   ┌─────────────────────────────────────┐   │
    │   │   Type: 2-finger parallel           │   │
    │   │   Force sensor: 0-500g              │   │
    │   │   Grip width: 10-80mm              │   │
    │   │   Speed: 50mm/s                    │   │
    │   │   Barcode scanner: Integrated      │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   REACH: 30cm                               │
    │   PAYLOAD: 500g                             │
    │   ACCURACY: ±1mm                            │
    │                                             │
    └─────────────────────────────────────────────┘
```

---

## ASSEMBLY STACK ORDER

```
    ASSEMBLY SEQUENCE (Bottom to Top)

    STEP 1: Bottom Shell
    ┌─────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Carbon fiber bottom
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Landing skids
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 2: Power System
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   FPB-5 Battery Pack               │ │  5kWh, 25.6V
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 3: Dispensing Arm
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   4-DOF Robotic Arm                │ │  30cm reach
    │ │   Force-sensing gripper            │ │  500g payload
    │ │   Barcode scanner                  │ │  Verification
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 4: Medication Storage
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Refrigerated Zone (2-8°C)        │ │  14 slots
    │ │   Peltier modules (2x)             │ │  RFID per slot
    │ │   Ambient Zone (15-25°C)           │ │  6 slots
    │ │   Ambient heater                   │ │  RFID per slot
    │ │   Tamper-evident locks (20x)       │ │  Electromagnetic
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 5: Avionics Bay
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Pixhawk 6C Flight Controller     │ │  Primary
    │ │   Safety Processor STM32F4         │ │  Independent
    │ │   LiDAR + 2x Cameras + GPS        │ │  Navigation
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 6: Propulsion
    ┌─────────────────────────────────────────┐
    │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
    │ │ M1  │ │ M2  │ │ M3  │ │ M4  │       │  4x T-Motor F40
    │ └─────┘ └─────┘ └─────┘ └─────┘       │  10-inch props
    │ ┌─────────────────────────────────────┐ │
    │ │   45A ESCs (4x)                    │ │  BLHeli_32
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 7: Top Shell
    ┌─────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Carbon fiber top
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  IP54 sealed
    └─────────────────────────────────────────┘
```

---

## DIMENSIONS SUMMARY

| Dimension | Value | Notes |
|-----------|-------|-------|
| Frame Width | 800mm | Quadcopter |
| Frame Depth | 800mm | Quadcopter |
| Total Height | 400mm | All layers |
| Propeller | 10-inch | Carbon fiber folding |
| Storage Slots | 20 | 14 cold + 6 ambient |
| Slot Size | 50 x 50 x 80mm | Per slot |
| Arm Reach | 30cm | 4-DOF |
| Arm Payload | 500g | Force-sensing |
| Weight (empty) | 6kg | Without payload |
| Max Payload | 5kg | Medications |
| IP Rating | IP54 | Dust/splash resistant |

---

## MATERIALS SPECIFICATION

| Component | Material | Grade | Notes |
|-----------|----------|-------|-------|
| Top/Bottom Shell | Carbon Fiber | Aerospace | IP54 sealed |
| Frame | Carbon Fiber | Medical | 6kg total |
| Storage Insulation | Foam | Medical-grade | 25mm thick |
| Dispensing Arm | Aluminum | Anodized | 4-DOF |
| Fasteners | Stainless Steel | 316L | Corrosion-resistant |
| Seals | Silicone | Food-grade | IP54 |

---

**Document**: 03_MECHANICAL.md
**Vehicle**: PHI PHARMACY DRONE
**Status**: BUILDABLE ✓
