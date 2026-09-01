# PHI FTL CAR — POWER SYSTEM

## FPB-80 Battery System

---

## FPB-80 SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Nominal Voltage | 80V DC |
| Capacity | 180Ah |
| Energy | 14,400 Wh (14.4 kWh) |
| Weight | 252 kg |
| Dimensions | 1100×550×380mm |
| Cell Configuration | 20S (20 series) |
| Cell Voltage | 3.2V nominal (LiFePO4) |
| Max Discharge | 360A (5C) |
| Charge Rate | 32A (0.18C) |
| Cycle Life | 5000+ cycles |
| Self-Discharge | <2% per month |
| Operating Temp | -20°C to 55°C |
| IP Rating | IP67 |
| Cost | $12,000 |

---

## POWER CONSUMPTION

| Mode | Power | Duration | SoC Used |
|------|-------|----------|----------|
| Idle (warp off) | 1.8 kW | 8.0 hours | 100% |
| Normal driving | 28 kW | 0.51 hours | 100% |
| Highway cruise | 42 kW | 0.34 hours | 100% |
| Warp field (idle) | 6 kW | 2.4 hours | 100% |
| FTL (D1-D3) | 95 kW | 0.15 hours | 100% |
| FTL (D4-D6) | 200 kW | 0.07 hours | 100% |
| Maximum output | 280 kW | 0.05 hours | 100% |

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

## CHARGING SYSTEM

| Parameter | Value |
|-----------|-------|
| Charge port | CCS2 combo |
| Max AC charge | 22 kW (3-phase) |
| Max DC charge | 128 kW |
| 10-80% DC time | 35 minutes |
| 0-100% AC time | 2.8 hours |
| Charge frequency | 432 Hz (resonant) |
| Charge efficiency | 97% |
