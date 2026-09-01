# PHI Pharmacy Drone - Design Document

## 1. Design Philosophy
The PHI Pharmacy Drone prioritizes:
- Medication integrity (temperature, light, humidity)
- Accurate dosage delivery
- Chain of custody compliance
- Patient safety (allergy/interaction checks)
- Rapid delivery for time-sensitive medications

## 2. Structural Design

### 2.1 Frame
- **Material**: Lightweight carbon fiber composite
- **Configuration**: Quadcopter (4 rotors)
- **Weight**: 6 kg (without payload)
- **Dimensions**: 0.8m x 0.8m x 0.4m
- **IP Rating**: IP54 (dust/splash resistant)

### 2.2 Medication Storage Bay
```
┌─────────────────────────────────────────┐
│         MEDICATION STORAGE BAY          │
│  ┌─────────────────────────────────┐    │
│  │    REFRIGERATED ZONE (2-8C)     │    │
│  │  ┌───┬───┬───┬───┬───┬───┬───┐ │    │
│  │  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ │    │
│  │  ├───┼───┼───┼───┼───┼───┼───┤ │    │
│  │  │ 8 │ 9 │10 │11 │12 │13 │14 │ │    │
│  │  └───┴───┴───┴───┴───┴───┴───┘ │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │    AMBIENT ZONE (15-25C)        │    │
│  │  ┌───┬───┬───┬───┬───┐          │    │
│  │  │15 │16 │17 │18 │19 │20       │    │
│  │  └───┴───┴───┴───┴───┘          │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │    DISPENSING ROBOTIC ARM        │    │
│  │  (Picks, verifies, delivers)    │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

## 3. Propulsion

| Component | Specification |
|-----------|---------------|
| Motors | 4x T-Motor F40 Pro II |
| Propellers | 10-inch carbon fiber |
| Total Power | 3 kW max |
| Battery | FPB-5 (5kWh) |
| Range | 40 km loaded |
| Cruise Speed | 60 km/h |

## 4. Medication Systems

### 4.1 Temperature Control
| Zone | Range | Method | Accuracy |
|------|-------|--------|----------|
| Refrigerated | 2-8C | Peltier + fan | +/- 0.5C |
| Ambient | 15-25C | Insulation + heater | +/- 1C |

### 4.2 Inventory Management
- 20 individual slots with RFID tags
- Barcode scanner for verification
- Real-time inventory tracking
- Expiry date monitoring
- Temperature logging per slot

### 4.3 Dosage Calculator
- Patient weight-based dosing
- Allergy cross-reference
- Drug interaction checking
- Age/renal/hepatic adjustments
- Maximum dose limits

## 5. Navigation & Control

### 5.1 AI Navigation
- GPS/GNSS with RTK
- Visual SLAM for last-meter delivery
- Obstacle avoidance (LiDAR + cameras)
- Weather-aware routing
- Priority-based dispatch

### 5.2 Delivery System
- Robotic arm with gripper
- Barcode verification before drop
- Secure drop box compatible
- Photo confirmation of delivery
- Patient notification via app

## 6. Safety Systems
- Dual flight controllers
- Parachute recovery
- Tamper-evident locks
- Emergency medication return
- Controlled substance security

## 7. Cost Breakdown
| Category | Cost |
|----------|------|
| Frame & Structure | $40 |
| Propulsion | $60 |
| Battery (FPB-5) | $50 |
| Flight Controllers | $40 |
| Temperature Control | $50 |
| Medication Storage | $40 |
| Robotic Arm | $40 |
| Navigation & Sensors | $30 |
| Communication | $15 |
| Safety Systems | $15 |
| Phi-Harmonic System | $20 |
| Assembly & Testing | $25 |
| **Total** | **$400** |
