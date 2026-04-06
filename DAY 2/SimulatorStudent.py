from random import *
class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I Will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest Time")
        self.gladness +=2
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out..")
            self.alive = False

        elif self.gladness <=0:
            print("Depression")
            self.alive = False

        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness is {self.gladness}")
        print(f"Progress is {self.progress}")


    def live(self,day):
        print(f"day is {day}")
        live_cube = randint(1,3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

max_student = Student("Max")

for day in range(365):
    if max_student.alive == False:
        break
    else:
        max_student.live(day)


