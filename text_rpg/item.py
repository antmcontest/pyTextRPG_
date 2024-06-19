class Item:
    def __init__(self, name, effect=0):
        self.name = name
        self.effect = effect

class Loot(Item):
    def __init__(self, name):
        super().__init__(name, 0)

class Equipment(Item):
    def __init__(self, name, effect):
        super().__init__(name, effect)
        self.equipped = False

class Gold(Item):
    def __init__(self, amount):
        super().__init__("Gold", 0)
        self.amount = amount