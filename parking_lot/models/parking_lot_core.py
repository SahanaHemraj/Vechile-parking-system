# models/parking_lot_core.py
from typing import List
from .slot import Slot
from .vehicle import Vehicle

class ParkingLot:
    def __init__(self, total_slots: int):
        self.slots: List[Slot] = []
        self.total_slots = total_slots
        self._create_slots(total_slots)

    def _create_slots(self, total_slots: int):
        small_count = int(total_slots * 0.4)
        large_count = int(total_slots * 0.4)
        oversize_count = total_slots - small_count - large_count

        slot_id = 1

        for _ in range(small_count):
            self.slots.append(Slot(slot_id, "SMALL"))
            slot_id += 1

        for _ in range(large_count):
            self.slots.append(Slot(slot_id, "LARGE"))
            slot_id += 1

        for _ in range(oversize_count):
            self.slots.append(Slot(slot_id, "OVERSIZE"))
            slot_id += 1

    def _allowed_slot_sizes(self, vehicle_size: str):
        v = vehicle_size.upper()
        if v == "SMALL":
            return ["SMALL", "LARGE", "OVERSIZE"]
        if v == "LARGE":
            return ["LARGE", "OVERSIZE"]
        if v == "OVERSIZE":
            return ["OVERSIZE"]
        raise ValueError("Invalid vehicle size")

    def park_vehicle(self, plate: str, vehicle_size: str):
        """Returns slot ID if parked, -1 if full, -2 if duplicate."""
        # duplicate check
        for slot in self.slots:
            if slot.vehicle and slot.vehicle.plate.lower() == plate.lower():
                return -2

        allowed = self._allowed_slot_sizes(vehicle_size)

        for slot in self.slots:
            if slot.is_free() and slot.size in allowed:
                slot.vehicle = Vehicle(plate, vehicle_size.upper())
                return slot.id

        return -1  # no suitable slot

    def leave_slot(self, slot_id: int) -> bool:
        for slot in self.slots:
            if slot.id == slot_id:
                if slot.is_free():
                    return False
                slot.vehicle = None
                return True
        return False

    def status(self):
        lines = []
        lines.append("ID | SIZE     | OCCUPIED | PLATE")
        lines.append("-----------------------------------")
        for s in self.slots:
            occ = "Yes" if not s.is_free() else "No"
            plate = s.vehicle.plate if s.vehicle else ""
            lines.append(f"{s.id:<3}| {s.size:<8}| {occ:<9}| {plate}")
        return "\n".join(lines)

    def summary_counts(self):
        small = sum(1 for s in self.slots if s.size == "SMALL")
        large = sum(1 for s in self.slots if s.size == "LARGE")
        oversize = sum(1 for s in self.slots if s.size == "OVERSIZE")
        return small, large, oversize
