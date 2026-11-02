class Battle:
    def __init__(self, hero: "Character", enemy: "Character"):
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
    def simulate_battle(self):

        round_count = 1
        while self.enemy.is_alive and self.hero.is_alive:
            self.play_round()
            round +=  1
        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"Battle ended after {round_count - 1} rounds. Winner: {winner.name}!")
        return winner