# PHI MOLECULAR ASSEMBLER — SAFETY

## Safety Guidelines v1.0

---

## HAZARD ASSESSMENT

| Hazard | Risk Level | Mitigation |
|--------|-----------|------------|
| Electrical shock (12V DC) | LOW | 12V is below the 30V safety threshold. No lethal shock risk. |
| Soldering iron burn | MEDIUM | Standard soldering precautions. Keep away from skin. |
| Copper/aluminum dust inhalation | MEDIUM | Work in ventilated area. Wear dust mask if sensitive. |
| Electromagnetic interference | LOW | Keep away from pacemakers, heart monitors, other medical devices. |
| Ear fatigue from 528 Hz | LOW | Take breaks. No continuous exposure > 2 hours without rest. |
| Hot glue burn | LOW | Standard hot glue precautions. |
| Fire risk | VERY LOW | No heating elements. No open flame. No high current. |
| Eye injury | LOW | No projectiles. No pressurized systems. Wear safety glasses if desired. |

**Overall risk level: LOW** — comparable to building a simple electronics project.

---

## MANDATORY SAFETY RULES

1. **DO NOT** operate near anyone with a pacemaker or implanted medical device
2. **DO NOT** exceed 12V power supply — higher voltage may overheat crystals
3. **DO** work in a ventilated area when handling metal powders
4. **DO** wash hands after handling copper/aluminum powder
5. **DO** keep small parts away from children and pets
6. **DO** unplug before modifying the assembly
7. **DO NOT** attempt to assemble hazardous materials (toxic metals, radioactive substances)
8. **DO NOT** use the assembler as a medical device (use the Healing Drone for that)

---

## MATERIAL SAFETY

### Copper Powder
- **Hazard:** Inhalation of fine copper dust can irritate lungs
- **Mitigation:** Wear dust mask when handling. Work in ventilated area.
- **First aid:** If inhaled, move to fresh air. If irritation persists, seek medical attention.

### Aluminum Powder
- **Hazard:** Fine aluminum dust is flammable in air (dust explosion risk)
- **Mitigation:** Keep powder moist or in sealed container. Avoid fine dust clouds.
- **First aid:** If in eyes, flush with water for 15 minutes.

### BaTiO₃ Crystals
- **Hazard:** Barium compounds are toxic if ingested
- **Mitigation:** Crystals are sealed in brass backing. Do not crush or ingest.
- **First aid:** If ingested, seek medical attention immediately.

### Solder (60/40 Sn/Pb)
- **Hazard:** Lead is toxic. Wash hands after handling.
- **Mitigation:** Use lead-free solder if available. Wash hands after soldering.
- **First aid:** If ingested, seek medical attention.

---

## ELECTRICAL SAFETY

- The assembler runs on 12V DC (safe extra-low voltage)
- No mains voltage inside the device
- The Arduino and amplifier run on 5V
- No capacitor banks, no high-current circuits
- The only risk is overheating the amplifier if run continuously > 8 hours

**If the amplifier gets too hot to touch:**
1. Unplug immediately
2. Let cool 30 minutes
3. Check for short circuits in wiring
4. Reduce run time to < 4 hours per session

---

## ELECTROMAGNETIC COMPATIBILITY

The phi-harmonic field operates at audio frequencies (528-40,135 Hz). This is:
- Below the radio frequency interference (RFI) threshold
- Too low to cause tissue heating
- Too weak to interfere with electronics (unless placed directly on a speaker)

**Keep 1 meter away from:**
- Pacemakers and defibrillators
- Hearing aids
- Sensitive audio equipment
- Old CRT monitors (may cause visible distortion)

---

## DISPOSAL

When you're done with the assembler:
- BaTiO₃ crystals: Return to electronics recycling (contain barium)
- Copper mesh: Recycle with copper scrap
- Arduino/amplifier: Reuse in another project
- Plastic container: Recycle with household plastics
- Foam: Recycle or discard
