# models/slot.py
from dataclasses import dataclass
from typing import Optional
from .vehicle import Vehicle

@dataclass
class Slot:
    id: int
    size: str            # "SMALL" | "LARGE" | "OVERSIZE"
    vehicle: Optional[Vehicle] = None

<<<<<<< HEAD
    def is_free(self) -> bool:  #To quickly check if a slot is available
=======
    def is_free(self) -> bool:
>>>>>>> d822ebb (initial commit)
        return self.vehicle is None
