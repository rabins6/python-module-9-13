import random


class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def drive(self):
        self.distance_travelled += self.current_speed

    def change_speed(self):
        speed_change = random.randint(-10, 15)
        self.current_speed += speed_change
        # Ensure the speed is within 0 and the max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.change_speed()
            car.drive()

    def print_status(self):
        print(f"{'Car Name':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance Travelled'}")
        print("-" * 55)
        for car in self.car_list:
            print(f"{car.name:<15}{car.max_speed:<12}{car.current_speed:<15}{car.distance_travelled}")

    def race_finished(self):
        # Check if any car has reached or exceeded the race distance
        for car in self.car_list:
            if car.distance_travelled >= self.distance:
                return True
        return False


# Main program simulating the race
if __name__ == "__main__":
    """Create a list of 10 cars statically
    cars = [
        Car("Car 1", random.randint(150, 200)),
        Car("Car 2", random.randint(150, 200)),
        Car("Car 3", random.randint(150, 200)),
        Car("Car 4", random.randint(150, 200)),
        Car("Car 5", random.randint(150, 200)),
        Car("Car 6", random.randint(150, 200)),
        Car("Car 7", random.randint(150, 200)),
        Car("Car 8", random.randint(150, 200)),
        Car("Car 9", random.randint(150, 200)),
        Car("Car 10", random.randint(150, 200))
    ]
    """
    # Create a list of 10 cars dynamically using a loop
    cars = [Car(f"Car {i + 1}", random.randint(150, 200)) for i in range(10)]
    # Create the race
    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        # Print status every 10 hours
        if hours_passed % 10 == 0:
            print(f"\n--- Hour {hours_passed} ---")
            race.print_status()

    # Final status when the race finishes
    print(f"\n--- Race Finished After {hours_passed} Hours ---")
    race.print_status()