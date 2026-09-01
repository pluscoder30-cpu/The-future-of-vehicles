# PHI TOXIC DRONE — WIRING DIAGRAMS

## Electrical Wiring

---

## POWER DISTRIBUTION

```
FPB-10 (24V) → 50A Fuse → Switch
  ├──→ ESC1-4 → Motors (24V)
  ├──→ 5V Buck → Arduino, sensors
  ├──→ 24V → Neutralizer pump (via relay)
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
| 10-11 | ESP8266 | WiFi |
| 12 | Neutralizer pump relay | Pump |
| 13 | Buzzer | Hazmat alert |
| 14 | Hazmat LED (red) | Warning light |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 x2 | Telemetry |
| 20-21 | I2C | Sensors |
| A0 | MQ-135 VOC | Analog |
| A1 | MQ-7 CO | Analog |
| A2 | MQ-2 smoke | Analog |
| A3 | pH sensor | Analog |
| A4 | Battery voltage | Monitor |
| A5 | Neutralizer level | Analog |
