
# Task 4

from items import Weapon

class Character:
    """
    Represents a base character in the RPG game.
    """

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None) -> None:
        """
        Initializes the Character instance.

        Parameters:
        ----------
        name : str
            The name of the character.
        hp_max : int, optional
            The maximum hit points (default is 100).
        damage : int, optional
            The default base damage dealt when attacking (default is 10).
        weapon : Weapon, optional
            An equipped weapon object used for damage calculations (default is None).
        """
        self.name = name
        self._hp = hp_max  # Protected attribute for hit points
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP safely."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property that returns True if HP is greater than 0, False otherwise."""
        return self._hp > 0

    def take_damage(self, amount: int) -> None:
        """
        Reduces the character's HP by the specified amount, ensuring it doesn't drop below 0.

        Parameters:
        ----------
        amount : int
            The amount of damage taken.
        """
        self._hp -= amount
        self._hp = max(self._hp, 0)

    def heal(self, amount: int) -> None:
        """
        Increases the character's HP by the specified amount, up to hp_max.

        Parameters:
        ----------
        amount : int
            The amount of healing applied.
        """
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target: "Character") -> None:
        """
        Attacks a target character, dealing damage using an equipped weapon or base damage.

        Parameters:
        ----------
        target : Character
            The character object being attacked.
        """
        if self.weapon is not None:
            dealt_damage = self.weapon.roll_damage()
        else:
            dealt_damage = self.damage

        target.take_damage(dealt_damage)

    def introduce(self) -> None:
        """Prints an introduction string for the character."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Returns the official string representation of the Character."""
        return f"<Character name={self.name} hp={self._hp} damage={self.damage}>"


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


# Funcionality test for Warrior and Mage classes
if __name__ == "__main__":
    warrior = Warrior(name="Thor")
    mage = Mage(name="Merlin")
    print("Testing Warrior and Mage classes:")
    print(warrior)
    print(mage)
            
    # Test a mage attack
    mage.attack(warrior)
    print(f"After Mage attacks Warrior -> Warrior HP: {warrior.hp}, Mage Mana: {mage.mana}")