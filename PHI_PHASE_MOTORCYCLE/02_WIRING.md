# PHI PHASE MOTORCYCLE — Wiring Diagram

## Main Power Distribution (96V DC System)

```
                    FPB-10 BATTERY (96V, 10kWh)
                    ============================
                          |         |
                     [MAIN CONTACTOR 100A]
                          |         |
                    [MAIN FUSE 80A]   [EMERGENCY FUSE 15A]
                          |                    |
                          |              [EMERGENCY RESERVE
                          |               96V, 750Wh]
                          |                    |
                    +-----+-----+              |
                    |           |              |
              [96V->72V]  [96V->12V]   [96V->12V]
              [DC-DC 3kW] [DC-DC 500W] [Emergency]
                    |           |              |
              +-----+     +----+----+         |
              |           |         |         |
         DRIVE BUS    AUX BUS   AUX BUS   AUX BUS
           72V        12V       12V       12V
              |           |         |         |
              |      [RPI ZERO]  [FUSE]   [SENSORS]
              |      [2W]        [BLOCK]
              |           |         |         |
              |      [DISPLAY]  [RELAY]   [LIGHTS]
              |      [5"]       [4CH]     [LED]
              |           |         |         |
              |      [GPS]     [KILL]    [BUZZER]
              |           |         |
              +--[MOTOR]  [ARDUINO] [OLCD]
              |  [CTRL]   [UNO]
              |  [72V]
              |     |
              |  [HUB MOTOR]
              |  [1500W]
              |     |
              +--[REGEN]
                 [RECOVERY]
```

## Phase Coil Wiring (6 Coils, Phi-Helical)

```
    PHASE COIL POWER BUS (96V, 5kW peak)
    =======================================
                        |
            +-----------+-----------+
            |                       |
      [COIL DRIVER]          [COIL DRIVER]
      [H-BRIDGE]            [H-BRIDGE]
      [2.5kW]               [2.5kW]
            |                       |
     +------+------+         +------+------+
     |      |      |         |      |      |
   [C1]  [C2]  [C3]       [C4]  [C5]  [C6]
   [FRONT]      [FRONT-R]  [REAR]  [REAR]  [REAR-R]
   [CENTER]     [137.5deg] [CENTER][275deg][45deg]

    COIL WINDING SPEC (per coil):
    -----------------------------
    - Litz Wire: 22 AWG, 90 turns
    - Ferrite Toroid Core: T82-2
    - Copper Foil Shield: 3" wrap
    - Capacitor Bank: 100pF ceramic + 0.05uF film
    - Resonance: 1.618 MHz (phi frequency)
```

## Signal & Control Wiring

```
    RASPBERRY PI ZERO 2W — Master Controller
    ==========================================
    |  |  |  |  |  |
    |  |  |  |  |  |
    |  |  |  |  |  +--[GPIO] [SPI] [I2C]
    |  |  |  |  |        |      |      |
    |  |  |  |  |   [ULTRASONIC] [GPS] [IMU]
    |  |  |  |  |   [x2]        [UART][I2C]
    |  |  |  |  |
    |  |  |  |  +--- 5" TOUCHSCREEN (HDMI/USB)
    |  |  |  |
    |  |  |  +------ WIFI (telemetry, OTA updates)
    |  |  +--------- SERIAL TO ARDUINO (USB)
    |  +------------ SD CARD (data logging)
    +--------------- POWER (5V from DC-DC)

    ARDUINO UNO — Safety & Low-Level Control
    ==========================================
    |  |  |  |  |  |  |
    |  |  |  |  |  |  |
    |  |  |  |  |  |  +--- CURRENT SENSOR ACS758
    |  |  |  |  |  +------ VOLTAGE DIVIDER
    |  |  |  |  +--------- TEMP SENSORS x2
    |  |  |  +------------ RELAY MODULE (4-ch)
    |  |  +--------------- MOTOR CONTROLLER
    |  +------------------ COIL DRIVERS x2
    +--------------------- PHASE BUTTON INPUT
                          KILL SWITCH INPUT
                          BRAKE SWITCH INPUT

    PI <-----> ARDUINO (USB Serial, 9600 baud)
    PI sends high-level commands, Arduino handles safety
```

## Motor Controller Wiring

```
    MOTOR CONTROLLER (72V, 60A)
    ============================
    +---[72V IN]---+
    |              |
    |  [CAP BANK]  |
    |    3x 470uF  |
    |              |
    +--[HALL SENSORS]---+
    |                   |
    +--[PHASE A]--------+---> MOTOR WINDING A
    |                   |
    +--[PHASE B]--------+---> MOTOR WINDING B
    |                   |
    +--[PHASE C]--------+---> MOTOR WINDING C
    |                   |
    +--[THROTTLE]-------+---> THROTTLE SIGNAL (0-5V)
    |                   |
    +--[BRAKE]----------+---> BRAKE SWITCH (NO)
    |                   |
    +--[ENABLE]---------+---> RELAY OUTPUT (Arduino)
    |                   |
    +--[FAULT]----------+---> LED / Arduino GPIO
    |
    +--[GND]------------+---> COMMON GROUND
```

## Emergency Circuit

```
    EMERGENCY KILL SWITCH (Keyed)
    =============================
    [MAIN CONTACTOR COIL]
           |
    [KILL SWITCH]---[BRAKE SWITCH]
           |               |
    [PARALLEL]---[EMERGENCY RELAY]
                       |
    [ARDUINO GPIO]-----+
    (reads state, triggers contactor drop)
    
    If kill switch opens OR Arduino detects fault:
    -> Contactor drops -> 96V disconnected
    -> Emergency reserve for brakes only
    -> Coils instantly de-energize (re-solidify)
```

## Phase Button Circuit

```
    PHASE ENGAGEMENT SEQUENCE
    ==========================
    
    [THROTTLE >50%]----+
                       |
    [PHASE BUTTON]-----+----[AND GATE]----[RELAY]----[COIL POWER]
    (left thumb)       |                  ENABLE
                       |
    [ARDUINO]----------+
    (monitors both, controls AND gate via relay)
    
    BOTH conditions must be true:
    1. Throttle twist > 50%
    2. Phase button held
    -> Arduino enables coil power relay
    -> Coils energize
    -> Phase state engaged
```

## Grounding Plan

```
    SINGLE POINT GROUND (frame)
    ============================
    All 12V grounds -> Star ground bolt on frame
    All signal grounds -> Frame via shield drain wires
    Battery negative -> Frame (10 AWG)
    Motor controller ground -> Frame (10 AWG)
    Pi/Arduino ground -> Frame (14 AWG)
    
    NO GROUND LOOPS. All returns go to ONE point.
```

## Connector Key

| Symbol | Connector Type |
|--------|---------------|
| [===] | XT90 (battery) |
| [=] | XT60 (motors, coils) |
| [..] | JST-XH (signals) |
| [--] | Anderson Powerpole (distribution) |
| [||] | Bullet 4mm (motor phase) |
