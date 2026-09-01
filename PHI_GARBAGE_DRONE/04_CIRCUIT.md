# PHI GARBAGE DRONE — CIRCUIT SCHEMATICS

## Circuit Design

---

## METAL DETECTOR

```
METAL DETECTOR MODULE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  AOUT → Arduino A0                 │
  │  DOUT → Arduino D2                 │
  │                                     │
  │  Detects: ferrous and non-ferrous  │
  │  Range: 5cm                        │
  │  Output: analog (0-1023)           │
  └─────────────────────────────────────┘
```

---

## IR SENSORS

```
IR OBSTACLE SENSORS:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │  VCC → 5V, GND → GND              │
  │  OUT → Arduino A1, A2              │
  │                                     │
  │  Used for:                          │
  │  - Trash detection                  │
  │  - Distance measurement            │
  │  - Material identification         │
  └─────────────────────────────────────┘
```

---

## ROBOTIC ARM

```
ARM SERVOS:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 → Base rotation servo
  Arduino Pin 13 → Shoulder servo
  Arduino Pin 14 → Gripper servo

  Servo SG90: 180° rotation, 1.8 kg·cm torque
```

---

## SORTING SERVOS

```
SORTING MECHANISM:
═══════════════════════════════════════════════════════════════

  Arduino Pin 15 → Plastic bin door servo
  Arduino Pin 16 → Metal bin door servo
  Arduino Pin 17 → Paper bin door servo

  Each servo opens bin door when trash is deposited
```
