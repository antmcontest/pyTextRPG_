from quest import Quest
from character import Character
from enemy import Enemy
from item import Item, Equipment, Gold, Loot
from save_load import save_game, load_game

def explore_town(hero):
    while True:
        print(f"\nYou explore the town and meet various villagers. You have {hero.inventory.gold} gold.")
        print("1. Visit the shop")
        print("2. Talk to the blacksmith")
        print("3. Talk to the healer")
        print("4. Go to the tavern")
        print("5. Check your status")
        print("6. Equip an item")
        print("7. Save game")
        print("8. Load game")
        print("9. Go back to the town square")

        choice = input("What do you want to do? (1/2/3/4/5/6/7/8/9): ").lower()
        if choice == '1':
            visit_shop(hero)
        elif choice == '2':
            talk_to_blacksmith(hero)
        elif choice == '3':
            talk_to_healer(hero)
        elif choice == '4':
            visit_tavern(hero)
        elif choice == '5':
            hero.show_status()
        elif choice == '6':
            equip_item(hero)
        elif choice == '7':
            save_game(hero)
        elif choice == '8':
            loaded_hero = load_game()
            if loaded_hero:
                hero = loaded_hero
        elif choice == '9':
            return
        else:
            print("Invalid choice. Please choose again.")

def visit_shop(hero):
    while True:
        print(f"\nYou enter the shop. The shopkeeper greets you warmly. You have {hero.inventory.gold} gold.")
        print("Shopkeeper: 'Hello! How can I help you today?'")
        print("1. Buy a Health Potion (10 gold)")
        print("2. Buy a Sword (50 gold)")
        print("3. Buy a Shield (40 gold)")
        print("4. Buy an Armor (60 gold)")
        print("5. Leave the shop")

        choice = input("What do you want to do? (1/2/3/4/5): ").lower()
        if choice == '1':
            if hero.inventory.spend_gold(10):
                hero.inventory.add_item(Item("Health Potion", 30))
                print("You bought a Health Potion.")
        elif choice == '2':
            if hero.inventory.spend_gold(50):
                item = Equipment("Iron Sword", 10)
                hero.inventory.add_item(item, hero)
                print("You bought and equipped an Iron Sword.")
        elif choice == '3':
            if hero.inventory.spend_gold(40):
                item = Equipment("Iron Shield", 5)
                hero.inventory.add_item(item, hero)
                print("You bought and equipped an Iron Shield.")
        elif choice == '4':
            if hero.inventory.spend_gold(60):
                item = Equipment("Iron Armor", 15)
                hero.inventory.add_item(item, hero)
                print("You bought and equipped an Iron Armor.")
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please choose again.")

def talk_to_blacksmith(hero):
    print("\nYou talk to the blacksmith. He tells you about the history of the town.")
    print("Blacksmith: 'This town used to be peaceful until the wolves started attacking.'")
    print("Blacksmith: 'If you need weapons or armor, come see me.'")

def talk_to_healer(hero):
    print("\nYou talk to the healer. She offers to heal your wounds.")
    print("Healer: 'You look weary from your travels. Let me heal you.'")
    if hero.health < hero.max_health:
        hero.heal(20)
    else:
        print("Healer: 'You are already at full health.'")

def visit_tavern(hero):
    print("\nYou enter the tavern and find a lively atmosphere with people drinking and sharing stories.")
    print("1. Talk to the barkeeper")
    print("2. Listen to the stories of other travelers")
    print("3. Challenge someone to an arm-wrestling match")
    print("4. Leave the tavern")

    choice = input("What do you want to do? (1/2/3/4): ").lower()
    if choice == '1':
        print("Barkeeper: 'Hello, traveler! What can I get you?'")
        print("1. Buy a drink (5 gold)")
        print("2. Ask about local rumors")
        choice = input("What do you want to do? (1/2): ").lower()
        if choice == '1':
            if hero.inventory.spend_gold(5):
                print("You bought a drink. It refreshes you.")
                hero.heal(10)
        elif choice == '2':
            print("Barkeeper: 'They say there's a hidden treasure in the forest, but it's guarded by a fearsome beast.'")
        else:
            print("Invalid choice.")
    elif choice == '2':
        print("You listen to the stories of other travelers and learn about hidden places and secrets in the town.")
    elif choice == '3':
        print("You challenge a burly man to an arm-wrestling match. After a tense struggle, you win and earn 20 gold.")
        hero.inventory.add_gold(20)
    elif choice == '4':
        return
    else:
        print("Invalid choice. Please choose again.")

def equip_item(hero):
    hero.show_status()
    item_name = input("\nEnter the name of the item you want to equip: ").strip()
    hero.equip_item(item_name)

def has_killed_wolves(player):
    return player.killed_wolves >= 3

def main():
    # Create characters and items
    hero = Character("Hero", 100, 20)
    wolf_template = Enemy("Wolf", 50, 10, [Loot("Wolf Fur"), Loot("Wolf Bones")])
    potion = Item("Health Potion", 30)
    sword = Equipment("Iron Sword", 10)
    hero.inventory.add_item(potion)
    hero.equipment.equip(sword)
    hero.inventory.add_item(Gold(100))  # Add initial gold

    # Sample quest
    kill_wolves_quest = Quest("Kill Wolves", "Help the town by killing 3 wolves.", has_killed_wolves, Gold(100))
    hero.quests = [kill_wolves_quest]
    hero.killed_wolves = 0

    # Debug: Verify sword is equipped
    print("Current Equipment:")
    print(hero.equipment.slots)

    # Introduction and choices
    print("You are wandering through the forest when you stumble upon the town of Willowbrook.")
    print("A townsperson approaches you.")
    print("'Greetings, traveler! We need your help. \n"
          "Wolves have been attacking our chicken coop and killing our chickens. Will you help us?'")

    choice = input("Do you want to help? (yes/no): ").lower()
    if choice == 'no':
        print("You decide not to help the town of Willowbrook. The adventure ends here.")
        return
    else:
        print("You agree to help the town of Willowbrook.")
        print("\nThe townsperson smiles and leads you to the chicken coop.")
        print("'Be careful,' they warn. 'The wolves are vicious.'")

    # Explore the town
    explore_town(hero)

    # Encounter with the wolves
    print("\nYou head towards the chicken coop and encounter a pack of wolves!")

    # Combat sequence with multiple wolves
    for _ in range(3):
        wolf = Enemy("Wolf", wolf_template.health, wolf_template.attack_power, wolf_template.loot)
        while wolf.is_alive() and hero.is_alive():
            print(f"\nYour health: {hero.health}, Wolf's health: {wolf.health}")
            action = input("Do you want to (A)ttack, (H)eal, or (R)un? ").lower()

            if action == 'a':
                hero.attack(wolf)
                if wolf.is_alive():
                    wolf.attack(hero)
                else:
                    hero.killed_wolves += 1
            elif action == 'h':
                hero.inventory.use_item("Health Potion", hero)
                if wolf.is_alive():
                    wolf.attack(hero)
            elif action == 'r':
                print("You try to run, but the wolf blocks your path!")
                wolf.attack(hero)
            else:
                print("Invalid action. Please choose again.")

            # Check if the hero is still alive
            if not hero.is_alive():
                break

    if hero.is_alive():
        print("\nYou have defeated the wolves!")
        for _ in range(3):
            for item in wolf_template.loot:
                hero.inventory.add_item(item)
        print("You take the items and return to the town.")
        hero.quests[0].check_completion(hero)  # Check quest completion and reward
       # if not hero.quests[0].is_completed:
       #     hero.quests[0].is_completed = True
        #    print("\nThe townspeople are grateful and reward you with 100 gold coins!")
        #    print("You can use the gold coins at various shops in the town.")
    else:
        print("\nYou have been defeated by the wolves. The adventure ends here.")

if __name__ == "__main__":
    main()
