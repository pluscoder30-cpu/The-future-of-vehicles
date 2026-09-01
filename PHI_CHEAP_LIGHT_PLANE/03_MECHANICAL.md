# PHI CHEAP LIGHT PLANE — MECHANICAL

## Frame Design, Dimensions, and Structural Specifications

---

## AIRFRAME OVERVIEW

The PHI Cheap Light Plane uses a conventional tube-and-fabric ultralight design with spruce wood longerons, pine ribs, and Dacron fabric covering. The airframe is designed for simplicity, light weight, and low cost while meeting FAA Part 103 weight requirements.

**Design Philosophy:**
- Simple bolted construction (no welding required)
- Standard lumber yard materials
- Conventional ultralight aerodynamics
- 25% structural margin on all members
- Weight budget: 115 kg empty (Part 103 limit)

---

## PRIMARY STRUCTURE — FUSELAGE

### Fuselage Dimensions

```
                    FUSELAGE CROSS-SECTION (at cockpit)
                    ┌─────────────────────┐
                    │                     │  ← Top longeron (1×4 spruce)
                    │    600mm            │
                    │    (23.6")          │
                    │                     │
     ┌──────────────┤                     ├──────────────┐
     │              │                     │              │
     │   600mm      │                     │              │
     │   (23.6")    │                     │              │
     │              │                     │              │
     └──────────────┤                     ├──────────────┘
                    │                     │  ← Bottom longeron (1×4 spruce)
                    └─────────────────────┘
                    │←─────── 600mm ──────→│
                         (23.6 inches)

     WOOD SIZES:
     - Top/Bottom longerons: 1×4" Sitka Spruce (89mm × 38mm)
     - Side longerons: 1×3" Pine (64mm × 19mm)
     - Formers: 1×3" Pine, cut to shape
     - Gussets: 1/4" Baltic Birch plywood
```

### Fuselage Side View

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FUSELAGE — SIDE VIEW                                  │
│                                                                          │
│  MOTOR     COCKPIT              BATTERY           AVIONICS    TAIL      │
│  MOUNT     AREA                 COMPARTMENT       BAY                   │
│                                                                          │
│  ┌───┐  ┌─────────────────┬──────────────────┬──────────────┬───┐      │
│  │   │  │                 │                  │              │   │      │
│  │ M │  │   ┌─────────┐  │   ┌──────────┐  │  ┌────────┐ │   │      │
│  │ O │  │   │  PILOT  │  │   │  4× FPB-20  │  │  │AVIONICS│ │   │      │
│  │ T │  │   │  SEAT   │  │   │ BATTERIES│  │  │  BAY   │ │   │      │
│  │ O │  │   │  Canvas │  │   │  40 kWh  │  │  │Arduino │ │   │      │
│  │ R │  │   │  sling  │  │   │  behind  │  │  │ + sensors│ │   │      │
│  │   │  │   └─────────┘  │   └──────────┘  │  └────────┘ │   │      │
│  │   │  │                 │                  │              │   │      │
│  └───┘  └─────────────────┴──────────────────┴──────────────┴───┘      │
│                                                                          │
│  │←1.0m→│←──── 2.0m ────→│←──── 1.5m ────→│←── 1.5m ──→│←0.5m→│      │
│                                                                          │
│  │←─────────────────── 6.0m total length ──────────────────────→│      │
│                                                                          │
│  STRUCTURAL MEMBERS:                                                     │
│  - Top longerons: 2× 1×4" Sitka Spruce, full 6m length                │
│  - Bottom longerons: 2× 1×4" Sitka Spruce, full 6m length             │
│  - Side longerons: 2× 1×3" Pine, full 6m length                       │
│  - Formers: 1×3" Pine, every 400mm (16 formers total)                 │
│  - Gussets: 1/4" Baltic Birch plywood, at every junction               │
│                                                                          │
│  LONGERON SPLICE DETAIL:                                                 │
│  - Spruce boards are 8ft (2.44m) long                                   │
│  - Splices at 2.4m and 4.8m marks                                      │
│  - Splice: 300mm overlap, 4× AN3 bolts, 2× plywood gussets            │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### Fuselage Top View

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FUSELAGE — TOP VIEW                                   │
│                                                                          │
│                              ┌───────┐                                   │
│                              │MOTOR  │                                   │
│                              │MOUNT  │                                   │
│                              └───┬───┘                                   │
│                     ┌────────────┼────────────┐                         │
│                     │            │            │                         │
│  ┌──────────────────┤  ┌─────────▼─────────┐  ├──────────────────┐     │
│  │                  │  │                   │  │                  │     │
│  │   LEFT WING      │  │    FUSELAGE       │  │   RIGHT WING     │     │
│  │   SPAR BOX       │  │    600mm wide     │  │   SPAR BOX       │     │
│  │                  │  │                   │  │                  │     │
│  │   1×4 spruce     │  │   1×4 spruce top  │  │   1×4 spruce     │     │
│  │   1×4 spruce     │  │   1×4 spruce bot  │  │   1×4 spruce     │     │
│  │                  │  │                   │  │                  │     │
│  └──────────────────┤  └───────────────────┘  ├──────────────────┘     │
│                     │            │            │                         │
│                     └────────────┼────────────┘                         │
│                              ┌───┴───┐                                   │
│                              │ TAIL  │                                   │
│                              │ POST  │                                   │
│                              │ 1×4   │                                   │
│                              │ spruce│                                   │
│                              └───────┘                                   │
│                                                                          │
│  │←────────────── 10.0m wingspan ──────────────────→│                  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## PRIMARY STRUCTURE — WINGS

### Wing Planform

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    WING — TOP VIEW (unfolded)                            │
│                                                                          │
│                              ┌───────┐                                   │
│                              │FUSELAGE│                                  │
│                              │(root)  │                                  │
│                              └───┬───┘                                   │
│               ┌──────────────────┼──────────────────┐                   │
│               │                  │                  │                   │
│  LEFT WING    │                  │                  │   RIGHT WING      │
│  5000mm       │                  │                  │   5000mm          │
│               │                  │                  │                   │
│  ┌────────────┤                  │                  ├────────────┐     │
│  │            │    SPAR (1×4 spruce)                │            │     │
│  │  ┌─────────┤══════════════════╪══════════════════├─────────┐  │     │
│  │  │         │                  │                  │         │  │     │
│  │  │  RIBS   │    RIBS (1/2×1 spruce)             │  RIBS   │  │     │
│  │  │  every  │    every 400mm                       │  every  │  │     │
│  │  │  400mm  │                  │                  │  400mm  │  │     │
│  │  │         │                  │                  │         │  │     │
│  │  └─────────┤                  │                  ├─────────┘  │     │
│  │            │                  │                  │            │     │
│  │  TRAILING  │                  │                  │  TRAILING  │     │
│  │  EDGE      │    Dacron fabric │                  │  EDGE      │     │
│  │  (strip)   │    covering      │                  │  (strip)   │     │
│  │            │                  │                  │            │     │
│  └────────────┤                  │                  ├────────────┘     │
│               │                  │                  │                   │
│               └──────────────────┼──────────────────┘                   │
│                                  │                                       │
│               │←──────────── 5000mm ────────────→│                     │
│                                  │                                       │
│               │←──────────────── 10000mm total wingspan ──────────────→│
│                                                                          │
│  WING SPECIFICATIONS:                                                    │
│  - Span: 10,000mm (32.8 ft)                                             │
│  - Chord (root): 800mm (31.5")                                          │
│  - Chord (tip): 494mm (19.4") — φ taper ratio                          │
│  - Area: 15.0 m² (161.4 sq ft)                                          │
│  - Aspect ratio: 6.67                                                    │
│  - Airfoil: Clark Y (flat bottom, easy to build)                       │
│  - Sweep: 0° (straight wing)                                            │
│  - Dihedral: 3° (stability)                                             │
│  - Washout: 2° (tip incidence reduction)                                │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### Wing Cross-Section (Clark Y Airfoil)

```
                    CLARK Y AIRFOIL — WING CROSS-SECTION
                    ─────────────────────────────────────

                    Leading Edge
                         │
                         ▼
                    ┌─────────────────────────────────────────┐
                    │  ┌─────────────────────────────────────┐│
                    │  │     CLARK Y AIRFOIL PROFILE         ││
                    │  │                                     ││
                    │  │  Max thickness: 11.7% at 30% chord  ││
                    │  │  Max camber: 3.5% at 40% chord      ││
                    │  │                                     ││
                    │  │  ┌─────────────────────────────┐   ││
                    │  │  │                             │   ││
                    │  │  │  ┌───┐    SPAR BOX          │   ││
                    │  │  │  │   │    (1×4 spruce)      │   ││
                    │  │  │  │ S │    89mm × 38mm        │   ││
                    │  │  │  │ P │                       │   ││
                    │  │  │  │ A │    Located at 30%     │   ││
                    │  │  │  │ R │    chord (max thick)  │   ││
                    │  │  │  │   │                       │   ││
                    │  │  │  └───┘                       │   ││
                    │  │  │                             │   ││
                    │  │  │  ┌───┐                      │   ││
                    │  │  │  │RIB│  1/2×1 spruce        │   ││
                    │  │  │  │   │  every 400mm         │   ││
                    │  │  │  └───┘                      │   ││
                    │  │  │                             │   ││
                    │  │  └─────────────────────────────┘   ││
                    │  │                                     ││
                    │  │  Dacron fabric stretched over       ││
                    │  │  ribs, sewn to trailing edge        ││
                    │  │                                     ││
                    │  └─────────────────────────────────────┘│
                    └─────────────────────────────────────────┘
                    │←──────────── 800mm chord ─────────────→│
                    (root chord — tip chord is 494mm)

                    TRAILING EDGE: 1/4" × 1/4" pine strip
                    LEADING EDGE: 1" × 1" balsa block, sanded to radius
                    RIBS: 1/2" × 1" spruce strip, cut to airfoil shape
```

### Wing Rib Template

```
┌─────────────────────────────────────────────────────────────────┐
│                    WING RIB — CLARK Y PROFILE                    │
│                                                                  │
│                    ┌───────────────────────────────────┐        │
│                    │          LEADING EDGE              │        │
│                    │     (1"×1" balsa, sanded)         │        │
│                    │              ┌───┐                 │        │
│                    │             ╱     ╲                │        │
│                    │           ╱         ╲              │        │
│                    │         ╱     SPAR    ╲            │        │
│                    │       ╱    ┌───────┐    ╲          │        │
│                    │     ╱      │ 1×4   │      ╲        │        │
│                    │   ╱        │SPRUCE │        ╲      │        │
│                    │ ╱          │       │          ╲    │        │
│                    │╱           └───────┘           ╲   │        │
│                    │                                 ╲  │        │
│                    │                                  ╲ │        │
│                    │                                   ╲│        │
│                    │                              TRAILING      │
│                    │                              EDGE          │
│                    │                           (1/4"×1/4")      │
│                    └───────────────────────────────────┘        │
│                    │←────────── 800mm ──────────────→│         │
│                                                                  │
│  RIB FABRICATION:                                                │
│  1. Draw Clark Y profile on 1/2" plywood template               │
│  2. Cut template with jigsaw                                     │
│  3. Trace profile onto 1/2"×1" spruce strips                    │
│  4. Cut ribs with band saw or coping saw                         │
│  5. Sand to smooth airfoil shape                                 │
│  6. Cut spar notch at 30% chord (89mm wide)                     │
│  7. Notch for trailing edge strip                                │
│  8. Total ribs needed: 26 (13 per wing)                         │
│                                                                  │
│  RIB SPACING:                                                    │
│  - Root section: 400mm spacing (closer for load)                │
│  - Mid section: 400mm spacing                                   │
│  - Tip section: 400mm spacing                                   │
│  - 13 ribs per wing × 2 wings = 26 total                        │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## TAIL SURFACES

### Horizontal Stabilizer

```
┌─────────────────────────────────────────────────────────────────┐
│                    HORIZONTAL STABILIZER — TOP VIEW              │
│                                                                  │
│                    ┌───────────────────────┐                    │
│                    │      FUSELAGE         │                    │
│                    │      (tail post)      │                    │
│                    └───────────┬───────────┘                    │
│               ┌────────────────┼────────────────┐               │
│               │                │                │               │
│  ┌────────────┤    SPAR (1×2 spruce)           ├────────────┐  │
│  │            │═════════════════╪═══════════════│            │  │
│  │  ┌─────────┤                │                ├─────────┐  │  │
│  │  │  RIBS   │    RIBS (1/4×1 spruce)         │  RIBS   │  │  │
│  │  │  every  │    every 300mm                  │  every  │  │  │
│  │  │  300mm  │                │                │  300mm  │  │  │
│  │  └─────────┤                │                ├─────────┘  │  │
│  │            │                │                │            │  │
│  │  TRAILING  │    Dacron      │                │  TRAILING  │  │
│  │  EDGE      │    fabric      │                │  EDGE      │  │
│  │            │                │                │            │  │
│  └────────────┤                │                ├────────────┘  │
│               │                │                │               │
│               └────────────────┼────────────────┘               │
│                                │                                 │
│               │←────────── 2000mm ──────────→│                 │
│                                │                                 │
│  ELEVATOR (in trailing edge):                                  │
│  - Hinge line at 75% chord                                    │
│  - Deflection: ±25°                                          │
│  - Control: cable to cockpit pushrod                          │
│  - Area: 2.5 m² (26.9 sq ft)                                  │
│  - φ ratio: H-stab area / V-stab area = 1.618                 │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

### Vertical Stabilizer

```
┌─────────────────────────────────────────────────────────────────┐
│                    VERTICAL STABILIZER — SIDE VIEW               │
│                                                                  │
│                    ┌───────────┐                                 │
│                    │  FUSELAGE │                                 │
│                    │  (tail)   │                                 │
│                    └─────┬─────┘                                 │
│                    ┌─────┴─────┐                                 │
│                    │   SPAR    │  (1×2 spruce)                  │
│                    │═══════════│                                  │
│                    │   RIBS    │  (1/4×1 spruce, every 200mm)   │
│                    │           │                                  │
│                    │   Dacron  │                                  │
│                    │   fabric  │                                  │
│                    │           │                                  │
│                    │   TRAILING│                                  │
│                    │   EDGE    │                                  │
│                    │           │                                  │
│                    └─────┬─────┘                                 │
│                          │                                       │
│                    ┌─────┴─────┐                                 │
│                    │   RUDDER  │                                 │
│                    │  (in trail│                                 │
│                    │   ing edge│                                 │
│                    └───────────┘                                 │
│                    │←── 800mm ──→│                              │
│                    │             │                              │
│                    │    1200mm   │                              │
│                    │    height   │                              │
│                    │             │                              │
│  RUDDER:                                                       │
│  - Hinge line at 75% chord                                    │
│  - Deflection: ±30°                                          │
│  - Control: cable to cockpit pedals                           │
│  - Area: 1.0 m² (10.8 sq ft)                                  │
│  - φ ratio: V-stab area = H-stab area / φ                    │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## CONTROL SURFACES

### Aileron Design

```
┌─────────────────────────────────────────────────────────────────┐
│                    AILERON — WING TRAILING EDGE                  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  WING TRAILING EDGE                                       │   │
│  │                                                           │   │
│  │  ┌─────────────────────────────────────────────────────┐  │   │
│  │  │                                                     │  │   │
│  │  │  AILERON                                            │  │   │
│  │  │  (Dacron fabric over spruce frame)                  │  │   │
│  │  │                                                     │  │   │
│  │  │  Span: 2000mm (6.6 ft)                              │  │   │
│  │  │  Chord: 300mm (11.8")                               │  │   │
│  │  │  Area: 0.6 m² (6.5 sq ft) per side                  │  │   │
│  │  │                                                     │  │   │
│  │  │  Hinge: AN3-4A clevis bolts, every 500mm           │  │   │
│  │  │  Deflection: ±25°                                   │  │   │
│  │  │  Control: cable to cockpit stick                    │  │   │
│  │  │                                                     │  │   │
│  │  │  ┌─────┐          ┌─────┐          ┌─────┐        │  │   │
│  │  │  │HINGE│          │HINGE│          │HINGE│        │  │   │
│  │  │  │ #1  │          │ #2  │          │ #3  │        │  │   │
│  │  │  └──┬──┘          └──┬──┘          └──┬──┘        │  │   │
│  │  │     │                │                │             │  │   │
│  │  │  ┌──▼──┐          ┌──▼──┐          ┌──▼──┐        │  │   │
│  │  │  │CABLE│          │CABLE│          │CABLE│        │  │   │
│  │  │  │CLAMP│          │CLAMP│          │CLAMP│        │  │   │
│  │  │  └─────┘          └─────┘          └─────┘        │  │   │
│  │  │                                                     │  │   │
│  │  └─────────────────────────────────────────────────────┘  │   │
│  │                                                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  AILERON OPERATION:                                              │
│  - Left stick → left aileron up, right aileron down             │
│  - Right stick → right aileron up, left aileron down            │
│  - Cable routing: through fuselage sidewall                     │
│  - Cable material: 1/8" steel cable, swaged terminals          │
│  - Cable tension: 10-15 lbs (adjustable via turnbuckle)        │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## MOTOR MOUNT

```
┌─────────────────────────────────────────────────────────────────┐
│                    MOTOR MOUNT — FRONT VIEW                      │
│                                                                  │
│                    ┌─────────────────────────┐                  │
│                    │      FUSELAGE            │                  │
│                    │      (front face)        │                  │
│                    │                          │                  │
│                    │   ┌─────────────────┐   │                  │
│                    │   │                 │   │                  │
│                    │   │    ┌───────┐    │   │                  │
│                    │   │    │MOTOR  │    │   │                  │
│                    │   │    │       │    │   │                  │
│                    │   │    │ 50kW  │    │   │                  │
│                    │   │    │OUTRUN │    │   │                  │
│                    │   │    │       │    │   │                  │
│                    │   │    └───┬───┘    │   │                  │
│                    │   │        │        │   │                  │
│                    │   │   ┌────┴────┐   │   │                  │
│                    │   │   │ MOUNT   │   │   │                  │
│                    │   │   │ PLATE   │   │   │                  │
│                    │   │   │ (1/4"   │   │   │                  │
│                    │   │   │ plywood)│   │   │                  │
│                    │   │   └────┬────┘   │   │                  │
│                    │   │        │        │   │                  │
│                    │   │   ┌────┴────┐   │   │                  │
│                    │   │   │ 4× AN4 │   │   │                  │
│                    │   │   │ BOLTS   │   │   │                  │
│                    │   │   └─────────┘   │   │                  │
│                    │   │                 │   │                  │
│                    │   └─────────────────┘   │                  │
│                    │                          │                  │
│                    └─────────────────────────┘                  │
│                                                                  │
│  MOTOR MOUNT SPECS:                                              │
│  - Mount plate: 1/4" Baltic Birch plywood, 200mm × 200mm       │
│  - Bolts: 4× AN4-5A (1/4"-28 × 5/8")                          │
│  - Gussets: 4× 1/4" plywood triangles, 50mm × 50mm            │
│  - Vibration isolation: rubber washers between plate and frame  │
│  - Access: removable for motor service                          │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## LANDING GEAR

```
┌─────────────────────────────────────────────────────────────────┐
│                    LANDING GEAR — FRONT VIEW                     │
│                                                                  │
│                    ┌─────────────────────────┐                  │
│                    │      FUSELAGE            │                  │
│                    └───────────┬─────────────┘                  │
│                                │                                │
│                    ┌───────────┴─────────────┐                  │
│                    │    GEAR LEG (steel tube) │                  │
│                    │    1" × 0.065" wall      │                  │
│                    │    300mm length          │                  │
│                    └───────────┬─────────────┘                  │
│                                │                                │
│                    ┌───────────┴─────────────┐                  │
│                    │    AXLE (M10 bolt)       │                  │
│                    │    100mm length          │                  │
│                    └───────────┬─────────────┘                  │
│                                │                                │
│                    ┌───────────┴─────────────┐                  │
│                    │    WHEEL (8" polyurethane)│                 │
│                    │    with bearing           │                 │
│                    └─────────────────────────┘                  │
│                                                                  │
│  LANDING GEAR CONFIGURATION:                                     │
│  - Type: Fixed tricycle                                          │
│  - Nose gear: 1× steel tube leg, 5" wheel                      │
│  - Main gear: 2× steel tube legs, 8" wheels                    │
│  - Shock absorption: bungee cord wrapping                        │
│  - Track width: 1200mm (main gear)                              │
│  - Wheelbase: 3000mm (nose to main)                             │
│  - Ground clearance: 300mm (propeller tip)                      │
│  - Braking: none (grass field only)                             │
│  - Tire pressure: 15-20 PSI                                     │
│                                                                  │
│  GEAR LEG DETAIL:                                                │
│  - Material: 1" OD × 0.065" wall mild steel tube               │
│  - Length: 300mm (45° angle from fuselage)                      │
│  - Attachment: welded to steel plate, bolted to fuselage        │
│  - Bungee wrapping: 3 turns of 1/2" bungee cord                │
│  - Axle: M10 × 100mm Grade 5 bolt, with castle nut + cotter   │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## STRUCTURAL LOAD ANALYSIS

### Design Load Factors

| Condition | Load Factor | Notes |
|-----------|-------------|-------|
| Normal cruise | 1.0g | Level flight |
| Gentle turn | 1.5g | 45° bank |
| Turbulence | 2.0g | Moderate gusts |
| Hard pull-up | 3.0g | Emergency maneuver |
| Landing impact | 3.0g | 6 ft/s descent rate |
| Design ultimate | 4.5g | 1.5× ultimate |

### Critical Member Sizing

| Member | Material | Size | Max Load | Safety Factor |
|--------|----------|------|----------|---------------|
| Main longerons | Spruce | 1×4" (89×38mm) | 2,000 N | 3.2 |
| Wing spar | Spruce | 1×4" (89×38mm) | 3,500 N | 2.8 |
| Wing ribs | Spruce | 1/2×1" (12×25mm) | 200 N | 4.1 |
| Fuselage formers | Pine | 1×3" (64×19mm) | 500 N | 3.5 |
| Gear legs | Steel | 1" × 0.065" | 5,000 N | 2.5 |
| Motor mount | Plywood | 1/4" Baltic Birch | 1,500 N | 3.0 |

### Weight Budget

| Component | Weight | % |
|-----------|--------|---|
| Wood frame (spruce + pine) | 35 kg | 30.4% |
| Dacron fabric covering | 8 kg | 7.0% |
| Hardware (bolts, nuts, washers) | 12 kg | 10.4% |
| Landing gear (steel + wheels) | 15 kg | 13.0% |
| Motor + ESC + propeller | 18 kg | 15.7% |
| Batteries (4× FPB-20) | 20 kg | 17.4% |
| Avionics + wiring | 5 kg | 4.3% |
| Seat (canvas sling) | 2 kg | 1.7% |
| **EMPTY WEIGHT** | **115 kg** | **100%** |
| Pilot (max) | 90 kg | — |
| Ballast (if needed) | 22 kg | — |
| **MAX GROSS WEIGHT** | **227 kg** | — |

---

## WOOD SPECIFICATIONS

### Sitka Spruce (Primary Structure)

| Property | Value | Notes |
|----------|-------|-------|
| Density | 400 kg/m³ | Lightweight |
| Modulus of Rupture | 67 MPa | Excellent bending |
| Modulus of Elasticity | 10 GPa | Good stiffness |
| Compression Parallel | 42 MPa | Strong in compression |
| Shear | 7 MPa | Adequate for pins |
| Source | Local lumber yard | Select grade, clear |

### Pine (Secondary Structure)

| Property | Value | Notes |
|----------|-------|-------|
| Density | 500 kg/m³ | Slightly heavier |
| Modulus of Rupture | 40 MPa | Adequate |
| Modulus of Elasticity | 8 GPa | Good for formers |
| Source | Home Depot | Common grade |

### Baltic Birch Plywood (Gussets)

| Property | Value | Notes |
|----------|-------|-------|
| Density | 650 kg/m³ | Dense |
| Modulus of Rupture | 70 MPa | Excellent |
| Thickness | 1/4" (6.35mm) | Gussets, bulkheads |
| Source | Home Depot | Cabinet grade |
