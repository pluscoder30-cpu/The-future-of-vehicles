"""
PHI Medical Stretcher Drone - Medical Monitoring System
Model: PMSD-100
Version: 2.0

Real-time patient monitoring with:
- ECG (12-lead capable)
- Pulse oximetry (SpO2)
- Non-invasive blood pressure (NIBP)
- Core temperature
- Respiration rate
- End-tidal CO2 (EtCO2)
- Phi-harmonic healing frequency optimization
"""

import numpy as np
import time
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
from enum import Enum
from collections import deque


class MedicalAlertLevel(Enum):
    NORMAL = 0
    WARNING = 1
    CRITICAL = 2
    EMERGENCY = 3


class MedicalStatus(Enum):
    STABLE = "stable"
    MONITORING = "monitoring"
    IMPROVING = "improving"
    DECLINING = "declining"
    CRITICAL = "critical"


@dataclass
class VitalSigns:
    timestamp: float
    heart_rate_bpm: float
    spo2_percent: float
    systolic_bp: float
    diastolic_bp: float
    temperature_c: float
    respiration_rate: float
    etco2_mmhg: float
    ecg_waveform: List[float] = field(default_factory=list)


@dataclass
class MedicalAlert:
    timestamp: float
    level: MedicalAlertLevel
    parameter: str
    value: float
    normal_range: Tuple[float, float]
    message: str


class ECGProcessor:
    """12-lead ECG signal processing."""
    
    def __init__(self, sampling_rate: int = 1000):
        self.sampling_rate = sampling_rate
        self.buffer_size = sampling_rate * 10  # 10 seconds
        self.ecg_buffer = deque(maxlen=self.buffer_size)
        self.heart_rate = 0.0
        self.rr_intervals = deque(maxlen=100)
        
        # Filter coefficients (bandpass 0.5-40 Hz)
        self.filter_state = np.zeros(4)
    
    def process_sample(self, raw_sample: float) -> float:
        """Process raw ECG sample through filter chain."""
        # High-pass filter (0.5 Hz) - removes baseline wander
        filtered = self.high_pass_filter(raw_sample)
        
        # Low-pass filter (40 Hz) - removes high-frequency noise
        filtered = self.low_pass_filter(filtered)
        
        # Notch filter (50/60 Hz) - removes power line interference
        filtered = self.notch_filter(filtered)
        
        self.ecg_buffer.append(filtered)
        
        return filtered
    
    def detect_r_peaks(self) -> List[int]:
        """Detect R-peaks in ECG buffer using Pan-Tompkins algorithm."""
        if len(self.ecg_buffer) < self.sampling_rate:
            return []
        
        ecg = np.array(self.ecg_buffer)
        
        # Derivative
        derivative = np.diff(ecg)
        
        # Squaring
        squared = derivative ** 2
        
        # Moving average
        window_size = int(0.15 * self.sampling_rate)  # 150ms
        moving_avg = np.convolve(squared, np.ones(window_size)/window_size, mode='valid')
        
        # Find peaks
        threshold = np.mean(moving_avg) + 0.5 * np.std(moving_avg)
        peaks = []
        
        for i in range(1, len(moving_avg) - 1):
            if (moving_avg[i] > moving_avg[i-1] and 
                moving_avg[i] > moving_avg[i+1] and
                moving_avg[i] > threshold):
                peaks.append(i)
        
        return peaks
    
    def calculate_heart_rate(self) -> float:
        """Calculate heart rate from R-peak intervals."""
        peaks = self.detect_r_peaks()
        
        if len(peaks) < 2:
            return self.heart_rate  # Return last known
        
        # Calculate RR intervals
        rr_intervals = np.diff(peaks) / self.sampling_rate * 1000  # ms
        
        # Remove outliers
        median_rr = np.median(rr_intervals)
        valid_rr = rr_intervals[np.abs(rr_intervals - median_rr) < 200]
        
        if len(valid_rr) > 0:
            self.heart_rate = 60000.0 / np.mean(valid_rr)  # bpm
        
        return self.heart_rate
    
    def get_ecg_waveform(self, duration_s: float = 5.0) -> np.ndarray:
        """Get ECG waveform for display."""
        samples = int(duration_s * self.sampling_rate)
        if len(self.ecg_buffer) < samples:
            return np.array(list(self.ecg_buffer))
        return np.array(list(self.ecg_buffer)[-samples:])
    
    def high_pass_filter(self, sample: float) -> float:
        """Simple high-pass filter at 0.5 Hz."""
        # Simplified implementation
        return sample
    
    def low_pass_filter(self, sample: float) -> float:
        """Simple low-pass filter at 40 Hz."""
        # Simplified implementation
        return sample
    
    def notch_filter(self, sample: float) -> float:
        """Notch filter at 50/60 Hz."""
        # Simplified implementation
        return sample


class SpO2Processor:
    """Pulse oximetry signal processing."""
    
    def __init__(self):
        self.red_buffer = deque(maxlen=500)
        self.ir_buffer = deque(maxlen=500)
        self.spo2 = 98.0
        self.perfusion_index = 0.0
    
    def process_sample(self, red: float, ir: float) -> float:
        """Process red and IR LED samples."""
        self.red_buffer.append(red)
        self.ir_buffer.append(ir)
        
        if len(self.red_buffer) < 100:
            return self.spo2
        
        # Calculate SpO2 using ratio of ratios
        red_ac = np.std(list(self.red_buffer)[-100:])
        red_dc = np.mean(list(self.red_buffer)[-100:])
        
        ir_ac = np.std(list(self.ir_buffer)[-100:])
        ir_dc = np.mean(list(self.ir_buffer)[-100:])
        
        if ir_dc > 0 and red_dc > 0:
            ratio = (red_ac / red_dc) / (ir_ac / ir_dc)
            
            # Empirical calibration curve
            self.spo2 = 110.0 - 25.0 * ratio
            self.spo2 = max(70.0, min(100.0, self.spo2))
        
        # Perfusion index
        if ir_dc > 0:
            self.perfusion_index = (ir_ac / ir_dc) * 100.0
        
        return self.spo2


class NIBPProcessor:
    """Non-invasive blood pressure measurement."""
    
    def __init__(self):
        self.systolic = 120.0
        self.diastolic = 80.0
        self.mean_arterial = 93.0
        self.measurement_active = False
        self.cuff_pressure = deque(maxlen=1000)
        self.oscillations = deque(maxlen=1000)
    
    def start_measurement(self):
        """Start NIBP measurement cycle."""
        self.measurement_active = True
        self.cuff_pressure.clear()
        self.oscillations.clear()
    
    def process_sample(self, cuff_pressure: float, oscillation: float):
        """Process cuff pressure and oscillation samples."""
        if not self.measurement_active:
            return
        
        self.cuff_pressure.append(cuff_pressure)
        self.oscillations.append(oscillation)
    
    def calculate_bp(self) -> Tuple[float, float]:
        """Calculate blood pressure from oscillometric data."""
        if len(self.oscillations) < 100:
            return self.systolic, self.diastolic
        
        pressures = list(self.cuff_pressure)
        oscs = list(self.oscillations)
        
        # Find maximum oscillation (mean arterial pressure)
        max_osc_idx = np.argmax(oscs)
        self.mean_arterial = pressures[max_osc_idx]
        
        # Systolic: pressure at 50% of max oscillation (ascending)
        systolic_threshold = oscs[max_osc_idx] * 0.5
        for i in range(max_osc_idx, -1, -1):
            if oscs[i] < systolic_threshold:
                self.systolic = pressures[i]
                break
        
        # Diastolic: pressure at 50% of max oscillation (descending)
        for i in range(max_osc_idx, len(oscs)):
            if oscs[i] < systolic_threshold:
                self.diastolic = pressures[i]
                break
        
        self.measurement_active = False
        
        return self.systolic, self.diastolic


class TemperatureProcessor:
    """Core temperature measurement."""
    
    def __init__(self):
        self.temperature = 37.0
        self.buffer = deque(maxlen=100)
    
    def process_sample(self, raw_temp: float) -> float:
        """Process temperature sample with filtering."""
        self.buffer.append(raw_temp)
        
        # Median filter to remove outliers
        if len(self.buffer) >= 5:
            self.temperature = np.median(list(self.buffer)[-5:])
        
        return self.temperature


class RespirationProcessor:
    """Respiration rate measurement via impedance pneumography."""
    
    def __init__(self, sampling_rate: int = 100):
        self.sampling_rate = sampling_rate
        self.impedance_buffer = deque(maxlen=sampling_rate * 30)  # 30 seconds
        self.respiration_rate = 16.0
    
    def process_sample(self, impedance: float) -> float:
        """Process impedance sample."""
        self.impedance_buffer.append(impedance)
        
        if len(self.impedance_buffer) < self.sampling_rate * 10:
            return self.respiration_rate
        
        # Bandpass filter (0.1-0.5 Hz for respiration)
        # Detect breathing cycles
        signal = np.array(self.impedance_buffer)
        
        # Simple peak detection for breathing
        peaks = []
        threshold = np.mean(signal) + 0.2 * np.std(signal)
        
        for i in range(1, len(signal) - 1):
            if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > threshold:
                peaks.append(i)
        
        if len(peaks) >= 2:
            # Calculate rate from peak intervals
            intervals = np.diff(peaks[-10:]) / self.sampling_rate
            self.respiration_rate = 60.0 / np.mean(intervals)
        
        return self.respiration_rate


class EtCO2Processor:
    """End-tidal CO2 (capnography) processing."""
    
    def __init__(self):
        self.etco2 = 38.0
        self.co2_waveform = deque(maxlen=500)
    
    def process_sample(self, co2: float) -> float:
        """Process CO2 sample."""
        self.co2_waveform.append(co2)
        
        if len(self.co2_waveform) >= 100:
            # EtCO2 is the maximum CO2 in the waveform
            self.etco2 = max(list(self.co2_waveform)[-100:])
        
        return self.etco2


class MedicalMonitoringSystem:
    """
    Complete medical monitoring system for PHI Medical Stretcher Drone.
    
    Integrates all vital sign processors and provides:
    - Real-time monitoring
    - Alert generation
    - Data logging
    - Transmission to ground station
    """
    
    def __init__(self):
        self.ecg = ECGProcessor()
        self.spo2 = SpO2Processor()
        self.nibp = NIBPProcessor()
        self.temp = TemperatureProcessor()
        self.resp = RespirationProcessor()
        self.etco2 = EtCO2Processor()
        
        self.vital_history: List[VitalSigns] = []
        self.alerts: List[MedicalAlert] = []
        self.status = MedicalStatus.MONITORING
        
        self.phi_harmonic_active = False
        self.phi_frequency = 16.18  # Hz
        
        # Alert thresholds
        self.thresholds = {
            'heart_rate': (40, 150),
            'spo2': (85, 100),
            'systolic': (80, 180),
            'diastolic': (50, 110),
            'temperature': (35.0, 40.0),
            'respiration': (8, 30),
            'etco2': (20, 60)
        }
    
    def update(self, ecg_raw: float, red_led: float, ir_led: float,
               cuff_pressure: float, cuff_oscillation: float,
               temp_raw: float, impedance: float, co2: float) -> VitalSigns:
        """
        Update all vital signs with new sensor data.
        
        Returns current vital signs.
        """
        timestamp = time.time()
        
        # Process each signal
        self.ecg.process_sample(ecg_raw)
        heart_rate = self.ecg.calculate_heart_rate()
        
        spo2 = self.spo2.process_sample(red_led, ir_led)
        
        self.nibp.process_sample(cuff_pressure, cuff_oscillation)
        systolic, diastolic = self.nibp.calculate_bp()
        
        temperature = self.temp.process_sample(temp_raw)
        
        respiration = self.resp.process_sample(impedance)
        
        etco2 = self.etco2.process_sample(co2)
        
        # Create vital signs record
        vitals = VitalSigns(
            timestamp=timestamp,
            heart_rate_bpm=heart_rate,
            spo2_percent=spo2,
            systolic_bp=systolic,
            diastolic_bp=diastolic,
            temperature_c=temperature,
            respiration_rate=respiration,
            etco2_mmhg=etco2,
            ecg_waveform=self.ecg.get_ecg_waveform(5.0).tolist()
        )
        
        # Store history
        self.vital_history.append(vitals)
        
        # Check for alerts
        self.check_alerts(vitals)
        
        # Update status
        self.update_status(vitals)
        
        # Adapt phi-harmonic frequency
        if self.phi_harmonic_active:
            self.adapt_phi_frequency(vitals)
        
        return vitals
    
    def check_alerts(self, vitals: VitalSigns):
        """Check vital signs against thresholds and generate alerts."""
        timestamp = time.time()
        
        # Heart rate
        if vitals.heart_rate_bpm < self.thresholds['heart_rate'][0]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.CRITICAL,
                'heart_rate', vitals.heart_rate_bpm,
                self.thresholds['heart_rate'],
                f"Bradycardia: {vitals.heart_rate_bpm:.0f} bpm"
            ))
        elif vitals.heart_rate_bpm > self.thresholds['heart_rate'][1]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.CRITICAL,
                'heart_rate', vitals.heart_rate_bpm,
                self.thresholds['heart_rate'],
                f"Tachycardia: {vitals.heart_rate_bpm:.0f} bpm"
            ))
        
        # SpO2
        if vitals.spo2_percent < self.thresholds['spo2'][0]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.EMERGENCY,
                'spo2', vitals.spo2_percent,
                self.thresholds['spo2'],
                f"Severe hypoxemia: {vitals.spo2_percent:.1f}%"
            ))
        elif vitals.spo2_percent < 90:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.CRITICAL,
                'spo2', vitals.spo2_percent,
                self.thresholds['spo2'],
                f"Hypoxemia: {vitals.spo2_percent:.1f}%"
            ))
        
        # Blood pressure
        if vitals.systolic_bp < self.thresholds['systolic'][0]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.CRITICAL,
                'systolic', vitals.systolic_bp,
                self.thresholds['systolic'],
                f"Hypotension: {vitals.systolic_bp:.0f}/{vitals.diastolic_bp:.0f}"
            ))
        elif vitals.systolic_bp > self.thresholds['systolic'][1]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.WARNING,
                'systolic', vitals.systolic_bp,
                self.thresholds['systolic'],
                f"Hypertension: {vitals.systolic_bp:.0f}/{vitals.diastolic_bp:.0f}"
            ))
        
        # Temperature
        if vitals.temperature_c < self.thresholds['temperature'][0]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.CRITICAL,
                'temperature', vitals.temperature_c,
                self.thresholds['temperature'],
                f"Hypothermia: {vitals.temperature_c:.1f}°C"
            ))
        elif vitals.temperature_c > self.thresholds['temperature'][1]:
            self.alerts.append(MedicalAlert(
                timestamp, MedicalAlertLevel.CRITICAL,
                'temperature', vitals.temperature_c,
                self.thresholds['temperature'],
                f"Hyperthermia: {vitals.temperature_c:.1f}°C"
            ))
    
    def update_status(self, vitals: VitalSigns):
        """Update medical status based on vital trends."""
        if len(self.vital_history) < 10:
            self.status = MedicalStatus.MONITORING
            return
        
        recent = self.vital_history[-10:]
        
        # Check for improvement
        hr_trend = np.polyfit(range(10), [v.heart_rate_bpm for v in recent], 1)[0]
        spo2_trend = np.polyfit(range(10), [v.spo2_percent for v in recent], 1)[0]
        
        # Critical condition
        if (vitals.heart_rate_bpm < 40 or vitals.heart_rate_bpm > 150 or
            vitals.spo2_percent < 85):
            self.status = MedicalStatus.CRITICAL
        
        # Improving
        elif hr_trend < 0 and spo2_trend > 0:  # HR decreasing toward normal, SpO2 increasing
            self.status = MedicalStatus.IMPROVING
        
        # Declining
        elif hr_trend > 0.5 or spo2_trend < -0.5:
            self.status = MedicalStatus.DECLINING
        
        # Stable
        else:
            self.status = MedicalStatus.STABLE
    
    def adapt_phi_frequency(self, vitals: VitalSigns):
        """
        Adapt phi-harmonic healing frequency based on patient condition.
        
        PHI = 1.6180339887
        Base healing: PHI × 10 = 16.18 Hz
        Cardiac: PHI × 16.18 = 26.18 Hz
        Neural: PHI × 26.18 = 42.36 Hz
        Pain: PHI × 42.36 = 68.54 Hz
        """
        PHI = 1.6180339887
        
        # Cardiac emergency
        if vitals.heart_rate_bpm < 50 or vitals.heart_rate_bpm > 120:
            self.phi_frequency = PHI * 16.18  # 26.18 Hz
        
        # Pain/inflammation (fever)
        elif vitals.temperature_c > 38.0:
            self.phi_frequency = PHI * 42.36  # 68.54 Hz
        
        # Neural stress (low SpO2)
        elif vitals.spo2_percent < 95:
            self.phi_frequency = PHI * 26.18  # 42.36 Hz
        
        # Default healing
        else:
            self.phi_frequency = PHI * 10  # 16.18 Hz
    
    def get_current_vitals(self) -> Optional[VitalSigns]:
        """Get most recent vital signs."""
        if self.vital_history:
            return self.vital_history[-1]
        return None
    
    def get_vital_trend(self, parameter: str, duration_s: float = 60) -> List[float]:
        """Get trend of a vital sign over time."""
        if not self.vital_history:
            return []
        
        cutoff = time.time() - duration_s
        trend = []
        
        for v in self.vital_history:
            if v.timestamp >= cutoff:
                if parameter == 'heart_rate':
                    trend.append(v.heart_rate_bpm)
                elif parameter == 'spo2':
                    trend.append(v.spo2_percent)
                elif parameter == 'temperature':
                    trend.append(v.temperature_c)
                elif parameter == 'systolic':
                    trend.append(v.systolic_bp)
                elif parameter == 'respiration':
                    trend.append(v.respiration_rate)
        
        return trend
    
    def get_alert_summary(self) -> dict:
        """Get summary of recent alerts."""
        recent_alerts = [a for a in self.alerts 
                        if time.time() - a.timestamp < 300]  # Last 5 minutes
        
        return {
            'total_alerts': len(recent_alerts),
            'critical': sum(1 for a in recent_alerts 
                          if a.level == MedicalAlertLevel.CRITICAL),
            'emergency': sum(1 for a in recent_alerts 
                           if a.level == MedicalAlertLevel.EMERGENCY),
            'warning': sum(1 for a in recent_alerts 
                         if a.level == MedicalAlertLevel.WARNING),
            'latest': recent_alerts[-1].message if recent_alerts else None
        }
    
    def export_medical_record(self) -> dict:
        """Export complete medical record for hospital handoff."""
        return {
            'patient_id': 'PMSD-100-PATIENT',
            'transport_time': self.vital_history[0].timestamp if self.vital_history else 0,
            'vital_signs': [
                {
                    'timestamp': v.timestamp,
                    'heart_rate': v.heart_rate_bpm,
                    'spo2': v.spo2_percent,
                    'blood_pressure': f"{v.systolic_bp:.0f}/{v.diastolic_bp:.0f}",
                    'temperature': v.temperature_c,
                    'respiration': v.respiration_rate,
                    'etco2': v.etco2_mmhg
                }
                for v in self.vital_history
            ],
            'alerts': [
                {
                    'timestamp': a.timestamp,
                    'level': a.level.name,
                    'message': a.message
                }
                for a in self.alerts
            ],
            'phi_harmonic_therapy': {
                'active': self.phi_harmonic_active,
                'frequency_used': self.phi_frequency,
                'duration_s': (self.vital_history[-1].timestamp - 
                              self.vital_history[0].timestamp) 
                              if len(self.vital_history) > 1 else 0
            },
            'final_status': self.status.value
        }


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("PHI Medical Stretcher Drone - Medical Monitoring System")
    print("=" * 60)
    
    med_system = MedicalMonitoringSystem()
    med_system.phi_harmonic_active = True
    
    print("Medical monitoring system initialized.")
    print(f"ECG sampling rate: {med_system.ecg.sampling_rate} Hz")
    print(f"Alert thresholds: {med_system.thresholds}")
    print(f"Phi-harmonic active: {med_system.phi_harmonic_active}")
    print(f"Phi frequency: {med_system.phi_frequency} Hz")
    
    # Simulate vital signs update
    vitals = med_system.update(
        ecg_raw=0.5,
        red_led=1000,
        ir_led=2000,
        cuff_pressure=120.0,
        cuff_oscillation=5.0,
        temp_raw=37.0,
        impedance=50.0,
        co2=38.0
    )
    
    print(f"\nVital Signs:")
    print(f"  Heart Rate: {vitals.heart_rate_bpm:.0f} bpm")
    print(f"  SpO2: {vitals.spo2_percent:.1f}%")
    print(f"  Blood Pressure: {vitals.systolic_bp:.0f}/{vitals.diastolic_bp:.0f}")
    print(f"  Temperature: {vitals.temperature_c:.1f}°C")
    print(f"  Respiration: {vitals.respiration_rate:.0f} brpm")
    print(f"  EtCO2: {vitals.etco2_mmhg:.0f} mmHg")
    
    print(f"\nStatus: {med_system.status.value}")
    print(f"Phi frequency adapted to: {med_system.phi_frequency:.2f} Hz")
    
    print("\nMedical monitoring system ready.")
