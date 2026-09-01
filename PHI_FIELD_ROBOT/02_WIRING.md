# PHI_FIELD_ROBOT — Complete Wiring Diagrams

## PHI_FIELD_ROBOT | Document 02: Wiring

---

## 1. POWER DISTRIBUTION ARCHITECTURE

```
                          ┌─────────────────────┐
                          │  AC MAINS (120/240V) │
                          └──────────┬──────────┘
                                     │
                          ┌──────────┴──────────┐
                          │   48V/10A CHARGER    │
                          │   (58.4V CV max)     │
                          └──────────┬──────────┘
                                     │ XT90
                          ┌──────────┴──────────┐
                          │   CHARGING PORT      │
                          │   (IP67 connector)   │
                          └──────────┬──────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
         ▼                           ▼                           ▼
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│   BATTERY #1     │        │  EMERGENCY STOP  │        │   BATTERY #2     │
│   FPB-10         │◄──────►│  (main contactor)│◄──────►│   FPB-10         │
│   48V / 208Ah    │        │  Solid-state     │        │   48V / 208Ah    │
│   10 kWh         │        │  60V/30A         │        │   10 kWh         │
└────────┬────────┘        └────────┬────────┘        └────────┬────────┘
         │ XT90                     │                          │ XT90
         │                          │                          │
         └──────────────────────────┼──────────────────────────┘
                                    │
                          ┌─────────┴─────────┐
                          │    48V MAIN BUS    │
                          │    (DC link)       │
                          └─────────┬─────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│  48V→24V BUCK     │   │  48V→5V BUCK      │   │  48V→12V BUCK     │
│  360W / 15A       │   │  25W / 5A         │   │  36W / 3A         │
│  95% eff.         │   │  92% eff.         │   │  93% eff.         │
└────────┬──────────┘   └────────┬──────────┘   └────────┬──────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   24V MOTOR      │     │    5V LOGIC      │     │   12V SENSORS    │
│   POWER BUS      │     │    POWER BUS     │     │    POWER BUS     │
│                  │     │                  │     │                  │
│  • 17× BLDC      │     │  • Raspberry Pi  │     │  • LIDAR         │
│    motors        │     │  • Coral TPU     │     │  • Cameras (4×)  │
│  • Motor drivers │     │  • Main PCB      │     │  • GPS           │
│  • CAN bus       │     │  • USB hub       │     │  • LEDs          │
│                  │     │                  │     │  • Fan           │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## 2. CAN BUS TOPOLOGY

```
                              ┌──────────────────┐
                              │   MAIN PCB        │
                              │   (STM32H743)     │
                              │                    │
                              │  CAN1 ────┐       │
                              │  CAN2 ───────┐   │
                              │  CAN3 ──────────┐│
                              └──┬──────┬─────┬──┘
                                 │      │     │
            ┌────────────────────┘      │     └────────────────────┐
            │                           │                          │
            ▼                           ▼                          ▼
   ┌────────────────┐         ┌────────────────┐         ┌────────────────┐
   │  LEG BUS (CAN1) │        │ ARM BUS (CAN2) │        │ SENSOR BUS(CAN3)│
   │                  │        │                  │        │                  │
   │  1 Mbps          │        │  1 Mbps          │        │  1 Mbps          │
   │  120Ω term       │        │  120Ω term       │        │  120Ω term       │
   │  both ends       │        │  both ends       │        │  both ends       │
   └───┬──┬──┬──┬────┘        └──┬──┬──┬──┬────┘        └──┬──┬──┬──┬────┘
       │  │  │  │                 │  │  │  │                 │  │  │  │
       │  │  │  │                 │  │  │  │                 │  │  │  │
       ▼  ▼  ▼  ▼                 ▼  ▼  ▼  ▼                 ▼  ▼  ▼  ▼
      FL  FR  RL  RR            SHP SHR ELB WRS            LID GPS IMU  ADC
      └───┘   └───┘              └───┘   └───┘              └───┘   └───┘
       │  │    │  │                │  │    │  │                │  │    │  │
       │  │    │  │                │  │    │  │                │  │    │  │
      HYP HPP  HYP HPP           SHP SHR  ELB WRS           LID GPS IMU ADC
       │  │    │  │                │  │    │  │                │  │    │  │
       ▼  ▼    ▼  ▼                ▼  ▼    ▼  ▼                ▼  ▼    ▼  ▼
      KN  KN  KN  KN              GR      ────              ────  ──── ────

   LEG IDENTIFIERS:                  ARM IDENTIFIERS:
   FL = Front Left                   SHP = Shoulder Pitch
   FR = Front Right                  SHR = Shoulder Roll
   RL = Rear Left                    ELB = Elbow Pitch
   RR = Rear Right                   WRS = Wrist Pitch
   HYP = Hip Yaw                     GR  = Gripper
   HPP = Hip Pitch
   KN  = Knee
```

### 2.1 CAN Bus Termination

| Bus | Termination Resistors | Value | Location |
|-----|----------------------|-------|----------|
| CAN1 (Legs) | 2× | 120Ω ±1% | Main PCB + last motor daisy-chain |
| CAN2 (Arm) | 2× | 120Ω ±1% | Main PCB + gripper motor |
| CAN3 (Sensors) | 2× | 120Ω ±1% | Main PCB + ADC module |

### 2.2 CAN Bus Cable Specification

| Parameter | Value |
|-----------|-------|
| Cable Type | Shielded twisted pair |
| Conductor | 24 AWG tinned copper |
| Impedance | 120Ω ±10% |
| Shield | Bare copper braid, >85% coverage |
| Jacket | PVC, 3.0mm OD |
| Max Length | 1m per segment |
| Connector | JST-GH 4-pin (CAN_H, CAN_L, GND, SHIELD) |

---

## 3. LEG MOTOR WIRING (4 LEGS × 3 MOTORS = 12 MOTORS)

### 3.1 Single Leg Wiring Detail (Example: Front Left)

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONT LEFT LEG                           │
│                                                              │
│  ┌──────────────┐                                            │
│  │  HIP YAW     │  CAN: ID 0x01                              │
│  │  MOTOR       │  Connector: JST-GH 4-pin                  │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │ JST-GH 4-pin                                       │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  HIP PITCH   │  CAN: ID 0x02                              │
│  │  MOTOR       │  Connector: JST-GH 4-pin                  │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │ JST-GH 4-pin                                       │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  KNEE         │  CAN: ID 0x03                             │
│  │  MOTOR       │  Connector: JST-GH 4-pin                  │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │ JST-GH 4-pin                                       │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  FSR SENSOR   │  Analog: 0-3.3V                          │
│  │  (foot pad)   │  Connector: JST-GH 3-pin                 │
│  │              │  Pin 1: FSR_OUT (yellow)                   │
│  │  FSR 402     │  Pin 2: FSR_REF (orange)                  │
│  │              │  Pin 3: GND (black)                        │
│  └──────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 CAN ID Assignment Table

| Motor | CAN ID | Bus | Description |
|-------|--------|-----|-------------|
| FL_HIP_YAW | 0x01 | CAN1 | Front Left Hip Yaw |
| FL_HIP_PIT | 0x02 | CAN1 | Front Left Hip Pitch |
| FL_KNEE | 0x03 | CAN1 | Front Left Knee |
| FR_HIP_YAW | 0x04 | CAN1 | Front Right Hip Yaw |
| FR_HIP_PIT | 0x05 | CAN1 | Front Right Hip Pitch |
| FR_KNEE | 0x06 | CAN1 | Front Right Knee |
| RL_HIP_YAW | 0x07 | CAN1 | Rear Left Hip Yaw |
| RL_HIP_PIT | 0x08 | CAN1 | Rear Left Hip Pitch |
| RL_KNEE | 0x09 | CAN1 | Rear Left Knee |
| RR_HIP_YAW | 0x0A | CAN1 | Rear Right Hip Yaw |
| RR_HIP_PIT | 0x0B | CAN1 | Rear Right Hip Pitch |
| RR_KNEE | 0x0C | CAN1 | Rear Right Knee |
| ARM_SHP | 0x10 | CAN2 | Arm Shoulder Pitch |
| ARM_SHR | 0x11 | CAN2 | Arm Shoulder Roll |
| ARM_ELB | 0x12 | CAN2 | Arm Elbow Pitch |
| ARM_WRS | 0x13 | CAN2 | Arm Wrist Pitch |
| ARM_GRP | 0x14 | CAN2 | Arm Gripper |

### 3.3 Motor Power Wiring (per motor)

| Pin | Color | Function | Current |
|-----|-------|----------|---------|
| 1 | Red | +24V Motor Power | 4.2A (continuous) |
| 2 | Black | GND Motor Power | 4.2A (continuous) |
| 3 | Green | CAN_H | 1mA |
| 4 | White | CAN_L | 1mA |

**Power Distribution (24V Bus):**

```
24V MAIN BUS (15A max)
    │
    ├── FL_HIP_YAW (0x01)    ── 24AWG, 200mm
    ├── FL_HIP_PIT (0x02)    ── 24AWG, 180mm
    ├── FL_KNEE (0x03)       ── 24AWG, 250mm
    ├── FR_HIP_YAW (0x04)    ── 24AWG, 200mm
    ├── FR_HIP_PIT (0x05)    ── 24AWG, 180mm
    ├── FR_KNEE (0x06)       ── 24AWG, 250mm
    ├── RL_HIP_YAW (0x07)    ── 24AWG, 200mm
    ├── RL_HIP_PIT (0x08)    ── 24AWG, 180mm
    ├── RL_KNEE (0x09)       ── 24AWG, 250mm
    ├── RR_HIP_YAW (0x0A)    ── 24AWG, 200mm
    ├── RR_HIP_PIT (0x0B)    ── 24AWG, 180mm
    └── RR_KNEE (0x0C)       ── 24AWG, 250mm
    
    LEG POWER TOTAL: ~12A continuous (walking gait)
    LEG POWER PEAK: ~18A (climbing, dynamic moves)
```

---

## 4. ARM MOTOR WIRING

### 4.1 Arm Wiring Detail

```
┌─────────────────────────────────────────────────────────────┐
│                    5-DOF ARM SYSTEM                          │
│                                                              │
│  ┌──────────────┐                                            │
│  │  SHOULDER     │  CAN: ID 0x10                             │
│  │  PITCH        │  Connector: JST-GH 4-pin                 │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  SHOULDER     │  CAN: ID 0x11                             │
│  │  ROLL         │  Connector: JST-GH 4-pin                 │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  ELBOW        │  CAN: ID 0x12                             │
│  │  PITCH        │  Connector: JST-GH 4-pin                 │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  WRIST        │  CAN: ID 0x13                             │
│  │  PITCH        │  Connector: JST-GH 4-pin                 │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  GRIPPER      │  CAN: ID 0x14                             │
│  │  MOTOR        │  Connector: JST-GH 4-pin                 │
│  │              │  Pin 1: CAN_H (green)                      │
│  │  M2006 PAP   │  Pin 2: CAN_L (white)                     │
│  │  24V / 100W  │  Pin 3: GND (black)                       │
│  │              │  Pin 4: +24V (red)                         │
│  └──────┬───────┘                                            │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  FORCE-TORQUE │  I2C bus                                  │
│  │  SENSOR       │  Connector: JST-GH 4-pin                 │
│  │              │  Pin 1: SDA (blue)                         │
│  │  Custom       │  Pin 2: SCL (purple)                      │
│  │  6-axis       │  Pin 3: VCC (red, 3.3V)                  │
│  │              │  Pin 4: GND (black)                        │
│  └──────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Arm Power Wiring

```
24V MAIN BUS (8A max for arm)
    │
    ├── ARM_SHP (0x10)  ── 24AWG, 400mm (from body to shoulder)
    ├── ARM_SHR (0x11)  ── 24AWG, 350mm
    ├── ARM_ELB (0x12)  ── 24AWG, 300mm
    ├── ARM_WRS (0x13)  ── 24AWG, 250mm
    └── ARM_GRP (0x14)  ── 24AWG, 200mm
    
    ARM POWER TOTAL: ~5A continuous
    ARM POWER PEAK: ~10A (heavy lift, fast motion)
```

---

## 5. SENSOR WIRING

### 5.1 Camera Connections (4×)

```
┌─────────────────────────────────────────────────────────────┐
│                   CAMERA WIRING                              │
│                                                              │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐            │
│  │ Camera 1  │     │ Camera 2  │     │ Camera 3  │            │
│  │ (Front)   │     │ (Rear)    │     │ (Left)    │            │
│  │ IMX519    │     │ IMX519    │     │ IMX519    │            │
│  └─────┬────┘     └─────┬────┘     └─────┬────┘            │
│        │ CSI-2           │ CSI-2           │ CSI-2            │
│        │ (22-pin FFC)    │ (22-pin FFC)    │ (22-pin FFC)     │
│        │                 │                 │                  │
│        ▼                 ▼                 ▼                  │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              RASPBERRY PI 5                          │    │
│  │                                                      │    │
│  │  CSI-2 Port 0 ◄── Camera 1 (Front)                  │    │
│  │  CSI-2 Port 1 ◄── Camera 2 (Rear)                   │    │
│  │                                                      │    │
│  │  Note: Cameras 3 & 4 use USB via hub                │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌──────────┐                                                │
│  │ Camera 4  │     USB Camera (via powered hub)              │
│  │ (Right)   │     Connector: USB-A                          │
│  │ IMX519    │     Cable: 300mm USB-C to USB-A               │
│  └─────┬────┘                                                │
│        │ USB                                                 │
│        ▼                                                     │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              USB 3.0 HUB (powered)                   │    │
│  │                                                      │    │
│  │  Port 1 ◄── Camera 4 (Right)                        │    │
│  │  Port 2 ◄── LIDAR (via USB-UART adapter)            │    │
│  │  Port 3 ◄── GPS (via USB-UART adapter)              │    │
│  │  Port 4 ◄── Coral TPU (M.2 to USB adapter)          │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 LIDAR Connection

```
┌─────────────────────────────────────────────────────────────┐
│                    LIDAR WIRING                              │
│                                                              │
│  ┌──────────────┐                                            │
│  │  RPLIDAR A1M8│                                            │
│  │              │                                            │
│  │  Connector:  │                                            │
│  │  Micro-USB   │──── USB Cable ────┐                       │
│  │              │                    │                       │
│  │  Power:      │                    │                       │
│  │  5V/GND      │──── 2-pin JST ────┤                       │
│  └──────────────┘                    │                       │
│                                      │                       │
│                                      ▼                       │
│                              ┌──────────────┐               │
│                              │  USB 3.0 HUB  │               │
│                              │  Port 2       │               │
│                              └──────┬───────┘               │
│                                     │                        │
│                                     ▼                        │
│                             ┌──────────────┐               │
│                             │ RASPBERRY PI 5│               │
│                             │ USB 3.0       │               │
│                             └──────────────┘               │
│                                                              │
│  LIDAR Specs:                                                │
│  • UART: 115200 baud                                         │
│  • Protocol: SLAMTEC binary                                   │
│  • Scan rate: 8 Hz                                           │
│  • Power: 5V, 500mA (2.5W)                                  │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 IMU Connection

```
┌─────────────────────────────────────────────────────────────┐
│                    IMU WIRING                                │
│                                                              │
│  ┌──────────────┐                                            │
│  │  BNO085       │                                            │
│  │  (Adafruit    │                                            │
│  │   breakout)   │                                            │
│  │              │                                            │
│  │  VCC ◄────── 3.3V (from main PCB)                       │
│  │  GND ◄────── GND (main PCB)                             │
│  │  SDA ◄────── I2C SDA (main PCB)                         │
│  │  SCL ◄────── I2C SCL (main PCB)                         │
│  │  INT ──────► GPIO PB6 (main PCB, interrupt)             │
│  │  RST ◄────── GPIO PA8 (main PCB, reset)                │
│  └──────────────┘                                            │
│                                                              │
│  I2C Bus Properties:                                         │
│  • Address: 0x4A (SDO/GND) or 0x4B (SDO/VCC)              │
│  • Speed: 400 kHz (Fast Mode)                               │
│  • Pull-ups: 4.7kΩ to 3.3V (on main PCB)                   │
│  • Cable length: < 100mm                                    │
│  • Mounting: vibration dampener (silicone 40A)              │
└─────────────────────────────────────────────────────────────┘
```

### 5.4 FSR Wiring (4×)

```
┌─────────────────────────────────────────────────────────────┐
│                   FSR WIRING (per foot)                      │
│                                                              │
│  ┌──────────────┐                                            │
│  │  FSR 402      │                                            │
│  │  (in foot pad)│                                            │
│  │              │                                            │
│  │  Leg 1 ◄──── 10kΩ resistor ── 3.3V                      │
│  │  Leg 2 ◄──── ADC input (ADS1115)                        │
│  └──────────────┘                                            │
│                                                              │
│  Voltage Divider:                                            │
│                                                              │
│     3.3V                                                     │
│      │                                                       │
│     [10kΩ]                                                   │
│      │                                                       │
│      ├──── FSR_OUT ────► ADS1115 AIN0                        │
│      │                                                       │
│    [FSR 402]                                                 │
│      │                                                       │
│     GND                                                      │
│                                                              │
│  FSR Resistance Range:                                       │
│  • No load: >10MΩ → V_out ≈ 3.3V                           │
│  • 1N: ~20kΩ → V_out ≈ 2.0V                                │
│  • 10N: ~2kΩ → V_out ≈ 0.5V                                │
│  • 100N: ~200Ω → V_out ≈ 0.06V                             │
│                                                              │
│  ADS1115 Configuration:                                      │
│  • AIN0: Front Left foot                                    │
│  • AIN1: Front Right foot                                   │
│  • AIN2: Rear Left foot                                     │
│  • AIN3: Rear Right foot                                    │
│  • Gain: ±4.096V (ADS1115_CONFIG_GAIN_FOUR)                │
│  • Sample rate: 860 SPS                                     │
└─────────────────────────────────────────────────────────────┘
```

### 5.5 GPS Wiring

```
┌─────────────────────────────────────────────────────────────┐
│                    GPS WIRING                                │
│                                                              │
│  ┌──────────────┐                                            │
│  │  NEO-M8N      │                                            │
│  │  (u-blox)     │                                            │
│  │              │                                            │
│  │  VCC ◄────── 3.3V (from main PCB)                       │
│  │  GND ◄────── GND (main PCB)                             │
│  │  TX  ──────► UART RX (main PCB, USART4)                 │
│  │  RX  ◄────── UART TX (main PCB, USART4)                 │
│  │  PPS ──────► GPIO PA0 (main PCB, pulse)                 │
│  └──────┬───────┘                                            │
│         │                                                    │
│  ┌──────┴───────┐                                            │
│  │  PATCH ANTENNA│  (external, magnetic mount)               │
│  │              │  Cable: 3m SMA to u.FL                    │
│  │  28dBi gain  │  Mounting: top of robot body              │
│  └──────────────┘                                            │
│                                                              │
│  UART Configuration:                                         │
│  • Baud rate: 9600                                           │
│  • Data bits: 8                                              │
│  • Stop bits: 1                                              │
│  • Parity: None                                              │
│  • Protocol: NMEA 0183 + UBX binary                         │
│  • Update rate: 10 Hz                                        │
└─────────────────────────────────────────────────────────────┘
```

### 5.6 Temperature/Humidity Sensor

```
┌─────────────────────────────────────────────────────────────┐
│                 TEMPERATURE/HUMIDITY WIRING                  │
│                                                              │
│  ┌──────────────┐                                            │
│  │  BME280       │                                            │
│  │  (breakout)   │                                            │
│  │              │                                            │
│  │  VCC ◄────── 3.3V (from main PCB)                       │
│  │  GND ◄────── GND (main PCB)                             │
│  │  SDA ◄────── I2C SDA (main PCB)                         │
│  │  SCL ◄────── I2C SCL (main PCB)                         │
│  │  CSB ◄────── VCC (I2C mode)                             │
│  │  SDO ◄────── GND (address 0x76)                         │
│  └──────────────┘                                            │
│                                                              │
│  I2C Configuration:                                          │
│  • Address: 0x76 (SDO/GND) or 0x77 (SDO/VCC)              │
│  • Speed: 400 kHz                                           │
│  • Oversampling: 16× temp, 16× pressure, 16× humidity      │
│  • Filter: coefficient 4                                    │
│  • Update rate: 1 Hz                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. MAIN PCB PIN ASSIGNMENTS

### 6.1 STM32H743 Pin Mapping

```
┌─────────────────────────────────────────────────────────────┐
│              STM32H743VIT6 PIN ASSIGNMENTS                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  CAN1 (Leg Bus):                                             │
│  • PD0 = CAN1_TX                                            │
│  • PD1 = CAN1_RX                                            │
│                                                              │
│  CAN2 (Arm Bus):                                             │
│  • PB5 = CAN2_TX                                            │
│  • PB6 = CAN2_RX                                            │
│                                                              │
│  CAN3 (Sensor Bus):                                          │
│  • PB12 = CAN3_TX                                           │
│  • PB13 = CAN3_RX                                           │
│                                                              │
│  I2C1 (IMU + BME280):                                        │
│  • PB8 = I2C1_SCL                                           │
│  • PB9 = I2C1_SDA                                           │
│  • PB6 = I2C1_INT (BNO085 interrupt)                        │
│                                                              │
│  I2C2 (ADC + FSR):                                           │
│  • PB10 = I2C2_SCL                                          │
│  • PB11 = I2C2_SDA                                          │
│                                                              │
│  I2C3 (Force-Torque Sensor):                                 │
│  • PA8 = I2C3_SCL                                           │
│  • PC9 = I2C3_SDA                                           │
│                                                              │
│  UART4 (GPS):                                                │
│  • PA0 = UART4_RX (GPS PPS input)                           │
│  • PA1 = UART4_TX                                           │
│                                                              │
│  UART5 (Debug):                                              │
│  • PC12 = UART5_TX                                          │
│  • PD2 = UART5_RX                                           │
│                                                              │
│  SPI1 (Internal):                                            │
│  • PA5 = SPI1_SCK                                           │
│  • PA6 = SPI1_MISO                                          │
│  • PA7 = SPI1_MOSI                                          │
│  • PA4 = SPI1_NSS                                           │
│                                                              │
│  ADC1 (Analog):                                              │
│  • PA0 = ADC1_IN0 (FSR_FL)                                  │
│  • PA1 = ADC1_IN1 (FSR_FR)                                  │
│  • PA2 = ADC1_IN2 (FSR_RL)                                  │
│  • PA3 = ADC1_IN3 (FSR_RR)                                  │
│                                                              │
│  TIMERS:                                                     │
│  • TIM1 = PWM for status LEDs                               │
│  • TIM2 = System tick (1 kHz)                               │
│  • TIM3 = Motor watchdog timer                              │
│  • TIM4 = LED animation                                     │
│                                                              │
│  GPIO:                                                       │
│  • PC0 = Emergency stop input (active low)                  │
│  • PC1 = Contactor enable (active high)                     │
│  • PC2 = Fan PWM control                                    │
│  • PC3 = Battery status LED                                 │
│  • PD3 = LIDAR reset                                        │
│  • PD4 = Coral TPU reset                                    │
│  • PD5 = Pi power enable                                    │
│  • PD6 = Pi reset                                           │
│  • PE0 = RGB LED data (WS2812)                              │
│  • PE1 = Buzzer output                                      │
│                                                              │
│  USB (Pi Connection):                                        │
│  • PA11 = USB_DM                                            │
│  • PA12 = USB_DP                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. I2C BUS MAP

```
┌─────────────────────────────────────────────────────────────┐
│                    I2C BUS TOPOLOGY                           │
│                                                              │
│  I2C1 (400 kHz, 4.7kΩ pull-ups):                           │
│  ├── BNO085 IMU (0x4A) ──── 100mm cable                    │
│  └── BME280 Temp/Hum (0x76) ── 50mm cable                  │
│                                                              │
│  I2C2 (400 kHz, 4.7kΩ pull-ups):                           │
│  └── ADS1115 ADC (0x48) ──── 150mm cable                   │
│      ├── AIN0: FSR Front Left                               │
│      ├── AIN1: FSR Front Right                              │
│      ├── AIN2: FSR Rear Left                                │
│      └── AIN3: FSR Rear Right                               │
│                                                              │
│  I2C3 (400 kHz, 4.7kΩ pull-ups):                           │
│  └── Force-Torque Sensor (0x28) ── 200mm cable             │
│                                                              │
│  Total I2C devices: 4                                       │
│  Total I2C cables: 3                                        │
│  Max cable length: 200mm                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. POWER WIRING DIAGRAM

### 8.1 48V Distribution

```
┌─────────────────────────────────────────────────────────────┐
│                 48V POWER DISTRIBUTION                       │
│                                                              │
│  ┌──────────┐    ┌──────────┐                               │
│  │ BATTERY 1 │    │ BATTERY 2 │                               │
│  │ 48V/208Ah │    │ 48V/208Ah │                               │
│  │ 10 kWh    │    │ 10 kWh    │                               │
│  └─────┬────┘    └─────┬────┘                               │
│        │ XT90          │ XT90                               │
│        │               │                                     │
│        └───────┬───────┘                                     │
│                │                                             │
│        ┌───────┴───────┐                                     │
│        │  EMERGENCY     │                                     │
│        │  STOP BUTTON   │                                     │
│        │  (main contact)│                                     │
│        └───────┬───────┘                                     │
│                │                                             │
│        ┌───────┴───────┐                                     │
│        │   48V MAIN     │                                     │
│        │   BUS BAR      │                                     │
│        └──┬────┬────┬──┘                                     │
│           │    │    │                                        │
│           ▼    ▼    ▼                                        │
│     ┌─────┐┌─────┐┌─────┐                                   │
│     │48→24││48→5 ││48→12│                                   │
│     │Buck ││Buck ││Buck │                                   │
│     └──┬──┘└──┬──┘└──┬──┘                                   │
│        │      │      │                                      │
│        ▼      ▼      ▼                                      │
│     24V Bus 5V Bus 12V Bus                                  │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 24V Motor Bus Detail

```
┌─────────────────────────────────────────────────────────────┐
│                 24V MOTOR POWER BUS                          │
│                                                              │
│  ┌──────────────┐                                            │
│  │  48V→24V BUCK │                                            │
│  │  360W / 15A   │                                            │
│  └──────┬───────┘                                            │
│         │                                                    │
│         │ 14 AWG (15A capable)                              │
│         │                                                    │
│    ┌────┴────┐                                               │
│    │  24V     │                                               │
│    │  BUS     │                                               │
│    │  BAR     │                                               │
│    └┬──┬──┬──┘                                               │
│     │  │  │                                                  │
│     │  │  │  24 AWG per motor (4.2A each)                   │
│     │  │  │                                                  │
│     ▼  ▼  ▼                                                  │
│   ┌──┐┌──┐┌──┐┌──┐ ... (12 leg motors)                     │
│   │M1││M2││M3││M4│                                           │
│   └──┘└──┘└──┘└──┘                                           │
│                                                              │
│  Voltage drop at 15A:                                        │
│  • 14 AWG, 300mm: 0.03V (negligible)                        │
│  • 24 AWG, 250mm: 0.05V per motor (acceptable)              │
│                                                              │
│  Total 24V bus current:                                      │
│  • Idle: 0.5A                                                │
│  • Walking: 8-12A                                            │
│  • Climbing: 12-15A                                          │
│  • Peak (all motors): 18A (3 sec max)                       │
└─────────────────────────────────────────────────────────────┘
```

### 8.3 5V Logic Bus

```
┌─────────────────────────────────────────────────────────────┐
│                 5V LOGIC POWER BUS                           │
│                                                              │
│  ┌──────────────┐                                            │
│  │  48V→5V BUCK  │                                            │
│  │  25W / 5A     │                                            │
│  └──────┬───────┘                                            │
│         │                                                    │
│         │ 18 AWG (5A capable)                               │
│         │                                                    │
│    ┌────┴────┐                                               │
│    │  5V      │                                               │
│    │  BUS     │                                               │
│    └┬──┬──┬──┘                                               │
│     │  │  │                                                  │
│     ▼  ▼  ▼                                                  │
│   ┌──┐┌──┐┌──┐┌──┐                                          │
│   │Pi││PCB││USB││LED│                                        │
│   └──┘└──┘└──┘└──┘                                           │
│                                                              │
│  5V Bus Current Budget:                                      │
│  • Raspberry Pi 5: 3A (max)                                 │
│  • Main PCB (STM32 + logic): 0.5A                           │
│  • USB Hub: 0.5A                                             │
│  • Status LEDs: 0.1A                                        │
│  • Fan: 0.1A                                                │
│  • Total: 4.2A (within 5A rating)                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. GROUNDING SCHEME

```
┌─────────────────────────────────────────────────────────────┐
│                    GROUNDING TOPOLOGY                         │
│                                                              │
│  ┌─────────────────────────────────────────────┐            │
│  │              CHASSIS GND (Star)              │            │
│  │              Single point ground             │            │
│  │              (main PCB, center)              │            │
│  └──────────┬──────────┬──────────┬────────────┘            │
│             │          │          │                          │
│             ▼          ▼          ▼                          │
│        ┌────────┐ ┌────────┐ ┌────────┐                     │
│        │ POWER  │ │ SIGNAL │ │ EARTH  │                     │
│        │ GND    │ │ GND    │ │ GND    │                     │
│        └───┬────┘ └───┬────┘ └───┬────┘                     │
│            │          │          │                          │
│            ▼          ▼          ▼                          │
│     • Motor GND  • I2C GND   • Chassis                     │
│     • Battery GND • SPI GND   • Frame                      │
│     • Buck GND   • UART GND  • Earth pin                   │
│     • CAN GND    • ADC GND    (charger)                    │
│                                                              │
│  Rules:                                                      │
│  1. All grounds meet at single star point                    │
│  2. No ground loops between power and signal                │
│  3. CAN shields grounded at one end only (main PCB)         │
│  4. Chassis connected to earth via charger                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 10. CABLE COLOR CODING

| Color | Function | Example |
|-------|----------|---------|
| Red | +24V power | Motor power |
| Black | GND | All grounds |
| Green | CAN_H | CAN bus high |
| White | CAN_L | CAN bus low |
| Blue | I2C SDA | Data line |
| Purple | I2C SCL | Clock line |
| Yellow | Analog signal | FSR output |
| Orange | Analog reference | FSR reference |
| Brown | UART TX | GPS transmit |
| Gray | UART RX | GPS receive |
| Pink | GPIO | Interrupt, control |
| Bare copper | Shield drain | CAN cable shield |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
