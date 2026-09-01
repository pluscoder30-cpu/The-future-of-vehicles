# PHI Surgical Assist Drone - Quick Start Guide

## What Is This?

The PHI Surgical Assist Drone (PSAD-200) is a ceiling-mounted drone that helps surgeons during operations. It holds surgical instruments, switches between them in less than 2 seconds, maintains a sterile field, and uses phi-harmonic healing to help tissue repair faster.

**Price:** $600 | **Runtime:** 4+ hours | **Instrument swap:** <2 seconds

---

## At a Glance

| Feature | Details |
|---------|---------|
| Model | PSAD-200 |
| Battery | FPB-5 (5kWh), inductive ceiling charging |
| Payload | 5 kg (surgical instruments) |
| Robotic arm | 6-DOF, 0.1mm accuracy |
| Instruments | 6 quick-change slots |
| Sterile field | UV-C + ionization + HEPA |
| Healing field | 16.18 Hz, 4 Helmholtz coils |
| Mounting | Ceiling rail, magnetic dock |

---

## How to Use It

### Step 1: Installation (One-Time)
1. Mount ceiling rail in operating room (requires 50kg structural support)
2. Install inductive power coil and optical data link
3. Connect to hospital power (220V AC, 10A dedicated circuit)
4. Test dock engagement

### Step 2: Pre-Procedure Setup (30 min before surgery)
1. Power on via ceiling dock
2. Run diagnostics (all green required)
3. Verify sterile field (particles <10/m3)
4. Load instrument tray (6 instruments)
5. Calibrate visual servoing
6. Test phi-harmonic at 16.18 Hz
7. Sync with surgeon console

### Step 3: Deploy (-5 min before surgery)
1. Surgeon says **"Deploy"**
2. Drone releases from ceiling dock
3. Drone positions over surgical site
4. Sterile field activates (UV-C + ionization)
5. Phi-harmonic healing activates (16.18 Hz)
6. Position lock confirmed (visual servoing)

### Step 4: During Surgery
1. Surgeon says **"Swap to [instrument]"** (e.g., "Swap to scalpel")
2. Drone changes instrument in <2 seconds
3. Surgeon says **"Hold position"** to lock the drone
4. Drone maintains sterile field continuously
5. Drone adapts phi-harmonic frequency based on tissue feedback

### Step 5: End of Procedure
1. Surgeon says **"Return to dock"**
2. Phi-harmonic deactivates
3. Sterile field stays on during exit
4. Drone returns to ceiling dock
5. Magnetic lock engages
6. Auto-sterilize cycle begins

---

## Voice Commands

| Command | What It Does |
|---------|--------------|
| "Deploy" | Leave dock, position over surgical site |
| "Return to dock" | Return to ceiling mount |
| "Swap to scalpel" | Change to scalpel |
| "Swap to forceps" | Change to forceps |
| "Swap to suction" | Change to suction tool |
| "Swap to cautery" | Change to cautery tool |
| "Swap to retractor" | Change to retractor |
| "Swap to scissors" | Change to scissors |
| "Phi healing" | Activate 16.18 Hz healing |
| "Phi pain" | Activate 68.54 Hz pain relief |
| "Phi inflammation" | Activate 26.18 Hz anti-inflammatory |
| "Phi off" | Deactivate phi-harmonic |
| "Hold position" | Lock current position |
| "Emergency stop" | All motion stops, brake engages |

---

## Emergency Procedures

| Situation | What Happens |
|-----------|--------------|
| Emergency stop | All motion stops, brake engages |
| Motor failure | Auto-ceiling dock |
| Arm fault | Brake engages, arm locks |
| Sterile breach | Alert + auto-resteralize |
| Battery low | Auto-return to dock |
| Surgeon foot pedal | Kill switch (always available) |

---

## Specifications

| Parameter | Value |
|-----------|-------|
| Frame | Medical-grade aluminum + titanium |
| Weight | 8 kg |
| Dimensions | 0.6m x 0.6m x 0.4m |
| Rotor count | 4 (fully enclosed) |
| Noise level | <45 dB at 1m |
| Arm DOF | 6 |
| Arm reach | 0.5m |
| Arm accuracy | 0.1mm |
| Force range | 0.1-50 N |
| Instrument slots | 6 |
| Swap time | <2 seconds |
| UV-C | 254nm, 40mW/cm2 |
| Sterility | 10^-6 SAL |
| Phi-harmonic | 16.18 Hz, 0.3 mT |
| Ceiling height | 2.5-4.0m |

---

## Maintenance Quick Reference

| When | What |
|------|------|
| After each procedure | Auto-sterilize, visual inspection |
| Daily | Full diagnostics, camera calibration |
| Weekly | Arm calibration, force sensor check |
| Monthly | UV-C intensity check, HEPA filter |
| Quarterly | Full overhaul, phi calibration |
| Annually | IEC 60601-1 recertification |

---

## Regulatory Compliance

- FDA Class II Medical Device
- IEC 60601-1 Medical Electrical Equipment
- ISO 13485 Quality Management
- CE Mark (European Conformity)

---

## Documentation

- `01_PARTS_LIST.md` — All parts with sources and prices
- `05_ASSEMBLY.md` — Step-by-step build instructions
- `DESIGN.md` — Full design document
- `ARCHITECTURE.md` — System architecture
- `TEST_PLAN.md` — Complete test procedures
- `MAINTENANCE.md` — Maintenance manual
- `DEPLOYMENT.md` — Deployment guide
