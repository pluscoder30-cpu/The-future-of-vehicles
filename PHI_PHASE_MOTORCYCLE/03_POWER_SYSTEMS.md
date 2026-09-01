# PHI PHASE MOTORCYCLE — Power Distribution

## Power Architecture
```
FPB-10 Battery (96V, 10kWh)
    |
    +-- Phase Coil Bus (96V, 5kW peak)
    |   +-- Front Phase Array (2.5 kW)
    |   +-- Rear Phase Array (2.5 kW)
    |   +-- Phase Synchronization Unit (500W)
    |
    +-- Drive Bus (96V -> 72V, 3kW peak)
    |   +-- Hub Motor (2.5 kW continuous)
    |   +-- Regenerative Braking (500W recovery)
    |
    +-- Auxiliary Bus (96V -> 12V/5V, 400W)
    |   +-- Control Computer (50W)
    |   +-- Rider Heating (100W)
    |   +-- Communications (50W)
    |   +-- Lighting (100W)
    |   +-- Sensors (100W)
    |
    +-- Emergency Reserve (96V, 500W for 20 min)
```

## Phase Coil Power Management
The phase coils require precise power sequencing:
1. **Pre-shift charging** (2 seconds): Coils charged to 95% capacity
2. **Phase window** (50 milliseconds): Full 5 kW burst
3. **Recovery** (100 milliseconds): Coils recharged for next window
4. **Repetition:** 20 phase windows per second during transit

## Power Management Unit (PMU)
- **Topology:** Triple-redundant DC-DC converters
- **Efficiency:** 98% peak
- **Monitoring:** Per-rail current/voltage/temperature sensing
- **Protection:** Overcurrent, overvoltage, overtemperature, short-circuit
- **Phase Priority:** Phase coils always get first power allocation

## Thermal Management
- Liquid cooling loop for phase coils (glycol-water mix)
- Heat exchanger integrated into motorcycle fairing
- Maximum coolant temp: 65C
- Air-cooled heat sink for drive motor
- Thermal cutoff at 90C triggers load shedding

## Emergency Power Protocol
1. Primary FPB-10 failure detected
2. Emergency reserve engaged (500W, 20 minutes)
3. Phase coils locked out (no phase shifting possible)
4. Drive motor reduced to 30% power
5. System navigates to nearest safe stopping point
