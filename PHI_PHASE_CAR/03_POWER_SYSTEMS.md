# PHI PHASE CAR — Power Distribution

## Power Architecture
```
FPB-20 Battery (144V, 20kWh)
    |
    +-- Phase Containment Bus (144V, 8kW peak)
    |   +-- Front Phase Array (2 kW, 4 coils)
    |   +-- Side Phase Arrays (2 kW each, 4 coils)
    |   +-- Rear Phase Array (2 kW, 4 coils)
    |   +-- Containment Synchronizer (1 kW)
    |
    +-- Drive Bus (144V -> 72V, 6kW continuous)
    |   +-- Front-Left Hub Motor (1.5 kW)
    |   +-- Front-Right Hub Motor (1.5 kW)
    |   +-- Rear-Left Hub Motor (1.5 kW)
    |   +-- Rear-Right Hub Motor (1.5 kW)
    |   +-- Regenerative Recovery (1.2 kW)
    |
    +-- Auxiliary Bus (144V -> 12V/5V, 2kW)
    |   +-- AI Computer (500W)
    |   +-- HVAC System (800W)
    |   +-- Entertainment (200W)
    |   +-- Lighting (200W)
    |   +-- Sensors (300W)
    |
    +-- Emergency Reserve (144V, 1kW for 30 min)
```

## Phase Containment Power Management
The 12 phase coils require precise power sequencing:
1. **Pre-transit charging** (3 seconds): All coils charged to 95%
2. **Phase window** (50 milliseconds): Full 8 kW burst
3. **Recovery** (80 milliseconds): Coils recharged for next window
4. **Repetition:** 25 phase windows per second during transit
5. **Synchronization:** All 12 coils within 5 nanoseconds

## Power Management Unit (PMU)
- **Topology:** Quad-redundant DC-DC converters
- **Efficiency:** 98.5% peak
- **Monitoring:** Per-rail current/voltage/temperature sensing
- **Protection:** Overcurrent, overvoltage, overtemperature, short-circuit
- **Phase Priority:** Phase containment always gets first power allocation
- **Load Balancing:** Dynamic power allocation across 4 drive motors

## Thermal Management
- Liquid cooling loop for phase coils (glycol-water mix)
- Separate cooling loop for drive motors
- Heat exchangers integrated into body panels
- Maximum coolant temp: 65C
- Thermal cutoff at 90C triggers load shedding

## Emergency Power Protocol
1. Primary FPB-20 failure detected
2. Emergency reserve engaged (1kW, 30 minutes)
3. Phase coils locked out (no phase shifting possible)
4. Drive motors reduced to 40% power
5. HVAC reduced to 30% power
6. System navigates to nearest safe stopping point
