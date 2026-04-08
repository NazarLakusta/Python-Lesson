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
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self,manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_index(self,day):
        pass

    def is_alive(self):
        pass

    def live(self,day):
        pass


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


class Home:
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