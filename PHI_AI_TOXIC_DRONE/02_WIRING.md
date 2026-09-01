# PHI AI TOXIC DRONE — WIRING DIAGRAMS

## Electrical Wiring (AI-Enhanced)

---

## POWER DISTRIBUTION

```
POWER FLOW:
═══════════════════════════════════════════════════════════════

  ┌─────────────────┐
  │  FPB-10 BATTERY │
  │  24V · 50Ah     │
  └────────┬────────┘
           │
    ┌──────┴──────┐
    │  40A FUSE   │
    └──────┬──────┘
           │
    ┌──────┴──────────────────────────────────┐
    │                                          │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │ MOTORS   │  │AVIONICS  │  │ AI    │ │
    │  │ 24V Bus  │  │ 5V Reg   │  │ 5V Reg│ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │                                          │
    │  ┌──────────┐  ┌──────────┐  ┌───────┐ │
    │  │NEUTRALIZER│ │ SENSORS  │  │FREQ   │ │
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
  CSI Port ───────→ Pi Camera (spill visual)
  I2C ───────────→ Chemical sensors (shared)
```

---

## CHEMICAL SENSOR WIRING

```
CHEMICAL SENSOR CONNECTIONS:
═══════════════════════════════════════════════════════════════

  MQ-135 (Air Quality):
  ├── Analog Out ──→ Arduino A0
  ├── VCC ──→ 5V
  └── GND ──→ GND

  MQ-2 (Gas Leak):
  ├── Analog Out ──→ Arduino A1
  ├── VCC ──→ 5V
  └── GND ──→ GND

  pH Sensor:
  ├── Analog Out ──→ Arduino A2
  ├── VCC ──→ 5V
  └── GND ──→ GND

  TDS Sensor:
  ├── Analog Out ──→ Arduino A3
  ├── VCC ──→ 5V
  └── GND ──→ GND

  DS18B20 Temperature:
  ├── Data ──→ Arduino Pin 22
  ├── VCC ──→ 5V
  └── GND ──→ GND

  Color Sensor:
  ├── S0-S3 ──→ Arduino Digital
  ├── OUT ──→ Arduino Pin 24
  ├── VCC ──→ 5V
  └── GND ──→ GND
```

---

## NEUTRALIZER PUMP WIRING

```
NEUTRALIZER PUMP CONTROL:
═══════════════════════════════════════════════════════════════

  Arduino Pin 25 ──→ MOSFET Gate
  MOSFET Drain ────→ Pump Motor (-)
  MOSFET Source ───→ GND
  Pump Motor (+) ──→ 12V Bus

  ┌─────────────────────────────────────┐
  │  Pump: 12V chemical-resistant pump  │
  │  Flow rate: 0.5L/min                │
  │  Material: PTFE lined               │
  │  AI controls flow and duration      │
  └─────────────────────────────────────┘
```
