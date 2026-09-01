# PHI PHASE CAR — Assembly Guide

## Estimated Build Time: 80-120 hours (motivated teenager, 2-4 weeks)

---

## PHASE 1: CHASSIS FRAME (16 hours)

### Step 1.1 — Cut the Frame Tubes
1. Measure and mark 4130 chromoly tubes per cut list below
2. Use angle grinder with cut-off wheel (SAFETY GLASSES + GLOVES)
3. Deburr all cuts with file or grinding wheel

**Cut List:**
- 2x 2000mm (main rails)
- 2x 1200mm (cross rails)
- 4x 600mm (uprights for cockpit)
- 4x 400mm (seat supports)
- 6x 300mm (coil mounts)
- 8x 200mm (bracket supports)
- Misc small pieces for Gussets

### Step 1.2 — Tack Weld the Base Rectangle
```
    <--------- 2000mm --------->
    +===========================+  ^
    |  [TACK WELD CORNERS]      |  |
    |                           |  1200mm
    |                           |  |
    +===========================+  v
    (Use square to check 90deg corners)
```
1. Lay tubes on flat surface (concrete floor)
2. Clamp corners with C-clamps
3. Check square with measuring tape (diagonals must be equal)
4. Tack weld 4 corners (small welds, check square again)
5. Full weld all 4 corners

### Step 1.3 — Add Cross Members
1. Weld 2 cross members at 1/3 and 2/3 points
2. Weld 2 diagonal gussets at corners for rigidity
3. Check for warping (re-measure diagonals)

### Step 1.4 — Add Uprights and Seat Rails
1. Weld 4 uprights (600mm) at cockpit positions
2. Connect uprights with seat rail tubes
3. Weld seat support cross-members

### Step 1.5 — Add Suspension Mounts
1. Drill and weld front suspension pickup points (reference 03_MECHANICAL.md)
2. Drill and weld rear suspension pickup points
3. Weld steering rack mounting bracket

### Step 1.6 — Grind and Clean
1. Grind all welds smooth with angle grinder
2. Check all dimensions against plan
3. Mark any corrections

---

## PHASE 2: DRIVETRAIN (12 hours)

### Step 2.1 — Mount Rear Hub Motors
1. Attach 19" wheel rims to hub motors (6x M10 bolts each)
2. Install airless tires on rims
3. Mount wheel+motor assemblies to rear suspension pickup points
4. Connect motor phase wires (A, B, C) temporarily
5. Verify free rotation (spin each wheel by hand)

### Step 2.2 — Mount Front Wheels
1. Install front 19" rims with airless tires
2. Mount to front suspension knuckles
3. Verify free rotation and steering range

### Step 2.3 — Mount Brake Calipers
1. Bolt 180mm rotors to each wheel (4x M8 bolts, 35 Nm)
2. Mount brake calipers on brackets (reference mechanical diagram)
3. Route brake lines from calipers to master cylinder location
4. Fill with DOT 4 fluid, bleed brakes (gravity bleed is fine)

### Step 2.4 — Install Motor Controllers
1. Mount 2x motor controllers on frame rails (zip ties + vibration pads)
2. Connect 72V power input (from DC-DC converter)
3. Connect phase wires to motors
4. Connect hall sensor wires to controllers
5. Connect throttle signal wire (0-5V from Arduino)

---

## PHASE 3: BATTERY & POWER (10 hours)

### Step 3.1 — Build Battery Bay
1. Cut aluminum sheet to create battery cradle
2. Bend sides up with sheet metal brake (or vise + hammer)
3. Line with foam padding
4. Bolt to frame rails (4x M8 bolts)

### Step 3.2 — Install FPB-20 Battery
1. Place battery in cradle
2. Secure with hold-down clamps (2x U-bolts)
3. Connect main positive (red 10 AWG) to main contactor
4. Connect main negative (black 10 AWG) to chassis ground bolt

### Step 3.3 — Install DC-DC Converters
1. Mount 144V->72V converter near battery (for motors)
2. Mount 144V->12V converter near fuse block (for aux)
3. Connect inputs to 144V bus (through fuses)
4. Connect outputs to respective bus bars

### Step 3.4 — Install Emergency Reserve
1. Mount small LiFePO4 pack in separate bay (away from main battery)
2. Connect through emergency fuse
3. Wire to emergency relay (activated on main power loss)

### Step 3.5 — Install Fuse Block and Contactor
1. Mount main contactor on frame (accessible for emergency key)
2. Mount 6-way fuse block on frame rail
3. Wire all circuits through fuses per wiring diagram

---

## PHASE 4: COOLING SYSTEM (6 hours)

### Step 4.1 — Install Radiators
1. Mount radiator 1 in front (behind grille area)
2. Mount radiator 2 on side panel
3. Secure with rubber-isolated brackets

### Step 4.2 — Install Water Pumps
1. Mount pump 1 for coil loop
2. Mount pump 2 for motor loop
3. Connect to 12V power through relay

### Step 4.3 — Route Hoses
1. Cut silicone hose to length
2. Connect pump -> radiator -> coils -> pump (loop 1)
3. Connect pump -> radiator -> motors -> pump (loop 2)
4. Secure with brass hose clamps
5. Fill with 50/50 glycol-water mix

### Step 4.4 — Install Temp Sensors
1. Thread NPT temp sensors into T-fittings
2. Connect to Arduino analog inputs
3. Program cutoff at 90C

---

## PHASE 5: CONTROL SYSTEM (16 hours)

### Step 5.1 — Mount Raspberry Pi
1. Mount Pi in protective case on frame rail
2. Connect 5V power supply
3. Connect Ethernet cable
4. Mount 7" touchscreen on dashboard bracket
5. Connect HDMI + USB power to touchscreen

### Step 5.2 — Mount Arduino Mega
1. Mount Arduino in project box on frame rail
2. Connect USB cable to Pi (serial comms)
3. Wire all sensor inputs per wiring diagram

### Step 5.3 — Install Sensors
1. Mount 4x ultrasonic sensors at corners of vehicle
2. Mount GPS module on roof
3. Mount IMU on center of chassis
4. Mount current sensors on battery leads
5. Mount voltage dividers on 144V bus

### Step 5.4 — Wire Control System
1. Follow wiring diagram 02_WIRING.md precisely
2. Use crimping tool for all connectors
3. Label every wire with tape marker
4. Route wires through wire loom
5. Secure with cable ties every 6 inches

### Step 5.5 — Install Relay Module
1. Mount 8-channel relay module
2. Wire relay outputs to:
   - Motor enable (x2)
   - Coil enable
   - Water pump 1
   - Water pump 2
   - Contactors
   - Lights
   - Buzzer
3. Wire relay inputs to Arduino digital outputs

### Step 5.6 — Install Dashboard Display
1. Mount 15" OLED on dashboard frame
2. Connect to Pi via HDMI
3. Install display software (see software guide)

---

## PHASE 6: BODY PANELS (14 hours)

### Step 6.1 — Create Panel Templates
1. Use cardboard to mock up each panel
2. Tape to frame, mark cut lines
3. Check clearances for all components

### Step 6.2 — Cut ABS Panels
1. Transfer templates to ABS sheets
2. Cut with jigsaw or bandsaw
3. Heat-form curves with heat gun (ABS bends at 160C)
4. Test fit each panel before finishing

### Step 6.3 — Fiberglass Reinforcement (optional)
1. Lay fiberglass cloth on high-stress areas
2. Apply epoxy resin with brush
3. Let cure 24 hours
4. Sand smooth

### Step 6.4 — Finish Panels
1. Fill imperfections with Bondo
2. Sand with 80 -> 150 -> 220 -> 400 grit
3. Prime with automotive primer (2 coats)
4. Paint with automotive paint (3 coats)
5. Clear coat (2 coats)
6. Wet sand with 1500 grit, buff

### Step 6.5 — Attach Panels
1. Pre-drill mounting holes
2. Use rubber grommets (vibration isolation)
3. Bolt with M5 x 0.8 stainless bolts + nylon lock nuts
4. Leave 2mm gap between panels for thermal expansion

---

## PHASE 7: PHASE COILS (16 hours)

### Step 7.1 — Wind Coils (x12)
1. Cut PVC pipe to 4" length (12 pieces)
2. Wind Litz wire around form: 120 turns per coil
3. Keep tension even, no overlaps
4. Leave 6" leads on each end
5. Wrap copper foil around outside (grounded shield)

### Step 7.2 — Build Capacitor Banks
1. Solder 100pF ceramic caps in parallel (10 per bank)
2. Solder 0.1uF film caps in parallel (5 per bank)
3. Connect capacitor bank across coil leads
4. Verify resonance at 1.618 MHz with oscilloscope

### Step 7.3 — Mount Coils
1. Bolt aluminum mounting brackets to frame
2. Install rubber vibration isolators on brackets
3. Mount coils at phi-angles per mechanical diagram
4. Connect water cooling hose through each coil
5. Wire coil leads to coil drivers (XT60 connectors)

### Step 7.4 — Coil Wiring
1. Connect all coil positive leads to coil driver bus
2. Connect all coil negative leads to coil driver bus
3. Connect coil driver control signals to Arduino
4. Route cooling hoses through all 12 coils in series
5. Fill loop with coolant, bleed air

---

## PHASE 8: SEATING & SAFETY (8 hours)

### Step 8.1 — Install Seats
1. Bolt seat brackets to seat rail cross-members
2. Mount front seats (driver + passenger)
3. Mount rear seats (if space allows)
4. Install seat sliders on front seats

### Step 8.2 — Install Seatbelts
1. Mount retractor mechanism to B-pillar area
2. Route belt through guide loop
3. Mount buckle to center console area
4. Test retraction and locking

### Step 8.3 — Install Safety Systems
1. Mount fire extinguisher (accessible, driver side)
2. Wire emergency kill switch to contactor coil
3. Wire smoke detector to 12V circuit
4. Mount emergency flasher on roof
5. Test all emergency circuits

---

## PHASE 9: FINAL ASSEMBLY & TESTING (8 hours)

### Step 9.1 — Final Wiring Check
1. Verify every connection against wiring diagram
2. Check for loose connectors
3. Verify ground connections
4. Check fuse ratings match circuits

### Step 9.2 — Power-Up Sequence (DO THIS LAST)
1. **Step 1:** Verify all switches OFF
2. **Step 2:** Connect battery (last connection!)
3. **Step 3:** Turn key to ON (contactor closes)
4. **Step 4:** Check 12V bus voltage (should be 12-14V)
5. **Step 5:** Check 72V bus voltage (should be 72-76V)
6. **Step 6:** Boot Raspberry Pi
7. **Step 7:** Boot Arduino
8. **Step 8:** Verify all sensors read correctly
9. **Step 9:** Test motor spin (lift wheels off ground!)
10. **Step 10:** Test brakes (manually push vehicle)
11. **Step 11:** Test emergency kill switch
12. **Step 12:** Test phase coil power-up (listen for hum)

### Step 9.3 — First Drive
1. Clear area of all people and objects
2. Lift wheels off ground, verify spin direction
3. Lower to ground, gentle throttle
4. Drive 10 meters, stop, test brakes
5. Drive in circles, test steering
6. Increase speed gradually
7. **DO NOT TEST PHASE SHIFT on first drive**

### Step 9.4 — Phase Coil Test
1. Verify coolant temperature < 65C
2. Power up coils at low power (25%)
3. Listen for resonance hum (1.618 MHz)
4. Check coil temperatures with IR thermometer
5. Increase to 50%, check again
6. Increase to 75%, check again
7. Full power test only after thermal stability confirmed

---

## SAFETY WARNINGS

**BEFORE FIRST DRIVE:**
- [ ] All bolts torqued to spec
- [ ] All electrical connections secure
- [ ] No exposed wires or terminals
- [ ] Emergency kill switch functional
- [ ] Brakes tested and working
- [ ] Fire extinguisher mounted and charged
- [ ] Battery fully charged
- [ ] Coolant system full and no leaks
- [ ] All body panels secure
- [ ] seats and seatbelts installed

**FIRST DRIVE RULES:**
- Drive at low speed (< 30 km/h) for first hour
- Test brakes gently at each speed
- No passengers on first drive
- No phase shift on first drive
- Have a spotter outside the vehicle
- Carry phone for emergency
