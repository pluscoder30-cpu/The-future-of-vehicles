# PHI_HUMANOID_ROBOT — Wiring Diagrams

## Electrical Wiring & Signal Routing

---

## 1. Power Distribution Topology

```
                    ┌─────────────────────────────┐
                    │     48V BATTERY PACK         │
                    │  ┌─────┐ ┌─────┐ ┌─────┐   │
                    │  │FPB  │ │FPB  │ │FPB  │   │
                    │  │-10  │ │-10  │ │-10  │   │
                    │  │#1   │ │#2   │ │#3   │   │
                    │  └──┬──┘ └──┬──┘ └──┬──┘   │
                    │     │       │       │      │
                    │  ┌──┴──┐    │       │      │
                    │  │FPB  │    │       │      │
                    │  │-10  │    │       │      │
                    │  │#4   │    │       │      │
                    │  └──┬──┘    │       │      │
                    └─────┼───────┼───────┼──────┘
                          │       │       │
                    ┌─────┴───────┴───────┴──────┐
                    │    MAIN CONTACTOR (100A)     │
                    │    + Main Fuse (80A)          │
                    └─────────┬───────────────────┘
                              │
                    ┌─────────┴───────────────────┐
                    │      48V BUS (8 AWG)         │
                    │    Power Distribution PCB     │
                    └──┬────┬────┬────┬────┬──────┘
                       │    │    │    │    │
         ┌─────────────┘    │    │    │    └──────────────┐
         │                  │    │    │                   │
    ┌────┴─────┐   ┌───────┴──┐ │  ┌─┴────────┐   ┌─────┴──────┐
    │48V→12V   │   │48V→12V   │ │  │48V→5V    │   │48V→5V      │
    │Buck #1   │   │Buck #2   │ │  │Buck #1   │   │Buck #2     │
    │12V/10A   │   │12V/10A   │ │  │5V/6A     │   │5V/6A       │
    └────┬─────┘   └───────┬──┘ │  └─┬────────┘   └─────┬──────┘
         │                  │    │    │                   │
    ┌────┴────────┐   ┌────┴──┐ │  ┌─┴────────┐   ┌─────┴──────┐
    │ 12V RAIL    │   │12V    │ │  │ 5V RAIL  │   │ 5V RAIL    │
    │ (Left Limb) │   │(Right │ │  │ (Logic)  │   │ (Logic)    │
    │             │   │ Limb) │ │  │          │   │            │
    └──────┬──────┘   └───┬───┘ │  └────┬─────┘   └─────┬──────┘
           │              │     │       │                │
      ┌────┴────┐    ┌────┴───┐ │  ┌────┴─────┐    ┌────┴─────┐
      │Left Leg │    │Right   │ │  │RPi 5     │    │Sensors   │
      │ODrive   │    │Leg     │ │  │Coral TPU │    │IMUs      │
      │S1×2    │    │ODrive  │ │  │STM32×2   │    │Encoders  │
      │12V      │    │S1×2   │ │  │NVMe SSD  │    │Cameras   │
      └─────────┘    └────────┘ │  └──────────┘    └──────────┘
                                │
                           ┌────┴─────┐
                           │ 3.3V LDO │
                           │ (×4)     │
                           └────┬─────┘
                                │
                           ┌────┴─────┐
                           │ 3.3V RAIL│
                           │ (Sensors)│
                           │ Encoders │
                           └──────────┘
```

---

## 2. Signal Bus Architecture

### 2.1 CAN Bus Network

The CAN bus is the primary communication backbone. All motor controllers communicate via CAN.

```
                    ┌─────────────────────────────┐
                    │         RPi 5               │
                    │    CAN-to-USB adapter        │
                    │    (MCP2515 HAT)             │
                    └──────────┬──────────────────┘
                               │ CAN_H / CAN_L
                               │ (120Ω termination)
                               │
                    ┌──────────┴──────────────────┐
                    │     CAN BUS TRUNK LINE       │
                    │     500 kbps, shielded       │
                    │     Molex Micro-Fit 4-pin    │
                    └──┬────┬────┬────┬────┬──────┘
                       │    │    │    │    │
          ┌────────────┘    │    │    │    └────────────┐
          │                 │    │    │                 │
    ┌─────┴─────┐  ┌───────┴┐  │  ┌─┴───────┐  ┌─────┴─────┐
    │ODrive S1  │  │ODrive  │  │  │ODrive   │  │ODrive     │
    │Left Leg   │  │Right   │  │  │Left Arm │  │Right Arm  │
    │#1 (HAA/   │  │Leg #1  │  │  │#1 (SAA/ │  │#1 (SAA/  │
    │ HFE)      │  │(HAA/   │  │  │ SFE)    │  │ SFE)     │
    │CAN ID: 0  │  │HFE)    │  │  │CAN ID: 4│  │CAN ID: 6 │
    └─────┬─────┘  │CAN ID:1│  │  └────┬────┘  └─────┬────┘
          │        └───┬────┘  │       │              │
          │            │       │       │              │
    ┌─────┴─────┐  ┌───┴────┐ │  ┌────┴────┐  ┌─────┴─────┐
    │ODrive S1  │  │ODrive  │ │  │ODrive   │  │ODrive     │
    │Left Leg   │  │Right   │ │  │Left Arm │  │Right Arm  │
    │#2 (KFE/   │  │Leg #2  │ │  │#2 (ELF/ │  │#2 (ELF/  │
    │ KAA)      │  │(KFE/   │ │  │ WFE)    │  │ WFE)     │
    │CAN ID: 2  │  │KAA)    │ │  │CAN ID: 5│  │CAN ID: 7 │
    └─────┬─────┘  │CAN ID:3│ │  └─────────┘  └───────────┘
          │        └───┬────┘ │
          │            │      │
    ┌─────┴─────┐  ┌───┴────┐│  ┌─────────────────────────┐
    │ODrive S1  │  │ODrive  ││  │  ODrive Pro (Dual)      │
    │Left Leg   │  │Right   ││  │  Torso Yaw + Pitch      │
    │#3 (AFE/   │  │Leg #3  ││  │  CAN ID: 8              │
    │ TOE)      │  │(AFE/   ││  └─────────────────────────┘
    │CAN ID: 9  │  │TOE)    ││
    └───────────┘  │CAN ID:10││  ┌─────────────────────────┐
                   └────────┘│  │  ODrive Pro (Dual)      │
                             │  │  Head Pan + Tilt        │
                             │  │  CAN ID: 11             │
                             │  └─────────────────────────┘
                             │
                             │  ┌─────────────────────────┐
                             │  │  Dynamixel Chain        │
                             │  │  U2D2 → XL330 × 12      │
                             │  │  TTL half-duplex         │
                             │  └─────────────────────────┘
```

### 2.2 I2C Sensor Bus

```
RPi 5 I2C-1 (Bus 0, 400kHz)
│
├── BNO085 IMU (Body)          — Address 0x4A
├── BNO055 IMU (Head)          — Address 0x50
├── INA260 #1 (Main power)     — Address 0x40
├── INA260 #2 (Left limb)      — Address 0x41
├── INA260 #3 (Right limb)     — Address 0x42
├── INA260 #4 (Logic)          — Address 0x43
├── TSL2591 (Ambient light)    — Address 0x28
├── TMP117 #1 (Torso temp)     — Address 0x48
└── TMP117 #2 (Head temp)      — Address 0x49

RPi 5 I2C-2 (Bus 1, 400kHz)
│
├── SSD1306 OLED Left Eye       — Address 0x3C
├── SSD1306 OLED Right Eye      — Address 0x3D
├── WM8960 Audio Codec          — Address 0x1A
└── AS5048A Encoders (shifted)  — Address 0x40-0x4F
```

### 2.3 SPI Bus

```
RPi 5 SPI0
│
├── AS5048A Encoder (Hip Left)     — CE0
├── AS5048A Encoder (Hip Right)    — CE1
└── NVMe SSD                       — PCIe (native)

RPi 5 SPI1 (via STM32 co-processor)
│
├── AS5048A Encoders (all leg joints) — multiplexed via STM32
└── Strain gauge ADCs (24-bit ADS1256) — multiplexed via STM32
```

### 2.4 I2S Audio Bus

```
RPi 5 I2S
│
├── INMP441 Microphone ×4
│   ├── Mic 1: WS=GPIO19, SCK=GPIO18, SD=GPIO20
│   ├── Mic 2: WS=GPIO19, SCK=GPIO18, SD=GPIO21
│   ├── Mic 3: WS=GPIO19, SCK=GPIO18, SD=GPIO22
│   └── Mic 4: WS=GPIO19, SCK=GPIO18, SD=GPIO23
│
├── MAX98357A Amplifier → Speaker L
│   └── BCLK=GPIO18, LRCLK=GPIO19, DIN=GPIO21
│
└── MAX98357A Amplifier → Speaker R
    └── BCLK=GPIO18, LRCLK=GPIO19, DIN=GPIO20
```

### 2.5 MIPI CSI Camera Bus

```
RPi 5 CSI-0 (2-lane)
│
├── Stereo Camera Left (Arducam 1280×800)
│   └── MIPI CSI-2, 200mm flex cable
│
RPi 5 CSI-1 (2-lane)
│
└── Stereo Camera Right (Arducam 1280×800)
    └── MIPI CSI-2, 200mm flex cable
```

---

## 3. Joint-Level Wiring Detail

### 3.1 Left Leg — Joint Wiring

```
┌─────────────────────────────────────────────────────────────────┐
│                     LEFT LEG WIRING                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HIP ABDUCTION/ADDUCTION (HAA) — Joint #1                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D6374 150KV                                │   │
│  │ Phase wires: 3× 14AWG (blue, green, yellow) → ODrive #1  │   │
│  │ Encoder: AS5048A → SPI (CE0)                             │   │
│  │   - VCC: 3.3V, GND, MOSI, MISO, SCK, CS                 │   │
│  │ Torque sensor: Strain gauge → ADS1256 → STM32 #1         │   │
│  │   - Excitation: 3.3V, Signal: ±10mV, 24-bit              │   │
│  │ ODrive #1 channel A                                       │   │
│  │   - CAN ID: 0                                             │   │
│  │   - Power: 48V from bus, 40A max                           │   │
│  │   - Temperature: NTC 10kΩ (on motor)                      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  HIP FLEXION/EXTENSION (HFE) — Joint #2                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D6374 150KV                                │   │
│  │ Phase wires: 3× 14AWG → ODrive #1 channel B              │   │
│  │ Encoder: AS5048A → SPI (CE1)                             │   │
│  │ Torque sensor: Strain gauge → ADS1256 → STM32 #1         │   │
│  │ CAN ID: 0 (shared with HAA on ODrive #1)                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  KNEE FLEXION/EXTENSION (KFE) — Joint #3                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D6374 150KV                                │   │
│  │ Phase wires: 3× 14AWG → ODrive #2 channel A              │   │
│  │ Encoder: AS5048A → SPI (multiplexed via STM32)            │   │
│  │ Torque sensor: Strain gauge → ADS1256 → STM32 #1         │   │
│  │ CAN ID: 2                                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  KNEE ABDUCTION/ADDUCTION (KAA) — Joint #4                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #2 channel B              │   │
│  │ Encoder: AS5048A → SPI (multiplexed via STM32)            │   │
│  │ CAN ID: 2 (shared with KFE on ODrive #2)                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ANKLE FLEXION/EXTENSION (AFE) — Joint #5                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #3 channel A              │   │
│  │ Encoder: AS5048A → SPI (multiplexed via STM32)            │   │
│  │ CAN ID: 9                                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  TOE FLEXION — Joint #6                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #3 channel B              │   │
│  │ Encoder: AS5048A → SPI (multiplexed via STM32)            │   │
│  │ CAN ID: 9 (shared with AFE on ODrive #3)                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  FOOT FORCE SENSORS                                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 4× FSR406 sensors per foot                               │   │
│  │   - Heel: FSR → voltage divider → ADC (STM32)            │   │
│  │   - Ball-lateral: FSR → voltage divider → ADC            │   │
│  │   - Ball-center: FSR → voltage divider → ADC             │   │
│  │   - Ball-medial: FSR → voltage divider → ADC             │   │
│  │   - ADC: ADS1256 24-bit, 30kHz sampling                  │   │
│  │   - Reference: 3.3V via 10kΩ, signal: 0-3.3V            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  12V POWER FEED                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ From 12V bus → 12V blade fuse (20A) → Joint motors       │   │
│  │ Return: Common ground, 10 AWG bus bar                    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Right Leg — Mirror of Left Leg

```
Same topology as Left Leg, mirrored:
- HAA: ODrive #4 channel A, CAN ID: 1
- HFE: ODrive #4 channel B, CAN ID: 1
- KFE: ODrive #5 channel A, CAN ID: 3
- KAA: ODrive #5 channel B, CAN ID: 3
- AFE: ODrive #6 channel A, CAN ID: 10
- TOE: ODrive #6 channel B, CAN ID: 10
- Encoders: Same SPI bus, different CS pins (via STM32 MUX)
- Force sensors: Same ADC bus, different channels
```

### 3.3 Left Arm — Joint Wiring

```
┌─────────────────────────────────────────────────────────────────┐
│                     LEFT ARM WIRING                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SHOULDER ABDUCTION/ADDUCTION (SAA) — Joint #7                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #7 channel A              │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ Torque sensor: Strain gauge → ADS1256 → STM32 #2         │   │
│  │ CAN ID: 4                                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SHOULDER FLEXION/EXTENSION (SFE) — Joint #8                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #7 channel B              │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 4 (shared with SAA on ODrive #7)                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SHOULDER HORIZONTAL (SHS) — Joint #9                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #8 channel A              │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 5                                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ELBOW FLEXION/EXTENSION (ELF) — Joint #10                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D5065 270KV                                │   │
│  │ Phase wires: 3× 16AWG → ODrive #8 channel B              │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ Torque sensor: Strain gauge → ADS1256 → STM32 #2         │   │
│  │ CAN ID: 5 (shared with SHS on ODrive #8)                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  WRIST FLEXION/EXTENSION (WFE) — Joint #11                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive M5671 100KV                                │   │
│  │ Phase wires: 3× 20AWG → ODrive #9 channel A              │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 12 (via separate mini-ODrive or shared)          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  WRIST ROTATION (WRU) — Joint #12                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive M5671 100KV                                │   │
│  │ Phase wires: 3× 20AWG → ODrive #9 channel B              │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 12 (shared with WFE on ODrive #9)                │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  HAND — FINGER ACTUATORS (5× XL330)                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Dynamixel XL330-M288 daisy chain                         │   │
│  │   - Thumb opposition: ID 1                               │   │
│  │   - Index flexion: ID 2                                  │   │
│  │   - Middle flexion: ID 3                                 │   │
│  │   - Ring flexion: ID 4                                   │   │
│  │   - Pinky flexion: ID 5                                  │   │
│  │   - Communication: TTL half-duplex, 1Mbps                │   │
│  │   - Power: 5V from USB bus, 2A peak                       │   │
│  │   - FSR sensors: 5× on fingertips → ADC                  │   │
│  │     - Signal: analog → ADS1256 → STM32                   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.4 Right Arm — Mirror of Left Arm

```
Same topology as Left Arm, mirrored:
- SAA: ODrive #10 channel A, CAN ID: 6
- SFE: ODrive #10 channel B, CAN ID: 6
- SHS: ODrive #11 channel A, CAN ID: 7
- ELF: ODrive #11 channel B, CAN ID: 7
- WFE: ODrive #12 channel A, CAN ID: 13
- WRU: ODrive #12 channel B, CAN ID: 13
- Hand: XL330 chain, IDs 6-10
```

### 3.5 Torso — Joint Wiring

```
┌─────────────────────────────────────────────────────────────────┐
│                     TORSO WIRING                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TORSO YAW — Joint #13                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D6374 150KV                                │   │
│  │ Phase wires: 3× 14AWG → ODrive Pro ch.A                  │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 8 channel A                                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  TORSO PITCH — Joint #14                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive D6374 150KV                                │   │
│  │ Phase wires: 3× 14AWG → ODrive Pro ch.B                  │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 8 channel B                                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.6 Head — Joint Wiring

```
┌─────────────────────────────────────────────────────────────────┐
│                     HEAD WIRING                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HEAD PAN — Joint #15                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive M5671 100KV                                │   │
│  │ Phase wires: 3× 20AWG → ODrive Pro ch.A                  │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 11 channel A                                      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  HEAD TILT — Joint #16                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Motor: ODrive M5671 100KV                                │   │
│  │ Phase wires: 3× 20AWG → ODrive Pro ch.B                  │   │
│  │ Encoder: AS5048A → SPI (via STM32 MUX)                   │   │
│  │ CAN ID: 11 channel B                                      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  CAMERAS (×2 stereo)                                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Left stereo cam: MIPI CSI-2 → RPi CSI-0                  │   │
│  │ Right stereo cam: MIPI CSI-2 → RPi CSI-1                 │   │
│  │ Power: 3.3V from logic bus, 200mA total                   │   │
│  │ Sync: GPIO trigger (shared frame sync line)               │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  MICROPHONES (×4 array)                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ INMP441 × 4, I2S bus                                     │   │
│  │   - Shared BCLK (GPIO18) and LRCLK (GPIO19)              │   │
│  │   - Individual SD: GPIO20, 21, 22, 23                     │   │
│  │   - Power: 3.3V, 1mA each                                │   │
│  │   - Placement: Square array, 40mm spacing                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SPEAKERS (×2)                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ MAX98357A amplifier → 3W 8Ω speakers                     │   │
│  │   - I2S input from RPi 5                                  │   │
│  │   - L/R channel split                                     │   │
│  │   - Power: 5V from USB bus, 600mA peak                    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  OLED DISPLAYS (×2 eyes)                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ SSD1306 0.96" 128×64 OLED                                │   │
│  │   - Left eye: I2C bus 0, Address 0x3C                     │   │
│  │   - Right eye: I2C bus 0, Address 0x3D                    │   │
│  │   - Power: 3.3V, 20mA each                                │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SENSORS                                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ BNO055 IMU: I2C bus 0, Address 0x50                       │   │
│  │ VL53L0X ToF ×2: I2C bus 0, Addresses 0x29, 0x30          │   │
│  │ TMP117 temp: I2C bus 0, Address 0x49                      │   │
│  │ MaxBotix ultrasonic ×2: Analog → ADC                      │   │
│  │   - Power: 5V, 10mA each                                  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Grounding & Shielding

```
┌─────────────────────────────────────────────────────────────────┐
│                    GROUNDING SCHEME                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  POWER GROUND (PGND) — Thick, high-current                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Battery negative → Main bus bar (copper, 25mm×3mm)        │   │
│  │ All motor controller grounds → bus bar                    │   │
│  │ All buck converter grounds → bus bar                      │   │
│  │ Wire gauge: 10 AWG minimum                                │   │
│  │ Star ground topology at bus bar                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SIGNAL GROUND (SGND) — Clean, low-noise                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ RPi 5 ground plane → single point to PGND bus bar         │   │
│  │ Sensor grounds → RPi 5 ground plane                       │   │
│  │ Encoder grounds → Star topology to RPi GND                │   │
│  │ Separate analog and digital ground planes on PCBs         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SHIELD GROUND                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ CAN bus shield: Connected to PGND at ONE end only         │   │
│  │ Camera flex cables: Shielded, grounded at camera end      │   │
│  │ Encoder cables: Shielded, grounded at controller end      │   │
│  │ Strain gauge cables: Shielded, driven end grounding      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  CHASSIS GROUND                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Aluminum frame → Connected to PGND at pelvis plate        │   │
│  │ Single connection point to prevent ground loops            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Connector Pinout Reference

### 5.1 CAN Bus Connector (Molex Micro-Fit 4-pin)

| Pin | Signal | Wire Color | Gauge |
|-----|--------|------------|-------|
| 1 | CAN_H | Yellow | 22 AWG |
| 2 | CAN_L | Green | 22 AWG |
| 3 | +48V | Red | 18 AWG |
| 4 | GND | Black | 18 AWG |

### 5.2 Encoder Connector (JST-SH 4-pin)

| Pin | Signal | Wire Color | Description |
|-----|--------|------------|-------------|
| 1 | VCC | Red | 3.3V power |
| 2 | GND | Black | Ground |
| 3 | MOSI | Blue | SPI MOSI |
| 4 | MISO | Green | SPI MISO |
| 5 | SCK | Yellow | SPI clock |
| 6 | CS | Orange | Chip select |

### 5.3 Motor Phase Connector (Molex Micro-Fit 3-pin)

| Pin | Signal | Wire Color | Gauge |
|-----|--------|------------|-------|
| 1 | Phase A | Blue | 14/16 AWG |
| 2 | Phase B | Green | 14/16 AWG |
| 3 | Phase C | Yellow | 14/16 AWG |

### 5.4 Battery Connector (XT90)

| Pin | Signal | Wire Color | Gauge |
|-----|--------|------------|-------|
| 1 | V+ | Red | 8 AWG |
| 2 | V- | Black | 8 AWG |

### 5.5 I2S Microphone Connector (JST-SH 4-pin)

| Pin | Signal | Wire Color |
|-----|--------|------------|
| 1 | VCC | Red |
| 2 | GND | Black |
| 3 | WS | Blue |
| 4 | SCK | Green |
| 5 | SD | Yellow |

---

## 6. Wire Gauge Summary

| Circuit | Gauge | Max Current | Length |
|---------|-------|-------------|--------|
| Battery main bus | 8 AWG | 100A | 0.5m |
| 48V to buck converters | 12 AWG | 30A | 0.3m |
| Motor phase wires (HAA/HFE/KFE) | 14 AWG | 20A | 0.4m |
| Motor phase wires (KAA/AFE/TOE) | 16 AWG | 10A | 0.5m |
| Motor phase wires (arms) | 16 AWG | 10A | 0.6m |
| Motor phase wires (wrist/head) | 20 AWG | 3A | 0.3m |
| CAN bus signal | 22 AWG | 1A | 1.5m |
| I2C/SPI signal | 26 AWG | 0.5A | 0.3m |
| Power to sensors (5V) | 22 AWG | 2A | 0.4m |
| Power to sensors (3.3V) | 26 AWG | 0.5A | 0.3m |
| Speaker wires | 20 AWG | 3A | 0.2m |
| Microphone signal | 28 AWG | 0.1A | 0.15m |

---

## 7. Cable Routing Notes

1. **Left/Right separation**: All left-side cables route through left limb channels; right-side through right. No cross-body routing except CAN trunk.
2. **Flex zones**: Joints require cable loops with φ-ratio excess (1.618× minimum bend radius). Minimum bend radius = 5× cable OD.
3. **Strain relief**: All connectors at joints use silicone potting compound for strain relief.
4. **Color coding**: Power = Red/Black, CAN = Yellow/Green, SPI = Blue/Green/Yellow/Orange, I2S = Blue/Green/Yellow.
5. **Service loops**: 50mm service loops at each joint for maintenance access.
6. **φ-ratio cable bundling**: Cables bundled in groups following Fibonacci sequence (1, 1, 2, 3, 5, 8...) with corresponding tie spacing.

---

*Document: 02_WIRING.md — PHI_HUMANOID_ROBOT Wiring Diagrams*
*Version: 1.0 | Date: 2026-08-27*
