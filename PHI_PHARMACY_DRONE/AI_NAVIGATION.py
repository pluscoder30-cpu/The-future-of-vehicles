"""
PHI Pharmacy Drone - AI Navigation System
Model: PPHD-300, Version: 1.0
Route optimization, weather-aware delivery, last-meter navigation
"""
import numpy as np
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class DeliveryMode(Enum):
    IDLE = 0
    DISPATCHED = 1
    EN_ROUTE = 2
    APPROACHING = 3
    DELIVERING = 4
    RETURNING = 5


@dataclass
class DeliveryOrder:
    order_id: str
    patient_name: str
    address: str
    lat: float
    lon: float
    medications: List[str]
    priority: int  # 1=urgent, 2=same-day, 3=standard
    temperature_sensitive: bool
    requires_signature: bool


@dataclass
class WeatherCondition:
    wind_speed_ms: float
    visibility_m: float
    precipitation: str
    temperature_c: float


class PharmacyNavigation:
    def __init__(self):
        self.mode = DeliveryMode.IDLE
        self.current_lat = 0.0
        self.current_lon = 0.0
        self.target_lat = 0.0
        self.target_lon = 0.0
        self.orders: List[DeliveryOrder] = []
        self.weather = WeatherCondition(0, 10000, "none", 20)

    def plan_route(self, orders: List[DeliveryOrder]) -> List[DeliveryOrder]:
        """Optimize delivery route using nearest-neighbor heuristic."""
        if not orders:
            return []
        
        # Sort by priority first, then distance
        self.orders = sorted(orders, key=lambda o: (o.priority, self._distance(o)))
        return self.orders

    def dispatch(self, order: DeliveryOrder):
        self.mode = DeliveryMode.DISPATCHED
        self.target_lat = order.lat
        self.target_lon = order.lon

    def update_position(self, lat: float, lon: float):
        self.current_lat = lat
        self.current_lon = lon

    def check_arrival(self) -> bool:
        dist = self._distance_to_target()
        return dist < 50.0  # 50m arrival threshold

    def adapt_to_weather(self, weather: WeatherCondition):
        self.weather = weather
        if weather.wind_speed_ms > 12:
            # Reduce speed, consider delaying
            pass

    def _distance(self, order: DeliveryOrder) -> float:
        R = 6371000
        dlat = np.radians(order.lat - self.current_lat)
        dlon = np.radians(order.lon - self.current_lon)
        a = np.sin(dlat/2)**2 + np.cos(np.radians(self.current_lat)) * np.cos(np.radians(order.lat)) * np.sin(dlon/2)**2
        return R * 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))

    def _distance_to_target(self) -> float:
        R = 6371000
        dlat = np.radians(self.target_lat - self.current_lat)
        dlon = np.radians(self.target_lon - self.current_lon)
        a = np.sin(dlat/2)**2 + np.cos(np.radians(self.current_lat)) * np.cos(np.radians(self.target_lat)) * np.sin(dlon/2)**2
        return R * 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))

    def get_eta_seconds(self, speed_ms: float = 16.7) -> float:
        dist = self._distance_to_target()
        return dist / speed_ms if speed_ms > 0 else -1


if __name__ == "__main__":
    print("PHI Pharmacy Drone - AI Navigation System")
    print("=" * 50)
    nav = PharmacyNavigation()
    order = DeliveryOrder("ORD-001", "John Doe", "123 Main St", 40.7128, -74.006,
                         ["Ibuprofen 200mg"], 2, False, False)
    nav.dispatch(order)
    nav.update_position(40.7100, -74.0040)
    print(f"Distance: {nav._distance_to_target():.0f}m")
    print(f"ETA: {nav.get_eta_seconds():.0f}s")
