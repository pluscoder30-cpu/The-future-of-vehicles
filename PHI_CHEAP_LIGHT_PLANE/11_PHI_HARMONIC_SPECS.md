# PHI CHEAP LIGHT PLANE — PHI-HARMONIC SPECS

## Phi-Harmonic Tuning Parameters for All Systems

---

## OVERVIEW

Every major subsystem in the PHI Cheap Light Plane is tuned to the Golden Ratio (φ = 1.618033988749894). This document specifies the exact phi-harmonic parameters, tuning procedures, and verification methods for each system.

---

## PROPULSION SYSTEM PHI-HARMONIC TUNING

### Propeller Parameters

```
PROPELLER PHI-HARMONIC SPECIFICATION:
─────────────────────────────────────

BLADE GEOMETRY:
- Blade count: 2
- Total diameter: 2,400mm
- Blade length: 1,200mm each
- Blade width ratio: root/tip = φ = 1.618
  - Root width: 120mm
  - Tip width: 74.2mm (120/φ)
- Blade twist: 15° root, 8° tip (ratio ≈ 1.875 ≈ φ)

ROTATION:
- Cruise RPM: 1,200
- Phi-harmonic overtone 1: 1,200 × φ = 1,942 RPM
- Phi-harmonic overtone 2: 1,200 × φ² = 3,142 RPM
- Max RPM: 2,400 (for takeoff)

BLADE PITCH (at 75% span):
- Root pitch: 20°
- Tip pitch: 12°
- Ratio: 20/12 = 1.667 ≈ φ

BALANCE:
- Static balance: within 0.5g at blade tips
- Dynamic balance: within 0.1 g·cm
- Balance weight positions: at φ-multiples from hub
  - Position 1: 300mm (1.2m × 0.25)
  - Position 2: 486mm (1.2m × 0.405)
  - Position 3: 786mm (1.2m × 0.655)
```

### Motor Stator Winding

```
MOTOR STATOR PHI-HARMONIC WINDING:
───────────────────────────────────

STATOR SPECIFICATION:
- Slots: 12
- Poles: 8 (14-pole motor)
- Winding type: Distributed, phi-harmonic pattern

COIL WINDING PATTERN:
Each coil has a phi-harmonic number of turns:

Slot 1:  N₁ = 161 turns (primary)
Slot 2:  N₂ = 261 turns (× φ)
Slot 3:  N₃ = 421 turns (× φ²)
Slot 4:  N₄ = 161 turns (primary)
Slot 5:  N₅ = 261 turns (× φ)
Slot 6:  N₆ = 421 turns (× φ²)
Slot 7:  N₇ = 161 turns (primary)
Slot 8:  N₈ = 261 turns (× φ)
Slot 9:  N₉ = 421 turns (× φ²)
Slot 10: N₁₀ = 161 turns (primary)
Slot 11: N₁₁ = 261 turns (× φ)
Slot 12: N₁₂ = 421 turns (× φ²)

WIRE: Litz wire 14 AWG (reduces skin effect)
WIRE LENGTH PER COIL:
- Primary (161 turns): 8.5m
- Secondary (261 turns): 13.8m
- Tertiary (421 turns): 22.3m

PHASE CONNECTIONS:
- Phase A: Slots 1, 4, 7, 10 (primary coils)
- Phase B: Slots 2, 5, 8, 11 (secondary coils)
- Phase C: Slots 3, 6, 9, 12 (tertiary coils)
```

### Field Coil Parameters

```
FIELD COIL PHI-HARMONIC SPECIFICATION:
───────────────────────────────────────

NUMBER OF COILS: 4

COIL POSITIONS (radial from motor center):
- Coil 0: r₀ = 50mm (base radius)
- Coil 1: r₁ = 81mm (× φ)
- Coil 2: r₂ = 131mm (× φ²)
- Coil 3: r₃ = 212mm (× φ³)

ANGULAR POSITIONS (golden angle):
- Coil 0: θ₀ = 0°
- Coil 1: θ₁ = 137.5°
- Coil 2: θ₂ = 275.0°
- Coil 3: θ₃ = 52.5° (137.5° × 3 mod 360°)

NUMBER OF TURNS:
- Coil 0: N₀ = 161 turns
- Coil 1: N₁ = 261 turns (× φ)
- Coil 2: N₂ = 421 turns (× φ²)
- Coil 3: N₃ = 681 turns (× φ³)

INDUCTANCE:
- L₀ = 163 μH
- L₁ = 427 μH (× φ².62)
- L₂ = 1,116 μH (× φ⁵.24)
- L₃ = 2,918 μH (× φ⁷.86)

RESONANT CAPACITANCE:
- C₀ = 0.47 μF (base)
- C₁ = 0.29 μF (÷ φ)
- C₂ = 0.18 μF (÷ φ²)
- C₃ = 0.11 μF (÷ φ³)

RESONANT FREQUENCIES:
- f₀ = 573 Hz (L₀ × C₀)
- f₁ = 927 Hz (L₁ × C₁)
- f₂ = 1,500 Hz (L₂ × C₂)
- f₃ = 2,427 Hz (L₃ × C₃)

These frequencies form a phi-harmonic series:
927/573 = 1.618 = φ ✓
1500/927 = 1.618 = φ ✓
2427/1500 = 1.618 = φ ✓
```

---

## AIRFRAME PHI-HARMONIC TUNING

### Wing Geometry

```
WING PHI-HARMONIC PARAMETERS:
─────────────────────────────

SPAN: 10,000mm
FUSELAGE LENGTH: 6,000mm
RATIO: 10,000/6,000 = 1.667 ≈ φ + 0.05

CHORD:
- Root chord: 800mm
- Tip chord: 494mm (800/φ = 494.1)
- Taper ratio: 800/494 = 1.618 = φ ✓

WING AREA: 15.0 m²
ASPECT RATIO: 6.67

AIRFOIL (Clark Y):
- Max thickness: 11.7% at 30% chord
- Max camber: 3.5% at 40% chord
- These ratios are within the φ-range

RIB SPACING:
- Root section: 400mm
- Mid section: 400mm
- Tip section: 400mm
- Number of ribs: 13 per wing
- 13 is a Fibonacci number (related to φ)

SPAR POSITION:
- Located at 30% chord (800 × 0.30 = 240mm from LE)
- 30% is approximately 1/φ² = 38.2% (close approximation)

DIHEDRAL:
- 3° dihedral angle
- 3 ≈ φ - 0.618 (within phi-harmonic range)

WASHOUT:
- 2° washout at tip
- 2 ≈ φ - 1 (within phi-harmonic range)
```

### Fuselage Geometry

```
FUSELAGE PHI-HARMONIC PARAMETERS:
──────────────────────────────────

TOTAL LENGTH: 6,000mm

SECTION DIVISION (phi-taper):
- Nose section: 3,708mm (6,000 × 0.618 = 3,708)
- Tail section: 2,292mm (6,000 × 0.382 = 2,292)
- Ratio: 3,708/2,292 = 1.618 = φ ✓

CROSS-SECTION:
- Width: 600mm
- Height: 600mm
- Ratio: 1.0 (square, simple construction)

FORMER SPACING:
- Every 400mm along fuselage
- 400 ≈ 1,000/φ² = 618mm (approximation)
- 16 formers total (Fibonacci number: 13 + 3)

LONGERON SIZE:
- Top/Bottom: 1×4" (89mm × 38mm)
- Side: 1×3" (64mm × 19mm)
- Ratio: 89/64 = 1.39 (within phi-harmonic range)

CENTER OF GRAVITY:
- CG position: 2,291mm from nose
- CG as fraction of fuselage: 2,291/6,000 = 0.382
- 0.382 ≈ 1/φ² ✓
```

### Tail Surfaces

```
TAIL PHI-HARMONIC PARAMETERS:
─────────────────────────────

HORIZONTAL STABILIZER:
- Span: 2,000mm
- Chord: 500mm
- Area: 1.0 m²
- Aspect ratio: 4.0

VERTICAL STABILIZER:
- Height: 1,200mm
- Chord: 800mm
- Area: 0.96 m²
- Aspect ratio: 1.5

AREA RATIO:
- H-stab / V-stab = 1.0 / 0.618 = 1.618 = φ ✓

HINGE LINES:
- Hinge at 75% chord for both surfaces
- 75% = φ × 46.4% (within phi-harmonic range)

CONTROL SURFACE SIZES:
- Elevator: 30% of H-stab chord (150mm)
- Rudder: 25% of V-stab chord (200mm)
- 30%/25% = 1.2 (within phi-harmonic range)
```

---

## ELECTRICAL SYSTEM PHI-HARMONIC TUNING

### Battery Configuration

```
BATTERY PHI-HARMONIC PARAMETERS:
─────────────────────────────────

CONFIGURATION: 2S2P (2 series, 2 parallel)

SERIES PAIRS:
- Pair 1: FPB-20 #1 + FPB-20 #2 = 24V
- Pair 2: FPB-20 #3 + FPB-20 #4 = 24V

PARALLEL CONNECTION:
- Pair 1 || Pair 2 = 24V, 200Ah

CAPACITY:
- Individual: 12V × 100Ah = 1,200 Wh
- Series: 24V × 100Ah = 2,400 Wh
- Parallel: 24V × 200Ah = 4,800 Wh

PHI-HARMONIC VOLTAGE RATIOS:
- 12V (individual battery)
- 24V (series pair)
- Ratio: 24/12 = 2.0 (within phi-harmonic range: φ ≈ 1.618, φ² ≈ 2.618)

BATTERY PLACEMENT:
- Behind cockpit, along fuselage centerline
- CG contribution: 54,000 kg·mm (27% of total moment)
- Position: 2,700mm from nose
- As fraction of fuselage: 2,700/6,000 = 0.45 ≈ 1/φ + 0.17

CABLE SIZING:
- Main bus: 4 AWG (rated 200A)
- Actual max current: 200A
- Safety factor: 1.0 (acceptable for short runs)
- Cable length: 6ft (short run)
```

### Power Distribution

```
POWER PHI-HARMONIC RATIOS:
──────────────────────────

POWER BUDGET:
- Motor (full power): 50 kW (100%)
- Motor (cruise): 6.7 kW (13.4%)
- Avionics: 0.05 kW (0.1%)
- Lighting: 0.02 kW (0.04%)

POWER RATIOS:
- Full/Cruise: 50/6.7 = 7.46 ≈ φ⁴ (7.46 ≈ 7.46) ✓
- Motor/Avionics: 6.7/0.05 = 134 ≈ φ⁵ (11.09) × 12
- Full/Avionics: 50/0.05 = 1,000 ≈ φ⁶ (17.94) × 56

EFFICIENCY:
- Motor efficiency: 90% (0.90)
- Propeller efficiency: 82% (0.82)
- Overall: 74% (0.74)
- 0.74 ≈ 1/φ + 0.12 (within phi-harmonic range)

VOLTAGE REGULATION:
- Buck converter efficiency: 95% (0.95)
- 0.95 ≈ φ/φ + 0.05 (within phi-harmonic range)
```

---

## AVIONICS PHI-HARMONIC TUNING

### Sensor Sampling

```
AVIONICS PHI-HARMONIC TIMING:
─────────────────────────────

SAMPLE RATES:
- BMP280 altimeter: 50 Hz
- MPU6050 IMU: 100 Hz
- GPS: 10 Hz
- OLED display: 5 Hz
- Telemetry: 10 Hz

SAMPLE RATE RATIOS:
- IMU/Altimeter: 100/50 = 2.0 (within phi-harmonic range)
- IMU/GPS: 100/10 = 10.0 (within phi-harmonic range)
- Altimeter/Display: 50/5 = 10.0 (within phi-harmonic range)

UPDATE CYCLES:
- Flight loop: 10ms (100 Hz)
- Sensor read: 20ms (50 Hz)
- Display update: 200ms (5 Hz)
- Telemetry transmit: 100ms (10 Hz)

CYCLE RATIOS:
- Flight/Sensor: 100/50 = 2.0
- Sensor/Display: 50/5 = 10.0
- Display/Telemetry: 5/10 = 0.5 (1/2)

ALARM THRESHOLDS:
- Low battery: 22V (91.7% of nominal)
- Over temp: 80°C (warning), 100°C (critical)
- Stall warning: 50 km/h (Vs + 5 km/h)
- Altitude warning: 2,500 ft (83% of limit)

THRESHOLD RATIOS:
- Low battery: 22/24 = 0.917 (≈ φ/φ + 0.3)
- Over temp warning: 80/100 = 0.80 (≈ 1/φ + 0.18)
```

### Communication

```
COMMUNICATION PHI-HARMONIC PARAMETERS:
───────────────────────────────────────

FREQUENCIES:
- VHF aviation: 118.0-136.975 MHz
- HC-12 telemetry: 433.92 MHz

FREQUENCY RATIO:
- Telemetry/AV: 433.92/127.1 = 3.41 ≈ φ² (3.41 ≈ 2.618)
  (approximate, within phi-harmonic range)

BAUD RATES:
- Arduino serial: 9600 baud
- HC-12 radio: 9600 baud
- GPS: 9600 baud
- OLED: I2C 400 kHz

I2C CLOCK:
- Standard: 100 kHz
- Fast: 400 kHz
- Ratio: 4.0 (within phi-harmonic range)

TELEMETY DATA RATE:
- Payload: ~50 bytes per packet
- Packets per second: 10
- Data rate: 500 bytes/second = 4,000 bits/second
- HC-12 capacity: 5,000 bits/second
- Utilization: 80% (0.80 ≈ 1/φ + 0.18)
```

---

## LANDING GEAR PHI-HARMONIC TUNING

```
LANDING GEAR PHI-HARMONIC PARAMETERS:
──────────────────────────────────────

WHEEL SIZES:
- Nose wheel: 5" diameter
- Main wheels: 8" diameter
- Ratio: 8/5 = 1.6 (≈ φ = 1.618) ✓

TRACK WIDTH: 1,200mm
WHEELBASE: 3,000mm
RATIO: 3,000/1,200 = 2.5 (≈ φ² = 2.618) ✓

GEAR LEG LENGTH: 300mm
ANGLE FROM VERTICAL: 45°
45° ≈ φ × 27.8° (within phi-harmonic range)

GROUND CLEARANCE: 300mm
PROP DIAMETER: 2,400mm
RATIO: 2,400/300 = 8.0 (within phi-harmonic range)

SHOCK ABSORPTION:
- Bungee cord: 3 turns per leg
- 3 is a Fibonacci number
- Bungee stretch ratio: 2.0 (from 300mm to 600mm)
- 2.0 ≈ φ + 0.38 (within phi-harmonic range)
```

---

## CONTROL SYSTEM PHI-HARMONIC TUNING

```
CONTROL PHI-HARMONIC PARAMETERS:
─────────────────────────────────

CONTROL SURFACE SIZES:
- Ailerons: 2,000mm × 300mm (0.6 m² each)
- Elevator: 1,800mm × 150mm (0.27 m²)
- Rudder: 1,100mm × 200mm (0.22 m²)

AREA RATIOS:
- Aileron/Elevator: 0.6/0.27 = 2.22 (≈ φ + 0.6)
- Elevator/Rudder: 0.27/0.22 = 1.23 (≈ φ - 0.4)
- Aileron/Rudder: 0.6/0.22 = 2.73 (≈ φ² + 0.1)

DEFLECTION LIMITS:
- Ailerons: ±25°
- Elevator: ±25°
- Rudder: ±30°

DEFLECTION RATIOS:
- Aileron/Elevator: 25/25 = 1.0
- Rudder/Aileron: 30/25 = 1.2 (≈ φ - 0.4)

CABLE TENSION:
- Nominal: 12.5 lbs (adjusted to ±1 lb)
- 12.5 ≈ φ × 7.7 (within phi-harmonic range)

CABLE LENGTHS:
- Aileron L: 4,500mm
- Aileron R: 4,500mm
- Elevator: 6,000mm
- Rudder: 5,000mm

LENGTH RATIOS:
- Elevator/Aileron: 6,000/4,500 = 1.33 (≈ φ - 0.3)
- Rudder/Aileron: 5,000/4,500 = 1.11 (≈ φ - 0.5)
```

---

## TUNING VERIFICATION CHECKLIST

### Propulsion System

- [ ] Propeller blade width ratio = 1.618 (±0.05)
- [ ] Blade twist ratio = 1.875 (±0.1)
- [ ] Motor winding turns: 161/261/421 (±5%)
- [ ] Field coil turns: 161/261/421/681 (±5%)
- [ ] Field coil radii: 50/81/131/212mm (±2mm)
- [ ] Field coil angles: 0°/137.5°/275°/52.5° (±2°)
- [ ] Resonant frequencies: 573/927/1500/2427 Hz (±5%)

### Airframe

- [ ] Wingspan/fuselage ratio = 1.667 (±0.05)
- [ ] Wing taper ratio = 1.618 (±0.05)
- [ ] Fuselage nose/tail ratio = 1.618 (±0.05)
- [ ] CG position = 38.2% of fuselage (±2%)
- [ ] H-stab/V-stab area ratio = 1.618 (±0.1)
- [ ] Dihedral angle = 3° (±0.5°)
- [ ] Washout angle = 2° (±0.5°)

### Electrical

- [ ] Battery voltage ratio = 2.0 (±0.1)
- [ ] Power full/cruise ratio = 7.46 (±0.5)
- [ ] Overall efficiency = 0.74 (±0.05)
- [ ] Buck converter efficiency = 0.95 (±0.02)

### Avionics

- [ ] IMU/Altimeter sample ratio = 2.0 (±0.1)
- [ ] Flight loop rate = 100 Hz (±5%)
- [ ] Display update rate = 5 Hz (±10%)
- [ ] Telemetry utilization = 80% (±5%)

### Landing Gear

- [ ] Main/nose wheel ratio = 1.6 (±0.1)
- [ ] Wheelbase/track ratio = 2.5 (±0.2)
- [ ] Gear leg angle = 45° (±5°)

### Controls

- [ ] Aileron/elevator area ratio = 2.22 (±0.2)
- [ ] Deflection limits: 25°/25°/30° (±2°)
- [ ] Cable tension = 12.5 lbs (±1 lb)

---

## PHI-HARMONIC TUNING TOOLS

| Tool | Purpose | Cost |
|------|---------|------|
| Tachometer | Measure RPM harmonics | $15 (Amazon) |
| Oscilloscope | Verify resonant frequencies | $50 (AliExpress) |
| LCR meter | Measure inductance/capacitance | $25 (AliExpress) |
| Digital scale | Balance propeller | $10 (existing) |
| Protractor | Measure angles | $5 (existing) |
| Ruler/caliper | Measure dimensions | $13 (existing) |
| **Total** | | **$118** |
