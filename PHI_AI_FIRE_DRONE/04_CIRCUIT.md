# PHI AI FIRE DRONE — CIRCUIT SCHEMATICS

## Avionics, AI, and Sensor Circuit Design

---

## MAIN CIRCUIT OVERVIEW

```
SYSTEM BLOCK DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  FPB-10     │────→│  POWER      │────→│  ARDUINO    │
  │  BATTERY    │     │  MANAGEMENT │     │  MEGA 2560  │
  │  24V 50Ah   │     │  5V/3.3V    │     │             │
  └─────────────┘     └─────────────┘     └──────┬──────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────┐
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   FLIGHT        │          │   FIRE          │    │   AI PROCESSOR  │
           │   SENSORS       │          │   SENSORS       │    │                 │
           │                 │          │                 │    │ - RPi Zero 2W   │
           │ - MPU6050       │          │ - MLX90614      │    │ - Pi Camera     │
           │ - BMP280        │          │ - Smoke Sensor  │    │ - AI Models     │
           │ - NEO-6M GPS   │          │ - 1080p Camera  │    │                 │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   MOTORS        │          │   RETARDANT     │    │   FREQUENCY     │
           │                 │          │   SYSTEM        │    │   GENERATOR     │
           │ - ESC1-4        │          │ - Pump          │    │ - PCM5102A      │
           └─────────────────┘          │ - Valves        │    │ - PAM8403       │
                                        └─────────────────┘    └─────────────────┘
```

---

## AI FIRE PREDICTION MODEL

```
FIRE SPREAD PREDICTION:
═══════════════════════════════════════════════════════════════

  INPUT FEATURES:
  ├── Wind speed (from BMP280 pressure changes)
  ├── Wind direction (from GPS drift analysis)
  ├── Temperature (from MLX90614 ambient)
  ├── Fire temperature (from MLX90614 object)
  ├── Fire size (from thermal image analysis)
  ├── Terrain slope (from barometric altitude changes)
  └── Time of day (from GPS time)

  AI MODEL (TensorFlow Lite):
  ┌──────────────────────────────────────┐
  │  Input Layer (7 features)            │
  │  Hidden Layer 1 (64 neurons, ReLU)   │
  │  Hidden Layer 2 (32 neurons, ReLU)   │
  │  Output: Spread vector (dx, dy, rate)│
  │                                      │
  │  Model size: ~100KB                  │
  │  Inference time: <200ms              │
  └──────────────────────────────────────┘

  AI OUTPUT:
  ├── Predicted spread direction (compass bearing)
  ├── Predicted spread rate (m/min)
  ├── Recommended drop zone
  └── Recommended retardant amount
```
