from text_rpg.save_load import save_game, load_game
from text_rpg.item import Item, Equipment
from text_rpg.helpers import has_killed_wolves, has_found_rare_herb
from text_rpg.effect import Effect
from text_rpg.ability import Ability

class Menu:
    def __init__(self, ui, hero):
        self.ui = ui
        self.hero = hero

    def display_menu(self):
        self.ui.display_main_menu()
        choice = self.ui.get_user_input()
        if choice == '1':
            self.visit_shop()
        elif choice == '2':
            self.talk_to_blacksmith()
        elif choice == '3':
            self.talk_to_healer()
        elif choice == '4':
            self.visit_tavern()
        elif choice == '5':
            self.visit_library()
        elif choice == '6':
            self.visit_marketplace()
        elif choice == '7':
            self.ui.display_status(self.hero)
        elif choice == '8':
            self.equip_item()
        elif choice == '9':
            self.manage_inventory()
        elif choice == '10':
            save_game(self.hero)
        elif choice == '11':
            loaded_hero = load_game()
            if loaded_hero:
                self.hero = loaded_hero
        elif choice == '12':
            return "continue_adventure"
        elif choice == '13':
            return "quit_game"
        else:
            self.ui.display_invalid_choice()

    def visit_shop(self):
        while True:
            self.ui.display_shop_menu(self.hero)
            choice = self.ui.get_user_input()
            if choice == '1':
                self.buy_item("Health Potion", 10, Item("Health Potion", 30))
            elif choice == '2':
                self.buy_item("Iron Sword", 50, Equipment("Iron Sword", 10, 'weapon'))
            elif choice == '3':
                self.buy_item("Iron Shield", 40, Equipment("Iron Shield", 5, 'shield'))
            elif choice == '4':
                self.buy_item("Iron Armor", 60, Equipment("Iron Armor", 15, 'armor'))
            elif choice == '5':
                break
            else:
                self.ui.display_invalid_choice()
        self.display_menu()

    def buy_item(self, item_name, cost, item):
        self.ui.display_confirmation(f"Do you want to buy a {item_name} for {cost} gold?")
        confirmation = self.ui.get_confirmation_input()
        if confirmation == 'yes':
            if self.hero.inventory.spend_gold(cost):
                self.hero.inventory.add_item(item)
                self.ui.display_purchase_message(item_name)
            else:
                self.ui.display_message("Not enough gold.")
        elif confirmation == 'no':
            self.ui.display_message("Purchase canceled.")

    def manage_inventory(self):
        while True:
            self.ui.display_inventory_menu(self.hero)
            choice = self.ui.get_user_input()
            if choice == '1':
                self.ui.display_inventory(self.hero)
            elif choice == '2':
                item_name = self.ui.get_item_name()
                self.hero.inventory.use_item(item_name, self.hero)
            elif choice == '3':
                item_name = self.ui.get_item_name()
                self.hero.inventory.remove_item(item_name)
            elif choice == '4':
                item_name = self.ui.get_item_name()
                self.sell_item(item_name)
            elif choice == '5':
                item_name = self.ui.get_item_name()
                self.upgrade_item(item_name)
            elif choice == '6':
                break
            else:
                self.ui.display_invalid_choice()
        self.display_menu()

    def sell_item(self, item_name):
        item = self.hero.inventory.get_item(item_name)
        if item:
            self.ui.display_confirmation(f"Do you want to sell {item_name} for 10 gold?")
            confirmation = self.ui.get_confirmation_input()
            if confirmation == 'yes':
                self.hero.inventory.remove_item(item_name)
                self.hero.inventory.add_gold(10)
                self.ui.display_message(f"You sold {item_name} for 10 gold.")
            elif confirmation == 'no':
                self.ui.display_message("Sale canceled.")
        else:
            self.ui.display_message(f"{item_name} not found in inventory.")

    def upgrade_item(self, item_name):
        item = self.hero.inventory.get_item(item_name)
        if item and isinstance(item, Equipment):
            self.ui.display_confirmation(f"Do you want to upgrade {item_name} for 20 gold?")
            confirmation = self.ui.get_confirmation_input()
            if confirmation == 'yes':
                if self.hero.inventory.spend_gold(20):
                    item.upgrade()
                    self.ui.display_message(f"You upgraded {item_name}.")
                else:
                    self.ui.display_message("Not enough gold.")
            elif confirmation == 'no':
                self.ui.display_message("Upgrade canceled.")
        else:
            self.ui.display_message(f"{item_name} not found in inventory or not upgradable.")

    def talk_to_blacksmith(self):
        self.ui.display_blacksmith_message()
        self.display_menu()

    def talk_to_healer(self):
        self.ui.display_healer_message()
        if self.hero.health < self.hero.max_health:
            self.hero.heal(20)
        else:
            self.ui.display_full_health_message()
        self.display_menu()

    def visit_tavern(self):
        while True:
            self.ui.display_tavern_menu()
            choice = self.ui.get_user_input()
            if choice == '1':
                self.ui.display_barkeeper_message()
                self.check_start_dungeon()
            elif choice == '2':
                self.ui.display_traveler_stories()
            elif choice == '3':
                self.ui.display_arm_wrestling()
                self.hero.inventory.add_gold(20)
                break
            elif choice == '4':
                break
            else:
                self.ui.display_invalid_choice()
        self.display_menu()

    def check_start_dungeon(self):
        if has_killed_wolves(self.hero) and has_found_rare_herb(self.hero):
            self.ui.display_message("Barkeeper: 'I've heard rumors of a dungeon nearby with a powerful artifact. Would you like to explore it?'")
            confirmation = self.ui.get_confirmation_input()
            if confirmation == 'yes':
                self.hero.found_artifact = True
                print("Dungeon quest started!")
            else:
                self.ui.display_message("Maybe another time, then.")

    def visit_library(self):
        while True:
            self.ui.display_library_menu()
            choice = self.ui.get_user_input()
            if choice == '1':
                self.ui.display_town_history()
            elif choice == '2':
                fireball_effect = Effect("Burn", 3, lambda target: setattr(target, 'health', target.health - 5))
                fireball = Ability("Fireball", 30, fireball_effect)
                self.hero.learn_ability(fireball)
                self.ui.display_learn_spell("Fireball")
            elif choice == '3':
                self.ui.display_wildlife_research()
            elif choice == '4':
                break
            else:
                self.ui.display_invalid_choice()
        self.display_menu()

    def visit_marketplace(self):
        while True:
            self.ui.display_marketplace_menu()
            choice = self.ui.get_user_input()
            if choice == '1':
                self.buy_item("Rare Herb", 20, Item("Rare Herb", 0))
            elif choice == '2':
                self.buy_item("Magical Trinket", 50, Item("Magical Trinket", 0))
            elif choice == '3':
                self.ui.display_merchant_chat()
            elif choice == '4':
                break
            else:
                self.ui.display_invalid_choice()
        self.display_menu()

    def equip_item(self):
        self.ui.display_status(self.hero)
        item_name = self.ui.get_item_name()
        self.hero.equip_item(item_name)
        self.display_menu()
