# PHI SUPER GOGGLES — CONTROL SYSTEM

## Button Interface, Menu System, and Firmware

---

## CONTROL INTERFACE

### Button Layout

```
LEFT TEMPLE:
  ┌─────────────────────────────────────┐
  │                                     │
  │  [UP]        [SELECT]     [DOWN]    │
  │                                     │
  │  [LEFT]      [MODE]      [RIGHT]   │
  │                                     │
  │  [BACK]                  [BRIGHT]   │
  │                                     │
  └─────────────────────────────────────┘

RIGHT TEMPLE:
  ┌─────────────────────────────────────┐
  │                                     │
  │  [ROTARY ENCODER]                   │
  │  (Volume/Zoom/Scroll)               │
  │                                     │
  │  [POWER] (long press)              │
  │                                     │
  └─────────────────────────────────────┘
```

### Button Functions

| Button | Short Press | Long Press (3s) | Double Tap |
|--------|-------------|-----------------|------------|
| UP | Menu up / Value increase | Reset to defaults | — |
| DOWN | Menu down / Value decrease | Factory reset | — |
| LEFT | Menu left / Back | — | — |
| RIGHT | Menu right / Enter | — | — |
| SELECT | Confirm / Enter | — | — |
| BACK | Back / Cancel | Power off | — |
| MODE | Cycle vision modes (1→7) | Mode settings | Quick mode menu |
| BRIGHT | Cycle brightness (3 levels) | Auto-brightness toggle | — |
| ROTARY | Zoom / Scroll / Volume | Mute audio | — |
| POWER | Power on (when off) | Power off (when on) | — |

---

## MENU SYSTEM

### Main Menu Structure

```
PHI SUPER GOGGLES
│
├── VISION MODE
│   ├── 1. EMF Detection
│   ├── 2. Energy Flow
│   ├── 3. Coherence Map
│   ├── 4. Dimensional Overlay
│   ├── 5. Quantum Field View
│   ├── 6. Retrocausal Timeline
│   └── 7. Void Visualization
│
├── SENSOR SETTINGS
│   ├── Sensitivity (0.1μT - 100mT)
│   ├── Sample Rate (1kHz - 100kHz)
│   ├── Auto-Zero
│   ├── Calibration
│   └── Sensor Test
│
├── DISPLAY SETTINGS
│   ├── Brightness (1-100%)
│   ├── Auto-Brightness (ON/OFF)
│   ├── Color Scheme (5 options)
│   ├── Display Mode (Dual/Mirror/Left/Right)
│   ├── IPD Adjustment (55-75mm)
│   └── OLED Protection (ON/OFF)
│
├── PHI-HARMONIC SETTINGS
│   ├── φ-Weighting (ON/OFF)
│   ├── φ-Cycle Timing (Auto/Manual)
│   ├── φ-Animation Speed (0.5x - 2x)
│   └── φ-Constant Display (ON/OFF)
│
├── DATA LOGGING
│   ├── Log Mode (OFF/Manual/Auto/Triggered)
│   ├── Log Rate (1Hz - 10kHz)
│   ├── Log Format (CSV/Binary)
│   ├── SD Card Status
│   ├── Free Space
│   └── Clear Data
│
├── POWER MANAGEMENT
│   ├── Battery Status
│   ├── Power Mode (Performance/Balanced/Power Saver)
│   ├── Auto-Sleep (1-30 minutes)
│   ├── Sleep Brightness (0-50%)
│   └── USB-C PD (ON/OFF)
│
├── AUDIO & HAPTICS
│   ├── Buzzer Volume (0-100%)
│   ├── Haptic Intensity (0-100%)
│   ├── Alert Sounds (ON/OFF)
│   └── Audio Feedback (ON/OFF)
│
├── IMU & MOTION
│   ├── IMU Calibration
│   ├── Head Tracking (ON/OFF)
│   ├── Motion Wake (ON/OFF)
│   └── Gyro Filter (ON/OFF)
│
├── SYSTEM INFO
│   ├── Firmware Version
│   ├── Hardware Version
│   ├── Uptime
│   ├── Temperature
│   ├── FPGA Utilization
│   └── Memory Usage
│
├── ABOUT
│   ├── PHI Super Goggles v2.0
│   ├── License
│   └── Credits
│
└── ADVANCED (PIN Protected)
    ├── Debug Mode
    ├── FPGA Reconfigure
    ├── Factory Calibration
    ├── Serial Console
    └── Reset All Settings
```

### Menu Navigation

```
Navigation Rules:
1. UP/DOWN: Move cursor
2. RIGHT/SELECT: Enter submenu or toggle setting
3. LEFT/BACK: Go back one level
4. LONG BACK: Return to main menu
5. LONG MODE: Quick mode selection overlay
6. ROTARY: Scroll through long lists

Visual Feedback:
- Current selection: Highlighted (bright text)
- Changed values: Flash briefly
- Error: Red highlight + buzzer
- Success: Green flash + haptic
```

---

## FIRMWARE ARCHITECTURE

### FPGA Firmware Structure

```
FPGA Design (Verilog/VHDL):
├── Top Level (phi_super_goggles.v)
│   ├── Clock Management (PLL)
│   │   ├── 50MHz → 30.9MHz (Domain 1)
│   │   ├── 50MHz → 19.1MHz (Domain 2)
│   │   ├── 50MHz → 11.8MHz (Domain 3)
│   │   └── 50MHz → 7.28MHz (Domain 4)
│   │
│   ├── Sensor Interface
│   │   ├── SPI Master (ADC1)
│   │   ├── SPI Master (ADC2)
│   │   ├── MUX Controller (4× CD74HC4067)
│   │   ├── Data Buffer (24 channels × 16-bit)
│   │   └── Sample Clock Generator
│   │
│   ├── Signal Processing
│   │   ├── FIR Filter Bank (24 channels)
│   │   ├── FFT Engine (1024-point, pipelined)
│   │   ├── Coherence Calculator (28 pairs)
│   │   ├── Energy Flow Vector Calculator
│   │   └── Phi-Harmonic Weighting Module
│   │
│   ├── Vision Mode Controller
│   │   ├── Mode 1: EMF Detection
│   │   ├── Mode 2: Energy Flow
│   │   ├── Mode 3: Coherence Map
│   │   ├── Mode 4: Dimensional Overlay
│   │   ├── Mode 5: Quantum Field View
│   │   ├── Mode 6: Retrocausal Timeline
│   │   └── Mode 7: Void Visualization
│   │
│   ├── Display Controller
│   │   ├── HDMI TX (Left)
│   │   ├── HDMI TX (Right)
│   │   ├── Frame Buffer (32KB SDRAM)
│   │   ├── Alpha Compositor (5 layers)
│   │   └── Phi-Spiral Animation Engine
│   │
│   ├── Input Controller
│   │   ├── Button Debouncer (8 buttons)
│   │   ├── Rotary Encoder Decoder
│   │   ├── I2C Master (BNO055)
│   │   └── UART (Debug)
│   │
│   ├── Output Controller
│   │   ├── PWM Generator (Haptic × 2)
│   │   ├── PWM Generator (Buzzer)
│   │   ├── WS2812B Controller (LEDs)
│   │   └── GPIO Outputs (Enable/Disable)
│   │
│   ├── Power Management
│   │   ├── Battery Monitor (ADC)
│   │   ├── Temperature Monitor (ADC)
│   │   ├── Power State Machine
│   │   └── Sleep Controller
│   │
│   └── Data Logger
│       ├── SD Card SPI Interface
│       ├── Circular Buffer (FIFO)
│       ├── File System (FAT32)
│       └── Timestamp Generator
```

### Firmware Modules

```
Module: Sensor Interface
  - 24 ADC channels sampled at 4.17 kHz each
  - DMA transfers to frame buffer
  - Calibration applied in real-time
  - Anti-aliasing filter before sampling

Module: FFT Engine
  - 1024-point radix-4 FFT
  - Pipelined architecture (1 clock per butterfly)
  - Input: 24 × 1024 samples
  - Output: 24 × 512 complex bins
  - Processing time: 1024 cycles at 19.1 MHz = 53.6 μs

Module: Coherence Calculator
  - 28 unique sensor pairs
  - Cross-spectral density estimation
  - Phi-harmonic weighting
  - Output: 28 × 512 coherence values
  - Processing time: 100 μs

Module: Display Renderer
  - Dual 1920×1080 frame buffers
  - 5-layer alpha compositing
  - Phi-spiral transition animation
  - 60 Hz refresh rate
  - Processing time: 16.7 ms per frame
```

---

## MODE IMPLEMENTATIONS

### Mode 1: EMF Detection

```
Input: 24 channels × 16-bit @ 4.17 kHz
Processing:
  1. Apply calibration offsets
  2. Convert to magnetic field (μT)
  3. Calculate magnitude per sensor: √(x² + y² + z²)
  4. Map to color: 0-100 mT → Blue-Green-Yellow-Red

Output: Heatmap overlay on display
  - Left eye: X-axis heatmap
  - Right eye: Y-axis heatmap
  - Combined: Z-axis (with toggle)

Update Rate: 60 Hz
```

### Mode 2: Energy Flow

```
Input: 24 channels × 16-bit @ 4.17 kHz
Processing:
  1. Calculate time derivatives: dE/dt
  2. Compute flow vectors between sensor pairs
  3. Apply phi-harmonic weighting
  4. Render arrow field

Output: Arrow field showing energy movement
  - Arrow direction: Flow direction
  - Arrow length: Flow magnitude
  - Arrow color: Speed (Blue=slow, Red=fast)

Update Rate: 60 Hz
```

### Mode 3: Coherence Map

```
Input: 24 channels × 1024 samples @ 4.17 kHz
Processing:
  1. FFT of each channel (1024-point)
  2. Cross-spectral density for 28 pairs
  3. Coherence calculation with phi-weighting
  4. Spatial interpolation to 1920×1080

Output: Coherence heatmap with phi-spiral overlay
  - Red: High coherence (>0.8)
  - Yellow: Moderate (0.5-0.8)
  - Green: Low (0.2-0.5)
  - Blue: Minimal (<0.2)

Update Rate: 3.9 kHz (raw), 60 Hz (display)
```

### Mode 4: Dimensional Overlay

```
Input: All sensor data + IMU
Processing:
  1. EMF intensity layer
  2. Energy flow layer
  3. Coherence layer
  4. Phi-structure layer
  5. Depth layer (stereoscopic)

Output: Multi-layer composite display
  - Each layer: 30-70% opacity
  - Stereo offset: φ⁻¹ × 10.3ms
  - Head tracking: Parallax effect

Update Rate: 60 Hz
```

### Mode 5: Quantum Field View

```
Input: Ultra-high-frequency components (>100 kHz)
Processing:
  1. Stochastic resonance amplification
  2. Probability density estimation
  3. Particle system simulation
  4. Quantum event detection

Output: Shimmering particle field
  - Particle density: Probability density
  - Particle color: Blue (low) → White (high)
  - Quantum events: Flash highlights

Update Rate: 60 Hz
```

### Mode 6: Retrocausal Timeline

```
Input: 30 seconds of buffered sensor data
Processing:
  1. Time-series analysis
  2. Phi-harmonic weighted extrapolation
  3. Future prediction (1-10 seconds)
  4. History visualization

Output: Timeline strip at bottom of display
  - Current time: Center
  - Past: Left (scrolling)
  - Future: Right (predicted, dimmed)
  - Field strength: Y-axis

Update Rate: 60 Hz
Buffer: 30 seconds × 100 kHz × 24 channels
```

### Mode 7: Void Visualization

```
Input: 24 channels × 16-bit @ 4.17 kHz
Processing:
  1. Threshold detection (0.485 μT)
  2. Void region identification
  3. Void edge detection
  4. Void size/shape analysis

Output: Dark regions with purple edges
  - Void interior: Near-black
  - Void edge: Purple glow (3px)
  - Void size: Logarithmic scaling
  - Void stability: Temporal indicator

Update Rate: 60 Hz
```

---

## INPUT HANDLING

### Button Debouncing

```
Debounce Parameters:
  Debounce Time: 20 ms
  Method: Edge detection + timer
  Long Press: 3 seconds
  Double Tap: 300 ms window

Debounce State Machine:
  IDLE → PRESSED (after 20ms stable)
  PRESSED → RELEASED (on release)
  RELEASED → CONFIRMED (after 20ms stable)
  
  Long press: PRESSED for 3000ms
  Double tap: CONFIRMED within 300ms of last CONFIRMED
```

### Rotary Encoder

```
Encoder Type: KY-040 (incremental quadrature)
Pulses per revolution: 20
Debounce: 1 ms (hardware + software)
Direction: Clockwise = increase, Counter-clockwise = decrease

Functions:
  Default: Zoom in/out (digital zoom on display)
  Menu mode: Scroll through menu items
  Volume mode: Adjust buzzer volume
  Brightness mode: Adjust display brightness
```

### IMU Integration

```
IMU: BNO055 (9-DOF)
Interface: I2C (400 kHz)
Update Rate: 100 Hz

Data Used:
  - Quaternion (orientation)
  - Angular velocity (gyro)
  - Linear acceleration (accel)
  - Magnetic field (magnetometer)

Applications:
  - Head tracking (Mode 4: Dimensional Overlay)
  - Motion wake (sleep mode)
  - Stabilization (display rendering)
  - Gesture detection (future)
```

---

## AUDIO & HAPTICS

### Buzzer

```
Buzzer Type: Piezo (passive, 3V)
PWM Frequency: 2-4 kHz
Duty Cycle: 50% (adjustable)

Sounds:
  - Startup: Rising tone (100ms)
  - Mode change: Short beep (50ms)
  - Button press: Click (20ms)
  - Error: Double beep (100ms × 2)
  - Low battery: Periodic beep (every 5s)
  - Shutdown: Falling tone (100ms)
```

### Haptic Motors

```
Motor Type: ERM (Eccentric Rotating Mass)
Voltage: 3V
Left Temple: Left motor
Right Temple: Right motor

Haptic Patterns:
  - Button press: Short buzz (20ms)
  - Mode change: Medium buzz (50ms)
  - Alert: Long buzz (200ms)
  - Error: Double buzz (100ms × 2)
  - Phi-harmonic: Rhythmic pattern (φ-timed)

PWM Control:
  Frequency: 200 Hz
  Duty Cycle: 0-100% (intensity)
  Direction: Left/Right/Both
```

### Status LEDs

```
LED Type: WS2812B (RGB, addressable)
Quantity: 4 (one per corner of housing)
Colors: Full RGB (16.7M colors)

Status Indications:
  - Power on: Green fade in
  - Mode 1 (EMF): Blue solid
  - Mode 2 (Flow): Cyan solid
  - Mode 3 (Coherence): Green solid
  - Mode 4 (Dimensional): Yellow solid
  - Mode 5 (Quantum): Purple solid
  - Mode 6 (Retrocausal): Orange solid
  - Mode 7 (Void): Red solid
  - Low battery: Red blink
  - Charging: Yellow pulse
  - Error: Red blink (fast)
```

---

## DATA LOGGING

### Log Formats

```
CSV Format:
  Timestamp,Mode,Sensor1_X,Sensor1_Y,Sensor1_Z,...,Sensor8_X,Sensor8_Y,Sensor8_Z,FFT_0,...,FFT_511
  
Binary Format:
  Header (32 bytes):
    Magic: 0x50484953 ("PHIS")
    Version: 2
    Mode: uint8
    Sample Rate: uint32
    Channel Count: uint8
    Resolution: uint8
    Timestamp: uint64
    
  Data Blocks:
    Timestamp: uint64 (microseconds)
    Sensor Data: 24 × int16
    FFT Data: 24 × 512 × complex (optional)
    Coherence Data: 28 × 512 (optional)
```

### SD Card Management

```
File System: FAT32
Cluster Size: 4KB
Max File Size: 4GB
Max Files: 65535

File Naming:
  PHI_LOG_YYYYMMDD_HHMMSS.csv
  PHI_LOG_YYYYMMDD_HHMMSS.bin

Auto-Deletion:
  When free space < 100MB
  Delete oldest files first
  Keep last 10 files minimum

Buffer:
  RAM Buffer: 64KB
  Write Speed: 10 MB/s (SD card limit)
  Flush Interval: 1 second
```

---

## POWER STATE MACHINE

```
States:
  OFF → ON (power button)
  ON → SLEEP (idle timeout)
  SLEEP → ON (button press, motion)
  SLEEP → OFF (long idle, 30 minutes)
  ON → OFF (long press power)

Transitions:
  OFF → ON: Power button press (< 1 second)
  ON → SLEEP: No input for configurable timeout
  SLEEP → ON: Any button press or IMU motion
  SLEEP → OFF: No input for 30 minutes
  ON → OFF: Long press power button (3 seconds)

Power Consumption per State:
  OFF: 0 mW
  ON (active): 3,885 mW
  ON (dimmed): 2,500 mW
  SLEEP: 160 mW
```

---

## FIRMWARE UPDATE

### Update Method

```
USB DFU (Device Firmware Update):
  1. Enter DFU mode (hold MODE + SELECT during power on)
  2. Connect USB cable
  3. Run DFU utility: dfu-util -D firmware.bin
  4. Wait for completion
  5. Power cycle

SD Card Update:
  1. Copy firmware.bin to SD card root
  2. Power on with SD card inserted
  3. Firmware auto-updates
  4. Remove SD card
  5. Power cycle

Verification:
  - CRC32 checksum comparison
  - Version number verification
  - Rollback on failure (dual-bank)
```

### Firmware Versioning

```
Version Format: MAJOR.MINOR.PATCH
  MAJOR: Breaking changes
  MINOR: New features
  PATCH: Bug fixes

Current Version: 2.0.0

Change Log (v2.0.0):
  - 8 EMF sensors (upgraded from 4)
  - Dual 1920×1080 OLED (upgraded from 1080×720)
  - FPGA processor (upgraded from microcontroller)
  - 7 vision modes (upgraded from 4)
  - Phi-harmonic timing system
  - Retrocausal timeline
  - Quantum field view
  - Void visualization
```
