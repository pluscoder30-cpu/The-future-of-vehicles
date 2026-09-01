# PHI_FIELD_ROBOT — Mechanical Design

## PHI_FIELD_ROBOT | Document 03: Mechanical Design

---

## 1. OVERALL DIMENSIONS

```
┌─────────────────────────────────────────────────────────────┐
│                PHI_FIELD_ROBOT — TOP VIEW                    │
│                                                              │
│            400mm (15.75 in)                                   │
│  ◄─────────────────────────────────────────────►            │
│                                                              │
│  ┌─────────────────────────────────────────────┐  ▲        │
│  │                                             │  │        │
│  │   ┌─────┐                     ┌─────┐      │  │        │
│  │   │ FL  │                     │ FR  │      │  │        │
│  │   │LEG  │     MAIN BODY      │LEG  │      │  200mm    │
│  │   │     │                     │     │      │  (7.87in) │
│  │   └─────┘                     └─────┘      │  │        │
│  │                                             │  │        │
│  │   ┌─────┐    ┌───────────┐    ┌─────┐      │  │        │
│  │   │ ARM │    │   BATTERY  │    │LIDAR│      │  │        │
│  │   │ MNT │    │   BAY #1   │    │     │      │  │        │
│  │   │     │    └───────────┘    │     │      │  │        │
│  │   └─────┘    ┌───────────┐    └─────┘      │  │        │
│  │              │   BATTERY  │                  │  │        │
│  │              │   BAY #2   │                  │  │        │
│  │              └───────────┘                  │  │        │
│  │                                             │  │        │
│  │   ┌─────┐                     ┌─────┐      │  │        │
│  │   │ RL  │                     │ RR  │      │  │        │
│  │   │LEG  │                     │LEG  │      │  │        │
│  │   │     │                     │     │      │  │        │
│  │   └─────┘                     └─────┘      │  ▼        │
│  └─────────────────────────────────────────────┘          │
│                                                              │
│  Total Height (standing): 600mm (23.6 in)                   │
│  Ground Clearance: 150mm (5.9 in)                           │
└─────────────────────────────────────────────────────────────┘
```

### 1.1 Dimension Summary

| Dimension | Value | Notes |
|-----------|-------|-------|
| Total Length | 400 mm (15.75 in) | Front to rear |
| Total Width | 200 mm (7.87 in) | Side to side |
| Total Height | 600 mm (23.6 in) | Ground to back panel |
| Ground Clearance | 150 mm (5.9 in) | Minimum under body |
| Leg Span (walking) | 300 mm (11.8 in) | Per leg, fully extended |
| Arm Reach | 500 mm (19.7 in) | Shoulder to gripper tip |
| Battery Bay | 350×150×100 mm | Each bay |

---

## 2. MAIN BODY FRAME

### 2.1 Frame Construction

```
┌─────────────────────────────────────────────────────────────┐
│                 MAIN BODY — CROSS SECTION (A-A)              │
│                                                              │
│     ┌─────────────────────────────────────────────┐         │
│     │              TOP PLATE (4mm)                 │         │
│     │  ┌─────────────────────────────────────┐    │         │
│     │  │         ELECTRONICS BAY              │    │         │
│     │  │  • Main PCB (120×80mm)              │    │         │
│     │  │  • Raspberry Pi 5                    │    │         │
│     │  │  • Coral TPU                        │    │         │
│     │  │  • USB Hub                          │    │         │
│     │  │  • NVMe SSD                         │    │         │
│     │  └─────────────────────────────────────┘    │         │
│     ├─────────────────────────────────────────────┤         │
│     │         BATTERY BAY #1 (front)              │         │
│     │  ┌─────────────────────────────────────┐    │         │
│     │  │         FPB-10 Battery              │    │         │
│     │  │         350×150×100mm               │    │         │
│     │  └─────────────────────────────────────┘    │         │
│     ├─────────────────────────────────────────────┤         │
│     │         BATTERY BAY #2 (rear)               │         │
│     │  ┌─────────────────────────────────────┐    │         │
│     │  │         FPB-10 Battery              │    │         │
│     │  │         350×150×100mm               │    │         │
│     │  └─────────────────────────────────────┘    │         │
│     └─────────────────────────────────────────────┘         │
│              BOTTOM PLATE (4mm)                             │
│                                                              │
│  Wall Thickness: 3mm (sides), 4mm (top/bottom)             │
│  Material: 6061-T6 Aluminum                                 │
│  Finish: Hard anodized, MIL-A-8625 Type III                 │
│  Weight: 1.2 kg (frame only)                                │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Frame Material Specification

| Property | Value |
|----------|-------|
| Material | 6061-T6 Aluminum Alloy |
| Yield Strength | 276 MPa |
| Ultimate Tensile Strength | 310 MPa |
| Elastic Modulus | 68.9 GPa |
| Density | 2.70 g/cm³ |
| Hardness | 95 HB (Brinell) |
| Thermal Conductivity | 167 W/m·K |
| Corrosion Resistance | Good (anodized) |
| Machinability | Excellent |
| Weldability | Good (TIG) |

### 2.3 Frame Features

**Mounting Points:**
- 4× Leg mounts (M4 threaded, steel inserts)
- 1× Arm mount (M4×4 threaded, steel inserts)
- 4× Electronics standoffs (M3×6, brass)
- 8× Battery bay rail guides (aluminum)
- 2× LIDAR mount (M3×3, aluminum bracket)
- 4× Camera mounts (M2.5×4, aluminum bracket)
- 2× Emergency stop button (M16 panel cutout)

**Cable Routing:**
- 4× Side cable channels (10mm × 5mm)
- 2× Bottom cable channels (8mm × 4mm)
- 8× Cable tie mounts (adhesive backed)

**Ventilation:**
- 12× Ventilation holes (8mm diameter) on top plate
- Filtered intake on side panel
- Exhaust fan mount on rear panel

---

## 3. LEG DESIGN

### 3.1 Leg Geometry

```
┌─────────────────────────────────────────────────────────────┐
│                    SINGLE LEG — SIDE VIEW                     │
│                                                              │
│                    HIP YAW JOINT                             │
│                         ●                                    │
│                        /│\                                   │
│                       / │ \                                  │
│                      /  │  \                                 │
│                     /   │   \                                │
│                    /    │    \                               │
│                   /     │     \                              │
│           ┌──────┐      │      ┌──────┐                     │
│           │      │      │      │      │                     │
│           │ HIP  │◄─────┤      │ HIP  │                     │
│           │ YAW  │      │      │ PITCH│                     │
│           │MOTOR │      │      │MOTOR │                     │
│           │      │      │      │      │                     │
│           └──┬───┘      │      └──┬───┘                     │
│              │           │         │                        │
│              │           │         │                        │
│         ┌────┴────────────┴─────────┴────┐                  │
│         │       UPPER LEG (FEMUR)         │                  │
│         │       200mm length              │                  │
│         │       40mm × 30mm cross section │                  │
│         └─────────────┬──────────────────┘                  │
│                       │                                     │
│                       ● KNEE JOINT                          │
│                       │                                     │
│              ┌────────┴────────┐                            │
│              │    KNEE MOTOR    │                            │
│              │    (M2006 PAP)   │                            │
│              └────────┬────────┘                            │
│                       │                                     │
│              ┌────────┴────────┐                            │
│              │  LOWER LEG      │                            │
│              │  (TIBIA)        │                            │
│              │  250mm length   │                            │
│              │  35mm × 25mm    │                            │
│              └────────┬────────┘                            │
│                       │                                     │
│              ┌────────┴────────┐                            │
│              │    FOOT PAD      │                            │
│              │    Ø60mm         │                            │
│              │    60A silicone  │                            │
│              │    FSR embedded  │                            │
│              └─────────────────┘                            │
│                                                              │
│  Joint Angles:                                               │
│  • Hip Yaw: ±45° (90° total range)                         │
│  • Hip Pitch: -30° to +90° (120° range)                    │
│  • Knee: 0° to +135° (135° range)                          │
│                                                              │
│  Leg Reach:                                                  │
│  • Maximum extension: 450mm from body                      │
│  • Minimum retraction: 100mm from body                     │
│  • Step height: 150mm                                       │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Joint Specifications

**Hip Yaw Joint:**

| Parameter | Value |
|-----------|-------|
| Range of Motion | ±45° (90° total) |
| Max Torque | 3.0 N·m |
| Continuous Torque | 1.0 N·m |
| Gear Ratio | 1:1 (direct drive) |
| Bearing | 2× flanged ball bearing (8mm bore) |
| Encoder | 14-bit absolute (16,384 CPR) |
| Angular Resolution | 0.022° |
| Max Speed | 460 RPM (4385°/s) |
| Stiffness | 50 N·m/rad |

**Hip Pitch Joint:**

| Parameter | Value |
|-----------|-------|
| Range of Motion | -30° to +90° (120° total) |
| Max Torque | 3.0 N·m |
| Continuous Torque | 1.0 N·m |
| Gear Ratio | 1:1 (direct drive) |
| Bearing | 2× flanged ball bearing (8mm bore) |
| Encoder | 14-bit absolute (16,384 CPR) |
| Angular Resolution | 0.022° |
| Max Speed | 460 RPM (4385°/s) |
| Stiffness | 50 N·m/rad |

**Knee Joint:**

| Parameter | Value |
|-----------|-------|
| Range of Motion | 0° to +135° (135° total) |
| Max Torque | 3.0 N·m |
| Continuous Torque | 1.0 N·m |
| Gear Ratio | 1:1 (direct drive) |
| Bearing | 2× flanged ball bearing (8mm bore) |
| Encoder | 14-bit absolute (16,384 CPR) |
| Angular Resolution | 0.022° |
| Max Speed | 460 RPM (4385°/s) |
| Stiffness | 50 N·m/rad |

### 3.3 Leg Kinematics

**Forward Kinematics (FK):**

Given joint angles (θ₁, θ₂, θ₃):
- θ₁ = Hip yaw angle
- θ₂ = Hip pitch angle
- θ₃ = Knee angle

```
x = L₂·cos(θ₂) + L₃·cos(θ₂ + θ₃)
y = L₁·sin(θ₁)
z = -L₂·sin(θ₂) - L₃·sin(θ₂ + θ₃)
```

Where:
- L₁ = 50mm (hip yaw offset)
- L₂ = 200mm (femur length)
- L₃ = 250mm (tibia length)

**Inverse Kinematics (IK):**

```
θ₁ = atan2(y, x)
r = sqrt(x² + y²) - L₁
s = z
D = (r² + s² - L₂² - L₃²) / (2·L₂·L₃)
θ₃ = atan2(√(1-D²), D)
θ₂ = atan2(s, r) - atan2(L₃·sin(θ₃), L₂ + L₃·cos(θ₃))
```

### 3.4 Leg Workspace

```
┌─────────────────────────────────────────────────────────────┐
│              LEG WORKSPACE — SIDE VIEW (X-Z plane)          │
│                                                              │
│                        Z (up)                                │
│                        ▲                                    │
│           450mm ───────┤                                    │
│                        │                                    │
│           300mm ───────┤         ╭───────╮                  │
│                        │        ╱         ╲                 │
│           150mm ───────┤───────╱───────────╲────────        │
│                        │      ╱  REACHABLE  ╲              │
│             0mm ───────┤─────╱───WORKSPACE──╲───────       │
│                        │    ╱                ╲              │
│          -150mm ───────┤   ╱                  ╲             │
│                        │  ╱                    ╲            │
│          -300mm ───────┤ ╱                      ╲           │
│                        │╱                        ╲          │
│          -450mm ───────┤                          ╲         │
│                        │                                    │
│                        └──────────────────────────────►     │
│                       -300  -150   0   150   300  450      │
│                                         X (forward)         │
│                                                              │
│  Workspace Volume: ~0.025 m³ per leg                        │
│  Total Robot Workspace: ~0.1 m³ (4 legs + arm)             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. ARM DESIGN

### 4.1 Arm Geometry

```
┌─────────────────────────────────────────────────────────────┐
│                    5-DOF ARM — SIDE VIEW                      │
│                                                              │
│         BODY FRAME                                           │
│         ┌──────────┐                                        │
│         │          │                                        │
│         │  SHOULDER │                                        │
│         │  MOUNT    │                                        │
│         │          │                                        │
│         └────┬─────┘                                        │
│              │                                               │
│         ┌────┴─────┐  SHOULDER PITCH                        │
│         │ SHOULDER  │  (Motor 0x10)                         │
│         │ PITCH     │  Range: 0° to 180°                    │
│         │ MOTOR     │  Torque: 1.0 N·m cont.               │
│         └────┬──────┘                                        │
│              │                                               │
│         ┌────┴─────┐  SHOULDER ROLL                         │
│         │ SHOULDER  │  (Motor 0x11)                         │
│         │ ROLL      │  Range: ±90°                          │
│         │ MOTOR     │  Torque: 1.0 N·m cont.               │
│         └────┬──────┘                                        │
│              │                                               │
│    ┌─────────┴──────────┐  UPPER ARM                        │
│    │    UPPER ARM LINK   │  200mm length                    │
│    │    (30×25mm tube)   │  60g weight                      │
│    └─────────┬──────────┘                                    │
│              │                                               │
│         ┌────┴─────┐  ELBOW PITCH                           │
│         │  ELBOW    │  (Motor 0x12)                         │
│         │  PITCH    │  Range: 0° to 150°                    │
│         │  MOTOR    │  Torque: 1.0 N·m cont.               │
│         └────┬──────┘                                        │
│              │                                               │
│    ┌─────────┴──────────┐  LOWER ARM                        │
│    │    LOWER ARM LINK   │  200mm length                    │
│    │    (25×20mm tube)   │  45g weight                      │
│    └─────────┬──────────┘                                    │
│              │                                               │
│         ┌────┴─────┐  WRIST PITCH                           │
│         │  WRIST    │  (Motor 0x13)                         │
│         │  PITCH    │  Range: ±90°                          │
│         │  MOTOR    │  Torque: 1.0 N·m cont.               │
│         └────┬──────┘                                        │
│              │                                               │
│    ┌─────────┴──────────┐                                    │
│    │  FORCE-TORQUE      │  6-axis sensor                    │
│    │  SENSOR            │  ±50N, ±5 N·m                    │
│    └─────────┬──────────┘                                    │
│              │                                               │
│    ┌─────────┴──────────┐                                    │
│    │    GRIPPER          │  (Motor 0x14)                     │
│    │    Parallel jaws    │  80mm max opening                 │
│    │    Silicone pads    │  20N max grip force              │
│    └────────────────────┘                                    │
│                                                              │
│  Total Arm Length: 500mm (shoulder to gripper tip)          │
│  Total Arm Weight: 0.75 kg                                  │
│  Payload Capacity: 10 kg (at full extension)                │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Arm Joint Specifications

| Joint | Range | Max Torque | Speed | Weight |
|-------|-------|-----------|-------|--------|
| Shoulder Pitch | 0°-180° | 1.0 N·m | 460 RPM | 156g |
| Shoulder Roll | ±90° | 1.0 N·m | 460 RPM | 156g |
| Elbow Pitch | 0°-150° | 1.0 N·m | 460 RPM | 156g |
| Wrist Pitch | ±90° | 1.0 N·m | 460 RPM | 156g |
| Gripper | 0-80mm | 1.0 N·m | 460 RPM | 156g |

### 4.3 Arm Workspace

```
┌─────────────────────────────────────────────────────────────┐
│              ARM WORKSPACE — SIDE VIEW                        │
│                                                              │
│                        ▲ Z                                   │
│                        │                                    │
│         500mm ─────────┤                                    │
│                        │                                    │
│         400mm ─────────┤                                    │
│                        │                                    │
│         300mm ─────────┤    ╭──────╮                       │
│                        │   ╱        ╲                      │
│         200mm ─────────┤──╱──────────╲──                   │
│                        │ ╱  REACHABLE  ╲                  │
│         100mm ─────────┤╱──WORKSPACE───╲──                │
│                        ╱                 ╲                 │
│            0mm ───────╱───────────────────╲──────► X       │
│                     ╱                     ╲                 │
│         -100mm ────╱                       ╲──             │
│                        │                                    │
│                        │                                    │
│                        └──────────────────────────────►     │
│                       -200  -100   0   100  200  300  400  │
│                                          X (forward)        │
│                                                              │
│  Workspace Envelope: ~0.08 m³                               │
│  Reachable Radius: 500mm max                               │
│  Minimum Reach: 100mm (fully retracted)                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. FOOT DESIGN

### 5.1 Foot Pad Detail

```
┌─────────────────────────────────────────────────────────────┐
│                    FOOT PAD — CROSS SECTION                   │
│                                                              │
│              ┌─────────────────────┐                        │
│              │  TIBIA ATTACHMENT    │                        │
│              │  M4×8 bolt          │                        │
│              │  (aluminum bracket) │                        │
│              └──────────┬──────────┘                        │
│                         │                                   │
│              ┌──────────┴──────────┐                        │
│              │   ALUMINUM PLATE     │                        │
│              │   Ø60mm × 3mm       │                        │
│              │   (6061-T6)         │                        │
│              └──────────┬──────────┘                        │
│                         │                                   │
│              ┌──────────┴──────────┐                        │
│              │   SILICONE RUBBER    │                        │
│              │   Ø60mm × 12mm      │                        │
│              │   60A Shore durometer│                        │
│              │                      │                        │
│              │   ┌──────────────┐  │                        │
│              │   │  FSR 402     │  │                        │
│              │   │  (center)    │  │                        │
│              │   └──────────────┘  │                        │
│              │                      │                        │
│              │   ┌──────────────┐  │                        │
│              │   │  TREAD       │  │                        │
│              │   │  PATTERN     │  │                        │
│              │   │  (waffle)    │  │                        │
│              │   └──────────────┘  │                        │
│              └─────────────────────┘                        │
│                                                              │
│  Tread Pattern: Waffle (10×10 grid, 4mm squares)           │
│  Grip Coefficient: μ = 0.8 (concrete), 0.6 (mud)          │
│  FSR Accuracy: ±0.1N                                        │
│  Weight: 45g per foot                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. ARM MOUNT INTERFACE

### 6.1 Shoulder Mount

```
┌─────────────────────────────────────────────────────────────┐
│                    SHOULDER MOUNT — TOP VIEW                  │
│                                                              │
│         ┌─────────────────────────┐                         │
│         │     BODY FRAME TOP      │                         │
│         │                         │                         │
│         │   ┌─────────────────┐   │                         │
│         │   │  SHOULDER MOUNT  │   │                         │
│         │   │  PLATE           │   │                         │
│         │   │  (80×80×5mm)    │   │                         │
│         │   │  6061-T6 Al      │   │                         │
│         │   │                  │   │                         │
│         │   │  ┌──┐  ┌──┐    │   │                         │
│         │   │  │●│  │●│    │   │  ● = M4 mounting bolt    │
│         │   │  └──┘  └──┘    │   │                         │
│         │   │                  │   │                         │
│         │   │  ┌──────────┐   │   │                         │
│         │   │  │  BEARING  │   │   │                         │
│         │   │  │  SADDLE   │   │   │                         │
│         │   │  │  Ø40mm    │   │   │                         │
│         │   │  └──────────┘   │   │                         │
│         │   │                  │   │                         │
│         │   │  ┌──┐  ┌──┐    │   │                         │
│         │   │  │●│  │●│    │   │                         │
│         │   │  └──┘  └──┘    │   │                         │
│         │   └─────────────────┘   │                         │
│         │                         │                         │
│         └─────────────────────────┘                         │
│                                                              │
│  Mounting: 4× M4×8 bolts into steel inserts                │
│  Load Rating: 50 kg static, 25 kg dynamic                  │
│  Bearing: 1× 608ZZ (8mm bore, 22mm OD)                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. LIDAR MOUNT

### 7.1 LIDAR Bracket

```
┌─────────────────────────────────────────────────────────────┐
│                    LIDAR MOUNT — SIDE VIEW                    │
│                                                              │
│         BODY FRAME (rear panel)                              │
│         ┌──────────────────┐                                │
│         │                  │                                │
│         │   ┌────────────┐ │                                │
│         │   │ LIDAR BRACKET│ │                                │
│         │   │ (3mm Al)    │ │                                │
│         │   │             │ │                                │
│         │   │  ┌───────┐  │ │                                │
│         │   │  │RPLIDAR│  │ │                                │
│         │   │  │ A1M8  │  │ │                                │
│         │   │  │       │  │ │                                │
│         │   │  │ Ø97mm │  │ │                                │
│         │   │  │       │  │ │                                │
│         │   │  └───────┘  │ │                                │
│         │   │             │ │                                │
│         │   └────────────┘ │                                │
│         │                  │                                │
│         └──────────────────┘                                │
│                                                              │
│  Mounting: 3× M3×4 bolts                                   │
│  Height: 20mm above body top                               │
│  Cable routing: Through body frame to main PCB             │
│  Protection: Clear polycarbonate dome (optional)           │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. CAMERA MOUNTS

### 8.1 Camera Positioning

```
┌─────────────────────────────────────────────────────────────┐
│              CAMERA POSITIONS — TOP VIEW                      │
│                                                              │
│              ┌─────────────────────────┐                    │
│              │                         │                    │
│              │    ┌──┐          ┌──┐   │                    │
│              │    │C1│          │C2│   │  C1 = Front camera │
│              │    └──┘          └──┘   │  C2 = Left camera  │
│              │                         │                    │
│              │         BODY            │                    │
│              │                         │                    │
│              │    ┌──┐          ┌──┐   │                    │
│              │    │C3│          │C4│   │  C3 = Right camera │
│              │    └──┘          └──┘   │  C4 = Rear camera  │
│              │                         │                    │
│              └─────────────────────────┘                    │
│                                                              │
│  Camera FOV: 79° each                                       │
│  Overlap: ~10° between adjacent cameras                    │
│  Coverage: 360° horizontal                                  │
│  Mounting: M2.5×4 bolts, aluminum brackets                 │
│  Cable routing: FFC through body frame                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. BATTERY MOUNTING

### 9.1 Battery Bay Detail

```
┌─────────────────────────────────────────────────────────────┐
│                 BATTERY BAY — CROSS SECTION                   │
│                                                              │
│         ┌─────────────────────────────┐                     │
│         │       BATTERY BAY COVER      │                     │
│         │       (quick-release)        │                     │
│         └──────────┬──────────────────┘                     │
│                    │                                        │
│         ┌──────────┴──────────────────┐                     │
│         │                              │                     │
│         │   ┌──────────────────────┐   │                     │
│         │   │     RAIL GUIDE (×4)   │   │                     │
│         │   │     (aluminum)        │   │                     │
│         │   └──────────────────────┘   │                     │
│         │                              │                     │
│         │   ┌──────────────────────┐   │                     │
│         │   │     FPB-10 BATTERY   │   │                     │
│         │   │     350×150×100mm     │   │                     │
│         │   │     48V / 10 kWh     │   │                     │
│         │   │     8.3 kg           │   │                     │
│         │   └──────────────────────┘   │                     │
│         │                              │                     │
│         │   ┌──────────────────────┐   │                     │
│         │   │     CONNECTOR BLOCK   │   │                     │
│         │   │     XT90 (power)      │   │                     │
│         │   │     XT30 (data/BMS)   │   │                     │
│         │   └──────────────────────┘   │                     │
│         │                              │                     │
│         └──────────────────────────────┘                     │
│                                                              │
│  Mounting: 4× rail guides (friction fit)                   │
│  Securing: 2× spring-loaded latches                        │
│  Hot-swap: Yes (with BMS communication)                    │
│  Eject: Push latch, slide out                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 10. THERMAL MANAGEMENT

### 10.1 Airflow Path

```
┌─────────────────────────────────────────────────────────────┐
│              THERMAL MANAGEMENT — SIDE VIEW                   │
│                                                              │
│         COOL AIR IN (filtered)                              │
│         ▼                                                   │
│    ┌────────┐     ┌────────────┐     ┌────────┐             │
│    │ INTAKE │────►│ ELECTRONICS │────►│ EXHAUST│             │
│    │ FILTER │     │   BAY       │     │ FAN    │             │
│    │        │     │             │     │        │             │
│    │ 8mm    │     │ • Pi 5     │     │ 40mm   │             │
│    │ holes  │     │ • Coral    │     │ 5V PWM │             │
│    │        │     │ • Main PCB │     │ 7.5CFM │             │
│    │        │     │ • NVMe     │     │        │             │
│    └────────┘     └────────────┘     └────────┘             │
│                                                              │
│  Airflow Rate: 7.5 CFM (fan on full)                       │
│  Air Changes: ~50 per minute                               │
│  Max Internal Temp: 45°C (Pi throttles at 80°C)           │
│  Ambient Temp Range: -10°C to 45°C                         │
│                                                              │
│  Heat Sources:                                               │
│  • Raspberry Pi 5: 5-12W (depending on load)               │
│  • Coral TPU: 2W                                            │
│  • Main PCB: 5W                                             │
│  • NVMe SSD: 3W                                             │
│  • DC-DC converters: 10W (at 95% efficiency)               │
│  • Total: ~25W max                                          │
│                                                              │
│  Cooling Capacity:                                           │
│  • Heatsink: 2.5°C/W × 25W = 62.5°C rise (fan off)       │
│  • Fan active: ~10°C rise above ambient                    │
│  • Thermal paste: 12.5 W/mK (Pi to heatsink)              │
└─────────────────────────────────────────────────────────────┘
```

---

## 11. MATERIALS SUMMARY

| Component | Material | Weight | Qty | Total Weight |
|-----------|----------|--------|-----|--------------|
| Main Frame | 6061-T6 Al | 1200g | 1 | 1200g |
| Femurs | 6061-T6 Al | 85g | 4 | 340g |
| Tibias | 6061-T6 Al | 70g | 4 | 280g |
| Foot Pads | Silicone + Al | 45g | 4 | 180g |
| Arm Links | 6061-T6 Al | 105g | 2 | 210g |
| Gripper | Al + Silicone | 80g | 1 | 80g |
| Heatsink | 6061-T6 Al | 80g | 1 | 80g |
| Battery Covers | 6061-T6 Al | 150g | 2 | 300g |
| Electronics Cover | 6061-T6 Al | 80g | 1 | 80g |
| Mounting Brackets | 6061-T6 Al | 30g | 6 | 180g |
| **Structural Total** | | | | **3.03 kg** |

---

## 12. WEIGHT BUDGET

| Category | Weight |
|----------|--------|
| Structural (frame, links, brackets) | 3.03 kg |
| Motors (17× M2006 PAP) | 2.65 kg |
| Batteries (2× FPB-10) | 16.6 kg |
| Electronics (Pi, Coral, PCB, sensors) | 0.8 kg |
| Wiring & Connectors | 0.5 kg |
| Fasteners & Misc | 0.42 kg |
| **Total** | **24.0 kg** |
| **Margin (for cables, ties, gaskets)** | **6.0 kg** |
| **Total with Margin** | **30.0 kg** |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
