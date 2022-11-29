from dataclasses import dataclass

@dataclass
class Player:
    health : int
    name : str
    armor : int
    attack: int

    def take_damage(self, damage):
        # if the armor is enough
        if self.armor >= 0 and damage <= self.armor:
            self.armor -= damage
        # if the armor isn't enough
        elif self.armor >= 0 and damage > self.armor:
            self.health -= damage - self.armor
            self.armor = 0
        # if there is no 
        else:
            self.health -= damage

p1 = Player(100, "Arnaud", 10, 15)
p2 = Player(800, "Boss", 100, 10)
p1.take_damage(p2.attack)
print(p1.health)