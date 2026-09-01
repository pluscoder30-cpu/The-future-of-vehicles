# PHI WATER DRONE — WIRING DIAGRAMS

## Electrical Wiring

---

## POWER DISTRIBUTION

```
FPB-5 (12V) → Fuse → Switch
  ├──→ ESC1-4 → Motors (12V)
  ├──→ 5V Buck → Arduino, sensors
  ├──→ 12V → Water pump (via relay)
  └──→ 3.3V → ESP8266, GPS
```

---

## PIN ALLOCATION

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion |
| 3-6 | ESC1-4 | Motors |
| 4,7,8 | PCM5102A | Frequency |
| 10-11 | ESP8266 | WiFi |
| 12 | Water pump relay | Pump |
| 13 | UV LED relay | UV sterilize |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 | Telemetry |
| 20-21 | I2C | Sensors |
| A0 | pH sensor | Analog |
| A1 | Turbidity sensor | Analog |
| A2 | Battery voltage | Monitor |
| A3 | Water level | Analog |
