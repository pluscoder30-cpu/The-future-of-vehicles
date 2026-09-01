# PHI_HOVERBOARD — Assembly Steps

> **Skill Level**: Beginner (12-year-old can do it with adult supervision)
> **Time**: 8-10 hours over a weekend
> **Tools Needed**: Soldering iron, wire strippers, screwdrivers, hot glue gun, multimeter

---

## Phase 1: Build the Coils (3 hours)

### Step 1: Wind the Coil Forms

1. Take a ferrite core rod (15mm × 80mm)
2. Wrap 3 layers of Kapton tape around the center section (40mm long)
3. Take AWG-20 magnet wire and tie a starting knot around the taped section
4. Wind **200 turns** evenly around the taped section
   - Keep turns tight and close together
   - Don't overlap — wind in neat layers
   - Count every 50 turns to track progress
5. After 200 turns, tie off the wire and leave 10cm of lead on each end
6. Wrap 3 more layers of Kapton tape over the winding to protect it
7. **Repeat for all 8 coils**

**Tip**: Make a simple winding jig by putting the rod in a drill chuck and turning slowly while guiding the wire.

### Step 2: Add the Magnets

1. Take 4 N52 neodymium magnets (20mm × 10mm disc)
2. Arrange them in a **phi-pattern** around the coil:
   - Magnet 1: 0° (top)
   - Magnet 2: 137.5° (bottom-right)
   - Magnet 3: 275° (bottom-left)
   - Magnet 4: 412.5° = 52.5° (top-right)
3. Hot-glue each magnet to the coil form
4. **Important**: All magnets must face the same direction (N-up) for phi-harmonic interference

### Step 3: Pot the Coils

1. Mix silicone potting compound (50/50 ratio)
2. Pour into a small mold (40mm diameter, 30mm tall)
3. Insert the coil+ magnet assembly
4. Let cure for 4 hours (or until fully hard)
5. **Repeat for all 8 coils**

**Result**: 8 identical phi-harmonic coils, each ~120g

---

## Phase 2: Build the Battery Pack (2 hours)

### Step 4: Assemble Battery Cells

1. Take 16 LiFePO4 26650 cells (3.2V 10Ah each)
2. Arrange in a 16S configuration (16 in series)
3. Use a spot welder or solder tabs to connect cells in series:
   - Cell 1 (+) → Cell 2 (-) → Cell 3 (-) → ... → Cell 16 (-)
   - **Do NOT use regular solder** — use nickel strips
4. Connect the BMS board:
   - BMS B- → Cell 1 (-) [main negative]
   - BMS B1 → between cells 1-2
   - BMS B2 → between cells 2-3
   - ... continue for all balance leads
   - BMS B+ → Cell 16 (+) [main positive]
5. Connect the XT90 connector:
   - XT90 Red (+) → BMS P+ (pack positive)
   - XT90 Black (-) → BMS P- (pack negative)

### Step 5: Test Battery Pack

1. Use multimeter to verify total voltage: should be **48V** (16 × 3.0V nominal)
2. Check each balance lead: should be 3.0-3.3V per cell
3. Plug in BMS — verify green light (balanced)
4. **If any cell is below 2.8V, DO NOT USE — return for warranty**

---

## Phase 3: Build the Controller (2 hours)

### Step 6: Build the Arduino Board

1. Take the perfboard (70×90mm)
2. Solder the Arduino Nano in the center
3. Install the I2C header pins for OLED display
4. Solder the 2× MPU-6050 breakout boards:
   - MPU-6050 #1 (front): Address 0x68
   - MPU-6050 #2 (rear): Address 0x69
   - Both share SDA/SCL bus
5. Solder pull-up resistors (4.7kΩ) on SDA and SCL lines
6. Connect the OLED display to I2C header

### Step 7: Build the MOSFET Driver Board

1. Take 4× IR2110 half-bridge drivers
2. For each driver, solder:
   - 1µF bootstrap capacitor (between VB and VS pins)
   - 10Ω gate resistors (on HO and LO outputs)
   - 10kΩ pull-down resistors (on each gate to source)
3. Connect control inputs:
   - IR2110 #1 HIN → Arduino D2
   - IR2110 #2 HIN → Arduino D3
   - IR2110 #3 HIN → Arduino D4
   - IR2110 #4 HIN → Arduino D5
   - IR2110 #5 HIN → Arduino D6
   - IR2110 #6 HIN → Arduino D7
   - IR2110 #7 HIN → Arduino D8
   - IR2110 #8 HIN → Arduino D9
4. Connect 12V power to all IR2110 VCC pins
5. Connect common GND

### Step 8: Install the MOSFETs

1. Take 32× IRFZ44N MOSFETs (8 per H-bridge)
2. Mount on small aluminum heatsinks (5mm×10mm)
3. Solder into H-bridge configuration:
   - Q1, Q2: High-side (PMOS) — connected to 48V bus
   - Q3, Q4: Low-side (NMOS) — connected to GND
4. Connect coil wires to H-bridge midpoints
5. **Double-check all connections before applying power**

### Step 9: Wire the Sensors

1. Mount 8× A3144 Hall Effect sensors near each coil
   - Sensor must face the coil magnet
   - Hot-glue in place
2. Connect each sensor:
   - VCC → 5V
   - GND → GND
   - OUT → Arduino digital pin (D10-D17)
3. Install 2× Force Sensitive Resistors in foot pads
   - Connect to Arduino A0 and A1
4. Install power button on D12
5. Install emergency stop button on D13

---

## Phase 4: Build the Frame (1 hour)

### Step 10: Cut the Deck

1. Take birch plywood (600mm × 200mm × 12mm)
2. Sand edges smooth
3. Cut 4 mounting holes for frame rails (corners)
4. Cut 2 holes for foot pads (marked positions)
5. Apply grip tape to top surface

### Step 11: Assemble the Aluminum Frame

1. Cut 4× aluminum extrusion rails to 200mm length
2. Cut 4× aluminum extrusion rails to 600mm length
3. Assemble using T-nuts and M5 bolts:
   - Form a rectangular frame: 600mm × 200mm
   - Add cross-braces at 150mm intervals
4. Attach frame to underside of deck using M5 bolts

---

## Phase 5: Final Assembly (1 hour)

### Step 12: Mount Components

1. Mount battery pack in center of frame (between rails)
   - Use foam padding for vibration dampening
   - Secure with zip ties
2. Mount controller board above battery
   - Use standoffs for air gap
3. Mount 8 coils at golden-angle positions:
   - Coil A: 0° (front center)
   - Coil B: 137.5° (front-right)
   - Coil C: 275° (rear-right)
   - Coil D: 412.5° = 52.5° (rear center)
   - Coil E: 550° = 190° (rear-left)
   - Coil F: 687.5° = 327.5° (front-left)
   - Coil G: 825° = 105° (left side)
   - Coil H: 962.5° = 242.5° (right side)
4. Connect all coil wires to H-bridges

### Step 13: Wire Everything

1. Connect 48V power bus to all H-bridges
2. Connect 12V buck converter output to IR2110 drivers
3. Connect 5V buck converter output to Arduino and sensors
4. Connect OLED display
5. Connect foot pads (FSRs)
6. Connect power button and E-stop
7. Connect charging port (GX16)

### Step 14: Upload Firmware

1. Connect Arduino to computer via USB
2. Open Arduino IDE
3. Load the phi-hoverboard firmware (provided separately)
4. Upload to Arduino Nano
5. Disconnect USB

### Step 15: Final Testing

1. **DO NOT stand on the board yet**
2. Turn on power switch
3. Verify OLED display shows battery voltage
4. Verify no error LEDs
5. Place board on steel surface
6. Verify coils activate (you'll feel magnetic pull)
7. Check gyroscope response (tilt board, verify LED changes)
8. **First hover test**: Place board on steel, step on lightly with one foot
9. If stable, step on fully and test

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Board won't power on | Check fuse, battery voltage, power switch |
| Coils don't activate | Check MOSFET connections, verify Arduino upload |
| Board tilts/instability | Recalibrate IMU, check Hall sensor alignment |
| Low hover height | Increase coil current (check temperature first) |
| Battery drains fast | Check for short circuits, verify BMS balance |
| OLED shows garbage | Check I2C connections, pull-up resistors |
