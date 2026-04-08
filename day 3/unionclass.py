class Human:
    def __init__(self,name):
        self.name = name


class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []


    def add_passenger(self,passenger):
        self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Names of {self.brand}")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print("No passengers")

kate = Human("Kate")
nick = Human("Nick")

car = Auto("Mercedes")

car.add_passenger(kate)
car.add_passenger(nick)

car.print_passengers()

