# PHI Surgical Assist Drone - Wiring Diagram

## 1. Power Distribution

```
                         ┌───────────────────┐
                         │   FPB-5 BATTERY   │
                         │   5kWh 25.6V      │
                         │   Inductive Dock  │
                         └─────────┬─────────┘
                                   │
                   ┌───────────────┼───────────────┐
                   │               │               │
              ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
              │  MOTOR  │    │ SYSTEM  │    │ MEDICAL │
              │  POWER  │    │ POWER   │    │ POWER   │
              │  2kW    │    │ 1kW     │    │ 0.5kW   │
              └────┬────┘    └────┬────┘    └────┬────┘
                   │              │              │
             25.6V Bus       25.6V Bus      25.6V Bus
                   │              │              │
          ┌────────┤         ┌────┤         ┌────┤
          │        │         │    │         │    │
     ┌────▼───┐ ┌──▼──┐  ┌──▼──┐ │      ┌──▼──┐ │
     │ 4x ESCs│ │ FC  │  │ ARM │ │      │UV-C │ │
     │ 50A    │ │     │  │ MCU │ │      │Array│ │
     └────┬───┘ └─────┘  └─────┘ │      └─────┘ │
          │                       │              │
     ┌────▼───┐              ┌────▼──┐      ┌────▼──┐
     │ 4x     │              │ 6-DOF │      │ PHI   │
     │ MOTORS │              │  ARM  │      │HARMONIC│
     └────────┘              └───────┘      └───────┘
```

## 2. Flight Controller Connections

```
┌──────────────────────────────────────────────────────────────┐
│                    PIXHAWK MINI                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  POWER INPUT (25.6V)           UART1 ──► EM Tracker          │
│  ┌─────────┐                   UART2 ──► Arm Controller      │
│  │ 25.6V   │                   UART3 ──► Safety Proc         │
│  │ → 5V    │                   SPI1 ──► Stereo Camera        │
│  │ → 3.3V  │                   SPI2 ──► IMU                   │
│  └─────────┘                   I2C1 ──► Barometer             │
│                                CAN1 ──► ESCs (4x)            │
│  PWM OUTPUTS                   ETH1 ──► Sterile Controller    │
│  ┌─────────┐                                               │
│  │ CH1: M1 │                   SAFETY                        │
│  │ CH2: M2 │                   ┌─────────┐                   │
│  │ CH3: M3 │                   │ AUX OUT │                   │
│  │ CH4: M4 │                   │ → Brake │                   │
│  └─────────┘                   │ → Dock  │                   │
│                                └─────────┘                   │
└──────────────────────────────────────────────────────────────┘
```

## 3. Robotic Arm Wiring

```
┌──────────────────────────────────────────────────────────────┐
│                   ARM CONTROLLER (STM32H7)                   │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  JOINT MOTORS (6x Servos)                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Joint 1 (Base) ────────► PWM Ch1 + Encoder             │  │
│  │ Joint 2 (Shoulder) ───► PWM Ch2 + Encoder             │  │
│  │ Joint 3 (Elbow) ──────► PWM Ch3 + Encoder             │  │
│  │ Joint 4 (Wrist Roll) ─► PWM Ch4 + Encoder             │  │
│  │ Joint 5 (Wrist Pitch) ► PWM Ch5 + Encoder             │  │
│  │ Joint 6 (Wrist Yaw) ──► PWM Ch6 + Encoder             │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  FORCE/TORQUE SENSOR                                        │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ F/T Sensor ───────────► SPI3 @ 1kHz sampling          │  │
│  │ 6-axis: Fx, Fy, Fz, Mx, My, Mz                       │  │
│  │ Resolution: 0.1N force, 0.01Nm torque                 │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  INSTRUMENT GRIPPER                                          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Gripper Motor ────────► PWM Ch7 + Encoder              │  │
│  │ Instrument Detect ────► 6x Digital Input               │  │
│  │ Grip Force Sensor ────► ADC Ch1                         │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  BRAKE CONTROL                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Brake Solenoid ───────► MOSFET Driver                  │  │
│  │ Brake Encoder ────────► Digital Input (position)       │  │
│  │ Fail-Safe: Power-off = Engaged                         │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  POWER: 12V from System Bus (10A max)                       │
│  DATA: UART to Flight Controller (arm status)               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 4. Sterile Field Wiring

```
┌──────────────────────────────────────────────────────────────┐
│                STERILE FIELD CONTROLLER (ESP32)              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  UV-C STERILIZATION                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ UV-C LEDs (12x) ──────► Constant Current Driver       │  │
│  │ Wavelength: 254nm     │ 40mW/cm2 per LED              │  │
│  │ Control: PWM dimming  │ Safety interlock               │  │
│  │ Timer: 30s sterilize  │ Auto-cycle between procedures  │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  IONIZATION                                                  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Ion Emitters (4x) ────► HV Driver (3kV)               │  │
│  │ Positive ion field     │ 10^6 ions/cm3                 │  │
│  │ Control: Analog        │ Continuous during operation   │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  HEPA FILTRATION                                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ HEPA Filter ──────────► Fan + Filter Monitor           │  │
│  │ Airflow: 100 CFM       │ Pressure differential sensor  │  │
│  │ Efficiency: 99.97%     │ Replace filter indicator      │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  PARTICLE SENSOR                                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Optical Particle Counter ──► I2C                        │  │
│  │ Detects: 0.3-10um particles                            │  │
│  │ Alert: >100 particles/m3                                │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 5. Phi-Harmonic Emitter Wiring

```
┌──────────────────────────────────────────────────────────────┐
│              PHI-HARMONIC CONTROLLER (ESP32)                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  HELMHOLTZ COIL PAIRS (4x)                                  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Coil Pair 1 (Front) ──► Amplifier Ch1 ──► Coil A+B   │  │
│  │ Coil Pair 2 (Right) ──► Amplifier Ch2 ──► Coil A+B   │  │
│  │ Coil Pair 3 (Rear) ───► Amplifier Ch3 ──► Coil A+B   │  │
│  │ Coil Pair 4 (Left) ───► Amplifier Ch4 ──► Coil A+B   │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  COIL SPECIFICATIONS                                        │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Core: Ferrite (mu_r = 2000)                            │  │
│  │ Turns: 300 per coil                                    │  │
│  │ Wire: 24 AWG copper                                    │  │
│  │ Current: 1A peak per coil                              │  │
│  │ Field: 0.3 mT at 15cm (center of pair)                 │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  CONTROL SIGNALS                                            │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ DAC Ch1-4 ────► Amplifiers (waveform generation)      │  │
│  │ I2C ───────────► Tissue impedance sensor               │  │
│  │ UART ──────────► Flight Controller (status)            │  │
│  │ Digital ───────► Emergency disable                      │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 6. Sensor Array Wiring

```
┌──────────────────────────────────────────────────────────────┐
│                    SENSOR CONNECTIONS                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  VISUAL SERVOING                                            │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Stereo Camera Left ────► Ethernet @ 1Gbps              │  │
│  │ Stereo Camera Right ───► Ethernet @ 1Gbps              │  │
│  │ Resolution: 1080p @ 100fps                              │  │
│  │ Stereo baseline: 60mm                                   │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ELECTROMAGNETIC TRACKING                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ EM Tracker Sensor ─────► UART @ 115200 baud            │  │
│  │ 6-DOF position + orientation                           │  │
│  │ Accuracy: 0.1mm / 0.1 degree                           │  │
│  │ Update rate: 100Hz                                      │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  INERTIAL MEASUREMENT                                       │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ IMU (ICM-42688-P) ────► SPI @ 24MHz                   │  │
│  │ 6-axis: Accel + Gyro                                   │  │
│  │ Update rate: 1kHz                                       │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  SAFETY SENSORS                                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Collision Sensor (IR) ──► Analog Ch1                    │  │
│  │ Arm Position Encoder ───► SPI4                          │  │
│  │ Brake Position ─────────► Digital Input                 │  │
│  │ Emergency Stop Button ──► Digital Input (pull-up)       │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 7. Ceiling Dock Connections

```
┌──────────────────────────────────────────────────────────────┐
│                CEILING DOCK SYSTEM                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  POWER (Inductive)                                          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ AC Mains ──► Rectifier ──► 25.6V DC ──► Coil ──► Dock │  │
│  │ Efficiency: 90%                                         │  │
│  │ Charging Rate: 2kW                                      │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  DATA (Optical)                                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Dock MCU ────► IR LED ────► Drone IR Receiver          │  │
│  │ Protocol: Custom (1Mbps)                                │  │
│  │ Data: Mission status, vitals, diagnostics              │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  MECHANICAL DOCKING                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Magnetic alignment (4x magnets)                        │  │
│  │ Positive locking (spring-loaded pins)                  │  │
│  │ Release: Electromagnetic (power-off = lock)            │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 8. Connector Specifications

| Connector | Type | Use | Current |
|-----------|------|-----|---------|
| XT30 | Power | Battery main | 30A |
| JST-SH | Signal | Servos, sensors | 2A |
| Molex Pico | Signal | Arm joints | 3A |
| RJ45 | Ethernet | Cameras | 0.5A |
| D-Sub 9 | CAN/Serial | CAN bus | 1A |
| USB-C | Data | Configuration | 3A |
| Magnetic | Dock | Ceiling mount | 50A |
| Optical | Data | Dock communication | N/A |
