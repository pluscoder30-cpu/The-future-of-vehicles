# PHI BIO SKIN WATCH — Power Distribution

## Power Architecture
```
FPB-5 Micro Battery (3.7V, 5kWh)
    |
    +-- Bio-Skin Bus (3.7V, 5 mW)
    |   +-- Surface Emitters (3 mW)
    |   +-- Self-Cleaning Field (1 mW)
    |   +-- Self-Healing Field (1 mW)
    |
    +-- Sensor Bus (3.7V -> 1.8V, 2 mW)
    |   +-- Heart Rate (0.3 mW)
    |   +-- SpO2 (0.3 mW)
    |   +-- Temperature (0.1 mW)
    |   +-- Accelerometer (0.1 mW)
    |   +-- Gyroscope (0.1 mW)
    |
    +-- Processing Bus (3.7V -> 1.2V, 2 mW)
    |   +-- Timekeeping (0.5 mW)
    |   +-- Health AI (0.5 mW)
    |   +-- Display Controller (0.5 mW)
    |   +-- Communication (0.5 mW)
    |
    +-- Display Bus (3.7V, 2 mW on-demand)
        +-- AMOLED Display (1.5 mW)
        +-- Haptic Motor (0.5 mW)
```

## Power Management Unit (PMU)
- **Topology:** Ultra-low-power DC-DC converters
- **Efficiency:** 92% peak
- **Monitoring:** Per-rail current sensing
- **Power Saving:** Aggressive duty cycling
- **Sleep Current:** <10 uA (timekeeping only)

## Battery Life
| Mode | Power | Runtime |
|------|-------|---------|
| Sleep (time only) | 10 uW | 365 days |
| Active (sensors) | 15 uW | 180 days |
| Full features | 25 uW | 90 days |
| Always-on display | 100 uW | 30 days |
| Emergency beacon | 5 mW | 30 days |

## Emergency Power Protocol
1. Primary battery <5% detected
2. Display dims to minimum
3. Sensors reduce to hourly sampling
4. Timekeeping continues
5. 30 days of emergency power reserved
