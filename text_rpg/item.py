class Item:
    def __init__(self, name, effect=None):
        self.name = name
        self.effect = effect

    def use(self, user):
        raise NotImplementedError("Use method must be implemented in subclass.")

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion")

    def use(self, user):
        if user.health >= user.max_health:
            return 0  # No healing needed
        healing_amount = 30
        actual_heal = healing_amount
        user.health += healing_amount
        if user.health > user.max_health:
            actual_heal = healing_amount - (user.health - user.max_health)
            user.health = user.max_health
        return actual_heal

class Equipment(Item):
    def __init__(self, name, effect, equipment_type):
        super().__init__(name, effect)
        self.type = equipment_type

    def upgrade(self):  # FIXME
        pass

class Gold(Item):
    def __init__(self, amount):
        super().__init__("Gold", amount)
        self.amount = amount

class Loot(Item):
    def __init__(self, name):
        super().__init__(name, 0)