import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.background_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.highlight_color = (100, 100, 255)

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
        self.screen.fill(self.background_color)
        wrapped_lines = self.wrap_text(message, 700)
        y = 300
        for line in wrapped_lines:
            text = self.font.render(line, True, self.text_color)
            self.screen.blit(text, (50, y))
            y += 40
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_main_menu(self):
        self.screen.fill(self.background_color)
        title = self.font.render("RPG Game", True, self.text_color)
        self.screen.blit(title, (350, 50))
        self.display_menu_options()

    def display_menu_options(self):
        options = ["1. Visit the shop", "2. Talk to the blacksmith", "3. Talk to the healer",
                   "4. Go to the tavern", "5. Visit the library", "6. Visit the marketplace",
                   "7. View your status", "8. Equip an item", "9. Manage inventory",
                   "a. Save game", "b. Load game", "c. Continue adventuring", "d. Quit game"]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def get_user_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit_game'
                if event.type == pygame.KEYDOWN:
                    print(f"Key pressed: {pygame.key.name(event.key)}")  # Debug print
                    if event.key == pygame.K_1:
                        return '1'
                    elif event.key == pygame.K_2:
                        return '2'
                    elif event.key == pygame.K_3:
                        return '3'
                    elif event.key == pygame.K_4:
                        return '4'
                    elif event.key == pygame.K_5:
                        return '5'
                    elif event.key == pygame.K_6:
                        return '6'
                    elif event.key == pygame.K_7:
                        return '7'
                    elif event.key == pygame.K_8:
                        return '8'
                    elif event.key == pygame.K_9:
                        return '9'
                    elif event.key == pygame.K_a:
                        return '10'
                    elif event.key == pygame.K_b:
                        return '11'
                    elif event.key == pygame.K_c:
                        return '12'
                    elif event.key == pygame.K_d:
                        return '13'
                    elif event.key == pygame.K_ESCAPE:
                        return 'quit_game'

    def display_encounter_options(self, hero, enemy):
        self.screen.fill(self.background_color)
        health_status = self.font.render(f"Your health: {hero.health}, {enemy.name}'s health: {enemy.health}", True, self.text_color)
        mana_status = self.font.render(f"Your mana: {hero.mana}/{hero.max_mana}", True, self.text_color)
        self.screen.blit(health_status, (50, 50))
        self.screen.blit(mana_status, (50, 100))

        options = ["(A)ttack", "(H)eal", "Use (F)ireball", "(R)un"]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def get_encounter_input(self):
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
                    elif event.key == pygame.K_ESCAPE:
                        return 'quit_game'

    def display_confirmation(self, message):
        self.screen.fill(self.background_color)
        wrapped_lines = self.wrap_text(message, 700)
        y = 250
        for line in wrapped_lines:
            text = self.font.render(line, True, self.text_color)
            self.screen.blit(text, (50, y))
            y += 40
        options = ["(Y)es", "(N)o"]
        y += 20
        for option in options:
            option_text = self.font.render(option, True, self.text_color)
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
        self.screen.fill(self.background_color)
        shopkeeper = self.font.render("Shopkeeper: 'Hello! How can I help you today?'", True, self.text_color)
        self.screen.blit(shopkeeper, (100, 50))
        gold_status = self.font.render(f"Your Gold: {hero.inventory.gold}", True, self.text_color)
        self.screen.blit(gold_status, (100, 100))
        options = [
            "1. Buy a Health Potion (10 gold)",
            "2. Buy a Sword (50 gold)",
            "3. Buy a Shield (40 gold)",
            "4. Buy an Armor (60 gold)",
            "5. Leave the shop"
        ]
        y = 150
        for option in options:
            text = self.font.render(option, True, self.text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_purchase_message(self, item):
        message = self.font.render(f"You bought a {item}.", True, self.text_color)
        self.screen.blit(message, (100, 500))
        pygame.display.flip()

    def display_inventory_menu(self, hero):
        self.screen.fill(self.background_color)
        inventory = self.font.render("Inventory Management", True, self.text_color)
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
            text = self.font.render(option, True, self.text_color)
            self.screen.blit(text, (100, y))
            y += 30
        pygame.display.flip()

    def display_inventory(self, hero):
        self.screen.fill(self.background_color)
        title = self.font.render("Inventory", True, self.text_color)
        self.screen.blit(title, (350, 50))
        y = 100
        if not hero.inventory.items:
            no_items = self.small_font.render("No items in inventory.", True, self.text_color)
            self.screen.blit(no_items, (100, y))
        else:
            for item in hero.inventory.items:
                item_text = self.small_font.render(f"- {item.name} (Effect: {item.effect})", True, self.text_color)
                self.screen.blit(item_text, (100, y))
                y += 30
        pygame.display.flip()
        pygame.time.wait(3000)

    def display_status(self, hero):
        self.screen.fill(self.background_color)
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
            text = self.font.render(line, True, self.text_color)
            self.screen.blit(text, (50, y))
            y += 30

        for item in hero.inventory.items:
            item_text = self.small_font.render(f"- {item.name} (Effect: {item.effect})", True, self.text_color)
            self.screen.blit(item_text, (100, y))
            y += 20

        self.screen.blit(self.font.render("Equipped:", True, self.text_color), (50, y))
        y += 30
        for slot, item in hero.equipment.slots.items():
            if item:
                item_text = self.small_font.render(f"- {slot.capitalize()}: {item.name} (Effect: {item.effect})", True, self.text_color)
            else:
                item_text = self.small_font.render(f"- {slot.capitalize()}: None", True, self.text_color)
            self.screen.blit(item_text, (100, y))
            y += 20

        if hero.abilities:
            self.screen.blit(self.font.render("Abilities:", True, self.text_color), (50, y))
            y += 30
            for ability in hero.abilities:
                if ability.effect:
                    ability_text = self.small_font.render(f"- {ability.name}: {ability.effect.name} (Mana cost: {ability.mana_cost})", True, self.text_color)
                else:
                    ability_text = self.small_font.render(f"- {ability.name} (Mana cost: {ability.mana_cost})", True, self.text_color)
                self.screen.blit(ability_text, (100, y))
                y += 20

        pygame.display.flip()
        pygame.time.wait(3000)

    def display_quest_completion(self, quest_name, description, reward):
        self.screen.fill(self.background_color)
        title = self.font.render(f"Quest Completed: {quest_name}", True, self.text_color)
        self.screen.blit(title, (50, 50))
        y = 100
        description_lines = self.wrap_text(description, 700)
        for line in description_lines:
            text = self.small_font.render(line, True, self.text_color)
            self.screen.blit(text, (50, y))
            y += 30
        reward_text = self.font.render(f"Reward: {reward.amount} gold", True, self.text_color)
        self.screen.blit(reward_text, (50, y + 20))
        pygame.display.flip()
        pygame.time.wait(3000)

    def display_dungeon_completion(self, dungeon_name, description, reward):
        self.screen.fill(self.background_color)
        title = self.font.render(f"Dungeon Completed: {dungeon_name}", True, self.text_color)
        self.screen.blit(title, (50, 50))
        y = 100
        description_lines = self.wrap_text(description, 700)
        for line in description_lines:
            text = self.small_font.render(line, True, self.text_color)
            self.screen.blit(text, (50, y))
            y += 30
        reward_text = self.font.render(f"Reward: {reward.amount} gold", True, self.text_color)
        self.screen.blit(reward_text, (50, y + 20))
        pygame.display.flip()
        pygame.time.wait(3000)

    # ... other methods ...