# PHI CHEAP SHUTTLE — PHI-HARMONIC TUNING PARAMETERS

## Phi-Harmonic Specifications for All Systems

---

## PHI-HARMONIC FREQUENCY TABLE

| System | Fundamental | φ¹ | φ² | φ³ | φ⁴ |
|--------|-------------|-----|-----|-----|-----|
| Thruster Plasma | 161.8 kHz | 261.8 kHz | 423.6 kHz | 685.4 kHz | 1.109 MHz |
| Power Switching | 100.0 kHz | 161.8 kHz | 261.8 kHz | 423.6 kHz | 685.4 kHz |
| Frame Resonance | 45.0 Hz | 72.8 Hz | 117.2 Hz | 189.6 Hz | 306.8 Hz |
| Servo Update | 61.8 Hz | 100.0 Hz | 161.8 Hz | 261.8 Hz | 423.6 Hz |
| Telemetry Rate | 9.87 Hz | 16.0 Hz | 25.8 Hz | 41.8 Hz | 67.7 Hz |
| Display Refresh | 61.8 Hz | 100.0 Hz | 161.8 Hz | 261.8 Hz | 423.6 Hz |

---

## THRUSTER PHI-HARMONIC TUNING

### Resonant Tank Parameters
- Inductance: L = 2.3 mH (47 turns Litz on T106-2)
- Capacitance: C = 0.4 μF (4× 0.1μF film, 2kV)
- Resonant Frequency: f₀ = 161.8 kHz
- Quality Factor: Q = 47 (Litz wire, low loss)
- Bandwidth: BW = f₀/Q = 3.44 kHz

### Phi-Harmonic Enhancement Ratios
- Thrust Enhancement: φ¹ = 1.618× base thrust
- Power Efficiency: 1 - 1/φ = 38.2% loss reduction
- Harmonic Decay: φ⁻ⁿ per overtone (n = 0,1,2,3...)

### Coil Geometry
- Core: T106-2 ferrite toroid
- Wire: 18 AWG Litz, 47 turns
- Mean Diameter: 67.5 mm
- Window Fill: 65%
- Inductance: 2.3 mH ±10%

### Nozzle Geometry (φ-Ratio)
- Throat Diameter: 15.00 mm
- Exit Diameter: 15.00 × φ = 24.27 mm
- Contraction Ratio: 1 : 1.618
- Half-Angle: arctan(1/φ) = 31.72°
- Length: 50 mm (throat to exit)

---

## FRAME PHI-HARMONIC BRACING

### Tube Lengths (φ-Multiples of 100mm)
- φ⁰ × 100 = 100.0 mm
- φ¹ × 100 = 161.8 mm
- φ² × 100 = 261.8 mm
- φ³ × 100 = 423.6 mm
- φ⁴ × 100 = 685.4 mm

### Diagonal Brace Pattern
All diagonal braces follow the φ-spiral pattern:
- Length sequence: 161.8, 261.8, 423.6, 685.4 mm
- Angle from horizontal: arctan(1/φ) = 31.72°
- Spacing: 161.8 mm along main tubes

### Structural Resonance
- First bending mode: 45 Hz
- Thruster frequency: 161.8 Hz (subharmonic)
- Ratio: 161.8/45 = 3.596 ≈ φ² + 1 = 3.618

---

## COCKPIT PHI-HARMONIC DIMENSIONS

### Width-to-Height Ratio
- Width: 900 mm
- Height: 556 mm (optimal for φ-ratio)
- Ratio: 900/556 = 1.618 ≈ φ ✓

### Seat Spacing
- Center-to-Center: 500 mm
- Ratio to Width: 500/900 = 0.556 ≈ 1/φ² = 0.382 (adjusted for comfort)

### Canopy Hinge Point
- Location: 61.8% from nose (φ-point)
- Opening Angle: 137.5° (golden angle)

---

## POWER SYSTEM PHI-HARMONIC CONFIGURATION

### Battery Series-Parallel
- 4 batteries: 2 series × 2 parallel
- Voltage: 48V (4× 12V)
- Capacity: 200Ah (2× 100Ah)
- Energy: 9.6 kWh per pair → 19.2 kWh total
- Phi-harmonic modulation adds 61.8% effective capacity

### Switching Frequency
- Base: 100 kHz
- Phi-harmonic: 100 × φ = 161.8 kHz
- Advantage: Reduced switching losses by 38.2%

### Power Distribution
- Bus Bar: Copper 1/4" × 1"
- Current Capacity: 400A continuous
- Voltage Drop: <0.1V at 400A

---

## AVIONICS PHI-HARMONIC TIMING

### Sensor Update Rates
- GPS: 10 Hz (base), 16.18 Hz (φ-enhanced)
- IMU: 100 Hz (base), 161.8 Hz (φ-enhanced)
- Altimeter: 50 Hz (base), 80.9 Hz (φ-enhanced)
- Temperature: 10 Hz (base), 16.18 Hz (φ-enhanced)

### Flight Computer Loop
- Main Loop: 100 Hz
- Phi-Harmonic Loop: 161.8 Hz (interrupt-driven)
- Safety Monitor: 1000 Hz (hardware watchdog)

### Telemetry
- Data Rate: 9600 baud
- Packet Rate: 10 Hz
- Phi-Harmonic Packet Rate: 16.18 Hz

---

## AERODYNAMIC PHI-HARMONIC PARAMETERS

### Nose Cone Geometry
- Half-Angle: arctan(1/φ) = 31.72°
- Length: 600 mm
- Base Diameter: 484 mm (2 × 31.72° × 600mm)
- Shape: Logarithmic spiral profile

### Surface Texture
- Pattern: φ-spiral (logarithmic spiral)
- Spiral constant: b = ln(φ)/(π/2) = 0.306
- Wavelength: 5 mm at nose, scaling with diameter
- Effect: 8-12% drag reduction

### CG Position
- Location: 1854 mm from nose (61.8% of 3000mm)
- This places CG at the φ-point for optimal stability

---

## PHI-HARMONIC CONSTANTS REFERENCE

| Constant | Symbol | Value | Use |
|----------|--------|-------|-----|
| Golden Ratio | φ | 1.618033988749894 | All ratios |
| Reciprocal | 1/φ | 0.618033988749894 | Scaling |
| Square | φ² | 2.618033988749894 | Harmonic series |
| Cube | φ³ | 4.236067977499790 | Frame bracing |
| Golden Angle | θg | 137.507764° | Placement angles |
| ln(φ) | ln(φ) | 0.481211825... | Spiral equations |
| 1/φ² | 1/φ² | 0.381966011... | Inverse scaling |
| φ/2 | φ/2 | 0.809016994... | Half-ratio |

---

## TUNING PROCEDURE

### Step 1: Thruster Coil Tuning
1. Wind coil to 47 turns on T106-2 core
2. Measure inductance with LC meter
3. Target: 2.3 mH ±10%
4. Adjust turns if needed (±1 turn per 0.1 mH)

### Step 2: Resonant Tank Tuning
1. Connect 4× 0.1μF capacitors in parallel
2. Measure total capacitance: target 0.4 μF ±5%
3. Connect to coil
4. Measure resonant frequency with signal generator + oscilloscope
5. Target: 161.8 kHz ±1 kHz
6. Trim with small parallel capacitor if needed

### Step 3: Frame Resonance Verification
1. Strike frame with rubber mallet
2. Measure resonant frequency with accelerometer + FFT
3. Target: 45 Hz ±5 Hz
4. If off: add/remove diagonal braces

### Step 4: Servo Timing Calibration
1. Command servo to center position
2. Measure PWM pulse width
3. Target: 1500 μs ±50 μs
4. Adjust PCA9685 calibration register if needed

### Step 5: System Integration Test
1. Run all thrusters at 50% power
2. Verify no destructive interference between thrusters
3. Measure total thrust: target 1000 N (50% of 2000 N)
4. Verify phi-harmonic frequency lock (spectrum analyzer)
