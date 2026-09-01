# PHI TIME SHUTTLE — ASSEMBLY INSTRUCTIONS

## Step-by-Step Build Guide (12-Year-Old Friendly)

**Estimated Build Time:** 800-1,200 hours (2 builders, 6-12 months)
**Skill Required:** TIG welding, carbon fiber layup, cryogenics, electronics assembly
**Safety:** Adult supervision required. Cryogenic handling requires training.

---

## PHASE 1: FRAME FABRICATION (150-200 hours)

### Step 1.1: Cut Carbon Fiber Tubes
1. Measure and mark all CF tubes per frame drawing
2. Cut using diamond-coated blade on chop saw (wear respirator!)
3. Deburr all cuts with 220-grit sandpaper
4. Clean cuts with isopropyl alcohol
5. **⚠️ Wear gloves — CF dust is itchy and harmful**

### Step 1.2: Cut Aluminum Space Frame Tubes
1. Measure and mark 7075-T6 tubes per drawing
2. Cut to φ-harmonic lengths using horizontal band saw
3. Deburr all cuts with file
4. Clean cuts with acetone

### Step 1.3: Weld Aluminum Space Frame
1. Set up welding table with fixtures
2. Tack-weld longitudinal tubes to cross-members
3. Check squareness with speed square (±2mm over 3m)
4. Full-weld all joints with ER5356 filler, TIG process
5. Weld sequence: center outward, alternating sides
6. Allow cooling between welds (do not quench)

### Step 1.4: Assemble Carbon Fiber Hull Frame
1. Bond CF tubes at joints using epoxy adhesive (3M DP420)
2. Clamp with C-clamps, allow 24hr cure
3. Reinforce joints with CF cloth wrap (2 layers, ±45°)
4. Verify alignment with laser level

### Step 1.5: Install Invar Temporal Frame
1. Position Invar 36 rods at temporal frame mounting points
2. Weld Invar joints with ERNi-3 filler (nickel-based)
3. Mount kinematic mount bases (3 per coil position)
4. Verify alignment: ±0.008mm tolerance (use dial indicator)

### Step 1.6: Install Titanium Structural Struts
1. Cut Ti-6Al-4V tubes to 618mm (φ × 382mm)
2. Thread ends for M6 titanium bolts
3. Attach struts from temporal frame to hull frame
4. Torque to 8 N·m with anti-seize compound

### Step 1.7: Install Floor Pan
1. Cut CFRP honeycomb panel to cockpit dimensions
2. Drill M6 holes for seat mounting (4 per seat)
3. Bond to frame with structural adhesive
4. Reinforce edges with CF tape

---

## PHASE 2: HULL SKIN (150-200 hours)

### Step 2.1: Prepare Hull Mold
1. Create foam plug for hull sections (carve from rigid foam)
2. Cover with body filler, sand smooth (220 → 400 grit)
3. Apply mold release wax (3 coats, buff between)

### Step 2.2: Layup CFRP Hull Panels
1. Lay CF cloth [0/±45/90]₅ quasi-isotropic schedule
2. Wet out with epoxy resin using vacuum infusion
3. Cure under vacuum bag (24 hours at room temperature)
4. Post-cure at 60°C for 4 hours (if oven available)

### Step 2.3: Install Shielding Layers
1. Bond lead lining (2.5mm) to inner hull surfaces
2. Apply tungsten foil (1.5mm) over lead
3. Attach polyethylene sheet (25mm) for neutron shielding
4. Seal all edges with epoxy

### Step 2.4: Attach Hull Skin to Frame
1. Test fit hull panels to frame
2. Bond with structural adhesive (3M DP420)
3. Rivet with pop rivets (3/16" aluminum, 50mm spacing)
4. Seal joints with high-temp silicone
5. Apply ceramic TPS tiles to exterior

---

## PHASE 3: TEMPORAL COIL ARRAY (200-300 hours)

### Step 3.1: Wind Temporal Coils (8 total)
1. Mount alumina ceramic former on winding machine
2. Wind 1,618 turns of YBCO superconductor wire
3. Maintain even tension (5N) and spacing
4. Secure windings with kapton tape every 100 turns
5. Measure inductance: target 3.6 mH ±5%
6. **⚠️ Handle YBCO wire carefully — brittle superconductor**

### Step 3.2: Test Coil Performance
1. Measure inductance with LCR meter
2. Measure DC resistance (should be <1mΩ at 77K)
3. Immerse in liquid nitrogen (77K)
4. Test current capacity: ramp to 6,000A
5. Verify no quench (sudden resistance jump)

### Step 3.3: Install Cryogenic System
1. Mount LN2 dewar (50L) in battery bay
2. Route insulated hoses to each coil position
3. Install solenoid valves for flow control
4. Wrap coils in MLI insulation (10 layers)
5. Test LN2 flow to each coil (2L/hour each)

### Step 3.4: Mount Coils on Temporal Frame
1. Install kinematic mounts on each coil former
2. Position coils at temporal frame mounting points
3. Verify alignment with dial indicator (±0.008mm)
4. Connect LN2 hoses to each coil
5. Connect power leads (10mm silicone, 6000A rated)

### Step 3.5: Wire Coil Drive Electronics
1. Mount full-bridge inverters on heatsinks
2. Wire MOSFETs (1200V 300A) per circuit schematic
3. Install gate drivers (isolated, 5kV)
4. Connect phase-lock loop boards
5. Wire PID controllers (phi-tuned gains)
6. Test gate drive signals with oscilloscope

---

## PHASE 4: POWER SYSTEM (60-80 hours)

### Step 4.1: Install Battery Bay
1. Line battery compartment with ceramic blanket
2. Install phase-change cooling pads
3. Mount copper bus bar on insulated standoffs
4. Route 2/0 AWG cables from bus bar to battery positions

### Step 4.2: Install FPB-100 Batteries
1. Place 4× FPB-100 batteries in bay
2. Connect terminals (positive first, then negative)
3. Secure with nylon straps (2" wide)
4. Connect voltage/current monitors
5. **⚠️ Batteries are heavy (85 kg each) — use hoist**

### Step 4.3: Install Power Distribution
1. Mount ANL fuse holders (500A)
2. Install 600A master disconnect switches
3. Wire auxiliary DC-DC converters (48V→12V, 48V→5V)
4. Test all power circuits before connecting loads

---

## PHASE 5: NAVIGATION SYSTEM (60-80 hours)

### Step 5.1: Install Navigation Computer
1. Mount Raspberry Pi 4 (8GB) in shielded enclosure
2. Connect power supply (48V→12V DC-DC)
3. Install navigation display (10.1" touchscreen)
4. Mount in cockpit console

### Step 5.2: Install Sensors
1. Mount rubidium atomic clock (clear sky view)
2. Mount IMU at center of gravity
3. Mount temporal radar transmitter + antenna
4. Mount 4× coherence sensors at hull positions
5. Mount fiber-optic gyroscope
6. Wire all sensors per circuit schematic

### Step 5.3: Install Chronology Monitor
1. Mount chronology monitor board
2. Connect to navigation computer (I2C)
3. Test CTC detection logic
4. Verify abort trigger works

---

## PHASE 6: SAFETY SYSTEMS (80-100 hours)

### Step 6.1: Install Fire Detection
1. Mount smoke detectors (4 locations)
2. Mount heat detectors (2 locations)
3. Mount flame detector (cabin)
4. Mount gas detector (battery bay)
5. Wire all detectors to safety controller

### Step 6.2: Install Fire Suppression
1. Mount CO₂ extinguisher solenoid (cabin)
2. Mount FM-200 system (electronics bay)
3. Mount N₂ flood system (coil bay)
4. Wire to safety controller
5. Test solenoid operation (dry run)

### Step 6.3: Install Quench System
1. Mount 8× quench switches (high-current)
2. Wire switches to heat sink bank (50kW)
3. Connect quench bus from coil inverters
4. Test quench sequence (dry run, no power)

### Step 6.4: Install Emergency Exits
1. Mount emergency exit mechanisms (left + right)
2. Connect cable releases to cockpit handles
3. Test release mechanism (door open/close)
4. Install warning labels

### Step 6.5: Install Emergency Beacon
1. Mount ELT (121.5 MHz + 406 MHz)
2. Connect antenna to external mount
3. Wire power (battery-backed 12V)
4. Test beacon transmission (ground test)

---

## PHASE 7: PASSENGER SYSTEMS (40-60 hours)

### Step 7.1: Install Seats
1. Mount carbon fiber bucket seats on floor rails
2. Install 4-point harnesses
3. Adjust seat position for pilot/copilot
4. Test harness release mechanism

### Step 7.2: Install Life Support
1. Mount O₂ generators (chemical, 45 min each)
2. Install CO₂ scrubber canisters
3. Mount temperature/humidity sensors
4. Install cabin fan (12V, 120mm)
5. Test O₂ flow

### Step 7.3: Install Temporal Cocoons
1. Position cocoon shells around seats
2. Install lead lining inside cocoons
3. Mount vital sign monitors (HR, SpO₂, resp)
4. Connect independent O₂ supply
5. Test cocoon closure mechanism

### Step 7.4: Install Windows
1. Cut polycarbonate panels (5mm)
2. Mount in window frames with rubber gaskets
3. Apply UV coating
4. Verify visibility and seal

---

## PHASE 8: COMMUNICATION SYSTEM (20-30 hours)

### Step 8.1: Install Radios
1. Mount VHF transceivers in cockpit
2. Route antenna cables to frame mounting points
3. Connect quantum-linked comms module
4. Test radio range (minimum 1km ground test)

### Step 8.2: Install Intercom
1. Mount aviation headset jacks
2. Wire intercom system
3. Test crew communication

---

## PHASE 9: WIRING (80-100 hours)

### Step 9.1: Run Power Wiring
1. Route 2/0 AWG from bus bar to batteries
2. Route 4 AWG to each temporal coil
3. Crimp ring terminals, heat-shrink all connections
4. Secure wiring with P-clamps every 200mm

### Step 9.2: Run Signal Wiring
1. Route sensor cables (shielded twisted pair)
2. Route navigation cables
3. Route safety system cables
4. Label all wires with heat-shrink labels

### Step 9.3: Ground System
1. Install star ground point on copper bus bar
2. Connect all grounds with 10 AWG green/yellow
3. Verify continuity (<0.1Ω to hull)

---

## PHASE 10: FINAL ASSEMBLY (40-60 hours)

### Step 10.1: Install Landing Gear
1. Weld landing gear mounts to frame
2. Attach struts with shock absorbers
3. Install wheels (10×4.00 pneumatic)
4. Verify ground clearance (500mm)

### Step 10.2: Final Inspection
1. Check all fasteners (torque to spec)
2. Check all wiring connections
3. Check all welds (visual + dye penetrant 10%)
4. Verify weight and balance
5. Complete weight and balance report

---

## PHASE 11: TESTING (80-120 hours)

### Step 11.1: Ground Tests
1. Battery charge/discharge cycle test
2. Temporal coil cool-down test (LN2, reach 77K)
3. Coil current ramp test (0→6000A)
4. Navigation system functional test
5. Safety system functional test
6. Quench system test (dry run)
7. Communications range test
8. Landing gear drop test (1m drop)

### Step 11.2: Fold Tests (Controlled)
1. Short-range fold test (1 meter)
2. Medium-range fold test (1 km)
3. Full-range fold test (24 hours)
4. Emergency abort test
5. Paradox prevention test

### Step 11.3: Flight Test
1. First fold: low energy, short range
2. Progressive range increases
3. Full envelope test: 24 hours temporal range
4. Emergency procedures test (fold abort)

---

## TOOLS REQUIRED

| Tool | Purpose | Estimated Cost |
|------|---------|---------------|
| TIG Welder (AC/DC) | Aluminum + Invar welding | $1,200 (used) or rent |
| Horizontal Band Saw | Tube cutting | $300 (used) or rent |
| Vacuum Pump | CF layup | $250 |
| Drill Press | Hole drilling | $200 (used) |
| Rivet Gun | Pop rivet installation | $15 (included in parts) |
| Soldering Iron (60W) | Electronics assembly | $30 |
| Multimeter | Electrical testing | $40 |
| Oscilloscope (100MHz) | Coil tuning | $250 (used) |
| LCR Meter | Inductance measurement | $60 (AliExpress) |
| Cryogenic Thermometer | LN2 testing | $45 |
| Torque Wrench | Fastener torque | $40 |
| Angle Grinder | Cutting/grinding | $45 |
| Clamps (various) | Assembly holding | $60 |
| Safety Gear | Protection | $80 (included in parts) |
| Respirator | CF dust protection | $35 |
| Hoist (manual, 1 ton) | Battery installation | $150 |

**Total Tool Cost: ~$2,750** (if buying all new; many can be borrowed/rented)
