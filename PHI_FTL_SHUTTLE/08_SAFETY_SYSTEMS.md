# Safety Systems — Bubble Containment, Abort Logic, and Shielding

## 1. Safety Philosophy

The FTL shuttle operates in a regime where superluminal travel creates unique hazards. The safety system is designed around three principles:

1. **Fail-safe**: Any single failure results in a safe state (warp abort, vehicle stationary)
2. **Fail-operational**: Critical systems have triple redundancy
3. **Fail-informed**: All failures are logged, reported, and analyzed

## 2. Warp Bubble Containment

### 2.1 Bubble Field Boundaries

The warp bubble field is contained within the coil array by design. The warp field amplitude decays exponentially outside the array:

```
B_warp(r) = B₀ · exp(-r/λ_warp)
```

where λ_warp = 1.0 m. At 5 meters from the hull, the warp field is:

```
B_warp(5m) = B₀ · exp(-5/1.0) = B₀ · exp(-5) ≈ 0.0067B₀
```

This is below the threshold for any physical effect on external objects.

### 2.2 Bubble Containment Monitor

The bubble containment monitor continuously measures the warp field amplitude at the hull surface:

| Sensor | Location | Measurement | Threshold |
|--------|----------|-------------|-----------|
| Warp probe 1 | Forward hull | B_warp | < 0.5 T |
| Warp probe 2 | Aft hull | B_warp | < 0.5 T |
| Warp probe 3 | Port hull | B_warp | < 0.5 T |
| Warp probe 4 | Starboard hull | B_warp | < 0.5 T |

If any probe reads above threshold, the bubble containment system activates:
1. Reduce warp amplitude to 50%
2. If still above threshold, abort warp
3. If warp abort fails, emergency dump all warp energy to heat sinks

### 2.3 Warp Quench System

The warp quench system is a last-resort safety measure that rapidly collapses the warp bubble by dumping all warp energy into resistive heat sinks:

```
Warp quench sequence:
  Time 0 ms: Cut power to all coils
  Time 50 ms: Activate quench switches (all coils shorted to heat sinks)
  Time 500 ms: Warp energy dissipating (100 MW → heat sinks)
  Time 1 sec: Warp field at 50%
  Time 5 sec: Warp field at 10%
  Time 15 sec: Warp field at 0%
```

Total quench time: 15 seconds.

## 3. Abort Logic

### 3.1 Abort Conditions

The warp is aborted automatically when any of the following conditions are detected:

| Condition | Detection method | Response time |
|-----------|-----------------|---------------|
| Warp bubble integrity < 95% | Bubble sensor | 100 ms |
| Warp field amplitude > 120% nominal | Warp probe | 20 ms |
| Warp frequency drift > 0.1% | PLL error signal | 10 ms |
| Warp bubble position error > 1 m | Warp radar | 200 ms |
| Metric coherence < 99% | Coherence sensor | 40 ms |
| Bubble containment breach | Containment monitor | 20 ms |
| Passenger vital sign anomaly | Biometric sensors | 500 ms |
| Structural integrity < 90% | Strain gauges | 200 ms |
| Warp time > 2× nominal | Timer | 200 ms |
| CTC risk detected | Chronology monitor | 10 ms |
| Manual abort command | Crew input | 10 ms |

### 3.2 Abort Sequence

```
Phase 1: Decision (0 - 20 ms)
  - Abort logic determines abort is necessary
  - Abort command issued to all subsystems

Phase 2: Power cut (20 - 120 ms)
  - All warp coil power cut
  - Warp power buses disconnected
  - Batteries isolated from warp system

Phase 3: Bubble collapse (120 - 5120 ms)
  - Warp field begins collapsing
  - Warp bubble dissolving
  - Vehicle returns to flat spacetime

Phase 4: Stabilization (5120 - 15120 ms)
  - Metric verified flat (within 0.1%)
  - Vehicle position verified (star tracker)
  - Systems status checked

Phase 5: Report (15120 - 16000 ms)
  - Abort reason logged
  - Crew notified
  - Ground control notified (if communication available)
```

Total abort time: 16 seconds.

### 3.3 Manual Abort

The crew can initiate a manual abort at any time by pressing the red warp abort button (located on the pilot's console and the copilot's console). The manual abort:
- Overrides all automatic systems
- Initiates the standard abort sequence
- Cannot be overridden by automatic systems

### 3.4 Abort Recovery

After an abort, the vehicle:
- Is in its original position (or very close, within ±0.01 LY)
- Has all systems operational (warp coils may need cooldown)
- Can attempt another warp after a 60-second cooldown
- Must wait 10 minutes if the abort was due to bubble containment breach

## 4. Shielding

### 4.1 Electromagnetic Shielding

The vehicle hull is a Faraday cage that provides electromagnetic shielding:

```
Shielding specification:
  Hull material: Aluminum alloy 7075-T6, 5mm thick
  Shielding effectiveness: > 80 dB (100 kHz - 1 GHz)
  Ground plane: Conductive mesh embedded in hull
  Cable shielding: Braided copper, double-shielded
```

### 4.2 Radiation Shielding

The vehicle provides radiation shielding against:

| Radiation type | Source | Shielding method | Protection level |
|----------------|--------|------------------|-----------------|
| X-rays | Warp formation | Lead lining (3mm) | > 95% attenuation |
| Gamma rays | Warp collapse | Tungsten shielding (2mm) | > 90% attenuation |
| Neutrons | Warp energy dissipation | Polyethylene (30mm) | > 98% attenuation |
| UV radiation | Warp plasma | Hull coating (TiO₂) | > 99% attenuation |

### 4.3 Warp Radiation

During warp formation and collapse, the vehicle emits **warp radiation** — metric perturbations that propagate at the speed of light. This radiation:
- Is harmless to humans (below safety thresholds)
- Can interfere with electronic equipment (mitigated by Faraday cage)
- Is detectable by warp signature monitors (used for warp conflict avoidance)

### 4.4 Bubble Radiation Shielding

The warp bubble itself provides radiation shielding:

| Radiation type | Source | Bubble shielding | Protection level |
|----------------|--------|------------------|-----------------|
| Cosmic rays | Interstellar space | Bubble wall (metric distortion) | > 99% attenuation |
| Solar radiation | Stars | Bubble wall | > 99% attenuation |
| Interstellar medium | Dust, gas | Bubble wall | > 99% attenuation |

## 5. Passenger Safety

### 5.1 Warp Cocoon

During warp transit, passengers are enclosed in a **warp cocoon** — a protective enclosure that:
- Shields passengers from warp radiation
- Provides structural support during metric perturbation
- Maintains life support during transit
- Monitors passenger vital signs

### 5.2 Warp Cocoon Specifications

| Parameter | Value |
|-----------|-------|
| Material | Carbon fiber composite |
| Thickness | 8 mm |
| Shielding | Lead lining (1 mm) |
| Life support | 60 minutes independent |
| Vital sign monitoring | Heart rate, SpO2, respiration |
| Emergency supply | Water, food, medical kit |

### 5.3 Passenger Monitoring During Warp

The warp cocoon monitors passenger vital signs throughout the warp:

```
Monitoring during warp:
  Heart rate: 60-100 bpm (normal range)
  Blood oxygen: 95-100% (normal range)
  Respiration: 12-20 breaths/min (normal range)
  Body temperature: 36.1-37.2°C (normal range)
  Acceleration: < 2g (warp limit)
  Consciousness: EEG (optional, research mode)
```

If any vital sign goes out of range:
1. Alert crew (audio + visual)
2. Provide medical intervention (automatic)
3. If necessary, trigger warp abort (passenger safety priority)

## 6. Chronology Protection

### 6.1 CTC Detection

The chronology monitor continuously checks for closed timelike curves (CTCs) that could create paradoxes:

```
CTC detection parameters:
  Warp velocity: < 0.99c (local frame)
  Warp bubble curvature: < threshold
  Gravitational field: < threshold
  Causal structure: Verified (no CTCs)
```

### 6.2 Chronology Protection Response

If CTC risk is detected:
1. Alert crew (audio + visual)
2. Reduce warp velocity to safe level
3. Adjust warp bubble geometry
4. If necessary, collapse warp bubble
5. Log event for analysis

### 6.3 Chronology Protection Limits

| Parameter | Limit | Action |
|-----------|-------|--------|
| Warp velocity | < 0.99c (local frame) | Reduce speed |
| Warp bubble curvature | < 0.01 m⁻¹ | Adjust geometry |
| Gravitational field | < 0.1 g/m | Avoid massive objects |
| Causal structure | No CTCs | Collapse bubble |

## 7. Structural Safety

### 7.1 Structural Integrity

The vehicle structure is designed to withstand:
- Warp forces (up to 2g equivalent)
- Warp radiation (up to 100 mSv per light-year)
- Warp thermal loads (up to 3.7 kWh per light-year)
- External impacts (up to 10 J at hull surface)
- Emergency landing (up to 5g vertical, 2g horizontal)

### 7.2 Structural Monitoring

| Sensor | Location | Measurement | Threshold |
|--------|----------|-------------|-----------|
| Strain gauge | Hull frame | Strain | < 0.1% |
| Accelerometer | Center of mass | Acceleration | < 3g |
| Gyroscope | Hull frame | Angular rate | < 10°/s |
| Pressure sensor | Cabin | Cabin pressure | 0.9-1.1 atm |
| Temperature sensor | Hull surface | Hull temperature | < 120°C |

## 8. Fire Safety

### 8.1 Fire Detection

| Sensor type | Location | Sensitivity |
|-------------|----------|-------------|
| Smoke detector | Cabin, battery bay, electronics bay | 0.1% obscurity/m |
| Heat detector | Battery bay, electronics bay | 68°C fixed, 8.3°C/min rise |
| Flame detector | Cabin, battery bay | UV + IR, 0.5 sec response |
| Gas detector | Battery bay | H₂, CO, electrolyte vapor |

### 8.2 Fire Suppression

| Zone | Suppression method | Agent |
|------|-------------------|-------|
| Cabin | Manual extinguisher | CO₂ |
| Battery bay | Automatic | Clean agent (FM-200) |
| Electronics bay | Automatic | Clean agent (FM-200) |
| Warp coil bay | Automatic | Nitrogen flood |

### 8.3 Emergency Evacuation

In case of fire:
1. Alert crew (audio + visual alarm)
2. Activate fire suppression in affected zone
3. If fire cannot be controlled, initiate warp abort (if in warp)
4. Open emergency exits (2 on each side)
5. Deploy evacuation slide (if height > 1.5 m)
6. Crew and passengers evacuate within 90 seconds
