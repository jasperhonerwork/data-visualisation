from random import randint

class Die:
    """A class representing a single die."""
    def __init__(self, num_sized=6):
        """Assume a six-sided die."""
        self.num_sides = num_sized

    def roll(self):
        """Return a random value between q and number of sides."""
        return randint(1, self.num_sides)