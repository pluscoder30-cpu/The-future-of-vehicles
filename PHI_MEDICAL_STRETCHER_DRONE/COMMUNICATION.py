"""
PHI Medical Stretcher Drone - Communication System
Model: PMSD-100, Version: 2.0
Multi-layer: 4G/5G LTE, 900 MHz mesh, Iridium satellite
"""
import time
import json
import struct
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class CommLink(Enum):
    LTE = "lte"
    MESH = "mesh"
    SAT = "satellite"
    NONE = "none"


class MsgType(Enum):
    TELEMETRY = 0x01
    MEDICAL = 0x02
    ALERT = 0x03
    VIDEO = 0x04
    COMMAND = 0x05
    HEARTBEAT = 0x07
    EMERGENCY = 0xFF


@dataclass
class Message:
    msg_type: MsgType
    seq: int
    timestamp: float
    payload: bytes
    src: str = ""
    dst: str = ""

    def serialize(self) -> bytes:
        hdr = struct.pack("!BBHd", self.msg_type.value, 0, self.seq, self.timestamp)
        return hdr + self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> "Message":
        mt, fl, sq, ts = struct.unpack("!BBHd", data[:12])
        return cls(MsgType(mt), sq, ts, data[12:])


@dataclass
class Telemetry:
    state: int
    phase: int
    lat: float
    lon: float
    alt: float
    speed: float
    battery: float
    voltage: float
    current: float
    dist_target: float
    eta: float
    hr: float
    spo2: float
    temp: float
    phi_active: bool
    phi_freq: float
    motors: List[bool]

    def to_bytes(self) -> bytes:
        mb = 0
        for i, ok in enumerate(self.motors[:8]):
            if ok:
                mb |= 1 << i
        return struct.pack(
            "!BBddddddddddBBBx",
            self.state, self.phase, self.lat, self.lon, self.alt, self.speed,
            self.battery, self.voltage, self.current, self.dist_target,
            self.eta, self.hr, self.spo2, self.temp,
            int(self.phi_active), int(self.phi_freq), mb,
        )


@dataclass
class MedicalData:
    patient_id: str
    hr: float
    spo2: float
    sys: float
    dia: float
    temp: float
    resp: float
    etco2: float
    alerts: List[str]

    def to_json(self) -> str:
        return json.dumps({
            "pid": self.patient_id, "hr": self.hr, "spo2": self.spo2,
            "bp": f"{self.sys:.0f}/{self.dia:.0f}", "temp": self.temp,
            "resp": self.resp, "etco2": self.etco2, "alerts": self.alerts,
        })


class LTEConnection:
    def __init__(self):
        self.connected = False
        self.rssi = -70
        self.up_mbps = 10
        self.down_mbps = 50

    def connect(self) -> bool:
        self.connected = True
        return True

    def disconnect(self):
        self.connected = False

    def send(self, data: bytes) -> bool:
        return self.connected

    def receive(self) -> Optional[bytes]:
        return None if not self.connected else b""


class MeshConnection:
    def __init__(self):
        self.connected = False
        self.mesh_id = 0
        self.node_count = 0
        self.range_km = 10

    def connect(self) -> bool:
        self.connected = True
        return True

    def send(self, data: bytes) -> bool:
        return self.connected

    def receive(self) -> Optional[bytes]:
        return None


class SatelliteConnection:
    def __init__(self):
        self.connected = False
        self.bandwidth_bps = 2400
        self.latency_ms = 600

    def connect(self) -> bool:
        self.connected = True
        return True

    def send(self, data: bytes) -> bool:
        return self.connected

    def receive(self) -> Optional[bytes]:
        return None


class CommunicationSystem:
    def __init__(self):
        self.lte = LTEConnection()
        self.mesh = MeshConnection()
        self.sat = SatelliteConnection()
        self.primary = CommLink.LTE
        self.seq = 0
        self.telemetry_log = []
        self.alerts = []

    def initialize(self):
        self.lte.connect()
        self.mesh.connect()
        print("Communication system initialized")
        print(f"  LTE: {self.lte.connected}, Mesh: {self.mesh.connected}")

    def send_telemetry(self, telemetry: Telemetry) -> bool:
        pkt = Message(MsgType.TELEMETRY, self.seq, time.time(), telemetry.to_bytes())
        self.seq += 1
        sent = self._send_primary(pkt.serialize())
        self.telemetry_log.append(telemetry)
        if len(self.telemetry_log) > 1000:
            self.telemetry_log.pop(0)
        return sent

    def send_medical(self, medical: MedicalData) -> bool:
        payload = medical.to_json().encode("utf-8")
        pkt = Message(MsgType.MEDICAL, self.seq, time.time(), payload)
        self.seq += 1
        return self._send_primary(pkt.serialize())

    def send_alert(self, alert_msg: str, level: int = 2) -> bool:
        payload = json.dumps({"level": level, "msg": alert_msg}).encode("utf-8")
        pkt = Message(MsgType.ALERT, self.seq, time.time(), payload)
        self.seq += 1
        self.alerts.append(alert_msg)
        self._send_all_links(pkt.serialize())
        return True

    def send_emergency(self, data: bytes) -> bool:
        pkt = Message(MsgType.EMERGENCY, self.seq, time.time(), data)
        self.seq += 1
        return self._send_all_links(pkt.serialize())

    def receive_command(self) -> Optional[dict]:
        for link in [self.lte, self.mesh, self.sat]:
            raw = link.receive()
            if raw and len(raw) > 12:
                msg = Message.deserialize(raw)
                if msg.msg_type == MsgType.COMMAND:
                    try:
                        return json.loads(msg.payload.decode("utf-8"))
                    except Exception:
                        pass
        return None

    def _send_primary(self, data: bytes) -> bool:
        if self.primary == CommLink.LTE:
            return self.lte.send(data)
        elif self.primary == CommLink.MESH:
            return self.mesh.send(data)
        elif self.primary == CommLink.SAT:
            return self.sat.send(data)
        return False

    def _send_all_links(self, data: bytes):
        self.lte.send(data)
        self.mesh.send(data)

    def get_status(self) -> dict:
        return {
            "lte": self.lte.connected,
            "mesh": self.mesh.connected,
            "sat": self.sat.connected,
            "primary": self.primary.value,
            "seq": self.seq,
            "alerts": len(self.alerts),
        }


if __name__ == "__main__":
    print("PHI Medical Stretcher Drone - Communication System")
    print("=" * 55)
    cs = CommunicationSystem()
    cs.initialize()
    tel = Telemetry(1, 3, 40.7128, -74.006, 100.0, 22.0, 0.85, 48.5, 120.0,
                    5000.0, 227.0, 72.0, 98.0, 37.0, True, 16.18,
                    [True]*8)
    cs.send_telemetry(tel)
    med = MedicalData("PT-001", 72.0, 98.0, 120.0, 80.0, 37.0, 16.0, 38.0, [])
    cs.send_medical(med)
    print(f"Comm status: {cs.get_status()}")
