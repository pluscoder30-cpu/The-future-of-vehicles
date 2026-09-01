# PHI FOOD DRONE — CIRCUIT SCHEMATICS

## Circuit Design

---

## MAIN CIRCUIT OVERVIEW

```
SYSTEM BLOCK DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  FPB-5      │────→│  POWER      │────→│  ARDUINO    │
  │  BATTERY    │     │  MANAGEMENT │     │  MEGA 2560  │
  └─────────────┘     └─────────────┘     └──────┬──────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────┐
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   FLIGHT        │          │   FOOD          │    │   FREQUENCY     │
           │   SENSORS       │          │   SENSORS       │    │   GENERATOR     │
           │ - MPU6050       │          │ - Soil moisture │    │ - PCM5102A      │
           │ - BMP280        │          │ - pH sensor     │    │ - PAM8403       │
           │ - GPS           │          │ - BH1750 light  │    │ - Transducers   │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   MOTORS        │          │   PLANTING      │    │   COMMS         │
           │ - ESC1-4        │          │ - Seed servos x3│    │ - ESP8266       │
           │                 │          │ - Nutrient pump │    │ - HC-12         │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
```

---

## ARDUINO PIN MAP

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion |
| 3 | ESC1 Signal | Motor 1 |
| 4 | PCM5102A DIN | Frequency data |
| 5 | ESC2 Signal | Motor 2 |
| 6 | ESC3 Signal | Motor 3 |
| 7 | PCM5102A BCK | Frequency clock |
| 8 | PCM5102A LCK | Frequency word |
| 9 | ESC4 Signal | Motor 4 |
| 10 | ESP8266 RX | WiFi |
| 11 | ESP8266 TX | WiFi |
| 12 | Seed servo 1 | Herb gate |
| 13 | Seed servo 2 | Veg gate |
| 14 | Seed servo 3 | Flower gate |
| 15 | Nutrient pump relay | Pump |
| 16 | GPS TX | GPS |
| 17 | GPS RX | GPS |
| 18 | HC-12 TX | Telemetry |
| 19 | HC-12 RX | Telemetry |
| 20 | I2C SDA | I2C bus |
| 21 | I2C SCL | I2C clock |
| A0 | Soil moisture 1 | Herbs |
| A1 | Soil moisture 2 | Vegetables |
| A2 | Soil moisture 3 | Flowers |
| A3 | pH sensor | Soil pH |
| A4 | Battery voltage | Monitor |

---

## SENSOR SPECIFICATIONS

| Sensor | I2C Address | Voltage | Range |
|--------|-------------|---------|-------|
| MPU6050 | 0x68 | 3.3V | Gyro/Accel |
| BMP280 | 0x76 | 3.3V | Pressure/Alt |
| BH1750 | 0x23 | 3.3V | 0-65535 lux |
| OLED | 0x3C | 5V | Display |
| pH sensor | Analog | 5V | 0-14 pH |
| Soil moisture x3 | Analog | 5V | 0-1023 |
