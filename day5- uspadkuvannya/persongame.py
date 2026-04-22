from os.path import isabs
from random import *

class Person:
    def __init__(self,name):
        self.name = name
        self.energy = 100
        self.alive = True

    def rest(self):
        self.energy += 25
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} відпочив. Енергія:{self.energy}")

    def status(self):
        print(f"\n{self.name}")
        print(f"Енергія:{self.energy}")

    def check_alive(self):
        if self.energy <= 0:
            self.alive = False
            print(f"{self.name} вибився з сил ... ГРА ЗАКІНЧЕНА")


class Worker(Person):
    def __init__(self,name):
        super().__init__(name)
        self.money = 0

    def work(self):
        gain = randint(10,30)
        loss = randint(15,25)

        self.money += gain
        self.energy -= loss
        print(f"{self.name}")
        print(f"Заробив: {gain}. Енергії втратив: {loss}")

    def status(self):
        super().status()
        print(f"Гроші: {self.money}")

class Hero(Person):
    def __init__(self, name):
        super().__init__(name)
        self.reputation = 0

    def save_people(self):
        gain = randint(10, 20)
        loss = randint(20, 35)

        self.reputation += gain
        self.energy -= loss

        print(f"🦸 {self.name} рятує людей!")
        print(f"+⭐ {gain} репутації  -⚡ {loss}")

        self.check_alive()

    def train(self):
        self.energy -= 15
        self.reputation += 5
        print(f"💪 {self.name} тренується (+5 репутації)")

    def status(self):
        super().status()
        print(f"⭐ Репутація: {self.reputation}")


class Police(Person):
    def __init__(self, name):
        super().__init__(name)
        self.arrests = 0

    def patrol(self):
        self.energy -= 20

        event = randint(1, 3)

        if event == 1:
            self.arrests += 1
            print(f"🚔 {self.name} затримав злочинця!")
        else:
            print(f"👮 {self.name} патрулює місто")

        self.check_alive()

    def status(self):
        super().status()
        print(f"🚨 Затримань: {self.arrests}")



def choose_character():
    print("\nОбери персонажа ")
    print("1 - Робітник ")
    print("2 - Герой ")
    print("3 - Поліцейський ")
    choice = input("Обери - ")
    name = input("Введи імя: ")

    if choice == "1":
        return Worker(name)
    elif choice == "2":
        return Hero(name)
    else:
        return Police(name)

def game_loop(player):
    day = 1

    while player.alive:
        print("\n" + "=" * 40)
        print(f"ДЕНЬ {day}")
        print("=" * 40)

        print("Дії")
        print("1 - Робота / дія класу")
        print("2 - Відпочинок")
        print("3 - Статистика")
        print("0 - Вихід")

        if isinstance(player,Worker):
            print("4 - Працювати")

        if isinstance(player,Hero):
            print("4 - Рятювати людей")
            print("5 - Тренування")

        if isinstance(player,Police):
            print("4 - Патруль")

        action = input("Обери дію: ")
        if action == "1":
            print("Обери спеціальну дію нижче")

        elif action == "2":
            player.rest()

        elif action == "3":
            player.status()

        elif action == "0":
            print("Exit")
            break

        elif action == "4":
            if isinstance(player,Worker):
                player.work()
            elif isinstance(player,Hero):
                player.save_people()
            elif isinstance(player,Police):
                player.patrol()

        elif action == "5" and isinstance(player,Hero):
            player.train()

        else:
            print("Не вірна дія")

        day += 1

        if player.energy <= 0:
            player.alive = False

    print("\n Гра завершена")


player = choose_character()
game_loop(player)