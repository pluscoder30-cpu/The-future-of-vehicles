# PHI WATER DRONE — CIRCUIT SCHEMATICS

## Circuit Design

---

## WATER SENSOR CIRCUITS

```
pH SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  POUT → Arduino A0                 │
  │  Range: 0-14 pH, Resolution: 0.1   │
  └─────────────────────────────────────┘

TURBIDITY SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  AOUT → Arduino A1                 │
  │  Range: 0-4000 NTU                │
  │  Clean water: < 10 NTU            │
  └─────────────────────────────────────┘
```

---

## FILTRATION CONTROL

```
FILTRATION SYSTEM:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 → Relay → Water pump (12V)
  Arduino Pin 13 → Relay → UV LED (5V)

  Water flow:
  Intake → Mesh → Carbon → UV LED → Output

  Processing: 1 liter per minute
```
