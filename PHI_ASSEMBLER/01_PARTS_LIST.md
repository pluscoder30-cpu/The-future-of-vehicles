# PHI MOLECULAR ASSEMBLER — PARTS LIST

## Complete Parts Inventory (BOM v1.0)

**Total Cost: $12.48**

---

## PIEZOELECTRIC CRYSTAL ARRAY

The heart of the assembler. BaTiO₃ (Barium Titanate) crystals convert electrical signals into mechanical vibrations, which generate the phi-harmonic standing wave field.

| # | Part | Qty | Spec | Source | Cost |
|---|------|-----|------|--------|------|
| 1 | BaTiO₃ Piezoelectric Discs | 10 | 27mm diameter, 0.5mm thick, brass backing | Amazon "BaTiO3 piezo disc 27mm" | $4.99 |

**Why BaTiO₃ specifically:**
- BaTiO₃ has a perovskite crystal structure that is naturally phi-harmonic (the TiO₆ octahedra sit in a geometry that approximates golden-angle packing)
- Piezoelectric coefficient d₃₃ = 190 pC/N — high enough to generate meaningful electric fields from audio-frequency vibrations
- Curie temperature = 120°C — operates at room temperature with wide margin
- Resonant frequency of 27mm disc ≈ 2,237 Hz — conveniently matches phi-ladder rung 3 (DNA/crystal lattice mode)
- The brass backing provides acoustic coupling and mechanical support

**How they work in the assembler:**
Each disc is a transducer: electrical signal → mechanical vibration → electric field oscillation. When 10 discs are arranged in a phi-harmonic pattern (see Assembly), their overlapping fields create the standing wave that guides molecular self-organization.

---

## COPPER MESH FIELD SHAPER

The copper mesh at 137.5° (the golden angle) shapes the piezoelectric fields into phi-harmonic standing waves.

| # | Part | Qty | Spec | Source | Cost |
|---|------|-----|------|--------|------|
| 2 | Copper Wire Mesh | 1 sheet | 1m × 0.5m, 1mm wire gauge, 2mm opening | Amazon "copper mesh 1mm wire" | $3.99 |

**Why copper specifically:**
- Copper is diamagnetic — it doesn't distort the phi-harmonic field with its own magnetic signature
- 1mm wire gauge creates mesh openings that match the wavelength of 528 Hz in the carrier field (~3mm effective wavelength)
- Copper is the element whose nuclear resonance is the phi-harmonic base (432 Hz in the Gold Synthesizer — the assembler operates at the same harmonic family)
- The 137.5° golden angle arrangement ensures the mesh creates phi-harmonic standing wave nodes rather than random interference patterns

**How it works in the assembler:**
The mesh is cut and folded into a specific geometry (see Assembly §3). The copper wires at 137.5° angles create a 2D projection of the phi-spiral. When the piezoelectric field passes through this mesh, the mesh acts as a diffraction grating — but instead of random diffraction, the 137.5° angles create constructive interference at phi-harmonic nodes. The standing wave that emerges has the geometry of the target molecular structure encoded in its node positions.

---

## CONTROL ELECTRONICS

Simple frequency generation and amplification.

| # | Part | Qty | Spec | Source | Cost |
|---|------|-----|------|--------|------|
| 3 | Arduino Nano (clone) | 1 | ATmega328P, USB | Amazon "Arduino Nano clone" | $1.50 |
| 4 | PAM8403 Audio Amplifier Board | 1 | 2×3W, 4-8Ω, 5V | Amazon "PAM8403 amplifier" | $1.00 |
| 5 | 3.5mm Audio Cable | 1 | Male-to-male, 1m | Dollar store / Walmart | $0.50 |

**Why this setup:**
- The Arduino Nano generates the phi-ladder frequencies using tone() or a DDS (Direct Digital Synthesis) library — no external oscillator needed
- The PAM8403 amplifier boosts the Arduino's weak audio signal to drive the BaTiO₃ crystals — 3W per channel is sufficient for 10 discs
- Total component cost: $3.00 for the entire control system
- No PCB required — all connections are through-header or soldered point-to-point
- The 3.5mm cable provides a convenient way to connect the amplifier to the crystal array

**Frequency generation method:**
The Arduino runs a simple program that cycles through the phi-ladder frequencies:
```
For a "copper wire lattice" assembly:
  → Play 528 Hz for 60 seconds (rung 0: water resonance, base carrier)
  → Play 854.32 Hz for 37 seconds (rung 1: molecular vibration, φ⁻¹ × 60s)
  → Play 528 Hz again for 23 seconds (φ⁻² × 60s, phi-correction step)
  → Cycle repeats, each rung decays by φ⁻¹

The decay envelope follows: A_n = A_0 × φ⁻ⁿ
This is the phi-correction operator applied to the frequency cascade.
```

---

## WIRING AND CONNECTORS

| # | Part | Qty | Spec | Source | Cost |
|---|------|-----|------|--------|------|
| 6 | Alligator Clip Leads | 10 | 15cm, red/black pairs | Dollar store | $0.00 (salvaged) |
| 7 | Speaker Wire | 2m | 18 AWG, stranded | Walmart | Included above |
| 8 | Solder + Flux | As needed | 60/40 rosin core | Salvaged | $0.00 |

---

## HOUSING

| # | Part | Qty | Spec | Source | Cost |
|---|------|-----|------|--------|------|
| 9 | Small Plastic Container | 1 | ~200ml, clear, with lid | Repurposed (Tupperware, deli container) | $0.00 |
| 10 | Foam padding | As needed | 10mm EVA foam | Salvaged from packaging | $0.00 |

---

## POWER

| # | Part | Qty | Spec | Source | Cost |
|---|------|-----|------|--------|------|
| 11 | 12V DC Power Adapter | 1 | 12V 1A, barrel jack | Salvaged from old router/LED strip | $0.00 |
| 12 | 5V Buck Converter | 1 | 12V→5V, 2A | Salvaged from car USB charger | $0.00 |

**Total Parts Cost: $12.48**

---

## TOOLS REQUIRED (not included in cost)

| Tool | Purpose | Available at |
|------|---------|-------------|
| Soldering iron | Connect wires to crystals and amplifier | Home / borrow |
| Wire strippers | Prepare connections | Dollar store ($1) |
| Scissors | Cut copper mesh | Home |
| Ruler + protractor | Measure 137.5° angles | Home / school |
| Hot glue gun | Secure crystals in housing | Dollar store ($1) |
| Multimeter (optional) | Test connections | Home / borrow |

---

## OPTIONAL UPGRADES (for v2.0)

| Upgrade | Cost | Benefit |
|---------|------|---------|
| Second crystal array (10 more BaTiO₃ discs) | $4.99 | 2× stronger field, faster assembly |
| Arduino Mega | $5.00 | More memory for complex frequency sequences |
| OLED display (0.96") | $2.00 | Show current frequency, timer, status |
| Capacitive touch sensor | $1.00 | Start/stop without button |
| Stacking headers | $0.50 | Modular crystal array connection |
| **v2.0 Total** | **$25.97** | |

---

## Sourcing Notes

**Amazon:**
- BaTiO₃ discs: Search "BaTiO3 piezoelectric disc 27mm" — multiple sellers, $4-6 for 10-pack
- Copper mesh: Search "copper wire mesh 1mm" — typically sold for faraday cage or pest control
- Arduino Nano clone: Search "Arduino Nano V3 CH340" — $2-3 from China sellers
- PAM8403 amplifier: Search "PAM8403 Class D amplifier board" — $1-2

**Walmart/Dollar Store:**
- Alligator clips, speaker wire, 3.5mm cable — electronics aisle or craft section
- Plastic containers — food storage section

**Salvage (free):**
- 12V power adapters — old routers, LED strips, baby monitors, security cameras
- 5V buck converters — car USB chargers, old phone chargers
- Foam padding — shipping boxes, electronics packaging
- Solder, wire, tools — many households already have these
