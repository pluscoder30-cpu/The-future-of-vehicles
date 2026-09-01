# PHI SUBMERSIBLE — Emergency Systems

## Emergency Priority Matrix
| Priority | Condition | Response |
|----------|-----------|----------|
| 1 - Critical | Hull breach | Emergency ascent + seal breach protocol |
| 2 - High | Power failure | Emergency ascent (gravity + ballast) |
| 3 - Medium | Life support failure | Surface immediately |
| 4 - Low | Field skimmer failure | Reduce speed, return to surface |
| 5 - Info | Low battery warning | Begin ascent planning |

## Emergency Ascent Protocol
1. System detects emergency condition
2. Drop weights released (positive buoyancy)
3. Field skimmer reverses (upward thrust)
4. Ascent rate: 10 m/s (30 seconds from 500m)
5. Surface beacon activates
6. Hatch opens at surface (pressure equalized)
7. Emergency kit deployed

## Hull Breach Response
1. Implosion sensors detect breach location
2. Breach compartment sealed (bulkhead doors close)
3. Emergency ascent initiated
4. Life support switches to emergency reserve
5. Occupants don emergency breathing apparatus
6. Ascent to surface
7. Hatch opens at surface
8. Evacuation to rescue vessel

## Emergency Breathing
- **Type:** Full-face mask with O2 supply
- **Duration:** 15 minutes (enough for 500m ascent)
- **Activation:** Automatic on cabin depressurization
- **Manual:** Pull mask from overhead compartment

## Underwater Entrapment
If the submersible cannot ascend (entangled, stuck):
1. Attempt field skimmer reversal (break free)
2. If unsuccessful: Deploy cutting tool (manual)
3. If still stuck: Activate acoustic distress signal
4. Deploy emergency marker buoy
5. Await rescue (2-hour life support reserve)

## Surface Emergency
Once at surface:
1. Activate 433 MHz beacon
2. Deploy orange smoke marker
3. Turn on strobe light (night)
4. Send GPS coordinates via LoRa
5. Open hatch only when safe
6. Deploy life raft if available

## Communication in Emergency
1. **Underwater:** Acoustic distress signal (active ping)
2. **Surface:** 433 MHz beacon + GPS broadcast
3. **Visual:** Strobe light + orange smoke
4. **Phone:** Bluetooth notification to paired device (surface only)
5. **Satellite:** Optional Iridium beacon (add-on)

## Post-Emergency
- System enters lockout mode
- Full inspection required before next dive
- Event data recorder preserves last 120 minutes
- Report filed via mobile app
- Emergency services contacted
