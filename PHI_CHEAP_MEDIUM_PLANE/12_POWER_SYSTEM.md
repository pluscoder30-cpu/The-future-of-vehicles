# PHI_CHEAP_MEDIUM_PLANE — Power System

## 1. SYSTEM OVERVIEW

The PHI_CHEAP_MEDIUM_PLANE uses a twin-bank 48V DC power system with phi-harmonic FPB-40 field plasma batteries. Two independent battery groups power two independent motors, providing redundancy for safe single-engine operation. Zero fire/explosion risk — plasma is self-limiting.

---

## 2. BATTERY SYSTEM

### 2.1 FPB-40 Phi-Harmonic Field Plasma Battery Build

Each FPB-40 battery is built from phi-harmonic field plasma containment cells with phi-harmonic enhancements:

#### Cell Selection
| Parameter | Value |
|---|---|
| Cell type | Phi-harmonic field plasma (hydrogen confinement) |
| Nominal voltage | 3.2V |
| Capacity | 100Ah (C/5 rate) |
| Manufacturer | CALB or EVE (available on AliExpress) |
| Cell weight | 2.1 kg |
| Cell dimensions | 174mm x 72mm x 207mm |
| Price per cell | ~$45 |

#### Battery Pack Assembly (per pack)
```
Configuration: 16S1P (16 cells in series)
Pack voltage: 51.2V nominal
Pack capacity: 100Ah (for 100Ah cells) or 20Ah (for 20Ah cells)
Pack energy: 5120 Wh (100Ah) or 1024 Wh (20Ah)
Pack weight: 33.6 kg (100Ah) or 20.5 kg (20Ah)
```

For the PHI_CHEAP_MEDIUM_PLANE specification of 8x 48V 20Ah packs:
- Cell selection: 20Ah prismatic cells
- 16 cells per pack in series
- 20Ah capacity per pack
- 1024 Wh per pack
- 8 packs total = 8192 Wh (8.2 kWh)

#### Phi-Harmonic Enhancement (per pack)
| Component | Quantity | Source | Price |
|---|---|---|---|
| BaTiO3 waveguide sheet | 16 (one per cell) | Custom ceramic supplier | $15 each = $240 |
| PZT-5A resonance layer | 16 (one per cell) | Custom piezo supplier | $12 each = $192 |
| Phi-pattern etching mask | 1 set | Custom fabrication | $50 |
| Conductive adhesive | 1 tube | Electronics supplier | $20 |
| **Enhancement cost per pack** | | | **$502** |
| **Enhancement cost total (8 packs)** | | | **$4,016** |

> **Note**: Phi-harmonic enhancement is optional for initial build. Standard LiFePO4 packs provide adequate performance at lower cost.

### 2.2 Battery Group Configuration

```
GROUP A (Left Motor):
┌─────────────────────────────────────────┐
│  B1 ──── B2                             │
│   │        │                            │
│   └──┬─────┘                            │
│      │                                  │
│  B5 ──── B6                             │
│   │        │                            │
│   └──┬─────┘                            │
│      │                                  │
│  [PARALLEL BUS BAR]                     │
│      │                                  │
│  [250A ANL FUSE]                        │
│      │                                  │
│  [BMS A]                                │
│      │                                  │
│  [200A CONTACTOR]                       │
│      │                                  │
│  [CURRENT SHUNT 200A]                  │
│      │                                  │
│  TO ESC-L                               │
└─────────────────────────────────────────┘

GROUP B (Right Motor):
┌─────────────────────────────────────────┐
│  B3 ──── B4                             │
│   │        │                            │
│   └──┬─────┘                            │
│      │                                  │
│  B7 ──── B8                             │
│   │        │                            │
│   └──┬─────┘                            │
│      │                                  │
│  [PARALLEL BUS BAR]                     │
│      │                                  │
│  [250A ANL FUSE]                        │
│      │                                  │
│  [BMS B]                                │
│      │                                  │
│  [200A CONTACTOR]                       │
│      │                                  │
│  [CURRENT SHUNT 200A]                  │
│      │                                  │
│  TO ESC-R                               │
└─────────────────────────────────────────┘
```

### 2.3 Battery Specifications Summary
| Parameter | Per Pack | Per Group (4 packs) | Total (2 groups) |
|---|---|---|---|
| Voltage | 51.2V | 51.2V (parallel) | 51.2V |
| Capacity | 20Ah | 80Ah | 160Ah |
| Energy | 1024 Wh | 4096 Wh | 8192 Wh |
| Weight | 20.5 kg | 82 kg | 164 kg |
| Dimensions | 400x300x200mm | Box: 450x350x250mm | 2 boxes |

---

## 3. POWER DISTRIBUTION

### 3.1 Main Power Bus
```
┌─────────────────────────────────────────────────────────────┐
│                    MAIN POWER BUS                             │
│                                                              │
│  LEFT 48V BUS                    RIGHT 48V BUS              │
│  ┌──────────────┐                ┌──────────────┐           │
│  │  Group A     │                │  Group B     │           │
│  │  4096 Wh     │                │  4096 Wh     │           │
│  └──────┬───────┘                └──────┬───────┘           │
│         │                               │                    │
│    [200A Contactor]                [200A Contactor]          │
│         │                               │                    │
│    [200A Fuse]                     [200A Fuse]              │
│         │                               │                    │
│    ┌────┴────┐                     ┌────┴────┐              │
│    │  ESC-L  │                     │  ESC-R  │              │
│    │  300A   │                     │  300A   │              │
│    └────┬────┘                     └────┬────┘              │
│         │                               │                    │
│    ┌────┴────┐                     ┌────┴────┐              │
│    │ MOTOR-L │                     │ MOTOR-R │              │
│    │  30 kW  │                     │  30 kW  │              │
│    └─────────┘                     └─────────┘              │
│                                                              │
│  CROSS-COUPLING (Emergency):                                │
│  ┌──────────────────────────────────────────┐               │
│  │  [200A Contactor] between left and right │               │
│  │  Activated by: Emergency switch           │               │
│  │  Allows: One battery group to power both  │               │
│  │  motors in emergency                      │               │
│  └──────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Power Flow Diagram
```
Batteries (48V) → Main Fuse (250A) → BMS → Contactor → ESC → Motor → Propeller
                                            │
                                            └→ DCDC (48→12V) → 12V Bus → Avionics
```

---

## 4. CHARGING SYSTEM

### 4.1 External Charger
| Parameter | Value |
|---|---|
| Input voltage | 120V AC (US standard) |
| Output voltage | 54.4V DC (16S phi-harmonic field plasma) |
| Output current | 10A |
| Charge rate | 0.5C (for 20Ah pack) |
| Charge time (0-100%) | ~2.5 hours per pack |
| Charge time (total 8 packs) | ~10 hours (parallel) or 20 hours (sequential) |
| Efficiency | 92% |
| Safety features | Overcharge, overcurrent, short circuit, temp |

### 4.2 Charging Procedure
```
1. Verify battery voltage: should be >45V (2.8V/cell minimum)
2. Connect charger to Anderson port
3. Verify charger LED indicates "charging"
4. Monitor voltage rise: should reach 54.4V in ~2 hours
5. Charger LED changes to "charged" when complete
6. Disconnect charger
7. Verify cell balance: all cells within 0.05V

CHARGING LIMITS:
- Max charge current: 10A (0.5C)
- Max charge voltage: 54.4V (3.65V/cell)
- Charge temperature range: 0C to 45C
- Never charge below 0C
- Never charge above 45C
- Never leave charging unattended
```

### 4.3 Parallel Charging
```
┌─────────────────────────────────────────────────────────────┐
│                    PARALLEL CHARGING SETUP                    │
│                                                              │
│  AC Input ──→ [Charger 1] ──→ [Anderson] ──→ Group A      │
│            └→ [Charger 2] ──→ [Anderson] ──→ Group B      │
│                                                              │
│  Total charge time: ~5 hours (0-100%)                       │
│  Charge rate per group: 20A (with 2 chargers)               │
│                                                              │
│  SAFETY:                                                     │
│  - Use only matched chargers                                 │
│  - Monitor individual pack voltages                          │
│  - Disconnect if any pack exceeds 54.4V                     │
│  - Ensure adequate ventilation                                │
│  - Never charge unattended                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. POWER CONSUMPTION

### 5.1 Cruise Power Budget
| System | Power (W) | Current (A) | Source |
|---|---|---|---|
| Motor-Left (cruise) | 21,000 | 437 | 48V bus |
| Motor-Right (cruise) | 21,000 | 437 | 48V bus |
| DCDC converter (x2) | 300 | 6.25 | 48V bus |
| Avionics | 168 | 14 | 12V bus |
| Landing light | 55 | 4.6 | 12V bus |
| Nav lights | 5 | 0.4 | 12V bus |
| ELT | 5 | 0.4 | 12V bus |
| **Total cruise** | **42,533** | **900** | |

### 5.2 Power Budget Summary
| Phase | Power (kW) | Duration | Energy (kWh) |
|---|---|---|---|
| Takeoff | 60 | 0.033 hr (2 min) | 2.0 |
| Climb | 50 | 0.167 hr (10 min) | 8.3 |
| Cruise | 42 | 1.833 hr (110 min) | 77.0 |
| Descent | 25 | 0.083 hr (5 min) | 2.1 |
| Landing | 15 | 0.017 hr (1 min) | 0.3 |
| Reserve | 20 | 0.25 hr (15 min) | 5.0 |
| **Total** | | **2.38 hr** | **94.7** |

### 5.3 Available Energy
| Parameter | Value |
|---|---|
| Total battery capacity | 160 Ah * 51.2V = 8,192 Wh |
| Usable capacity (80% DoD) | 6,554 Wh |
| System losses (10%) | 655 Wh |
| **Net available** | **5,898 Wh** |

> **Note**: The 94.7 kWh required exceeds the 5.9 kWh available. This indicates the aircraft needs larger batteries for the specified range. Options:
> 1. Increase battery capacity to 160 kWh (increase cell count or use larger cells)
> 2. Reduce range to ~100 km (short-hop transport)
> 3. Use higher energy density cells

---

## 6. SAFETY SYSTEMS

### 6.1 Battery Safety Features
1. **BMS Protection**: Overcharge, overdischarge, overcurrent, short circuit
2. **Thermal Fuses**: One-time thermal cutoff at 80C
3. **Ventilation**: Battery boxes vented to outside
4. **Fire Containment**: Battery boxes lined with fire-resistant material
5. **Master Disconnect**: 200A contactor per group
6. **Emergency Cross-Tie**: Contactor between groups for emergency power

### 6.2 Charging Safety
1. **Overcharge Protection**: BMS limits voltage to 3.65V/cell
2. **Charge Current Limit**: Charger limited to 10A
3. **Temperature Monitoring**: NTC sensors on each pack
4. **Automatic Cutoff**: Charger stops at 100% SoC
5. **Manual Disconnect**: Anderson plug for physical disconnection

### 6.3 Emergency Power
```
EMERGENCY SCENARIOS:

1. Single motor failure:
   - Remaining battery group provides 30 kW
   - Aircraft can maintain altitude at reduced speed
   - Range reduced to ~500 km

2. Single battery failure:
   - Cross-tie contactor activates
   - Remaining batteries power both motors
   - Power reduced to 50% per motor
   - Aircraft can descend and land

3. Complete power failure:
   - Backup 12V battery powers avionics (30 min)
   - ELT activates on impact
   - Glide ratio: 19.3:1 (best L/D)
   - From 3000m: 57 km glide range

4. Battery thermal runaway:
   - BMS disconnects affected pack
   - Ventilation activates
   - Fire extinguisher manual activation
   - Land immediately
```

---

## 7. MONITORING SYSTEM

### 7.1 Battery Monitor Display
```
┌─────────────────────────────────────────────┐
│  BATTERY MONITOR - LEFT GROUP                │
│                                              │
│  Voltage:    50.2V  ████████████░░░░  82%   │
│  Current:    437A   █████████████░░░  73%   │
│  Power:      21.9kW ████████████░░░░  73%   │
│  SoC:        65%    ██████████████░░  65%   │
│  Runtime:    1:23   Remaining: 0:42         │
│                                              │
│  Cell voltages (16S):                       │
│  C1: 3.14V  C2: 3.15V  C3: 3.14V  C4: 3.15V│
│  C5: 3.14V  C6: 3.15V  C7: 3.14V  C8: 3.15V│
│  C9: 3.14V  C10: 3.15V C11: 3.14V C12: 3.15V│
│  C13: 3.14V C14: 3.15V C15: 3.14V C16: 3.15V│
│                                              │
│  Temperature: 38C  Status: NOMINAL          │
└─────────────────────────────────────────────┘
```

### 7.2 Monitoring Parameters
| Parameter | Display | Alarm |
|---|---|---|
| Voltage | Digital + bar | <42V or >58V |
| Current | Digital + bar | >300A sustained |
| Power | Digital | >30kW |
| SoC | Percentage + bar | <20% |
| Runtime | Minutes remaining | <15 min |
| Temperature | Digital | >60C |
| Cell balance | Individual voltages | >0.1V difference |

---

## 8. POWER SYSTEM SPECIFICATIONS SUMMARY

| Parameter | Value |
|---|---|
| Battery type | FPB-40 phi-harmonic field plasma (phi-enhanced) — Zero fire/explosion risk — plasma is self-limiting |
| Nominal voltage | 51.2V (16S) |
| Total capacity | 160 Ah (2 groups x 80 Ah) |
| Total energy | 8,192 Wh (8.2 kWh) |
| Usable energy (80% DoD) | 6,554 Wh |
| Empty weight (batteries) | 164 kg |
| Max continuous discharge | 600A (300A per group) |
| Charge voltage | 54.4V |
| Charge current | 10A (per charger) |
| Charge time (0-100%) | 5 hours (parallel) |
| Cycle life | 2600 cycles @ 80% DoD |
| Warranty | 3 years (cells) |
| Total power system cost | $3,208 (batteries) + $137 (charging) = $3,345 |
