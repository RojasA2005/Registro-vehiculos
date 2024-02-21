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
    def __init__(self, brand, year, gasoline, kilometers, price=0, concessionaire=""):
        Vehicle.__init__(self, brand, year, gasoline)
        self.kilometers = kilometers
        self.seller = Seller(price, concessionaire)
    def show(self):
        print("It's a car!")
        Vehicle.show(self)
        print("It has run {} kilometers".format(self.kilometers))

class Seller:
    def __init__(self, price=0, concessionaire=""):
        self.price = price
        self.concessionaire = concessionaire
        self.sold = False
    def sell_car(self, money):
        if self.sold == True:
            return "Sorry, car not available"
        if money >= self.price:
             self.sold = True
             return "The car is yours!"
        return "Insufficient funds :("
    def change_price(self, new_price):
        self.price = new_price
    def change_concessionaire(self, new_location):
        self.concessionaire = new_location
    def show(self):
        if self.sold == False:
            print("The price is {}".format(self.price))
            print("You can buy it in {}".format(self.concessionaire))
        else:
            print("Not available")

ferrari_car = Car("Ferrari", 2023, 120, 50000, 23000, "Costa Automotriz")
aveo_car = Car("Aveo", 2015, 30, 63890)

#Probando funciones
ferrari_car.seller.show()
ferrari_car.seller.change_price(50000)
ferrari_car.seller.show
#Vendiendo el carro
print(ferrari_car.seller.sell_car(65000))
ferrari_car.seller.show()

#Segundo carro, añadiendo valores
aveo_car.seller.change_price(35000)
aveo_car.seller.change_concessionaire("Jac Tersa")
print(aveo_car.seller.sell_car(10000))
aveo_car.seller.show()