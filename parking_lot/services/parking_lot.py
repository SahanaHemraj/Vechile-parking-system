# parking_lot.py
from models.parking_lot_core import ParkingLot

def read_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid number. Try again.")

def print_help():
    print("""
Commands:
  park <plate> <size>   - Park a vehicle (size: small|large|oversize)
  leave <slot_id>       - Free a slot
  status                - Show parking lot status
  help                  - Show commands
  exit                  - Quit
""")

def main():
    n = read_positive_int("Enter total number of parking slots: ")
    lot = ParkingLot(n)

    small, large, oversize = lot.summary_counts()
    print(f"Parking lot initialized with {n} slots:")
    print(f"  SMALL: {small}")
    print(f"  LARGE: {large}")
    print(f"  OVERSIZE: {oversize}")

    print_help()

    while True:
        cmd = input("> ").strip().split()

        if not cmd:
            continue

        action = cmd[0].lower()

        if action == "park":
            if len(cmd) < 3:
                print("Usage: park <plate> <size>")
                continue

            plate = cmd[1]
            size = cmd[2].upper()

            if size not in ["SMALL", "LARGE", "OVERSIZE"]:
                print("Size must be: small | large | oversize")
                continue

            result = lot.park_vehicle(plate, size)

            if result == -2:
                print("Vehicle already parked.")
            elif result == -1:
                print("No suitable slot available.")
            else:
                print(f"Vehicle parked at slot {result}.")

        elif action == "leave":
            if len(cmd) < 2:
                print("Usage: leave <slot_id>")
                continue

            try:
                sid = int(cmd[1])
            except ValueError:
                print("Slot ID must be a number.")
                continue

            if lot.leave_slot(sid):
                print(f"Slot {sid} is now free.")
            else:
                print("Invalid slot or already free.")

        elif action == "status":
            print(lot.status())

        elif action == "help":
            print_help()

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()
