# PHI SUBMERSIBLE — Power Distribution

## Power Architecture
```
FPB-20 Battery (144V, 20kWh)
    |
    +-- Field Skimmer Bus (144V, 5kW continuous)
    |   +-- Port Field Array (1.25 kW)
    |   +-- Starboard Field Array (1.25 kW)
    |   +-- Bow Field Array (1.25 kW)
    |   +-- Stern Field Array (1.25 kW)
    |
    +-- Hull Integrity Bus (144V, 2kW)
    |   +-- Pressure Compensation (1 kW)
    |   +-- Seal Monitoring (500W)
    |   +-- Emergency Ballast (500W)
    |
    +-- Auxiliary Bus (144V -> 12V/5V, 2kW)
    |   +-- Life Support (1 kW)
    |   +-- Control Computer (300W)
    |   +-- Lighting (300W)
    |   +-- Cameras/Sensors (400W)
    |
    +-- Emergency Reserve (144V, 1kW for 2 hours)
```

## Field Skimmer Power Management
The 4 field arrays require precise power sequencing:
1. **Activation** (5 seconds): Arrays power up, field forms
2. **Steady State:** 5 kW continuous for drag reduction
3. **Burst Mode:** 10 kW for rapid acceleration
4. **Emergency:** 15 kW for emergency ascent (30 seconds)

## Power Management Unit (PMU)
- **Topology:** Dual-redundant DC-DC converters (pressure-sealed)
- **Efficiency:** 98% peak
- **Monitoring:** Per-rail current/voltage/temperature/pressure sensing
- **Protection:** Overcurrent, overvoltage, overtemperature, implosion detection
- **Field Priority:** Skimmer always gets first power allocation

## Thermal Management
- Glycol cooling loop for battery and electronics
- Heat exchanger integrated into hull
- Waste heat used for cabin heating at depth
- Maximum coolant temp: 65C
- Thermal cutoff at 85C triggers load shedding

## Emergency Power Protocol
1. Primary FPB-20 failure detected
2. Emergency reserve engaged (1kW, 2 hours life support only)
3. Field skimmer deactivated (drag returns to normal)
4. Emergency ballast release for positive buoyancy
5. Vehicle ascends to surface at 3 m/s
