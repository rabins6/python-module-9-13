class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def drive(self):
        self.distance_travelled += self.current_speed

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kilowatt-hours (kWh)

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters (l)

# Main program
if __name__ == "__main__":
    # Creating one electric car and one gasoline car
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Setting speeds for both cars
    electric_car.current_speed = 100
    gasoline_car.current_speed = 120

    # for 3 hours drive
    for _ in range(3):
        electric_car.drive()
        gasoline_car.drive()

    print(f"Electric Car ({electric_car.registration_number}) travelled: {electric_car.distance_travelled} km")
    print(f"Gasoline Car ({gasoline_car.registration_number}) travelled: {gasoline_car.distance_travelled} km")



