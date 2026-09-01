# PHI BIO-SKIN WATCH — WIRING DIAGRAM
## Buildable Documentation | Electrical Connections

---

## SYSTEM OVERVIEW

```
                    ┌─────────────────────────────────────────┐
                    │         PHI BIO-SKIN WATCH              │
                    │  ┌─────────────────────────────────┐   │
                    │  │     RASPBERRY PI ZERO 2 W       │   │
                    │  │  ┌─────┐ ┌─────┐ ┌─────┐       │   │
                    │  │  │GPU  │ │CPU  │ │RAM  │       │   │
                    │  │  │VideoCore│BCM2710│512MB│       │   │
                    │  │  └──┬──┘ └──┬──┘ └──┬──┘       │   │
                    │  │     │       │       │           │   │
                    │  │  ┌──┴───────┴───────┴──┐       │   │
                    │  │  │   GPIO HEADER       │       │   │
                    │  │  │   (40 pins)         │       │   │
                    │  │  └────────────────────┘       │   │
                    │  └─────────────────────────────────┘   │
                    │           │                           │
                    │           │ I2C/SPI/UART              │
                    │           │                           │
                    │  ┌────────┴────────┐                  │
                    │  │ SENSOR BUS      │                  │
                    │  │ (I2C + SPI)     │                  │
                    │  └────────┬────────┘                  │
                    │           │                           │
                    │  ┌────────┼──────────────────┐       │
                    │  │        │                  │       │
                    │  │  ┌─────┴─────┐  ┌────────┴────┐ │
                    │  │  │ MAX30102   │  │ ADS1115     │ │
                    │  │  │ PPG Sensor │  │ 16-bit ADC  │ │
                    │  │  │ (I2C:0x57)│  │ (I2C:0x48)  │ │
                    │  │  └─────┬─────┘  └──────┬──────┘ │
                    │  │        │                │        │
                    │  │  ┌─────┴─────┐  ┌──────┴──────┐ │
                    │  │  │ MCP9808   │  │ BME280      │ │
                    │  │  │ Temp      │  │ Env Sensor  │ │
                    │  │  │ (I2C:0x18)│  │ (I2C:0x76)  │ │
                    │  │  └───────────┘  └─────────────┘ │
                    │  │                                  │
                    │  │  ┌───────────┐  ┌─────────────┐ │
                    │  │  │ MPU6050   │  │ VEML6075    │ │
                    │  │  │ IMU       │  │ UV Sensor   │ │
                    │  │  │ (I2C:0x68)│  │ (I2C:0x10)  │ │
                    │  │  └───────────┘  └─────────────┘ │
                    │  └──────────────────────────────────┘
                    │           │
                    │  ┌────────┴────────┐
                    │  │  DISPLAY        │
                    │  │  (SPI: GPIO)    │
                    │  │  SSD1351 1.2"   │
                    │  │  AMOLED 128x128 │
                    │  └─────────────────┘
                    │           │
                    │  ┌────────┴────────┐
                    │  │  BLE MODULE     │
                    │  │  nRF52840       │
                    │  │  (UART: TX/RX)  │
                    │  └─────────────────┘
                    │           │
                    │  ┌────────┴────────┐
                    │  │  POWER SYSTEM   │
                    │  │  Qi + LiPo      │
                    │  │  TP4056 + LDO   │
                    │  └─────────────────┘
                    └─────────────────────────────────────────┘
```

---

## DETAILED WIRING TABLE

### I2C Bus (SDA/SCL)

| Device | SDA Pin | SCL Pin | Address | Power |
|--------|---------|---------|---------|-------|
| MAX30102 PPG | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x57 | 3.3V |
| ADS1115 ADC | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x48 | 3.3V |
| MCP9808 Temp | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x18 | 3.3V |
| BME280 Env | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x76 | 3.3V |
| MPU6050 IMU | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x68 | 3.3V |
| VEML6075 UV | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x10 | 3.3V |

**Note**: All I2C devices share SDA (GPIO 2) and SCL (GPIO 3) with 4.7k pull-up resistors to 3.3V.

### SPI Bus (Display)

| Signal | GPIO Pin | Device Pin |
|--------|----------|------------|
| MOSI (Data) | GPIO 10 (MOSI) | DIN |
| SCLK (Clock) | GPIO 11 (SCLK) | CLK |
| CS (Chip Select) | GPIO 8 (CE0) | CS |
| DC (Data/Command) | GPIO 24 | DC |
| RESET | GPIO 25 | RST |
| VCC | 3.3V | VCC |
| GND | GND | GND |

### UART Bus (BLE Module)

| Signal | GPIO Pin | Device Pin |
|--------|----------|------------|
| TX (Pi → BLE) | GPIO 14 (TXD) | RX |
| RX (BLE → Pi) | GPIO 15 (RXD) | TX |
| VCC | 3.3V | VCC |
| GND | GND | GND |

---

## POWER DISTRIBUTION

```
                    ┌─────────────────────────────────────┐
                    │        POWER FLOW DIAGRAM           │
                    │                                     │
                    │   Qi Coil ──► TP4056 ──► LiPo      │
                    │   (5V/1A)    (Charger)  (80mAh)    │
                    │                        │           │
                    │                        ▼           │
                    │                   MCP1700 LDO      │
                    │                   (3.3V/250mA)     │
                    │                        │           │
                    │          ┌─────────────┼──────┐    │
                    │          │             │      │    │
                    │          ▼             ▼      ▼    │
                    │     ┌────────┐   ┌────────┐ ┌───┐ │
                    │     │Pi Zero │   │Sensors │ │BLE│ │
                    │     │150mA   │   │25mA    │ │15mA│ │
                    │     └────────┘   └────────┘ └───┘ │
                    │                                     │
                    │   Total: 190mA (within 250mA limit) │
                    └─────────────────────────────────────┘
```

### Battery Connection

```
LiPo Battery (80mAh, 3.7V)
    │
    ├──[TP4056]──┐
    │             │
    │    ┌────────┴────────┐
    │    │   MCP1700 LDO   │
    │    │   IN  ──── OUT  │
    │    │    │         │  │
    │    │    ▼    3.3V ▼  │
    │    └─────────────────┘
    │
    └──[Qi Coil]──► Charging (5V/1A)
```

---

## SENSOR WIRING DETAILS

### MAX30102 PPG (Heart Rate + SpO2)

```
MAX30102 Module          Raspberry Pi Zero
┌─────────────┐         ┌─────────────────┐
│  VCC ───────┼─────────┼── 3.3V          │
│  GND ───────┼─────────┼── GND           │
│  SDA ───────┼─────────┼── GPIO 2 (SDA)  │
│  SCL ───────┼─────────┼── GPIO 3 (SCL)  │
│  INT ───────┼─────────┼── GPIO 7 (IRQ)  │
└─────────────┘         └─────────────────┘
```

### ADS1115 ADC (Glucose Sensor Input)

```
ADS1115 Module           Raspberry Pi Zero
┌─────────────┐         ┌─────────────────┐
│  VDD ───────┼─────────┼── 3.3V          │
│  GND ───────┼─────────┼── GND           │
│  SDA ───────┼─────────┼── GPIO 2 (SDA)  │
│  SCL ───────┼─────────┼── GPIO 3 (SCL)  │
│  A0 ────────┼─────────┼── Glucose Sensor│
│  A1 ────────┼─────────┼── Cortisol Strip│
│  A2 ────────┼─────────┼── (Reserved)    │
│  A3 ────────┼─────────┼── (Reserved)    │
└─────────────┘         └─────────────────┘
```

### SSD1351 AMOLED Display (SPI)

```
SSD1351 Display          Raspberry Pi Zero
┌─────────────┐         ┌─────────────────┐
│  VCC ───────┼─────────┼── 3.3V          │
│  GND ───────┼─────────┼── GND           │
│  DIN ───────┼─────────┼── GPIO 10 (MOSI)│
│  CLK ───────┼─────────┼── GPIO 11 (SCLK)│
│  CS ────────┼─────────┼── GPIO 8 (CE0)  │
│  DC ────────┼─────────┼── GPIO 24       │
│  RST ───────┼─────────┼── GPIO 25       │
└─────────────┘         └─────────────────┘
```

---

## I2C BUS DETAIL

```
                    3.3V
                     │
                     ├──[4.7kΩ]──┐
                     │            │
                     ├──[4.7kΩ]──┤
                     │            │
    ┌────────────────┼────────────┼────────────────────┐
    │                │            │                    │
    │   SDA Bus      │            │   SCL Bus          │
    │   (GPIO 2)     │            │   (GPIO 3)         │
    │                │            │                    │
    │  ┌─────────────┼────────────┼─────────────┐     │
    │  │             │            │             │     │
    │  │  ┌──────────┴──┐  ┌─────┴─────────┐  │     │
    │  │  │ MAX30102    │  │ MAX30102      │  │     │
    │  │  │ SDA         │  │ SCL           │  │     │
    │  │  │ 0x57        │  │               │  │     │
    │  │  └─────────────┘  └───────────────┘  │     │
    │  │                                      │     │
    │  │  ┌─────────────┐  ┌───────────────┐  │     │
    │  │  │ ADS1115     │  │ ADS1115       │  │     │
    │  │  │ SDA         │  │ SCL           │  │     │
    │  │  │ 0x48        │  │               │  │     │
    │  │  └─────────────┘  └───────────────┘  │     │
    │  │                                      │     │
    │  │  ┌─────────────┐  ┌───────────────┐  │     │
    │  │  │ MCP9808     │  │ MCP9808       │  │     │
    │  │  │ SDA         │  │ SCL           │  │     │
    │  │  │ 0x18        │  │               │  │     │
    │  │  └─────────────┘  └───────────────┘  │     │
    │  │                                      │     │
    │  │  ┌─────────────┐  ┌───────────────┐  │     │
    │  │  │ BME280      │  │ BME280        │  │     │
    │  │  │ SDA         │  │ SCL           │  │     │
    │  │  │ 0x76        │  │               │  │     │
    │  │  └─────────────┘  └───────────────┘  │     │
    │  │                                      │     │
    │  │  ┌─────────────┐  ┌───────────────┐  │     │
    │  │  │ MPU6050     │  │ MPU6050       │  │     │
    │  │  │ SDA         │  │ SCL           │  │     │
    │  │  │ 0x68        │  │               │  │     │
    │  │  └─────────────┘  └───────────────┘  │     │
    │  │                                      │     │
    │  │  ┌─────────────┐  ┌───────────────┐  │     │
    │  │  │ VEML6075    │  │ VEML6075      │  │     │
    │  │  │ SDA         │  │ SCL           │  │     │
    │  │  │ 0x10        │  │               │  │     │
    │  │  └─────────────┘  └───────────────┘  │     │
    │  │                                      │     │
    │  │            GPIO 2    GPIO 3          │     │
    │  └──────────────┼──────────┼────────────┘     │
    │                 │          │                   │
    └─────────────────┼──────────┼───────────────────┘
                      │          │
                   Raspberry Pi Zero
```

---

## GPIO PIN MAP

| GPIO | Function | Connected To | Direction |
|------|----------|--------------|-----------|
| 2 | I2C SDA | All sensors | Bidirectional |
| 3 | I2C SCL | All sensors | Output |
| 4 | (Reserved) | - | - |
| 5 | (Reserved) | - | - |
| 6 | (Reserved) | - | - |
| 7 | IRQ | MAX30102 INT | Input |
| 8 | SPI CS | Display CS | Output |
| 9 | (Reserved) | - | - |
| 10 | SPI MOSI | Display DIN | Output |
| 11 | SPI SCLK | Display CLK | Output |
| 12 | (Reserved) | - | - |
| 13 | (Reserved) | - | - |
| 14 | UART TX | BLE RX | Output |
| 15 | UART RX | BLE TX | Input |
| 16-23 | (Reserved) | - | - |
| 24 | Display DC | Display DC | Output |
| 25 | Display RST | Display RST | Output |
| 26-27 | (Reserved) | - | - |

---

## POWER PINS

| Pin | Voltage | Current | Notes |
|-----|---------|---------|-------|
| 3.3V (Pin 1) | 3.3V | 50mA max | From MCP1700 LDO |
| 5V (Pin 2) | 5V | 1.2A max | From Qi/USB |
| GND (Pin 6,9,14,20,25,30,34,39) | 0V | - | Common ground |

---

## WIRING BEST PRACTICES

1. **I2C Pull-ups**: Always include 4.7kΩ pull-ups on SDA and SCL to 3.3V
2. **Bypass Caps**: Add 100nF ceramic capacitors on each sensor's VCC pin
3. **Wire Length**: Keep I2C wires under 10cm to prevent signal degradation
4. **Power Filtering**: Add 10µF bulk capacitor near power input
5. **Ground Plane**: Use ground plane or star ground topology
6. **Shielding**: Wrap SPI wires in foil if display shows noise

---

## CONTINUITY CHECK LIST

Before powering on, verify:

- [ ] All GND pins connected together
- [ ] 3.3V rail to all sensor VCC pins
- [ ] No shorts between 3.3V and GND
- [ ] I2C SDA not shorted to SCL
- [ ] SPI MOSI/SCLK not shorted
- [ ] BLE TX/RX not swapped
- [ ] Display CS/DC/RST correct

---

**Document**: 02_WIRING.md
**Vehicle**: PHI BIO-SKIN WATCH
**Status**: BUILDABLE ✓
