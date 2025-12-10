# models/slot.py
from dataclasses import dataclass
from typing import Optional
from .vehicle import Vehicle

@dataclass
class Slot:
    id: int
    size: str            # "SMALL" | "LARGE" | "OVERSIZE"
    vehicle: Optional[Vehicle] = None

    def is_free(self) -> bool:  #To quickly check if a slot is available
        return self.vehicle is None
