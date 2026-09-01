# PHI PLANT DRONE — CIRCUIT SCHEMATICS

## Avionics and Sensor Circuit Design

---

## MAIN CIRCUIT OVERVIEW

```
SYSTEM BLOCK DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  FPB-5      │────→│  POWER      │────→│  ARDUINO    │
  │  BATTERY    │     │  MANAGEMENT │     │  MEGA 2560  │
  │  12V 50Ah   │     │  5V/3.3V    │     │             │
  └─────────────┘     └─────────────┘     └──────┬──────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────┐
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   FLIGHT        │          │   PLANT         │    │   FREQUENCY     │
           │   SENSORS       │          │   SENSORS       │    │   GENERATOR     │
           │                 │          │                 │    │                 │
           │ - MPU6050       │          │ - Soil moisture │    │ - PCM5102A DAC  │
           │ - BMP280        │          │ - BH1750 light  │    │ - PAM8403 AMP   │
           │ - NEO-6M GPS   │          │ - DS18B20 temp  │    │ - Transducers   │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   MOTORS        │          │   PLANTING      │    │   COMMS         │
           │                 │          │   SYSTEM        │    │                 │
           │ - ESC1-4        │          │ - Seed servo    │    │ - ESP8266 WiFi  │
           │ - Brushless     │          │ - Water pump    │    │ - HC-12 Radio   │
           │                 │          │ - Agitator      │    │ - Buzzer        │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
```

---

## ARDUINO MEGA PIN MAP

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
| A3 | Pump current | Analog |

---

## SOIL MOISTURE SENSOR

```
SOIL MOISTURE CIRCUIT:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │       SOIL MOISTURE SENSOR          │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  AOUT ──────→ Arduino A0           │
  │  DOUT ──────→ Arduino D2 (optional)│
  │                                     │
  │  Analog output: 0-1023             │
  │  Dry: ~800 (high resistance)       │
  │  Wet: ~300 (low resistance)        │
  │                                     │
  │  Mount on bottom of drone          │
  │  Probes extend 2cm below frame     │
  │                                     │
  └─────────────────────────────────────┘

  TWO sensors for different plant zones
```

---

## LIGHT SENSOR (BH1750)

```
LIGHT SENSOR CIRCUIT:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │          BH1750 Module              │
  │                                     │
  │  VCC ───────→ 3.3V                 │
  │  GND ───────→ GND                  │
  │  SDA ───────→ Arduino Pin 20 (SDA) │
  │  SCL ───────→ Arduino Pin 21 (SCL) │
  │  ADDR ──────→ GND (0x23)          │
  │                                     │
  │  I2C Address: 0x23                 │
  │  Range: 0-65535 lux                │
  │  Resolution: 1 lux                 │
  │                                     │
  │  Used to measure sunlight          │
  │  for optimal planting timing       │
  │                                     │
  └─────────────────────────────────────┘
```

---

## WATER PUMP RELAY

```
WATER PUMP CIRCUIT:
═══════════════════════════════════════════════════════════════

  Arduino Pin 13 ──→ Relay Module ──→ Water Pump (12V)

  ┌─────────────────────────────────────┐
  │         RELAY MODULE                │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  IN ────────→ Arduino Pin 13       │
  │  COM ───────→ Battery + (12V)      │
  │  NO ────────→ Water pump +         │
  │  Water pump - ──→ Battery -        │
  │                                     │
  │  Relay rated: 10A at 12V           │
  │  Pump draws: 2A at 12V            │
  │                                     │
  └─────────────────────────────────────┘

  SAFETY: Pump only runs when drone is
  within 2m of ground (altitude check)
```

---

## COMPLETE SCHEMATIC TABLE

| Component | Pins | I2C Address | Voltage | Current |
|-----------|------|-------------|---------|---------|
| Arduino Mega | - | - | 5V | 200mA |
| MPU6050 | 20,21 | 0x68 | 3.3V | 5mA |
| BMP280 | 20,21 | 0x76 | 3.3V | 1mA |
| BH1750 | 20,21 | 0x23 | 3.3V | 0.12mA |
| OLED | 20,21 | 0x3C | 5V | 20mA |
| Soil moisture x2 | A0, A1 | Analog | 5V | 10mA |
| NEO-6M GPS | 16,17 | Serial | 3.3V | 45mA |
| ESP8266 | 10,11 | Serial | 3.3V | 80mA |
| HC-12 | 18,19 | Serial | 5V | 20mA |
| PCM5102A | 4,7,8 | I2S | 5V | 20mA |
| PAM8403 | Analog | - | 5V | 500mA |
| Seed servo | 12 | PWM | 5V | 250mA |
| Water pump relay | 13 | Digital | 5V | 80mA |
| Agitator motor | 14 | Digital | 12V | 500mA |
