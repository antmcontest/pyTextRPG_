class Enemy:
    def __init__(self, name, health, attack_power, defense, loot, level=1):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.loot = loot
        self.level = level
        self.active_effect = None
        self.effect_duration = 0

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

    def use_ability(self, target):
        if self.ability:
            self.ability.use(self, target)

class Wolf(Enemy):
    def __init__(self):
        super().__init__("Wolf", 50, 10, 1,  [Loot("Wolf Fur"), Loot("Wolf Bones")], level=1)


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 30, 5, 2,  [Loot("Goblin Ear")], level=2)

class GoblinKing(Enemy):
    def __init__(self):
        super().__init__("Goblin King", 100, 15, 5,  [Loot("Goblin Crown")], level=5)

