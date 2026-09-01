# PHI HEALING DRONE — POWER SYSTEM

## FPB-5 Battery Design and Power Distribution

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
| Dimensions | 120mm × 70mm × 30mm |
| Max Discharge | 30A continuous |
| Charge Voltage | 14.4V |
| Charge Current | 15A (standard) |
| Cycle Life | 2000+ cycles |
| Self-Discharge | 2% per month |
| Operating Temp | -20°C to 50°C |
| Cost | $85 |

### Battery Construction

```
FPB-5 INTERNAL LAYOUT:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │  ┌────────────────────────────────────────────┐ │
  │  │           FIELD PLASMA CELLS               │ │
  │  │                                            │ │
  │  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐    │ │
  │  │  │Cell 1│ │Cell 2│ │Cell 3│ │Cell 4│    │ │
  │  │  │ 3V   │ │ 3V   │ │ 3V   │ │ 3V   │    │ │
  │  │  │ 12.5 │ │ 12.5 │ │ 12.5 │ │ 12.5 │    │ │
  │  │  │ Ah   │ │ Ah   │ │ Ah   │ │ Ah   │    │ │
  │  │  └──────┘ └──────┘ └──────┘ └──────┘    │ │
  │  │                                            │ │
  │  │  Configuration: 4S1P (4 series)           │ │
  │  │  Voltage: 4 × 3V = 12V nominal           │ │
  │  │  Capacity: 12.5Ah × 4 = 50Ah             │ │
  │  │                                            │ │
  │  └────────────────────────────────────────────┘ │
  │                                                  │
  │  ┌────────────────────────────────────────────┐ │
  │  │           BATTERY MANAGEMENT               │ │
  │  │                                            │ │
  │  │  • Cell balancing circuit                  │ │
  │  │  • Over-charge protection                  │ │
  │  │  • Over-discharge protection               │ │
  │  │  • Short circuit protection                │ │
  │  │  • Temperature monitoring                  │ │
  │  │                                            │ │
  │  └────────────────────────────────────────────┘ │
  │                                                  │
  │  CONNECTORS:                                    │
  │  • XT60 (main power)                           │
  │  • JST-XH (balance port)                      │ │
  │                                                  │
  └──────────────────────────────────────────────────┘
```

---

## POWER DISTRIBUTION

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
    │  │                      ├──→ Servos                  │
    │  │                      └──→ Buzzer                  │
    │  │                                                   │
    │  ├──→ 3.3V BUCK REGULATOR ──→ ESP8266               │
    │  │    (AMS1117)           ├──→ BMP180                │
    │  │                        └──→ GPS (部分)             │
    │  │                                                   │
    │  └──→ 5V BUCK REGULATOR ──→ PCM5102A DAC            │
    │       (LM2596)          └──→ PAM8403 Amplifier       │
    │                                                      │
    └──────────────────────────────────────────────────────┘
```

---

## VOLTAGE REGULATORS

### 5V Regulator (Main)

```
LM2596 BUCK CONVERTER:
═══════════════════════════════════════════════════════════════

  Input: 12V (FPB-5)
  Output: 5V (regulated)
  Current: 3A max
  Efficiency: 92%
  Heat sink: Required for > 1A

  Connections:
  VIN+ ──→ Battery + (via switch)
  VIN- ──→ Battery -
  VOUT+ ──→ 5V bus
  VOUT- ──→ GND bus

  Load: Arduino (200mA) + Sensors (50mA) + Servos (250mA)
        + Display (20mA) + Buzzer (30mA) = 550mA total
  Headroom: 2.45A (plenty)
```

### 3.3V Regulator

```
AMS1117-3.3V LDO:
═══════════════════════════════════════════════════════════════

  Input: 5V (from main buck)
  Output: 3.3V (regulated)
  Current: 800mA max
  Dropout: 1.3V
  Heat sink: Small tab

  Connections:
  VIN ──→ 5V bus
  GND ──→ GND bus
  VOUT ──→ 3.3V bus

  Load: ESP8266 (80mA) + BMP280 (1mA) + GPS (45mA)
        = 126mA total
  Headroom: 674mA (plenty)
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
| **Total** | | | **182.3W** |

### Hover Mode

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Motors (4x) | 12V | 8A total | 96W |
| Arduino | 5V | 200mA | 1W |
| Sensors | 5V | 100mA | 0.5W |
| ESP8266 | 3.3V | 80mA | 0.26W |
| GPS | 3.3V | 45mA | 0.15W |
| ESCs (logic) | 5V | 80mA | 0.4W |
| **Total** | | | **98.3W** |

### Standby Mode

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Arduino | 5V | 50mA | 0.25W |
| Sensors | 5V | 20mA | 0.1W |
| ESP8266 | 3.3V | 20mA | 0.066W |
| GPS | 3.3V | 10mA | 0.033W |
| **Total** | | | **0.45W** |

---

## FLIGHT TIME CALCULATIONS

### Hover Time

```
HOVER ENDURANCE:
═══════════════════════════════════════════════════════════════

  Battery capacity: 600Wh
  Hover power: 98.3W
  Efficiency factor: 0.85 (battery + regulator losses)

  Effective capacity: 600 × 0.85 = 510Wh

  Hover time = 510Wh / 98.3W = 5.19 hours

  With 500g payload:
  Additional motor power: ~10W
  Total hover power: 108.3W
  Hover time = 510 / 108.3 = 4.71 hours

  Conservative estimate: 4.0 hours (with safety margin)
```

### Range

```
RANGE CALCULATION:
═══════════════════════════════════════════════════════════════

  Cruise speed: 25 km/h
  Cruise power: ~130W (motors at cruise)
  Effective capacity: 510Wh

  Flight time = 510 / 130 = 3.92 hours

  Range = 25 km/h × 3.92 h = 98 km theoretical

  Practical range (with reserve):
  Reserve: 20% (always land with 20% battery)
  Usable: 80% × 3.92 = 3.14 hours
  Range = 25 × 3.14 = 78.5 km

  Conservative: 15 km one-way (30 km round trip)
```

---

## BATTERY MANAGEMENT

### Charge Protocol

```
CHARGING SEQUENCE:
═══════════════════════════════════════════════════════════════

  1. Connect charger to XT60 port
  2. Charger verifies cell voltages
  3. Balancing phase: equalize all cells
  4. Constant Current (CC) phase: 15A to 14.4V
  5. Constant Voltage (CV) phase: hold 14.4V until current < 1A
  6. Complete: all cells at 3.6V

  Charge Time:
  0% → 80%: 1.5 hours (CC phase)
  80% → 100%: 1.5 hours (CV phase)
  Total: 3 hours

  PHI-HARMONIC charge: 15A / φ = 9.3A
  Charge time: 5 hours (but 20% more cycles)
```

### State of Charge Indicator

| Voltage | SoC | Status | Action |
|---------|-----|--------|--------|
| 14.4V | 100% | Full | Ready |
| 13.6V | 80% | Good | Normal ops |
| 12.8V | 60% | Fair | Plan return |
| 12.0V | 40% | Low | Return to base |
| 11.2V | 20% | Critical | Land immediately |
| 10.8V | 10% | Emergency | Emergency land |
| 10.4V | 0% | Empty | Shutdown |

---

## SAFETY FEATURES

### Battery Protection

| Feature | Threshold | Action |
|---------|-----------|--------|
| Over-charge | >14.6V | Charger disconnect |
| Over-discharge | <10.8V | Flight termination |
| Over-current | >30A | Fuse blow |
| Short circuit | >100A | Fuse blow instantly |
| Over-temperature | >60°C | Warning + reduce power |
| Under-temperature | <-20°C | Prevent charging |

### Emergency Power

```
EMERGENCY POWER PROTOCOL:
═══════════════════════════════════════════════════════════════

  If battery fails in flight:

  1. Arduino detects voltage drop
  2. Immediately reduce motor power to minimum
  3. Begin controlled descent
  4. Activate GPS return-to-home
  5. Land as soon as possible
  6. If voltage < 10.4V: cut all motors, free fall

  Last resort: Deploy parachute (if installed)
```
