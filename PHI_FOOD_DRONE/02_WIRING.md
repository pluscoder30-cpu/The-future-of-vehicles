# PHI FOOD DRONE — WIRING DIAGRAMS

## Electrical Wiring

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
    │  ├──→ ESC1-4 ──→ Motors (12V)             │
    │  ├──→ 5V Buck ──→ Arduino, servos         │
    │  ├──→ 12V direct ──→ Nutrient pump        │
    │  └──→ 3.3V Buck ──→ ESP8266, GPS          │
    └────────────────────────────────────────────┘
```

---

## SENSOR WIRING

| Pin | Connection | Function |
|-----|------------|----------|
| 2 | MPU6050 INT | Motion |
| 3 | ESC1 Signal | Motor 1 |
| 4 | PCM5102A DIN | Frequency |
| 5 | ESC2 Signal | Motor 2 |
| 6 | ESC3 Signal | Motor 3 |
| 7 | PCM5102A BCK | Freq clock |
| 8 | PCM5102A LCK | Freq word |
| 9 | ESC4 Signal | Motor 4 |
| 10 | ESP8266 RX | WiFi |
| 11 | ESP8266 TX | WiFi |
| 12-14 | Seed servos | Herb/Veg/Flower |
| 15 | Nutrient pump relay | Pump |
| 16-17 | GPS | Serial2 |
| 18-19 | HC-12 | Telemetry |
| 20-21 | I2C bus | Sensors |
| A0-A2 | Soil moisture | Analog |
| A3 | pH sensor | Analog |
| A4 | Battery voltage | Analog |

---

## SEED SYSTEM WIRING

```
3-CHANNEL SEED DISPENSER:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 ──→ Servo 1 (Herb seeds gate)
  Arduino Pin 13 ──→ Servo 2 (Vegetable seeds gate)
  Arduino Pin 14 ──→ Servo 3 (Flower seeds gate)

  Each hopper has:
  - Gravity-fed seed storage
  - Servo-controlled gate
  - Vibration agitator motor

  ┌──────────────────────────────────────┐
  │  SEED BAY LAYOUT:                    │
  │                                      │
  │  ┌────────┐ ┌────────┐ ┌────────┐  │
  │  │ HERBS  │ │  VEG   │ │FLOWERS │  │
  │  │ 130mm  │ │  80mm  │ │  50mm  │  │
  │  │ basil  │ │ lettuce│ │ marigold│  │
  │  │ cilantro│ │ spinach│ │ petunia│  │
  │  │ parsley│ │ radish │ │ zinnia │  │
  │  └────────┘ └────────┘ └────────┘  │
  │                                      │
  │  Bay sizes in phi ratio:             │
  │  130/80 = 1.625 ≈ phi              │
  │  80/50 = 1.600 ≈ phi               │
  └──────────────────────────────────────┘
```

---

## NUTRIENT SYSTEM WIRING

```
NUTRIENT DELIVERY:
═══════════════════════════════════════════════════════════════

  Arduino Pin 15 ──→ Relay ──→ Nutrient pump (12V)

  ┌──────────────────────────────────────┐
  │  NUTRIENT SYSTEM:                    │
  │                                      │
  │  ┌──────────┐                       │
  │  │ TANK     │ 300ml liquid nutrient │
  │  │ 300ml    │                       │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ PUMP     │ 12V, 1L/min          │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ VALVE    │ prevent drip          │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ NOZZLE   │ adjustable spray      │
  │  └──────────┘                       │
  └──────────────────────────────────────┘
```

---

## pH SENSOR WIRING

```
pH SENSOR CIRCUIT:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │         pH SENSOR MODULE            │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  POUT ──────→ Arduino A3           │
  │  PINT ──────→ Arduino D2          │
  │                                     │
  │  Range: 0-14 pH                    │
  │  Resolution: 0.1 pH               │
  │  Accuracy: +/- 0.1 pH             │
  │                                     │
  │  Used to measure soil pH           │
  │  Optimal for most plants: 6.0-7.0 │
  │                                     │
  └─────────────────────────────────────┘
```
