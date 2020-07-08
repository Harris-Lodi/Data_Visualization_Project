from random import randint

# a class representing a single die
class Die:

    # assume a six-sided die
    def __init__(self, num_sides = 6):

        self.num_sides = num_sides

    # return a random value between 1 and the number of sides
    def roll(self):

        return randint(1, self.num_sides)