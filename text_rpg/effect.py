class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    #def apply(self, target):
    #    pass

class Burn(Effect):
    def __init__(self):
        super().__init__("Burn", 3)
        self.damage_per_turn = 2

    def apply(self, target):
        print(f"DEBUG: {target.name} is burning for {self.damage_per_turn} damage per turn.")
        target.health -= self.damage_per_turn


    def tick(self, target):
        print(f"DEBUG: Burn effect deals {self.damage_per_turn} damage to {target.name}")
        target.health -= self.damage_per_turn
        self.duration -= 1
        if self.duration <= 0:
            target.active_effect = None
            print(f"DEBUG: Burn effect on {target.name} has ended")