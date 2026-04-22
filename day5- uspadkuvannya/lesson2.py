class Character:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def info(self):
        print(f"{self.name} має {self.hp} HP.")

class Warrior(Character):
    def __init__(self,name,hp, damage):
        super().__init__(name,hp)
        self.damage = damage

    def attack(self):
        print(f"{self.name} атакуэ на {self.damage} шкоди.")


w = Warrior("Warrior",50,25)
w.info()
w.attack()