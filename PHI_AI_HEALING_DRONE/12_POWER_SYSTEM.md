# PHI AI HEALING DRONE — POWER SYSTEM

## FPB-5 Battery Design and Power Distribution (AI-Enhanced)

---

## FPB-5 FIELD PLASMA BATTERY

### Specifications

| Parameter | Value |
|-----------|-------|
| Chemistry | Field Plasma (FPB) |
| Model | FPB-5 |
| Nominal Voltage | 12.0V |
| Capacity | 50Ah |
| Energy | 600Wh |
| Weight | 850g |
| Dimensions | 120mm x 70mm x 30mm |
| Max Discharge | 30A continuous |
| Charge Voltage | 14.4V |
| Charge Current | 15A (standard) |
| Cycle Life | 2000+ cycles |
| Self-Discharge | 2% per month |
| Operating Temp | -20°C to 50°C |
| Cost | $85 |

---

## POWER DISTRIBUTION (AI-ENHANCED)

```
POWER FLOW DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────────┐
  │  FPB-5 BATTERY  │
  │  12V · 50Ah     │
  │  600Wh          │
  └────────┬────────┘
           │
           │ XT60 Connector
           │
    ┌──────┴──────┐
    │  30A FUSE   │ ← Protects against shorts
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │  MAIN SWITCH│ ← Emergency shutoff
    │  (30A)      │
    └──────┬──────┘
           │
    ┌──────┴──────────────────────────────────────────────┐
    │                                                      │
    │  12V BUS                                             │
    │  ├──→ ESC1 (Motor 1) ──→ Brushless Motor 1         │
    │  ├──→ ESC2 (Motor 2) ──→ Brushless Motor 2         │
    │  ├──→ ESC3 (Motor 3) ──→ Brushless Motor 3         │
    │  ├──→ ESC4 (Motor 4) ──→ Brushless Motor 4         │
    │  │                                                   │
    │  ├──→ 5V BUCK REGULATOR ──→ Arduino Mega            │
    │  │    (LM2596)          ├──→ MPU6050                 │
    │  │                      ├──→ BMP280                  │
    │  │                      ├──→ OLED Display            │
    │  │                      ├──→ Medical Sensors         │
    │  │                      └──→ Servos                  │
    │  │                                                   │
    │  ├──→ 3.3V BUCK REGULATOR ──→ ESP8266               │
    │  │    (AMS1117)           ├──→ BMP180                │
    │  │                        └──→ GPS (部分)             │
    │  │                                                   │
    │  ├──→ 5V BUCK REGULATOR ──→ PCM5102A DAC            │
    │  │    (LM2596)          └──→ PAM8403 Amplifier       │
    │  │                                                   │
    │  └──→ 5V BUCK REGULATOR ──→ RASPBERRY PI ZERO 2W    │
    │       (LM2596)          └──→ Pi Camera Module        │
    │                                                      │
    └──────────────────────────────────────────────────────┘
```

---

## POWER CONSUMPTION

### Flight Mode

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Motors (4x) | 12V | 15A total | 180W |
| Arduino | 5V | 200mA | 1W |
| Sensors | 5V | 100mA | 0.5W |
| ESP8266 | 3.3V | 80mA | 0.26W |
| GPS | 3.3V | 45mA | 0.15W |
| ESCs (logic) | 5V | 80mA | 0.4W |
| **AI System** | **5V** | **540mA** | **2.7W** |
| **Total** | | | **185.0W** |

### AI System Power Breakdown

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Raspberry Pi Zero 2W | 5V | 350mA | 1.75W |
| Pi Camera Module | 5V | 180mA | 0.9W |
| Serial Level Shifter | 5V | 10mA | 0.05W |
| **AI Total** | | **540mA** | **2.7W** |

---

## FLIGHT TIME CALCULATIONS

### Hover Time (with AI)

```
HOVER ENDURANCE:
═══════════════════════════════════════════════════════════════

  Battery capacity: 600Wh
  Hover power: 100.3W (98.3W + 2W AI)
  Efficiency factor: 0.85

  Effective capacity: 600 × 0.85 = 510Wh

  Hover time = 510Wh / 100.3W = 5.08 hours

  With 500g payload:
  Total hover power: 110.3W
  Hover time = 510 / 110.3 = 4.62 hours

  Conservative estimate: 4.0 hours (with safety margin)
  (AI adds ~2W overhead — minimal impact on flight time)
```

---

## AI POWER MANAGEMENT

```
AI POWER STATES:
═══════════════════════════════════════════════════════════════

  IDLE: Pi Zero in sleep mode
  ├── Power: 0.1W
  ├── Wake: Serial interrupt from Arduino
  └── Use: During transit (no diagnosis needed)

  ACTIVE: Pi Zero processing
  ├── Power: 2.7W
  ├── Camera: Active
  └── Use: During patient assessment

  INFERENCE: AI model running
  ├── Power: 2.7W (CPU at 100%)
  ├── Duration: <100ms per inference
  └── Use: When analyzing sensor data

  POWER SAVINGS:
  ├── AI uses ~2W average (vs 2.7W peak)
  ├── Flight time impact: ~2% reduction
  └── Acceptable for AI capability gain
```
