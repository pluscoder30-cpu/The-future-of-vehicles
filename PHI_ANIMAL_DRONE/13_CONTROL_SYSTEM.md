# PHI ANIMAL DRONE — CONTROL SYSTEM

## Avionics and Autonomy

---

## FLIGHT MODES

| Mode | Description | Speed |
|------|-------------|-------|
| SILENT | Whisper-quiet hover | 0 km/h |
| OBSERVE | Slow approach | 5 km/h |
| FEED | Hover and dispense | 0 km/h |
| CALM | Hover and emit freq | 0 km/h |
| RTH | Return home | 15 km/h |
| LAND | Auto-land | Descending |

---

## WILDLIFE AUTONOMY

```
ANIMAL OBSERVATION MISSION:
═══════════════════════════════════════════════════════════════

  1. Navigate to observation area
  2. Switch to SILENT mode
  3. Hover at 10m altitude
  4. Scan with thermal camera
  5. If animal detected:
     a. Approach to 5m distance
     b. Record video and thermal
     c. Monitor behavior
     d. If animal stressed: activate CALM mode
     e. If animal calm: continue observation
  6. If food needed: activate FEED mode
  7. Log all observations
  8. Return to base
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| Animal detection | Thermal signature | Alert operator |
| Dangerous animal | Size/pattern match | Auto RTH |
| Battery < 20% | Low voltage | Auto RTH |
| Signal loss | 30 sec | Auto land |
