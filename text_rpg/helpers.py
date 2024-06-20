def has_killed_wolves(player):
    return player.killed_wolves >= 3

def has_found_rare_herb(player):
    return any(item.name == "Rare Herb" for item in player.inventory.items)
