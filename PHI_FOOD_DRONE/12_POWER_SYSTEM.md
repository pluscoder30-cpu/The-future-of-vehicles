# PHI FOOD DRONE — POWER SYSTEM

## FPB-5 Battery and Power Distribution

---

## FPB-5 SPECIFICATIONS

| Parameter | Value |
|-----------|-------|
| Voltage | 12.0V |
| Capacity | 50Ah (600Wh) |
| Weight | 850g |
| Max Discharge | 30A |
| Charge Time | 3 hours |
| Cycle Life | 2000+ |

---

## POWER DISTRIBUTION

```
POWER FLOW:
═══════════════════════════════════════════════════════════════

  FPB-5 (12V) → 30A Fuse → Main Switch
    ├──→ ESC1-4 → Motors (12V)
    ├──→ 5V Buck → Arduino, servos, sensors
    ├──→ 12V → Nutrient pump (via relay)
    └──→ 3.3V Buck → ESP8266, GPS
```

---

## POWER CONSUMPTION

| Mode | Power | Flight Time |
|------|-------|-------------|
| Hover (no payload) | 100W | 4.0 hours |
| Hover (800g payload) | 130W | 3.5 hours |
| Planting mode | 155W | 3.0 hours |
| Standby | 0.5W | 50+ days |

---

## BATTERY STATUS

| Voltage | SoC | Action |
|---------|-----|--------|
| 14.4V | 100% | Full |
| 13.6V | 80% | Good |
| 12.8V | 60% | Fair |
| 12.0V | 40% | Return to base |
| 11.2V | 20% | Land immediately |
| 10.8V | 10% | Emergency land |
