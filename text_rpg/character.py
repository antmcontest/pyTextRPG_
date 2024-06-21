from equipment import Equipment
from inventory import Inventory

class Character:
    def __init__(self, name, health, attack_power, defense, mana):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.max_mana = mana
        self.mana = mana
        self.inventory = Inventory()
        self.equipment = Equipment()
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.abilities = []
        self.quests = []
        self.active_effect = None
        self.effect_duration = 0
        self.killed_wolves = 0

    def attack(self, other):
        total_attack_power = self.attack_power + self.equipment.get_total_attack_power()
        other.health -= total_attack_power
        print(f"{self.name} attacks {other.name} for {total_attack_power} damage")
        if other.health <= 0:
            print(f"{other.name} has been defeated!")
            self.gain_experience(50)
        else:
            print(f"{other.name}'s remaining health: {other.health}")

    def use_ability(self, ability_name, target):
        ability = next((a for a in self.abilities if a.name == ability_name), None)
        if ability and self.mana >= ability.mana_cost:
            ability.use(self, target)
            self.mana -= ability.mana_cost
        else:
            print(f"Not enough mana to use {ability_name}")

    def learn_ability(self, ability):
        self.abilities.append(ability)
        print(f"{self.name} has learned {ability.name}!")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points.")
        if self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.experience_to_next_level *= 1.5
        self.max_health += 20
        self.health = self.max_health
        self.attack_power += 5
        self.max_mana += 10
        self.mana = self.max_mana
        print(f"{self.name} has leveled up to level {self.level}!")

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} heals for {amount} health. Current health: {self.health}/{self.max_health}")

    def equip_item(self, item_name):
        item = self.inventory.get_item(item_name)
        if item and isinstance(item, Equipment):
            self.equipment.equip(item)
            self.inventory.remove_item(item_name)
            print(f"{item.name} equipped.")
        else:
            print(f"{item_name} not found or is not equipment.")

    def show_status(self):
        print(f"Character: {self.name}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Mana: {self.mana}/{self.max_mana}")
        print(f"Attack Power: {self.attack_power}")
        print("Inventory:")
        for item in self.inventory.items:
            print(f"  - {item.name} (Effect: {item.effect})")
        print(f"Gold: {self.inventory.gold}")
        print("Equipped:")
        for slot, item in self.equipment.slots.items():
            if item:
                print(f"  - {slot.capitalize()}: {item.name} (Effect: {item.effect})")
            else:
                print(f"  - {slot.capitalize()}: None")

    def show_quest_log(self):
        print("Quest Log:")
        for quest in self.quests:
            status = "Completed" if quest.completed else "Active"
            print(f"- {quest.name}: {status} - {quest.description}")

    def is_alive(self):
        return self.health > 0

    def set_location(self, location):
        self.location = location
        print(f"Moved to {location.name}.")
