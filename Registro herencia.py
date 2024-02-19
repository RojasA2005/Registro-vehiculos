class Vehicle:
    def __init__(self, brand, year, gasoline):
        self.brand = brand
        self.year = year
        self.gasoline = gasoline
    def show(self):
        print("Brand is: {}".format(self.brand))
        print("Year is: {}".format(self.year))
        print("It has {} liters of gas left".format(self.gasoline))

class Car(Vehicle):
    def __init__(self, brand, year, gasoline, kilometers):
        Vehicle.__init__(self, brand, year, gasoline)
        self.kilometers = kilometers
    def show(self):
        print("It's a car!")
        Vehicle.show(self)
        print("It has run {} kilometers".format(self.kilometers))

class Plane(Vehicle):
    def __init__(self, brand, year, gasoline, flights):
        Vehicle.__init__(self, brand, year, gasoline)
        self.flights = flights
    def show(self):
        print("It's a plane!")
        Vehicle.show(self)
        print("It has had {} flights".format(self.flights))

class Boat(Vehicle):
    def __init__(self, brand, year, gasoline, size, speed, capacity):
        Vehicle.__init__(self, brand, year, gasoline)
        self.size = size
        self.speed = speed
        self.capacity = capacity
    def show(self):
        print("It's a boat!")
        Vehicle.show(self)
        print("It's a {} size boat".format(self.size))
        print("It can go up to {} miles per hour".format(self.speed))
        print("It can hold up to {} people".format(self.capacity))


ferrari_car = Car("Ferrari", 2023, 120, 50000)
aveo_car = Car("Aveo", 2015, 30, 63890)
first_plane = Plane("Boeing", 2017, 500, 12)
second_plane = Plane("Lockheed Martin", 1998, 432, 310)
first_boat = Boat("Chaparral Steel", 2020, 300, "medium", 50, 20)
second_boat = Boat("Boston Whaler", 2023, 250, "small", 15, 2)

aveo_car.show()
ferrari_car.show()
first_plane.show()
second_plane.show()
first_boat.show()
second_boat.show()