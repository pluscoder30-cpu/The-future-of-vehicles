# PHI GARBAGE DRONE — WIRING DIAGRAMS

## Electrical Wiring

---

## POWER DISTRIBUTION

```
FPB-5 (12V) → Fuse → Switch
  ├──→ ESC1-4 → Motors (12V)
  ├──→ 5V Buck → Arduino, sensors, servos
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
| 12-14 | Arm servos | 2-DOF + gripper |
| 15-17 | Sort servos | Plastic/Metal/Paper |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 | Telemetry |
| 20-21 | I2C | Sensors |
| A0 | Metal detector | Analog |
| A1 | IR sensor left | Analog |
| A2 | IR sensor right | Analog |
| A3 | Battery voltage | Monitor |
