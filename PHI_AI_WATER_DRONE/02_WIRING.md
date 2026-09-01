# PHI AI WATER DRONE — WIRING DIAGRAMS

## Electrical Wiring (AI-Enhanced)

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
    ┌──────┴──────────────────────────────────┐
    │                                          │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │ MOTORS   │  │AVIONICS  │  │ AI    │ │
    │  │ 12V Bus  │  │ 5V Reg   │  │ 5V Reg│ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │                                          │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │ FILTRATION│ │ SENSORS  │  │FREQ   │ │
    │  │ PUMP 12V │  │ 5V Reg   │  │ GEN   │ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │                                          │
    └──────────────────────────────────────────┘
```

---

## AI PROCESSOR WIRING

```
RASPBERRY PI ZERO 2W:
═══════════════════════════════════════════════════════════════

  GPIO 14 (TX) ───→ Arduino RX1
  GPIO 15 (RX) ←─── Arduino TX1
  5V ───────────→ 5V Supply
  GND ──────────→ Common Ground
  CSI Port ───────→ Pi Camera (water surface)
  I2C ───────────→ Water sensors (shared)
```

---

## WATER SENSOR WIRING

```
WATER SENSOR CONNECTIONS:
═══════════════════════════════════════════════════════════════

  pH Sensor:
  ├── Analog Out ──→ Arduino A0
  ├── VCC ──→ 5V
  └── GND ──→ GND

  Turbidity Sensor:
  ├── Analog Out ──→ Arduino A1
  ├── VCC ──→ 5V
  └── GND ──→ GND

  TDS Sensor:
  ├── Analog Out ──→ Arduino A2
  ├── VCC ──→ 5V
  └── GND ──→ GND

  DS18B20 Temperature:
  ├── Data ──→ Arduino Pin 22
  ├── VCC ──→ 5V
  └── GND ──→ GND
```
