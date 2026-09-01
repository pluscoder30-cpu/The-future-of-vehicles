"""
PHI Pharmacy Drone - Medication Monitoring System
Model: PPHD-300, Version: 1.0
Inventory tracking, temperature logging, dosage verification
"""
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class MedicationStatus(Enum):
    LOADED = "loaded"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    RETURNED = "returned"
    EXPIRED = "expired"


@dataclass
class MedicationRecord:
    slot_id: int
    name: str
    barcode: str
    rfid_tag: str
    dosage: str
    quantity: int
    expiry_date: str
    temperature_log: List[float] = field(default_factory=list)
    status: MedicationStatus = MedicationStatus.LOADED
    load_time: float = field(default_factory=time.time)
    delivery_time: Optional[float] = None


class PharmacyMonitor:
    def __init__(self):
        self.inventory: Dict[int, MedicationRecord] = {}
        self.delivery_log: List[dict] = []
        self.temperature_alerts: List[str] = []

    def load_medication(self, slot: int, name: str, barcode: str, rfid: str,
                       dosage: str, qty: int, expiry: str) -> bool:
        if slot in self.inventory:
            return False
        self.inventory[slot] = MedicationRecord(
            slot, name, barcode, rfid, dosage, qty, expiry
        )
        return True

    def update_temperature(self, slot: int, temp_c: float):
        if slot in self.inventory:
            self.inventory[slot].temperature_log.append(temp_c)
            # Check range
            if temp_c < 2.0 or temp_c > 8.0:
                self.temperature_alerts.append(
                    f"Slot {slot}: {temp_c:.1f}C out of range"
                )

    def verify_barcode(self, slot: int, scanned_barcode: str) -> bool:
        if slot in self.inventory:
            return self.inventory[slot].barcode == scanned_barcode
        return False

    def mark_delivered(self, slot: int):
        if slot in self.inventory:
            self.inventory[slot].status = MedicationStatus.DELIVERED
            self.inventory[slot].delivery_time = time.time()

    def get_inventory_summary(self) -> dict:
        loaded = sum(1 for m in self.inventory.values() if m.status == MedicationStatus.LOADED)
        delivered = sum(1 for m in self.inventory.values() if m.status == MedicationStatus.DELIVERED)
        return {
            "total_slots": len(self.inventory),
            "loaded": loaded,
            "delivered": delivered,
            "temperature_alerts": len(self.temperature_alerts),
        }


if __name__ == "__main__":
    print("PHI Pharmacy Drone - Medication Monitor")
    print("=" * 45)
    mon = PharmacyMonitor()
    mon.load_medication(0, "Ibuprofen", "123456", "RF001", "200mg", 30, "2027-12-31")
    mon.load_medication(1, "Amoxicillin", "789012", "RF002", "500mg", 21, "2027-06-30")
    print(f"Inventory: {mon.get_inventory_summary()}")
    mon.update_temperature(0, 5.0)
    mon.update_temperature(1, 12.0)
    print(f"Temperature alerts: {mon.temperature_alerts}")
