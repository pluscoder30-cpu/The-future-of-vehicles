# PHI SUPER GOGGLES — POWER SYSTEM

## Battery, Charging, and Power Distribution

---

## POWER ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                      POWER SYSTEM                               │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  USB-C PD INPUT (5V/3A or 15V/1A)                       │  │
│  │  ──────────────────────                                  │  │
│  │  PD Negotiation: 15W (15V × 1A)                         │  │
│  │  Fallback: 10W (5V × 2A)                                │  │
│  └──────────────────────┬───────────────────────────────────┘  │
│                         │                                      │
│  ┌──────────────────────┴───────────────────────────────────┐  │
│  │  TP5100 CHARGER IC                                       │  │
│  │  Charge Current: 1.5A (CC mode)                          │  │
│  │  Charge Voltage: 4.2V/cell (CV mode)                     │  │
│  │  Trickle: 100mA (below 3.0V)                             │  │
│  │  Status LEDs: Red (charging), Green (complete)           │  │
│  └──────────────────────┬───────────────────────────────────┘  │
│                         │                                      │
│  ┌──────────────────────┴───────────────────────────────────┐  │
│  │  FPB-5 BATTERY 3.7V 8000mAh                                │  │
│  │  Type: Phi-harmonic field plasma (hydrogen confinement)      │  │
│  │  Capacity: 8000mAh (29.6Wh)                             │  │
│  │  Max Discharge: 16A (2C)                                 │  │
│  │  Protection: Overcurrent, Overdischarge, Short-circuit   │  │
│  │  Connector: JST-XH 3-pin (V+, V-, Temp)                 │  │
│  └──────────────────────┬───────────────────────────────────┘  │
│                         │                                      │
│            ┌────────────┼────────────┐                         │
│            │            │            │                          │
│  ┌─────────┴──────┐  ┌─┴──────────┐ ┌┴──────────────┐         │
│  │  LM2596 #1     │  │  LM2596 #2 │ │  AMS1117 ×3   │         │
│  │  5V Rail A      │  │  5V Rail B │ │  3.3V Rails   │         │
│  │  (Sensors/ADC)  │  │  (Displays)│ │  (Digital)    │         │
│  │  3A max         │  │  3A max    │ │  1A each      │         │
│  └─────────┬──────┘  └─┬──────────┘ └┬──────────────┘         │
│            │            │            │                          │
│            ▼            ▼            ▼                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  POWER DISTRIBUTION                                      │  │
│  │                                                          │  │
│  │  5V Rail A: ADC1, ADC2, MUX1-4, BNO055, SD Card        │  │
│  │  5V Rail B: Left OLED, Right OLED, ADV7533 × 2         │  │
│  │  3.3V #1:  FPGA Core, FPGA I/O                          │  │
│  │  3.3V #2:  EMF Sensors (8×), ADC Reference              │  │
│  │  3.3V #3:  IMU, SD Card Module, Misc                    │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## BATTERY SPECIFICATIONS

### FPB-5 8000mAh Phi-Harmonic Field Plasma Battery

```
Physical:
  Type: Phi-harmonic field plasma (hydrogen confinement)
  Configuration: Micro-toroidal plasma ring
  Dimensions: 71mm × 36mm × 22mm
  Weight: 95g
  Connector: JST-XH 3-pin

Electrical:
  Nominal Voltage: 3.7V
  Full Charge Voltage: 4.2V
  Minimum Voltage: 3.0V
  Capacity: 8000mAh (29.6Wh)
  Max Continuous Discharge: 16A (2C)
  Max Pulse Discharge: 32A (4C, <30s)
  Internal Resistance: <50mΩ
  Self-Discharge: <3%/month

Thermal:
  Charge Temperature: 0°C to 45°C
  Discharge Temperature: -20°C to 60°C
  Storage Temperature: 10°C to 30°C
  Storage Voltage: 3.7V (40% charge)

Safety:
  Zero fire/explosion risk — plasma is self-limiting
  No thermal runaway — plasma dissipates harmlessly
  No flammable electrolyte — hydrogen plasma only

Cycle Life:
  500 cycles to 80% capacity
  1000 cycles to 60% capacity
  Calendar life: 2-3 years
```

### Battery Protection Circuit

```
Protection Features:
  Overcurrent: 16A cutoff (<100ms response)
  Overdischarge: 3.0V cutoff (<1s response)
  Short-circuit: <1ms response
  Overcharge: 4.2V cutoff (TP5100 controlled)

Protection IC: DW01A
  Overcurrent threshold: 16A
  Overdischarge voltage: 3.0V
  Overcharge voltage: 4.25V
  Short-circuit current: 32A (immediate)
```

### Battery Life Calculations

```
Typical Use Case (Mixed Vision Modes):
  Average Current Draw: 1.05A
  Battery Capacity: 8000mAh
  Runtime: 8000mAh / 1050mA = 7.62 hours

Heavy Use Case (All Modes Active):
  Peak Current Draw: 1.5A
  Battery Capacity: 8000mAh
  Runtime: 8000mAh / 1500mA = 5.33 hours

Light Use Case (EMF Detection Only):
  Minimum Current Draw: 0.6A
  Battery Capacity: 8000mAh
  Runtime: 8000mAh / 600mA = 13.33 hours

Standby (Sleep Mode):
  Sleep Current: 0.043A
  Battery Capacity: 8000mAh
  Standby: 8000mAh / 43mA = 186 hours (7.75 days)
```

---

## CHARGING SYSTEM

### TP5100 Charger IC

```
Specifications:
  Input Voltage: 5V to 20V (USB-C PD)
  Charge Current: Adjustable (500mA to 2A)
  Charge Voltage: 4.2V per cell
  Top-off Voltage: 4.1V
  Trickle Current: 100mA (below 3.0V)
  Charge Termination: 1/10C (80mA)
  Status Outputs: LED1 (charging), LED2 (complete)

Charging Profile:
  Stage 1: Pre-charge (below 3.0V)
    Current: 100mA
    Duration: Until 3.0V reached

  Stage 2: Constant Current (CC)
    Current: 1.5A
    Voltage: 3.0V → 4.2V
    Duration: ~4 hours

  Stage 3: Constant Voltage (CV)
    Voltage: 4.2V
    Current: 1.5A → 80mA
    Duration: ~1.3 hours

  Stage 4: Termination
    Current: <80mA
    Status: Green LED on
    Top-off: 4.1V maintenance

Total Charge Time: ~5.3 hours (0-100%)
```

### USB-C PD Negotiation

```
USB-C PD Protocol:
  Source Capabilities:
    PDO 1: 5V/3A (15W)
    PDO 2: 9V/2A (18W)
    PDO 3: 15V/1A (15W)

  Requested PDO: 3 (15V/1A, 15W)
  Fallback: PDO 1 (5V/3A) if PD not supported

  Cable Requirements:
    USB-C to USB-C (PD-rated)
    E-marked cable (5A capable)
    Length: <2m for best performance
```

### Charging Indicator

```
LED Status:
  Red ON:    Charging (CC or CV mode)
  Green ON:  Charge complete (top-off or standby)
  Red FLASH: Fault (overvoltage, overcurrent)
  Both OFF:  Not connected / no power

Charging Animation (on OLED):
  Battery icon with filling animation
  Percentage display (0-100%)
  Time remaining estimate
  Charging power display (W)
```

---

## POWER REGULATION

### LM2596 Buck Converter (5V Rails)

```
LM2596 #1 (5V Rail A — Sensors/ADC):
  Input: 3.0V - 4.2V (battery)
  Output: 5.0V ±2%
  Max Current: 3A
  Efficiency: 85% (typical)
  Ripple: <50mVpp
  Switching Frequency: 150 kHz

  Component Values:
    L1: 33μH (power inductor, 3A rated)
    C_out: 330μF (electrolytic) + 10μF (ceramic)
    C_in: 100μF (electrolytic) + 10μF (ceramic)
    D1: SS34 Schottky (3A, 40V)
    R_feedback: 2.7kΩ / 8.2kΩ (voltage divider)

  Thermal:
    Power dissipation: 0.75W (at 1A load)
    Heatsink: PCB copper pour (1 sq inch)
    Temperature rise: 15°C above ambient

LM2596 #2 (5V Rail B — Displays):
  Same specifications as LM2596 #1
  Separate output for display isolation
```

### AMS1117 LDO Regulator (3.3V Rails)

```
AMS1117 #1 (3.3V Rail #1 — FPGA):
  Input: 5V (from LM2596 #1)
  Output: 3.3V ±1%
  Max Current: 1A
  Dropout: 1.3V
  PSRR: 72dB @ 120Hz
  Quiescent Current: 5mA

  Bypass:
    C_in: 22μF (tantalum)
    C_out: 22μF (tantalum) + 0.1μF (ceramic)

  Thermal:
    Power dissipation: 1.7W (at 500mA load)
    Heatsink: PCB copper pour
    Temperature rise: 25°C above ambient
    Note: Active cooling recommended

AMS1117 #2 (3.3V Rail #2 — Sensors):
  Input: 5V (from LM2596 #1)
  Output: 3.3V ±1%
  Max Current: 1A
  Load: 100mA (sensors + reference)
  Thermal: 0.5W dissipation

AMS1117 #3 (3.3V Rail #3 — Misc):
  Input: 5V (from LM2596 #1)
  Output: 3.3V ±1%
  Max Current: 1A
  Load: 50mA (IMU + SD card)
  Thermal: 0.3W dissipation
```

### Power Rail Specifications

```
5V Rail A (Sensors/ADC):
  Voltage: 5.0V ±2% (4.9V - 5.1V)
  Max Current: 3A
  Typical Current: 250mA
  Ripple: <50mVpp
  Load Regulation: <1%
  Line Regulation: <0.5%

5V Rail B (Displays):
  Voltage: 5.0V ±2% (4.9V - 5.1V)
  Max Current: 3A
  Typical Current: 400mA
  Ripple: <50mVpp
  Load Regulation: <1%
  Line Regulation: <0.5%

3.3V Rail #1 (FPGA):
  Voltage: 3.3V ±1% (3.267V - 3.333V)
  Max Current: 1A
  Typical Current: 400mA
  Ripple: <20mVpp
  Load Regulation: <0.5%
  Line Regulation: <0.5%

3.3V Rail #2 (Sensors):
  Voltage: 3.3V ±1% (3.267V - 3.333V)
  Max Current: 1A
  Typical Current: 100mA
  Ripple: <20mVpp
  Load Regulation: <0.5%
  Line Regulation: <0.5%

3.3V Rail #3 (Misc):
  Voltage: 3.3V ±1% (3.267V - 3.333V)
  Max Current: 1A
  Typical Current: 50mA
  Ripple: <20mVpp
  Load Regulation: <0.5%
  Line Regulation: <0.5%
```

---

## POWER MANAGEMENT IC

### Power Switching

```
Main Power Switch:
  SI2302 N-Channel MOSFET
  Gate: Connected to power button
  Source: Battery negative
  Drain: System ground
  
  On-Resistance: 0.065Ω
  Max Current: 2.8A
  Threshold Voltage: 1.2V
  
  When ON: GPIO[45] (power button) pulls gate high via 10kΩ
  When OFF: 10kΩ pull-down to source

Power Distribution Switches:
  SI2302 #2: 5V Rail A enable (GPIO-controlled)
  SI2302 #3: 5V Rail B enable (GPIO-controlled)
  SI2302 #4: 3.3V Rail #3 enable (GPIO-controlled)

Soft-Start:
  All rails have RC soft-start (100ms rise time)
  Prevents inrush current damage
```

### Power Monitoring

```
Battery Voltage Monitor:
  Resistor Divider: 100kΩ / 100kΩ (2:1)
  ADC Input: ADC1 AIN2
  Resolution: 16-bit (0.065mV per LSB)
  Range: 0-5V (actual: 3.0-4.2V)
  
  Voltage Calculation:
    V_battery = V_adc × (R1 + R2) / R2
    V_battery = V_adc × 2.0

  Accuracy: ±10mV
  Update Rate: 10 Hz

Temperature Monitoring:
  LM35 Temperature Sensor
  Output: 10mV/°C
  ADC Input: ADC1 AIN3
  Range: -55°C to 150°C
  
  Accuracy: ±0.5°C
  Update Rate: 1 Hz

Current Monitoring:
  Method: High-side current sense
  Resistor: 0.01Ω (10mΩ)
  Amplifier: INA219 (I2C)
  Range: 0-3A
  Resolution: 0.1mA
  
  Note: INA219 can be added as optional upgrade
```

---

## POWER SAFETY

### Protection Circuits

```
Overcurrent Protection:
  Method: PTC resettable fuse + MOSFET cutoff
  PTC Rating: 2A (hold), 4A (trip)
  MOSFET Cutoff: 3A (GPIO-monitored)
  Response Time: <100ms

Short-Circuit Protection:
  Method: Battery internal + external PTC
  Battery: DW01A IC (<1ms)
  External: PTC (<100ms)
  Combined: <100ms total

Overvoltage Protection:
  Method: TP5100 + Zener clamp
  TP5100: 4.2V cutoff
  Zener: 5.1V clamp on 5V rails
  Response: <1µs (Zener), <10ms (TP5100)

Undervoltage Protection:
  Method: ADC monitoring + firmware
  Warning: 3.4V (20% remaining)
  Critical: 3.2V (5% remaining)
  Cutoff: 3.0V (0%)
  Response: <1s (firmware)
```

### Thermal Protection

```
Temperature Monitoring Points:
  1. FPGA junction (internal sensor)
  2. Ambient (LM35)
  3. Battery (NTC thermistor)
  4. LM2596 #1 (thermal pad)
  5. LM2596 #2 (thermal pad)

Thermal Limits:
  FPGA: 85°C warning, 95°C shutdown
  Battery: 60°C warning, 70°C shutdown
  Regulators: 120°C shutdown (thermal pad)
  Ambient: 40°C warning, 50°C shutdown

Thermal Actions:
  Warning: Reduce brightness 50%
  Critical: Reduce brightness 75%
  Shutdown: Power off all subsystems
  
Fan Control:
  Below 40°C: Fan OFF
  40-60°C: Fan LOW (50% PWM)
  60-80°C: Fan HIGH (100% PWM)
  Above 80°C: System shutdown
```

---

## POWER EFFICIENCY

### System Efficiency

```
Overall Efficiency (Battery to Load):
  5V Rail A: 85% (LM2596) × 95% (AMS1117) = 80.75%
  5V Rail B: 85% (LM2596) = 85%
  3.3V Rails: 85% (LM2596) × 95% (AMS1117) = 80.75%

Weighted Average:
  (0.25 × 80.75%) + (0.40 × 85%) + (0.35 × 80.75%) = 82.4%

Power Loss:
  Total Input: 3.885W
  Useful Output: 3.204W
  Loss: 0.681W (17.5%)

Loss Distribution:
  LM2596 #1: 0.28W (41%)
  LM2596 #2: 0.25W (37%)
  AMS1117: 0.12W (18%)
  Wiring/other: 0.03W (4%)
```

### Battery Life Optimization

```
Optimization Strategies:
1. Duty cycling: 35% savings (φ-harmonic cycling)
2. Display dimming: 20% savings (auto-brightness)
3. Sleep mode: 95% savings (when idle)
4. Sensor gating: 15% savings (reduce sample rate)
5. FPGA optimization: 10% savings (clock gating)

Combined Savings:
  Active mode: 35% duty cycling = 65% average power
  Sleep mode: 95% savings
  Average (mixed use): 70% of nominal power

Extended Battery Life:
  Nominal: 7.6 hours
  Optimized: 7.6 / 0.70 = 10.9 hours
```

---

## POWER CONNECTORS AND WIRING

### Battery Connector (JST-XH 3-pin)

```
Pin 1: VBAT (3.7V positive) — Brown wire
Pin 2: NTC (temperature sensor) — White wire
Pin 3: GND (negative) — Black wire

Wire Gauge: 22AWG silicone
Connector: JST-XH 3-pin, 2.5mm pitch
Current Rating: 3A
Mating Cycles: 100+
```

### USB-C Connector

```
Pin Assignments:
  VBUS: 5V/9V/15V/20V (PD negotiated)
  D+: USB 2.0 data / PD communication
  D-: USB 2.0 data / PD communication
  CC1: PD configuration channel
  CC2: PD configuration channel
  GND: Power ground
  Shield: Cable shield

USB-C Specifications:
  Type: USB-C 3.1 Gen 1
  Current Rating: 5A (with e-marked cable)
  PD Version: 3.0
  VBUS Protection: 20V max
```

### Power Distribution Wiring

```
Battery to Power Board:
  Wire: 22AWG silicone
  Length: 50mm
  Connector: JST-XH 3-pin

Power Board to Main Board:
  Wire: 24AWG silicone (5V rails)
  Wire: 26AWG silicone (3.3V rails)
  Length: 100mm
  Connector: 6-pin header (2× 5V, 2× 3.3V, 2× GND)

Main Board to Display:
  Wire: 26AWG silicone
  Length: 80mm
  Connector: 4-pin header (5V, GND, EN, Status)

Wire Color Code:
  Red: 5V positive
  Orange: 3.3V positive
  Black: Ground
  Brown: Battery positive
  White: Temperature sense
  Green: Enable signal
  Yellow: Status signal
```

---

## POWER SYSTEM TESTING

### Test Points

```
TP1: Battery voltage (before charger)
TP2: Battery voltage (after protection)
TP3: 5V Rail A output
TP4: 5V Rail B output
TP5: 3.3V Rail #1 output
TP6: 3.3V Rail #2 output
TP7: 3.3V Rail #3 output
TP8: Ground reference

Test Procedure:
1. Measure TP1: Should be 3.6-3.8V (nominal battery)
2. Measure TP3: Should be 5.0V ±2%
3. Measure TP4: Should be 5.0V ±2%
4. Measure TP5: Should be 3.3V ±1%
5. Measure TP6: Should be 3.3V ±1%
6. Measure TP7: Should be 3.3V ±1%
7. Apply load and verify regulation
8. Measure ripple on all rails (<50mVpp)
9. Test charging cycle (0-100%)
10. Test low-battery cutoff (3.0V)
```

### Efficiency Measurement

```
Method: Input power vs output power
Equipment: Digital multimeter (voltage), clamp meter (current)

Test Points:
  Input: Battery terminals (V × I)
  Output: Each rail (V × I)

Calculation:
  Efficiency = (Σ V_out × I_out) / (V_batt × I_batt) × 100%

Expected: 80-85% overall
Acceptable: >75%
```
