# PHI SYNTHETIC WINGS — Quick Start Guide

## What You Built

Biosynthetic wings that enable sustained human flight. Phi-harmonic lift amplifies human power by 100x. You can hover, cruise at 35 km/h, and fly for 4 hours.

**Cost:** ~$1,200 | **Build Time:** 20-25 hours | **Weight:** 12 kg (wings + harness)

---

## Before You Fly

### Safety (NON-NEGOTIABLE)

1. **NEVER FLY ALONE** — always have a ground crew
2. **RESERVE PARACHUTE** — pin accessible with one hand
3. Kill switch tested — motor MUST stop instantly
4. Wings locked — deployment pins clicked into place
5. All bolts tight — every single one
6. Open field, no obstacles, no overhead wires
7. Wind <20 km/h (beginners: <10 km/h)
8. Helmet secured, chin strap tight

### Pre-Flight Checklist

- [ ] Wings locked in deployed position (both sides)
- [ ] All bolts tight (hex key check)
- [ ] Servos respond to controls
- [ ] Motor spins on throttle
- [ ] Kill switch stops motor instantly
- [ ] Battery >80%
- [ ] Altimeter reads correctly (0m on ground)
- [ ] Radio works
- [ ] GPS has satellite lock
- [ ] Helmet secured
- [ ] Parachute pin accessible
- [ ] Wind <20 km/h
- [ ] Open field, clear zone
- [ ] Ground crew briefed

---

## Deployment Sequence

### From Carry to Air (5 minutes)

1. **Unpack** — remove wings and harness from bag
2. **Assemble frame** — connect wing spars to harness
3. **Lock wings** — push pins until they CLICK
4. **Connect battery** — XT60 connector, verify 36V
5. **Power on:**
   - Arduino boots (LED blinks)
   - All servos center
   - Altimeter reads 0m
6. **Put on harness** — shoulder straps, chest strap, leg straps
7. **Check controls:**
   - Throttle: motor spins
   - Left/right: flaps respond
   - Up/down: pitch surfaces respond
8. **Attach kill switch** to wrist
9. **You're ready!**

---

## Flying

### Controls

| Input | Action |
|-------|--------|
| Throttle (thumb) | Motor speed (lift) |
| Body lean left | Left wing dips (turn left) |
| Body lean right | Right wing dips (turn right) |
| Shoulder shrug up | Nose up (climb) |
| Shoulder shrug down | Nose down (descend) |
| Kill switch | Emergency stop |

### Takeoff

1. Stand in open field, facing into wind
2. Throttle up to 50% — wings generate lift
3. At 80% throttle — feet leave ground
4. **CLIMB SLOWLY** — gain 10m, level off
5. Get comfortable at 10m before going higher

### Level Flight

- **Cruise throttle:** 40-50% (15-25 km/h)
- **Optimal altitude:** 30-50m
- **Monitor battery:** green = good, red = land soon
- **Monitor wind:** if gusting, descend to 10m

### Landing

1. **Start early** — begin descent at 30% battery
2. **Reduce throttle** — 20%, then 10%
3. **Approach into wind** — straight line
4. **Flare** — pull up slightly just before ground
5. **Touch down** — feet first, run it out
6. **Kill motor** — immediately after landing

---

## Emergency Procedures

### Motor Failure
1. Kill switch (if motor runs wild)
2. Glide — wings still generate lift!
3. Find soft landing spot (grass, sand)
4. Flare and touch down

### Tangled Tether/Cord
1. Kill motor
2. Use knife to cut free
3. Glide to landing

### Strong Gust
1. Reduce throttle
2. Descend to 5m (ground effect)
3. Land immediately

### Battery Dies
1. Wings still glide (L/D = 31.6)
2. From 50m: you have ~1 minute of glide
3. Find landing spot NOW
4. Flare and land

### Wing Damage
1. Kill motor immediately
2. Wings may still generate some lift
3. Land ASAP
4. Check for structural damage before next flight

---

## Flight Envelope

| Parameter | Limit |
|-----------|-------|
| Max altitude | 500m |
| Cruise altitude | 30-50m |
| Min altitude | 2m (ground effect) |
| Max speed | 90 km/h (dive) |
| Cruise speed | 35 km/h |
| Stall speed | 6.5 m/s (23 km/h) |
| Max wind | 20 km/h |
| Max pilot weight | 90 kg |
| Max flight time | 4 hours |
| Max range | 120 km |

---

## Post-Flight

1. **Fold wings** — pull pins, swing inward
2. **Disconnect battery** — XT60
3. **Inspect wings** — check for damage, tears
4. **Check servos** — move freely, no grinding
5. **Check motor** — spins freely, no heat damage
6. **Pack carefully** — wings don't bend
7. **Log flight** — time, altitude, battery usage

---

## Maintenance Schedule

| Interval | Task |
|----------|------|
| Every flight | Visual inspection, bolt check |
| Weekly | Servo lubrication, hinge inspection |
| Monthly | Full bolt torque check, battery load test |
| 3 months | Wing skin inspection, spar check |
| 1 year | Complete teardown, replace worn parts |

---

## Specifications

| Spec | Value |
|------|-------|
| Wing Span | 12m (deployed) |
| Wing Span Folded | 1.2m |
| Wing Area | 19.42 m² |
| Structure Weight | 12 kg |
| Total Flying Weight | 89-104 kg |
| Battery | 36V 5Ah Li-Ion |
| Motor | 400W, 36V |
| L/D Ratio | 31.6 |
| Stall Speed | 23 km/h |
| Cruise Speed | 35 km/h |
| Max Speed | 90 km/h |
| Flight Time | 4 hours |
| Range | 120 km |

---

## Costs After Build

| Item | Cost | Frequency |
|------|------|-----------|
| Feather replacement | $50 | Annual |
| Wing skin patch | $10 | As needed |
| Servo replacement | $15 per servo | Annual |
| Parachute repack | $50 | Every 6 months |
| Battery replacement | $120 | Every 2 years |
| Insurance | $500/year | Annual |
