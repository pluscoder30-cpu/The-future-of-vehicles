# Temporal Mechanism — Dimension Folding Time Sequence

## 1. Overview

The temporal mechanism is the core system that enables matter translocation through temporal dimension folding. This document describes the complete fold-and-transport sequence in detail.

## 2. The Temporal Fold Process

### 2.1 Pre-Fold State

Before time folding, the vehicle exists in normal spacetime. The temporal metric is flat:

```
ds² = -c²dt² + dx² + dy² + dz²
```

The temporal distance between the vehicle and the target is Δt (measured in the flat metric).

### 2.2 Temporal Fold Initiation

The temporal coils project phi-harmonic standing waves into the temporal metric. This creates a perturbation:

```
g'_tt = g_tt + λ · τ(t, x)
```

The temporal fold amplitude λ increases over time as energy is pumped into the system:

```
λ(t) = λ_max · (1 - exp(-t/τ_tfold))
```

where τ_tfold = 1.0 second is the temporal fold time constant.

### 2.3 Temporal Fold Node Formation

At λ ≈ 0.618 (= 1/φ), the temporal metric admits a fold-compatible decomposition. Two temporal fold nodes form:

1. **Vehicle node**: At the vehicle's current time
2. **Target node**: At the target time (Δt hours in the past or future)

The temporal fold nodes are topological defects in the temporal metric — points where the curvature tensor has a non-trivial fundamental group:

```
π₁(R_μνρσ) ≠ 0
```

### 2.4 Temporal Fold Bridge

The two temporal fold nodes are connected by a **temporal fold bridge** — a region where the time metric is folded so that the two nodes are coincident. In the folded metric, the temporal distance between the nodes is zero:

```
ds'_fold = 0
```

In the external (unfolded) metric, the bridge has a physical temporal extent:

```
Δt_bridge = Δt · exp(-λ)
```

At λ = 1 (full fold):

```
Δt_bridge = Δt · exp(-1) ≈ 0.368Δt
```

At λ = φ (phi-fold):

```
Δt_bridge = Δt · exp(-φ) ≈ 0.208Δt
```

### 2.5 Temporal Fold Transit

The vehicle traverses the temporal fold bridge. In the folded metric, this is a zero-temporal-distance transition. In the external metric, the vehicle follows a geodesic through the folded temporal region.

The transit velocity in the external metric appears to be:

```
v_transit = Δt / τ_transit ≈ Δt / 1.2 sec
```

For Δt = 24 hours:

```
v_transit ≈ 86,400 / 1.2 = 72,000 sec/sec
```

But this is not the vehicle moving through time — it is the temporal metric folding. The vehicle itself has zero velocity in the folded metric.

### 2.6 Temporal Fold Collapse

After the vehicle arrives at the target time, the temporal fold bridge collapses. The temporal fold amplitude decreases:

```
λ(t) = λ_max · exp(-t/τ_collapse)
```

The temporal metric returns to flat:

```
g'_tt → g_tt as t → ∞
```

The collapse is controlled to prevent energy release that could damage the vehicle or surroundings.

## 3. Passenger Experience

### 3.1 During Temporal Fold Initiation

Passengers feel a mild pressure change (similar to an airplane cabin pressurizing) as the temporal coils power up. The pressure change is less than 5% of atmospheric pressure.

### 3.2 During Temporal Fold Transit

The transit is instantaneous from the passenger's perspective. There is no sensation of movement, acceleration, or time dilation. The passenger's experience is:

- Before: Vehicle at time T
- After: Vehicle at time T ± Δt
- During: No perceptible event (1.2 seconds of subjective time)

### 3.3 Time Dilation Effects

The temporal fold does not create time dilation effects inside the vehicle. Time passes normally for passengers during the fold. The fold is a geometric manipulation of the temporal metric, not a relativistic time dilation.

### 3.4 Post-Fold

After temporal fold collapse, passengers may experience:
- Mild disorientation (vestibular system recalibrating)
- Slight warmth (residual temporal energy dissipation)
- Temporary tinnitus (high-frequency temporal signature)
- Déjà vu (memory overlap with target time, if backward fold)

These symptoms typically resolve within 60 seconds.

## 4. Temporal Geometry

### 4.1 The Temporal Fold Manifold

The temporal fold creates a temporary manifold M_tfold that connects two regions of normal spacetime. The topology of M_tfold is:

```
M_tfold = R³ × T¹ × [0, 1]
```

where:
- R³ is the spatial dimensions
- T¹ is the temporal fold dimension (compact, radius = 0 at fold nodes)
- [0, 1] is the fold parameter

### 4.2 Temporal Fold Boundary Conditions

The temporal fold manifold must satisfy boundary conditions at the fold nodes:

```
∂M_tfold / ∂t = 0 (at temporal fold nodes)
```

This ensures that the temporal fold field does not radiate energy away from the nodes, maintaining the fold structure.

### 4.3 Temporal Fold Stability

The temporal fold is stable because:
1. The phi-harmonic field structure creates a self-similar geometry at all temporal scales
2. The temporal fold nodes are topologically protected (they cannot be removed by smooth deformations)
3. The temporal fold bridge is maintained by the phi-harmonic drive, which continuously replenishes any energy lost to temporal metric radiation

## 5. Causal Consistency

### 5.1 The Novikov Self-Consistency Principle

The temporal fold enforces the Novikov self-consistency principle: events on the temporal fold are self-consistent. This means:
- The vehicle cannot change its own past (bootstrap paradox prevention)
- Any events caused by the temporal fold are part of the original timeline
- The fold does not create closed timelike curves (CTCs)

### 5.2 Causal Consistency Enforcement

The causal consistency system:
1. Checks for potential paradoxes before fold initiation
2. Monitors causal structure during fold transit
3. Aborts the fold if a paradox is detected
4. Enforces the Novikov principle (events on the fold are self-consistent)

### 5.3 Bootstrap Paradox Prevention

The vehicle cannot fold to a time before it was created. This is enforced by:
- Temporal boundary check (vehicle creation time is the earliest possible fold target)
- Causal consistency check (no events on the fold contradict the vehicle's existence)
- Automatic abort if bootstrap paradox is detected

## 6. Safety Considerations

### 6.1 Temporal Fold Abort

If the temporal fold becomes unstable at any point during the sequence, the temporal fold abort system activates:

```
Temporal fold abort sequence:
  1. Cut power to all coils (50 ms)
  2. Activate temporal fold quench (100 ms)
  3. Dissipate temporal fold energy to heat sinks (500 ms)
  4. Verify temporal metric return to flat (1 sec)
  5. Report status to crew
```

Total abort time: 1.65 seconds.

### 6.2 Temporal Fold Containment

The temporal fold is contained within the coil array. The temporal fold field decays exponentially outside the array:

```
B_tfold(r) = B₀ · exp(-r/λ_tfold)
```

where λ_tfold = 0.5 m is the temporal fold decay length. This ensures that:
- The temporal fold does not affect objects outside the vehicle
- The temporal fold does not interact with nearby structures
- The temporal fold is localized to the vehicle and its immediate surroundings

### 6.3 Post-Fold Temporal Relaxation

After temporal fold collapse, the temporal metric takes approximately 60 seconds to fully relax to flat. During this time, the vehicle is in a "temporal shadow" — a region where the temporal metric is slightly perturbed.

The temporal shadow has no observable physical effects, but it is detectable by sensitive instruments. The vehicle should remain stationary during the relaxation period to avoid temporal drag effects.
