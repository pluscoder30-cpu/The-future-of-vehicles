# PHI CHEAP SHUTTLE — SAFETY GUIDELINES

## Emergency Procedures and Safety Systems

---

## SAFETY PHILOSOPHY

The PHI Cheap Shuttle is an experimental vehicle. Safety is achieved through:
1. Redundant critical systems
2. Conservative structural margins (SF > 1.5)
3. Emergency recovery system (parachutes)
4. Ground-based safety protocols
5. Progressive test flight envelope expansion

---

## CRITICAL SAFETY SYSTEMS

### 1. Emergency Recovery (Parachutes)
- 2× 15 ft round parachutes (independent)
- Deployment: Manual pull-cable from cockpit
- Deployment speed: < 150 mph (240 km/h)
- Descent rate: ~25 fps (7.6 m/s) with 2 passengers
- Landing load: ~3g (survivable)

### 2. Engine Cutoff
- 4× independent ANL fuse disconnects (150A each)
- 2× master disconnect switches (400A, left/right bus)
- Arduino-controlled relay shutdown (software watchdog)
- Manual cutoff button (red, cockpit)

### 3. Fire Suppression
- 2× ABC fire extinguishers (5 lb each) mounted in cockpit
- Fire-resistant wiring (silicone insulation)
- Ceramic thermal barriers around thrusters
- Fuel: Phi-harmonic field plasma batteries (no flammable fuel — zero fire/explosion risk — plasma is self-limiting)

### 4. Structural Integrity
- All welds: minimum 3mm fillet, 75% penetration
- Fasteners: Grade 5 minimum, lock nuts on critical joints
- Safety wire on all vibration-prone fasteners
- Post-weld inspection: 100% visual, 10% dye penetrant

---

## EMERGENCY PROCEDURES

### E1: Engine Failure (Single Thruster)
1. Reduce power on remaining 3 thrusters to 75%
2. Verify thrust symmetry
3. Abort ascent, begin controlled descent
4. Deploy parachutes if below 10,000 ft

### E2: Engine Failure (Multiple Thrusters)
1. Cut all thruster power immediately
2. Deploy parachutes
3. Activate VHF mayday call
4. Prepare for off-field landing

### E3: Battery Failure
1. Monitor remaining battery voltage
2. Reduce power to minimum for controlled descent
3. Deploy parachutes before battery depletion
4. Emergency landing

### E4: Fire
1. Cut all electrical power (master disconnect)
2. Deploy fire extinguisher
3. If fire persists: deploy parachutes immediately
4. Emergency egress

### E5: Structural Failure
1. Deploy parachutes immediately
2. Brace for impact
3. Activate emergency beacon

### E6: Loss of Communications
1. Continue mission if all other systems nominal
2. Activate HC-12 telemetry (backup)
3. If complete comms loss: descend to safe altitude
4. Land at nearest safe location

---

## GROUND SAFETY PROTOCOLS

### Pre-Flight Checklist
1. ☐ Visual inspection of all welds
2. ☐ Torque check on critical fasteners
3. ☐ Battery voltage check (all 4 ≥ 12.4V)
4. ☐ Thruster continuity check (all 4 coils)
5. ☐ Avionics power-on test
6. ☐ GPS fix acquired
7. ☐ VHF radio check (both units)
8. ☐ Parachute pin inspection
9. ☐ Fire extinguisher armed
10. ☐ Ground crew briefed

### Launch Area Requirements
- Minimum 2 km × 2 km clear area (no structures)
- No public roads within 1 km of flight path
- Fire extinguishers at launch pad (2× ABC, 20 lb)
- First aid kit at launch pad
- Ambulance on standby (or within 15 min)
- NOTAM filed with FAA

### Ground Crew Positions
- **Launch Director:** 500m from pad, has abort authority
- **Safety Officer:** 300m from pad, monitors fire/structural
- **Recovery Team:** 2 km downrange, monitors descent
- **Medical:** 1 km from pad, first aid capability

---

## WEIGHT AND BALANCE LIMITS

| Parameter | Limit | Consequence |
|-----------|-------|-------------|
| Max Gross Weight | 375 kg | Structural overstress |
| CG Forward Limit | 55% MAC | Pitch instability |
| CG Aft Limit | 68% MAC | Pitch instability |
| Max Pilot Weight | 100 kg | CG shift forward |
| Max Passenger Weight | 100 kg | CG shift aft |

---

## INSPECTION INTERVALS

| Inspection | Interval | Scope |
|------------|----------|-------|
| Pre-flight | Every flight | Visual, functional |
| 10-hour | Every 10 flight hours | Torque, wiring, welds |
| 50-hour | Every 50 flight hours | Full structural, dye penetrant |
| Annual | Every 12 months | Complete teardown, NDT |

---

## LIMITATIONS

1. Maximum demonstrated airspeed: Mach 3 (do not exceed)
2. Maximum altitude: 100 km (suborbital limit)
3. Maximum G-load: +6g / -3g
4. Maximum wind at launch: 15 knots
5. No flight in precipitation
6. No flight within 5 nm of airports (without clearance)
7. No flight over populated areas
8. Minimum visibility: 3 statute miles
