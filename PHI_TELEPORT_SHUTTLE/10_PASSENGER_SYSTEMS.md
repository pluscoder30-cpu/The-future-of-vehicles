# Passenger Systems — Seating, Life Support, and Fold Cocoon

## 1. Cabin Layout

### 1.1 Configuration

The cabin accommodates 2 passengers in a side-by-side configuration:

```
Cabin top view:

  ┌─────────────────────────────┐
  │  ┌───────┐    ┌───────┐    │
  │  │Seat 1 │    │Seat 2 │    │
  │  │(Pilot)│    │(Co-pilot)   │
  │  └───────┘    └───────┘    │
  │                             │
  │  ┌─────────────────────┐   │
  │  │    Fold Coil Array   │   │
  │  │    (Below cabin)     │   │
  │  └─────────────────────┘   │
  │                             │
  │  ┌───────┐    ┌───────┐    │
  │  │Seat 3 │    │Seat 4 │    │
  │  │(Pass.)│    │(Pass.)│    │
  │  └───────┘    └───────┘    │
  └─────────────────────────────┘
```

### 1.2 Seat Specifications

| Parameter | Value |
|-----------|-------|
| Seat type | Fold-rated crash seat |
| Material | Carbon fiber shell, memory foam cushion |
| Restraint | 5-point harness |
| Adjustment | Electric (fore/aft, height, recline) |
| Fold cocoon | Integrated (deploys automatically) |
| Life support | 30 minutes independent |
| Communication | Headset with boom mic |
| Reading light | LED, adjustable intensity |
| Power outlet | 12V DC, 5V USB |
| Mass per seat | 12 kg |

### 1.3 Cabin Dimensions

| Parameter | Value |
|-----------|-------|
| Cabin length | 2.4 m |
| Cabin width | 1.8 m |
| Cabin height | 1.2 m |
| Headroom (seated) | 0.95 m |
| Legroom | 0.8 m |
| Floor area | 4.32 m² |
| Volume | 5.18 m³ |

## 2. Life Support

### 2.1 Atmosphere

| Parameter | Value |
|-----------|-------|
| Composition | 78% N₂, 21% O₂, 1% Ar |
| Pressure | 1.0 atm (101.3 kPa) |
| Temperature | 20-24°C |
| Humidity | 30-60% RH |
| CO₂ level | < 0.5% (5,000 ppm) |
| Air exchange rate | 10 changes/hour |
| Filtration | HEPA + activated carbon |

### 2.2 Oxygen Supply

```
Oxygen supply:
  Type: Compressed oxygen (medical grade)
  Capacity: 30 minutes for 2 passengers
  Flow rate: 2 L/min per passenger
  Regulator: Demand-type, failsafe
  Backup: Chemical oxygen generator (15 min)
```

### 2.3 Temperature Control

| System | Method | Capacity |
|--------|--------|----------|
| Heating | Electric resistance | 500 W |
| Cooling | Thermoelectric (Peltier) | 300 W |
| Distribution | Forced air | 200 CFM |
| Control | Automatic (thermostat) | ±1°C |

### 2.4 Water Supply

```
Water supply:
  Drinking water: 2 L per passenger
  Total: 4 L
  Container: Food-grade HDPE
  Dispenser: Manual pump
  Emergency: Water purification tablets (10 doses)
```

### 2.5 Waste Management

```
Waste management:
  Type: Portable chemical toilet
  Capacity: 5 uses
  Deodorizer: Chemical (formaldehyde-based)
  Disposal: Ground-based (post-flight)
  Sanitizer: Alcohol-based hand gel (100 mL)
```

## 3. Fold Cocoon

### 3.1 Purpose

The fold cocoon is a protective enclosure that deploys around each passenger during fold transit. It provides:
- Structural support during metric perturbation
- Fold radiation shielding
- Life support during transit
- Vital sign monitoring

### 3.2 Deployment Sequence

```
Fold cocoon deployment:
  Time -5 sec: Pre-deploy check (cabin pressure, passenger position)
  Time -3 sec: Cocoon shells extend from seat sides
  Time -1 sec: Cocoon shells close around passenger
  Time 0 sec: Fold transit begins (cocoon fully sealed)
  Time +0.8 sec: Fold transit complete
  Time +1 sec: Cocoon shells retract
  Time +3 sec: Cocoon fully retracted
```

### 3.3 Cocoon Specifications

| Parameter | Value |
|-----------|-------|
| Material | CFRP shell (2 mm) + lead lining (0.5 mm) |
| Shape | Human-form enclosure |
| Internal volume | 0.3 m³ |
| Mass | 8 kg per cocoon |
| Deployment time | 5 seconds |
| Retraction time | 3 seconds |
| Fold radiation shielding | > 90% attenuation |
| Life support | 30 minutes independent |
| Vital sign monitoring | Heart rate, SpO2, respiration |
| Emergency supply | Water (200 mL), medical kit |

### 3.4 Fold Radiation Protection

The fold cocoon protects passengers from fold radiation:

| Radiation type | Source | Cocoon shielding | Exposure limit |
|----------------|--------|------------------|----------------|
| X-rays | Fold formation | Lead lining (0.5 mm) | < 0.1 mSv per fold |
| Gamma rays | Fold collapse | Lead lining (0.5 mm) | < 0.05 mSv per fold |
| Neutrons | Fold energy | Polyethylene (10 mm) | < 0.01 mSv per fold |
| UV radiation | Fold plasma | CFRP shell (2 mm) | < 0.001 mSv per fold |
| **Total** | — | — | **< 0.161 mSv per fold** |

Annual exposure limit: 20 mSv. Maximum folds per year: 124.

### 3.5 Passenger Monitoring During Fold

The fold cocoon monitors passenger vital signs throughout the fold:

```
Monitoring during fold:
  Heart rate: 60-100 bpm (normal range)
  Blood oxygen: 95-100% (normal range)
  Respiration: 12-20 breaths/min (normal range)
  Body temperature: 36.1-37.2°C (normal range)
  Acceleration: < 5g (fold limit)
  Consciousness: EEG (optional, research mode)
```

If any vital sign goes out of range:
1. Alert crew (audio + visual)
2. Provide medical intervention (automatic)
3. If necessary, trigger fold abort (passenger safety priority)

## 4. Cabin Environment

### 4.1 Lighting

| Parameter | Value |
|-----------|-------|
| Type | LED |
| Color temperature | 4,000K (neutral white) |
| Intensity | 300 lux (adjustable) |
| Night mode | 5 lux red (preserve night vision) |
| Emergency lighting | 5 lux white (battery-powered, 30 min) |

### 4.2 Noise

| Source | Noise level |
|--------|-------------|
| Fold coils (idle) | 45 dB(A) |
| Fold coils (active) | 75 dB(A) |
| Life support | 35 dB(A) |
| Communication | 60 dB(A) |
| **Cabin noise (fold transit)** | **75 dB(A)** |

### 4.3 Vibration

| Source | Vibration level |
|--------|----------------|
| Fold coils (idle) | 0.1g RMS |
| Fold coils (active) | 0.5g RMS |
| Fold transit | 4.2g peak (0.8 sec) |
| **Cabin vibration (fold transit)** | **4.2g peak** |

### 4.4 Windows

| Parameter | Value |
|-----------|-------|
| Number | 2 (one per side) |
| Material | Polycarbonate |
| Thickness | 10 mm |
| Size | 0.3m × 0.2 m |
| UV protection | > 99% UV-A, UV-B |
| Visibility | > 90% visible light transmission |
| Fold radiation protection | Lead lining (0.3 mm) |

## 5. Passenger Briefing

### 5.1 Pre-Fold Briefing

Before each fold, passengers receive a briefing:

```
Pre-fold briefing:
  1. Fold sequence explanation (30 sec)
  2. Fold cocoon deployment (15 sec)
  3. Safety harness check (15 sec)
  4. Communication check (10 sec)
  5. Emergency procedure review (30 sec)
  6. Questions (30 sec)
  Total: 2 minutes
```

### 5.2 Emergency Procedures

Passengers are briefed on:
1. Fold abort procedure (automatic, no passenger action required)
2. Emergency evacuation (manual, crew-directed)
3. Emergency communication (intercom, visual signals)
4. Medical emergency (crew first aid, automatic cocoon response)

## 6. Accessibility

### 6.1 Accessibility Features

| Feature | Description |
|---------|-------------|
| Wheelchair access | Ramp deployed for boarding |
| Seat modification | Removable armrest, adjustable headrest |
| Communication | Visual + audio alerts |
| Emergency evacuation | Crew-assisted, fold cocoon provides protection |
| Medical equipment | AED, first aid kit, emergency medication |

### 6.2 Passenger Limitations

| Limitation | Reason | Mitigation |
|------------|--------|------------|
| Maximum passenger mass | 120 kg (fold payload limit) | Weight check before boarding |
| Maximum passenger height | 2.0 m (cocoon fit) | Height check before boarding |
| Minimum passenger age | 12 years (fold cocoon fit) | Age verification |
| Medical conditions | Heart condition, pregnancy, claustrophobia | Medical clearance required |
