# PHI PLANT DRONE — WIRING DIAGRAMS

## Electrical Wiring Specifications

---

## POWER DISTRIBUTION

```
POWER FLOW:
═══════════════════════════════════════════════════════════════

  ┌─────────────────┐
  │  FPB-5 BATTERY  │
  │  12V · 50Ah     │
  └────────┬────────┘
           │
    ┌──────┴──────┐
    │  30A FUSE   │
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │  MAIN SWITCH│
    └──────┬──────┘
           │
    ┌──────┴────────────────────────────────────┐
    │                                            │
    │  ├──→ ESC1-4 ──→ Motors (12V direct)      │
    │  ├──→ 5V Buck ──→ Arduino, servos, sensors│
    │  ├──→ 5V Buck ──→ Frequency generator     │
    │  ├──→ 12V Pump ──→ Water pump (direct)    │
    │  └──→ 3.3V Buck ──→ ESP8266, GPS          │
    │                                            │
    └────────────────────────────────────────────┘
```

---

## MOTOR WIRING

```
MOTOR CONNECTION:
═══════════════════════════════════════════════════════════════

  FPB-5 (12V) ──→ ESC1 ──→ Motor 1 (Front Left, CW)
              ──→ ESC2 ──→ Motor 2 (Front Right, CCW)
              ──→ ESC3 ──→ Motor 3 (Rear Left, CCW)
              ──→ ESC4 ──→ Motor 4 (Rear Right, CW)

  ESC Signal Wires:
  ESC1 → Arduino Pin 3
  ESC2 → Arduino Pin 5
  ESC3 → Arduino Pin 6
  ESC4 → Arduino Pin 9

  ESC1 BEC provides 5V to Arduino (through main switch)
```

---

## SENSOR WIRING

```
SENSOR BUS:
═══════════════════════════════════════════════════════════════

  Arduino Mega 2560
  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │  I2C BUS (pins 20-21):                          │
  │  ├── MPU6050 (0x68) — Gyro/Accel               │
  │  ├── BMP280 (0x76) — Barometer                 │
  │  ├── BH1750 (0x23) — Light sensor              │
  │  └── OLED (0x3C) — Display                     │
  │                                                  │
  │  ANALOG:                                         │
  │  ├── A0 — Soil moisture sensor 1               │
  │  ├── A1 — Soil moisture sensor 2               │
  │  └── A2 — Battery voltage divider              │
  │                                                  │
  │  DIGITAL:                                        │
  │  ├── Pin 2 — MPU6050 interrupt                 │
  │  ├── Pin 3 — ESC1 signal                       │
  │  ├── Pin 4 — PCM5102A DIN (frequency)          │
  │  ├── Pin 5 — ESC2 signal                       │
  │  ├── Pin 6 — ESC3 signal                       │
  │  ├── Pin 7 — PCM5102A BCK                      │
  │  ├── Pin 8 — PCM5102A LCK                      │
  │  ├── Pin 9 — ESC4 signal                       │
  │  ├── Pin 10 — ESP8266 RX                       │
  │  ├── Pin 11 — ESP8266 TX                       │
  │  ├── Pin 12 — Seed servo                       │
  │  ├── Pin 13 — Water pump relay                 │
  │  ├── Pin 14 — Agitator motor                   │
  │  ├── Pin 16 — GPS TX                           │
  │  ├── Pin 17 — GPS RX                           │
  │  ├── Pin 18 — HC-12 TX                         │
  │  └── Pin 19 — HC-12 RX                         │
  │                                                  │
  └──────────────────────────────────────────────────┘
```

---

## SEED DISPENSER WIRING

```
SEED DISPENSER CIRCUIT:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 ──→ Servo (opens seed gate)
  Arduino Pin 14 ──→ Agitator motor (vibrates seeds)

  ┌─────────────────────────────────────┐
  │         SEED DISPENSER              │
  │                                     │
  │  Hopper (3D printed)               │
  │  ┌──────────────────┐              │
  │  │ Seeds ──→ Gate   │              │
  │  │          (servo) │              │
  │  └────────┬─────────┘              │
  │           │                         │
  │           ▼                         │
  │  ┌──────────────────┐              │
  │  │  Agitator        │              │
  │  │  (vibration motor)│             │
  │  └────────┬─────────┘              │
  │           │                         │
  │           ▼                         │
  │  ┌──────────────────┐              │
  │  │  Seed tray       │              │
  │  │  (drops to ground)│             │
  │  └──────────────────┘              │
  │                                     │
  └─────────────────────────────────────┘
```

---

## WATER SYSTEM WIRING

```
WATER PUMP CIRCUIT:
═══════════════════════════════════════════════════════════════

  Arduino Pin 13 ──→ Relay module ──→ Water pump

  ┌─────────────────────────────────────┐
  │         WATER SYSTEM               │
  │                                     │
  │  Water Tank (500ml)                │
  │  ┌──────────────────┐              │
  │  │                  │              │
  │  └────────┬─────────┘              │
  │           │                         │
  │           ▼                         │
  │  ┌──────────────────┐              │
  │  │  Pump (12V)      │              │
  │  │  3L/min          │              │
  │  └────────┬─────────┘              │
  │           │                         │
  │           ▼                         │
  │  ┌──────────────────┐              │
  │  │  Check valve     │              │
  │  │  (prevents drip) │              │
  │  └────────┬─────────┘              │
  │           │                         │
  │           ▼                         │
  │  ┌──────────────────┐              │
  │  │  Nozzle          │              │
  │  │  (adjustable)    │              │
  │  └──────────────────┘              │
  │                                     │
  └─────────────────────────────────────┘
```

---

## FREQUENCY GENERATOR WIRING

```
FREQUENCY GENERATOR:
═══════════════════════════════════════════════════════════════

  Arduino Pins 4,7,8 ──→ PCM5102A DAC ──→ PAM8403 Amp ──→ Transducers

  Frequencies: 432Hz, 528Hz, 639Hz (plant growth)

  Transducers mounted on bottom of drone, facing plants
```

---

## COMPLETE WIRING TABLE

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion interrupt |
| 3 | ESC1 Signal | Motor 1 PWM |
| 4 | PCM5102A DIN | Frequency data |
| 5 | ESC2 Signal | Motor 2 PWM |
| 6 | ESC3 Signal | Motor 3 PWM |
| 7 | PCM5102A BCK | Frequency clock |
| 8 | PCM5102A LCK | Frequency word |
| 9 | ESC4 Signal | Motor 4 PWM |
| 10 | ESP8266 RX | WiFi |
| 11 | ESP8266 TX | WiFi |
| 12 | Servo | Seed gate |
| 13 | Relay | Water pump |
| 14 | Agitator motor | Seed vibration |
| 15 | Buzzer | Alerts |
| 16 | GPS TX | GPS data |
| 17 | GPS RX | GPS data |
| 18 | HC-12 TX | Telemetry |
| 19 | HC-12 RX | Telemetry |
| 20 | I2C SDA | I2C bus |
| 21 | I2C SCL | I2C clock |
| A0 | Soil moisture 1 | Analog |
| A1 | Soil moisture 2 | Analog |
| A2 | Battery voltage | Analog |

---

## WIRE GAUGE

| Circuit | Current | Wire Gauge |
|---------|---------|------------|
| Battery to fuse | 30A | 12 AWG |
| ESC to motor | 15A | 18 AWG |
| Pump power | 2A | 20 AWG |
| Arduino to sensors | 100mA | 26 AWG |
| I2C bus | 10mA | 26 AWG |
