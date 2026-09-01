# PHI ANIMAL DRONE — WIRING DIAGRAMS

## Electrical Wiring

---

## POWER DISTRIBUTION

```
FPB-5 (12V) → Fuse → Switch
  ├──→ ESC1-4 → Motors (12V)
  ├──→ 5V Buck → Arduino, servos, sensors
  ├──→ 5V → Cameras
  └──→ 3.3V → ESP8266, GPS
```

---

## PIN ALLOCATION

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion |
| 3 | ESC1 | Motor 1 |
| 4 | PCM5102A DIN | Frequency |
| 5 | ESC2 | Motor 2 |
| 6 | ESC3 | Motor 3 |
| 7-8 | PCM5102A | Freq clock/word |
| 9 | ESC4 | Motor 4 |
| 10-11 | ESP8266 | WiFi |
| 12 | Food servo | Dispenser |
| 13 | Buzzer | Alerts |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 | Telemetry |
| 20-21 | I2C | Sensors |
| A0 | Thermal sensor | MLX90614 |
| A1 | Camera video | Composite |
| A2 | Battery voltage | Monitor |
