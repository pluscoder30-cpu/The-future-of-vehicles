# PHI EMOTION CLOAK — Control System

## Control Interface
The Emotion Cloak uses minimal physical controls — the primary interface is the emotions themselves. Additional controls are hidden in the collar for privacy and mode management.

## Physical Controls

### Phi-Lock Clasp
- **Location:** Collar
- **Function:** Power on/off, mode selection
- **Operation:** Single press = mode cycle, Hold = power

### Privacy Button
- **Location:** Left collar (hidden)
- **Function:** Activates Privacy Mode
- **Operation:** Single press = toggle privacy
- **Indicator:** Subtle LED on collar

### Social Button
- **Location:** Right collar (hidden)
- **Function:** Activates Social Mode
- **Operation:** Single press = toggle social
- **Indicator:** Subtle LED on collar

## Mobile App Controls
- **Color Override:** Choose a fixed color (bypasses emotion)
- **Sensitivity:** Adjust biofeedback sensitivity
- **Privacy List:** Select who can see your emotions
- **Pattern Style:** Choose color pattern style
- **Calibration:** Calibrate sensors to your baseline
- **History:** View emotional patterns over time

## Modes
| Mode | Description | Display |
|------|-------------|---------|
| Normal | Shows emotions transparently | Full color |
| Privacy | Hides emotional state | Neutral gray |
| Social | Shares with nearby cloaks | Full color + broadcast |
| Override | Fixed color chosen by user | Selected color |
| Sleep | Minimal display, sensors only | Dim single color |
| Therapy | Enhanced sensitivity for sessions | High-resolution color |

## Calibration
On first use, the cloak calibrates to the wearer:
1. 5-minute baseline measurement (neutral state)
2. Emotion prompts (happy, sad, angry, calm)
3. ML model fine-tunes to individual physiology
4. Recalibration available anytime via app

## Data Privacy
- All processing on-device (no cloud)
- No emotional data leaves the cloak
- Social sharing requires explicit opt-in
- History stored locally (encrypted)
- Factory reset erases all data
