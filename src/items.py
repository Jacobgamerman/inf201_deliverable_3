
class Weapon:
    def  __init__(self, name:str, damage_dice: "Dice") -> None:
        """
        Initialize the Weapon instance.

        Parameters
        ----------
        name : str
            The descriptive name of the weapon.
        damage_dice : Dice
            The Dice instance used to determine damage rolls.
        """
        self.name = name
        self.damage_dice = damage_dice
    def roll_damage(self) -> int:
        """
        Roll the associated damage dice to determine damage dealt.

        Returns
        -------
        int
            The rolled damage value from the weapon's dice.
        """
        return self.damage_dice.roll()

