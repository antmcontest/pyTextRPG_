class Enemy:
    def __init__(self, name, health, attack_power, loot):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.loot = loot

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
