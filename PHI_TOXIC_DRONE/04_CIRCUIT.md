# PHI TOXIC DRONE — CIRCUIT SCHEMATICS

## Circuit Design

---

## CHEMICAL SENSOR CIRCUITS

```
MQ-135 VOC SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  AOUT → Arduino A0                 │
  │  DOUT → Arduino D2                 │
  │  Detects: NH3, NOx, CO2, benzene   │
  │  Range: 10-1000 ppm               │
  └─────────────────────────────────────┘

MQ-7 CO SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  AOUT → Arduino A1                 │
  │  Detects: Carbon monoxide          │
  │  Range: 10-1000 ppm               │
  └─────────────────────────────────────┘

MQ-2 SMOKE SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  AOUT → Arduino A2                 │
  │  Detects: Smoke, methane, LPG      │
  │  Range: 200-10000 ppm             │
  └─────────────────────────────────────┘

pH SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  POUT → Arduino A3                 │
  │  Range: 0-14 pH                   │
  │  Accuracy: +/- 0.1 pH            │
  └─────────────────────────────────────┘
```

---

## NEUTRALIZER CONTROL

```
NEUTRALIZER DELIVERY:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 → Relay → Pump (24V)

  ┌──────────────────────────────────────┐
  │  NEUTRALIZER SYSTEM:                 │
  │                                      │
  │  ┌──────────┐                       │
  │  │ TANK 1.5L│                       │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ PUMP 24V │                       │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ NOZZLE   │                       │
  │  └──────────┘                       │
  └──────────────────────────────────────┘
```

---

## HAZMAT WARNING SYSTEM

```
HAZMAT ALERTS:
═══════════════════════════════════════════════════════════════

  Arduino Pin 13 → Buzzer (audible alert)
  Arduino Pin 14 → Red LED (visual warning)

  Alert triggers:
  - VOC > 100 ppm (warning)
  - CO > 50 ppm (danger)
  - Smoke detected (danger)
  - pH < 4 or > 10 (corrosive)
```
