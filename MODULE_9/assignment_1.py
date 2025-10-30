class Car:
    def __init__(self, registr_num, max_speed, current_speed=0, travel_distance=0):
        self.registr_num = registr_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def print_info(self):
        print(f"registration number: {self.registr_num}, maximum speed is: {self.max_speed}, current speed is: {self.current_speed}, travelled distance is: {self.travel_distance}")



car1 = Car('ABC-124', '142 km/h')
car1.print_info()
