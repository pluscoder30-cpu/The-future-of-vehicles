# PHI PLANT DRONE — PHI-HARMONIC SPECS

## Phi Tuning Parameters for All Systems

---

## PHI CONSTANT

```
PHI (φ) = 1.618033988749894

Used throughout all drone systems:
├── Structural ratios
├── Frequency sequences
├── Motor timing
├── Sensor placement
├── Control loop rates
└── Weight distribution
```

---

## STRUCTURAL PHI RATIOS

| Component | Dimension | Phi Relationship |
|-----------|-----------|-----------------|
| Overall width | 500mm | Base |
| Overall height | 309mm | 500/φ |
| Body width | 200mm | 500/φ^1.3 |
| Body height | 124mm | 200/φ |
| Arm length | 180mm | 500/φ^1.6 |
| Arm width | 111mm | 180/φ |
| Motor mount | 70mm | 180/φ^1.4 |
| Motor holes | 43mm | 70/phi |

---

## PHI-HARMONIC FREQUENCIES

| # | Frequency | Hz | Property |
|---|-----------|----|----------|
| 1 | 432 Hz | 432.0 | Root growth |
| 2 | 528 Hz | 528.0 | Cell division |
| 3 | 639 Hz | 639.0 | Nutrient uptake |

### Phi-Harmonic Overtones

| Base | × φ | × φ² |
|------|-----|------|
| 432 Hz | 699 Hz | 1131 Hz |
| 528 Hz | 854 Hz | 1382 Hz |
| 639 Hz | 1034 Hz | 1673 Hz |

---

## MOTOR TIMING

```
PHI-HARMONIC MOTOR SETTINGS:
═══════════════════════════════════════════════════════════════

  Standard PWM: 400 Hz
  PHI PWM: 400 × φ = 647 Hz

  Motor RPM at hover:
  Standard: 2500 RPM
  PHI: 2500 / φ = 1545 RPM (quieter, more efficient)
```

---

## FLIGHT CONTROLLER

```
PID CONTROLLER (PHI-ADJUSTED):
═══════════════════════════════════════════════════════════════

  Loop rate: 1000 / φ = 618 Hz

  PID Gains:
  ┌──────────────────────────────────────┐
  │  Roll:  P=5.0  I=0.9×φ=1.5  D=2.5/φ=1.5 │
  │  Pitch: P=5.0  I=0.9×φ=1.5  D=2.5/φ=1.5 │
  │  Yaw:   P=7.0  I=1.2×φ=1.9  D=3.5/φ=2.2 │
  └──────────────────────────────────────┘
```

---

## SENSOR PLACEMENT

| Sensor | Position | Angle from Center |
|--------|----------|-------------------|
| MPU6050 | Center | 0° |
| BMP280 | Bottom | 90° |
| GPS | Top mast | 0° |
| Soil moisture 1 | Bottom front | 45° |
| Soil moisture 2 | Bottom rear | 225° |
| BH1750 | Top | 180° |

---

## COMPLETE PHI PARAMETER TABLE

| System | Parameter | Standard | PHI-Harmonic |
|--------|-----------|----------|--------------|
| Frame | W/H ratio | varies | φ = 1.618 |
| Motors | PWM freq | 400 Hz | 647 Hz |
| Motors | Hover RPM | 2500 | 1545 |
| PID | Loop rate | 1000 Hz | 618 Hz |
| PID | I gain | Ki | Ki × φ |
| PID | D gain | Kd | Kd / φ |
| Sensors | Placement | random | φ-angles |
| Frequency | Base | 432 Hz | 432 Hz |
| Frequency | Overtone | none | × φ |
| Telemetry | Interval | 100ms | 162ms |
| Battery | Charge rate | 0.5C | 0.5C/φ |
| CG | Position | 50% | 1/φ = 61.8% |
