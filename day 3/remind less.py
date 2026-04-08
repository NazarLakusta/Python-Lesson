class Human:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def info(self):
        print(self.name)
        print(self.age)
        print(self.score)

human1 = Human("Alex",45,90)
human1.info()

human2 = Human("Mary",45,90)