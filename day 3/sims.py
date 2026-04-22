from random import *

class Human:
    def __init__(self,name, job=None, home=None, car=None):
        self.name = name

        self.money = 100
        self.gladness = 50
        self.satiety = 50

        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return

        self.job = Job(job_list)


    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety +=5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
                return
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100

        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50

        elif manage == "delicacies":
            print("Hooraayy! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50


    def days_index(self,day):
       print("\n\n-------------------------------------------")
       print(f"Day: {day}")
       print(f"{self.name}")

       print(f"Money - {self.money}")
       print(f"Satiety - {self.satiety}")
       print(f"Gladness - {self.gladness}")
       print(f"Food - {self.home.food}")
       print(f"Mess - {self.home.mess}")
       print(f"Fuel - {self.car.fuel}")
       print(f"Strenth - {self.car.strength}")

       print("-------------------------------------------")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        elif self.satiety < 0 :
            print("Dead ...")
            return False
        elif self.money < -500:
            print("Bankrupt...")
            return False

    def live(self,day):

         if self.is_alive() == False:
             return False

         if self.home is None:
             print("Settled in the house")
             self.get_home()

         if self.car is None:
             self.get_car()
             print(f"I bouth a car {self.car.brand}")

         if self.job is None:
             self.get_job()
             print(f"I dont have a job, goint to get a job {self.job.job} with salary {self.job.salary}")

         self.days_index(day)

         dice = randint(1,4)

         if self.satiety < 20:
             print("I'll go eat")
             self.eat()
         elif self.gladness < 20:
             if self.home.mess > 15:
                 print("I want to chill, but there is so mess")
                 self.clean_home()
             else:
                print("Lets chill")
                self.chill
         elif self.money < 0:
             print("Start working")
             self.work()
         elif self.car.strength < 15:
             print("I need to repair my car")
             self.to_repair()

         elif dice == 1:
             print("Lets chill")
             self.chill()

         elif dice == 2:
             print("Start Working")
             self.work()

         elif dice == 3:
              print("Cleaning Time!!")
              self.clean_home()

         elif dice == 4:
             print("Time to treats")
             self.shopping(manage="delicacies")



class Auto:
    def __init__(self,brand_list):
        self.brand = choice(list(brand_list))
        self.strength = brand_list[self.brand]["strength"]
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            if self.brand == "BMW":
                self.strength -= 2
            elif self.brand == "Lada":
                self.strength -= 4
            elif self.brand == "Volvo":
                self.strength -= 1
            elif self.brand == "Ferrari":
                self.strength -= 1
            return True

        else:
            print("The car cannot move")
            return False


class Job:
    def __init__(self,job_list):
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

brands_of_car = {
    "BMW":{"fuel":100,"strength":100, "consumption":8},
    "Lada":{"fuel":50,"strength":40, "consumption":10},
    "Volvo":{"fuel":70,"strength":150, "consumption":8},
    "Ferrari":{"fuel":80,"strength":120, "consumption":14}
}

job_list = {
    "Java developer":{"salary":50,"gladness_less" : 10},
    "Python developer":{"salary":40,"gladness_less" : 3},
    "C++ developer":{"salary":45,"gladness_less" : 25},
    "Ruby":{"salary":70,"gladness_less" : 1},
}


nick = Human("Nick")

for day in range(1,365):
    if nick.live(day) == False:
        break