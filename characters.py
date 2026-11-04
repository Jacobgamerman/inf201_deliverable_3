
# Task 1,3, and 4
from items import Weapon


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
        """
        Reduce the character's hit points by the specified damage amount.

        Ensures HP does not drop below 0.

        Parameters
        ----------
        damage : int
            The amount of damage to deduct from the character's HP.
        """
        self._hp = max(0, self._hp - damage)

    def heal(self, multiplier:float= 0.1)  ->  None:
        """
        Heal the character by a percentage of their maximum hit points.

        Healing only occurs if the character is alive, and health cannot exceed hp_max.

        Parameters
        ----------
        multiplier : float, optional
            The proportion of hp_max to restore (default is 0.1, or 10%).
        """
        if self.is_alive:
            self._hp = round(min(self._hp + self.hp_max  *  multiplier, self.hp_max))
    
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    @property
    def  is_alive(self) -> bool:
        """
        Check whether the character is currently alive.

        Returns
        -------
        bool
            True if _hp is strictly greater than 0, False otherwise.
        """
        return self._hp > 0



class Warrior(Character):
    """
    A specialized defensive subclass of Character with added armor.
    """

    def __init__(self, name: str, hp_max: int = 120, damage: int = 15, armor: int = 5, weapon: Weapon = None) -> None:
        """
        Initializes a Warrior instance.

        Parameters:
        ----------
        name : str
            The name of the warrior.
        hp_max : int, optional
            Max hit points (default is 120).
        damage : int, optional
            Base attack damage (default is 15).
        armor : int, optional
            Armor value that reduces incoming damage (default is 5).
        weapon : Weapon, optional
            Equipped weapon (default is None).
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """
        Overrides take_damage to reduce incoming damage by the armor value before applying it.

        Parameters:
        ----------
        amount : int
            The raw incoming damage.
        """
        reduced_damage = max(amount - self.armor, 0)
        super().take_damage(reduced_damage)


class Mage(Character):
    """
    A specialized resource-based attacker subclass of Character utilizing mana for spellcasting.
    """

    def __init__(self, name: str, hp_max: int = 80, damage: int = 10, mana: int = 30, mana_max: int = 30, weapon: Weapon = None) -> None:
        """
        Initializes a Mage instance.

        Parameters:
        ----------
        name : str
            The name of the mage.
        hp_max : int, optional
            Max hit points (default is 80).
        damage : int, optional
            Base attack damage (default is 10).
        mana : int, optional
            Current mana pool (default is 30).
        mana_max : int, optional
            Maximum mana pool (default is 30).
        weapon : Weapon, optional
            Equipped weapon (default is None).
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: "Character") -> None:
        """
        Overrides attack to perform a high-damage spell if sufficient mana is available,
        otherwise falls back to a base attack and restores mana.

        Parameters:
        ----------
        target : Character
            The character object being attacked.
        """
        if self.mana >= 10:
            # Spend mana and deal double damage via a spell (ignoring weapons)
            self.mana -= 10
            spell_damage = self.damage * 2
            target.take_damage(spell_damage)
        else:
            # Fall back to base attack using equipment, and restore 5 mana
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)