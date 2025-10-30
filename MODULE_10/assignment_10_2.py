


class Elevator:

    def __init__(self, num_of_bot, num_of_top):
        self.num_of_bot = num_of_bot
        self.num_of_top = num_of_top
        self.current_floor = num_of_bot

    def go_to_floor(self, target_floor):
        self.target_floor = target_floor
        if target_floor<1 or target_floor>10:
            print(f"no such floor as {target_floor}")
            return


        elif target_floor == self.current_floor:
            print(f"the floor is already {target_floor}")
            return

        elif target_floor > self.current_floor:
            self.floor_up()
            return
        elif target_floor < self.current_floor:
            self.floor_down()
            return


        elif target_floor == self.current_floor:
            print(f"the floor is already {target_floor}")
            return


    def floor_up(self):
        while self.target_floor > self.current_floor:
            self.current_floor = self.current_floor +1


    def floor_down(self):
        while self.target_floor > self.current_floor:
            self.current_floor = self.num_of_bot.current_floor -1
        print(f"you are now at the floor {self.current_floor}")

class Building:
    def __init__(self, num_of_bot, num_of_top, num_of_elev):
        self.num_of_bot = num_of_bot
        self.num_of_top = num_of_top
        self.num_of_elev = num_of_elev
        self.list_of_elevators = []

        for i in range(num_of_elev):
            new_elevator = Elevator(num_of_bot, num_of_top)
            self.list_of_elevators.append(new_elevator)

    def run_elevator(self, num_of_elev, floor_dest):
        elev_index = num_of_elev -1

        if elev_index <= 0 or elev_index>= len(self.list_of_elevators):
            print("no such elevator")
            return
        elevator = self.list_of_elevators[elev_index]
        elevator.go_to_floor(floor_dest)





h = Elevator(1,10)
h.go_to_floor(5)
h.go_to_floor(h.num_of_bot)

the_building = Building(1,20,5)
the_building.run_elevator(3,6)
the_building.run_elevator(3,1)
the_building.run_elevator(8,3)
the_building.run_elevator(1, 25)

