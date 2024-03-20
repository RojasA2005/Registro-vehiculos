class Vehicle:
    def __init__(self, brand, year, gasoline, warranty):
        self.brand = brand
        self.year = year
        self.gasoline = gasoline
        self.warranty = warranty
    def show(self):
        print("Brand is: {}".format(self.brand))
        print("Year is: {}".format(self.year))
        print("It has {} liters of gas left".format(self.gasoline))

class Car(Vehicle):
    def __init__(self, brand, year, gasoline, warranty, kilometers, price=0, concessionaire=""):
        Vehicle.__init__(self, brand, year, gasoline, warranty)
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

ferrari_car = Car("Ferrari", 2023, 120, 20, 50000, 23000, "Costa Automotriz")
aveo_car = Car("Aveo", 2015, 30, 12, 63890)
Volksvagen_car = Car("Volksvagen", 1985, 45, 3, 180560)
Ford_car = Car("Ford", 2000, 50, 5, 230985)
Tesla_car = Car("Tesla", 2019, 50, 10, 10000)
Hellcat_car = Car("Hellcat", 2020, 70, 25, 10000)

car_list = [[ferrari_car, ferrari_car.warranty], [aveo_car, aveo_car.warranty], [Volksvagen_car, Volksvagen_car.warranty], [Ford_car, Ford_car.warranty], [Tesla_car, Tesla_car.warranty], [Hellcat_car, Hellcat_car.warranty]]


def bubble_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        for j in range(0, n-i):
            if my_list[j][1] > my_list[j+1][1]:
                aux = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = aux

def mergeSort(my_list):
    if len(my_list) > 1:
        mid = len(my_list)//2
        L = my_list[:mid]
        R = my_list[mid:]
 
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][1] >= R[j][1]:
                my_list[k] = L[i]
                i += 1
            else:
                my_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            my_list[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            my_list[k] = R[j]
            j += 1
            k += 1

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while j >= 0 and temp[1] < my_list[j][1]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = temp

def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if my_list[min_idx][1] > my_list[j][1]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

print("""¿Comó desea organizar la lista?
1. Bubble sort
2. Insertion sort
3. Selection sort
4. Merge sort""")
answer = input("")
if answer == "1":
    bubble_sort(car_list)
    for car in car_list:
        car[0].show()
    print(car_list)
elif answer == "2":
    insertion_sort(car_list)
    for car in car_list:
        car[0].show()
    print(car_list)
elif answer == "3":
    selection_sort(car_list)
    for car in car_list:
        car[0].show()
    print(car_list)
elif answer == "4":
    mergeSort(car_list)
    for car in car_list:
        car[0].show()
    print(car_list)
else:
    print("Selección inválida")