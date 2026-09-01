"""
PHI Medical Stretcher Drone - Safety System
Model: PMSD-100, Version: 2.0
Redundant safety with motor loss tolerance, parachute, and emergency protocols
"""
import time
from dataclasses import dataclass, field
from typing import List, Callable, Optional
from enum import Enum


class SafetyEvent(Enum):
    MOTOR_FAIL = "motor_fail"
    BATTERY_LOW = "battery_low"
    BATTERY_CRITICAL = "battery_critical"
    COMM_LOST = "comm_lost"
    MEDICAL_EMERGENCY = "medical_emergency"
    STRUCTURAL_FAULT = "structural_fault"
    GPS_LOST = "gps_lost"
    WEATHER_OVERRIDE = "weather_override"


class EmergencyAction(Enum):
    NONE = 0
    REDISTRIBUTE_THRUST = 1
    RETURN_HOME = 2
    EMERGENCY_LAND = 3
    DEPLOY_PARACHUTE = 4
    DIVERT_HOSPITAL = 5


@dataclass
class SafetyConfig:
    max_motor_loss: int = 2
    battery_low_pct: float = 0.20
    battery_critical_pct: float = 0.10
    parachute_min_alt_m: float = 30.0
    max_negative_g: float = -0.5
    max_vibration_g: float = 0.5
    max_noise_db: float = 65.0
    comm_timeout_s: float = 10.0


@dataclass
class MotorStatus:
    index: int
    rpm: int = 0
    temperature_c: float = 25.0
    current_a: float = 0.0
    healthy: bool = True


@dataclass
class SafetyState:
    motors_failed: int = 0
    battery_percent: float = 1.0
    battery_voltage: float = 51.2
    altitude_m: float = 0.0
    speed_ms: float = 0.0
    comm_ok: bool = True
    gps_ok: bool = True
    last_comm_time: float = 0.0
    emergency_active: bool = False
    parachute_armed: bool = False
    parachute_deployed: bool = False
    event_log: List[str] = field(default_factory=list)


class SafetySystem:
    def __init__(self, config: SafetyConfig = None):
        self.config = config or SafetyConfig()
        self.state = SafetyState()
        self.motors = [MotorStatus(i) for i in range(8)]
        self.callbacks: dict = {}
        self.patient_hr = 72.0
        self.patient_spo2 = 98.0
        self.patient_temp = 37.0

    def register_callback(self, event: SafetyEvent, callback: Callable):
        self.callbacks[event] = callback

    def update_motor(self, index: int, rpm: int, temp: float, current: float):
        m = self.motors[index]
        m.rpm = rpm
        m.temperature_c = temp
        m.current_a = current
        m.healthy = rpm > 1000 and temp < 120 and current < 30

    def check_motors(self) -> EmergencyAction:
        self.state.motors_failed = sum(1 for m in self.motors if not m.healthy)
        if self.state.motors_failed > self.config.max_motor_loss:
            self._trigger(SafetyEvent.MOTOR_FAIL, f"{self.state.motors_failed} motors failed")
            if self.state.altitude_m > self.config.parachute_min_alt_m:
                return EmergencyAction.DEPLOY_PARACHUTE
            return EmergencyAction.EMERGENCY_LAND
        if self.state.motors_failed > 0:
            return EmergencyAction.REDISTRIBUTE_THRUST
        return EmergencyAction.NONE

    def check_battery(self, percent: float, voltage: float) -> EmergencyAction:
        self.state.battery_percent = percent
        self.state.battery_voltage = voltage
        if percent < self.config.battery_critical_pct:
            self._trigger(SafetyEvent.BATTERY_CRITICAL, f"Battery {percent*100:.1f}%")
            return EmergencyAction.EMERGENCY_LAND
        if percent < self.config.battery_low_pct:
            self._trigger(SafetyEvent.BATTERY_LOW, f"Battery {percent*100:.1f}%")
            return EmergencyAction.RETURN_HOME
        return EmergencyAction.NONE

    def check_comm(self) -> EmergencyAction:
        if not self.state.comm_ok:
            elapsed = time.time() - self.state.last_comm_time
            if elapsed > self.config.comm_timeout_s:
                self._trigger(SafetyEvent.COMM_LOST, f"No comm for {elapsed:.0f}s")
                return EmergencyAction.RETURN_HOME
        return EmergencyAction.NONE

    def check_patient(self, hr: float, spo2: float, temp: float) -> EmergencyAction:
        self.patient_hr = hr
        self.patient_spo2 = spo2
        self.patient_temp = temp
        if hr < 30 or hr > 180 or spo2 < 80 or temp < 34 or temp > 41:
            self._trigger(SafetyEvent.MEDICAL_EMERGENCY,
                         f"HR={hr:.0f} SpO2={spo2:.0f} T={temp:.1f}")
            return EmergencyAction.DIVERT_HOSPITAL
        return EmergencyAction.NONE

    def should_deploy_parachute(self) -> bool:
        return (self.state.parachute_armed and
                not self.state.parachute_deployed and
                self.state.altitude_m > self.config.parachute_min_alt_m and
                self.state.motors_failed > 2)

    def deploy_parachute(self):
        self.state.parachute_deployed = True
        self.state.event_log.append(f"PARACHUTE DEPLOYED at {self.state.altitude_m:.1f}m")

    def arm_parachute(self):
        self.state.parachute_armed = True

    def full_check(self) -> EmergencyAction:
        actions = [
            self.check_motors(),
            self.check_battery(self.state.battery_percent, self.state.battery_voltage),
            self.check_comm(),
            self.check_patient(self.patient_hr, self.patient_spo2, self.patient_temp),
        ]
        for a in actions:
            if a.value > EmergencyAction.NONE.value:
                return a
        return EmergencyAction.NONE

    def _trigger(self, event: SafetyEvent, detail: str):
        ts = time.strftime("%H:%M:%S")
        self.state.event_log.append(f"[{ts}] {event.value}: {detail}")
        self.state.emergency_active = True
        if event in self.callbacks:
            self.callbacks[event](detail)

    def get_status(self) -> dict:
        return {
            "motors_ok": 8 - self.state.motors_failed,
            "motors_failed": self.state.motors_failed,
            "battery_pct": self.state.battery_percent,
            "emergency": self.state.emergency_active,
            "parachute_armed": self.state.parachute_armed,
            "parachute_deployed": self.state.parachute_deployed,
            "events": len(self.state.event_log),
        }


if __name__ == "__main__":
    print("PHI Medical Stretcher Drone - Safety System")
    print("=" * 50)
    ss = SafetySystem()
    ss.arm_parachute()
    for i in range(8):
        ss.update_motor(i, 5000, 60, 15)
    action = ss.full_check()
    print(f"Full check: {action.name}")
    print(f"Status: {ss.get_status()}")
