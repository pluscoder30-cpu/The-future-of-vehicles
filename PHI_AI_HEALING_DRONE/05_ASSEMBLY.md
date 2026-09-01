# PHI AI HEALING DRONE — ASSEMBLY GUIDE

## Step-by-Step Build Instructions (AI-Enhanced)

---

## TOOLS REQUIRED

| Tool | Purpose | Cost |
|------|---------|------|
| Soldering iron (40W) | Solder connections | $15 |
| Wire strippers | Strip insulation | $8 |
| Multimeter | Test voltages | $12 |
| Hex key set (M2-M4) | Bolt tightening | $8 |
| Screwdriver set | General assembly | $10 |
| Hot glue gun | Secure components | $8 |
| 3D printer (or service) | Print frame parts | $0-200 |
| Needle-nose pliers | Bend wires | $6 |
| Heat gun | Shrink tubing | $12 |
| MicroSD card reader | Flash Pi OS | $5 |

---

## PHASE 1: FRAME ASSEMBLY (8-12 hours)

### Step 1: Print Frame Parts

Print all frame components including AI processor mount:
- Material: PLA 1.75mm
- Layer height: 0.2mm
- Infill: 40% gyroid
- Walls: 4 perimeters
- Top/Bottom: 5 layers

**Print Time Estimate: ~20 hours total**

### Step 2: Assemble Frame

Follow standard assembly plus install AI processor mount:
1. Connect 4 arms to center body
2. Install motor mounts
3. Install prop guards
4. Mount AI processor bracket inside center body
5. Mount camera bracket on bottom

---

## PHASE 2: MOTOR INSTALLATION (4-6 hours)

Same as standard PHI Healing Drone — see standard assembly.

---

## PHASE 3: ELECTRONICS WIRING (12-16 hours)

### Step 9: Install Power Distribution

Same as standard, add 5V buck for Raspberry Pi.

### Step 10: Wire Arduino and Sensors

Same as standard pin allocation.

### Step 11: Install AI Processor

```
AI PROCESSOR INSTALLATION:
═══════════════════════════════════════════════════════════════

  1. Mount Raspberry Pi Zero 2W on standoffs
  2. Connect 5V power from buck regulator
  3. Connect serial pins to Arduino (TX/RX)
  4. Connect camera ribbon cable to CSI port
  5. Mount camera module on bottom bracket
  6. Insert microSD card with pre-loaded OS
  7. Test serial communication with Arduino
```

### Step 12: Flash AI Software

```
AI SOFTWARE SETUP:
═══════════════════════════════════════════════════════════════

  1. Flash Raspberry Pi OS Lite to microSD
  2. Install TensorFlow Lite runtime
  3. Install OpenCV
  4. Copy AI model files
  5. Configure serial communication
  6. Set up auto-start service
  7. Test AI inference with dummy data
```

---

## PHASE 4: MEDICAL PAYLOAD (6-8 hours)

Same as standard PHI Healing Drone.

---

## PHASE 5: AVIONICS (6-8 hours)

Same as standard, plus AI processor installation.

---

## PHASE 6: FINAL ASSEMBLY (4-6 hours)

Same as standard PHI Healing Drone.

---

## PHASE 7: TESTING (6-8 hours)

### Additional AI System Tests

```
AI SYSTEM TEST CHECKLIST:
═══════════════════════════════════════════════════════════════

  □ AI PROCESSOR
    □ Raspberry Pi boots correctly
    □ AI model loads without errors
    □ Camera captures images
    □ Serial communication with Arduino works

  □ AI DIAGNOSIS
    □ Test with simulated vital signs
    □ Verify diagnosis codes output
    □ Check confidence scores
    □ Test emergency detection

  □ AI TREATMENT
    □ Verify treatment recommendations
    □ Check frequency selection
    □ Test medication bay commands
    □ Verify drone coordination requests

  □ AI INTEGRATION
    □ Arduino receives AI commands
    □ Motors respond to AI flight commands
    □ Medication bay responds to AI
    □ Frequency gen responds to AI
    □ Emergency override works

  □ FULL MISSION TEST
    □ Simulate patient scenario
    □ Verify end-to-end AI workflow
    □ Test human override capability
    □ Log all AI decisions
```

---

## ASSEMBLY TROUBLESHOOTING

| Problem | Cause | Fix |
|---------|-------|-----|
| Pi Zero won't boot | Bad microSD | Re-flash OS |
| Camera not detected | Loose ribbon | Re-seat ribbon cable |
| Serial comm fails | TX/RX swapped | Check pin connections |
| AI model crashes | Insufficient RAM | Use smaller model |
| AI slow inference | CPU throttling | Add heatsink |
| Camera blurry | Dirty lens | Clean lens |
