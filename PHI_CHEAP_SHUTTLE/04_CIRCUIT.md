# PHI CHEAP SHUTTLE — CIRCUIT SCHEMATICS

## Avionics and Control Circuits

---

## FLIGHT COMPUTER — ARDUINO MEGA 2560

### Power Supply
- Input: 12V DC from Avionics Bus
- Regulator: LM7805 → +5V Rail
- LDO: AMS1117-3.3 → +3.3V Rail
- Decoupling: 100μF electrolytic + 10μF tantalum + 100nF ceramic at each rail

### Voltage Monitoring (Battery 1-4)
- Voltage divider: 10kΩ / 2.2kΩ → A0-A3
- Formula: V_batt = V_adc × 5.545
- Accuracy: ±0.3V at 12V

### Current Sensing (Thruster 1-4)
- ACS712 30A module → A4-A7
- Sensitivity: 66mV/A
- 0A = 2.5V, 30A = 4.48V

### Temperature Sensing (Thruster 1-4)
- LM35 sensor → A8-A11
- Sensitivity: 10mV/°C
- Range: -55°C to +150°C

---

## THRUSTER DRIVER (Per Unit)

### Gate Driver: IR2110
- Input: Arduino D6-D9 (PWM, 161.8 kHz)
- Output: Drives full-bridge MOSFET pair
- Bootstrap: 0.1μF 50V capacitor

### Full-Bridge Inverter
- Q1-Q4: IRFP460 N-ch MOSFET (500V, 20A)
- Switching: Full-bridge, 161.8 kHz
- Dead time: 500ns (prevent shoot-through)

### Resonant Tank
- Inductor: Litz wire on T106-2 core, N=47 turns, L=2.3mH
- Capacitor: 4× 0.1μF 2kV film in parallel = 0.4μF
- Resonant frequency: f₀ = 1/(2π√LC) = 161.8 kHz

### Enable Relay
- Arduino D10-D13 → 330Ω → LED → 2N2222 → 12V relay coil
- Flyback diode: 1N4007 across coil
- Relay rating: 30A, 250V AC

---

## SERVO DRIVER (PCA9685)

- I2C: SDA → D20, SCL → D21
- VCC: +5V, V+: +12V (servo power)
- Outputs 0-3 → Servos 1-4 (thruster vectoring)
- PWM: 500μs (0°) to 2500μs (180°), center 1500μs

---

## COMMUNICATIONS

### GPS (BN-880)
- VCC: +5V, TX → D19 (Serial1 RX), RX → D18
- Baud: 9600, Protocol: NMEA 0183, Update: 10 Hz

### HC-12 Telemetry (433MHz)
- VCC: +5V, TX → D17 (Serial2 RX), RX → D16
- Baud: 9600, Range: 1800m, Power: 20mW

### VHF Radio (×2 handheld)
- 5W output, 136-174 MHz
- Connected via aviation headset jacks for intercom

---

## SENSOR DECOUPLING

All sensors use 100nF ceramic capacitors at VCC pins. I2C lines have 4.7kΩ pull-ups to 3.3V. GPS module has additional 10μF bulk capacitor.
