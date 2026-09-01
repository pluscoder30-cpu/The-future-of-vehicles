# PHI SYNTHETIC WINGS — Assembly Guide

**Skill Level:** 12-year-old friendly (with adult supervision)
**Time:** 20-25 hours
**Tools Needed:** Rivet gun, soldering iron, multimeter, hex keys, sewing machine

---

## Step 1: Build the Wing Spars (1 hour)

1. Cut carbon fiber tubes to length:
   - Main spar: 1x 15mm × 6m (cut in half = 2x 3m)
   - Secondary spars: 4x 10mm × 3m each

2. Assemble main spar for LEFT wing:
   - Join 2x 3m sections with aluminum connector (item #3)
   - Push connector halfway into each tube
   - Apply Loctite (item #47) to connector
   - Let cure 10 minutes

3. Repeat for RIGHT wing

4. Your spars should be:
   ```
   LEFT WING:  |<----------- 6m ---------->|
   RIGHT WING: |<----------- 6m ---------->|
   ```

5. **CHECK:** Spars are straight, connectors tight

---

## Step 2: Build the Wing Ribs (2 hours)

1. 3D print rib spacers (item #7):
   - Print 24 total (4 per spar station × 6 stations)
   - Settings: PLA or PETG, 0.2mm layers, 20% infill
   - Print time: ~3 hours each

2. Each rib has:
   - Hole for 10mm spar
   - Hole for 15mm spar (at root station)
   - PHI-taper profile (airfoil shape)

3. Slide ribs onto spars:
   - Left wing: ribs face forward
   - Right wing: ribs face forward (mirror image)
   - Space at PHI intervals:
     ```
     Station 1: 0mm (root)
     Station 2: 382mm
     Station 3: 618mm
     Station 4: 1000mm
     ```

4. Secure ribs with zip ties through pre-printed holes

---

## Step 3: Attach Wing Skin (2 hours)

1. Lay out ripstop nylon (item #6):
   - Cut to wing shape (tapered, with flap cutout)
   - Leave 50mm extra on all edges

2. Drape skin over rib frame:
   - Start at root (thickest part)
   - Work toward tip
   - Pull skin taut (no wrinkles)

3. Attach with rivets (item #45):
   - Rivet through skin into rib spacers
   - Every 100mm along each rib
   - Pull skin tight before each rivet

4. Fold and sew wing tips:
   - Fold 50mm edge over
   - Sew with sewing machine
   - Strong seam (zigzag stitch)

5. Leave trailing edge OPEN for flap installation

---

## Step 4: Install Flap Hinges (1 hour)

1. Attach piano hinge (item #13) along trailing edge:
   - Position at 70% chord (30% from trailing edge)
   - Rivet hinge to wing skin every 50mm
   - Rivet other hinge leaf to flap skin

2. Test flap movement:
   - Flap should swing freely
   - Range: 0° (flush) to 45° (down)
   - No binding or sticking

3. Repeat for both wings

---

## Step 5: Install Servos (1 hour)

1. Mount servo 1 (left flap) and servo 2 (right flap):
   - Position near wing root (closest to body)
   - Attach servo mount (item #14) to spar with zip ties
   - Bolt servo to mount

2. Connect push rods (item #11):
   - Attach one end to servo horn (item #10)
   - Attach other end to bellcrank (item #12)
   - Bellcrank connects to flap

3. Test servo movement:
   - Arduino sends signal
   - Servo arm moves
   - Flap deflects

4. Install servo 3 (left pitch) and servo 4 (right pitch):
   - Same process as flap servos
   - Connect to pitch control surfaces

---

## Step 6: Build the Harness (1 hour)

1. Modify paragliding harness (item #15):
   - Add wing attachment points (item #20)
   - Bolt D-rings to harness at shoulder level
   - Position: directly above pilot's shoulders

2. Attach chest strap (item #16):
   - 50mm padded nylon
   - Buckles at front
   - Snug but comfortable

3. Attach leg straps (item #17):
   - 25mm nylon
   - Quick-release buckles
   - Through leg loops

4. Test harness:
   - Put on harness
   - Clip all buckles
   - Hang from D-rings (inverted)
   - Should support your weight without slipping

---

## Step 7: Install Battery (30 min)

1. Mount battery (item #21) to chest harness:
   - Quick-release bracket (item #22)
   - Position on back, centered
   - Accessible for removal

2. Connect battery:
   - XT60 connector (item #23)
   - Red to +, Black to -
   - Battery monitor (item #25) shows voltage

3. Test: Battery should show ~36V (fully charged)

---

## Step 8: Wire the Electronics (1.5 hours)

1. **Follow the wiring diagram (02_WIRING.md)**

2. Connect Arduino flight controller (item #26):
   - Mount to chest harness (easy access)
   - Connect servos to pins D3, D5, D6, D9
   - Connect ESC to pin D10
   - Connect kill switch to pin D2

3. Connect sensors:
   - IMU (item #26) via I2C (A4, A5)
   - Altimeter via SPI
   - Wing angle pots (item #28) to A1, A2
   - Throttle input (item #29) to A0

4. Solder ALL connections:
   - Twist wires
   - Solder
   - Heat-shrink

5. Secure wiring with cable ties:
   - Every 150mm along spars
   - No loose wires near flaps
   - No wires pinched at fold joint

6. **POWER TEST:**
   - Connect battery
   - Arduino should boot (LED blinks)
   - Move throttle — motor should spin
   - Move joystick — servos should respond

---

## Step 9: Install Propulsion (30 min)

1. Mount motor (item #34) to rear of harness:
   - Aluminum mount (item #36)
   - Bolt to harness frame

2. Attach propeller (item #35):
   - Thread onto motor shaft
   - Tighten (reverse thread!)
   - Test spin by hand — smooth

3. Connect ESC (item #37) to motor:
   - 3 wires from ESC to motor
   - Order doesn't matter (swap any 2 to reverse)

4. **MOTOR TEST:**
   - Throttle up gently
   - Motor should spin smoothly
   - Kill switch should stop motor instantly

---

## Step 10: Install Safety Gear (20 min)

1. Helmet (item #38):
   - Padded, aviation-style
   - Chin strap secure

2. Reserve parachute (item #39):
   - Store in harness compartment
   - Pin accessible with one hand
   - TEST: Practice pulling pin (on ground only!)

3. Altimeter (item #40):
   - Mount on wrist or chest
   - Set alarm for 500m

4. Radio (item #41):
   - Clip to harness
   - Earpiece in ear
   - Pre-set to emergency channel

5. GPS (item #42):
   - Mount where you can see it
   - Powered from battery

---

## Step 11: Wing Fold Test (20 min)

1. Deploy wings:
   - Pull lock pin on fold joint
   - Swing wings outward
   - Lock pin clicks into place

2. Fold wings:
   - Pull lock pin
   - Swing wings inward
   - Wings fold against body

3. Verify:
   - [ ] Wings lock in deployed position
   - [ ] Wings fold cleanly for storage
   - [ ] Lock pins are secure
   - [ ] No binding at fold joint

---

## Step 12: Ground Test (30 min)

1. Put on full system:
   - Harness on body
   - Chest strap buckled
   - Leg straps buckled
   - Battery connected
   - Kill switch attached to wrist

2. Stand up with wings deployed:
   - Wings should balance on your shoulders
   - Not too heavy (target: 12 kg total)

3. Test all controls:
   - Flap left/right — works
   - Pitch up/down — works
   - Throttle — motor spins
   - Kill switch — motor stops

4. **FLIGHT READINESS:**
   - All controls responsive
   - No strange sounds
   - No loose parts
   - Kill switch tested
   - Parachute pin accessible

---

## Pre-Flight Checklist

**BEFORE EVERY FLIGHT:**

- [ ] Wings locked in deployed position
- [ ] All bolts tight
- [ ] Servos respond to controls
- [ ] Motor spins on throttle
- [ ] Kill switch stops motor instantly
- [ ] Battery charged (>80%)
- [ ] Altimeter reads correctly
- [ ] Radio works
- [ ] GPS has satellite lock
- [ ] Helmet secured
- [ ] Parachute pin accessible
- [ ] Wind speed <20 km/h (beginners: <10 km/h)
- [ ] Open field, no obstacles
- [ ] Buddy system (never fly alone!)

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Flap doesn't move | Servo wire loose | Re-solder connection |
| Motor won't start | Kill switch active | Re-attach magnet |
| Motor runs backwards | Wires swapped | Swap any 2 motor wires |
| Wings won't lock | Lock pin bent | Replace pin |
| Wings fold in flight | Lock pin not engaged | Re-engage, check spring |
| Altimeter wrong | Calibration off | Recalibrate on ground |
| Radio static | Wrong channel | Check frequency setting |
| Battery dies fast | Cold weather | Pre-warm battery |
