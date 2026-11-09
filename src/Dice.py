import random

class Dice:
    """
    Represents an n-sided die used for variable damage and combat mechanics.
    """

    def __init__(self, sides: int = 6) -> None:
        """
        Initializes a Dice instance with a specified number of sides.

        Parameters:
        ----------
        sides : int, optional
            The number of sides on the die (must be >= 2, default is 6).
        
        Raises:
        ------
        ValueError
            If the number of sides is less than 2.
        """
        if sides < 2:
            raise ValueError("A die must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """
        Rolls the die and returns a random integer between 1 and the number of sides.

        Returns:
        -------
        int
            The result of the dice roll.
        """
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """
        Returns the official string representation of the Dice object.
        """
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """
        Allows the Dice instance to be called directly like a function to roll it.
        Example:
            d20 = Dice(sides=20)
            result = d20()  # Equivalent to d20.roll()
        """
        return self.roll()

