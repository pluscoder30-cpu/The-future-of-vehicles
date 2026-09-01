# PHI_HUMANOID_ROBOT — Circuit Design

## Custom PCB Schematics & Circuit Analysis

---

## 1. System Circuit Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHI_HUMANOID_ROBOT CIRCUIT ARCHITECTURE              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    POWER DISTRIBUTION PCB                        │   │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐            │   │
│  │  │48V   │  │48V→  │  │48V→  │  │48V→  │  │48V→  │            │   │
│  │  │Input │  │12V #1│  │12V #2│  │5V #1 │  │5V #2 │            │   │
│  │  │80A   │  │10A   │  │10A   │  │6A    │  │6A    │            │   │
│  │  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘            │   │
│  │     │         │         │         │         │                   │   │
│  │  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐            │   │
│  │  │80A   │  │12V   │  │12V   │  │5V    │  │5V    │            │   │
│  │  │Blade │  │Bus   │  │Bus   │  │Bus   │  │Bus   │            │   │
│  │  │Fuse  │  │Bar   │  │Bar   │  │Bar   │  │Bar   │            │   │
│  │  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    POWER MONITORING PCB                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │   │
│  │  │INA260 #1 │  │INA260 #2 │  │INA260 #3 │  │INA260 #4 │       │   │
│  │  │48V Main  │  │12V Left  │  │12V Right │  │5V Logic  │       │   │
│  │  │I²C: 0x40 │  │I²C: 0x41 │  │I²C: 0x42 │  │I²C: 0x43 │       │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    SENSOR HUB PCB                                │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │   │
│  │  │STM32H7   │  │ADS1256   │  │AS5048A   │  │BNO085    │       │   │
│  │  │#1 (Legs) │  │ADC Mux   │  │Encoder   │  │IMU       │       │   │
│  │  │          │  │24-bit    │  │Mux       │  │9-DoF     │       │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │   │
│  │                                                                 │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │   │
│  │  │STM32H7   │  │ADS1256   │  │AS5048A   │  │BNO055    │       │   │
│  │  │#2 (Arms) │  │ADC Mux   │  │Encoder   │  │IMU (Head)│       │   │
│  │  │          │  │24-bit    │  │Mux       │  │          │       │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    AI CORE                                       │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │   │
│  │  │RPi 5     │  │Coral TPU │  │NVMe SSD  │  │WiFi/BLE  │       │   │
│  │  │8GB       │  │4 TOPS    │  │256GB     │  │          │       │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Power Distribution PCB — Detailed Schematic

### 2.1 Main Input Stage

```
                    48V BATTERY INPUT
                         │
                    ┌────┴────┐
                    │  XT90   │
                    │  CONN   │
                    └────┬────┘
                         │
                    ┌────┴────┐
                    │  MAIN   │
                    │ CONTACTOR│ ← GPIO控制 (RPi GPIO24)
                    │ 100A    │   Failsafe: NC relay
                    └────┬────┘
                         │
                    ┌────┴────┐
                    │  80A    │
                    │  BLADE  │
                    │  FUSE   │
                    └────┬────┘
                         │
                    ┌────┴────────────────────────────┐
                    │        48V MAIN BUS              │
                    │    (4-layer, 2oz copper, 10mm)    │
                    └──┬────┬────┬────┬────┬──────────┘
                       │    │    │    │    │
```

### 2.2 Buck Converter Circuit (48V→12V, 10A)

```
                         48V
                          │
                     ┌────┴────┐
                     │  C1     │ 100µF, 63V electrolytic
                     │         │
                     └────┬────┘
                          │
                     ┌────┴─────────────────────────────────┐
                     │                                      │
                     │  ┌──────────────────────────────┐    │
                     │  │     TPS54360 (TI)            │    │
                     │  │     48V→12V, 3.5A, 95%       │    │
                     │  │                              │    │
                     │  │ VIN ───┬──────────────────   │    │
                     │  │        │                      │    │
                     │  │ EN ────┤  ← R1 (100kΩ) →VIN │    │
                     │  │        │                      │    │
                     │  │ BOOT ──┤  CBOOT 100nF        │    │
                     │  │        │                      │    │
                     │  │ SW ────┤──── L1 (33µH) ──┐   │    │
                     │  │        │                  │   │    │
                     │  │ GND ───┤                  │   │    │
                     │  └────────┘                  │   │    │
                     │                              │   │    │
                     │                         ┌────┴───┘   │
                     │                         │            │
                     │                    ┌────┴────┐       │
                     │                    │  C2     │ 220µF │
                     │                    │         │ 16V   │
                     │                    └────┬────┘       │
                     │                         │            │
                     │                    ┌────┴────┐       │
                     │                    │  FB     │       │
                     │                    │  Divider│       │
                     │                    │  R2=10kΩ│       │
                     │                    │  R3=2.49kΩ│     │
                     │                    │  Vout=12V │     │
                     │                    └────┬────┘       │
                     └─────────────────────────│────────────┘
                                               │
                                          12V OUTPUT
                                          (10A max)
```

### 2.3 Buck Converter Circuit (48V→5V, 6A)

```
                         48V
                          │
                     ┌────┴────┐
                     │  C1     │ 100µF, 63V electrolytic
                     └────┬────┘
                          │
                     ┌────┴─────────────────────────────────┐
                     │  ┌──────────────────────────────┐    │
                     │  │     LM5146 (TI)             │    │
                     │  │     48V→5V, 6A, 95%          │    │
                     │  │     Synchronous Buck          │    │
                     │  │                              │    │
                     │  │ VIN ──────────────────       │    │
                     │  │ EN ──── R1 (100kΩ) →VIN     │    │
                     │  │ BOOT ── CBOOT 100nF          │    │
                     │  │ SW ───── L1 (15µH) ──┐       │    │
                     │  │ GND ──────           │       │    │
                     │  └──────────────────────│───────┘    │
                     │                         │            │
                     │                    ┌────┴────┐       │
                     │                    │  C2     │ 470µF │
                     │                    │         │ 10V   │
                     │                    └────┬────┘       │
                     │                    ┌────┴────┐       │
                     │                    │  FB     │       │
                     │                    │  R2=10kΩ│       │
                     │                    │  R3=3.24kΩ│     │
                     │                    │  Vout=5V  │     │
                     │                    └────┬────┘       │
                     └─────────────────────────│────────────┘
                                               │
                                           5V OUTPUT
                                           (6A max)
```

---

## 3. Sensor Hub PCB — Detailed Schematic

### 3.1 STM32H7 Interface

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    STM32H743VIT6 — SENSOR HUB #1 (LEGS)                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  POWER                                                                  │
│  ├── 3.3V Rail (from LDO)                                              │
│  ├── Decoupling: 10µF + 100nF per VDD pin (×8)                        │
│  ├── VBAT: 3V coin cell (backup RTC)                                   │
│  └── VREF: 3.3V via 10Ω + 100nF filter                                │
│                                                                         │
│  SPI BUS 1 (ENCODERS)                                                   │
│  ├── PA5  → SPI1_SCK   → Level shift (3.3V→1.8V) → AS5048A #1-12    │
│  ├── PA6  → SPI1_MISO  ← Level shift ← AS5048A data out              │
│  ├── PA7  → SPI1_MOSI  → Level shift → AS5048A data in               │
│  ├── PA4  → GPIO → CS1 (Hip Left HAA)                                │
│  ├── PA3  → GPIO → CS2 (Hip Left HFE)                                │
│  ├── PA2  → GPIO → CS3 (Knee Left KFE)                               │
│  ├── PA1  → GPIO → CS4 (Knee Left KAA)                               │
│  ├── PA0  → GPIO → CS5 (Ankle Left AFE)                              │
│  ├── PC3  → GPIO → CS6 (Toe Left)                                    │
│  ├── PC2  → GPIO → CS7 (Hip Right HAA)                               │
│  ├── PC1  → GPIO → CS8 (Hip Right HFE)                               │
│  ├── PC0  → GPIO → CS9 (Knee Right KFE)                              │
│  ├── PC13 → GPIO → CS10 (Knee Right KAA)                             │
│  ├── PC14 → GPIO → CS11 (Ankle Right AFE)                            │
│  └── PC15 → GPIO → CS12 (Toe Right)                                  │
│                                                                         │
│  SPI BUS 2 (FORCE SENSORS)                                              │
│  ├── PB10 → SPI2_SCK  → ADS1256 SCLK                                 │
│  ├── PB14 → SPI2_MISO ← ADS1256 DOUT                                 │
│  ├── PB15 → SPI2_MOSI → ADS1256 DIN                                  │
│  ├── PB12 → GPIO → ADS1256 CS (Left foot)                             │
│  └── PB13 → GPIO → ADS1256 CS (Right foot)                            │
│                                                                         │
│  I2C BUS (POWER MONITORING)                                             │
│  ├── PB8  → I2C1_SCL → INA260 #1-4                                   │
│  ├── PB9  → I2C1_SDA → INA260 #1-4                                   │
│  └── Pull-ups: 4.7kΩ to 3.3V                                          │
│                                                                         │
│  UART (DEBUG)                                                           │
│  ├── PA9  → USART1_TX → USB-UART bridge (debug)                       │
│  └── PA10 → USART1_RX → USB-UART bridge (debug)                       │
│                                                                         │
│  CAN BUS (MOTOR CONTROL)                                                │
│  ├── PD0  → CAN1_RX → MCP2515 → CAN transceiver (TJA1050)            │
│  └── PD1  → CAN1_TX → MCP2515 → CAN transceiver (TJA1050)            │
│                                                                         │
│  GPIO (MISC)                                                            │
│  ├── PE0  → GPIO → Emergency stop input (NC)                          │
│  ├── PE1  → GPIO → Status LED (green)                                  │
│  ├── PE2  → GPIO → Status LED (red)                                    │
│  ├── PE3  → GPIO → Cooling fan PWM                                     │
│  └── PE4  → GPIO → Buzzer output                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 ADS1256 24-Bit ADC Circuit (Force Sensors)

```
                         3.3V
                          │
                     ┌────┴────┐
                     │  10µF   │ + 100nF decoupling
                     └────┬────┘
                          │
              ┌───────────┴───────────┐
              │                       │
    ┌─────────┴───────────────────────┴─────────┐
    │              ADS1256 (TI)                 │
    │              24-bit ADC                   │
    │              30kHz sampling               │
    │                                           │
    │  VDD ─── 3.3V                             │
    │  VREF ── 2.5V (internal ref)             │
    │  AVDD ── 5V (analog supply)              │
    │                                           │
    │  AIN0 ←── FSR406 (Heel)                  │
    │           Voltage divider:                │
    │           3.3V → FSR → 10kΩ → GND        │
    │           Vout = 3.3V × (Rfsr / (Rfsr + 10kΩ)) │
    │                                           │
    │  AIN1 ←── FSR406 (Ball-Lateral)          │
    │  AIN2 ←── FSR406 (Ball-Center)           │
    │  AIN3 ←── FSR406 (Ball-Medial)           │
    │                                           │
    │  AIN4 ←── FSR406 (Thumb)                 │
    │  AIN5 ←── FSR406 (Index)                 │
    │  AIN6 ←── FSR406 (Middle)                │
    │  AIN7 ←── FSR406 (Ring/Pinky)            │
    │                                           │
    │  DRDY → STM32 GPIO (data ready)          │
    │  CS   → STM32 GPIO (chip select)         │
    │  SCLK → SPI2_SCK                         │
    │  DIN  → SPI2_MOSI                        │
    │  DOUT ← SPI2_MISO                        │
    │                                           │
    │  CLKIN ← 7.68MHz crystal                 │
    │                                           │
    └───────────────────────────────────────────┘

    FSR VOLTAGE DIVIDER DETAIL:
    ┌────────────────────────────────────────────────┐
    │                                                │
    │  3.3V ──┬── FSR406 ──┬── 10kΩ ──┬── GND      │
    │         │            │          │              │
    │         └── Vout ────┘          │              │
    │              │                   │              │
    │              └── To ADS1256 AINx │              │
    │                                                │
    │  When no force: Rfsr ≈ ∞, Vout ≈ 3.3V         │
    │  When 100N force: Rfsr ≈ 100Ω, Vout ≈ 0.033V │
    │  ADC resolution: 3.3V / 2²⁴ ≈ 0.2µV          │
    │  Force resolution: ≈ 0.001N (1mN)             │
    │                                                │
    └────────────────────────────────────────────────┘
```

### 3.3 AS5048A Magnetic Encoder Circuit

```
                         3.3V
                          │
                     ┌────┴────┐
                     │  100nF  │ + 10µF decoupling
                     └────┬────┘
                          │
              ┌───────────┴───────────┐
              │                       │
    ┌─────────┴───────────────────────┴─────────┐
    │              AS5048A (AMS)                │
    │              14-bit magnetic encoder       │
    │                                           │
    │  VDD ─── 3.3V                             │
    │  GND ─── GND                              │
    │                                           │
    │  SCK  ← SPI_SCK (STM32)                  │
    │  SDO  → SPI_MISO (STM32)                 │
    │  SDI  ← SPI_MOSI (STM32)                 │
    │  CSn  ← GPIO (STM32, active low)         │
    │                                           │
    │  MAG  → Diagnostic output (optional)      │
    │  AUTH → Authentication output (optional)  │
    │                                           │
    │  ┌─────────────────────────────┐          │
    │  │    DIPOLE MAGNET            │          │
    │  │    6mm diameter             │          │
    │  │    N-S aligned with shaft   │          │
    │  │    1mm above IC             │          │
    │  └─────────────────────────────┘          │
    │                                           │
    │  Resolution: 14-bit (16384 positions/rev) │
    │  Accuracy: ±0.1°                          │
    │  Update rate: up to 10kHz                 │
    │  SPI clock: up to 10MHz                   │
    │                                           │
    └───────────────────────────────────────────┘

    ENCODER MOUNTING DETAIL:
    ┌────────────────────────────────────────────────┐
    │                                                │
    │    ┌───────────────────────┐                   │
    │    │   AS5048A PCB        │ ← 20mm × 20mm     │
    │    │   (mounted on shaft) │                   │
    │    └───────────┬───────────┘                   │
    │                │                               │
    │         ┌──────┴──────┐                        │
    │         │  Dipole     │ ← 6mm dia, 3mm thick   │
    │         │  Magnet     │                        │
    │         └──────┬──────┘                        │
    │                │                               │
    │         ┌──────┴──────┐                        │
    │         │  Motor Shaft│ ← D-shaft, 8mm         │
    │         │             │                        │
    │         └─────────────┘                        │
    │                                                │
    │    Air gap: 0.5mm - 1.5mm (optimal: 1mm)      │
    │                                                │
    └────────────────────────────────────────────────┘
```

### 3.4 INA260 Current/Voltage Monitor Circuit

```
                         3.3V
                          │
                     ┌────┴────┐
                     │  100nF  │ decoupling
                     └────┬────┘
                          │
              ┌───────────┴───────────┐
              │                       │
    ┌─────────┴───────────────────────┴─────────┐
    │              INA260 (TI)                  │
    │              Current/Voltage/Power         │
    │                                           │
    │  VBUS ─── To voltage source (48V or 12V) │
    │  IN+  ─── To current path (high side)    │
    │  IN-  ─── To current path (load side)    │
    │                                           │
    │  VDD  ─── 3.3V                            │
    │  GND  ─── GND                             │
    │                                           │
    │  SCL  ← I2C_SCL (RPi/STM32)             │
    │  SDA  ↔ I2C_SDA (RPi/STM32)             │
    │  ALERT → STM32 GPIO (optional)           │
    │                                           │
    │  Address pins: A0, A1 (via pull-up/down) │
    │    #1: 0x40 (A0=GND, A1=GND)            │
    │    #2: 0x41 (A0=VDD, A1=GND)            │
    │    #3: 0x42 (A0=GND, A1=VDD)            │
    │    #4: 0x43 (A0=VDD, A1=VDD)            │
    │                                           │
    │  Shunt resistor: Internal (2mΩ)          │
    │  Current range: 0-15A (continuous)        │
    │  Voltage range: 0-36V                     │
    │  Resolution: 1.25mA / 1.25mV             │
    │                                           │
    └───────────────────────────────────────────┘

    WIRING DETAIL:
    ┌────────────────────────────────────────────────┐
    │                                                │
    │  48V SOURCE ──┬── INA260 IN+ ── INA260 IN- ──┬── LOAD (ODrive)  │
    │               │                              │                   │
    │               └── INA260 VBUS               │                   │
    │                                                │
    │  Note: INA260 has internal shunt,            │
    │  no external shunt resistor needed.           │
    │                                                │
    └────────────────────────────────────────────────┘
```

---

## 4. Motor Controller Interface

### 4.1 ODrive S1 Channel Wiring

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ODrive S1 — SINGLE CHANNEL FOC                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  POWER INPUT                                                            │
│  ├── VBUS+ ←── 48V bus (via 20A fuse)                                 │
│  ├── VBUS- ←── GND bus                                                 │
│  └── Decoupling: 100µF + 10µF + 100nF (on VBUS)                       │
│                                                                         │
│  MOTOR OUTPUT                                                           │
│  ├── M0 ─── Phase A (Blue)  → Motor terminal A                        │
│  ├── M1 ─── Phase B (Green) → Motor terminal B                        │
│  └── M2 ─── Phase C (Yellow)→ Motor terminal C                        │
│                                                                         │
│  ENCODER INPUT                                                          │
│  ├── ENC_A ←── AS5048A SDO (via level shift)                          │
│  ├── ENC_B ←── (optional second encoder)                               │
│  ├── ENC_Z ←── (optional index pulse)                                  │
│  └── 5V out → Encoder power                                            │
│                                                                         │
│  CAN BUS                                                                │
│  ├── CAN_H ──→ CAN bus trunk (120Ω termination)                       │
│  └── CAN_L ──→ CAN bus trunk                                           │
│                                                                         │
│  USB (configuration only)                                               │
│  └── USB-C → RPi 5 (via hub) for initial config                       │
│                                                                         │
│  GPIO                                                                   │
│  ├── GPIO1 ←── Emergency stop (active low)                             │
│  ├── GPIO2 ←── Limit switch (optional)                                 │
│  └── GPIO3 →── Status LED                                               │
│                                                                         │
│  CURRENT SENSE                                                          │
│  ├── Internal shunt resistors (1mΩ)                                    │
│  └── 3-phase current measurement (16-bit ADC)                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 CAN Bus Transceiver Circuit

```
    ODrive CAN_H ──────┬─────────────────────── CAN_H (bus)
                       │
                  ┌────┴────┐
                  │  120Ω   │ ← Termination resistor
                  │         │   (at one end only)
                  └────┬────┘
                       │
    ODrive CAN_L ──────┴─────────────────────── CAN_L (bus)

    SHIELDED CABLE:
    ┌────────────────────────────────────────┐
    │  Shield drain wire → GND at ONE end   │
    │  Characteristic impedance: 120Ω        │
    │  Max length: 40m (at 500kbps)          │
    └────────────────────────────────────────┘
```

---

## 5. Audio Circuit

### 5.1 Microphone Array Circuit

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    4-CHANNEL MICROPHONE ARRAY                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────────┐                                                      │
│  │  INMP441 #1  │  I2S Digital MEMS Microphone                        │
│  │  (Front)     │                                                      │
│  │  VDD=3.3V    │                                                      │
│  │  SD=GPIO20   │──────┐                                               │
│  │  SCK=GPIO18  │──────┤                                               │
│  │  WS=GPIO19   │──────┤                                               │
│  └──────────────┘      │                                               │
│                         │                                               │
│  ┌──────────────┐      │                                               │
│  │  INMP441 #2  │  I2S │                                               │
│  │  (Right)     │      │                                               │
│  │  SD=GPIO21   │──────┤                                               │
│  └──────────────┘      │                                               │
│                         │                                               │
│  ┌──────────────┐      │                                               │
│  │  INMP441 #3  │  I2S │                                               │
│  │  (Left)      │      │                                               │
│  │  SD=GPIO22   │──────┤                                               │
│  └──────────────┘      │                                               │
│                         │                                               │
│  ┌──────────────┐      │                                               │
│  │  INMP441 #4  │  I2S │                                               │
│  │  (Rear)      │      │                                               │
│  │  SD=GPIO23   │──────┘                                               │
│  └──────────────┘                                                      │
│                                                                         │
│  SPACING: 40mm × 40mm square array (φ-optimized for beamforming)      │
│  SAMPLING: 48kHz, 24-bit                                               │
│  SNR: 61dB                                                              │
│                                                                         │
│  RPi 5 I2S CONFIGURATION:                                              │
│  ├── BCLK: GPIO18 (shared)                                             │
│  ├── LRCLK/WS: GPIO19 (shared)                                        │
│  ├── SD1: GPIO20 (Mic 1 data)                                         │
│  ├── SD2: GPIO21 (Mic 2 data)                                         │
│  ├── SD3: GPIO22 (Mic 3 data)                                         │
│  └── SD4: GPIO23 (Mic 4 data)                                         │
│                                                                         │
│  BEAMFORMING:                                                           │
│  ├── 4-channel delay-and-sum beamformer                                │
│  ├── φ-weighted coefficients (1, φ, φ², φ³ normalized)               │
│  ├── Noise floor: -90dBFS                                              │
│  └── Voice activity detection at 3m range                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Speaker Amplifier Circuit

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SPEAKER OUTPUT (×2 channels)                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  RPi 5 I2S → MAX98357A → Speaker                                       │
│                                                                         │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐           │
│  │  RPi 5       │     │  MAX98357A   │     │  SPEAKER     │           │
│  │  I2S         │     │  Class-D Amp │     │  3W, 8Ω     │           │
│  │  BCLK=GPIO18 │────→│  BCLK        │     │  40mm driver │           │
│  │  LRCLK=GPIO19│────→│  LRC         │     │              │           │
│  │  DIN=GPIO21  │────→│  DIN         │     │              │           │
│  │              │     │  GAIN=12dB   │     │              │           │
│  │              │     │  SD_MODE=High│     │              │           │
│  │              │     │  OUT+ ───────│────→│  Speaker +   │           │
│  │              │     │  OUT- ───────│────→│  Speaker -   │           │
│  └──────────────┘     └──────────────┘     └──────────────┘           │
│                                                                         │
│  MAX98357A CONFIGURATION:                                              │
│  ├── Gain: 12dB (GAIN pin tied to VDD)                                │
│  ├── SD_MODE: High (auto-shutdown)                                    │
│  ├── Output: 3.2W into 4Ω, 1.5W into 8Ω                              │
│  ├── THD+N: 0.015%                                                     │
│  ├── PSRR: 80dB                                                        │
│  └── Supply: 5V from USB bus, 600mA peak                               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Eye Display Circuit

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    OLED EYE DISPLAYS (×2)                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────────┐     ┌──────────────┐                                │
│  │  RPi 5       │     │  SSD1306     │                                │
│  │  I2C-0       │     │  0.96" OLED  │                                │
│  │  SDA=GPIO2   │────→│  SDA         │  LEFT EYE                      │
│  │  SCL=GPIO3   │────→│  SCL         │  Address: 0x3C                 │
│  │              │     │  VCC=3.3V    │  128×64 pixels                 │
│  └──────────────┘     │  GND=GND     │                                │
│                        └──────────────┘                                │
│                                                                         │
│  ┌──────────────┐     ┌──────────────┐                                │
│  │  RPi 5       │     │  SSD1306     │                                │
│  │  I2C-0       │     │  0.96" OLED  │                                │
│  │  SDA=GPIO2   │────→│  SDA         │  RIGHT EYE                     │
│  │  SCL=GPIO3   │────→│  SCL         │  Address: 0x3D                 │
│  │              │     │  VCC=3.3V    │  128×64 pixels                 │
│  └──────────────┘     │  GND=GND     │                                │
│                        └──────────────┘                                │
│                                                                         │
│  DISPLAY CONTENT:                                                       │
│  ├── Eye animation (blinking, expressions)                             │
│  ├── Status indicators (battery, mode, errors)                         │
│  └── φ-harmonic geometric patterns (idle state)                        │
│                                                                         │
│  I2C PULL-UPS: 4.7kΩ to 3.3V (both lines)                            │
│  I2C SPEED: 400kHz                                                      │
│  POWER: 3.3V, 20mA per display                                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Battery Monitoring Circuit

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BATTERY MONITORING                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  FPB-10 BATTERY #1                                                     │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Internal BMS (built into FPB-10)                               │  │
│  │  ├── Cell balancing: Active balancing                            │  │
│  │  ├── Overcharge protection: 3.65V/cell                          │  │
│  │  ├── Overdischarge protection: 2.5V/cell                        │  │
│  │  ├── Overcurrent protection: 50A                                │  │
│  │  ├── Short circuit protection: Yes                               │  │
│  │  ├── Temperature cutoff: 60°C                                   │  │
│  │  └── Communication: CAN bus (BMS status)                        │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  EXTERNAL MONITORING:                                                   │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  INA260 #1 monitors total pack voltage and current              │  │
│  │  ├── Voltage measurement: 0-53V (48V nominal)                   │  │
│  │  ├── Current measurement: 0-100A (bidirectional)                │  │
│  │  ├── Power calculation: V × I (1.25mW resolution)               │  │
│  │  └── Integration: Coulomb counting for SOC estimation           │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  SOC ESTIMATION:                                                        │
│  ├── Method: Coulomb counting + voltage lookup                         │
│  ├── Initial calibration: Full charge voltage mapping                  │
│  ├── Update rate: 10Hz (via I2C polling)                              │
│  └── Accuracy: ±3% (with periodic recalibration)                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Emergency Stop Circuit

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    EMERGENCY STOP CIRCUIT                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  HARDWARE E-STOP (DUAL REDUNDANT):                                     │
│                                                                         │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐           │
│  │  E-STOP      │     │  E-STOP      │     │  MAIN        │           │
│  │  BUTTON #1   │     │  BUTTON #2   │     │  CONTACTOR   │           │
│  │  (Head)      │     │  (Torso)     │     │  (100A)      │           │
│  │              │     │              │     │              │           │
│  │  NC contact  │     │  NC contact  │     │  Coil: 48V   │           │
│  │  30A rated   │     │  30A rated   │     │  Latching     │           │
│  └──────┬───────┘     └──────┬───────┘     └──────┬───────┘           │
│         │                    │                    │                     │
│         │  SERIES WIRING:    │                    │                     │
│         │  Both must be      │                    │                     │
│         │  CLOSED for robot  │                    │                     │
│         │  to operate.       │                    │                     │
│         │                    │                    │                     │
│         └────────────────────┴────────────────────┘                     │
│                                                                         │
│  SOFTWARE E-STOP:                                                       │
│  ├── RPi 5 GPIO24 → Contactor coil driver (MOSFET)                    │
│  ├── Can open contactor via software (in addition to hardware)         │
│  └── Watchdog: If RPi hangs, contactor opens after 2 seconds          │
│                                                                         │
│  FAILOPEN DESIGN:                                                       │
│  ├── E-stop buttons are NC (normally closed)                           │
│  ├── Wiring break = contactor opens (safe state)                       │
│  ├── Software failure = contactor opens (watchdog timeout)             │
│  └── Power loss = contactor opens (failsafe)                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 9. PCB Specifications

### 9.1 Power Distribution PCB

| Parameter | Value |
|-----------|-------|
| Layers | 4 |
| Board size | 120mm × 80mm |
| Copper weight | 2oz (outer), 2oz (inner) |
| Material | FR-4, Tg 170°C |
| Min trace width | 100µm (signal), 5mm (power) |
| Min drill | 0.3mm |
| Surface finish | ENIG |
| Solder mask | Black |
| Silk | White, φ-ratio labeling |

### 9.2 Sensor Hub PCB

| Parameter | Value |
|-----------|-------|
| Layers | 4 |
| Board size | 80mm × 60mm |
| Copper weight | 1oz |
| Material | FR-4, Tg 150°C |
| Min trace width | 75µm |
| Min drill | 0.2mm |
| Surface finish | ENIG |
| Solder mask | Blue |
| Analog/digital split ground planes | Yes |

### 9.3 Foot Sensor PCB

| Parameter | Value |
|-----------|-------|
| Layers | 2 |
| Board size | 240mm × 90mm (foot-shaped) |
| Copper weight | 1oz |
| Material | FR-4, flexible bend area |
| Waterproofing | Conformal coat, IP54 |
| FSR mounting | Recessed pockets, adhesive |

---

*Document: 04_CIRCUIT.md — PHI_HUMANOID_ROBOT Circuit Design*
*Version: 1.0 | Date: 2026-08-27*
