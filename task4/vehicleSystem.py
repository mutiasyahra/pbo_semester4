# Vehicle Rental System (Multiple Inheritance & Super Call)
# Class: Vehicle, Car, Bike, LuxuryFeatures, LuxuryCar
# Attributes: brand, model, rental_rate
# Methods: calculate_rental(), open_trunk(), kickstart(), enable_gps(), enable_heated_seats()

class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def __init__(self, brand, model, rental_rate):
        super().__init__(brand, model, rental_rate)

    def open_trunk(self):
        print(f"The trunk of the {self.brand} {self.model} is now open.")


class Bike(Vehicle):
    def __init__(self, brand, model, rental_rate):
        super().__init__(brand, model, rental_rate)

    def kickstart(self):
        print(f"The {self.brand} {self.model} bike is now kickstarted.")


class LuxuryFeatures:
    def enable_gps(self):
        print("GPS has been enabled.")

    def enable_heated_seats(self):
        print("Heated seats have been enabled.")


class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, rental_rate):
        super().__init__(brand, model, rental_rate)

    def calculate_rental(self, days):
        base_rental = super().calculate_rental(days)
        luxury_charge = 50  # Extra charge for luxury features
        return base_rental + luxury_charge


# Main program to demonstrate the functionality
def main():
    vehicles = []

    while True:
        print("--Menu--")
        print("1. List Vehicles")
        print("2. Create Car")
        print("3. Create Bike")
        print("4. Create Luxury Car")
        print("5. Calculate Rental")
        print("6. Open Trunk (Car)")
        print("7. Kickstart (Bike)")
        print("8. Enable GPS (Luxury Car)")
        print("9. Enable Heated Seats (Luxury Car)")
        print("10. Exit")

        menu = input("Select menu: ")

        if menu == "1":
            for index, vehicle in enumerate(vehicles):
                print(f"{index} - {vehicle.brand} {vehicle.model}, Rental Rate: ${vehicle.rental_rate}")

        elif menu == "2":
            brand = input("Insert car brand: ")
            model = input("Insert car model: ")
            rental_rate = int(input("Insert rental rate: "))
            vehicles.append(Car(brand, model, rental_rate))

        elif menu == "3":
            brand = input("Insert bike brand: ")
            model = input("Insert bike model: ")
            rental_rate = int(input("Insert rental rate: "))
            vehicles.append(Bike(brand, model, rental_rate))

        elif menu == "4":
            brand = input("Insert luxury car brand: ")
            model = input("Insert luxury car model: ")
            rental_rate = int(input("Insert rental rate: "))
            vehicles.append(LuxuryCar(brand, model, rental_rate))

        elif menu == "5":
            index = int(input("Choose vehicle index: "))
            days = int(input("Insert number of days: "))
            print(f"Rental price for {days} days: ${vehicles[index].calculate_rental(days)}")

        elif menu == "6":
            index = int(input("Choose car index: "))
            if isinstance(vehicles[index], Car):
                vehicles[index].open_trunk()
            else:
                print("Selected vehicle is not a car.")

        elif menu == "7":
            index = int(input("Choose bike index: "))
            if isinstance(vehicles[index], Bike):
                vehicles[index].kickstart()
            else:
                print("Selected vehicle is not a bike.")

        elif menu == "8":
            index = int(input("Choose luxury car index: "))
            if isinstance(vehicles[index], LuxuryCar):
                vehicles[index].enable_gps()
            else:
                print("Selected vehicle is not a luxury car.")

        elif menu == "9":
            index = int(input("Choose luxury car index: "))
            if isinstance(vehicles[index], LuxuryCar):
                vehicles[index].enable_heated_seats()
            else:
                print("Selected vehicle is not a luxury car.")

        elif menu == "10":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()