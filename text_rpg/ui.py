import pygame
from pygame.locals import MOUSEBUTTONDOWN

from text_rpg import enemy


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.background_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.menu_text_color = (0, 43, 51)
        self.health_color = (255, 0, 0)
        self.mana_color = (0, 0, 255)
        self.gold_color = (255, 215, 0)
        self.options_menu_open = False
        self.load_assets()

    def load_assets(self):
        self.background_image = pygame.image.load('../assets/background.png').convert()
        self.health_icon = pygame.image.load('../assets/health_icon.png').convert_alpha()
        self.mana_icon = pygame.image.load('../assets/mana_icon.png').convert_alpha()
        self.gold_icon = pygame.image.load('../assets/gold_icon.png').convert_alpha()
        self.enemy_images = {
            "Wolf": pygame.transform.scale(pygame.image.load('../assets/wolf.png').convert_alpha(), (150, 150)),
            "Goblin": pygame.transform.scale(pygame.image.load('../assets/goblin.png').convert_alpha(), (150, 150)),
            "Goblin King": pygame.transform.scale(pygame.image.load('../assets/goblin_king.png').convert_alpha(),
                                                  (150, 150)),
            # Add more enemy images as needed
        }

    def wrap_text(self, text, max_width):
        words = text.split(' ')
        lines = []
        current_line = words[0]

        for word in words[1:]:
            if self.font.size(current_line + ' ' + word)[0] <= max_width:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines

    def display_message(self, message):
        self.screen.blit(self.background_image, (0, 0))
        wrapped_lines = self.wrap_text(message, 700)
        y = 300
        for line in wrapped_lines:
            text = self.font.render(line, True, self.menu_text_color)
            self.screen.blit(text, (50, y))
            y += 40
        continue_text = self.font.render("[Press any button to continue]", True, self.menu_text_color)
        self.screen.blit(continue_text, (50, y + 20))
        pygame.display.flip()
        self.wait_for_key()

    def display_main_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        title = self.font.render("RPG Game", True, self.menu_text_color)
        self.screen.blit(title, (350, 50))
        self.display_menu_options()

    def display_menu_options(self):
        options = ["C. Continue Your Adventure", "1. Visit the shop", "2. Talk to the blacksmith",
                   "3. Talk to the healer", "4. Go to the tavern", "5. Visit the library",
                   "6. Visit the marketplace", "7. View your status", "8. Equip an item", "9. Manage inventory"]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        self.display_options_button()
        pygame.display.flip()

    def display_options_button(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (10, 10, 80, 40))
        options_text = self.small_font.render("Options", True, (0, 0, 0))
        self.screen.blit(options_text, (20, 20))

    def get_user_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit_game'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.options_menu_open = not self.options_menu_open
                        if self.options_menu_open:
                            self.display_options_menu()
                        else:
                            self.display_main_menu()
                    else:
                        return pygame.key.name(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 10 <= mouse_x <= 90 and 10 <= mouse_y <= 50:
                        self.options_menu_open = True
                        self.display_options_menu()
                        break

    def display_options_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        options = ["a. Save game", "b. Load game", "d. Quit game", "ESC. Back"]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def get_options_menu_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit_game'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.options_menu_open = False
                        self.display_main_menu()
                        break
                    else:
                        return pygame.key.name(event.key)

    def display_encounter_options(self, hero, enemy):
        self.screen.blit(self.background_image, (0, 0))
        health_status = self.font.render(
            f"Your health: {hero.health}/{hero.max_health}, {enemy.name}'s health: {enemy.health}/{enemy.max_health}",
            True, self.menu_text_color)
        mana_status = self.font.render(f"Your mana: {hero.mana}/{hero.max_mana}", True, self.menu_text_color)
        self.screen.blit(health_status, (50, 50))
        self.screen.blit(mana_status, (50, 100))

        # Display enemy image centered horizontally and adjusted vertically
        enemy_image = self.enemy_images.get(enemy.name)
        if enemy_image:
            image_x = (self.screen.get_width() - enemy_image.get_width()) // 2
            image_y = 200  # Adjust this value to move the image down
            self.screen.blit(enemy_image, (image_x, image_y))

        options = ["(A)ttack", "(H)eal", "Use (F)ireball", "(R)un", "(S)tatus"]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30

        pygame.display.flip()

    def get_encounter_input(self, enemy):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit_game'
                if event.type == pygame.KEYDOWN:
                    print(f"Key pressed: {pygame.key.name(event.key)}")  # Debug print
                    if event.key == pygame.K_a:
                        return 'a'
                    elif event.key == pygame.K_h:
                        return 'h'
                    elif event.key == pygame.K_f:
                        return 'f'
                    elif event.key == pygame.K_r:
                        return 'r'
                    elif event.key == pygame.K_s:
                        return 'status'
                    elif event.key == pygame.K_ESCAPE:
                        return 'quit_game'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (500 <= mouse_x <= 500 + self.enemy_images[enemy.name].get_width() and
                            50 <= mouse_y <= 50 + self.enemy_images[enemy.name].get_height()):
                        return 'enemy_hover'

    def display_tooltip(self, enemy):
        tooltip_text = f"{enemy.name} (Level: {enemy.level})\nHP: {enemy.health}/{enemy.max_health}\nAttack: {enemy.attack_power}"
        wrapped_lines = self.wrap_text(tooltip_text, 200)
        y = 400  # Position the tooltip below the enemy image
        for line in wrapped_lines:
            text = self.small_font.render(line, True, self.menu_text_color)
            self.screen.blit(text, (500, y))
            y += 20
        pygame.display.flip()

    def display_combat_info(self, attacker, defender, damage, effect=None):
        self.screen.blit(self.background_image, (0, 0))
        info = f"{attacker.name} attacks {defender.name} for {damage} damage"
        if effect:
            info += f" and causes {effect}!"  #  effect.name
        text = self.font.render(info, True, self.menu_text_color)
        self.screen.blit(text, (50, 300))
        pygame.display.flip()
        self.wait_for_key()  # Ensure this method waits for the player's key press before continuing

    def display_heal_info(self, hero, healing_amount):
        message = f"{hero.name} heals for {healing_amount} HP."
        self.display_message(message)

    def display_no_health_potions(self):
        message = "You have no health potions left!"
        self.display_message(message)

    def display_heal_attempt_full_health_info(self):
        message = "You are already at full health!"
        self.display_message(message)

    def display_confirmation(self, message):
        self.screen.blit(self.background_image, (0, 0))
        wrapped_lines = self.wrap_text(message, 700)
        y = 250
        for line in wrapped_lines:
            text = self.font.render(line, True, self.menu_text_color)
            self.screen.blit(text, (50, y))
            y += 40
        options = ["(Y)es", "(N)o"]
        y += 20
        for option in options:
            option_text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(option_text, (100, y))
            y += 50
        pygame.display.flip()

    def get_confirmation_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit_game'
                if event.type == pygame.KEYDOWN:
                    print(f"Key pressed: {pygame.key.name(event.key)}")  # Debug print
                    if event.key == pygame.K_y:
                        return 'yes'
                    elif event.key == pygame.K_n:
                        return 'no'
                    elif event.key == pygame.K_ESCAPE:
                        return 'quit_game'

    def display_shop_menu(self, hero):
        self.screen.blit(self.background_image, (0, 0))
        shopkeeper = self.font.render("Shopkeeper: 'Hello! How can I help you today?'", True, self.menu_text_color)
        self.screen.blit(shopkeeper, (100, 50))
        gold_status = self.font.render(f"Your Gold: {hero.inventory.gold}", True, self.menu_text_color)
        self.screen.blit(gold_status, (100, 100))
        self.screen.blit(self.gold_icon, (70, 100))
        options = [
            "1. Buy a Health Potion (10 gold)",
            "2. Buy an Iron Sword (50 gold)",
            "3. Buy an Iron Shield (40 gold)",
            "4. Buy Iron Armor (60 gold)",
            "5. Leave the shop"
        ]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_purchase_message(self, item):
        message = self.font.render(f"You bought a {item}.", True, self.menu_text_color)
        self.screen.blit(message, (100, 500))
        pygame.display.flip()

    def display_inventory_menu(self, hero):
        self.screen.blit(self.background_image, (0, 0))
        inventory = self.font.render("Inventory Management", True, self.menu_text_color)
        self.screen.blit(inventory, (100, 50))
        options = [
            "1. View inventory",
            "2. Use item",
            "3. Discard item",
            "4. Sell item",
            "5. Upgrade item",
            "6. Go back"
        ]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_inventory(self, hero):
        self.screen.blit(self.background_image, (0, 0))
        title = self.font.render("Inventory", True, self.menu_text_color)
        self.screen.blit(title, (350, 50))
        y = 100
        if not hero.inventory.items:
            no_items = self.small_font.render("No items in inventory.", True, self.menu_text_color)
            self.screen.blit(no_items, (100, y))
        else:
            for item in hero.inventory.items:
                item_text = self.small_font.render(f"- {item.name} (Effect: {item.effect})", True, self.menu_text_color)
                self.screen.blit(item_text, (100, y))
                y += 30
        pygame.display.flip()
        self.wait_for_key()

    def display_status(self, hero):
        self.screen.blit(self.background_image, (0, 0))
        status = [
            f"Character: {hero.name}",
            f"Health: {hero.health}/{hero.max_health}",
            f"Mana: {hero.mana}/{hero.max_mana}",
            f"Attack Power: {hero.attack_power}",
            f"Gold: {hero.inventory.gold}",
            "Inventory:"
        ]
        y = 50
        for line in status:
            if "Health" in line:
                color = self.health_color
            elif "Mana" in line:
                color = self.mana_color
            elif "Gold" in line:
                color = self.gold_color
            else:
                color = self.text_color
            text = self.font.render(line, True, color)
            self.screen.blit(text, (50, y))
            y += 30

        for item in hero.inventory.items:
            item_text = self.small_font.render(f"- {item.name} (Effect: {item.effect})", True, self.menu_text_color)
            self.screen.blit(item_text, (100, y))
            y += 20

        self.screen.blit(self.font.render("Equipped:", True, self.menu_text_color), (50, y))
        y += 30
        for slot, item in hero.equipment.slots.items():
            if item:
                item_text = self.small_font.render(f"- {slot.capitalize()}: {item.name} (Effect: {item.effect})", True, self.menu_text_color)
            else:
                item_text = self.small_font.render(f"- {slot.capitalize()}: None", True, self.menu_text_color)
            self.screen.blit(item_text, (100, y))
            y += 20

        if hero.abilities:
            self.screen.blit(self.font.render("Abilities:", True, self.menu_text_color), (50, y))
            y += 30
            for ability in hero.abilities:
                if ability.effect:
                    ability_text = self.small_font.render(f"- {ability.name}: {ability.effect.name} (Mana cost: {ability.mana_cost})", True, self.menu_text_color)
                else:
                    ability_text = self.small_font.render(f"- {ability.name} (Mana cost: {ability.mana_cost})", True, self.menu_text_color)
                self.screen.blit(ability_text, (100, y))
                y += 20

        pygame.display.flip()
        self.wait_for_key()

    def get_item_name(self):
        self.screen.blit(self.background_image, (0, 0))
        prompt_text = self.font.render("Enter the item name:", True, self.menu_text_color)
        self.screen.blit(prompt_text, (50, 50))
        pygame.display.flip()

        item_name = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return item_name
                    elif event.key == pygame.K_BACKSPACE:
                        item_name = item_name[:-1]
                    else:
                        item_name += event.unicode

                    # Clear the input area
                    self.screen.fill(self.background_color, (50, 100, 700, 50))
                    # Display the current item name being typed
                    input_text = self.font.render(item_name, True, self.menu_text_color)
                    self.screen.blit(input_text, (50, 100))
                    pygame.display.flip()

    def display_quest_log(self, hero):
        self.screen.blit(self.background_image, (0, 0))
        title = self.font.render("Quest Log", True, self.menu_text_color)
        self.screen.blit(title, (350, 50))
        y = 100
        for quest in hero.quests:
            status = "Completed" if quest.completed else "Active"
            quest_text = self.small_font.render(f"{quest.name}: {status} - {quest.description}", True,
                                                self.menu_text_color)
            self.screen.blit(quest_text, (50, y))
            y += 30
        pygame.display.flip()
        self.wait_for_key()

    def display_quest_completion(self, quest_name, description, reward):
        self.screen.blit(self.background_image, (0, 0))
        title = self.font.render(f"Quest Completed: {quest_name}", True, self.menu_text_color)
        self.screen.blit(title, (50, 50))
        y = 100
        description_lines = self.wrap_text(description, 700)
        for line in description_lines:
            text = self.small_font.render(line, True, self.menu_text_color)
            self.screen.blit(text, (50, y))
            y += 30
        reward_text = self.font.render(f"Reward: {reward.amount} gold", True, self.menu_text_color)
        self.screen.blit(reward_text, (50, y + 20))
        pygame.display.flip()
        self.wait_for_key()

    def display_dungeon_completion(self, dungeon_name, description, reward):
        self.screen.blit(self.background_image, (0, 0))
        title = self.font.render(f"Dungeon Completed: {dungeon_name}", True, self.menu_text_color)
        self.screen.blit(title, (50, 50))
        y = 100
        description_lines = self.wrap_text(description, 700)
        for line in description_lines:
            text = self.small_font.render(line, True, self.menu_text_color)
            self.screen.blit(text, (50, y))
            y += 30
        reward_text = self.font.render(f"Reward: {reward} gold", True, self.menu_text_color)
        self.screen.blit(reward_text, (50, y + 20))
        pygame.display.flip()
        self.wait_for_key()

    def display_map(self, hero):
        self.screen.blit(self.background_image, (0, 0))
        title = self.font.render("Map", True, self.menu_text_color)
        self.screen.blit(title, (350, 50))
        y = 100
        locations = [
            "1. Town",
            "2. Forest",
            "3. Dungeon",
        ]
        for location in locations:
            location_text = self.font.render(location, True, self.menu_text_color)
            self.screen.blit(location_text, (50, y))
            y += 30
        pygame.display.flip()
        self.wait_for_key()

    def get_map_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit_game'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 'town'
                    elif event.key == pygame.K_2:
                        return 'forest'
                    elif event.key == pygame.K_3:
                        return 'dungeon'
                    elif event.key == pygame.K_ESCAPE:
                        return 'quit_game'

    def display_blacksmith_message(self):
        self.display_message("Blacksmith: 'Hello there! I can upgrade your weapons and armor.'")

    def display_healer_message(self):
        self.display_message("Healer: 'I can heal your wounds for a small fee.'")

    def display_full_health_message(self):
        self.display_message("Healer: 'You are already at full health!'")

    def display_barkeeper_message(self):
        self.display_message("Barkeeper: 'Welcome! What can I do for you?'")

    def display_tavern_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        tavern = self.font.render("Tavern", True, self.menu_text_color)
        self.screen.blit(tavern, (100, 50))
        options = [
            "1. Talk to the barkeeper",
            "2. Listen to traveler stories",
            "3. Engage in arm wrestling",
            "4. Go back"
        ]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_library_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        library = self.font.render("Library", True, self.menu_text_color)
        self.screen.blit(library, (100, 50))
        options = [
            "1. Learn about the town history",
            "2. Research spells",
            "3. Study local wildlife",
            "4. Go back"
        ]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_marketplace_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        marketplace = self.font.render("Marketplace", True, self.menu_text_color)
        self.screen.blit(marketplace, (100, 50))
        options = [
            "1. Buy a Rare Herb (20 gold)",
            "2. Buy a Magical Trinket (50 gold)",
            "3. Chat with a merchant",
            "4. Go back"
        ]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.menu_text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_traveler_stories(self):
        self.display_message("Traveler: 'I have seen many things in my journeys.'")

    def display_merchant_chat(self):
        self.display_message("Merchant: 'I have the finest goods in town.'")

    def display_arm_wrestling(self):
        self.display_message("You engage in an arm wrestling match and win 20 gold!")

    def display_town_history(self):
        self.display_message("The town has a rich history dating back to the ancient times.")

    def display_learn_spell(self, spell_name):
        self.display_message(f"You have learned the spell: {spell_name}.")

    def display_wildlife_research(self):
        self.display_message("You study the local wildlife and learn about various creatures.")

    def wait_for_key(self):
        print("DEBUG: Waiting for key press...")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"DEBUG: Key pressed: {pygame.key.name(event.key)}")
                    return

    # ... other methods ...

