# PHI PHASE CAR — Wiring Diagram

## Main Power Distribution (144V DC System)

```
                    FPB-20 BATTERY (144V, 20kWh)
                    ============================
                          |         |
                     [MAIN CONTACTOR 200A]
                          |         |
                    [MAIN FUSE 100A]  [EMERGENCY FUSE 20A]
                          |                    |
                          |              [EMERGENCY RESERVE
                          |               144V, 1.5kWh]
                          |                    |
                    +-----+-----+              |
                    |           |              |
              [144V->72V]  [144V->12V]  [144V->12V]
              [DC-DC 6kW]  [DC-DC 2kW]  [Emergency]
                    |           |              |
              +-----+     +----+----+         |
              |           |         |         |
         DRIVE BUS    AUX BUS   AUX BUS   AUX BUS
           72V        12V       12V       12V
              |           |         |         |
    +---------+    +------+------+ |    +----+----+
    |         |    |      |      | |    |         |
  [FL]     [FR] [PI4]  [FUSE] [SENS] [KILL]  [LIGHTS]
  [MOTOR]  [MOTOR]      [BLOCK]                [12V]
    |         |    |      |      | |    |         |
    |      +--+----+------+------+-+----+----+    |
    |      |                        |    |    |    |
  [72V   [RL]                    [RELAY][OLCD][BUZZ]
  CTRL]  [MOTOR]                  [8CH] [1.3"]
    |      |                       |
    |    [RR]
    |    [MOTOR]
    |
  [REGEN]
  [RECOVERY]
```

## Phase Coil Wiring (12 Coils, Phi-Dodecahedral)

```
    PHASE COIL POWER BUS (144V, 8kW peak)
    =======================================
                        |
            +-----------+-----------+
            |           |           |
      [COIL DRIVER] [COIL DRIVER] [COIL DRIVER]
      [H-BRIDGE]   [H-BRIDGE]   [H-BRIDGE]
      [3kW]        [3kW]        [3kW]
            |           |           |
     +------+------+ +------+------+ +------+
     |      |      | |      |      | |      |
   [C1]  [C2]  [C3] [C4]  [C5]  [C6] [C7]  [C8]
   [FRONT-CENTER]  [SIDE-L] [SIDE-R] [REAR-CENTER]
   [137.5deg]     [275deg] [0deg]   [222.5deg]
     |      |      | |      |      | |      |
   [C9]  [C10] [C11] [C12]
   [FRONT-R]  [REAR-L] [REAR-R]
   [90deg]    [315deg] [45deg]

    COIL WINDING SPEC (per coil):
    -----------------------------
    - Litz Wire: 20 AWG, 120 turns
    - Ferrite Toroid Core: T106-2
    - Copper Foil Shield: 4" wrap
    - Capacitor Bank: 100pF ceramic + 0.1uF film
    - Resonance: 1.618 MHz (phi frequency)
```

## Signal & Control Wiring

```
    RASPBERRY PI 4 (8GB) — Master Controller
    ==========================================
    |  |  |  |  |  |  |  |  |  |  |
    |  |  |  |  |  |  |  |  |  |  |
    |  |  |  |  |  |  +  +--+--+  +--+
    |  |  |  |  |  |     |     |     |
    |  |  |  |  |  |  [GPIO] [SPI] [I2C]
    |  |  |  |  |  |     |     |     |
    |  |  |  |  |  |  +--+--+  |  +--+--+
    |  |  |  |  |  |  |  |  |  |  |  |  |
    |  |  |  |  |  +--+--+--+--+--+--+--+--+
    |  |  |  |  |     |  |  |  |  |  |  |  |
    |  |  |  |  +-----+--+--+--+--+--+--+--+--+
    |  |  |  |        |  |  |  |  |  |  |  |  |
    |  |  |  |     [7" TOUCHSCREEN — I2C/HDMI]
    |  |  |  |
    |  |  |  +--- ULTRASONIC x4 (GPIO TRIG/ECHO)
    |  |  +------ GPS MODULE (UART)
    |  +--------- IMU MPU-9250 (I2C)
    +------------ ETHERNET (W5500 shield)

    ARDUINO MEGA 2560 — Safety & Low-Level Control
    ================================================
    |  |  |  |  |  |  |  |  |  |
    |  |  |  |  |  |  |  |  |  |
    |  |  |  |  |  |  |  |  |  +--- CURRENT SENSOR ACS758 x2
    |  |  |  |  |  |  |  |  +------ VOLTAGE DIVIDER x2
    |  |  |  |  |  |  |  +--------- TEMP SENSORS x4
    |  |  |  |  |  |  +------------ RELAY MODULE (8-ch)
    |  |  |  |  |  +--------------- MOTOR CONTROLLERS x2
    |  |  |  |  +------------------ COIL DRIVERS x3
    |  |  |  +--------------------- PHASE BUTTON INPUT
    |  |  +------------------------ KILL SWITCH INPUT
    |  +--------------------------- SEATBELT SENSORS x4
    +------------------------------ COMM TO PI (Serial)

    PI <-----> ARDUINO (USB Serial, 115200 baud)
    PI sends commands, Arduino executes safety-critical ops
```

## Motor Controller Wiring (Per Wheel)

```
    MOTOR CONTROLLER (72V, 80A)
    ============================
    +---[72V IN]---+
    |              |
    |  [CAP BANK]  |
    |    4x 470uF  |
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
    [KILL SWITCH 1]---[KILL SWITCH 2]
           |                |
    [PARALLEL]---[EMERGENCY RELAY]
                       |
    [ARDUINO GPIO]-----+
    (reads state, triggers contactor drop)
    
    If either kill switch opens OR Arduino detects fault:
    -> Contactor drops -> All 144V disconnected
    -> Emergency reserve engages for steering/brakes
    -> Coils instantly de-energize (re-solidify)
```

## Grounding Plan

```
    SINGLE POINT GROUND (chassis)
    =============================
    All 12V grounds -> Star ground bolt on chassis rail
    All signal grounds -> Chassis via shield drain wires
    Battery negative -> Chassis (10 AWG)
    Motor controller grounds -> Chassis (10 AWG each)
    PI/Arduino ground -> Chassis (14 AWG)
    
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
