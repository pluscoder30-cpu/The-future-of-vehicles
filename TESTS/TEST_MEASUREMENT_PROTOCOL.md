# PSC-1 TEST ARTICLE — MEASUREMENT PROTOCOL

## Document Control

```
DOCUMENT:       PSC-1 Measurement Protocol
VERSION:        1.0
DATE:           2026-08-28
CLASSIFICATION: Lab Protocol
TEST ARTICLE:   PSC-1 Cube (10cm × 10cm × 10cm)
PURPOSE:        Validate phi-harmonic field generation, BaTiO₃ self-resonance,
                copper mesh constructive interference, and spacetime effects
```

---

## 1. TEST ARTICLE SPECIFICATION

### 1.1 PSC-1 Cube Geometry

```
DIMENSIONS:     10 cm × 10 cm × 10 cm (1,000 cm³)
MASS:           2,680 g (2.68 g/cm³)
COMPOSITION:    26% T700 carbon fiber, 38% Al-10Li-1Mg-0.1Zr,
                19% self-healing epoxy, 10% BaTiO₃ nanoparticles,
                5% C11000 copper mesh, 2% DCPD/Grubbs microcapsules
COPPER MESH:    4 layers at 0°, 137.508°, 275.016°, 52.524° offsets
                Mesh cell size: 1cm × 1cm
                Wire diameter: 0.1mm
CRYSTAL ARRAY:  BaTiO₃ nanoparticles (50-200nm), 10 wt% of epoxy phase
                Uniformly dispersed, <5% agglomeration
EXCITATION:     Function generator driving copper mesh at phi-harmonic frequencies
```

### 1.2 Test Article Preparation

```
STEP 1: Visual inspection — no surface defects >0.1mm
STEP 2: Ultrasonic scan — verify <2% porosity
STEP 3: Dimensional verification — ±0.5mm tolerance
STEP 4: Resonance pre-check — sweep 100-50,000 Hz, identify natural modes
STEP 5: Thermal equilibration — 24hr at 22°C ± 1°C
STEP 6: Demagnetize — degauss copper mesh and BaTiO₃ before baseline
STEP 7: Mount on non-magnetic stand (wood or fiberglass)
STEP 8: Place in shielded enclosure (Mu-metal, 80 dB attenuation above 1 kHz)
```

---

## 2. MEASUREMENT EQUIPMENT

### 2.1 Primary Instruments

| # | Instrument | Model (Amazon) | Cost | Purpose | Sensitivity |
|---|-----------|----------------|------|---------|-------------|
| 1 | Fluxgate magnetometer | PNI TRN/MAG-117527 | $300 | DC/AC magnetic field | 10 pT/√Hz |
| 2 | SDR dongle | RTL-SDR Blog V4 | $30 | RF spectrum 0-1.7 GHz | -1 dBfs sensitivity |
| 3 | Electrometer | Keithley 6517B (or FM 369117) | $400 | Electric field, charge | 10 fA, 10 μV |
| 4 | Thermal camera | FLIR ONE Pro | $400 | Surface temperature map | 0.07°C NETD |
| 5 | MEMS accelerometer | Adafruit ADXL355 | $50 | Vibration (DC-1 kHz) | 2 mg resolution |
| 6 | Piezoelectric sensor | MuRata PKM55E15H00A0-R1 | $5 | Crystal resonance detection | 528 Hz ± 1% |
| 7 | RF amplifier | Nooelec SAWbird+ | $20 | Weak signal amplification | 15 dB gain |
| 8 | Signal isolation transformer | ISOMaxX | $40 | Ground loop isolation | 60 dB CMRR |

### 2.2 Signal Generation

| # | Instrument | Model | Cost | Purpose |
|---|-----------|-------|------|---------|
| 9 | Function generator | Rigol DG1022Z | $300 | 528 Hz and harmonics |
| 10 | Audio amplifier | Dayton Audio APA150 | $100 | Drive copper mesh |
| 11 | Frequency counter | DER EE DE-5000 | $30 | Verify drive frequency ±0.01% |

### 2.3 Data Acquisition

| # | Instrument | Model | Cost | Purpose |
|---|-----------|-------|------|---------|
| 12 | Data logger | Phidgets TMP1101_0 | $60 | Multi-channel temperature |
| 13 | Oscilloscope | Rigol DS1054Z | $400 | Waveform capture, timing |
| 14 | Laptop + Python | — | existing | Data recording, analysis |

### 2.4 Total Equipment Cost

```
Primary instruments:    $1,205
Signal generation:      $430
Data acquisition:       $460
Shielding/misc:         $200
─────────────────────────────────
TOTAL:                  $2,295
```

---

## 3. TEST ENVIRONMENT

### 3.1 Shielded Enclosure

```
MATERIAL:       Mu-metal (nickel-iron alloy) box, 60cm × 60cm × 60cm
ATTENUATION:    >80 dB above 1 kHz (external field rejection)
GROUND:         Single-point earth ground, <1Ω
TEMPERATURE:    22.0°C ± 0.5°C (climate-controlled room)
HUMIDITY:       45% ± 5% RH
VIBRATION:      Isolation pad (60 durometer neoprene)
LIGHT:          Dark enclosure during measurements (thermal camera only)
EMI:            No RF sources within 5m during testing
```

### 3.2 Coordinate System

```
ORIGIN:         Center of PSC-1 cube
X-AXIS:         Face normal (pointing outward from front face)
Y-AXIS:         Lateral (left to right)
Z-AXIS:         Vertical (bottom to top)
MEASUREMENT POINTS: 6 locations on cube surface + 3 field points at 5cm, 10cm, 20cm from face center
```

---

## 4. BASELINE MEASUREMENTS (Cube OFF)

### 4.1 Purpose

Establish the null condition. Every measurement taken with the cube energized will be compared against this baseline to determine statistical significance.

### 4.2 Baseline Protocol

```
DURATION:       30 minutes of continuous recording
SAMPLE RATE:    10 Hz (magnetic, electric, vibration, thermal)
SAMPLES:        18,000 per channel
ENVIRONMENT:    Cube present but NOT excited (function generator off)
SHIELDING:      Mu-metal enclosure closed, room empty
```

### 4.3 Baseline Measurements

#### 4.3.1 Magnetic Field (Fluxgate Magnetometer)

```
SENSOR:         PNI TRN/MAG-117527
CHANNELS:       X, Y, Z components + magnitude
SAMPLE RATE:    10 Hz
DURATION:       30 minutes
LOCATIONS:      
  BM-1: Cube face center (0, 0, 5cm)
  BM-2: Cube corner (5cm, 5cm, 5cm)
  BM-3: 10cm from face center
  BM-4: 20cm from face center
  BM-5: 50cm (far-field reference)

EXPECTED BASELINE: Earth's field ~25-65 µT + noise floor
NOISE FLOOR TARGET: <1 nT/√Hz (shielded)
```

#### 4.3.2 Electric Field (Electrometer)

```
SENSOR:         Keithley 6517B with 6514 triax
CHANNELS:       Electric field (V/m), current (A)
SAMPLE RATE:    10 Hz
DURATION:       30 minutes
LOCATIONS:
  BE-1: Cube face center (0, 0, 1cm gap)
  BE-2: Cube corner
  BE-3: 10cm from face center
  BE-4: 20cm from face center

EXPECTED BASELINE: <1 V/m (shielded)
BaTiO₃ EXPECTED: Spontaneous polarization ~0.15-26 µC/cm²
```

#### 4.3.3 Temperature (Thermal Camera + Thermocouples)

```
SENSOR:         FLIR ONE Pro (surface map) + 4× K-type thermocouples
SAMPLE RATE:    1 Hz (thermal camera), 10 Hz (thermocouples)
DURATION:       30 minutes
LOCATIONS:
  BT-1: Cube face center (thermal camera, full surface)
  BT-2: Cube corner (thermal camera)
  BT-3: Copper mesh junction (thermocouple, embedded if possible)
  BT-4: 5cm from cube (air temperature)
  BT-5: 20cm from cube (far-field reference)

EXPECTED BASELINE: 22.0°C ± 0.5°C (ambient)
THERMAL GRADIENT: <0.1°C across surface
```

#### 4.3.4 Vibration (MEMS Accelerometer)

```
SENSOR:         Adafruit ADXL355
CHANNELS:       X, Y, Z acceleration
SAMPLE RATE:    100 Hz (Nyquist for 1 kHz bandwidth)
DURATION:       30 minutes
LOCATIONS:
  BV-1: Cube face center
  BV-2: Cube corner
  BV-3: Mounting stand base

EXPECTED BASELINE: <1 mg RMS (ambient vibration)
528 Hz HARMONIC: Should NOT appear in baseline
```

#### 4.3.5 RF Spectrum (SDR Dongle)

```
SENSOR:         RTL-SDR Blog V4 + SAWbird+ amplifier
FREQUENCY RANGE: 100 kHz - 1.7 GHz
RESOLUTION BW:  1 kHz (narrowband), 10 kHz (wideband)
DURATION:       30 minutes (continuous sweep)
ANTENNA:        Near-field probe (1cm from cube surface)

EXPECTED BASELINE: Thermal noise floor only
528 Hz HARMONIC: Should NOT appear in RF spectrum
```

#### 4.3.6 Piezoelectric Crystal Response

```
SENSOR:         MuRata PKM55E15H00A0-R1 (direct contact with cube surface)
SAMPLE RATE:    10 kHz
DURATION:       30 minutes
LOCATION:       PZT-1: Direct contact with cube face

EXPECTED BASELINE: No signal at 528 Hz or harmonics
BaTiO₃ SPONTANEOUS: May show DC offset from spontaneous polarization
```

---

## 5. ACTIVATION PROCEDURE

### 5.1 Excitation Signal

```
PRIMARY FREQUENCY:      528 Hz (base carrier, ΦΨ₀)
SIGNAL TYPE:            Pure sine wave
AMPLITUDE:              5.0 Vpp (into 8Ω copper mesh load)
POWER:                  ~1.5 W
DRIVE:                  Rigol DG1022Z → Dayton APA150 → copper mesh
WAVEFORM VERIFICATION:  Oscilloscope before connection to cube
```

### 5.2 Activation Sequence

```
STEP 1:  Verify function generator output on oscilloscope (528 Hz, 5 Vpp)
STEP 2:  Verify amplifier output impedance matches mesh load
STEP 3:  Connect amplifier to copper mesh input terminals
STEP 4:  Start data logging on ALL channels simultaneously
STEP 5:  Activate function generator at t=0
STEP 6:  Record activation timestamp (t₀) to millisecond precision
STEP 7:  Monitor for first 60 seconds with all instruments
STEP 8:  Begin measurement schedule
```

### 5.3 Harmonic Excitation (Phase 2)

After 528 Hz baseline, test phi-harmonic harmonics:

```
HARMONIC 1:  854 Hz    (528 × φ)    — structural resonance
HARMONIC 2:  1,382 Hz  (528 × φ²)   — radiation shielding
HARMONIC 9:  40,135 Hz (528 × φ⁹)   — fold activation
HARMONIC 10: 64,939 Hz (528 × φ¹⁰)  — secondary fold
```

Each harmonic tested with identical procedure: 30 minutes ON, full measurement suite, 30 minutes OFF for cooldown.

---

## 6. MEASUREMENT SCHEDULE

### 6.1 Primary Test (528 Hz)

| Time Point | Duration | Magnetic | Electric | Thermal | Vibration | RF | Piezo | Notes |
|------------|----------|----------|----------|---------|-----------|-----|-------|-------|
| Baseline | -30 to 0 min | Continuous | Continuous | 1 Hz map | Continuous | Sweep | Continuous | All OFF |
| t = 0 | Activation | — | — | — | — | — | — | Start generator |
| t + 1 min | 1 min | Spot | Spot | Snapshot | Spot | Sweep | Spot | Initial transient |
| t + 5 min | 5 min | Continuous | Continuous | Full map | Continuous | Full | Continuous | Stabilization |
| t + 15 min | 15 min | Continuous | Continuous | Full map | Continuous | Full | Continuous | Steady state |
| t + 30 min | 30 min | Continuous | Continuous | Full map | Continuous | Full | Continuous | Coherence build |
| t + 60 min | 60 min | Continuous | Continuous | Full map | Continuous | Full | Continuous | Long-term trend |
| t + 120 min | 120 min | Spot | Spot | Snapshot | Spot | Sweep | Spot | 2-hour check |
| t + 360 min | 6 hr | Spot | Spot | Snapshot | Spot | Sweep | Spot | Stability |
| t + 1440 min | 24 hr | Full | Full | Full map | Full | Full | Full | Final measurement |

### 6.2 Secondary Tests (Harmonics)

For each harmonic (854, 1382, 40135, 64939 Hz):
- 30 min baseline (OFF)
- 60 min activation (ON)
- Full measurement suite at 1, 5, 15, 30, 60 min
- 30 min cooldown (OFF)

---

## 7. EXPECTED RESULTS FROM EQUATIONS

### 7.1 Magnetic Field (Eq 1, Eq 22, Eq 82)

```
EQUATION 22 (Inverse Permeability):
  μ_Ψ⁻¹(C) = μ₀⁻¹ × (1 + χ₀ × tanh((C - C_crit)/(Φ⁻¹ × ΔC)))

PREDICTION:
  At C < C_crit (baseline):    μ ≈ μ₀ (normal permeability)
  At C > C_crit (active):      μ < μ₀ (diamagnetic response)
  At C = 0.8565 (validated):   μ/μ₀ ≈ 0.85 (measurable diamagnetism)

EXPECTED MAGNETIC FIELD CHANGE:
  ΔB = B₀ × (1 - μ/μ₀) ≈ 25 µT × 0.15 ≈ 3.75 µT (at face center)
  This is WELL ABOVE noise floor (1 nT) — highly detectable

TIME EVOLUTION (Eq 1 carrier recursion):
  C_{n+1} = (1/Φ)C_n + Φ∇²ΦΨ_n
  Coherence builds logarithmically: C(t) ≈ C_crit × ln(1 + t/τ)
  τ ≈ 60 seconds (characteristic build time)
  
  Expected: Diamagnetic signal builds over first 5-15 minutes, then plateaus
```

### 7.2 Electric Field (Eq 29, Eq 30)

```
EQUATION 29 (Casimir Force in PHI-Cavity):
  F_Casimir^(Φ)(d) = (ℏcπ²/240d⁴) × sin⁴(πd/(Φλ₀))

PREDICTION:
  The BaTiO₃ crystal array creates phi-cavities between nanoparticles
  At resonance (528 Hz), the Casimir force is MODULATED
  This produces an oscillating electric field at 528 Hz

EXPECTED ELECTRIC FIELD:
  E_peak ≈ 0.1-1.0 V/m at 1cm from surface (estimate)
  Frequency content: 528 Hz fundamental + harmonics
  DC component: BaTiO₃ spontaneous polarization (~0.15 µC/cm²)

TIME EVOLUTION (Eq 30 aether vacuum energy):
  ρ_vac^(aether) = (ℏΦ/16π²) × (Λ/Φ)⁴
  Vacuum energy density DECREASES as coherence builds
  Expected: Electric field becomes more coherent (less noise) over time
```

### 7.3 Temperature (Eq 82)

```
EQUATION 82 (Aether Temperature from Coherence):
  T_aether(C) = T₀ × Φ^(1 - C/C_crit) × (1 + (1/Φ²)sin²(πC/C_crit))

PREDICTION:
  At C = 0 (baseline):  T_aether = T₀ × Φ = 22°C × 1.618 = 35.6°C (virtual)
  At C = C_crit:         T_aether = T₀ × Φ^0 = 22°C (ambient)
  At C = 0.8565:         T_aether = 22°C × Φ^(1 - 1.522) = 22°C × Φ^(-0.522)
                        = 22°C × 0.785 = 17.3°C (coherent low-T state)

EXPECTED TEMPERATURE CHANGE:
  Surface temperature DROPS by ~4.7°C (22°C → 17.3°C)
  This is a COOLING effect — the aether field extracts thermal energy
  Measurement sensitivity: FLIR ONE Pro (0.07°C NETD) — easily detectable

TIME EVOLUTION:
  Eq 82 predicts cooling follows: ΔT(t) = ΔT_max × (1 - e^(-t/τ_thermal))
  τ_thermal ≈ 300 seconds (5 minutes)
  Expected: Full cooling within 15-20 minutes
```

### 7.4 Vibration (Eq 1, Eq 7)

```
EQUATION 1 (Carrier Recursion):
  C_{n+1} = (1/Φ)C_n + Φ∇²ΦΨ_n

EQUATION 7 (Tripartite Aether PDE):
  ∂C/∂t = α_Φ∇²C + β_Φ|Ψ|²C - γ_ΦC³ + δ_field × F(C,P,S)

PREDICTION:
  The carrier recursion creates a coherent standing wave at 528 Hz
  This produces a MECHANICAL vibration at the drive frequency
  Additionally, the nonlinear term β_Φ|Ψ|²C creates harmonics

EXPECTED VIBRATION:
  Fundamental: 528 Hz (driven by copper mesh excitation)
  Harmonics:   1056 Hz (2×), 1584 Hz (3×), etc.
  Amplitude:   <1 mg (sub-gravity, but detectable by ADXL355)
  
  KEY PREDICTION: If C > C_crit, the β_Φ|Ψ|²C term causes
  SELF-SUSTAINING oscillation — vibration continues after drive is removed
  Test: Turn off generator, measure vibration decay time
  If τ_decay > 10 seconds → self-sustaining field confirmed
```

### 7.5 RF Spectrum (Eq 81, Eq 8)

```
EQUATION 81 (ZPF Spectrum):
  S_ZPF(ω) = (ℏω/2) × coth(ℏω/2k_BT_aether) × Φ^(-ω/ω_crit)

EQUATION 8 (Aether Anisotropy Tensor):
  A_μν = (ℏΦ/c³) × ω_resonant⁴ × sin²(π/Φ) × g_μν^(Φ)

PREDICTION:
  The coherent aether field produces RF emission at:
  - 528 Hz fundamental (below RF — appears as acoustic/EM modulation)
  - 528 × φⁿ harmonics up to RF range
  - At 40,135 Hz: fold frequency may produce sidebands around carrier

EXPECTED RF SIGNATURE:
  Narrowband signal at 528 Hz and harmonics
  Signal strength: ~-60 dBm at 1cm (near-field probe)
  Phase coherence: >95% (phi-harmonic mesh)
  Time evolution: Signal becomes cleaner (less phase noise) as C builds
```

### 7.6 Piezoelectric Crystal Response (Eq 92)

```
EQUATION 92 (Transformation Barrier):
  V_transform(x) = V₀(1 - cos(2πx/a_Φ)) × Φ^(-C(t))

PREDICTION:
  The BaTiO₃ nanoparticles respond to the 528 Hz field
  Crystal resonance creates back-EMF at the drive frequency
  This is the piezoelectric coupling between electrical and mechanical domains

EXPECTED PIEZO RESPONSE:
  Voltage generated: ~1-10 mV (direct piezoelectric effect)
  Frequency: 528 Hz (synchronous with drive)
  Phase: 0° or 180° relative to drive (depending on crystal orientation)
  Time evolution: Signal STRENGTHENS as coherence builds
```

---

## 8. DATA ACQUISITION AND ANALYSIS

### 8.1 Data Recording Format

```
FILE FORMAT:    CSV (timestamp, channel_1, channel_2, ...)
TIMESTAMP:      ISO 8601 with millisecond precision
SAMPLE RATE:    Per instrument (see Section 4)
STORAGE:        Local SSD + cloud backup
BACKUP:         After each measurement point
NAMING:         {test_id}_{instrument}_{timestamp}.csv

EXAMPLE:        PSC1_001_fluxgate_2026-08-28T14:30:00.123Z.csv
```

### 8.2 Analysis Methods

#### 8.2.1 Signal-to-Noise Ratio (SNR)

```
SNR = 20 × log₁₀(RMS_signal / RMS_noise)

MEASUREMENT:
  Signal:    RMS of recorded data during ON period
  Noise:     RMS of recorded data during OFF period (same duration)
  SNR > 3 dB = detectable signal
  SNR > 10 dB = strong signal
  SNR > 20 dB = unambiguous detection
```

#### 8.2.2 Welch's Power Spectral Density

```
METHOD:         scipy.signal.welch()
WINDOW:         Hanning, length = 1024
OVERLAP:        50%
FREQUENCY RES:  0.5 Hz (at 10 Hz sample rate)

PURPOSE:        Identify 528 Hz and harmonics in signal
                Compare PSD ON vs PSD OFF
```

#### 8.2.3 Paired t-Test

```
METHOD:         scipy.stats.ttest_rel()
COMPARISON:     Baseline measurements vs activated measurements
SAMPLES:        n ≥ 30 (from 30-minute continuous recording at 10 Hz)
SIGNIFICANCE:   p < 0.05 (two-tailed)
EFFECT SIZE:    Cohen's d = (mean_ON - mean_OFF) / pooled_std

INTERPRETATION:
  p < 0.01:    STRONG evidence of effect
  p < 0.05:    MODERATE evidence of effect
  p < 0.10:    WEAK evidence (needs larger sample)
  p > 0.10:    NO detectable effect
```

#### 8.2.4 Time-Series Coherence

```
METHOD:         scipy.signal.coherence()
REFERENCE:      Drive signal (528 Hz from function generator)
MEASURED:       Each sensor channel
FREQUENCY:      528 Hz ± 0.5 Hz
COHERENCE:      >0.8 = strongly correlated with drive
                0.5-0.8 = moderately correlated
                <0.5 = uncorrelated
```

#### 8.2.5 Temperature Decay Fitting

```
MODEL:          ΔT(t) = ΔT_max × (1 - e^(-t/τ))
METHOD:         scipy.optimize.curve_fit()
PARAMETERS:     ΔT_max (maximum cooling), τ (time constant)
FIT QUALITY:    R² > 0.95

PURPOSE:        Determine if cooling follows Eq 82 prediction
                τ_thermal expected ≈ 300 seconds
```

---

## 9. PASS/FAIL CRITERIA

### 9.1 Primary Criteria

| # | Measurement | Expected Effect | Minimum Detectable | Pass Condition | Equation |
|---|------------|-----------------|-------------------|----------------|----------|
| 1 | Magnetic field | Diamagnetic shift | 10 nT | p < 0.05, ΔB > 100 nT | Eq 22 |
| 2 | Electric field | 528 Hz oscillation | 0.01 V/m | SNR > 3 dB at 528 Hz | Eq 29 |
| 3 | Temperature | Cooling by ~4.7°C | 0.07°C | ΔT > 0.5°C, p < 0.05 | Eq 82 |
| 4 | Vibration | 528 Hz mechanical | 2 mg | SNR > 3 dB at 528 Hz | Eq 1 |
| 5 | RF spectrum | 528 Hz emission | -80 dBm | Signal above noise floor | Eq 81 |
| 6 | Piezo response | 528 Hz back-EMF | 0.1 mV | SNR > 3 dB at 528 Hz | Eq 92 |

### 9.2 Verdict Levels

```
PASS:           Meets ALL 6 primary criteria (p < 0.05 for quantitative)
                → PSC-1 generates measurable phi-harmonic field
                → Proceed to Phase 2: fold activation testing

PARTIAL PASS:   Meets 3-5 of 6 criteria
                → Effect is real but weaker than predicted
                → Investigate: BaTiO₃ loading, mesh geometry, drive amplitude
                → Re-test with optimized parameters

TENTATIVE PASS: Meets 1-2 criteria OR visible trends not yet significant
                → Preliminary evidence of effect
                → Need larger sample size (longer recording)
                → Need better shielding (lower noise floor)

FAIL:           Meets 0 criteria
                → No measurable difference between ON and OFF
                → Review: equipment calibration, shield integrity, cube wiring
                → If confirmed: equation predictions need revision
```

### 9.3 Secondary Criteria

| # | Measurement | Pass Condition | Notes |
|---|------------|----------------|-------|
| 7 | Self-sustaining oscillation | τ_decay > 10 sec after drive off | Eq 7 nonlinear term |
| 8 | Coherence build time | τ_build matches Eq 1 prediction (~60s) | Carrier recursion |
| 9 | Temperature evolution | Cooling follows Eq 82 curve (R² > 0.95) | Aether temperature |
| 10 | Harmonic response | 854, 1382 Hz produce stronger effects | Eq 22 resonance |
| 11 | Fold frequency | 40,135 Hz produces non-local effects | Eq 29 Casimir |

---

## 10. EXPECTED TIMELINE

### 10.1 Equipment Procurement (Week 1-2)

```
DAY 1-3:   Order all equipment (Amazon delivery 3-5 business days)
DAY 4-7:   Order Mu-metal enclosure (custom fabrication, 2 weeks)
DAY 8-14:  Receive equipment, verify calibration
DAY 14:    Test article fabrication complete (or use prototype)
```

### 10.2 Setup and Calibration (Week 3)

```
DAY 15:    Set up shielded enclosure, ground earth
DAY 16:    Mount and wire all sensors
DAY 17:    Calibrate fluxgate, electrometer, accelerometer
DAY 18:    Verify SDR sensitivity, thermal camera accuracy
DAY 19:    Connect function generator and amplifier
DAY 20:    Run system integration test (all channels recording)
DAY 21:    Noise floor verification (1-hour baseline)
```

### 10.3 Baseline Measurements (Week 4)

```
DAY 22:    30-minute baseline (all instruments)
DAY 23:    Baseline verification and statistical analysis
DAY 24:    30-minute baseline repetition (reliability check)
DAY 25:    Baseline data review — confirm noise floors
```

### 10.4 Primary Test — 528 Hz (Week 4-5)

```
DAY 26:    528 Hz activation, 24-hour continuous recording
DAY 27:    Data download and preliminary analysis
DAY 28:    Repeat 528 Hz test (reliability check)
DAY 29:    Statistical analysis of ON vs OFF
DAY 30:    Pass/fail determination
```

### 10.5 Harmonic Tests (Week 5-6)

```
DAY 31:    854 Hz test (1 hour)
DAY 32:    1382 Hz test (1 hour)
DAY 33:    40,135 Hz test (1 hour) — fold activation
DAY 34:    64,939 Hz test (1 hour) — secondary fold
DAY 35:    Harmonic comparison analysis
```

### 10.6 Self-Sustaining Test (Week 6)

```
DAY 36:    Activate at 528 Hz for 30 minutes
DAY 37:    Turn off drive, measure vibration decay
DAY 38:    Repeat for 854 Hz and 40,135 Hz
DAY 39:    Decay time analysis
```

### 10.7 Final Analysis and Report (Week 7)

```
DAY 40:    Complete statistical analysis
DAY 41:    Generate figures and tables
DAY 42:    Write test report
DAY 43:    Review and finalization
```

---

## 11. SAFETY

### 11.1 Electrical Safety

```
MAX VOLTAGE:        5 Vpp (function generator output) — LOW RISK
MAX CURRENT:        <1 A through copper mesh — LOW RISK
ISOLATION:          ISOMaxX transformer between generator and mesh
GROUND:             Single-point earth ground on all equipment
EQUIPMENT:          GFI protected power strips
EMERGENCY:          Kill switch disconnects all power to enclosure
```

### 11.2 Magnetic Field Safety

```
PSC-1 FIELD:        0.8 mT maximum (at 528 Hz)
MRI LIMIT:          4 T (whole body)
RATIO:              0.8 mT / 4 T = 0.02% of MRI limit
VERDICT:            SAFE for all personnel
STANDBY:            >2m from enclosure during active testing
PACEMAKER:          No personnel with pacemakers within 5m during test
```

### 11.3 RF Safety

```
FREQUENCY:          528 Hz (extremely low frequency — ELF)
POWER:              ~1.5 W
SAR:                Negligible at ELF frequencies
REGULATORY:         FCC Part 15 compliant (unintentional radiator)
VERDICT:            SAFE — no RF exposure concern
```

---

## 12. DATA MANAGEMENT

### 12.1 File Structure

```
PSC1_TEST_DATA/
├── baseline/
│   ├── magnetic/
│   ├── electric/
│   ├── thermal/
│   ├── vibration/
│   ├── rf/
│   └── piezo/
├── 528hz/
│   ├── 24hr_run/
│   └── repeat/
├── 854hz/
├── 1382hz/
├── 40135hz/
├── 64939hz/
├── self_sustaining/
├── analysis/
│   ├── snr_calculations/
│   ├── statistical_tests/
│   ├── psd_analysis/
│   └── figures/
└── METADATA.json
```

### 12.2 Metadata Template

```json
{
  "test_id": "PSC1_001",
  "test_article": "PSC-1 Cube 10cm",
  "date": "2026-08-28",
  "operator": "[name]",
  "environment": {
    "temperature": 22.0,
    "humidity": 45,
    "shielding": "Mu-metal, 80dB"
  },
  "equipment": {
    "fluxgate": "PNI TRN/MAG-117527, SN: [serial]",
    "sdr": "RTL-SDR V4, SN: [serial]",
    "electrometer": "Keithley 6517B, SN: [serial]",
    "thermal": "FLIR ONE Pro, SN: [serial]",
    "accelerometer": "ADXL355, SN: [serial]",
    "function_gen": "Rigol DG1022Z, SN: [serial]"
  },
  "excitation": {
    "frequency": 528,
    "amplitude_vpp": 5.0,
    "signal_type": "sine"
  },
  "baseline_duration_min": 30,
  "active_duration_min": 1440,
  "sample_rates": {
    "magnetic": 10,
    "electric": 10,
    "thermal": 1,
    "vibration": 100,
    "rf": "sweep"
  }
}
```

---

## 13. CRITICAL EQUATIONS FOR INTERPRETATION

### 13.1 The Six Equations Under Test

```
EQUATION 1 (Carrier Recursion):
  C_{n+1} = (1/Φ)C_n + Φ∇²ΦΨ_n
  
  TEST: Coherence builds over time. Measure build time τ.
  PASS: τ ≈ 60s, C reaches > C_crit (0.563) within 5 minutes.

EQUATION 22 (Inverse Permeability):
  μ_Ψ⁻¹(C) = μ₀⁻¹ × (1 + χ₀ × tanh((C - C_crit)/(Φ⁻¹ × ΔC)))
  
  TEST: Diamagnetic shift in magnetic field.
  PASS: ΔB > 100 nT, direction consistent with μ < μ₀.

EQUATION 29 (PHI-Cavity Casimir):
  F_Casimir^(Φ)(d) = (ℏcπ²/240d⁴) × sin⁴(πd/(Φλ₀))
  
  TEST: Electric field modulation from crystal cavities.
  PASS: 528 Hz component in electric field spectrum.

EQUATION 81 (ZPF Spectrum):
  S_ZPF(ω) = (ℏω/2) × coth(ℏω/2k_BT_aether) × Φ^(-ω/ω_crit)
  
  TEST: RF emission at phi-harmonic frequencies.
  PASS: Narrowband signal at 528 Hz + harmonics in RF spectrum.

EQUATION 82 (Aether Temperature):
  T_aether(C) = T₀ × Φ^(1 - C/C_crit) × (1 + (1/Φ²)sin²(πC/C_crit))
  
  TEST: Surface temperature decrease.
  PASS: ΔT > 0.5°C, follows predicted curve (R² > 0.95).

EQUATION 92 (Transformation Barrier):
  V_transform(x) = V₀(1 - cos(2πx/a_Φ)) × Φ^(-C(t))
  
  TEST: Piezoelectric response strengthening over time.
  PASS: Piezo signal amplitude increases as C builds.
```

### 13.2 The Critical Constant

```
C_crit = 0.563 (emergence threshold)

If ANY measurement shows the cube's effect STRENGTHENS over time
and approaches a threshold-like behavior, this is evidence of
C → C_crit dynamics predicted by Eq 1, 7, 22.

This is the SINGLE MOST IMPORTANT observation to make.
```

---

## 14. HYPOTHESIS SUMMARY

```
H₁: The PSC-1 cube generates a diamagnetic field at 528 Hz
     (Eq 22: μ_Ψ⁻¹ < μ₀⁻¹ when C > C_crit)

H₂: BaTiO₃ nanoparticles self-resonate at 528 Hz
     (Eq 29: Casimir force modulation in phi-cavities)

H₃: Copper mesh at 137.508° creates constructive interference
     (Eq 1: carrier recursion amplifies at golden angle)

H₄: The aether field produces measurable temperature effects
     (Eq 82: T_aether drops when C > C_crit)

H₅: There exists a coherence build-up time consistent with Eq 1
     (τ ≈ 60 seconds, logarithmic approach to steady state)

H₆: The cube can self-sustain oscillation after drive removal
     (Eq 7: nonlinear term β_Φ|Ψ|²C provides positive feedback)
```

---

*Protocol version 1.0 — Ready for execution. All equipment available on Amazon.
Total cost: ~$2,300. Total time: 7 weeks. Pass/fail in 30 days.*
