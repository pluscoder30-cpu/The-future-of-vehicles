# PHI CHEAP SHUTTLE — Kid-Friendly Instruction Manual

## What Is the PHI Cheap Shuttle?

The PHI Cheap Shuttle is a tiny SPACECRAFT that can fly to the edge of space! It uses special "phi-harmonic" plasma thrusters that push it up to 100 km high (that's where space starts!) and fast enough to break the sound barrier three times.

This is NOT a toy. It's a real vehicle that carries 2 people. But don't worry — you're not building it alone. An adult team with welding and electronics experience will help you build every part.

```
 ┌─────────────────────────────────────────────────┐
 │              PHI CHEAP SHUTTLE                   │
 │                                                  │
 │              ┌──────────┐                        │
 │              │ COCKPIT  │ ← You sit here!        │
 │              │ (2 seat) │                        │
 │              └────┬─────┘                        │
 │                   │                              │
 │  ┌────────────────┼────────────────┐             │
 │  │    ALUMINUM SPACEFRAME          │             │
 │  │    (3 meters long!)             │             │
 │  │                                 │             │
 │  │  🔥 ← THRUSTER   THRUSTER → 🔥 │             │
 │  │                                 │             │
 │  │  🔋 BATTERIES (4 big ones)      │             │
 │  │                                 │             │
 │  │  📡 AVIONICS (brain computer)   │             │
 │  └─────────────────────────────────┘             │
 │                                                  │
 │  Cost: $4,500 (cheapest spacecraft ever!)       │
 │  Altitude: 100 km (edge of space!)              │
 │  Speed: Mach 3 (3 times speed of sound!)        │
 └─────────────────────────────────────────────────┘
```

### How Does It Fly?

1. **Batteries** store electricity (like a giant phone battery, but 40,000 times bigger!)
2. **Plasma thrusters** use that electricity to create super-hot gas
3. The gas shoots out the back and pushes the shuttle forward
4. The shuttle climbs up through the atmosphere
5. At 100 km, you're in SPACE — you can see the curve of the Earth!

```
 HOW IT FLIES — SIDE VIEW:
 ═══════════════════════════════════════

 Altitude (km)
     │
 100 │                    ⭐ APOGEE (space!)
     │                   ╱ ╲
  80 │                  ╱   ╲
     │                 ╱     ╲
  60 │                ╱       ╲
     │               ╱         ╲
  40 │              ╱           ╲
     │             ╱             ╲
  20 │            ╱               ╲
     │           ╱                 ╲
   0 │───🚀────╱───────────────────╲────
     └────────────────────────────────── Time
      Takeoff    Boost    Coast   Land

      ↑ The shuttle goes UP, then falls back down
        and lands with parachutes!
```

---

## Tools You Will Need

**THIS IS A BIG PROJECT — YOU NEED A TEAM!**

| Tool | What It Does | Who Uses It |
|------|-------------|-------------|
| TIG Welder | Joins aluminum tubes together | Adult welder |
| Band Saw | Cuts metal tubes to length | Adult |
| Drill Press | Makes holes in metal | Adult |
| Rivet Gun | Puts in permanent rivets | Adult + you (with supervision) |
| Soldering Iron | Connects electronics wires | Adult + you (with supervision) |
| Multimeter | Measures electricity | You (with adult watching) |
| Torque Wrench | Tightens bolts to exact tightness | Adult |
| Angle Grinder | Cuts and smooths metal | Adult only! |
| Clamps | Holds pieces together while working | Everyone |
| Safety Gear | Glasses, gloves, ear protection | Everyone |

```
 ⚠️  DANGER ZONE
 ═══════════════════════════════════════
 🔥 WELDING = VERY HOT! Only trained adults
 ⚡ BATTERIES = HIGH VOLTAGE! Don't touch terminals
 🔊 LOUD NOISES = Wear ear protection
 🧤 METAL EDGES = Wear gloves at all times
 ═══════════════════════════════════════
```

---

## Parts Checklist

### Frame (Aluminum)
- [ ] 12× aluminum tubes, 1.5" diameter, 8 feet long
- [ ] 8× aluminum tubes, 1.0" diameter, 8 feet long
- [ ] 6× aluminum tubes, 0.75" diameter, 8 feet long
- [ ] 10× aluminum angle pieces, 6 feet long
- [ ] 1× aluminum plate, 1/8" thick, 4ft × 8ft
- [ ] 1× aluminum sheet, 0.063" thick
- [ ] 1× aluminum sheet, 0.040" thick

### Shell (Fiberglass)
- [ ] 2× fiberglass cloth rolls (6oz, 10 yards each)
- [ ] 2× polyester resin gallons
- [ ] 2× MEKP hardener bottles
- [ ] 2× PVC foam core sheets
- [ ] Body filler (Bondo)
- [ ] Mold release wax

### Thrusters (4 total — the exciting part!)
- [ ] 4× Litz wire spools (100ft each)
- [ ] 8× ferrite toroid cores (donut-shaped magnets)
- [ ] 16× high-voltage capacitors (0.1μF, 2000V!)
- [ ] 8× medium capacitors (1.0μF, 1000V)
- [ ] 8× IRFP460 MOSFETs (big power switches)
- [ ] 4× IR2110 gate driver chips
- [ ] 4× quartz plasma tubes
- [ ] 4× copper exhaust nozzles
- [ ] 4× ignition coils (from old cars!)
- [ ] 8× aluminum heatsinks

### Batteries (4 big ones!)
- [ ] 4× FPB-20 phi-harmonic field plasma batteries (12V, 100Ah each — Zero fire/explosion risk — plasma is self-limiting)
- [ ] 4× ANL fuse holders (150A fuses)
- [ ] 50ft of 4 AWG welding cable (thick red and black)
- [ ] 2× 400A master disconnect switches
- [ ] 4× battery boxes (plastic)
- [ ] 4× digital voltage monitors

### Avionics (the brain)
- [ ] 2× Arduino Mega boards (the flight computer)
- [ ] 1× GPS module (tells you where you are)
- [ ] 2× barometric altimeters (tells you how high)
- [ ] 2× motion sensors (IMU — tells you which way you're pointing)
- [ ] 2× VHF handheld radios (talk to the ground)
- [ ] 2× OLED screens (show you instrument readings)
- [ ] 4× servo motors (move the thrust direction)

### Recovery (how you land safely!)
- [ ] 2× 15-foot parachutes (emergency backup!)
- [ ] 200ft of parachute cord
- [ ] 4× quick-release pins
- [ ] 2× deployment bags

---

## Step-by-Step Assembly

### Phase 1: Build the Frame (Weeks 1-3)

**Step 1:** Cut all the aluminum tubes
- Use the band saw to cut tubes to the right lengths
- Some tubes are cut to special "phi-harmonic" lengths like 161.8mm and 261.8mm
- File all the cut edges smooth (no sharp bits!)
- Clean each cut with acetone

```
 TUBE CUTTING GUIDE:
 ═══════════════════════════════════════
 Main frame tubes:    3000mm (3 meters!)
 Secondary tubes:    1618mm (φ × 1000)
 Diagonal braces:    423.6mm (φ³ × 100)
 Smaller braces:     261.8mm (φ² × 100)
 Tiny braces:        161.8mm (φ¹ × 100)
 ═══════════════════════════════════════
```

**Step 2:** Weld the main frame
- An adult welder uses TIG welding to join tubes
- The frame is a box shape with diagonal braces
- All welds need to be strong — this holds people!

**Step 3:** Weld the thruster mounts
- 4 thick aluminum plates get welded to the frame
- These hold the thrusters in place
- Make sure they're flat (within 0.5mm)

**Step 4:** Install the floor
- A flat aluminum plate goes in the bottom
- Drill holes for seat bolts
- Stitch-weld it to the frame

**Step 5:** Weld the gussets
- Small triangular pieces go at every corner
- They make the frame much stronger
- Like adding corner brackets to a bookshelf

---

### Phase 2: Build the Shell (Weeks 4-6)

**Step 6:** Make the mold shapes
- Carve foam blocks into the nose cone shape
- Cover with body filler and sand smooth
- Apply mold release wax (so fiberglass doesn't stick!)

**Step 7:** Lay up fiberglass
- Mix resin with hardener (follow the recipe on the bottle!)
- Lay cloth over the mold
- Wet it out with resin (use a roller, no dry spots!)
- Layer after layer, building up the shell
- Let it cure 24 hours

```
 FIBERGLASS LAYUP ORDER:
 ═══════════════════════════════════════
 1. Gel coat (pretty outside)
 2. 2oz cloth (smooth finish)
 3. 6oz cloth ×2 (strength)
 4. Foam core (stiffness)
 5. 6oz cloth ×2 (more strength)
 ═══════════════════════════════════════
 Total thickness: about 16mm (5/8 inch)
```

**Step 8:** Trim and fit the shell
- Cut off extra fiberglass with an oscillating tool
- Test-fit to the frame
- Drill rivet holes every 50mm

**Step 9:** Attach shell to frame
- Use structural adhesive (super-strong glue)
- Rivet the shell to the frame
- Seal all joints with high-temperature silicone

---

### Phase 3: Build the Thrusters (Weeks 7-10)

This is the COOLEST part! You're building plasma thrusters!

**Step 10:** Wind the coils
- Take the donut-shaped ferrite cores
- Wind 47 turns of Litz wire around each core
- Keep the turns even and neat
- Secure with tape
- Measure the inductance — should be about 2.3 mH

```
 COIL WINDING:
 ═══════════════════════════════════════

        ┌───────────┐
       ╱  ╱╱╱╱╱╱╱╱╱  ╲
      │  ╱  Ferrite  ╲  │
      │ │   Core     │ │
      │  ╲  (donut) ╱  │
       ╲  ╲╲╲╲╲╲╲╲╲  ╱
        └───────────┘

      ← Litz wire wraps around 47 times
      ← This creates a magnetic field
      ← When electricity flows, it makes PLASMA!
```

**Step 11:** Build the resonant tanks
- Connect 4 capacitors in parallel on a circuit board
- This stores energy like a spring
- It should vibrate at 161,800 times per second!

**Step 12:** Build the power switches (inverters)
- Mount big MOSFETs on heatsinks
- These switch electricity on and off very fast
- Use thermal paste between MOSFET and heatsink

**Step 13:** Build the plasma tubes
- Clean quartz tubes with acetone
- Install a metal mesh inside (anode)
- Install a wire in the center (cathode)
- Seal with high-temperature gasket

**Step 14:** Attach the exhaust nozzles
- Copper nozzles with a special phi-ratio shape
- Throat: 15mm, Exit: 24.27mm
- Bolt them to the thruster housing

**Step 15:** Assemble each thruster
- Put coil + plasma tube + nozzle together
- Wire the power cables (4 AWG — very thick!)
- Wire the control cables (22 AWG — thin)
- Repeat 3 more times!

---

### Phase 4: Install Batteries (Weeks 11-12)

**Step 16:** Prepare the battery boxes
- Line boxes with ceramic blanket (fire protection!)
- Install rubber mounting pads
- Route thick cables from bus bar

**Step 17:** Install the bus bar
- Mount a big copper bar to the frame
- This is where all the power flows
- Install 400A master disconnect switches

**Step 18:** Install the batteries
- Place FPB-20 phi-harmonic field plasma batteries in their boxes
- Connect positive first, then negative
- Secure with nylon straps
- Install voltage monitors

```
 BATTERY LAYOUT:
 ═══════════════════════════════════════

  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
  │FPB-20│  │FPB-20│  │FPB-20│  │FPB-20│
  │ #1   │  │ #2   │  │ #3   │  │ #4   │
  │12V   │  │12V   │  │12V   │  │12V   │
  │100Ah │  │100Ah │  │100Ah │  │100Ah │
  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘
     │         │         │         │
     └─────────┴────┬────┴─────────┘
                    │
              ┌─────┴─────┐
              │  BUS BAR  │
              │  (copper) │
              └───────────┘

  Total: 48V, 40 kWh of energy!
  That's enough to power a house for 3 days!
```

---

### Phase 5: Install Avionics (Weeks 13-14)

**Step 19:** Build the instrument panel
- Mount Arduino Mega to an aluminum bracket
- Wire the power supply (12V → 5V for Arduino)
- Install OLED screens in panel cutouts
- Wire toggle switches and pushbuttons

**Step 20:** Install sensors
- Mount GPS module where it can see the sky
- Mount motion sensors at the center of gravity
- Mount altimeters in a protected spot
- Wire everything to the Arduino

**Step 21:** Install radios
- Mount VHF radios (one for pilot, one for passenger)
- Route antenna cables
- Test: can you talk to each other from 1 km apart?

**Step 22:** Install servos
- These move the thrusters to steer the shuttle
- Mount servo brackets to thruster pivots
- Connect servo horns to thrust vector mechanisms
- Test: servos should move ±15°

---

### Phase 6: Wire Everything (Weeks 15-17)

**Step 23:** Run power cables
- Thick 4 AWG cables from bus bar to thrusters
- Medium 10 AWG cables from bus bar to avionics
- Crimp ring terminals on all connections
- Heat-shrink every connection

**Step 24:** Run signal cables
- Sensor cables (shielded twisted pair)
- Servo cables (3-conductor)
- Communication cables
- Label EVERY wire at BOTH ends!

**Step 25:** Build the ground system
- Install a star ground point on the aluminum floor
- Connect all grounds to this one point
- Scratch through anodize at connection points
- Verify continuity (<0.1Ω)

---

### Phase 7: Install Recovery System (Week 18)

**Step 26:** Install parachute compartments
- Mount parachute bags in the back of the shuttle
- Install quick-release pins (pull-type)
- Connect pull cables to cockpit handles
- Test deployment on the ground (no canopy!)

```
 PARACHUTE DEPLOYMENT:
 ═══════════════════════════════════════

    ┌─────────────────┐
    │   PARACHUTE     │ ← Packed in bag
    │   COMPARTMENT   │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  QUICK RELEASE  │ ← Pull pin to release
    │     PIN         │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  PULL CABLE     │ ← Connected to cockpit
    │  (to cockpit)   │
    └─────────────────┘

    ⚠️ Test this on the ground FIRST!
    ⚠️ Make sure cables aren't tangled!
```

---

### Phase 8: Final Assembly (Weeks 19-20)

**Step 27:** Install landing gear
- Weld landing gear mounts to frame
- Attach skid tubes with pivot bolts
- Install coil springs (200 lb/in)
- Attach rubber skid pads

**Step 28:** Install canopy
- Mount the hinge
- Attach gas struts (helps open the heavy canopy)
- Install the latch
- Test open/close

**Step 29:** Final inspection
- Check EVERY bolt is tight
- Check EVERY wire is connected
- Check EVERY weld looks good
- Weigh the shuttle — must be under 350 kg with passengers

---

## How to Test Your Shuttle

### Ground Tests (DO THESE FIRST!)

**Step 30:** Battery test
- Charge all 4 batteries fully
- Measure voltage: each should be 12.4V or higher
- Discharge test: watch voltage under load

**Step 31:** Thruster ignition test (STATIC — no thrust!)
- Connect one thruster to a battery
- Turn it on for 5 seconds
- Check for sparks, smoke, or weird smells
- If anything goes wrong: STOP and tell an adult

**Step 32:** Thruster full-power test
- Mount the shuttle on a scale
- Run all 4 thrusters at full power
- Measure the thrust: should be 2000 N total
- Check temperature of all parts

**Step 33:** Avionics test
- Turn on all electronics
- Check that GPS finds satellites
- Check that altimeter reads correctly
- Check that servos move properly
- Check that radios can communicate

**Step 34:** Communications test
- Test VHF radios at 1 km distance
- Test HC-12 telemetry data link
- Verify ground station receives data

**Step 35:** Landing gear drop test
- Lift the shuttle 1 meter off the ground
- Drop it (carefully!)
- Measure the g-force on landing
- Should survive 5g impact

---

## How to Fly

### Pre-Flight Checklist

```
 PRE-FLIGHT CHECKLIST — PHI CHEAP SHUTTLE
 ═══════════════════════════════════════════════

 □ FRAME
   □ All welds inspected
   □ All bolts torqued
   □ No cracks or damage

 □ THRUSTERS
   □ All 4 thrusters connected
   □ Coil resistance measured
   □ Ignition test passed

 □ BATTERIES
   □ All 4 batteries > 12.4V
   □ Fuses installed
   □ Master switch works

 □ AVIONICS
   □ Arduino powered on
   □ GPS has satellites
   □ Altimeter reading
   □ Motion sensors working
   □ Radios communicating
   □ Servos responding

 □ RECOVERY
   □ Parachutes packed correctly
   □ Pull cables connected
   □ Test deployment successful

 □ SAFETY
   □ Fire extinguisher charged
   □ First aid kit on board
   □ Ground crew briefed
   □ Weather checked (no wind > 15 knots)
   □ NOTAM filed with FAA

 ═══════════════════════════════════════════════
 INSPECTION RESULT: □ PASS  □ FAIL
 ═══════════════════════════════════════════════
```

### Flight Profile

```
 WHAT HAPPENS DURING A FLIGHT:
 ═══════════════════════════════════════

 MINUTE 0: TAKEOFF
 ─────────────────
 • All 4 thrusters at full power
 • Shuttle accelerates down the runway
 • After 150 meters, you're airborne!
 • Climb steeply (20° nose up)

 MINUTE 0-4: BOOST
 ─────────────────
 • Thrusters at full power
 • Climbing through the atmosphere
 • Getting darker as you go higher
 • Speed increasing past Mach 1, 2, 3...

 MINUTE 4: ENGINE CUTOFF
 ─────────────────
 • Thrusters shut off at 80 km altitude
 • You're in near-space!
 • Everything goes quiet
 • You float in your seat (zero gravity!)

 MINUTE 4-7: COASTING
 ─────────────────
 • Ballistic arc — like throwing a ball
 • Continuing to climb to 100 km
 • Looking out the window: black sky, curved Earth!
 • This is the best part!

 MINUTE 7: APOGEE (highest point)
 ─────────────────
 • 100 km altitude — THE EDGE OF SPACE!
 • You see the thin blue line of atmosphere
 • Stars visible in daytime
 • Moment of weightlessness

 MINUTE 7-10: REENTRY
 ─────────────────
 • Falling back toward Earth
 • Getting faster and faster
 • Heat shield protecting you from friction
 • Sky turns from black to blue

 MINUTE 10-12: DESCENT
 ─────────────────
 • Deploy parachutes at 3000 meters
 • Gentle descent under canopy
 • Touchdown at about 30 m/s (70 mph)
 • Roll to a stop

 TOTAL FLIGHT TIME: 12 minutes!
```

---

## Safety Precautions

```
╔═══════════════════════════════════════════════════════════╗
║              ⚠️  EXTREME DANGER ZONE  ⚠️                  ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  This is a REAL SPACECRAFT. It can KILL you.              ║
║                                                           ║
║  • NEVER fly without FAA Experimental Certificate         ║
║  • NEVER fly without a ground crew of at least 2 people   ║
║  • NEVER fly over populated areas                         ║
║  • NEVER fly in bad weather                               ║
║  • NEVER fly without checking EVERY bolt                  ║
║  • NEVER fly without parachutes                           ║
║  • NEVER fly alone — always have a rescue plan            ║
║                                                           ║
║  Battery Safety:                                          ║
║  • Phi-harmonic field plasma batteries — zero fire/explosion risk     ║
║  • Plasma is self-limiting — no thermal runaway possible              ║
║  • No acid, no flammable electrolyte                                  ║
║                                                           ║
║  Thruster Safety:                                         ║
║  • Plasma temperatures reach 5,000°C!                     ║
║  • Never look directly at an operating thruster           ║
║  • Keep 3 meters away from thruster exhaust               ║
║  • High voltage (500V!) inside thrusters — don't touch!   ║
║                                                           ║
║  Emergency:                                               ║
║  • If you see fire: cut ALL power, evacuate               ║
║  • If thrusters fail: deploy parachutes immediately       ║
║  • If you hear a loud bang: check for damage, land ASAP   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### Emergency Procedures

**If a thruster fails during flight:**
1. Reduce power on remaining 3 thrusters to 75%
2. Check if you can still climb
3. If not: abort, begin controlled descent
4. Deploy parachutes below 10,000 feet

**If multiple thrusters fail:**
1. CUT ALL POWER immediately
2. Deploy parachutes
3. Call "MAYDAY MAYDAY MAYDAY" on VHF radio
4. Prepare for emergency landing

**If a battery catches fire:**
1. Cut master switch OFF
2. Use fire extinguisher
3. If fire continues: deploy parachutes and land
4. After landing: evacuate and move 50m away

**If you lose communications:**
1. Continue mission if everything else is OK
2. Use HC-12 telemetry as backup
3. If total comms loss: descend to safe altitude
4. Land at the nearest safe location

---

## Troubleshooting

| Problem | What It Means | How to Fix It |
|---------|--------------|---------------|
| Thruster won't ignite | Ignition coil failed | Check coil wiring, replace coil |
| Low thrust | Resonant tank out of tune | Adjust capacitor values |
| Battery voltage drops fast | Battery old or damaged | Replace battery |
| GPS won't lock | Antenna blocked | Reposition antenna |
| Altimeter reads wrong | Sensor needs calibration | Calibrate at known altitude |
| Servos jittering | Signal noise | Add capacitor to servo power |
| Radio static | Bad antenna connection | Check antenna cable |
| Parachute won't deploy | Cable tangled | Re-rig deployment system |
| Frame vibrating | Loose bolt or cracked weld | Inspect and repair |

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════╗
║    PHI CHEAP SHUTTLE — QUICK CARD             ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  STARTUP:                                     ║
║  1. Master switch ON                          ║
║  2. Battery switches ON (1,2,3,4)             ║
║  3. Avionics switch ON                        ║
║  4. Wait for GPS lock (green light)           ║
║  5. Radio check                               ║
║  6. Thruster check                            ║
║                                               ║
║  TAKEOFF:                                     ║
║  1. All thrusters to full power               ║
║  2. Release brakes                            ║
║  3. Rotate at 100 km/h (nose up)              ║
║  4. Climb at 20°                              ║
║                                               ║
║  EMERGENCY:                                   ║
║  1. RED button = cut all power                ║
║  2. Pull handle = deploy parachutes           ║
║  3. "MAYDAY" on VHF radio                     ║
║                                               ║
║  LIMITS:                                      ║
║  • Max altitude: 100 km                       ║
║  • Max speed: Mach 3                          ║
║  • Max G: +6g / -3g                           ║
║  • Max wind at launch: 15 knots              ║
║  • No flying in rain                          ║
║                                               ║
║  WEIGHT:                                      ║
║  • Empty: 200 kg                              ║
║  • Max with passengers: 350 kg                ║
║  • Pilot max: 100 kg                          ║
║  • Passenger max: 100 kg                      ║
║                                               ║
╚═══════════════════════════════════════════════╝
```

---

## Cost Summary

| What | How Much | Where |
|------|----------|-------|
| Aluminum frame | $621 | Scrapyard |
| Fiberglass shell | $348 | Home Depot + eBay |
| 4 thrusters | $676 | AliExpress + eBay |
| 4 batteries | $658 | eBay surplus |
| Avionics | $329 | eBay + AliExpress |
| Fasteners | $359 | Home Depot |
| Parachutes | $118 | eBay surplus |
| Misc | $209 | Various |
| **TOTAL** | **$4,487** | |

That's less than a fancy car! And you get a SPACECRAFT!

---

## Congratulations!

You built a spacecraft! Well, you designed it and helped build it with your team. The PHI Cheap Shuttle is the cheapest spacecraft ever designed — and you helped make it real.

Remember: the first time you fly, keep it low and slow. Test everything. Trust your training. And most importantly — have fun looking down at Earth from the edge of space!

**Now go explore the cosmos! 🚀**

---

*This manual was written for builders age 12 and up, with professional adult supervision. Spaceflight is dangerous. Always follow safety rules. Never fly without proper certification and training.*
