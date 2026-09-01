# Payload Systems — Cargo Bay, Clamping, and Payload Integrity

## 1. Cargo Bay Configuration

### 1.1 Location

The cargo bay is located beneath the passenger cabin, between the fold coil array and the hull bottom:

```
Side view:

  ┌─────────────────────┐
  │    Passenger Cabin   │
  ├─────────────────────┤
  │    Fold Coil Array   │
  ├─────────────────────┤
  │    Cargo Bay         │
  │    (100 kg max)      │
  └─────────────────────┘
       Landing Gear
```

### 1.2 Cargo Bay Dimensions

| Parameter | Value |
|-----------|-------|
| Length | 1.2 m |
| Width | 1.0 m |
| Height | 0.8 m |
| Volume | 0.96 m³ |
| Door size | 0.8m × 0.6 m |
| Door type | Split, gull-wing |
| Loading | Manual or conveyor |

### 1.3 Cargo Bay Environment

| Parameter | Value |
|-----------|-------|
| Temperature | -20°C to +50°C (uncontrolled) |
| Pressure | Ambient (1 atm) |
| Humidity | Ambient |
| Vibration | 0.1g RMS (idle), 4.2g peak (fold transit) |
| Radiation | Shielded (> 80% attenuation) |

## 2. Payload Specifications

### 2.1 Payload Limits

| Parameter | Value |
|-----------|-------|
| Maximum mass | 100 kg |
| Maximum volume | 0.96 m³ |
| Maximum density | 104 kg/m³ |
| Maximum dimensions | 1.2m × 1.0m × 0.8 m |
| Maximum fold force | 4.2g (fold transit) |
| Maximum fold radiation | 0.161 mSv (fold transit) |

### 2.2 Payload Types

| Type | Description | Special requirements |
|------|-------------|---------------------|
| General cargo | Boxes, equipment | Standard clamping |
| Sensitive cargo | Electronics, instruments | Vibration isolation |
| Hazardous cargo | Chemicals, radioactive | Containment, shielding |
| Fragile cargo | Glass, ceramics | Cushioning, gentle clamping |
| Living cargo | Plants, small animals | Life support, temperature control |
| Human remains | Body, cremains | Dignity, temperature control |

### 2.3 Payload Classification

| Class | Description | Requirements |
|-------|-------------|-------------|
| Class 1 | Non-hazardous, non-fragile | Standard handling |
| Class 2 | Fragile | Cushioning, gentle clamping |
| Class 3 | Sensitive (electronics) | Vibration isolation, ESD protection |
| Class 4 | Hazardous (chemical) | Containment, labeling, MSDS |
| Class 5 | Hazardous (radioactive) | Shielding, monitoring, labeling |
| Class 6 | Living | Life support, temperature, humidity |
| Class 7 | Human remains | Temperature, dignity, documentation |

## 3. Payload Clamping System

### 3.1 Clamp Design

The clamping system secures the payload during fold transit:

```
Clamp configuration (top view):

  ┌─────────────────────────┐
  │  C1          C2          │
  │  ┌───────────────────┐  │
  │  │                   │  │
  │  │    Payload        │  │
  │  │                   │  │
  │  └───────────────────┘  │
  │  C3          C4          │
  └─────────────────────────┘

C1-C4 = Clamp points (4 total)
```

### 3.2 Clamp Specifications

| Parameter | Value |
|-----------|-------|
| Number of clamps | 4 |
| Clamp type | Pneumatic, spring-loaded |
| Clamp force | 500 N per clamp |
| Clamp travel | 50 mm |
| Clamp material | Aluminum 6061-T6 |
| Clamp pad | Rubber (Shore 60A) |
| Release | Manual or automatic |

### 3.3 Clamping Sequence

```
Clamping sequence:
  1. Position payload in cargo bay
  2. Align payload with clamp points
  3. Activate clamps (manual switch or automatic)
  4. Verify clamp force (sensor feedback)
  5. Lock clamps (mechanical latch)
  6. Verify payload secure (vibration test)
```

### 3.4 Clamp Monitoring

| Sensor | Measurement | Threshold |
|--------|-------------|-----------|
| Clamp force sensor | Force per clamp | > 400 N |
| Payload position sensor | X, Y, Z position | ±10 mm |
| Payload vibration sensor | Acceleration | < 2g RMS |
| Payload temperature sensor | Temperature | -20°C to +50°C |

## 4. Payload Integrity

### 4.1 Fold Transit Effects

During fold transit, the payload experiences:
- Fold forces: up to 4.2g (0.8 seconds)
- Fold radiation: up to 0.161 mSv
- Fold thermal loads: up to 0.1 kWh
- Fold vibration: up to 2g RMS (3.8 seconds)

### 4.2 Payload Protection

| Hazard | Protection method | Effectiveness |
|--------|------------------|---------------|
| Fold forces | Clamping system | 100% (payload secured) |
| Fold radiation | Hull shielding (> 80%) + cargo bay location | > 90% attenuation |
| Fold thermal loads | Cargo bay insulation | Temperature change < 5°C |
| Fold vibration | Clamp pads (rubber) | Vibration attenuation > 50% |
| Impact (landing) | Clamp system + cargo bay structure | 100% (payload secured) |

### 4.3 Payload Monitoring During Fold

The cargo bay monitoring system tracks payload status throughout the fold:

```
Payload monitoring during fold:
  Position: Continuous (GPS + inertial)
  Vibration: Continuous (accelerometer)
  Temperature: Continuous (thermocouple)
  Clamp force: Continuous (force sensor)
  Radiation: Continuous (Geiger counter)
  Integrity: Visual (camera)
```

If any parameter goes out of range:
1. Alert crew (audio + visual)
2. Log the event (data recorder)
3. If necessary, trigger fold abort (payload safety priority)

### 4.4 Payload Integrity Verification

After fold transit, the cargo bay system verifies payload integrity:

```
Post-fold verification:
  □ Clamp force: All clamps within tolerance
  □ Payload position: Within ±10 mm of pre-fold position
  □ Payload temperature: Within ±5°C of pre-fold temperature
  □ Payload vibration: Below 2g RMS
  □ Payload radiation: Below 0.2 mSv total exposure
  □ Visual inspection: No visible damage (camera)
  □ Weight check: Within ±0.5 kg of pre-fold weight
```

## 5. Special Payload Configurations

### 5.1 Sensitive Electronics

For sensitive electronics (computers, instruments):

```
Special requirements:
  - Vibration isolation pads (25 mm thick)
  - ESD protection (grounding strap)
  - Temperature control (±2°C)
  - Humidity control (±5% RH)
  - EMI shielding (Faraday cage)
```

### 5.2 Hazardous Materials

For hazardous materials (chemicals, radioactive):

```
Special requirements:
  - Secondary containment (drip tray)
  - MSDS documentation (physical and digital)
  - Labeling (hazard symbols, UN number)
  - Monitoring (gas detector, radiation monitor)
  - Emergency response kit (neutralizer, absorbent)
```

### 5.3 Living Cargo

For living cargo (plants, small animals):

```
Special requirements:
  - Temperature control (15-25°C)
  - Humidity control (40-70% RH)
  - Light cycle (12 hr light / 12 hr dark)
  - Water supply (automatic mister)
  - Air supply (fresh air exchange)
  - Monitoring (camera, temperature, humidity)
```

### 5.4 Human Remains

For human remains (body, cremains):

```
Special requirements:
  - Temperature control (2-8°C for body, ambient for cremains)
  - Dignity handling (respectful placement, cover)
  - Documentation (death certificate, transport permit)
  - Monitoring (temperature, vibration)
  - Post-fold procedure (body to morgue, cremains to family)
```

## 6. Loading and Unloading

### 6.1 Loading Procedure

```
Loading procedure:
  1. Open cargo bay door (manual or power)
  2. Inspect cargo bay (clean, clear)
  3. Position payload (manual or conveyor)
  4. Align with clamp points
  5. Activate clamps (manual or automatic)
  6. Verify clamp force
  7. Close cargo bay door
  8. Verify door seal
  9. Log payload (type, weight, dimensions)
```

### 6.2 Unloading Procedure

```
Unloading procedure:
  1. Verify fold complete (navigation system)
  2. Verify cargo bay safe (no hazards)
  3. Open cargo bay door
  4. Release clamps (manual or automatic)
  5. Remove payload (manual or conveyor)
  6. Inspect cargo bay (clean, clear)
  7. Close cargo bay door
  8. Verify door seal
  9. Log payload (type, weight, condition)
```

### 6.3 Loading Time

| Payload type | Loading time | Unloading time |
|--------------|-------------|----------------|
| General cargo (1 person) | 5 minutes | 3 minutes |
| General cargo (2 persons) | 3 minutes | 2 minutes |
| Sensitive cargo | 10 minutes | 5 minutes |
| Hazardous cargo | 15 minutes | 10 minutes |
| Living cargo | 10 minutes | 5 minutes |
| Human remains | 15 minutes | 10 minutes |

## 7. Cargo Bay Safety

### 7.1 Cargo Bay Hazards

| Hazard | Source | Mitigation |
|--------|--------|------------|
| Crush injury | Clamping system | Safety interlocks, warning labels |
| Toxic fumes | Hazardous cargo | Gas detection, ventilation |
| Radiation | Radioactive cargo | Shielding, monitoring, labeling |
| Fire | Flammable cargo | Fire detection, suppression |
| Impact | Loose cargo | Clamping system, cargo bay structure |

### 7.2 Cargo Bay Safety Equipment

| Equipment | Location | Purpose |
|-----------|----------|---------|
| Gas detector | Cargo bay ceiling | Detect toxic fumes |
| Radiation monitor | Cargo bay wall | Detect radiation |
| Fire detector | Cargo bay ceiling | Detect fire |
| Fire extinguisher | Cargo bay door | Extinguish fire |
| Emergency ventilation | Cargo bay ceiling | Remove fumes |
| Warning labels | Cargo bay door | Warn of hazards |
| Safety interlock | Cargo bay door | Prevent opening during fold |
