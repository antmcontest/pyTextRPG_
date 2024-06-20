class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, target):
        target.heal(self.effect)
        print(f"{self.name} used on {target.name}. Healed for {self.effect} health.")

class Equipment(Item):
    def __init__(self, name, effect, equipment_type):
        super().__init__(name, effect)
        self.type = equipment_type

class Gold(Item):
    def __init__(self, amount):
        super().__init__("Gold", amount)
        self.amount = amount


class Loot(Item):
    def __init__(self, name):
        super().__init__(name, 0)