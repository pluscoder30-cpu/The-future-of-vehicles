# PHI AI HEALING DRONE — CIRCUIT SCHEMATICS

## Avionics, AI Processor, and Sensor Circuit Design

---

## MAIN CIRCUIT OVERVIEW

```
SYSTEM BLOCK DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  FPB-5      │────→│  POWER      │────→│  ARDUINO    │
  │  BATTERY    │     │  MANAGEMENT │     │  MEGA 2560  │
  │  12V 50Ah   │     │  5V/3.3V    │     │             │
  └─────────────┘     └─────────────┘     └──────┬──────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────┐
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   FLIGHT        │          │   MEDICAL       │    │   AI PROCESSOR  │
           │   SENSORS       │          │   SENSORS       │    │                 │
           │                 │          │                 │    │ - RPi Zero 2W   │
           │ - MPU6050       │          │ - MAX30102      │    │ - Pi Camera     │
           │ - BMP280        │          │ - DS18B20 x2   │    │ - AI Models     │
           │ - NEO-6M GPS   │          │ - AD8232 ECG   │    │                 │
           │ - BMP180        │          │ - OLED Display  │    │                 │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   MOTORS        │          │   COMMS         │    │   FREQUENCY     │
           │                 │          │                 │    │   GENERATOR     │
           │ - ESC1 (M1)     │          │ - ESP8266 WiFi  │    │ - PCM5102A DAC  │
           │ - ESC2 (M2)     │          │ - HC-12 Radio   │    │ - PAM8403 AMP   │
           │ - ESC3 (M3)     │          │ - Buzzer        │    │ - Transducers   │
           │ - ESC4 (M4)     │          │                 │    │                 │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
```

---

## AI PROCESSOR CIRCUIT

```
RASPBERRY PI ZERO 2W:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────┐
  │              RASPBERRY PI ZERO 2W                   │
  │                                                     │
  │  Power:                                             │
  │  5V ────────→ 5V Regulated Supply (3A capable)     │
  │  GND ───────→ Common Ground (star)                 │
  │                                                     │
  │  Serial to Arduino:                                 │
  │  GPIO 14 (TX) ──→ Arduino RX1 (Pin 19)             │
  │  GPIO 15 (RX) ←── Arduino TX1 (Pin 18)             │
  │                                                     │
  │  Camera:                                            │
  │  CSI Port ─────→ Pi Camera Module                  │
  │  Resolution: 1080p @ 30fps                         │
  │  Purpose: Wound/visual assessment                  │
  │                                                     │
  │  Storage:                                           │
  │  MicroSD ──────→ 32GB (AI models, OS, logs)       │
  │                                                     │
  │  Debug:                                             │
  │  Mini HDMI ────→ (optional debug monitor)          │
  │  Micro USB ────→ (power + serial console)          │
  │                                                     │
  │  AI Software:                                       │
  │  - TensorFlow Lite (injury classification)         │
  │  - OpenCV (wound detection)                        │
  │  - Custom treatment recommendation engine          │
  │  - Multi-drone coordination protocol               │
  │                                                     │
  └─────────────────────────────────────────────────────┘

  POWER CONSUMPTION:
  ──────────────────
  Idle: 0.4W
  AI Inference: 1.5W
  Camera Active: 0.8W
  Total AI System: ~2.7W max
```

---

## AI COMMUNICATION PROTOCOL

```
ARDUINO ↔ PI ZERO SERIAL PROTOCOL:
═══════════════════════════════════════════════════════════════

  Arduino → Pi Zero (Sensor Data):
  ┌──────────────────────────────────────────────────────┐
  │  Byte 0: Header (0xAA)                              │
  │  Byte 1: Heart Rate (BPM)                           │
  │  Byte 2: SpO2 (%)                                   │
  │  Byte 3-4: Temperature (0.1°C)                      │
  │  Byte 5-6: ECG Peak (raw)                           │
  │  Byte 7-10: GPS Lat (float)                         │
  │  Byte 11-14: GPS Lon (float)                        │
  │  Byte 15-16: Altitude (dm)                          │
  │  Byte 17: Battery SoC (%)                           │
  │  Byte 18: Motor Status                              │
  │  Byte 19: Checksum (XOR)                            │
  └──────────────────────────────────────────────────────┘

  Pi Zero → Arduino (AI Recommendations):
  ┌──────────────────────────────────────────────────────┐
  │  Byte 0: Header (0x55)                              │
  │  Byte 1: Diagnosis Code (0=ok, 1=mild, 2=moderate, 3=critical)
  │  Byte 2: Recommended Treatment                      │
  │  Byte 3: Recommended Frequency                      │
  │  Byte 4: Treatment Duration (minutes)               │
  │  Byte 5: Medication Bay Command                     │
  │  Byte 6: Drone Coordination Request                 │
  │  Byte 7: Confidence Score (0-100%)                  │
  │  Byte 8: Checksum (XOR)                             │
  └──────────────────────────────────────────────────────┘
```

---

## AI DIAGNOSIS ENGINE

```
INJURY CLASSIFICATION MODEL:
═══════════════════════════════════════════════════════════════

  INPUT FEATURES (from sensors):
  ├── Heart Rate (BPM)
  ├── SpO2 (%)
  ├── Temperature (°C)
  ├── ECG waveform features
  ├── Pain level (verbal scale 1-10)
  ├── Wound visual features (from camera)
  └── Patient age group

  AI MODEL (TensorFlow Lite):
  ┌──────────────────────────────────────┐
  │  Input Layer (7 features)            │
  │  Hidden Layer 1 (32 neurons, ReLU)   │
  │  Hidden Layer 2 (16 neurons, ReLU)   │
  │  Output Layer (4 classes)            │
  │                                      │
  │  Classes:                            │
  │  0: No treatment needed              │
  │  1: Minor (basic first aid)          │
  │  2: Moderate (medication + freq)     │
  │  3: Critical (alert emergency svc)   │
  │                                      │
  │  Model size: ~50KB                   │
  │  Inference time: <100ms              │
  │  Accuracy: ~85% (trained on synthetic data) │
  └──────────────────────────────────────┘
```

---

## CAMERA CIRCUIT

```
PI CAMERA MODULE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │          Pi Camera Module           │
  │                                     │
  │  CSI Ribbon ────→ Pi Zero CSI Port  │
  │                                     │
  │  Resolution: 1920x1080             │
  │  Frame Rate: 30 fps                │
  │  FOV: 60 degrees                   │
  │  Focus: Fixed (10cm to infinity)   │
  │                                     │
  │  Purpose:                           │
  │  - Wound visual assessment          │
  │  - Bleeding detection               │
  │  - Burn severity estimation         │
  │  - Fracture visual indicators       │
  │                                     │
  │  Mounting:                          │
  │  - Bottom of drone (patient-facing) │
  │  - Vibration-dampened bracket       │
  │  - LED flash for low-light          │
  │                                     │
  └─────────────────────────────────────┘
```
