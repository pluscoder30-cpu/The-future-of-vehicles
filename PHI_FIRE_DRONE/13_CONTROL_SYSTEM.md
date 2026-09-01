# PHI FIRE DRONE — CONTROL SYSTEM

## Avionics and Autonomy

---

## FLIGHT MODES

| Mode | Description | Speed |
|------|-------------|-------|
| PATROL | Grid search | 25 km/h |
| INVESTIGATE | Slow approach | 10 km/h |
| SUPPRESS | Hover and spray | 0 km/h |
| RTH | Return home | 25 km/h |
| LAND | Auto-land | Descending |

---

## FIRE FIGHTING AUTONOMY

```
FIRE SUPPRESSION MISSION:
═══════════════════════════════════════════════════════════════

  1. Thermal anomaly detected
  2. Approach carefully (INVESTIGATE mode)
  3. Confirm fire (thermal > 100°C + visual)
  4. Alert fire department (automatic)
  5. Assess fire size via thermal mapping
  6. If < 1m²:
     a. Position above fire edge
     b. Activate retardant pump
     c. Apply in sweeping pattern
     d. Monitor for re-ignition
  7. If > 1m²:
     a. Maintain 50m distance
     b. Monitor fire spread
     c. Report to fire department
  8. Return to base when done
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| Flame detection | Temp > 200°C | Maintain distance |
| Smoke detected | MQ-2 trigger | Investigate |
| Battery < 30% | Low voltage | Abort, RTH |
| Retardant empty | Level < 10% | Return to base |
| Wind > 30 km/h | High wind | Abort mission |
