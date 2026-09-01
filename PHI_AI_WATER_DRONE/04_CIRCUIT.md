# PHI AI WATER DRONE — CIRCUIT SCHEMATICS

## Avionics, AI, and Water Sensor Circuits

---

## MAIN CIRCUIT OVERVIEW

```
SYSTEM BLOCK DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  FPB-5      │────→│  POWER      │────→│  ARDUINO    │
  │  BATTERY    │     │  MANAGEMENT │     │  MEGA 2560  │
  └─────────────┘     └─────────────┘     └──────┬──────┘
                                                 │
           ┌──────────────┬──────────────┬────────┴────────┐
           │              │              │                  │
     ┌─────┴─────┐ ┌─────┴─────┐ ┌─────┴─────┐ ┌────────┴────────┐
     │  FLIGHT   │ │  WATER    │ │FILTRATION │ │  AI PROCESSOR   │
     │  SENSORS  │ │  SENSORS  │ │  SYSTEM   │ │                 │
     │           │ │           │ │           │ │ - RPi Zero 2W   │
     │ - MPU6050 │ │ - pH      │ │ - Pump    │ │ - Pi Camera     │
     │ - BMP280  │ │ - Turbid  │ │ - Valves  │ │ - AI Models     │
     │ - GPS     │ │ - TDS     │ │ - Filters │ │                 │
     └───────────┘ └───────────┘ └───────────┘ └─────────────────┘
```

---

## AI CONTAMINATION MAPPING MODEL

```
CONTAMINATION MAP GENERATION:
═══════════════════════════════════════════════════════════════

  INPUTS:
  ├── pH reading (0-14 scale)
  ├── Turbidity (NTU)
  ├── TDS (ppm)
  ├── Temperature (°C)
  ├── GPS position
  └── Camera image (water color)

  AI MODEL:
  ┌──────────────────────────────────────┐
  │  Contamination Classifier            │
  │  Input: 6 features                   │
  │  Hidden: 32 neurons                  │
  │  Output: Contamination level (0-5)  │
  │  + Pollutant type (chemical/organic/sediment)│
  │  Model size: ~30KB                   │
  │  Inference time: <50ms               │
  └──────────────────────────────────────┘

  AI OUTPUT:
  ├── Contamination heatmap (real-time)
  ├── Pollutant classification
  ├── Recommended cleaning priority
  └── Estimated cleaning time
```
