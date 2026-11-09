class Battle:
    """
    Manages turn-based combat simulations between two Character objects.
    """
    def __init__(self, hero: "Character", enemy: "Character")->None:
        """
        Initialize the battle simulation with two combatants.

        Parameters
        ----------
        hero : Character
            The primary character who takes the first turn in each combat round.
        enemy : Character
            The opposing character who counter-attacks if they survive.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self)->None:
        """
        Execute a single combat round.

        The hero attacks the enemy first. If the enemy survives (is_alive evaluates
        to True), the enemy executes a counter-attack against the hero.
        """
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
    def simulate_battle(self)->"Character":
        """
        Simulate rounds of combat in a loop until one combatant is defeated.

        Runs repeated rounds while both combatants are alive, prints the summary
        of the battle outcome, and returns the surviving Character.

        Returns
        -------
        Character
            The victorious Character instance that survived the battle.
        """
        round_count = 1
        while self.enemy.is_alive and self.hero.is_alive:
            self.play_round()
            round_count +=  1
        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"Battle ended after {round_count - 1} rounds. Winner: {winner.name} with {winner._hp}hp!")
        return winner
