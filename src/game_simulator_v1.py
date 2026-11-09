# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: "Weapon" =  None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon =  weapon


    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            damage_dealt = self.weapon.roll_damage()
        else:
            damage_dealt  =  self.damage
        target.take_damage(damage_dealt)
        

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    def  take_damage(self, damage:  int)  -> None:
        self._hp = max(0, self._hp - damage)

    def heal(self, multiplier:float= 0.1)  ->  None:
        if self.is_alive:
            self._hp = round(min(self._hp + self.hp_max  *  multiplier, self.hp_max))
    
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    @property
    def  is_alive(self) -> bool:
        return self._hp > 0