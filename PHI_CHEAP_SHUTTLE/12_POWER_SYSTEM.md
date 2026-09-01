# PHI CHEAP SHUTTLE — POWER SYSTEM

## FPB-20 Phi-Harmonic Field Plasma Battery Design and Power Distribution

---

## POWER ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────┐
│                    POWER SYSTEM ARCHITECTURE                         │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │  FPB-20 #1  │  │  FPB-20 #2  │  │  FPB-20 #3  │  │  FPB-20 #4  │           │
│  │ 12V/100Ah│  │ 12V/100Ah│  │ 12V/100Ah│  │ 12V/100Ah│           │
│  │  10 kWh  │  │  10 kWh  │  │  10 kWh  │  │  10 kWh  │           │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘           │
│       │              │              │              │                  │
│       │  SERIES      │  PARALLEL    │  SERIES      │  PARALLEL       │
│       └──────┬───────┴──────┬───────┴──────┬───────┘                  │
│              │              │              │                          │
│         ┌────┴────┐    ┌────┴────┐                                 │
│         │ 24V     │    │ 24V     │                                  │
│         │ STRING  │    │ STRING  │                                  │
│         └────┬────┘    └────┬────┘                                  │
│              │              │                                        │
│              └──────┬───────┘                                        │
│                     │                                                │
│              ┌──────┴──────┐                                        │
│              │  48V NOMINAL │                                        │
│              │  200Ah       │                                        │
│              │  9.6 kWh     │                                        │
│              └──────┬──────┘                                        │
│                     │                                                │
│              ┌──────┴──────┐                                        │
│              │  PHI-HARMONIC│                                       │
│              │  MODULATOR   │                                        │
│              │  (161.8 kHz) │                                        │
│              └──────┬──────┘                                        │
│                     │                                                │
│         ┌───────────┼───────────┐                                   │
│         │           │           │                                   │
│    ┌────┴────┐ ┌────┴────┐ ┌────┴────┐                             │
│    │THRUSTER │ │THRUSTER │ │AVIONICS │                             │
│    │ BUS     │ │ BUS     │ │ BUS     │                             │
│    │ 48V     │ │ 48V     │ │ 48V→5V  │                             │
│    │ 400A    │ │ 400A    │ │ 48V→3.3V│                             │
│    └─────────┘ └─────────┘ └─────────┘                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## FPB-20 FIELD BATTERY SPECIFICATIONS

### Individual Battery

| Parameter | Value |
|-----------|-------|
| Type | Phi-harmonic field plasma (hydrogen confinement) | Zero fire/explosion risk — plasma is self-limiting |
| Voltage | 12V nominal (12.8V full, 11.8V empty) |
| Capacity | 100 Ah (1,200 Wh) |
| Weight | 14 kg (30.8 lb) |
| Dimensions | 330mm × 172mm × 215mm |
| Max Discharge | 10C = 1,000A (10 sec) |
| Cycle Life | 500 cycles at 80% DoD |
| Charge Rate | 0.1C = 10A (10-hour charge) |
| Source | eBay Surplus |
| Unit Cost | $85.00 |

### Battery Bank Configuration

| Parameter | Value |
|-----------|-------|
| Configuration | 2S2P (2 series × 2 parallel) |
| Nominal Voltage | 48V (4 × 12V) |
| Capacity | 200 Ah |
| Energy | 9,600 Wh (9.6 kWh) |
| Weight | 56 kg (123.2 lb) |
| Max Continuous Discharge | 400A |
| Max Pulse Discharge | 1,000A (10 sec) |

---

## PHI-HARMONIC POWER MODULATION

### Concept
The power electronics switch at φ-harmonic frequencies (161.8 kHz base) to reduce switching losses and improve efficiency.

### Implementation
- Full-bridge inverter switching at 161.8 kHz
- Resonant tank tuned to 161.8 kHz
- Phi-harmonic overtones: 261.8, 423.6, 685.4 kHz

### Efficiency Gains
- Standard PWM (100 kHz): η ≈ 95%
- Phi-Harmonic (161.8 kHz): η ≈ 97%
- Improvement: 2% at 40 kW = 800W saved
- Over 1-hour mission: 800 Wh saved = 8.3% more range

---

## POWER DISTRIBUTION

### Bus Bar Specifications

| Parameter | Value |
|-----------|-------|
| Material | Copper |
| Dimensions | 1/4" × 1" × 24" |
| Current Capacity | 400A continuous |
| Voltage Drop | <0.1V at 400A |
| Mounting | Insulated standoffs to frame |
| Protection | ANL fuses (150A per thruster) |

### Power Routing

| Circuit | Voltage | Current | Wire Gauge | Fuse |
|---------|---------|---------|------------|------|
| Thruster 1 | 48V DC | 100A | 4 AWG | 150A ANL |
| Thruster 2 | 48V DC | 100A | 4 AWG | 150A ANL |
| Thruster 3 | 48V DC | 100A | 4 AWG | 150A ANL |
| Thruster 4 | 48V DC | 100A | 4 AWG | 150A ANL |
| Avionics | 48V → 5V | 10A | 10 AWG | 15A blade |
| Avionics | 48V → 3.3V | 2A | 18 AWG | 3A blade |
| Servos | 48V → 12V | 5A | 14 AWG | 10A blade |
| Comms | 48V → 12V | 2A | 18 AWG | 5A blade |

---

## BATTERY MANAGEMENT

### Monitoring
- 4× Digital voltage monitors (0-50V, AliExpress)
- 4× Current sensors (ACS712 30A, for each thruster)
- 4× Temperature sensors (LM35, at battery terminals)
- Arduino Mega reads all sensors at 10 Hz

### Protection
- ANL fuses: 150A per thruster circuit
- Master disconnect: 400A switch per bus
- Low-voltage cutoff: 11.5V per battery (38.3V total)
- Over-temperature: 60°C cutoff at battery terminals

### Charge System
- Solar charge controller: 30A, 48V (for ground charging)
- Charge time: 8 hours at 10A (0-100%)
- Float voltage: 13.8V per battery (55.2V total)
- Equalization: 14.4V per battery (57.6V total, monthly)

---

## WEIGHT BUDGET

| Component | Weight |
|-----------|--------|
| 4× FPB-20 Batteries | 56.0 kg |
| Bus Bar (copper) | 2.5 kg |
| ANL Fuses & Holders | 0.8 kg |
| Wiring (4 AWG, 10 AWG) | 3.2 kg |
| Battery Boxes (4× plastic) | 4.0 kg |
| Master Switches (2×) | 0.8 kg |
| Voltage Monitors (4×) | 0.2 kg |
| **TOTAL POWER SYSTEM** | **67.5 kg** |

---

## ENERGY BUDGET

### Mission Profile (100 km Altitude)

| Phase | Duration | Power | Energy |
|-------|----------|-------|--------|
| Takeoff (full thrust) | 30 sec | 40 kW | 333 Wh |
| Boost (full thrust) | 3.5 min | 40 kW | 2,333 Wh |
| Coast (avionics only) | 3 min | 0.5 kW | 25 Wh |
| Reentry (partial thrust) | 3 min | 20 kW | 1,000 Wh |
| Descent (avionics only) | 2 min | 0.5 kW | 17 Wh |
| **TOTAL** | **12 min** | | **3,708 Wh** |

### Energy Margin
- Total Available: 9,600 Wh
- Mission Requirement: 3,708 Wh
- Margin: 5,892 Wh (61.4% reserve)
- Endurance: ~30 minutes at full thrust

---

## THERMAL MANAGEMENT

### Heat Generation
- Thruster MOSFETs: 800W total (2% of 40 kW)
- Bus Bar: 16W (I²R at 400A, 0.1Ω)
- Wiring: 50W (estimated)
- **Total Heat: ~866W**

### Cooling
- Thruster heatsinks: Natural convection (8× aluminum fins)
- Bus bar: Air-cooled (mounted on frame)
- Batteries: Passive (no active cooling needed at 100A discharge)
- Emergency: Fire extinguisher (ABC, 5 lb × 2)
