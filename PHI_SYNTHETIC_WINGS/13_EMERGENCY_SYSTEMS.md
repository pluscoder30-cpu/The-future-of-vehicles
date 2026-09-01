# PHI SYNTHETIC WINGS — Emergency Systems

## Emergency Priority Matrix
| Priority | Condition | Response |
|----------|-----------|----------|
| 1 - Critical | Freefall / loss of lift | Parachute deploy |
| 2 - High | Power failure | Controlled descent |
| 3 - Medium | Wing damage | Glide to landing |
| 4 - Low | Battery <10% | Begin descent planning |
| 5 - Info | Weather warning | Descend to safe altitude |

## Parachute System
- **Type:** Ballistic parachute (backpack-integrated)
- **Area:** 30 m2 (sufficient for 200 kg total load)
- **Deployment:** Automatic at >5 m/s descent / manual pull
- **Descent Rate Under Canopy:** 3-5 m/s
- **Repack Interval:** Every 2 years or after deployment
- **Activation:** Pull handle (red, left shoulder)

## Power Failure Protocol
1. System detects power loss
2. Lift field reduced to 50% (controlled descent)
3. Wing flapping stops (glide mode)
4. Descent rate: 3 m/s
5. GPS distress beacon activates
6. Emergency contact notified
7. Touchdown within 3 minutes from 500m

## Wing Damage Response
1. Load sensors detect damage
2. System adjusts for asymmetric lift
3. Controlled descent to nearest safe landing
4. If catastrophic: Parachute deploy
5. Post-landing: System lockout

## Freefall Detection
1. Accelerometer detects >2g freefall for >500ms
2. Parachute auto-deploys (0.5 second response)
3. Descent rate under canopy: 3-5 m/s
4. GPS beacon activates
5. Emergency contact notified

## Emergency Descent
From maximum altitude (3,000m):
- **Controlled:** 16 minutes (3 m/s)
- **Glide:** 10 minutes (5 m/s)
- **Parachute:** 10 minutes (5 m/s)

## Communication in Emergency
1. **433 MHz:** Distress beacon (auto-activate)
2. **GPS:** Location broadcast every 10 seconds
3. **Phone:** Notification via Bluetooth (if paired)
4. **LoRa:** Telemetry continues during descent
5. **Strobe:** Visual beacon on backpack

## Post-Emergency
- System enters lockout mode
- Full inspection required before next flight
- Flight data recorder preserves last 60 minutes
- Report filed via mobile app
- Emergency services contacted
- Parachute must be repacked before next use
