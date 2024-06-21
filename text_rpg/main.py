import pygame

from text_rpg.ability import Ability
from text_rpg.character import Character
from text_rpg.enemy import Enemy
from text_rpg.item import Item, Equipment, Gold, Loot
from text_rpg.town import explore_town
from text_rpg.save_load import save_game, load_game
from text_rpg.ui import UI
from text_rpg.menu import Menu
from text_rpg.quest import create_adventures, continue_adventure


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('RPG Game')

    hero = Character("Hero", 100, 20, 5, 50)  # Added mana attribute
    potion = Item("Health Potion", 30)
    sword = Equipment("Iron Sword", 10, 'weapon')
    fireball = Ability("Fireball", 10, 20)
    hero.learn_ability(fireball)
    hero.inventory.add_item(potion)
    hero.equipment.equip(sword)
    hero.inventory.add_item(Gold(100))
    print(f"Screen size: {screen.get_width()}x{screen.get_height()} pixels")

    create_adventures(hero)

    ui = UI(screen)
    menu = Menu(ui, hero)

    running = True
    while running:
        if ui.options_menu_open:
            action = ui.get_options_menu_input()
            if action == 'a':
                print("Save game")
            elif action == 'b':
                print("Load game")
            elif action == 'd':
                running = False
        else:
            ui.display_main_menu()
            action = ui.get_user_input()
            if action == '1':
                print("Visit the shop")
                menu.visit_shop()
            elif action == '2':
                print("Talk to the blacksmith")
                menu.talk_to_blacksmith()
            elif action == '3':
                print("Talk to the healer")
                menu.talk_to_healer()
            elif action == '4':
                print("Go to the tavern")
                menu.visit_tavern()
            elif action == '5':
                print("Visit the library")
                menu.visit_library()
            elif action == '6':
                print("Visit the marketplace")
                menu.visit_marketplace()
            elif action == '7':
                print("View your status")
                ui.display_status(hero)
            elif action == '8':
                print("Equip an item")
                menu.equip_item()
            elif action == '9':
                print("Manage inventory")
                menu.manage_inventory()
            elif action == 'c':
                print("Continue adventuring")
                continue_adventure(hero, ui)
            elif action == 'quit_game':
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()