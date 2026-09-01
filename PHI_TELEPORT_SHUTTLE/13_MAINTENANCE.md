# Maintenance — Coil Inspection, Battery Service, and Fold-Node Calibration

## 1. Maintenance Philosophy

The teleport shuttle requires specialized maintenance due to its fold technology. Maintenance is organized into three tiers:

| Tier | Scope | Performed by | Interval |
|------|-------|-------------|----------|
| Tier 1 | Pre-flight, post-flight checks | Pilot / crew | Every flight |
| Tier 2 | Scheduled maintenance | PHI technician | Per schedule |
| Tier 3 | Major overhaul | PHI engineering | Per schedule |

## 2. Tier 1 — Pre-Flight / Post-Flight Checks

### 2.1 Pre-Flight Checklist

```
Pre-flight checklist (15 minutes):
  □ Visual inspection (hull, windows, exits)
  □ Fold coil status (temperature, integrity)
  □ Battery status (charge level, temperature)
  □ Navigation system (GPS lock, fold node map)
  □ Communication system (radio check, quantum link)
  □ Life support (oxygen, temperature, pressure)
  □ Safety systems (fold abort, emergency beacon)
  □ Fold cocoon (deployment test)
  □ Payload (clamped, secure)
  □ Cabin (clean, clear, exits unobstructed)
  □ Fold node scan (target location)
  □ Fold clearance (ground control)
```

### 2.2 Post-Flight Checklist

```
Post-flight checklist (10 minutes):
  □ Fold status (completed, no anomalies)
  □ Fold coil status (temperature, integrity)
  □ Battery status (charge level, temperature)
  □ Navigation system (arrival accuracy)
  □ Communication system (log transmitted)
  □ Life support (consumables level)
  □ Safety systems (status OK)
  □ Fold cocoon (retracted, clean)
  □ Payload (unloaded, condition OK)
  □ Cabin (clean, clear, exits unobstructed)
  □ Data log (downloaded, reviewed)
  □ Maintenance log (updated)
```

## 3. Tier 2 — Scheduled Maintenance

### 3.1 Every 50 Folds

| Task | Duration | Tools required |
|------|----------|----------------|
| Fold coil visual inspection | 30 min | Flashlight, mirror |
| Fold coil temperature check | 15 min | IR thermometer |
| Fold coil mount torque check | 30 min | Torque wrench |
| Battery charge capacity test | 1 hour | PHI diagnostic tool |
| Battery plasma density check | 30 min | PHI diagnostic tool |
| Navigation system calibration | 1 hour | PHI calibration tool |
| Communication system test | 30 min | Radio tester |
| Life support consumables check | 15 min | Visual inspection |
| Safety system function test | 30 min | PHI diagnostic tool |
| Fold cocoon deployment test | 15 min | Manual |
| **Total** | **4.5 hours** | — |

### 3.2 Every 200 Folds

| Task | Duration | Tools required |
|------|----------|----------------|
| All 50-fold tasks | 4.5 hours | As above |
| Fold coil deep inspection | 2 hours | Coil inspection tool |
| Fold coil superconductor test | 1 hour | PHI diagnostic tool |
| Fold coil former inspection | 1 hour | Visual inspection |
| Battery seal inspection | 30 min | Visual inspection |
| Battery capacitor test | 1 hour | PHI diagnostic tool |
| Navigation fold radar test | 1 hour | PHI diagnostic tool |
| Communication quantum link test | 1 hour | PHI diagnostic tool |
| Hull structural inspection | 2 hours | Strain gauge reader |
| Fold-node frame inspection | 1 hour | Visual inspection |
| **Total** | **14 hours** | — |

### 3.3 Every 1,000 Folds

| Task | Duration | Tools required |
|------|----------|----------------|
| All 200-fold tasks | 14 hours | As above |
| Fold coil replacement | 8 hours | Coil replacement tool |
| Battery plasma refresh | 4 hours | PHI service tool |
| Battery capacitor replacement | 2 hours | PHI service tool |
| Navigation system overhaul | 4 hours | PHI overhaul tool |
| Communication system overhaul | 4 hours | PHI overhaul tool |
| Life support system overhaul | 4 hours | PHI overhaul tool |
| Safety system certification | 4 hours | PHI certification tool |
| Hull coating renewal | 8 hours | Coating equipment |
| Fold cocoon reline | 4 hours | Cocoon service tool |
| **Total** | **56 hours** | — |

## 4. Tier 3 — Major Overhaul

### 4.1 Every 5,000 Folds

| Task | Duration | Tools required |
|------|----------|----------------|
| Complete vehicle disassembly | 40 hours | Disassembly tool set |
| Hull structural inspection (NDT) | 20 hours | NDT equipment |
| Hull repair/replacement | 40 hours | Composite repair kit |
| Fold-node frame replacement | 16 hours | Frame replacement tool |
| Structural strut replacement | 8 hours | Strut replacement tool |
| All fold coils replacement | 16 hours | Coil replacement tool |
| All batteries replacement | 8 hours | Battery replacement tool |
| All electronics overhaul | 24 hours | Electronics tool set |
| All wiring harness replacement | 16 hours | Wiring tool set |
| Complete reassembly | 40 hours | Assembly tool set |
| Complete system test | 24 hours | PHI test suite |
| Flight test | 8 hours | Flight test protocol |
| **Total** | **264 hours** | — |

## 5. Fold-Node Calibration

### 5.1 Purpose

Fold-node calibration ensures that the fold coils generate fold nodes at the correct locations with the correct characteristics. Calibration is required:
- After every 50 folds
- After any fold coil replacement
- After any structural modification
- After any navigation system change
- After any transportation of the vehicle

### 5.2 Calibration Procedure

```
Fold-node calibration procedure (2 hours):
  1. Set up calibration targets (3 at known GPS positions)
  2. Power up fold coils to idle
  3. Run calibration sequence (automatic):
     a. Generate fold node at vehicle center
     b. Measure fold node position (±0.01 mm)
     c. Measure fold node strength (±0.1%)
     d. Measure fold node orientation (±0.1°)
     e. Adjust coil phases to correct errors
     f. Repeat until all parameters within tolerance
  4. Generate remote fold node at each calibration target
  5. Measure remote fold node position (±0.1 m)
  6. Measure remote fold node strength (±1%)
  7. Adjust coil phases to correct errors
  8. Verify fold bridge formation at each target
  9. Log calibration data
  10. Generate calibration certificate
```

### 5.3 Calibration Tolerances

| Parameter | Tolerance | Consequence of exceedance |
|-----------|-----------|--------------------------|
| Primary fold node position | ±0.01 mm | Fold bridge misalignment |
| Primary fold node strength | ±0.1% | Fold instability |
| Primary fold node orientation | ±0.1° | Fold bridge misalignment |
| Remote fold node position | ±0.1 m | Inaccurate arrival |
| Remote fold node strength | ±1% | Fold instability |
| Fold bridge integrity | > 95% | Fold abort |

### 5.4 Calibration Equipment

| Equipment | Purpose | Calibration interval |
|-----------|---------|---------------------|
| PHI calibration tool | Fold node measurement | Annual |
| GPS reference receiver | Position reference | Annual |
| Fold field probe | Field strength measurement | Annual |
| Fold frequency analyzer | Frequency measurement | Annual |
| Fold coherence sensor | Metric coherence measurement | Annual |

## 6. Battery Service

### 6.1 Battery Service Schedule

| Interval | Task | Duration |
|----------|------|----------|
| Every 50 folds | Charge capacity test | 1 hour |
| Every 50 folds | Plasma density check | 30 min |
| Every 200 folds | Seal inspection | 30 min |
| Every 200 folds | Capacitor test | 1 hour |
| Every 1,000 folds | Plasma refresh | 4 hours |
| Every 1,000 folds | Capacitor replacement | 2 hours |
| Every 5,000 folds | Complete replacement | 8 hours |

### 6.2 Battery Service Procedures

**Plasma density check:**
```
1. Discharge battery to 50%
2. Measure plasma density ( PHI diagnostic tool)
3. Compare to specification (1.0 ± 0.05 × 10¹⁸ m⁻³)
4. If out of tolerance, schedule plasma refresh
5. Recharge battery to 100%
```

**Plasma refresh:**
```
1. Discharge battery to 0%
2. Remove plasma containment field
3. Inject fresh plasma (noble gas mix)
4. Re-establish phi-harmonic confinement field
5. Charge battery to 100%
6. Verify plasma density (1.0 ± 0.05 × 10¹⁸ m⁻³)
7. Verify confinement field stability
```

**Capacitor replacement:**
```
1. Discharge battery to 0%
2. Verify zero voltage (safety check)
3. Remove old capacitors (8 per unit)
4. Install new capacitors
5. Verify capacitor installation (visual + electrical)
6. Charge battery to 100%
7. Verify capacity (100 ± 2 kWh)
```

## 7. Coil Inspection

### 7.1 Visual Inspection

```
Fold coil visual inspection:
  □ Coil former (cracks, chips, discoloration)
  □ Coil windings (loose wires, corrosion)
  □ Coil connections (tight, clean, corrosion-free)
  □ Coil mount (tight, aligned, no damage)
  □ Coil cooling (lines clear, no leaks)
  □ Coil field probes (clean, aligned)
```

### 7.2 Electrical Inspection

```
Fold coil electrical inspection:
  □ Coil resistance (< 0.1 Ω)
  □ Coil inductance (2.4 ± 0.1 mH)
  □ Coil resonant frequency (161.8 ± 0.5 kHz)
  □ Coil current capacity (5,000 A)
  □ Coil insulation resistance (> 100 MΩ)
  □ Coil quench detection (functional)
```

### 7.3 Superconductor Inspection

```
Fold coil superconductor inspection:
  □ YBCO tape integrity (visual)
  □ YBCO critical current (> 500 A at 77K)
  □ YBCO cooling (liquid nitrogen level, flow)
  □ YBCO joints (resistance < 1 nΩ)
  □ YBCO insulation (integrity, no damage)
```

## 8. Documentation

### 8.1 Maintenance Log

All maintenance must be documented in the maintenance log:

```
Maintenance log entry format:
  Date: YYYY-MM-DD
  Technician: [name]
  Vehicle: [call sign]
  Fold count: [number]
  Tier: [1/2/3]
  Tasks performed: [list]
  Parts replaced: [list]
  Anomalies found: [list]
  Corrective actions: [list]
  Next maintenance: [date/fold count]
  Signature: [technician]
```

### 8.2 Maintenance Records

Maintenance records must be retained for:
- Life of the vehicle + 10 years
- All Tier 2 and Tier 3 maintenance
- All fold abort events
- All emergency events
- All modifications

### 8.3 Maintenance Training

| Role | Training required | Certification |
|------|------------------|---------------|
| Pilot | Tier 1 checks | PHI pilot license |
| Crew | Tier 1 checks | PHI crew certificate |
| PHI technician | Tier 2 maintenance | PHI technician license |
| PHI engineer | Tier 3 overhaul | PHI engineer license |
| PHI inspector | Inspection and certification | PHI inspector license |
