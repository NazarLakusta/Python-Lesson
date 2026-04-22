class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def move(self):
        print(f"{self.brand} рухаэться")

class Car(Vehicle):
    def __init__(self,brand,fuel):
        super().__init__(brand)
        self.fuel = fuel

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 10
            self.move()
            print(f"Паливо: {self.fuel}")
        else:
            print("Немаэ пального")

    def refuel(self,amount):
        self.fuel += amount
        print(f"Заправлено +{amount}. Паливо: {self.fuel}")

class Bike(Vehicle):
    def __init__(self,brand,bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def ride(self):
        print(f"{self.brand} ({self.bike_type}) Їде по дорозі")


car = Car("Toyota",50)
bike = Bike("Giant","mountaint")

car.move()
bike.move()

car.drive()
car.drive()
car.drive()
car.refuel(30)
car.drive()

bike.ride()