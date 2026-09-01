"""
PHI Pharmacy Drone - Safety System
Model: PPHD-300, Version: 1.0
Controlled substance security, temperature safety, delivery verification
"""
import time
from dataclasses import dataclass
from typing import List
from enum import Enum


class SafetyEvent(Enum):
    TEMP_OUT_OF_RANGE = "temp_out_of_range"
    TAMPER_DETECTED = "tamper_detected"
    MOTOR_FAULT = "motor_fault"
    BATTERY_LOW = "battery_low"
    BARCODE_MISMATCH = "barcode_mismatch"
    CONTROLLED_SUBSTANCE = "controlled_substance"


@dataclass
class SafetyConfig:
    temp_min_c: float = 2.0
    temp_max_c: float = 8.0
    battery_low_pct: float = 0.15
    max_flight_time_min: float = 120


class PharmacySafetySystem:
    def __init__(self):
        self.config = SafetyConfig()
        self.events: List[str] = []
        self.tamper_detected = False
        self.emergency_active = False

    def check_temperature(self, temp_c: float, zone: str) -> bool:
        if zone == "refrigerated":
            if temp_c < self.config.temp_min_c or temp_c > self.config.temp_max_c:
                self._trigger(SafetyEvent.TEMP_OUT_OF_RANGE,
                             f"{zone}: {temp_c:.1f}C")
                return False
        return True

    def check_tamper(self, slot_id: int, seal_intact: bool) -> bool:
        if not seal_intact:
            self._trigger(SafetyEvent.TAMPER_DETECTED, f"Slot {slot_id}")
            self.tamper_detected = True
            return False
        return True

    def check_barcode(self, slot_id: int, expected: str, scanned: str) -> bool:
        if expected != scanned:
            self._trigger(SafetyEvent.BARCODE_MISMATCH,
                         f"Slot {slot_id}: expected {expected}, got {scanned}")
            return False
        return True

    def check_battery(self, percent: float) -> bool:
        if percent < self.config.battery_low_pct:
            self._trigger(SafetyEvent.BATTERY_LOW, f"{percent*100:.1f}%")
            return False
        return True

    def emergency_return(self):
        self.emergency_active = True
        self.events.append(f"EMERGENCY RETURN at {time.strftime('%H:%M:%S')}")

    def _trigger(self, event: SafetyEvent, detail: str):
        self.events.append(f"[{event.value}] {detail}")

    def get_status(self) -> dict:
        return {
            "tamper_detected": self.tamper_detected,
            "emergency": self.emergency_active,
            "events": len(self.events),
        }


if __name__ == "__main__":
    print("PHI Pharmacy Drone - Safety System")
    print("=" * 45)
    ss = PharmacySafetySystem()
    print(f"Temp 5C: {ss.check_temperature(5.0, 'refrigerated')}")
    print(f"Temp 10C: {ss.check_temperature(10.0, 'refrigerated')}")
    print(f"Status: {ss.get_status()}")
