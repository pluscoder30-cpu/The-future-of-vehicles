# PHI FIRE DRONE — WIRING DIAGRAMS

## Electrical Wiring

---

## POWER DISTRIBUTION

```
FPB-10 (24V) → 50A Fuse → Switch
  ├──→ ESC1-4 → Motors (24V direct)
  ├──→ 5V Buck → Arduino, sensors
  ├──→ 24V → Retardant pump (via relay)
  └──→ 3.3V → ESP8266, GPS

NOTE: FPB-10 = 2× FPB-5 in series (24V)
```

---

## PIN ALLOCATION

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion |
| 3-6 | ESC1-4 | Motors |
| 4,7,8 | PCM5102A | Frequency |
| 9 | ESC4 | Motor 4 |
| 10-11 | ESP8266 | WiFi |
| 12 | Retardant pump relay | Pump |
| 13 | Buzzer | Fire alert |
| 14 | Smoke sensor | Digital |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 x2 | Telemetry |
| 20-21 | I2C | Thermal, sensors |
| A0 | Thermal sensor | MLX90614 |
| A1 | Camera video | 1080p |
| A2 | Battery voltage | Monitor |
| A3 | Retardant level | Analog |
