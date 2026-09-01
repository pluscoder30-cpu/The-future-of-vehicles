# PHI_HUMANOID_ROBOT — Power System

## Battery, Power Distribution & Thermal Management

---

## 1. Power System Overview

```
POWER ARCHITECTURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────┐
│                    48V BATTERY PACK                              │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                              │
│  │FPB  │ │FPB  │ │FPB  │ │FPB  │                              │
│  │-10  │ │-10  │ │-10  │ │-10  │                              │
│  │#1   │ │#2   │ │#3   │ │#4   │                              │
│  │10kWh│ │10kWh│ │10kWh│ │10kWh│                              │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘                              │
│     └───────┴───────┴───────┘                                  │
│                   │                                            │
│            48V DC Bus (100A max)                                │
└───────────────────┬─────────────────────────────────────────────┘
                    │
         ┌──────────┴──────────┐
         │   MAIN CONTACTOR    │
         │   100A, latching    │
         │   + 80A main fuse   │
         └──────────┬──────────┘
                    │
    ┌───────────────┴───────────────────────────────┐
    │              POWER DISTRIBUTION PCB            │
    │                                               │
    │  48V Bus ──┬── Buck 48V→12V #1 (10A) ──→ 12V Left  │
    │            ├── Buck 48V→12V #2 (10A) ──→ 12V Right │
    │            ├── Buck 48V→5V #1 (6A) ──→ 5V Logic   │
    │            ├── Buck 48V→5V #2 (6A) ──→ 5V Backup  │
    │            └── LDO 48V→3.3V ×4 ──→ 3.3V Sensors  │
    │                                               │
    │  INA260 ×4 (power monitoring)                  │
    │  E-stop relay ×2                               │
    │  Fuse holders ×6                               │
    └───────────────────────────────────────────────┘
```

---

## 2. Battery System

### 2.1 FPB-10 Module Specifications

```
FPB-10 BATTERY MODULE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Chemistry:          LiFePO4 (Lithium Iron Phosphate)
Nominal voltage:    48V (16S configuration, 3.2V/cell × 16 = 51.2V)
Capacity:           10 kWh per module
Energy density:     160 Wh/kg
Weight:             3.0 kg per module
Dimensions:         300mm × 200mm × 100mm (approximate)
Cycle life:         2000+ cycles to 80% capacity
Calendar life:      10+ years
Operating temp:     -20°C to 60°C (discharge), 0°C to 45°C (charge)
Charge voltage:     54.6V (3.41V/cell × 16)
Max charge current: 20A per module
Max discharge current: 50A per module

CELL CONFIGURATION:
├── 16S (16 cells in series)
├── 1P (1 cell per series string)
├── Nominal cell voltage: 3.2V
├── Charge cutoff: 3.65V/cell
└── Discharge cutoff: 2.5V/cell

INTEGRATED BMS:
├── Active cell balancing
├── Overcharge protection: 3.65V/cell
├── Overdischarge protection: 2.5V/cell
├── Overcurrent protection: 50A
├── Short circuit protection: <100µs response
├── Temperature monitoring: NTC thermistors
├── CAN bus communication: Status reporting
└── SOC estimation: Coulomb counting + voltage
```

### 2.2 Pack Configuration

```
4× FPB-10 IN PARALLEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total capacity:  40 kWh (4 × 10 kWh)
Nominal voltage: 48V (all modules in parallel)
Max discharge:   200A (4 × 50A)
Max charge:      80A (4 × 20A)
Total weight:    12 kg (4 × 3 kg)
Total volume:    24 liters (4 × 6 liters)

PARALLEL CONNECTION:
├── All modules share common 48V bus
├── Each module has independent BMS
├── BMS coordinates via CAN bus
├── Load sharing managed by BMS
└── Failed module: others continue (graceful degradation)

CHARGING:
├── Standard charge: 20A × 48V = 960W → 42 hours (0-100%)
├── Fast charge: 40A × 48V = 1920W → 21 hours
├── Rapid charge: 80A × 48V = 3840W → 10.5 hours
├── Charge time (typical): 2.5 hours at 40A
└── Charging connector: XT90 (via adapter)
```

### 2.3 Battery Monitoring

```
MONITORING POINTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INA260 #1 (Main 48V Bus):
├── Voltage: Total pack voltage (48V nominal)
├── Current: Total pack current (bidirectional)
├── Power: V × I (real-time)
├── I2C Address: 0x40
└── Update rate: 10 Hz

SOC ESTIMATION:
├── Method: Coulomb counting + OCV lookup
├── Coulomb counting: ∫I(t)dt / C_total
├── OCV lookup: Voltage → SOC table (LiFePO4 specific)
├── Combined: Weighted average (70% Coulomb, 30% OCV)
├── Accuracy: ±3% (with periodic recalibration)
├── Recalibration: At full charge (SOC = 100%)
└── Display: Percentage in app + OLED eyes

BATTERY HEALTH:
├── Cycle count: Tracked per module
├── Capacity fade: Estimated from cycle count + temperature
├── Internal resistance: Measured during charge/discharge
├── Health score: 100% (new) to 80% (end of life)
└── Warning: At 80% health, recommend replacement
```

---

## 3. Power Distribution

### 3.1 Voltage Rails

```
POWER RAIL TOPOLOGY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

48V MAIN BUS
├── 80A main fuse
├── Latching contactor (e-stop controlled)
├── INA260 monitoring
│
├── 12V LEFT LIMB BUS (Buck #1: 48V→12V, 10A)
│   ├── Left leg ODrives #1-3 (6 motors)
│   ├── Left arm ODrives #7-9 (6 motors)
│   ├── 20A blade fuse
│   └── INA260 monitoring
│
├── 12V RIGHT LIMB BUS (Buck #2: 48V→12V, 10A)
│   ├── Right leg ODrives #4-6 (6 motors)
│   ├── Right arm ODrives #10-12 (6 motors)
│   ├── 20A blade fuse
│   └── INA260 monitoring
│
├── 5V LOGIC BUS (Buck #1: 48V→5V, 6A)
│   ├── Raspberry Pi 5 (3A)
│   ├── Coral USB TPU (0.5A)
│   ├── NVMe SSD (0.3A)
│   ├── ODrive logic (0.5A)
│   ├── STM32 co-processors (0.2A)
│   ├── 10A blade fuse
│   └── INA260 monitoring
│
├── 5V SERVO BUS (Buck #2: 48V→5V, 6A)
│   ├── Dynamixel servos (12 × 0.5A = 6A peak)
│   ├── Speakers/amplifier (0.6A)
│   ├── OLED displays (0.04A)
│   ├── Cooling fans (0.8A)
│   ├── 10A blade fuse
│   └── INA260 monitoring
│
└── 3.3V SENSOR BUS (LDOs ×4: 48V→3.3V, 1A each)
    ├── IMUs (BNO085, BNO055) — LDO #1
    ├── Encoders (AS5048A ×28) — LDO #2
    ├── ADCs (ADS1256 ×4) — LDO #3
    └── Cameras + misc sensors — LDO #4
```

### 3.2 Current Budget

```
CURRENT CONSUMPTION BY SUBSYSTEM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subsystem              Voltage    Current    Power
──────────────────────────────────────────────────────
Left leg motors (×6)   12V        4.0A       48W
Right leg motors (×6)  12V        4.0A       48W
Left arm motors (×6)   12V        2.0A       24W
Right arm motors (×6)  12V        2.0A       24W
Torso motors (×2)      12V        1.5A       18W
Head motors (×2)       12V        0.5A       6W
──────────────────────────────────────────────────────
Motor subtotal         12V        14.0A      168W

RPi 5 + Coral          5V         3.5A       17.5W
Dynamixel servos       5V         3.0A       15W
Cameras                5V         0.3A       1.5W
Audio system           5V         1.2A       6W
OLED displays          3.3V       0.04A      0.13W
IMUs                   3.3V       0.01A      0.03W
Encoders               3.3V       0.03A      0.1W
ADCs                   3.3V       0.02A      0.07W
──────────────────────────────────────────────────────
Electronics subtotal   —          8.1A       40.3W

Cooling fans           5V         0.8A       4W
──────────────────────────────────────────────────────
GRAND TOTAL            —          —          212.3W
──────────────────────────────────────────────────────

At 48V: 212.3W / 48V = 4.42A average

Peak current (all motors + electronics): ~20A
Typical current (walking): ~8A
Idle current (standing): ~2A
Sleep current: ~0.5A
```

---

## 4. Thermal Management

### 4.1 Heat Sources

```
HEAT GENERATION MAP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Component           Power    Efficiency    Heat    Location
──────────────────────────────────────────────────────────────
D6374 motors (×8)   14.5Nm   85%          2.2W/motor  Joints
D5065 motors (×12)  4.8Nm    85%          0.7W/motor  Joints
M5671 motors (×4)   1.2Nm    85%          0.2W/motor  Joints
XL330 servos (×12)  0.52Nm   80%          0.1W/servo  Hands
ODrive S1 (×6)      —        95%          6W/controller  Torso/limbs
ODrive Pro (×2)     —        95%          10W/controller Torso
STM32H7 (×2)        —        —            0.5W/chip     Sensor hub
RPi 5               10W      —            10W           Head/torso
Coral TPU           2W       —            2W            Head/torso
Buck converters (×4) 212W   95%          10.6W         Torso
LDOs (×4)           48V→3.3V —            3W           Torso
──────────────────────────────────────────────────────────────
TOTAL               —        —            ~75W          —

AMBIENT TEMPERATURE RISE:
├── Torso cavity: +15°C (at 25°C ambient = 40°C)
├── Head cavity: +10°C (at 25°C ambient = 35°C)
├── Motor housings: +20°C (at 25°C ambient = 45°C)
└── Battery compartment: +5°C (at 25°C ambient = 30°C)
```

### 4.2 Cooling Strategy

```
ACTIVE + PASSIVE COOLING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASSIVE:
├── Aluminum frame as heat sink (thermal conductivity: 205 W/mK)
├── Motor housings: Anodized aluminum, natural convection
├── PCB copper planes: 2oz copper, thermal vias
├── Thermal pads: 6W/mK silicone pads on hot components
└── φ-ratio fin spacing: 3mm fins at 5mm spacing (optimal natural convection)

ACTIVE:
├── Fan 1: Torso bottom intake (40mm, 5V PWM, Noctua)
│   └── Airflow: 8.2 CFM, 19.7 dB(A)
├── Fan 2: Torso top exhaust (40mm, 5V PWM, Noctua)
│   └── Airflow: 8.2 CFM, 19.7 dB(A)
├── Fan 3: Head (40mm, 5V PWM, Noctua)
│   └── Airflow: 8.2 CFM, 19.7 dB(A)
└── Fan 4: Battery compartment (40mm, 5V PWM, Noctua)
    └── Airflow: 8.2 CFM, 19.7 dB(A)

FAN CONTROL (via STM32 GPIO PWM):
├── Temperature < 35°C: Fans OFF
├── 35°C - 45°C: Fans at 30% (2.5 CFM)
├── 45°C - 55°C: Fans at 60% (4.9 CFM)
├── 55°C - 65°C: Fans at 100% (8.2 CFM)
└── > 65°C: Emergency stop

THERMAL TIMELINE:
├── Cold start (25°C): Fans OFF for first 5 min
├── Walking (384W): Fans ramp to 30% after 10 min
├── Running (720W): Fans ramp to 60% immediately
├── Standing idle (96W): Fans OFF (passive only)
└── After shutdown: Fans run 2 min to cool components
```

---

## 5. Power Efficiency

### 5.1 Conversion Efficiency

```
EFFICIENCY CHAIN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Stage                   Input    Output   Efficiency
──────────────────────────────────────────────────────
Battery (48V)           48V      48V      99% (internal R)
Buck 48V→12V            48V      12V      95%
Buck 48V→5V             48V      5V       95%
LDO 48V→3.3V            48V      3.3V     85%
Motor driver (ODrive)   48V      Phase    95%
Motor (BLDC)            Phase    Mech     85%
──────────────────────────────────────────────────────

Overall efficiency (battery to motor shaft):
η_total = 0.99 × 0.95 × 0.95 × 0.85 = 0.646 (64.6%)

For motor power specifically:
η_motor_path = 0.99 × 0.95 × 0.95 = 0.894 (89.4%)
η_mechanical = 0.85 (motor + gearbox)
η_total_motor = 0.894 × 0.85 = 0.76 (76%)

This is typical for BLDC motor systems.
```

### 5.2 Range Analysis

```
BATTERY LIFE CALCULATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Walking (5 km/h):
├── Power: 384W (motors) + 40W (electronics) = 424W
├── Battery: 40 kWh
├── Runtime: 40,000Wh / 424W = 94.3 hours
├── Distance: 94.3h × 5 km/h = 472 km
└── Realistic (with losses): 80 hours, 400 km

Running (10 km/h):
├── Power: 720W (motors) + 40W (electronics) = 760W
├── Runtime: 40,000Wh / 760W = 52.6 hours
├── Distance: 52.6h × 10 km/h = 526 km
└── Realistic: 45 hours, 450 km

Standing (idle):
├── Power: 96W (motors holding) + 40W (electronics) = 136W
├── Runtime: 40,000Wh / 136W = 294 hours
└── Realistic: 250 hours (10.4 days)

Mixed use (typical day):
├── Walking 4 hours: 424W × 4h = 1,696Wh
├── Manipulation 2 hours: 192W × 2h = 384Wh
├── Standing 4 hours: 136W × 4h = 544Wh
├── Sleep 14 hours: 24W × 14h = 336Wh
├── Daily total: 2,960Wh
├── Days on single charge: 40,000 / 2,960 = 13.5 days
└── Realistic: 8 hours active use per charge (as specified)
```

---

## 6. Safety Features

### 6.1 Electrical Protection

```
PROTECTION LAYERS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Layer 1: Fuses
├── 80A main fuse (slow-blow, 5s response)
├── 20A per limb fuse (fast-blow, 100ms)
├── 10A logic fuse (fast-blow, 50ms)
└── 5A head fuse (fast-blow, 50ms)

Layer 2: Contactors
├── Main contactor: 100A, latching, opens on e-stop
├── E-stop relay #1: 30A, NC, series with contactor
└── E-stop relay #2: 30A, NC, series with contactor

Layer 3: Software
├── ODrive current limits (per motor)
├── INA260 overcurrent detection
├── Temperature monitoring + shutdown
└── Watchdog timer (2s timeout)

Layer 4: Battery BMS
├── Per-module overcurrent: 50A
├── Per-module overvoltage: 54.6V
├── Per-module undervoltage: 40V
├── Short circuit: <100µs response
└── Temperature: 60°C cutoff

FAILSAFE SEQUENCE:
1. E-stop pressed → relays open → contactor coil de-energized
2. Contactor opens → all 48V power cut
3. Motors: Free-spin (no regenerative braking)
4. RPi: Loses power, shuts down gracefully (UPS mode)
5. Result: Robot stops, all motion ceases
```

---

*Document: 12_POWER_SYSTEM.md — PHI_HUMANOID_ROBOT Power System*
*Version: 1.0 | Date: 2026-08-27*
