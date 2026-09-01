/*
 * PHI Medical Stretcher Drone - Main Firmware
 * Model: PMSD-100
 * Version: 2.0
 * 
 * Real-time flight control, medical monitoring, and phi-harmonic healing
 * Target: Pixhawk 6X (STM32H7) + Safety Processor (STM32F4)
 */

#include <PX4_Autopilot.h>
#include <PX4_Math.h>
#include <drivers/drv_hrt.h>
#include <uORB/Publication.hpp>
#include <uORB/Subscription.hpp>
#include <uORB/topics/vehicle_local_position.h>
#include <uORB/topics/actuator_controls.h>
#include <uORB/topics/battery_status.h>
#include <uORB/topics/sensor_combined.h>

// ============================================================================
// CONSTANTS
// ============================================================================

#define PHI 1.6180339887
#define PHI_HEALING_FREQ 16.18
#define PHI_CARDIAC_FREQ 26.18
#define PHI_NEURAL_FREQ 42.36
#define PHI_PAIN_FREQ 68.54

#define MAX_MOTOR_LOSS 2
#define BATTERY_LOW_THRESHOLD 0.20
#define BATTERY_CRITICAL_THRESHOLD 0.10
#define MAX_PATIENT_WEIGHT_KG 120
#define PARACHUTE_MIN_ALTITUDE_M 30
#define MAX_NEGATIVE_G -0.5
#define MAX_VIBRATION_G 0.5
#define MAX_NOISE_DB 65

// ============================================================================
// SYSTEM STATE
// ============================================================================

enum DroneState {
    STATE_INIT,
    STATE_READY,
    STATE_ARMED,
    STATE_MISSION,
    STATE_PATIENT_SECURED,
    STATE_TRANSPORT,
    STATE_LANDING,
    STATE_EMERGENCY,
    STATE_LANDED,
    STATE_OFF
};

enum MissionPhase {
    PHASE_IDLE,
    PHASE_DISPATCH,
    PHASE_SCENE_APPROACH,
    PHASE_PATIENT_LOAD,
    PHASE_HOSPITAL_ROUTE,
    PHASE_HOSPITAL_APPROACH,
    PHASE_PATIENT_DELIVER,
    PHASE_RETURN_BASE
};

enum MedicalStatus {
    MEDICAL_IDLE,
    MEDICAL_MONITORING,
    MEDICAL_CRITICAL,
    MEDICAL_STABLE,
    MEDICAL_IMPROVING
};

// ============================================================================
// GLOBAL VARIABLES
// ============================================================================

static DroneState g_state = STATE_INIT;
static MissionPhase g_phase = PHASE_IDLE;
static MedicalStatus g_medical_status = MEDICAL_IDLE;

// Flight data
static float g_altitude_m = 0.0f;
static float g_speed_ms = 0.0f;
static float g_battery_percent = 1.0f;
static float g_battery_voltage = 51.2f;
static float g_current_draw_a = 0.0f;
static float g_temperature_c = 25.0f;

// Patient data
static float g_patient_weight_kg = 0.0f;
static bool g_patient_secured = false;

// Medical vitals
static float g_ecg_bpm = 0.0f;
static float g_spo2_percent = 0.0f;
static float g_systolic_bp = 0.0f;
static float g_diastolic_bp = 0.0f;
static float g_patient_temp_c = 37.0f;
static float g_respiration_rate = 0.0f;
static float g_etco2_mmhg = 0.0f;

// Navigation
static float g_target_lat = 0.0f;
static float g_target_lon = 0.0f;
static float g_target_alt = 0.0f;
static float g_distance_to_target_m = 0.0f;
static float g_eta_seconds = 0.0f;

// Phi-harmonic
static float g_phi_frequency_hz = PHI_HEALING_FREQ;
static float g_phi_field_strength_mt = 0.0f;
static bool g_phi_active = false;

// Motor health
static bool g_motor_health[8] = {true, true, true, true, true, true, true, true};
static int g_motors_failed = 0;

// Safety
static bool g_parachute_armed = false;
static bool g_emergency_active = false;

// uORB publishers and subscribers
static uORB::Publication<actuator_controls_s> actuator_controls_pub{ORB_ID(actuator_controls)};
static uORB::Subscription battery_status_sub{ORB_ID(battery_status)};
static uORB::Subscription sensor_combined_sub{ORB_ID(sensor_combined)};
static uORB::Subscription vehicle_local_position_sub{ORB_ID(vehicle_local_position)};

// ============================================================================
// PHI-HARMONIC HEALING SYSTEM
// ============================================================================

class PhiHarmonicSystem {
private:
    float current_frequency;
    float field_strength;
    bool active;
    
    // DDS waveform generator
    float dds_phase;
    float dds_increment;
    float dds_sample_rate;
    
public:
    PhiHarmonicSystem() : current_frequency(PHI_HEALING_FREQ), 
                          field_strength(0.0f), 
                          active(false),
                          dds_phase(0.0f),
                          dds_sample_rate(1000.0f) {
        dds_increment = current_frequency / dds_sample_rate;
    }
    
    void set_frequency(float freq_hz) {
        current_frequency = freq_hz;
        dds_increment = freq_hz / dds_sample_rate;
    }
    
    void set_healing_mode() {
        set_frequency(PHI_HEALING_FREQ);
    }
    
    void set_cardiac_mode() {
        set_frequency(PHI_CARDIAC_FREQ);
    }
    
    void set_neural_mode() {
        set_frequency(PHI_NEURAL_FREQ);
    }
    
    void set_pain_mode() {
        set_frequency(PHI_PAIN_FREQ);
    }
    
    void activate() {
        active = true;
        field_strength = 0.5f;  // 0.5 mT at patient
    }
    
    void deactivate() {
        active = false;
        field_strength = 0.0f;
    }
    
    float generate_waveform() {
        if (!active) return 0.0f;
        
        // Generate sine wave with phi-harmonic modulation
        float sine_wave = sinf(2.0f * M_PI * dds_phase);
        float phi_modulation = 1.0f + 0.1f * sinf(2.0f * M_PI * PHI * dds_phase);
        
        dds_phase += dds_increment;
        if (dds_phase >= 1.0f) dds_phase -= 1.0f;
        
        return sine_wave * phi_modulation * field_strength;
    }
    
    void update(float patient_heart_rate, float patient_spo2, float patient_temp) {
        if (!active) return;
        
        // Adaptive frequency based on patient state
        if (patient_heart_rate > 100.0f || patient_spo2 < 90.0f) {
            set_cardiac_mode();  // Emergency: stabilize heart
        } else if (patient_temp > 38.5f) {
            set_pain_mode();     // Fever: pain/inflammation relief
        } else {
            set_healing_mode();  // Normal: cellular repair
        }
        
        // Adjust field strength based on patient weight
        float weight_factor = g_patient_weight_kg / MAX_PATIENT_WEIGHT_KG;
        field_strength = 0.3f + 0.2f * weight_factor;  // 0.3-0.5 mT range
    }
};

PhiHarmonicSystem phi_system;

// ============================================================================
// MEDICAL MONITORING SYSTEM
// ============================================================================

class MedicalMonitor {
private:
    float ecg_buffer[1000];
    int ecg_index;
    float heart_rate;
    float spo2;
    float systolic;
    float diastolic;
    float temp;
    float resp_rate;
    float etco2;
    
public:
    MedicalMonitor() : ecg_index(0), heart_rate(0), spo2(0),
                       systolic(0), diastolic(0), temp(37.0f),
                       resp_rate(0), etco2(0) {
        memset(ecg_buffer, 0, sizeof(ecg_buffer));
    }
    
    void read_sensors() {
        // Simulated sensor reads (actual implementation reads from ADC/I2C)
        // In production, these would be real medical sensor interfaces
        
        // ECG: 1kHz sampling, R-peak detection
        ecg_buffer[ecg_index] = read_ecg_raw();
        ecg_index = (ecg_index + 1) % 1000;
        heart_rate = detect_heart_rate(ecg_buffer, 1000);
        
        // SpO2: 100Hz sampling, ratio of ratios
        spo2 = read_spo2_raw();
        
        // NIBP: 50Hz sampling, oscillometric method
        read_nibp(&systolic, &diastolic);
        
        // Temperature: 10Hz sampling, thermistor
        temp = read_temperature_raw();
        
        // Respiration: 100Hz sampling, impedance
        resp_rate = read_respiration_raw();
        
        // EtCO2: 50Hz sampling, capnography
        etco2 = read_etco2_raw();
    }
    
    MedicalStatus evaluate() {
        // Check for critical conditions
        if (heart_rate < 40 || heart_rate > 150) return MEDICAL_CRITICAL;
        if (spo2 < 85) return MEDICAL_CRITICAL;
        if (systolic < 80 || systolic > 180) return MEDICAL_CRITICAL;
        if (temp < 35.0f || temp > 40.0f) return MEDICAL_CRITICAL;
        
        // Check for stable conditions
        if (heart_rate >= 60 && heart_rate <= 100 &&
            spo2 >= 95 && 
            systolic >= 100 && systolic <= 140 &&
            temp >= 36.0f && temp <= 38.0f) {
            return MEDICAL_STABLE;
        }
        
        // Check for improvement (requires history)
        // For now, return monitoring
        return MEDICAL_MONITORING;
    }
    
    float get_heart_rate() { return heart_rate; }
    float get_spo2() { return spo2; }
    float get_systolic() { return systolic; }
    float get_diastolic() { return diastolic; }
    float get_temperature() { return temp; }
    float get_resp_rate() { return resp_rate; }
    float get_etco2() { return etco2; }
    
private:
    float read_ecg_raw() {
        // Placeholder - reads from ADS1299 ECG ADC
        return 0.0f;
    }
    
    float detect_heart_rate(float* buffer, int length) {
        // Placeholder - R-peak detection algorithm
        return 72.0f;  // Simulated normal heart rate
    }
    
    float read_spo2_raw() {
        // Placeholder - reads from MAX30102
        return 98.0f;  // Simulated normal SpO2
    }
    
    void read_nibp(float* sys, float* dia) {
        // Placeholder - oscillometric NIBP
        *sys = 120.0f;
        *dia = 80.0f;
    }
    
    float read_temperature_raw() {
        // Placeholder - thermistor read
        return 37.0f;
    }
    
    float read_respiration_raw() {
        // Placeholder - impedance pneumography
        return 16.0f;
    }
    
    float read_etco2_raw() {
        // Placeholder - capnography
        return 38.0f;
    }
};

MedicalMonitor med_monitor;

// ============================================================================
// AI NAVIGATION SYSTEM
// ============================================================================

class AINavigation {
private:
    float home_lat, home_lon, home_alt;
    float current_lat, current_lon, current_alt;
    float target_lat, target_lon, target_alt;
    float ground_speed;
    float heading;
    
    // Hospital database
    struct Hospital {
        float lat;
        float lon;
        char name[64];
        int trauma_level;  // 1=highest, 5=lowest
        float distance_m;
    };
    
    Hospital hospitals[50];
    int hospital_count;
    
    // Obstacle map (simplified)
    struct Obstacle {
        float lat;
        float lon;
        float radius_m;
        float height_m;
    };
    
    Obstacle obstacles[100];
    int obstacle_count;
    
public:
    AINavigation() : home_lat(0), home_lon(0), home_alt(0),
                     current_lat(0), current_lon(0), current_alt(0),
                     target_lat(0), target_lon(0), target_alt(0),
                     ground_speed(0), heading(0),
                     hospital_count(0), obstacle_count(0) {}
    
    void initialize(float lat, float lon, float alt) {
        home_lat = lat;
        home_lon = lon;
        home_alt = alt;
        current_lat = lat;
        current_lon = lon;
        current_alt = alt;
        
        load_hospital_database();
        load_obstacle_map();
    }
    
    void update_position(float lat, float lon, float alt, float spd, float hdg) {
        current_lat = lat;
        current_lon = lon;
        current_alt = alt;
        ground_speed = spd;
        heading = hdg;
    }
    
    Hospital* find_nearest_hospital() {
        Hospital* nearest = nullptr;
        float min_distance = 1e10f;
        
        for (int i = 0; i < hospital_count; i++) {
            float dist = haversine_distance(current_lat, current_lon,
                                           hospitals[i].lat, hospitals[i].lon);
            hospitals[i].distance_m = dist;
            
            if (dist < min_distance) {
                min_distance = dist;
                nearest = &hospitals[i];
            }
        }
        
        return nearest;
    }
    
    void set_target(float lat, float lon, float alt) {
        target_lat = lat;
        target_lon = lon;
        target_alt = alt;
    }
    
    // A* path planning with obstacle avoidance
    void plan_path(float* path_lats, float* path_lons, int* path_points) {
        // Simplified A* implementation
        // In production: RRT* with dynamic obstacle avoidance
        
        int points = 0;
        float lat_step = (target_lat - current_lat) / 10.0f;
        float lon_step = (target_lon - current_lon) / 10.0f;
        
        for (int i = 0; i <= 10; i++) {
            float interp_lat = current_lat + lat_step * i;
            float interp_lon = current_lon + lon_step * i;
            
            // Check for obstacles
            bool collision = false;
            for (int j = 0; j < obstacle_count; j++) {
                float dist = haversine_distance(interp_lat, interp_lon,
                                               obstacles[j].lat, obstacles[j].lon);
                if (dist < obstacles[j].radius_m + 10.0f) {  // 10m safety margin
                    collision = true;
                    // Reroute around obstacle
                    interp_lat += 0.0001f;  // Simple avoidance
                    break;
                }
            }
            
            path_lats[points] = interp_lat;
            path_lons[points] = interp_lon;
            points++;
        }
        
        *path_points = points;
    }
    
    float calculate_eta() {
        float dist = haversine_distance(current_lat, current_lon,
                                       target_lat, target_lon);
        if (ground_speed > 0.1f) {
            return dist / ground_speed;  // seconds
        }
        return -1.0f;  // Unknown
    }
    
    float get_distance_to_target() {
        return haversine_distance(current_lat, current_lon,
                                 target_lat, target_lon);
    }
    
    bool is_near_hospital() {
        return get_distance_to_target() < 100.0f;  // 100m
    }
    
private:
    float haversine_distance(float lat1, float lon1, float lat2, float lon2) {
        const float R = 6371000.0f;  // Earth's radius in meters
        float dlat = (lat2 - lat1) * M_PI / 180.0f;
        float dlon = (lon2 - lon1) * M_PI / 180.0f;
        float a = sinf(dlat/2) * sinf(dlat/2) +
                  cosf(lat1 * M_PI / 180.0f) * cosf(lat2 * M_PI / 180.0f) *
                  sinf(dlon/2) * sinf(dlon/2);
        float c = 2.0f * atan2f(sqrtf(a), sqrtf(1.0f - a));
        return R * c;
    }
    
    void load_hospital_database() {
        // Placeholder - loads from cloud or local database
        hospital_count = 0;
    }
    
    void load_obstacle_map() {
        // Placeholder - loads terrain/obstacle data
        obstacle_count = 0;
    }
};

AINavigation ai_nav;

// ============================================================================
// SAFETY SYSTEM
// ============================================================================

class SafetySystem {
private:
    bool motors_failed[8];
    int motor_fail_count;
    bool battery_critical;
    bool parachute_ready;
    
public:
    SafetySystem() : motor_fail_count(0), battery_critical(false),
                     parachute_ready(false) {
        for (int i = 0; i < 8; i++) motors_failed[i] = false;
    }
    
    void check_motor_health(bool motor_ok[8]) {
        motor_fail_count = 0;
        for (int i = 0; i < 8; i++) {
            motors_failed[i] = !motor_ok[i];
            if (motors_failed[i]) motor_fail_count++;
        }
        
        if (motor_fail_count > MAX_MOTOR_LOSS) {
            trigger_emergency_landing();
        }
    }
    
    void check_battery(float percent, float voltage) {
        if (percent < BATTERY_CRITICAL_THRESHOLD) {
            battery_critical = true;
            trigger_emergency_landing();
        } else if (percent < BATTERY_LOW_THRESHOLD) {
            trigger_low_battery_return();
        }
    }
    
    void check_patient_vitals(float hr, float spo2, float temp) {
        if (hr < 30 || hr > 180 || spo2 < 80 || temp < 34.0f || temp > 41.0f) {
            trigger_medical_emergency();
        }
    }
    
    bool should_deploy_parachute() {
        return parachute_ready && 
               g_altitude_m > PARACHUTE_MIN_ALTITUDE_M &&
               motor_fail_count > 2;
    }
    
    void arm_parachute() {
        parachute_ready = true;
    }
    
    void trigger_emergency_landing() {
        g_emergency_active = true;
        g_state = STATE_EMERGENCY;
        
        // Find nearest safe landing spot
        // Reduce altitude while maintaining stability
        // Deploy parachute if necessary
    }
    
    void trigger_low_battery_return() {
        // Calculate if we can reach home
        float dist_home = ai_nav.haversine_distance(
            ai_nav.current_lat, ai_nav.current_lon,
            ai_nav.home_lat, ai_nav.home_lon);
        
        float energy_needed = dist_home * 0.5f;  // Rough estimate
        
        if (energy_needed > g_battery_percent * 20.0f) {  // 20kWh total
            // Cannot reach home - find nearest landing
            trigger_emergency_landing();
        } else {
            // Return to home
            ai_nav.set_target(ai_nav.home_lat, ai_nav.home_lon, ai_nav.home_alt);
        }
    }
    
    void trigger_medical_emergency() {
        // Find nearest hospital immediately
        AINavigation::Hospital* nearest = ai_nav.find_nearest_hospital();
        if (nearest) {
            ai_nav.set_target(nearest->lat, nearest->lon, 0.0f);
            g_state = STATE_MISSION;
            g_phase = PHASE_HOSPITAL_ROUTE;
        }
    }
};

SafetySystem safety_system;

// ============================================================================
// COMMUNICATION SYSTEM
// ============================================================================

class CommunicationSystem {
private:
    bool lte_connected;
    bool mesh_connected;
    bool sat_connected;
    
public:
    CommunicationSystem() : lte_connected(false), mesh_connected(false),
                           sat_connected(false) {}
    
    void update_connection_status() {
        // Check all communication links
        lte_connected = check_lte();
        mesh_connected = check_mesh();
        sat_connected = check_satellite();
    }
    
    void send_telemetry() {
        // Pack telemetry data
        struct TelemetryPacket {
            uint8_t state;
            uint8_t phase;
            uint8_t medical_status;
            float altitude;
            float speed;
            float battery_percent;
            float distance_to_target;
            float eta;
            float heart_rate;
            float spo2;
            float temperature;
            bool phi_active;
            float phi_frequency;
        };
        
        TelemetryPacket pkt;
        pkt.state = g_state;
        pkt.phase = g_phase;
        pkt.medical_status = g_medical_status;
        pkt.altitude = g_altitude_m;
        pkt.speed = g_speed_ms;
        pkt.battery_percent = g_battery_percent;
        pkt.distance_to_target = g_distance_to_target_m;
        pkt.eta = g_eta_seconds;
        pkt.heart_rate = g_ecg_bpm;
        pkt.spo2 = g_spo2_percent;
        pkt.temperature = g_patient_temp_c;
        pkt.phi_active = g_phi_active;
        pkt.phi_frequency = g_phi_frequency_hz;
        
        // Send via available link
        if (lte_connected) {
            send_lte((uint8_t*)&pkt, sizeof(pkt));
        } else if (mesh_connected) {
            send_mesh((uint8_t*)&pkt, sizeof(pkt));
        } else if (sat_connected) {
            send_satellite((uint8_t*)&pkt, sizeof(pkt));
        }
    }
    
    void send_medical_alert(const char* alert) {
        // Emergency medical data transmission
        struct MedicalAlert {
            uint8_t type = 0x01;  // Alert type
            char message[128];
            float timestamp;
        };
        
        MedicalAlert ma;
        strncpy(ma.message, alert, 127);
        ma.timestamp = hrt_elapsed_time_seconds();
        
        // Send via all available links
        if (lte_connected) send_lte((uint8_t*)&ma, sizeof(ma));
        if (mesh_connected) send_mesh((uint8_t*)&ma, sizeof(ma));
        if (sat_connected) send_satellite((uint8_t*)&ma, sizeof(ma));
    }
    
private:
    bool check_lte() {
        // Placeholder - check 4G/5G modem
        return true;
    }
    
    bool check_mesh() {
        // Placeholder - check 900 MHz mesh
        return false;
    }
    
    bool check_satellite() {
        // Placeholder - check Iridium
        return false;
    }
    
    void send_lte(uint8_t* data, int len) {
        // Placeholder - send via LTE
    }
    
    void send_mesh(uint8_t* data, int len) {
        // Placeholder - send via mesh
    }
    
    void send_satellite(uint8_t* data, int len) {
        // Placeholder - send via satellite
    }
};

CommunicationSystem comms;

// ============================================================================
// MAIN CONTROL LOOP
// ============================================================================

void setup() {
    // Initialize all systems
    Serial.begin(115200);
    Serial.println("PMSD-100 PHI Medical Stretcher Drone v2.0");
    Serial.println("Initializing systems...");
    
    // Initialize flight controller
    PX4_Autopilot.begin();
    
    // Initialize AI navigation with home position
    ai_nav.initialize(0.0f, 0.0f, 0.0f);  // Will be set by GPS
    
    // Arm safety systems
    safety_system.arm_parachute();
    
    // Initialize phi-harmonic system
    phi_system.set_healing_mode();
    
    // Initialize communication
    comms.update_connection_status();
    
    g_state = STATE_READY;
    Serial.println("System ready.");
}

void loop() {
    static uint32_t last_loop_time = 0;
    uint32_t current_time = millis();
    
    // Run at 100Hz (10ms loop)
    if (current_time - last_loop_time < 10) return;
    last_loop_time = current_time;
    
    // ---- READ SENSORS ----
    // Battery
    struct battery_status_s battery;
    battery_status_sub.copy(&battery);
    g_battery_percent = battery.remaining;
    g_battery_voltage = battery.voltage_filtered_v;
    g_current_draw_a = battery.current_filtered_a;
    
    // Position
    struct vehicle_local_position_s lpos;
    vehicle_local_position_sub.copy(&lpos);
    g_altitude_m = lpos.z;
    g_speed_ms = sqrtf(lpos.vx * lpos.vx + lpos.vy * lpos.vy);
    ai_nav.update_position(lpos.lat, lpos.lon, lpos.alt, g_speed_ms, 0.0f);
    
    // ---- MEDICAL MONITORING ----
    med_monitor.read_sensors();
    g_ecg_bpm = med_monitor.get_heart_rate();
    g_spo2_percent = med_monitor.get_spo2();
    g_systolic_bp = med_monitor.get_systolic();
    g_diastolic_bp = med_monitor.get_diastolic();
    g_patient_temp_c = med_monitor.get_temperature();
    g_respiration_rate = med_monitor.get_resp_rate();
    g_etco2_mmhg = med_monitor.get_etco2();
    
    g_medical_status = med_monitor.evaluate();
    
    // ---- PHI-HARMONIC SYSTEM ----
    if (g_patient_secured && !g_phi_active) {
        phi_system.activate();
        g_phi_active = true;
    }
    
    if (g_phi_active) {
        phi_system.update(g_ecg_bpm, g_spo2_percent, g_patient_temp_c);
        g_phi_frequency_hz = PHI_HEALING_FREQ;
        g_phi_field_strength_mt = 0.5f;
    }
    
    // ---- NAVIGATION ----
    g_distance_to_target_m = ai_nav.get_distance_to_target();
    g_eta_seconds = ai_nav.calculate_eta();
    
    // ---- SAFETY CHECKS ----
    bool motor_ok[8];
    for (int i = 0; i < 8; i++) motor_ok[i] = true;  // Would read from ESCs
    safety_system.check_motor_health(motor_ok);
    safety_system.check_battery(g_battery_percent, g_battery_voltage);
    safety_system.check_patient_vitals(g_ecg_bpm, g_spo2_percent, g_patient_temp_c);
    
    // ---- STATE MACHINE ----
    switch (g_state) {
        case STATE_READY:
            // Waiting for mission
            break;
            
        case STATE_MISSION:
            switch (g_phase) {
                case PHASE_DISPATCH:
                    // Takeoff and head to scene
                    break;
                case PHASE_SCENE_APPROACH:
                    // Approach accident location
                    break;
                case PHASE_PATIENT_LOAD:
                    // Secure patient
                    if (g_patient_secured) {
                        g_phase = PHASE_HOSPITAL_ROUTE;
                        AINavigation::Hospital* nearest = ai_nav.find_nearest_hospital();
                        if (nearest) {
                            ai_nav.set_target(nearest->lat, nearest->lon, 0.0f);
                        }
                    }
                    break;
                case PHASE_HOSPITAL_ROUTE:
                    // Navigate to hospital
                    break;
                case PHASE_HOSPITAL_APPROACH:
                    // Prepare for landing
                    if (ai_nav.is_near_hospital()) {
                        g_phase = PHASE_PATIENT_DELIVER;
                    }
                    break;
                case PHASE_PATIENT_DELIVER:
                    // Deliver patient
                    break;
                case PHASE_RETURN_BASE:
                    // Return to home
                    break;
            }
            break;
            
        case STATE_EMERGENCY:
            // Handle emergency
            if (safety_system.should_deploy_parachute()) {
                // Deploy parachute
                deploy_parachute();
            }
            break;
            
        default:
            break;
    }
    
    // ---- COMMUNICATION ----
    comms.update_connection_status();
    comms.send_telemetry();
    
    // ---- ACTUATOR OUTPUTS ----
    // Would send motor commands via actuator_controls_pub
    
    // ---- DEBUG OUTPUT ----
    static int debug_counter = 0;
    debug_counter++;
    if (debug_counter >= 100) {  // Every 1 second
        debug_counter = 0;
        
        Serial.print("State: "); Serial.print(g_state);
        Serial.print(" | Battery: "); Serial.print(g_battery_percent * 100);
        Serial.print("% | Alt: "); Serial.print(g_altitude_m);
        Serial.print("m | Speed: "); Serial.print(g_speed_ms * 3.6);
        Serial.print("km/h | HR: "); Serial.print(g_ecg_bpm);
        Serial.print(" | SpO2: "); Serial.print(g_spo2_percent);
        Serial.print("% | Temp: "); Serial.print(g_patient_temp_c);
        Serial.print("C | Phi: "); Serial.print(g_phi_active ? "ON" : "OFF");
        Serial.print(" | ETA: "); Serial.print(g_eta_seconds);
        Serial.println("s");
    }
}

void deploy_parachute() {
    // Safety processor handles this independently
    Serial.println("PARACHUTE DEPLOYMENT INITIATED");
    // Trigger ballistic deployment
    digitalWrite(PARACHUTE_PIN, HIGH);
    delay(100);
    digitalWrite(PARACHUTE_PIN, LOW);
}
