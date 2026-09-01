# PHI FIRE DRONE — CIRCUIT SCHEMATICS

## Circuit Design

---

## THERMAL DETECTION CIRCUIT

```
MLX90614 THERMAL SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │         MLX90614 Module             │
  │                                     │
  │  VCC ───────→ 3.3V                 │
  │  GND ───────→ GND                  │
  │  SDA ───────→ Arduino Pin 20       │
  │  SCL ───────→ Arduino Pin 21       │
  │                                     │
  │  I2C Address: 0x5A                 │
  │  Range: -70°C to +380°C           │
  │  Detection range: 100m             │
  │  Field of View: 90°               │
  │                                     │
  │  Used for:                          │
  │  - Fire detection (temp > 100°C)   │
  │  - Hotspot mapping                 │
  │  - Fire spread monitoring          │
  │                                     │
  └─────────────────────────────────────┘
```

---

## SMOKE SENSOR

```
SMOKE SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │         MQ-2 Smoke Sensor          │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  DOUT ──────→ Arduino Pin 14       │
  │  AOUT ──────→ Arduino A4           │
  │                                     │
  │  Detects: Smoke, methane, CO       │
  │  Range: 0-10000 ppm               │
  │  Response: < 10 seconds           │
  │                                     │
  └─────────────────────────────────────┘
```

---

## RETARDANT PUMP

```
RETARDANT DELIVERY:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 ──→ Relay ──→ Pump (24V)

  ┌──────────────────────────────────────┐
  │  RETARDANT SYSTEM:                   │
  │                                      │
  │  ┌──────────┐                       │
  │  │ TANK 2L  │                       │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ PUMP 24V │ 5L/min               │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐                       │
  │  │ VALVE    │                       │
  │  └────┬─────┘                       │
  │       │                              │
  │  ┌────┴─────┐  ┌────────┐          │
  │  │ SPLITTER │──│NOZZLE 1│          │
  │  │          │──│NOZZLE 2│          │
  │  └──────────┘  └────────┘          │
  └──────────────────────────────────────┘
```
