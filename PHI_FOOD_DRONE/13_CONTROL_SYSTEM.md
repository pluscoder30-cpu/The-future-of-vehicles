# PHI FOOD DRONE — CONTROL SYSTEM

## Avionics and Autonomy

---

## FLIGHT MODES

| Mode | Description | Speed |
|------|-------------|-------|
| MANUAL | Pilot control | 0-35 km/h |
| STABILIZE | Auto-level | 0-25 km/h |
| GPS HOLD | Position hold | 0 km/h |
| GPS RETURN | Return home | 15 km/h |
| PLANTING | Grid pattern | 5 km/h |
| NUTRIENT | Hover and spray | 0 km/h |
| FREQUENCY | Hover and emit | 0 km/h |

---

## AUTO-PLANTING SEQUENCE

```
PLANTING MISSION:
═══════════════════════════════════════════════════════════════

  1. Receive area coordinates (WiFi)
  2. Takeoff to 10m
  3. Navigate to start point
  4. Descend to 1.5m AGL
  5. Grid pattern:
     For each point:
     a. Drop seeds (2 sec)
     b. Spray nutrients (3 sec)
     c. Apply frequency (5 sec)
     d. Move to next point
  6. Complete grid
  7. Return to base
  8. Land

  Coverage: 500m² per hour
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| GPS check | < 6 sats | Prevent takeoff |
| Battery | < 30% | Prevent takeoff |
| Seeds empty | No seeds | Disable dispenser |
| Nutrients empty | No nutrients | Disable pump |
| Geo-fence | > 500m | Auto RTH |
| Low battery | < 20% | Auto RTH |
| Signal loss | 30 sec | Auto land |

---

## COMMANDS

| Command | Description |
|---------|-------------|
| `ARM` | Arm motors |
| `TAKEOFF 10` | Takeoff to 10m |
| `PLANT lat lon w h` | Start planting |
| `NUTRIENT ON/OFF` | Control nutrient spray |
| `FREQ 417 300` | Frequency for 300 sec |
| `RTH` | Return to home |
| `LAND` | Auto land |
| `STATUS` | Get status |
