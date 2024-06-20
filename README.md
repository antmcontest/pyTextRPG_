# Text RPG Game

Welcome to the Text RPG Game! This is a role-playing game where you can explore a town, complete quests, battle enemies, and manage your character's inventory and abilities. The game features a simple text-based interface using Pygame.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Explore different areas such as the shop, blacksmith, healer, tavern, library, and marketplace.
- Engage in combat with various enemies, including wolves and goblins.
- Complete quests and receive rewards.
- Manage your inventory and equipment.
- Level up your character and unlock new abilities.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/text-rpg-game.git
    cd text-rpg-game
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the game, run the following command:

```bash
python text_rpg/main.py
```

## Controls

- **1-9, a-d**: Navigate through the menu options.
- **a**: Attack during combat.
- **h**: Heal during combat.
- **f**: Use Fireball ability during combat.
- **r**: Run during combat.
- **ESC**: Quit the game.

## File Structure

text_rpg/

├── __init__.py

├── ability.py

├── character.py

├── combat.py

├── enemy.py

├── equipment.py

├── helpers.py

├── inventory.py

├── item.py

├── main.py

├── menu.py

├── quest.py

├── save_load.py

├── town.py

└── ui.py


## Contributing

Contributions are welcome! If you have suggestions for improvements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

