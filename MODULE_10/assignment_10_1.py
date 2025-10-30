



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


h = Elevator(1,10)
target_floor = 5

num_of_bot = h.num_of_bot
h.go_to_floor(target_floor)
print(f" you are at the floor {target_floor}")




