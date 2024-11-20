class Car:
    def __init__(self, registration_number, max_speed):
        # Initialize the properties
        self.registration_number = registration_number
        self.max_speed = max_speed
        # Set default values
        self.current_speed = 0
        self.travelled_distance = 0

    def print_properties(self):
        # Method to print the properties of the car
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")


# Main program
car = Car("ABC-123", 142)
car.print_properties()