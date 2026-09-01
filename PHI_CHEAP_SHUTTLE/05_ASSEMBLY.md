# PHI CHEAP SHUTTLE — ASSEMBLY INSTRUCTIONS

## Step-by-Step Build Guide

**Estimated Build Time:** 400-600 hours (2 builders, 3-6 months)
**Skill Required:** TIG welding, fiberglass layup, electronics assembly

---

## PHASE 1: FRAME FABRICATION (80-120 hours)

### Step 1.1: Cut Aluminum Tubes
1. Measure and mark all tubes per frame drawing
2. Cut to φ-harmonic lengths using horizontal band saw or chop saw with carbide blade
3. Deburr all cuts with file and sandpaper
4. Clean cuts with acetone

### Step 1.2: Weld Main Frame
1. Tack-weld longitudinal tubes to cross-members on welding table
2. Check squareness with speed square (tolerance: ±2mm over 3m)
3. Full-weld all joints with ER4043 filler, TIG process
4. Weld sequence: center outward, alternating sides to minimize distortion
5. Allow cooling between welds (do not quench)

### Step 1.3: Install Gussets
1. Cut aluminum angle to 423.6mm lengths (φ³ × 100mm)
2. Weld gussets at all critical joints (90° corners, thruster mounts)
3. Minimum fillet weld size: 3mm

### Step 1.4: Weld Thruster Mounts
1. Drill M10 holes in 6mm aluminum mounting plates
2. Weld mounting plates to frame at thruster positions
3. Verify plate flatness (±0.5mm)

### Step 1.5: Install Floor Pan
1. Cut 1/8" aluminum plate to cockpit dimensions
2. Drill holes for seat mounting (M10, 4 per seat)
3. Stitch-weld to frame (50mm welds, 100mm spacing)
4. Leave access holes for wiring routing

---

## PHASE 2: FIBERGLASS SHELL (80-100 hours)

### Step 2.1: Build Mold/Plug
1. Create foam plug for nose cone (carve from rigid insulation foam)
2. Cover with body filler, sand smooth (220 grit → 400 grit)
3. Apply mold release wax (3 coats, buff between)

### Step 2.2: Layup Shell Sections
1. Mix polyester resin with MEKP hardener (10:1 ratio by volume)
2. Apply gel coat to mold surface (0.5mm)
3. Lay 2oz cloth, wet out with resin
4. Lay 6oz cloth ×2 at ±45° and 0°/90°
5. Apply foam core (12mm PVC)
6. Lay 6oz cloth ×2 on outside
7. Roll out air bubbles with phenolic roller
8. Cure 24 hours at room temperature

### Step 2.3: Trim and Fit
1. Trim excess fiberglass with oscillating multi-tool
2. Test fit to frame, mark trimming lines
3. Sand edges smooth (80 grit → 220 grit)
4. Drill rivet holes (3/16") at 50mm spacing

### Step 2.4: Attach Shell to Frame
1. Apply structural adhesive (3M 5200) to frame contact points
2. Rivet shell to frame with pop rivets
3. Seal joints with high-temp silicone
4. Apply body filler to smooth rivet heads

---

## PHASE 3: PROPULSION SYSTEM (100-140 hours)

### Step 3.1: Wind Thruster Coils
1. Prepare T106-2 ferrite toroid cores (8 total, 2 per thruster)
2. Wind 47 turns of 18 AWG Litz wire per core
3. Maintain even spacing, secure with kapton tape
4. Measure inductance: target 2.3mH ±10%

### Step 3.2: Assemble Resonant Tanks
1. Mount 4× 0.1μF 2kV film capacitors in parallel on PCB
2. Connect to coil terminals with short leads (<50mm)
3. Verify resonant frequency with LC meter: target 161.8 kHz

### Step 3.3: Build Full-Bridge Inverters
1. Mount IRFP460 MOSFETs on aluminum heatsinks
2. Apply thermal paste between MOSFET and heatsink
3. Wire IR2110 gate drivers per circuit schematic
4. Install 0.1μF 50V bootstrap capacitors
5. Wire full-bridge topology

### Step 3.4: Build Plasma Tubes
1. Clean quartz tubes with acetone
2. Install stainless steel mesh grid (anode)
3. Install tungsten wire center electrode (cathode)
4. Seal with high-temp silicone gasket
5. Connect to ignit

### Step 3.5: Mount Exhaust Nozzles
1. Drill copper nozzles to φ-ratio dimensions (throat 15mm, exit 24.27mm)
2. Thread for M10 mounting bolts
3. Attach to thruster housing with silicone gasket
4. Align nozzle axis with thrust vector

### Step 3.6: Assemble Complete Thrusters
1. Mount coil assembly to ceramic insulators
2. Attach plasma tube to coil assembly
3. Mount exhaust nozzle
4. Wire power connections (4 AWG from bus)
5. Wire gate driver connections (22 AWG to Arduino)
6. Repeat for all 4 thrusters

---

## PHASE 4: POWER SYSTEM (40-60 hours)

### Step 4.1: Prepare Battery Compartments
1. Line battery boxes with ceramic blanket (thermal protection)
2. Install rubber mounting pads
3. Route 4 AWG cables from bus bar to battery positions
4. Install ANL fuse holders

### Step 4.2: Install Bus Bar
1. Mount copper bus bar (1/4" × 1") to frame with insulated standoffs
2. Connect battery cables to bus bar with ring terminals
3. Install 400A master disconnect switches

### Step 4.3: Install Batteries
1. Place FPB-20 phi-harmonic field plasma batteries in boxes
2. Connect terminals (positive first, then negative)
3. Secure with nylon straps
4. Install battery voltage monitors

---

## PHASE 5: AVIONICS (40-60 hours)

### Step 5.1: Build Avionics Panel
1. Mount Arduino Mega to aluminum bracket
2. Wire power supply (12V → 5V buck, 12V → 3.3V LDO)
3. Install OLED displays in panel cutouts
4. Wire toggle switches and pushbuttons

### Step 5.2: Install Sensors
1. Mount GPS module on frame (clear sky view)
2. Mount IMU at center of gravity
3. Mount barometric altimeters in protected bay
4. Wire all sensors per circuit schematic

### Step 5.3: Install Communications
1. Mount VHF radios in cockpit (pilot and passenger positions)
2. Route antenna cables to frame mounting points
3. Connect HC-12 telemetry modules
4. Test radio range (minimum 1km ground test)

### Step 5.4: Install Servos
1. Mount servo brackets to thruster pivots
2. Connect servo horns to thrust vector mechanisms
3. Wire servos to PCA9685 driver
4. Test servo range (±15°)

---

## PHASE 6: WIRING (40-60 hours)

### Step 6.1: Run Power Wiring
1. Route 4 AWG cables from bus bar to thrusters
2. Route 10 AWG cables from bus bar to avionics
3. Crimp ring terminals, heat-shrink all connections
4. Secure wiring with P-clamps every 200mm

### Step 6.2: Run Signal Wiring
1. Route sensor cables (shielded twisted pair)
2. Route servo cables (3-conductor)
3. Route communication cables
4. Label all wires with heat-shrink labels

### Step 6.3: Ground System
1. Install star ground point on aluminum floor pan
2. Connect all grounds to star point with 10 AWG green/yellow wire
3. Scratch through anodize at ground connection points
4. Verify continuity (<0.1Ω to frame)

---

## PHASE 7: RECOVERY SYSTEM (10-15 hours)

### Step 7.1: Install Parachute Compartments
1. Mount parachute deployment bags in aft fuselage
2. Install quick-release pins (pull-type)
3. Connect pull cables to cockpit handles
4. Test deployment mechanism (ground test, no canopy)

---

## PHASE 8: FINAL ASSEMBLY (20-30 hours)

### Step 8.1: Install Landing Gear
1. Weld landing gear mounts to frame
2. Attach skid tubes with pivot bolts
3. Install coil springs (200 lb/in)
4. Attach rubber skid pads

### Step 8.2: Install Canopy
1. Mount canopy hinge to frame
2. Attach gas struts for assisted opening
3. Install canopy latch
4. Test open/close cycle

### Step 8.3: Final Inspection
1. Check all fasteners (torque to spec)
2. Check all wiring connections
3. Check all welds (visual + dye penetrant on 10%)
4. Verify weight and balance
5. Complete weight and balance report

---

## PHASE 9: TESTING (40-60 hours)

### Step 9.1: Ground Tests
1. Battery charge/discharge cycle test
2. Thruster ignition test (static, no thrust)
3. Thruster full-power test (with thrust measurement)
4. Avionics functional test
5. Communications range test
6. Landing gear drop test (1m drop, measure g-load)

### Step 9.2: Taxi Tests
1. Low-speed taxi (0-30 mph)
2. Medium-speed taxi (30-60 mph)
3. High-speed taxi (60-100 mph)
4. Verify steering, braking, tracking

### Step 9.3: Flight Test
1. First flight: low altitude (< 1 km), short duration
2. Progressive altitude increases
3. Full envelope test: 100 km altitude, Mach 3
4. Emergency procedures test (parachute deployment)

---

## TOOLS REQUIRED

| Tool | Purpose | Estimated Cost |
|------|---------|---------------|
| TIG Welder (AC/DC) | Aluminum welding | $800 (used) or rent |
| Horizontal Band Saw | Tube cutting | $200 (used) or rent |
| Drill Press | Hole drilling | $150 (used) or manual drill |
| Rivet Gun | Pop rivet installation | $15 (included in H12) |
| Soldering Iron (60W) | Electronics assembly | $25 |
| Multimeter | Electrical testing | $30 |
| Oscilloscope (optional) | Thruster tuning | $200 (used) or borrow |
| LC Meter (optional) | Resonant tank tuning | $50 (AliExpress) |
| Torque Wrench | Fastener torque | $35 |
| Angle Grinder | Cutting/grinding | $40 |
| Clamps (various) | Assembly holding | $50 |
| Safety Gear | Protection | $50 (included in X05-X07) |

**Total Tool Cost: ~$1,645** (if buying all new; many can be borrowed/rented)
