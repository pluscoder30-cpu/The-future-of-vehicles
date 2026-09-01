# Safety Systems — Fold Containment, Abort Logic, and Shielding

## 1. Safety Philosophy

The teleport shuttle operates in a regime where spatial metric manipulation creates unique hazards. The safety system is designed around three principles:

1. **Fail-safe**: Any single failure results in a safe state (fold abort, vehicle stationary)
2. **Fail-operational**: Critical systems have triple redundancy
3. **Fail-informed**: All failures are logged, reported, and analyzed

## 2. Fold Containment

### 2.1 Fold Field Boundaries

The fold field is contained within the coil array by design. The fold field amplitude decays exponentially outside the array:

```
B_fold(r) = B₀ · exp(-r/λ_fold)
```

where λ_fold = 0.5 m. At 2 meters from the hull, the fold field is:

```
B_fold(2m) = B₀ · exp(-2/0.5) = B₀ · exp(-4) ≈ 0.018B₀
```

This is below the threshold for any physical effect on external objects.

### 2.2 Fold Containment Monitor

The fold containment monitor continuously measures the fold field amplitude at the hull surface:

| Sensor | Location | Measurement | Threshold |
|--------|----------|-------------|-----------|
| Fold probe 1 | Forward hull | B_fold | < 0.1 T |
| Fold probe 2 | Aft hull | B_fold | < 0.1 T |
| Fold probe 3 | Port hull | B_fold | < 0.1 T |
| Fold probe 4 | Starboard hull | B_fold | < 0.1 T |

If any probe reads above threshold, the fold containment system activates:
1. Reduce fold amplitude to 50%
2. If still above threshold, abort fold
3. If fold abort fails, emergency dump all fold energy to heat sinks

### 2.3 Fold Quench System

The fold quench system is a last-resort safety measure that rapidly collapses the fold by dumping all fold energy into resistive heat sinks:

```
Fold quench sequence:
  Time 0 ms: Cut power to all coils
  Time 10 ms: Activate quench switches (all coils shorted to heat sinks)
  Time 50 ms: Fold energy dissipating (100 MW → heat sinks)
  Time 100 ms: Fold field at 50%
  Time 500 ms: Fold field at 10%
  Time 1000 ms: Fold field at 0%
```

Total quench time: 1 second.

## 3. Abort Logic

### 3.1 Abort Conditions

The fold is aborted automatically when any of the following conditions are detected:

| Condition | Detection method | Response time |
|-----------|-----------------|---------------|
| Fold bridge integrity < 95% | Fold bridge sensor | 50 ms |
| Fold field amplitude > 120% nominal | Fold probe | 10 ms |
| Fold frequency drift > 0.1% | PLL error signal | 5 ms |
| Fold node position error > 1 m | Fold radar | 100 ms |
| Metric coherence < 99% | Coherence sensor | 20 ms |
| Fold containment breach | Containment monitor | 10 ms |
| Passenger vital sign anomaly | Biometric sensors | 500 ms |
| Structural integrity < 90% | Strain gauges | 100 ms |
| Fold time > 2× nominal | Timer | 100 ms |
| Manual abort command | Crew input | 10 ms |

### 3.2 Abort Sequence

The abort sequence is:

```
Phase 1: Decision (0 - 10 ms)
  - Abort logic determines abort is necessary
  - Abort command issued to all subsystems

Phase 2: Power cut (10 - 60 ms)
  - All fold coil power cut
  - Fold power buses disconnected
  - Batteries isolated from fold system

Phase 3: Fold collapse (60 - 560 ms)
  - Fold field begins collapsing
  - Fold bridge dissolving
  - Vehicle returns to flat metric

Phase 4: Stabilization (560 - 1650 ms)
  - Metric verified flat (within 0.1%)
  - Vehicle position verified (GPS)
  - Systems status checked

Phase 5: Report (1650 - 2000 ms)
  - Abort reason logged
  - Crew notified
  - Ground control notified (if communication available)
```

Total abort time: 2 seconds.

### 3.3 Manual Abort

The crew can initiate a manual abort at any time by pressing the red fold abort button (located on the pilot's console and the copilot's console). The manual abort:
- Overrides all automatic systems
- Initiates the standard abort sequence
- Cannot be overridden by automatic systems

### 3.4 Abort Recovery

After an abort, the vehicle:
- Is in its original position (or very close, within ±1 m)
- Has all systems operational (fold coils may need cooldown)
- Can attempt another fold after a 30-second cooldown
- Must wait 5 minutes if the abort was due to fold containment breach

## 4. Shielding

### 4.1 Electromagnetic Shielding

The vehicle hull is a **Faraday cage** that provides electromagnetic shielding:

```
Shielding specification:
  Hull material: Aluminum alloy 7075-T6, 3mm thick
  Shielding effectiveness: > 60 dB (100 kHz - 1 GHz)
  Ground plane: Conductive mesh embedded in hull
  Cable shielding: Braided copper, double-shielded
```

### 4.2 Radiation Shielding

The vehicle provides radiation shielding against:

| Radiation type | Source | Shielding method | Protection level |
|----------------|--------|------------------|-----------------|
| X-rays | Fold formation | Lead lining (2mm) | > 90% attenuation |
| Gamma rays | Fold collapse | Tungsten shielding (1mm) | > 80% attenuation |
| Neutrons | Fold energy dissipation | Polyethylene (20mm) | > 95% attenuation |
| UV radiation | Fold plasma | Hull coating (TiO₂) | > 99% attenuation |

### 4.3 Fold Radiation

During fold formation and collapse, the vehicle emits **fold radiation** — metric perturbations that propagate at the speed of light. This radiation:
- Is harmless to humans (below safety thresholds)
- Can interfere with electronic equipment (mitigated by Faraday cage)
- Is detectable by fold signature monitors (used for fold conflict avoidance)

### 4.4 Thermal Shielding

The vehicle hull has thermal protection against:
- Fold heat dissipation (up to 5.2 kWh per fold)
- Re-entry heating (not applicable for teleport shuttle, but included for safety)
- External heat sources (fire, solar radiation)

Thermal protection specification:
```
Hull coating: Ceramic thermal protection tiles
Temperature rating: 1,200°C
Thermal conductivity: 0.1 W/m·K
Emissivity: 0.85
```

## 5. Passenger Safety

### 5.1 Fold Cocoon

During fold transit, passengers are enclosed in a **fold cocoon** — a protective enclosure that:
- Shields passengers from fold radiation
- Provides structural support during metric perturbation
- Maintains life support during transit
- Monitors passenger vital signs

### 5.2 Fold Cocoon Specifications

| Parameter | Value |
|-----------|-------|
| Material | Carbon fiber composite |
| Thickness | 5 mm |
| Shielding | Lead lining (0.5 mm) |
| Life support | 30 minutes independent |
| Vital sign monitoring | Heart rate, SpO2, respiration |
| Emergency supply | Water, food, medical kit |

### 5.3 Passenger Monitoring

The fold cocoon monitors passenger vital signs throughout the fold:

```
Monitoring parameters:
  Heart rate: Continuous ECG
  Blood oxygen: Pulse oximetry
  Respiration: Chest impedance
  Body temperature: Infrared sensor
  Orientation: Accelerometer
  Consciousness: EEG (optional)
```

If any vital sign goes out of range, the fold cocoon:
1. Alerts the crew
2. Provides medical intervention (automatic defibrillation, oxygen)
3. If necessary, triggers a fold abort to protect the passenger

## 6. Structural Safety

### 6.1 Structural Integrity

The vehicle structure is designed to withstand:
- Fold forces (up to 4.2g equivalent)
- Fold radiation (up to 100 mSv per fold)
- Fold thermal loads (up to 5.2 kWh per fold)
- External impacts (up to 10 J at hull surface)
- Emergency landing (up to 5g vertical, 2g horizontal)

### 6.2 Structural Monitoring

| Sensor | Location | Measurement | Threshold |
|--------|----------|-------------|-----------|
| Strain gauge | Hull frame | Strain | < 0.1% |
| Accelerometer | Center of mass | Acceleration | < 5g |
| Gyroscope | Hull frame | Angular rate | < 10°/s |
| Pressure sensor | Cabin | Cabin pressure | 0.9-1.1 atm |
| Temperature sensor | Hull surface | Hull temperature | < 120°C |

### 6.3 Structural Redundancy

The vehicle structure has triple redundancy:
1. **Primary structure**: Carbon fiber monocoque
2. **Secondary structure**: Aluminum space frame
3. **Tertiary structure**: Fold-reinforced hull (fold field provides structural support during fold operations)

## 7. Fire Safety

### 7.1 Fire Detection

| Sensor type | Location | Sensitivity |
|-------------|----------|-------------|
| Smoke detector | Cabin, battery bay, electronics bay | 0.1% obscurity/m |
| Heat detector | Battery bay, electronics bay | 68°C fixed, 8.3°C/min rise |
| Flame detector | Cabin, battery bay | UV + IR, 0.5 sec response |
| Gas detector | Battery bay | H₂, CO, electrolyte vapor |

### 7.2 Fire Suppression

| Zone | Suppression method | Agent |
|------|-------------------|-------|
| Cabin | Manual extinguisher | CO₂ |
| Battery bay | Automatic | Clean agent (FM-200) |
| Electronics bay | Automatic | Clean agent (FM-200) |
| Fold coil bay | Automatic | Nitrogen flood |

### 7.3 Emergency Evacuation

In case of fire:
1. Alert crew (audio + visual alarm)
2. Activate fire suppression in affected zone
3. If fire cannot be controlled, initiate fold abort (if in fold)
4. Open emergency exits (2 on each side)
5. Deploy evacuation slide (if height > 1.5 m)
6. Crew and passengers evacuate within 90 seconds
