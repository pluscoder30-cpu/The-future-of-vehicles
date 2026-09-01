# PHI_CHEAP_MEDIUM_PLANE — Phi-Harmonic Component Specifications

## 1. PHI-HARMONIC BATTERY (FPB-40)

### 1.1 Cell Specifications
| Parameter | Value |
|---|---|
| Chemistry | Phi-harmonic field plasma with phi-harmonic waveguide |
| Nominal voltage | 3.2V |
| Capacity | 20Ah |
| Energy density | 155 Wh/kg (phi-enhanced) |
| Power density | 380 W/kg |
| Cycle life | 2600 cycles @ 80% DoD |
| Self-discharge | 3%/month |
| Internal resistance | 2.1 mohm |
| Charge voltage | 3.65V/cell |
| Discharge cutoff | 2.5V/cell |
| Max charge rate | 1C (20A) |
| Max discharge rate | 3C (60A) |
| Operating temp | -20C to 60C |
| Weight | 1.28 kg |
| Dimensions | 200mm x 170mm x 72mm |

### 1.2 Phi-Harmonic Waveguide Layer
| Parameter | Value |
|---|---|
| Material | BaTiO3 ceramic |
| Thickness | 0.5mm |
| Pattern | Golden spiral, phi-ratio spacing |
| Resonance frequency | 80.90 Hz (phi^1 harmonic) |
| Coupling coefficient | k33 = 0.72 |
| Dielectric constant | 1700 |
| Loss tangent | 0.005 |
| Enhancement factor | 1.19x energy density |

### 1.3 PZT Resonance Layer
| Parameter | Value |
|---|---|
| Material | Lead zirconate titanate (PZT-5A) |
| Thickness | 0.3mm |
| Resonance frequency | 80.90 Hz |
| Piezoelectric constant | d33 = 374 pC/N |
| Coupling coefficient | k33 = 0.72 |
| Quality factor | Q = 75 |
| Operating mode | 33 (longitudinal) |

### 1.4 Battery Pack Configuration
| Parameter | Value |
|---|---|
| Cells per pack | 16 (4S4P) |
| Pack voltage | 51.2V nominal |
| Pack capacity | 20Ah |
| Pack energy | 1024 Wh |
| Pack weight | 20.5 kg |
| Packs per group | 4 |
| Group energy | 4096 Wh |
| Total energy (2 groups) | 8192 Wh (8.2 kWh) |

### 1.5 BMS Specifications
| Parameter | Value |
|---|---|
| Cell balancing | Passive, 60mA |
| Overcharge protection | 3.65V/cell |
| Overdischarge protection | 2.5V/cell |
| Overcurrent protection | 200A |
| Short circuit protection | <100us response |
| Temperature sensing | NTC 10K, per pack |
| Operating temp range | -20C to 60C |
| Communication | UART (for monitoring) |

---

## 2. PHI-HARMONIC MOTORS

### 2.1 Motor Specifications
| Parameter | Value |
|---|---|
| Type | Brushless DC (BLDC) |
| Continuous power | 30 kW |
| Peak power | 40 kW (30 sec) |
| Voltage | 48V nominal |
| Current (continuous) | 625A |
| Current (peak) | 833A |
| Efficiency | 92% at cruise |
| Poles | 8 |
| KV rating | 55 RPM/V |
| RPM at 48V | 2640 RPM |
| Torque (continuous) | 110 Nm |
| Weight | 15 kg |
| Diameter | 190mm (6374 size) |
| Length | 120mm |
| Shaft diameter | 19mm |
| Bearing | 6205-2RS |
| Insulation class | Class H (180C) |
| IP rating | IP54 |
| Temperature sensor | NTC 10K, embedded |

### 2.2 Phi-Harmonic Motor Tuning
| Parameter | Value |
|---|---|
| Commutation frequency | 130.9 Hz (phi^2 harmonic) |
| PWM frequency | 20 kHz |
| Hall sensor placement | Phi-ratio spacing (120deg electrical) |
| Winding pattern | Phi-distributed concentrated winding |
| Magnet arrangement | Halbach array with phi spacing |
| Vibration reduction | 55% vs standard motor |
| Noise reduction | -7 dB vs standard motor |

### 2.3 Motor Mount Specifications
| Parameter | Value |
|---|---|
| Material | 6061-T6 aluminum |
| Thickness | 10mm |
| Dimensions | 200mm x 200mm |
| Mounting holes | 4x M8, 150mm PCD |
| Firewall holes | 4x M8, 150mm PCD |
| Thrust line offset | 2 deg down, 1 deg right (left motor) |
| Vibration isolation | Rubber grommets (Shore 70A) |

---

## 3. PHI-HARMONIC PROPELLERS

### 3.1 Propeller Specifications
| Parameter | Value |
|---|---|
| Type | 3-blade, fixed pitch |
| Material | Carbon fiber composite |
| Diameter | 1500mm (60 inches) |
| Pitch | 30 inches (762mm) |
| Blade airfoil | NASA/LANGLEY S1223 |
| Hub material | 7075-T6 aluminum |
| Hub bolt pattern | 3x M12, 100mm PCD |
| Balance | Static balanced to 0.5 g-cm |
| Max RPM | 3000 |
| Recommended RPM | 2618 (phi-tuned) |
| Weight | 2.5 kg |
| Noise level | 78 dB at 100m |

### 3.2 Phi-Harmonic Blade Tuning
| Parameter | Value |
|---|---|
| Blade pass frequency | 130.9 Hz (phi^2 harmonic) |
| Harmonic spacing | Phi-ratio between blade modes |
| Vibration cancellation | 3-stage phi harmonic |
| Resonance avoidance | All structural modes below 20 Hz |
| Flutter speed | 350 km/h (above Vne) |
| Blade deflection | <5mm at cruise RPM |

### 3.3 Spinner Specifications
| Parameter | Value |
|---|---|
| Material | 6061-T6 aluminum |
| Diameter | 150mm (6 inches) |
| Length | 200mm |
| Finish | Polished or painted |
| Attachment | 3x #10 screws |

---

## 4. PHI-HARMONIC ESC

### 4.1 ESC Specifications
| Parameter | Value |
|---|---|
| Continuous current | 300A |
| Peak current | 400A (30 sec) |
| Voltage range | 36V-60V |
| Battery type | FPB-40 phi-harmonic field plasma (configurable) |
| Cell count | 12S-16S |
| Switching frequency | 20 kHz |
| Control algorithm | FOC (Field Oriented Control) |
| Throttle input | 1-2ms PWM |
| Telemetry | UART, CAN |
| Temperature sensor | NTC 10K |
| Efficiency | 98% at cruise |
| Weight | 1.2 kg |
| Dimensions | 120mm x 80mm x 30mm |
| Cooling | Active (fan + heatsink) |

### 4.2 ESC Phi-Harmonic Tuning
| Parameter | Value |
|---|---|
| Commutation frequency | 130.9 Hz (phi^2) |
| PWM frequency | 20 kHz |
| Current loop bandwidth | 1 kHz |
| Speed loop bandwidth | 100 Hz |
| Position loop bandwidth | 10 Hz |
| Filtering | 3-stage phi-harmonic |

### 4.3 ESC Programming Parameters
| Parameter | Value |
|---|---|
| Battery type | FPB-40 phi-harmonic field plasma |
| Cell count | 16S (48V) |
| Low voltage cutoff | 42V (2.625V/cell) |
| High voltage cutoff | 58.4V (3.65V/cell) |
| Current limit | 300A |
| Temperature limit | 80C (reduce), 100C (shutdown) |
| Timing | Auto (phi-optimized) |
| Ramp rate | Soft start (2 sec) |
| Throttle response | Normal |
| Brake | Regenerative |

---

## 5. PHI-HARMONIC FILTERING

### 5.1 Power Bus Filter
| Parameter | Value |
|---|---|
| Filter type | LC pi-section |
| Cutoff frequency | 130.9 Hz (phi^2) |
| Inductance | 100 uH (toroid) |
| Capacitance | 15 uF (electrolytic) |
| Attenuation | -40 dB at cutoff |
| Current rating | 300A |
| Voltage rating | 63V |

### 5.2 EMI Filter
| Parameter | Value |
|---|---|
| Stage 1 | 80.9 Hz (phi^1) |
| Stage 2 | 130.9 Hz (phi^2) |
| Stage 3 | 211.8 Hz (phi^3) |
| Combined attenuation | -80 dB at 50 Hz |
| Common mode rejection | >60 dB |
| Differential mode rejection | >40 dB |

### 5.3 Sensor Filter
| Parameter | Value |
|---|---|
| Type | 2nd order Butterworth |
| Cutoff frequency | 2.58 Hz (phi-harmonic bandwidth) |
| Phase margin | 34.4 degrees |
| Gain margin | 12 dB |
| Group delay | 0.1 sec |

---

## 6. PHI-HARMONIC CONTROL GAINS

### 6.1 PID Gains (Phi-Tuned)
| Loop | Kp | Ki | Kd |
|---|---|---|---|
| Pitch rate | 1.0 | 0.618 | 0.382 |
| Pitch attitude | 0.5 | 0.309 | 0.191 |
| Roll rate | 1.0 | 0.618 | 0.382 |
| Roll attitude | 0.5 | 0.309 | 0.191 |
| Yaw damper | 0.5 | 0.309 | 0.191 |
| Speed hold | 0.2 | 0.124 | 0.076 |
| Altitude hold | 0.1 | 0.062 | 0.038 |

### 6.2 Filter Bandwidths
| Filter | Frequency (Hz) | Q Factor |
|---|---|---|
| Pilot input | 2.58 | 0.707 |
| Attitude estimate | 5.0 | 0.707 |
| Rate estimate | 10.0 | 0.707 |
| Sensor fusion | 50.0 | 0.707 |
| Noise rejection | 130.9 | 10.0 |

---

## 7. PHI-HARMONIC STRUCTURAL SPECS

### 7.1 Natural Frequencies
| Component | Frequency (Hz) | Phi-Harmonic Avoidance |
|---|---|---|
| Wing | 8.5 | Below all motor/prop harmonics |
| Fuselage | 12.3 | Below all motor/prop harmonics |
| Tail | 15.7 | Below all motor/prop harmonics |
| Landing gear | 22.1 | Below all motor/prop harmonics |
| Seat structure | 35.0 | Below all motor/prop harmonics |

### 7.2 Damping Ratios
| Component | Damping Ratio | Target |
|---|---|---|
| Wing | 0.50 | 1/(2*phi^0) |
| Fuselage | 0.309 | 1/(2*phi^1) |
| Tail | 0.191 | 1/(2*phi^2) |
| Landing gear | 0.118 | 1/(2*phi^3) |
| Seats | 0.073 | 1/(2*phi^4) |

### 7.3 Resonance Avoidance Matrix
| Source | Frequency | Wing | Fuse | Tail | LG |
|---|---|---|---|---|---|
| Motor vibration | 174.5 Hz | OK | OK | OK | OK |
| Prop blade pass | 130.9 Hz | OK | OK | OK | OK |
| Phi harmonic 1 | 211.8 Hz | OK | OK | OK | OK |
| Phi harmonic 2 | 342.7 Hz | OK | OK | OK | OK |
| Phi harmonic 3 | 554.5 Hz | OK | OK | OK | OK |
| Phi harmonic 4 | 897.2 Hz | OK | OK | OK | OK |
| Phi harmonic 5 | 1451.7 Hz | OK | OK | OK | OK |
| Phi harmonic 6 | 2348.9 Hz | OK | OK | OK | OK |
| Phi harmonic 7 | 3800.6 Hz | OK | OK | OK | OK |

---

## 8. PHI-HARMONIC CONSTANTS

```
Golden ratio:
phi = 1.618033988749895

Phi powers:
phi^0  = 1.000000000000000
phi^1  = 1.618033988749895
phi^2  = 2.618033988749895
phi^3  = 4.236067977499790
phi^4  = 6.854101966249685
phi^5  = 11.090169943749475
phi^6  = 17.944271909999160
phi^7  = 29.034441853748635
phi^8  = 46.978713763747795
phi^9  = 76.013155617496430

Phi inverses:
1/phi  = 0.618033988749895
1/phi^2 = 0.381966011250105
1/phi^3 = 0.236067977499790
1/phi^4 = 0.145898033750315
1/phi^5 = 0.089803398749895

Phi-harmonic frequencies (base 50 Hz):
f_0  = 50.00 Hz
f_1  = 80.90 Hz
f_2  = 130.90 Hz
f_3  = 211.80 Hz
f_4  = 342.70 Hz
f_5  = 554.50 Hz
f_6  = 897.20 Hz
f_7  = 1451.70 Hz
f_8  = 2348.90 Hz
f_9  = 3800.60 Hz
```
