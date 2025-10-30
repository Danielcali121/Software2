import random
class Car:

    def __init__(self, registr_num, max_speed, current_speed=0, travel_distance=0):
        self.registr_num = registr_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance
    def print_info(self):
        print(
            f"registration number: {self.registr_num}, maximum speed is: {self.max_speed}, current speed is: {self.current_speed}, travelled distance is: {self.travel_distance}")

    def accelerate(self, speed):
            self.current_speed += speed
            if self.current_speed > self.max_speed or self.current_speed == self.max_speed:
                self.current_speed = self.max_speed - 1
                print(f"registration number is {self.registr_num}")
                print(f"maximum speed is {self.max_speed}")
                print(f"current speed is {self.current_speed} km/h")
                print(f"travelled distance is {self.travel_distance} km")


            elif self.current_speed < self.max_speed and self.current_speed > 0:
                print(f"registration number is {self.registr_num}")
                print(f"maximum speed is {self.max_speed}")
                print(f"current speed is {self.current_speed} km/h")
                print(f"travelled distance is {self.travel_distance} km")



            elif self.current_speed < 0 or self.current_speed == 0:
                self.current_speed = 1
                print(f"registration number is {self.registr_num}")
                print(f"maximum speed is {self.max_speed}")
                print(f"current speed is {self.current_speed} km/h")
                print(f"travelled distance is {self.travel_distance} km")






    def drive(self, hours):
        self.travel_distance += (hours* self.current_speed)
        print(f"registration number is {self.registr_num}")
        print(f"maximum speed is {self.max_speed}")
        print(f"current speed is {self.current_speed} km/h")
        print(f"travelled distance is {self.travel_distance} km")

class Race:
    def __init__(self,name, travel_distance, listofcars):
        self.name = name
        self.travel_distance = travel_distance
        self.listofcars = listofcars


    def hour_passes(self):
        winner_found = False
        race_hour = 0
        race_hour += 1
        speed_change = random.randint(-16,16)



    def print_status(self):


    def race_finished(self):
        winner_found = False
        race_hour = 0
        while not winner_found:



def create_race():
    cars=[]
    for i in range(1,11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100,200)

        car = Car(reg_number, max_speed)
        cars.append(car)

    race_hour= 0
    winner_found= False
    while not winner_found:
        race_hour += 1

        for car in cars:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)
            if car.travel_distance >= 10000:
                winner_found= True

    print(f"the race has ended in {race_hour} hours")
    cars.sort(key=lambda car: car.travel_distance, reverse=True)
    print(f"{'reg.no':<10},  {'max speed':>10}, {'current speed':>15}, {'distance (km)': >15}")

    for car in cars:
        print(f"{car.registr_num:<10},  {car.max_speed:>10}, {car.current_speed:>15}, {car.travel_distance:>15.2f}")
create_race()
