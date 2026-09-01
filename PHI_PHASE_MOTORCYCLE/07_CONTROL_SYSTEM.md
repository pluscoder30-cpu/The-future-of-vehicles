# PHI PHASE MOTORCYCLE — Control System

## Control Architecture
The Phase Motorcycle uses a fly-by-wire control system with phi-harmonic haptic feedback. All rider inputs are processed by the flight computer and translated to actuator commands.

## Primary Controls

### Throttle
- **Type:** Twist grip with haptic feedback
- **Function:** Controls drive motor power (0-100%)
- **Phase Integration:** Full throttle + phase button engages phase mode

### Phase Button
- **Location:** Left handlebar, thumb-accessible
- **Function:** Engages/disengages phase shift
- **Safety:** Requires simultaneous throttle >50% to activate
- **Haptic Feedback:** Strong vibration on engage, pulse on phase windows

### Brake Levers
- **Front:** Regenerative braking (70% energy recovery)
- **Rear:** Regenerative + ceramic disc (emergency stop)
- **Phase Mode:** Brakes auto-disengage during phase transit

### Steering
- **Type:** Conventional handlebar
- **Phase Mode:** Steering assist reduces effort by 50% during phase transit

## Dashboard Display
- **Type:** 5-inch OLED, integrated into fairing
- **Information:**
  - Speed (km/h)
  - Battery level and range
  - Phase coil status and cooldown
  - Navigation turn-by-turn
  - Barrier pre-scan results
  - Rider mode selection

## Riding Modes
| Mode | Description | Power | Phase |
|------|-------------|-------|-------|
| Eco | Maximum range, gentle acceleration | 50% | Disabled |
| Normal | Balanced performance | 75% | Available |
| Sport | Full power, aggressive response | 100% | Available |
| Phase | Optimized for barrier transit | 100% | Active |

## Automated Systems
### Auto-Phase
- Detects barrier ahead via ultrasonic pre-scan
- Automatically initiates phase sequence if rider confirms
- Adjusts speed for optimal transit timing
- Disengages phase after confirmed passage

### Lane Assist
- Monitors lane position via cameras
- Gentle haptic feedback for lane departure
- Auto-corrects during phase transit

### Night Vision
- Infrared camera projects to dashboard display
- Overlays on forward view
- Auto-activates in low-light conditions

## Mobile App Integration
- Real-time ride telemetry
- Phase usage logging and statistics
- Firmware updates over-the-air
- Remote diagnostics
- Ride history and GPS tracks
