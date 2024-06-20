class Ability:
    def __init__(self, name, mana_cost, damage, effect=None):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.effect = effect

    def use(self, user, target):
        target.health -= self.damage
        print(f"{user.name} uses {self.name} on {target.name} for {self.damage} damage")
        if self.effect:
            self.effect.apply(target)
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

