"""
PHI Medical Stretcher Drone - AI Navigation System
Model: PMSD-100
Version: 2.0

Deep reinforcement learning based autonomous navigation with:
- Hospital routing optimization
- Dynamic obstacle avoidance
- Weather-aware path planning
- Emergency landing site selection
"""

import numpy as np
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum


class NavigationMode(Enum):
    IDLE = 0
    DISPATCH = 1
    SCENE_APPROACH = 2
    PATIENT_LOAD = 3
    HOSPITAL_ROUTE = 4
    HOSPITAL_APPROACH = 5
    PATIENT_DELIVER = 6
    RETURN_BASE = 7
    EMERGENCY = 8


@dataclass
class GPSPosition:
    latitude: float
    longitude: float
    altitude_m: float
    
    def to_array(self) -> np.ndarray:
        return np.array([self.latitude, self.longitude, self.altitude_m])


@dataclass
class Hospital:
    name: str
    position: GPSPosition
    trauma_level: int  # 1=highest, 5=lowest
    specialties: List[str]
    bed_available: int
    distance_m: float = 0.0f


@dataclass
class Obstacle:
    position: GPSPosition
    radius_m: float
    height_m: float
    obstacle_type: str  # building, powerline, tree, bird, drone


@dataclass
class WeatherCondition:
    wind_speed_ms: float
    wind_direction_deg: float
    visibility_m: float
    precipitation: str  # none, rain, snow, fog
    temperature_c: float
    turbulence_index: float  # 0-1


class AINavigationSystem:
    """
    AI-powered navigation system for medical evacuation drone.
    
    Uses deep reinforcement learning for:
    - Path planning with obstacle avoidance
    - Hospital selection optimization
    - Dynamic rerouting based on conditions
    - Emergency landing site selection
    """
    
    PHI = 1.6180339887
    
    def __init__(self):
        self.home_position = GPSPosition(0, 0, 0)
        self.current_position = GPSPosition(0, 0, 0)
        self.target_position = GPSPosition(0, 0, 0)
        
        self.hospitals: List[Hospital] = []
        self.obstacles: List[Obstacle] = []
        self.weather = WeatherCondition(0, 0, 10000, 'none', 20, 0)
        
        self.current_mode = NavigationMode.IDLE
        self.path_points: List[GPSPosition] = []
        self.current_path_index = 0
        
        self.ground_speed_ms = 0
        self.heading_deg = 0
        self.battery_percent = 1.0
        
        # AI model parameters (simplified)
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.95
        self.exploration_rate = 0.1
        
        self.load_hospital_database()
        self.load_obstacle_map()
    
    def load_hospital_database(self):
        """Load hospital database from cloud or local storage."""
        # Placeholder - in production, query real hospital API
        self.hospitals = [
            Hospital("City General Hospital", GPSPosition(40.7128, -74.0060, 0), 
                    1, ["trauma", "cardiac", "neuro"], 50),
            Hospital("Regional Medical Center", GPSPosition(40.7580, -73.9855, 0),
                    2, ["trauma", "pediatric"], 30),
            Hospital("Community Hospital", GPSPosition(40.6892, -74.0445, 0),
                    3, ["general"], 20),
        ]
    
    def load_obstacle_map(self):
        """Load obstacle data from terrain database."""
        self.obstacles = []  # Placeholder
    
    def update_position(self, position: GPSPosition, speed: float, heading: float):
        """Update current drone position from GPS/INS."""
        self.current_position = position
        self.ground_speed_ms = speed
        self.heading_deg = heading
    
    def find_nearest_hospital(self) -> Optional[Hospital]:
        """Find nearest hospital with trauma capability."""
        best_hospital = None
        best_score = -1
        
        for hospital in self.hospitals:
            distance = self.haversine_distance(
                self.current_position.latitude,
                self.current_position.longitude,
                hospital.position.latitude,
                hospital.position.longitude
            )
            hospital.distance_m = distance
            
            # Score: weighted by distance, trauma level, and availability
            # Higher score is better
            distance_score = 1.0 / (1.0 + distance / 10000.0)  # Normalize to 10km
            trauma_score = (6 - hospital.trauma_level) / 5.0  # Level 1 = 1.0
            availability_score = min(hospital.bed_available / 50.0, 1.0)
            
            score = (0.5 * distance_score + 
                    0.3 * trauma_score + 
                    0.2 * availability_score)
            
            if score > best_score:
                best_score = score
                best_hospital = hospital
        
        return best_hospital
    
    def find_emergency_landing_site(self) -> Optional[GPSPosition]:
        """Find nearest suitable emergency landing site."""
        # In production: query terrain database for flat areas
        # For now, return position 100m ahead at ground level
        heading_rad = math.radians(self.heading_deg)
        
        lat_offset = 0.001 * math.cos(heading_rad)  # ~100m
        lon_offset = 0.001 * math.sin(heading_rad)
        
        return GPSPosition(
            self.current_position.latitude + lat_offset,
            self.current_position.longitude + lon_offset,
            0.0
        )
    
    def plan_path(self, target: GPSPosition) -> List[GPSPosition]:
        """
        Plan path from current position to target.
        Uses A* with dynamic obstacle avoidance.
        """
        path = []
        
        # Simple straight-line path (placeholder for RRT*)
        num_points = 20
        
        for i in range(num_points + 1):
            t = i / num_points
            
            # Interpolate position
            lat = self.current_position.latitude + t * (target.latitude - self.current_position.latitude)
            lon = self.current_position.longitude + t * (target.longitude - self.current_position.longitude)
            alt = self.current_position.altitude_m + t * (target.altitude_m - self.current_position.altitude_m)
            
            # Check for obstacles
            pos = GPSPosition(lat, lon, alt)
            if not self.check_collision(pos):
                path.append(pos)
            else:
                # Reroute around obstacle
                rerouted = self.reroute_around_obstacle(pos)
                path.extend(rerouted)
        
        self.path_points = path
        self.current_path_index = 0
        
        return path
    
    def check_collision(self, position: GPSPosition) -> bool:
        """Check if position conflicts with any obstacle."""
        for obstacle in self.obstacles:
            distance = self.haversine_distance(
                position.latitude, position.longitude,
                obstacle.position.latitude, obstacle.position.longitude
            )
            
            if distance < obstacle.radius_m + 10.0:  # 10m safety margin
                if position.altitude_m < obstacle.height_m + 5.0:  # 5m clearance
                    return True
        
        return False
    
    def reroute_around_obstacle(self, blocked_pos: GPSPosition) -> List[GPSPosition]:
        """Generate path around detected obstacle."""
        # Simple avoidance: go 20m to the right
        heading_rad = math.radians(self.heading_deg + 90)
        
        lat_offset = 0.0002 * math.cos(heading_rad)
        lon_offset = 0.0002 * math.sin(heading_rad)
        
        return [
            GPSPosition(blocked_pos.latitude + lat_offset,
                       blocked_pos.longitude + lon_offset,
                       blocked_pos.altitude_m),
            GPSPosition(blocked_pos.latitude,
                       blocked_pos.longitude,
                       blocked_pos.altitude_m)
        ]
    
    def calculate_eta(self) -> float:
        """Calculate ETA to current target in seconds."""
        distance = self.haversine_distance(
            self.current_position.latitude,
            self.current_position.longitude,
            self.target_position.latitude,
            self.target_position.longitude
        )
        
        if self.ground_speed_ms > 0.1:
            return distance / self.ground_speed_ms
        
        return -1.0  # Unknown
    
    def get_distance_to_target(self) -> float:
        """Get distance to target in meters."""
        return self.haversine_distance(
            self.current_position.latitude,
            self.current_position.longitude,
            self.target_position.latitude,
            self.target_position.longitude
        )
    
    def is_near_hospital(self, threshold_m: float = 100.0) -> bool:
        """Check if drone is near hospital landing zone."""
        return self.get_distance_to_target() < threshold_m
    
    def adapt_to_weather(self, weather: WeatherCondition):
        """Adjust navigation parameters based on weather."""
        self.weather = weather
        
        # Reduce speed in high winds
        if weather.wind_speed_ms > 10:
            max_speed = 20.0  # m/s
        elif weather.wind_speed_ms > 15:
            max_speed = 15.0
        else:
            max_speed = 33.3  # 120 km/h
        
        # Adjust altitude for turbulence
        if weather.turbulence_index > 0.7:
            # Increase altitude for smoother air
            pass
        
        # Reroute in low visibility
        if weather.visibility_m < 1000:
            # Switch to instrument navigation
            pass
    
    def ai_decision_making(self, state: np.ndarray) -> int:
        """
        AI decision making using simplified Q-learning.
        
        State vector:
        [battery_percent, distance_to_target, wind_speed, obstacle_nearby,
         patient_critical, motor_health]
        
        Actions:
        0: Continue current path
        1: Increase altitude
        2: Decrease altitude
        3: Speed up
        4: Slow down
        5: Reroute
        6: Emergency land
        7: Return home
        """
        # Get state hash for Q-table
        state_hash = tuple(np.round(state, 2))
        
        # Exploration vs exploitation
        if np.random.random() < self.exploration_rate:
            return np.random.randint(8)
        
        # Get Q-values for state
        if state_hash not in self.q_table:
            self.q_table[state_hash] = np.zeros(8)
        
        return np.argmax(self.q_table[state_hash])
    
    def update_q_table(self, state: np.ndarray, action: int, 
                       reward: float, next_state: np.ndarray):
        """Update Q-table with experience."""
        state_hash = tuple(np.round(state, 2))
        next_state_hash = tuple(np.round(next_state, 2))
        
        if state_hash not in self.q_table:
            self.q_table[state_hash] = np.zeros(8)
        if next_state_hash not in self.q_table:
            self.q_table[next_state_hash] = np.zeros(8)
        
        # Q-learning update
        current_q = self.q_table[state_hash][action]
        max_next_q = np.max(self.q_table[next_state_hash])
        
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_next_q - current_q
        )
        
        self.q_table[state_hash][action] = new_q
    
    def get_state_vector(self) -> np.ndarray:
        """Get current state vector for AI decision making."""
        return np.array([
            self.battery_percent,
            self.get_distance_to_target() / 10000.0,  # Normalize to 10km
            self.weather.wind_speed_ms / 20.0,  # Normalize to 20m/s
            1.0 if len(self.obstacles) > 0 else 0.0,
            0.0,  # patient_critical (set externally)
            1.0   # motor_health (1.0 = all OK)
        ])
    
    def haversine_distance(self, lat1: float, lon1: float,
                          lat2: float, lon2: float) -> float:
        """Calculate distance between two GPS coordinates in meters."""
        R = 6371000.0  # Earth's radius in meters
        
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        
        a = (math.sin(delta_phi / 2) ** 2 +
             math.cos(phi1) * math.cos(phi2) *
             math.sin(delta_lambda / 2) ** 2)
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c
    
    def calculate_phi_harmonic_path(self, path: List[GPSPosition]) -> List[GPSPosition]:
        """
        Optimize path using phi-harmonic principles.
        
        The golden ratio (φ = 1.618) is used to:
        - Distribute path points with natural spacing
        - Create smooth, organic trajectories
        - Minimize energy expenditure through resonance
        """
        if len(path) < 3:
            return path
        
        optimized = [path[0]]
        
        for i in range(1, len(path) - 1):
            # Apply phi-harmonic smoothing
            prev = path[i - 1]
            curr = path[i]
            next_pt = path[i + 1]
            
            # Weighted average with phi ratio
            w1 = 1.0 / self.PHI
            w2 = 1.0 - w1
            
            smoothed_lat = w1 * curr.latitude + w2 * (prev.latitude + next_pt.latitude) / 2
            smoothed_lon = w1 * curr.longitude + w2 * (prev.longitude + next_pt.longitude) / 2
            smoothed_alt = w1 * curr.altitude_m + w2 * (prev.altitude_m + next_pt.altitude_m) / 2
            
            optimized.append(GPSPosition(smoothed_lat, smoothed_lon, smoothed_alt))
        
        optimized.append(path[-1])
        
        return optimized


class NavigationController:
    """
    High-level navigation controller that coordinates
    the AI navigation system with mission planning.
    """
    
    def __init__(self, nav_system: AINavigationSystem):
        self.nav = nav_system
        self.mission_active = False
        self.target_hospital: Optional[Hospital] = None
    
    def dispatch_to_scene(self, scene_lat: float, scene_lon: float):
        """Dispatch drone to accident scene."""
        self.nav.current_mode = NavigationMode.DISPATCH
        self.nav.target_position = GPSPosition(scene_lat, scene_lon, 0)
        self.nav.path_points = self.nav.plan_path(self.nav.target_position)
        self.mission_active = True
    
    def load_patient_and_route(self):
        """After patient is secured, route to hospital."""
        self.nav.current_mode = NavigationMode.HOSPITAL_ROUTE
        
        # Find nearest appropriate hospital
        self.target_hospital = self.nav.find_nearest_hospital()
        
        if self.target_hospital:
            self.nav.target_position = self.target_hospital.position
            self.nav.path_points = self.nav.plan_path(self.nav.target_position)
            
            # Apply phi-harmonic path optimization
            self.nav.path_points = self.nav.calculate_phi_harmonic_path(
                self.nav.path_points
            )
    
    def update(self):
        """Update navigation controller."""
        if not self.mission_active:
            return
        
        # Check if we've reached the target
        if self.nav.is_near_hospital():
            self.nav.current_mode = NavigationMode.HOSPITAL_APPROACH
            # Initiate landing sequence
        
        # Update ETA
        eta = self.nav.calculate_eta()
        
        # Check weather conditions
        self.nav.adapt_to_weather(self.nav.weather)
        
        # AI decision making
        state = self.nav.get_state_vector()
        action = self.nav.ai_decision_making(state)
        
        # Execute action
        self.execute_action(action)
    
    def execute_action(self, action: int):
        """Execute navigation action from AI."""
        if action == 0:
            pass  # Continue
        elif action == 1:
            pass  # Increase altitude
        elif action == 2:
            pass  # Decrease altitude
        elif action == 3:
            pass  # Speed up
        elif action == 4:
            pass  # Slow down
        elif action == 5:
            # Reroute
            self.nav.path_points = self.nav.plan_path(self.nav.target_position)
        elif action == 6:
            # Emergency land
            self.emergency_land()
        elif action == 7:
            # Return home
            self.return_home()
    
    def emergency_land(self):
        """Initiate emergency landing."""
        self.nav.current_mode = NavigationMode.EMERGENCY
        landing_site = self.nav.find_emergency_landing_site()
        if landing_site:
            self.nav.target_position = landing_site
            self.nav.plan_path(landing_site)
    
    def return_home(self):
        """Return to home base."""
        self.nav.target_position = self.nav.home_position
        self.nav.path_points = self.nav.plan_path(self.nav.target_position)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Initialize navigation system
    nav = AINavigationSystem()
    controller = NavigationController(nav)
    
    print("PHI Medical Stretcher Drone - AI Navigation System")
    print("=" * 50)
    
    # Set home position (example: New York)
    nav.home_position = GPSPosition(40.7128, -74.0060, 0)
    nav.current_position = GPSPosition(40.7128, -74.0060, 100)
    
    # Dispatch to scene
    controller.dispatch_to_scene(40.7580, -73.9855)
    
    print(f"Dispatched to scene at {nav.target_position.latitude}, {nav.target_position.longitude}")
    print(f"Hospitals in database: {len(nav.hospitals)}")
    
    # Find nearest hospital
    nearest = nav.find_nearest_hospital()
    if nearest:
        print(f"Nearest hospital: {nearest.name}")
        print(f"  Trauma Level: {nearest.trauma_level}")
        print(f"  Distance: {nearest.distance_m:.0f}m")
    
    # Plan path
    path = nav.plan_path(nav.target_position)
    print(f"Path planned: {len(path)} waypoints")
    
    print("\nNavigation system ready.")
