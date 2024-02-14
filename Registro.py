class Car:
    def __init__(self, brand, year, kilometers, registration):
        self.brand = brand
        self.year = year
        self.kilometers = kilometers
        self.registration = registration
    def show(self):
        print("Brand is: {}".format(self.brand))
        print("Year is: {}".format(self.year))
        print("Number of kilometers is: {}".format(self.kilometers))
        print("Registration is: {}".format(self.registration))

class Plane:
    def __init__(self, year, gasoline, flights):
        self.year = year
        self.gasoline = gasoline
        self.flights = flights
    def show(self):
        print("Year is: {}".format(self.year))
        print("It has {} liters of gas left".format(self.gasoline))
        print("It has had {} flights".format(self.gasoline))

class Boat:
    def __init__(self, size, speed, capacity):
        self.size = size
        self.speed = speed
        self.capacity = capacity
    def show(self):
        print("It's a {} size boat".format(self.size))
        print("It can go up to {} miles per hour".format(self.speed))
        print("It can hold up to {} people".format(self.capacity))


ferrari_car = Car("Ferrari", 2023, 12000, "20TRW5")
aveo_car = Car("Aveo", 2015, 30543, "44TR09")
first_plane = Plane(2017, 500, 12)
second_plane = Plane(1998, 432, 310)
first_boat = Boat("medium", 50, 20)
second_boat = Boat("small", 15, 2)

aveo_car.show()
ferrari_car.show()
first_plane.show()
second_plane.show()
first_boat.show()
second_boat.show()