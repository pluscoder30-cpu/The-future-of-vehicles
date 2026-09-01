# PHI SUBMERSIBLE — Assembly Guide

**Skill Level:** 12-year-old friendly (with adult supervision)
**Time:** 8-10 hours
**Tools Needed:** Drill, soldering iron, multimeter, wrenches, screwdrivers

---

## Step 1: Build the Frame (30 min)

1. Cut aluminum 2020 extrusions to length:
   - 4x vertical rails: 500mm each
   - 4x horizontal rails: 400mm each

2. Connect rails with corner brackets (item #9):
   - Insert T-nuts into rail slots
   - Attach brackets with M5 bolts
   - Tighten finger-tight, then 1/4 turn with wrench

3. Your frame should look like a box:
   ```
   +---+===============+---+
   |   |               |   |
   +---+===============+---+
   |   |               |   |
   +---+===============+---+
   ```

4. **CHECK:** Frame sits flat on table, all corners are 90°

---

## Step 2: Prepare the Hull (45 min)

1. Take the HDPE pipe (item #2, 400mm × 1200mm)

2. Drill mounting holes for frame:
   - 8 holes, 8mm diameter
   - 4 on each side, evenly spaced
   - Use frame as template for alignment

3. Install flange on one end:
   - Apply marine sealant (item #47) around flange face
   - Align with pipe end
   - Insert bolts through flange holes
   - Tighten in star pattern (opposite bolts first)

4. **SAFETY CHECK:** Run finger around flange — no gaps in sealant

---

## Step 3: Install the Acrylic Dome (30 min)

1. Grease O-rings (item #5) with silicone grease:
   - Roll O-ring in your fingers with grease
   - Should feel slippery, not sticky

2. Seat O-ring in flange groove:
   - Groove is 3mm deep, 5mm wide
   - Push O-ring in, make sure it's not twisted

3. Place acrylic dome onto flange:
   - Dome sits on top of O-ring
   - Align bolt holes

4. Tighten flange bolts (star pattern):
   ```
   Tighten order:  1  4
                   3  2
                   (opposite pairs)
   ```
   - 5 Nm torque (hand-tight + 1/4 turn)

5. **LEAK TEST (IMPORTANT!):**
   - Fill sink with 10cm of water
   - Place dome/hull assembly in water
   - Wait 5 minutes
   - Check inside for ANY water
   - No water = PASS. Water = re-do seal

---

## Step 4: Mount the Battery (20 min)

1. Place battery (item #17) inside hull

2. Secure with battery box (item #18):
   - Position at bottom of hull (low center of gravity)
   - Screw box to hull wall with self-tapping screws
   - Battery clicks into box

3. Connect battery monitor (item #21):
   - Red wire to battery positive (+)
   - Black wire to battery negative (-)
   - Display should light up showing voltage

4. **CHECK:** Battery monitor shows ~36V (fully charged)

---

## Step 5: Install the Propulsion (45 min)

1. Mount motor bracket (item #14) to frame:
   - Use M6 bolts (item #44)
   - Position at rear of frame

2. Install through-hull bearing (item #15):
   - Drill 12mm hole in rear end cap (item #3)
   - Apply sealant around bearing
   - Push bearing through hole
   - Let sealant cure 10 minutes

3. Connect shaft coupling (item #16):
   - Slide coupling onto motor shaft
   - Tighten set screws (Allen key)
   - Slide coupling onto propeller shaft
   - Tighten set screws

4. Attach propeller (item #12):
   - Thread propeller onto shaft
   - Tighten prop nut (reverse thread!)
   - Spin by hand — should be smooth

5. Install prop duct (item #13):
   - Slide duct over propeller
   - Zip-tie to frame rails
   - Should NOT touch propeller blades

6. **SPIN TEST:** Connect battery briefly, motor should spin smoothly

---

## Step 6: Wire the Electronics (1 hour)

1. Follow the wiring diagram (02_WIRING.md)

2. Connect components in this order:
   - Battery → Main fuse → Switch panel
   - Fuse → ESC → Motor
   - Battery → 12V step-down → Pump + Lights

3. Solder all connections:
   - Twist wires together
   - Apply solder (shiny, not dull)
   - Cover with heat-shrink tubing
   - Heat with heat gun or lighter

4. Install cable glands (item #30):
   - Drill holes where wires exit hull
   - Feed wires through glands
   - Tighten gland nut until snug

5. **POWER TEST:**
   - Turn on SW1 — motor should be silent
   - Turn on SW3 — lights should turn on
   - Turn on SW2 — pump should hum

---

## Step 7: Ballast System (30 min)

1. Mount ballast tank (item #7) inside hull:
   - Position at lowest point (center bottom)
   - Secure with brackets

2. Connect ballast pump (item #32):
   - Inlet goes to through-hull fitting
   - Outlet goes to tank
   - Use check valves (item #35) to prevent backflow

3. Connect solenoid valve (item #33):
   - Wire to SW2 (toggle switch)
   - When ON = valve opens = water fills tank
   - When OFF = valve closes = pump empties tank

4. **BALLAST TEST (dry):**
   - Turn pump ON — should hear motor run
   - Turn pump OFF — should stop
   - Turn valve ON/OFF — should hear click

---

## Step 8: Safety Systems (20 min)

1. Install kill switch (item #27):
   - Attach lanyard to wrist strap
   - Magnet connects to switch
   - Pulling magnet away = motor stops INSTANTLY

2. Test kill switch:
   - Motor running
   - Pull magnet away
   - Motor MUST stop within 1 second
   - If not: RE-WIRE (faulty connection)

3. Install dive flag (item #37):
   - Attach to top of dome
   - Visible from 100m+

4. Store safety gear inside:
   - O2 bottle (item #39) — within arm's reach
   - Whistle (item #40) — clipped to harness
   - Knife (item #42) — sheathed on belt

---

## Step 9: Final Assembly (30 min)

1. Attach frame to hull:
   - Slide frame rails into drilled holes
   - Secure with M6 bolts + washers
   - Tighten all bolts

2. Attach buoyancy foam (item #10):
   - Position on top and bottom of hull
   - Zip-tie through pre-drilled holes
   - Apply sealant where foam touches hull

3. Route all wiring:
   - Secure with cable ties every 150mm
   - No loose wires near propeller
   - No wires pinched by frame

4. Attach surface marker buoy (item #38):
   - Clip to rear of hull
   - Reel with 30m line

---

## Step 10: Pre-Dive Checklist

**BEFORE EVERY DIVE, CHECK:**

- [ ] O-ring seal inspected (no damage, no debris)
- [ ] Battery charged (>80%)
- [ ] Kill switch works (pull magnet, motor stops)
- [ ] Thruster spins freely (no debris on prop)
- [ ] All bolts tight (frame, dome, motor)
- [ ] No water inside hull (leak test)
- [ ] Ballast pump works (test on surface)
- [ ] Dive flag attached
- [ ] Safety gear accessible
- [ ] Buddy system (never dive alone!)

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Motor won't start | Kill switch active | Re-attach magnet |
| Motor runs but no thrust | Propeller loose | Tighten prop nut |
| Water leaking at dome | O-ring damaged | Replace O-ring |
| Water leaking at bolts | Sealant failed | Re-apply 3M 5200 |
| Pump won't run | Fuse blown | Replace 60A fuse |
| Battery dies fast | Cold water (capacity loss) | Pre-warm battery |
| Dome fogs up | Moisture inside | Add silica gel packs |
