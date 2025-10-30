class Car:
    def __init__(self, registr_num, max_speed, current_speed=0, travel_distance=0):
        self.registr_num = registr_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def print_info(self):
        print(f"registration number: {self.registr_num}, maximum speed is: {self.max_speed}, current speed is: {self.current_speed}, travelled distance is: {self.travel_distance}")

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
                self.current_speed = 0
                print(f"registration number is {self.registr_num}")
                print(f"maximum speed is {self.max_speed}")
                print(f"current speed is {self.current_speed} km/h")
                print(f"travelled distance is {self.travel_distance} km")












car1 = Car('ABC-124', 542)
car1.print_info()
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)