# PHI PLANT DRONE — POWER SYSTEM

## FPB-5 Battery Design and Power Distribution

---

## FPB-5 FIELD PLASMA BATTERY

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
| Charge Time | 3 hours (standard) |
| Cycle Life | 2000+ cycles |

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
    │                                            │
    │  ├──→ ESC1-4 ──→ Motors (12V direct)      │
    │  ├──→ 5V Buck ──→ Arduino, servos, sensors│
    │  ├──→ 12V direct ──→ Water pump (via relay)│
    │  └──→ 3.3V Buck ──→ ESP8266, GPS          │
    │                                            │
    └────────────────────────────────────────────┘
```

---

## POWER CONSUMPTION

### Flight Mode

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Motors (4x) | 12V | 12A total | 144W |
| Arduino | 5V | 200mA | 1W |
| Sensors | 5V | 100mA | 0.5W |
| ESP8266 | 3.3V | 80mA | 0.26W |
| GPS | 3.3V | 45mA | 0.15W |
| **Total** | | | **145.9W** |

### Planting Mode (hover + planting)

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Motors (4x) | 12V | 10A total | 120W |
| Water pump | 12V | 2A | 24W |
| Seed servo | 5V | 250mA | 1.25W |
| Agitator | 12V | 500mA | 6W |
| Arduino | 5V | 200mA | 1W |
| Sensors | 5V | 100mA | 0.5W |
| Frequency gen | 5V | 500mA | 2.5W |
| **Total** | | | **155.25W** |

---

## FLIGHT TIME CALCULATIONS

### Hover Time

```
HOVER ENDURANCE:
═══════════════════════════════════════════════════════════════

  Battery capacity: 600Wh
  Hover power (no payload): 100W
  Hover power (1kg payload): 130W
  Efficiency factor: 0.85

  Effective capacity: 600 × 0.85 = 510Wh

  Hover time (no payload): 510 / 100 = 5.1 hours
  Hover time (1kg payload): 510 / 130 = 3.9 hours

  Conservative: 3.5 hours with payload
```

### Range

```
RANGE CALCULATION:
═══════════════════════════════════════════════════════════════

  Cruise speed: 20 km/h
  Cruise power: ~110W
  Effective capacity: 510Wh

  Flight time: 510 / 110 = 4.6 hours
  Range: 20 × 4.6 = 92 km theoretical

  Practical: 12 km one-way (24 km round trip)
  (with 20% reserve)
```

---

## BATTERY MANAGEMENT

### Charge Protocol

```
CHARGING SEQUENCE:
═══════════════════════════════════════════════════════════════

  Standard: 0.5C = 25A to 14.4V
  PHI: 0.5C / φ = 15.4A (gentler, longer life)

  Charge time:
  Standard: 3 hours
  PHI: 5 hours (but 20% more cycles)
```

### State of Charge

| Voltage | SoC | Status |
|---------|-----|--------|
| 14.4V | 100% | Full |
| 13.6V | 80% | Good |
| 12.8V | 60% | Fair |
| 12.0V | 40% | Low — plan return |
| 11.2V | 20% | Critical — land |
| 10.8V | 10% | Emergency land |

---

## SAFETY FEATURES

| Feature | Threshold | Action |
|---------|-----------|--------|
| Over-charge | >14.6V | Charger disconnect |
| Over-discharge | <10.8V | Flight termination |
| Over-current | >30A | Fuse blow |
| Short circuit | >100A | Fuse blow instantly |
| Over-temperature | >60°C | Warning |
