from text_rpg.enemy import Enemy
from text_rpg.item import Gold, Loot
from text_rpg.helpers import has_killed_wolves, has_found_rare_herb
from text_rpg.combat import encounter_wolves, encounter_enemy

class Adventure:
    def __init__(self, name, description, completion_check, reward):
        self.name = name
        self.description = description
        self.completion_check = completion_check
        self.reward = reward
        self.is_completed = False

    def check_completion(self, hero, ui):
        self.is_completed = self.completion_check(hero)
        if self.is_completed:
            ui.display_quest_completion(self.name, self.description, self.reward)

    def start(self, hero, ui):
        raise NotImplementedError("This method should be overridden in subclasses")

class Quest(Adventure):
    def start(self, hero, ui):
        print(f"Starting quest: {self.name}")
        if self.name == "Kill Wolves":
            wolf_template = Enemy("Wolf", 50, 10, [Loot("Wolf Fur"), Loot("Wolf Bones")], level=1)
            encounter_wolves(hero, wolf_template, self, ui)
        self.check_completion(hero, ui)

class Dungeon(Adventure):
    def start(self, hero, ui):
        print(f"Starting dungeon: {self.name}")
        enemies = [Enemy("Goblin", 30, 5, [Loot("Goblin Ear")], level=2) for _ in range(5)]
        boss = Enemy("Goblin King", 100, 15, [Loot("Goblin Crown")], level=5)
        for enemy in enemies:
            if hero.is_alive():
                encounter_enemy(hero, enemy, ui)
        if hero.is_alive():
            encounter_enemy(hero, boss, ui)
        self.check_completion(hero, ui)
        if self.is_completed:
            hero.inventory.add_gold(self.reward.amount)
            print(f"\nYou have completed the dungeon and earned {self.reward.amount} gold!")
            ui.display_dungeon_completion(self.name, self.description, self.reward)


def create_adventures(hero):
    kill_wolves_quest = Quest("Kill Wolves", "Help the town by killing 3 wolves.", has_killed_wolves, Gold(100))
    find_herb_quest = Quest("Find Rare Herb", "Find a rare herb in the forest for the healer.", has_found_rare_herb, Gold(50))
    dungeon_quest = Dungeon("Find Ancient Artifact", "Retrieve an ancient artifact from the old ruins.", lambda hero: hero.found_artifact, Gold(200))
    hero.adventures = [kill_wolves_quest, find_herb_quest, dungeon_quest]
    hero.killed_wolves = 0
    hero.found_artifact = False

def continue_adventure(hero, ui):
    for adventure in hero.adventures:
        if not adventure.is_completed:
            adventure.start(hero, ui)
            return
    print("You have completed all available adventures.")
