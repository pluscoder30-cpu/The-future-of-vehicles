# Propulsion System — Phi-Harmonic Temporal Coils

## 1. System Overview

The time shuttle has no conventional propulsion system. It does not move through space — it folds time. The "propulsion system" is therefore the **temporal coil array** that creates the temporal fold bridge between the vehicle's current time and the target time.

## 2. Temporal Coil Architecture

### 2.1 Array Layout

The temporal coil array consists of **8 phi-harmonic coils** arranged in a bi-toroidal configuration around the vehicle hull:

```
Side view:

         C01    C02
        / | \  / | \
      C08  | C03  |  C03
      /    |/   \|    \
    C07 ---+-- TC --+--- C03
      \    |\   /|    /
      C06  | C04  |  C04
        \ | /  \ | /
         C05    C04

TC = Temporal center (fold node location)
```

### 2.2 Individual Coil Specifications

| Parameter | Value |
|-----------|-------|
| Coil type | Phi-harmonic standing wave driver |
| Inner diameter | 0.6 m |
| Outer diameter | 0.9 m |
| Length | 0.4 m |
| Number of turns | 1,618 (≈ 1000 × φ) |
| Wire material | YBCO superconductor (77K operation) |
| Maximum current | 6,000 A |
| Inductance | 3.6 mH |
| Resonant frequency (1st harmonic) | 90.9 kHz |
| Resonant frequency (2nd harmonic) | 147.1 kHz |
| Mass | 22 kg per coil |
| Total array mass | 176 kg |

### 2.3 Phi-Harmonic Drive

Each coil is driven at phi-harmonic frequencies:

```
Drive signal: V(t) = Σ Aₙ · sin(ω₀ · φⁿ · t + φₙ)
```

The first five harmonics:
- n=0: 90.9 kHz (fundamental — temporal fold initiation)
- n=1: 147.1 kHz (φ-harmonic — temporal fold formation)
- n=2: 237.9 kHz (φ²-harmonic — temporal fold stabilization)
- n=3: 385.0 kHz (φ³-harmonic — temporal fold bridge)
- n=4: 622.9 kHz (φ⁴-harmonic — temporal fold transit)

## 3. Temporal Fold Generation

### 3.1 Temporal Fold Initiation

The temporal coils project phi-harmonic standing waves into the temporal metric. This creates a temporal perturbation:

```
δg_tt = ε × φⁿ × f_φ(t, x)
```

where ε is the perturbation amplitude, n is the harmonic index, and f_φ(t, x) is the phi-harmonic envelope.

### 3.2 Temporal Fold Node Formation

When the perturbation amplitude exceeds the threshold:

```
ε × φⁿ > 1/φ = 0.618
```

Temporal fold nodes form at:
1. **Vehicle time**: The vehicle's current time coordinate
2. **Target time**: The target time coordinate (±24 hours)

### 3.3 Temporal Fold Bridge

The two temporal fold nodes are connected by a **temporal fold bridge** — a region where the time metric is folded so that the two temporal points are coincident. In the folded metric, the temporal distance between the nodes is zero.

The temporal fold bridge formation time is:

```
τ_bridge = Δt / (c · φ⁻¹) ≈ Δt / (0.618c)
```

For Δt = 24 hours:

```
τ_bridge ≈ 86,400 / (0.618 × 3×10⁸) ≈ 0.47 μs
```

### 3.4 Temporal Fold Transit

The vehicle traverses the temporal fold bridge. In the folded metric, this is a zero-temporal-distance transition. In the external (unfolded) metric, the vehicle disappears at one time and reappears at the other.

The transit time in the external metric appears to be:

```
v_transit = Δt / τ_transit ≈ Δt / 1.2 sec
```

For Δt = 24 hours:

```
v_transit ≈ 86,400 / 1.2 = 72,000 sec/sec ≈ 72,000× temporal velocity
```

But this is not the vehicle moving through time — it is the metric folding. The vehicle itself has zero temporal velocity in the folded metric.

### 3.5 Temporal Fold Collapse

After the vehicle arrives at the target time, the temporal fold bridge collapses. The temporal fold amplitude decreases:

```
λ(t) = λ_max · exp(-t/τ_collapse)
```

The temporal metric returns to flat:

```
g'_tt → g_tt as t → ∞
```

The collapse is controlled to prevent energy release that could damage the vehicle or surroundings.

## 4. Temporal Coil Control System

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

### 4.2 Temporal Fold Controller

The temporal fold controller manages:
- Temporal fold node position (vehicle time, target time)
- Temporal fold bridge integrity (no temporal breaks)
- Temporal fold amplitude (stability)
- Temporal fold transit (vehicle movement through fold)
- Causal consistency (paradox prevention)

### 4.3 Navigation Integration

The temporal fold controller interfaces with the navigation system:
- Receives target time and temporal approach vector
- Adjusts temporal fold geometry for navigation
- Provides temporal status to navigation display
- Responds to navigation commands (course corrections, abort)

## 5. Performance Envelope

| Parameter | Minimum | Nominal | Maximum |
|-----------|---------|---------|---------|
| Temporal fold distance | 1 second | 12 hours | 24 hours |
| Temporal fold accuracy | ±0.1 sec | ±1 sec | ±10 sec |
| Transit time | 0.3 sec | 1.2 sec | 3.0 sec |
| Fold duration | 30 sec | 60 sec | 120 sec |
| Energy per fold | 0.1 kWh | 1.15 kWh | 5 kWh |
