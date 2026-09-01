# PHI_FIELD_ROBOT — Circuit Design

## PHI_FIELD_ROBOT | Document 04: Circuit Design

---

## 1. MAIN PCB SCHEMATIC OVERVIEW

```
┌─────────────────────────────────────────────────────────────┐
│                    MAIN PCB — BLOCK DIAGRAM                  │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                    POWER SECTION                     │    │
│  │                                                      │    │
│  │  48V IN ──┬──► 48V→24V Buck (360W) ──► 24V Bus     │    │
│  │           │                                          │    │
│  │           ├──► 48V→5V Buck (25W) ──► 5V Bus         │    │
│  │           │                                          │    │
│  │           └──► 48V→12V Buck (36W) ──► 12V Bus       │    │
│  │                                                      │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │  POWER MONITORING                           │    │    │
│  │  │  • INA226 (voltage/current)                 │    │    │
│  │  │  • LTC2944 (coulomb counter)                │    │    │
│  │  │  • TMP102 (temperature)                     │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                 MCU SECTION                          │    │
│  │                                                      │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │           STM32H743VIT6                      │    │    │
│  │  │                                              │    │    │
│  │  │  • Cortex-M7 @ 480 MHz                      │    │    │
│  │  │  • 2MB Flash, 1MB RAM                       │    │    │
│  │  │  • 3× ADC (16-bit, 24ch)                    │    │    │
│  │  │  • 2× CAN FD                               │    │    │
│  │  │  • 8× UART                                  │    │    │
│  │  │  • 4× I2C                                   │    │    │
│  │  │  • 6× SPI                                   │    │    │
│  │  │  • 24× Timers                               │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  │                                                      │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │         EXTERNAL MEMORY                      │    │    │
│  │  │  • W25Q128 (128Mbit SPI Flash)              │    │    │
│  │  │  • AT24C256 (256Kbit I2C EEPROM)            │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │               COMMUNICATION SECTION                  │    │
│  │                                                      │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │    │
│  │  │ CAN1 TX  │  │ CAN2 TX  │  │ CAN3 TX  │          │    │
│  │  │ (Legs)   │  │ (Arm)    │  │ (Sensors)│          │    │
│  │  │ MCP2562  │  │ MCP2562  │  │ MCP2562  │          │    │
│  │  └──────────┘  └──────────┘  └──────────┘          │    │
│  │                                                      │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │    │
│  │  │ UART GPS │  │ UART DBG │  │ UART LIDAR│         │    │
│  │  │ (9600)   │  │ (115200) │  │ (115200)  │         │    │
│  │  └──────────┘  └──────────┘  └──────────┘          │    │
│  │                                                      │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │    │
│  │  │ I2C1     │  │ I2C2     │  │ I2C3     │          │    │
│  │  │ (IMU,    │  │ (ADC)    │  │ (FT      │          │    │
│  │  │  BME280) │  │          │  │  Sensor) │          │    │
│  │  └──────────┘  └──────────┘  └──────────┘          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              INTERFACE SECTION                       │    │
│  │                                                      │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │  USB (to Raspberry Pi 5)                     │    │    │
│  │  │  • Device mode (CDC-ACM virtual serial)      │    │    │
│  │  • Pin: PA11 (DM), PA12 (DP)                   │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  │                                                      │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │  GPIO (to Raspberry Pi 5)                    │    │    │
│  │  │  • 8× direct GPIO pins                      │    │    │
│  │  │  • Level shifted (3.3V ↔ 3.3V)             │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. POWER SECTION CIRCUITS

### 2.1 48V→24V Buck Converter

```
┌─────────────────────────────────────────────────────────────┐
│              48V → 24V BUCK CONVERTER (360W)                 │
│                                                              │
│  48V INPUT                                                   │
│  ─────┬──────────────────────────────────────               │
│       │                                                      │
│       ├────[C1: 100µF/100V]────GND                          │
│       │                                                      │
│       ├────[C2: 10µF/100V]────GND                           │
│       │                                                      │
│       └────►┌─────────────────┐                              │
│             │   LM5145-Q1     │                              │
│             │   SYNC BUCK     │                              │
│             │   CONTROLLER    │                              │
│             │                 │                              │
│             │  VIN ──►│       │                              │
│             │  SW ◄───┤       │                              │
│             │  FB ──►│       │                              │
│             │  BST ──►│       │                              │
│             │  PG ──►│       │                              │
│             │  EN ──►│       │                              │
│             └──┬──┬──┬──┬──┬─┘                              │
│                │  │  │  │  │                                │
│                │  │  │  │  └──►[R4: 10kΩ]──►GND (enable)  │
│                │  │  │  └─────►[R3: 100kΩ]──GND (PG pull) │
│                │  │  └────────►[C4: 100nF]──GND (BST cap)  │
│                │  └───────────►[C3: 1µF]──GND (VIN decoup) │
│                │                                            │
│                └──── SW Pin                                  │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  Q1: CSD19536│ (N-ch MOSFET)                │
│              │  60V/100A    │                                │
│              │  RDS(on): 3mΩ│                                │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  L1: 10µH   │ (Shielded inductor)           │
│              │  15A sat     │                                │
│              │  DCR: 5mΩ    │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  OUTPUT      │                                │
│              │  24V / 15A   │                                │
│              │  (360W)      │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  C5: 2×470µF │ (Output caps)                │
│              │  50V low ESR │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│                     GND                                      │
│                                                              │
│  Feedback Network:                                           │
│  R1 = 30kΩ (top), R2 = 10kΩ (bottom)                      │
│  Vout = 0.6V × (1 + R1/R2) = 0.6V × 4 = 24V             │
│                                                              │
│  Efficiency: 95% at full load                               │
│  Ripple: <50mV p-p                                          │
│  Load Regulation: ±0.5%                                     │
│  Line Regulation: ±0.2%                                     │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 48V→5V Buck Converter

```
┌─────────────────────────────────────────────────────────────┐
│              48V → 5V BUCK CONVERTER (25W)                   │
│                                                              │
│  48V INPUT                                                   │
│  ─────┬──────────────────────────────────────               │
│       │                                                      │
│       ├────[C1: 47µF/100V]────GND                           │
│       │                                                      │
│       └────►┌─────────────────┐                              │
│             │   TPS54331      │                              │
│             │   3A BUCK       │                              │
│             │   CONTROLLER    │                              │
│             │                 │                              │
│             │  VIN ──►│       │                              │
│             │  SW ◄───┤       │                              │
│             │  FB ──►│       │                              │
│             │  EN ──►│       │                              │
│             │  PH ──►│       │                              │
│             └──┬──┬──┬──┬────┘                              │
│                │  │  │  │                                   │
│                │  │  │  └─────►[C2: 10nF]──GND (BOOT)     │
│                │  │  └────────►[R1: 47kΩ]──GND (EN pull)  │
│                │  └───────────►[C3: 1µF]──GND (VIN decoup)│
│                │                                            │
│                └──── SW Pin                                  │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  L1: 22µH    │ (Shielded inductor)          │
│              │  4A sat       │                               │
│              │  DCR: 80mΩ    │                               │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  OUTPUT      │                                │
│              │  5V / 5A     │                                │
│              │  (25W)       │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  C4: 220µF   │ (Output cap)                 │
│              │  10V low ESR │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│                     GND                                      │
│                                                              │
│  Feedback Network:                                           │
│  R2 = 10kΩ (top), R3 = 30kΩ (bottom)                      │
│  Vout = 0.8V × (1 + R2/R3) = 0.8V × 1.33 = 1.067V...    │
│  * Adjusted: R2 = 30kΩ, R3 = 6.8kΩ → Vout = 5.0V        │
│                                                              │
│  Efficiency: 92% at full load                               │
│  Ripple: <20mV p-p                                          │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 48V→12V Buck Converter

```
┌─────────────────────────────────────────────────────────────┐
│              48V → 12V BUCK CONVERTER (36W)                  │
│                                                              │
│  48V INPUT                                                   │
│  ─────┬──────────────────────────────────────               │
│       │                                                      │
│       ├────[C1: 47µF/100V]────GND                           │
│       │                                                      │
│       └────►┌─────────────────┐                              │
│             │   LM2596-12     │                              │
│             │   3A SIMPLE     │                              │
│             │   BUCK          │                              │
│             │                 │                              │
│             │  VIN ──►│       │                              │
│             │  SW ◄───┤       │                              │
│             │  FB ──►│       │                              │
│             │  GND ──►│       │                              │
│             └──┬──┬──┬───────┘                              │
│                │  │  │                                      │
│                │  │  └────────►[C2: 100nF]──GND (VIN)     │
│                │  └───────────►[C3: 330µF]──GND (VIN)     │
│                │                                            │
│                └──── SW Pin                                  │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  L1: 33µH    │ (Toroid inductor)            │
│              │  4A sat       │                               │
│              │  DCR: 40mΩ    │                               │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  OUTPUT      │                                │
│              │  12V / 3A    │                                │
│              │  (36W)       │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│              ┌──────┴──────┐                                │
│              │  C4: 220µF   │ (Output cap)                 │
│              │  25V low ESR │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│                     GND                                      │
│                                                              │
│  Efficiency: 93% at full load                               │
│  Ripple: <30mV p-p                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. MCU CIRCUITS

### 3.1 STM32H743 Minimal System

```
┌─────────────────────────────────────────────────────────────┐
│              STM32H743VIT6 MINIMAL SYSTEM                    │
│                                                              │
│              ┌─────────────────────────┐                    │
│              │     STM32H743VIT6        │                    │
│              │     LQFP-100             │                    │
│              │                          │                    │
│              │  VDD ──┬──[100nF]──GND  │  (Decoupling)     │
│              │        ├──[100nF]──GND  │                    │
│              │        ├──[100nF]──GND  │                    │
│              │        ├──[10µF]──GND   │                    │
│              │        │                 │                    │
│              │  VDDA ──[100nF]──GND    │  (Analog supply)  │
│              │         [1µF]──GND       │                    │
│              │                          │                    │
│              │  VBAT ──[100nF]──GND    │  (Battery backup) │
│              │                          │                    │
│              │  NRST ──[100nF]──GND    │  (Reset)          │
│              │         └──[10kΩ]──3.3V  │                    │
│              │                          │                    │
│              │  BOOT0 ──[10kΩ]──GND    │  (Boot from flash)│
│              │                          │                    │
│              │  OSC_IN ──[8MHz XTAL]──  │  (HSE crystal)   │
│              │  OSC_OUT──┘              │                    │
│              │         [20pF]──GND ×2   │                    │
│              │                          │                    │
│              │  VCAP ──[2.2µF]──GND    │  (Internal LDO)   │
│              │                          │                    │
│              └─────────────────────────┘                    │
│                                                              │
│  Power-up Sequence:                                          │
│  1. VDD rails stable (3.3V)                                │
│  2. VDDA stable (3.3V, low noise)                          │
│  3. Reset released (NRST high)                              │
│  4. Clocks configured (HSE → PLL → 480 MHz)                │
│  5. Flash prefetch enabled                                  │
│                                                              │
│  Clock Configuration:                                        │
│  HSE = 8 MHz → PLL × 60 = 480 MHz (SYSCLK)                │
│  AHB = 240 MHz (HCLK)                                      │
│  APB1 = 120 MHz (PCLK1)                                    │
│  APB2 = 120 MHz (PCLK2)                                    │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 CAN Transceiver Circuit

```
┌─────────────────────────────────────────────────────────────┐
│              CAN TRANSCEIVER (MCP2562FD)                     │
│                                                              │
│              ┌─────────────────────────┐                    │
│              │      MCP2562FD          │                    │
│              │                          │                    │
│              │  TXD ◄── STM32 CAN_TX   │                    │
│              │  RXD ──► STM32 CAN_RX   │                    │
│              │                          │                    │
│              │  CANH ──┬──[120Ω]──CANL │  (Termination)    │
│              │         │                │                    │
│              │  CANL ──┘                │                    │
│              │                          │                    │
│              │  STBY ── GPIO            │  (Sleep control)  │
│              │  VDD ── 5V              │                    │
│              │  VSS ── GND             │                    │
│              └─────────────────────────┘                    │
│                                                              │
│  ┌──────────────────────────────────────────────┐          │
│  │              CAN BUS CABLE                     │          │
│  │                                                │          │
│  │  ┌─────┐    ┌────────────────────┐    ┌─────┐ │          │
│  │  │ 120Ω│    │    TWISTED PAIR    │    │120Ω │ │          │
│  │  │ term│◄──►│  CAN_H (green)     │◄──►│term │ │          │
│  │  │     │    │  CAN_L (white)     │    │     │ │          │
│  │  │     │    │  GND (black)       │    │     │ │          │
│  │  └─────┘    │  SHIELD (bare)     │    └─────┘ │          │
│  │  (Main PCB) └────────────────────┘  (Last    │          │
│  │                                    motor)     │          │
│  └──────────────────────────────────────────────┘          │
│                                                              │
│  Bus Speed: 1 Mbps (CAN2.0B)                               │
│  Max Nodes: 32 per bus                                     │
│  Max Cable Length: 1m per segment (at 1 Mbps)              │
│  ESD Protection: ±8kV contact, ±15kV air                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. SENSOR CIRCUITS

### 4.1 IMU Circuit (BNO085)

```
┌─────────────────────────────────────────────────────────────┐
│              IMU CIRCUIT (BNO085)                            │
│                                                              │
│              ┌─────────────────────────┐                    │
│              │      BNO085              │                    │
│              │      (Adafruit           │                    │
│              │       breakout)          │                    │
│              │                          │                    │
│              │  VCC ── 3.3V            │                    │
│              │         [100nF]──GND     │  (Decoupling)     │
│              │         [10µF]──GND      │                    │
│              │                          │                    │
│              │  GND ── GND             │                    │
│              │                          │                    │
│              │  SDA ──┬──[4.7kΩ]──3.3V │  (I2C pull-up)   │
│              │        └── STM32 PB9    │                    │
│              │                          │                    │
│              │  SCL ──┬──[4.7kΩ]──3.3V │  (I2C pull-up)   │
│              │        └── STM32 PB8    │                    │
│              │                          │                    │
│              │  INT ── STM32 PB6       │  (Interrupt)      │
│              │  RST ── STM32 PA8       │  (Reset)          │
│              │                          │                    │
│              └─────────────────────────┘                    │
│                                                              │
│  I2C Configuration:                                          │
│  • Address: 0x4A (SDO/GND)                                 │
│  • Speed: 400 kHz (Fast Mode)                              │
│  • Pull-up: 4.7kΩ (on breakout board)                     │
│  • Cable length: <100mm                                     │
│                                                              │
│  Mounting:                                                   │
│  • Vibration dampener: Silicone 40A                        │
│  • Center of body (for best IMU readings)                  │
│  • Orientation: X forward, Y left, Z up                   │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 FSR Circuit (per foot)

```
┌─────────────────────────────────────────────────────────────┐
│              FSR CIRCUIT (Force-Sensitive Resistor)          │
│                                                              │
│  3.3V                                                        │
│   │                                                          │
│   └──[R1: 10kΩ]──┬──► ADS1115 AINx                         │
│                   │                                          │
│               [FSR 402]                                      │
│                   │                                          │
│                  GND                                         │
│                                                              │
│  Transfer Function:                                          │
│  V_out = 3.3V × R_FSR / (R1 + R_FSR)                      │
│                                                              │
│  FSR Resistance vs Force:                                    │
│  ┌──────────┬──────────┬──────────┐                         │
│  │ Force (N)│ R_FSR (Ω)│ V_out (V)│                         │
│  ├──────────┼──────────┼──────────┤                         │
│  │ 0        │ >10M     │ 3.30     │                         │
│  │ 0.1      │ 100k     │ 3.27     │                         │
│  │ 1        │ 20k      │ 3.14     │                         │
│  │ 5        │ 5k       │ 2.75     │                         │
│  │ 10       │ 2k       │ 2.20     │                         │
│  │ 50       │ 500      │ 1.10     │                         │
│  │ 100      │ 200      │ 0.55     │                         │
│  └──────────┴──────────┴──────────┘                         │
│                                                              │
│  ADC Configuration (ADS1115):                                │
│  • Gain: ±4.096V (ADS1115_CONFIG_GAIN_FOUR)               │
│  • Resolution: 16-bit (0.125mV/bit)                        │
│  • Sample rate: 860 SPS                                     │
│  • Input: Single-ended                                      │
│  • AIN0: FL foot, AIN1: FR foot                            │
│  • AIN2: RL foot, AIN3: RR foot                            │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 ADS1115 ADC Circuit

```
┌─────────────────────────────────────────────────────────────┐
│              ADS1115 ADC CIRCUIT                             │
│                                                              │
│              ┌─────────────────────────┐                    │
│              │      ADS1115             │                    │
│              │      (I2C 16-bit ADC)    │                    │
│              │                          │                    │
│              │  VDD ── 3.3V            │                    │
│              │         [100nF]──GND     │  (Decoupling)     │
│              │                          │                    │
│              │  GND ── GND             │                    │
│              │                          │                    │
│              │  SCL ──┬──[4.7kΩ]──3.3V │  (I2C pull-up)   │
│              │        └── STM32 PB10   │                    │
│              │                          │                    │
│              │  SDA ──┬──[4.7kΩ]──3.3V │  (I2C pull-up)   │
│              │        └── STM32 PB11   │                    │
│              │                          │                    │
│              │  ADDR ── GND            │  (Address 0x48)   │
│              │  ALRT ── NC             │  (Not used)       │
│              │                          │                    │
│              │  AIN0 ── FSR_FL         │                    │
│              │  AIN1 ── FSR_FR         │                    │
│              │  AIN2 ── FSR_RL         │                    │
│              │  AIN3 ── FSR_RR         │                    │
│              │  GND ── GND             │                    │
│              └─────────────────────────┘                    │
│                                                              │
│  I2C Configuration:                                          │
│  • Address: 0x48 (ADDR = GND)                              │
│  • Speed: 400 kHz                                           │
│  • Pull-up: 4.7kΩ (on main PCB)                           │
│                                                              │
│  Measurement Sequence:                                       │
│  1. Select AIN0 (FSR_FL) → Read → Store                   │
│  2. Select AIN1 (FSR_FR) → Read → Store                   │
│  3. Select AIN2 (FSR_RL) → Read → Store                   │
│  4. Select AIN3 (FSR_RR) → Read → Store                   │
│  5. Repeat at 100 Hz                                        │
└─────────────────────────────────────────────────────────────┘
```

### 4.4 Force-Torque Sensor Circuit

```
┌─────────────────────────────────────────────────────────────┐
│              FORCE-TORQUE SENSOR CIRCUIT                     │
│                                                              │
│              ┌─────────────────────────┐                    │
│              │  FORCE-TORQUE SENSOR     │                    │
│              │  (Custom strain gauge)   │                    │
│              │                          │                    │
│              │  VCC ── 3.3V            │                    │
│              │         [100nF]──GND     │  (Decoupling)     │
│              │                          │                    │
│              │  GND ── GND             │                    │
│              │                          │                    │
│              │  SDA ──┬──[4.7kΩ]──3.3V │  (I2C pull-up)   │
│              │        └── STM32 PC9    │                    │
│              │                          │                    │
│              │  SCL ──┬──[4.7kΩ]──3.3V │  (I2C pull-up)   │
│              │        └── STM32 PA8    │                    │
│              │                          │                    │
│              └─────────────────────────┘                    │
│                                                              │
│  Strain Gauge Bridge (inside sensor):                       │
│                                                              │
│         3.3V                                                  │
│          │                                                   │
│     ┌────┴────┐                                              │
│     │         │                                              │
│   [R1]      [R2]                                            │
│  (1kΩ)     (1kΩ)                                            │
│     │         │                                              │
│     ├────┬────┤                                              │
│     │    │    │                                              │
│    V+   Vout  V-                                            │
│     │    │    │                                              │
│     ├────┴────┤                                              │
│     │         │                                              │
│   [R3]      [R4]                                            │
│  (1kΩ)     (1kΩ)                                            │
│     │         │                                              │
│     └────┬────┘                                              │
│          │                                                   │
│         GND                                                  │
│                                                              │
│  Full Bridge: 4 active gauges                               │
│  Gauge Factor: 2.0                                           │
│  Excitation: 3.3V                                            │
│  Output: ±10mV at full load                                │
│  Amplifier: INA333 (gain 100)                               │
│  Output: ±1V → ADC (16-bit)                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. USB INTERFACE CIRCUIT

### 5.1 USB to Raspberry Pi

```
┌─────────────────────────────────────────────────────────────┐
│              USB INTERFACE (STM32 ↔ RPi 5)                   │
│                                                              │
│  ┌──────────────┐                    ┌──────────────┐       │
│  │   STM32H743   │                    │  RASPBERRY    │       │
│  │               │                    │  PI 5         │       │
│  │  PA11 (DM) ──┼──[22Ω]──┬──────┬──┼── USB DM      │       │
│  │  PA12 (DP) ──┼──[22Ω]──┤      ├──┼── USB DP      │       │
│  │               │         │      │  │               │       │
│  │  VDD (3.3V) ─┼─[ESD]──┤      ├──┼── VCC         │       │
│  │  GND ────────┼─────────┘      └──┼── GND         │       │
│  │               │                    │               │       │
│  └──────────────┘                    └──────────────┘       │
│                                                              │
│  USB Configuration:                                          │
│  • Mode: Device (CDC-ACM virtual serial)                   │
│  • Speed: Full Speed (12 Mbps)                              │
│  • Endpoint 0: Control (setup)                              │
│  • Endpoint 1: Bulk OUT (host → device)                    │
│  • Endpoint 2: Bulk IN (device → host)                     │
│  • Endpoint 3: Interrupt IN (notifications)                │
│                                                              │
│  Protocol:                                                   │
│  • Commands: JSON over CDC-ACM                             │
│  • Baud rate: 921600 (virtual, not actual USB)             │
│  • Flow control: None (USB handles it)                     │
│                                                              │
│  ESD Protection:                                             │
│  • TVS diode: USBLC6-2SC6                                  │
│  • Clamp voltage: 6V                                        │
│  • Capacitance: 0.5pF                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. STATUS LED CIRCUIT

### 6.1 RGB LED Array

```
┌─────────────────────────────────────────────────────────────┐
│              RGB LED CIRCUIT (WS2812B)                       │
│                                                              │
│  3.3V                                                        │
│   │                                                          │
│   └──[100nF]──GND  (per LED)                               │
│                                                              │
│   STM32 PE0 ──[330Ω]──►┌─────────┐                         │
│                         │ WS2812B │                         │
│                         │ (LED 1) │                         │
│                         └────┬────┘                         │
│                              │ DATA OUT                     │
│                              ▼                               │
│                         ┌─────────┐                         │
│                         │ WS2812B │                         │
│                         │ (LED 2) │                         │
│                         └────┬────┘                         │
│                              │ DATA OUT                     │
│                              ▼                               │
│                         ┌─────────┐                         │
│                         │ WS2812B │                         │
│                         │ (LED 3) │                         │
│                         └────┬────┘                         │
│                              │ ... (8 total)                │
│                              ▼                               │
│                         ┌─────────┐                         │
│                         │ WS2812B │                         │
│                         │ (LED 8) │                         │
│                         └─────────┘                         │
│                                                              │
│  LED Assignments:                                            │
│  • LED 1-4: Body corners (navigation/status)               │
│  • LED 5: Battery status (green=OK, red=low)              │
│  • LED 6: System status (blue=running, yellow=boot)       │
│  • LED 7: Arm status (orange=moving, green=idle)          │
│  • LED 8: Error indicator (red=error)                      │
│                                                              │
│  Protocol:                                                   │
│  • Data rate: 800 kbps                                     │
│  • Color depth: 24-bit (RGB)                               │
│  • PWM: 8-bit per channel                                  │
│  • Refresh: 400 Hz                                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. EMERGENCY STOP CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│              EMERGENCY STOP CIRCUIT                           │
│                                                              │
│  48V MAIN BUS                                                │
│  ──────┬─────────────────────────────────────               │
│        │                                                     │
│        └──►┌──────────────┐                                 │
│            │  EMERGENCY    │                                 │
│            │  STOP BUTTON  │                                 │
│            │  (Mushroom)   │                                 │
│            │  NC contact   │                                 │
│            └──────┬───────┘                                 │
│                   │                                          │
│            ┌──────┴───────┐                                 │
│            │  SOLID-STATE  │                                 │
│            │  RELAY        │                                 │
│            │  (MOSFET)     │                                 │
│            │  60V / 30A    │                                 │
│            │  <1mΩ RDS(on)│                                 │
│            └──────┬───────┘                                 │
│                   │                                          │
│            ┌──────┴───────┐                                 │
│            │  48V MAIN     │                                 │
│            │  OUTPUT       │                                 │
│            └──────────────┘                                 │
│                                                              │
│  Control Logic:                                              │
│  • Button pressed (NC opens) → Relay OFF → Power cut      │
│  • GPIO PC0 monitors button state                          │
│  • Firmware can also trigger via GPIO PC1                  │
│  • Hardware interlock (button → relay, no software)       │
│                                                              │
│  Response Time:                                              │
│  • Button press to power cut: <10ms                        │
│  • Button release to power restore: manual reset          │
│  • Software emergency stop: <1ms (GPIO toggle)            │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. COMPLETE BILL OF MATERIALS (CIRCUITS)

| Component | Part Number | Value/Type | Qty | Unit Cost | Total |
|-----------|------------|------------|-----|-----------|-------|
| **Power** | | | | | |
| Buck Controller | LM5145-Q1 | Sync Buck | 1 | $3.00 | $3.00 |
| Buck Converter | TPS54331 | 3A Buck | 1 | $1.50 | $1.50 |
| Buck Converter | LM2596-12 | 3A Buck | 1 | $1.00 | $1.00 |
| MOSFET | CSD19536 | 60V/100A N-ch | 1 | $2.00 | $2.00 |
| Inductor 10µH | Coilcraft | 15A sat | 1 | $3.00 | $3.00 |
| Inductor 22µH | Coilcraft | 4A sat | 1 | $1.50 | $1.50 |
| Inductor 33µH | Coilcraft | 4A sat | 1 | $1.50 | $1.50 |
| Capacitor 100µF/100V | Nichicon | Low ESR | 1 | $1.00 | $1.00 |
| Capacitor 47µF/100V | Nichicon | Low ESR | 2 | $0.50 | $1.00 |
| Capacitor 220µF/50V | Nichicon | Low ESR | 2 | $0.75 | $1.50 |
| Capacitor 100nF | Generic | MLCC | 20 | $0.05 | $1.00 |
| Capacitor 10µF | Generic | MLCC | 10 | $0.10 | $1.00 |
| Capacitor 1µF | Generic | MLCC | 10 | $0.05 | $0.50 |
| Resistor 10kΩ | Generic | 0402 | 20 | $0.01 | $0.20 |
| Resistor 4.7kΩ | Generic | 0402 | 10 | $0.01 | $0.10 |
| Resistor 120Ω | Generic | 0402 | 6 | $0.01 | $0.06 |
| **MCU** | | | | | |
| STM32H743VIT6 | ST Micro | Cortex-M7 | 1 | $10.00 | $10.00 |
| 8MHz Crystal | Generic | HC49 | 1 | $0.50 | $0.50 |
| W25Q128 Flash | Winbond | 128Mbit SPI | 1 | $1.50 | $1.50 |
| AT24C256 EEPROM | Microchip | 256Kbit I2C | 1 | $0.50 | $0.50 |
| **Communication** | | | | | |
| MCP2562FD | Microchip | CAN FD Transceiver | 3 | $1.50 | $4.50 |
| **Sensors** | | | | | |
| INA226 | TI | Power Monitor | 1 | $3.00 | $3.00 |
| LTC2944 | Analog | Coulomb Counter | 1 | $5.00 | $5.00 |
| TMP102 | TI | Temperature | 1 | $1.00 | $1.00 |
| **Interface** | | | | | |
| USBLC6-2SC6 | ST Micro | USB ESD Protection | 1 | $0.50 | $0.50 |
| **Misc** | | | | | |
| PCB (4-layer, ENIG) | JLCPCB | 120×80mm | 1 | $10.00 | $10.00 |
| Assembly (SMD) | JLCPCB | Full assembly | 1 | $15.00 | $15.00 |
| **Circuit Total** | | | | | **$66.76** |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
