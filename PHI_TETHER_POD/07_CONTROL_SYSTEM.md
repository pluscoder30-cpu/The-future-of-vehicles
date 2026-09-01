# PHI TETHER POD — Control System

## Control Architecture
The Tether Pod uses a minimalist, intuitive control system designed for single-operator use without training.

## Primary Interface
### Touch Ring Controller
- **Location:** Pod rim, accessible from seated position
- **Type:** Capacitive touch ring with haptic feedback
- **Functions:**
  - Rotate clockwise: Ascend (increase field strength)
  - Rotate counter-clockwise: Descend (decrease field strength)
  - Tap: Lock current altitude
  - Double-tap: Initiate controlled descent
  - Triple-tap: Emergency field kill

### Status Display
- **Type:** OLED ring embedded in pod rim
- **Information:**
  - Current altitude (0-50m)
  - Battery level (0-100%)
  - Field coherence (0-100%)
  - Time aloft
  - Wind speed and direction

## Automated Systems
### Altitude Hold
- Maintains set altitude within ±0.5m
- Compensates for wind drift automatically
- Adjustable by touching ring and rotating

### Auto-Descent
- Triggered by low battery (<10%)
- Controlled 0.5 m/s descent
- Touchdown detection and field release

### Obstacle Avoidance
- Ultrasonic sensors on pod bottom
- Detects ground proximity below 5m
- Auto-decelerates descent to 0.1 m/s

## Communication
- **Bluetooth 5.3:** Phone pairing for remote monitoring
- **LoRa:** Long-range telemetry (10km)
- **Emergency:** 433 MHz distress beacon (auto-activate on freefall)

## Mobile App
- Real-time altitude and battery monitoring
- Flight logging and history
- Field strength diagnostics
- Firmware updates over-the-air
