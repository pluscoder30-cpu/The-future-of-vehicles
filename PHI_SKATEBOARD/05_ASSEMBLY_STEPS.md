# PHI_SKATEBOARD — Assembly Steps

> **Skill Level**: Beginner (12-year-old can do it with adult supervision)
> **Time**: 4-5 hours
> **Tools Needed**: Screwdrivers, wire strippers, soldering iron, Allen key set, multimeter

---

## Phase 1: Assemble the Deck (30 minutes)

### Step 1: Prepare the Deck

1. Take the bamboo deck out of packaging
2. Sand any rough edges with 120-grit sandpaper
3. Apply grip tape to the top surface:
   - Peel backing off grip tape
   - Align with deck edges
   - Press down firmly from center outward
   - Use a razor blade to trim excess around edges
4. Apply foam grip pads to standing areas (4 pads, one per quadrant)

### Step 2: Install the Trucks

1. Take the reverse kingpin trucks (2 total)
2. Insert bushings into each truck:
   - Barrel bushing on bottom (toward deck)
   - Cone bushing on top (toward road)
3. Position front truck on deck (4 bolt holes)
4. Insert M10 bolts from top of deck through holes
5. Thread truck baseplate onto bolts from below
6. Tighten nuts with Allen key — snug but not overtightened
7. Repeat for rear truck

**Tip**: Leave truck bolts slightly loose until final tuning — you'll adjust tightness after first ride.

---

## Phase 2: Install the Hub Motor (1 hour)

### Step 3: Mount the Hub Motor

1. Take the 500W hub motor wheel
2. The motor has a built-in axle — it slides into the rear truck hanger
3. Insert motor axle into the truck hanger slot
4. Secure with the axle nut (finger-tight, then 1/4 turn with wrench)
5. Make sure wheel spins freely without rubbing the truck

### Step 4: Install Non-Drive Wheels

1. Take 3× free-spinning 90mm wheels
2. Insert ABEC-7 bearings into each wheel (2 per wheel)
3. Add wheel spacer between bearings
4. Slide wheel onto front truck axle
5. Add speed washer, then axle nut
6. Tighten until wheel spins with slight resistance
7. Repeat for other front wheel and one rear wheel

### Step 5: Route Motor Wires

1. The hub motor has 3 phase wires (Blue, Green, Yellow) + 3 hall sensor wires
2. Route wires through the truck hanger channel
3. Secure with zip ties to prevent rubbing
4. Feed wires up through a hole in the deck (drill 10mm hole if needed)

---

## Phase 3: Build the Battery Pack (1.5 hours)

### Step 6: Assemble Battery Cells

1. Take 10 LiFePO4 26650 cells (3.2V 10Ah each)
2. Arrange in a 10S configuration (10 in series)
3. Use nickel strips and spot welder (or solder carefully):
   - Cell 1 (+) → Cell 2 (-) → Cell 3 (-) → ... → Cell 10 (-)
   - **Do NOT use regular solder on cells** — use nickel strips
4. Connect the BMS board:
   - BMS B- → Cell 1 (-) [main negative]
   - BMS B1 → between cells 1-2
   - BMS B2 → between cells 2-3
   - ... continue for all balance leads
   - BMS B+ → Cell 10 (+) [main positive]
5. Connect the XT60 connector:
   - XT60 Red (+) → BMS P+ (pack positive)
   - XT60 Black (-) → BMS P- (pack negative)

### Step 7: Test Battery Pack

1. Use multimeter to verify total voltage: should be **32V-36V** (10 × 3.2V nominal)
2. Check each balance lead: should be 3.0-3.3V per cell
3. Plug in BMS — verify green light (balanced)
4. **If any cell is below 2.8V, DO NOT USE — return for warranty**

### Step 8: Enclose the Battery

1. Place battery pack in ABS enclosure
2. Add foam padding on all sides (prevents vibration)
3. Feed XT60 connector and balance leads through enclosure hole
4. Seal enclosure with silicone (waterproof the hole)
5. Mount enclosure under deck with zip ties + foam padding

---

## Phase 4: Wire the Electronics (1 hour)

### Step 9: Connect the ESC

1. Mount ESC on top of battery enclosure (double-sided tape + zip tie)
2. Connect battery to ESC:
   - ESC BATTERY+ → XT60 Red (+)
   - ESC BATTERY- → XT60 Black (-)
3. Connect motor to ESC:
   - ESC MOTOR U → Motor Blue wire
   - ESC MOTOR V → Motor Green wire
   - ESC MOTOR W → Motor Yellow wire
4. Connect hall sensors:
   - ESC HALL U → Motor hall sensor U
   - ESC HALL V → Motor hall sensor V
   - ESC HALL W → Motor hall sensor W
   - ESC 5V → Hall sensor VCC
   - ESC GND → Hall sensor GND

### Step 10: Install the Arduino Display

1. Mount Arduino Nano on perfboard
2. Connect OLED display to I2C pins (A4=SDA, A5=SCL)
3. Connect voltage divider:
   - 36V → 33kΩ resistor → A0
   - A0 → 3.3kΩ resistor → GND
4. Connect 5V power from LM2596 buck converter to Arduino VIN
5. Mount display on deck edge (visible while riding)
6. Secure all wiring with zip ties

### Step 11: Pair the Remote

1. Turn on ESC (flip power switch)
2. Turn on Bluetooth remote
3. Hold pairing button on remote for 3 seconds
4. Wait for LED to stop blinking (paired)
5. Test throttle: thumb forward = accelerate
6. Test brake: trigger pull = brake
7. Test range: walk 10m away — should stay connected

---

## Phase 5: Final Assembly (30 minutes)

### Step 12: Secure Everything

1. Double-check all zip ties are tight
2. Verify no wires are near wheels or moving parts
3. Apply threadlocker to all axle nuts
4. Tighten truck bolts to desired tightness:
   - Loose = more turning (carving)
   - Tight = more stability (speed)

### Step 13: Initial Test

1. **DO NOT stand on the board yet**
2. Turn on power switch
3. Verify OLED display shows battery voltage (should be ~36V)
4. Lift rear wheel off ground
5. Gently apply throttle — wheel should spin
6. Apply brake — wheel should stop
7. Listen for unusual noises (grinding, clicking)
8. Check motor temperature after 30 seconds of running

### Step 14: First Ride

1. Find a flat, empty parking lot
2. **Wear all safety gear**: helmet, wrist guards, knee pads
3. Place board on ground
4. Step on with front foot first (over front truck)
5. Push off with back foot (like a regular skateboard)
6. Once rolling, engage throttle gently
7. Practice braking at low speed first
8. Ride in a straight line for 10 minutes before turning

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Board won't power on | Check fuse, battery voltage, power switch |
| Motor doesn't spin | Check phase wire connections, re-pair remote |
| Motor stutters | Check hall sensor connections, re-calibrate ESC |
| Remote disconnects | Re-pair remote, check battery level |
| OLED shows garbage | Check I2C connections (A4=SDA, A5=SCL) |
| Range is short | Check battery balance, reduce speed |
| Wheel wobbles | Tighten axle nut, check bearing alignment |
| Brakes too weak | Adjust brake sensitivity on ESC |
