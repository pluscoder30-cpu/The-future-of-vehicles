# PHI AI FIRE DRONE — WIRING DIAGRAMS

## Electrical Wiring Specifications (AI-Enhanced)

---

## POWER DISTRIBUTION

```
POWER FLOW:
═══════════════════════════════════════════════════════════════

  ┌─────────────────┐
  │  FPB-10 BATTERY │
  │  24V · 50Ah     │
  │  1200Wh         │
  └────────┬────────┘
           │
    ┌──────┴──────┐
    │  40A FUSE   │
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │  MAIN SWITCH│
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
    │  │RETARDANT │  │ THERMAL  │  │FREQ   │ │
    │  │ PUMP 12V │  │ CAM 3.3V │  │ GEN   │ │
    │  └──────────┘  └──────────┘  └───────┘ │
    │                                          │
    └──────────────────────────────────────────┘
```

---

## AI PROCESSOR WIRING

```
RASPBERRY PI ZERO 2W CONNECTIONS:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────┐
  │              RASPBERRY PI ZERO 2W                   │
  │                                                     │
  │  GPIO 14 (TX) ───→ Arduino RX1                     │
  │  GPIO 15 (RX) ←─── Arduino TX1                     │
  │  5V ───────────→ 5V Supply                        │
  │  GND ──────────→ Common Ground                    │
  │                                                     │
  │  CSI Port ───────→ Pi Camera (fire visual)         │
  │  I2C ───────────→ Thermal MLX90614 (shared)       │
  │                                                     │
  └─────────────────────────────────────────────────────┘
```

---

## THERMAL CAMERA WIRING

```
MLX90614 THERMAL SENSOR:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │         MLX90614 Module             │
  │                                     │
  │  VIN ───────→ 3.3V                 │
  │  GND ───────→ GND                  │
  │  SDA ───────→ Arduino Pin 20 (SDA) │
  │  SCL ───────→ Arduino Pin 21 (SCL) │
  │                                     │
  │  I2C Address: 0x5A                 │
  │  Range: -70°C to 380°C             │
  │  Accuracy: ±0.5°C                  │
  │  Field of View: 90°                │
  │                                     │
  │  Purpose: Fire detection           │
  │  Trigger: > 50°C                   │
  └─────────────────────────────────────┘
```

---

## RETARDANT PUMP WIRING

```
RETARDANT PUMP CONTROL:
═══════════════════════════════════════════════════════════════

  Arduino Pin 24 ──→ MOSFET Gate
  MOSFET Drain ────→ Pump Motor (-)
  MOSFET Source ───→ GND
  Pump Motor (+) ──→ 12V Bus

  ┌─────────────────────────────────────┐
  │  Pump: 12V high-flow water pump     │
  │  Flow rate: 2L/min                  │
  │  Duty cycle: PWM controlled         │
  │  AI adjusts flow based on fire size │
  └─────────────────────────────────────┘
```
