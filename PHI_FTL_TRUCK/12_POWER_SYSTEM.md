# PHI FTL TRUCK — POWER SYSTEM

## FPB-80 Battery System

---

## FPB-80 SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Nominal Voltage | 80V DC |
| Capacity | 200Ah |
| Energy | 16,000 Wh (16 kWh) |
| Weight | 280 kg |
| Dimensions | 1200×600×400mm |
| Cell Configuration | 20S (20 series) |
| Cell Voltage | 3.2V nominal (LiFePO4) |
| Max Discharge | 400A (5C) |
| Charge Rate | 40A (0.2C) |
| Cycle Life | 5000+ cycles |
| Self-Discharge | <2% per month |
| Operating Temp | -20°C to 55°C |
| IP Rating | IP67 |
| Cost | $15,000 |

---

## POWER CONSUMPTION

| Mode | Power | Duration | SoC Used |
|------|-------|----------|----------|
| Idle (warp off) | 2.5 kW | 6.4 hours | 100% |
| Normal driving | 35 kW | 0.46 hours | 100% |
| Highway cruise | 55 kW | 0.29 hours | 100% |
| Warp field (idle) | 8 kW | 2.0 hours | 100% |
| FTL (D1-D3) | 120 kW | 0.13 hours | 100% |
| FTL (D4-D6) | 250 kW | 0.06 hours | 100% |
| Maximum output | 320 kW | 0.05 hours | 100% |

---

## BATTERY STATE OF CHARGE

| Voltage | SoC | Range | Action |
|---------|-----|-------|--------|
| 84.0V | 100% | Full | Ready |
| 82.4V | 90% | Excellent | Normal ops |
| 80.8V | 80% | Good | Normal ops |
| 79.2V | 70% | Good | Monitor |
| 77.6V | 60% | Fair | Plan return |
| 76.0V | 50% | Fair | Reduce FTL |
| 74.4V | 40% | Low | Return home |
| 72.8V | 30% | Low | Emergency |
| 71.2V | 20% | Critical | Land now |
| 69.6V | 10% | Critical | Emergency |
| 68.0V | 0% | Empty | Shutdown |

---

## WARP FIELD POWER BUDGET

```
FTL POWER ALLOCATION:
══════════════════════════════════════════════════════════════

  Total FPB-80 output: 320 kW peak

  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │   POWER DISTRIBUTION                            │
  │                                                  │
  │   Warp coils (6×):          180 kW  (56.3%)     │
  │   Resonance stabilizer:      40 kW  (12.5%)     │
  │   Dimensional tuner:         15 kW   (4.7%)     │
  │   Field emitter nodes:       25 kW   (7.8%)     │
  │   Navigation/display:        10 kW   (3.1%)     │
  │   Traction motor:            35 kW  (10.9%)     │
  │   Auxiliary systems:         15 kW   (4.7%)     │
  │                                                  │
  │   TOTAL:                    320 kW (100%)       │
  │                                                  │
  └──────────────────────────────────────────────────┘

  At D6 (maximum FTL):
  - Warp coils: 180 kW
  - Duration: 16,000 Wh / 320 kW = 0.05 hours = 3 minutes
  - Distance at 12c: 3.24 million km
  
  At D1 (minimum FTL):
  - Warp coils: 180 kW
  - Duration: 16,000 Wh / 120 kW = 0.133 hours = 8 minutes
  - Distance at 1.2c: 2.88 million km
```

---

## CHARGING SYSTEM

| Parameter | Value |
|-----------|-------|
| Charge port | CCS2 combo |
| Max AC charge | 22 kW (3-phase) |
| Max DC charge | 160 kW |
| 10-80% DC time | 38 minutes |
| 0-100% AC time | 3.2 hours |
| Charge frequency | 432 Hz (resonant) |
| Charge efficiency | 97% |

---

## BATTERY HEALTH MONITORING

```
BMS ALERTS:
══════════════════════════════════════════════════════════════

  CELL IMBALANCE:
  - Normal: <50mV difference
  - Warning: 50-100mV difference
  - Critical: >100mV difference

  TEMPERATURE:
  - Normal: 20-40°C
  - Warning: 40-50°C
  - Critical: >50°C
  - Low warning: <0°C
  - Low critical: <-10°C

  CURRENT:
  - Normal: <300A
  - Warning: 300-400A
  - Critical: >400A

  VOLTAGE:
  - Normal: 72-84V
  - Warning: 68-72V or 84-86V
  - Critical: <68V or >86V
```
