# Passenger Systems — Seating, Life Support, and Warp Cocoon

## 1. Cabin Layout

### 1.1 Configuration

The cabin accommodates 4 passengers in a 2×2 configuration:

```
Cabin top view:

  ┌─────────────────────────────────┐
  │  ┌───────┐        ┌───────┐    │
  │  │Seat 1 │        │Seat 2 │    │
  │  │(Pilot)│        │(Co-pilot)   │
  │  └───────┘        └───────┘    │
  │                                 │
  │  ┌─────────────────────────┐   │
  │  │    Warp Coil Array       │   │
  │  │    (Below cabin)         │   │
  │  └─────────────────────────┘   │
  │                                 │
  │  ┌───────┐        ┌───────┐    │
  │  │Seat 3 │        │Seat 4 │    │
  │  │(Pass.)│        │(Pass.)│    │
  │  └───────┘        └───────┘    │
  │                                 │
  │  ┌───────┐        ┌───────┐    │
  │  │Seat 5 │        │Seat 6 │    │
  │  │(Pass.)│        │(Pass.)│    │
  │  └───────┘        └───────┘    │
  └─────────────────────────────────┘
```

### 1.2 Seat Specifications

| Parameter | Value |
|-----------|-------|
| Seat type | Warp-rated crash seat |
| Material | Carbon fiber shell, memory foam cushion |
| Restraint | 5-point harness |
| Adjustment | Electric (fore/aft, height, recline) |
| Warp cocoon | Integrated (deploys automatically) |
| Life support | 60 minutes independent |
| Communication | Headset with boom mic |
| Reading light | LED, adjustable intensity |
| Power outlet | 12V DC, 5V USB |
| Mass per seat | 15 kg |

### 1.3 Cabin Dimensions

| Parameter | Value |
|-----------|-------|
| Cabin length | 3.6 m |
| Cabin width | 2.4 m |
| Cabin height | 1.6 m |
| Headroom (seated) | 1.1 m |
| Legroom | 1.0 m |
| Floor area | 8.64 m² |
| Volume | 13.82 m³ |

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
  Capacity: 60 minutes for 4 passengers
  Flow rate: 2 L/min per passenger
  Regulator: Demand-type, failsafe
  Backup: Chemical oxygen generator (30 min)
```

### 2.3 Temperature Control

| System | Method | Capacity |
|--------|--------|----------|
| Heating | Electric resistance | 1,000 W |
| Cooling | Thermoelectric (Peltier) | 600 W |
| Distribution | Forced air | 400 CFM |
| Control | Automatic (thermostat) | ±1°C |

### 2.4 Water Supply

```
Water supply:
  Drinking water: 2 L per passenger
  Total: 8 L
  Container: Food-grade HDPE
  Dispenser: Manual pump
  Emergency: Water purification tablets (20 doses)
```

### 2.5 Waste Management

```
Waste management:
  Type: Portable chemical toilet
  Capacity: 10 uses
  Deodorizer: Chemical (formaldehyde-based)
  Disposal: Ground-based (post-flight)
  Sanitizer: Alcohol-based hand gel (200 mL)
```

## 3. Warp Cocoon

### 3.1 Purpose

The warp cocoon is a protective enclosure that deploys around each passenger during warp transit. It provides:
- Structural support during metric perturbation
- Warp radiation shielding
- Life support during transit
- Vital sign monitoring

### 3.2 Deployment Sequence

```
Warp cocoon deployment:
  Time -10 sec: Pre-deploy check (cabin pressure, passenger position)
  Time -5 sec: Cocoon shells extend from seat sides
  Time -2 sec: Cocoon shells close around passenger
  Time 0 sec: Warp transit begins (cocoon fully sealed)
  Time +T warp: Warp transit complete
  Time +2 sec: Cocoon shells retract
  Time +5 sec: Cocoon fully retracted
```

### 3.3 Cocoon Specifications

| Parameter | Value |
|-----------|-------|
| Material | CFRP shell (3 mm) + lead lining (1 mm) |
| Shape | Human-form enclosure |
| Internal volume | 0.4 m³ |
| Mass | 12 kg per cocoon |
| Deployment time | 8 seconds |
| Retraction time | 5 seconds |
| Warp radiation shielding | > 95% attenuation |
| Life support | 60 minutes independent |
| Vital sign monitoring | Heart rate, SpO2, respiration |
| Emergency supply | Water (500 mL), food (1 meal), medical kit |

### 3.4 Warp Radiation Protection

The warp cocoon protects passengers from warp radiation:

| Radiation type | Source | Cocoon shielding | Exposure limit |
|----------------|--------|------------------|----------------|
| X-rays | Warp formation | Lead lining (1 mm) | < 0.05 mSv per LY |
| Gamma rays | Warp collapse | Lead lining (1 mm) | < 0.02 mSv per LY |
| Neutrons | Warp energy | Polyethylene (15 mm) | < 0.005 mSv per LY |
| UV radiation | Warp plasma | CFRP shell (3 mm) | < 0.0005 mSv per LY |
| **Total** | — | — | **< 0.0755 mSv per LY** |

Annual exposure limit: 20 mSv. Maximum light-years per year: 265.

### 3.5 Passenger Monitoring During Warp

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

## 4. Cabin Environment

### 4.1 Lighting

| Parameter | Value |
|-----------|-------|
| Type | LED |
| Color temperature | 4,000K (neutral white) |
| Intensity | 300 lux (adjustable) |
| Night mode | 5 lux red (preserve night vision) |
| Emergency lighting | 5 lux white (battery-powered, 60 min) |

### 4.2 Noise

| Source | Noise level |
|--------|-------------|
| Warp coils (idle) | 50 dB(A) |
| Warp coils (active) | 80 dB(A) |
| Life support | 40 dB(A) |
| Communication | 65 dB(A) |
| **Cabin noise (warp transit)** | **80 dB(A)** |

### 4.3 Vibration

| Source | Vibration level |
|--------|----------------|
| Warp coils (idle) | 0.1g RMS |
| Warp coils (active) | 0.8g RMS |
| Warp transit | 2g peak (0.8 sec) |
| **Cabin vibration (warp transit)** | **2g peak** |

### 4.4 Windows

| Parameter | Value |
|-----------|-------|
| Number | 4 (one per side) |
| Material | Polycarbonate |
| Thickness | 15 mm |
| Size | 0.4m × 0.3 m |
| UV protection | > 99% UV-A, UV-B |
| Visibility | > 90% visible light transmission |
| Warp radiation protection | Lead lining (0.5 mm) |

## 5. Passenger Briefing

### 5.1 Pre-Warp Briefing

Before each warp, passengers receive a briefing:

```
Pre-warp briefing:
  1. Warp sequence explanation (60 sec)
  2. Warp cocoon deployment (30 sec)
  3. Safety harness check (15 sec)
  4. Communication check (10 sec)
  5. Emergency procedure review (60 sec)
  6. Questions (60 sec)
  Total: 3.5 minutes
```

### 5.2 Emergency Procedures

Passengers are briefed on:
1. Warp abort procedure (automatic, no passenger action required)
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
| Emergency evacuation | Crew-assisted, warp cocoon provides protection |
| Medical equipment | AED, first aid kit, emergency medication |

### 6.2 Passenger Limitations

| Limitation | Reason | Mitigation |
|------------|--------|------------|
| Maximum passenger mass | 120 kg (warp payload limit) | Weight check before boarding |
| Maximum passenger height | 2.1 m (cocoon fit) | Height check before boarding |
| Minimum passenger age | 12 years (warp cocoon fit) | Age verification |
| Medical conditions | Heart condition, pregnancy, claustrophobia | Medical clearance required |
