class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Floor {target_floor} is out of range.")
            return

        print(f"Moving elevator to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator {elevator_number} does not exist.")
            return

        print(f"Running elevator {elevator_number} to floor {target_floor}...")
        self.elevators[elevator_number - 1].go_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm triggered! Moving all elevators to the bottom floor...")
        for idx, elevator in enumerate(self.elevators, 1):
            print(f"Moving elevator {idx} to the bottom floor...")
            elevator.go_to_floor(self.bottom_floor)


# Testing the Building class with fire alarm
if __name__ == "__main__":

    building = Building(0, 10, 3)

    building.run_elevator(1, 5)

    building.run_elevator(2, 7)

    building.fire_alarm()