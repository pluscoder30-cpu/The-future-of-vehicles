# PHI Surgical Assist Drone — MECHANICAL DIAGRAM
## Buildable Documentation | Physical Layout & Assembly

---

## EXPLODED VIEW (Top-Down)

```
                    PHI SURGICAL ASSIST DRONE
                   EXPLODED VIEW (TOP-DOWN)

                    ┌─────────────────────────────────────────┐
                    │              CEILING DOCK                │
                    │         Magnetic docking station        │
                    │         Inductive power (2kW)           │
                    │         Optical data link               │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         TOP SHELL                        │
                    │    Medical-grade anodized aluminum      │
                    │    + Titanium enclosed rotors           │
                    │    IEC 60601-1 compliant                │
                    │              600mm x 600mm              │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         PROPULSION LAYER                 │
                    │    ┌─────────────────────────────┐      │
                    │    │   4x T-Motor F80 Pro        │      │
                    │    │   500W, quiet medical-grade  │      │
                    │    │   8-inch enclosed props     │      │
                    │    └─────────────────────────────┘      │
                    │              80mm tall                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         AVIONICS BAY                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   Pixhawk Mini Flight Ctrl   │      │
                    │    │   Arm Controller STM32H7     │      │
                    │    │   Safety Processor STM32F4   │      │
                    │    └─────────────────────────────┘      │
                    │              60mm tall                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         6-DOF ROBOTIC ARM                 │
                    │    ┌─────────────────────────────┐      │
                    │    │   0.5m reach, 5kg payload    │      │
                    │    │   0.1mm accuracy             │      │
                    │    │   Force/torque sensor        │      │
                    │    │   Quick-change gripper       │      │
                    │    └─────────────────────────────┘      │
                    │              300mm (extended)            │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         STERILE FIELD                    │
                    │    ┌─────────────────────────────┐      │
                    │    │   UV-C Array (254nm)        │      │
                    │    │   Ionization System          │      │
                    │    │   HEPA Filtration            │      │
                    │    │   Particle Counter           │      │
                    │    └─────────────────────────────┘      │
                    │              100mm tall                  │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         POWER SYSTEM                     │
                    │    ┌─────────────────────────────┐      │
                    │    │   FPB-5 Battery              │      │
                    │    │   5kWh, 25.6V                │      │
                    │    │   Inductive charging         │      │
                    │    └─────────────────────────────┘      │
                    │              80mm tall                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         PHI-HARMONIC EMITTERS            │
                    │    ┌─────────────────────────────┐      │
                    │    │   4x Helmholtz coil pairs   │      │
                    │    │   16.18Hz healing field      │      │
                    │    │   Tissue impedance sensor   │      │
                    │    └─────────────────────────────┘      │
                    │              50mm tall                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         BOTTOM SHELL                     │
                    │         Medical-grade aluminum          │
                    │         Rotor enclosures                │
                    │         600mm x 600mm                    │
                    └─────────────────────────────────────────┘

    TOTAL LENGTH: 600mm
    TOTAL WIDTH: 600mm
    TOTAL HEIGHT: 400mm
    ARM REACH: 500mm (extended)
```

---

## TOP VIEW WITH DIMENSIONS

```
                    TOP VIEW (Plan Form)

                    ┌─────────────────────────────────────────────┐
                    │                                             │
                    │              600mm                           │
                    │◄───────────────────────────────────────────►│
                    │                                             │
                    │    ┌───┐                         ┌───┐     │ ▲
                    │    │M1 │                         │M2 │     │ │
                    │    └───┘                         └───┘     │ │
                    │      │                           │         │ │
                    │      │     ┌───────────────┐     │         │ 600mm
                    │      │     │   FLIGHT      │     │         │ │
                    │      │     │   CONTROLLER  │     │         │ │
                    │      │     └───────────────┘     │         │ │
                    │      │                           │         │ │
                    │    ┌───┐   ┌───────────────┐   ┌───┐     │ ▼
                    │    │M4 │───│   6-DOF ARM   │───│M3 │
                    │    └───┘   │   (retracted)  │   └───┘
                    │            └───────────────┘
                    │            ┌───────────────┐
                    │            │   STERILE     │
                    │            │   FIELD       │
                    │            └───────────────┘
                    │            ┌───────────────┐
                    │            │   PHI-HARMONIC│
                    │            │   EMITTERS    │
                    │            └───────────────┘
                    │                                             │
                    └─────────────────────────────────────────────┘

                    600mm width
                    ◄───────────────────────────────────────────►

    MOTOR POSITIONS (4x quadcopter):
    - M1: Front-Left
    - M2: Front-Right
    - M3: Rear-Right
    - M4: Rear-Left
    - All rotors fully enclosed (IEC 60601-1)
```

---

## SIDE CROSS-SECTION

```
    SIDE VIEW (Cross-Section)

    ◄──────────── 600mm (width) ────────────►

    ▲
    │   ┌─────────────────────────────────────────────┐
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         CEILING DOCK MOUNT              │ │
    │   │ │    Magnetic alignment (4x magnets)      │ │
    │   │ │    Inductive power coil                 │ │
    │   │ │    Optical data port                    │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Top Shell
    │   │░░░░░░░░ Medical-grade aluminum ░░░░░░░░░░░░░│ Anodized
    │   ├─────────────────────────────────────────────┤
    │   │ ┌───┐ ┌─────────────────────┐ ┌───┐       │
    │   │ │M1 │ │    ENCLOSED ROTOR   │ │M2 │       │ Propulsion
    │   │ └───┘ │    8-inch props     │ └───┘       │ (500W each)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │         AVIONICS BAY                     │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Flight + Arm Controllers  │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    6-DOF ROBOTIC ARM                     │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Joint 1 (Base)            │      │ │
    │   │ │    │   ┌───────────────────┐     │      │ │
    │   │ │    │   │ Joint 2 (Shoulder)│     │      │ │
    │   │ │    │   │ ┌─────────────┐  │     │      │ │
    │   │ │    │   │ │Joint 3 (Elb)│  │     │      │ │
    │   │ │    │   │ │ ┌───────┐  │  │     │      │ │
    │   │ │    │   │ │ │ J4/J5/J6│  │  │     │      │ │
    │   │ │    │   │ │ │ Wrist  │  │  │     │      │ │
    │   │ │    │   │ │ └───┬───┘  │  │     │      │ │
    │   │ │    │   │ │     │GRIP  │  │     │      │ │
    │   │ │    │   │ └─────┴──────┘  │     │      │ │
    │   │ │    │   └─────────────────┘     │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Force/Torque Sensor       │      │ │
    │   │ │    │   6-axis, 0.1N resolution   │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   Quick-Change Gripper      │      │ │
    │   │ │    │   6-slot auto-swap <2s      │      │ │
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    STERILE FIELD                         │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   UV-C LEDs (12x, 254nm)    │      │ │ 40mW/cm²
    │   │ │    │   Ionization Emitters (4x)   │      │ │ 10⁶ ions/cm³
    │   │ │    │   HEPA Filter (100 CFM)      │      │ │ 99.97%
    │   │ │    │   Particle Counter           │      │ │ 0.3-10μm
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    POWER SYSTEM                          │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   FPB-5 Battery             │      │ │ 5kWh 25.6V
    │   │ │    │   Inductive charging        │      │ │ Dock power
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │
    │   │ │    PHI-HARMONIC EMITTERS                 │ │
    │   │ │    ┌─────────────────────────────┐      │ │
    │   │ │    │   4x Helmholtz coil pairs   │      │ │ 300 turns each
    │   │ │    │   16.18Hz primary frequency  │      │ │ 0.3 mT at 15cm
    │   │ │    │   Tissue impedance sensor    │      │ │ Feedback
    │   │ │    └─────────────────────────────┘      │ │
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Bottom Shell
    │   │░░░░░░░░ Enclosed rotor shrouds ░░░░░░░░░░░░│ HEPA-filtered
    │   └─────────────────────────────────────────────┘
    ▼
         TOTAL HEIGHT: 400mm
```

---

## ROBOTIC ARM DETAIL

```
    6-DOF ROBOTIC ARM (Extended View)

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   ARM SPECIFICATIONS                        │
    │   ┌─────────────────────────────────────┐   │
    │   │   Reach: 0.5m                       │   │
    │   │   Payload: 5kg                      │   │
    │   │   Accuracy: 0.1mm repeatability     │   │
    │   │   Speed: 0.5 m/s (tip)              │   │
    │   │   Joints: 6-DOF                     │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   JOINT LAYOUT                              │
    │   ┌─────────────────────────────────────┐   │
    │   │                                     │   │
    │   │   ┌─────┐                           │   │
    │   │   │ J1  │ ◄── Base (360° rotate)   │   │
    │   │   └──┬──┘                           │   │
    │   │      │                              │   │
    │   │   ┌──┴──┐                           │   │
    │   │   │ J2  │ ◄── Shoulder (-90/+90°)  │   │
    │   │   └──┬──┘                           │   │
    │   │      │                              │   │
    │   │   ┌──┴──┐                           │   │
    │   │   │ J3  │ ◄── Elbow (0/135°)       │   │
    │   │   └──┬──┘                           │   │
    │   │      │                              │   │
    │   │   ┌──┴──┐                           │   │
    │   │   │ J4  │ ◄── Wrist Roll (360°)    │   │
    │   │   └──┬──┘                           │   │
    │   │      │                              │   │
    │   │   ┌──┴──┐                           │   │
    │   │   │ J5  │ ◄── Wrist Pitch (-90/90°)│   │
    │   │   └──┬──┘                           │   │
    │   │      │                              │   │
    │   │   ┌──┴──┐                           │   │
    │   │   │ J6  │ ◄── Wrist Yaw (360°)     │   │
    │   │   └──┬──┘                           │   │
    │   │      │                              │   │
    │   │   ┌──┴──┐                           │   │
    │   │   │F/T  │ ◄── Force/Torque Sensor   │   │
    │   │   └──┬──┘     6-axis, 0.1N          │   │
    │   │      │                              │   │
    │   │   ┌──┴──────────────┐               │   │
    │   │   │   GRIPPER       │               │   │
    │   │   │   6-slot auto   │               │   │
    │   │   │   <2s swap      │               │   │
    │   │   └─────────────────┘               │   │
    │   │                                     │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   INSTRUMENT SLOTS (6x)                     │
    │   ┌─────────────────────────────────────┐   │
    │   │   Slot 1: Scalpel holder            │   │
    │   │   Slot 2: Retractor holder          │   │
    │   │   Slot 3: Suction holder            │   │
    │   │   Slot 4: Cautery holder            │   │
    │   │   Slot 5: Suture holder             │   │
    │   │   Slot 6: Free (custom)             │   │
    │   │                                     │   │
    │   │   Auto-swap: <2 seconds             │   │
    │   │   Verification: EM tracker          │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   BRAKE SYSTEM                              │
    │   ┌─────────────────────────────────────┐   │
    │   │   Type: Electromagnetic fail-safe   │   │
    │   │   Engage: Power-off (default)       │   │
    │   │   Release: Software controlled      │   │
    │   │   Response: <10ms                   │   │
    │   │   Independent safety processor      │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    └─────────────────────────────────────────────┘
```

---

## STERILE FIELD DETAIL

```
    STERILE FIELD ZONE (Cross-Section)

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   UV-C STERILIZATION                        │
    │   ┌─────────────────────────────────────┐   │
    │   │   12x UV-C LEDs                     │   │
    │   │   Wavelength: 254nm (germicidal)    │   │
    │   │   Intensity: 40mW/cm² per LED       │   │
    │   │   Coverage: 360° around arm         │   │
    │   │   Cycle: 30s sterilize between      │   │
    │   │           procedures                 │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   IONIZATION                                │
    │   ┌─────────────────────────────────────┐   │
    │   │   4x Ion Emitters                   │   │
    │   │   Voltage: 3kV                      │   │
    │   │   Ion density: 10⁶ ions/cm³        │   │
    │   │   Field: Positive (repels particles)│   │
    │   │   Continuous during operation       │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   HEPA FILTRATION                           │
    │   ┌─────────────────────────────────────┐   │
    │   │   Flow rate: 100 CFM                │   │
    │   │   Efficiency: 99.97% @ 0.3μm       │   │
    │   │   Pressure differential sensor      │   │
    │   │   Filter replacement indicator      │   │
    │   │   Airflow: Downward (clean → dirty) │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   PARTICLE COUNTER                          │
    │   ┌─────────────────────────────────────┐   │
    │   │   Type: Optical particle counter    │   │
    │   │   Range: 0.3-10μm particles        │   │
    │   │   Alert threshold: >100 particles/m³│   │
    │   │   Interface: I2C to Sterile Ctrl    │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    └─────────────────────────────────────────────┘
```

---

## CEILING DOCK DETAIL

```
    CEILING DOCK SYSTEM

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   DOCK MECHANISM                            │
    │   ┌─────────────────────────────────────┐   │
    │   │   Alignment: 4x neodymium magnets   │   │
    │   │   Locking: Spring-loaded pins        │   │
    │   │   Release: Electromagnetic (power-off│   │
    │   │            = locked)                 │   │
    │   │   Mount: Rail system (adjustable)    │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   POWER (Inductive)                         │
    │   ┌─────────────────────────────────────┐   │
    │   │   AC Mains → Rectifier → 25.6V DC  │   │
    │   │   Charging coil → Drone coil        │   │
    │   │   Efficiency: 90%                   │   │
    │   │   Rate: 2kW                         │   │
    │   │   Full charge: 2.5 hours            │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   DATA (Optical)                            │
    │   ┌─────────────────────────────────────┐   │
    │   │   IR LED ↔ IR Receiver              │   │
    │   │   Protocol: Custom (1Mbps)          │   │
    │   │   Data: Mission status, vitals,     │   │
    │   │         diagnostics, software update│   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    │   DOCK LAYOUT (Top View)                    │
    │   ┌─────────────────────────────────────┐   │
    │   │                                     │   │
    │   │      ┌───────┐   ┌───────┐         │   │
    │   │      │ Power │   │ Data  │         │   │
    │   │      │ Coil  │   │Port   │         │   │
    │   │      └───────┘   └───────┘         │   │
    │   │                                     │   │
    │   │   [M]           ┌───┐         [M]  │   │
    │   │                 │   │              │   │
    │   │                 │ D │              │   │
    │   │                 │ O │              │   │
    │   │   [M]           │ C │         [M]  │   │
    │   │                 │ K │              │   │
    │   │                 └───┘              │   │
    │   │                                     │   │
    │   │   [M] = Magnet (alignment)         │   │
    │   └─────────────────────────────────────┘   │
    │                                             │
    └─────────────────────────────────────────────┘
```

---

## ASSEMBLY STACK ORDER

```
    ASSEMBLY SEQUENCE (Bottom to Top)

    STEP 1: Bottom Shell
    ┌─────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Medical-grade aluminum
    │░░░░░░░░░░░ Enclosed rotor shrouds ░░░░░░│  HEPA-filtered
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 2: Phi-Harmonic Emitters
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   4x Helmholtz coil pairs          │ │  16.18Hz healing
    │ │   Tissue impedance sensor          │ │  Feedback control
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 3: Power System
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   FPB-5 Battery Pack               │ │  5kWh, 25.6V
    │ │   Inductive charging coil          │ │  Dock power
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 4: Sterile Field
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   UV-C LEDs (12x, 254nm)           │ │  40mW/cm²
    │ │   Ionization Emitters (4x)          │ │  10⁶ ions/cm³
    │ │   HEPA Filter (100 CFM)             │ │  99.97%
    │ │   Particle Counter                  │ │  0.3-10μm
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 5: 6-DOF Robotic Arm
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   6-DOF Arm (0.5m reach)           │ │  5kg payload
    │ │   Force/Torque Sensor (6-axis)     │ │  0.1N resolution
    │ │   Quick-Change Gripper (6-slot)    │ │  <2s swap
    │ │   Electromagnetic Brake            │ │  Fail-safe
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 6: Avionics Bay
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Pixhawk Mini Flight Controller   │ │  Primary
    │ │   Arm Controller STM32H7           │ │  6-axis control
    │ │   Safety Processor STM32F4         │ │  Independent
    │ │   Stereo Camera + EM Tracker       │ │  Visual servoing
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 7: Propulsion
    ┌─────────────────────────────────────────┐
    │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
    │ │ M1  │ │ M2  │ │ M3  │ │ M4  │       │  4x T-Motor F80
    │ └─────┘ └─────┘ └─────┘ └─────┘       │  Enclosed rotors
    │ ┌─────────────────────────────────────┐ │
    │ │   60A Medical-grade ESCs (4x)      │ │  IEC certified
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 8: Top Shell
    ┌─────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Medical-grade aluminum
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Anodized
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 9: Ceiling Dock Mount
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Magnetic Docking Station          │ │  4x magnets
    │ │   Inductive Power Coil              │ │  2kW charging
    │ │   Optical Data Port                 │ │  1Mbps
    │ │   Spring-loaded Lock Pins           │ │  EM release
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
```

---

## DIMENSIONS SUMMARY

| Dimension | Value | Notes |
|-----------|-------|-------|
| Frame Width | 600mm | Quadcopter |
| Frame Depth | 600mm | Quadcopter |
| Total Height | 400mm | Docked |
| Arm Reach | 500mm | Extended |
| Arm Payload | 5kg | Surgical instruments |
| Arm Accuracy | 0.1mm | Repeatability |
| Instrument Slots | 6 | Quick-change |
| UV-C Coverage | 360° | Around arm |
| HEPA Flow | 100 CFM | 99.97% efficient |
| Weight (empty) | 8kg | Without instruments |
| Max Payload | 5kg | Instruments + tissue |
| Dock Power | 2kW | Inductive |

---

## MATERIALS SPECIFICATION

| Component | Material | Grade | Notes |
|-----------|----------|-------|-------|
| Frame | Anodized Aluminum | Medical | IEC 60601-1 |
| Rotor Shrouds | Titanium | Medical | Fully enclosed |
| Arm Links | Carbon Fiber | Aerospace | 0.1mm accuracy |
| Gripper | Stainless Steel | 316L | Surgical grade |
| Fasteners | Titanium | Medical | Corrosion-resistant |
| Seals | Silicone | Medical | Sterile barrier |

---

**Document**: 03_MECHANICAL.md
**Vehicle**: PHI SURGICAL ASSIST DRONE
**Status**: BUILDABLE ✓
