# Navigation System — Targeting, Fold-Node Mapping, and Approach

## 1. System Overview

The navigation system is responsible for:
1. Selecting the target location
2. Mapping fold nodes at the target
3. Aligning the fold bridge
4. Monitoring fold integrity during transit
5. Verifying arrival accuracy

## 2. Target Selection

### 2.1 Target Input Methods

| Method | Interface | Accuracy |
|--------|-----------|----------|
| GPS coordinates | Touchscreen / voice | ±1 m |
| Address / landmark | Voice recognition | ±5 m |
| Visual target | Camera + image match | ±0.3 m |
| Fold beacon | Radio link to target beacon | ±0.1 m |
| Manual entry | Coordinate keypad | ±1 m |

### 2.2 Target Validation

Before fold initiation, the navigation system validates the target:

```
Target validation checklist:
  □ Target within operational range (0 m - 15,000 km)
  □ Target not within event horizon of massive object
  □ Target not in vacuum (requires medium for fold node)
  □ Target free of obstacles (minimum 3m × 3m × 3m clear volume)
  □ Target fold node density sufficient (τ_fold > 0.618)
  □ Target not in restricted airspace / fold zone
  □ Target fold signature not already present (no fold conflict)
```

If any check fails, the navigation system reports the reason and suggests alternative targets.

### 2.3 Fold Node Mapping

The navigation system scans the target location for fold nodes using a **fold radar** — a low-power phi-harmonic transmitter that probes the local spatial curvature:

```
Fold radar scan:
  Frequency: 100 kHz (fundamental)
  Power: 100 W
  Range: 100 m
  Resolution: 0.1 m
  Scan time: 2 seconds
```

The fold radar returns a map of fold node locations, strengths, and orientations. The navigation system selects the optimal fold node based on:
- Distance from target center
- Fold node strength (higher is better)
- Fold node orientation (aligned with vehicle fold axis)
- Fold node stability (steady vs. fluctuating)

## 3. Fold Bridge Alignment

### 3.1 Alignment Procedure

Once the target fold node is selected, the navigation system aligns the fold bridge:

```
Alignment sequence:
  1. Calculate fold axis (vehicle fold node → target fold node)
  2. Adjust coil phases to align fold field with fold axis
  3. Verify fold bridge endpoints are within tolerance
  4. Lock fold bridge alignment
  5. Confirm ready for fold initiation
```

### 3.2 Alignment Tolerance

| Parameter | Tolerance | Consequence of exceedance |
|-----------|-----------|--------------------------|
| Fold axis angle | ±0.5° | Fold bridge misalignment |
| Fold node position | ±0.3 m | Inaccurate arrival |
| Fold field amplitude | ±2% | Fold instability |
| Fold frequency | ±0.01% | Fold coherence loss |

### 3.3 Continuous Alignment

During fold transit, the navigation system continuously monitors fold bridge alignment and adjusts coil phases in real-time. The alignment correction bandwidth is 10 kHz — fast enough to compensate for:
- Vehicle motion (up to 100 m/s)
- Target motion (up to 50 m/s)
- Gravitational perturbations (up to 0.1 m/s²)
- Fold field fluctuations (up to 1% per second)

## 4. Fold Transit Monitoring

### 4.1 Transit Sensors

| Sensor | Measurement | Sample rate |
|--------|-------------|-------------|
| Fold field probe | Fold amplitude, phase | 100 kHz |
| Metric coherence sensor | Curvature deviation | 10 kHz |
| Inertial measurement unit | Acceleration, rotation | 1 kHz |
| GPS receiver | Position, velocity | 10 Hz |
| Fold radar | Fold bridge integrity | 1 kHz |

### 4.2 Transit Monitoring

During the 0.8-second fold transit, the navigation system monitors:
- Fold bridge integrity (no breaks or distortions)
- Vehicle position within fold bridge
- Fold field amplitude stability
- Fold frequency stability

If any parameter goes out of tolerance, the navigation system can:
- Adjust coil phases to correct the error (if within capability)
- Abort the fold and return the vehicle to the starting point (if error is large)
- Report the issue to the crew (if error is marginal)

### 4.3 Arrival Verification

After fold transit, the navigation system verifies:
- Vehicle position matches target position (within ±0.3 m)
- Vehicle orientation is correct
- Fold field has fully collapsed
- Metric is within 0.01% of flat
- No residual fold signature at starting point

## 5. Navigation Display

### 5.1 Main Display

The navigation display shows:
- Current position (GPS coordinates)
- Target position (GPS coordinates)
- Distance to target
- Fold node map (current location and target)
- Fold bridge status (forming, stable, collapsing)
- Transit progress (during fold transit)
- Arrival accuracy (after fold transit)

### 5.2 Fold Status Indicators

```
Fold Status: ● READY
Fold Node:   ● LOCKED
Fold Bridge: ● STABLE
Fold Field:  ● NOMINAL
Transit:     ● COMPLETE
Accuracy:    ● ±0.2 m (within tolerance)
```

### 5.3 Warning Indicators

```
⚠ FOLD NODE DRIFT — Recalculating...
⚠ FOLD BRIDGE INTEGRITY — 98.7% (minimum 95%)
⚠ METRIC COHERENCE — 0.3% deviation (maximum 0.1%)
⚠ FOLD COLLAPSE DELAYED — Extended relaxation
```

## 6. Performance

| Parameter | Value |
|-----------|-------|
| Target acquisition time | 5 sec (GPS) / 10 sec (visual) |
| Fold node scan time | 2 sec |
| Alignment time | 3 sec |
| Total pre-fold time | 10-15 sec |
| Transit monitoring rate | 100 kHz |
| Arrival accuracy (nominal) | ±0.3 m |
| Arrival accuracy (maximum range) | ±3 m |
| Navigation power consumption | 5 kW peak, 2 kW sustained |
