# Parking Lot Management - Assignment

## Overview
Simple CLI Parking Lot Management application.  
Models a parking lot with `n` slots (user input). Slots are split into:
- SMALL (40%)
- LARGE (40%)
- OVERSIZE (remaining)

Features:
- Park vehicles with sizes: `small`, `large`, `oversize`
- Leave slot (free a slot)
- Show status (table of slots and parked vehicles)
- Find by plate
- Save/Load state to JSON file

This project is implemented in **Python** and organized as a small package.

## Repo structure
parking_lot/
├─ models/
│ ├─ parking_lot_core.py
│ ├─ slot.py
│ └─ vehicle.py
├─ tests/
│ └─ test_parking_core.py
├─ parking_lot.py
└─ README.md



## How to run
1. Ensure Python 3.8+ is installed.
2. From project root:
```bash
python3 parking_lot.py

3. When prompted, enter total number of parking slots (positive integer).

4. Use commands:
park <plate> <size> (size: small|large|oversize)
leave <slot_id>
status
help
exit