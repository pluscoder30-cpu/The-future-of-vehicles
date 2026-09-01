# PHI SUBMERSIBLE — Control System

## Control Architecture
The Submersible uses a fly-by-wire control system with phi-harmonic haptic feedback. All pilot inputs are processed by the dive computer and translated to field array commands.

## Primary Controls

### Thrust Controller
- **Type:** Joystick (right hand)
- **Function:** Forward/reverse, lateral movement
- **Phase Integration:** Speed scales with field strength

### Depth Controller
- **Type:** Joystick (left hand)
- **Function:** Pitch control, depth adjustment
- **Station Lock:** Center position holds depth

### Field Engage
- **Type:** Toggle switch
- **Function:** Engages/disengages field skimmer
- **Safety:** Requires depth >1m and ballast check

### Emergency Ascent
- **Type:** Red pull handle
- **Function:** Instant full-power ascent
- **Override:** Works even with main power failure

## Dashboard Display
- **Type:** 10-inch OLED, pressure-rated
- **Information:**
  - Depth and pressure
  - Speed and heading
  - Battery level and endurance
  - Field skimmer status
  - Ballast status
  - External camera feeds
  - Life support status

## Dive Modes
| Mode | Description | Field | Depth |
|------|-------------|-------|-------|
| Surface | Boat mode | Off | 0-1m |
| Transit | Fast underwater | Full | 0-500m |
| Explore | Slow, precise | Reduced | 0-500m |
| Station | Hold position | Reduced | Any |
| Emergency | Ascent/descent | Max | Any |

## Automated Systems
### Auto-Depth
- Maintains set depth within +/-0.5m
- Compensates for currents automatically
- Adjustable by joystick input

### Auto-Heading
- Maintains compass heading
- Corrects for drift
- Manual override via joystick

### Obstacle Avoidance
- Sonar array detects obstacles
- Auto-decelerates within 10m
- Alerts pilot to hazards

## Communication
- **Acoustic modem:** 10 km range (underwater)
- **Bluetooth:** Surface only (paired devices)
- **Hardwire:** Umbilical option (unlimited range)
- **Emergency:** 433 MHz beacon (surface only)

## Mobile App
- Dive logging and history
- Real-time depth/speed monitoring
- Field skimmer diagnostics
- Firmware updates (surface only)
