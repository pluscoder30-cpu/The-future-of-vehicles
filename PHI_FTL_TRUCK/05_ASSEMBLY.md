# PHI FTL TRUCK — ASSEMBLY GUIDE

## Step-by-Step Build Instructions

---

## PHASE 1: CHASSIS ASSEMBLY (40-60 hours)

### Step 1: Frame Preparation
```
1. Lay steel ladder frame on flat surface
2. Verify all cross members at φ-spaced intervals (618mm)
3. Weld cross members to main rails
4. Grind welds smooth
5. Apply rust-preventive coating
```

### Step 2: Suspension Mounting
```
1. Install front double-wishbone mounting points
2. Install rear leaf spring hangers
3. Mount front coilovers (phi-tuned to 35 N/mm)
4. Mount rear leaf springs (7-leaf packs)
5. Install anti-roll bars (φ ratio: 32mm front, 20mm rear)
```

### Step 3: Axle Installation
```
1. Install front steering knuckles
2. Mount rear axle housing
3. Install differential (phi-ratio gear set: 3.732:1)
4. Connect axle shafts
5. Verify alignment
```

---

## PHASE 2: FPB-80 BATTERY INSTALLATION (20-30 hours)

### Step 4: Battery Mount
```
1. Install battery cradle under cab floor
2. Secure with 8× M16 bolts (phi-spaced pattern)
3. Verify clearance to frame: 150mm minimum
4. Install thermal insulation mat
5. Route battery cables through frame rails
```

### Step 5: Battery Connection
```
1. Mount FPB-80 in cradle
2. Connect HV main cables (50mm² orange)
3. Install HV contactor (400A)
4. Connect BMS CAN bus
5. Verify all connections with multimeter
6. DO NOT ENERGIZE until Phase 4 complete
```

---

## PHASE 3: WARP FIELD SYSTEM (30-40 hours)

### Step 6: Warp Coil Installation
```
1. Mount 6 warp coils in phi-hexagonal pattern
   ┌───────────────────────────────┐
   │         ╱  ╲                  │
   │        ╱ C1 ╲  C2            │
   │       ╱      ╲               │
   │   C6 │   ●    │ C3           │
   │       ╲      ╱               │
   │        ╲ C5 ╱  C4            │
   │         ╲  ╱                  │
   └───────────────────────────────┘
   
2. Each coil: 432μH, rated 200A peak
3. Connect coil drivers to warp controller
4. Install field emitter nodes (8× around perimeter)
5. Mount resonance stabilizer
```

### Step 7: Dimensional Tuner
```
1. Install 7-band frequency selector
2. Mount dimensional HUD display in cab
3. Connect tuner to warp controller
4. Calibrate each dimension frequency
5. Test lock-on to D0 (home dimension)
```

---

## PHASE 4: CABIN & INTERIOR (20-30 hours)

### Step 8: Cab Assembly
```
1. Mount cab onto frame
2. Install windshield and side windows
3. Mount steering column and wheel
4. Install pedal assembly
5. Mount driver and co-pilot seats
6. Route all wiring through firewall
```

### Step 9: Dashboard & Controls
```
1. Install custom dashboard
2. Mount 10" touchscreen display
3. Install dimensional navigation controls
4. Wire CAN bus connections
5. Test all displays
```

---

## PHASE 5: CARGO BED (15-20 hours)

### Step 10: Bed Assembly
```
1. Install cargo bed subframe
2. Mount 4mm steel floor
3. Attach 3mm aluminum side walls
4. Install hydraulic rear gate
5. Add tie-down points (12×)
6. Install cargo lights
```

---

## PHASE 6: ELECTRICAL & FINAL (20-30 hours)

### Step 11: Wiring
```
1. Install DC-DC converter
2. Mount auxiliary battery
3. Wire all 12V circuits
4. Install fuse box (10 circuits)
5. Connect CAN bus network
6. Ground all components to chassis
```

### Step 12: Final Assembly
```
1. Install HVAC system
2. Mount exterior mirrors
3. Add protective coatings
4. Install all body panels
5. Final inspection
```

---

## ASSEMBLY TOOLS REQUIRED

| Tool | Purpose |
|------|---------|
| MIG welder | Frame welding |
| Torque wrench | Bolt tightening |
| Multimeter | Electrical testing |
| Oscilloscope | Warp coil calibration |
| Frequency analyzer | Resonance tuning |
| Hoist/engine lift | Heavy component handling |
| Alignment rack | Suspension setup |

---

## PHI-HARMONIC ASSEMBLY NOTES

```
CROSS-MEMBER SPACING:
══════════════════════════════════════════════════════════════

  Frame cross-members are placed at φ-ratio intervals:

  Position 0:    0 mm
  Position 1:    618 mm  (φ × 1000)
  Position 2:    1236 mm (φ² × 1000)
  Position 3:    1854 mm (φ³ × 1000)
  Position 4:    2472 mm (φ⁴ × 1000)
  Position 5:    3090 mm (φ⁵ × 1000)
  Position 6:    3708 mm (φ⁶ × 1000)

  This ensures the frame naturally resonates at 432 Hz,
  eliminating vibration during FTL travel.
```
