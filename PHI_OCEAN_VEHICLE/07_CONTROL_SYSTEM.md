# PHI OCEAN VEHICLE — Control System

## Control Architecture
The Ocean Vehicle uses a fly-by-wire control system with phi-harmonic haptic feedback. All helm inputs are processed by the navigation computer and translated to thruster and field commands.

## Primary Controls

### Helm Wheel
- **Type:** Compact wheel with force feedback
- **Function:** Steering (lateral thrusters)
- **Phase Integration:** Steering scales with field strength

### Throttle
- **Type:** Lever (starboard side)
- **Function:** Forward/reverse thrust
- **Phase Integration:** Speed scales with drag reduction

### Depth Control
- **Type:** Joystick (port side)
- **Function:** Surface/subsurface transition
- **Station Lock:** Center position maintains depth

### Field Engage
- **Type:** Toggle switch
- **Function:** Engages/disengages drag reduction
- **Safety:** Requires speed <5 km/h and depth check

## Dashboard Display
- **Type:** 12-inch OLED, marine-rated
- **Information:**
  - Speed (knots)
  - Depth and draft
  - Battery level and range
  - Drag reduction field status
  - Navigation chart
  - Weather and sea state
  - Camera feeds (360 degrees)

## Driving Modes
| Mode | Description | Field | Speed |
|------|-------------|-------|-------|
| Eco | Maximum range | Reduced | 0-30 km/h |
| Normal | Balanced | Full | 0-50 km/h |
| Sport | Full power | Full | 0-80 km/h |
| Subsurface | Underwater | Full | 0-40 km/h |
| Station | Hold position | Reduced | 0 km/h |

## Automated Systems
### Auto-Helm
- Maintains heading via GPS waypoints
- Corrects for wind and current
- Manual override via helm wheel

### Auto-Depth (Subsurface)
- Maintains set depth within +/-0.5m
- Compensates for currents
- Adjustable via depth joystick

### Collision Avoidance
- Radar and sonar detect obstacles
- Auto-decelerates within 100m
- Alerts helm to hazards
- Auto-avoidance in autonomous mode

## Communication
- **VHF Radio:** Marine standard (15 km)
- **AIS:** Automatic identification system
- **Bluetooth:** Phone pairing (surface only)
- **Satellite:** Optional Iridium (global)
- **Emergency:** 433 MHz + EPIRB

## Mobile App
- Real-time navigation and tracking
- Weather and sea state monitoring
- Field skimmer diagnostics
- Firmware updates (surface only)
- Remote monitoring
