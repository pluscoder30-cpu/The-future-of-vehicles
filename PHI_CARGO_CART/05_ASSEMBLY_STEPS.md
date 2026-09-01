# PHI_CARGO_CART — Assembly Steps

> **Skill Level**: Intermediate (12-year-old can do it with adult supervision)
> **Time**: 8-10 hours over a weekend
> **Tools Needed**: Drill, screwdrivers, wire strippers, soldering iron, Allen key set, wrench set, multimeter

---

## Phase 1: Build the Frame (2 hours)

### Step 1: Cut Steel Tubes

1. Cut 2× steel tubes to 800mm (length)
2. Cut 2× steel tubes to 600mm (width)
3. Cut 4× steel tubes to 300mm (legs/supports)
4. Cut 4× aluminum angles to 200mm (corner braces)
5. Sand all cut edges smooth

### Step 2: Assemble Frame

1. Lay out 2 long tubes (800mm) parallel, 600mm apart
2. Place 2 short tubes (600mm) perpendicular at ends
3. Join corners using aluminum angles and M6 bolts
4. Tighten all bolts evenly
5. Add cross braces at 400mm intervals
6. Verify frame is square (diagonals equal)

### Step 3: Install Plywood Base

1. Place plywood (800×600×12mm) on frame
2. Align edges with frame
3. Drill pilot holes through plywood into frame
4. Secure with M6 bolts and T-nuts
5. Sand edges smooth

### Step 4: Paint Frame

1. Clean frame with degreaser
2. Apply rust-resistant primer (2 coats)
3. Apply black spray paint (2 coats)
4. Let dry completely (24 hours)

---

## Phase 2: Install Wheels (1 hour)

### Step 5: Install Rear Wheels

1. The hub motor goes on the right rear position
2. Insert motor axle through frame dropout
3. Secure with axle nuts
4. Install free-spinning wheel on left rear position
5. Both rear wheels should spin freely

### Step 6: Install Front Caster

1. Mount 8" swivel caster at front center of frame
2. Bolt through plywood base and frame
3. Verify caster swivels freely
4. Test foot brake on caster

---

## Phase 3: Build Battery Pack (1.5 hours)

### Step 7: Assemble Battery Cells

1. Take 10 LiFePO4 26650 cells (3.2V 15Ah each)
2. Arrange in 10S configuration (10 in series)
3. Use nickel strips and spot welder:
   - Cell 1 (+) → Cell 2 (-) → ... → Cell 10 (-)
   - **Do NOT use regular solder** — use nickel strips
4. Connect BMS board:
   - BMS B- → Cell 1 (-)
   - BMS B1-B10 → between each cell pair
   - BMS B+ → Cell 10 (+)
5. Connect XT60 connector:
   - XT60 Red (+) → BMS P+
   - XT60 Black (-) → BMS P-

### Step 8: Test and Enclose Battery

1. Verify total voltage: **32V-36V**
2. Check each balance lead: 3.0-3.3V per cell
3. Place battery in waterproof ABS enclosure
4. Add foam padding on all sides
5. Seal enclosure with silicone
6. Mount enclosure under bin, on plywood base

---

## Phase 4: Install Motor and Electronics (2 hours)

### Step 9: Connect Motor to ESC

1. Mount ESC on frame (foam padding + zip ties)
2. Connect battery to ESC:
   - ESC BATTERY+ → XT60 Red (+)
   - ESC BATTERY- → XT60 Black (-)
3. Connect motor to ESC:
   - ESC MOTOR U → Motor Blue wire
   - ESC MOTOR V → Motor Green wire
   - ESC MOTOR W → Motor Yellow wire
4. Connect hall sensors:
   - ESC HALL U/V/W → Motor hall sensor wires

### Step 10: Install Handlebar and Steering

1. Mount handlebar stem to steering column
2. Install handlebar in stem
3. Connect steering column to front caster
4. Verify steering turns smoothly

### Step 11: Wire the Electronics

1. Mount Arduino Nano on perfboard
2. Connect OLED display to I2C pins
3. Connect voltage divider:
   - 36V → 33kΩ resistor → A0
   - A0 → 3.3kΩ resistor → GND
4. Connect power button to D2
5. Connect brake signal to D3
6. Mount display on handlebar (visible while operating)
7. Connect 5V power from ESC to Arduino

### Step 12: Install Battery and Controls

1. Place bin on frame (secure with clips or bolts)
2. Connect battery to ESC
3. Install power switch on handlebar area
4. Install fuse holder near battery
5. Mount charging port on frame (accessible)

---

## Phase 5: Final Assembly (1 hour)

### Step 13: Cable Management

1. Secure all wires along frame with zip ties
2. Ensure no wires near wheels or moving parts
3. Route motor wires through frame channel
4. Trim excess zip ties

### Step 14: Upload Firmware

1. Connect Arduino to computer via USB
2. Open Arduino IDE
3. Load phi-cargo-cart firmware (provided separately)
4. Upload to Arduino Nano

### Step 15: Initial Test

1. **DO NOT load cargo yet**
2. Turn on power switch
3. Verify OLED display shows battery voltage
4. Lift rear wheel off ground
5. Test throttle — wheel should spin
6. Test brake — wheel should stop
7. Verify remote Bluetooth connection

### Step 16: Load Test

1. Start with light cargo (10 kg)
2. Push cart at walking speed
3. Engage throttle gently
4. Test braking with cargo
5. Gradually increase cargo weight
6. Test hill climbing with moderate load

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Cart won't power on | Check fuse, battery voltage, power switch |
| Motor doesn't spin | Check phase wire connections, re-pair remote |
| Motor stutters | Check hall sensor connections, re-calibrate ESC |
| Steering is stiff | Lubricate caster, check alignment |
| Remote disconnects | Re-pair remote, check battery level |
| OLED shows garbage | Check I2C connections (A4=SDA, A5=SCL) |
| Range is short | Check battery balance, reduce cargo weight |
| Brakes too weak | Adjust brake sensitivity on ESC |
