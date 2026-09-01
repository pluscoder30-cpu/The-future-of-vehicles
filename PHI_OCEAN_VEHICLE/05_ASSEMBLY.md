# PHI OCEAN VEHICLE — Assembly Guide

**Skill Level:** 12-year-old friendly (with adult supervision)
**Time:** 14-18 hours
**Tools Needed:** Drill, fiberglass kit, soldering iron, multimeter, wrenches

---

## Step 1: Prepare the Hull (1 hour)

1. Inspect used kayak/canoe hull (item #1):
   - Check for cracks, holes, soft spots
   - Clean thoroughly with soap + water
   - Sand lightly (220 grit) for paint/adhesion

2. Mark centerline on hull:
   - Measure width at 3 points
   - Mark center with marker
   - This is your reference line

3. Cut deck plate holes (item #5):
   - Trace 300mm circle at marked positions
   - Cut with jigsaw (slow, steady)
   - File edges smooth

4. **SAFETY:** Wear safety glasses + dust mask when cutting

---

## Step 2: Build the PHI Bow Cone (2 hours)

1. Cut XPS foam blocks (item #9):
   - 2x blocks: 600mm × 300mm × 150mm
   - Stack and glue together

2. Carve the PHI profile:
   - Use template from 03_MECHANICAL.md
   - Profile follows golden ratio curve:
     ```
     y = A × x^(1/1.618)
     ```
   - Sand until smooth
   - Leading edge should be pointed (not blunt)

3. Fiberglass the foam cone:
   - Cut fiberglass cloth to wrap entire cone
   - Mix epoxy resin (item #4) per instructions
   - Wet foam with resin
   - Lay fiberglass cloth over wet foam
   - Work resin into cloth with brush
   - Let cure 4 hours (or use heat gun to speed up)

4. Apply carbon fiber patches (item #11):
   - Cut 2 patches: 200mm × 200mm
   - Apply to nose tip and base
   - Extra reinforcement at high-stress areas

5. Seal cone to kayak hull:
   - Position cone at front of kayak
   - Apply 3M 5200 sealant (item #50) generously
   - Clamp in place
   - Let cure overnight

---

## Step 3: Reinforce the Hull (1.5 hours)

1. Mix epoxy resin (item #4)

2. Apply fiberglass cloth (item #3) to hull bottom:
   - Wet hull surface with resin
   - Lay cloth starting from bow
   - Work toward stern
   - Overlap cloth edges by 50mm
   - Apply 2 layers

3. Reinforce high-stress areas:
   - Around motor mount location
   - Around deck plate holes
   - At bow cone connection

4. Let cure 4-6 hours

---

## Step 4: Install Jet Propulsion (1 hour)

1. Mount motor bracket (item #17):
   - Position at rear of hull
   - Drill 4 mounting holes
   - Bolt bracket with M8 hardware
   - Apply thread locker (item #53)

2. Install motor (item #13):
   - Bolt to bracket
   - Align shaft with jet duct

3. Attach impeller (item #14):
   - Thread onto motor shaft
   - Tighten with wrench (reverse thread!)

4. Connect jet duct (item #19):
   - Slide 150mm PVC pipe over impeller
   - Zip-tie to motor bracket
   - Leave 20mm clearance around impeller

5. Install intake grate (item #16):
   - Cut SS mesh to fit intake opening
   - Rivet to duct entrance
   - Prevents debris from entering impeller

6. Mount steering nozzle (item #18):
   - Attach to duct exit
   - Connect steering cable (item #38)
   - Should articulate 15° left and right

---

## Step 5: Mount the Battery (30 min)

1. Position battery box (item #21) inside hull:
   - Low and centered (best stability)
   - Secure to hull with brackets

2. Place LiFePO4 battery (item #20) in box:
   - Connect XT90 connector (item #23)
   - Red to +, Black to -

3. Install battery monitor (item #24):
   - Mount display where pilot can see it
   - Connect to battery

4. Mount fuse block (item #25):
   - Near battery positive terminal
   - Install 100A main fuse (item #26)

---

## Step 6: Wire the Electronics (1.5 hours)

1. **Follow the wiring diagram (02_WIRING.md)**

2. Connect in order:
   - Battery → Fuse block → Switch panel
   - Fuse block → ESC → Motor
   - Battery → Step-down → Nav lights, GPS, instruments
   - Battery → Step-down → Bilge pump

3. Solder ALL connections:
   - Twist wires
   - Solder (shiny joint)
   - Heat-shrink tubing

4. Install cable glands (item #35):
   - Drill holes where wires pass through hull
   - Feed wires through glands
   - Tighten until snug

5. Mount switch panel:
   - Drill holes for 4 toggle switches
   - Label each switch
   - Wire to components

6. **POWER TEST:**
   - SW1 OFF, SW2 OFF, SW3 OFF, SW4 OFF
   - Turn SW3 ON — GPS + depth finder should light up
   - Turn SW1 ON — motor should beep (ESC arming)
   - Turn SW4 ON — bilge pump should run

---

## Step 7: Steering System (30 min)

1. Mount steering wheel (item #37):
   - Position in cockpit where pilot reaches easily
   - Bolt to hull

2. Route steering cable (item #38):
   - Connect wheel to stern bracket
   - Cable should move freely (no kinks)
   - Test: turning wheel should move nozzle

3. Mount foot braces (item #40):
   - Adjustable, aluminum
   - Position so pilot can brace while standing

---

## Step 8: Navigation & Instruments (30 min)

1. Mount GPS (item #29):
   - Where pilot can see screen
   - Wire to 12V switched power

2. Mount depth finder (item #30):
   - Transducer mounted on hull bottom
   - Display in cockpit

3. Install navigation lights (item #31):
   - RED light on port (left) bow
   - GREEN light on starboard (right) bow
   - WHITE light on stern
   - Wire to SW2

4. Install kill switch (item #32):
   - Magnetic lanyard to pilot wrist
   - Kills motor when pulled

---

## Step 9: Safety Equipment (20 min)

1. Mount fire extinguisher (item #43):
   - Within arm's reach of pilot
   - Secure with bracket

2. Stow life jackets (item #41):
   - 2x Type III PFD
   - In cockpit, accessible

3. Attach anchor (item #46):
   - Store in bow compartment
   - Ensure rope is coiled, not tangled

4. Mount bilge pump (item #47):
   - Automatic mode (float switch)
   - Test: pour water in hull, pump should activate

5. Attach throwable flotation (item #42):
   - On stern, quick grab

---

## Step 10: Final Checks (30 min)

1. **WEIGHT BALANCE TEST:**
   - Place empty hull on scale
   - Target: 65 kg total (with battery)
   - If too heavy: remove non-essential items

2. **WATER TEST (in pool or calm water):**
   - Place in water, no pilot
   - Check for leaks (wait 10 min)
   - Check buoyancy (should float high)
   - Test motor on low throttle
   - Test steering (turns left/right)
   - Test bilge pump (pour water, pump activates)

3. **FINAL WALK-AROUND:**
   - All bolts tight
   - All wiring secured
   - No loose items in cockpit
   - Kill switch works
   - Battery charged
   - Navigation lights work
   - Anchor accessible

---

## Pre-Launch Checklist

**BEFORE EVERY LAUNCH:**

- [ ] Hull inspected for damage
- [ ] Battery charged (>80%)
- [ ] Kill switch tested (pull magnet, motor stops)
- [ ] Steering works (turns nozzle)
- [ ] Bilge pump tested
- [ ] GPS has satellite lock
- [ ] Depth finder reads correctly
- [ ] All navigation lights work
- [ ] Anchor rope coiled and ready
- [ ] Life jackets accessible
- [ ] Fire extinguisher charged
- [ ] Buddy system (never launch alone!)

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Motor won't start | Kill switch active | Re-attach magnet |
| No thrust | Impeller loose | Tighten impeller |
| Steering stuck | Cable kinked | Re-route cable |
| Water in hull | Leak at gland | Re-tighten gland + sealant |
| Bilge won't pump | Float switch stuck | Clean/replace float |
| GPS no signal | Antenna blocked | Move to open sky |
| Battery dies fast | Cold water | Pre-warm battery |
| Bow water over deck | Overloaded | Reduce weight |
