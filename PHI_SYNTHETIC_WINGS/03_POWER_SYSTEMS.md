# PHI SYNTHETIC WINGS — Power Distribution

## Power Architecture
```
FPB-5 Battery (48V, 5kWh)
    |
    +-- Lift Field Bus (48V, 1kW continuous)
    |   +-- Left Wing Field Emitters (400W)
    |   +-- Right Wing Field Emitters (400W)
    |   +-- Field Synchronizer (200W)
    |
    +-- Actuation Bus (48V -> 24V, 300W)
    |   +-- Left Wing Servos (150W)
    |   +-- Right Wing Servos (150W)
    |
    +-- Control Bus (48V -> 5V/3.3V, 200W)
    |   +-- Flight Computer (50W)
    |   +-- Sensors (50W)
    |   +-- Communications (50W)
    |   +-- Safety Systems (50W)
    |
    +-- Emergency Reserve (48V, 100W for 30 min)
```

## Lift Field Power Management
The phi-harmonic lift field requires precise power sequencing:
1. **Activation** (2 seconds): Field forms around wings
2. **Steady State:** 1 kW continuous for hover
3. **Ascent:** 2 kW for climbing
4. **Descent:** 500W for controlled descent
5. **Emergency:** 3 kW burst for 30 seconds

## Power Management Unit (PMU)
- **Topology:** Dual-redundant DC-DC converters
- **Efficiency:** 97% peak
- **Monitoring:** Per-rail current/voltage/temperature
- **Protection:** Overcurrent, overvoltage, overtemperature
- **Lift Priority:** Lift field always gets first power allocation

## Emergency Power Protocol
1. Primary FPB-5 failure detected
2. Emergency reserve engaged (100W, 30 minutes)
3. Lift field reduced to 50% (controlled descent)
4. Wing flapping stops (glide mode)
5. System descends at 3 m/s
6. Parachute deploys if descent exceeds 5 m/s
