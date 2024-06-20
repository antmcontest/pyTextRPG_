class Enemy:
    def __init__(self, name, health, attack_power, loot, level=1):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.loot = loot
        self.level = level

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage")
        if other.health <= 0:
            print(f"{other.name} has been defeated!")
        else:
            print(f"{other.name}'s remaining health: {other.health}")

    def is_alive(self):
        return self.health > 0

    def drop_loot(self):
        return self.loot


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 30, 5, [Loot("Goblin Ear")], level=2)

class GoblinKing(Enemy):
    def __init__(self):
        super().__init__("Goblin King", 100, 15, [Loot("Goblin Crown")], level=5)

