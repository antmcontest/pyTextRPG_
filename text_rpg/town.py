import pygame

from save_load import save_game, load_game
from item import Item, Equipment, Gold
from ability import Ability
from effect import Effect
from text_rpg.menu import Menu
from text_rpg.ui import UI


def explore_town(hero, menu):
    while True:
        action = menu.display_menu()
        if action == "quit_game":
            return "quit_game"
        elif action == "continue_adventure":
            return "continue_adventure"
