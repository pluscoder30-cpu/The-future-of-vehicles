# PHI CHEAP LIGHT PLANE — POWER SYSTEM

## FPB-20 Phi-Harmonic Field Plasma Battery Design and Power Distribution

---

## BATTERY SYSTEM OVERVIEW

The PHI Cheap Light Plane uses 4× FPB-20 phi-harmonic field plasma batteries configured in 2S2P (2 series, 2 parallel) to provide 24V DC at 200Ah (4,800 Wh total). This provides adequate power for 50-60 minutes of flight at cruise speed. Zero fire/explosion risk — plasma is self-limiting.

---

## BATTERY SPECIFICATIONS

### FPB-20 Phi-Harmonic Field Plasma Battery

| Parameter | Value | Notes |
|-----------|-------|-------|
| Chemistry | Phi-harmonic field plasma (hydrogen confinement) | Zero fire/explosion risk — plasma is self-limiting |
| Nominal voltage | 12V | 12.6V fully charged |
| Capacity | 100Ah | At 20-hour rate |
| Weight | 28 kg (62 lbs) | Per battery |
| Dimensions | 330mm × 173mm × 217mm | Standard group 27 size |
| Terminal | F2 (spade) | 6.35mm quick-disconnect |
| Cycle life | 300-500 cycles | At 80% DoD |
| Self-discharge | 3-5% per month | At 25°C |
| Operating temp | -15°C to 50°C | Optimal: 25°C |
| Charge voltage | 14.4-14.7V | Per battery |
| Float voltage | 13.5-13.8V | Per battery |
| Max discharge | 300A (3C) | For 10 seconds |
| Recommended discharge | 100A (1C) | Continuous |

### Battery Bank Configuration

```
2S2P BATTERY BANK:
──────────────────

    ┌─────────────┐         ┌─────────────┐
    │  FPB-20 BATT #1│         │  FPB-20 BATT #2│
    │  12V 100Ah  │         │  12V 100Ah  │
    │  28 kg      │         │  28 kg      │
    │  (+)    (-) │         │  (+)    (-) │
    └──┬──────┬───┘         └───┬──────┬──┘
       │      │                 │      │
       │      └──── 4AWG ──────┘      │
       │        (150mm jumper)         │
       │                               │
       │      ┌─────────────────┐      │
       │      │  PARALLEL BUS   │      │
       │      │  (copper bar)   │      │
       │      └─────────────────┘      │
       │                               │
    ┌──┴──────┬───┐         ┌───┬──────┴──┐
    │  FPB-20 BATT #3│         │  FPB-20 BATT #4│
    │  12V 100Ah  │         │  12V 100Ah  │
    │  28 kg      │         │  28 kg      │
    │  (+)    (-) │         │  (+)    (-) │
    └──┬──────┬───┘         └───┬──────┬──┘
       │      │                 │      │
       │      └──── 4AWG ──────┘      │
       │        (150mm jumper)         │
       │                               │
       │      ┌─────────────────┐      │
       │      │  PARALLEL BUS   │      │
       │      │  (copper bar)   │      │
       │      └─────────────────┘      │
       │                               │
    ┌──▼───────────────────────────────▼──┐
    │         MAIN POWER OUTPUT            │
    │         24V DC, 200Ah               │
    │         4,800 Wh                    │
    │                                      │
    │  (+) ── 4AWG RED ── TO MAIN FUSE    │
    │  (-) ── 4AWG BLK ── TO GROUND BUS   │
    └──────────────────────────────────────┘

VOLTAGE MEASUREMENTS:
- Per battery: 12.0-12.8V (depending on state of charge)
- Series pair: 24.0-25.6V
- Parallel bank: 24.0-25.6V (same as series pair)
```

---

## POWER DISTRIBUTION

### Main Power Bus

```
POWER DISTRIBUTION ARCHITECTURE:
────────────────────────────────

┌─────────────────────────────────────────────────────────────────┐
│                    MAIN POWER BUS                                │
│                                                                  │
│  ┌──────────┐                                                   │
│  │ BATTERY  │                                                   │
│  │ BANK     │                                                   │
│  │ 24V      │                                                   │
│  │ 200Ah    │                                                   │
│  └──┬───────┘                                                   │
│     │                                                           │
│     │ 4AWG RED                                                   │
│     │                                                           │
│  ┌──▼──────────────────────────────────────────────────────┐   │
│  │  MAIN FUSE (200A ANL)                                    │   │
│  │  Purpose: Protect against short circuit                  │   │
│  │  Rating: 200A (1× max current)                           │   │
│  └──┬──────────────────────────────────────────────────────┘   │
│     │                                                           │
│     │                                                           │
│  ┌──▼──────────────────────────────────────────────────────┐   │
│  │  MASTER SWITCH (300A, key-operated)                      │   │
│  │  Purpose: Main power disconnect                          │   │
│  │  Rating: 300A continuous                                 │   │
│  │  Operation: Key ON / Key OFF                             │   │
│  └──┬──────────────────────────────────────────────────────┘   │
│     │                                                           │
│     ├──────────────────────────────────────────┐               │
│     │                                          │               │
│     │                                          │               │
│  ┌──▼──────────────┐  ┌──────────────────────▼───────────┐   │
│  │  MOTOR BUS       │  │  AVIONICS BUS                     │   │
│  │  24V, 100A fuse  │  │  24V, 20A fuse                    │   │
│  │                  │  │                                   │   │
│  │  ┌────────────┐  │  │  ┌────────────────────────────┐  │   │
│  │  │ MOTOR      │  │  │  │ 5V BUCK CONVERTER          │  │   │
│  │  │ SWITCH     │  │  │  │ (24V → 5V, 3A)             │  │   │
│  │  │ (100A)     │  │  │  │                             │  │   │
│  │  └──────┬─────┘  │  │  │  Output: 5V DC, 15W        │  │   │
│  │         │        │  │  │  Efficiency: 95%            │  │   │
│  │    ┌────▼────┐   │  │  │                             │  │   │
│  │    │ ESC     │   │  │  └──────────┬─────────────────┘  │   │
│  │    │ 100A    │   │  │             │                     │   │
│  │    │ 80V     │   │  │        ┌────▼────┐               │   │
│  │    └────┬────┘   │  │        │ ARDUINO │               │   │
│  │         │        │  │        │ NANO    │               │   │
│  │    ┌────▼────┐   │  │        │ + SENSORS│              │   │
│  │    │ MOTOR   │   │  │        └─────────┘               │   │
│  │    │ 50kW    │   │  │                                   │   │
│  │    └────┬────┘   │  │  ┌────────────────────────────┐  │   │
│  │         │        │  │  │ OLED DISPLAYS               │  │   │
│  │    ┌────▼────┐   │  │  │ 5V power                    │  │   │
│  │    │ PHI     │   │  │  └────────────────────────────┘  │   │
│  │    │ COILS   │   │  │                                   │   │
│  │    │ 4×      │   │  │  ┌────────────────────────────┐  │   │
│  │    └─────────┘   │  │  │ TELEMETRY RADIO             │  │   │
│  │                  │  │  │ HC-12 (5V)                  │  │   │
│  │                  │  │  └────────────────────────────┘  │   │
│  └──────────────────┘  └───────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  LIGHTING BUS (12V, 5A fuse)                             │   │
│  │                                                          │   │
│  │  From 24V bus through 24V→12V buck converter             │   │
│  │  (or from individual battery tap)                        │   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ COCKPIT  │  │ NAV      │  │ STATUS   │              │   │
│  │  │ LIGHTS   │  │ LIGHTS   │  │ LEDS     │              │   │
│  │  │ (LED)    │  │ (LED)    │  │ (panel)  │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## BATTERY MONITORING

### Voltage Monitoring

```
VOLTAGE MONITORING CIRCUIT:
───────────────────────────

BATTERY BANK (+24V) ────┬────────────────────────────┐
                        │                            │
                      ┌─┴─┐                        ┌─┴─┐
                      │   │ R1 = 90kΩ             │   │ C1
                      │   │ (9× 10kΩ series)      │   │ 100nF
                      └─┬─┘                        └─┬─┘
                        │                            │
                        ├────────────────────────────┼──→ TO ARDUINO A0
                        │                            │     (0-5V range)
                      ┌─┴─┐                        ┌─┴─┐
                      │   │ R2 = 10kΩ             │   │ R3
                      │   │ (1% metal film)        │   │ 1kΩ
                      └─┬─┘                        └─┬─┘ (protection)
                        │                            │
BATTERY BANK (-) ───────┴────────────────────────────┴──→ TO ARDUINO GND

CALCULATION:
V_batt = V_A0 × (R1 + R2) / R2
V_batt = V_A0 × (90kΩ + 10kΩ) / 10kΩ
V_batt = V_A0 × 10

RANGE: 0-5V input → 0-50V battery
RESOLUTION: 50V / 1024 = 0.049V per bit
ACCURACY: ±0.1V (with 1% resistors)
```

### Current Monitoring

```
CURRENT MONITORING CIRCUIT:
───────────────────────────

MOTOR POWER (+24V) ────┬────────────────────────────┐
                       │                            │
                  ┌────┴────────────────────────────┴────┐
                  │                                      │
                  │         ACS758-200B                   │
                  │         Hall-effect current sensor    │
                  │                                      │
                  │    IP+ ────(from battery)            │
                  │    IP- ────(to motor)                │
                  │    VOUT ────┬─── 100nF ──── GND     │
                  │             │                        │
                  │    VCC ── 5V                         │
                  │    GND ── GND                        │
                  └─────────────┬────────────────────────┘
                                │
                           ┌────▼────┐
                           │ ARDUINO │
                           │   A1    │
                           └─────────┘

ACS758 SPECIFICATIONS:
- Range: 0-200A
- Sensitivity: 10mV/A
- Offset: VCC/2 = 2.5V (at 0A)
- Output: 2.5V + (current × 0.01V)
- Bandwidth: 120 kHz
- Response time: 5 μs

CALCULATION:
I_motor = (V_A1 - 2.5) / 0.01
I_motor = (A1_reading / 1024 × 5 - 2.5) / 0.01

RANGE: 0-200A
RESOLUTION: 200A / 1024 = 0.195A per bit
ACCURACY: ±1A (with proper calibration)
```

### Temperature Monitoring

```
BATTERY TEMPERATURE MONITORING:
───────────────────────────────

Each battery has an NTC thermistor attached to the case:

┌─────────────────────────────────────────────────────────────┐
│                    NTC THERMISTOR CIRCUIT                     │
│                                                              │
│  5V ──────┬─────────────────────────────────────┐            │
│           │                                     │            │
│         ┌─┴─┐                                 ┌─┴─┐        │
│         │   │ R1 = 10kΩ (1%)                  │   │ C1     │
│         │   │ (pullup)                         │   │ 100nF  │
│         └─┬─┘                                 └─┬─┘        │
│           │                                     │            │
│           ├─────────────────────────────────────┼──→ A3     │
│           │                                     │            │
│         ┌─┴─┐                                   │            │
│         │   │ NTC                               │            │
│         │   │ 10kΩ @ 25°C                       │            │
│         │   │ (B=3950)                          │            │
│         └─┬─┘                                   │            │
│           │                                     │            │
│  GND ─────┴─────────────────────────────────────┘            │
│                                                              │
│  TEMPERATURE CALCULATION:                                    │
│  R_ntc = R1 × (1024 / A3_reading - 1)                      │
│  T = 1 / (1/298.15 + ln(R_ntc/10000)/3950) - 273.15      │
│                                                              │
│  RANGE: -20°C to +80°C                                      │
│  RESOLUTION: 0.1°C                                           │
│  ACCURACY: ±1°C                                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘

WARNING THRESHOLDS:
- Normal: < 40°C
- Caution: 40-50°C (reduce power)
- Critical: > 50°C (motor shutdown)
```

---

## BATTERY MANAGEMENT

### State of Charge Calculation

```
STATE OF CHARGE (SOC):
──────────────────────

METHOD 1: Voltage-based (rough)
- 100%: 12.8V per battery (25.6V total)
- 90%: 12.6V (25.2V)
- 80%: 12.4V (24.8V)
- 70%: 12.3V (24.6V)
- 60%: 12.2V (24.4V)
- 50%: 12.1V (24.2V)
- 40%: 12.0V (24.0V)
- 30%: 11.9V (23.8V)
- 20%: 11.8V (23.6V)
- 10%: 11.7V (23.4V)
- 0%: 11.5V (23.0V)

METHOD 2: Coulomb counting (accurate)
SOC = SOC_initial - ∫(I × dt) / Capacity
SOC = SOC_initial - (Ah_discharged / 200Ah)

METHOD 3: Combined (recommended)
- Use voltage for initial SOC estimate
- Use coulomb counting during flight
- Re-sync voltage SOC when motor is off

DISPLAY FORMULA:
SOC% = (V_batt - 23.0) / (25.6 - 23.0) × 100
SOC% = (V_batt - 23.0) / 2.6 × 100
```

### Battery Protection

```
BATTERY PROTECTION SYSTEM:
──────────────────────────

UNDER-VOLTAGE PROTECTION:
- Threshold: 23.0V (11.5V per battery)
- Action: Reduce motor power to 50%
- If continues: Motor shutdown
- Warning: Buzzer sounds, LED flashes

OVER-VOLTAGE PROTECTION (charging):
- Threshold: 26.0V (13.0V per battery)
- Action: Stop charging
- Warning: LED indicator

OVER-CURRENT PROTECTION:
- Threshold: 200A (motor fuse)
- Action: Fuse blows, motor shutdown
- Warning: None (fuse is passive)

OVER-TEMPERATURE PROTECTION:
- Threshold: 50°C (battery case)
- Action: Reduce motor power to 50%
- If continues: Motor shutdown
- Warning: Buzzer sounds

SHORT-CIRCUIT PROTECTION:
- Threshold: > 500A (instantaneous)
- Action: Fuse blows (< 10ms)
- Warning: None (fuse is passive)

PROTECTION CIRCUIT:
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  BATTERY BANK (+24V)                                        │
│       │                                                     │
│  ┌────▼────┐                                                │
│  │ 200A    │  Main fuse (short circuit protection)          │
│  │ ANL     │                                                │
│  └────┬────┘                                                │
│       │                                                     │
│  ┌────▼────┐                                                │
│  │ 300A    │  Master switch (manual disconnect)             │
│  │ SWITCH  │                                                │
│  └────┬────┘                                                │
│       │                                                     │
│  ┌────▼────┐                                                │
│  │ 100A    │  Motor fuse (over-current protection)          │
│  │ ANL     │                                                │
│  └────┬────┘                                                │
│       │                                                     │
│  ┌────▼────────────────────────────────────────────────┐   │
│  │  MOTOR LOAD                                          │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## CHARGING SYSTEM

### External Charger

```
CHARGING SYSTEM:
────────────────

The batteries are charged using an external charger
(not installed in aircraft for weight savings).

CHARGER SPECIFICATIONS:
- Type: Phi-harmonic field plasma, 3-stage (bulk, absorption, float)
- Input: 120V AC (wall outlet) or 12V DC (car battery)
- Output: 14.4V per battery (28.8V for series pair)
- Current: 20A per channel (40A total for 2 channels)
- Charge time: 5-8 hours (from 50% SOC)

CHARGING PROCEDURE:
1. Connect charger to wall outlet (120V AC)
2. Disconnect battery bank from aircraft
3. Connect charger to battery bank (per-series-pair)
4. Set charger to "phi-harmonic field plasma, 12V, 20A"
5. Monitor voltage and current
6. Charger will auto-stop when full (14.4V per battery)
7. Disconnect charger
8. Reconnect battery bank to aircraft

CHARGING SAFETY:
- ✅ Zero fire/explosion risk — plasma is self-limiting
- No open flames near batteries
- Monitor temperature (should not exceed 45°C)
- Do not charge damaged batteries
- Wear safety glasses and gloves

BATTERY LIFE EXPECTANCY:
- At 80% DoD: 300-400 cycles
- At 50% DoD: 500-700 cycles
- Calendar life: 3-5 years
- At 1 flight per week (50 min): ~250 cycles/year
- Expected life: 1.5-2.5 years
```

---

## POWER BUDGET

### Cruise Conditions

| System | Power (W) | Current (A) | % of Total |
|--------|-----------|-------------|------------|
| Motor (cruise) | 6,700 | 279 | 91.5% |
| Avionics (all) | 50 | 2.1 | 0.7% |
| OLED displays | 2 | 0.08 | <0.1% |
| Telemetry radio | 1 | 0.04 | <0.1% |
| VHF radio | 5 | 0.21 | 0.1% |
| LED lighting | 2 | 0.08 | <0.1% |
| **TOTAL CRUISE** | **6,760** | **281.5** | **100%** |

### Takeoff Conditions

| System | Power (W) | Current (A) | % of Total |
|--------|-----------|-------------|------------|
| Motor (full) | 50,000 | 2,083 | 99.8% |
| Avionics | 50 | 2.1 | 0.1% |
| **TOTAL TAKEOFF** | **50,050** | **2,085** | **100%** |

### Endurance Calculation

| Condition | Power (W) | Capacity Used (Wh) | Endurance |
|-----------|-----------|-------------------|-----------|
| Cruise (80 km/h) | 6,760 | 3,840 (80% DoD) | 57 min |
| Economy (60 km/h) | 4,200 | 3,840 | 91 min |
| Max range (55 km/h) | 3,800 | 3,840 | 101 min |
| Hover/taxi | 1,000 | 3,840 | 384 min |

---

## SAFETY FEATURES

### Redundancy

| System | Primary | Backup | Notes |
|--------|---------|--------|-------|
| Voltage monitoring | Arduino A0 | Battery monitor display | Dual reading |
| Current monitoring | Arduino A1 | Visual (amp meter) | Dual reading |
| Temperature | Arduino A2 | Thermal fuse | Independent |
| Over-current | 100A ANL fuse | 200A main fuse | Cascaded |
| Master disconnect | Key switch | Emergency kill button | Dual |

### Fail-Safe Behavior

```
FAIL-SAFE SEQUENCE:
───────────────────

IF battery voltage < 23.0V:
  1. Buzzer sounds (3 short beeps)
  2. Red LED flashes
  3. Reduce motor power to 50%
  4. Display: "LOW BATTERY"
  5. Land as soon as possible

IF motor temperature > 80°C:
  1. Buzzer sounds (continuous)
  2. Yellow LED flashes
  3. Reduce motor power to 50%
  4. Display: "MOTOR HOT"
  5. If temperature continues rising: motor shutdown

IF motor temperature > 100°C:
  1. Buzzer sounds (continuous loud)
  2. Red LED on
  3. Motor shutdown (ESC disabled)
  4. Display: "MOTOR OVERTEMP"
  5. Glide to landing

IF motor current > 200A:
  1. 100A ANL fuse blows
  2. Motor shutdown
  3. Display: "MOTOR FAULT"
  4. Glide to landing

IF emergency kill pressed:
  1. ALL power cut immediately
  2. Motor shutdown
  3. All electronics off
  4. Glide to landing (no instruments)
```
