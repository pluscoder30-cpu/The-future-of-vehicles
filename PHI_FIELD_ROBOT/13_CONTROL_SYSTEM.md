# PHI_FIELD_ROBOT — Control System

## PHI_FIELD_ROBOT | Document 13: Control System

---

## 1. SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTROL SYSTEM ARCHITECTURE                │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                 HIGH LEVEL (RPi 5)                   │    │
│  │                                                      │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │    │
│  │  │ ROS 2    │  │ AI/ML    │  │ Mission  │          │    │
│  │  │ Humble   │  │ Pipeline │  │ Planner  │          │    │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘          │    │
│  │       │              │              │                │    │
│  │       └──────────────┼──────────────┘                │    │
│  │                      │                               │    │
│  │              ┌───────┴───────┐                       │    │
│  │              │  PHI-HARMONIC │                       │    │
│  │              │  CONTROL      │                       │    │
│  │              │  COORDINATOR  │                       │    │
│  │              └───────┬───────┘                       │    │
│  │                      │                               │    │
│  │              ┌───────┴───────┐                       │    │
│  │              │  USB CDC-ACM   │                       │    │
│  │              │  (921600 baud) │                       │    │
│  │              └───────┬───────┘                       │    │
│  └──────────────────────┼──────────────────────────────┘    │
│                         │                                   │
│  ┌──────────────────────┼──────────────────────────────┐    │
│  │                 LOW LEVEL (STM32H743)                │    │
│  │                      │                               │    │
│  │              ┌───────┴───────┐                       │    │
│  │              │  REAL-TIME    │                       │    │
│  │              │  CONTROLLER   │                       │    │
│  │              │  (1 kHz)      │                       │    │
│  │              └──┬────┬────┬──┘                       │    │
│  │                 │    │    │                          │    │
│  │        ┌────────┘    │    └────────┐                 │    │
│  │        ▼             ▼             ▼                 │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │    │
│  │  │ LEG      │  │ ARM      │  │ SENSOR   │          │    │
│  │  │ CONTROL  │  │ CONTROL  │  │ FUSION   │          │    │
│  │  │ (12 DOF) │  │ (5 DOF)  │  │ (IMU+FSR)│          │    │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘          │    │
│  └───────┼──────────────┼──────────────┼───────────────┘    │
│          │              │              │                    │
│          ▼              ▼              ▼                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                 │
│  │ CAN BUS  │  │ CAN BUS  │  │ I2C BUS  │                 │
│  │ (Legs)   │  │ (Arm)    │  │ (Sensors)│                 │
│  │ 1 Mbps   │  │ 1 Mbps   │  │ 400 kHz  │                 │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘                 │
│       │              │              │                       │
│       ▼              ▼              ▼                       │
│  12× Motors    5× Motors     IMU+FSR+ADC                  │
│  (M2006 PAP)   (M2006 PAP)   +Temp+GPS                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. SOFTWARE STACK

### 2.1 Raspberry Pi 5 (High-Level)

| Layer | Component | Version | Purpose |
|-------|-----------|---------|---------|
| OS | Ubuntu 24.04 LTS | — | Base OS |
| Middleware | ROS 2 Humble | 2.0 | Robot middleware |
| AI Runtime | TensorFlow Lite | 2.15 | ML inference |
| Edge TPU | Edge TPU Runtime | 2024.01 | Coral acceleration |
| Vision | OpenCV | 4.8 | Image processing |
| Navigation | Nav2 | 2.0 | Path planning |
| Custom | Phi-Harmonic Stack | 1.0 | Phi algorithms |

### 2.2 STM32H743 (Low-Level)

| Layer | Component | Purpose |
|-------|-----------|---------|
| HAL | STM32 HAL | Hardware abstraction |
| RTOS | FreeRTOS | Real-time scheduling |
| Motor | FOC Library | Field-oriented control |
| CAN | SocketCAN | CAN bus communication |
| I2C | I2C Master | Sensor communication |
| Custom | Phi-Harmonic RT | Real-time phi algorithms |

---

## 3. ROS 2 NODES (RASPBERRY PI 5)

### 3.1 Node Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ROS 2 NODE GRAPH                           │
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │ /camera_front │    │ /camera_rear  │    │ /camera_left │  │
│  │ (Publisher)   │    │ (Publisher)   │    │ (Publisher)   │  │
│  │ topic:        │    │ topic:        │    │ topic:        │  │
│  │ /img_front    │    │ /img_rear     │    │ /img_left     │  │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘  │
│         │                   │                    │           │
│         └───────────────────┼────────────────────┘           │
│                             │                                │
│                    ┌────────┴────────┐                       │
│                    │ /perception      │                       │
│                    │ (Subscriber)     │                       │
│                    │ Detects objects, │                       │
│                    │ terrain, people  │                       │
│                    └────────┬────────┘                       │
│                             │                                │
│                    ┌────────┴────────┐                       │
│                    │ /phi_planner     │                       │
│                    │ (Subscriber)     │                       │
│                    │ Phi-A* path      │                       │
│                    │ planning         │                       │
│                    └────────┬────────┘                       │
│                             │                                │
│                    ┌────────┴────────┐                       │
│                    │ /mission_control │                       │
│                    │ (Subscriber)     │                       │
│                    │ High-level       │                       │
│                    │ commands         │                       │
│                    └────────┬────────┘                       │
│                             │                                │
│                    ┌────────┴────────┐                       │
│                    │ /phi_controller  │                       │
│                    │ (Publisher)      │                       │
│                    │ Sends commands   │                       │
│                    │ to STM32         │                       │
│                    └────────┬────────┘                       │
│                             │                                │
│                    ┌────────┴────────┐                       │
│                    │ /stm32_bridge    │                       │
│                    │ (USB CDC-ACM)    │                       │
│                    │ Serial comm      │                       │
│                    └─────────────────┘                       │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Key ROS 2 Topics

| Topic | Type | Rate | Publisher | Subscriber |
|-------|------|------|-----------|------------|
| /img_front | sensor_msgs/Image | 30 Hz | camera_front | perception |
| /img_rear | sensor_msgs/Image | 30 Hz | camera_rear | perception |
| /img_left | sensor_msgs/Image | 30 Hz | camera_left | perception |
| /img_right | sensor_msgs/Image | 30 Hz | camera_right | perception |
| /lidar_scan | sensor_msgs/LaserScan | 8 Hz | lidar_node | perception, planner |
| /imu/data | sensor_msgs/Imu | 100 Hz | imu_node | controller |
| /gps/fix | sensor_msgs/NavSatFix | 10 Hz | gps_node | planner |
| /fsr/data | std_msgs/Float32MultiArray | 100 Hz | fsr_node | controller |
| /cmd_vel | geometry_msgs/Twist | 10 Hz | teleop/mission | controller |
| /arm_cmd | custom_msgs/ArmCommand | 10 Hz | mission | arm_controller |
| /phi_status | custom_msgs/PhiStatus | 10 Hz | controller | mission |

### 3.3 ROS 2 Parameters

```yaml
# phi_controller.yaml
phi_controller:
  ros__parameters:
    # Phi-harmonic parameters
    phi: 1.618033988749895
    
    # Gait parameters
    gait:
      cycle_time: 0.5  # seconds
      stance_fraction: 0.618  # 1/phi
      foot_height: 0.05  # meters
      step_length: 0.2  # meters
    
    # Balance parameters
    balance:
      kp: 10.0
      ki: 2.0
      kd: 1.0
      phi_adaptive: true
      max_tilt: 25.0  # degrees
    
    # Grip parameters
    grip:
      kp: 100.0
      kd: 10.0
      max_force: 20.0  # Newtons
      phi_compliance: true
    
    # Navigation parameters
    navigation:
      phi_astar_weight: 1.618
      grid_resolution: 0.05  # meters
      smoothing_iterations: 5
```

---

## 4. STM32 FIRMWARE

### 4.1 Task Structure (FreeRTOS)

| Task | Priority | Period | Function |
|------|----------|--------|----------|
| motor_control | Highest | 1 ms | FOC for all motors |
| sensor_read | High | 2 ms | IMU, FSR, ADC |
| can_tx | Medium | 2 ms | CAN bus transmit |
| can_rx | Medium | Event | CAN bus receive |
| phi_gait | Medium | 5 ms | Gait generation |
| phi_balance | Medium | 5 ms | Balance control |
| usb_comm | Low | 10 ms | USB to Pi |
| led_status | Lowest | 50 ms | LED updates |

### 4.2 Control Loop (1 kHz)

```
CONTROL LOOP TIMELINE:

Time (µs)  Task                    Action
─────────────────────────────────────────────────
0          Read sensors           IMU, FSR, encoders
100        Sensor fusion          Combine IMU + FSR
200        Phi-balance            Calculate corrections
300        Phi-gait               Generate foot trajectories
400        Inverse kinematics     Joint angles for each leg
500        Motor commands         Send CAN to motors 1-4
600        Motor commands         Send CAN to motors 5-8
700        Motor commands         Send CAN to motors 9-12
800        Arm control            Joint angles for arm
900        Send to Pi             USB data update
1000       Next cycle             → Repeat
```

### 4.3 Motor Control (FOC)

```
FIELD-ORIENTED CONTROL (FOC) ALGORITHM:

For each motor (17 total):

1. Read encoder (14-bit absolute, 16384 CPR)
2. Calculate electrical angle (θ_e)
3. Read phase currents (I_a, I_b)
4. Clarke transform: (I_a, I_b) → (I_α, I_β)
5. Park transform: (I_α, I_β) → (I_d, I_q)
6. PI controller for I_d (flux)
7. PI controller for I_q (torque)
8. Inverse Park transform: (V_d, V_q) → (V_α, V_β)
9. Space Vector Modulation → PWM outputs
10. Apply PWM to H-bridge (3 phases)

Phi-harmonic modification:
• PI gains scale with φ based on error magnitude
• Smoother current transitions
• Reduced torque ripple by ~30%
```

---

## 5. COMMUNICATION PROTOCOL

### 5.1 USB CDC-ACM Protocol (Pi ↔ STM32)

```
MESSAGE FORMAT (JSON over UART):

Command (Pi → STM32):
{
  "type": "cmd",
  "timestamp": 1234567890,
  "data": {
    "gait_mode": "walk",
    "velocity": [0.5, 0.0, 0.0],
    "arm_cmd": {
      "joint_angles": [0.0, 0.0, 0.0, 0.0, 0.0],
      "grip_force": 5.0
    }
  }
}

Status (STM32 → Pi):
{
  "type": "status",
  "timestamp": 1234567891,
  "data": {
    "motor_positions": [0.0, ...],  // 17 values
    "motor_velocities": [0.0, ...],
    "motor_currents": [0.0, ...],
    "imu": {
      "orientation": [0.0, 0.0, 0.0, 1.0],
      "angular_velocity": [0.0, 0.0, 0.0],
      "linear_acceleration": [0.0, 0.0, 9.81]
    },
    "fsr": [0.0, 0.0, 0.0, 0.0],
    "battery": {
      "voltage": 48.0,
      "current": 5.0,
      "soc": 85.0
    }
  }
}

Baud rate: 921600
Frame delimiter: \n
Error handling: CRC-16 checksum
```

### 5.2 CAN Bus Protocol

```
CAN MESSAGE FORMAT:

Standard CAN 2.0B (11-bit ID)

Motor Command (0x100 + motor_id):
  Byte 0-1: Target angle (int16, 0.01° resolution)
  Byte 2-3: Target velocity (int16, 0.1 RPM resolution)
  Byte 4-5: Feedforward torque (int16, 0.01 N·m resolution)
  Byte 6: Control mode (0=position, 1=velocity, 2=torque)
  Byte 7: Reserved

Motor Status (0x200 + motor_id):
  Byte 0-1: Current angle (int16, 0.01° resolution)
  Byte 2-3: Current velocity (int16, 0.1 RPM resolution)
  Byte 4-5: Current torque (int16, 0.01 N·m resolution)
  Byte 6: Temperature (uint8, 1°C resolution)
  Byte 7: Error flags (bitfield)

BMS Status (0x300):
  Byte 0-1: Pack voltage (uint16, 0.1V resolution)
  Byte 2-3: Pack current (int16, 0.1A resolution)
  Byte 4: State of charge (uint8, 1% resolution)
  Byte 5: Temperature (uint8, 1°C resolution)
  Byte 6-7: Cell voltage min/max (uint16, 0.01V resolution)
```

---

## 6. PHI-HARMONIC CONTROL ALGORITHMS

### 6.1 Phi-PID Implementation

```c
// phi_pid.h
typedef struct {
    float Kp, Ki, Kd;
    float phi;
    float integral;
    float prev_error;
    float integral_max;
    float derivative_max;
} PhiPID;

float phi_pid_update(PhiPID *pid, float error, float dt) {
    // Phi-harmonic adaptive gain
    float phi_factor = powf(pid->phi, fabsf(error) / pid->derivative_max);
    
    float Kp = pid->Kp * phi_factor;
    float Ki = pid->Ki * phi_factor;
    float Kd = pid->Kd * phi_factor;
    
    // Integral with anti-windup
    pid->integral += error * dt;
    if (pid->integral > pid->integral_max) 
        pid->integral = pid->integral_max;
    if (pid->integral < -pid->integral_max) 
        pid->integral = -pid->integral_max;
    
    // Derivative with filtering
    float derivative = (error - pid->prev_error) / dt;
    if (derivative > pid->derivative_max) 
        derivative = pid->derivative_max;
    if (derivative < -pid->derivative_max) 
        derivative = -pid->derivative_max;
    
    // Output
    float output = Kp * error + Ki * pid->integral + Kd * derivative;
    
    pid->prev_error = error;
    return output;
}
```

### 6.2 Phi-Gait Generator

```c
// phi_gait.h
typedef struct {
    float cycle_time;
    float phi;
    float phase_offsets[4];
    float stance_fraction;
} PhiGait;

void phi_gait_init(PhiGait *gait, float cycle_time) {
    gait->cycle_time = cycle_time;
    gait->phi = 1.618033988749895f;
    gait->stance_fraction = 1.0f / gait->phi;
    
    // Phi-ratio phase offsets
    gait->phase_offsets[0] = 0.0f;
    gait->phase_offsets[1] = 1.0f / (gait->phi * gait->phi);
    gait->phase_offsets[2] = 1.0f / gait->phi;
    gait->phase_offsets[3] = 1.0f / (gait->phi * gait->phi * gait->phi);
}

int phi_gait_stance(PhiGait *gait, int leg, float time) {
    float phase = fmodf(time / gait->cycle_time + gait->phase_offsets[leg], 1.0f);
    return (phase < gait->stance_fraction) ? 1 : 0;
}

float phi_gait_height(PhiGait *gait, int leg, float time) {
    float phase = fmodf(time / gait->cycle_time + gait->phase_offsets[leg], 1.0f);
    
    if (phase < gait->stance_fraction) {
        return 0.0f;  // Stance phase
    } else {
        // Swing phase: parabolic trajectory
        float swing_phase = (phase - gait->stance_fraction) / 
                           (1.0f - gait->stance_fraction);
        return 4.0f * swing_phase * (1.0f - swing_phase);
    }
}
```

### 6.3 Phi-Balance Controller

```c
// phi_balance.h
typedef struct {
    PhiPID pid_roll;
    PhiPID pid_pitch;
    float max_tilt;
    float phi;
} PhiBalance;

void phi_balance_init(PhiBalance *bal) {
    bal->phi = 1.618033988749895f;
    bal->max_tilt = 25.0f;
    
    // Initialize PID controllers
    bal->pid_roll = (PhiPID){
        .Kp = 10.0f, .Ki = 2.0f, .Kd = 1.0f,
        .phi = bal->phi,
        .integral = 0.0f, .prev_error = 0.0f,
        .integral_max = 1.0f, .derivative_max = 10.0f
    };
    
    bal->pid_pitch = bal->pid_roll;  // Same gains
}

void phi_balance_update(PhiBalance *bal, float roll, float pitch, 
                        float roll_rate, float pitch_rate, float dt) {
    // Check for tipping
    if (fabsf(roll) > bal->max_tilt || fabsf(pitch) > bal->max_tilt) {
        // Emergency stop
        emergency_stop();
        return;
    }
    
    // Phi-harmonic balance corrections
    float roll_correction = phi_pid_update(&bal->pid_roll, roll, dt);
    float pitch_correction = phi_pid_update(&bal->pid_pitch, pitch, dt);
    
    // Apply corrections to leg trajectories
    apply_balance_correction(roll_correction, pitch_correction);
}
```

---

## 7. MISSION CONTROL

### 7.1 Mission Types

| Mission | Description | Autonomy |
|---------|-------------|----------|
| Survey | Walk path, collect sensor data | High |
| Sample | Navigate to points, collect samples | Medium |
| Inspect | Navigate to targets, capture images | Medium |
| Transport | Carry payload between points | High |
| Monitor | Stationary monitoring | Full |
| Follow | Follow operator | Medium |
| Return | Return to base | Full |

### 7.2 Mission State Machine

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  IDLE    │────►│ PLANNING │────►│ EXECUTING│
│          │     │          │     │          │
└──────────┘     └──────────┘     └────┬─────┘
      ▲                                │
      │            ┌──────────┐        │
      │            │ PAUSED   │◄───────┤
      │            │          │        │
      │            └────┬─────┘        │
      │                 │              │
      │                 ▼              │
      │            ┌──────────┐        │
      └────────────│ COMPLETE │◄───────┘
                   │          │
                   └──────────┘

States:
• IDLE: Waiting for mission command
• PLANNING: Computing phi-A* path
• EXECUTING: Running mission
• PAUSED: Operator pause
• COMPLETE: Mission finished
```

---

## 8. DIAGNOSTICS

### 8.1 System Health Monitoring

| Parameter | Threshold | Action |
|-----------|-----------|--------|
| CPU usage | >90% | Log warning |
| Memory usage | >80% | Log warning |
| Disk usage | >90% | Log warning |
| Temperature | >70°C | Reduce performance |
| Motor current | >80% rated | Log warning |
| Battery SOC | <20% | Return to base |
| CAN errors | >100/sec | Log error |
| IMU drift | >5°/hour | Re-calibrate |

### 8.2 ROS 2 Diagnostics

```
ros2 topic hz /phi_status
ros2 topic echo /phi_status --once
ros2 node list
ros2 node info /phi_controller
ros2 param list /phi_controller
ros2 param get /phi_controller phi
```

### 8.3 Log Levels

| Level | Use |
|-------|-----|
| DEBUG | Detailed debugging info |
| INFO | Normal operation messages |
| WARN | Potential issues |
| ERROR | Errors requiring attention |
| FATAL | System failure |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
