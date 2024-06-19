class Quest:
    def __init__(self, name, description, objective, reward):
        self.name = name
        self.description = description
        self.objective = objective
        self.reward = reward
        self.is_completed = False

    def check_completion(self, player):
        if not self.is_completed and self.objective(player):
            self.is_completed = True
            player.inventory.add_item(self.reward)
            print(f"Quest '{self.name}' completed! You received {self.reward.amount} gold.")
