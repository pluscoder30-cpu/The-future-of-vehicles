# PHI HEALING DRONE — CONTROL SYSTEM

## Avionics, Flight Controller, and Autonomy

---

## FLIGHT CONTROLLER ARCHITECTURE

```
SYSTEM ARCHITECTURE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────┐
  │                    ARDUINO MEGA 2560                     │
  │                    (Main Flight Controller)              │
  │                                                         │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
  │  │  SENSOR  │  │  FLIGHT  │  │  MISSION │             │
  │  │  FUSION  │  │  CONTROL │  │  CONTROL │             │
  │  │          │  │          │  │          │             │
  │  │ IMU Data │→│ PID Loop │→│ Waypoint │             │
  │  │ GPS Data │  │ Motor Out│  │ Navigation│             │
  │  │ Baro Data│  │ Stabilize│  │ Medication│             │
  │  └──────────┘  └──────────┘  └──────────┘             │
  │       ↑              ↓              ↓                   │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
  │  │  INPUT   │  │  OUTPUT  │  │ COMMS    │             │
  │  │          │  │          │  │          │             │
  │  │ MPU6050  │  │ ESC1-4   │  │ WiFi     │             │
  │  │ BMP280   │  │ Servos   │  │ Telemetry│             │
  │  │ GPS      │  │ Frequency│  │ Buzzer   │             │
  │  │ Medical  │  │ Display  │  │ LED      │             │
  │  └──────────┘  └──────────┘  └──────────┘             │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

---

## FLIGHT MODES

| Mode | Description | Speed | Altitude | Control |
|------|-------------|-------|----------|---------|
| MANUAL | Full pilot control | 0-40 km/h | 0-120m | RC/Phone |
| STABILIZE | Auto-level, manual throttle | 0-30 km/h | 0-120m | RC/Phone |
| GPS HOLD | Position hold | 0 km/h | Set altitude | Auto |
| GPS RETURN | Return to home | 15 km/h | 30m | Auto |
| MISSION | Waypoint following | 25 km/h | Set altitude | Auto |
| LAND | Auto-land | 0 km/h | Descending | Auto |
| EMERGENCY | Motor shutdown | 0 km/h | Falling | None |

### Mode Transitions

```
MODE TRANSITION DIAGRAM:
═══════════════════════════════════════════════════════════════

                    ┌─────────┐
                    │  STABILIZE │ ← Default after boot
                    └────┬────┘
                         │
            ┌────────────┼────────────┐
            │            │            │
            ▼            ▼            ▼
      ┌──────────┐ ┌──────────┐ ┌──────────┐
      │  MANUAL  │ │ GPS HOLD │ │ MISSION  │
      └────┬─────┘ └────┬─────┘ └────┬─────┘
           │            │            │
           │     ┌──────┘     ┌──────┘
           │     │            │
           ▼     ▼            ▼
      ┌──────────┐     ┌──────────┐
      │ GPS      │     │   LAND   │
      │ RETURN   │     └──────────┘
      └────┬─────┘
           │
           ▼
      ┌──────────┐
      │ EMERGENCY│ ← Triggered by: low battery,
      └──────────┘   signal loss, or manual switch
```

---

## PID CONTROLLER

### Roll/Pitch Controller

```
STABILIZATION PID:
═══════════════════════════════════════════════════════════════

  Input: Desired angle (from RC or mission)
  Feedback: Actual angle (from MPU6050)

  error = desired_angle - actual_angle

  Output = Kp × error + Ki × ∫error × dt + Kd × d(error)/dt

  PHI-HARMONIC GAINS:
  ┌──────────────────────────────────────┐
  │  Kp = 4.5                            │
  │  Ki = 0.8 × φ = 1.294               │
  │  Kd = 2.2 / φ = 1.360               │
  │                                      │
  │  Loop rate: 618 Hz (1000/φ)         │
  │  Sample time: 1.62ms                 │
  └──────────────────────────────────────┘

  Output range: -500 to +500 (motor commands)
  Deadband: +/- 2° (no correction needed)
  Integrator limit: +/- 200 (anti-windup)
```

### Yaw Controller

```
YAW PID:
═══════════════════════════════════════════════════════════════

  Input: Desired heading (from RC or mission)
  Feedback: Actual heading (from MPU6050 magnetometer)

  PHI-HARMONIC GAINS:
  ┌──────────────────────────────────────┐
  │  Kp = 6.0                            │
  │  Ki = 1.0 × φ = 1.618               │
  │  Kd = 3.0 / φ = 1.854               │
  │                                      │
  │  Turn rate limit: 100°/sec           │
  │  Heading wrap-around handling        │
  └──────────────────────────────────────┘
```

### Altitude Controller

```
ALTITUDE PID:
═══════════════════════════════════════════════════════════════

  Input: Desired altitude (from RC or mission)
  Feedback: Actual altitude (from BMP280 barometer)

  PHI-HARMONIC GAINS:
  ┌──────────────────────────────────────┐
  │  Kp = 1.2                            │
  │  Ki = 0.3 × φ = 0.485               │
  │  Kd = 0.8 / φ = 0.494               │
  │                                      │
  │  Alt hold precision: +/- 0.5m       │
  │  Max climb rate: 3 m/s              │
  │  Max descend rate: 2 m/s            │
  └──────────────────────────────────────┘
```

---

## MOTOR MIXING

```
MOTOR MIX (QUADCOPTER X CONFIG):
═══════════════════════════════════════════════════════════════

  Motor Layout (TOP VIEW):
  ┌──────────────────────────────────────┐
  │                                      │
  │    M1 (CW)              M2 (CCW)    │
  │      ↻                    ↺          │
  │                                      │
  │              CENTER                  │
  │                                      │
  │    M3 (CCW)              M4 (CW)    │
  │      ↺                    ↻          │
  │                                      │
  └──────────────────────────────────────┘

  MIXING EQUATIONS:
  ─────────────────
  M1 = Throttle + Roll - Pitch + Yaw
  M2 = Throttle - Roll - Pitch - Yaw
  M3 = Throttle + Roll + Pitch - Yaw
  M4 = Throttle - Roll + Pitch + Yaw

  All values normalized to 0-1000 (ESC range)
  Idle speed: 1000 (motors spinning, no thrust)
  Max speed: 2000 (full thrust)
```

---

## GPS NAVIGATION

### Waypoint Mission

```
WAYPOINT FORMAT:
═══════════════════════════════════════════════════════════════

  Mission consists of waypoints:

  Waypoint 1: HOME (launch point)
    Lat: 40.7128° N
    Lon: 74.0060° W
    Alt: 10m
    Action: Takeoff

  Waypoint 2: PATIENT
    Lat: 40.7135° N
    Lon: 74.0055° W
    Alt: 30m
    Action: Hover, deliver medication

  Waypoint 3: HOME (return)
    Lat: 40.7128° N
    Lon: 74.0060° W
    Alt: 10m
    Action: Land

  NAVIGATION:
  ────────────
  - Follows GPS course to each waypoint
  - Maintains set altitude
  - Auto-advances to next waypoint when reached
  - Waypoint radius: 2m (switch when within)
  - Speed: 25 km/h cruise
```

### Return-to-Home

```
RTH SEQUENCE:
═══════════════════════════════════════════════════════════════

  Trigger: Low battery, signal loss, or manual RTH

  1. Climb to 30m altitude (if below)
  2. Turn toward home point
  3. Fly at 15 km/h toward home
  4. Descend to 10m when within 50m
  5. Hover 10 seconds (stabilize)
  6. Descend to 2m
  7. Hover 5 seconds (verify clear)
  8. Land and disarm motors

  SAFETY: If battery < 20%, skip hover phases
          and land immediately at current position
```

---

## MEDICAL MISSION AUTONOMY

### Auto-Delivery Sequence

```
MEDICATION DELIVERY AUTOMATION:
═══════════════════════════════════════════════════════════════

  1. Receive patient coordinates (WiFi/app)
  2. Auto-takeoff to 30m
  3. Navigate to patient GPS
  4. Descend to 3m AGL
  5. Hover and scan for patient (thermal/visual)
  6. Descend to 1m AGL
  7. Activate medical sensors
  8. Record patient vitals
  9. If vitals OK:
     - Activate frequency therapy (5 min)
     - Release medication bay
     - Wait 30 seconds
  10. If vitals critical:
      - Alert emergency services
      - Maintain position for first responders
  11. Ascend to 30m
  12. Return to base
  13. Auto-land
  14. Transmit mission report

  TOTAL AUTONOMOUS TIME: 20-40 minutes
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| Arm check | Any motor not responding | Prevent arming |
| GPS check | < 6 satellites | Prevent takeoff |
| Battery check | < 30% | Prevent takeoff |
| IMU check | Calibration failed | Prevent takeoff |
| Prop check | Vibration > threshold | Alert, reduce power |
| Geo-fence | > 500m from home | Auto RTH |
| Altitude | > 120m AGL | Auto descend |
| Low battery | < 20% | Auto RTH |
| Critical battery | < 10% | Auto land |
| Signal loss | No RC for 5 sec | Auto RTH |
| Signal loss | No RC for 30 sec | Auto land |
| Temperature | ESC > 80°C | Reduce power |
| Current | > 30A sustained | Reduce power |

---

## TELEMETRY DATA

### Transmitted Data (every 162ms — phi-harmonic interval)

```
TELEMETRY PACKET:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────────┐
  │  Byte 0-1: Header (0xAA 0x55)                       │
  │  Byte 2: Sequence number (phi-modulated)            │
  │  Byte 3-4: Battery voltage (mV)                     │
  │  Byte 5-6: Battery current (mA)                     │
  │  Byte 7-8: GPS latitude (0.0001°)                   │
  │  Byte 9-10: GPS longitude (0.0001°)                 │
  │  Byte 11-12: Altitude (0.1m)                        │
  │  Byte 13-14: Speed (0.1 m/s)                        │
  │  Byte 15: Satellites count                           │
  │  Byte 16: Flight mode                                │
  │  Byte 17-18: Heart rate (BPM)                        │
  │  Byte 19: SpO2 (%)                                   │
  │  Byte 20-21: Temperature (0.1°C)                     │
  │  Byte 22-23: ECG data (raw)                          │
  │  Byte 24-25: GPS heading (0.1°)                      │
  │  Byte 26: Medication bay status                      │
  │  Byte 27: Frequency generator status                 │
  │  Byte 28-29: Checksum (CRC16)                        │
  └──────────────────────────────────────────────────────┘

  Total: 30 bytes per packet
  Rate: 6.17 packets/second (1000/162)
  Data rate: 185 bytes/second
```

---

## COMMAND INTERFACE

### WiFi Commands (via ESP8266)

| Command | Description | Example |
|---------|-------------|---------|
| ARM | Arm motors | `ARM` |
| DISARM | Disarm motors | `DISARM` |
| TAKEOFF | Auto takeoff | `TAKEOFF 10` (10m) |
| LAND | Auto land | `LAND` |
| RTH | Return to home | `RTH` |
| WP | Set waypoint | `WP 40.7128 -74.0060 30` |
| FREQ | Start frequency | `FREQ 432 300` (432Hz, 300s) |
| STOP | Stop frequency | `STOP` |
| MEDS | Release medication | `MEDS 1` (compartment 1) |
| STATUS | Get status | `STATUS` |
| CALIBRATE | Calibrate sensors | `CALIBRATE` |

### Status Response

```
STATUS RESPONSE FORMAT:
═══════════════════════════════════════════════════════════════

  {
    "mode": "GPS_HOLD",
    "battery": {"voltage": 12.4, "current": 8.2, "soc": 85},
    "gps": {"lat": 40.7128, "lon": -74.0060, "alt": 30, "sats": 8},
    "sensors": {"hr": 72, "spo2": 98, "temp": 36.8},
    "motors": [1200, 1200, 1200, 1200],
    "frequency": null,
    "meds": {"bay1": true, "bay2": true, "bay3": true},
    "uptime": 1800
  }
```
