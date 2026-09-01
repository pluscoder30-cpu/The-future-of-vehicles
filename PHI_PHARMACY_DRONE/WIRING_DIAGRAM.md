# PHI Pharmacy Drone - Wiring Diagram

## 1. Power Distribution

```
                         ┌───────────────────┐
                         │   FPB-5 BATTERY   │
                         │   5kWh 25.6V      │
                         └─────────┬─────────┘
                                   │
                   ┌───────────────┼───────────────┐
                   │               │               │
              ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
              │  MOTOR  │    │ SYSTEM  │    │  TEMP   │
              │  POWER  │    │ POWER   │    │ CONTROL │
              │  3kW    │    │ 1kW     │    │ 140W    │
              └────┬────┘    └────┬────┘    └────┬────┘
                   │              │              │
             25.6V Bus       12V Bus        12V Bus
                   │              │              │
          ┌────────┤         ┌────┤         ┌────┤
          │        │         │    │         │    │
     ┌────▼───┐ ┌──▼──┐  ┌──▼──┐ │      ┌──▼──┐ │
     │ 4x ESCs│ │ FC  │  │ ARM │ │      │Peltier│ │
     │ 45A    │ │     │  │ MCU │ │      │Heater │ │
     └────┬───┘ └─────┘  └─────┘ │      └─────┘ │
          │                       │              │
     ┌────▼───┐              ┌────▼──┐      ┌────▼──┐
     │ 4x     │              │ DISP. │      │ PHI   │
     │ MOTORS │              │  ARM  │      │HARMONIC│
     └────────┘              └───────┘      └───────┘
```

## 2. Temperature Control Wiring

```
┌──────────────────────────────────────────────────────────────┐
│              TEMPERATURE CONTROL SYSTEM                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  REFRIGERATED ZONE (2-8C)                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Peltier #1 ────► H-Bridge Driver ────► PWM Controller │  │
│  │ Peltier #2 ────► H-Bridge Driver ────► PWM Controller │  │
│  │ Fan #1 ────────► MOSFET Driver ──────► PWM Controller │  │
│  │ Fan #2 ────────► MOSFET Driver ──────► PWM Controller │  │
│  │ Temp Sensors (4x) ──► ADC Ch1-4 (10-bit)              │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  AMBIENT ZONE (15-25C)                                      │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Heater ────────► MOSFET Driver ──────► PWM Controller │  │
│  │ Temp Sensors (2x) ──► ADC Ch5-6 (10-bit)              │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  CONTROL (STM32F4)                                          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PID Loop: 1Hz update rate                              │  │
│  │ Peltier control: 0-100% duty cycle                    │  │
│  │ Heater control: 0-100% duty cycle                     │  │
│  │ Fan control: 0-100% duty cycle                        │  │
│  │ Alarm: Buzzer + LED on out-of-range                   │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 3. Medication Storage Wiring

```
┌──────────────────────────────────────────────────────────────┐
│              MEDICATION STORAGE SYSTEM                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  RFID READERS (20x)                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ RFID #1-10 ──────► RFID Multiplexer ──► I2C Bus       │  │
│  │ RFID #11-20 ─────► RFID Multiplexer ──► I2C Bus       │  │
│  │ Frequency: 13.56MHz                                    │  │
│  │ Protocol: ISO 15693 / ICode SLIX                       │  │
│  │ Read range: 0-5cm                                      │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  BARCODE SCANNERS (2x)                                      │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Scanner #1 (Loading) ──► UART1 @ 115200 baud          │  │
│  │ Scanner #2 (Dispensing) ► UART2 @ 115200 baud         │  │
│  │ Types: 1D (UPC, Code128) + 2D (QR, DataMatrix)       │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  TAMPER-EVIDENT LOCKS (20x)                                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Lock #1-20 ──────► I/O Expander (MCP23017) ──► I2C    │  │
│  │ Type: Electromagnetic solenoid                         │  │
│  │ Control: Power-off = locked                            │  │
│  │ Audit: Timestamp of every open/close                   │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  INVENTORY SENSORS                                          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Slot Presence (20x) ──► Digital Input (via MCP23017)  │  │
│  │ Weight Sensors (20x) ──► ADC (via multiplexer)        │  │
│  │ Status LED (20x) ──────► PWM (via PCA9685)           │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 4. Dispensing Arm Wiring

```
┌──────────────────────────────────────────────────────────────┐
│              DISPENSING ARM SYSTEM                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ARM JOINTS (4x Servos)                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Joint 1 (Base Rotation) ──► PWM Ch1 + Encoder         │  │
│  │ Joint 2 (Shoulder) ──────► PWM Ch2 + Encoder         │  │
│  │ Joint 3 (Elbow) ─────────► PWM Ch3 + Encoder         │  │
│  │ Joint 4 (Wrist) ─────────► PWM Ch4 + Encoder         │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  GRIPPER                                                    │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Gripper Motor ───────────► PWM Ch5 + Encoder          │  │
│  │ Force Sensor ────────────► ADC Ch7 (0-500g)           │  │
│  │ Presence Sensor ─────────► Digital Input               │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  CAMERA (Delivery Confirmation)                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Camera Module ──────────► USB / CSI                     │  │
│  │ Resolution: 5MP                                       │  │
│  │ Use: Photo confirmation of delivery                   │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ARM CONTROLLER (ESP32)                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PWM Outputs: 5x (4 joints + gripper)                  │  │
│  │ Encoder Inputs: 5x (SPI shift registers)             │  │
│  │ ADC: 1x (force sensor)                                │  │
│  │ Digital: 2x (presence, home switch)                   │  │
│  │ UART: 1x (barcode scanner)                            │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 5. Navigation & Communication

```
┌──────────────────────────────────────────────────────────────┐
│              NAVIGATION & COMMUNICATION                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  NAVIGATION SENSORS                                         │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ GPS (u-blox F9P) ──────► UART1 @ 460800 baud         │  │
│  │ IMU (ICM-42688-P) ─────► SPI1 @ 24MHz                │  │
│  │ Barometer (DPS310) ─────► I2C1 @ 400kHz              │  │
│  │ LiDAR (Livox Mid-360) ──► Ethernet @ 100Mbps         │  │
│  │ Camera Left ────────────► USB / CSI                    │  │
│  │ Camera Right ───────────► USB / CSI                    │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  COMMUNICATION                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 4G LTE Modem ──────────► USB ──► Flight Controller    │  │
│  │ WiFi Module ────────────► SPI ──► Backup link         │  │
│  │ GPS Antenna ────────────► SMA ──► GPS module          │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  FLIGHT CONTROLLER (Pixhawk 6C)                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PWM: CH1-4 (ESCs)                                     │  │
│  │ UART1: GPS                                             │  │
│  │ UART2: Safety Processor                                │  │
│  │ UART3: LTE Modem                                       │  │
│  │ SPI1: IMU                                              │  │
│  │ I2C1: Barometer                                        │  │
│  │ CAN1: ESCs (backup)                                    │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 6. Phi-Harmonic & Safety

```
┌──────────────────────────────────────────────────────────────┐
│              PHI-HARMONIC & SAFETY                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PHI-HARMONIC EMITTERS (2x)                                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Emitter #1 (Front) ──► Amplifier ──► Helmholtz Coil   │  │
│  │ Emitter #2 (Rear) ───► Amplifier ──► Helmholtz Coil   │  │
│  │ Control: DDS waveform via DAC                         │  │
│  │ Frequency: 1-100 Hz (adjustable)                      │  │
│  │ Default: 16.18 Hz (absorption)                        │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  SAFETY SYSTEMS                                             │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Parachute ────────────► Igniter ──► Safety Proc        │  │
│  │ Emergency Buzzer ──────► MOSFET ──► Safety Proc        │  │
│  │ Status LEDs (4x) ──────► PWM ────► Flight Controller  │  │
│  │ Emergency Stop Button ──► Digital Input ──► Safety Proc│  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  SAFETY PROCESSOR (STM32F4)                                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ Independent from Flight Controller                    │  │
│  │ Monitors: Motor health, battery, altitude             │  │
│  │ Can: Deploy parachute, activate buzzer, emergency land│  │
│  │ Watchdog: 100ms timeout                               │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```
