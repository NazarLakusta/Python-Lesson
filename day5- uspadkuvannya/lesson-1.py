# батьківський клас
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("Їсть")
        
    def speak(self):
        print("я тваринка")


#  дочірний клас
class Dog(Animal):
    def speak(self):
        print("гав-гав")

    def fetch(self):
        print(f"{self.name} приносить мяч")

class Cat(Animal):
    def speak(self):
        print("Мяу")

dog = Dog("Бобік")

print(dog.name)
dog.speak()
dog.fetch()

cat = Cat("Барсік")
print(cat.name)
cat.speak()