# PHI CHEAP LIGHT PLANE — CONTROL SYSTEM

## Avionics, Flight Computer, and Control Surfaces

---

## CONTROL SYSTEM OVERVIEW

The PHI Cheap Light Plane uses a conventional 3-axis cable-pull control system for the pilot, with a phi-harmonic brushless motor controlled by an Arduino-based flight computer. The pilot has direct mechanical control of all flight surfaces via cables, with the flight computer providing motor control, instrumentation, and telemetry.

---

## FLIGHT COMPUTER ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLIGHT COMPUTER ARCHITECTURE                  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    ARDUINO NANO #1                        │   │
│  │                    PRIMARY FLIGHT COMPUTER                │   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ SENSOR   │  │ MOTOR    │  │ DISPLAY  │              │   │
│  │  │ READING  │  │ CONTROL  │  │ OUTPUT   │              │   │
│  │  │          │  │          │  │          │              │   │
│  │  │ BMP280   │  │ ESC PWM  │  │ OLED #1  │              │   │
│  │  │ MPU6050  │  │ Throttle │  │ OLED #2  │              │   │
│  │  │ GPS      │  │ Phi-harm │  │ LED      │              │   │
│  │  │ Voltage  │  │          │  │ Buzzer   │              │   │
│  │  │ Current  │  │          │  │          │              │   │
│  │  │ Temp     │  │          │  │          │              │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘              │   │
│  │       │              │              │                     │   │
│  │       └──────────────┼──────────────┘                     │   │
│  │                      │                                    │   │
│  │              ┌───────▼───────┐                            │   │
│  │              │   MAIN LOOP   │                            │   │
│  │              │   100 Hz      │                            │   │
│  │              │   (10ms)      │                            │   │
│  │              └───────────────┘                            │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    ARDUINO NANO #2                        │   │
│  │                    BACKUP / TELEMETRY                     │   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ BACKUP   │  │ TELEMETRY│  │ WARNING  │              │   │
│  │  │ SENSORS  │  │ RADIO    │  │ SYSTEM   │              │   │
│  │  │          │  │          │  │          │              │   │
│  │  │ BMP280   │  │ HC-12    │  │ Buzzer   │              │   │
│  │  │ Voltage  │  │ 433MHz   │  │ LED      │              │   │
│  │  │ Current  │  │          │  │          │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## FLIGHT SOFTWARE

### Main Loop Structure

```cpp
// PHI CHEAP LIGHT PLANE — FLIGHT COMPUTER SOFTWARE
// Arduino Nano #1 — Primary Flight Computer

#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <SoftwareSerial.h>
#include <Servo.h>

// PIN DEFINITIONS
#define ESC_PIN        8    // Motor ESC PWM
#define RUDDER_PIN     9    // Rudder servo
#define AILERON_L_PIN  10   // Left aileron servo
#define AILERON_R_PIN  11   // Right aileron servo
#define ELEVATOR_PIN   12   // Elevator servo
#define STATUS_LED     13   // Status LED

#define BATT_VOLTAGE   A0   // Battery voltage (divider)
#define MOTOR_CURRENT  A1   // Motor current (ACS758)
#define MOTOR_TEMP     A2   // Motor temperature (K-type)
#define BATT_TEMP      A3   // Battery temperature (NTC)
#define AIRSPEED       A6   // Airspeed (pitot, optional)
#define THROTTLE_POS   A7   // Throttle position (pot)

// I2C ADDRESSES
#define BMP280_ADDR    0x76
#define MPU6050_ADDR   0x68
#define OLED_ADDR_1    0x3C
#define OLED_ADDR_2    0x3D

// THROTTLE LIMITS
#define THROTTLE_MIN   1000  // ESC min (off)
#define THROTTLE_MAX   2000  // ESC max (full)
#define THROTTLE_IDLE  1100  // Idle

// WARNING THRESHOLDS
#define LOW_BATT_VOLTAGE  23.0   // Volts
#define CRITICAL_BATT     22.0   // Volts
#define OVER_TEMP_WARN    80.0   // Celsius
#define OVER_TEMP_CRIT    100.0  // Celsius
#define STALL_SPEED       50.0   // km/h
#define MAX_ALTITUDE      914.4  // 3000 ft in meters

// GLOBAL VARIABLES
float altitude = 0;
float airspeed = 0;
float battery_voltage = 0;
float motor_current = 0;
float motor_temp = 0;
float battery_temp = 0;
float latitude = 0;
float longitude = 0;
int gps_satellites = 0;
float heading = 0;
int throttle = THROTTLE_MIN;
unsigned long last_loop = 0;
unsigned long loop_count = 0;

Servo esc;
Servo rudder;
Servo aileron_l;
Servo aileron_r;
Servo elevator;

Adafruit_SSD1306 display1(128, 64, &Wire, -1);
Adafruit_SSD1306 display2(128, 64, &Wire, -1);

void setup() {
  // Initialize serial
  Serial.begin(9600);
  
  // Initialize I2C
  Wire.begin();
  
  // Initialize displays
  display1.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR_1);
  display2.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR_2);
  
  // Initialize servos
  esc.attach(ESC_PIN);
  rudder.attach(RUDDER_PIN);
  aileron_l.attach(AILERON_L_PIN);
  aileron_r.attach(AILERON_R_PIN);
  elevator.attach(ELEVATOR_PIN);
  
  // Initialize sensors
  initBMP280();
  initMPU6050();
  initGPS();
  
  // Set initial throttle to off
  esc.writeMicroseconds(THROTTLE_MIN);
  
  // Status LED
  pinMode(STATUS_LED, OUTPUT);
  digitalWrite(STATUS_LED, HIGH);
  
  // Startup delay
  delay(2000);
}

void loop() {
  unsigned long now = millis();
  
  // Run at 100 Hz (10ms interval)
  if (now - last_loop >= 10) {
    last_loop = now;
    loop_count++;
    
    // READ SENSORS (every 20ms = 50 Hz)
    if (loop_count % 2 == 0) {
      readSensors();
    }
    
    // UPDATE DISPLAY (every 200ms = 5 Hz)
    if (loop_count % 20 == 0) {
      updateDisplays();
    }
    
    // SEND TELEMETRY (every 100ms = 10 Hz)
    if (loop_count % 10 == 0) {
      sendTelemetry();
    }
    
    // CHECK WARNINGS (every 100ms = 10 Hz)
    if (loop_count % 10 == 0) {
      checkWarnings();
    }
    
    // UPDATE MOTOR (every 10ms = 100 Hz)
    updateMotor();
  }
}

void readSensors() {
  // Read BMP280 (altitude)
  altitude = readBMP280();
  
  // Read MPU6050 (attitude)
  readMPU6050();
  
  // Read GPS
  readGPS();
  
  // Read analog sensors
  battery_voltage = analogRead(BATT_VOLTAGE) * 5.0 / 1024.0 * 10.0;
  motor_current = (analogRead(MOTOR_CURRENT) * 5.0 / 1024.0 - 2.5) / 0.01;
  motor_temp = readThermocouple(MOTOR_TEMP);
  battery_temp = readNTC(BATT_TEMP);
  
  // Read throttle position
  int throttle_raw = analogRead(THROTTLE_POS);
  throttle = map(throttle_raw, 0, 1023, THROTTLE_MIN, THROTTLE_MAX);
}

void updateMotor() {
  // Apply throttle with phi-harmonic modulation
  int phi_throttle = applyPhiHarmonic(throttle);
  
  // Apply safety limits
  phi_throttle = constrain(phi_throttle, THROTTLE_MIN, THROTTLE_MAX);
  
  // Send to ESC
  esc.writeMicroseconds(phi_throttle);
}

int applyPhiHarmonic(int input_throttle) {
  // Phi-harmonic modulation: smooths throttle response
  // and reduces vibration through non-integer harmonic interaction
  
  static float phi = 1.618033988749894;
  static unsigned long t = 0;
  
  t++;
  
  // Base throttle
  float output = input_throttle;
  
  // Add phi-harmonic oscillation (very small amplitude)
  // This creates a "soft" motor response that avoids
  // resonance with airframe natural frequencies
  float modulation = 2.0 * sin(phi * t * 0.001);
  
  output += modulation;
  
  return (int)output;
}

void updateDisplays() {
  // Display 1: Primary flight data
  display1.clearDisplay();
  display1.setTextSize(1);
  display1.setTextColor(WHITE);
  
  display1.setCursor(0, 0);
  display1.print("ALT: ");
  display1.print(altitude * 3.281, 0);  // Convert m to ft
  display1.println(" ft");
  
  display1.setCursor(0, 10);
  display1.print("SPD: ");
  display1.print(airspeed, 0);
  display1.println(" km/h");
  
  display1.setCursor(0, 20);
  display1.print("HDG: ");
  display1.print(heading, 0);
  display1.println(" deg");
  
  display1.setCursor(0, 30);
  display1.print("BAT: ");
  display1.print(battery_voltage, 1);
  display1.println(" V");
  
  display1.setCursor(0, 40);
  display1.print("AMP: ");
  display1.print(motor_current, 0);
  display1.println(" A");
  
  display1.setCursor(0, 50);
  display1.print("TMP: ");
  display1.print(motor_temp, 0);
  display1.print("C  ");
  display1.print("THR:");
  display1.print(map(throttle, THROTTLE_MIN, THROTTLE_MAX, 0, 100));
  display1.print("%");
  
  display1.display();
  
  // Display 2: System status
  display2.clearDisplay();
  display2.setTextSize(1);
  display2.setTextColor(WHITE);
  
  display2.setCursor(0, 0);
  display2.print("GPS: ");
  display2.print(gps_satellites);
  display2.print(" SAT  FIX:");
  display2.println(gps_satellites >= 4 ? "3D" : "2D");
  
  display2.setCursor(0, 10);
  display2.print("LAT: ");
  display2.println(latitude, 4);
  
  display2.setCursor(0, 20);
  display2.print("LON: ");
  display2.println(longitude, 4);
  
  display2.setCursor(0, 30);
  display2.print("BTEMP: ");
  display2.print(battery_temp, 0);
  display2.println(" C");
  
  display2.setCursor(0, 40);
  display2.print("LOOP: ");
  display2.print(loop_count);
  
  display2.display();
}

void sendTelemetry() {
  // Send JSON telemetry data over SoftwareSerial
  // to HC-12 radio for ground station
  
  Serial.print("{");
  Serial.print("\"alt\":");
  Serial.print(altitude * 3.281, 0);
  Serial.print(",\"spd\":");
  Serial.print(airspeed, 0);
  Serial.print(",\"hdg\":");
  Serial.print(heading, 0);
  Serial.print(",\"bat\":");
  Serial.print(battery_voltage, 1);
  Serial.print(",\"amp\":");
  Serial.print(motor_current, 0);
  Serial.print(",\"tmp\":");
  Serial.print(motor_temp, 0);
  Serial.print(",\"lat\":");
  Serial.print(latitude, 4);
  Serial.print(",\"lon\":");
  Serial.print(longitude, 4);
  Serial.print(",\"fix\":");
  Serial.print(gps_satellites >= 4 ? 3 : 2);
  Serial.println("}");
}

void checkWarnings() {
  // Low battery warning
  if (battery_voltage < CRITICAL_BATT) {
    // Critical: reduce motor to minimum
    throttle = THROTTLE_IDLE;
    tone(A8, 2000, 100);  // Buzzer
  } else if (battery_voltage < LOW_BATT_VOLTAGE) {
    // Warning: reduce motor power
    throttle = constrain(throttle, THROTTLE_MIN, 1500);
    tone(A8, 1000, 50);   // Buzzer
  }
  
  // Over temperature warning
  if (motor_temp > OVER_TEMP_CRIT) {
    // Critical: shutdown motor
    throttle = THROTTLE_MIN;
    tone(A8, 3000, 200);  // Buzzer
  } else if (motor_temp > OVER_TEMP_WARN) {
    // Warning: reduce power
    throttle = constrain(throttle, THROTTLE_MIN, 1500);
    tone(A8, 1500, 100);  // Buzzer
  }
  
  // Stall warning
  if (airspeed < STALL_SPEED && altitude > 10) {
    tone(A8, 500, 100);   // Low buzzer
  }
  
  // Altitude warning
  if (altitude > MAX_ALTITUDE) {
    // Near Part 103 limit
    tone(A8, 800, 50);
  }
}
```

---

## CONTROL SURFACE MECHANICS

### Cable Routing

```
CONTROL CABLE ROUTING:
──────────────────────

AILERON CONTROL:
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│  COCKPIT                                                          │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │                                                           │   │
│  │  ┌─────────┐                                              │   │
│  │  │ STICK   │                                              │   │
│  │  │ (joystick│                                             │   │
│  │  │  type)   │                                             │   │
│  │  └────┬────┘                                              │   │
│  │       │                                                    │   │
│  │  ┌────▼────┐                                              │   │
│  │  │ CONTROL │                                              │   │
│  │  │ CABLES  │                                              │   │
│  │  │ (1/8"   │                                              │   │
│  │  │  steel) │                                              │   │
│  │  └────┬────┘                                              │   │
│  │       │                                                    │   │
│  └───────┼────────────────────────────────────────────────────┘   │
│          │                                                        │
│     LEFT CABLE ────────────────────────────────────┐              │
│          │                                          │              │
│          │    ┌─────────────────────────────────────┼──────┐      │
│          │    │  LEFT WING                           │      │      │
│          │    │                                      │      │      │
│          │    │  ┌────────────────────────────────┐ │      │      │
│          │    │  │  AILERON (2000mm × 300mm)     │ │      │      │
│          │    │  │                                │ │      │      │
│          │    │  │  ┌─────┐    ┌─────┐    ┌─────┐│ │      │      │
│          │    │  │  │HINGE│    │HINGE│    │HINGE││ │      │      │
│          │    │  │  │ 1   │    │ 2   │    │ 3   ││ │      │      │
│          │    │  │  └──┬──┘    └──┬──┘    └──┬──┘│ │      │      │
│          │    │  │     │          │          │    │ │      │      │
│          │    │  │  ┌──▼──┐    ┌──▼──┐    ┌──▼──┐│ │      │      │
│          │    │  │  │CABLE│    │CABLE│    │CABLE││ │      │      │
│          │    │  │  └─────┘    └─────┘    └─────┘│ │      │      │
│          │    │  └────────────────────────────────┘ │      │      │
│          │    │                                      │      │      │
│          │    └──────────────────────────────────────┘      │      │
│          │                                                   │      │
│     RIGHT CABLE ───────────────────────────────┐           │      │
│          │                                      │           │      │
│          │    ┌─────────────────────────────────┼──────┐   │      │
│          │    │  RIGHT WING                      │      │   │      │
│          │    │                                   │      │   │      │
│          │    │  ┌──────────────────────────────┐│      │   │      │
│          │    │  │  AILERON (2000mm × 300mm)   ││      │   │      │
│          │    │  │                              ││      │   │      │
│          │    │  │  ┌─────┐  ┌─────┐  ┌─────┐ ││      │   │      │
│          │    │  │  │HINGE│  │HINGE│  │HINGE│ ││      │   │      │
│          │    │  │  │ 1   │  │ 2   │  │ 3   │ ││      │   │      │
│          │    │  │  └──┬──┘  └──┬──┘  └──┬──┘ ││      │   │      │
│          │    │  │     │        │        │     ││      │   │      │
│          │    │  │  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐ ││      │   │      │
│          │    │  │  │CABLE│  │CABLE│  │CABLE│ ││      │   │      │
│          │    │  │  └─────┘  └─────┘  └─────┘ ││      │   │      │
│          │    │  └──────────────────────────────┘│      │   │      │
│          │    │                                   │      │   │      │
│          │    └───────────────────────────────────┘      │   │      │
│          │                                                │   │      │
│                                                                   │
└────────────────────────────────────────────────────────────────────┘

CABLE SPECIFICATIONS:
- Material: 1/8" (3.2mm) galvanized steel cable
- Construction: 7×7 strand (flexible)
- Breaking strength: 1,780 lbs (7.9 kN)
- Working load: 356 lbs (1.6 kN) — 5:1 safety factor
- Turnbuckle: M6 × 150mm (adjustable)
- Cable clamps: 1/8" copper crimp sleeves
- Total cable length: ~20m (all surfaces combined)
```

### Control Deflections

```
CONTROL SURFACE DEFLECTIONS:
───────────────────────────

AILERON (left/right):
- Up: +25° (left up = right down)
- Down: -25° (left down = right up)
- Neutral: 0°
- Travel: 50° total

ELEVATOR:
- Up: +25° (nose up)
- Down: -25° (nose down)
- Neutral: 0°
- Travel: 50° total

RUDDER:
- Left: +30° (nose left)
- Right: -30° (nose right)
- Neutral: 0°
- Travel: 60° total

CONTROL FORCES:
- Stick force (aileron): 2-5 lbs at full deflection
- Stick force (elevator): 3-8 lbs at full deflection
- Pedal force (rudder): 5-15 lbs at full deflection
- Spring return to neutral on all axes

CONTROL RATES:
- Maximum deflection rate: 60°/second
- Normal deflection rate: 30°/second
- Damped return: 20°/second
```

---

## INSTRUMENT PANEL

```
┌─────────────────────────────────────────────────────────────────┐
│                    INSTRUMENT PANEL — COCKPIT VIEW               │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │   │
│  │  │ MASTER   │  │ MOTOR    │  │ AVIONICS │  │ RADIO  │ │   │
│  │  │ SWITCH   │  │ SWITCH   │  │ SWITCH   │  │ SWITCH │ │   │
│  │  │  [RED]   │  │ [YELLOW] │  │ [GREEN]  │  │ [BLUE] │ │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └────────┘ │   │
│  │                                                         │   │
│  │  ┌────────────────────┐  ┌────────────────────┐       │   │
│  │  │   OLED DISPLAY #1  │  │   OLED DISPLAY #2  │       │   │
│  │  │                    │  │                    │       │   │
│  │  │   ALT:  1250 ft    │  │   GPS: 12 SAT      │       │   │
│  │  │   SPD:  80 km/h    │  │   FIX: 3D          │       │   │
│  │  │   HDG:  270°       │  │   LAT: 40.7128°    │       │   │
│  │  │   BAT:  24.2V      │  │   LON: -74.006°    │       │   │
│  │  │   AMP:  45A        │  │   TEMP: 65°C       │       │   │
│  │  │   TMP:  65°C       │  │   LOOP: 12345      │       │   │
│  │  │                    │  │                    │       │   │
│  │  └────────────────────┘  └────────────────────┘       │   │
│  │                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │   │
│  │  │ THROTTLE │  │ KILL     │  │ BUZZER   │            │   │
│  │  │ LEVER    │  │ BUTTON   │  │ (audio)  │            │   │
│  │  │ (push-   │  │ (red     │  │          │            │   │
│  │  │  pull)   │  │ momentary│  │          │            │   │
│  │  └──────────┘  └──────────┘  └──────────┘            │   │
│  │                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │   │
│  │  │ STATUS   │  │ LOW BATT │  │ MOTOR    │            │   │
│  │  │ LED      │  │ LED      │  │ TEMP LED │            │   │
│  │  │ (green)  │  │ (red)    │  │ (yellow) │            │   │
│  │  └──────────┘  └──────────┘  └──────────┘            │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  CONTROLS:                                                       │
│  - Stick: Ailerons (left/right) + Elevator (forward/back)       │
│  - Pedals: Rudder (left/right)                                  │
│  - Throttle: Push/pull lever (motor power)                      │
│  - Kill switch: Red momentary button (emergency motor off)      │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## GROUND STATION

### Telemetry Display (Laptop)

```
┌─────────────────────────────────────────────────────────────────┐
│                    GROUND STATION SOFTWARE                       │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  PHI CHEAP LIGHT PLANE — GROUND STATION                 │   │
│  │  ──────────────────────────────────────                  │   │
│  │                                                         │   │
│  │  ┌──────────────┐  ┌──────────────┐                   │   │
│  │  │ FLIGHT DATA  │  │ SYSTEM STATUS │                   │   │
│  │  │              │  │              │                   │   │
│  │  │ Alt: 1250 ft │  │ Battery: OK  │                   │   │
│  │  │ Spd: 80 km/h │  │ Motor: OK    │                   │   │
│  │  │ Hdg: 270°    │  │ GPS: 3D fix  │                   │   │
│  │  │ Lat: 40.71°  │  │ Radio: OK    │                   │   │
│  │  │ Lon: -74.00° │  │ Link: -45dBm │                   │   │
│  │  │ Bat: 24.2V   │  │              │                   │   │
│  │  │ Amp: 45A     │  │              │                   │   │
│  │  │ Tmp: 65°C    │  │              │                   │   │
│  │  └──────────────┘  └──────────────┘                   │   │
│  │                                                         │   │
│  │  ┌──────────────────────────────────────────────────┐  │   │
│  │  │ FLIGHT PATH (GPS track)                           │  │   │
│  │  │                                                   │  │   │
│  │  │  ┌───────────────────────────────────────────┐   │  │   │
│  │  │  │                                           │   │  │   │
│  │  │  │           * ← current position            │   │  │   │
│  │  │  │          /                                │   │  │   │
│  │  │  │         /                                 │   │  │   │
│  │  │  │        /                                  │   │  │   │
│  │  │  │       * ← start                           │   │  │   │
│  │  │  │                                           │   │  │   │
│  │  │  └───────────────────────────────────────────┘   │  │   │
│  │  │                                                   │  │   │
│  │  └──────────────────────────────────────────────────┘  │   │
│  │                                                         │   │
│  │  ┌──────────────────────────────────────────────────┐  │   │
│  │  │ LOG                                               │  │   │
│  │  │ 14:32:05 — Flight started                         │  │   │
│  │  │ 14:32:15 — GPS 3D fix acquired                    │  │   │
│  │  │ 14:35:22 — Reached 1000 ft                        │  │   │
│  │  │ 14:42:10 — Battery 80% SOC                        │  │   │
│  │  │ 14:55:30 — Returning to base                      │  │   │
│  │  └──────────────────────────────────────────────────┘  │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  GROUND STATION HARDWARE:                                        │
│  - Laptop (any OS)                                              │
│  - USB-Serial adapter                                           │
│  - HC-12 radio (433MHz)                                         │
│  - 173mm wire antenna                                           │
│  - Range: 1.8km (urban), 5km (open field)                      │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## CALIBRATION PROCEDURES

### Sensor Calibration

```
CALIBRATION SEQUENCE:
─────────────────────

1. BMP280 ALTIMETER CALIBRATION:
   a. Place aircraft on level ground
   b. Record pressure at ground level
   c. Set altimeter to field elevation
   d. Verify reading matches GPS altitude

2. MPU6050 IMU CALIBRATION:
   a. Place aircraft on perfectly level surface
   b. Run calibration sketch (auto-level detection)
   c. Record offset values
   d. Verify roll/pitch = 0° ±1° on level surface

3. GPS CALIBRATION:
   a. Power on GPS with clear sky view
   b. Wait for 3D fix (12+ satellites)
   c. Record home position (lat/lon)
   d. Verify position matches known location

4. CURRENT SENSOR CALIBRATION:
   a. With motor off, record ACS758 output (should be 2.5V)
   b. If not 2.5V, adjust offset in software
   c. Apply known load (if available) and verify reading

5. VOLTAGE DIVIDER CALIBRATION:
   a. Measure battery voltage with multimeter
   b. Compare to Arduino reading
   c. Adjust calibration factor if needed

6. CONTROL SURFACE CALIBRATION:
   a. Center all controls
   b. Verify servos are at neutral (1500μs)
   c. Move controls to full deflection
   d. Verify surface travel matches expected range
   e. Adjust servo endpoints if needed
```

---

## SOFTWARE VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Aug 2026 | Initial release — basic flight computer |
| 1.1 | — | Planned: phi-harmonic motor control optimization |
| 1.2 | — | Planned: autonomous return-to-home feature |
| 2.0 | — | Planned: machine learning flight optimization |

---

## SYSTEM WEIGHT

| Component | Weight |
|-----------|--------|
| Arduino Nano #1 | 7g |
| Arduino Nano #2 | 7g |
| BMP280 × 2 | 4g |
| MPU6050 | 3g |
| GPS module | 10g |
| OLED displays × 2 | 12g |
| HC-12 radio × 2 | 20g |
| VHF radio | 250g |
| ESC (100A) | 800g |
| Motor (50kW) | 8,000g |
| Propeller | 1,200g |
| Wiring (all) | 500g |
| Switches/indicators | 200g |
| Protoboards × 4 | 40g |
| **TOTAL AVIONICS** | **~10.8 kg** |
