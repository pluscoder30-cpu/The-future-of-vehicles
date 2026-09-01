# PHI Medical Stretcher Drone - Wiring Diagram

## 1. Power Distribution

```
                           ┌─────────────────┐
                           │  FPB-20 BATTERY │
                           │  20kWh 51.2V    │
                           │  80kW Max       │
                           └────────┬────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
               ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
               │  MAIN   │    │ MEDICAL │    │ SAFETY  │
               │ POWER   │    │ POWER   │    │ POWER   │
               │ 120A    │    │ 20A     │    │ 10A     │
               └────┬────┘    └────┬────┘    └────┬────┘
                    │              │              │
              51.2V Bus       51.2V Bus      51.2V Bus
                    │              │              │
    ┌───────────────┼──────────────┼──────────────┤
    │               │              │              │
┌───▼───┐      ┌───▼───┐    ┌────▼────┐    ┌────▼────┐
│ 8x    │      │ FLIGHT│    │ MEDICAL │    │ PHI-    │
│ ESCs  │      │ CTRL  │    │ MCU     │    │ HARMONIC│
│ 15A   │      │ 5A    │    │ 2A      │    │ CTRL    │
│ EACH  │      │       │    │         │    │ 3A      │
└───┬───┘      └───────┘    └─────────┘    └─────────┘
    │
┌───▼───┐
│ 8x    │
│ MOTORS│
│ 15kW  │
│ EACH  │
└───────┘
```

## 2. Flight Controller Connections

```
┌──────────────────────────────────────────────────────────────┐
│                    PIXHAWK 6X                                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  POWER INPUT (51.2V)         UART1 ──► GPS #1 (u-blox)     │
│  ┌─────────┐                 UART2 ──► GPS #2 (u-blox)     │
│  │ 51.2V   │                 UART3 ──► Radio (900MHz)       │
│  │ → 12V   │                 UART4 ──► Safety Processor     │
│  │ → 5V    │                 UART5 ──► Telemetry (4G/5G)    │
│  └─────────┘                 UART6 ──► Medical MCU          │
│                                                              │
│  PWM OUTPUTS                   SPI1 ──► LiDAR (Livox)       │
│  ┌─────────┐                 SPI2 ──► IMU #1                │
│  │ CH1: M1 │                 SPI3 ──► IMU #2                │
│  │ CH2: M2 │                 I2C1 ──► Barometer #1          │
│  │ CH3: M3 │                 I2C2 ──► Barometer #2          │
│  │ CH4: M4 │                 I2C3 ──► Magnetometer          │
│  │ CH5: M5 │                 CAN1 ──► ESCs (8x)             │
│  │ CH6: M6 │                 CAN2 ──► Battery BMS           │
│  │ CH7: M7 │                 ETH1 ──► Camera (4K)           │
│  │ CH8: M8 │                                               │
│  └─────────┘                                               │
│                                                              │
│  SAFETY SWITCH                 USB ──► Configuration         │
│  ┌─────────┐                                               │
│  │ AUX OUT │                                               │
│  │ → Para  │                                               │
│  └─────────┘                                               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 3. Medical Systems Wiring

```
┌──────────────────────────────────────────────────────────────┐
│                   MEDICAL MCU (STM32F4)                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PATIENT SENSORS                                            │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ ECG Leads ──────► ADC Ch1 (24-bit, 1kHz)              │  │
│  │ SpO2 Probe ─────► ADC Ch2 (16-bit, 100Hz)             │  │
│  │ BP Cuff ────────► ADC Ch3 (16-bit, 50Hz)              │  │
│  │ Temp Probe ─────► ADC Ch4 (24-bit, 10Hz)              │  │
│  │ Resp Belt ──────► ADC Ch5 (16-bit, 100Hz)             │  │
│  │ EtCO2 Sensor ───► ADC Ch6 (16-bit, 50Hz)              │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  LIFE SUPPORT CONTROL                                       │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ O2 Valve ───────► PWM Ch1 (Flow control)              │  │
│  │ IV Pump ────────► PWM Ch2 (Rate control)              │  │
│  │ AED Trigger ────► Digital Out (Safety interlock)      │  │
│  │ Med Dispenser ──► I2C (Servo control)                 │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  DATA OUTPUT                                                │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ UART1 ──────► Flight Controller (Vital signs)         │  │
│  │ UART2 ──────► 4G Modem (Cloud upload)                 │  │
│  │ SPI1 ───────► Display (Patient info)                  │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  POWER: 5V from Medical Power Bus (20A max)                 │
│  GND: Common ground with Flight Controller                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 4. Phi-Harmonic Emitter Array

```
┌──────────────────────────────────────────────────────────────┐
│              PHI-HARMONIC CONTROLLER (ESP32)                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  FREQUENCY GENERATION                                       │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ DAC Ch1 ──► Amplifier ──► Emitter #1 (Front-Left)    │  │
│  │ DAC Ch2 ──► Amplifier ──► Emitter #2 (Front-Right)   │  │
│  │ DAC Ch3 ──► Amplifier ──► Emitter #3 (Right-Front)   │  │
│  │ DAC Ch4 ──► Amplifier ──► Emitter #4 (Right-Rear)    │  │
│  │ DAC Ch5 ──► Amplifier ──► Emitter #5 (Rear-Right)    │  │
│  │ DAC Ch6 ──► Amplifier ──► Emitter #6 (Rear-Left)     │  │
│  │ DAC Ch7 ──► Amplifier ──► Emitter #7 (Left-Rear)     │  │
│  │ DAC Ch8 ──► Amplifier ──► Emitter #8 (Left-Front)    │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  EMITTER SPECIFICATIONS                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Type: Helmholtz coil pair per emitter                 │  │
│  │ Core: Ferrite (μr = 2000)                             │  │
│  │ Turns: 500 per coil                                   │  │
│  │ Wire: 26 AWG copper                                   │  │
│  │ Current: 2A peak per emitter                          │  │
│  │ Field: 0.5 mT at 1m distance                         │  │
│  │ Frequency: 1-100 Hz (adjustable)                      │  │
│  │ Resonance: 16.18 Hz (φ × 10)                         │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  CONTROL SIGNALS                                            │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ UART ──────► Flight Controller (Patient state)        │  │
│  │ I2C ───────► Medical MCU (Vital signs)                │  │
│  │ SPI ───────► Emitter feedback sensors                 │  │
│  │ Digital ───► Emergency override                        │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  POWER: 12V from Medical Power Bus (5A max)                 │
│  GND: Common ground with Medical MCU                        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 5. Sensor Array Wiring

```
┌──────────────────────────────────────────────────────────────┐
│                    SENSOR CONNECTIONS                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  NAVIGATION SENSORS                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ GPS #1 (u-blox F9P) ──► UART1 @ 460800 baud          │  │
│  │ GPS #2 (u-blox F9P) ──► UART2 @ 460800 baud          │  │
│  │ IMU #1 (ICM-42688-P) ──► SPI1 @ 24MHz                │  │
│  │ IMU #2 (ICM-42688-P) ──► SPI2 @ 24MHz                │  │
│  │ IMU #3 (BMI088) ───────► SPI3 @ 20MHz                │  │
│  │ Baro #1 (DPS310) ──────► I2C1 @ 400kHz               │  │
│  │ Baro #2 (DPS310) ──────► I2C2 @ 400kHz               │  │
│  │ Magnetometer (RM3100) ──► I2C3 @ 400kHz               │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  OBSTACLE AVOIDANCE                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ LiDAR (Livox Mid-360) ──► Ethernet @ 100Mbps         │  │
│  │ Camera Front (4K) ──────► Ethernet @ 1Gbps            │  │
│  │ Camera Rear (4K) ───────► Ethernet @ 1Gbps            │  │
│  │ Camera Left (4K) ───────► Ethernet @ 1Gbps            │  │
│  │ Camera Right (4K) ──────► Ethernet @ 1Gbps            │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ENVIRONMENTAL                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Weather Radar ──────────► SPI4 @ 10MHz                │  │
│  │ Wind Sensor ────────────► Analog Ch1                   │  │
│  │ Humidity Sensor ────────► I2C4 @ 100kHz               │  │
│  │ Ambient Light ──────────► ADC Ch7                       │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 6. Safety & Redundancy Wiring

```
┌──────────────────────────────────────────────────────────────┐
│                  SAFETY SYSTEMS WIRING                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PARACHUTE DEPLOYMENT                                       │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Safety Processor ──► Igniter ──► Parachute            │  │
│  │                  (Ballistic deployment)                │  │
│  │ Deploy conditions:                                     │  │
│  │   - Altitude > 30m                                     │  │
│  │   - All motors failed                                  │  │
│  │   - Speed < 30 m/s                                     │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  EMERGENCY BUZZER                                           │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Safety Processor ──► Buzzer (120dB @ 1m)              │  │
│  │ Activate: Any critical fault                          │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  STATUS LIGHTS                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ LED Front (Red) ──────► PWM Ch9                        │  │
│  │ LED Rear (Green) ─────► PWM Ch10                       │  │
│  │ LED Left (Blue) ──────► PWM Ch11                       │  │
│  │ LED Right (Amber) ────► PWM Ch12                       │  │
│  │ Mode: Flash on error, solid on normal                  │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  BATTERY MONITORING                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ BMS CAN Bus ──────────► CAN2 on Flight Controller     │  │
│  │ Cell Voltages (16S) ──► Reported every 100ms          │  │
│  │ Current Sensor ────────► 200A hall effect              │  │
│  │ Temperature (4x) ──────► NTC 10K thermistors          │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 7. Ground Station Interface

```
┌──────────────────────────────────────────────────────────────┐
│              GROUND STATION CONNECTIONS                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PRIMARY: 4G/5G LTE                                        │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Drone 4G Modem ──► Cell Tower ──► Internet            │  │
│  │                                    └──► Cloud Server   │  │
│  │                                         └──► Web UI    │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  SECONDARY: 900 MHz Mesh                                    │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Drone Radio ──► Mesh Node ──► Base Station            │  │
│  │                                  └──► Local Server    │  │
│  │                                       └──► Monitor    │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  TERTIARY: Satellite (Iridium)                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Drone Sat Modem ──► Iridium SBD ──► Ground Station    │  │
│  │ (Emergency only, 2.4 kbps)                            │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 8. Connector Specifications

| Connector | Type | Pins | Current | Use |
|-----------|------|------|---------|-----|
| JST-XH | Servo | 3-6 | 3A | ESCs, servos |
| XT90 | Power | 2 | 90A | Battery main |
| AS150 | Power | 2 | 150A | Battery parallel |
| Molex Pico | Signal | 4-8 | 2A | Sensors |
| RJ45 | Ethernet | 8 | 0.5A | Cameras, LiDAR |
| D-Sub 9 | CAN/Serial | 9 | 1A | CAN bus |
| SMA | Coax | 1 | RF | Antennas |
| USB-C | Data | 24 | 3A | Configuration |
| MIL-DTL-38999 | Mil-Spec | 19-37 | 5A | Critical systems |
