# PHI EMOTION CLOAK — ASSEMBLY GUIDE
## Buildable Documentation | Step-by-Step Instructions

---

## BEFORE YOU START

### Safety Rules
1. **Wear safety glasses** when soldering
2. **Unplug** the soldering iron when not in use
3. **Work in a well-ventilated area** (solder fumes)
4. **Keep water away** from electronics
5. **Ask an adult** if you're unsure about anything
6. **tDCS SAFETY**: Read all warnings before using stimulation module

### Tools You'll Need
- Soldering iron (40-60W, adjustable temperature)
- Solder wire (60/40 or lead-free)
- Wire stripper (22-30 AWG)
- Flush cutters
- Tweezers (ESD safe)
- Magnifying lamp or headset
- Multimeter
- Hot glue gun
- Heat gun
- Sewing needle kit
- Conductive thread
- Isopropyl alcohol (90%)

### Time Needed
- **Total**: 6-8 hours
- **Sections**: Can be done in 1.5-hour chunks
- **Drying time**: 24 hours (adhesive)

---

## STEP 1: PREPARE THE COLLAR (45 minutes)

### 1.1 Cut Collar Fabric
```
Cut List:
- Outer layer: 240mm x 120mm (neoprene)
- Middle layer: 240mm x 120mm (flexible PCB)
- Inner layer: 240mm x 120mm (conductive fabric)
- Skin layer: 240mm x 120mm (medical silicone)

Tools: Fabric scissors, rotary cutter, cutting mat
```

### 1.2 Mark Component Positions
```
Using fabric marker, mark positions:
- Electronics box: Center front (60mm x 40mm)
- LED ring: Around collar (16 positions)
- Peltier patches: 4 zones (forehead, cheeks, neck, wrists)
- Vibration motors: 6 positions (evenly spaced)
- Microphones: 4 positions (front/sides)
- Speakers: 2 positions (left/right)
```

### 1.3 Sew Conductive Traces
```
Using conductive thread, sew traces:
- Power lines (5V, 3.3V, GND)
- I2C bus (SDA, SCL)
- SPI bus (MOSI, MISO, SCLK, CS)
- I2S bus (BCLK, LRCLK, DIN, DOUT)

Sewing tips:
- Use running stitch for traces
- Keep traces 5mm apart
- Knot ends securely
- Test continuity with multimeter
```

---

## STEP 2: SOLDER FLEXIBLE PCB (60 minutes)

### 2.1 Prepare Flexible PCB
```
Flexible PCB Layout:
┌─────────────────────────────────────────────────┐
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │         Main Electronics Area           │   │
│   │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────────┐  │   │
│   │  │Pi 4 │ │EEG  │ │FLIR │ │Power    │  │   │
│   │  │     │ │ADC  │ │Cam  │ │System   │  │   │
│   │  └─────┘ └─────┘ └─────┘ └─────────┘  │   │
│   └─────────────────────────────────────────┘   │
│                     │                           │
│   ┌─────────────────┼───────────────────────┐   │
│   │                 │                       │   │
│   │  ┌──────────────┴──────────┐  ┌─────────┴──┐ │
│   │  │    Sensor Connectors    │  │ Projection │ │
│   │  │  ┌────┐ ┌────┐ ┌────┐  │  │ Connectors │ │
│   │  │  │EEG │ │PPG │ │GSR │  │  │ ┌────┐    │ │
│   │  │  └────┘ └────┘ └────┘  │  │ │LED │    │ │
│   │  └────────────────────────┘  │ │Pelt│    │ │
│   │                              │ │Vib │    │ │
│   │  ┌────────────────────────┐  │ └────┘    │ │
│   │  │    Audio Connectors    │  └────────────┘ │
│   │  │  ┌────┐ ┌────┐        │                 │
│   │  │  │Mic │ │DAC │        │                 │
│   │  │  └────┘ └────┘        │                 │
│   │  └────────────────────────┘                 │
│   │                                             │
│   └─────────────────────────────────────────────┘
│                                                 │
└─────────────────────────────────────────────────┘
```

### 2.2 Solder Raspberry Pi 4
```
Pi 4 Connections:
1. Solder Pi header to flexible PCB
2. Connect 5V and GND rails
3. Connect GPIO pins to respective traces
4. Add 100nF bypass capacitor near Pi
```

### 2.3 Solder EEG System (ADS1299)
```
ADS1299 Connections:
1. Solder ADS1299 module to PCB
2. Connect SPI pins (MOSI, MISO, SCLK, CS)
3. Connect DRDY to GPIO 25 (IRQ)
4. Connect electrode inputs to connector
5. Add 4.7kΩ pull-ups on I2C bus
```

### 2.4 Solder Camera Systems
```
FLIR Lepton:
1. Solder FLIR module to PCB
2. Connect SPI pins (shared with ADS1299, use CS1)
3. Connect RESET to GPIO 24
4. Connect PWR_DWN to GPIO 27
5. Connect INT to GPIO 22

OV2640 NIR:
1. Solder OV2640 module to PCB
2. Connect CSI ribbon cable to Pi
3. Connect I2C pins (SDA, SCL)
4. Connect PWDN to GPIO 0
5. Connect RESET to GPIO 1
```

### 2.5 Solder Audio System
```
Microphone Array (4x INMP441):
1. Solder 4 microphones to PCB
2. Connect shared I2S bus (BCLK, LRCLK)
3. Connect individual SD pins to GPIO
4. Add 100nF caps on each mic VCC

PCM5102A DAC:
1. Solder DAC module to PCB
2. Connect I2S pins (BCLK, LRCLK, DIN)
3. Connect speakers to LOUT/ROUT
4. Connect XMT to 3.3V (unmute)
```

---

## STEP 3: SOLDER PROJECTION SYSTEM (45 minutes)

### 3.1 Solder LED Ring
```
WS2812B LED Ring:
1. Solder 16 LEDs in circle
2. Connect DIN to GPIO 12 (PWM)
3. Connect VCC to 5V rail
4. Connect GND to ground rail
5. Test with NeoPixel library
```

### 3.2 Solder Peltier Patches
```
Peltier TEC1-12706 (x4):
1. Solder MOSFETs (IRF540N) for each patch
2. Connect MOSFET gates to GPIO pins
3. Connect Peltier + to MOSFET drain
4. Connect Peltier - to GND
5. Add flyback diodes across each Peltier
6. Add 10kΩ pull-down on each gate
```

### 3.3 Solder Vibration Motors
```
LRA Vibration Motors (x6):
1. Solder 6 motors to PCB
2. Connect + to GPIO pins (PWM)
3. Connect - to GND
4. Add 100nF caps across each motor
```

### 3.4 Solder tDCS Stimulator
```
tDCS Module:
1. Solder tDCS module to PCB
2. Connect UART pins (TX, RX)
3. Connect ENABLE to GPIO 4
4. Connect CURRENT_SET to GPIO 27 (PWM)
5. Connect electrodes to output terminals
6. **CRITICAL**: Test with multimeter before use!
```

---

## STEP 4: SOLDER SENSOR ELECTRODES (30 minutes)

### 4.1 Prepare EEG Electrodes
```
Ag/AgCl Dry Electrodes (x8):
1. Strip electrode wires (26 AWG)
2. Solder wires to electrode pads
3. Connect to EEG connector on PCB
4. Label each electrode (Fp1, Fp2, F3, F4, etc.)
5. Apply conductive gel to electrode surfaces
```

### 4.2 Prepare ECG Electrodes
```
Wrist Band Electrodes:
1. Solder ECG wires to wrist band
2. Connect to MAX30102 PPG module
3. Test continuity with multimeter
4. Ensure proper polarity (+ and -)
```

### 4.3 Prepare GSR Electrodes
```
Finger Clip Electrodes:
1. Solder GSR wires to finger clip
2. Connect to ADS1115 ADC
3. Test continuity with multimeter
4. Ensure proper polarity (+ and -)
```

---

## STEP 5: ASSEMBLE COLLAR (45 minutes)

### 5.1 Install Flexible PCB
1. Place flexible PCB in collar
2. Align with marked positions
3. Hot glue edges to secure
4. Route wires neatly
5. Ensure no wire pinch points

### 5.2 Install Projection System
1. Place LED ring in collar
2. Secure with hot glue
3. Install Peltier patches
4. Secure with thermal adhesive
5. Install vibration motors
6. Secure with hot glue

### 5.3 Install Audio System
1. Place microphones in collar
2. Secure with hot glue
3. Install speakers
4. Secure with hot glue
5. Route audio wires

### 5.4 Install Sensors
1. Place FLIR Lepton in collar
2. Secure with hot glue
3. Install OV2640 NIR camera
4. Secure with hot glue
5. Install tDCS stimulator
6. Secure with hot glue (insulate!)

---

## STEP 6: INSTALL POWER SYSTEM (30 minutes)

### 6.1 Prepare Battery Pack
```
2x 18650 Battery Pack:
1. Connect batteries in series (7.4V)
2. Solder TP4056 dual charger
3. Solder 5V/3A boost converter
4. Add 100µF bulk capacitor
5. Test output voltage (5V ±0.1V)
```

### 6.2 Install Battery Pack
1. Place battery pack in collar
2. Secure with hot glue
3. Connect power rails to PCB
4. Route power wires
5. Add strain relief

### 6.3 Test Power System
1. Connect battery pack
2. Measure 5V output
3. Measure 3.3V output (from Pi LDO)
4. Verify all rails powered
5. Check for shorts

---

## STEP 7: INSTALL ELECTRODES (30 minutes)

### 7.1 Install EEG Headband
```
Headband Assembly:
1. Sew conductive traces on headband
2. Attach 4 EEG electrodes
3. Connect traces to collar connector
4. Test continuity
5. Adjust headband length
```

### 7.2 Install Wrist Band
```
Wrist Band Assembly:
1. Sew conductive traces on band
2. Attach ECG electrodes
3. Connect traces to collar connector
4. Test continuity
5. Adjust band length
```

### 7.3 Install Finger Clip
```
Finger Clip Assembly:
1. Solder GSR electrodes to clip
2. Connect to collar connector
3. Test continuity
4. Verify spring mechanism works
```

---

## STEP 8: APPLY SKIN LAYER (30 minutes)

### 8.1 Prepare Skin Layer
1. Cut medical silicone to size
2. Mark electrode positions
3. Cut holes for electrodes
4. Clean with isopropyl alcohol

### 8.2 Attach Skin Layer
1. Place skin layer on collar
2. Align electrode holes
3. Apply UV adhesive around electrodes
4. Cure with UV light (2 minutes)
5. Wipe excess adhesive

### 8.3 Test Comfort
1. Wear collar for 10 minutes
2. Check for irritation
3. Adjust padding if needed
4. Verify electrode contact

---

## STEP 9: FINAL ASSEMBLY (30 minutes)

### 9.1 Close Collar
1. Apply UV adhesive to collar edges
2. Press layers together
3. Cure with UV light (5 minutes)
4. Wipe excess adhesive

### 9.2 Install Clasp
1. Attach Velcro strips to collar ends
2. Test closure
3. Adjust length for comfortable fit

### 9.3 Final Inspection
1. Check all solder joints
2. Verify no shorts
3. Test all connections
4. Clean flux residue

---

## STEP 10: SOFTWARE SETUP (60 minutes)

### 10.1 Flash Raspberry Pi
```
Flash Raspberry Pi OS:
1. Download Raspberry Pi OS Lite
2. Flash to microSD card (32GB+)
3. Enable SSH and WiFi
4. Boot Pi and connect
```

### 10.2 Install Dependencies
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python packages
pip3 install numpy scipy scikit-learn
pip3 install RPi.GPIO spidev smbus2
pip3 install opencv-python
pip3 install pyaudio wave

# Install EEG library
pip3 install mne

# Install FLIR library
pip3 install lepton-camera

# Install audio library
pip3 install sounddevice
```

### 10.3 Install PHI Emotion Cloak Software
```bash
# Clone repository
git clone https://github.com/phi-cloak/emotion-cloak.git
cd emotion-cloak

# Install
sudo python3 setup.py install

# Configure
python3 config.py --calibrate
```

### 10.4 Calibrate Sensors
```bash
# Calibrate EEG
python3 calibrate_eeg.py

# Calibrate PPG
python3 calibrate_ppg.py

# Calibrate GSR
python3 calibrate_gsr.py

# Calibrate thermal
python3 calibrate_thermal.py
```

### 10.5 Test All Systems
```bash
# Run full system test
python3 test_all.py

# Expected output:
# EEG System: OK (8 channels)
# PPG System: OK (Heart rate detected)
# GSR System: OK (Skin conductance)
# Thermal Camera: OK (320x240)
# NIR Camera: OK (120fps)
# Audio System: OK (4 mics, 2 speakers)
# LED Ring: OK (16 LEDs)
# Peltier: OK (4 zones)
# Vibration: OK (6 motors)
# tDCS: OK (1mA max)
# Power System: OK (5V, 3A)
# All systems operational!
```

---

## TROUBLESHOOTING

### Problem: Pi won't boot
- Check power connections
- Verify 5V output from boost converter
- Check SD card (if used)
- Re-flash firmware

### Problem: EEG not reading
- Check electrode contact
- Verify conductive gel applied
- Check ADS1299 connections
- Run I2C scanner

### Problem: Camera not working
- Check CSI ribbon cable
- Verify GPIO connections
- Check power supply
- Run camera test

### Problem: Audio not working
- Check I2S connections
- Verify microphone solder joints
- Check DAC connections
- Run audio test

### Problem: LEDs not lighting
- Check GPIO 12 connection
- Verify 5V power
- Check LED polarity
- Run NeoPixel test

### Problem: Peltier not heating/cooling
- Check MOSFET connections
- Verify GPIO control
- Check flyback diodes
- Test with multimeter

### Problem: tDCS not working
- **STOP**: Do not use if malfunctioning
- Check UART connections
- Verify power supply
- Test electrodes (no short)
- Contact support

---

## CARE & MAINTENANCE

### Daily Care
- Wipe collar with damp cloth
- Clean electrodes with isopropyl alcohol
- Check for skin irritation
- Remove before sleeping

### Weekly Care
- Wash collar with soap and water
- Replace electrode pads
- Check all connections
- Calibrate sensors

### Monthly Care
- Deep clean all components
- Check battery health
- Update software
- Test all systems

### Battery Care
- Charge after each use
- Don't fully discharge
- Store in cool, dry place
- Replace every 500 cycles

---

## SAFETY WARNINGS

### tDCS Safety
1. **Maximum current**: 1mA (DO NOT EXCEED)
2. **Maximum voltage**: 12V
3. **Session time**: 20 minutes max
4. **Frequency**: 1x daily max
5. **Contraindications**:
   - Epilepsy
   - Metal implants in head
   - Pregnancy
   - Pacemaker
   - Skin conditions on electrode sites
6. **Always** use with supervision
7. **Always** start at 0.5mA
8. **Always** use conductive sponge electrodes
9. **Never** use if electrodes are damaged
10. **Never** use if skin is broken

### General Safety
1. Do not submerge in water
2. Do not expose to extreme heat
3. Do not use if skin irritation occurs
4. Do not share with others (hygiene)
5. Do not use medical claims without FDA approval
6. Do not use while driving
7. Do not use while operating machinery

---

## NEXT STEPS

After assembly:
1. Download companion app (see MANUAL.md)
2. Pair with phone via WiFi
3. Set up emotion profiles
4. Calibrate for your emotions
5. Join community forum

---

**Document**: 05_ASSEMBLY.md
**Vehicle**: PHI EMOTION CLOAK
**Status**: BUILDABLE ✓
**Time**: 6-8 hours
**Difficulty**: Advanced (soldering + sewing + safety)
