#Extending Mod_9_1.py, Mod_9_2.py and Mod_9_3.py file according to the question
"""NEED HELP IN THIS SPECIFIC EXCERCISE
Couldn't figure out how to break the loop when the distance travelled exceeds 10000 km"""

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def print_properties(self):
        # to print in table format
        print(f"{self.registration_number:<13}| {self.max_speed:<13}    | {self.current_speed:<17}    | {self.travelled_distance:<15}")

# Main
def main():
    # Creating a list of cars
    cars = []
    race_finished = False
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        registration_number = f"ABC-{i}"
        cars.append(Car(registration_number, max_speed))

    # Race until one car reaches 10,000 km
    while not race_finished:
        for car in cars:
            # Randomly adjust speed between -10 and +15 km/h
            change_speed = random.randint(-10, 15)
            car.accelerate(change_speed)
            # All car drives for 1 hour
            car.drive(1)
            # Check if any car has reached 10,000 km
            if car.travelled_distance >= 10000:
                print(f"Race over! {car.registration_number} has exceeded 10,000 km.")
                race_finished = True
                break


        if race_finished:
            break
    # Print out the properties of each car formatted in a table
    print(f"{'Registration':<13}{'| Max Speed (km/h)':<13}{' | Current Speed (km/h)':<17}{' | Travelled Distance (km)':<15}")
    print("-------------|------------------|----------------------|----------------")
    for car in cars:
        car.print_properties()

if __name__ == "__main__":
    main()