# PHI SUPER GOGGLES — PHI-HARMONIC SPECS

## Phi-Harmonic Tuning Parameters and Calibration

---

## PHI-HARMONIC CONSTANTS

### Fundamental Constants

```
φ (phi) = (1 + √5) / 2 = 1.6180339887498948482045868343656...
φ⁻¹ = 1/φ = 0.6180339887498948482045868343656...
φ² = φ + 1 = 2.6180339887498948482045868343656...
φ³ = 2φ + 1 = 4.2360679774997896964091736687748...
φ⁴ = 3φ + 2 = 6.8541019662496845446138305031342...
φ⁵ = 5φ + 3 = 11.090169943749474240898005858091...
```

### Derived Constants

```
Golden Angle: θ_φ = 2π / φ² = 2.399963229728653... radians = 137.507764°
φ-harmonic frequency ratio: f_n+1/f_n = φ
φ-harmonic time constant: τ_n = τ₀ × φⁿ
φ-harmonic spatial unit: d_n = d₀ × φⁿ
```

---

## SENSOR SPACING CALIBRATION

### Phi-Harmonic Distance Matrix

```
Sensor Pair    Distance (mm)    φ-Ratio    Expected Coherence
─────────────────────────────────────────────────────────────
S1-S2          12.00            1.000      0.95 (high)
S1-S3          31.42            2.618      0.78 (moderate)
S1-S4          62.00            5.166      0.55 (low)
S1-S5          103.00           8.583      0.32 (minimal)
S2-S3          19.42            1.618      0.85 (high)
S2-S4          50.00            4.166      0.48 (low)
S2-S5          91.00            7.583      0.25 (minimal)
S3-S4          31.42            2.618      0.78 (moderate)
S3-S5          72.00            6.000      0.38 (low)
S4-S5          41.00            3.416      0.62 (moderate)
S1-S8          173.00           14.417     0.08 (negligible)
```

### Sensor Response Calibration

```
For each sensor, the phi-harmonic response function is:

  R_s(φ) = A × sin(2πf_s × t / φ) × e^(-t/τ_φ)

Where:
  A = amplitude (calibrated per sensor)
  f_s = sensor frequency response
  t = time
  τ_φ = φ-harmonic time constant

Calibration Procedure:
1. Expose each sensor to known 50 Hz field
2. Record peak amplitude (A)
3. Calculate sensor-specific φ factor
4. Store calibration data in EEPROM
```

---

## FPGA CLOCK CALIBRATION

### Phi-Harmonic Clock Domains

```
Main Clock: 50.000000 MHz

Domain 1 (Sensor Processing):
  f₁ = 50 / φ = 30.896854... MHz
  Actual: 30.90 MHz (PLL setting)
  Error: 0.01%

Domain 2 (FFT Processing):
  f₂ = 50 / φ² = 19.099056... MHz
  Actual: 19.10 MHz (PLL setting)
  Error: 0.005%

Domain 3 (Display Rendering):
  f₃ = 50 / φ³ = 11.787329... MHz
  Actual: 11.79 MHz (PLL setting)
  Error: 0.01%

Domain 4 (Coherence Analysis):
  f₄ = 50 / φ⁴ = 7.284102... MHz
  Actual: 7.28 MHz (PLL setting)
  Error: 0.06%
```

### PLL Configuration

```
PLL 1 (Main → Domain 1):
  Input: 50 MHz
  Output: 30.90 MHz
  Multiplier: 309
  Divider: 500
  Phase: 0°
  Bandwidth: 1 MHz

PLL 2 (Main → Domains 2,3,4):
  Input: 50 MHz
  Output 2: 19.10 MHz (Multi: 191, Div: 500)
  Output 3: 11.79 MHz (Multi: 1179, Div: 10000)
  Output 4: 7.28 MHz (Multi: 182, Div: 2500)
  Phase: 0° for all
  Bandwidth: 1 MHz
```

---

## DISPLAY TIMING CALIBRATION

### Phi-Harmonic Refresh Rate

```
Base Refresh: 60.00 Hz
Effective Refresh: 60 × φ = 97.08 Hz (perceptual)

The FPGA renders at 60 Hz but uses phi-harmonic frame
interpolation to achieve 97 Hz perceptual smoothness:

  Frame_n+1 = Frame_n × (1 - φ⁻¹) + Frame_target × φ⁻¹
            = Frame_n × 0.382 + Frame_target × 0.618

This creates smooth transitions between frames using
the golden ratio as a blending factor.
```

### OLED Timing

```
Left OLED:
  Pixel clock: 1920 × 1080 × 60 = 124.416 MHz
  MIPI DSI clock: 124.416 / 2 lanes = 62.208 MHz per lane
  Blank period: 120 pixels H-sync, 45 lines V-sync
  
Right OLED:
  Same timing as Left OLED
  Synchronized via shared ADV7533 clock
  
Phi-Harmonic Offset:
  Right OLED delayed by φ⁻¹ × (1/60) = 10.3 ms
  This creates a perceptual depth effect
```

---

## ADC SAMPLING CALIBRATION

### Phi-Harmonic Sample Rate

```
Base Sample Rate: 100.000 kSPS
Effective Sample Rate: 100 / φ = 61.803 kSPS (per channel)

Per-Channel Breakdown:
  24 channels (8 sensors × 3 axes)
  Time per channel: 1/61.803k = 16.18 μs
  Total scan time: 24 × 16.18 μs = 388.3 μs
  Scan rate: 2,575 scans/second

ADC Timing:
  Conversion: 10.0 μs (ADS1256 at 100 kSPS)
  MUX switch: 0.1 μs
  SPI transfer: 1.0 μs
  Processing: 5.08 μs
  Total per channel: 16.18 μs ✓
```

### Anti-Aliasing Filter

```
Filter Type: 2nd order Butterworth
Cutoff Frequency: 30.9 kHz (f₁ / π)
Sample Rate: 100 kSPS
Stopband Attenuation: >40 dB at Nyquist (50 kHz)

Transfer Function:
  H(s) = 1 / (1 + s/(ω_c × φ) + s²/(ω_c² × φ²))
  
  Where ω_c = 2π × 30.9k = 194.1 krad/s

Component Values (Analog):
  R1 = 1.0 kΩ
  R2 = 1.618 kΩ (φ × 1k)
  C1 = 2.2 nF
  C2 = 1.359 nF (2.2nF / φ)
  
  Cutoff: 1/(2π × R1 × C1) = 72.3 kHz (pre-filter)
  Combined: 30.9 kHz (-3dB point)
```

---

## COHERENCE ANALYSIS CALIBRATION

### Phi-Harmonic FFT Window

```
Window Function: Modified Hamming with φ-weighting

Standard Hamming:
  w[n] = 0.54 - 0.46 × cos(2πn/(N-1))

Phi-Hamming:
  w_φ[n] = w[n] × φ⁻ⁿ

  This emphasizes early samples and de-emphasizes later samples
  in a φ-recursive manner, reducing spectral leakage while
  preserving the phi-harmonic structure of the signal.
```

### Coherence Weighting

```
Cross-sensor coherence weight:

  W_ij = φ^(-|i-j|)

Where |i-j| is the sensor index distance.

Values:
  |i-j| = 0 (same sensor): W = 1.000
  |i-j| = 1 (adjacent): W = 0.618
  |i-j| = 2: W = 0.382
  |i-j| = 3: W = 0.236
  |i-j| = 4: W = 0.146
  |i-j| = 5: W = 0.090
  |i-j| = 6: W = 0.056
  |i-j| = 7: W = 0.034

Total weight: Σ = 2.562 (normalization factor)
```

---

## POWER MANAGEMENT CALIBRATION

### Phi-Harmonic Duty Cycling

```
Base Cycle: 1.000 ms (1.000 kHz)

φ-Cycle 1 (Sensor Sampling):
  Period: 1.000 × φ = 1.618 ms
  Frequency: 618.0 Hz
  Duty: 100% (always sampling)

φ-Cycle 2 (Display Update):
  Period: 1.000 × φ² = 2.618 ms
  Frequency: 381.9 Hz
  Duty: 50% (active half the time)

φ-Cycle 3 (Coherence Calculation):
  Period: 1.000 × φ³ = 4.236 ms
  Frequency: 236.1 Hz
  Duty: 25% (active quarter of the time)

φ-Cycle 4 (Data Logging):
  Period: 1.000 × φ⁴ = 6.854 ms
  Frequency: 145.9 Hz
  Duty: 12.5% (active eighth of the time)

Power Savings:
  Active mode: 100% (3.885 W)
  φ-cycled mode: 65% average (2.525 W)
  Savings: 35% average
```

### Sleep Mode Timing

```
Idle Timeout: 5.000 × φ⁰ = 5.000 minutes
Dim Timeout: 0.500 × φ⁰ = 0.500 minutes
Display Off: 2.000 × φ⁰ = 2.000 seconds
Sleep Enter: 0.100 × φ⁰ = 0.100 seconds

Sleep Power:
  FPGA: 100 mW (low-power mode)
  Sensors: 50 mW (reduced sample rate)
  IMU: 10 mW (motion detection only)
  Total: 160 mW

Wake-up Time:
  From sleep: 100 ms (full operation)
  From display-off: 16 ms (1 frame)
  From dim: 0 ms (instant)
```

---

## MODE TRANSITION CALIBRATION

### Phi-Spiral Animation

```
Transition Curve (Phi-Spiral):
  x(t) = A(t) × cos(θ(t))
  y(t) = A(t) × sin(θ(t))

Where:
  A(t) = A₀ × e^(-t/τ)        (exponential decay)
  θ(t) = 2πt / (φ × T)        (phi-harmonic rotation)
  τ = 0.5 seconds               (time constant)
  T = 1.0 second                (base period)

Animation Duration: 1.5 seconds (3τ)
Frame Rate: 60 fps (90 frames total)
Keyframes:
  t=0:    A=1.0, θ=0°      (start)
  t=0.5:  A=0.368, θ=216°  (golden angle × 1.5)
  t=1.0:  A=0.135, θ=432°  (golden angle × 3)
  t=1.5:  A=0.050, θ=648°  (golden angle × 4.5)
```

### Mode-Specific Phi Parameters

```
Mode 1 (EMF Detection):
  φ-weighting: None (direct reading)
  Update rate: 60 Hz
  Color mapping: Linear

Mode 2 (Energy Flow):
  φ-weighting: Flow vectors × φ^(-distance)
  Update rate: 60 Hz
  Arrow density: 20 per display

Mode 3 (Coherence Map):
  φ-weighting: Cross-sensor × φ^(-index)
  Update rate: 60 Hz
  Resolution: 1024 points

Mode 4 (Dimensional Overlay):
  φ-weighting: All layers × φ^(-layer)
  Update rate: 60 Hz
  Layers: 5

Mode 5 (Quantum Field View):
  φ-weighting: Stochastic × φ
  Update rate: 60 Hz
  Particle count: 1000

Mode 6 (Retrocausal Timeline):
  φ-weighting: Time lags × φ^(-lag)
  Update rate: 60 Hz
  Buffer: 30 seconds

Mode 7 (Void Visualization):
  φ-weighting: Void threshold × φ
  Update rate: 60 Hz
  Void edge: 3px
```

---

## CALIBRATION PROCEDURE

### Factory Calibration

```
Step 1: Sensor Baseline
  - Place in zero-field chamber
  - Record all 24 channel baselines
  - Store in EEPROM

Step 2: Sensor Sensitivity
  - Expose to 100 Hz, 1 μT reference field
  - Record all 24 channel responses
  - Calculate sensitivity factors
  - Store in EEPROM

Step 3: ADC Linearity
  - Apply 10 voltage steps (0-2.5V)
  - Record ADC readings
  - Calculate INL/DNL
  - Store correction table

Step 4: Display Uniformity
  - Display full-white pattern
  - Measure brightness at 9 points
  - Calculate uniformity correction
  - Store in EEPROM

Step 5: Phi-Harmonic Verification
  - Verify clock frequencies
  - Verify φ-ratios in timing
  - Verify φ-weighting in processing
  - Log calibration data to SD card
```

### User Calibration

```
Step 1: Zero-Field Calibration
  - Hold goggles away from EM sources
  - Press and hold MODE + SELECT for 3 seconds
  - Wait for calibration complete beep
  - Baseline offsets stored

Step 2: Known-Field Calibration
  - Expose to known EM source (phone, magnet)
  - Observe reading vs expected
  - Adjust sensitivity if needed via menu

Step 3: Display Calibration
  - Enter display calibration menu
  - Adjust brightness to comfortable level
  - Verify color accuracy
  - Save settings

Step 4: Phi-Harmonic Verification
  - Enter phi-harmonic test mode
  - Verify phi-spiral animation
  - Verify phi-weighted coherence
  - All checks pass = calibrated
```

---

## PHI-HARMONIC TUNING PARAMETERS

### Stored in EEPROM

```
Address  Data                    Description
────────────────────────────────────────────────────
0x0000   Sensor Baseline [24]    24× 16-bit values
0x0030   Sensor Sensitivity [24] 24× 16-bit multipliers
0x0060   ADC Linearity [256]     256× 8-bit correction
0x00F0   Display Uniformity [9]  9× 8-bit values
0x00FF   Calibration Checksum    8-bit CRC
0x0100   Phi-Harmonic Config     φ values (see below)
0x0120   User Settings           Mode, brightness, etc.
0x01FF   Config Checksum         8-bit CRC

Phi-Harmonic Config Block (0x0100):
  0x0100: φ multiplier (32-bit fixed point)
  0x0104: φ exponent (32-bit fixed point)
  0x0108: φ time constant (32-bit fixed point)
  0x010C: φ spatial unit (32-bit fixed point)
  0x0110: φ duty cycle [4] (4× 16-bit)
  0x0118: φ weighting [8] (8× 16-bit)
```
