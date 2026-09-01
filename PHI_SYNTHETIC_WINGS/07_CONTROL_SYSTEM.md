# PHI SYNTHETIC WINGS — Control System

## Control Architecture
The Synthetic Wings use a body-motion control system — the wearer controls the wings through natural arm and body movements. The flight computer translates these movements into wing commands.

## Primary Controls

### Arm Movement
- **Forward:** Nose down, forward flight
- **Back:** Nose up, climb
- **Left Arm Up:** Bank right
- **Right Arm Up:** Bank left
- **Both Arms Neutral:** Hover/level flight
- **Flapping Intensity:** Altitude control

### Wrist Rotation
- **Left Wrist Left:** Yaw left
- **Left Wrist Right:** Yaw right
- **Right Wrist Left:** Yaw left
- **Right Wrist Right:** Yaw right

### Body Lean
- **Forward Lean:** Accelerate
- **Back Lean:** Decelerate
- **Side Lean:** Assist bank turns

## Control Modes
| Mode | Description | Control |
|------|-------------|---------|
| Beginner | Stabilized, limited angles | Auto-level, max 30 deg bank |
| Intermediate | Full control, some assist | Auto-level, full bank range |
| Expert | No assist, full manual | Full manual control |
| Hover | Station-keeping | Auto-hover, altitude hold |
| Auto | Autonomous flight | GPS waypoint navigation |

## Flight Computer
- **Type:** Neuromorphic AI processor
- **Function:** Translates body motion to wing commands
- **Stability:** Auto-levels in Beginner mode
- **Navigation:** GPS waypoint following (Auto mode)
- **Safety:** Auto-descent on power failure
- **Learning:** Adapts to wearer's flying style

## Dashboard
- **Type:** Heads-up display (projected on visor)
- **Information:**
  - Altitude
  - Speed
  - Heading
  - Battery level and range
  - Wind speed and direction
  - Stall warning
  - Navigation waypoints

## Communication
- **Bluetooth:** Phone pairing (ground only)
- **LoRa:** Long-range telemetry (10 km)
- **Emergency:** 433 MHz distress beacon
- **Intercom:** Wing-to-wing communication (optional)
