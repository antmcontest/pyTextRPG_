class Effect:
    def __init__(self, name, duration, apply_effect):
        self.name = name
        self.duration = duration
        self.apply_effect = apply_effect

    def apply(self, target):
        self.apply_effect(target)
        print(f"{target.name} is affected by {self.name} for {self.duration} turns")
