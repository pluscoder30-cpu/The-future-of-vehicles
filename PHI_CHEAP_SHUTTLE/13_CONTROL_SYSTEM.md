# PHI CHEAP SHUTTLE — CONTROL SYSTEM

## Avionics, Flight Computer, and Control Surfaces

---

## FLIGHT COMPUTER ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FLIGHT COMPUTER ARCHITECTURE                      │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    ARDUINO MEGA 2560 (Primary)                │  │
│  │                                                               │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │  │
│  │  │ SENSOR  │  │ SENSOR  │  │ SENSOR  │  │ SENSOR  │        │  │
│  │  │ INPUT   │  │ INPUT   │  │ INPUT   │  │ INPUT   │        │  │
│  │  │ (A0-A11)│  │ (D2-D9) │  │ (I2C)   │  │ (Serial)│        │  │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │  │
│  │       │            │            │            │               │  │
│  │       └────────────┴──────┬─────┴────────────┘               │  │
│  │                           │                                  │  │
│  │                    ┌──────┴──────┐                           │  │
│  │                    │  PROCESSING │                           │  │
│  │                    │   CORE      │                           │  │
│  │                    │             │                           │  │
│  │                    │  ┌────────┐ │                           │  │
│  │                    │  │ Main   │ │ ← 100 Hz loop            │  │
│  │                    │  │ Loop   │ │                           │  │
│  │                    │  └────────┘ │                           │  │
│  │                    │  ┌────────┐ │                           │  │
│  │                    │  │ Safety │ │ ← 1000 Hz watchdog       │  │
│  │                    │  │ Monitor│ │                           │  │
│  │                    │  └────────┘ │                           │  │
│  │                    │  ┌────────┐ │                           │  │
│  │                    │  │ Phi-H  │ │ ← 161.8 Hz phi loop     │  │
│  │                    │  │ Loop   │ │                           │  │
│  │                    │  └────────┘ │                           │  │
│  │                    └──────┬──────┘                           │  │
│  │                           │                                  │  │
│  │       ┌───────────┬───────┴───────┬───────────┐             │  │
│  │       │           │               │           │             │  │
│  │  ┌────┴────┐ ┌────┴────┐ ┌───────┴──┐ ┌─────┴─────┐       │  │
│  │  │ THRUST │ │ SERVO   │ │ COMMS    │ │ DISPLAY   │       │  │
│  │  │ CONTROL│ │ CONTROL │ │ CONTROL  │ │ CONTROL   │       │  │
│  │  │ (PWM)  │ │ (I2C)   │ │ (Serial) │ │ (I2C)     │       │  │
│  │  └────────┘ └─────────┘ └──────────┘ └───────────┘       │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    ARDUINO MEGA 2560 (Backup)                 │  │
│  │                                                               │  │
│  │  Duplicate of primary computer                               │  │
│  │  Independent power supply                                    │  │
│  │  Cross-checks primary outputs                                │  │
│  │  Takes over if primary fails                                 │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## SENSOR SUITE

### Navigation Sensors

| Sensor | Model | Qty | Purpose | Accuracy |
|--------|-------|-----|---------|----------|
| GPS | BN-880 (u-blox) | 1 | Position, altitude, velocity | ±2.5m position, ±0.1m/s velocity |
| Barometric Altimeter | BMP388 | 2 | Altitude (backup) | ±0.5m (0-10m), ±1m (10-100m) |
| IMU | MPU-9250 | 2 | Attitude (pitch, roll, yaw) | ±0.1° static, ±1° dynamic |
| Magnetometer | MPU-9250 (integrated) | 2 | Heading | ±1° |

### Vehicle Health Sensors

| Sensor | Model | Qty | Purpose | Range |
|--------|-------|-----|---------|-------|
| Voltage Monitor | Digital 0-50V | 4 | Battery voltage | 0-50V ±0.1V |
| Current Sensor | ACS712 30A | 4 | Thruster current | 0-30A ±0.1A |
| Temperature | LM35 | 4 | Thruster temperature | -55°C to +150°C |
| Accelerometer | MPU-9250 | 2 | G-force measurement | ±16g |

---

## CONTROL MODES

### Mode 1: Manual (Pilot Control)
- Pilot uses toggle switches and pushbuttons
- Thrust: 4-position switch (off, low, medium, full)
- Vectoring: 2-axis joystick (pitch/yaw)
- All other systems automated

### Mode 2: Assisted (Semi-Automatic)
- Arduino controls thrust profile
- Pilot controls vectoring
- Automated safety monitoring
- Auto-shutdown on anomaly

### Mode 3: Full Automatic
- Arduino controls entire flight profile
- Takeoff to apogee to landing
- Pilot can override at any time
- Emergency procedures automated

---

## FLIGHT CONTROL SOFTWARE

### Main Loop (100 Hz)
```
1. Read all sensors
2. Calculate vehicle state (position, velocity, attitude)
3. Check safety limits
4. Execute flight phase logic
5. Command thrusters
6. Command servos
7. Update displays
8. Log data to SD card
9. Transmit telemetry
```

### Safety Monitor (1000 Hz, hardware interrupt)
```
1. Check battery voltage (per cell)
2. Check thruster current (per thruster)
3. Check temperature (per thruster)
4. Check G-forces
5. Check altitude limits
6. Check communication status
7. Execute emergency shutdown if any limit exceeded
```

### Phi-Harmonic Loop (161.8 Hz, timer interrupt)
```
1. Update thruster PWM phase (phi-harmonic pattern)
2. Modulate power switching frequency
3. Optimize resonant tank drive
4. Log phi-harmonic performance metrics
```

---

## FLIGHT PHASES

### Phase 1: Pre-Flight (Ground)
- Power-on self-test (POST)
- Sensor calibration
- GPS fix acquisition
- Communication check
- Arm thrusters
- Wait for launch command

### Phase 2: Takeoff (0-30 seconds)
- Full thrust (4× 500N = 2000N)
- Climb at 45° angle
- Target: 100 m/s, 500m altitude

### Phase 3: Boost (30 seconds - 4 minutes)
- Maintain full thrust
- Pitch to 60° climb angle
- Target: 1000 m/s, 80 km altitude
- Monitor max-Q (maximum dynamic pressure)

### Phase 4: Coast (4-7 minutes)
- Engine cutoff at 80 km
- Ballistic arc to 100 km apogee
- Avionics-only power
- Coast to apogee

### Phase 5: Reentry (7-10 minutes)
- Partial thrust for deceleration
- Pitch to 0° (level flight)
- Monitor heating
- Target: 200 m/s at 10 km

### Phase 6: Descent (10-12 minutes)
- Parachute deployment at 10 km
- Controlled descent
- Target: 30 m/s at ground contact

### Phase 7: Landing
- Touchdown at 30 m/s
- Roll-out to stop
- Engine shutdown
- Data download

---

## DISPLAY SYSTEM

### Cockpit Displays

| Display | Size | Location | Data Shown |
|---------|------|----------|------------|
| Primary (OLED) | 1.3" I2C | Pilot panel | Altitude, speed, heading |
| Secondary (OLED) | 1.3" I2C | Passenger panel | Battery, temperature, status |
| LED Strip | 12V | Cockpit frame | Mode indication (green/yellow/red) |

### Display Data

**Primary Display:**
- Altitude: 0-100 km (digital + bar graph)
- Speed: 0-1200 m/s (digital + bar graph)
- Heading: 0-360° (compass rose)
- G-Force: ±10g (digital)
- Flight Phase: Text indicator

**Secondary Display:**
- Battery 1-4: Voltage (digital)
- Thruster 1-4: Current (digital)
- Temperature 1-4: °C (digital)
- System Status: OK/Warning/Fault
- Time: Mission clock

---

## COMMUNICATION SYSTEM

### Primary: VHF Radio (×2)
- Frequency: 136-174 MHz
- Power: 5W
- Range: 50 km (line of sight)
- Purpose: Voice communication with ground

### Secondary: HC-12 Telemetry (×2)
- Frequency: 433 MHz
- Power: 20 mW
- Range: 1800m (open air)
- Purpose: Data telemetry downlink
- Data: GPS, altitude, speed, battery, temperature

### Tertiary: GPS Beacon
- Frequency: 121.5 MHz (emergency locator)
- Purpose: Emergency location
- Activation: Automatic on crash detection

---

## EMERGENCY SYSTEMS

### Emergency Shutdown
- Trigger: Manual (red button) or automatic (sensor limits)
- Action: Cut all thruster power, deploy parachutes
- Response time: <100ms

### Parachute Deployment
- Trigger: Manual (pull cable) or automatic (altitude < 10 km + rate of descent > 50 m/s)
- Action: Release quick-release pins, deploy parachutes
- Descent rate: 25 fps (7.6 m/s) with both parachutes

### Emergency Locator
- Trigger: Crash detection (accelerometer > 10g)
- Action: Activate 121.5 MHz beacon
- Battery: 9V alkaline (independent)
- Duration: 48 hours

---

## WEIGHT BUDGET

| Component | Weight |
|-----------|--------|
| Arduino Mega (×2) | 0.1 kg |
| GPS Module | 0.02 kg |
| IMU (×2) | 0.02 kg |
| Altimeter (×2) | 0.02 kg |
| OLED Displays (×2) | 0.05 kg |
| VHF Radios (×2) | 0.6 kg |
| HC-12 Telemetry (×2) | 0.04 kg |
| Servos (×4) | 2.0 kg |
| Relay Modules (×2) | 0.1 kg |
| Wiring Harness | 1.5 kg |
| Connectors | 0.3 kg |
| Switches & Buttons | 0.2 kg |
| LEDs & Buzzers | 0.1 kg |
| **TOTAL AVIONICS** | **5.06 kg** |
