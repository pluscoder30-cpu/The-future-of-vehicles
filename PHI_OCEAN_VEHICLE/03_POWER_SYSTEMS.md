# PHI OCEAN VEHICLE — Power Distribution

## Power Architecture
```
FPB-20 Battery (144V, 20kWh)
    |
    +-- Drag Reduction Bus (144V, 3kW continuous)
    |   +-- Port Field Array (750W)
    |   +-- Starboard Field Array (750W)
    |   +-- Bow Field Array (750W)
    |   +-- Stern Field Array (750W)
    |   +-- Field Synchronizer (500W)
    |
    +-- Propulsion Bus (144V, 2kW continuous)
    |   +-- Forward Thrusters (1 kW)
    |   +-- Lateral Thrusters (500W)
    |   +-- Depth Control (500W)
    |
    +-- Auxiliary Bus (144V -> 12V/5V, 2kW)
    |   +-- Navigation Computer (300W)
    |   +-- Life Support (500W)
    |   +-- Climate Control (500W)
    |   +-- Lighting (300W)
    |   +-- Entertainment (400W)
    |
    +-- Emergency Reserve (144V, 500W for 8 hours)
```

## Drag Reduction Power Management
The 4 drag reduction arrays require continuous power:
1. **Activation** (10 seconds): Arrays power up, field forms
2. **Steady State:** 3 kW continuous for zero-drag cruising
3. **High Speed:** 5 kW for speeds >40 km/h
4. **Emergency:** 8 kW for emergency maneuvering (60 seconds)

## Power Management Unit (PMU)
- **Topology:** Dual-redundant DC-DC converters (marine-rated)
- **Efficiency:** 98% peak
- **Monitoring:** Per-rail current/voltage/temperature/salinity sensing
- **Protection:** Overcurrent, overvoltage, overtemperature, saltwater intrusion
- **Field Priority:** Drag reduction always gets first power allocation

## Thermal Management
- Glycol cooling loop for battery and electronics
- Seawater heat exchanger (free cooling at sea)
- Waste heat used for cabin heating
- Maximum coolant temp: 65C

## Emergency Power Protocol
1. Primary FPB-20 failure detected
2. Emergency reserve engaged (500W, 8 hours life support)
3. Drag reduction deactivated (normal drag returns)
4. Field propulsion reduced to 30%
5. Vehicle drifts to nearest coast or rescue point
