import random

from text_rpg.ability import Fireball
from text_rpg.enemy import Enemy
from item import HealthPotion

def combat_loop(ui, hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        ui.display_encounter_options(hero, enemy)
        action = ui.get_encounter_input(enemy)

        if action in ['a', 'f', 'h']:
            handle_combat_turn(ui, hero, enemy, action)
            print(f"DEBUG: {hero.name} chose action: {action}")

        elif action == 'r':
            print("DEBUG: You run away!")
            break

        elif action == 'status':
            ui.display_status(hero)
            print("DEBUG: Displaying hero status")
            continue  # Return to combat options after displaying status

        elif action == 'enemy_hover':
            ui.display_tooltip(enemy)
            print("DEBUG: Displaying enemy tooltip")
            continue  # Return to combat options after displaying tooltip

        if not hero.is_alive():
            print(f"DEBUG: You have been defeated by the {enemy.name}.")
            break


def determine_attack_order(hero, enemy):
    # Randomly choose who attacks first
    if random.random() < 0.5:
        return hero, enemy
    else:
        return enemy, hero


def handle_combat_turn(ui, hero, enemy, action):
    if action == 'h':
        if hero.health == hero.max_health:
            ui.display_message("You are already at full health!")
            print("DEBUG: Hero is already at full health.")
        else:
            health_potion = hero.inventory.get_item("Health Potion")
            if health_potion:
                actual_heal = hero.inventory.use_item("Health Potion", hero)
                if actual_heal > 0:
                    ui.display_combat_info(hero, hero, actual_heal, effect="heal")
                    print(f"DEBUG: {hero.name} heals for {actual_heal} HP. Current health: {hero.health}/{hero.max_health}")
                else:
                    ui.display_message("You are already at full health!")
                    print("DEBUG: Hero is already at full health.")
            else:
                ui.display_message("You are out of health potions!")
                print("DEBUG: No health potions left.")
    else:
        attacker, defender = determine_attack_order(hero, enemy)
        effect = None
        if action == 'f':
            fireball = Fireball()
            if hero.mana >= fireball.mana_cost:
                fireball.use(hero, enemy)
                damage = fireball.damage
                effect = fireball.effect
                hero.mana -= fireball.mana_cost
                print(f"DEBUG: {hero.name} uses Fireball on {enemy.name}. Mana left: {hero.mana}/{hero.max_mana}")
            else:
                ui.display_message("Not enough mana to cast Fireball!")
                print("DEBUG: Not enough mana to cast Fireball")
                return
        else:
            damage = attacker.attack_power - defender.defense
            if damage < 0:
                damage = 0

        defender.health -= damage
        print(f"DEBUG: {attacker.name} attacks {defender.name} for {damage} damage. {defender.name} health: {defender.health}/{defender.max_health}")

        if effect:
            effect.apply(defender)
            defender.active_effect = effect
            print(f"DEBUG: {attacker.name} applies {effect.name} to {defender.name}")

        ui.display_combat_info(attacker, defender, damage, effect)

        if defender.is_alive():
            damage = defender.attack_power - attacker.defense
            if damage < 0:
                damage = 0
            attacker.health -= damage
            print(f"DEBUG: {defender.name} counterattacks {attacker.name} for {damage} damage. {attacker.name} health: {attacker.health}/{attacker.max_health}")

            effect = None
            if hasattr(defender, 'active_effect') and defender.active_effect:
                effect = defender.active_effect
                defender.active_effect.apply(attacker)
                print(f"DEBUG: {defender.name} applies {effect.name} to {attacker.name}")

            ui.display_combat_info(defender, attacker, damage, effect)

    # Apply burn effect tick
    if hasattr(hero, 'active_effect') and hero.active_effect:
        hero.active_effect.tick(hero)
        if hero.active_effect and hero.active_effect.damage_per_turn:
            ui.display_combat_info(hero, hero, hero.active_effect.damage_per_turn, effect=hero.active_effect)
            print(f"DEBUG: Burn effect deals {hero.active_effect.damage_per_turn} damage to {hero.name}. {hero.name} health: {hero.health}/{hero.max_health}")
        if hero.active_effect and hero.active_effect.duration <= 0:
            hero.active_effect = None
            print("DEBUG: Burn effect on Hero has ended")

    if hasattr(enemy, 'active_effect') and enemy.active_effect:
        enemy.active_effect.tick(enemy)
        if enemy.active_effect and enemy.active_effect.damage_per_turn:
            ui.display_combat_info(enemy, enemy, enemy.active_effect.damage_per_turn, effect=enemy.active_effect)
            print(f"DEBUG: Burn effect deals {enemy.active_effect.damage_per_turn} damage to {enemy.name}. {enemy.name} health: {enemy.health}/{enemy.max_health}")
        if enemy.active_effect and enemy.active_effect.duration <= 0:
            enemy.active_effect = None
            print("DEBUG: Burn effect on Enemy has ended")

def encounter_enemy(hero, enemy, ui):
    combat_loop(ui, hero, enemy)


def encounter_wolves(hero, wolf_template, quest, ui):
    wolves = [Enemy("Wolf", wolf_template.max_health, wolf_template.attack_power, wolf_template.defense, wolf_template.loot, level=1) for _ in range(3)]
    for wolf in wolves:
        encounter_enemy(hero, wolf, ui)
        if hero.is_alive():
            hero.killed_wolves += 1

    if hero.is_alive():
        print("\nYou have defeated the wolves!")
        quest.check_completion(hero, ui)
        if quest.is_completed:
            print("\nThe townspeople are grateful and reward you with 100 gold coins!")
            hero.inventory.add_gold(100)
            print("You can use the gold coins at various shops in the town.")
    else:
        print("\nYou have been defeated by the wolves. The adventure ends here.")
