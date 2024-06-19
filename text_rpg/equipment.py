class Equipment:
    def __init__(self):
        self.slots = {"weapon": None, "armor": None, "shield": None}

    def equip(self, item):
        if item.effect > 0:
            if "sword" in item.name.lower() or "dagger" in item.name.lower():
                if not self.slots["weapon"] or self.slots["weapon"].effect < item.effect:
                    self.slots["weapon"] = item
                    print(f"{item.name} equipped as weapon.")
            elif "armor" in item.name.lower():
                if not self.slots["armor"] or self.slots["armor"].effect < item.effect:
                    self.slots["armor"] = item
                    print(f"{item.name} equipped as armor.")
            elif "shield" in item.name.lower():
                if not self.slots["shield"] or self.slots["shield"].effect < item.effect:
                    self.slots["shield"] = item
                    print(f"{item.name} equipped as shield.")
            else:
                print(f"Cannot equip {item.name}: Not recognized as weapon, armor, or shield.")

    def get_total_attack_power(self):
        return sum(item.effect for item in self.slots.values() if item is not None)

    def get_total_defense(self):
        return sum(item.effect for item in self.slots.values() if item is not None and "shield" in item.name.lower())
