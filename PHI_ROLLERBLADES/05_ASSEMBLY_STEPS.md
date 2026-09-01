# PHI_ROLLERBLADES — Assembly Steps

> **Skill Level**: Advanced (12-year-old can do it with adult supervision)
> **Time**: 8-10 hours over a weekend
> **Tools Needed**: Soldering iron, wire strippers, screwdrivers, Allen key set, multimeter, heat gun

---

## Phase 1: Prepare the Skate Boots (1 hour)

### Step 1: Disassemble Skates

1. Remove all wheels from both skates
2. Remove existing bearings from wheels
3. Remove frames from boots (unscrew frame bolts)
4. Set aside: boots, frames, bearings, axle bolts

### Step 2: Modify Frames for Hub Motor

1. The rear wheel position needs to accept the hub motor
2. The hub motor axle is 6mm (standard is 8mm)
3. Drill out rear axle holes to 6mm if needed
4. Test-fit hub motor wheel in rear position
5. Verify wheel spins freely

---

## Phase 2: Build the Hub Motors (2 hours)

### Step 3: Prepare Hub Motors

1. The hub motors come pre-wound (phi-harmonic winding)
2. Identify wire colors: Blue (U), Green (V), Yellow (W)
3. Identify hall sensor wires: Red (VCC), Black (GND), Blue/White/Orange (U/V/W)
4. Solder motor phase wires to XT30 connector
5. Solder hall sensor wires to JST connector
6. Heat-shrink all connections
7. **Repeat for second motor**

### Step 4: Install Motors in Wheels

1. Insert hub motor into rear wheel position
2. Secure with axle nuts (finger-tight, then 1/4 turn)
3. Verify wheel spins freely without rubbing
4. Route motor wires through frame channel
5. Secure with zip ties

### Step 5: Install Front Wheels

1. Insert bearings into front wheels (2 per wheel)
2. Add wheel spacer between bearings
3. Slide wheel onto front truck axle
4. Add speed washer, then axle nut
5. Tighten until wheel spins with slight resistance
6. Repeat for other front wheel

---

## Phase 3: Build the Battery Packs (2 hours)

### Step 6: Assemble Battery Cells

1. Take 10 LiFePO4 18650 cells (3.2V 5Ah each) per boot
2. Arrange in 10S configuration (10 in series)
3. Use nickel strips and spot welder:
   - Cell 1 (+) → Cell 2 (-) → ... → Cell 10 (-)
   - **Do NOT use regular solder** — use nickel strips
4. Connect BMS board:
   - BMS B- → Cell 1 (-)
   - BMS B1-B10 → between each cell pair
   - BMS B+ → Cell 10 (+)
5. Connect XT30 connector:
   - XT30 Red (+) → BMS P+
   - XT30 Black (-) → BMS P-
6. **Repeat for second battery pack**

### Step 7: Test Battery Packs

1. Verify total voltage: **32V-36V** per pack
2. Check each balance lead: 3.0-3.3V per cell
3. **If any cell below 2.8V, DO NOT USE**

### Step 8: Enclose Batteries

1. Place each battery pack in nylon pouch
2. Add foam padding on all sides
3. Feed XT30 connector through pouch opening
4. Seal pouch with Velcro strap
5. Test Velcro strap fits snugly around calf

---

## Phase 4: Build the Electronics (2 hours)

### Step 9: Build Arduino Boards

1. Take 2× Arduino Nano
2. Solder header pins
3. Mount on small perfboard (50×30mm)
4. Solder voltage divider (33kΩ + 3.3kΩ) to A1
5. Solder FSR connections to A0
6. Connect MPU-6050 to I2C pins (A4=SDA, A5=SCL)
7. Connect HC-05 Bluetooth to D12/D13
8. Connect ESC throttle wire to D9
9. **Repeat for second boot**

### Step 10: Install Pressure Sensors

1. Cut hole in toe area of each boot
2. Mount FSR sensor inside toe area
3. Connect to Arduino A0
4. Secure with hot glue
5. Test: press toe area, verify reading changes

### Step 11: Install IMU Sensors

1. Mount MPU-6050 on inside of each boot (ankle area)
2. Secure with hot glue + zip tie
3. Connect to Arduino I2C
4. Test: tilt boot, verify lean angle reading

### Step 12: Wire Everything

1. Mount ESC inside each boot (ankle area)
2. Connect battery to ESC via XT30
3. Connect motor to ESC (3 phase + hall sensors)
4. Connect Arduino to ESC throttle
5. Connect sensors to Arduino
6. Connect Bluetooth modules
7. Route all wires through boot shell
8. Secure with zip ties

---

## Phase 5: Final Assembly (1 hour)

### Step 13: Reassemble Skates

1. Reinstall frames on boots
2. Install hub motor wheels in rear position
3. Install front wheels
4. Tighten all axle bolts
5. Verify all wheels spin freely

### Step 14: Mount Battery Pouches

1. Wrap Velcro strap around calf area
2. Attach battery pouch to strap
3. Connect XT30 to boot
4. Verify battery is secure and doesn't interfere with skating

### Step 15: Upload Firmware

1. Connect Arduino to computer via USB
2. Open Arduino IDE
3. Load phi-rollerblade firmware (provided separately)
4. Upload to Arduino Nano
5. Repeat for second boot
6. Pair Bluetooth between boots

### Step 16: Initial Test

1. **DO NOT wear skates yet**
2. Turn on power switches
3. Verify both motors spin
4. Verify lean sensor activates motor
5. Verify Bluetooth sync works
6. Test heel brake stops motor
7. Put on safety gear

### Step 17: First Ride

1. Find a flat, empty parking lot
2. **Wear all safety gear**: helmet, wrist guards, knee pads, elbow pads
3. Put on skates, tighten buckles
4. Stand still, lean forward slightly
5. Feel motor engage (gentle push)
6. Practice at walking speed first
7. Practice braking with heel brake
8. Ride for 30 minutes before increasing speed

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Motor doesn't spin | Check ESC connections, verify firmware upload |
| Motor too powerful | Reduce throttle mapping in firmware |
| Lean sensor not working | Check FSR connections, adjust threshold |
| Bluetooth not pairing | Re-pair devices, check baud rate |
| One boot stronger than other | Calibrate both FSRs, adjust gains |
| Battery drains fast | Check for shorts, reduce speed |
| Wheel wobbles | Tighten axle nut, check bearing |
