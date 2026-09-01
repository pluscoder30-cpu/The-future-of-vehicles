# Propulsion System — Phi-Harmonic Warp Drive Coils

## 1. System Overview

The FTL shuttle uses a **warp drive** — a system of phi-harmonic coils that create a warp bubble around the vehicle. The warp bubble contracts spacetime ahead and expands it behind, propelling the vehicle at superluminal speed.

## 2. Warp Coil Architecture

### 2.1 Array Layout

The warp drive uses **8 phi-harmonic coils** arranged in a toroidal configuration around the vehicle:

```
Top view:

         C01
        / | \
      C08  |  C02
      /    |    \
    C07 ---+--- C03
      \    |    /
      C06  |  C04
        \ | /
         C05

+ = Warp center (bubble center)
```

### 2.2 Individual Coil Specifications

| Parameter | Value |
|-----------|-------|
| Coil type | Phi-harmonic standing wave driver |
| Inner diameter | 0.8 m |
| Outer diameter | 1.2 m |
| Length | 0.5 m |
| Number of turns | 1,618 (≈ 1000 × φ) |
| Wire material | YBCO superconductor (77K operation) |
| Maximum current | 8,000 A |
| Inductance | 4.8 mH |
| Resonant frequency (1st harmonic) | 80.9 kHz |
| Resonant frequency (2nd harmonic) | 130.9 kHz |
| Mass | 35 kg per coil |
| Total array mass | 280 kg |

### 2.3 Phi-Harmonic Drive

Each coil is driven at phi-harmonic frequencies:

```
Drive signal: V(t) = Σ Aₙ · sin(ω₀ · φⁿ · t + φₙ)
```

The first five harmonics:
- n=0: 80.9 kHz (fundamental — bubble initiation)
- n=1: 130.9 kHz (φ-harmonic — bubble formation)
- n=2: 211.8 kHz (φ²-harmonic — bubble stabilization)
- n=3: 342.7 kHz (φ³-harmonic — bubble acceleration)
- n=4: 554.5 kHz (φ⁴-harmonic — bubble cruise)

## 3. Warp Bubble Generation

### 3.1 Bubble Initiation

The warp coils generate phi-harmonic standing waves that polarize the quantum vacuum, creating virtual particle-antiparticle pairs that contribute to the warp energy density. The vacuum polarization creates a metric perturbation:

```
δg_μν = ε × φⁿ × f(r, t)
```

where ε is the perturbation amplitude, n is the harmonic index, and f(r, t) is the phi-harmonic envelope.

### 3.2 Bubble Formation

As the perturbation grows, it reaches the threshold for warp bubble formation:

```
δg_μν > δ_threshold = 0.618 (= 1/φ)
```

At this point, the warp bubble spontaneously forms around the vehicle. The bubble has:
- Flat interior (Minkowski metric)
- Warped wall (phi-harmonic metric)
- Flat exterior (Minkowski metric)

### 3.3 Bubble Acceleration

The warp bubble accelerates by asymmetrically driving the coils:
- Forward coils: Higher amplitude (contract spacetime ahead)
- Aft coils: Lower amplitude (expand spacetime behind)

The acceleration is:

```
a_warp = (c² / R) × (ε_forward - ε_aft) × φⁿ
```

For ε_forward = 0.3, ε_aft = 0.1, R = 2.5 m, n = 5:

```
a_warp = (9 × 10¹⁶ / 2.5) × 0.2 × 11.09
        = 3.6 × 10¹⁶ × 0.2 × 11.09
        = 7.98 × 10¹⁶ m/s²
```

This acceleration is achieved in the warp bubble frame. In the external frame, the bubble propagates at superluminal speed without local acceleration of the vehicle.

### 3.4 Bubble Cruise

At cruise speed (10c), the warp coils maintain a steady-state warp bubble:

```
Cruise power: 40 MW sustained
Bubble radius: 2.5 m
Bubble wall thickness: 0.1 m
Interior tidal force: < 2g
Exterior metric distortion: 10c effective velocity
```

### 3.5 Bubble Deceleration

Deceleration is achieved by reversing the coil asymmetry:
- Forward coils: Lower amplitude (reduce contraction)
- Aft coils: Higher amplitude (reduce expansion)

The deceleration rate matches the acceleration rate.

### 3.6 Bubble Collapse

At the destination, the warp bubble is collapsed:

```
Bubble collapse sequence:
  Time 0 sec: Cut power to all coils
  Time 0.1 sec: Warp field begins decaying
  Time 1 sec: Warp field at 50%
  Time 5 sec: Warp field at 10%
  Time 15 sec: Warp field at 0% (metric flat)
```

Total collapse time: 15 seconds.

## 4. Warp Coil Control System

### 4.1 Phase-Lock Loop

Each coil has an independent phase-lock loop (PLL) locked to the master oscillator:

```
Error signal: e(t) = θ_ref(t) - θ_coil(t)
Control signal: u(t) = Kp · e(t) + Ki · ∫e(t)dt + Kd · de(t)/dt
```

PID gains (phi-harmonic tuned):
- Kp = 1.0
- Ki = 1/φ ≈ 0.618
- Kd = 1/φ² ≈ 0.382

### 4.2 Warp Bubble Controller

The warp bubble controller manages:
- Bubble radius (target: 2.5 m)
- Bubble wall thickness (target: 0.1 m)
- Bubble velocity (target: 10c)
- Interior tidal forces (limit: 2g)
- Bubble stability (monitor metric coherence)

### 4.3 Navigation Integration

The warp bubble controller interfaces with the navigation system:
- Receives target coordinates and approach vector
- Adjusts warp bubble geometry for navigation
- Provides warp status to navigation display
- Responds to navigation commands (course corrections, deceleration)

## 5. Performance Envelope

| Parameter | Minimum | Nominal | Maximum |
|-----------|---------|---------|---------|
| Warp speed | 1c | 10c | 10c |
| Cruise speed | 1c | 5c | 10c |
| Warp bubble radius | 2.0 m | 2.5 m | 3.0 m |
| Warp bubble wall | 0.05 m | 0.1 m | 0.2 m |
| Acceleration time | 10 sec | 30 sec | 60 sec |
| Deceleration time | 5 sec | 15 sec | 30 sec |
| Energy per light-year | 50 kWh | 100 kWh | 200 kWh |
