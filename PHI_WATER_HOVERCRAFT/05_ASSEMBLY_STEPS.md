# PHI_WATER_HOVERCRAFT — Assembly Steps

> **Skill Level**: Intermediate (12-year-old can do it with adult supervision)
> **Time**: 10-12 hours over 2 days
> **Tools Needed**: Drill, screwdrivers, wire strippers, soldering iron, scissors, multimeter, measuring tape

---

## Phase 1: Build the Frame (2 hours)

### Step 1: Cut Aluminum Tubes

1. Cut 4× aluminum square tubes to 1200mm (length)
2. Cut 4× aluminum square tubes to 800mm (width)
3. Cut 4× aluminum angle to 200mm (corner braces)
4. Sand all cut edges smooth

### Step 2: Assemble the Frame

1. Lay out 2 long tubes (1200mm) parallel, 800mm apart
2. Place 2 short tubes (800mm) perpendicular at ends
3. Join corners using aluminum angles and M6 bolts
4. Tighten all bolts evenly
5. Add cross braces at 400mm intervals
6. Verify frame is square (diagonals equal)

### Step 3: Install Foam Blocks

1. Place 8 closed-cell foam blocks under frame
2. Space evenly for buoyancy and vibration dampening
3. Zip-tie foam blocks to frame rails

---

## Phase 2: Build the Platform (1.5 hours)

### Step 4: Cut and Prepare Deck

1. Cut marine plywood to 1200mm × 800mm
2. Sand edges smooth
3. Drill mounting holes for frame bolts
4. Apply marine-grade varnish or sealant (2 coats)
5. Let dry completely

### Step 5: Cut Fan Opening

1. Mark center of platform (600mm × 400mm from corner)
2. Trace 260mm circle for fan opening
3. Cut with jigsaw
4. Sand edges smooth
5. Reinforce edges with aluminum angle

### Step 6: Mount Platform to Frame

1. Place platform on frame
2. Align mounting holes
3. Insert M6 bolts from top
4. Thread T-nuts from below
5. Tighten evenly

---

## Phase 3: Build the Lift System (2 hours)

### Step 7: Build the Phi-Harmonic Port Ring

1. Take PVC pipe (50mm diameter, 1.5m)
2. Cut into 8 segments of 200mm each
3. Arrange in a ring at golden-angle positions:
   - Port 1: 0° (front)
   - Port 2: 137.5° (front-right)
   - Port 3: 275° (rear-right)
   - Port 4: 52.5° (rear center)
   - Port 5: 190° (rear-left)
   - Port 6: 327.5° (front-left)
   - Port 7: 105° (left side)
   - Port 8: 242.5° (right side)
4. Join segments to form a ring (use PVC cement or 3D-printed connectors)
5. Verify 8 ports are evenly distributed at golden angles

### Step 8: Mount the Lift Motor and Fan

1. Mount 800W BLDC motor below platform, centered on fan opening
2. Attach centrifugal fan to motor shaft with coupler
3. Install fan shroud around fan (directs airflow)
4. Connect air ducting from shroud to port ring
5. Secure all connections with hose clamps

### Step 9: Inflate and Test Skirt

1. Cut nylon fabric to skirt pattern (see 03_MECHANICAL_DIAGRAM)
2. Sew or glue skirt panels together
3. Attach skirt to platform edge with clips
4. Connect inflatable tube to skirt base
5. Inflate tube with bicycle pump
6. Verify skirt inflates evenly around all 8 ports

---

## Phase 4: Build the Thrust System (1.5 hours)

### Step 10: Mount Thrust Motor

1. Build motor mount from aluminum angle
2. Mount 500W BLDC motor at rear of platform
3. Align motor shaft with propeller direction
4. Install thrust bearing between motor and mount
5. Secure motor with bolts and threadlocker

### Step 11: Install Propeller

1. Attach folding propeller to motor shaft
2. Install propeller guard (wire cage)
3. Verify propeller spins freely
4. Check guard clearance (minimum 25mm from blade tips)

### Step 12: Build Rudder

1. Cut aluminum plate to 200mm × 150mm
2. Drill pivot hole at top center
3. Mount rudder on pivot behind propeller
4. Connect rudder to foot pedals via cables
5. Test steering response

---

## Phase 5: Build the Battery Pack (1.5 hours)

### Step 13: Assemble Battery Cells

1. Take 16 LiFePO4 26650 cells (3.2V 15Ah each)
2. Arrange in 16S configuration (16 in series)
3. Use nickel strips and spot welder:
   - Cell 1 (+) → Cell 2 (-) → ... → Cell 16 (-)
   - **Do NOT use regular solder** — use nickel strips
4. Connect BMS board:
   - BMS B- → Cell 1 (-)
   - BMS B1-B16 → between each cell pair
   - BMS B+ → Cell 16 (+)
5. Connect XT90 connector:
   - XT90 Red (+) → BMS P+
   - XT90 Black (-) → BMS P-

### Step 14: Test and Enclose Battery

1. Verify total voltage: **48V** (16 × 3.0V nominal)
2. Check each balance lead: 3.0-3.3V per cell
3. Place battery in waterproof ABS enclosure
4. Add foam padding on all sides
5. Seal enclosure with silicone
6. Mount enclosure on platform with zip ties

---

## Phase 6: Wire Everything (1.5 hours)

### Step 15: Wire the ESCs

1. Mount lift ESC on platform (foam padding + zip ties)
2. Mount thrust ESC nearby
3. Connect battery to both ESCs:
   - ESC BATTERY+ → XT90 Red (+)
   - ESC BATTERY- → XT90 Black (-)
4. Connect motors:
   - Lift ESC → Lift Motor (3 phase wires)
   - Thrust ESC → Thrust Motor (3 phase wires)
5. Connect hall sensors for both motors
6. Wire throttle to both ESCs (parallel signal)

### Step 16: Install Controls

1. Mount throttle lever on right side of platform
2. Mount foot pedals for rudder control
3. Connect rudder cables to pedals
4. Install power switch on dashboard area
5. Install fuse holder near battery

### Step 17: Cable Management

1. Secure all wires along frame with zip ties
2. Ensure no wires near fan, propeller, or moving parts
3. Use waterproof connectors where possible
4. Leave service loops for maintenance

---

## Phase 7: Final Testing (30 minutes)

### Step 18: Water Test

1. **Wear life jacket**
2. Find calm, shallow water (knee-deep)
3. Place hovercraft in water
4. Turn on power switch
5. Engage lift motor slowly — skirt should inflate
6. Verify craft lifts off water (50-100mm)
7. Engage thrust motor slowly
8. Test rudder steering
9. Practice for 15 minutes before open water

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Skirt won't inflate | Check lift motor direction, fan orientation |
| Craft won't lift | Increase throttle, check skirt for leaks |
| Wobble/unstable | Check port ring alignment, skirt symmetry |
| Motor overheats | Reduce throttle, check air cooling |
| Propeller vibration | Balance propeller, check motor mount |
| Rudder not responding | Check cable tension, pivot lubrication |
| Battery drains fast | Check for shorts, reduce thrust |
