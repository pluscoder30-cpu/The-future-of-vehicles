# PHI SUPER GOGGLES — ASSEMBLY GUIDE

## Step-by-Step Assembly Instructions

---

## PREREQUISITES

### Tools Required
- Soldering iron (TS101, temp-controlled)
- Solder (63/37 leaded, 0.02mm)
- Flux pen
- Multimeter
- Oscilloscope
- 3D printer
- Hex drivers (M2, M2.5, M3)
- Tweezers (precision, anti-static)
- Heat gun
- Hot glue gun
- Isopropyl alcohol (99%)
- ESD wrist strap

---

## PHASE 1: 3D PRINTED PARTS (20-30 hours)

1. Print Main Housing (PETG, 8 hours)
2. Print Sensor Plate (PETG, 4 hours)
3. Print Display Housings ×2 (PLA, 3 hours each)
4. Print Eyecups ×2 (TPU, 1 hour each)
5. Print Diopter Rings ×2 (PLA, 30 min each)
6. Post-process: remove supports, sand, test fit

---

## PHASE 2: SENSOR BOARD (4-6 hours)

1. Solder MUX ICs (CD74HC4067 × 4)
2. Solder sensor footprints (ML8511 × 8)
3. Solder bypass caps, resistors, ferrite beads
4. Solder connectors (BNC, GPIO header, SPI headers)
5. Test: verify 3.3V at each sensor, test MUX channels

---

## PHASE 3: MAIN BOARD (6-8 hours)

1. Solder voltage reference (REF5025)
2. Solder ADC ICs (ADS1256 × 4) with bypass caps
3. Solder power regulation (LM2596 × 2, AMS1117 × 3)
4. Mount DE10-Lite FPGA on standoffs
5. Solder GPIO headers, USB-C, DC jack
6. Test: verify all power rails, FPGA programming, SPI communication

---

## PHASE 4: DISPLAY ASSEMBLY (3-4 hours)

1. Mount ADV7533 bridge ICs
2. Connect OLED displays via FPC cables
3. Assemble display modules (lens, housing, diopter)
4. Optical alignment (test patterns, brightness)

---

## PHASE 5: POWER SYSTEM (2-3 hours)

1. Assemble battery pack with JST-XH connector
2. Mount TP5100 charger module
3. Install power distribution board
4. Test: verify voltages, charging, battery life

---

## PHASE 6: INTERFACE (2-3 hours)

1. Solder button array with pull-ups
2. Install haptic motors in temple sections
3. Install buzzer and WS2812B LEDs
4. Test: verify all buttons, haptics, LEDs

---

## PHASE 7: FINAL ASSEMBLY (4-5 hours)

1. Install electronics tray in main housing
2. Route all ribbon cables
3. Mount sensor plate
4. Install display assemblies
5. Install battery
6. Attach head strap
7. Complete system test (all 7 modes)

---

## CALIBRATION

1. Zero-field calibration (baseline)
2. Known-field calibration (sensitivity)
3. Display calibration (brightness, color)
4. IMU calibration (level and still)
5. Phi-harmonic verification

---

## TROUBLESHOOTING

| Issue | Cause | Solution |
|-------|-------|----------|
| No power | Battery dead | Charge 30 min |
| One display dark | FPC loose | Reseat cable |
| Sensor not responding | Bad solder | Reflow joint |
| Buttons not working | Pull-up missing | Check resistors |
| Overheating | Fan blocked | Check ventilation |
