# PHI EMOTION CLOAK — Biofeedback System

## Sensor Array
The Emotion Cloak uses 6 non-invasive biofeedback sensors woven into the fabric:

### Heart Rate Sensor
- **Type:** Photoplethysmography (PPG)
- **Location:** Wrist cuff
- **Accuracy:** +/-1 BPM
- **Sample Rate:** 100 Hz
- **Measures:** Heart rate, HRV, arrhythmia

### Skin Conductance Sensor
- **Type:** Galvanic skin response (GSR)
- **Location:** Fingertip contact pads
- **Accuracy:** +/-0.01 uS
- **Sample Rate:** 50 Hz
- **Measures:** Emotional arousal, stress

### Temperature Sensor
- **Type:** Infrared thermopile
- **Location:** Chest panel
- **Accuracy:** +/-0.1C
- **Sample Rate:** 10 Hz
- **Measures:** Core body temperature

### Accelerometer
- **Type:** 6-axis IMU
- **Location:** Waistband
- **Accuracy:** +/-0.01g
- **Sample Rate:** 200 Hz
- **Measures:** Movement, posture, gesture

### Respiration Sensor
- **Type:** Chest strap (strain gauge)
- **Location:** Chest panel
- **Accuracy:** +/-0.5 breaths/min
- **Sample Rate:** 20 Hz
- **Measures:** Breathing rate, depth

### EMG Sensor
- **Type:** Surface electromyography
- **Location:** Shoulder panels
- **Accuracy:** +/-1 uV
- **Sample Rate:** 500 Hz
- **Measures:** Muscle tension, posture

## Signal Processing
All sensor data is processed by an on-board emotion AI:
1. **Raw Signal:** Individual sensor readings
2. **Phi-Harmonic Filtering:** Golden-ratio smoothing (removes noise)
3. **Emotion Classification:** ML model maps signals to emotional states
4. **Color Mapping:** Emotion state mapped to HSL color value
5. **Fabric Update:** Color sent to nano-photonic fabric (60 Hz)

## Emotion Classification
The AI classifies emotions into a continuous spectrum:
| Emotion | Primary Color | Secondary Color | Pattern |
|---------|--------------|----------------|---------|
| Joy | Gold | Yellow | Rising waves |
| Calm | Blue | Cyan | Gentle ripples |
| Sadness | Indigo | Violet | Slow drift |
| Anger | Red | Crimson | Sharp pulses |
| Fear | White | Silver | Rapid flicker |
| Love | Pink | Rose | Warm glow |
| Surprise | Orange | Amber | Flash burst |
| Disgust | Green | Olive | Slow swirl |
| Neutral | Gray | White | Steady glow |
