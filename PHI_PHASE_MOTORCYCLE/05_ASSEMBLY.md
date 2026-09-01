# PHI PHASE MOTORCYCLE — Assembly Guide

## Estimated Build Time: 60-80 hours (motivated teenager, 1-3 weeks)

---

## PHASE 1: FRAME FABRICATION (12 hours)

### Step 1.1 — Cut the Frame Tubes
1. Measure and mark 4130 chromoly tubes per cut list below
2. Use angle grinder with cut-off wheel (SAFETY GLASSES + GLOVES)
3. Deburr all cuts with file

**Cut List:**
- 2x 1200mm (main rails — top and bottom)
- 2x 400mm (head tube gussets)
- 2x 300mm (cross members)
- 2x 200mm (seat post supports)
- 4x 150mm (bracket supports)
- 1x 200mm (steering head tube — 1 1/8" ID)
- Misc small pieces for Gussets

### Step 1.2 — Tack Weld the Main Frame
```
    TOP VIEW:
    <---- 1200mm ---->
    +=================+
    |  [TACK CORNERS] |  <- 750mm wide
    |                 |
    +=================+

    SIDE VIEW:
    +=================+  TOP RAIL
    |  /           \  |
    | / HEAD TUBE   \ |
    |/               \|
    +=================+  BOTTOM RAIL
```
1. Lay tubes on flat concrete floor
2. Clamp with C-clamps, check square
3. Tack weld corners (small welds, check square again)
4. Full weld all 4 corners

### Step 1.3 — Add Head Tube
1. Insert 1 1/8" ID tube vertically between rails at front
2. Weld top and bottom gussets for rigidity
3. Insert headset bearings (top and bottom)
4. Verify alignment with straight edge

### Step 1.4 — Add Cross Members and Gussets
1. Weld 2 cross members for rigidity
2. Add gusset plates at high-stress areas:
   - Steering head junction
   - Swingarm pivot
   - Shock mount
3. Check all angles with protractor

### Step 1.5 — Add Mounting Points
1. Drill and weld swingarm pivot holes (M12)
2. Weld shock mount tabs
3. Weld battery bay brackets
4. Weld footpeg mounting tabs
5. Weld handlebar clamp mounts
6. Weld seat rail mounts

### Step 1.6 — Grind and Clean
1. Grind all welds smooth
2. Check dimensions against plan
3. Sand frame for paint prep

---

## PHASE 2: FORK & SWINGARM (8 hours)

### Step 2.1 — Install Front Fork
1. Slide fork tubes through triple clamps
2. Tighten pinch bolts (10 Nm, blue Loctite)
3. Install steering stem through head tube
4. Adjust headset bearings (snug, no play)
5. Lock steering stem nut

### Step 2.2 — Install Rear Swingarm
1. Align swingarm pivot holes with frame
2. Insert M12 pivot bolt
3. Tighten to 70 Nm with nylock nut
4. Verify swingarm moves freely

### Step 2.3 — Install Rear Shock
1. Mount upper shock eyelet to frame tab
2. Mount lower shock eyelet to swingarm tab
3. Insert M10 bolts, torque to 40 Nm
4. Set sag to 30% (30mm of 100mm travel)

### Step 2.4 — Install Handlebars
1. Clamp handlebars in triple clamp mounts
2. Position: 30mm rise, 15deg sweep back
3. Tighten clamp bolts to 10 Nm
4. Attach grips (lock-on style, no glue needed)

---

## PHASE 3: DRIVETRAIN (6 hours)

### Step 3.1 — Install Rear Hub Motor
1. Slide rear axle through swingarm
2. Mount 17" rim with airless tire
3. Connect motor phase wires (A, B, C) to controller
4. Connect hall sensor wires
5. Verify free rotation (spin wheel by hand)
6. Tighten axle nuts to 80 Nm

### Step 3.2 — Install Front Wheel
1. Slide front axle through fork dropouts
2. Mount 17" rim with airless tire
3. Tighten axle nuts to 75 Nm
4. Verify free rotation

### Step 3.3 — Install Motor Controller
1. Mount controller on frame rail (zip ties + vibration pads)
2. Connect 72V power input (from DC-DC converter)
3. Connect phase wires to motor
4. Connect hall sensor wires
5. Connect throttle signal wire

### Step 3.4 — Install Throttle
1. Mount twist throttle on right handlebar
2. Route throttle cable to controller
3. Connect 0-5V signal wire
4. Test: full twist = full power, release = zero

### Step 3.5 — Install Brake Levers
1. Mount left lever (rear brake)
2. Mount right lever (front brake)
3. Both have regen switch integrated
4. Route brake lines to calipers
5. Fill with DOT 4 fluid, bleed brakes
6. Test regen: both levers regenerate on first pull

---

## PHASE 4: BATTERY & POWER (8 hours)

### Step 4.1 — Build Battery Bay
1. Cut aluminum sheet to create battery cradle
2. Bend sides up with vise + hammer (or sheet metal brake)
3. Line with foam padding
4. Bolt to frame rails (4x M8 bolts)

### Step 4.2 — Install FPB-10 Battery
1. Place battery in cradle
2. Secure with hold-down clamps (2x U-bolts)
3. Connect main positive (red 10 AWG) to main contactor
4. Connect main negative (black 10 AWG) to frame ground bolt

### Step 4.3 — Install DC-DC Converters
1. Mount 96V->72V converter near battery (for motor)
2. Mount 96V->12V converter near fuse block (for aux)
3. Connect inputs to 96V bus (through fuses)
4. Connect outputs to respective bus bars

### Step 4.4 — Install Emergency Reserve
1. Mount small LiFePO4 pack in separate bay
2. Connect through emergency fuse
3. Wire to emergency relay

### Step 4.5 — Install Fuse Block and Contactor
1. Mount main contactor on frame (accessible for emergency key)
2. Mount 4-way fuse block on frame rail
3. Wire all circuits through fuses per wiring diagram

---

## PHASE 5: COOLING SYSTEM (4 hours)

### Step 5.1 — Install Radiator
1. Mount radiator on side of frame (airflow when riding)
2. Secure with rubber-isolated brackets

### Step 5.2 — Install Water Pump
1. Mount pump below radiator (gravity feed)
2. Connect to 12V power through relay

### Step 5.3 — Route Hoses
1. Cut silicone hose to length
2. Connect pump -> radiator -> coils -> pump (loop)
3. Secure with hose clamps
4. Fill with 50/50 glycol-water mix
5. Bleed air from system

### Step 5.4 — Install Temp Sensors
1. Thread NPT temp sensors into T-fittings
2. Connect to Arduino analog inputs
3. Program cutoff at 90C

---

## PHASE 6: CONTROL SYSTEM (10 hours)

### Step 6.1 — Mount Raspberry Pi Zero 2W
1. Mount Pi in protective case on frame rail
2. Connect 5V power supply
3. Mount 5" touchscreen on fairing bracket
4. Connect via HDMI ribbon cable

### Step 6.2 — Mount Arduino Uno
1. Mount Arduino in project box on frame rail
2. Connect USB cable to Pi (serial comms)
3. Wire all sensor inputs per wiring diagram

### Step 6.3 — Install Sensors
1. Mount 2x ultrasonic sensors at front
2. Mount GPS module on top of frame
3. Mount IMU on center of chassis
4. Mount current sensor on battery lead
5. Mount voltage divider on 96V bus

### Step 6.4 — Wire Control System
1. Follow wiring diagram 02_WIRING.md precisely
2. Use crimping tool for all connectors
3. Label every wire with tape marker
4. Route wires through wire loom
5. Secure with cable ties every 4 inches

### Step 6.5 — Install Relay Module
1. Mount 4-channel relay module
2. Wire relay outputs to:
   - Motor enable
   - Coil enable
   - Water pump
   - Lights/buzzer
3. Wire relay inputs to Arduino digital outputs

### Step 6.6 — Install OLED Display
1. Mount 0.96" OLED in center of dashboard
2. Connect to Arduino I2C (SDA/SCL)
3. Display: speed, battery, phase status

---

## PHASE 7: FAIRING & BODY (10 hours)

### Step 7.1 — Create Fairing Templates
1. Use cardboard to mock up each panel
2. Tape to frame, mark cut lines
3. Check clearances for all components

### Step 7.2 — Cut ABS Panels
1. Transfer templates to ABS sheets
2. Cut with jigsaw
3. Heat-form curves with heat gun
4. Test fit each panel

### Step 7.3 — Fiberglass Reinforcement
1. Lay fiberglass cloth on fairing interior
2. Apply epoxy resin with brush
3. Let cure 24 hours
4. Sand smooth

### Step 7.4 — Finish Fairing
1. Fill imperfections with Bondo
2. Sand with 80 -> 150 -> 220 -> 400 grit
3. Prime (2 coats)
4. Paint (3 coats)
5. Clear coat (2 coats)
6. Wet sand with 1500 grit, buff

### Step 7.5 — Attach Fairing
1. Pre-drill mounting holes
2. Use rubber grommets for vibration isolation
3. Bolt with M5 stainless bolts + nylon lock nuts
4. Leave gaps for cooling airflow

### Step 7.6 — Install Lights
1. Mount LED headlight in front fairing
2. Mount LED taillight in rear
3. Wire to 12V through relay
4. Test: high beam, low beam, running, brake

---

## PHASE 8: PHASE COILS (10 hours)

### Step 8.1 — Wind Coils (x6)
1. Cut PVC pipe to 3" length (6 pieces)
2. Wind Litz wire around form: 90 turns per coil
3. Keep tension even, no overlaps
4. Leave 6" leads on each end
5. Wrap copper foil around outside (grounded shield)

### Step 8.2 — Build Capacitor Banks
1. Solder 100pF ceramic caps in parallel (6 per bank)
2. Solder 0.05uF film caps in parallel (3 per bank)
3. Connect capacitor bank across coil leads
4. Verify resonance at 1.618 MHz with oscilloscope

### Step 8.3 — Mount Coils
1. Bolt aluminum mounting rings to fairing brackets
2. Install rubber vibration isolators
3. Mount coils at phi-angles per mechanical diagram
4. Connect water cooling hose through each coil
5. Wire coil leads to coil drivers (XT60 connectors)

### Step 8.4 — Coil Wiring
1. Connect all coil positive leads to coil driver bus
2. Connect all coil negative leads to coil driver bus
3. Connect coil driver control signals to Arduino
4. Route cooling hoses through all 6 coils in series
5. Fill loop with coolant, bleed air

---

## PHASE 9: SAFETY & RIDER SYSTEMS (4 hours)

### Step 9.1 — Install Harness
1. Mount harness anchor points to frame (4 points)
2. Install shoulder strap anchors behind seat
3. Install lap belt anchors on frame rails
4. Test quick-release mechanism

### Step 9.2 — Install Safety Systems
1. Mount fire extinguisher (accessible, right side)
2. Wire emergency kill switch to contactor coil
3. Mount emergency flasher on rear
4. Test all emergency circuits

### Step 9.3 — Install Rider Comfort
1. Mount seat on frame
2. Install footpegs on brackets
3. Mount mirrors on handlebar ends
4. Install helmet communication system

---

## PHASE 10: FINAL ASSEMBLY & TESTING (6 hours)

### Step 10.1 — Final Wiring Check
1. Verify every connection against wiring diagram
2. Check for loose connectors
3. Verify ground connections
4. Check fuse ratings

### Step 10.2 — Power-Up Sequence (DO THIS LAST)
1. **Step 1:** Verify all switches OFF
2. **Step 2:** Connect battery (last connection!)
3. **Step 3:** Turn key to ON (contactor closes)
4. **Step 4:** Check 12V bus voltage (12-14V)
5. **Step 5:** Check 72V bus voltage (72-76V)
6. **Step 6:** Boot Raspberry Pi
7. **Step 7:** Boot Arduino
8. **Step 8:** Verify all sensors read correctly
9. **Step 9:** Test motor spin (lift wheel off ground!)
10. **Step 10:** Test brakes (manually push motorcycle)
11. **Step 11:** Test emergency kill switch
12. **Step 12:** Test phase coil power-up (listen for hum)

### Step 10.3 — First Ride
1. Clear area of all people and objects
2. Lift rear wheel off ground, verify spin direction
3. Lower to ground, gentle throttle
4. Ride 20 meters, stop, test brakes
5. Ride in circles, test steering
6. Increase speed gradually
7. **DO NOT TEST PHASE SHIFT on first ride**

### Step 10.4 — Phase Coil Test
1. Verify coolant temperature < 65C
2. Power up coils at low power (25%)
3. Listen for resonance hum (1.618 MHz)
4. Check coil temperatures with IR thermometer
5. Increase to 50%, check again
6. Increase to 75%, check again
7. Full power test only after thermal stability confirmed

---

## SAFETY WARNINGS

**BEFORE FIRST RIDE:**
- [ ] All bolts torqued to spec
- [ ] All electrical connections secure
- [ ] No exposed wires or terminals
- [ ] Emergency kill switch functional
- [ ] Brakes tested and working (front + rear)
- [ ] Fire extinguisher mounted and charged
- [ ] Battery fully charged
- [ ] Coolant system full and no leaks
- [ ] Fairing secure
- [ ] Harness tested (quick-release works)
- [ ] Helmet (DOT approved minimum)
- [ ] Protective riding gear

**FIRST RIDE RULES:**
- Ride at low speed (< 30 km/h) for first hour
- Test brakes gently at each speed
- No passenger on first ride
- No phase shift on first ride
- Have a spotter outside
- Carry phone for emergency
- Wear full gear (helmet, gloves, jacket, boots)
