# PHI HEALING DRONE — WIRING DIAGRAMS

## Electrical Wiring Specifications

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
    │  ┌──────────┐  ┌──────────┐             │
    │  │FREQUENCY │  │ WIFI     │             │
    │  │ GEN 5V   │  │ 3.3V Reg │             │
    │  │ Buck     │  │ Buck     │             │
    │  └──────────┘  └──────────┘             │
    │                                          │
    └──────────────────────────────────────────┘

  VOLTAGE REGULATORS:
  ─────────────────────
  FPB-5 (12V) → 5V Buck (Arduino, sensors, frequency gen)
  FPB-5 (12V) → 5V Buck (Medical sensors, servo)
  FPB-5 (12V) → 3.3V Buck (ESP8266, BMP280)
  FPB-5 (12V) → Direct to ESCs (motors)
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

  ESC WIRING (each):
  ───────────────────
  ┌─────────────────────────────────┐
  │           ESC 30A               │
  │                                 │
  │  Red (+) ──────→ Battery +     │
  │  Black (-) ─────→ Battery -    │
  │                                 │
  │  Orange (Signal) → Arduino PWM │
  │  Red (5V BEC) ──→ Arduino 5V   │  ← Only ESC1 powers Arduino
  │  Brown (GND) ───→ Arduino GND  │
  │                                 │
  │  Blue ──────→ Motor Phase A    │
  │  Green ─────→ Motor Phase B    │
  │  Yellow ────→ Motor Phase C    │
  └─────────────────────────────────┘
```

---

## SENSOR WIRING

```
SENSOR BUS DIAGRAM:
═══════════════════════════════════════════════════════════════

  Arduino Mega 2560
  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │  I2C BUS (pins 20-21):                          │
  │  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
  │  │ MPU6050 │  │ BMP280  │  │ OLED    │         │
  │  │ 0x68    │  │ 0x76    │  │ 0x3C    │         │
  │  └─────────┘  └─────────┘  └─────────┘         │
  │                                                  │
  │  I2C BUS (pins 20-21):                          │
  │  ┌─────────┐  ┌─────────┐                       │
  │  │ MAX30102│  │ AD8232  │                       │
  │  │ 0x57    │  │ Analog  │                       │
  │  └─────────┘  └─────────┘                       │
  │                                                  │
  │  ONE-WIRE (Pin 22):                             │
  │  ┌─────────┐  ┌─────────┐                       │
  │  │ DS18B20 │  │ DS18B20 │  (temperature x2)     │
  │  │ Sensor 1│  │ Sensor 2│                       │
  │  └─────────┘  └─────────┘                       │
  │                                                  │
  │  SERIAL (pins 16-17):                           │
  │  ┌─────────┐                                    │
  │  │ GPS     │                                    │
  │  │ NEO-6M  │                                    │
  │  └─────────┘                                    │
  │                                                  │
  │  SERIAL2 (pins 17-18):                          │
  │  ┌─────────┐                                    │
  │  │ HC-12   │  (telemetry)                       │
  │  │ Radio   │                                    │
  │  └─────────┘                                    │
  │                                                  │
  │  DIGITAL (Pin 10):                              │
  │  ┌─────────┐                                    │
  │  │ ESP8266 │                                    │
  │  │ WiFi    │                                    │
  │  └─────────┘                                    │
  │                                                  │
  │  ANALOG (A0-A3):                                │
  │  ┌─────────┐  ┌─────────┐                       │
  │  │AD8232   │  │ Battery │                       │
  │  │ECG Out  │  │ Voltage │                       │
  │  └─────────┘  └─────────┘                       │
  │                                                  │
  └──────────────────────────────────────────────────┘
```

---

## FREQUENCY GENERATOR WIRING

```
FREQUENCY GENERATOR CIRCUIT:
═══════════════════════════════════════════════════════════════

  Arduino Pin 4 (PWM)
       │
       │ Signal
       ▼
  ┌─────────────┐
  │  PCM5102A   │
  │  DAC Module │
  │             │
  │  VIN → 5V   │
  │  GND → GND  │
  │  DIN → Pin 4│
  │  BCK → Pin 7│
  │  LCK → Pin 8│
  │  OUT → amp  │
  └──────┬──────┘
         │
         │ Audio Signal
         ▼
  ┌─────────────┐
  │  PAM8403    │
  │  Amplifier  │
  │             │
  │  IN+ → DAC  │
  │  IN- → GND  │
  │  OUT+ → transducer 1 │
  │  OUT- → transducer 2 │
  │  VCC → 5V   │
  │  GND → GND  │
  └──────┬──────┘
         │
         │ Amplified Signal
         ▼
  ┌─────────────┐
  │ TRANSDUCERS │
  │ (2x 40mm)   │
  │             │
  │  T1: Head   │
  │  T2: Body   │
  │             │
  │  Frequency: │
  │  432-852Hz  │
  └─────────────┘

  PHI-HARMONIC FREQUENCIES:
  ─────────────────────────
  432Hz - Healing (fundamental)
  528Hz - Transformation
  639Hz - Connection
  741Hz - Expression
  852Hz - Intuition

  All frequencies are phi-related:
  432 x 1.618 = 699Hz (next harmonic)
  699 x 1.618 = 1131Hz (overtone)
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
| 19 | HC-12 TX | White | Telemetry Out |
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

## GROUND PLANE

```
GROUND WIRING:
═══════════════════════════════════════════════════════════════

  All grounds connect to a SINGLE POINT (star ground):

                    ┌──────────────┐
                    │  BATTERY -   │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │  STAR GROUND │
                    │  POINT       │
                    └──┬──┬──┬──┬──┘
                       │  │  │  │
           ┌───────────┘  │  │  └───────────┐
           │              │  │              │
    ┌──────┴──────┐ ┌─────┴──┴─────┐ ┌──────┴──────┐
    │   ESC GND   │ │ Arduino GND  │ │ Sensor GND  │
    │  (all 4)    │ │              │ │ (all)       │
    └─────────────┘ └──────────────┘ └─────────────┘

  CRITICAL: Do NOT create ground loops!
  All grounds meet at ONE point near the battery.
```

---

## WIRE GAUGE SPECIFICATIONS

| Circuit | Current | Wire Gauge | Color |
|---------|---------|------------|-------|
| Battery to fuse | 30A | 12 AWG | Red (+), Black (-) |
| Fuse to switch | 30A | 12 AWG | Red (+), Black (-) |
| Switch to ESCs | 30A each | 14 AWG | Red (+), Black (-) |
| ESC to motor | 15A | 18 AWG | Blue, Green, Yellow |
| Battery to Arduino | 2A | 22 AWG | Red (+), Black (-) |
| Arduino to sensors | 100mA | 26 AWG | Various |
| I2C bus | 10mA | 26 AWG | Yellow (SDA), Orange (SCL) |
| Signal wires | 10mA | 26 AWG | White/Gray |
