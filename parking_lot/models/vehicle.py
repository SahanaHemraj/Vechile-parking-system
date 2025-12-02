# models/vehicle.py
from dataclasses import dataclass

@dataclass
class Vehicle:
    plate: str
    size: str   # "SMALL" | "LARGE" | "OVERSIZE"
