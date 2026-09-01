# PHI-HARMONIC FIELD PLASMA BATTERY — ASSEMBLY INSTRUCTIONS

## Step-by-Step Assembly Guide (12-Year-Old Friendly)

### 1. Tools Required

```
    ESSENTIAL TOOLS
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   SAFETY GEAR:                                             │
    │   ├── Safety glasses (ANSI Z87.1)                          │
    │   ├── Heat-resistant gloves                                │
    │   ├── Anti-static wrist strap                               │
    │   └── Fire extinguisher (Class C, electrical)              │
    │                                                             │
    │   TOOLS:                                                   │
    │   ├── Screwdriver set (Phillips #1, #2, flathead)          │
    │   ├── Allen key set (2mm, 2.5mm, 3mm, 4mm)                │
    │   ├── Soldering iron (25-60W, adjustable temp)             │
    │   ├── Solder wire (SAC305 lead-free)                       │
    │   ├── Wire strippers (22-10 AWG)                           │
    │   ├── Wire cutters                                         │
    │   ├── Multimeter (Fluke or equivalent)                     │
    │   ├── Heat gun (for heat shrink tubing)                    │
    │   ├── Drill with bits (1mm-10mm)                           │
    │   ├── Tap set (M3, M4)                                     │
    │   ├── File set (flat, round, triangular)                   │
    │   ├── Sandpaper (220, 400, 800 grit)                       │
    │   ├── Clamps (various sizes)                               │
    │   ├── Tweezers (fine tip)                                  │
    │   └── Magnifying glass or loupe                            │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

### 2. Safety Precautions

```
    ⚠️  CRITICAL SAFETY RULES ⚠️
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   BEFORE YOU START:                                        │
    │   ✓ Read ALL instructions completely                       │
    │   ✓ Work in a well-ventilated area                         │
    │   ✓ Have fire extinguisher nearby                          │
    │   ✓ Wear safety glasses at ALL times                       │
    │   ✓ Wear heat-resistant gloves when soldering              │
    │   ✓ Use anti-static wrist strap with electronics           │
    │                                                             │
    │   NEVER:                                                   │
    │   ✗ Work alone — have adult supervisor present             │
    │   ✗ Touch live circuits with bare hands                    │
    │   ✗ Look directly at plasma (UV radiation)                 │
    │   ✗ Open gas cylinders near open flame                     │
    │   ✗ Bypass safety circuits                                 │
    │                                                             │
    │   EMERGENCY:                                               │
    │   → If fire: Use Class C extinguisher, do NOT use water    │
    │   → If shock: Call 911, do NOT touch victim while live     │
    │   → If gas leak: Evacuate, ventilate, do NOT spark         │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

### 3. Assembly Sequence Overview

```
    ASSEMBLY FLOW
    
    PHASE 1: PREPARATION (2 hours)
    ├── Step 1: Verify all components
    ├── Step 2: Prepare workspace
    ├── Step 3: Test electronics (bench test)
    └── Step 4: Pre-tin wires
    
    PHASE 2: STRUCTURE (3 hours)
    ├── Step 5: Cut and drill aluminum
    ├── Step 6: Prepare plasma chamber
    ├── Step 7: Install gas ports
    └── Step 8: Assemble outer casing
    
    PHASE 3: COILS (4 hours)
    ├── Step 9: Wind coils
    ├── Step 10: Test coil inductance
    ├── Step 11: Mount coils
    └── Step 12: Wire coil array
    
    PHASE 4: ELECTRONICS (3 hours)
    ├── Step 13: Build control board
    ├── Step 14: Build power board
    ├── Step 15: Build monitoring board
    └── Step 16: Wire all boards
    
    PHASE 5: INTEGRATION (2 hours)
    ├── Step 17: Install electronics
    ├── Step 18: Connect all wiring
    ├── Step 19: Final inspection
    └── Step 20: Gas fill and seal
    
    PHASE 6: TESTING (1 hour)
    ├── Step 21: Power-on test
    ├── Step 22: Containment test
    ├── Step 23: Safety test
    └── Step 24: Performance test
    
    TOTAL TIME: 15 hours (with breaks)
```

---

### 4. Step-by-Step Instructions

#### STEP 1: Verify All Components

```
    COMPONENT CHECKLIST
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   Check off each item as you verify it:                    │
    │                                                             │
    │   □ 6061-T6 Aluminum sheets (3mm and 5mm)                  │
    │   □ Enameled copper wire (18 AWG, 1000ft spool)            │
    │   □ Borosilicate glass tube                                │
    │   □ Viton O-rings                                          │
    │   □ G10 fiberglass sheets                                  │
    │   □ Aerogel blanket                                        │
    │   □ STM32F407 development board                            │
    │   □ NTC thermistors (10kΩ)                                 │
    │   □ Capacitive pressure sensor                             │
    │   □ MOSFET driver boards                                   │
    │   □ IRFZ44N MOSFETs                                        │
    │   □ DC-DC converter                                        │
    │   □ XT90 connectors                                        │
    │   □ JST-SH connectors                                      │
    │   □ Silicone rubber sheets                                 │
    │   □ Kapton tape                                            │
    │   □ Stainless steel bolts                                  │
    │   □ FR4 PCBs                                               │
    │   □ SAC305 solder                                          │
    │   □ Hydrogen gas cylinder                                  │
    │   □ Helium gas cylinder                                    │
    │   □ Gas pressure regulator                                 │
    │   □ Gas fill port                                          │
    │   □ Pressure relief valve                                  │
    │   □ Vacuum pump                                            │
    │   □ Piezoelectric elements                                 │
    │   □ Thermoelectric modules                                 │
    │   □ RF receiving coils                                     │
    │   □ Misc hardware                                          │
    │                                                             │
    │   If ANY item is missing or damaged, STOP and get          │
    │   replacement before proceeding.                           │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 2: Prepare Workspace

```
    WORKSPACE SETUP
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                   WORKBENCH                          │  │
    │   │                                                      │  │
    │   │   ┌──────────┐  ┌──────────┐  ┌──────────┐         │  │
    │   │   │SOLDERING │  │ ASSEMBLY │  │ TESTING  │         │  │
    │   │   │  STATION │  │  AREA    │  │  AREA    │         │  │
    │   │   └──────────┘  └──────────┘  └──────────┘         │  │
    │   │                                                      │  │
    │   │   Requirements:                                      │  │
    │   │   - Anti-static mat on all surfaces                  │  │
    │   │   - Good lighting (500+ lux)                         │  │
    │   │   - Ventilation fan (for soldering fumes)            │  │
    │   │   - Fire extinguisher within arm's reach             │  │
    │   │   - First aid kit visible                            │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 3: Test Electronics (Bench Test)

```
    BENCH TEST PROCEDURE
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   1. Connect STM32F407 to USB power (5V)                   │
    │                                                             │
    │   2. Upload test firmware:                                 │
    │      - Verify all GPIOs work                               │
    │      - Test ADC readings                                   │
    │      - Test PWM outputs                                    │
    │      - Test I2C communication                               │
    │                                                             │
    │   3. Test each component individually:                     │
    │      □ Thermistors: Measure resistance at room temp        │
    │        (should be ~10kΩ at 25°C)                           │
    │      □ Pressure sensor: Apply 0V, verify output            │
    │      □ MOSFETs: Gate trigger test (3.3V = ON)              │
    │      □ DC-DC converter: Verify 48V output                  │
    │      □ Connectors: Test continuity                         │
    │                                                             │
    │   4. If ANY component fails, replace before assembly       │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 4: Pre-tin Wires

```
    PRE-TINNING WIRES
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   1. Cut wires to required lengths:                        │
    │      - Power wires: 10 AWG, various lengths                │
    │      - Signal wires: 22 AWG, 150mm each                    │
    │      - Coil wires: 18 AWG, 15m each                        │
    │                                                             │
    │   2. Strip 3-5mm of insulation from each end               │
    │                                                             │
    │   3. Apply flux to stripped ends                           │
    │                                                             │
    │   4. Heat with soldering iron (350°C)                      │
    │                                                             │
    │   5. Apply solder until wire is coated                      │
    │                                                             │
    │   6. Allow to cool naturally (do NOT blow on it)           │
    │                                                             │
    │   7. Inspect: Smooth, shiny coating, no cold joints        │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 5: Cut and Drill Aluminum

```
    ALUMINUM FABRICATION
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   5.1 CUT OUTER CASING (3mm aluminum):                     │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │              CUTTING LAYOUT                          │  │
    │   │                                                      │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │ 500mm × 400mm (top plate)                   │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │ 500mm × 400mm (bottom plate)                │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │ 500mm × 250mm (side 1)                      │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │ 500mm × 250mm (side 2)                      │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │ 400mm × 250mm (side 3)                      │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │ 400mm × 250mm (side 4)                      │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │                                                      │  │
    │   │   Use: Jigsaw with metal-cutting blade              │  │
    │   │   Or: CNC router (if available)                      │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   5.2 DRILL HOLES:                                         │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │              DRILLING LAYOUT                         │  │
    │   │                                                      │  │
    │   │   For each side plate:                               │  │
    │   │   - Corner holes: 4mm (M4 bolts)                     │  │
    │   │   - Edge spacing: 15mm from edge                      │  │
    │   │   - Hole spacing: 100mm along edges                  │  │
    │   │                                                      │  │
    │   │   For top/bottom plates:                              │  │
    │   │   - Gas port hole: 12mm                              │  │
    │   │   - Connector holes: 20mm                            │  │
    │   │   - Ventilation holes: 6mm (if needed)               │  │
    │   │                                                      │  │
    │   │   Use: Step drill bit for clean holes                │  │
    │   │   Deburr all holes with file                         │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 6: Prepare Plasma Chamber

```
    PLASMA CHAMBER PREPARATION
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   6.1 GLASS TUBE PREPARATION:                              │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Clean tube with isopropyl alcohol               │  │
    │   │   2. Inspect for cracks or chips                     │  │
    │   │   3. Cut to length if needed (350mm for FPB-10)     │  │
    │   │   4. Sand edges smooth (220 grit → 400 → 800)       │  │
    │   │   5. Clean again with IPA                            │  │
    │   │   6. Dry completely (use heat gun on LOW)            │  │
    │   │                                                      │  │
    │   │   ⚠️  Glass is fragile — handle with care!          │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   6.2 O-RING GROOVES:                                      │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Measure tube outer diameter                     │  │
    │   │   2. Select O-ring size (Viton, 3mm cross-section)  │  │
    │   │   3. Test fit O-ring on tube ends                    │  │
    │   │   4. Apply vacuum grease to O-rings                  │  │
    │   │   5. Place O-rings in groove                         │  │
    │   │   6. Verify seal (should be snug, not forced)       │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 7: Install Gas Ports

```
    GAS PORT INSTALLATION
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   7.1 GAS FILL PORT:                                       │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Drill 12mm hole in top plate                    │  │
    │   │   2. Install brass fitting with O-ring seal          │  │
    │   │   3. Tighten to 5 N·m (do NOT over-tighten)         │  │
    │   │   4. Test for leaks (apply soapy water, look        │  │
    │   │      for bubbles when pressurized)                   │  │
    │   │                                                      │  │
    │   │   ┌──────────┐                                       │  │
    │   │   │  PLATE   │                                       │  │
    │   │   │ ┌──────┐ │                                       │  │
    │   │   │ │FITTING│ │                                       │  │
    │   │   │ └──────┘ │                                       │  │
    │   │   │  │    │  │                                       │  │
    │   │   │  │○RNG│  │                                       │  │
    │   │   └──┴────┴──┘                                       │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   7.2 PRESSURE RELIEF VALVE:                               │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Install relief valve on opposite side           │  │
    │   │   2. Set relief pressure to 2.0 Torr                 │  │
    │   │   3. Verify valve opens at set pressure              │  │
    │   │   4. Seal with thread sealant (Teflon tape)          │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 8: Assemble Outer Casing

```
    OUTER CASING ASSEMBLY
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   8.1 ASSEMBLE FRAME:                                      │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Lay out all aluminum pieces                     │  │
    │   │   2. Deburr all edges (file + sandpaper)             │  │
    │   │   3. Test fit all pieces together                    │  │
    │   │   4. Mark bolt holes with marker                     │  │
    │   │   5. Drill final holes (4mm)                         │  │
    │   │   6. Tap threads if needed (M4)                      │  │
    │   │                                                      │  │
    │   │   Assembly order:                                     │  │
    │   │   a. Attach side 1 to bottom plate                   │  │
    │   │   b. Attach side 2 to bottom plate                   │  │
    │   │   c. Attach side 3 to bottom plate                   │  │
    │   │   d. Attach side 4 to bottom plate                   │  │
    │   │   e. Verify square corners (90°)                     │  │
    │   │                                                      │  │
    │   │   Use M4 × 10mm bolts, tighten to 3 N·m             │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   8.2 INSTALL INSULATION:                                  │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Cut aerogel blanket to fit inner walls          │  │
    │   │   2. Leave 20mm clearance for coil mounting          │  │
    │   │   3. Attach with high-temp adhesive (RTV silicone)   │  │
    │   │   4. Ensure no gaps in insulation                    │  │
    │   │                                                      │  │
    │   │   ⚠️  Aerogel is fragile — handle gently!           │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 9: Wind Coils

```
    COIL WINDING (Critical Step!)
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   ⚠️  THIS STEP REQUIRES PRECISION! ⚠️                     │
    │                                                             │
    │   9.1 COIL WINDING PROCEDURE:                              │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   WINDING JIG:                                       │  │
    │   │                                                      │  │
    │   │   ┌─────────────────────────────────────────────┐   │  │
    │   │   │                                              │   │  │
    │   │   │   ┌──────────────────────────────────────┐  │   │  │
    │   │   │   │         WINDING FORM                  │  │   │  │
    │   │   │   │                                      │  │   │  │
    │   │   │   │   ┌──────────────────────────────┐  │  │   │  │
    │   │   │   │   │                              │  │  │   │  │
    │   │   │   │   │      200mm diameter          │  │  │   │  │
    │   │   │   │   │                              │  │  │   │  │
    │   │   │   │   └──────────────────────────────┘  │  │   │  │
    │   │   │   │                                      │  │   │  │
    │   │   │   └──────────────────────────────────────┘  │   │  │
    │   │   │                                              │   │  │
    │   │   │   Material: PVC pipe or 3D printed form      │   │  │
    │   │   │   Surface: Smooth, release agent applied     │   │  │
    │   │   │                                              │   │  │
    │   │   └─────────────────────────────────────────────┘   │  │
    │   │                                                      │  │
    │   │   WINDING STEPS:                                     │  │
    │   │                                                      │  │
    │   │   1. Secure wire end to form with tape              │  │
    │   │   2. Wind first layer: 120 turns, tight             │  │
    │   │      - Keep tension consistent                      │  │
    │   │      - No gaps between turns                        │  │
    │   │      - No overlapping                               │  │
    │   │   3. Apply Kapton tape over first layer             │  │
    │   │   4. Wind second layer (if needed for inductance)   │  │
    │   │   5. Secure end with tape                           │  │
    │   │   6. Test inductance (should be 47μH ±5%)          │  │
    │   │   7. Repeat for all 5 coils                         │  │
    │   │                                                      │  │
    │   │   Quality checks:                                    │  │
    │   │   □ No damaged insulation                            │  │
    │   │   □ Consistent winding tension                       │  │
    │   │   □ Correct number of turns                         │  │
    │   │   □ Inductance within spec                          │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 10: Test Coil Inductance

```
    COIL TESTING
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   10.1 INDUCTANCE TEST:                                    │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   Equipment: LCR meter or oscilloscope + function   │  │
    │   │              generator                               │  │
    │   │                                                      │  │
    │   │   Method 1 (LCR meter):                             │  │
    │   │   1. Connect coil to LCR meter                       │  │
    │   │   2. Set frequency to 1 kHz                          │  │
    │   │   3. Read inductance value                           │  │
    │   │   4. Expected: 47μH ± 5% (44.65 - 49.35 μH)        │  │
    │   │                                                      │  │
    │   │   Method 2 (Oscilloscope):                          │  │
    │   │   1. Build LC tank circuit with known capacitor      │  │
    │   │   2. Measure resonant frequency                      │  │
    │   │   3. Calculate: L = 1/(4π²f²C)                       │  │
    │   │   4. Verify result matches expected inductance       │  │
    │   │                                                      │  │
    │   │   If inductance is wrong:                            │  │
    │   │   - Too high: Remove turns                           │  │
    │   │   - Too low: Add turns                               │  │
    │   │   - Unstable: Check for shorted turns                │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   10.2 RESISTANCE TEST:                                    │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Measure DC resistance of each coil              │  │
    │   │   2. Expected: 2.5Ω ± 0.2Ω                          │  │
    │   │   3. All coils should match within 5%                │  │
    │   │                                                      │  │
    │   │   If resistance is wrong:                            │  │
    │   │   - Too high: Check for poor connections             │  │
    │   │   - Too low: Check for shorted turns                 │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 11: Mount Coils

```
    COIL MOUNTING
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   11.1 COIL POSITIONS (FPB-10):                            │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   Top view (looking down into casing):              │  │
    │   │                                                      │  │
    │   │                    Coil 1 (0°)                       │  │
    │   │                        │                             │  │
    │   │                  ┌─────┴─────┐                       │  │
    │   │                  │           │                       │  │
    │   │             ┌────┤           ├────┐                  │  │
    │   │             │    │           │    │                  │  │
    │   │        ┌────┤    │     ●     │    ├────┐             │  │
    │   │        │    │    │   CENTER  │    │    │             │  │
    │   │   ┌────┤    │    │           │    │    ├────┐        │  │
    │   │   │    │    │    │           │    │    │    │        │  │
    │   │   │    │    │    │           │    │    │    │        │  │
    │   │Coil 5   │    │    │           │    │    │  Coil 2    │  │
    │   │(272°)   │    │    │           │    │    │ (137.5°)  │  │
    │   │   │    │    │    │           │    │    │    │        │  │
    │   │   │    │    │    │           │    │    │    │        │  │
    │   │   └────┤    │    │           │    │    ├────┘        │  │
    │   │        │    │    │           │    │    │             │  │
    │   │        └────┤    │           │    ├────┘             │  │
    │   │             │    │           │    │                  │  │
    │   │             └────┤           ├────┘                  │  │
    │   │                  │           │                       │  │
    │   │                  └─────┬─────┘                       │  │
    │   │                        │                             │  │
    │   │                    Coil 4 (225°)   Coil 3 (72.5°)   │  │
    │   │                                                      │  │
    │   │   All coils equidistant from center: 100mm           │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   11.2 MOUNTING PROCEDURE:                                 │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Cut G10 fiberglass mounting plate               │  │
    │   │   2. Mark coil positions using angle measurements    │  │
    │   │   3. Drill mounting holes for each coil              │  │
    │   │   4. Install vibration dampers (silicone pads)       │  │
    │   │   5. Place coils on dampers                          │  │
    │   │   6. Secure with M4 bolts (hand-tight only!)        │  │
    │   │   7. Verify coil alignment (use protractor)         │  │
    │   │   8. Route coil wires to electronics bay            │  │
    │   │                                                      │  │
    │   │   ⚠️  Do NOT overtighten bolts — will crack G10!   │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### STEP 12: Wire Coil Array

```
    COIL ARRAY WIRING
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   12.1 WIRING SCHEMATIC:                                   │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   48V BUS ──┬──┬──┬──┬──┬──                         │  │
    │   │             │  │  │  │  │                            │  │
    │   │             ▼  ▼  ▼  ▼  ▼                           │  │
    │   │           ┌──┐┌──┐┌──┐┌──┐┌──┐                      │  │
    │   │           │Q1││Q2││Q3││Q4││Q5│  MOSFETs             │  │
    │   │           └┬─┘└┬─┘└┬─┘└┬─┘└┬─┘                      │  │
    │   │            │   │   │   │   │                         │  │
    │   │            ▼   ▼   ▼   ▼   ▼                        │  │
    │   │          ┌──┐┌──┐┌──┐┌──┐┌──┐                       │  │
    │   │          │C1││C2││C3││C4││C5│  Coils                │  │
    │   │          └┬─┘└┬─┘└┬─┘└┬─┘└┬─┘                       │  │
    │   │           │   │   │   │   │                          │  │
    │   │           └───┴───┴───┴───┘                          │  │
    │   │                    │                                  │  │
    │   │                   GND                                 │  │
    │   │                                                      │  │
    │   │   MCU PWM → Gate resistors → MOSFET gates            │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    │   12.2 WIRING PROCEDURE:                                   │
    │                                                             │
    │   ┌─────────────────────────────────────────────────────┐  │
    │   │                                                      │  │
    │   │   1. Route coil wires along mounting plate edges     │  │
    │   │   2. Keep power wires away from signal wires         │  │
    │   │   3. Use cable ties every 50mm                       │  │
    │   │   4. Solder connections with heat shrink tubing      │  │
    │   │   5. Test continuity of each connection              │  │
    │   │   6. Label all wires clearly                         │  │
    │   │                                                      │  │
    │   │   Wire colors:                                       │  │
    │   │   - Red: 48V power                                   │  │
    │   │   - Black: GND                                       │  │
    │   │   - Yellow: PWM signal (Coil 1)                      │  │
    │   │   - Orange: PWM signal (Coil 2)                      │  │
    │   │   - Green: PWM signal (Coil 3)                       │  │
    │   │   - Blue: PWM signal (Coil 4)                        │  │
    │   │   - Purple: PWM signal (Coil 5)                      │  │
    │   │                                                      │  │
    │   └─────────────────────────────────────────────────────┘  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

### 5. Electronics Assembly (Steps 13-16)

```
    ELECTRONICS ASSEMBLY SUMMARY
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   STEP 13: Build control board                              │
    │   - Mount STM32F407 on perfboard                           │
    │   - Add pull-up resistors for I2C                          │
    │   - Add decoupling capacitors (100nF, 10μF)                │
    │   - Wire MOSFET drivers                                    │
    │   - Test all connections                                   │
    │                                                             │
    │   STEP 14: Build power board                                │
    │   - Mount DC-DC converter                                   │
    │   - Add input/output capacitors                             │
    │   - Wire current sense resistor                             │
    │   - Add TVS diodes for protection                          │
    │   - Test output voltage and current                        │
    │                                                             │
    │   STEP 15: Build monitoring board                           │
    │   - Mount INA219 current sensor                            │
    │   - Wire temperature sensors                               │
    │   - Wire pressure sensor                                   │
    │   - Wire plasma density sensor                             │
    │   - Test all sensor readings                               │
    │                                                             │
    │   STEP 16: Wire all boards together                        │
    │   - Connect power board to control board                   │
    │   - Connect monitoring board to control board              │
    │   - Connect coil array to power board                      │
    │   - Connect harvesting inputs to power board               │
    │   - Connect output connector to power board                │
    │   - Final continuity test                                  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

### 6. Integration (Steps 17-20)

```
    INTEGRATION SUMMARY
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   STEP 17: Install electronics                              │
    │   - Place control board in electronics bay                 │
    │   - Secure with M3 bolts                                   │
    │   - Route wires neatly                                     │
    │   - Connect all cables                                     │
    │                                                             │
    │   STEP 18: Connect all wiring                              │
    │   - Power connections                                       │
    │   - Signal connections                                     │
    │   - Sensor connections                                     │
    │   - Output connections                                     │
    │   - Double-check all connections                           │
    │                                                             │
    │   STEP 19: Final inspection                                 │
    │   - Visual inspection of all solder joints                 │
    │   - Continuity test of all power paths                     │
    │   - Insulation resistance test (>1MΩ)                      │
    │   - No loose wires or components                           │
    │   - All bolts tightened                                    │
    │                                                             │
    │   STEP 20: Gas fill and seal                                │
    │   - Connect vacuum pump to gas fill port                   │
    │   - Evacuate to 10⁻³ Torr (wait 30 minutes)               │
    │   - Close vacuum valve                                     │
    │   - Connect H₂/He gas cylinders                            │
    │   - Fill to 0.5 Torr                                       │
    │   - Close gas fill valve                                   │
    │   - Apply thread sealant to all fittings                   │
    │   - Verify pressure stability (24 hours)                   │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

### 7. Testing (Steps 21-24)

```
    TESTING SUMMARY
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   STEP 21: Power-on test                                    │
    │   - Connect 48V power supply                                │
    │   - Verify MCU boots correctly                              │
    │   - Check all sensor readings                               │
    │   - Verify status LED turns on                             │
    │   - Monitor current draw (should be <500mA idle)           │
    │                                                             │
    │   STEP 22: Containment test                                 │
    │   - Enable coil array                                       │
    │   - Verify all 5 coils are energized                       │
    │   - Check coil currents (should match spec)                │
    │   - Monitor plasma density sensor                           │
    │   - Verify containment field is stable                     │
    │                                                             │
    │   STEP 23: Safety test                                      │
    │   - Test overcurrent protection (trip at 250A)             │
    │   - Test overvoltage protection (clamp at 62V)             │
    │   - Test temperature protection (shutdown at 80°C)         │
    │   - Test pressure relief valve (opens at 2.0 Torr)         │
    │   - Verify fault relay activates                            │
    │                                                             │
    │   STEP 24: Performance test                                 │
    │   - Measure energy storage capacity                         │
    │   - Measure charge/discharge efficiency                     │
    │   - Measure self-charging rate                              │
    │   - Measure temperature rise during operation               │
    │   - Verify all specs are met                                │
    │                                                             │
    │   ⚠️  If ANY test fails, do NOT use the battery!          │
    │      Return to troubleshooting and fix the issue.          │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

### 8. Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Coil inductance wrong | Incorrect number of turns | Rewind coil with correct turns |
| Plasma won't ignite | Low gas pressure | Check for leaks, refill gas |
| High temperature | Poor thermal management | Improve insulation, add cooling |
| Noise from coils | Loose mounting | Tighten bolts, add dampers |
| Low efficiency | Poor coil alignment | Realign coils to correct angles |
| No self-charging | Harvesting not connected | Check wiring to harvesting systems |
| MCU not booting | Power supply issue | Check 3.3V regulator, decoupling |
| Sensor readings wrong | Bad connections | Check wiring, reflow solder joints |

---

*Document Version: 1.0*
*Created: 2026-08-27*
*Author: Battery Agent 1 of 27*
*Project: PHI_FIELD_PLASMA_BATTERY*
