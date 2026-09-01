# PHI BIO SKIN WATCH — Emergency Systems

## Emergency Priority Matrix
| Priority | Condition | Response |
|----------|-----------|----------|
| 1 - Critical | Fall detected | Alert emergency contact |
| 2 - High | Abnormal heart rhythm | Alert wearer + contact |
| 3 - Medium | SOS activated | Call emergency services |
| 4 - Low | Battery <5% | Alert wearer to charge |
| 5 - Info | Sensor malfunction | Switch to safe mode |

## Fall Detection
1. Accelerometer detects hard fall (>3g impact)
2. Watch waits 10 seconds for wearer response
3. If no response: Sends alert to emergency contact
4. If no response in 60 seconds: Calls emergency services
5. GPS coordinates included in alert

## Emergency SOS
1. Hold side button for 5 seconds
2. Watch vibrates and beeps
3. After 10 seconds (cancel window): Sends SOS
4. SOS includes GPS coordinates
5. Calls emergency contact
6. If no contact: Calls emergency services

## Heart Rate Alert
1. Sensor detects abnormal rhythm
2. Watch vibrates gently
3. App notifies wearer
4. If severe: Alert emergency contact
5. Display shows "Seek Medical Attention"

## Medical ID
When activated (hold both buttons):
- Displays wearer's name
- Emergency contact numbers
- Blood type
- Allergies
- Medical conditions
- Medications
- Works even when watch is locked

## Crash Detection
1. Accelerometer + gyroscope detect severe impact
2. Watch checks for movement
3. If no movement for 30 seconds: Assumes unconscious
4. Sends alert to emergency contact
5. Includes GPS coordinates
6. Calls emergency services after 60 seconds

## Communication in Emergency
1. **Phone:** Calls emergency contact (via paired phone)
2. **GPS:** Sends location to emergency contact
3. **Text:** Sends pre-written emergency message
4. **Haptic:** Vibration pattern for attention
5. **Audio:** Emergency tone from speaker

## Post-Emergency
- Event logged in device (encrypted)
- Medical ID accessible by first responders
- App provides post-emergency report
- Contact support if issues persist
