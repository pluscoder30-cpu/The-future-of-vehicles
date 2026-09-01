# PHI AI HEALING DRONE — WIRING DIAGRAMS

## Electrical Wiring Specifications (AI-Enhanced)

---

## POWER DISTRIBUTION

```
POWER FLOW:
═══════════════════════════════════════════════════════════════

  ┌─────────────────┐
  │  FPB-5 BATTERY  │
  │  12V · 50Ah     │
  │  600Wh          │
  └────────┬────────┘
           │
           │ 12V Main Bus
           │
    ┌──────┴──────┐
    │  30A FUSE   │
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │  MAIN SWITCH│
    └──────┬──────┘
           │
    ┌──────┴──────────────────────────────────┐
    │                                          │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │ MOTORS   │  │AVIONICS  │  │MEDICAL│ │
    │  │ 12V Bus  │  │ 5V Reg   │  │ 5V Reg│ │
    │  │ 4x30A    │  │ Buck     │  │ Buck  │ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │                                          │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │FREQUENCY │  │ WIFI     │  │ AI    │ │
    │  │ GEN 5V   │  │ 3.3V Reg │  │ 5V Reg│ │
    │  │ Buck     │  │ Buck     │  │ Buck  │ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │                                          │
    └──────────────────────────────────────────┘

  VOLTAGE REGULATORS:
  ─────────────────────
  FPB-5 (12V) → 5V Buck (Arduino, sensors, frequency gen)
  FPB-5 (12V) → 5V Buck (Medical sensors, servo)
  FPB-5 (12V) → 3.3V Buck (ESP8266, BMP280)
  FPB-5 (12V) → 5V Buck (Raspberry Pi Zero 2W)
  FPB-5 (12V) → Direct to ESCs (motors)
```

---

## AI PROCESSOR WIRING

```
RASPBERRY PI ZERO 2W CONNECTIONS:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────┐
  │              RASPBERRY PI ZERO 2W                   │
  │                                                     │
  │  GPIO 14 (TX) ───→ Arduino RX1 (Pin 19)            │
  │  GPIO 15 (RX) ←─── Arduino TX1 (Pin 18)            │
  │  5V ───────────→ 5V Regulated Supply               │
  │  GND ──────────→ Common Ground                     │
  │                                                     │
  │  CSI Camera Port ───→ Pi Camera Module              │
  │  MicroSD ───────────→ 32GB (AI models + OS)        │
  │  Mini HDMI ─────────→ (debug output)               │
  │                                                     │
  │  I2C (GPIO 2/3) ───→ Arduino I2C Bus (shared)      │
  │                                                     │
  └─────────────────────────────────────────────────────┘

  COMMUNICATION FLOW:
  ───────────────────
  Sensors → Arduino → Serial → Pi Zero → AI Processing
                                    ↓
  Pi Zero → Serial → Arduino → ESCs/Motors/Medication
```

---

## MOTOR WIRING

```
MOTOR CONNECTION DIAGRAM:
═══════════════════════════════════════════════════════════════

  FPB-5 Battery (12V)
       │
       ├──→ ESC1 ──→ Motor 1 (Front Left)
       │    └── Signal wire → Arduino Pin 3
       │
       ├──→ ESC2 ──→ Motor 2 (Front Right)
       │    └── Signal wire → Arduino Pin 5
       │
       ├──→ ESC3 ──→ Motor 3 (Rear Left)
       │    └── Signal wire → Arduino Pin 6
       │
       └──→ ESC4 ──→ Motor 4 (Rear Right)
            └── Signal wire → Arduino Pin 9
```

---

## COMPLETE WIRING TABLE

| Arduino Pin | Connection | Wire Color | Function |
|------------|------------|------------|----------|
| 2 | MPU6050 SDA | Yellow | I2C Data |
| 3 | ESC1 Signal | Orange | Motor 1 PWM |
| 4 | PCM5102A DIN | White | Frequency Data |
| 5 | ESC2 Signal | Orange | Motor 2 PWM |
| 6 | ESC3 Signal | Orange | Motor 3 PWM |
| 7 | PCM5102A BCK | Gray | Frequency Bit Clock |
| 8 | PCM5102A LCK | Purple | Frequency Word Clock |
| 9 | ESC4 Signal | Orange | Motor 4 PWM |
| 10 | ESP8266 RX | Blue | WiFi Communication |
| 11 | ESP8266 TX | Green | WiFi Communication |
| 12 | Servo 1 (Med Bay) | Red | Medication Release |
| 13 | Servo 2 (Vial Bay) | Red | Vial Release |
| 14 | Servo 3 (Wound) | Red | Wound Care |
| 15 | Buzzer | Black | Audible Alerts |
| 16 | GPS RX | Yellow | GPS Data In |
| 17 | GPS TX | Green | GPS Data Out |
| 18 | HC-12 RX | Blue | Telemetry In |
| 19 | HC-12 TX / Pi RX | White | Telemetry Out / AI Data |
| 20 | I2C SDA | Yellow | I2C Bus |
| 21 | I2C SCL | Orange | I2C Clock |
| 22 | DS18B20 Data | Red | Temperature |
| A0 | AD8232 Output | White | ECG Signal |
| A1 | Battery Voltage | Red | Battery Monitor |
| A2 | Current Sense | Blue | Current Monitor |
| 5V | Sensor Power | Red | 5V Supply |
| GND | Common Ground | Black | Ground |
| VIN | Battery Input | Red | 12V Supply |

---

## I2C BUS SHARING

```
I2C BUS ARCHITECTURE:
═══════════════════════════════════════════════════════════════

  Arduino Mega (I2C Master)
       │
       ├──→ MPU6050 (0x68) — Gyro/Accel
       ├──→ BMP280 (0x76) — Barometer
       ├──→ MAX30102 (0x57) — Pulse Oximeter
       ├──→ OLED Display (0x3C) — Status Display
       └──→ Pi Zero (0x10) — AI Data Exchange

  Pi Zero (I2C Slave)
       │
       ├──→ Shares sensor data with Arduino
       └──→ Sends AI recommendations to Arduino

  Address conflicts avoided by using different addresses
  on each device.
```
