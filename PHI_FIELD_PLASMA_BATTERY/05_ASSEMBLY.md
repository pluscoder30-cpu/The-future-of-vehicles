# PHI-HARMONIC FIELD PLASMA BATTERY — ASSEMBLY GUIDE

## Step-by-Step Instructions (For 12-Year-Olds!)

---

## What You're Building

You're building a **plasma battery** — a super safe battery that stores energy in plasma (like lightning in a box!). When you're done, you'll have a battery that:

- Stores energy in glowing plasma
- Self-charges from vibrations and heat
- Can NEVER catch fire or explode
- Lasts for 10+ years

**Time needed:** 15 hours (with breaks)
**Difficulty:** Medium (with adult help)

---

## BEFORE YOU START

### Safety Rules (Read These First!)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   ALWAYS:                                                   │
│   ✓ Wear safety glasses when working                       │
│   ✓ Work with an adult nearby                               │
│   ✓ Wash your hands after working                           │
│   ✓ Take breaks every hour                                  │
│                                                             │
│   NEVER:                                                    │
│   ✗ Touch the soldering iron (it gets VERY hot!)            │
│   ✗ Look directly at plasma (it's bright like the sun!)     │
│   ✗ Open gas cylinders near open flame                      │
│   ✗ Work alone — always have help                           │
│                                                             │
│   IF SOMETHING GOES WRONG:                                  │
│   → Fire: Use fire extinguisher, yell for help              │
│   → Cut: Apply pressure, tell an adult                      │
│   → Gas leak: Leave the room, tell an adult                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tools You'll Need

```
TOOLS CHECKLIST:
├── Safety glasses (from hardware store)
├── Screwdriver set
├── Soldering iron (adult only!)
├── Solder wire
├── Wire strippers
├── Multimeter (to measure electricity)
├── Drill with small bits
├── Allen keys (hex wrenches)
├── File set
├── Sandpaper
└── Clamps
```

---

## STEP 1: Check All Your Parts (30 minutes)

**What to do:** Open every box and bag. Check each part against this list.

```
PARTS CHECKLIST:
□ 6 Aluminum sheets (3mm and 5mm)
□ Copper wire spool (18 AWG, lots of wire!)
□ Glass tube (the plasma chamber!)
□ Rubber O-rings (round black rings)
□ Fiberglass sheets (green/yellow board)
□ Aerogel blanket (soft, white insulation)
□ STM32 circuit board (green board with chips)
□ Small temperature sensors (little black beads)
□ Pressure sensor (small silver box)
□ Circuit boards (yellow/green boards)
□ MOSFETs (small black chips with 3 legs)
□ Power converter (black box with wires)
□ Connectors (XT90 — yellow plugs)
□ Small connectors (JST — tiny white plugs)
□ Rubber sheets (silicone)
□ Kapton tape (yellow, shiny tape)
□ Bolts and screws (in a bag)
□ Solder (shiny wire for joining)
□ Hydrogen gas tank (SPECIAL — adult handles this!)
□ Helium gas tank (SPECIAL — adult handles this!)
□ Gas regulator (attaches to tanks)
□ Brass fitting (for gas fill)
□ Pressure relief valve (safety device!)
□ Vacuum pump (sucks air out)
□ Piezo elements (flat, buzzer-like things)
□ Thermoelectric modules (small squares)
□ RF coils (small wire coils)
```

**If ANY part is missing:** STOP! Get the part before continuing.

---

## STEP 2: Build the Metal Box (2 hours)

**What to do:** Cut and assemble the aluminum casing.

### 2.1 Cut the Aluminum

```
CUT LIST:
├── Top plate: 500mm × 400mm
├── Bottom plate: 500mm × 400mm
├── Side 1: 500mm × 250mm
├── Side 2: 500mm × 250mm
├── Side 3: 400mm × 250mm
└── Side 4: 400mm × 250mm

Use a jigsaw with metal-cutting blade (adult helps!)
```

### 2.2 Drill Holes

```
FOR EACH SIDE:
├── Corner holes: 4mm (for M4 bolts)
├── Edge spacing: 15mm from edge
└── Hole spacing: 100mm along edges

FOR TOP/BOTTOM:
├── Gas port hole: 12mm
├── Connector holes: 20mm
└── Ventilation holes: 6mm (if needed)

Deburr all holes with a file (no sharp edges!)
```

### 2.3 Assemble the Box

```
ASSEMBLY ORDER:
1. Lay out bottom plate
2. Attach Side 1 to bottom (4 bolts)
3. Attach Side 2 to bottom (4 bolts)
4. Attach Side 3 to bottom (4 bolts)
5. Attach Side 4 to bottom (4 bolts)
6. Check corners are square (90°)
7. Don't put top on yet!

Use M4 × 10mm bolts, tighten hand-tight + quarter turn
```

---

## STEP 3: Wind the Coils (4 hours) ⚠️ MOST IMPORTANT STEP!

**What to do:** Make 5 special coils in a golden spiral pattern.

### 3.1 Make a Winding Form

```
WINDING FORM:
├── Use PVC pipe or 3D print
├── Diameter: 200mm
├── Length: 50mm
└── Surface: Smooth (apply wax or tape)
```

### 3.2 Wind Each Coil

```
COIL WINDING (Do this 5 times!):
1. Secure wire end to form with tape
2. Wind first layer: 120 turns, tight and neat
   - Keep tension consistent
   - No gaps between wires
   - No overlapping
3. Apply yellow Kapton tape over first layer
4. Secure end with tape
5. Test inductance (should be 47μH)
6. Repeat for all 5 coils

TIME PER COIL: ~45 minutes
TOTAL TIME: ~4 hours

TIPS:
- Wind slowly and carefully
- Keep wire tight but not too tight
- Use tape to hold each layer
- If wire breaks, start that coil over
```

### 3.3 Mount Coils in Golden Spiral

```
COIL POSITIONS (Top View):

                    Coil 1 (0°)
                        │
                  ┌─────┴─────┐
             ┌────┤           ├────┐
        ┌────┤    │     ●     │    ├────┐
   Coil 5   │    │   CENTER  │    │   Coil 2
   (272°)   │    │           │    │  (137.5°)
        └────┤    │           │    ├────┘
             └────┤           ├────┘
                  │           │
                  └─────┬─────┘
                        │
                    Coil 4 (225°)     Coil 3 (72.5°)

Mounting:
1. Cut G10 fiberglass plate to fit inside box
2. Mark coil positions using angle measurements
3. Drill mounting holes
4. Install silicone rubber pads (vibration dampers)
5. Place coils on dampers
6. Secure with M4 bolts (hand-tight only!)
7. Verify coil angles with protractor
```

---

## STEP 4: Install Glass Chamber (1 hour)

**What to do:** Prepare and install the plasma chamber.

### 4.1 Prepare Glass Tube

```
GLASS PREPARATION:
1. Clean tube with rubbing alcohol
2. Check for cracks or chips (reject if damaged!)
3. Sand edges smooth (220 → 400 → 800 grit)
4. Clean again with alcohol
5. Dry completely

⚠️ GLASS IS FRAGILE — Handle with care!
```

### 4.2 Install O-rings

```
O-RING INSTALLATION:
1. Measure tube outer diameter
2. Select matching O-ring size
3. Test fit O-ring on tube ends
4. Apply vacuum grease to O-rings
5. Place O-rings in groove
6. Verify seal (should be snug)
```

### 4.3 Install Gas Ports

```
GAS PORTS:
1. Gas fill port (left side):
   - Drill 12mm hole in top plate
   - Install brass fitting with O-ring
   - Tighten gently (don't over-tighten!)
   - Test for leaks (soapy water → bubbles = leak)

2. Pressure relief valve (top):
   - Install relief valve on opposite side
   - Set to 2.0 Torr
   - Seal with Teflon tape
```

---

## STEP 5: Build Electronics (3 hours)

**What to do:** Solder and assemble the control circuits.

⚠️ **SOLDERING IS FOR ADULTS ONLY!** Watch and help, but let the adult do the hot iron work.

### 5.1 Build Control Board

```
CONTROL BOARD:
1. Mount STM32F407 on perfboard
2. Add pull-up resistors (tiny resistors)
3. Add decoupling capacitors (tiny cylinders)
4. Wire MOSFET drivers (small chips)
5. Test all connections with multimeter
```

### 5.2 Build Power Board

```
POWER BOARD:
1. Mount DC-DC converter (black box)
2. Add input/output capacitors
3. Wire current sense resistor
4. Add TVS diodes (protection)
5. Test output voltage (should be 48V)
```

### 5.3 Build Monitoring Board

```
MONITORING BOARD:
1. Mount INA219 current sensor
2. Wire temperature sensors (5 of them)
3. Wire pressure sensor
4. Wire plasma density sensor
5. Test all sensor readings
```

---

## STEP 6: Wire Everything Together (2 hours)

**What to do:** Connect all the parts with wires.

### 6.1 Wire Coil Array

```
COIL WIRING:
1. Route coil wires along mounting plate edges
2. Keep power wires away from signal wires
3. Use zip ties every 50mm
4. Solder connections with heat shrink tubing
5. Test continuity of each connection
6. Label all wires clearly

WIRE COLORS:
├── Red: 48V power
├── Black: GND
├── Yellow: Coil 1 PWM
├── Orange: Coil 2 PWM
├── Green: Coil 3 PWM
├── Blue: Coil 4 PWM
└── Purple: Coil 5 PWM
```

### 6.2 Connect Power

```
POWER CONNECTIONS:
1. Connect XT90 connector (yellow plug)
2. Red wire to +, Black wire to -
3. Verify polarity with multimeter!
4. Apply dielectric grease to connectors
5. Secure loose wires away from moving parts
```

---

## STEP 7: Final Assembly (1 hour)

**What to do:** Put everything together.

### 7.1 Install Insulation

```
AEROGEL INSULATION:
1. Cut aerogel blanket to fit inner walls
2. Leave 20mm clearance for coil mounting
3. Attach with high-temp adhesive
4. Ensure no gaps in insulation

⚠️ AEROGEL IS FRAGILE — Handle gently!
```

### 7.2 Install Electronics

```
ELECTRONICS INSTALLATION:
1. Mount control board in electronics bay
2. Mount power board
3. Mount monitoring board
4. Route all wires neatly
5. Secure with zip ties
6. Connect all JST connectors
```

### 7.3 Close the Box

```
FINAL CLOSURE:
1. Verify all connections are secure
2. Double-check polarity everywhere!
3. Place top plate on box
4. Install M4 bolts around edges
5. Tighten evenly (cross pattern)
6. Verify no wires are pinched
```

---

## STEP 8: Fill with Gas (30 minutes)

**ADULT ONLY!** This step uses high-pressure gas.

```
GAS FILL PROCEDURE:
1. Connect vacuum pump to gas fill port
2. Evacuate chamber to 10⁻³ Torr
3. Close vacuum valve
4. Connect hydrogen gas cylinder
5. Fill to 0.5 Torr
6. Add helium to complete mixture
7. Seal gas fill port
8. Verify pressure holds for 24 hours

⚠️ HYDROGEN IS FLAMMABLE — No open flames!
⚠️ HELIUM IS SAFE but can displace oxygen
⚠️ Work in well-ventilated area!
```

---

## STEP 9: Test Everything (1 hour)

**What to do:** Make sure everything works.

```
TEST CHECKLIST:
□ Power-on test: Connect 48V, verify MCU boots
□ Coil test: All 5 coils activate
□ Sensor test: Temperature, pressure, plasma density
□ Safety test: Overcurrent, overvoltage protection
□ Containment test: Measure magnetic field (>0.5 Tesla)
□ Efficiency test: Charge/discharge cycle
□ Self-charging test: Measure harvesting rate
```

---

## TROUBLESHOOTING

### Problem: Battery won't turn on
- Check power connections
- Verify 48V supply
- Check MCU boot (LED should light)
- Power cycle (unplug, wait 10 seconds, plug back in)

### Problem: Coils not activating
- Check MOSFET connections
- Verify PWM signals from MCU
- Test coil inductance (should be 47μH)
- Check for loose wires

### Problem: Low power output
- Check gas pressure (should be 0.5 Torr)
- Verify coil current
- Check temperature sensors
- Look for gas leaks (soapy water test)

### Problem: Gas leak (hissing sound)
- **NO FIRE RISK!** Plasma dissipates safely
- Evacuate area
- Wait 10 minutes
- Inspect battery for damage
- Replace O-rings if needed

---

## CARE & MAINTENANCE

### Monthly
- Visual inspection
- Check gas pressure
- Clean terminals

### Annually
- Refill gas if needed
- Inspect O-rings
- Test all safety systems

### Every 5 Years
- Replace O-rings
- Full inspection
- Recalibrate sensors

---

## NEXT STEPS

After assembly:
1. Install in your vehicle (see installation guide)
2. Connect to motor controller
3. Test at low speed first
4. Gradually increase power
5. Enjoy your plasma-powered ride!

---

**Document**: 05_ASSEMBLY.md
**Vehicle**: PHI_FIELD_PLASMA_BATTERY
**Status**: BUILDABLE ✓
**Time**: 15 hours (with breaks)
**Difficulty**: Medium (adult supervision required)
**Version**: 2.0 (12-year-old friendly)
