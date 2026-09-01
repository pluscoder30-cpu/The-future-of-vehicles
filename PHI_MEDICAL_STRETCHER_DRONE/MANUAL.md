# PHI Medical Stretcher Drone - Quick Start Guide

## What Is This?

The PHI Medical Stretcher Drone (PMSD-100) is an autonomous drone that picks up injured or sick people and flies them to the hospital while monitoring their heartbeat, blood oxygen, blood pressure, and temperature. It also uses phi-harmonic healing fields (16.18 Hz) to help the patient feel better during transport.

**Price:** $800 | **Range:** 80 km loaded | **Speed:** 80 km/h cruise

---

## At a Glance

| Feature | Details |
|---------|---------|
| Model | PMSD-100 |
| Battery | FPB-20 (20kWh), ~60 min flight |
| Patient capacity | Up to 120 kg |
| Medical monitors | ECG, SpO2, BP, Temp, Respiration, EtCO2 |
| Life support | Oxygen, AED, IV hooks, 4 medications |
| Communication | 4G/5G LTE + 900 MHz mesh + satellite |
| Healing field | 16.18 Hz phi-harmonic, 8 emitters |

---

## How to Use It

### Step 1: Power On
1. Connect the battery (XT90 connector)
2. Wait for the flight controller to show green LEDs (GPS lock)
3. Check ground station — all systems should be green

### Step 2: Load Medications
1. Open the Life Support Module
2. Verify O2 tank is full
3. Check medication expiry dates
4. Confirm AED pads are in date

### Step 3: Dispatch
1. Emergency call received at mission control
2. AI calculates route to patient and nearest hospital
3. Drone launches automatically
4. ETA displayed on ground station

### Step 4: Patient Pickup
1. Drone hovers at 5m above scene
2. Winch extends with patient harness
3. Medical team secures patient in harness
4. Winch retracts — patient is now onboard
5. Medical monitoring starts automatically

### Step 5: Transport
1. AI navigates to hospital at 80 km/h
2. All vital signs displayed in real-time
3. Phi-harmonic healing active at 16.18 Hz
4. Medical team can communicate via 2-way audio

### Step 6: Hospital Arrival
1. Drone approaches landing zone
2. Controlled descent
3. Medical team receives patient
4. Vital signs data transmitted via HL7 to hospital

### Step 7: Return
1. Drone returns to base automatically
2. Battery starts charging
3. Mission log saved
4. Ready for next call

---

## Emergency Procedures

| Situation | What Happens |
|-----------|--------------|
| 1 motor fails | AI redistributes thrust, continues mission |
| 2 motors fail | Emergency landing at nearest safe spot |
| Battery low (<20%) | Auto-return to base |
| Battery critical (<10%) | Emergency landing immediately |
| Comm lost (>10s) | Auto-return to base |
| Patient vitals critical | Divert to nearest hospital |
| All motors fail | Parachute deploys (above 30m) |

---

## Patient Monitoring

The drone monitors 6 vital signs in real-time:

| Parameter | Normal Range | Alert If |
|-----------|--------------|----------|
| Heart rate | 60-100 bpm | <30 or >180 |
| Blood oxygen | 95-100% | <80% |
| Blood pressure | 90-140 systolic | - |
| Temperature | 36-38°C | <34 or >41 |
| Respiration | 12-20 brpm | - |
| EtCO2 | 35-45 mmHg | - |

---

## Phi-Harmonic Healing

The drone uses phi-harmonic fields to help patients:

| Frequency | Purpose |
|-----------|---------|
| 16.18 Hz | General healing (reduces cortisol) |
| 26.18 Hz | Cardiac stabilization (emergency) |
| 42.36 Hz | Neural calming |
| 68.54 Hz | Pain reduction |

The healing field is **optional** — patients can decline. It's logged for medical records.

---

## Specifications

| Parameter | Value |
|-----------|-------|
| Frame | Carbon fiber octocopter |
| Weight (empty) | 65 kg |
| Max takeoff weight | 165 kg |
| Max speed | 120 km/h |
| Cruise speed | 80 km/h |
| Max range | 80 km (loaded) / 150 km (empty) |
| Max altitude | 120m AGL |
| Wind resistance | 50 km/h |
| Operating temp | -10°C to +45°C |
| IP rating | IP67 |
| Night ops | Full capability |

---

## Maintenance Quick Reference

| When | What |
|------|------|
| After each flight | Visual inspection, battery check |
| Weekly | Motor inspection, sensor calibration |
| Monthly | Full diagnostic, software update |
| Quarterly | Battery test, winch service |
| Annually | Complete overhaul, recertification |

---

## Regulatory Compliance

- FAA Part 107 (medical drone exemption)
- HIPAA compliant data transmission
- FDA Class II medical device
- Emergency medical services certification

---

## Documentation

- `01_PARTS_LIST.md` — All parts with sources and prices
- `05_ASSEMBLY.md` — Step-by-step build instructions
- `DESIGN.md` — Full design document
- `ARCHITECTURE.md` — System architecture
- `TEST_PLAN.md` — Complete test procedures
- `MAINTENANCE.md` — Maintenance manual
- `DEPLOYMENT.md` — Deployment guide
