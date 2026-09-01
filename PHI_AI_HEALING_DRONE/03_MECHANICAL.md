# PHI AI HEALING DRONE — MECHANICAL DESIGN

## Frame Design and Structural Specifications (AI-Enhanced)

---

## FRAME OVERVIEW

The PHI AI Healing Drone frame is 3D printed from PLA filament. The design uses phi-harmonic proportions for structural efficiency and flight stability. Additional mounting provisions for the Raspberry Pi Zero 2W AI processor and camera module.

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         400mm
  ←─────────────────────→
  ┌──────────────────────┐  ─┬─
  │                      │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M1║        ║M2║  │   │
  │    ╚══╝        ╚══╝  │   │
  │                      │   │
  │   ┌──────────────┐   │   │
  │   │              │   │   │
  │   │   CENTER     │   │   │ 247mm
  │   │   BODY       │   │   │ (400/phi)
  │   │              │   │   │
  │   │   ┌──────┐   │   │   │
  │   │   │BATT  │   │   │   │
  │   │   └──────┘   │   │   │
  │   │              │   │   │
  │   │   ┌──────┐   │   │   │
  │   │   │PI AI │   │   │   │ ← NEW: AI Processor
  │   │   └──────┘   │   │   │
  │   │              │   │   │
  │   └──────────────┘   │   │
  │                      │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M3║        ║M4║  │   │
  │    ╚══╝        ╚══╝  │   │
  │                      │   │
  └──────────────────────┘  ─┴─
```

---

## AI PROCESSOR MOUNTING

```
PI ZERO 2W MOUNTING DETAIL:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────┐
  │                                      │
  │   RASPBERRY PI ZERO 2W              │
  │   ┌──────────────────────────────┐  │
  │   │  ┌──────┐    ┌──────────┐   │  │
  │   │  │CPU   │    │CSI PORT  │   │  │
  │   │  │      │    │(Camera)  │   │  │
  │   │  └──────┘    └──────────┘   │  │
  │   │                              │  │
  │   │  ┌──────┐    ┌──────────┐   │  │
  │   │  │GPIO  │    │MicroSD   │   │  │
  │   │  │Header│    │Slot      │   │  │
  │   │  └──────┘    └──────────┘   │  │
  │   │                              │  │
  │   │  65mm × 30mm × 5mm          │  │
  │   └──────────────────────────────┘  │
  │                                      │
  │   Mounting: 2x M2 standoffs          │
  │   Height: 5mm above body floor       │
  │   Cooling: Passive (thermal pad)     │
  │   Camera: CSI cable to bottom mount  │
  │                                      │
  └──────────────────────────────────────┘
```

---

## CAMERA MODULE MOUNTING

```
CAMERA POSITION:
═══════════════════════════════════════════════════════════════

  Bottom View (patient contact side):

  ┌──────────────────────────────────────┐
  │                                      │
  │   ┌──────┐                ┌──────┐  │
  │   │SpO2  │                │Temp  │  │
  │   │Sensor│                │Sensor│  │
  │   └──────┘                └──────┘  │
  │                                      │
  │          ┌──────────┐               │
  │          │  CAMERA  │               │
  │          │ (AI Scan)│               │
  │          └──────────┘               │
  │                                      │
  │          ┌──────────┐               │
  │          │   ECG    │               │
  │          │  Pads    │               │
  │          └──────────┘               │
  │                                      │
  └──────────────────────────────────────┘

  Camera FOV: 60° (wide angle)
  Resolution: 1080p (for wound analysis)
  Mounting: Vibration-dampened bracket
  Purpose: Visual wound assessment for AI diagnosis
```

---

## MATERIAL SPECIFICATIONS

| Component | Material | Dimensions | Weight |
|-----------|----------|------------|--------|
| Frame arms | PLA 3D printed | 4x 150x25x8mm | 85g |
| Center body | PLA 3D printed | 160x160x45mm | 130g |
| Motor mounts | PLA 3D printed | 4x 60x60x10mm | 45g |
| Prop guards | PLA 3D printed | 4x 350mm rings | 60g |
| Lid | PLA 3D printed | 160x160x3mm | 25g |
| AI processor mount | PLA 3D printed | 70x35x10mm | 10g |
| Camera bracket | PLA 3D printed | 30x20x15mm | 5g |
| Hardware | Steel bolts/nuts | M3 assorted | 35g |
| Dampeners | Rubber | 8x 8mm | 10g |
| **Total Frame** | | | **405g** |

---

## WEIGHT CHECKLIST

| Component | Target Weight |
|-----------|---------------|
| Frame (with AI mount) | 405g |
| Motors (4x) | 200g |
| ESCs (4x) | 80g |
| Propellers (4x) | 40g |
| Battery (FPB-5) | 850g |
| Arduino + sensors | 60g |
| Raspberry Pi Zero 2W | 10g |
| Pi Camera Module | 5g |
| Medical payload | 120g |
| Frequency generator | 50g |
| Wiring and hardware | 80g |
| **Total** | **1,900g** |

**Target: Under 2,000g (4.4 lbs)**
