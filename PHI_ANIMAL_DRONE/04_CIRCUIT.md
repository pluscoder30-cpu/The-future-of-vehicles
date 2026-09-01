# PHI ANIMAL DRONE — CIRCUIT SCHEMATICS

## Circuit Design

---

## THERMAL CAMERA CIRCUIT

```
MLX90614 THERMAL SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │         MLX90614 Module             │
  │                                     │
  │  VCC ───────→ 3.3V                 │
  │  GND ───────→ GND                  │
  │  SDA ───────→ Arduino Pin 20 (SDA) │
  │  SCL ───────→ Arduino Pin 21 (SCL) │
  │                                     │
  │  I2C Address: 0x5A                 │
  │  Range: -70°C to +380°C           │
  │  Accuracy: +/- 0.5°C              │
  │  Field of View: 90°               │
  │                                     │
  │  Used for:                          │
  │  - Animal heat detection           │
  │  - Night observation               │
  │  - Health monitoring               │
  │                                     │
  └─────────────────────────────────────┘
```

---

## 1080P CAMERA

```
CAMERA MODULE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │       1080p Camera Module           │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  VIDEO ─────→ Arduino A1 (analog)  │
  │ /audio ─────→ Not connected        │
  │                                     │
  │  Resolution: 1920x1080             │
  │  Frame rate: 30fps                 │
  │  Lens: 120° wide angle             │
  │                                     │
  │  Transmits via WiFi to app         │
  │                                     │
  └─────────────────────────────────────┘
```

---

## COMPLETE PIN MAP

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion |
| 3-6 | ESC1-4 | Motors |
| 4,7,8 | PCM5102A | Frequency |
| 9 | ESC4 | Motor 4 |
| 10-11 | ESP8266 | WiFi |
| 12 | Food servo | Dispenser |
| 13 | Buzzer | Alerts |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 | Telemetry |
| 20-21 | I2C | Thermal, sensors |
| A0 | Camera video | 1080p |
| A2 | Battery voltage | Monitor |
