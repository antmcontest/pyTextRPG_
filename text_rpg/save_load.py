import pickle

def save_game(hero, filename='savegame.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(hero, f)
    print("Game saved successfully.")

def load_game(filename='savegame.pkl'):
    try:
        with open(filename, 'rb') as f:
            hero = pickle.load(f)
        print("Game loaded successfully.")
        return hero
    except FileNotFoundError:
        print("No save file found.")
        return None
