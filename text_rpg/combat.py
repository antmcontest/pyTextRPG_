from text_rpg.enemy import Enemy

def encounter_enemy(hero, enemy, ui):
    while enemy.is_alive() and hero.is_alive():
        ui.display_encounter_options(hero, enemy)
        action = ui.get_encounter_input()

        if action == 'a':
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
        elif action == 'h':
            hero.inventory.use_item("Health Potion", hero)
            if enemy.is_alive():
                enemy.attack(hero)
        elif action == 'f':
            hero.use_ability("Fireball", enemy)
            if enemy.is_alive():
                enemy.attack(hero)
        elif action == 'r':
            print("You try to run, but the enemy blocks your path!")
            enemy.attack(hero)
        else:
            print("Invalid action. Please choose again.")

        if not hero.is_alive():
            break

    if hero.is_alive():
        print(f"\nYou have defeated the {enemy.name}!")
        for item in enemy.drop_loot():
            hero.inventory.add_item(item)
    else:
        print("\nYou have been defeated by the {enemy.name}. The adventure ends here.")

def encounter_wolves(hero, wolf_template, quest, ui):
    wolves = [Enemy("Wolf", wolf_template.max_health, wolf_template.attack_power, wolf_template.loot, level=1) for _ in range(3)]
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
