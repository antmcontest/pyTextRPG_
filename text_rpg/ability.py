from effect import Burn

class Ability:
    def __init__(self, name, mana_cost, damage, effect=None):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.effect = effect

    def use(self, user, target):
        target.health -= self.damage
        print(f"DEBUG: {user.name} uses {self.name} on {target.name} for {self.damage} damage")
        if self.effect:
            self.effect.apply(target)
            target.active_effect = self.effect
            target.effect_duration = self.effect.duration
            print(f"DEBUG: {user.name} applies {self.effect.name} to {target.name} for {self.effect.duration} turns")
        if target.health <= 0:
            print(f"DEBUG: {target.name} has been defeated!")

class Fireball(Ability):
    def __init__(self):
        super().__init__("Fireball", 10, 15, Burn())

    def use(self, caster, target):
        if caster.mana >= self.mana_cost:
            caster.mana -= self.mana_cost
            target.health -= self.damage
            if self.effect:
                self.effect.apply(target)
                target.active_effect = self.effect
                target.effect_duration = self.effect.duration
                print(f"DEBUG: {caster.name} hits {target.name} with Fireball for {self.damage} damage and applies burn!")
        else:
            print(f"DEBUG: {caster.name} does not have enough mana to cast Fireball")



#class Fireball:
#    def __init__(self):
#        self.name = "Fireball"
#        self.mana_cost = 10
#        self.damage = 15
#        self.effect = Burn()  # Apply Burn effect

