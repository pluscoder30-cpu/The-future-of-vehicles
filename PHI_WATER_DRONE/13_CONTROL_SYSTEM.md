# PHI WATER DRONE — CONTROL SYSTEM

## Avionics and Autonomy

---

## FLIGHT MODES

| Mode | Description | Speed |
|------|-------------|-------|
| CLEAN | Hover and filter | 0 km/h |
| PATROL | Grid search | 15 km/h |
| RTH | Return home | 20 km/h |
| LAND | Auto-land | Descending |

---

## CLEANING AUTONOMY

```
AUTO-CLEANING MISSION:
═══════════════════════════════════════════════════════════════

  1. Navigate to water body
  2. Test initial water quality
  3. Descend to 2m above water
  4. Lower intake filter
  5. Activate filtration
  6. Apply cleaning frequencies
  7. Monitor water quality improvement
  8. Move to next area
  9. Repeat until area clean
  10. Return to base
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| Water detected | Below 5m | Reduce speed |
| Battery < 30% | Low voltage | Return to base |
| Filter clogged | High pressure | Alert, reduce flow |
| pH extreme | < 5 or > 10 | Alert operator |
