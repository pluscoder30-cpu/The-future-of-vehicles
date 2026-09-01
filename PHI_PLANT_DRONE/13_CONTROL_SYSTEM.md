# PHI PLANT DRONE — CONTROL SYSTEM

## Avionics, Flight Controller, and Autonomy

---

## FLIGHT CONTROLLER

```
SYSTEM ARCHITECTURE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────┐
  │                    ARDUINO MEGA 2560                     │
  │                                                         │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
  │  │  SENSOR  │  │  FLIGHT  │  │  MISSION │             │
  │  │  FUSION  │  │  CONTROL │  │  CONTROL │             │
  │  │ IMU+GPS  │→│ PID Loop │→│ Planting │             │
  │  │ Baro     │  │ Motor Out│  │ Grid Nav │             │
  │  └──────────┘  └──────────┘  └──────────┘             │
  │       ↑              ↓              ↓                   │
  │  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
  │  │  INPUT   │  │  OUTPUT  │  │ COMMS    │             │
  │  │ Soil     │  │ ESC1-4   │  │ WiFi     │             │
  │  │ Light    │  │ Seed svc │  │ Telemetry│             │
  │  │ Temp     │  │ Pump     │  │ Buzzer   │             │
  │  └──────────┘  └──────────┘  └──────────┘             │
  └─────────────────────────────────────────────────────────┘
```

---

## FLIGHT MODES

| Mode | Description | Speed | Control |
|------|-------------|-------|---------|
| MANUAL | Full pilot control | 0-35 km/h | RC/Phone |
| STABILIZE | Auto-level | 0-25 km/h | RC/Phone |
| GPS HOLD | Position hold | 0 km/h | Auto |
| GPS RETURN | Return to home | 15 km/h | Auto |
| PLANTING | Grid pattern | 5 km/h | Auto |
| WATERING | Hover and spray | 0 km/h | Auto |
| FREQUENCY | Hover and emit | 0 km/h | Auto |
| LAND | Auto-land | Descending | Auto |

---

## PLANTING AUTONOMY

```
AUTO-PLANTING SEQUENCE:
═══════════════════════════════════════════════════════════════

  1. Receive planting area coordinates (WiFi/app)
  2. Auto-takeoff to 10m
  3. Navigate to area start point
  4. Descend to 1.5m AGL
  5. Begin grid pattern:
     For each grid point:
     a. Hover over point
     b. Drop seeds (2 sec)
     c. Spray water (3 sec)
     d. Apply frequency (5 sec)
     e. Move to next point
  6. Complete grid
  7. Ascend to 10m
  8. Return to base
  9. Auto-land
  10. Transmit mission report

  COVERAGE: 500m² per hour
  TOTAL AUTONOMOUS TIME: 1-5 hours (area dependent)
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| Arm check | Motor not responding | Prevent arming |
| GPS check | < 6 satellites | Prevent takeoff |
| Battery check | < 30% | Prevent takeoff |
| Water check | Tank empty | Disable spray |
| Seed check | Hopper empty | Disable dispenser |
| Geo-fence | > 500m from home | Auto RTH |
| Altitude | > 120m AGL | Auto descend |
| Low battery | < 20% | Auto RTH |
| Critical battery | < 10% | Auto land |
| Signal loss | No RC for 30 sec | Auto land |

---

## TELEMETRY

### Data Packet (every 162ms)

```
TELEMETRY PACKET:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────────┐
  │  Byte 0-1: Header (0xAA 0x55)                       │
  │  Byte 2: Sequence number                             │
  │  Byte 3-4: Battery voltage (mV)                     │
  │  Byte 5-6: GPS latitude                             │
  │  Byte 7-8: GPS longitude                            │
  │  Byte 9-10: Altitude                                │
  │  Byte 11-12: Speed                                  │
  │  Byte 13: Satellites                                │
  │  Byte 14: Flight mode                               │
  │  Byte 15-16: Soil moisture 1                        │
  │  Byte 17-18: Soil moisture 2                        │
  │  Byte 19-20: Light level                            │
  │  Byte 21-22: Temperature                            │
  │  Byte 23: Seed hopper level                         │
  │  Byte 24: Water tank level                          │
  │  Byte 25-26: Checksum (CRC16)                       │
  └──────────────────────────────────────────────────────┘
```

---

## COMMAND INTERFACE

### WiFi Commands

| Command | Description | Example |
|---------|-------------|---------|
| ARM | Arm motors | `ARM` |
| DISARM | Disarm | `DISARM` |
| TAKEOFF | Auto takeoff | `TAKEOFF 10` |
| LAND | Auto land | `LAND` |
| RTH | Return home | `RTH` |
| PLANT | Start planting | `PLANT 40.7128 -74.0060 10 10` |
| WATER | Start watering | `WATER ON` |
| FREQ | Start frequency | `FREQ 432 300` |
| STATUS | Get status | `STATUS` |
