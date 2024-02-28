class Vehicle:
    def __init__(self, number, car_type, seats):
        self.number = number
        self.car_type = car_type
        self.seats = seats
        self.booked_by = None


vehicles = [
    Vehicle(1, "Suzuki Van", 2),
    Vehicle(2, "Toyota Corolla", 4),
    Vehicle(3, "Honda CRV", 4),
    Vehicle(4, "Suzuki Swift", 4),
    Vehicle(5, "Mitsubishi Airtrek", 4),
    Vehicle(6, "Nissan DC Ute", 4),
    Vehicle(7, "Toyota Previa", 7),
    Vehicle(8, "Toyota Hi Ace", 12),
    Vehicle(9, "Toyota Hi Ace", 12)
]


def display_available_vehicles(seats_needed):
    print("Available Vehicles:")
    for vehicle in vehicles:
        if vehicle.booked_by is None:
            if vehicle.seats >= seats_needed:
                print(f"{vehicle.number}. {vehicle.car_type} ({vehicle.seats} "
                      f"seats)")
            else:
                print(f"{vehicle.number}. {vehicle.car_type} ({vehicle.seats} "
                      f"seats) - Not enough seats")


def book_vehicle(vehicle_number, name):
    for vehicle in vehicles:
        if vehicle.number == vehicle_number and vehicle.booked_by is None:
            vehicle.booked_by = name
            return True
    return False


def main():
    print("Welcome to the University's Vehicle Booking System!")
    while True:
        seats_needed = int(input("Enter the number of seats needed "
                                 "(type '-1' to stop): "))
        if seats_needed == -1:
            print("Input mode stopped.")
            break
        display_available_vehicles(seats_needed)
        vehicle_number = int(input("Enter the number of the vehicle to be "
                                   "booked: "))
        name = input("Enter your name: ")
        if book_vehicle(vehicle_number, name):
            print(f"Vehicle {vehicle_number} has been booked for {name}.")
        else:
            print("Sorry, the selected vehicle is not available or invalid. "
                  "Please try again.")

    print("\nSummary of Vehicles Booked Today:")
    for vehicle in vehicles:
        if vehicle.booked_by is not None:
            print(f"Vehicle Number: {vehicle.number}, Vehicle Type: "
                  f"{vehicle.car_type}, Booked by: {vehicle.booked_by}")


if __name__ == "__main__":
    main()

