class Elevator:

    def __init__(self, num_of_bot, num_of_top):

        self.num_of_bot = num_of_bot
        self.num_of_top = num_of_top
        self.current_floor = num_of_bot
        print(f"Elevator created, starting at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
  
        self.target_floor = target_floor

        if not (self.num_of_bot <= target_floor <= self.num_of_top):
            print(f"Error: Floor {target_floor} is outside the building's range ({self.num_of_bot}-{self.num_of_top}).")
            return


        if target_floor == self.current_floor:
            print(f"The elevator is already at floor {target_floor}")
            return

        print(f"Elevator moving from floor {self.current_floor} to {self.target_floor}")


        if target_floor > self.current_floor:
            self.floor_up()
        elif target_floor < self.current_floor:
            self.floor_down()

    def floor_up(self):

        while self.target_floor > self.current_floor:
            self.current_floor += 1

            print(f"  ...now at floor {self.current_floor}")
        print(f"Elevator arrived at floor {self.current_floor}.")

    def floor_down(self):


        while self.current_floor > self.target_floor:

            self.current_floor -= 1

            print(f"  ...now at floor {self.current_floor}")

        print(f"You are now at the floor {self.current_floor}")


class Building:


    def __init__(self, num_of_bot, num_of_top, num_of_elev):
        self.num_of_bot = num_of_bot
        self.num_of_top = num_of_top
        self.num_of_elev = num_of_elev


        self.list_of_elevators = []


        for i in range(num_of_elev):
            new_elevator = Elevator(num_of_bot, num_of_top)
            self.list_of_elevators.append(new_elevator)
        print(f"Building created with {len(self.list_of_elevators)} elevators, floors {num_of_bot} to {num_of_top}.\n")

    def run_elevator(self, num_of_elev, floor_dest):

        elev_index = num_of_elev - 1


        if not (0 <= elev_index < len(self.list_of_elevators)):
            print(
                f"Error: Elevator number {num_of_elev} does not exist (only {len(self.list_of_elevators)} available).")
            return


        elevator = self.list_of_elevators[elev_index]
        print(f"--- Running Elevator {num_of_elev} ---")


        elevator.go_to_floor(floor_dest)
        print(f"Elevator {num_of_elev} is now on floor {elevator.current_floor}.\n")

    def fire_alarm(self):

        print("Attention, fire ongoing......please evacuate")


        for i, elevator_obj in enumerate(self.list_of_elevators):
            elevator_number = i + 1
            print(f"--- Fire Alarm: Moving Elevator {elevator_number} ---")


            elevator_obj.go_to_floor(elevator_obj.num_of_bot)


            print(f"Elevator {elevator_number} is secured at floor {elevator_obj.current_floor}\n")



h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(h.num_of_bot)  # Go back to floor 1



the_building = Building(1, 20, 5)


the_building.run_elevator(3, 16)
the_building.run_elevator(1, 19)
the_building.run_elevator(5, 7)


the_building.fire_alarm()