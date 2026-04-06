def printhi():
    print("hi")

class Student:

    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print()

    def grow(self):
        print("Grow")
        self.age+=1
        self.height+=2

first_student = Student("Nazar",22,178)
first_student.print_info()
first_student.grow()
first_student.print_info()

second_student = Student("Vasia",25,182)
second_student.print_info()

