# PHI_HUMANOID_ROBOT — Control System

## Software Architecture, Firmware & Control Loops

---

## 1. System Architecture

```
CONTROL SYSTEM HIERARCHY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────┐
│                    LEVEL 4: AI / BEHAVIOR                       │
│                    Raspberry Pi 5 + Coral TPU                    │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Vision   │  │ Voice    │  │ Planning │  │ Behavior │      │
│  │ Pipeline │  │ Pipeline │  │ Engine   │  │ State    │      │
│  │ (Coral)  │  │ (RPi)    │  │ (RPi)    │  │ Machine  │      │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
│       └──────────────┼──────────────┼──────────────┘           │
│                      │              │                           │
│              ┌───────┴──────────────┴───────┐                  │
│              │      PHI-HARMONIC CORE        │                  │
│              │      (Python / NumPy)         │                  │
│              │      100 Hz update rate       │                  │
│              └──────────────┬───────────────┘                  │
└─────────────────────────────┼───────────────────────────────────┘
                              │ CAN Bus (500 kbps)
                              │
┌─────────────────────────────┼───────────────────────────────────┐
│                    LEVEL 3: GAIT / BALANCE                      │
│                    Raspberry Pi 5                                │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Gait     │  │ Balance  │  │ Trajectory│  │ φ-Harmonic│     │
│  │ Generator│  │ Control  │  │ Planner  │  │ Controller│      │
│  │ 100 Hz   │  │ 1000 Hz  │  │ 100 Hz   │  │ 1000 Hz   │     │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
│       └──────────────┼──────────────┼──────────────┘           │
│                      │              │                           │
│              ┌───────┴──────────────┴───────┐                  │
│              │      STM32 Co-Processor #1    │                  │
│              │      (Leg control, 1kHz)      │                  │
│              └──────────────┬───────────────┘                  │
└─────────────────────────────┼───────────────────────────────────┘
                              │ CAN Bus
                              │
┌─────────────────────────────┼───────────────────────────────────┐
│                    LEVEL 2: JOINT CONTROL                        │
│                    ODrive Motor Controllers                      │
│                                                                 │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐      │
│  │ODrive│ │ODrive│ │ODrive│ │ODrive│ │ODrive│ │ODrive│      │
│  │#1    │ │#2    │ │#3    │ │#4    │ │#5    │ │#6    │      │
│  │HAA/  │ │KFE/  │ │AFE/  │ │HAA/  │ │KFE/  │ │AFE/  │      │
│  │HFE   │ │KAA   │ │TOE   │ │HFE   │ │KAA   │ │TOE   │      │
│  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘      │
│     └────────┼────────┼────────┼────────┼────────┘            │
│              │        │        │        │                      │
│  ┌───────────┴────────┴────────┴────────┴──────────┐          │
│  │  + ODrive #7-12 (Arms), ODrive Pro (Torso/Head)│          │
│  │  Total: 14 ODrives, 28 motor channels           │          │
│  └──────────────────────────────────────────────────┘          │
│                                                                 │
│  EACH ODRIVE:                                                  │
│  ├── FOC motor control at 10 kHz                               │
│  ├── Encoder feedback at 10 kHz                                │
│  ├── Current sensing at 10 kHz                                 │
│  ├── Position/velocity/torque control                          │
│  └── CAN bus interface at 500 kbps                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────┼───────────────────────────────────┐
│                    LEVEL 1: HARDWARE                             │
│                    Motors + Sensors + Actuators                  │
│                                                                 │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐      │
│  │BLDC  │ │BLDC  │ │BLDC  │ │BLDC  │ │BLDC  │ │XL330 │      │
│  │Motor │ │Motor │ │Motor │ │Motor │ │Motor │ │Servo │      │
│  │D6374 │ │D6374 │ │D6374 │ │D5065 │ │M5671 │ │      │      │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘      │
│                                                                 │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐      │
│  │AS5048│ │AS5048│ │BNO085│ │FSR406│ │ADS1256│ │INA260│     │
│  │Encoder│ │Encoder│ │IMU   │ │FSR   │ │ADC   │ │Power │      │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Software Stack

### 2.1 Operating System

```
OS: Ubuntu Server 24.04 LTS (arm64)
├── Kernel: 6.5.x (real-time patch optional)
├── Init: systemd
├── Network: NetworkManager
├── SSH: OpenSSH server
└── Python: 3.12.x

PACKAGES:
├── ROS 2 Humble (optional, for modularity)
├── NumPy 1.26+
├── SciPy 1.12+
├── OpenCV 4.9+
├── PySerial 3.5+
├── python-odrive 0.6.x
├── pycoral 2.0+
├── whisper (OpenAI) — voice recognition
├── piper — text-to-speech
├── Flask — web API
└── Custom phi-harmonic control stack
```

### 2.2 Software Modules

```
MODULE MAP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

phi_core/
├── __init__.py
├── config.py              # System configuration
├── constants.py           # φ constants, motor params
├── main.py                # Main control loop (100 Hz)
│
├── perception/
│   ├── vision.py          # Camera pipeline (Coral TPU)
│   ├── audio.py           # Microphone array + beamforming
│   ├── proximity.py       # ToF + ultrasonic sensors
│   └── force.py           # FSR + strain gauge processing
│
├── control/
│   ├── gait.py            # Gait generator (φ-harmonic)
│   ├── balance.py         # Balance controller (Fibonacci gains)
│   ├── trajectory.py      # Joint trajectory planner
│   ├── hand.py            # Hand manipulation controller
│   └── phi_controller.py  # φ-harmonic control algorithm
│
├── hardware/
│   ├── odrive_manager.py  # ODrive CAN interface
│   ├── encoder_reader.py  # AS5048A encoder interface
│   ├── sensor_hub.py      # STM32 communication
│   ├── power_monitor.py   # INA260 power monitoring
│   └── motor_config.py    # Motor calibration data
│
├── ai/
│   ├── object_detector.py # Coral TPU object detection
│   ├── face_recognizer.py # Face detection/recognition
│   ├── voice_recognizer.py# Whisper voice recognition
│   ├── voice_synthesizer.py# Piper TTS
│   └── nlp.py             # Natural language understanding
│
├── behavior/
│   ├── state_machine.py   # Behavior state machine
│   ├── navigation.py      # Path planning
│   ├── interaction.py     # Human-robot interaction
│   └── safety.py          # Safety monitoring
│
└── utils/
    ├── logging.py          # Structured logging
    ├── calibration.py      # Calibration routines
    ├── diagnostics.py      # System diagnostics
    └── web_api.py          # Flask REST API
```

---

## 3. Control Loop Hierarchy

### 3.1 Loop Frequencies

```
CONTROL LOOP TIMING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Loop                Frequency    Period    Priority    Processor
──────────────────────────────────────────────────────────────────
Motor FOC           10,000 Hz    100µs     Highest     ODrive
Encoder sampling    10,000 Hz    100µs     Highest     ODrive
Current sensing     10,000 Hz    100µs     Highest     ODrive
CAN bus             1,000 Hz     1ms       High        ODrive↔RPi
Balance control     1,000 Hz     1ms       High        STM32 #1
Joint position      1,000 Hz     1ms       High        ODrive
IMU reading         1,000 Hz     1ms       High        STM32
Force sensing       1,000 Hz     1ms       High        STM32
──────────────────────────────────────────────────────────────────
Gait generation     100 Hz       10ms      Medium      RPi
Trajectory planning 100 Hz       10ms      Medium      RPi
φ-Harmonic ctrl     100 Hz       10ms      Medium      RPi
Vision processing   30 Hz        33ms      Medium      Coral TPU
Voice recognition   5 Hz         200ms     Low         RPi CPU
Behavior planning   10 Hz        100ms     Medium      RPi
──────────────────────────────────────────────────────────────────
Web API             10 Hz        100ms     Low         RPi
Diagnostics         1 Hz         1000ms    Low         RPi
──────────────────────────────────────────────────────────────────
```

### 3.2 Main Control Loop

```python
# phi_core/main.py — Main Control Loop (simplified)

import time
import numpy as np
from phi_core.control.gait import GaitGenerator
from phi_core.control.balance import BalanceController
from phi_core.control.phi_controller import PhiHarmonicController
from phi_core.hardware.odrive_manager import ODriveManager
from phi_core.perception.force import ForceSensorArray

class PhiHumanoidController:
    def __init__(self):
        self.odrive = ODriveManager()
        self.gait = GaitGenerator()
        self.balance = BalanceController()
        self.phi_ctrl = PhiHarmonicController()
        self.force = ForceSensorArray()
        
        # φ-harmonic timing
        self.phi = 1.618033988749895
        self.dt = 0.01  # 100 Hz
        self.t = 0.0
        
    def run(self):
        """Main control loop at 100 Hz."""
        while True:
            t_start = time.time()
            
            # 1. Read sensors
            imu_data = self.read_imu()
            encoders = self.read_encoders()
            forces = self.force.read()
            
            # 2. φ-harmonic balance
            balance_torques = self.balance.compute(
                imu_data, encoders, forces
            )
            
            # 3. Gait generation (φ-optimized)
            joint_targets = self.gait.generate(
                self.t, self.phi
            )
            
            # 4. φ-harmonic correction
            corrected = self.phi_ctrl.correct(
                joint_targets, balance_torques
            )
            
            # 5. Send to motors
            self.odrive.set_positions(corrected)
            
            # 6. φ-harmonic timing
            t_elapsed = time.time() - t_start
            t_sleep = self.dt - t_elapsed
            if t_sleep > 0:
                time.sleep(t_sleep)
            
            self.t += self.dt
    
    def read_imu(self):
        """Read body IMU at 1kHz (via STM32)."""
        return self.stm32.read_imu()
    
    def read_encoders(self):
        """Read all 28 encoders (via STM32 MUX)."""
        return self.stm32.read_encoders()
```

---

## 4. φ-Harmonic Controller

### 4.1 Algorithm

```python
# phi_core/control/phi_controller.py

import numpy as np

class PhiHarmonicController:
    """
    φ-Harmonic Control Algorithm
    
    Uses golden ratio (φ) as the organizing principle for
    multi-frequency control with self-stabilizing properties.
    """
    
    PHI = 1.618033988749895
    
    def __init__(self, n_harmonics=8):
        self.n_harmonics = n_harmonics
        self.phi = self.PHI
        
        # Base gains
        self.Kp_0 = 0.5
        self.Ki_0 = 0.1
        self.Kd_0 = 0.05
        
        # Pre-compute φ-harmonic gains
        self.Kp = np.array([
            self.Kp_0 * self.phi**(n/2) 
            for n in range(n_harmonics)
        ])
        self.Ki = np.array([
            self.Ki_0 * self.phi**(n/2) 
            for n in range(n_harmonics)
        ])
        self.Kd = np.array([
            self.Kd_0 * self.phi**(n/2) 
            for n in range(n_harmonics)
        ])
        
        # Error history for each harmonic
        self.errors = np.zeros((n_harmonics, 3))  # [prev, integral, derivative]
    
    def compute(self, error, dt):
        """
        Compute φ-harmonic control output.
        
        Args:
            error: Position error (rad) for each joint
            dt: Time step (seconds)
        
        Returns:
            Control torques (Nm) for each joint
        """
        torques = np.zeros_like(error)
        
        for n in range(self.n_harmonics):
            # φ-weighted error decomposition
            e_n = error * (1 / self.phi**n)
            
            # Proportional
            P = self.Kp[n] * e_n
            
            # Integral (with φ-decay)
            self.errors[n, 1] += e_n * dt
            I = self.Ki[n] * self.errors[n, 1]
            
            # Derivative
            de = (e_n - self.errors[n, 0]) / dt if dt > 0 else 0
            D = self.Kd[n] * de
            
            # Accumulate
            torques += P + I + D
            
            # Update history
            self.errors[n, 0] = e_n
        
        return torques
    
    def stability_check(self):
        """
        Verify φ-harmonic stability criterion.
        
        Returns:
            is_stable: bool
            gain_product: float (should be < 1)
        """
        # Product of normalized gains
        product = np.prod(self.Kp / self.phi**np.arange(self.n_harmonics))
        return product < 1.0, product
```

### 4.2 Balance Controller

```python
# phi_core/control/balance.py

import numpy as np

class BalanceController:
    """
    φ-Harmonic Balance Controller
    
    Uses Fibonacci recursive gains for self-stabilizing balance.
    """
    
    PHI = 1.618033988749895
    
    def __init__(self):
        self.phi = self.PHI
        
        # Base gains (tuned)
        self.Kp_base = np.array([0.5, 0.5, 0.8])  # [roll, pitch, yaw]
        self.Ki_base = np.array([0.1, 0.1, 0.15])
        self.Kd_base = np.array([0.05, 0.05, 0.08])
        
        # Error accumulators
        self.integral = np.zeros(3)
        self.prev_error = np.zeros(3)
        
        # φ-harmonic reference trajectory
        self.A_sway = 0.015  # 15mm sway amplitude
        self.A_bounce = 0.005  # 5mm bounce amplitude
        self.f_0 = 1.0 / self.phi  # 0.618 Hz base frequency
    
    def compute(self, imu_data, encoder_data, force_data, dt):
        """
        Compute balance correction torques.
        
        Args:
            imu_data: [roll, pitch, yaw, roll_rate, pitch_rate, yaw_rate]
            encoder_data: Joint positions
            force_data: Foot pressure sensor readings
            dt: Time step
        
        Returns:
            correction_torques: [hip_L, hip_R, ankle_L, ankle_R]
        """
        # Current orientation
        roll = imu_data[0]
        pitch = imu_data[1]
        roll_rate = imu_data[3]
        pitch_rate = imu_data[4]
        
        # φ-harmonic reference (natural sway)
        t = time.time()
        ref_roll = self.A_sway * np.sin(2 * np.pi * self.f_0 * t)
        ref_pitch = self.A_sway * np.sin(2 * np.pi * self.f_0 * self.phi * t)
        
        # Error
        error = np.array([
            roll - ref_roll,
            pitch - ref_pitch,
            0  # yaw controlled separately
        ])
        
        # φ-harmonic PID with recursive gains
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else np.zeros(3)
        
        # Apply φ-weighted gains
        Kp = self.Kp_base
        Ki = self.Ki_base
        Kd = self.Kd_base
        
        # Recursive Fibonacci gain schedule
        for n in range(1, 5):
            weight = 1 / self.phi**n
            Kp += weight * self.Kp_base
            Ki += weight * self.Ki_base
            Kd += weight * self.Kd_base
        
        # PID output
        correction = Kp * error + Ki * self.integral + Kd * derivative
        
        # Map to joint torques
        torques = self._map_to_joints(correction, force_data)
        
        self.prev_error = error
        return torques
    
    def _map_to_joints(self, correction, force_data):
        """Map body-level correction to joint torques."""
        # Simplified mapping
        roll_correction = correction[0]
        pitch_correction = correction[1]
        
        # Distribute to hip and ankle joints
        hip_torque = roll_correction * 0.6 + pitch_correction * 0.4
        ankle_torque = roll_correction * 0.4 + pitch_correction * 0.6
        
        return np.array([
            hip_torque,   # Left hip
            hip_torque,   # Right hip
            ankle_torque, # Left ankle
            ankle_torque  # Right ankle
        ])
```

---

## 5. Gait Generator

### 5.1 φ-Harmonic Gait

```python
# phi_core/control/gait.py

import numpy as np

class GaitGenerator:
    """
    φ-Harmonic Gait Generator
    
    Generates walking gait with golden ratio timing.
    """
    
    PHI = 1.618033988749895
    
    def __init__(self):
        self.phi = self.PHI
        
        # Gait parameters
        self.step_length = 0.306  # H/φ³ = 1600/4.236 mm
        self.step_height = 0.076  # H/φ⁵
        self.cadence = 1.5  # Hz
        self.phase_offset = 68.76  # φ × 180° mod 360°
        
        # Joint trajectories (pre-computed)
        self.trajectories = self._compute_trajectories()
    
    def generate(self, t, phi):
        """
        Generate joint positions for current time.
        
        Args:
            t: Current time (seconds)
            phi: Golden ratio
        
        Returns:
            joint_positions: Dict of joint angles (radians)
        """
        # Gait cycle phase
        phase = (t * self.cadence) % 1.0
        
        # φ-harmonic phase decomposition
        phase_harmonics = np.array([
            phase * phi**n for n in range(4)
        ])
        
        # Left leg trajectory
        left_leg = self._left_leg_trajectory(phase_harmonics)
        
        # Right leg (φ-phase offset)
        right_phase = (phase + self.phase_offset / 360) % 1.0
        right_harmonics = np.array([
            right_phase * phi**n for n in range(4)
        ])
        right_leg = self._right_leg_trajectory(right_harmonics)
        
        # Arms (counter-phase swing)
        left_arm = self._arm_trajectory(phase_harmonics, side='left')
        right_arm = self._arm_trajectory(right_harmonics, side='right')
        
        # Torso (φ-modulated sway)
        torso = self._torso_trajectory(phase_harmonics)
        
        return {
            'left_leg': left_leg,
            'right_leg': right_leg,
            'left_arm': left_arm,
            'right_arm': right_arm,
            'torso': torso
        }
    
    def _left_leg_trajectory(self, phases):
        """Generate left leg joint angles."""
        p = phases[0]  # Base phase
        
        # Hip flexion/extension (sine with φ-modulation)
        hip_fe = 0.3 * np.sin(2 * np.pi * p)  # ±17°
        
        # Hip abduction/adduction
        hip_aa = 0.1 * np.sin(2 * np.pi * p + 0.5)  # ±6°
        
        # Knee flexion
        knee = 0.5 * (1 + np.sin(2 * np.pi * p - np.pi/2))  # 0 to 50°
        
        # Ankle flexion
        ankle = 0.2 * np.sin(2 * np.pi * p + 0.3)  # ±11°
        
        return {
            'hip_fe': hip_fe,
            'hip_aa': hip_aa,
            'knee_fe': knee,
            'ankle_fe': ankle
        }
    
    def _right_leg_trajectory(self, phases):
        """Generate right leg (mirror of left with φ-offset)."""
        return self._left_leg_trajectory(phases)
    
    def _arm_trajectory(self, phases, side):
        """Generate arm swing (counter-phase to legs)."""
        p = phases[0]
        sign = 1.0 if side == 'left' else -1.0
        
        shoulder_fe = sign * 0.2 * np.sin(2 * np.pi * p)
        elbow = 0.3 * (1 + np.sin(2 * np.pi * p - np.pi/3))
        
        return {
            'shoulder_fe': shoulder_fe,
            'elbow_fe': elbow
        }
    
    def _torso_trajectory(self, phases):
        """Generate torso sway (φ-modulated)."""
        p = phases[0]
        
        yaw = 0.05 * np.sin(2 * np.pi * p * self.phi)
        pitch = 0.03 * np.sin(2 * np.pi * p)
        
        return {
            'yaw': yaw,
            'pitch': pitch
        }
```

---

## 6. STM32 Firmware

### 6.1 Sensor Hub Firmware

```
STM32H7 FIRMWARE (Sensor Hub #1 — Legs):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Language: C (bare metal or FreeRTOS)
Clock: 480 MHz
Interrupt priority: Highest (sensor sampling)

TASKS:
├── Task 1: IMU Reading (1 kHz)
│   ├── Read BNO085 via SPI
│   ├── Quaternion → Euler angles
│   └── Store in shared buffer
│
├── Task 2: Encoder Reading (10 kHz)
│   ├── Read 12× AS5048A via SPI (MUX)
│   ├── Convert to angle (radians)
│   └── Store in shared buffer
│
├── Task 3: Force Sensing (1 kHz)
│   ├── Read 2× ADS1256 via SPI
│   ├── Convert ADC → Force (N)
│   └── Store in shared buffer
│
├── Task 4: CAN Communication (1 kHz)
│   ├── Receive commands from RPi
│   ├── Send sensor data to RPi
│   └── Relay commands to ODrives
│
└── Task 5: Safety Monitor (10 kHz)
    ├── Watch RPi heartbeat
    ├── Monitor emergency stop
    └── Trigger motor disable on fault
```

### 6.2 CAN Bus Protocol

```
CAN MESSAGE FORMAT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Message ID: 11-bit standard CAN

RPi → ODrive Messages:
├── 0x001: Set position (target, velocity, torque)
├── 0x002: Set velocity
├── 0x003: Set torque
├── 0x004: Request state
├── 0x005: Set limits (current, velocity)
├── 0x00F: E-stop (broadcast)
└── 0x0FF: Heartbeat (broadcast)

ODrive → RPi Messages:
├── 0x100: Encoder position (actual)
├── 0x101: Encoder velocity
├── 0x102: Motor current
├── 0x103: Motor temperature
├── 0x104: Fault status
├── 0x105: Controller state
└── 0x1FF: Heartbeat response

DATA FORMAT (8 bytes):
├── Bytes 0-3: Float32 (value)
├── Bytes 4-5: uint16 (flags)
├── Byte 6: uint8 (sequence number)
└── Byte 7: uint8 (checksum)

TIMING:
├── Command cycle: 1ms (1 kHz)
├── Feedback cycle: 1ms (1 kHz)
├── Heartbeat: 100ms (10 Hz)
└── Timeout: 100ms (no response → fault)
```

---

## 7. Vision Pipeline

```
VISION PROCESSING PIPELINE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Camera Input (2× stereo, 1280×800, 60fps)
    │
    ├── Stereo Matching (RPi CPU, 30fps)
    │   ├── Block matching algorithm
    │   ├── Disparity map → depth map
    │   └── Output: 640×400 depth map @ 30fps
    │
    ├── Object Detection (Coral TPU, 30fps)
    │   ├── Model: MobileNet SSD v2
    │   ├── Input: 320×320 RGB
    │   ├── Output: Bounding boxes + classes
    │   └── Latency: 33ms per frame
    │
    ├── Face Detection (Coral TPU, 15fps)
    │   ├── Model: MTCNN
    │   ├── Input: 320×240 RGB
    │   ├── Output: Face landmarks + embedding
    │   └── Latency: 66ms per frame
    │
    ├── Semantic Segmentation (Coral TPU, 20fps)
    │   ├── Model: DeepLab v3
    │   ├── Input: 257×257 RGB
    │   ├── Output: Pixel-wise class labels
    │   └── Latency: 50ms per frame
    │
    └── Visual SLAM (RPi CPU, 10fps)
        ├── ORB features
        ├── Pose estimation
        └── Map building

OUTPUT:
├── Object list (class, position, confidence)
├── Face list (ID, position, emotion)
├── Depth map (3D point cloud)
├── Segmentation mask (floor, obstacles, walls)
├── Robot pose (x, y, θ)
└── Obstacle map (occupancy grid)
```

---

## 8. Voice Pipeline

```
VOICE PROCESSING PIPELINE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Microphone Array (4× INMP441, I2S, 48kHz)
    │
    ├── Beamforming (RPi CPU, real-time)
    │   ├── 4-channel delay-and-sum
    │   ├── φ-weighted coefficients
    │   ├── Noise reduction: 20 dB
    │   └── Output: Single enhanced audio stream
    │
    ├── Voice Activity Detection (RPi CPU)
    │   ├── Energy-based VAD
    │   ├── Spectral flux VAD
    │   └── Output: Speech segments
    │
    ├── Speech Recognition (Whisper, RPi CPU)
    │   ├── Model: whisper-base (74M params)
    │   ├── Input: 30s audio chunks
    │   ├── Output: Text transcription
    │   └── Latency: ~500ms
    │
    ├── NLP Understanding (RPi CPU)
    │   ├── Intent classification
    │   ├── Entity extraction
    │   └── Output: Command structure
    │
    └── Voice Synthesis (Piper, RPi CPU)
        ├── Model: en_US-libritts_r-medium
        ├── Input: Text string
        ├── Output: Audio waveform
        ├── φ-harmonic formant modulation
        └── Latency: ~200ms

COMMAND EXAMPLES:
├── "Hello" → Greeting response
├── "Walk forward" → Enter walking mode
├── "Stop" → Emergency stop
├── "Pick up the cup" → Grasp task
├── "What do you see?" → Vision description
├── "Status" → Battery + system report
└── "φ-harmonic balance" → Recalibrate balance
```

---

## 9. State Machine

```
BEHAVIOR STATE MACHINE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    ┌──────────┐
                    │  POWER   │
                    │  OFF     │
                    └────┬─────┘
                         │ Power on
                         ▼
                    ┌──────────┐
                    │  BOOT    │
                    │  SEQUENCE│
                    └────┬─────┘
                         │ Self-test pass
                         ▼
                    ┌──────────┐
              ┌────▶│  IDLE    │◀────┐
              │     │  STANDING│     │
              │     └────┬─────┘     │
              │          │           │
              │     Voice command    │
              │     or app command   │
              │          │           │
              │          ▼           │
              │     ┌──────────┐     │
              │     │  WALKING │     │
              │     │  MODE    │     │
              │     └────┬─────┘     │
              │          │           │
              │     Speed > 5km/h    │
              │          │           │
              │          ▼           │
              │     ┌──────────┐     │
              │     │  RUNNING │     │
              │     │  MODE    │─────┘
              │     └────┬─────┘     │
              │          │           │
              │     Obstacle detected│
              │          │           │
              │          ▼           │
              │     ┌──────────┐     │
              │     │  NAVIGATE│     │
              │     │  AROUND  │─────┘
              │     └──────────┘
              │
              │     Voice: "Pick up"
              │          │
              │          ▼
              │     ┌──────────┐
              │     │  GRASP   │
              │     │  OBJECT  │─────┘
              │     └──────────┘
              │
              │     Fault detected
              │          │
              │          ▼
              │     ┌──────────┐
              └────▶│  SAFE    │
                    │  STATE   │
                    └────┬─────┘
                         │ E-stop released
                         │ + self-test
                         ▼
                    ┌──────────┐
                    │  RECOVERY│
                    │  MODE    │
                    └────┬─────┘
                         │ Recovery complete
                         └──────▶ IDLE
```

---

*Document: 13_CONTROL_SYSTEM.md — PHI_HUMANOID_ROBOT Control System*
*Version: 1.0 | Date: 2026-08-27*
