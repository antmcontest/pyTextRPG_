from item import Gold, Equipment

class Inventory:
    def __init__(self):
        self.items = []
        self.gold = 0

    def add_item(self, item, character=None):
        if isinstance(item, Gold):
            self.add_gold(item.amount)
        else:
            self.items.append(item)
            print(f"{item.name} added to inventory.")
            if isinstance(item, Equipment) and character:
                self.auto_equip(item, character)

    def auto_equip(self, item, character):
        if "sword" in item.name.lower() or "dagger" in item.name.lower():
            if not character.equipment.slots["weapon"] or character.equipment.slots["weapon"].effect < item.effect:
                character.equipment.equip(item)
                self.items.remove(item)
                print(f"{item.name} equipped as weapon.")
        elif "armor" in item.name.lower():
            if not character.equipment.slots["armor"] or character.equipment.slots["armor"].effect < item.effect:
                character.equipment.equip(item)
                self.items.remove(item)
                print(f"{item.name} equipped as armor.")
        elif "shield" in item.name.lower():
            if not character.equipment.slots["shield"] or character.equipment.slots["shield"].effect < item.effect:
                character.equipment.equip(item)
                self.items.remove(item)
                print(f"{item.name} equipped as shield.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{amount} gold added to inventory. Total gold: {self.gold}")

    def use_item(self, item_name, character):
        for item in self.items:
            if item.name == item_name:
                if isinstance(item, Equipment):
                    character.equip_item(item_name)
                else:
                    character.heal(item.effect)
                    self.items.remove(item)
                    print(f"{item.name} used.")
                return
        print(f"{item_name} not found in inventory.")

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"{amount} gold spent. Remaining gold: {self.gold}")
            return True
        else:
            print("Not enough gold.")
            return False

    def show_inventory(self):
        print("Inventory:")
        for item in self.items:
            print(f"  - {item.name} (Effect: {item.effect})")
        print(f"Total Gold: {self.gold}")
