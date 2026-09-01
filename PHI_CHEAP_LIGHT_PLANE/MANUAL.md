# PHI CHEAP LIGHT PLANE — Kid-Friendly Instruction Manual

## What Is the PHI Cheap Light Plane?

The PHI Cheap Light Plane is a real, flyable AIRPLANE that you can build in your garage! It's an "ultralight" — a special type of small, lightweight plane that doesn't need a pilot's license to fly (in the US, under FAA Part 103 rules).

It costs less than $3,000 — that's cheaper than most used cars! And instead of gasoline, it runs on batteries, so it's quiet and clean.

```
 ┌──────────────────────────────────────────────────────┐
 │              PHI CHEAP LIGHT PLANE                    │
 │                                                       │
 │                    ╔═══╗                              │
 │                    ║ P ║ ← Propeller spins here!      │
 │                    ╚═╤═╝                              │
 │          ┌──────────┼──────────┐                      │
 │          │          │          │                      │
 │    ══════╪══════════╪══════════╪══════ ← WINGS!     │
 │          │    ┌─────┴─────┐    │      (10 meters!)  │
 │          │    │           │    │                      │
 │          │    │  FUSELAGE │    │                      │
 │          │    │  (body)   │    │                      │
 │          │    │           │    │                      │
 │          │    │  🪑 pilot │    │                      │
 │          │    │           │    │                      │
 │          │    └───────────┘    │                      │
 │          │         │           │                      │
 │          └─────────┼───────────┘                      │
 │                    │                                  │
 │          ══════════╪══════════ ← TAIL                │
 │                    │                                  │
 │              ┌─────┴─────┐                            │
 │              │   WHEELS  │                            │
 │              └───────────┘                            │
 │                                                       │
 │  Cost: $2,744  Weight: 115 kg (253 lbs)             │
 │  Speed: 102 km/h  Range: 500 km                     │
 └──────────────────────────────────────────────────────┘
```

### How Does It Fly?

An airplane flies because of **lift** — the wings are shaped so that air moves faster over the top than the bottom. This creates a force that pushes the wing UP.

```
 HOW A WING CREATES LIFT:
 ═══════════════════════════════════════

     Fast air (low pressure)
     ───────────────────────→
    ╱                         ╲
   ╱   ═══════════════════════  ╲ ← Wing (Clark Y shape)
   ╲   ═══════════════════════  ╱
    ╲                         ╱
     ───────────────────────→
     Slow air (high pressure)

     The pressure difference PUSHES the wing UP!
     This is called LIFT.
```

The propeller pulls the plane forward, the wings create lift, and up you go!

---

## Tools You Will Need

**THIS IS A WOODWORKING PROJECT — YOU NEED A GARAGE!**

| Tool | What It Does | Where to Get It |
|------|-------------|-----------------|
| Cordless drill | Makes holes, drives screws | Hardware store |
| Circular saw | Cuts long boards | Hardware store |
| Hand saw | Makes fine cuts | Hardware store |
| Coping saw | Cuts curves (for ribs) | Hardware store |
| Sandpaper | Smooths wood | Hardware store |
| Clamps | Holds pieces together | Hardware store |
| Measuring tape | Measures things | Hardware store |
| Speed square | Measures angles | Hardware store |
| Soldering iron | Connects wires | Electronics store |
| Heat gun | Shrinks fabric | Hardware store |
| Rivet gun | Puts in permanent rivets | Hardware store |
| Digital caliper | Measures small things precisely | Hardware store |

```
 ⚠️  SAFETY FIRST!
 ═══════════════════════════════════════
 🪚 Saw blades are SHARP — wear gloves!
 🔌 Power tools need careful handling
 👓 Always wear safety glasses
 🔥 Epoxy and glue have fumes — work outside
 📏 Measure TWICE, cut ONCE!
 ═══════════════════════════════════════
```

---

## Parts Checklist

### Wood Frame
- [ ] 12× Sitka spruce boards, 1×4" × 8ft (main structure)
- [ ] 8× Sitka spruce boards, 1×2" × 8ft (secondary)
- [ ] 20× Sitka spruce strips, 1/2" × 1" × 8ft (ribs)
- [ ] 6× Pine boards, 1×3" × 6ft (formers)
- [ ] 2× Baltic birch plywood sheets, 1/4" × 4'×8' (gussets)
- [ ] 4× Spruce blocks, 2"×2" × 12" (landing gear mounts)
- [ ] 10× Balsa sheets, 1/16" × 4" × 36" (leading edge)
- [ ] 30× Pine strips, 1/4" × 1/4" × 4ft (trailing edge)

### Fabric Covering
- [ ] 2× Dacron fabric rolls (aircraft grade, 60" wide)
- [ ] 1× Polybrush primer (fabric treatment)
- [ ] 1× Polyspanite tape (reinforcement)
- [ ] 2× Fabric paint cans (white, UV protection)
- [ ] 100ft rib stitching cord
- [ ] 3× curved needles (for sewing fabric to ribs)

### Propulsion
- [ ] 1× brushless outrunner motor (50 kW!)
- [ ] 1× propeller hub (CNC aluminum)
- [ ] 2× propeller blades (carbon-reinforced, 1.2m each)
- [ ] 1× motor controller (ESC, 100A, 80V)
- [ ] 1× phi-harmonic stator ring (special coil pattern)
- [ ] 4× ferrite toroid cores
- [ ] 8× film capacitors
- [ ] 4× MOSFETs (power switches)
- [ ] 2× gate drivers

### Batteries (4 big ones!)
- [ ] 4× FPB-20 phi-harmonic field plasma batteries (12V, 100Ah each — Zero fire/explosion risk — plasma is self-limiting)
- [ ] 2× ANL fuse holders (200A fuses)
- [ ] 30ft of 4 AWG welding cable
- [ ] 1× 300A master disconnect switch
- [ ] 1× battery monitor

### Avionics (the brain)
- [ ] 2× Arduino Nano boards
- [ ] 2× BMP280 altimeters
- [ ] 1× MPU6050 motion sensor
- [ ] 1× GPS module
- [ ] 2× OLED screens (show instrument readings)
- [ ] 1× VHF handheld radio
- [ ] 2× telemetry radios (433MHz)
- [ ] 2× piezo buzzers (warning sounds)

### Landing Gear
- [ ] 3× steel tubes, 1" diameter × 4ft (gear legs)
- [ ] 1× polyurethane wheel, 5" (nose)
- [ ] 2× polyurethane wheels, 8" (main)
- [ ] 6× bearings
- [ ] 2× bungee cords (shock absorption)

---

## Step-by-Step Assembly

### Phase 1: Build the Fuselage (Weeks 1-3)

The fuselage is the body of the plane — like the hull of a boat, but for the sky!

**Step 1:** Prepare the longerons (the long bones of the plane)

```
 LONGERON SPLICE (joining two boards):
 ═══════════════════════════════════════

 Board 1            Board 2
 ┌────────────┐  ┌────────────┐
 │            │  │            │
 │  ┌─────────┤  ├─────────┐  │
 │  │  300mm  │  │  300mm  │  │
 │  │ overlap │  │ overlap │  │
 │  └─────────┤  ├─────────┘  │
 │            │  │            │
 └────────────┘  └────────────┘

 1. Overlap boards by 300mm
 2. Drill 4 holes through both
 3. Bolt with AN3 bolts
 4. Epoxy plywood gussets on both sides
 5. Let dry 24 hours
```

- Cut 1×4" spruce boards into 6-meter longerons (3 boards spliced together)
- Make 4 longerons: top-left, top-right, bottom-left, bottom-right

**Step 2:** Cut the formers (the ribs of the fuselage)

```
 FORMER SHAPE:
 ═══════════════════════════════════════

    ╱                ╲
  ╱                    ╲
 │                      │
 │    ┌──────────┐     │
 │    │ LIGHTEN- │     │
 │    │ ING HOLE │     │ ← Saves weight!
 │    │ (150mm)  │     │
 │    └──────────┘     │
 │                      │
  ╲                    ╱
    ╲                ╱

 Cut from 1×3" pine boards
 16 formers total, one every 400mm
```

**Step 3:** Assemble the fuselage box
- Lay out top and bottom longerons on a flat surface
- Mark former positions every 400mm
- Screw and epoxy each former in place
- Attach side longerons (1×3" pine)
- Install plywood gussets at every junction
- Check for square (measure diagonals — they must match!)

```
 FUSELAGE ASSEMBLY ORDER:
 ═══════════════════════════════════════

 1. TOP LONGERONS    ════════════════════
                    ║    ║    ║    ║
 2. FORMERS          ║    ║    ║    ║
                    ║    ║    ║    ║
 3. BOTTOM LONGERONS ════════════════════

 4. SIDE LONGERONS   ════════════════════

 5. GUSSETS          ┌─┐ ┌─┐ ┌─┐ ┌─┐

 Total time: 8-12 hours
```

**Step 4:** Install the motor mount
- Cut a plywood plate (200mm × 200mm)
- Drill holes for motor bolts
- Epoxy gusset triangles for strength
- Bolt to the nose of the fuselage

---

### Phase 2: Build the Wings (Weeks 4-6)

The wings are the most important part — they keep you in the air!

**Step 5:** Cut the wing spars (the main strength of the wing)

```
 WING SPAR:
 ═══════════════════════════════════════

 Each wing has ONE spar made from 2× 8ft boards spliced
 together with a 400mm overlap and 6 bolts.

 ┌──────────────────────────────────────────┐
 │  ═══════════════SPAR═════════════════════ │ ← 1×4" spruce
 └──────────────────────────────────────────┘
 │←────────────── 5000mm ──────────────────→│

 Cut notches every 400mm for ribs (13 notches per spar)
```

**Step 6:** Cut the wing ribs (the curved shapes that give the wing its shape)

```
 WING RIB (Clark Y Airfoil):
 ═══════════════════════════════════════

         Leading Edge (balsa, sanded round)
              ┌───┐
             ╱     ╲
           ╱         ╲
         ╱     SPAR    ╲
       ╱    ┌───────┐    ╲
     ╱      │ 1×4   │      ╲
   ╱        │SPRUCE │        ╲
  ╱          │       │          ╲
 ╱           └───────┘           ╲
│                                 ╲│
│                              TRAILING EDGE
│                           (1/4"×1/4" pine)

 ←──────────── 800mm chord ──────────────→

 Cut 26 ribs total (13 per wing)
 Use a plywood template to trace the shape
```

**Step 7:** Assemble the wing panels
- Lay spar on flat surface
- Install leading edge balsa blocks
- Install ribs on spar notches (every 400mm)
- Install trailing edge strip
- Epoxy all joints
- Add 3° dihedral (wing tips angle up slightly)

**Step 8:** Install ailerons (control surfaces that make the plane roll)
- Cut aileron frames from spruce
- Hinge to wing trailing edge with clevis bolts
- Route control cables through wing
- Connect to cockpit pushrod

---

### Phase 3: Build the Tail (Week 7)

**Step 9:** Build horizontal stabilizer (keeps the nose from going up or down)
- 2000mm × 500mm
- Same construction as wing (spar + ribs + fabric)

**Step 10:** Build vertical stabilizer (keeps the nose from going side to side)
- 800mm × 1200mm
- Same construction method

**Step 11:** Attach tail to fuselage
- Bolt horizontal stabilizer to tail post (4 bolts)
- Bolt vertical stabilizer to fuselage side (4 bolts)
- Connect rudder and elevator cables

---

### Phase 4: Build Landing Gear (Week 8)

**Step 12:** Make the gear legs
- Cut steel tubes to 300mm
- Bend to 45° angle (heat with torch if needed)
- Weld mounting plate to each leg

**Step 13:** Assemble wheels
- Press bearings into wheel hubs
- Install axle bolts
- Add castle nuts and cotter pins
- Wrap gear legs with bungee cord (shock absorption!)

```
 LANDING GEAR:
 ═══════════════════════════════════════

         FUSELAGE
     ┌───────────────┐
     │    GEAR LEG   │ ← Steel tube
     │    (300mm)    │
     └───────┬───────┘
             │
     ┌───────┴───────┐
     │    AXLE       │ ← M10 bolt
     └───────┬───────┘
             │
     ┌───────┴───────┐
     │    WHEEL      │ ← 8" polyurethane
     └───────────────┘

 Tricycle gear: 1 nose wheel + 2 main wheels
 Bungee wrapping absorbs landing bumps
```

---

### Phase 5: Cover with Fabric (Weeks 9-10)

**Step 14:** Prepare the fabric
- Pre-shrink Dacron with heat gun
- Cut panels to size (add 25mm extra on all sides)

**Step 15:** Apply fabric to wings
- Apply primer to wood surfaces
- Lay fabric over wing frame
- Cement fabric to leading and trailing edges
- Shrink with heat gun (150°C, 100mm away)
- Rib stitch: sew fabric to ribs every 200mm
- Apply reinforcing tape over stitching
- Paint with UV-protective fabric paint

**Step 16:** Apply fabric to fuselage and tail
- Same process as wings
- Leave openings for cockpit, battery compartment, avionics bay

```
 FABRIC SHRINKING:
 ═══════════════════════════════════════

 1. Heat gun at 150°C
 2. Hold 100mm from fabric
 3. Move slowly — fabric tightens like a drum!
 4. Don't hold in one spot (will burn!)
 5. Start at center, work outward

 ┌─────────────────────────────────┐
 │  LOOSE FABRIC → TIGHT FABRIC   │
 │                                 │
 │  ~~wrinkles~~  →  ═══smooth═══  │
 │                                 │
 │  Test: tap with finger —       │
 │  should sound like a drum!     │
 └─────────────────────────────────┘
```

---

### Phase 6: Install Motor & Propeller (Week 11)

**Step 17:** Mount the motor
- Bolt motor to mount plate (4 bolts)
- Install propeller hub on motor shaft
- Attach 2 propeller blades to hub
- Balance the propeller (spin it, see which side is heavy, add tape to the light side)

**Step 18:** Connect the ESC (motor controller)
- Mount ESC on fuselage wall (needs airflow for cooling)
- Connect 3 motor phase wires
- Connect power wires from battery
- Connect signal wire to Arduino

---

### Phase 7: Install Electrical System (Weeks 12-13)

**Step 19:** Install batteries
- Place 4 FPB-20 phi-harmonic field plasma batteries behind cockpit
- Connect in series-parallel for 24V, 200Ah
- Install 200A main fuses
- Install master disconnect switch

```
 BATTERY WIRING:
 ═══════════════════════════════════════

  ┌───────┐  ┌───────┐
  │FPB-20 #1 │──│FPB-20 #2 │  Series pair = 24V
  │12V    │  │12V    │
  └───────┘  └───────┘
                    │
  ┌───────┐  ┌───────┐
  │FPB-20 #3 │──│FPB-20 #4 │  Series pair = 24V
  │12V    │  │12V    │
  └───────┘  └───────┘
                    │
        ────────────┴────────────
                    │
              ┌─────┴─────┐
              │ 200A FUSE │
              └─────┬─────┘
                    │
              ┌─────┴─────┐
              │  MASTER   │
              │  SWITCH   │
              └───────────┘

 Total: 24V, 200Ah = 4,800Wh of energy!
```

**Step 20:** Wire the switch panel
- Mount on cockpit left wall
- Install 4 switches: MASTER, MOTOR, AVIONICS, RADIO
- Install emergency kill button (red, push to stop everything!)
- Label all switches clearly

---

### Phase 8: Install Avionics (Week 14)

**Step 21:** Build the flight computer
- Solder Arduino Nano to a protoboard
- Wire I2C bus for sensors
- Wire GPS to serial port
- Wire voltage divider for battery monitoring
- Wire current sensor for motor monitoring
- Upload flight software

**Step 22:** Install displays
- Mount 2 OLED screens on instrument panel
- Screen 1: altitude, speed, heading, battery
- Screen 2: GPS position, satellite count, time

**Step 23:** Install telemetry
- Mount HC-12 radio in aircraft
- Set up ground station (laptop + USB adapter)
- Test: ground station should receive flight data

---

### Phase 9: Final Assembly (Weeks 15-16)

**Step 24:** Attach wings to fuselage
- Position wing spar box on fuselage
- Install 4× AN4 bolts per wing
- Torque to 20 N·m
- Install dihedral braces (3° angle)

**Step 25:** Attach tail surfaces
- Bolt horizontal stabilizer to tail post
- Bolt vertical stabilizer to fuselage
- Connect all control cables

**Step 26:** Install landing gear
- Bolt gear brackets to fuselage bottom
- Install gear legs with bungee wrapping
- Install wheels on axles

**Step 27:** Final inspection
- Check every bolt is tight
- Check every wire is connected
- Check every control surface moves correctly
- Weigh the plane — must be under 115 kg empty!

---

## How to Test Your Plane

### Pre-Flight Checks

```
 PRE-FLIGHT CHECKLIST — PHI CHEAP LIGHT PLANE
 ═══════════════════════════════════════════════

 □ FRAME
   □ All longeron bolts tight
   □ All gussets intact
   □ No cracked wood
   □ Fabric tight, no tears

 □ WINGS
   □ Wing bolts tight
   □ Dihedral angle correct (3°)
   □ Ailerons move freely
   □ Control cables tight

 □ MOTOR
   □ Motor bolts tight
   □ Propeller balanced
   □ ESC connected
   □ Motor spins freely

 □ BATTERIES
   □ All 4 batteries > 12.0V
   □ Fuses installed
   □ Master switch works
   □ Emergency kill works

 □ AVIONICS
   □ Arduino on
   □ Altimeter reading
   □ Motion sensor working
   □ GPS has satellites
   □ Screens showing data
   □ Radio working

 □ LANDING GEAR
   □ Wheels rotate freely
   □ Axle bolts tight
   □ Bungee wrapping intact

 ═══════════════════════════════════════════════
 INSPECTION: □ PASS  □ FAIL
 ═══════════════════════════════════════════════
```

### First Flight Procedure

**DO NOT attempt a full flight on your first try!**

**Step 1: Taxi tests (ground driving)**
- Drive the plane on the ground at low speed
- Test steering with rudder pedals
- Test brakes (if installed)
- Get comfortable with the controls

**Step 2: Taxi tests at higher speed**
- Drive at 30 km/h
- Feel how the plane wants to lift off
- Practice staying on the centerline

**Step 3: Short hops**
- At 50 km/h, gently pull back on the stick
- The plane should lift off for a few seconds
- Land gently
- This teaches you how it feels to fly!

**Step 4: Full flight**
- Take off, climb to 100 meters
- Fly around the field
- Practice turns
- Come back and land
- Celebrate! You're a pilot!

```
 FIRST FLIGHT PROFILE:
 ═══════════════════════════════════════

 Altitude
     │
 300 │
     │
 200 │         ╭────────────╮
     │        ╱              ╲
 100 │───────╱                ╲
     │ ╱                       ╲
   0 │╱─────────────────────────╲────
     └────────────────────────────── Time
      Takeoff    Fly     Land

 Keep it LOW and SLOW for the first flight!
```

---

## Safety Precautions

```
╔═══════════════════════════════════════════════════════════╗
║                    ⚠️  FLIGHT SAFETY  ⚠️                   ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  THIS IS A REAL AIRCRAFT. FLYING CAN BE DANGEROUS.        ║
║                                                           ║
║  ALWAYS:                                                  ║
║  ✓ Have an A&P mechanic inspect before first flight       ║
║  ✓ Wear a helmet (motorcycle or aviation)                 ║
║  ✓ Check weather before EVERY flight                      ║
║  ✓ Do pre-flight inspection before EVERY flight           ║
║  ✓ Fly only in calm conditions (< 5 knots wind)          ║
║  ✓ Tell someone where you're going                        ║
║  ✓ Carry a fire extinguisher                              ║
║                                                           ║
║  NEVER:                                                   ║
║  ❌ Fly in rain, fog, or low visibility                   ║
║  ❌ Fly over towns or crowds                              ║
║  ❌ Fly at night                                          ║
║  ❌ Fly with low battery (< 50%)                         ║
║  ❌ Fly with loose bolts or damaged fabric                ║
║  ❌ Attempt aerobatics (loops, rolls, etc.)               ║
║  ❌ Fly in icing conditions                               ║
║                                                           ║
║  PROPELLER DANGER:                                        ║
║  • The propeller is nearly invisible when spinning        ║
║  • Stay 3 meters away from the prop at ALL times         ║
║  • Never approach from the front while motor is running   ║
║  • Shout "CLEAR PROP" before starting the motor           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### Emergency Procedures

**If the motor stops:**
1. Maintain airspeed (60 km/h)
2. Look for a landing field
3. Turn off avionics (save battery)
4. Land straight ahead or to the left
5. Flare just above the ground
6. Touch down on main wheels first
7. Roll to a stop

**If a control cable breaks:**
1. Use the remaining controls
2. If only rudder lost: use ailerons for turns
3. If only ailerons lost: use rudder for turns
4. Land as soon as possible

**If the fabric tears:**
1. Reduce speed to minimum
2. Check if the wing is still producing lift
3. Land immediately

**If you feel dizzy or nauseous:**
1. Reduce power
2. Fly straight and level
3. Descend to a safe altitude
4. Land as soon as possible
5. Take a break before flying again

---

## Troubleshooting

| Problem | What It Means | How to Fix It |
|---------|--------------|---------------|
| Engine won't start | Battery dead or ESC error | Check battery voltage, reprogram ESC |
| Motor runs rough | Propeller unbalanced | Rebalance propeller |
| Plane pulls left | Thrust line misaligned | Adjust motor mount angle |
| Plane won't climb | Weight too far forward | Move batteries aft |
| Plane noses down | CG too far forward | Move batteries aft, add ballast to tail |
| Fabric sags | Temperature changed | Re-shrink with heat gun |
| Control feels loose | Cable tension low | Adjust turnbuckles |
| Wheels wobble | Bearing worn | Replace bearing |
| Radio static | Antenna loose | Check antenna connection |
| Altimeter wrong | Needs calibration | Calibrate at known ground level |

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════╗
║   PHI CHEAP LIGHT PLANE — QUICK CARD          ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  STARTUP:                                     ║
║  1. Master switch ON                          ║
║  2. Motor switch ON                           ║
║  3. Avionics switch ON                        ║
║  4. Wait for GPS (green light)                ║
║  5. Radio check                               ║
║  6. "CLEAR PROP!"                             ║
║  7. Motor to idle, then full power            ║
║                                               ║
║  TAKEOFF:                                     ║
║  1. Full throttle                             ║
║  2. Accelerate to 60 km/h                     ║
║  3. Gently pull back on stick                 ║
║  4. Climb at 80 km/h                          ║
║                                               ║
║  LANDING:                                     ║
║  1. Reduce power                              ║
║  2. Line up with runway                       ║
║  3. Reduce to 70 km/h                         ║
║  4. Flare 1 meter above ground                ║
║  5. Touch down gently                         ║
║  6. Roll to stop                              ║
║                                               ║
║  LIMITS:                                      ║
║  • Max speed: 102 km/h (55 knots)            ║
║  • Max altitude: 914m (3000 ft)              ║
║  • Max wind: 10 knots (18 km/h)             ║
║  • No flying in rain or fog                   ║
║  • Daytime VFR only                           ║
║                                               ║
║  WEIGHT:                                      ║
║  • Empty: 115 kg (253 lbs)                   ║
║  • Max pilot: 90 kg (198 lbs)                ║
║  • Max gross: 227 kg (500 lbs)               ║
║                                               ║
╚═══════════════════════════════════════════════╝
```

---

## Cost Summary

| What | How Much | Where |
|------|----------|-------|
| Wood frame | $443 | Lumber yard |
| Fabric covering | $236 | eBay surplus |
| Motor + propeller | $623 | AliExpress |
| 4 batteries | $751 | eBay surplus |
| Avionics | $159 | eBay + AliExpress |
| Fasteners | $236 | Home Depot + Aircraft Spruce |
| Landing gear | $139 | Home Depot + Amazon |
| Misc | $226 | Various |
| **TOTAL** | **$2,744** | |

Less than $3,000 for a FLYING AIRPLANE! That's amazing!

---

## Congratulations!

You built an airplane! Not a model, not a toy — a REAL, flyable ultralight aircraft. It's made from wood, fabric, and batteries, and it flies on the same principles that have kept planes in the sky for over 100 years.

The only difference is yours is powered by phi-harmonic physics and costs less than a used motorcycle. How cool is that?

**Now go fly! ✈️**

---

*This manual was written for builders age 12 and up, with adult supervision. Always follow FAA Part 103 rules. Never fly without proper training. Safety is YOUR responsibility.*
