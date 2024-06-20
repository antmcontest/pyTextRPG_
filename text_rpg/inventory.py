from item import Gold, Equipment

class Inventory:
    def __init__(self):
        self.items = []
        self.gold = 0

    def add_item(self, item, hero=None):
        self.items.append(item)
        if isinstance(item, Equipment) and hero:
            self.auto_equip(item, hero)
        print(f"{item.name} added to inventory.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} removed from inventory.")
                return True
        print(f"{item_name} not found in inventory.")
        return False

    def use_item(self, item_name, target):
        for item in self.items:
            if item.name == item_name:
                if isinstance(item, Item):
                    item.use(target)
                    self.items.remove(item)
                return True
        print(f"{item_name} not found in inventory.")
        return False

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"{amount} gold spent. Remaining gold: {self.gold}")
            return True
        print("Not enough gold.")
        return False

    def add_gold(self, amount):
        self.gold += amount
        print(f"{amount} gold added to inventory. Total gold: {self.gold}")

    def auto_equip(self, item, hero):
        if isinstance(item, Equipment):
            if item.type == 'weapon' and (not hero.equipment.slots['weapon'] or hero.equipment.slots['weapon'].effect < item.effect):
                hero.equipment.equip(item)
                print(f"{item.name} equipped as weapon.")
            elif item.type == 'armor' and (not hero.equipment.slots['armor'] or hero.equipment.slots['armor'].effect < item.effect):
                hero.equipment.equip(item)
                print(f"{item.name} equipped as armor.")
            elif item.type == 'shield' and (not hero.equipment.slots['shield'] or hero.equipment.slots['shield'].effect < item.effect):
                hero.equipment.equip(item)
                print(f"{item.name} equipped as shield.")
