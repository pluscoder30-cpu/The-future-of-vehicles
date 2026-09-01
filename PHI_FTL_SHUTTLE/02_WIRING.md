# PHI FTL SHUTTLE — WIRING DIAGRAM
## Buildable Documentation | Electrical Connections

---

## SYSTEM OVERVIEW

```
                    ┌─────────────────────────────────────────────────┐
                    │              PHI FTL SHUTTLE                     │
                    │                                                 │
                    │  ┌─────────────────────────────────────────┐   │
                    │  │         FLIGHT COMPUTER (x3)            │   │
                    │  │  Triple-redundant, voting logic         │   │
                    │  │  CAN bus interconnect                   │   │
                    │  └─────────────────────────────────────────┘   │
                    │                    │                            │
                    │                    │ CAN Bus (MIL-STD-1553)    │
                    │                    │                            │
                    │  ┌─────────────────┼────────────────────────┐  │
                    │  │                 │                        │  │
                    │  │  ┌──────────────┴──────────┐            │  │
                    │  │  │    WARP SUBSYSTEM        │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Warp Bubble Ctrl   │  │            │  │
                    │  │  │  │ (triple-redundant) │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Resonance Stabilizer│  │            │  │
                    │  │  │  │ (phi-feedback)      │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Dimensional Tuner   │  │            │  │
                    │  │  │  │ (7-band selector)   │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  └──────────────────────────┘            │  │
                    │  │                                           │  │
                    │  │  ┌──────────────┴──────────┐            │  │
                    │  │  │    PROPULSION            │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Metric Contraction  │  │            │  │
                    │  │  │  │ Emitters (4x)       │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Metric Expansion    │  │            │  │
                    │  │  │  │ Emitters (4x)       │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Warp Plasma Injectors│  │            │  │
                    │  │  │  │ (8x phi-harmonic)   │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  └──────────────────────────┘            │  │
                    │  │                                           │  │
                    │  │  ┌──────────────┴──────────┐            │  │
                    │  │  │    POWER SYSTEM          │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ FPB-100 x4          │  │            │  │
                    │  │  │  │ (400 kWh total)     │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ 100V Power Bus      │  │            │  │
                    │  │  │  │ (1000A rated)       │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  └──────────────────────────┘            │  │
                    │  │                                           │  │
                    │  │  ┌──────────────┴──────────┐            │  │
                    │  │  │    NAVIGATION            │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Warp Radar          │  │            │  │
                    │  │  │  │ (light-cone mapping)│  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Star Trackers (x2)  │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  │  ┌────────────────────┐  │            │  │
                    │  │  │  │ Fiber-Optic IMU     │  │            │  │
                    │  │  │  └────────────────────┘  │            │  │
                    │  │  └──────────────────────────┘            │  │
                    │  └──────────────────────────────────────────┘  │
                    └─────────────────────────────────────────────────┘
```

---

## POWER DISTRIBUTION

```
                    ┌─────────────────────────────────────────────────┐
                    │           POWER FLOW DIAGRAM                     │
                    │                                                 │
                    │   FPB-100 x4 (100V, 100Ah each)                │
                    │   Total: 100V, 400Ah (40,000Wh = 400kWh)       │
                    │                    │                           │
                    │                    ▼                           │
                    │              100V POWER BUS                    │
                    │              (1000A rated)                     │
                    │                    │                           │
                    │     ┌──────────────┼──────────────┐           │
                    │     │              │              │           │
                    │     ▼              ▼              ▼           │
                    │ ┌────────┐   ┌────────┐   ┌────────┐         │
                    │ │ WARP   │   │PROPULS.│   │AVIONICS│         │
                    │ │ 800A   │   │ 150A   │   │  50A   │         │
                    │ └────────┘   └────────┘   └────────┘         │
                    │                                                 │
                    │   DC-DC Conversion:                            │
                    │   100V → 28V (avionics)                       │
                    │   100V → 12V (sensors)                        │
                    │   100V → 5V (computers)                       │
                    │                                                 │
                    │   Runtime: 400kWh / 100kW = 4 hours at warp   │
                    └─────────────────────────────────────────────────┘
```

### Battery Connections

```
FPB-100 Battery Pack (x4)
    │
    ├──[Anderson 600A]──┐
    │                    │
    │    ┌───────────────┴───────────────┐
    │    │      100V POWER BUS           │
    │    │      (1000A rated bus bar)    │
    │    └───┬───────────┬───────────┬───┘
    │        │           │           │
    │        ▼           ▼           ▼
    │   ┌─────────┐ ┌─────────┐ ┌─────────┐
    │   │ WARP    │ │PROPULS. │ │AVIONICS │
    │   │ 800A    │ │ 150A    │ │  50A    │
    │   └─────────┘ └─────────┘ └─────────┘
    │
    ├──[BMS x4]──► Cell Balancing
    │              (25S configuration)
    │
    └──[CCS2]──► Charging (100kW DC fast charge)
```

---

## WARP SUBSYSTEM WIRING

### Warp Bubble Controller

```
Warp Bubble Controller (Triple-Redundant)     CAN Bus
┌─────────────────────────────────────────┐   │
│  PRIMARY CONTROLLER                     │   │
│  ┌───────────────────────────────────┐  │   │
│  │  Main CPU: FPGA (Xilinx Artix-7) │  │───┤
│  │  Backup CPU: ARM Cortex-M7        │  │   │
│  │  Voting Logic: Triple Modular     │  │   │
│  │  CAN TX/RX: MIL-STD-1553         │  │   │
│  └───────────────────────────────────┘  │   │
│                                         │   │
│  WARP BUBBLE OUTPUTS                    │   │
│  ┌───────────────────────────────────┐  │   │
│  │  Field Emitter Control (12x)     │  │───┤
│  │  120° arc coverage per emitter   │  │   │
│  │  Control: 100kHz PWM             │  │   │
│  └───────────────────────────────────┘  │   │
│                                         │   │
│  STABILIZER INTERFACE                   │   │
│  ┌───────────────────────────────────┐  │   │
│  │  Resonance Feedback: SPI @ 1MHz  │  │───┤
│  │  Phase Lock: Digital (triple)    │  │   │
│  │  Emergency Shutdown: Hardwired   │  │   │
│  └───────────────────────────────────┘  │   │
│                                         │   │
│  CHRONOLOGY PROTECTION                  │   │
│  ┌───────────────────────────────────┐  │   │
│  │  CTC Detector: Analog Front-End  │  │───┤
│  │  Shutdown Relay: Hardwired       │  │   │
│  │  Response Time: <1μs             │  │   │
│  └───────────────────────────────────┘  │   │
│                                         │   │
│  POWER: 100V direct from bus            │   │
│  CURRENT: 200A max during formation     │   │
└─────────────────────────────────────────┘
```

### Field Emitter Nodes (12x)

```
Field Emitter Node (per node)
┌─────────────────────────────────────────┐
│  HIGH-VOLTAGE POWER STAGE               │
│  ┌───────────────────────────────────┐  │
│  │  100V Bus → H-Bridge → Coil      │  │
│  │  Current: 50A peak per emitter    │  │
│  │  Switching: 100kHz MOSFETs       │  │
│  └───────────────────────────────────┘  │
│                                         │
│  COIL ASSEMBLY                          │
│  ┌───────────────────────────────────┐  │
│  │  Superconducting coil (NbTi)     │  │
│  │  Turns: 2000 per emitter         │  │
│  │  Current: 50A (cryo-cooled)      │  │
│  │  Field: 10T peak at coil center  │  │
│  └───────────────────────────────────┘  │
│                                         │
│  CONTROL INTERFACE                      │
│  ┌───────────────────────────────────┐  │
│  │  CAN: From Warp Bubble Controller│  │
│  │  Feedback: Hall sensor (position)│  │
│  │  Temp: Cryocooler sensor         │  │
│  └───────────────────────────────────┘  │
│                                         │
│  12 EMITTERS IN 120° ARC:              │
│  ┌───────────────────────────────────┐  │
│  │        FRONT (120°)              │  │
│  │   E1    E2    E3    E4           │  │
│  │    \    |    |    /              │  │
│  │     \   |    |   /               │  │
│  │      \  |    |  /                │  │
│  │   E12--[SHUTTLE]--E5             │  │
│  │      /  |    |  \                │  │
│  │     /   |    |   \               │  │
│  │    /    |    |    \              │  │
│  │   E11   E10   E9   E8   E7  E6  │  │
│  │        REAR (240°)               │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### Warp Coil Array (8x)

```
Warp Coil (per coil)
┌─────────────────────────────────────────┐
│  SUPERCONDUCTING COIL                   │
│  ┌───────────────────────────────────┐  │
│  │  Material: NbTi (Niobium-Titanium)│  │
│  │  Diameter: 800mm                  │  │
│  │  Turns: 5000 per coil             │  │
│  │  Current: 200A (cryo-cooled)      │  │
│  │  Field: 5T at coil center         │  │
│  │  Resonance: 432Hz (phi-harmonic)  │  │
│  └───────────────────────────────────┘  │
│                                         │
│  CRYOCOOLER                             │
│  ┌───────────────────────────────────┐  │
│  │  Type: Pulse-tube (closed cycle)  │  │
│  │  Temperature: 4.2K (liquid He)    │  │
│  │  Power: 2kW per cooler            │  │
│  │  Cool-down time: 4 hours          │  │
│  └───────────────────────────────────┘  │
│                                         │
│  POWER CONNECTIONS                      │
│  ┌───────────────────────────────────┐  │
│  │  100V Bus → Current Regulator     │  │
│  │  → Superconducting Coil           │  │
│  │  Cryocooler: 100V → 5V (local)   │  │
│  └───────────────────────────────────┘  │
│                                         │
│  8 COILS IN PHI-PATTERN:               │
│  ┌───────────────────────────────────┐  │
│  │          FRONT                    │  │
│  │      C1       C2                  │  │
│  │        \     /                    │  │
│  │    C8---[SHUTTLE]---C3            │  │
│  │        /     \                    │  │
│  │      C7       C4                  │  │
│  │     C6         C5                 │  │
│  │          REAR                     │  │
│  │                                   │  │
│  │  Spacing: φ-harmonic (golden)     │  │
│  │  8 coils at 45° intervals         │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## PROPULSION WIRING

### Metric Contraction/Expansion Emitters

```
Metric Emitter (per emitter, 8 total)
┌─────────────────────────────────────────┐
│  EMITTER COIL                           │
│  ┌───────────────────────────────────┐  │
│  │  Superconducting solenoid         │  │
│  │  Turns: 3000                      │  │
│  │  Current: 100A                    │  │
│  │  Field: 3T peak                   │  │
│  └───────────────────────────────────┘  │
│                                         │
│  POWER STAGE                            │
│  ┌───────────────────────────────────┐  │
│  │  100V Bus → IGBT H-Bridge         │  │
│  │  Switching: 50kHz                 │  │
│  │  Current: 100A peak               │  │
│  │  Cooling: Liquid nitrogen jacket  │  │
│  └───────────────────────────────────┘  │
│                                         │
│  CONTROL                                │
│  ┌───────────────────────────────────┐  │
│  │  CAN from Flight Computer        │  │
│  │  Current feedback: Hall sensor    │  │
│  │  Temperature: RTD sensor          │  │
│  └───────────────────────────────────┘  │
│                                         │
│  LAYOUT:                                │
│  ┌───────────────────────────────────┐  │
│  │   CONTRACTION (Front)  EXPANSION │  │
│  │   C1  C2  C3  C4      E1  E2  E3  E4│
│  │    \  |  |  /          /  |  |  \│  │
│  │     [SHUTTLE FRONT]   [SHUTTLE REAR]│  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## NAVIGATION & AVIONICS WIRING

### Flight Computer (Triple-Redundant)

```
Flight Computer (per unit, 3 total)
┌─────────────────────────────────────────┐
│  CPU: ARM Cortex-A72 (quad-core)        │
│  RAM: 8GB DDR4                          │
│  Storage: 256GB NVMe                    │
│  CAN Bus: 2x MIL-STD-1553              │
│  Ethernet: 2x 1Gbps                     │
│  Serial: 8x UART                        │
│                                         │
│  INTERFACES:                            │
│  ┌───────────────────────────────────┐  │
│  │  CAN1 ──► Warp Bubble Controller │  │
│  │  CAN2 ──► Propulsion / Power     │  │
│  │  ETH1 ──► Warp Radar             │  │
│  │  ETH2 ──► Star Tracker           │  │
│  │  SPI1 ──► IMU                     │  │
│  │  UART1──► Navigation Display     │  │
│  │  UART2──► Communications Array   │  │
│  │  USB  ──► Control Stick          │  │
│  └───────────────────────────────────┘  │
│                                         │
│  TRIPLE VOTING:                         │
│  ┌───────────────────────────────────┐  │
│  │  FC1 ──┐                          │  │
│  │  FC2 ──┼──► Voting Logic ──► Action│  │
│  │  FC3 ──┘    (2-of-3)             │  │
│  │                                   │  │
│  │  If FC disagrees:                 │  │
│  │  1. Log fault                     │  │
│  │  2. Isolate faulty FC             │  │
│  │  3. Continue with 2 FCs           │  │
│  │  4. If 2 disagree: EMERGENCY STOP │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### Warp Radar System

```
Warp Radar (Light-Cone Mapping)
┌─────────────────────────────────────────┐
│  RADAR ANTENNA                          │
│  ┌───────────────────────────────────┐  │
│  │  Phased array: 64 elements       │  │
│  │  Frequency: 1-10 GHz             │  │
│  │  Beamforming: Digital             │  │
│  │  Range: 10 light-minutes          │  │
│  └───────────────────────────────────┘  │
│                                         │
│  PROCESSING                             │
│  ┌───────────────────────────────────┐  │
│  │  FPGA: Xilinx Kintex UltraScale  │  │
│  │  Light-cone computation           │  │
│  │  Causal boundary detection        │  │
│  └───────────────────────────────────┘  │
│                                         │
│  INTERFACE                              │
│  ┌───────────────────────────────────┐  │
│  │  ETH1 ──► Flight Computer        │  │
│  │  CAN1  ──► Warp Bubble Controller│  │
│  │  Power: 100V → 28V (local DC-DC) │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## CABIN & PASSENGER WIRING

### Life Support System

```
Life Support System
┌─────────────────────────────────────────┐
│  O2 GENERATION                          │
│  ┌───────────────────────────────────┐  │
│  │  O2 Tank: 3000 PSI, 50L          │  │
│  │  Regulator: 2-stage               │  │
│  │  Flow: 2L/min per passenger       │  │
│  │  Duration: 8 hours (4 passengers) │  │
│  └───────────────────────────────────┘  │
│                                         │
│  CO2 SCRUBBING                          │
│  ┌───────────────────────────────────┐  │
│  │  LiOH canisters (4x)             │  │
│  │  Capacity: 8 hours               │  │
│  │  Monitor: CO2 sensor (NDIR)      │  │
│  └───────────────────────────────────┘  │
│                                         │
│  TEMPERATURE CONTROL                    │
│  ┌───────────────────────────────────┐  │
│  │  Peltier modules (8x)            │  │
│  │  Heating: 200W total             │  │
│  │  Cooling: 150W total             │  │
│  │  Control: PID per zone           │  │
│  └───────────────────────────────────┘  │
│                                         │
│  POWER: 28V from Avionics Bus (5A)     │
│  CONTROL: CAN from Flight Computer     │
└─────────────────────────────────────────┘
```

### Communications Array

```
Communications Array (FTL-Capable)
┌─────────────────────────────────────────┐
│  SUBSPACE TRANSCEIVER                   │
│  ┌───────────────────────────────────┐  │
│  │  Frequency: 1-100 GHz            │  │
│  │  Bandwidth: 1 Gbps (FTL)         │  │
│  │  Range: 100 light-years          │  │
│  │  Protocol: PHI-modulated QPSK    │  │
│  └───────────────────────────────────┘  │
│                                         │
│  CONVENTIONAL RADIO                     │
│  ┌───────────────────────────────────┐  │
│  │  VHF/UHF: Aviation band          │  │
│  │  HF: Long-range backup           │  │
│  │  WiFi: 802.11ac (in-system)      │  │
│  └───────────────────────────────────┘  │
│                                         │
│  ANTENNAS                               │
│  ┌───────────────────────────────────┐  │
│  │  Subspace: Phased array (hull)   │  │
│  │  VHF/UHF: Whip antenna           │  │
│  │  HF: Wire dipole                 │  │
│  │  WiFi: Patch antenna             │  │
│  └───────────────────────────────────┘  │
│                                         │
│  POWER: 100V → 28V (2A)               │
│  CONTROL: UART from Flight Computer    │
└─────────────────────────────────────────┘
```

---

## SAFETY SYSTEMS WIRING

### Warp Quench System

```
Emergency Warp Quench
┌─────────────────────────────────────────┐
│  ENERGY DUMP RESISTORS                  │
│  ┌───────────────────────────────────┐  │
│  │  100x 10Ω, 5kW resistors        │  │
│  │  Total capacity: 500kW for 50ms  │  │
│  │  Purpose: Dump warp energy safely │  │
│  └───────────────────────────────────┘  │
│                                         │
│  SWITCHING                              │
│  ┌───────────────────────────────────┐  │
│  │  Main contactor: 1000A, 100V     │  │
│  │  Bypass contactor: 1000A         │  │
│  │  Trigger: Hardwired from bubble  │  │
│  │           controller (redundant)  │  │
│  │  Response time: <100μs           │  │
│  └───────────────────────────────────┘  │
│                                         │
│  COOLING                                │
│  ┌───────────────────────────────────┐  │
│  │  Liquid cooling loop             │  │
│  │  Capacity: 500kW for 50ms        │  │
│  │  Fluid: Fluorinert (FC-77)       │  │
│  └───────────────────────────────────┘  │
│                                         │
│  POWER: 100V direct from bus            │
│  TRIGGER: Hardwired (NOT software)     │
└─────────────────────────────────────────┘
```

---

## GPIO PIN MAP (Flight Computer)

| GPIO | Function | Connected To | Direction |
|------|----------|--------------|-----------|
| CAN1-H | CAN Bus | Warp Controller | Bidirectional |
| CAN1-L | CAN Bus | Warp Controller | Bidirectional |
| CAN2-H | CAN Bus | Power System | Bidirectional |
| CAN2-L | CAN Bus | Power System | Bidirectional |
| ETH1 | Ethernet | Warp Radar | Bidirectional |
| ETH2 | Ethernet | Star Tracker | Bidirectional |
| SPI1-MOSI | SPI | IMU | Output |
| SPI1-MISO | SPI | IMU | Input |
| SPI1-SCLK | SPI | IMU | Output |
| SPI1-CS | SPI | IMU | Output |
| UART1-TX | Serial | Navigation Display | Output |
| UART1-RX | Serial | Navigation Display | Input |
| UART2-TX | Serial | Communications | Output |
| UART2-RX | Serial | Communications | Input |
| USB1 | USB | Control Stick | Bidirectional |
| USB2 | USB | Throttle | Bidirectional |
| AUX1 | Digital | Emergency Stop | Input |
| AUX2 | Digital | Master Warning | Output |

---

## CONTINUITY CHECK LIST

Before powering on, verify:

- [ ] All GND connections bonded to hull ground
- [ ] 100V bus isolation tested (10MΩ min)
- [ ] CAN bus termination (120Ω each end)
- [ ] Emergency stop circuit functional
- [ ] Warp quench hardwired (no software dependency)
- [ ] Triple-redundant voting logic verified
- [ ] Chronology protection unit active
- [ ] All HV connections torque-checked
- [ ] Cryocooler systems operational
- [ ] Fire suppression armed

---

**Document**: 02_WIRING.md
**Vehicle**: PHI FTL SHUTTLE
**Status**: BUILDABLE ✓
