"""
PHI Surgical Assist Drone - Safety System
Model: PSAD-200, Version: 1.0
Medical device safety with IEC 60601-1 compliance
"""
import time
from dataclasses import dataclass
from typing import List
from enum import Enum


class SafetyEvent(Enum):
    MOTOR_FAULT = "motor_fault"
    ARM_FORCE_EXCEEDED = "arm_force_exceeded"
    COLLISION_DETECTED = "collision_detected"
    STERILE_BREACH = "sterile_breach"
    BATTERY_LOW = "battery_low"
    COMM_LOST = "comm_lost"
    EMERGENCY_STOP = "emergency_stop"


@dataclass
class SafetyConfig:
    max_force_n: float = 50.0
    max_arm_speed_ms: float = 0.5
    collision_distance_m: float = 0.05
    battery_low_pct: float = 0.15
    comm_timeout_s: float = 5.0


class SafetySystem:
    def __init__(self):
        self.config = SafetyConfig()
        self.events: List[str] = []
        self.arm_brake_engaged = True
        self.emergency_active = False
        self.force_limit_active = True

    def check_force(self, force_magnitude: float) -> bool:
        if force_magnitude > self.config.max_force_n:
            self._trigger(SafetyEvent.ARM_FORCE_EXCEEDED, f"{force_magnitude:.1f}N")
            self.engage_brake()
            return False
        return True

    def check_collision(self, distance_m: float) -> bool:
        if distance_m < self.config.collision_distance_m:
            self._trigger(SafetyEvent.COLLISION_DETECTED, f"{distance_m:.3f}m")
            self.engage_brake()
            return False
        return True

    def check_sterile(self, particle_count: int) -> bool:
        if particle_count > 100:
            self._trigger(SafetyEvent.STERILE_BREACH, f"{particle_count} particles")
            return False
        return True

    def engage_brake(self):
        self.arm_brake_engaged = True
        self.events.append(f"BRAKE ENGAGED at {time.strftime('%H:%M:%S')}")

    def release_brake(self):
        self.arm_brake_engaged = False

    def emergency_stop(self):
        self.emergency_active = True
        self.engage_brake()
        self.events.append(f"EMERGENCY STOP at {time.strftime('%H:%M:%S')}")

    def _trigger(self, event: SafetyEvent, detail: str):
        self.events.append(f"[{event.value}] {detail}")

    def get_status(self) -> dict:
        return {
            "brake": "engaged" if self.arm_brake_engaged else "released",
            "emergency": self.emergency_active,
            "events": len(self.events),
        }


if __name__ == "__main__":
    print("PHI Surgical Assist Drone - Safety System")
    print("=" * 50)
    ss = SafetySystem()
    ss.release_brake()
    ok = ss.check_force(25.0)
    print(f"Force check (25N): {'OK' if ok else 'BRAKE'}")
    ok = ss.check_force(60.0)
    print(f"Force check (60N): {'OK' if ok else 'BRAKE'}")
    print(f"Status: {ss.get_status()}")
