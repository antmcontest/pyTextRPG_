class Ability:
    def __init__(self, name, damage, effect=None):
        self.name = name
        self.damage = damage
        self.effect = effect

    def use(self, user, target):
        target.health -= self.damage
        print(f"{user.name} uses {self.name} on {target.name} for {self.damage} damage")
        if self.effect:
            self.effect.apply(target)

class Effect:
    def __init__(self, name, duration, apply_effect):
        self.name = name
        self.duration = duration
        self.apply_effect = apply_effect

    def apply(self, target):
        self.apply_effect(target)
        print(f"{target.name} is affected by {self.name} for {self.duration} turns")
