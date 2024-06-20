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

    hero = Character("Hero", 100, 20, 50)  # Added mana attribute
    potion = Item("Health Potion", 30)
    sword = Equipment("Iron Sword", 10, 'weapon')
    fireball = Ability("Fireball", 10, 20)
    hero.learn_ability(fireball)
    hero.inventory.add_item(potion)
    hero.equipment.equip(sword)
    hero.inventory.add_item(Gold(100))

    create_adventures(hero)

    ui = UI(screen)
    menu = Menu(ui, hero)

    running = True
    while running:
        action = explore_town(hero, menu)
        if action == "quit_game":
            running = False
        elif action == "continue_adventure":
            continue_adventure(hero, ui)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()