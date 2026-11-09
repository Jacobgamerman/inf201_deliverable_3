
# Task 2

from Dice_py import Dice

# Create standard 6-sided die and a custom 20-sided die
standard_dice = Dice()
d20 = Dice(sides=20)

# Demonstrate string representation
print("Standard dice representation:", standard_dice)
print("D20 dice representation:", d20)

# Roll using the roll() method
print("Rolling standard dice using roll():", standard_dice.roll())

# Roll using the __call__ method directly on the object
print("Rolling D20 directly using __call__():", d20())